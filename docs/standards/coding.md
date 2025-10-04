<div align="center">

# 💻 Kansas Frontier Matrix — Coding Standards & Style Guide  
`docs/standards/coding.md`

**Purpose:** Define consistent **coding, formatting, documentation, and governance standards**  
for all source code and configuration files across the **Kansas Frontier Matrix (KFM)** repository —  
ensuring maintainability, reproducibility, and MCP-aligned auditability.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../../LICENSE)

</div>

---

## 📚 Overview

The **KFM Coding Standards** exist to guarantee that:
- Code is **reproducible** and deterministic.
- Implementations are **transparent**, well-documented, and auditable.
- Practices are **consistent** across data, pipelines, web, and automation systems.
- All contributors adhere to **MCP principles**:  
  📘 Documentation-first · 🔁 Reproducible · 🌍 Open-standard · 🔗 Provenance · 🧾 Auditable.

These standards apply to:
- `src/` (Python ETL and pipeline scripts)
- `web/` (JavaScript + MapLibre visualization)
- `.github/workflows/` (YAML automation scripts)
- `Makefile`, configuration files, and documentation scripts.

---

## 🧩 Core Coding Principles (MCP-Aligned)

| Principle | Description | Implementation |
|:-----------|:--------------|:----------------|
| **Documentation-first** | Code must include clear docstrings and README references. | Use docstrings for all functions and modules. |
| **Reproducibility** | All code must produce identical results given the same inputs. | Version-lock dependencies in `requirements.txt` or `package.json`. |
| **Open Standards** | Use open libraries and formats only. | Prefer `GeoTIFF`, `GeoJSON`, `CSV`, `JSON Schema`. |
| **Provenance** | Code must log transformations and data lineage. | Use `data/work/logs/` for logging. |
| **Auditability** | Code must pass linting, type checking, and security scans. | CI/CD workflows enforce `pre-commit` and `CodeQL`. |

---

## 🐍 Python Standards

### Code Style
- Follow **PEP 8** style conventions.
- Maximum line length: **100 characters**.
- Indentation: **4 spaces** (no tabs).
- Imports:
  - Standard library imports first.
  - Third-party libraries next.
  - Local imports last.
- Use **type hints** for all functions and class methods.

### Example
```python
from pathlib import Path
import geopandas as gpd
from utils.checksum import sha256_file

def process_terrain(input_file: Path, output_dir: Path) -> Path:
    """
    Process terrain raster data into a standardized GeoTIFF output.

    Args:
        input_file (Path): Path to input DEM file.
        output_dir (Path): Directory for processed output.

    Returns:
        Path: Path to validated GeoTIFF.
    """
    terrain = gpd.read_file(input_file)
    processed = terrain.to_crs(epsg=4326)
    output_path = output_dir / "processed_dem.tif"
    processed.to_file(output_path)
    sha256_file(output_path)
    return output_path
````

---

### Naming Conventions

| Element                | Convention                 | Example                        |
| :--------------------- | :------------------------- | :----------------------------- |
| **Modules / Packages** | lowercase with underscores | `terrain_pipeline.py`          |
| **Classes**            | PascalCase                 | `TerrainProcessor`             |
| **Functions**          | lowercase with underscores | `generate_checksum()`          |
| **Variables**          | lowercase with underscores | `input_path`, `checksum_value` |
| **Constants**          | ALL_CAPS                   | `DEFAULT_CRS = 4326`           |

---

### Documentation

| Element             | Requirement                                              | Example                      |
| :------------------ | :------------------------------------------------------- | :--------------------------- |
| **Docstrings**      | Required for all public functions, classes, and modules. | PEP 257 format.              |
| **Inline Comments** | Short, context-specific, limited to <80 chars.           | `# Compute DEM slope values` |
| **README.md**       | Each module directory must have one.                     | Describes purpose and usage. |

---

### Linting & Formatting

| Tool           | Purpose                                  | Configuration              |
| :------------- | :--------------------------------------- | :------------------------- |
| **Black**      | Auto-format Python code.                 | Line length 100.           |
| **Ruff**       | Fast linter for style and import checks. | `.ruff.toml`               |
| **Isort**      | Enforces import sorting.                 | Integrated via pre-commit. |
| **Mypy**       | Type-checking for all Python scripts.    | Optional in CI/CD.         |
| **Pre-Commit** | Runs all checks automatically.           | `.pre-commit-config.yaml`  |

---

## 🌐 JavaScript / Web Standards

### Frameworks & Tools

* Use **Vanilla JS** or **MapLibre GL JS** for mapping.
* Optional libraries: D3.js, Turf.js, or Lodash (only if documented and justified).
* Follow **ES6+ syntax** and modern JS conventions.

### Code Style

