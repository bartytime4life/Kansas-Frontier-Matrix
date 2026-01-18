---
kfm:
  artifact: ui-workflow-screenshots
  id: "{{WORKFLOW_ID}}" # e.g., WF-012__focus-mode__verify-citations
  title: "🧭 {{WORKFLOW_TITLE}}"
  status: "template" # template | draft | review | published
  owners:
    - "{{OWNER_OR_TEAM}}"
  created: "{{YYYY-MM-DD}}"
  updated: "{{YYYY-MM-DD}}"
  version: "0.1.0"
  tags:
    - ui
    - workflow
    - screenshots
    - kfm
  sensitivity:
    level: "public" # public | internal | restricted
    notes: ""
  related:
    feature_or_epic: "{{FEATURE_OR_EPIC}}"
    issues:
      - "{{ISSUE_URL_OR_ID}}"
    pull_request: "{{PR_URL_OR_ID}}"
    contracts:
      openapi: "{{OPENAPI_PATH_OR_ENDPOINT}}" # e.g., src/server/contracts/openapi.yaml#/paths/~1layers/get
      graphql: "{{GRAPHQL_OPERATION}}" # optional
    evidence:
      dcat_dataset_ids: []   # e.g., ["kfm:dcat:air_quality:pm25_v1"]
      stac_collection_ids: [] # e.g., ["kfm:stac:collections:historical_maps"]
      prov_bundle_paths: []   # e.g., ["data/prov/air-quality/pm25_v1.prov.json"]
  capture:
    environment: "local" # local | dev | staging | prod
    app:
      url: "{{APP_URL}}"      # e.g., http://localhost:3000
      commit: "{{GIT_SHA}}"   # e.g., 7e65379
      build_tag: "{{BUILD_TAG_OR_VERSION}}" # e.g., web@0.42.0
    device:
      viewport_px: "1440x900"
      pixel_ratio: 2
      os: "{{OS}}"            # macOS | Windows | Linux
      browser: "{{BROWSER}}"  # Chrome | Firefox | Safari (+version)
      theme: "light"          # light | dark
      locale: "en-US"
    data_snapshot:
      id: "{{DATA_SNAPSHOT_ID}}" # e.g., releases/2026-01-18
      notes: ""
    redactions:
      applied: false
      notes: ""
---

<!--
🧩 HOW TO USE THIS TEMPLATE
1) Copy this folder 📁
   web/assets/media/screenshots/workflows/_template/
   ➜ web/assets/media/screenshots/workflows/{{WORKFLOW_ID}}/

2) Fill in front-matter + sections below.
3) Drop screenshots into the same folder as this workflow.md.
4) Keep filenames stable once referenced (treat as public API for docs).
-->

# 🧭 Workflow — {{WORKFLOW_TITLE}}

