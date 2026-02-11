# 🧪 Experiments

This directory is a **governed, reproducible** sandbox for testing ideas that may improve Kansas Frontier Matrix (KFM) as a **pipeline → catalog → database → API → UI** system.[^kfm-blueprint-what]

Experiments are expected to:
- be **evidence-first** (claims and results trace back to sources),[^kfm-md-guide-evidence]
- respect the **trust membrane** (UI and external clients never access databases directly; access is mediated by the governed API),[^kfm-blueprint-trust-membrane]
- capture **provenance** so that results can be audited and repeated,[^kfm-comprehensive-provenance][^prov-sidecar]
- pass repository **validation + CI gates** (docs linting, link validation, sensitivity and security scanning, schema checks where applicable).[^md-guide-ci]

> [!IMPORTANT]
> **This folder is not a loophole.** “Experimental” does *not* exempt work from provenance, sensitivity, licensing, or security rules.[^md-guide-ci]

## 🔗 Related governed docs

These references are part of KFM’s governed documentation set (paths shown as referenced in the KFM Markdown guide; verify in-repo paths if they change):[^kfm-md-guide-scope]

- `docs/MASTER_GUIDE_v13.md` — repo structure, pipeline sequence, governance gates.[^kfm-md-guide-artifacts]
- `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` — how to author governed Markdown docs.[^kfm-md-guide-artifacts]
- `docs/standards/KFM_CHATGPT_WORK_PROTOCOL.md` — rules for AI-assisted content (project-file grounding, no uncited claims).[^kfm-md-guide-artifacts]
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` — baseline template for governed docs.[^kfm-md-guide-artifacts]
- `docs/templates/TEMPLATE__STORY_NODE_V3.md` — Story Node template (Focus Mode integration + citations).[^kfm-md-guide-artifacts]
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` — documenting API changes.[^kfm-md-guide-artifacts]

> [!NOTE]
> Even a README can be a governed document. The KFM Markdown guide explicitly includes README files within scope and subject to governance + CI validation.[^kfm-md-guide-scope]

## 🚀 Quick start

1. Create an experiment folder: `experiments/EXP-YYYYMMDD-short_slug/`
2. Add:
   - `experiment.yaml` (required; see template below)
   - `README.md` (experiment-level decision record; see template below)
3. Run locally:
   - Start the dev stack (Docker Compose) if needed.[^kfm-blueprint-compose]
   - Run your experiment end-to-end.
4. Before a PR:
   - Run local checks where possible (example: `pre-commit run --all-files`).[^kfm-md-guide-local]
   - Verify links and citations; preview Markdown rendering.[^kfm-md-guide-local]

---

## 📌 When to use `experiments/`

Use this folder when you need a tight loop to answer questions like:

- Does a new pipeline transformation improve data quality without breaking downstream contracts?
- Does an indexing choice improve spatial query performance?
- Does a Focus Mode prompt/template reduce hallucinations and improve citation coverage?
- Can a UI interaction pattern be made accessible without sacrificing map performance?
- Can we validate STAC/DCAT/PROV constraints earlier (and more cheaply) in CI?

Experiments should **either**:
1) graduate into production code/docs (via the correct KFM layers and templates), **or**
2) be archived with a clear decision record.

---

## ✅ In scope / 🚫 Out of scope

| ✅ In scope (good) | 🚫 Out of scope (do not do here) |
|---|---|
| Reproducible benchmarks, prototypes, evaluation harnesses | “Quick hacks” with no provenance or unclear licensing |
| Small, reviewable datasets (fixtures), or synthetic data | Committing large raw datasets or sensitive exports |
| Notebooks + scripts that can be rerun end-to-end | Results that cannot be recreated (missing seeds / env) |
| Contract experiments that preserve API boundaries | Bypassing the API to query PostGIS/Neo4j “just to test”[^kfm-blueprint-trust-membrane] |
| Documentation experiments (lint rules, templates, render tests) | Shipping production features from `experiments/` |

> [!WARNING]
> If your experiment requires **sensitive locations, culturally restricted knowledge, or PII**, stop and route it through the governance process first. CI includes automated scanning for sensitive content and classification inconsistencies.[^md-guide-ci]

---

## 🗂️ Directory layout

Recommended structure (create one folder per experiment):

```text
experiments/
  README.md                         # (this file)
  _shared/                          # optional shared helpers for experiments only
    datasets/                        # small fixture datasets (no sensitive data)
    schemas/                         # experimental schemas (STAC/DCAT/PROV, JSON Schema, etc.)
    runners/                         # small harness scripts (benchmarks, report generators)
  EXP-YYYYMMDD-short_slug/           # one experiment = one folder
    README.md                        # experiment overview + decision record
    experiment.yaml                  # machine-readable experiment manifest (see below)
    src/                             # code used by the experiment
    notebooks/                       # notebooks (if used)
    data/                            # inputs (fixtures or pointers; avoid large commits)
    outputs/                         # generated outputs (small + versioned)
    prov/                            # provenance bundle(s) (PROV JSON-LD, RO-Crate, etc.)
    logs/                            # run logs (timestamps, parameters, checksums)
```

