# 🧪 MCP Experiments

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-5b5bff)
![Docs-First](https://img.shields.io/badge/Documentation-First-brightgreen)
![Reproducible](https://img.shields.io/badge/Reproducible-By%20Design-orange)
![Traceable](https://img.shields.io/badge/Provenance-Traceable-informational)

> **What this is:** a documentation-first, reproducibility-first lab notebook for **Kansas Frontier Matrix (KFM)** experiments—where every run becomes a reusable, reviewable knowledge artifact. [^kfm-provenance] [^docs-first] [^mcp-dir]

---

## ⚡ TL;DR Workflow

1) **Create** a new experiment folder (`EXP-###_<slug>/`)  
2) **Write the protocol first** (`protocol.md`)  
3) **Run the experiment** (code/notebook + captured config)  
4) **Record results** (`README.md`) + store artifacts (`results/`)  
5) **Update the logbook** (`EXPERIMENT_LOG.md`) and/or traceability row

This mirrors MCP’s scientific-method emphasis and makes comparisons repeatable across time, contributors, and toolchains. [^mcp-scientific-method] [^mcp-logbook]

---

## 🎯 What belongs in `mcp/experiments/`

This directory is for **experiment logs & results**—including the *purpose, configuration, and outcomes* of tests across the KFM stack (data → processing → models → UI), plus any R&D spikes that need a durable record. [^mcp-dir] [^kfm-pipeline]

Typical examples:
- 🗺️ Geospatial processing benchmarks (e.g., georeferencing RMSE thresholds, tiling strategies)
- 🤖 NLP/LLM comparisons (e.g., spaCy vs regex extraction; prompt/model variants)
- 🧱 Pipeline experiments (e.g., new catalog schema, provenance tracking, OCR variants)
- 📈 Performance tests (e.g., DB query plans, caching strategies, ingest throughput)

---

## 🗂️ Recommended folder layout

Here’s the **expected** structure for experiments (add or remove subfolders as needed, but keep the core artifacts consistent):

```text
📁 mcp/
└─ 📁 experiments/                             🧪 experiment lane (reproducible, logged, reviewable)
   ├─ 📄 README.md                              👈 you are here
   ├─ 📄 EXPERIMENT_LOG.md                      🧾 rolling lab notebook / index (append-only)
   ├─ 📁 _templates/                            ◻️ optional: shared templates for experiments
   └─ 📁 EXP-001_example_slug/                  🏷️ one experiment (numbered + named)
      ├─ 📄 README.md                            🧾 experiment report (Goals → Data → Method → Results → Interpretation)
      ├─ 📄 protocol.md                          🧪 protocol (Objective → Materials → Procedure → Variables → Expected)
      ├─ 📁 data/                                🧱 inputs (or pointers/manifests if too large)
      ├─ 📁 src/                                 🧠 scripts used for the run (versioned)
      ├─ 📁 notebooks/                           ◻️ optional notebooks (if used; keep minimal)
      ├─ 📁 configs/                             ⚙️ params, env manifests, seeds (deterministic)
      ├─ 📁 results/                             📈 outputs (plots, tables, metrics, artifacts)
      └─ 📁 archive/                             ◻️ optional: frozen snapshots (for long-term reproducibility)
```

This structure is aligned with MCP’s reproducibility/logging patterns and the KFM “templates + experiment reports” approach. [^mcp-exp-structure] [^kfm-exp-template]

---

## 🚀 Create a new experiment (copy/paste friendly)

> **Naming convention:** `EXP-###_<short-kebab-slug>`  
> Examples: `EXP-014_georef-rmse-threshold`, `EXP-021_spacy-vs-regex-entities`  
> Numbering/labels are recommended for long-running research threads. [^mcp-protocol-template]

1. **Create folder**
   ```bash
   mkdir -p mcp/experiments/EXP-###_my-experiment/{data,src,configs,results}
   ```

