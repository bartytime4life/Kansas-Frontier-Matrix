# 🧩 Story Node UI Screenshots

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Scope](https://img.shields.io/badge/scope-Story%20Nodes%20%2B%20Focus%20Mode-blue)
![Asset](https://img.shields.io/badge/asset-UI%20screenshots-lightgrey)
![Path](https://img.shields.io/badge/path-web%2Fassets%2Fmedia%2Fscreenshots%2Fui%2Fstory--nodes-informational)

> 📍 **Directory:** `web/assets/media/screenshots/ui/story-nodes/`

This folder holds **curated UI screenshots** for the **Story Nodes experience** (Narrative Mode) and closely related UI states (e.g., citations, entity links, Focus Mode context).  
Think: *“what the user sees”* ✅ — captured in a way that supports **documentation**, **QA/regression**, and **design review**.

---

## 🎬 What are “Story Nodes” (context)

In KFM, **Story Nodes** are *guided narrative experiences* that combine **maps + data + text + media**, presented as a step-based “interactive storybook” where each step can sync the map view (zoom/layers/time) with the narrative. 🗺️🧠  
They’re typically authored as **Markdown + JSON config** (narrative + step instructions), and the UI renders them as a narrative panel with navigation controls (next/prev or scroll-driven).  

Focus Mode (AI) is often adjacent to this experience and is expected to show **citations and click-through sources** when it generates summaries.

---

## ✅ What belongs in this folder (and what doesn’t)

| ✅ Put it here | 🚫 Don’t put it here | Why |
|---|---|---|
| UI screenshots of Story Node reader panel, step navigation, map-sync states, citation UI, entity link popovers | Story Node **content** (`.md`, `.json`) | Content should live in Story Node content directories (governed + versioned as narrative artifacts) |
| “How-to” screenshots for onboarding/help docs | Raw third‑party images intended *inside* a Story Node | In-story media should live in Story Node asset folders (licensed + credited) |
| QA “golden reference” screenshots (stable UI states) | Screenshots containing secrets, personal data, API keys, or sensitive coordinates | Governance + security + CARE/FAIR alignment 🚦 |

---

## 🗂️ Suggested mini-structure (recommended)

You can keep it flat, but this pattern scales well:

```text
📁 web/assets/media/screenshots/ui/story-nodes/
├─ 📄 README.md
├─ 📄 manifest.story-nodes.screenshots.json        # optional but recommended ✅
├─ 🖼️ 2026-01-17__story-mode__intro-panel__desktop.png
├─ 🖼️ 2026-01-17__story-mode__step-sync__desktop.png
├─ 🖼️ 2026-01-17__focus-mode__answer-with-citations__desktop.png
└─ 🧾 2026-01-17__focus-mode__answer-with-citations__desktop.meta.json  # optional sidecar
```

---

## 🧷 Screenshot “sets” (capture targets)

Use these as “must-have” states when documenting or verifying Story Node UX:

| Category | What it proves | Prefix idea |
|---|---|---|
| 📖 Story reader panel | Story UI layout + navigation affordances | `story-mode__reader-*` |
| 🧭 Step → map sync | Next/Prev step changes **layers / camera / time** | `story-mode__step-sync-*` |
| 🧾 Citations visible | Claims/AI output show provenance links | `citations__*` |
| 🔗 Entity link popover | Narrative references bind to graph entities (people/places/events/docs) | `entities__*` |
| 🤖 Focus Mode answer | AI output is clearly labeled + includes citations + click-through | `focus-mode__*` |
| 🧩 Responsive layout | Mobile/tablet behavior (panel collapse, map priority) | `responsive__*` |

---

## 🏷️ File naming convention (please follow)

**Goal:** stable, searchable, and diff-friendly names.

### Format

```text
YYYY-MM-DD__<area>__<state>__<device>.<png|webp>
```

### Examples

```text
2026-01-17__story-mode__reader-panel__desktop.png
2026-01-17__story-mode__step-03-map-sync__desktop.png
2026-01-17__focus-mode__answer-with-citations__desktop.png
2026-01-17__entities__person-popover__desktop.png
2026-01-17__responsive__story-panel-collapsed__mobile.png
```

**Rules**
- ✅ Use `kebab-case` inside segments.
- ✅ Prefer PNG for crisp UI text; use WebP only if you must reduce size.
- ✅ Keep filenames ASCII (no spaces, no emojis in filenames).

---

## 🧾 Optional metadata sidecar (`.meta.json`) ⭐

If a screenshot will be used as a **QA reference** or **long-lived documentation**, add a sidecar file with capture context:

**Example:**

```json
{
  "id": "focus-mode__answer-with-citations__desktop",
  "file": "2026-01-17__focus-mode__answer-with-citations__desktop.png",
  "purpose": "Shows Focus Mode response with citations and click-through UI affordances.",
  "story_node": {
    "story_id": "kfm.story.dust-bowl",
    "step": 2
  },
  "ui_state": {
    "map": {
      "camera": "stored-view-id-or-short-description",
      "layers": ["kfm.layer.precipitation", "kfm.layer.county-boundaries"],
      "timeline": "1935"
    }
  },
  "capture": {
    "date_utc": "2026-01-17T00:00:00Z",
    "viewport": "1440x900",
    "device": "desktop",
    "browser": "Chrome",
    "app_version": "v0.13.x",
    "commit": "abcdef1"
  },
  "governance": {
    "contains_sensitive_data": false,
    "redactions": []
  }
}
```

> 💡 This matches KFM’s “evidence-first” mindset: even screenshots can be treated as small, traceable artifacts when they matter.

---

## 📸 Capture checklist (Definition of Done)

Before committing a screenshot, confirm:

- [ ] The UI state is **intentional** (no random hover states unless that’s the point).
- [ ] **Citations are visible** when the screenshot relates to Story claims or Focus Mode output.
- [ ] Any AI panel content is **clearly labeled** as AI output (if present).
- [ ] Any sensitive information is removed/redacted:
  - [ ] No secrets/tokens
  - [ ] No personal identifying information
  - [ ] No precise coordinates for sensitive sites (use generalized views)
- [ ] File name follows the convention (`YYYY-MM-DD__...`).
- [ ] Image is readable at 100% (no blur, no compression artifacts).
- [ ] File size is reasonable (aim: **< 1 MB** unless there’s a strong reason).
- [ ] (Optional) `.meta.json` added for durable/QA-relevant screenshots.

---

## 🔐 Governance & safety notes

> ⚠️ **KFM is provenance-first.** Story Nodes and Focus Mode are trust-sensitive surfaces.  
> Screenshots should reinforce this trust: citations, source affordances, and careful labeling.

Additional guardrails:
- If you capture Story steps that contain third‑party media, ensure it is properly licensed/credited in the Story Node content (screenshots may show those assets).
- If a screenshot demonstrates data layers, it should ideally be captured with the **legend/source UI visible** somewhere in the workflow (or captured in a companion screenshot).

---

## 🔗 Using these screenshots in docs / UI

### In Markdown docs

```md
![Story Node reader panel](./2026-01-17__story-mode__reader-panel__desktop.png)
```

### In the web app (example pattern)

If your bundler supports static imports:

```ts
import storyReaderPanel from "@/assets/media/screenshots/ui/story-nodes/2026-01-17__story-mode__reader-panel__desktop.png";
```

*(Adjust import aliasing to match the project’s build config.)*

---

## 🧭 Related (project) references

If these exist in the repo, they’re the best “source of truth” for Story Node standards:

- 📘 `/docs/MASTER_GUIDE_v13.md` — governance + pipeline conventions
- 🧩 `/docs/templates/TEMPLATE__STORY_NODE_V3.md` — Story Node authoring structure
- 🎬 `/web/story_nodes/` — runtime Story Node bundles (Markdown/JSON) consumed by the UI

---

## 🧪 (Optional) Future upgrade: visual regression automation

If/when we add automated UI testing:
- Use a stable viewport (e.g., `1440×900`) and deterministic data fixtures.
- Generate screenshots into this folder (or a sibling `__generated__/` folder) and promote only curated ones into the main directory.

---

🧡 Keep it clean, consistent, and provenance-friendly.
