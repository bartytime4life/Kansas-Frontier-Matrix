<div align="center">

# 💻 Kansas Frontier Matrix — **Coding Standards & Style Guide**

`docs/standards/coding.md`

**Purpose:** Define consistent **coding, formatting, documentation, security, and governance** standards
for all source and configuration files across **Kansas Frontier Matrix (KFM)** — ensuring maintainability,
reproducibility, and **MCP-aligned** auditability.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../../LICENSE)

</div>

---

## 📚 Overview

The **KFM Coding Standards** guarantee that:

* Code is **reproducible** and deterministic.
* Implementations are **transparent**, documented, and auditable.
* Practices are **consistent** across data pipelines, web UI, and automation.
* All work follows **MCP** principles:
  📘 Documentation-first · 🔁 Reproducible · 🌍 Open-standard · 🔗 Provenance · 🧾 Auditable.

**Applies to**

* `src/` (Python ETL/AI/graph/pipeline code)
* `web/` (React, MapLibre, JS/TS)
* `.github/workflows/` (CI/CD YAML)
* `Makefile`, `Dockerfile`, Infra configs
* Docs build scripts and dataset tooling

---

## 🧩 Core Coding Principles (MCP-Aligned)

| Principle               | Description                   | Implementation Examples                                 |
| :---------------------- | :---------------------------- | :------------------------------------------------------ |
| **Documentation-first** | Design + doc before code      | Module `README.md`, docstrings, ADRs                    |
| **Reproducibility**     | Same inputs ⇒ same outputs    | Pinned deps, containers, seeds, idempotent Make targets |
| **Open Standards**      | Prefer open formats/tools     | GeoJSON, COG, CSV/JSON, STAC, JSON Schema               |
| **Provenance**          | Log lineage + decisions       | `data/work/logs/`, provenance records, STAC links       |
| **Auditability**        | Machine-checked quality gates | pre-commit, CodeQL, Trivy, tests in CI                  |

---

## 🐍 Python Standards

### Style & Structure

* **PEP 8** with line length **100**.
* Indentation **4 spaces**; no tabs.
* Imports: stdlib → third-party → local; group with blank lines.
* **Type hints** required on all public functions/classes.
* **Pure functions** where feasible; keep side effects explicit.
* **Small modules**: single responsibility; prefer composition over inheritance.

```python
from pathlib import Path
from typing import Final

import geopandas as gpd

DEFAULT_CRS: Final[int] = 4326

def process_terrain(input_file: Path, output_dir: Path) -> Path:
    """
    Reproject terrain vector/raster and persist in a standard format.

    Args:
        input_file: Input dataset path (vector or raster).
        output_dir: Output directory for processed artifact(s).

    Returns:
        Path to the processed artifact.
    """
    gdf = gpd.read_file(input_file)
    gdf = gdf.to_crs(epsg=DEFAULT_CRS)

    output = output_dir / "processed_dem.tif"
    gdf.to_file(output)
    return output
```

### Naming

| Element          | Convention   | Example               |
| :--------------- | :----------- | :-------------------- |
| Modules/Packages | `snake_case` | `terrain_pipeline.py` |
| Classes          | `PascalCase` | `TerrainProcessor`    |
| Functions        | `snake_case` | `generate_checksum()` |
| Variables        | `snake_case` | `input_path`          |
| Constants        | `ALL_CAPS`   | `DEFAULT_CRS = 4326`  |

### Documentation

* **Docstrings** (PEP 257) mandatory for modules, public classes, functions (Google or reST).
* Inline comments are short, **≤ 80 chars**, for non-obvious logic only.
* Each subpackage has a **README.md** with purpose, usage, and small example.

### Linting, Types & Formatting

| Tool           | Purpose             | Config                                             |
| :------------- | :------------------ | :------------------------------------------------- |
| **Black**      | Auto-format         | Line length 100                                    |
| **Ruff**       | Lint + import rules | `.ruff.toml` (enable flake8/pycodestyle/pyupgrade) |
| **isort**      | Import ordering     | Via Ruff or `.isort.cfg`                           |
| **mypy**       | Static typing       | `mypy.ini` (strict on `src/`, relaxed in tests)    |
| **pre-commit** | Local checks        | `.pre-commit-config.yaml`                          |

