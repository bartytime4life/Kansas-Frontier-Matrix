# ✅ MCP Checklists (Quality Gates)

![MCP](https://img.shields.io/badge/MCP-Protocol-2ea44f?style=for-the-badge)
![Provenance](https://img.shields.io/badge/Provenance-First-blue?style=for-the-badge)
![Fail%20Closed](https://img.shields.io/badge/Governance-Fail%20Closed-critical?style=for-the-badge)

Welcome to `mcp/checklists/` 👋  
This folder contains **copy/paste checklists** used across Kansas-Frontier-Matrix (KFM) to keep contributions:

- 🧾 **Evidence-backed & traceable**
- 🧪 **Reproducible**
- 🧭 **Pipeline-correct**
- 🛡️ **Policy-compliant (fail-closed)**  
- 🤝 **Reviewable by humans + CI**

> ⚠️ **Fail-Closed Rule:** If you can’t verify an item, treat it as **NOT DONE**. No “trust me bro.” 😄

---

## 🧠 Why checklists exist

KFM is a **pipeline → catalog → database → API → UI** system, where everything (including AI outputs) should be traceable back to original sources. Checklists are the smallest “unit of discipline” that keeps the whole system from turning into a black box.

They also make reviews faster: maintainers scan for ✅ “done + linked evidence” instead of re-deriving context from scratch.

---

## 🚀 Quick Start

### ✅ In a Pull Request
1. Choose the relevant checklist(s) below.
2. Paste into the PR description.
3. Check items with links to evidence (files, logs, screenshots, commit SHAs).

### ✅ In an Issue
Use checklists to define “done” (especially for data adds, experiments, and AI changes).

---

## 📦 Checklist Index

> If a checklist file listed here doesn’t exist yet, treat it as **planned** and add it (or open an issue). 🛠️

| Checklist | Use it when… | Typical reviewers |
|---|---|---|
| `pr.md` 🧩 | Any code change | Maintainers + domain owner |
| `data_addition.md` 🗺️ | Adding new data (raw/processed/catalog/prov) | Data steward + geo reviewer |
| `pipeline_run.md` ⚙️ | Running/adding ETL steps | Pipeline owner |
| `metadata_provenance.md` 🧾 | Any new dataset or transformation | Data steward |
| `experiment.md` 🧪 | Any analysis, evaluation, benchmark, or AI experiment | Research lead + reviewer |
| `model_card.md` 🤖 | Adding/updating any model (NER/LLM/classifier/etc.) | ML reviewer + maintainer |
| `policy_ethics_fair_care.md` 🧑‍⚖️ | Anything with sensitive data, access, community impacts | Governance + maintainer |
| `security_privacy.md` 🛡️ | Anything touching auth, user data, external APIs, uploads | Security reviewer |
| `release_milestone.md` 🏁 | Cutting releases, major merges, big dataset drops | Maintainers |

---

## 🧭 The “Golden Path” (KFM Flow)

Use this mental model when selecting checklists:

```text
🧱 Raw → 🧼 Processed → 🧾 Catalog/Provenance → 🗄️ Database → 🔌 API → 🖥️ UI
```

If a change “teleports” around the system (example: UI reads raw files directly), you’re probably skipping governance and traceability gates 🚫.

---

## 🧾 What “Good Evidence” Looks Like

When checking items, prefer **links to repo artifacts**:

- ✅ File paths (e.g. `data/catalog/...`, `data/provenance/...`)
- ✅ CLI output pasted into PR (short)
- ✅ Screenshots for GIS alignment checks (QGIS/MapLibre sanity)
- ✅ Commit SHA referencing exact code used
- ✅ Metrics tables or plots committed as artifacts

> Tip: Prefer **small, atomic evidence** per checkbox rather than one mega write-up.

---

## 🧰 Recommended PR Snippet (copy/paste)

<details>
<summary><b>📋 PR Mini-Checklist (Generic)</b> (click to expand)</summary>

- [ ] This PR has a clear goal statement (1–3 sentences)
- [ ] I linked relevant Issue(s) / Decision(s) / ADR(s)
- [ ] I ran tests / checks locally (or explained why not)
- [ ] I updated docs where behavior changed
- [ ] If data is involved, I included `data_addition.md` checklist items
- [ ] If an experiment/model is involved, I included `experiment.md` / `model_card.md`
- [ ] Nothing bypasses policy / provenance expectations (“fail-closed”)
- [ ] I added rollback notes (how to undo safely)

</details>

---

## 🧪 Experiments & AI (special rules)

If your PR adds or changes **analysis** or **model behavior**, expect to include:

- 🧪 an **experiment report** (or update an existing one)
- 🤖 a **model card** (for any model you ship or fine-tune)
- 🧾 data & provenance references (what data, which version, how produced)
- 🔁 reproducibility details (seeds, environment, parameters)

If the work can’t be reproduced by another contributor, it’s not “done” yet.

---

## 🧑‍⚖️ Ethics / CARE / Sensitive Data

Some data and locations are sensitive. If your change touches:

- sacred sites / burial grounds
- exact coordinates for vulnerable resources
- personally identifiable information
- community-owned knowledge

…then you **must** run `policy_ethics_fair_care.md` and document:
- why the contribution provides collective benefit 🌱
- who has authority to control access 🔐
- how responsibility/ethics are handled 🧭
- what safety mitigations exist (redaction, aggregation, tiered access)

---

## 🧱 How to add a new checklist

1. Create a new file in `mcp/checklists/` (lowercase, underscores):  
   `domain_purpose.md` ✅
2. Keep it **short**, **binary**, and **auditable**:
   - Good: “License is present and compatible (link to file)”
   - Bad: “Data looks fine”
3. Add it to the **Checklist Index** above.
4. If you can automate it in CI later, note it in a `TODO:` line. 🤖

---

## 🔗 Related (handy paths)

- 🏠 Project root: [`../../README.md`](../../README.md)
- 📚 Docs: [`../../docs/`](../../docs/)
- 🗺️ Data: [`../../data/`](../../data/)
- ⚙️ Pipelines: [`../../pipelines/`](../../pipelines/)
- 🔌 API: [`../../api/`](../../api/)
- 🖥️ Web UI: [`../../web/`](../../web/)
- 🧪 Experiments (if present): [`../../experiments/`](../../experiments/)

---

## ✅ Philosophy (simple)

Checklists are not bureaucracy. They are **how KFM scales without losing trust** 🧠✨  
If we can’t explain where something came from, how it was produced, and why it’s safe to use… then it doesn’t belong in the system (yet).