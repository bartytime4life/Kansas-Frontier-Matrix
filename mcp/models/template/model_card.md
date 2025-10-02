<div align="center">

# 🤖 Model Card — TEMPLATE  
### `mcp/models/template/model_card.md`

**Mission:** Provide a **transparent, reproducible, and auditable** record  
for every AI/ML model in Kansas-Frontier-Matrix.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../../.github/workflows/tests.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  

![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen?logo=dependabot)  
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)  
![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix)  

</div>

---

## 📑 Metadata

- **Model ID:** `model-YYYYMMDD-<slug>`  
- **Version:** v0.1.0  
- **Owner(s):** @user  
- **Date:** YYYY-MM-DD  
- **Status:** ☐ Planned ☐ Training ☐ Validated ☐ Released ☐ Deprecated  
- **License:** Apache-2.0 | MIT | CC-BY | Other  

---

## 🎯 Purpose

- **Task:** What does this model solve?  
- **Context:** How is it used in Kansas-Frontier-Matrix (e.g., classification, feature extraction, geospatial reasoning)?  
- **Intended users:** Researchers, contributors, general public  

---

## 📂 Training Data

- **Datasets:**  
  - STAC items/collections  
  - Source descriptors in `data/sources/*.json`  
- **Size & coverage:** samples, spatial/temporal bounds  
- **Preprocessing SOPs:** link to `mcp/sops/*.md`  
- **License constraints:** redistribution, attribution, sensitive use notes  

---

## 🏗 Architecture & Configs

- **Type:** RF | CNN | Transformer | LSTM | Hybrid  
- **Framework:** PyTorch | TensorFlow | Scikit-learn | Other  
- **Config files:** link to `config.yaml`  
- **Randomness policy:** fixed seeds, deterministic ops  

```yaml
# Example config.yaml snippet
model:
  type: RandomForestClassifier
  params:
    n_estimators: 200
    max_depth: 20
seed: 12345
````

---

## 📊 Metrics

* **Quantitative:**

  * Accuracy/F1/Precision/Recall
  * RMSE/MAE (if regression)
  * Coverage %

* **Qualitative:**

  * Interpretability
  * Uncertainty estimates

```json
{
  "accuracy": 0.92,
  "f1_score": 0.89,
  "coverage": 0.95
}
```

---

## ⚖️ Bias & Risks

* Known limitations
* Potential bias sources (dataset imbalance, geography, language)
* Ethical considerations (indigenous data, sensitive sites)
* Fail gracefully → how does the model behave when out-of-scope?

---

## 🧮 Provenance & Reproducibility

* **Commit SHA:** `abc1234`
* **Artifact hashes:** `provenance/artifact_hashes.txt`
* **Environment:** `env.txt` (`pip freeze`)
* **Training logs:** `logs/`

```bash
git rev-parse HEAD > provenance/git_sha.txt
sha256sum models/** > provenance/artifact_hashes.txt
```

---

## 🔐 Security & Validation

* Vulnerability scans (Trivy, CodeQL) applied?
* SBOM available?
* Reproducibility checks (`make model-validate`)?

---

## 📑 Roadmap Link

* Milestone: …
* Related epic/issue: …
* Roadmap marker:

```markdown
<!-- roadmap:key=model-<stable-key> -->
```

---

## ✅ Checklist

* [ ] Metadata complete (ID, owner, version, license)
* [ ] Purpose & scope documented
* [ ] Training data referenced (STAC, sources)
* [ ] Configs deterministic & saved in repo
* [ ] Metrics.json generated & versioned
* [ ] Provenance captured (hashes, git SHA, env freeze)
* [ ] Bias/risks documented
* [ ] Roadmap marker added

---

## 📚 References

* [Experiment Template](../../experiments/template/README.md)
* [SOPs](../../sops/)
* [Roadmap](../../../.github/roadmap/)
* [Glossary](../../glossary.md)

---

## ✅ Summary

This model card ensures **AI/ML models** in Kansas-Frontier-Matrix are:
**transparent, reproducible, provenance-tracked, and roadmap-linked.**
Every contributor can understand **what the model does, how it was built, and how to reproduce it.**
