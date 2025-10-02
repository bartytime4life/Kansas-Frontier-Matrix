<div align="center">

# 🧭 Kansas-Frontier-Matrix — MCP (`/mcp/`)

**Mission:** Implement the **Master Coder Protocol (MCP)** across  
all experiments, SOPs, and models to ensure **reproducibility, provenance,  
and documentation-first science**.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](.github/workflows/site.yml)  
[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](.github/workflows/tests.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](.github/workflows/stac-validate.yml)  
[![STAC Badges](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](.github/workflows/stac-badges.yml)  

[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](.github/workflows/trivy.yml)  
[![Secret Scanning](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/secret-scanning.yml/badge.svg)](.github/workflows/secret-scanning.yml)  
[![OpenSSF Scorecard](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ossf-scorecard.yml/badge.svg)](.github/workflows/ossf-scorecard.yml)  

[![Roadmap Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/roadmap.yml/badge.svg)](.github/workflows/roadmap.yml)  
[![Labels Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/labels.yml/badge.svg)](.github/workflows/labels.yml)  
[![PR Labeler](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pr-labeler.yml/badge.svg)](.github/workflows/pr-labeler.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](.github/workflows/automerge.yml)  

![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen?logo=dependabot)  
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)  
![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix)  

</div>

---

## 🎯 Purpose

The `mcp/` directory is the **protocol backbone** for Kansas-Frontier-Matrix:  

- **Experiments (`experiments/`)** — reproducible, hypothesis-driven logs  
- **SOPs (`sops/`)** — canonical instructions for tasks and pipelines  
- **Model Cards (`models/`)** — documentation for AI/ML components  
- **Glossary / Templates (`docs/templates/`)** — controlled vocab and research scaffolds  

Together, they ensure **every dataset, pipeline, and result is auditable, reproducible, and roadmap-linked.**

---

## 📂 Directory Layout

```

mcp/
├── experiments/       # MCP experiments (template + individual runs)
│   └── template/      # scaffold for new experiments
├── sops/              # Standard Operating Procedures
├── models/            # Model cards, configs, benchmarks
├── glossary.md        # Controlled vocabulary (cross-disciplinary)
└── templates/         # experiment.md, sop.md, model_card.md

````

---

## 🔄 MCP Lifecycle

```mermaid
flowchart TD
  A["Problem / Hypothesis"] --> B["Experiment Plan\n(mcp/experiments/template)"]
  B --> C["SOPs\n(mcp/sops/*.md)"]
  C --> D["Run commands.sh\nDeterministic execution"]
  D --> E["Artifacts\nmetrics.json · stac_report.json · figures/"]
  D --> F["Provenance\nSHA-256 hashes · git commit"]
  E --> G["Analysis & Interpretation"]
  G --> H["Roadmap Integration\nmilestones, issues, PRs"]
````

<!-- END OF MERMAID -->

---

## 🧪 Experiments

* Template lives at [`mcp/experiments/template/`](./experiments/template/)
* Start new experiments by copying the template:

```bash
cp -r mcp/experiments/template mcp/experiments/EXP-2025XXXX-my-study
```

* Fill out metadata, hypothesis, and parameters
* Run `commands.sh` to generate metrics, reports, hashes
* Link results to roadmap with:

```markdown
<!-- roadmap:key=exp-<stable-key> -->
```

---

## 📝 SOPs (Standard Operating Procedures)

SOPs live in [`mcp/sops/`](./sops/).
Each SOP documents:

* Problem + scope
* Step-by-step procedure
* Validation hooks (`make stac-validate`, `make config-validate`)
* Safety, provenance, and reproducibility requirements

---

## 🤖 Models

Model cards live in [`mcp/models/`](./models/).
Each `model_card.md` includes:

* **Purpose** — what task does the model solve
* **Training data** — source, size, licensing
* **Metrics** — accuracy, uncertainty, coverage
* **Bias & risks** — limitations
* **Repro details** — config files, hyperparameters, seeds

---

## 🧮 Validation & CI Hooks

* **Experiments** must pass STAC + schema validation
* **SOPs** must run deterministically with reproducible Make targets
* **Models** must document hyperparams + metrics
* **CI pipelines** enforce:

```bash
make stac-validate
make config-validate
make site
```

Artifacts (`stac_report.json`, provenance hashes, metrics) are uploaded in CI for audit trails.

---

## ✅ Checklists

**Before starting an experiment**

* [ ] Hypothesis & success criteria defined
* [ ] Inputs linked to STAC/source descriptors
* [ ] SOP reference(s) included
* [ ] Params noted in `params.yaml`

**Before merging results**

* [ ] Commands reproducible (`commands.sh`)
* [ ] Provenance captured (`git_sha.txt`, `artifact_hashes.txt`)
* [ ] Outputs validated (`stac-validate`, schema checks)
* [ ] Roadmap marker added (`<!-- roadmap:key=exp-... -->`)

---

## 📚 References

* [Experiment Template](./experiments/template/README.md)
* [SOPs](./sops/)
* [Model Cards](./models/)
* [Glossary](./glossary.md)
* [Templates](./templates/)

---

## ✅ Summary

The `mcp/` directory is the **MCP-grade governance hub** of Kansas-Frontier-Matrix.
Every experiment, SOP, and model card is **traceable, reproducible, and roadmap-connected**,
with CI/CD ensuring integrity, provenance, and scientific rigor.