2. **Add protocol**
   - Create `protocol.md` using the template below  
   - Fill in objective/materials/procedure/variables *before running* [^mcp-protocol-template]

3. **Run the experiment**
   - Put scripts in `src/` (or notebooks in `notebooks/`)
   - Capture params and environment in `configs/` (see “Reproducibility”)

4. **Write the report**
   - Create `README.md` (inside the experiment folder) with **Goals / Data Used / Method / Results / Interpretation** [^kfm-exp-template]

5. **Log it**
   - Add an entry to `EXPERIMENT_LOG.md` (rolling index) [^mcp-logbook]

---

## 🧬 MCP scientific method checklist

MCP experiments follow a scientific-method loop (question → hypothesis → design → run → analyze → conclude → iterate). [^mcp-scientific-method]

Recommended steps:
- **Ask a clear question**
- **Background research** (collect references + constraints)
- **Form a testable hypothesis**
- **Design a method** (controls, variables, metrics)
- **Conduct the experiment**
- **Collect + analyze data**
- **Document results**
- **Draw conclusions**
- **Iterate / refine** [^mcp-scientific-method]

---

## 📦 Required artifacts (minimum viable experiment record)

| Artifact | Required | Why |
|---|---:|---|
| `protocol.md` | ✅ | Prevents “wandering experiments” & makes assumptions explicit. [^mcp-protocol-template] |
| `README.md` (report) | ✅ | Human-readable summary for future you + reviewers. [^kfm-exp-template] |
| `configs/` | ✅ | Ensures you can reproduce the run (params, seeds, env). [^mcp-env] |
| `src/` or `notebooks/` | ✅ | The “how” (what actually executed). |
| `results/` | ✅ | Artifacts: figures, tables, metrics, outputs. |
| `data/` or `data_manifest.*` | ✅* | Inputs or pointers; never overwrite raw. [^mcp-data] |
| `EXPERIMENT_LOG.md` entry | ✅ | Makes it discoverable + searchable. [^mcp-logbook] |

\*If data is large/private, store a **manifest** (paths, hashes, IDs, access notes) rather than raw data.

---

## 🔗 Traceability matrix (strongly recommended)

For experiments that impact the platform, keep a **traceability matrix** row tying:
- Experiment ID ↔ hypothesis/decision ↔ code version ↔ data/model version ↔ result artifact link. [^mcp-traceability]

Suggested file (optional):
- `mcp/experiments/TRACEABILITY.csv`

---

## ✅ Reproducibility & quality gates

### Repro checklist (per experiment)
- [ ] **All parameters** recorded (and defaults noted)
- [ ] **Code committed** (or commit SHA referenced)
- [ ] **Random seeds** recorded (where applicable)
- [ ] **Dependencies** captured (requirements / env / container)
- [ ] **Results summarized** with metrics + artifacts
- [ ] **Independent verification** attempted (even a partial rerun) [^mcp-repro] [^mcp-validation]

### Statistics hygiene (avoid misleading “too good to be true”)
- 📌 **Log failures and null results**, not just successes (selective reporting inflates effects). [^stats-bias]
- 📌 Avoid **optional stopping** (increasing sample size until significance) without explicitly labeling it. [^stats-bias]
- 📌 When possible, **pre-register** the plan (even “lightweight prereg” inside `protocol.md` helps). [^stats-prereg]

---

## 🧰 Tooling hooks (optional but powerful)

- **DVC experiments** can snapshot parameterized runs and track metrics/artifacts for comparisons. [^kfm-dvc]
- For ML-heavy work, consider experiment managers:
  - **MLflow**, **Weights & Biases**, **Neptune**, **TensorBoard**, **Sacred** (pick one per track). [^mcp-tools]

> Rule of thumb: if the experiment influences a product decision, capture it in a way that a third party can reproduce without tribal knowledge.

---

## 🧾 Templates

### 🧪 Protocol template (`protocol.md`)
<details>
<summary><strong>Click to expand</strong></summary>

