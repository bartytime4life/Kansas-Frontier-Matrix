<div align="center">

# 📜 Kansas-Frontier-Matrix — Standard Operating Procedures (`mcp/sops/`)

**Mission:** Define **reproducible, safe, and auditable protocols**  
for every task in the Kansas-Frontier-Matrix.  

SOPs ensure that **pipelines, datasets, and workflows** are:  
✅ Deterministic · ✅ Documented-first · ✅ Validated · ✅ Provenance-tracked  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../.github/workflows/tests.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![STAC Badges](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](../../.github/workflows/stac-badges.yml)  

[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)  
[![Secret Scanning](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/secret-scanning.yml/badge.svg)](../../.github/workflows/secret-scanning.yml)  
[![OpenSSF Scorecard](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ossf-scorecard.yml/badge.svg)](../../.github/workflows/ossf-scorecard.yml)  

![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen?logo=dependabot)  
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)  
![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix)  

</div>

---

## 🎯 Purpose

SOPs capture the **exact reproducible procedure** for any workflow:  
data ingestion, preprocessing, validation, visualization, or integration.  

Every SOP answers:  
- **What is the task?** (scope & problem statement)  
- **Why does it matter?** (context in Kansas-Frontier-Matrix)  
- **How is it done reproducibly?** (steps + validation + provenance)  

---

## 📂 Directory Layout

```

mcp/sops/
├── sop-template.md        # Copy this to start a new SOP
├── ingest_dem.md          # Example: DEM ingestion SOP
├── validate_stac.md       # Example: STAC validation SOP
├── build_tiles.md         # Example: PMTiles generation SOP
└── ...

````

---

## 🔄 SOP Lifecycle

```mermaid
flowchart TD
  A["Problem Definition"] --> B["SOP Draft\n(mcp/sops/sop-template.md)"]
  B --> C["Validation Hooks\nmake targets · schema checks"]
  C --> D["Execution\ncommands copy-paste runnable"]
  D --> E["Artifacts\noutputs, logs, provenance"]
  E --> F["CI/CD Integration\nrun in Actions · track badges"]
  F --> G["Roadmap Link\nlabels · milestones"]
````

<!-- END OF MERMAID -->

---

## 🧩 SOP Template (required fields)

Each SOP must include:

1. **Metadata**

   * SOP ID, owner, version/date, related issues/PRs

2. **Objective**

   * What is the task? Why is it important?

3. **Inputs & Outputs**

   * Data paths, STAC/source descriptors, configs
   * Expected artifacts (COGs, JSON, metrics, tiles)

4. **Procedure (Step-by-step)**

   * Copy-paste commands (deterministic)
   * Make targets (`make fetch`, `make stac`, etc.)

5. **Validation & Checks**

   * Example:

```bash
make stac-validate
make config-validate || true
jq -e 'type=="object"' data/sources/example.json
```

6. **Provenance & Reproducibility**

   * Capture git SHA, checksums, env freeze

7. **Safety / Ethics / Licensing**

   * Sensitive data handling
   * License verification
   * Attribution requirements

8. **Roadmap Integration**

   * Roadmap key marker:

```markdown
<!-- roadmap:key=sop-<stable-key> -->
```

---

## 🧮 CI/CD Integration

* SOPs should reference **Make targets** that CI can run deterministically
* Outputs should produce **artifacts** for upload in GitHub Actions
* Validation hooks ensure every SOP can be re-run on demand

```yaml
jobs:
  run-sop:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: make stac-validate
      - run: make config-validate || true
```

---

## ✅ Checklist for SOP Authors

* [ ] Title + metadata filled (ID, owner, version)
* [ ] Objective + context clearly stated
* [ ] Inputs & outputs listed (STAC, sources, configs)
* [ ] Commands reproducible and deterministic
* [ ] Validation steps included (`make`, `jq`, `kgt`)
* [ ] Provenance captured (hashes, git SHA, env freeze)
* [ ] Safety / license notes included
* [ ] Roadmap marker added (`<!-- roadmap:key=sop-... -->`)

---

## 📚 References

* [Experiment Template](../experiments/template/README.md)
* [Model Cards](../models/)
* [Glossary](../glossary.md)
* [Roadmap](../../.github/roadmap/)

---

## ✅ Summary

The `mcp/sops/` directory contains **auditable SOPs** that define
exact, reproducible workflows for Kansas-Frontier-Matrix.

Each SOP is **deterministic, CI-validatable, provenance-tracked, and roadmap-linked**.
Together, they make the system **transparent, scientific, and MCP-compliant**.