**Recommended `mypy.ini` excerpt**

```ini
[mypy]
python_version = 3.11
warn_unused_ignores = True
warn_return_any = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
no_implicit_optional = True
```

### Logging & Errors

* Use **`logging`** (no `print`) with structured context; default level `INFO` in apps, `WARNING` in libs.
* **Never** swallow exceptions. Convert to domain-specific errors if needed and re-raise.
* Emit file/record identifiers that support provenance links.

```python
import logging
logger = logging.getLogger(__name__)

try:
    # step…
except Exception as exc:  # noqa: BLE001
    logger.exception("terrain.process_failed file=%s", input_file)
    raise
```

### Config & Secrets

* Use `pydantic-settings`/`dotenv` or environment variables; **no secrets in code**.
* Define a single settings module per service; support overrides via `ENV`.

---

## 🌐 JavaScript / TypeScript (Web)

### Frameworks

* React 18+, **MapLibre GL JS**, optional D3/Turf.
* Prefer **TypeScript** for new code; otherwise JSDoc types.

### Style

* Indentation **2 spaces**, max line **100**.
* Use `const`/`let` (never `var`).
* **Functional components + hooks**; avoid class components.
* Keep components small; extract hooks for data fetching.

```ts
/**
 * Add raster terrain layer.
 */
export function addTerrainLayer(map: maplibregl.Map, id: string, tiles: string[]) {
  map.addSource(id, { type: "raster", tiles, tileSize: 256 });
  map.addLayer({ id, type: "raster", source: id, paint: { "raster-opacity": 0.85 } });
}
```

### Lint, Format, Build

| Tool               | Purpose               | Config                       |
| :----------------- | :-------------------- | :--------------------------- |
| **ESLint**         | Linting (TS/JS/React) | `.eslintrc.json`             |
| **Prettier**       | Formatting            | `.prettierrc`                |
| **TypeScript**     | Types                 | `tsconfig.json`              |
| **Vite / Webpack** | Bundling              | `vite.config.ts` (preferred) |

**Accessibility**

* Use ARIA roles/labels, keyboard navigation, and color-contrast tokens.
* Run automated a11y checks (axe) in CI for critical routes.

**Security (Web)**

* Avoid `innerHTML`; sanitize untrusted input.
* Set CSP/security headers at serving layer; use HTTPS-only endpoints.

---

## ⚙️ YAML / GitHub Actions

* YAML 1.2 compliant; avoid anchors for readability.
* Workflow names must be explicit: `Validate STAC`, `Checksums`, `CodeQL`.
* Use matrices where helpful, but restrict triggers with `paths`/`paths-ignore`.

```yaml
name: Validate STAC
on:
  pull_request:
    paths: ["data/stac/**", ".github/workflows/stac-validate.yml"]
jobs:
  stac:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pipx install stac-validator
      - run: stac-validator data/stac --recursive --links
```

---

## 🧩 Makefile Conventions

| Target                       | Purpose                    |
| :--------------------------- | :------------------------- |
| `make all`                   | Run top-level pipelines    |
| `make terrain/hydrology/...` | Domain ETL                 |
| `make checksums`             | Generate/verify SHA-256    |
| `make stac-validate`         | Validate STAC/JSON schema  |
| `make site`                  | Build + deploy docs/site   |
| `make clean-*`               | Remove temp or cache files |

**Rules**

* Idempotent; safe to re-run.
* Log to `data/work/logs/` with timestamps.
* Exit non-zero on failures; concise error messages.

---

## 🐳 Containers & Repro Environments

* Each service has a **Dockerfile** with pinned versions and a minimal runtime (e.g., `python:3.11-slim`).
* Multi-stage builds for smaller images; include **SBOM** generation (Syft) when possible.
* Prefer **rootless** containers, drop caps, and read-only filesystem for runtime.

