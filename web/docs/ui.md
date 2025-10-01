<div align="center">

# 🖥 Kansas-Frontier-Matrix — Web UI Behavior (`web/docs/UI.md`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.github/workflows/pre-commit.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy Security Scan](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

</div>

---

## 📖 Purpose

This document describes the **Web Viewer UI behavior**:  
how layers are listed, filtered, styled, and presented to the user — including **sidebar, timeline, popups, legend, and accessibility expectations**.

---

## 🧩 Sidebar

- Displays all **layers grouped by category** (see [CATEGORIES.md](CATEGORIES.md)).  
- Each layer row has:
  - **Toggle** → show/hide visibility  
  - **Opacity slider** → adjust alpha transparency  
- Category chips are color-coded from `config/categories.json`.  

---

## 🕑 Timeline

- Filters features by layer **time metadata**.  
- Layer-level: `time.start` / `time.end` → span of entire layer  
- Feature-level: `timeProperty` / `endTimeProperty` → per-feature timeline attributes  
- Behavior configurable via `timeUI` in `app.config.json` or overrides in `config/time_config.json`:  
  - `step` — year increment  
  - `loop` — whether to loop animation  
  - `fps` — frames per second during playback  

---

## 💬 Popups

- Configurable per layer with a `popup` array:

```json
"popup": ["name", "year", "notes"]

	•	Fields are displayed in a popup when the feature is clicked.
	•	Uses window.attachPopup in app.js if defined — to customize formatting or add richer interactivity.

⸻

🎨 Legend
	•	Reads symbolization keys from config/legend.json.
	•	Maps layer.legendKey → legend entry.
	•	Uses window.LegendControl if defined in app.js.
	•	Provides visual symbols, colors, and labels consistent across categories.

⸻

♿ Accessibility

UI follows WCAG & ARIA best practices:
	•	Keyboard focus:
	•	All toggles, sliders, and timeline controls are tab-navigable.
	•	:focus-visible styles applied in style.css.
	•	ARIA roles:
	•	Sidebar → role="navigation"
	•	Timeline → role="slider" with aria-valuemin, aria-valuemax, aria-valuenow
	•	Popups → role="dialog" or role="tooltip" depending on implementation
	•	Legend → role="list" with role="listitem" for symbols
	•	Reduced motion: timeline animation respects prefers-reduced-motion.
	•	Color contrast: category/legend colors meet contrast guidance.

⸻

🔄 UI Flow (Visual)

flowchart TD
  S["Sidebar\n(categories.json)"] --> L["Layer Toggle\n(show/hide)"]
  S --> O["Opacity Slider\n(alpha adjust)"]

  T["Timeline\n(timeConfig)"] --> F["Filter Layers\n(time/timeProperty)"]

  M["MapLibre Map"] --> P["Popup\n(layer.popup[])"]
  M --> G["Legend\n(legend.json + legendKey)"]

  L --> M
  O --> M
  F --> M
  G --> UI["User sees symbols/colors"]
  P --> UI


⸻

📊 UI Component Reference (Developer Cheat Sheet)

UI Component	Behavior / Controls	Config Keys & Files
Sidebar	List layers by category, toggle visibility, adjust opacity	category (layer) → config/categories.json; visible, opacity (layer/defaults)
Timeline	Filter layers/features by time span; animate slider	time (layer), timeProperty/endTimeProperty (feature), timeUI (app.config.json), config/time_config.json
Popups	Show feature info when clicked; customizable with attachPopup	popup array (layer), optional window.attachPopup in app.js
Legend	Show colors/symbols by category or legendKey	legendKey (layer), config/legend.json, optional window.LegendControl in app.js
Accessibility	ARIA roles, focus styles, reduced motion, contrast	style.css (tokens, :focus-visible), media queries for motion/contrast


⸻

🧭 UI Event Sequence (Visual)

sequenceDiagram
  autonumber
  participant U as User
  participant SB as Sidebar
  participant TL as Timeline
  participant MAP as MapLibre
  participant POP as Popup
  participant LEG as Legend

  U->>SB: Toggle layer / adjust opacity
  SB-->>MAP: setVisibility(layer), setOpacity(layer)

  U->>TL: Move year / play animation
  TL-->>MAP: filterByTime(year)

  U->>MAP: Click feature
  MAP-->>POP: buildPopup(fields)
  POP-->>U: Show popup

  MAP-->>LEG: refreshSymbols(legendKey)
  LEG-->>U: Display legend


⸻


<div align="center">


✅ The Kansas-Frontier-Matrix UI must be config-driven, accessible, and reproducible —
ensuring every dataset is explorable in time and space.

</div>
```
