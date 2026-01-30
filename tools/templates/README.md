# 🧰 `tools/templates/` — KFM Tooling Templates Pack

<p align="center">
  <img alt="Kansas Frontier Matrix" src="https://img.shields.io/badge/KFM-provenance--first-1f6feb">
  <img alt="Contract First" src="https://img.shields.io/badge/contract--first-schemas%20%2B%20APIs-2ea44f">
  <img alt="Evidence First" src="https://img.shields.io/badge/evidence--first-catalog%20before%20narrative-8a2be2">
  <img alt="Fail Closed" src="https://img.shields.io/badge/governance-fail--closed-critical">
  <img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%20%2B%20CARE-by%20design-ffb000">
</p>

> **Purpose:** This directory contains **copy-ready templates** for building new **tools, scripts, configs, and mini-modules** that support the Kansas Frontier Matrix approach: **pipeline → catalog → provenance → API → UI → AI**.  
> **Goal:** Make it fast to ship something _and_ hard to ship something untraceable. ✅

---

## 🧭 Quick Navigation

- [What belongs here](#-what-belongs-here)
- [Folder map](#-folder-map)
- [Template picker](#-template-picker)
- [KFM guardrails](#-kfm-guardrails-non-negotiables)
- [How to use templates](#-how-to-use-templates)
- [Template conventions](#-template-conventions)
- [Add a new template](#-add-a-new-template)
- [FAQ](#-faq)

---

## 📦 What belongs here

✅ **Put in `tools/templates/`**
- “Starter kits” for **CLI tools** (Python/Node/Bash), helpers, validators, generators  
- Templates for **pipeline plugins** / ingestion stubs (when your tool touches data)  
- Templates for **metadata & provenance scaffolding** (STAC/DCAT/PROV helpers)  
- Templates for **policy-as-code** scaffolds (OPA/Rego placeholders)  
- Templates for **AI tool integration** (local LLM wiring, safe defaults, citations-first outputs)

🚫 **Do NOT put in `tools/templates/`**
- Narrative documentation templates → use `docs/templates/`
- GitHub issue/PR templates → use `.github/`
- One-off scripts with no reuse value → put them in the right subsystem folder (`pipelines/`, `api/`, etc.)

---

## 🗺️ Folder map

> This is the **intended** layout for this folder. Not all templates may exist yet — this README is the contract.

```text
📁 tools/
  📁 templates/
    📄 README.md                         👈 you are here
    📁 TEMPLATE__CLI_TOOL__PYTHON/        (skeleton CLI: logging, args, config, output)
    📁 TEMPLATE__PIPELINE_PLUGIN/         (ingest/transform/load + pipeline.yml)
    📄 TEMPLATE__ENV__EXAMPLE.env         (safe env wiring: local LLM, DB, API URLs)
    📄 TEMPLATE__OPA_POLICY__MODULE.rego  (policy-as-code starter)
    📄 TEMPLATE__DATASET__STAC_ITEM.json  (metadata contract starter)
    📄 TEMPLATE__DATASET__DCAT.json       (metadata contract starter)
    📄 TEMPLATE__PROVENANCE__PROV.json    (lineage record starter)
    📄 TEMPLATE__RUNBOOK.md               (ops & “what to do when it breaks”)
    📄 TEMPLATE__AI__SYSTEM_PROMPT.md     (Focus Mode system prompt starter)
    📄 TEMPLATE__AI__TOOL_SCHEMA.json     (tool/function schema starter)
    📄 TEMPLATE__MAP_STYLE.json           (cartography style scaffold)
```

---

## 🧩 Template picker

Pick the fastest path based on what you’re building:

<details>
<summary><strong>🧪 I’m adding a new ingestion / ETL integration</strong></summary>

Use:
- `TEMPLATE__PIPELINE_PLUGIN/`
- `TEMPLATE__DATASET__STAC_ITEM.json`
- `TEMPLATE__PROVENANCE__PROV.json`

Why:
- In KFM, **processed outputs require catalog + provenance updates** (not optional).
</details>

<details>
<summary><strong>🧰 I’m adding a CLI helper (validator, generator, exporter)</strong></summary>

Use:
- `TEMPLATE__CLI_TOOL__PYTHON/` (or your preferred language equivalent)
- `TEMPLATE__RUNBOOK.md` (if it’s operationally important)

Why:
- Tools should be repeatable, log clearly, and fail safely.
</details>

<details>
<summary><strong>🔐 I’m adding governance checks (metadata/license/sensitivity/AI constraints)</strong></summary>

Use:
- `TEMPLATE__OPA_POLICY__MODULE.rego`

Why:
- KFM governance is **policy-as-code** and should be reviewable, versioned, and enforceable.
</details>

<details>
<summary><strong>🤖 I’m wiring Focus Mode / AI features (local or hosted)</strong></summary>

Use:
- `TEMPLATE__ENV__EXAMPLE.env`
- `TEMPLATE__AI__SYSTEM_PROMPT.md`
- `TEMPLATE__AI__TOOL_SCHEMA.json`

Why:
- Keep secrets out of git, and keep AI outputs **citation-first** with guardrails.
</details>

---

## 🧱 KFM guardrails (non-negotiables)

These aren’t “style preferences” — they’re **system invariants**.

### 1) ✅ Provenance-first (“map behind the map”)
If your tool creates or modifies an artifact that will be visible in the platform, you must be able to answer:
- **Where did this come from?**
- **What transformations happened?**
- **Who/what ran it and when?**
- **How do I reproduce it?**

### 2) 📜 Contract-first
- Define/extend **schemas and contracts** before (or alongside) code changes.
- If a tool emits JSON, it should align to a known schema (or ship the schema with it).

### 3) 🧾 Evidence-first (catalog before narrative)
- Datasets should be described in **metadata** (catalog records) before they’re used in stories or AI answers.

### 4) 🛑 Fail-closed governance
When checks can’t be satisfied (missing license, missing metadata, unknown sensitivity), tools should:
- **stop**
- **exit non-zero**
- **tell the operator what to fix**
- **not “best-effort” publish**

### 5) 🤝 FAIR + CARE by design
- FAIR: Findable, Accessible, Interoperable, Reusable
- CARE: Collective Benefit, Authority to Control, Responsibility, Ethics  
Your tool should preserve these principles, especially around **sensitive data**.

---

## 🚀 How to use templates

### Step 1 — Copy, don’t edit in place
```bash
# Example: new CLI tool
cp -R tools/templates/TEMPLATE__CLI_TOOL__PYTHON tools/my_new_tool

# Example: new pipeline plugin
cp -R tools/templates/TEMPLATE__PIPELINE_PLUGIN pipelines/plugins/my_new_source
```

### Step 2 — Rename placeholders
Search/replace common tokens (template-dependent):
- `TEMPLATE__...`
- `{{PROJECT_SLUG}}`
- `{{DATASET_ID}}`
- `{{OWNER}}`
- `{{LICENSE}}`
- `{{SENSITIVITY}}`

### Step 3 — Wire outputs into the canonical flow
If your work touches data:

```mermaid
flowchart LR
  A[📦 data/raw] --> B[🧹 pipelines/*]
  B --> C[✅ data/processed]
  C --> D[🗂️ data/catalog (STAC/DCAT)]
  C --> E[🧾 data/provenance (W3C PROV)]
  D --> F[🔌 api (FastAPI)]
  E --> F
  F --> G[🖥️ web (React)]
  F --> H[🤖 Focus Mode (AI)]
  H -->|citations| G
```

### Step 4 — Validate like CI will
Before a PR, run the repo’s local equivalents of:
- formatting/linting
- unit tests (if applicable)
- metadata validation (schema checks)
- policy checks (fail closed)

> If you don’t know the command, check the repo root `Makefile`, `package.json`, or CI workflows in `.github/workflows/`.

---

## 🧷 Template conventions

### ✅ Naming
Use consistent names so templates sort cleanly and are easy to grep:

- `TEMPLATE__<AREA>__<THING>__v<MAJOR>`
  - Example: `TEMPLATE__PIPELINE_PLUGIN__v1`

### ✅ Minimal “works out of the box”
Every template should include:
- a short header comment explaining when to use it
- clear placeholders + examples
- sane defaults
- an example command in a `USAGE` section

### ✅ Include a “Definition of Done” checklist
Templates should help contributors self-review:

```markdown
**Definition of Done**
- [ ] All placeholders replaced
- [ ] Output paths follow canonical layout
- [ ] Metadata present (license, source, dates, spatial/temporal extent)
- [ ] Provenance record created/updated
- [ ] No secrets committed (keys/tokens)
- [ ] Local checks pass (lint/tests/validation)
```

---

## 🧠 AI templates notes (local-first friendly)

KFM supports both hosted and local AI paths. For local testing, templates should assume:
- `.env` contains **model selection** (example: `OLLAMA_MODEL=...`)
- local LLM runs via an **AI backend URL** (example: `http://localhost:11434` pattern)
- system prompts and tool schemas are versioned and reviewable

✅ AI template outputs must:
- cite sources (or emit “insufficient evidence”)
- respect sensitivity tiers
- avoid leaking restricted data
- log “redaction applied” style events if applicable

---

## 🧾 Add a new template

When adding templates to this folder:

1) Add the template file/folder  
2) Add it to the [Folder map](#-folder-map) and [Template picker](#-template-picker)  
3) Include a **tiny example** (`example/` folder or a short `USAGE` section)  
4) Avoid copying proprietary text/code into templates  
5) Prefer templates that **force metadata + provenance**, not ones that encourage shortcuts  

---

## ❓ FAQ

### “Why so much structure for a simple template folder?”
Because KFM is not a “black-box GIS” — it’s a **trustworthy pipeline**. Templates are where we encode the habits:
- traceability
- schema discipline
- governance
- reproducibility

### “Where do story templates live?”
In `docs/templates/` (not here). This folder is for **tools** and operational scaffolds.

### “What if I’m prototyping?”
Prototype fast — but when it becomes shared, it needs:
- repeatability
- safe defaults
- provenance hooks
- validation gates

---

## 🔗 Related internal docs (typical paths)

> These are common companion docs in the KFM repo layout.

- `docs/templates/` — narrative/doc templates (universal doc, story nodes, API extensions)
- `docs/architecture/` — system overview & redesign blueprints
- `docs/governance/` — ethics, sovereignty, governance rules
- `policy/` — OPA/Rego policies (data + AI + security + compliance)

---

<p align="center">
  <sub>🧭 If you’re unsure which template to use: choose the one that forces you to record <strong>license + source + provenance</strong> first.</sub>
</p>