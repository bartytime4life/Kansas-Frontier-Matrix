# 🧩 KFM UI Component Samples  
> **Path:** `web/assets/samples/ui/components/README.md`

![scope](https://img.shields.io/badge/scope-UI%20samples-blue)
![kfm](https://img.shields.io/badge/KFM-provenance--first-success)
![status](https://img.shields.io/badge/status-draft-orange)
![docs](https://img.shields.io/badge/docs-contract--first%20%26%20evidence--first-informational)

This folder contains **small, isolated UI “mini-apps” / component demos** used to validate patterns for the Kansas Frontier Matrix (KFM) frontend **before** they are integrated into production UI code.

KFM’s UI is expected to be **auditable**: the platform is designed so that *every layer, dataset, and even AI outputs can be traced back to sources and processing*, with citations treated as first-class UI data.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🎯 Why this exists

KFM’s frontend is described as a modern web app (React-based SPA) that loads dynamic content from the governed API, with reusable UI elements (buttons, menus, charts, map overlays), map viewers (MapLibre + Cesium), and Story Node experiences.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

This `samples/` area is the **safe playground** where we:
- prototype interaction patterns quickly (map overlays, panels, citations, timeline UI),
- prove the UX works with **realistic data contracts**, and
- keep KFM’s **trust model** intact while iterating.

> [!IMPORTANT]
> **Contract-first + provenance-first is not optional in KFM.**  
> Anything that appears in the UI or Focus Mode must be traceable to cataloged sources and provable processing, using standards like **STAC / DCAT / PROV-O**.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🚦 Non‑negotiables (KFM invariants)

These rules apply to **samples too** (otherwise they become dangerous “lie demos”):

1) **Pipeline ordering is absolute**  
ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode.  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

2) **API boundary rule**  
The UI must not query the graph directly; all access goes through the governed API layer.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

3) **Provenance first**  
No “mystery layers.” Unsourced or ad-hoc data isn’t allowed into the official catalog, and UI experiences are expected to show provenance/citations when relevant.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

4) **Evidence-first narrative**  
No unsourced narrative content in Story Nodes / Focus Mode; any AI-generated text must be clearly identified and constrained by evidence.  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

5) **Focus Mode: provenance-linked only + AI is opt-in**  
Focus Mode must show only provenance-linked content; AI contributions must be user-triggered, clearly labeled, and include uncertainty/confidence.  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

6) **Sovereignty & sensitivity propagate**  
No output can be less restricted than its inputs; UI must honor sensitivity rules (including map safeguards).  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗺️ Where this fits in `web/`

KFM’s web app structure includes:
- `components/` (reusable UI components),
- `views/` (pages),
- `viewers/` (map viewers + MapLibre/Cesium integration),
- `story_nodes/` (story content + config),
- `assets/` (static assets),
- `styles/` (CSS/Sass).  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

This folder is inside **`web/assets/`**, which the docs describe as a home for static assets (icons/images/etc.).  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

> [!TIP]
> If a sample becomes “real,” graduate it to `web/components/` (or `web/viewers/` / `web/views/`) and keep this area for **portable demos** only.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧪 What belongs in this samples folder

✅ Good fits:
- **Component harnesses** (e.g., `ProvenanceBadge`, `LayerList`, `TimelineScrubber`, `CitationPopover`)
- **Interaction prototypes** (panel docking, map click → info panel, story stepper)
- **Accessibility experiments** (keyboard nav + focus order)
- **Data-contract mockups** (sample JSON shaped like the real API responses)

