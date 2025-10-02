<div align="center">

# 📑 Kansas-Frontier-Matrix — Documentation & File Templates (`docs/templates/`)

**Mission:** Provide **standardized templates** for all datasets, scripts, modules, STAC items, and issues.  
Templates enforce **consistency, reproducibility, and provenance** across the repository.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../.github/workflows/tests.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![STAC Badges](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](../../.github/workflows/stac-badges.yml)  

[![Labels Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/labels.yml/badge.svg)](../../.github/workflows/labels.yml)  
[![PR Labeler](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pr-labeler.yml/badge.svg)](../../.github/workflows/pr-labeler.yml)  
[![Roadmap Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/roadmap.yml/badge.svg)](../../.github/workflows/roadmap.yml)  

![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen?logo=dependabot)  
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)  
![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix)  

</div>

---

## 🎯 Design Goals

- **Consistency** → every file follows the same conventions  
- **Traceability** → provenance, versioning, and authorship required  
- **Clarity** → contributors start without guesswork  
- **Reusability** → templates can be copied & adapted across modules  

---

## 📂 Directory Layout

```

docs/templates/
├── README.md            # This file
├── dataset.md           # Template for documenting new datasets
├── script.md            # Template for new utility scripts
├── module.md            # Template for new Python modules/packages
├── stac_item.json       # Skeleton STAC Item template
├── stac_collection.json # Skeleton STAC Collection template
└── issue.md             # Fallback GitHub Issue template

````

---

## 🔄 Template Lifecycle

```mermaid
flowchart TD
  A["New contribution"] --> B["Choose template\ndataset · script · module · issue"]
  B --> C["Fill metadata\nsource · license · provenance"]
  C --> D["Validation\nstac-validate · schema checks"]
  D --> E["Commit & review\nno TODO/FILL_ME_IN placeholders"]
  E --> F["Roadmap integration\nlabels · milestones"]
````

<!-- END OF MERMAID -->

---

## 📘 Usage

### 1. 🗂 Datasets

When adding new data under `data/raw/` or `data/processed/`, copy `dataset.md` into the dataset folder as `README.md`:

```bash
cp docs/templates/dataset.md data/processed/hydrology/README.md
```

Fill in:

* **Source & citation**
* **Ingest method**
* **Checksum**
* **Projection / schema**
* **License**

---

### 2. ⚙️ Scripts

For new utilities under `scripts/`, copy `script.md` and paste at the top of the file as a docstring or comment block.
Always describe:

* Purpose
* Usage examples
* Inputs/outputs
* Dependencies

---

### 3. 📦 Modules

When adding a new submodule under `src/kansas_geo_timeline/`, copy `module.md` as `README.md`.
Document:

* Purpose
* Public API
* Dependencies
* Example usage

---

### 4. 🗺️ STAC Templates

Use `stac_item.json` and `stac_collection.json` as **boilerplate** for new metadata records.
Validate with:

```bash
make stac-validate
```

---

### 5. 📝 Issues

If `.github/ISSUE_TEMPLATE/` is missing, `issue.md` can be used to scaffold new GitHub issues consistently.

---

## ✅ Good Practices

* Always update the template **before committing** — placeholders like `TODO` or `FILL_ME_IN` are **not allowed in `main`**
* Templates are **living documents** — evolve them as workflows and metadata standards grow
* Reference [`docs/sop.md`](../sop.md) for the authoritative Standard Operating Procedures

---

## 📑 Roadmap Integration

Templates link to roadmap milestones via hidden markers:

```markdown
<!-- roadmap:key=template-<stable-key> -->
```

This ensures new templates or template changes appear in **roadmap sync**.

---

## ✅ Summary

The `docs/templates/` folder enforces **discipline at scale**:
Every new dataset, script, module, or metadata file starts **self-documented, reproducible, and auditable**,
supporting the Kansas-Frontier-Matrix’s mission of **MCP-grade reproducibility and provenance**.