> [!NOTE]
> If you generate something valuable, consider converting it into a pipeline step, a governed doc, or a Story Node—don’t leave it stranded in a notebook.[^kfm-blueprint-jupyter]

---

## 🧭 Experiment lifecycle

```mermaid
flowchart TD
  A[Idea / Problem Statement] --> B[Design (question + hypothesis + metrics)]
  B --> C[Run (script/notebook + pinned environment)]
  C --> D[Record outputs + provenance]
  D --> E[Review (governance + correctness + reproducibility)]
  E -->|Promote| F[Production change (proper layer + tests + docs)]
  E -->|Archive| G[Close out (decision + links + retained artifacts)]
```

---

## 🏷️ Naming & IDs

Each experiment folder **must** use a unique ID:

- `EXP-YYYYMMDD-short_slug`  
  Example: `EXP-20260211-prov-sidecar-checks`

Rationale: stable IDs improve traceability, review, and future search.

---

## 🧾 Required experiment manifest

Each experiment folder must include an `experiment.yaml` (or `experiment.json`) that answers:

- **what** was tested,
- **why** it matters to KFM,
- **inputs** (datasets, docs, code refs),
- **how** it was run (environment, parameters),
- **outputs** (files + checksums),
- **decision** (promote / archive / pending).

### Minimal `experiment.yaml` template

```yaml
id: "EXP-20260211-prov-sidecar-checks"
title: "Provenance sidecar validation for derived artifacts"
status: "draft"  # draft | active | complete | archived
owners:
  - name: "TBD"
    role: "maintainer|contributor"
created: "2026-02-11"
last_updated: "2026-02-11"

question: >
  What problem are we trying to solve?
hypothesis: >
  What do we expect to be true if the approach works?

scope:
  in_scope:
    - "What is included"
  out_of_scope:
    - "What is excluded"

inputs:
  datasets:
    - "dcat:TBD"   # DCAT dataset id (preferred)
    - "stac:TBD"   # STAC item/collection id (if relevant)
  documents:
    - "docs/MASTER_GUIDE_v13.md"
    - "docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md"
  code_refs:
    - path: "experiments/EXP-20260211-prov-sidecar-checks/src"
      commit: "<commit-sha>"  # (not confirmed in repo) include when known

environment:
  execution:
    method: "docker-compose|local|ci"
    notes: "Pin versions where possible (python/node, docker image tag, etc.)"
  hardware:
    cpu: "TBD"
    memory_gb: "TBD"
  seeds:
    - 1337

procedure:
  steps:
    - "Step 1…"
    - "Step 2…"
  commands:
    - "docker-compose up --build"
    - "docker-compose exec api pytest"  # example; adjust to repo reality

metrics:
  - name: "validation_pass_rate"
    definition: "% of outputs with valid provenance metadata"
    target: ">= 100%"

outputs:
  artifacts:
    - path: "outputs/report.md"
      sha256: "TBD"
    - path: "prov/provenance.jsonld"
      sha256: "TBD"

risks:
  - kind: "sensitivity"
    description: "Does this touch protected locations or culturally restricted info?"
    mitigation: "Use redaction/generalization; governance review required."

decision:
  outcome: "pending"  # promote | archive | pending
  rationale: "TBD"
  follow_ups:
    - "TBD"
links:
  issues:
    - "TBD"
  prs:
    - "TBD"
```

> [!TIP]
> KFM documentation governance expects **explicit provenance linkages** (dataset IDs, doc URNs, or commit hashes) for substantive claims.[^kfm-md-guide-evidence]

---

## 🔁 Reproducibility rules (non‑negotiable)

### Required
- Pin or record environment (container image tag, runtime version, OS).
- Record **parameters**, **seeds**, and **commands** used.
- Store outputs with **checksums** (at minimum `sha256`).
- Ensure a reviewer can re-run your work **from scratch** using only repo content + documented dependencies.

### Strongly recommended
- Prefer deterministic pipelines over ad-hoc interactive runs.
- Avoid “mystery notebooks”: if you use notebooks, also provide a runnable script version, or a clear notebook execution order.

---

## 🧱 Architecture & trust membrane guardrails

KFM is designed so that:
- the UI never directly touches the databases; all access is mediated by backend API governance layers,[^kfm-blueprint-trust-membrane]
- Focus Mode is **not** an ungoverned chatbot; it is constrained to verified data with references.[^kfm-blueprint-trust-membrane]

**Implication for experiments:**  
If your experiment needs database data, obtain it via:
- governed APIs,
- pipeline outputs in `data/processed` (if present), or
- sanctioned fixtures.

If you believe bypassing a layer is necessary for a benchmark, you must:
1) state why in `experiment.yaml`,
2) limit it to local runs, and
3) ensure no “backdoor pattern” is promoted into production.

---

## 🧬 Provenance: what to capture

KFM’s ethos is that provenance logging is “first-class,” and user interfaces (like Focus Mode audit panels and dataset dialogs) can surface origin + transformation history.[^kfm-comprehensive-provenance]

