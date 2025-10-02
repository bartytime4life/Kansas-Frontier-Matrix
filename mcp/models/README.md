<div align="center">

# 🤖 Kansas-Frontier-Matrix — Models (`mcp/models/`)

**Mission:** Document and govern all **AI/ML models** in the project  
using **MCP-grade model cards** for **transparency, reproducibility, and provenance**.  

Every model must be:  
✅ Fully documented · ✅ Deterministic/reproducible · ✅ Auditable · ✅ Linked to roadmap  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../.github/workflows/tests.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![STAC Badges](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](../../.github/workflows/stac-badges.yml)  

[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)  
[![Secret Scanning](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/secret-scanning.yml/badge.svg)](../../.github/workflows/secret-scanning.yml)  
[![OpenSSF Scorecard](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ossf-scorecard.yml/badge.svg)](../../.github/workflows/ossf-scorecard.yml)  

[![Roadmap Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/roadmap.yml/badge.svg)](../../.github/workflows/roadmap.yml)  
[![Labels Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/labels.yml/badge.svg)](../../.github/workflows/labels.yml)  
[![PR Labeler](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pr-labeler.yml/badge.svg)](../../.github/workflows/pr-labeler.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../.github/workflows/automerge.yml)  

![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen?logo=dependabot)  
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)  
![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix)  

</div>

---

## 🎯 Purpose

The `mcp/models/` directory ensures every model used in this project is:  

- **Reproducible** — documented configs, seeds, dependencies  
- **Transparent** — data sources, metrics, bias risks stated up front  
- **Auditable** — provenance (hashes, env snapshots, commit IDs)  
- **Governed** — tied to roadmap milestones and automation  

---

## 📂 Directory Layout

```

mcp/models/
├── template/             # Model card template (copy for new models)
│   └── model_card.md
├── example-model/        # Example implementation
│   ├── model_card.md
│   ├── config.yaml
│   ├── metrics.json
│   └── provenance/
└── ...

````

---

## 🔄 Model Lifecycle

```mermaid
flowchart TD
  A["Define task & scope"] --> B["Draft model_card.md\n(template-based)"]
  B --> C["Train / Load model\nconfigs + SOPs"]
  C --> D["Evaluate\nmetrics.json · figures/"]
  D --> E["Provenance\nhashes · env freeze · commit IDs"]
  E --> F["CI/CD Integration\nvalidation + artifact checks"]
  F --> G["Roadmap Link\nlabels · milestones"]
````

<!-- END OF MERMAID -->

---

## 📑 Model Card (Required Fields)

Each model must have a `model_card.md` with:

1. **Metadata**

   * Model ID, version, owner, date, license

2. **Purpose**

   * What problem does this model solve?
   * How is it used in Kansas-Frontier-Matrix?

3. **Training Data**

   * Source datasets (STAC/sources descriptors)
   * Size, coverage, license restrictions

4. **Architecture & Configs**

   * Algorithms (e.g., RF, CNN, Transformer)
   * Configs: YAML/JSON in repo

5. **Metrics**

   * Quantitative: accuracy, F1, RMSE, coverage
   * Qualitative: interpretability, uncertainty

6. **Bias & Risks**

   * Known limitations, failure modes
   * Ethical considerations (data bias, sensitive sites)

7. **Provenance**

   * Commit SHA, artifact hashes, env snapshot

8. **Roadmap Integration**

   * Milestone, epic, issue links
   * Roadmap marker:

```markdown
<!-- roadmap:key=model-<stable-key> -->
```

---

## 🧮 Validation & CI Hooks

Models integrate with CI/CD via:

* **Config checks** → `jsonschema`, `yamllint`
* **Repro runs** → `make model-validate` (optional)
* **Artifact uploads** → metrics.json, provenance logs

Example validation block:

```yaml
jobs:
  validate-model:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: yamllint mcp/models/**/config.yaml
      - run: jq -e 'type=="object"' mcp/models/**/metrics.json
```

---

## ✅ Checklist for Model Authors

* [ ] Model card filled (metadata, purpose, configs, metrics)
* [ ] Training data referenced (STAC/source descriptors)
* [ ] Configs + SOPs deterministic
* [ ] Metrics.json generated & versioned
* [ ] Provenance captured (`git_sha.txt`, artifact hashes, env freeze)
* [ ] Bias/risks documented
* [ ] Roadmap marker added (`<!-- roadmap:key=model-... -->`)

---

## 📚 References

* [Experiment Template](../experiments/template/README.md)
* [SOPs](../sops/)
* [Glossary](../glossary.md)
* [Roadmap](../../.github/roadmap/)

---

## ✅ Summary

The `mcp/models/` directory is the **AI/ML governance hub** of Kansas-Frontier-Matrix.
Every model is **documented, reproducible, and roadmap-linked**,
with CI/CD enforcing **validation, provenance, and transparency**.
