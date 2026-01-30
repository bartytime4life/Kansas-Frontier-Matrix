# ⚖️ MCP Governance — Master Coder Protocol (KFM)

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-blue)
![Governance](https://img.shields.io/badge/Governance-Policy--as--Code-5c6bc0)
![Pipeline](https://img.shields.io/badge/Pipeline-Evidence--First-success)
![Default](https://img.shields.io/badge/Default-Fail%20Closed-critical)
![Status](https://img.shields.io/badge/Status-Draft-orange)

> **Mission 🧭:** Keep KFM’s computational work **reproducible**, **reviewable**, and **policy-compliant** — so anything that reaches the graph, APIs, UI, or **Focus Mode** is backed by traceable evidence (and can be audited later).[^kfm_blueprint_intro]

---

## 🧩 What “MCP” means here

In this repo, **MCP = Master Coder Protocol**: a disciplined way to document and govern **methods, experiments, runs, and model artifacts** so results can be replicated and trusted.[^mcp_design_doc][^mcp_scientific_method]

MCP exists to prevent “cool results” from becoming **unverifiable folklore**. If it isn’t repeatable, it isn’t real (at least not in this repo). ✅

---

## 🗺️ Where MCP fits in KFM’s “non‑negotiable” pipeline

KFM is explicitly designed as a **pipeline → catalogs → graph → APIs → UI → stories → Focus Mode** system, where *no stage may leapfrog the prior stage’s contracts/outputs*.[^kfm_master_guide_pipeline]

```mermaid
flowchart LR
  A[ETL / Pipelines] --> B[STAC / DCAT / PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[Governed APIs]
  D --> E[UI (Map + Narrative)]
  E --> F[Story Nodes]
  F --> G[Focus Mode (AI)]

  subgraph MCP["🧩 MCP (Methods & Experiments)"]
    R[Runs] --> EA[Evidence Artifacts]
    X[Experiments] --> EA
    EA --> B
  end
```

> [!IMPORTANT]
> **MCP outputs do not go directly into the UI.** They become *evidence artifacts* that must be cataloged + provenanced, then exposed via the governed API boundary.[^kfm_master_guide_artifacts][^kfm_master_guide_invariants]

---

## 🗂️ Folder scope

This README governs everything under:

```text
📁 mcp/
  ├─ 📁 governance/          👈 you are here
  │   └─ 📄 README.md
  ├─ 📁 runs/                (execution records, logs, outputs)
  ├─ 📁 experiments/         (experiment reports + comparisons)
  └─ 📁 model_cards/         (model cards + evaluation notes; if present)
```

The repo’s documented layout calls out **mcp/runs** and **mcp/experiments** as the home for “Methods & Computational Experiments”.[^mcp_dir_layout]  
The broader design also references **model cards** as first-class artifacts in MCP workflows.[^mcp_design_doc]

---

## ✅ Governance principles (MCP inherits KFM’s invariants)

### 1) 📜 Contract‑first & deterministic
- **Contracts are first‑class** (schemas + API contracts are governed artifacts).[^kfm_contract_first]
- Transformations should be **deterministic, idempotent, fully logged** when feasible.[^kfm_contract_first]

### 2) 🧾 Evidence‑first (no unsourced “magic”)
- “Evidence artifacts” (AI outputs, analyses, derived layers) must be treated like datasets:
  - stored like processed data,
  - cataloged (STAC/DCAT),
  - and traced (PROV).[^kfm_master_guide_artifacts]

### 3) 🧱 API boundary rule
- The UI must never bypass governance by querying raw stores directly; all access goes through governed APIs.[^kfm_master_guide_invariants][^kfm_blueprint_intro]

### 4) 🔒 Fail‑closed by default
If a governance check is missing or fails, we **block** the merge/release instead of “letting it slide”.[^kfm_blueprint_fail_closed]

---

## 👥 Roles & decision rights

> [!NOTE]
> Titles are pragmatic. One human can wear multiple hats — but the **responsibilities** remain.

### Core roles 🧑‍🤝‍🧑
- **Maintainers** 🛠️: final merge authority; own release and production-risk decisions.
- **Domain Stewards** 🗺️: validate domain truth (e.g., hydrology, treaties, soils).
- **Policy Owners** 🧩: own governance-as-code rules (OPA/Rego) and enforcement gates.[^kfm_blueprint_policy_as_code]
- **Reviewers** 🔎: technical review + reproducibility review.
- **FAIR+CARE Council** ⚖️: human accountability layer for sensitive material & community rights.[^kfm_blueprint_care]
- **Contributors** 🌱: propose + implement experiments, runs, and artifacts.

### Decision matrix (RACI-lite) 🧭

| Decision / Change Type | Contributors | Reviewers | Domain Steward | Policy Owner | Maintainers | FAIR+CARE Council |
|---|---:|---:|---:|---:|---:|---:|
| Add new experiment report | ✅ | ✅ | ➖ | ➖ | ✅ | ➖ |
| Add new evidence artifact (derived layer/report) | ✅ | ✅ | ✅ | ✅ | ✅ | ➖ |
| Promote an experiment into a pipeline / API feature | ✅ | ✅ | ✅ | ✅ | ✅ | ➖ |
| Change policy rules (OPA/Rego) | ➖ | ✅ | ➖ | ✅ | ✅ | ✅ (if sensitive) |
| Add/modify sensitive or community-controlled data | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Takedown / withdraw dataset or artifact | ➖ | ➖ | ✅ | ✅ | ✅ | ✅ |

---

## 🚦 Review gates for MCP work

**Review gates scale with impact.** If you’re unsure, assume the higher gate. 🔺

### Gate 0 — Docs-only (low risk) 📝
- No code execution changes, no new data artifacts.
- Requires: **1 reviewer**

### Gate 1 — New experiment/run (reproducibility risk) 🧪
- Adds experiment report, notebook, or run log.
- Requires:
  - **repro steps**
  - **inputs + outputs referenced**
  - **1 technical reviewer** + **1 reproducibility reviewer** (can be same person if small)

### Gate 2 — New evidence artifact (catalog + provenance risk) 🧾
- Adds derived dataset/layer/model output intended to be used downstream.
- Requires:
  - STAC/DCAT/PROV alignment ✅[^kfm_master_guide_artifacts]
  - Domain Steward approval ✅
  - Policy checks pass ✅[^kfm_blueprint_policy_checks]

### Gate 3 — Policy / Access / Focus Mode impact (high risk) 🔒🤖
- Any change affecting:
  - access control rules,
  - policy enforcement,
  - Focus Mode constraints,
  - or what the UI can display.
- Requires:
  - Maintainer approval ✅
  - Policy Owner approval ✅
  - FAIR+CARE Council review when sensitive/community-controlled ✅[^kfm_blueprint_care]

---

## 🧪 MCP experiment protocol (required shape)

MCP follows scientific-method discipline: question → hypothesis → method → data → analysis → results → conclusion → next steps.[^mcp_scientific_method]

### Minimum required “experiment logbook entry” fields 🧾
Each experiment should have at least:
- **Date**
- **Experiment ID**
- **Author**
- **Purpose**
- **Method summary**
- **References to protocol/code**
- **Results summary**
- **Conclusion / next steps**[^mcp_logbook]

### Reproducible coding expectations 🧰
When applicable:
- set **random seeds** for determinism,
- add **logging** (params, runtime, versions),
- handle errors with actionable messages,
- avoid notebook “hidden state” (run-all-cells discipline),
- document where logs live and how to interpret them.[^mcp_repro]

---

## 🧾 MCP artifact requirements

### 📌 MCP artifacts must be linkable downstream
MCP artifacts are only “real” if they can be referenced as evidence (and traced).

#### Evidence artifact pattern (required) 🧬
If an MCP output is to be used as evidence (map layer, report, extraction output):
- store in processed-like structure,
- **catalog** in STAC/DCAT,
- **trace** in PROV (inputs, parameters, agent, timestamps),
- integrate into graph cautiously,
- expose only through governed APIs (no direct UI injection).[^kfm_master_guide_artifacts]

> [!IMPORTANT]
> The repo is designed so **every narrative claim can be traced to versioned evidence**, and derived products have explicit lineage.[^kfm_master_guide_pipeline]

### Suggested front‑matter (proposed) 🏷️
Use this pattern in MCP Markdown artifacts (experiment reports, model cards):

```yaml
---
mcp:
  type: experiment | run | model_card
  id: EXP-<DOMAIN>-<NNN>
  status: draft | accepted | deprecated
  created: YYYY-MM-DD
  owners: ["@github_handle"]
  links:
    inputs:
      - dcat: data/catalog/dcat/<dataset>.json
      - stac: data/catalog/stac/<collection-or-item>.json
    prov:
      - data/prov/<activity>.prov.json
    outputs:
      - artifact: data/processed/<domain>/<artifact>
  risk:
    data_class: open | restricted | sensitive
    notes: "Why / mitigations"
---
```

*(If/when a JSON Schema exists for this front matter, CI should validate it.)*

---

## 🔐 Sovereignty, sensitivity, and takedowns

KFM’s governance explicitly includes **CARE** principles — including **Authority to Control** and honoring **takedown/withdrawal** requests.[^kfm_blueprint_care]

Practical expectations:
- Tag restricted material with metadata like:
  - `accessLevel: "Restricted"`
  - `ownerGroup: "<GroupName>"`
- Policy enforcement should ensure only authorized roles/groups can access it, and withdrawn items become non-queryable.[^kfm_blueprint_care]

> [!CAUTION]
> If you suspect an artifact reveals sensitive locations (e.g., archeological sites) or living-person PII, treat it as **Gate 3** immediately.

---

## 🧩 Governance‑as‑Code (how rules are enforced)

KFM describes a `policy/` directory where governance is encoded like code (versioned, testable, enforceable).[^kfm_blueprint_policy_as_code]

### Policy-as-code (OPA / Rego) 📜
Example rule families include:
- dataset rules (licenses, sensitivity),
- AI behavior rules (citations, privacy constraints),
- security/access rules,
- compliance rules.[^kfm_blueprint_policy_as_code]

### CI policy checks (Conftest) ✅
CI runs policy checks (e.g., “dataset missing license”, missing PROV, forbidden AI prompt phrase).  
Contributors should run these locally:

```bash
conftest test .
```

…and/or target a specific path for faster iteration.[^kfm_blueprint_policy_checks]

### Runtime enforcement + audit logs 🧾
Runtime requests can be checked against OPA decisions (deny/sanitize) and logged with the **policy bundle/version** that made the decision for later accountability.[^kfm_blueprint_runtime_audit]

---

## 🧑‍💻 Contribution flow (MCP-compliant)

### 1) Propose 📣
- Open an issue/RFC describing:
  - goal + hypothesis,
  - inputs you’ll use,
  - expected outputs,
  - risk notes (sensitivity/licensing).

### 2) Implement 🛠️
- Add experiment/run artifacts under:
  - `mcp/experiments/…`
  - `mcp/runs/…`
- Ensure outputs intended for evidence follow the evidence artifact pattern.[^kfm_master_guide_artifacts]

### 3) Validate ✅
Run:
- unit/integration tests (as applicable),
- lint/format (as applicable),
- **policy checks** (`conftest test .`).[^kfm_blueprint_policy_checks]

### 4) Submit PR 🔀
Include a PR checklist like:

- [ ] Experiment ID assigned + described
- [ ] Repro steps included
- [ ] Inputs/outputs linked
- [ ] STAC/DCAT/PROV added (if evidence artifact)
- [ ] Policy checks pass (Conftest)
- [ ] Gate level declared (0–3)

---

## 🧯 Incident handling

If governance fails after merge (or a harmful artifact is discovered):
1. **Stop the bleeding** 🧯 (revert/disable exposure via API/UI)
2. **Record the incident** 🧾 (issue + linked PRs + affected artifacts)
3. **Preserve audit context** 🧷 (policy version, decision logs)[^kfm_blueprint_runtime_audit]
4. **Apply takedown/withdrawal** if required (CARE Authority to Control)[^kfm_blueprint_care]
5. **Patch the policy** so it can’t recur (fail-closed mindset)[^kfm_blueprint_fail_closed]

---

## 🔗 Related governance + standards (repo links)

- `docs/governance/ROOT_GOVERNANCE.md` (repo-wide governance)
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`
- `docs/governance/REVIEW_GATES.md`
- `docs/standards/` (STAC/DCAT/PROV profiles)
- `docs/templates/` (experiment/story/API templates)[^kfm_master_guide_governance_map]

---

## 🔖 References

[^kfm_master_guide_pipeline]: KFM is a provenance-first “living atlas” with strict pipeline ordering (ETL → catalogs → graph → APIs → UI → story nodes → Focus Mode).:contentReference[oaicite:0]{index=0}
[^kfm_master_guide_invariants]: Key invariants include the API boundary rule and evidence-first narrative constraints.:contentReference[oaicite:1]{index=1}
[^kfm_master_guide_artifacts]: Evidence artifacts (including AI outputs) must be stored, cataloged (STAC/DCAT), traced (PROV), integrated cautiously, and exposed via governed APIs only.:contentReference[oaicite:2]{index=2}
[^kfm_contract_first]: “Contract-first” and “Deterministic pipeline” principles in the repo’s master guide framing.:contentReference[oaicite:3]{index=3}
[^mcp_dir_layout]: Repo structure explicitly includes `mcp/runs/` and `mcp/experiments/`.:contentReference[oaicite:4]{index=4}
[^mcp_design_doc]: MCP-compatible experiment reports and model-card references as part of the repo’s method tracking vision.:contentReference[oaicite:5]{index=5}
[^mcp_repro]: Reproducible coding practices: determinism/seeds, logging, error handling, and notebook reproducibility conventions.:contentReference[oaicite:6]{index=6}
[^mcp_logbook]: Experiment logbook entry expectations (date, ID, author, purpose, method, results, conclusion/next steps).:contentReference[oaicite:7]{index=7}
[^mcp_scientific_method]: Scientific method steps as a documentation and rigor backbone for investigations/experiments.:contentReference[oaicite:8]{index=8}
[^kfm_blueprint_intro]: KFM blueprint: provenance-first design, mediated access via backend API, Focus Mode constrained by policies, and FAIR/CARE principles.:contentReference[oaicite:9]{index=9}
[^kfm_blueprint_fail_closed]: Blueprint principle: fail-closed governance by default; policy failures block merges/actions.:contentReference[oaicite:10]{index=10}
[^kfm_blueprint_policy_as_code]: Blueprint describes policy-as-code via OPA/Rego in a `policy/` directory (data/AI/security/compliance).:contentReference[oaicite:11]{index=11}
[^kfm_blueprint_policy_checks]: CI “Policy Checks” using Conftest; local reproduction via `conftest test .` and targeted runs.:contentReference[oaicite:12]{index=12}
[^kfm_blueprint_runtime_audit]: Runtime OPA-style enforcement and audit logs that retain policy version/hash context for accountability.:contentReference[oaicite:13]{index=13}
[^kfm_blueprint_care]: CARE “Authority to Control”, access tagging, withdraw/takedown support, and community oversight/council role framing.:contentReference[oaicite:14]{index=14}
[^kfm_master_guide_governance_map]: Repo documentation map includes governance, standards, templates, and story node governance structure references.:contentReference[oaicite:15]{index=15}