Recommended provenance patterns:
- **Sidecar provenance files** (e.g., `prov/provenance.jsonld`) stored next to derived artifacts.[^prov-sidecar]
- **RO-Crate** style packaging when distributing a set of files with metadata + provenance.[^prov-sidecar]
- Provide a stable way to retrieve provenance by resource identity (PROV-AQ patterns such as `.prov` or `?prov`) where applicable *(implementation may vary; not confirmed in repo)*.[^prov-aq]

> [!CAUTION]
> Provenance itself can be sensitive (agent names, protected locations, etc.). If needed, abstract/redact or restrict access and document what was withheld.[^prov-sidecar]

---

## 🧪 Local dev hooks for experiments

KFM’s dev environment is expected to support Docker Compose workflows and API exploration via Swagger UI.[^kfm-blueprint-compose][^kfm-blueprint-swagger]

<details>
<summary><strong>Common Docker Compose tips (ports, rebuilds)</strong></summary>

- Port conflicts: if something is already using `5432` (Postgres), change port mappings or stop the conflicting service.[^kfm-blueprint-compose]  
- Rebuild after dependency changes: `docker-compose up --build` or `docker-compose build`.[^kfm-blueprint-compose]

</details>

<details>
<summary><strong>API exploration</strong></summary>

- Swagger UI is expected at `http://localhost:8000/docs`.[^kfm-blueprint-swagger]  
- If GraphQL is enabled, it may be exposed at `/graphql`.[^kfm-blueprint-swagger]

</details>

> [!NOTE]
> The blueprint suggests checking for CLI utilities (e.g., scripts under `api/scripts/` or an entrypoint script) to run admin tasks, reindexing, or fixture loading. *(Exact scripts not confirmed in repo.)*[^kfm-blueprint-cli]

---

## 🧷 CI expectations for experiments

KFM’s CI expectations include (not exhaustive):
- Markdown protocol/front-matter validation
- Link/reference validation
- STAC/DCAT/PROV schema validation (where relevant)
- Graph integrity tests (fixtures)
- API contract tests
- Security scans (secret scanning, PII/sensitive content scanning, sensitive location checks, classification consistency checks)[^md-guide-ci]

**Design experiments to pass CI**, or explicitly scope them as “local-only” and avoid committing outputs that trigger failures.

---

## ✅ Definition of Done (DoD) for a new experiment

Before opening a PR:

- [ ] New experiment folder name follows `EXP-YYYYMMDD-short_slug`
- [ ] `experiment.yaml` completed (question, hypothesis, metrics, inputs, env, outputs)
- [ ] Provenance bundle included (or documented why it is not applicable)
- [ ] Outputs are small, reviewable, and checksummed
- [ ] No secrets in commits; no PII; no protected locations without governance approval[^md-guide-ci]
- [ ] README (experiment-level) includes outcome/decision and links to follow-up work
- [ ] CI passes (or explicit, approved exception documented)

---

## 📚 References

[^kfm-blueprint-what]: *Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint* — description of KFM as a pipeline–catalog–database–API–UI system and provenance-first emphasis.  
[^kfm-blueprint-trust-membrane]: *Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint* — “UI never directly touches the databases” and governed access enforcement.  
[^kfm-comprehensive-provenance]: *Kansas Frontier Matrix (KFM) Comprehensive Guide* — provenance logging integrated into UX (Focus Mode audit panel, dataset dialogs) and AI answers with footnotes.  
[^kfm-md-guide-evidence]: *KFM Markdown Formatting & Style Guide* — evidence-first requirement for claims and CI-ready docs (including README files).  
[^kfm-md-guide-scope]: *KFM Markdown Formatting & Style Guide* — scope includes README files as governed documentation artifacts.
[^kfm-md-guide-artifacts]: *KFM Markdown Formatting & Style Guide* — key artifacts & references (Master Guide, templates, work protocols).
[^kfm-md-guide-local]: *KFM Markdown Formatting & Style Guide* — local workflow tips (run checks like pre-commit, preview Markdown, verify links, update Version History).
[^md-guide-ci]: *MARKDOWN_GUIDE_v13* — CI checks for front-matter, links, schema validation, and security/governance scans (secret/PII/sensitive location/classification).  
[^prov-sidecar]: *KFM-Software Support* — provenance publication options including sidecar files and RO-Crate packaging.  
[^prov-aq]: *KFM-Software Support* — PROV-AQ recommendations for provenance retrieval patterns (e.g., `.prov` / `?prov`).  
[^kfm-blueprint-compose]: *Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint* — Docker Compose troubleshooting (port conflicts, rebuild advice).  
[^kfm-blueprint-swagger]: *Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint* — Swagger UI at `http://localhost:8000/docs` and GraphQL option.  
[^kfm-blueprint-cli]: *Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint* — suggested CLI utilities under `api/scripts/` or equivalent.  
[^kfm-blueprint-jupyter]: *Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint* — notebook use and guidance to convert valuable work into pipelines/docs.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---:|---|---|---|
| v0.1.0 | 2026-02-11 | Initial governed README for experiments (structure, provenance, CI expectations). | (AI-assisted; reviewer TBD) |
