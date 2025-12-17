---
title: "Accessibility Pattern — Story Node Content"
path: "docs/accessibility/patterns/story-node-content.md"
version: "v0.1.0"
last_updated: "2025-12-17"
status: "draft"
doc_kind: "Pattern"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:accessibility:patterns:story-node-content:v0.1.0"
semantic_document_id: "kfm-a11y-pattern-story-node-content-v0.1.0"
event_source_id: "ledger:kfm:doc:accessibility:patterns:story-node-content:v0.1.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Accessibility Pattern — Story Node Content

## 📘 Overview

### Purpose
Define how Story Node content should be rendered so it is:
- readable (headings, spacing, semantic structure),
- operable (keyboard focus management),
- understandable (citations, media alternatives),
- and consistent across panels/modals/Focus Mode.

### Scope
| In Scope | Out of Scope |
|---|---|
| Panel/modal semantics, headings/landmarks, focus handling, citations/media a11y | Story Node factual content governance (covered by Story Node template), backend provenance plumbing |

### Audience
- Primary: UI engineers rendering story nodes
- Secondary: content authors (so they understand how structure maps to UI)

## 🗂️ Directory Layout

~~~text
📁 docs/
└── ♿ accessibility/
    └── 📁 patterns/
        └── 🧩 story-node-content.md
~~~

## 🧭 Context

### Why this pattern exists
Story Nodes are narrative-heavy and often shown in a sidebar or modal. Without a standard:
- keyboard focus can get lost,
- screen readers get “flat text” with no structure,
- citations and evidence become inaccessible.

## ✅ Pattern requirements

## 1) Container semantics and landmarks
When the Story Node is displayed in a side panel or modal:

- The container has a clear role:
  - modal dialog: `role="dialog"` and `aria-modal="true"`
  - non-modal panel: use an `<aside>` region with an accessible name

- The container must be labeled:
  - `aria-labelledby` points to the visible title heading.

## 2) Focus management
### 2.1 Opening
- On open, move focus to:
  1) the panel title (`<h1>`/`<h2>`), or
  2) the first interactive control inside (if title is not focusable)

### 2.2 Closing
- Closing returns focus to the triggering element (the map marker, list item, or “open story” button).

### 2.3 Escape + close button
- Provide a visible Close button (`<button>Close</button>`)
- `Esc` closes modals (if modal)
- Close button has an accessible name that includes the story title when helpful (e.g., “Close Pawnee Rock story”)

## 3) Heading structure and reading order
- Use real headings (h2/h3) for sections like:
  - Summary
  - Evidence & citations
  - Related entities
  - Media
- Do not rely on bold text as the only structural cue.

## 4) Citations and evidence (interaction)
- Citations must be keyboard reachable and readable:
  - Link text should be descriptive (not “click here”).
  - If citations open new panes/modals, apply the same focus rules as above.
- If citations are expandable/collapsible:
  - Use button semantics + `aria-expanded`
  - Preserve focus and do not auto-scroll users unexpectedly

## 5) Related entities navigation
If the panel includes related places/events/people:
- Render as a list (`<ul>`/`<ol>`)
- Each item is a link/button with an accessible name
- Optionally group by entity type with headings (e.g., “Places”, “Events”)

## 6) Media accessibility
### 6.1 Images
- Every image includes:
  - `alt` text (brief, content-relevant)
  - a visible caption including provenance/source reference
- If an image is purely decorative: `alt=""` and ensure the same info is present elsewhere.

### 6.2 Charts/figures
- Provide a text summary near the figure (key takeaway + what varies over time/space).
- If figure is interactive (zoom/pan), keyboard controls must exist *(implementation not confirmed in repo)*.

### 6.3 Audio/video
- Provide transcript (audio) and captions (video).
- Controls must be keyboard accessible.

## 7) Announcements and updates
- If interacting with story content updates the map/time context:
  - Announce changes via a polite status region (e.g., “Timeline set to 1867”).
  - Do not force focus into the map.

## 8) Sensitivity messaging (CARE/sovereignty)
If content is generalized/redacted:
- Show a visible note near the affected content.
- Provide the same note to screen readers (not only iconography).
- Avoid language that implies the user can “find the exact site” if policy forbids it.

## 9) Example structure (illustrative)

~~~html
<aside aria-labelledby="story-title">
  <h2 id="story-title" tabindex="-1">Pawnee Rock</h2>

  <nav aria-label="Story sections">
    <ul>
      <li><a href="#summary">Summary</a></li>
      <li><a href="#evidence">Evidence &amp; citations</a></li>
      <li><a href="#related">Related entities</a></li>
    </ul>
  </nav>

  <section id="summary">
    <h3>Summary</h3>
    <p>...</p>
  </section>

  <section id="evidence">
    <h3>Evidence &amp; citations</h3>
    <ol>
      <li><a href="...">Kansas Historical Society record …</a></li>
    </ol>
  </section>

  <button type="button">Close</button>
</aside>
~~~

## 🧪 Validation & CI/CD
- [ ] Keyboard: open/close panel, navigate headings, open citations, return focus
- [ ] SR: reads title, headings, lists; citations announced properly
- [ ] 200% zoom: content reflows without hidden critical controls
- [ ] Reduced motion: no forced scroll/animation on section changes

## 🕰️ Version History
| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-17 | Initial story node content accessibility pattern | TBD |
