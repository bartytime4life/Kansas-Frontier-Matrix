<!-- .github/ISSUE_TEMPLATE/README.md -->

# 🧩 Issue Templates — Kansas Matrix System (KFM) 🗺️🤖

![KFM](https://img.shields.io/badge/KFM-provenance--first-2ea44f)
![Repo](https://img.shields.io/badge/monorepo-code%2Bdata%2Bdocs-blue)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-orange)

> This folder contains the GitHub Issue Templates used to keep **Kansas Frontier Matrix (KFM)** contributions **evidence-backed**, **transparent**, and **collaborative** — with provenance and governance built-in. ✅

---

## 🚀 Start here

### 🧭 Open the template picker
➡️ Use GitHub’s template chooser: **`Issues → New issue → Choose a template`**

If you’re unsure which template to use, read the guide below and pick the closest match. Maintainers can retag later — clarity beats perfection. 🙌

---

## 🧠 The “why” behind these templates (KFM rules of the road)

KFM is designed as a **pipeline → catalog → database → API → UI** platform where everything remains traceable (“the map behind the map”). 🧬🗺️  
These templates ask for extra context because that context is **part of the product**.

### 🔁 Canonical data path (non-negotiable)
> **Raw → Processed → Catalog/Prov → Database → API → UI**

If a proposal tries to shortcut this flow (e.g., “inject directly into UI”), it will be treated as **architecturally risky** by default. 🧱

### 🧾 Provenance-first & fail-closed governance
- Missing license/metadata/provenance can block a merge. 🚫
- Sensitive/community-controlled information needs special handling. 🛡️

---

## 🗂️ Quick routing — where does your issue “live”?

Use these prefixes in your title to help triage fast:

- `[api]` 🧪 FastAPI backend (endpoints, validation, policy enforcement)
- `[web]` 🎛️ React/TypeScript UI (maps, timelines, UX, rendering)
- `[pipelines]` 🏭 ETL & simulation (imports, transforms, QA)
- `[data]` 🧱 Raw/processed datasets + metadata
- `[catalog]` 🗃️ STAC/DCAT metadata + discoverability
- `[provenance]` 🧬 PROV lineage logs + audit trails
- `[docs]` 📚 Architecture docs, stories, narratives, diagrams
- `[ai]` 🤖 Focus Mode, retrieval, citations, policy constraints
- `[security]` 🔐 Privacy, access control, abuse prevention

---

## 🧰 Template guide (what to choose + what we’ll ask for)

<details>
<summary><strong>🐞 Bug Report</strong> — Something is broken</summary>

Include:
- **What happened vs what you expected**
- **Exact steps to reproduce**
- Screenshots / console logs / stack traces (sanitize secrets)
- Scope: `[api]`, `[web]`, `[pipelines]`, etc.
- Environment: OS, browser, Python/Node versions, dataset name(s)

Bonus points:
- “Smallest repro” branch/commit
- Any relevant file paths (ex: `api/...`, `web/...`)
</details>

<details>
<summary><strong>✨ Feature Request</strong> — New capability or major change</summary>

Include:
- The **user goal** (what problem are we solving?)
- The **data path** impact (how it fits the canonical pipeline)
- Proposed UI/UX behavior (mockups welcome 🎨)
- API changes (new endpoints? schema?)
- Governance implications (FAIR/CARE, privacy, access tiers)

Helpful:
- “Definition of done” checklist ✅
- Alternatives considered
</details>

<details>
<summary><strong>🗺️ Dataset / Data Ingest Request</strong> — Add or update data</summary>

Include:
- **Source link(s)** + citation(s)
- **License** (required)
- Coverage: **time range**, **spatial extent**, **format** (GeoJSON, raster, CSV, etc.)
- Suggested pipeline steps (or what you tried)
- Expected outputs in:
  - `data/processed/`
  - `data/catalog/` (STAC/DCAT)
  - `data/provenance/` (PROV / lineage)

Tip: If your request implies “skip metadata,” it will likely be rejected — metadata + provenance are first-class. 🧾🧬
</details>

<details>
<summary><strong>📚 Story / Narrative / Docs</strong> — Add or improve story content</summary>

Include:
- What story you want to add/change (scope)
- Proposed outline (bullets are fine)
- **Sources / citations** (required)
- Any related dataset IDs or file paths
- Sensitivity notes (content warnings if needed)

If you’re contributing a full story: expect review for accuracy, writing quality, and citations. ✍️🕰️
</details>

<details>
<summary><strong>🤖 AI / Focus Mode</strong> — Answer quality, citations, retrieval, policy behavior</summary>

Include:
- The exact question/prompt you used
- The answer you got (and why it’s wrong/unsafe/incomplete)
- Expected answer + what sources should have been used
- Whether it’s:
  - Retrieval issue (missing docs/data)
  - Prompt/policy constraint issue
  - Citation formatting/grounding issue
  - Hallucination / overreach issue

Remember: Focus Mode should remain policy-bound and citation-forward. 🧠📎
</details>

<details>
<summary><strong>🔐 Security / Privacy / Governance</strong> — Potential harm, sensitive info, access control</summary>

✅ File an issue for:
- Policy gaps
- Access tier logic bugs
- Data takedown/withdrawal workflows
- Sensitive content handling improvements

🚫 Do <em>not</em> post:
- Secrets, tokens, private keys
- Personal info about living people
- Restricted community-controlled data

If you suspect an exploitable vulnerability, use the repository’s **Security Advisory** flow (if enabled) instead of a public issue. 🛡️
</details>

---

## ✅ “Good issue” checklist (copy/paste into your issue if needed)

- [ ] I searched for duplicates 🔎
- [ ] I used a clear scope prefix (e.g., `[api]`, `[data]`) 🏷️
- [ ] I included reproduction steps / expected outcome 🧪
- [ ] If data-related: I included **license + source** 📜
- [ ] If story-related: I included **citations** 📚
- [ ] I did **not** include sensitive/private info 🔐

---

## 🧱 KFM repo mental map (helps you file issues precisely)

```text
📦 repo/
├── api/          🧪 FastAPI backend
├── web/          🎛️ React + TypeScript UI
├── pipelines/    🏭 ETL pipelines & simulation scripts
├── data/         🧱 Versioned datasets + metadata
│   ├── raw/          🧊 immutable source snapshots
│   ├── processed/    🧼 cleaned/standardized outputs
│   ├── catalog/      🗃️ STAC/DCAT metadata
│   └── provenance/   🧬 lineage logs (PROV)
└── docs/         📚 narratives, architecture, stories
```

---

## 🤝 What happens after you file

Maintainers will typically:
1. Label + route (`api/web/data/pipelines/...`)
2. Ask for missing info (if needed)
3. Convert to a PR task list or link to a tracking issue
4. Close when fixed (or mark as “blocked” with next steps)

Thanks for helping keep KFM **auditable**, **reproducible**, and **community-trustworthy**. 🧡🗺️