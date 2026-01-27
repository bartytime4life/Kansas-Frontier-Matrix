<div align="center">

# 🧩 Issue Templates for Kansas Frontier Matrix (KFM)

**Pick the right form ➜ capture the right evidence ➜ ship clean, governed changes.** 🧭🗺️

</div>

---

## 🎯 What this folder is for

This directory contains **GitHub Issue Forms** (YAML templates) that standardize how we collect:

- 🐞 Bugs & CI failures  
- ✨ Feature requests  
- 🗃️ Data additions + data layers (raw ➜ processed ➜ catalog ➜ UI)  
- 🧵 Story nodes (narrative + citations + choreography)  
- 🕸️ Graph/ontology changes (Neo4j + relationships)  
- 🧠 Governance questions & approvals  
- 🤖 Agent/automation ops (Focus Mode / AI workflows)

> [!IMPORTANT]
> KFM is **provenance-first** and **governed-by-default**.  
> If a request can’t be traced (source, license, metadata, sensitivity), it will likely be blocked later in CI/review. Use the templates to get it right up front.

---

## 🗂️ What should exist in `.github/ISSUE_TEMPLATE/`

At minimum, keep:

- ✅ **`config.yml`** (template chooser + contact links)
- ✅ **Issue form templates** (`*.yml`)
- ✅ **`README.md`** (this file) to explain how to choose and fill templates

Recommended folder contents (matches current KFM setup):

```text
.github/ISSUE_TEMPLATE/
├─ README.md
├─ config.yml
├─ agent_ops_issue.yml
├─ api_contract_change.yml
├─ bug_report.yml
├─ ci_failure.yml
├─ data_addition_request.yml
├─ data_layer_request.yml
├─ feature_request.yml
├─ governance_form.yml
├─ governance_question.yml
├─ graph_model_change.yml
├─ question.yml
├─ story_node_request.yml
└─ ui_layer_issue.yml
```

---

## 🧭 Which template should I pick?

Use this quick chooser:

- 🐛 **Bug in code or UI** → `bug_report.yml`
- 🚨 **CI pipeline broke** → `ci_failure.yml`
- ✨ **New capability** → `feature_request.yml`
- 🗃️ **New source/dataset entering the system** → `data_addition_request.yml`
- 🧩 **New/updated map layer in UI (style + rendering + metadata)** → `data_layer_request.yml` or `ui_layer_issue.yml`
- 🧵 **New story node / narrative module** → `story_node_request.yml`
- 🕸️ **Graph model / ontology / relationships update** → `graph_model_change.yml`
- 🔌 **Breaking or evolving API contract** → `api_contract_change.yml`
- 🧠 **Policy, permissions, or sensitivity uncertainty** → `governance_form.yml` or `governance_question.yml`
- 🤖 **Agent / automation / Focus Mode workflow** → `agent_ops_issue.yml`
- ❓ **Not sure / general** → `question.yml`

> [!TIP]
> If you’re unsure whether something is **governance-sensitive**, start with **`governance_question.yml`** (fastest path to “allowed / denied / needs redaction”).

---

## 🧾 Template glossary (what each one is for)

### 🐛 `bug_report.yml`
Use for: regressions, incorrect behavior, crashes, incorrect outputs.  
Include: steps to reproduce, expected vs actual, logs/screenshots, environment (OS, browser, commit SHA if known).

### 🚨 `ci_failure.yml`
Use for: failing GitHub Actions, lint/test failures, broken release workflows.  
Include: workflow run link, error snippet, suspected commit/PR, how to reproduce locally (if possible).

### ✨ `feature_request.yml`
Use for: new functionality or major improvement.  
Include: user story, scope boundaries, success criteria, risks, alternatives, and any UI/API implications.

### 🗃️ `data_addition_request.yml`
Use for: introducing a new source dataset (raw data enters KFM).  
Include (required mindset): **source + license + provenance + intended outputs**.

You should be ready to provide:
- Source link (or archive reference)
- License / terms
- Sensitivity / CARE considerations (if any)
- Expected pipeline outputs (processed artifact + catalog metadata + provenance log)
- Spatial reference details (CRS/EPSG, datum, projection) when applicable