🚫 Not a good fit:
- production-only logic, large refactors, app-wide routing/state,
- hardcoded “cool” data with no provenance,
- anything that bypasses the API boundary (even in demos).  [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧰 Recommended folder layout

> This is a **suggested** structure to keep samples consistent and easy to review.

```text
📁 web/
  📁 assets/
    📁 samples/
      📁 ui/
        📁 components/
          📄 README.md   👈 you are here
          📁 _template/
          📁 provenance/
          📁 map/
          📁 story/
          📁 catalog/
          📁 charts/
```

---

## 🧩 Sample catalog (starter map)

These are **core UI elements KFM calls out** (layer list, search, legends, timeline slider, pop-ups/side panels).  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

| Area | Sample ideas | Why it matters |
|---|---|---|
| 🧾 Provenance | `ProvenanceBadge`, `CitationList`, `AttributionFooter`, `DataContractViewer` | “Citations & metadata are first-class” in KFM; users must be able to inspect sources.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) |
| 🗺️ Map UI | `LayerListPanel`, `Legend`, `MapPopup → SidePanel`, `FeatureInspector` | KFM includes map overlays + interactive map behaviors.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) |
| 🕰️ Time | `TimelineSlider`, `TemporalRangePicker` | Temporal navigation is a standard UI element for KFM.  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) |
| 🔎 Search | `GlobalSearchBar`, `DatasetSearchResultCard` | KFM expects search for locations/datasets by keywords.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) |
| 🎬 Story / Focus Mode | `StoryStepNavigator`, `AIHintCard (opt-in)`, `EvidencePanel` | Focus Mode rules require provenance-only content + transparent AI.  [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |

---

## ➕ Adding a new sample

1. Copy the template folder:
   - `web/assets/samples/ui/components/_template/` → `web/assets/samples/ui/components/<your-sample>/`

2. Include a **local** README with:
   - purpose + UX notes,
   - expected data inputs (contract fields),
   - provenance/citation behavior,
   - keyboard + screen-reader notes.

3. Provide a minimal “data contract” mock (JSON) with:
   - `source`, `license`,
   - spatial/temporal extent,
   - processing steps (or pointer to PROV).  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

4. Update **this** README’s “Sample catalog” if the sample is reusable.

---

## 🧾 Sample README mini‑template

<details>
<summary>📄 Copy/paste template for <code>components/&lt;sample&gt;/README.md</code></summary>

```markdown
# 🧪 <Sample Name>

## Purpose
- What pattern is being tested?
- What production component(s) will this influence?

## Data contract inputs
- Required fields:
  - source
  - license
  - spatial extent
  - temporal extent
  - processing steps / PROV link

## Provenance UX rules
- Where do citations appear?
- How does a user inspect the source?
- What happens if provenance is missing? (Should fail closed.)

## Accessibility checklist
- [ ] Keyboard operable
- [ ] Visible focus
- [ ] ARIA labels for icon-only controls
- [ ] Tested at 200% zoom

## Notes / screenshots
- (Optional) GIF or PNG
```
</details>

---

## ♿ Accessibility & responsiveness expectations

KFM’s frontend is intended to be **responsive and accessible**, working across desktop and mobile form factors.  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Minimum bar for samples:
- ✅ Works with keyboard only (tab/shift+tab/enter/esc)
- ✅ Visible focus states
- ✅ Doesn’t rely on color alone for meaning
- ✅ Supports narrow layouts (side panels collapse gracefully)

---

## 🔐 Trust & safety UI patterns (recommended)

Because KFM is **evidence-first** and sovereignty-aware, samples should model these patterns early:

- **“Fail closed” on provenance**  
  If a component can’t show where data came from, it should display a **blocked / missing provenance** state (not silently render).  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

- **AI output must be labeled + opt-in**  
  Any AI-assisted text should be clearly tagged as AI-generated and include uncertainty/confidence metadata.  [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

- **Sensitive location guards**  
  Avoid precise coordinates and apply blurring/generalization rules where applicable.  [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔗 Key docs used for this README

- **KFM Technical Documentation** (architecture + web UI structure + provenance-first requirements)  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **KFM Master Guide v13 (Markdown Guide)** (pipeline ordering + governance invariants + Focus Mode gates)  [oai_citation:27‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:28‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:29‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- **Open-source hub design doc** (repo structure context, including `web/`)  [oai_citation:30‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  [oai_citation:31‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  
