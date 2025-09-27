# `docs/templates/` — Documentation & File Templates

This folder contains **standard templates** for use across the Kansas Frontier Matrix repository.  
They ensure that **all new files, datasets, scripts, and docs** follow consistent structure, metadata, and reproducibility guidelines.

---

## Design Goals

- **Consistency**: Every new file follows the same conventions.
- **Traceability**: Templates require provenance, versioning, and authorship.
- **Clarity**: Easy for contributors to start new files without guesswork.
- **Reusability**: Templates can be copied and adapted across modules.

---

## Directory Layout

```

docs/templates/
├── README.md            # This file
├── dataset.md           # Template for documenting new datasets
├── script.md            # Template for new utility scripts
├── module.md            # Template for new Python modules/packages
├── stac_item.json       # Skeleton STAC Item template
├── stac_collection.json # Skeleton STAC Collection template
└── issue.md             # GitHub Issue template (fallback if .github not available)

````

---

## Usage

### 1. Datasets

When adding new data under `data/raw/` or `data/processed/`, copy `dataset.md` into the dataset folder as `README.md`:

```bash
cp docs/templates/dataset.md data/processed/hydrology/README.md
````

Fill in:

* **Source & citation**
* **Ingest method**
* **Checksum**
* **Projection / schema**
* **License**

---

### 2. Scripts

When creating a new utility under `scripts/`, copy `script.md` and paste at the top of the file as a docstring or comment block.
Always describe:

* Purpose
* Usage examples
* Inputs/outputs
* Dependencies

---

### 3. Modules

When adding a new submodule under `src/kansas_geo_timeline/`, copy `module.md` as `README.md`.
Document:

* Purpose
* Public API
* Dependencies
* Example usage

---

### 4. STAC Templates

Use `stac_item.json` and `stac_collection.json` as **boilerplate** for new metadata records.
Validate with:

```bash
make stac-validate
```

---

### 5. Issues

If `.github/ISSUE_TEMPLATE/` is missing, `issue.md` can be used to scaffold new GitHub issues consistently.

---

## Notes

* Always update the template before committing — placeholders like `TODO` or `FILL_ME_IN` are not allowed in `main`.
* Templates are **living documents** — update them if workflows or metadata standards evolve.
* See [`docs/sop.md`](../sop.md) for the authoritative Standard Operating Procedures.

---

✅ **Mission-grade principle**: Templates enforce **discipline at scale**, so every new addition is **self-documented, reproducible, and auditable**.

```
