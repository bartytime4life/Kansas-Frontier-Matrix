# 🧪 MCP Experiments Lab

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-2ea44f)
![Docs-First](https://img.shields.io/badge/Docs--First-Always-blue)
![Reproducible](https://img.shields.io/badge/Reproducible-Required-brightgreen)
![Status](https://img.shields.io/badge/Status-Experimental-yellow)
![Traceability](https://img.shields.io/badge/Traceability-Git%20Backed-orange)

> **What is this?**  
> This folder is the **version-controlled lab notebook** for KFM experiments: every significant analysis / AI trial / pipeline tweak gets documented, reproducible, and reviewable.  
> It exists to keep **data + code + documentation + results** tightly integrated (and traceable via Git history). [oai_citation:0‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

---

## 🧠 MCP, in this repo

**MCP = Master Coder Protocol** — a documentation-first, scientific, reproducible, modular workflow spanning AI, data science, and full-stack practices. [oai_citation:1‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) [oai_citation:2‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

In KFM’s design, the `mcp/` directory anchors protocol docs + templates, and **experiments** are meant to be logged and comparable over time (optionally with metrics/artifacts tracked by tools like DVC). [oai_citation:3‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## 🎯 What belongs here

Put an experiment here if it answers **a question** like:

- “Does OCR pipeline A produce fewer date-parsing errors than pipeline B?”
- “Does NER model X extract more correct place names than regex or baseline?”
- “Does georeferencing workflow change RMS error or layer alignment?”
- “Do we get better performance/cost by changing caching strategy or query batching?”
- “Does a visualization change improve comprehension of time-sliced layers?”

KFM’s system is explicitly built around **ingesting & processing** historical maps + GIS datasets, OCR/parsing documents, and an AI engine that cross-references spatial + textual knowledge for the UI. [oai_citation:4‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)  
So experiments commonly touch: **ingestion**, **georeferencing**, **OCR**, **NLP**, **geospatial analysis**, **temporal indexing**, **UI/visualization**.

---

## 🧱 Folder layout (standard)

Use one folder per experiment. The MCP documentation recommends encapsulating each experiment’s artifacts with a consistent structure like README + protocol + data + code + results. [oai_citation:5‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

**Recommended structure:**

```text
📁 mcp/experiments/
  📁 EXP-0001_place-name-ner/
    📄 README.md          # experiment report (filled template)
    📄 protocol.md        # planned method (before running)
    📁 data/              # raw + derived inputs (or pointers if huge)
    📁 src/               # scripts/notebooks used
    📁 results/           # figures/tables/metrics + short narrative
    📁 configs/           # parameter files tied to this EXP ID
    📁 logs/              # execution logs (if applicable)
```

> Tip: Don’t overwrite raw data. Version it (or store immutable references) and log what changed. [oai_citation:6‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🏷️ Naming conventions

Keep it boring and sortable:

- **Experiment ID:** `EXP-####` (sequential) **or** `EXP-YYYYMMDD-##` (dated)
- **Slug:** short kebab-case summary (`place-name-ner`, `cog-tiling-benchmark`, `georef-rms-tuning`)
- **Folder:** `EXP-####_<slug>/`

Numbering/dating enables tracing “how we got here” over time (and comparing approach changes). [oai_citation:7‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

---

## ✅ The experiment lifecycle (scientific method, MCP style)

Every experiment should explicitly follow (and **write down**) the scientific method steps:

1. **Ask a question / define the problem**
2. **Background research** (what’s already known, cite it)
3. **Hypothesis / expected outcome**
4. **Experiment design (methods)** — written *before* running
5. **Conduct experiment** (note deviations in real time)
6. **Data collection** (how/where data is stored + labeled)
7. **Analysis** (tests, metrics, visualizations)
8. **Results** (traceable outputs)
9. **Conclusion** (supports/refutes hypothesis; limitations)
10. **Iterate / next steps** [oai_citation:8‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🧾 Required documents (minimum)

| Artifact 📄 | Location | Why it matters |
|---|---|---|
| Experiment report | `mcp/experiments/EXP-xxxx_*/README.md` | Version-controlled experiment history & decisions [oai_citation:9‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw) |
| Protocol | `protocol.md` | Standardized experiment protocol; improves reproducibility [oai_citation:10‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) |
| Code | `src/` | Links results to exact scripts/notebooks used [oai_citation:11‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) |
| Results | `results/` | Figures/tables/metrics + short interpretation |
| Configs | `configs/` | Retrieve exact parameters later (treat configs as code) [oai_citation:12‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) |

---

## 🧩 Experiment report template (copy/paste)

KFM’s design calls for an **experiment report template** with sections like Goals, Data Used, Method, Results, Interpretation. [oai_citation:13‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

Create `mcp/experiments/EXP-xxxx_slug/README.md` using this skeleton:

```markdown
# EXP-0000 — <short title>

## 🔎 Goal
- Question:
- Why it matters to KFM:
- Success criteria (metrics + thresholds):

## 📚 Background
- Prior art / related experiments:
- Assumptions:

## 🧪 Hypothesis
- Expected outcome:
- What would falsify it:

## 🧰 Data Used
- Datasets (with versions/IDs):
- Data provenance links (where/how generated):
- Train/val/test split (if applicable):

## 🧠 Method
- Approach summary:
- Key parameters:
- Tools + versions:
- Runtime environment:
- Random seeds:

## ▶️ How to Reproduce
1. Setup steps
2. Commands to run
3. Expected artifacts

## 📈 Results
- Tables / plots:
- Primary metrics:
- Secondary observations:

## 🧾 Interpretation
- What the results mean:
- Limitations / threats to validity:

## ✅ Conclusion
- Support/refute hypothesis:
- Decision / recommendation:

## 🧭 Next Steps
- Follow-up experiments:
- TODOs:
```

---

## 📓 Experiment logbook (project-wide index)

MCP recommends a project-wide experiment log where **every** experiment creates an entry with:
**Date, Experiment ID, Author, Purpose, Method summary, references to protocol/code, results summary, and conclusion/next steps**. [oai_citation:14‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

**Suggested file:** `mcp/experiments/EXPERIMENT_LOG.md`

Example entry:

```markdown
- 2026-01-30 — EXP-0007 — @your-handle
  - Purpose: Compare spaCy NER vs baseline regex for place extraction
  - Method: <1–3 lines> (links: protocol + src)
  - Results: <1–3 lines> (link: results/)
  - Conclusion/Next: <1–2 lines>
```

---

## 🔁 Reproducibility rules (non-negotiable)

### Determinism & repeatability
- Prefer deterministic outputs; record and set **random seeds** where applicable. [oai_citation:15‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- Add logging for long-running experiments and document where logs live + how to read them. [oai_citation:16‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- Capture failures: error handling should be informative; experiment docs should note failure modes. [oai_citation:17‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### Version everything that matters
- Record how to access prior versions and what changed (data changelog mindset). [oai_citation:18‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- Tag trained models with IDs and keep a simple model registry (data + code + params + metrics). [oai_citation:19‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- Treat config files as code; store configs by experiment ID. [oai_citation:20‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### Snapshots (for “future-proof” replication)
When an experiment completes, capture a “snapshot” of:
- code reference (commit)
- data version/reference
- environment details  
…and store it in an archive location if needed. [oai_citation:21‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### Reproducibility checklist ✅
Before merging/closing an experiment, ensure:
- Parameters/configurations documented
- Code committed (and commit hash noted)
- Seeds recorded (if used)
- Dependency versions noted
- Results independently verified
- Documentation checked by another team member [oai_citation:22‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🧪 Stats & rigor guardrails (avoid self-inflicted lies)

Even good-faith experimentation can go wrong through:
- **Optional stopping** (changes error rates if stopping rules depend on results) [oai_citation:23‡Understanding Statistics & Experimental Design.pdf](sediment://file_0000000038e0722f8ee76e6a371bf703)
- **HARKing / post-hoc storytelling** (theory shaped to noise) [oai_citation:24‡Understanding Statistics & Experimental Design.pdf](sediment://file_0000000038e0722f8ee76e6a371bf703)
- **Flexible analyses / p-hacking** (trying many transforms/outlier rules until “significant”) [oai_citation:25‡Understanding Statistics & Experimental Design.pdf](sediment://file_0000000038e0722f8ee76e6a371bf703)

If an experiment is high-stakes or likely to be contentious, consider **preregistration**:
write the plan first, run second, and document deviations (with justification). [oai_citation:26‡Understanding Statistics & Experimental Design.pdf](sediment://file_0000000038e0722f8ee76e6a371bf703)

---

## 🧭 SOPs (how we do things the same way)

KFM’s design calls for **SOP documents** as step-by-step guides (purpose, prerequisites, procedure, expected outcome, troubleshooting). They may live under `docs/sops/` or `mcp/sops/` and cover workflows like adding a map layer, updating gazetteer/training data, QC, or deployment. [oai_citation:27‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

If your experiment adds a new repeatable workflow, consider writing or updating an SOP.

---

## 🔌 How this plugs into KFM

KFM is designed as a modular pipeline:
- ingest raw sources (maps, GIS, documents)
- process into structured spatial + textual repositories
- run AI cross-referencing / pattern recognition
- publish results into an interactive map + timeline UI [oai_citation:28‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

Experiments in this folder are how we **validate improvements** to any of those layers without losing the reasoning trail.

---

## 🛠️ Suggested tools (optional, but helpful)

MCP explicitly suggests tracking experiments with tools like:
- MLflow / Neptune / Weights & Biases (params/metrics/artifacts)
- ELN/LIMS for lab-style work
- A structured folder system if no specialized tool is used [oai_citation:29‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

KFM’s design also notes DVC can be used to track metrics/artifacts for comparing runs over time. [oai_citation:30‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## 🧷 Quick Start (new experiment in ~5 minutes)

1. 📁 Create folder: `mcp/experiments/EXP-####_<slug>/`
2. 📄 Add `protocol.md` (write the method first)
3. 📄 Copy the report template into `README.md`
4. 🧰 Add `src/` and `configs/` (commit everything needed to rerun)
5. ▶️ Run experiment, save outputs to `results/` (plus `logs/` if needed)
6. 🧾 Fill in Results + Interpretation + Conclusion + Next Steps
7. 📓 Append a new line to `EXPERIMENT_LOG.md` (if present)
8. ✅ Run the reproducibility checklist, then commit

---

## 🤝 Contribution style (tiny rules that save us later)

- Prefer “small, complete” experiments over giant sprawling ones.
- If it isn’t documented, it didn’t happen. 🧾
- If it can’t be reproduced, it’s not done. 🔁
- If it can’t be traced to code + data versions, it’s not trustworthy. 🧭

KFM’s goal is a system that stays **evidence-backed, transparent, and collaborative** as it grows. [oai_citation:31‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)