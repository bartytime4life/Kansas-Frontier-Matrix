# 🧰 MCP Runbooks

Welcome to `mcp/runbooks/` — the **operational brain** of the Kansas Matrix System.  
This folder holds **repeatable, step-by-step runbooks** for running pipelines, validating outputs, troubleshooting dev/prod workflows, and capturing “what we did + why it worked” in a way others can reproduce.

> **Why here?** The repo is intentionally built as a living, evidence-backed knowledge base where docs, methods, and outcomes are first-class citizens (not an afterthought). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 Quick navigation

- 📂 **MCP core**
  - `../runs/` → reproducible “run artifacts” (inputs, outputs, manifests, logs)
  - `../experiments/` → experiment reports & results
  - _(optional)_ `../model_cards/` → model cards & AI component documentation (if/when present) [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:3‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

- 🏛️ **Canonical docs**
  - `../../docs/` → governed documentation, standards, templates, architecture notes [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

- 🧱 **Data pipeline anchor**
  - `../../data/` → raw → processed → catalog/prov → database → API → UI (canonical order) [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧠 What counts as a “runbook”?

A **runbook** is a **procedural guide** that answers:

- ✅ **When** should we run this?
- ✅ **What** are the prerequisites + risks?
- ✅ **Exactly how** do we do it (commands + checkpoints)?
- ✅ **How do we verify** it worked?
- ✅ **How do we roll back** safely?
- ✅ **What artifacts** (logs/manifests/provenance) must be committed?

This aligns with the project’s documentation-first + reproducibility goals and the MCP emphasis on explicit methods and traceable outcomes. [oai_citation:7‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) [oai_citation:8‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🧱 Non‑negotiable rules

### 1) 🛤️ Follow the canonical pipeline order
All data + derived assets must flow through the canonical sequence:

`Raw → Processed → Catalog/Prov → Database → API → UI`

Any proposed shortcut is assumed flawed unless justified and reviewed. [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 2) 🧾 Git is the catalog of record
Runbooks must assume the repo is the system-of-record for code, data snapshots, and provenance. Tagging/releases + `CITATION.cff` usage supports reproducible references to specific repository states. [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 3) 🔍 Evidence-backed, transparent, collaborative
If a runbook changes behavior, it should state **why**, link evidence, and make verification unambiguous. This supports community oversight and “show your work” rigor. [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 4) 🧭 Ethics and stewardship are part of operations
Operational steps must respect project ethics (e.g., sensitive locations, community control expectations) and embed FAIR/CARE thinking where applicable. [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🗂️ Folder conventions

Suggested layout inside `mcp/runbooks/`:

```text
📁 mcp/
  📁 runbooks/
    📄 README.md                       👈 you are here
    📄 TEMPLATE__RUNBOOK.md            (recommended)
    📄 RB-010__local-dev-stack.md      (recommended)
    📄 RB-020__api-smoke-tests.md      (recommended)
    📄 RB-030__ingest-new-dataset.md   (recommended)
    📄 RB-040__generate-stac-dcat-prov.md
    📄 RB-050__model-eval-and-report.md
    📄 RB-060__release-tag-and-cite.md
```

> Note: The repo’s broader structure expects a dedicated `mcp/` area for methods/experiments and a governed `docs/` system for standards/templates. [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🏷️ Naming + lifecycle

### File naming
Use one of these patterns:

- `RB-###__short-slug.md` (simple, sortable)
- `RB-<area>-###__short-slug.md` (if you want categories)

Examples:
- `RB-010__local-dev-stack.md`
- `RB-data-030__ingest-new-dataset.md`

### Status tags
Put a status badge near the top of each runbook:

- 🟢 **Stable** — regularly used, verified recently
- 🟡 **Draft** — under development / needs validation
- 🔴 **Deprecated** — kept for history, do not use

---

## 🧪 Runbooks vs Experiments

Runbooks and experiments complement each other:

- 🧰 **Runbook** = “How to do a process reliably”
- 🧪 **Experiment report** = “What we tested + results + interpretation”

The project explicitly expects experiment reports with goals/data/method/results/interpretation to preserve a traceable research history. [oai_citation:14‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

When a runbook produces a novel outcome (new extraction method, new model, changed pipeline), **link to an experiment report** in `../experiments/` and store artifacts under `../runs/`.

---

## ✅ Runbook quality bar

Every runbook **must** include:

- 🎯 **Objective** (what success looks like)
- 🧩 **Scope** (what it does *not* cover)
- ⛓️ **Prerequisites** (tools, credentials, containers, datasets)
- ⚠️ **Risk & safety notes**
- 🧪 **Procedure** (commands + checkpoints)
- 🔎 **Verification** (how to confirm correctness)
- ⏪ **Rollback** (how to undo safely)
- 🧾 **Provenance** (what to commit, where, and naming rules)
- 📎 **References** (docs/specs/issues/PRs that justify steps)

This matches MCP’s emphasis on standardized protocols and complete, replicable methods documentation. [oai_citation:15‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) [oai_citation:16‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🧩 Runbook template

<details>
<summary><b>📄 Click to expand TEMPLATE__RUNBOOK.md (copy/paste)</b></summary>

```markdown
# 🧰 RB-XXX — <Runbook Title>

**Status:** 🟡 Draft / 🟢 Stable / 🔴 Deprecated  
**Owner(s):** @<name-or-team>  
**Last reviewed:** YYYY-MM-DD  
**Applies to:** <local / CI / prod / research>  
**Related:** ../runs/<run_id>/ • ../experiments/<exp_id>.md • ../../docs/<ref>.md

---

## 🎯 Objective
- What does “done” mean?

## 🧭 Scope
- In scope:
- Out of scope:

## ⛓️ Prerequisites
- [ ] Tooling installed (list versions if relevant)
- [ ] Env vars / secrets present
- [ ] Input dataset available at: `data/...`

## ⚠️ Safety / Ethics / Data Stewardship
- Sensitive data? Access tier? Redactions?
- Any special handling requirements?

## 📥 Inputs
- Paths:
- Parameters:

## 📤 Outputs
- Paths:
- Expected artifacts:
  - `mcp/runs/<run_id>/manifest.json`
  - `data/catalog/...`
  - `data/prov/...`

## 🧪 Procedure (step-by-step)
1) Step one
   - Command:
     ```bash
     <command>
     ```
   - Checkpoint (expected output):
     - ✅ …

2) Step two
   - …

## 🔎 Verification
- [ ] Validate schema
- [ ] Compare counts/checksums
- [ ] Spot-check map layers / samples

## ⏪ Rollback
- If step X fails:
  - How to revert data outputs
  - How to revert metadata/provenance
  - How to revert database changes (if any)

## 🧾 Provenance & Commit Rules
- What must be committed (and where):
  - `data/processed/...`
  - `data/catalog/...`
  - `data/prov/...`
  - `mcp/runs/<run_id>/...`
- Required commit message format:
  - `runbook(RB-XXX): <summary>`

## 📎 References
- Links to internal docs/specs/issues/PRs
```
</details>

---

## 🧪 Starter runbooks we should keep in this folder

Below are the first “high ROI” runbooks for this repo. Create these files as you implement them:

| Runbook | What it covers | Status |
|---|---|---|
| `RB-010__local-dev-stack.md` | Bring up containers, common port/resource fixes | 🔲 |
| `RB-020__api-smoke-tests.md` | Swagger/GraphQL quick checks + sanity queries | 🔲 |
| `RB-030__ingest-new-dataset.md` | Add a new source following Raw→Processed→Catalog/Prov→DB→API→UI | 🔲 |
| `RB-040__generate-stac-dcat-prov.md` | Regenerate catalogs + provenance bundles | 🔲 |
| `RB-050__model-eval-and-report.md` | Run eval + produce experiment report + save artifacts | 🔲 |
| `RB-060__release-tag-and-cite.md` | Tag release + ensure citation/versioning hygiene | 🔲 |

Why these? Because the project explicitly expects:  
- reproducible dev workflows (compose stack, troubleshooting) [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- API exploration and testing habits (Swagger UI / GraphQL checks) [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- strict pipeline ordering and repository-as-record discipline [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🛠️ Operational snippets we already know we’ll need

### 🐳 Local dev stack gotchas (compose)
Common issues to document in `RB-010__local-dev-stack.md`:

- container dependency timing → re-run `docker-compose up`
- port conflicts (e.g., `5432`, `7474`, `8000`, `3000`) → change mappings or stop local services
- Docker memory limits when loading big datasets
- volume permission issues on Windows/Mac
- rebuild after package changes → `docker-compose up --build` or `docker-compose build` [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🔌 API smoke checks
Document quick checks like:

- Swagger UI (local):
  - `http://localhost:8000/docs`
- Example REST checks:
  - `GET /datasets`
  - `GET /features/{id}`
- GraphQL (local):
  - `http://localhost:8000/graphql`
  - Example query:
    ```graphql
    query {
      storyNodes {
        id
        title
        yearRange
      }
    }
    ``` [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> Tip: keep URLs in code blocks/inline code so they remain copyable and clearly “operational constants”.

---

## 🧾 Sources & alignment notes

This folder exists to implement MCP’s “documentation-first, reproducible, modular” operating style and to keep day-to-day procedures aligned with the KFM architecture and canonical pipeline ordering. [oai_citation:25‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Key reference docs used:**
-  [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf
-  [oai_citation:28‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) MARKDOWN_GUIDE_v13.md.gdoc
-  [oai_citation:29‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) Scientific Method _ Research _ Master Coder Protocol Documentation.pdf
-  [oai_citation:30‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H) Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf