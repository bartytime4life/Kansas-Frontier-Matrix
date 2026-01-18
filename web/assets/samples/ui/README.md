# UI Samples 🎛️🗺️

![Scope](https://img.shields.io/badge/scope-UI%20samples-blue)
![KFM](https://img.shields.io/badge/principle-provenance--first-6f42c1)
![UX](https://img.shields.io/badge/UX-responsive%20%26%20accessible-brightgreen)
![Status](https://img.shields.io/badge/status-WIP-yellow)

> **📍 You are here:** `web/assets/samples/ui/`  
> A small, practical “pattern library” for the Kansas Frontier Matrix (KFM) web UI — **map + timeline + narrative + evidence**.

---

## 🎯 Purpose

This folder exists to keep **UI examples, asset snippets, and interaction patterns** that demonstrate how KFM should *look* and *behave* — especially around the project’s defining requirement:

✅ **If it appears in the UI, a user must be able to trace it back to sources + processing.**  
No black boxes. No orphaned visuals. No “trust me” overlays.

Use these samples for:
- 🧩 component prototyping (panels, chips, modals)
- 🧭 UX walkthroughs (layer → inspect → cite → share)
- 🗓️ timeline UI behaviors (scrub/play/filter)
- 🧾 provenance presentation patterns (source/license/version/run)
- 🖼️ screenshots/mockups used in docs & PRs

---

## 📦 Recommended folder layout

> This is a **suggested** structure for what *belongs* under `web/assets/samples/ui/`.  
> Add folders as needed, but keep it tidy & discoverable.

```text
web/
└─ 📁 assets/
   └─ 🧪 samples/
      └─ 🎛️ ui/
         ├─ 📄 README.md            # 👈 you are here 📌 What UI samples cover, how to run/view them, and licensing notes
         ├─ 🧩 components/          # Isolated UI patterns (panels, chips, cards, drawers) for quick review/testing
         ├─ 🧭 flows/               # Step-by-step walkthroughs (annotated sequences) for common user journeys
         ├─ 🧷 icons/               # Sample icon sets (svg/png) + attribution (NOT canonical production icons)
         ├─ 📸 screenshots/         # Annotated images for docs/PRs (redacted, small, labeled)
         ├─ 🎛️ tokens/              # Sample design tokens (json/css) used by demos (not the canonical app tokens)
         └─ 🧪 fixtures/            # Sample API responses for mocks (deterministic, tiny, no sensitive data)
```

---

## ✅ KFM UI invariants (non‑negotiable)

### 1) 🧾 Provenance-first, evidence-first
UI patterns must **make provenance visible**:
- **Source** (institution / dataset name)
- **License** (what the user can do with it)
- **Version** (dataset + app)
- **Processing** (pipeline run / method / timestamp)
- **Citations** (clickable evidence references)

> Rule of thumb: if a user screenshots a view, the screenshot should *still* contain enough metadata to understand what’s being shown.

---

### 2) 🔌 API boundary (no direct graph access)
Samples must assume:
- UI consumes **governed API** responses
- UI does **not** query the knowledge graph directly

This keeps access control, redaction, and schema consistency centralized.

---

### 3) 🛡️ Sovereignty & sensitivity propagation
If a layer (or any of its inputs) is restricted:
- The UI must show the restriction clearly
- The UI must prevent “leaking” precise sensitive details (e.g., generalized geometry, blurred overlays)
- Prefer patterns like: **“Request access”** / **“Why is this restricted?”**

---

### 4) ♿📱 Responsive + accessible by default
Every sample should be designed to:
- work at narrow widths (mobile/tablet)
- support keyboard navigation & focus states
- avoid “hover-only” critical interactions
- include alt text for any images in docs samples

---

## 🧩 Standard UI patterns (samples to keep in this folder)

Below are the **core UI building blocks** that should have example implementations / mockups in `components/` or `flows/`.

---

### 🗂️ Pattern: Layer Catalog Panel
**Goal:** toggle datasets on/off, group layers, adjust opacity, and quickly open provenance.

**Must include:**
- Layer toggle ✅
- Opacity slider 🎚️
- Legend / symbology entry 🗺️
- “Inspect provenance” entry 🧾
- Temporal tag if layer is time-aware 🗓️

**Microcopy ideas:**
- “Show on map”
- “Opacity”
- “Legend”
- “About this layer”
- “Sources & license”

**Mini wireframe**
```text
┌───────────────────────────────┐
│ Layers 🗂️         Search 🔎   │
├───────────────────────────────┤
│ ☐ 1885 Railroads              │
│    Opacity: [──●────]  62%    │
│    Legend ▸   Provenance ▸     │
│    Time: 1880–1890             │
│                               │
│ ☑ Drought Index (NOAA)         │
│    Opacity: [────●──]  80%     │
│    Legend ▸   Provenance ▸     │
│    Time: 1895–2024             │
└───────────────────────────────┘
```

---

### 🗓️ Pattern: Timeline Slider + Playback
**Goal:** let users scrub through time and see layers respond (filter, interpolate, or switch).

**Must include:**
- Scrub slider (year/date)
- Play/pause for animation
- Step controls (← / →)
- “Layer supports time?” indicator per layer
- Optional “snap to events” markers ⭐

**Mini wireframe**
```text
⏪  ⏯  ⏩     1876 ─────────────── 2024
               ▲
            current
```

---

### 🧭 Pattern: Legend Block (Per Layer)
**Goal:** keep symbology understandable + consistent.

**Must include:**
- units (if applicable)
- color ramp meaning (min/max)
- “no data” representation
- link to layer metadata

---

### 🧾 Pattern: Provenance Drawer (Source + License + Processing)
**Goal:** the “map behind the map” — what this is, where it came from, how it was produced.

**Recommended sections:**
- **Dataset identity** (title, short description)
- **Source / Publisher** (institution)
- **License** (human readable + link)
- **Lineage** (inputs → process → outputs)
- **Confidence / uncertainty indicators** (when available)
- **Citations** (list of referenced sources)

**Mini wireframe**
```text
┌─────────────────────────────────────┐
│ Provenance 🧾  1885 Railroads        │
├─────────────────────────────────────┤
│ Source: Kansas Historical Society    │
│ License: CC BY 4.0                   │
│ Version: v1.2 • Updated: 2025-01-10  │
│                                     │
│ Lineage:                             │
│  • scan.tif → georef → tileset       │
│  • run_id: 2025-01-10T02:14Z         │
│                                     │
│ Citations:                           │
│  [1] KHS Map Archive Record …        │
│  [2] Georeference control points …   │
└─────────────────────────────────────┘
```

---

### 🖱️ Pattern: Feature Inspector (Map Click)
**Goal:** clicking a feature reveals details without losing context.

**Must include:**
- What is it? (feature label)
- Which layer is it from?
- Key attributes
- Link to provenance / source record
- If charts appear (stations/sensors): include caption citations

---

### 🧠 Pattern: Focus Mode Answer Card (Evidence-linked)
**Goal:** AI/QA results should read clearly **and** show evidence links.

**Must include:**
- Answer summary
- Evidence chips (each opens citation)
- Confidence / limitations label (if applicable)
- “Show on map” action (when spatial)

**Mini wireframe**
```text
Answer 🧠
Kansas saw major drought conditions in … (summary)

Evidence:
[NOAA index] [USGS water] [KHS newspaper]

Confidence: Medium • Notes: sparse coverage pre‑1900
Actions: 📍Show places  🧾View provenance  📤Share
```

---

### ✍️ Pattern: Story Builder Wizard (for contributors)
**Goal:** enable non-coders to create story content: text + media + map actions + citations.

**Wizard steps (recommended):**
1. Title + summary
2. Add sections
3. Add media (with attribution)
4. Add map steps (camera/layers/time)
5. Add citations per claim
6. Preview + validate

---

## 🎨 Asset conventions (keep samples consistent)

### ✅ File naming
Use **kebab-case** and keep names descriptive:
- `layer-panel--collapsed.png`
- `timeline-slider--playback.svg`
- `provenance-drawer--states.json`
- `focus-answer-card--anatomy.png`

### ✅ Preferred formats
- Icons: **SVG** preferred (clean `viewBox`, minimal paths)
- Screenshots: PNG (compressed), or WebP if supported
- Tokens/fixtures: JSON (stable keys, pretty-printed)

### ✅ Attribution + licensing
If you include any third-party icons/images:
- keep an `ATTRIBUTION.md` beside them (or per subfolder)
- include license name + source link + author (when known)

> 📌 KFM treats licensing and provenance as first-class — sample assets should model that discipline too.

---

## 🧪 Adding a new sample (fast checklist)

**1) Pick the right home**
- `components/` → one reusable UI element
- `flows/` → multi-step UX walkthrough
- `screenshots/` → annotated images for docs
- `fixtures/` → sample API payloads used by a mock

**2) Provide both**
- ✅ *a visual* (mock/screenshot) **and**
- ✅ *a short writeup* (what it demonstrates, what invariant it satisfies)

**3) Use the PR checklist**
- [ ] Names are kebab-case
- [ ] Includes provenance affordance (or explains why not)
- [ ] Includes attribution for any third-party assets
- [ ] Works at narrow width (or has a mobile variant)
- [ ] Keyboard / focus behavior documented (if interactive)

---

## 🧯 Common pitfalls (avoid these in samples)

- ❌ A “pretty” panel with no link to source/license
- ❌ Hover-only actions for core workflows
- ❌ Timeline control that doesn’t actually change any layer state
- ❌ Icons added without attribution/licensing info
- ❌ Mock text that implies certainty without evidence

---

## 🔗 Suggested “next samples” to create

- 🧾 Provenance drawer with STAC/DCAT/PROV “tabs”
- 🗓️ Timeline slider + “snap to story events”
- 🗂️ Layer panel with groupings + opacity + legend
- 🧠 Focus Mode answer card with evidence chips
- 🛡️ Restricted dataset UI (blur/generalize + explain why)

---

## 🪪 License

This folder may include assets with varying licenses.  
**Do not assume** everything here is automatically reusable without checking:
- the asset’s local `ATTRIBUTION.md`
- the project’s overall licensing policy (repo root)
