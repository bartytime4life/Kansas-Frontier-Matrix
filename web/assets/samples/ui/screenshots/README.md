# 📸 UI Screenshots (Samples)

Welcome to **`web/assets/samples/ui/screenshots/`** — a curated, lightweight gallery of **KFM UI screenshots** used for:
- 🧾 Docs & guides
- 🧪 UI samples / design reviews
- 🧭 Story Node + Focus Mode demos
- ✅ PRs (before/after) when a screenshot is the clearest proof

> **North Star:** screenshots should reflect KFM’s *trust-first UI* — i.e., whenever possible, capture the **source/provenance panel** alongside the visual output (layer, chart, note, etc.).

---

## 🗂️ Suggested folder layout

> Keep it simple. Add subfolders only when it’s clearly helping discoverability.

```text
web/assets/samples/ui/screenshots/
├── README.md
├── 🧭 flows/              # multi-step UX walkthroughs (numbered)
├── 🧩 components/         # focused UI component states
├── 🗺️ map/                # map & layer interactions
├── 🕰️ timeline/           # time slider / temporal navigation
├── 🎭 focus-mode/         # Focus Mode panels + evidence bundle states
└── 📱 responsive/         # tablet/mobile breakpoints
```

---

## 🏷️ File naming convention (please follow)

Use **predictable, sortable, grep-friendly** names:

```
<area>__<feature>__<state>__<viewport>__vNN.<ext>
```

✅ Examples:
- `map__layer-catalog__open__desktop-1440x900__v01.webp`
- `focus__evidence-panel__expanded__desktop-1440x900__v02.webp`
- `timeline__scrub__2020-to-2023__tablet-1024x768__v01.png`

Guidelines:
- Use **kebab-case** for words, **double-underscores** between segments.
- Always include a **viewport token** (even if it’s “default”).
- Increment `vNN` when updating a screenshot (don’t overwrite without a reason).

---

## 🧪 Capture rules (quality + consistency)

### ✅ Do
- 🟦 Prefer **light mode** unless the screenshot is explicitly about dark mode.
- 🧭 Include UI context: **breadcrumbs / panel headers / active layer names**.
- 🔎 When applicable, show the **dataset inspector / provenance drawer** in-frame.
- 🧼 Use clean demo data (or anonymized data) and remove personal info.
- 🧩 Keep the UI “still” — no half-animated states, no mid-transition frames.

### 🚫 Don’t
- ❌ Don’t include secrets, tokens, personal emails, or private locations.
- ❌ Don’t crop so hard that the feature loses context (unless it’s a component shot).
- ❌ Don’t add “random” screenshots; every image should earn its place.

---

## 🖼️ Format + size guidelines

**Preferred format:** `webp`  
**Allowed:** `png` (when transparency or crisp UI text suffers in webp)

Target constraints:
- **Desktop:** ~1440×900 (or 1366×768 if that’s your baseline)
- **Tablet:** ~1024×768
- **Mobile:** ~390×844 (or common device presets)
- Keep files **small** (aim: < 500KB when feasible)

<details>
<summary>🛠️ Optional: quick optimization tips</summary>

- WebP (good default):
  - `cwebp -q 82 input.png -o output.webp`
- PNG (when needed):
  - `pngquant --quality=70-90 --strip --skip-if-larger -o output.png input.png`

</details>

---

## 🧾 Optional (but awesome): a tiny manifest for traceability

If you’re adding many screenshots (or a flow), drop a `manifest.yml` next to them:

```yaml
# flows/irrigation-recommendation/manifest.yml
flow_id: irrigation-recommendation
screenshots:
  - id: step-01
    path: step-01__search__typed__desktop-1440x900__v01.webp
    route: /map
    notes: "Search for region; provenance drawer visible"
  - id: step-02
    path: step-02__layer__enabled__desktop-1440x900__v01.webp
    route: /map
    notes: "Layer enabled; legend and source panel shown"
```

Keep it minimal — the goal is “future you” can understand what the screenshot demonstrates.

---

## 🔗 How to reference screenshots in docs

Use relative links so GitHub renders them everywhere:

```md
![Layer catalog with provenance panel open](./map/map__layer-catalog__open__desktop-1440x900__v01.webp)
```

For flows, keep them numbered:

```md
![Step 1 — Search](./flows/irrigation-recommendation/step-01__search__typed__desktop-1440x900__v01.webp)
![Step 2 — Enable layer](./flows/irrigation-recommendation/step-02__layer__enabled__desktop-1440x900__v01.webp)
```

---

## ✅ PR checklist (screenshots)

- [ ] Filename matches convention
- [ ] No sensitive info visible
- [ ] Shows enough context to understand the UI state
- [ ] Provenance/source panel shown (when relevant)
- [ ] File size is reasonable
- [ ] If it’s a flow, steps are ordered + (optional) manifest included

---

## ✨ What “good” looks like

A great screenshot makes it obvious:
- **what** the UI is showing,
- **why** it matters,
- and **where it came from** (source/provenance) 🔍🧾🗺️