```markdown
# Protocol — EXP-###: <Short Title>

## Objective
- What question are we answering?
- What decision will this experiment support?

## Background / References
- Links to related experiments
- Papers/datasets/docs

## Materials
- Data inputs (or manifests)
- Tools (libs, versions)
- Hardware assumptions

## Procedure
1. Step-by-step instructions to reproduce
2. Include commands and expected intermediate outputs
3. Define stopping rules (time/iterations/sample size)

## Expected Outcome
- What do we expect to see if the hypothesis is supported?
- What would falsify the hypothesis?

## Variables
- Independent variables:
- Dependent variables (metrics):
- Controls:
- Confounders to watch:

## Notes
- Risks, ethics, sensitive handling, access constraints
```

</details>

This structure mirrors MCP’s protocol guidance (Objective / Materials / Procedure / Expected Outcome / Variables). [^mcp-protocol-template]

---

### 🧾 Experiment report template (`README.md` inside experiment folder)
<details>
<summary><strong>Click to expand</strong></summary>

```markdown
---
title: "EXP-### — <Short Title>"
status: "draft|active|final"
last_updated: "YYYY-MM-DD"
doc_kind: "ExperimentReport"
commit_sha: "<git sha>"
fair_category: "FAIR+CARE"
care_label: "Public|Restricted|Tribal Sensitive|TBD"
---

# EXP-### — <Short Title>

## Goals
- What did we set out to learn?

## Data Used
- Source(s), IDs, hashes, access notes
- Any filtering/selection criteria

## Method
- Approach + rationale
- Parameters (table or bullet list)
- Evaluation metrics

## Results
- Key plots/tables
- Metrics summary
- Links to `results/` artifacts

## Interpretation
- What do results mean?
- Caveats / limitations

## Next Steps
- Follow-up experiments
- Recommended implementation changes (if any)
```

</details>

The section layout (Goals, Data Used, Method, Results, Interpretation) is consistent with the KFM experiment-report template concept. [^kfm-exp-template]  
The YAML front-matter pattern and “care_label / FAIR+CARE” style align with KFM-inspired metadata practices. [^md-frontmatter] [^md-sensitive]

---

### 🧾 Logbook entry template (`EXPERIMENT_LOG.md`)
<details>
<summary><strong>Click to expand</strong></summary>

```markdown
## YYYY-MM-DD — EXP-###_<slug>
- **Owner(s):** @handle
- **Purpose:** one sentence
- **Status:** planned | running | final
- **Links:** ./EXP-###_<slug>/README.md
- **Key results:** (fill in after run)
- **Next steps:** (what to do next)
```

</details>

This matches MCP’s recommendation for a consistent, date/ID-based experiment logbook. [^mcp-logbook]

---

## 🛡️ Sensitive data & ethics

If an experiment touches potentially sensitive locations, communities, or personal data:
- Consider redaction/aggregation and mark sensitivity clearly (e.g., `care_label`). [^md-sensitive]
- Keep provenance and access constraints explicit (who can reproduce, what is restricted). [^kfm-provenance]

---

## ✅ Definition of Done (for each experiment)

- [ ] `protocol.md` complete *before* running  
- [ ] Report written in `README.md` (Goals→Data→Method→Results→Interpretation)  
- [ ] Parameters + environment captured (`configs/`)  
- [ ] Artifacts saved (`results/`) and linked from report  
- [ ] Logbook entry added (`EXPERIMENT_LOG.md`)  
- [ ] All claims backed by references/citations (or marked as assumptions) [^md-dod] [^md-evidence-first]

---

## 📚 Project grounding references