![Status](https://img.shields.io/badge/status-template-blue)
![Artifact](https://img.shields.io/badge/artifact-ui--workflow--screenshots-6f42c1)
![KFM](https://img.shields.io/badge/KFM-provenance--first-1f883d)

> ✅ **Goal:** Provide a reproducible, screenshot-backed walkthrough of a UI workflow that can be used for docs, QA, and onboarding.
>
> 🧷 **KFM rule-of-thumb:** If it appears in the UI, it should be traceable to cataloged sources (no “mystery layers”). Capture that traceability in screenshots when relevant.

---

## 📦 Directory layout

```text
📁 web/assets/media/screenshots/workflows/
  ├─ 📁 _template/
  │  └─ 📄 workflow.md
  └─ 📁 {{WORKFLOW_ID}}/
     ├─ 📄 workflow.md
     ├─ 🖼️ 01__{{slug}}__{{short_desc}}.png
     ├─ 🖼️ 02__{{slug}}__{{short_desc}}.png
     └─ 🖼️ ...
```

**Naming convention (recommended):**
- `NN__{{slug}}__{{short_desc}}.png`  
  - `NN` = 2-digit step number (01, 02, 03…)
  - `slug` = stable workflow slug (lowercase, dashes)
  - `short_desc` = 2–5 words, lowercase, dashes

---

## 🎯 Purpose

Explain and visually document **{{WORKFLOW_TITLE}}** with:
- a **step-by-step** recipe 🧪
- **expected results** ✅
- a **screenshot for each meaningful UI state** 🖼️
- a **traceability hook** (data/source/citation surfaces) 🧾

---

## 🧭 Scope

### ✅ In scope
- Primary “happy path” flow
- Key UI states (empty/loading/error/redaction notices) where meaningful
- Evidence surfaces (metadata panel, citations, layer info, dataset details, etc.) where applicable

### ❌ Out of scope
- Deep implementation details (belongs in design docs / code comments)
- Unverified interpretations of historical/scientific claims (belongs in Story Nodes with citations)

---

## 👥 Audience

- 🧑‍💻 Engineers (front-end/back-end) debugging or validating UI behavior
- 🧪 QA / testers verifying regression behavior
- 🧭 Product / domain stewards reviewing workflow outcomes
- 📚 Docs / onboarding readers

---

## ✅ Definition of done

- [ ] Front-matter is fully filled (no `{{...}}` placeholders remain)
- [ ] Every screenshot referenced exists on disk and renders correctly in GitHub
- [ ] Steps are reproducible using the listed environment + data snapshot
- [ ] Sensitive data is redacted or omitted (and noted)
- [ ] Any “trust surfaces” relevant to this workflow are captured (citations/metadata/redactions)
- [ ] File names are stable (renaming after publication requires updating all references)

---

## 🧪 Preconditions

- **User role:** {{ROLE}} (e.g., Guest | Researcher | Admin)
- **App URL:** {{APP_URL}}
- **Environment:** {{local|dev|staging|prod}}
- **Data snapshot:** {{DATA_SNAPSHOT_ID}}
- **Feature flags:** {{FLAGS_OR_NONE}}
- **Browser:** {{BROWSER}} on {{OS}}

### Data + evidence dependencies (fill these!)
- DCAT dataset IDs: `{{...}}`
- STAC collection/item IDs: `{{...}}`
- PROV bundles: `{{...}}`

---

## 🗺️ Workflow map

```mermaid
flowchart TD
  A([Start]) --> B[Open app]
  B --> C[Navigate to {{entry_point}}]
  C --> D[Perform {{primary_action}}]
  D --> E[Verify {{expected_outcome}}]
  E --> F([End])
```

> 💡 Keep this diagram high-level. The screenshot sequence below is the ground truth.

---

## 🧾 Step-by-step with screenshots

> Tip: Keep steps **atomic** (one user intent per step). If a step is “click 6 things,” split it.

| # | User action | Expected result | Screenshot file | Notes |
|---:|------------|-----------------|----------------|------|
| 01 | {{Action}} | {{Expected}} | `01__{{slug}}__{{desc}}.png` | |
| 02 | {{Action}} | {{Expected}} | `02__{{slug}}__{{desc}}.png` | |
| 03 | {{Action}} | {{Expected}} | `03__{{slug}}__{{desc}}.png` | |
| 04 | {{Action}} | {{Expected}} | `04__{{slug}}__{{desc}}.png` | |
| 05 | {{Action}} | {{Expected}} | `05__{{slug}}__{{desc}}.png` | |

---

## 🖼️ Screenshot manifest

Use this table as the “API surface” for your workflow screenshots.

| File | Alt text (required) | Why this screenshot matters | Redaction notes |
|------|----------------------|-----------------------------|-----------------|
| `01__{{slug}}__{{desc}}.png` | {{Alt text}} | {{Reason}} | {{None / what}} |
| `02__{{slug}}__{{desc}}.png` | {{Alt text}} | {{Reason}} | {{None / what}} |
| `03__{{slug}}__{{desc}}.png` | {{Alt text}} | {{Reason}} | {{None / what}} |

---

## 🧩 Screenshots

### 01 — {{Step title}}
![{{Alt text}}](./01__{{slug}}__{{desc}}.png)

**What to notice:**
- {{UI state details}}
- {{Trust surface / citation surface if applicable}}

---

### 02 — {{Step title}}
![{{Alt text}}](./02__{{slug}}__{{desc}}.png)

**What to notice:**
- {{UI state details}}
- {{Data lineage / metadata surfaced if applicable}}

---

### 03 — {{Step title}}
![{{Alt text}}](./03__{{slug}}__{{desc}}.png)

**What to notice:**
- {{UI state details}}
- {{Error/empty/redaction handling (if applicable)}}

---

## 🔎 Validation checklist

### Functional ✅
- [ ] The workflow completes without errors
- [ ] The visible UI state matches “Expected result” per step
- [ ] Loading states are reasonable (no infinite spinners)
- [ ] Errors (if triggered) are actionable and non-leaky

### Provenance & trust 🧾
- [ ] Any layer/dataset used can be traced to a catalog entry (DCAT/STAC)
- [ ] The UI provides a way to inspect source/metadata where expected
- [ ] If a redaction/generalization applies, a clear notice is shown
- [ ] If AI assistance is present, outputs are presented as advisory and evidence-backed (with references)

### Accessibility ♿
- [ ] Keyboard path works for core interactions (tab/focus visible)
- [ ] Contrast is acceptable for labels/controls shown in screenshots
- [ ] Screenshot alt text is descriptive (what + why), not just “screenshot”

---

## 🔒 Governance & safety notes

- **Sensitive locations / communities:** {{Yes/No}}  
  If yes, document what was generalized/redacted and why.
- **Personal data (names/emails/IDs):** {{Yes/No}}  
  If yes, ensure it is removed before committing screenshots.
- **License considerations:** If third-party imagery/data is visible, ensure attribution is discoverable and terms allow display.

---

## 🧰 Automation hooks (optional but recommended)

- **Playwright/Cypress test:** `{{path/to/test}}`
- **Test data seed script:** `{{path/to/seed}}`
- **CI job name / workflow:** `{{.github/workflows/...}}`

> 🧪 Ideal state: this workflow can be replayed automatically, and screenshots can be updated intentionally when UI changes.

---

## 🧭 Known issues / drift log

- {{YYYY-MM-DD}} — {{What changed?}} (UI/data/version)
- {{YYYY-MM-DD}} — {{What changed?}} (UI/data/version)

---

## 🧷 Related docs & references

- `docs/MASTER_GUIDE_v13.md` (canonical pipeline + invariants)
- `docs/templates/` (governed templates: universal doc / story node / API contract extensions)
- `docs/governance/` (ethics, sovereignty, review triggers)

---

## 🕰️ Changelog

| Version | Date | Notes | Author |
|--------:|------|-------|--------|
| 0.1.0 | {{YYYY-MM-DD}} | Initial workflow capture | {{name}} |