### 🧩 `data_layer_request.yml`
Use for: adding or updating a **renderable layer** (vector/raster/tiles), plus how it should look and behave in the UI.  
Include: symbology rules, zoom thresholds, styling notes, attribution text, and any filtering rules (time, category).

### 🖥️ `ui_layer_issue.yml`
Use for: UI presentation issues or enhancements related to layers (legend wrong, styling off, performance, interaction).  
Include: screenshots, expected behavior, and steps to reproduce.

### 🧵 `story_node_request.yml`
Use for: a new story node / narrative sequence.  
Include: narrative outline, citations plan, data layers needed, and choreography requirements (camera/layers/timeline).

### 🕸️ `graph_model_change.yml`
Use for: schema/ontology changes in Neo4j (new node types, relationships, properties, constraints).  
Include: example queries, migration notes, backward compatibility, and impact on API/UI.

### 🔌 `api_contract_change.yml`
Use for: changes that affect request/response models, OpenAPI schema, endpoints, or breaking changes.  
Include: current behavior, proposed behavior, versioning notes, migration guidance, example payloads.

### 🧠 `governance_form.yml`
Use for: requests needing an explicit governance decision (restricted data, redaction, permission boundaries).  
Include: who benefits, who might be harmed, sensitivity labels, proposed mitigations (aggregation, fuzzing, access tiering).

### 🧠❓ `governance_question.yml`
Use for: “Is this allowed?” or “How should we handle this?” policy questions.

### 🤖 `agent_ops_issue.yml`
Use for: Focus Mode / AI tooling changes, context bundles, retrieval rules, citations pipeline, sandboxing rules.

### ❓ `question.yml`
Use for: general questions, onboarding help, “where does this live?”, “what’s the right place for…?”

---

## 🧠 Filing standards (what “good” looks like)

### ✅ One issue = one scope
If you find yourself writing “also, while we’re here…”, split into separate issues and link them.

### 🧾 Evidence-first
Whenever possible, attach:
- logs, screenshots, minimal repro
- dataset IDs / filenames
- links to relevant docs
- a small sample (or checksum + location for larger artifacts)

### 🌍 Geospatial essentials (don’t skip)
When the issue touches data or rendering:
- **CRS / EPSG** (and any reprojection expectations)
- **Datum / projection** (if known)
- **Units** (meters vs degrees)
- **Spatial extent** (bounding box or counties/regions)
- **Time coverage** (start/end dates, granularity)

> [!CAUTION]
> If you don’t know the CRS/projection yet, say so explicitly and mark it as a blocker. “Unknown CRS” becomes tech debt fast.

### 🛡️ Sensitive locations & restricted data
If locations could be sensitive (cultural sites, endangered resources, private addresses, etc.):
- Prefer aggregation/redaction
- Use governance templates
- Don’t post exact coordinates publicly unless cleared

---

## 🛠️ Maintainers: adding/updating templates

1) Add a new `*.yml` Issue Form in this folder  
2) Update `config.yml` so it appears in the “New issue” chooser  
3) Keep names **snake_case** and stable (renames break links/bookmarks)  
4) Default labels should be meaningful (e.g., `needs-triage`, `data`, `governance`)  
5) Prefer **required fields** for provenance-sensitive workflows (data/story/governance)

---

## 🔒 Security issues

If you found a security vulnerability, **do not** open a public issue.  
Follow the repo’s security policy: **see `../SECURITY.md`**.

---

## 🔗 Useful links (in-repo)

- 🧭 Project overview: `../../README.md`
- 🤝 Contributing: `../../CONTRIBUTING.md`
- 🛡️ Security: `../SECURITY.md`
- 🧱 Architecture docs: `../../docs/architecture/` *(if present in your branch)*
- 🧾 Governance/policy docs: `../../policy/` *(if present in your branch)*

---

<div align="center">

**Thanks for helping keep KFM clean, traceable, and buildable.** 🧼🧾🗺️

</div>