* Indentation: **2 spaces**.
* Max line length: **100 characters**.
* Use `const` and `let` instead of `var`.
* Always include inline JSDoc comments for functions.

```javascript
/**
 * Add terrain layer to MapLibre map viewer.
 * @param {Object} map - MapLibre map instance.
 * @param {string} id - Unique layer ID.
 */
function addTerrainLayer(map, id) {
  map.addSource(id, {
    type: "raster",
    tiles: ["data/tiles/terrain/{z}/{x}/{y}.png"],
    tileSize: 256,
  });

  map.addLayer({
    id: id,
    type: "raster",
    source: id,
    paint: { "raster-opacity": 0.85 },
  });
}
```

---

### JavaScript Linting & Build

| Tool            | Purpose               | Configuration               |
| :-------------- | :-------------------- | :-------------------------- |
| **ESLint**      | JavaScript linting    | `.eslintrc.json`            |
| **Prettier**    | Code formatting       | `.prettierrc`               |
| **Node.js**     | Dependency management | `package.json`              |
| **Mermaid CLI** | Diagram generation    | used in documentation build |

---

## ⚙️ YAML / Workflow Standards

| Standard           | Description                                                              |
| :----------------- | :----------------------------------------------------------------------- |
| **YAML Schema**    | All GitHub Actions workflows must validate under YAML 1.2.               |
| **Workflow Names** | Use clear, descriptive names: `Build & Deploy Docs`, `Validate STAC`     |
| **Secrets**        | Managed only via GitHub Actions secrets. Never hardcoded.                |
| **Triggers**       | Minimize redundant workflow triggers. Use `paths-ignore` and `branches`. |

---

## 🧩 Makefile Conventions

| Target                              | Purpose                               |
| :---------------------------------- | :------------------------------------ |
| **make all**                        | Run all major pipelines sequentially. |
| **make terrain / hydrology / etc.** | Run domain-specific ETL.              |
| **make checksums**                  | Generate and validate SHA-256 hashes. |
| **make stac-validate**              | Validate STAC and metadata.           |
| **make site**                       | Build documentation and deploy site.  |
| **make clean-***                    | Remove temporary or cache files.      |

All Makefile commands must:

* Be **idempotent** (safe to rerun).
* Log all operations to `data/work/logs/`.
* Fail gracefully with clear messages.

---

## 🧠 Security & Governance Standards

| Policy                 | Implementation                                          |
| :--------------------- | :------------------------------------------------------ |
| **Code Signing**       | Commits verified via GPG or GitHub verified signatures. |
| **Dependencies**       | Locked in `requirements.txt` / `package-lock.json`.     |
| **Secrets Management** | Environment variables or GitHub Secrets only.           |
| **Static Analysis**    | CodeQL + Trivy scan results reviewed before merge.      |
| **Access Control**     | Write permissions restricted to maintainers and CI/CD.  |

---

## 🧾 Version Control Practices

| Rule                | Description                                                               |
| :------------------ | :------------------------------------------------------------------------ |
| **Commit Messages** | Use semantic prefixes: `feat:`, `fix:`, `docs:`, `data:`, `ci:`, `chore:` |
| **Branch Naming**   | Use lowercase hyphenated format: `feature/add-stac-validation`            |
| **Pull Requests**   | Must include a link to related issue or ADR.                              |
| **Tags**            | Use `vX.Y.Z` semantic versioning for releases.                            |
| **Code Reviews**    | Required before merging to `main`.                                        |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                              |
| :---------------------- | :---------------------------------------------------------- |
| **Documentation-first** | Code and workflows documented before merge.                 |
| **Reproducibility**     | Configs and dependencies versioned; CI/CD verified.         |
| **Open Standards**      | Python, JS, YAML, JSON Schema, STAC.                        |
| **Provenance**          | Logs + metadata track code and data lineage.                |
| **Auditability**        | CodeQL, pre-commit, and CI/CD enforce traceable validation. |

---

## 📎 Related Documentation

| File                                   | Description                                  |
| :------------------------------------- | :------------------------------------------- |
| `docs/standards/metadata-standards.md` | Metadata and schema conventions.             |
| `docs/architecture/ci-cd.md`           | CI/CD automation enforcing coding standards. |
| `.pre-commit-config.yaml`              | Pre-commit hook configuration.               |
| `.github/workflows/codeql.yml`         | Code security scanning workflow.             |
| `.github/workflows/trivy.yml`          | Dependency vulnerability scanning.           |

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                                      |
| :------ | :--------- | :--------------------- | :----------------------------------------------------------- |
| v1.0    | 2025-10-04 | KFM Documentation Team | Initial coding standards and style guide for MCP compliance. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Line Documented. Every Function Proven.”*
📍 [`docs/standards/coding.md`](.) · Official coding standards and style guide for reproducible development in KFM.

</div>