---

## 🛡️ Security & Governance

| Policy                  | Enforcement                                                     |
| :---------------------- | :-------------------------------------------------------------- |
| **Commit verification** | GPG or GitHub Verified                                          |
| **Dependencies**        | Locked (`requirements.txt`, `poetry.lock`, `package-lock.json`) |
| **Static analysis**     | CodeQL; JS/TS rules enabled                                     |
| **Vuln scanning**       | Trivy for images/deps                                           |
| **Secrets**             | GitHub/OIDC; no plaintext in code/logs                          |
| **Access control**      | Least privilege; PRs require review                             |

---

## 🧪 Testing Standards

* **Unit tests** for pure logic; **integration** for I/O and data flows; **contract** tests for APIs.
* Minimum coverage goals (guideline): **70% unit**, **smoke** coverage for pipelines.
* Store test fixtures under `tests/fixtures/`.
* Use deterministic seeds and temporary dirs; clean up artifacts.

```bash
pytest -q --maxfail=1 --disable-warnings
```

---

## 🧾 Version Control Practices

| Rule                     | Description                                                              |
| :----------------------- | :----------------------------------------------------------------------- |
| **Conventional Commits** | `feat:`, `fix:`, `docs:`, `data:`, `ci:`, `refactor:`, `chore:`          |
| **Branch naming**        | `feature/add-stac-validation`, `fix/terrain-proj-bug`                    |
| **PR requirements**      | Link issue/ADR; include screenshots for UI; attach logs for data changes |
| **Tags**                 | `vX.Y.Z` semver; changelog entries required                              |
| **Code reviews**         | 1+ approval; CI green; large PRs require design notes/ADR                |

---

## 🧰 Pre-Commit (Reference Snippet)

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks: [{ id: ruff, args: ["--fix"] }, { id: ruff-format }]
  - repo: https://github.com/psf/black
    rev: 24.8.0
    hooks: [{ id: black }]
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v4.0.0-alpha.8
    hooks: [{ id: prettier }]

  - repo: local
    hooks:
      - id: mypy
        name: mypy
        entry: mypy
        language: system
        types: [python]
```

---

## 🗂️ .editorconfig (Reference)

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.py]
indent_style = space
indent_size = 4
max_line_length = 100

[*.{js,ts,jsx,tsx,css,scss}]
indent_style = space
indent_size = 2
max_line_length = 100
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                  |
| :---------------------- | :---------------------------------------------- |
| **Documentation-first** | Docstrings, module READMEs, ADRs before merge   |
| **Reproducibility**     | Pinned deps, containers, Make idempotence       |
| **Open Standards**      | STAC, GeoJSON, COG, CSV/JSON, JSON Schema       |
| **Provenance**          | Logs + checksums + provenance templates         |
| **Auditability**        | pre-commit, CodeQL, Trivy, CI gates, PR reviews |

---

## 🔗 Related Documentation

| File                             | Description                                |
| :------------------------------- | :----------------------------------------- |
| `docs/standards/data-formats.md` | File/format rules (GeoJSON, COG, CSV/JSON) |
| `docs/standards/metadata.md`     | STAC + JSON Schema conventions             |
| `docs/architecture/ci-cd.md`     | CI/CD workflows and gates                  |
| `.pre-commit-config.yaml`        | Local quality automation                   |
| `.github/workflows/codeql.yml`   | Static analysis setup                      |
| `.github/workflows/trivy.yml`    | Vulnerability scanning pipeline            |

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                                        |
| :-----: | :--------- | :--------------------- | :------------------------------------------------------------- |
|   v1.0  | 2025-10-04 | KFM Documentation Team | Initial coding standards (MCP compliant)                       |
|   v1.1  | 2025-10-05 | KFM Engineering        | Added TS, containers, a11y/security, mypy strictness, examples |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Line Documented. Every Function Proven.”*
📍 [`docs/standards/coding.md`](.) · Official code & style standards for reproducible development in KFM.

</div>
