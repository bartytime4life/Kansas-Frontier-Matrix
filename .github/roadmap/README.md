<div align="center">

# 🗺️ Kansas-Frontier-Matrix — Roadmap Sync (`.github/roadmap/`)

**Mission:** Maintain the **single source of truth** for the project roadmap.  
Everything here drives **GitHub labels, milestones, and issues**  
via automated sync to keep development reproducible and aligned.  

[![Roadmap Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/roadmap.yml/badge.svg)](../workflows/roadmap.yml)
[![Labels Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/labels.yml/badge.svg)](../workflows/labels.yml)
[![PR Labeler](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pr-labeler.yml/badge.svg)](../workflows/pr-labeler.yml)
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../workflows/automerge.yml)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../workflows/site.yml)
[![STAC Badges](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](../workflows/stac-badges.yml)
[![OpenSSF Scorecard](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ossf-scorecard.yml/badge.svg)](../workflows/ossf-scorecard.yml)

</div>

---

## 🔄 Workflow Lifecycle

```mermaid
flowchart TD
  A["Edit roadmap.yaml"] --> B["Workflow: roadmap.yml"]
  B --> C["sync-roadmap.js\n(DRY RUN on PRs)"]
  B --> D["sync-roadmap.js\n(APPLY on main/manual)"]
  D --> E["Labels\ncreate/update"]
  D --> F["Milestones\ncreate/update"]
  D --> G["Issues\ncreate/update by key marker"]
  G --> H["Provenance marker\nin issue body"]
````

<!-- END OF MERMAID -->

**Idempotent by design** → every synced issue carries a hidden marker:

```
<!-- roadmap:key=<your-stable-key> -->
```

This ensures reruns update instead of duplicating.

---

## 📂 Directory Layout

```
.github/roadmap/
├── README.md        # (this file)
├── roadmap.yaml     # declarative roadmap (edit me)
└── schema.json      # optional JSON Schema for CI validation
```

---

## 📝 Roadmap Components

* **`roadmap.yaml`** → human-edited source of truth
* **Workflow** → `.github/workflows/roadmap.yml`
* **Sync script** → `scripts/sync-roadmap.js`

---

## 🧩 Minimal Example (`roadmap.yaml`)

```yaml
version: 1

labels:
  - name: area:web
    color: 1f6feb
    description: Web viewer and UI
  - name: priority:p1
    color: d73a4a

milestones:
  - key: m25q4
    title: "2025 Q4"
    due_on: 2025-12-31
    state: open

epics:
  - key: epic-web-v1
    title: "Web Viewer v1"
    milestone: m25q4
    labels: [area:web, priority:p1, status:planned]
    body: |
      Goals:
      - Time slider
      - Schema validation
      - Pages deploy CI
    issues:
      - key: web-config-schema
        title: "Schema: app.config.json + layers.json"
        labels: [area:web, type:chore, status:doing]
        body: |
          Validate configs against JSON Schema in CI.
          <!-- roadmap:key=web-config-schema -->

issues:
  - key: stac-validate-ci
    title: "STAC validation workflow"
    milestone: m25q4
    labels: [area:data, type:chore, status:planned]
    body: |
      Validate catalog + items with pystac + JSON sanity checks.
      <!-- roadmap:key=stac-validate-ci -->
```

---

## 🗂️ Quick Reference

| Thing           | Where                                     | Who updates it | What it drives                            |
| --------------- | ----------------------------------------- | -------------- | ----------------------------------------- |
| Labels taxonomy | `roadmap.yaml → labels:`                  | Humans         | Repo labels (created/updated)             |
| Milestones      | `roadmap.yaml → milestones:`              | Humans         | Repo milestones (dates, state)            |
| Epics           | `roadmap.yaml → epics:`                   | Humans         | Issue bundles + hierarchy                 |
| Issues          | `roadmap.yaml → issues:` or under an epic | Humans         | Tracked tasks, linked to milestone/labels |
| Schema          | `schema.json` (optional)                  | Maintainers    | CI validation for structure/keys          |

---

## 🏷️ Taxonomy Guidelines

**Labels**

* `area:*` → domain (e.g., `area:web`, `area:data`, `area:ci`, `area:docs`)
* `type:*` → class (`feature`, `bug`, `chore`, `refactor`)
* `priority:p1..p3` → urgency
* `status:*` → `planned`, `doing`, `blocked`, `done`

**Milestones**

* Timeboxed (`YYYY Q#`) or release (`vX.Y`)
* Always use a **stable key** (e.g., `m25q4`)

**Keys**

* Treated as **immutable IDs**.
* Changing keys = a **new** issue will be created.

---

## 🚀 Running the Sync

**In CI (recommended)**

* **PRs** → **DRY RUN** (summary in logs, **no writes**)
* **Push to `main`** → apply changes
* **Manual dispatch** → choose `dry_run: true|false`

**Locally (advanced)**

```bash
export GITHUB_TOKEN=ghp_xxx   # token with repo scope
npm ci
DRY_RUN=true  node scripts/sync-roadmap.js    # simulate
DRY_RUN=false node scripts/sync-roadmap.js    # apply
```

---

## ✅ Validation

1. **YAML sanity**

```bash
yamllint .github/roadmap/roadmap.yaml
```

2. **Schema check (optional)**

```bash
python -m jsonschema -i .github/roadmap/roadmap.yaml .github/roadmap/schema.json
```

`schema.json` can enforce required keys (`version`, `labels[].name`, `milestones[].key`, …).

---

## 🔐 Guardrails & Security

* 🔒 **No writes on PRs** (fork safety)
* 🧩 **Workflow permissions** limited to labels, milestones, issues
* 🧾 **Provenance marker** → audit trail in issue body + run logs

---

## 🧯 Troubleshooting

* **Duplicate issues** → add the key marker to the old issue body, rerun sync
* **Label color error** → must be 6-digit hex **without** `#`
* **Assignee failed** → ensure user has repo access
* **Dry run confusion** → PRs always run **DRY RUN**

---

## 🗓️ CI Hooks (related)

* **Roadmap Sync** → `.github/workflows/roadmap.yml`
* **Labels Sync** → `.github/workflows/labels.yml`
* **PR Labeler** → `.github/workflows/pr-labeler.yml`
* **Automerge** → `.github/workflows/automerge.yml`

---

## 📜 Changelog

* **2025-09-30** → Rebuilt README with lifecycle diagram, schema guardrails, troubleshooting
* **2025-09-28** → Clarified local run instructions
* **2025-09-23** → Initial roadmap sync docs

---

## ✅ Summary

`.github/roadmap/` keeps the roadmap **reproducible and synced**.
Edit `roadmap.yaml`, run the workflow, and let automation manage **labels, milestones, and issues**.
Every change is **auditable, idempotent, and MCP-compliant**.
