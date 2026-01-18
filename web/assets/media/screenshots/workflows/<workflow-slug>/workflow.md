---
title: "<Workflow Title>"
slug: "<workflow-slug>"
area: "web-ui"
artifact_type: "workflow-screenshots"
status: "draft"
owner: "Docs / UX"
last_updated: "YYYY-MM-DD"
---

# 📸 Workflow Screenshots: `<Workflow Title>`

| 🏷️ Slug | 📁 Folder | ✅ Status | 🔍 Provenance | 🤖 AI | 🔐 Sensitive Locations |
|---|---|---|---|---|---|
| `<workflow-slug>` | `web/assets/media/screenshots/workflows/<workflow-slug>/` | `draft` | **required** | **opt-in** | **generalize / omit** |

> [!IMPORTANT]
> KFM is designed to be **provenance-first** (sources + processing steps are always traceable), and this must show up in what we capture in screenshots (especially for anything “Focus Mode” or story-driven). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧭 What this file is

This `workflow.md` is the **runbook + gallery index** for one UI workflow. It lives **next to** the screenshots that demonstrate the flow.

Screenshots are not just “pretty docs” in KFM—they’re part of the trust story:
- the UI is expected to surface **source + provenance** (no unsourced “mystery layers”) [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Focus Mode content is governed: provenance-linked only, AI is opt-in + labeled, and sensitive locations must not leak [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📁 Expected folder layout

```txt
📁 web/
  📁 assets/
    📁 media/
      📁 screenshots/
        📁 workflows/
          📁 <workflow-slug>/
            ├── workflow.md
            ├── 00-cover.png
            ├── 01-<short-step-name>.png
            ├── 02-<short-step-name>.png
            ├── 03-<short-step-name>.png
            └── ...
```

> [!TIP]
> Use **zero-padded numbering** to keep files self-sorting in GitHub + OS file explorers (and to preserve the order of the user journey). [oai_citation:5‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV)

---

## 🧱 KFM workflow guardrails (non‑negotiables)

### 1) Provenance-first UI evidence 📎
Anything that appears in the UI (layers, charts, story content, AI answers) should be traceable to **cataloged sources + processing**; KFM’s architecture treats provenance as fundamental, and rejects unsourced “mystery” content in official catalogs. [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 2) Focus Mode trust gate 🛡️
When screenshots include Focus Mode:
- show **provenance-linked** story/data only
- AI content must be **opt-in** and clearly labeled (and should show uncertainty/confidence when applicable)
- ensure **no sensitive location leaks** (blur, generalize, or omit) [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 3) AI is advisory + evidence-backed 🤖
Focus Mode AI is intended to be **advisory** and **evidence-backed**, providing sources for outputs (and relying heavily on the knowledge graph context). [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 4) CARE / sovereignty compliance 🌿
If the workflow involves highlighting locations or story-linked map features, verify screenshots reflect any required **redaction / coordinate hiding** for sensitive items (CARE-aligned). [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📸 Screenshot standards

**Keep it readable, reproducible, and accessible:**
- Always include **alt text** when embedding images
- Keep image sizes reasonable (repos bloat fast)
- Keep screenshots organized in a dedicated folder and name them clearly [oai_citation:13‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

Recommended defaults (adjust per workflow):
- **Viewport:** 1440×900 (or 1280×720 minimum)
- **Theme:** pick one (Light *or* Dark) and stay consistent per workflow
- **Cursor:** show only when it helps explain interaction
- **Redaction:** blur private info, tokens, emails, and sensitive coordinates

---

## 🧩 Workflow capture plan

### Step 0 — Cover / “what we’re about to do” 🧷
**Goal:** establish the feature + context in 1 image.

- ✅ Screenshot: `00-cover.png`
- Must include:
  - workflow entry point visible
  - any key toggle (e.g., Focus Mode entry point) if relevant [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Embed:
![Cover — <Workflow Title>](./00-cover.png "Workflow cover screenshot")

---

### Steps 1..N — One screenshot per meaningful state change 🪜
Each step should have:
- **Action** (what the user does)
- **Expected UI result**
- **Screenshot filename**
- **Any governance notes** (provenance, redaction, AI labeling)

> [!NOTE]
> If this workflow includes Story Mode: stories are authored as **Markdown + JSON config**, and each step can drive map camera, active layers, and time (so screenshots should show that synchronization). [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧠 Example workflow template: Focus Mode Q&A with citations

Use this as a ready-to-copy skeleton if your workflow is about Focus Mode.

### 01 — Open the Focus Mode panel
- **Action:** open the optional Focus Mode panel (AI assistant surface) [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- ✅ Screenshot: `01-open-focus-mode.png`

![Step 01 — Open Focus Mode panel](./01-open-focus-mode.png "Open Focus Mode panel")

---

### 02 — Ask a map/data question
- **Action:** ask a question about the current view/dataset
- **Expected:** the assistant response is grounded in KFM’s knowledge graph context [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- ✅ Screenshot: `02-ask-question.png`

![Step 02 — Ask a question](./02-ask-question.png "Ask a question in Focus Mode")

---

### 03 — Verify references / provenance surfaced
- **Expected:** response shows **references** (citations/links) and can trace back to provenance metadata [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- ✅ Screenshot: `03-answer-with-references.png`

![Step 03 — Answer with references](./03-answer-with-references.png "Answer includes references/citations")

---

### 04 — Confirm AI is opt-in + clearly labeled
- **Expected:** AI output is not silently injected; it is user-triggered and clearly marked as AI-generated (with uncertainty/confidence when applicable) [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- ✅ Screenshot: `04-ai-labeling.png`

![Step 04 — AI labeling](./04-ai-labeling.png "AI output is clearly labeled and opt-in")

---

### 05 — Sensitive location safety check
- **Expected:** no screenshot exposes restricted coordinates (blur/generalize/omit) [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- ✅ Screenshot: `05-sensitive-location-safety.png`

![Step 05 — Sensitive location safety](./05-sensitive-location-safety.png "Sensitive locations are generalized or omitted")

---

## 🗂️ Screenshot manifest (fill this in)

| # | File | UI state captured | Why it matters | Notes (provenance / redaction) |
|---:|---|---|---|---|
| 0 | `00-cover.png` | Entry point | Sets context | — |
| 1 | `01-...png` |  |  |  |
| 2 | `02-...png` |  |  |  |
| 3 | `03-...png` |  |  |  |
| 4 | `04-...png` |  |  |  |

---

## ✅ Validation checklist

### Visual / documentation quality
- [ ] All embedded images have meaningful **alt text** [oai_citation:22‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- [ ] Filenames are consistent + self-sorting (`00`, `01`, `02`, …) [oai_citation:23‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV)
- [ ] Steps are reproducible (someone else can follow)

### Governance & trust (KFM core)
- [ ] UI evidence is provenance-first (no unsourced/mystery assets) [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Focus Mode screenshots show provenance-linked content only [oai_citation:25‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] AI content is opt-in and clearly labeled [oai_citation:26‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Sensitive locations are not exposed [oai_citation:27‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧾 Definition of done (doc-level)

This workflow page is “done” when:
- [ ] Front matter is complete (template-consistent)
- [ ] Key claims are linked to artifacts / sources
- [ ] Validation steps are listed and repeatable
- [ ] Governance + sovereignty considerations are explicit [oai_citation:28‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗓️ Changelog

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial draft | @<handle> |
