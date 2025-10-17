<div align="center">

# 💻 Kansas Frontier Matrix — **Coding Standards & Style Guide**
`docs/standards/coding.md`

**Master Coder Protocol (MCP-DL v6.3+) · Reproducibility · Security · Provenance · Validation**

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/)
[![Docs Validated](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/docs-validate.yml?label=Docs%20Validated&color=blue)](../../.github/workflows/docs-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL&logo=github)](../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy&logo=security)](../../.github/workflows/trivy.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate&color=green)](../../.github/workflows/stac-validate.yml)
[![Security: SLSA-3 (target)](https://img.shields.io/badge/Security-SLSA--3%20(target)-orange)](../standards/security.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Coding Standards & Style Guide"
version: "v1.3.0"
last_updated: "2025-10-17"
owners: ["@kfm-architecture","@kfm-docs","@kfm-security"]
tags: ["standards","coding","style","security","validation","mcp","docs","stac"]
status: "Stable"
scope: "Monorepo-Wide"
license: "MIT"
semver_policy: "MAJOR.MINOR.PATCH"
audit_framework: "MCP-DL v6.3"
ci_required_checks:
  - docs-validate
  - codeql
  - trivy
  - stac-validate
  - pre-commit
semantic_alignment:
  - STAC 1.0
  - DCAT 2.0
  - JSON Schema
  - ISO 8601
  - CIDOC CRM
  - OWL-Time
  - SLSA Level 3 (target)
---
````

---

## 📚 Overview

The **KFM Coding Standards** ensure code across **ETL/AI (Python)**, **Web (React/TS/MapLibre)**, and **CI/CD (YAML)** is:

* 🔁 **Reproducible** — deterministic, pinned, containerized, idempotent.
* 🧾 **Auditable** — documented, typed, linted, tested, validated in CI.
* 🌍 **Open-standard** — GeoJSON, COG, CSV/JSON, STAC, JSON Schema.
* 🔗 **Provenanced** — checksums, logs, STAC lineage, signed releases.
* 🛡️ **Secure-by-default** — CodeQL, Trivy, OIDC, least privilege, no plaintext secrets.

**Applies to**

* `src/` (Python ETL/AI/graph/pipelines) · `web/` (React/MapLibre JS/TS) · `.github/workflows/` (Actions)
* `Makefile`, `Dockerfile*`, infra configs · docs build scripts · dataset tooling

---

## 🧭 Compliance Snapshot

| Category       | Policy                               | Status     | Evidence                                |
| :------------- | :----------------------------------- | :--------- | :-------------------------------------- |
| Documentation  | MCP-DL front-matter + module READMEs | ✅          | `docs-validate.yml`                     |
| Lint/Format    | Black/Ruff · ESLint/Prettier         | ✅          | `.pre-commit-config.yaml`               |
| Types          | mypy strict · TS strict              | ✅          | `mypy.ini` · `tsconfig.json`            |
| Security       | CodeQL · Trivy · SBOM                | ✅          | `codeql.yml` · `trivy.yml`              |
| Provenance     | Checksums · STAC lineage             | ✅          | `data/work/checksums.*` · `data/stac/*` |
| Signing (SLSA) | Sigstore/Cosign                      | ⚠️ Planned | `provenance.yml` (planned)              |

---

## 🧩 Core Coding Principles (MCP-Aligned)

| Principle               | Description                | Implementation                               |
| :---------------------- | :------------------------- | :------------------------------------------- |
| **Documentation-first** | Design & doc before code   | Module `README.md`, ADRs, docstrings         |
| **Reproducibility**     | Same inputs ⇒ same outputs | Pinned deps, containers, Make idempotence    |
| **Open Standards**      | Prefer open formats        | GeoJSON, COG, CSV/JSON, STAC, JSON Schema    |
| **Provenance**          | Log lineage & decisions    | checksums + STAC + pipeline logs             |
| **Auditability**        | Machine checks in CI       | pre-commit, CodeQL, Trivy, schema validation |

---

## 🐍 Python Standards

### Style & Structure

* PEP-8, line length **100**, 4-space indent; **no tabs**.
* Imports ordered: stdlib → third-party → local (with blank-line groups).
* **Type hints** on all public APIs; prefer **pure functions** and small, single-responsibility modules.
* Avoid global state; pass config/IO explicitly; deterministic RNG seeds.

```python
from pathlib import Path
from typing import Final

import geopandas as gpd

DEFAULT_CRS: Final[int] = 4326

def process_terrain(input_file: Path, output_dir: Path) -> Path:
    """Reproject and persist in a standard format (COG/GeoJSON)."""
    gdf = gpd.read_file(input_file).to_crs(epsg=DEFAULT_CRS)
    output = output_dir / "processed_terrain.geojson"
    gdf.to_file(output, driver="GeoJSON")
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

* **Docstrings** (PEP-257) mandatory for modules, public classes/functions (Google or reST style).
* Each subpackage ships a **README.md** with purpose, usage, and short runnable example.
* ADRs (Architecture Decision Records) for significant changes: `docs/adr/ADR-YYYYMMDD-<slug>.md`.

### Linting, Types & Formatting

| Tool           | Purpose             | Config                                          |
| :------------- | :------------------ | :---------------------------------------------- |
| **Black**      | Auto-format         | Line length 100                                 |
| **Ruff**       | Lint + import rules | `.ruff.toml` (flake8/pycodestyle/pyupgrade)     |
| **isort**      | Import ordering     | via Ruff or `.isort.cfg`                        |
| **mypy**       | Static typing       | `mypy.ini` (strict in `src/`, relaxed in tests) |
| **pre-commit** | Local checks        | `.pre-commit-config.yaml`                       |

`mypy.ini` (strict baseline)

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

* Use **`logging`** (no `print`) with structured context; lib default `WARNING`, apps `INFO`.
* Never swallow exceptions; wrap into domain exceptions if needed and **re-raise**.
* Log **identifiers** (dataset id, file path, record id) to enable lineage tracing.

```python
import logging
logger = logging.getLogger(__name__)
try:
    ...
except Exception as exc:  # noqa: BLE001
    logger.exception("terrain.process_failed file=%s", input_file)
    raise
```

### Config & Secrets

* Use env-vars + `pydantic-settings` (or dotenv) for config; **no secrets in code/logs**.
* One settings module per service; support `ENV` overrides; document defaults and overrides.

---

## 🌐 JavaScript / TypeScript (Web)

### Frameworks & Architecture

* React 18+, **MapLibre GL JS**, D3/Turf as needed. Prefer **TypeScript** (strict).
* Use **functional components** + hooks; avoid classes; isolate side-effects in hooks/services.
* Break down UI with container/presentational components; memoize expensive renders.

```ts
export function addTerrainLayer(map: maplibregl.Map, id: string, tiles: string[]) {
  map.addSource(id, { type: "raster", tiles, tileSize: 256 });
  map.addLayer({ id, type: "raster", source: id, paint: { "raster-opacity": 0.85 } });
}
```

### Style & Tooling

| Tool           | Purpose            | Config                   |
| :------------- | :----------------- | :----------------------- |
| **ESLint**     | Lint (TS/JS/React) | `.eslintrc.json`         |
| **Prettier**   | Formatting         | `.prettierrc`            |
| **TypeScript** | Types              | `tsconfig.json` (strict) |
| **Vite**       | Bundling           | `vite.config.ts`         |

* Indentation **2 spaces**, max line **100**; `const`/`let` only.
* **Accessibility:** ARIA roles/labels, keyboard nav, color-contrast tokens; run **axe** checks in CI.
* **Security:** Avoid `innerHTML`; sanitize untrusted input; CSP/security headers at serving layer.

### i18n / l10n

* Use message catalogs; no hard-coded strings in components.
* RTL readiness where feasible; date/number formatting via Intl APIs.

---

## ⚙️ YAML / GitHub Actions

* YAML 1.2, avoid anchors for readability; document each workflow with a brief header comment.
* Workflow names explicit: `Validate STAC`, `Docs Validate`, `Security Scan`, `Release`.
* Use matrices prudently; limit triggers with `paths`/`paths-ignore` to reduce CI noise.

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

| Target                       | Purpose                   |
| :--------------------------- | :------------------------ |
| `make all`                   | Run top-level pipelines   |
| `make terrain/hydrology/...` | Domain ETL                |
| `make checksums`             | Generate/verify SHA-256   |
| `make stac-validate`         | Validate STAC/JSON Schema |
| `make site`                  | Build + deploy docs/site  |
| `make clean-*`               | Remove temp/cache         |

**Rules**

* Idempotent; safe to re-run.
* Log to `data/work/logs/` with timestamps.
* Exit non-zero on failures; concise errors.

---

## 🐳 Containers & Repro Environments

* Minimal pinned images (e.g. `python:3.11-slim`); multi-stage builds to keep runtime small.
* Rootless runtime; drop caps; read-only FS; mount only required volumes.
* Generate **SBOM** (Syft/CycloneDX) in CI; scan images with Trivy.

---

## 🛡️ Security & Governance

| Policy                     | Enforcement                                                            |
| :------------------------- | :--------------------------------------------------------------------- |
| **Commit verification**    | GPG or GitHub Verified                                                 |
| **Dependencies**           | Locked (`requirements*.txt`, `poetry.lock`, `package-lock.json`)       |
| **Static analysis**        | CodeQL (Python/JS/TS)                                                  |
| **Vulnerability scanning** | Trivy for deps/images                                                  |
| **Secrets**                | OIDC, GH Secrets; never plaintext                                      |
| **Access control**         | Least privilege; PRs require review; branch protection required checks |

**AI-Assist Guardrails**

* AI-generated code must pass lint, types, tests; authorship noted in PR description.
* No sensitive prompts or secrets in repo/CI logs.

---

## 🧪 Testing Standards

* **Unit** for pure logic; **integration** for I/O & data flows; **contract** tests for APIs.
* Coverage goals (guidelines): **≥70% unit** overall; smoke coverage for pipelines.
* Fixtures under `tests/fixtures/`; deterministic seeds; temp dirs; cleanup artifacts.
* Web: component tests (RTL), accessibility checks (axe), basic e2e for critical flows.

```bash
pytest -q --maxfail=1 --disable-warnings
```

---

## 🗃️ Data, STAC & Schemas (Code-Adjacent)

* Validate **STAC Items/Collections** in CI; ensure `datetime`/`temporal` ISO-8601; bbox CRS WGS84.
* Provide JSON Schema for custom configs; include `$schema` and version fields.
* Dataset provenance template (add): `docs/standards/provenance_dataset.md`.

---

## 🧾 Version Control Practices

| Rule                     | Description                                                      |
| :----------------------- | :--------------------------------------------------------------- |
| **Conventional Commits** | `feat:`, `fix:`, `docs:`, `data:`, `ci:`, `refactor:`, `chore:`  |
| **Branch naming**        | `feature/add-stac-validation`, `fix/terrain-proj-bug`            |
| **PR requirements**      | Link issue/ADR; screenshots for UI; attach logs for data changes |
| **Tags**                 | `vX.Y.Z` semver; changelog required                              |
| **Reviews**              | ≥1 approval; CI green; large PRs include design note/ADR         |

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

[*.{js,ts,jsx,tsx,css,scss,json,yml,yaml}]
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
| **Provenance**          | Logs + checksums + STAC lineage + templates     |
| **Auditability**        | pre-commit, CodeQL, Trivy, CI gates, PR reviews |

---

## 🔗 Related Documentation

| File                                  | Description                                 |
| :------------------------------------ | :------------------------------------------ |
| `docs/standards/metadata.md`          | STAC + JSON Schema conventions              |
| `docs/standards/security.md`          | Security posture & SLSA policy              |
| `docs/standards/data-formats.md`      | File/format rules (GeoJSON, COG, CSV/JSON)  |
| `docs/audit/repository_compliance.md` | Audit (RMI/DCI), governance plan, sign-offs |
| `.pre-commit-config.yaml`             | Local quality automation                    |
| `.github/workflows/*`                 | CI/CD pipelines (CodeQL/Trivy/Docs/STAC)    |

---

## 📅 Version History

| Version | Date       | Author            | Summary                                                                                                                           |
| :------ | :--------- | :---------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| v1.3.0  | 2025-10-17 | @kfm-architecture | Added YAML front-matter, compliance snapshot, SLSA policy, i18n/a11y, AI guardrails, data/STAC section; aligned with audit report |
| v1.2.0  | 2025-10-05 | @kfm-engineering  | Added TS strict, containers, testing & security expansions                                                                        |
| v1.0.0  | 2025-10-04 | @kfm-docs         | Initial MCP-aligned coding standards                                                                                              |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Line Documented. Every Function Proven.”*
📍 `docs/standards/coding.md` — Official code & style standards for reproducible development in KFM.

</div>