[^kfm-provenance]: KFM frames itself as **provenance-first**, traceable to original sources, and emphasizes **reproducibility/auditability** with **FAIR and CARE** principles. :contentReference[oaicite:0]{index=0}  
[^kfm-pipeline]: KFM specifies a canonical pipeline order (Raw → Processed → Catalog/PROV → Database → API → UI), which experiments should respect/describe when they touch pipeline steps. :contentReference[oaicite:1]{index=1}  
[^mcp-dir]: The KFM hub design doc defines `mcp/` as **Master Coder Protocol** resources and explicitly calls out `mcp/experiments/` as a place for experiment logs/results (purpose/config/outcome) and mentions DVC experiments as an option. :contentReference[oaicite:2]{index=2}  
[^docs-first]: Documentation-first workflow is described as writing down goals/structure and updating docs as knowledge evolves. :contentReference[oaicite:3]{index=3}  
[^kfm-exp-template]: The hub design doc proposes an experiment report template with sections like Goals, Data Used, Method, Results, Interpretation, and emphasizes recording code versions/params and linking outputs. :contentReference[oaicite:4]{index=4}  
[^kfm-dvc]: The hub design doc references using tools like **DVC** for tracking experiments/metrics and versioning artifacts/catalogs. :contentReference[oaicite:5]{index=5}  

[^mcp-scientific-method]: MCP documentation outlines scientific-method steps (question → research → hypothesis → method → run → analyze → conclude → iterate). :contentReference[oaicite:6]{index=6}  
[^mcp-protocol-template]: MCP protocol template fields: Objective, Materials, Procedure, Expected Outcome, Variables; plus recommendation to number/label protocols (EXP-001, etc.). :contentReference[oaicite:7]{index=7}  
[^mcp-exp-structure]: MCP provides an example experiment folder structure (README, protocol, data, src, results, configs, archive). :contentReference[oaicite:8]{index=8}  
[^mcp-logbook]: MCP describes maintaining an experiment logbook with date, experiment ID, notes, and references; suggests domain-specific logs (AI/Physics/Bio/etc.). :contentReference[oaicite:9]{index=9}  
[^mcp-data]: MCP data management guidance includes storing raw data safely, avoiding overwrite, and keeping a data dictionary / provenance. :contentReference[oaicite:10]{index=10}  
[^mcp-repro]: MCP reproducibility checklist includes parameters recorded, code committed, seeds, dependencies, independent verification, documentation/peer review. :contentReference[oaicite:11]{index=11}  
[^mcp-env]: MCP environment setup suggests capturing hardware + dependencies (requirements.txt / environment.yml / Docker) and noting version impacts. :contentReference[oaicite:12]{index=12}  
[^mcp-validation]: MCP highlights validation and peer review (replication/verification; peer review of design/analysis). :contentReference[oaicite:13]{index=13}  
[^mcp-tools]: MCP lists experiment management tools (e.g., MLflow, W&B, Neptune, TensorBoard, ELN/LIMS). :contentReference[oaicite:14]{index=14}  
[^mcp-traceability]: MCP recommends a traceability matrix linking experiment IDs, features/hypotheses, code version, data version, and results reference. :contentReference[oaicite:15]{index=15}  

[^md-frontmatter]: YAML front-matter example and metadata fields (title/path/version/last_updated/status/doc_kind/governance/ethics/FAIR+CARE/doc_uuid/commit_sha/checksum). :contentReference[oaicite:16]{index=16}  
[^md-dod]: “Definition of Done” checklist concept for docs, including “front-matter complete,” “claims cited,” and peer review. :contentReference[oaicite:17]{index=17}  
[^md-evidence-first]: The Markdown guide describes an “evidence-first” style where factual claims include citations/refs (e.g., via footnotes). :contentReference[oaicite:18]{index=18}  
[^md-sensitive]: The Markdown guide discusses redacting/aggregating sensitive info and using metadata fields like `care_label` for restricted handling. :contentReference[oaicite:19]{index=19}  

[^stats-bias]: Stats/design guidance notes that only reporting successful outcomes is problematic and illustrates issues with publication bias and optional stopping. :contentReference[oaicite:20]{index=20}:contentReference[oaicite:21]{index=21}  
[^stats-prereg]: Preregistration: write down the experimental plan and note deviations after running. :contentReference[oaicite:22]{index=22}
