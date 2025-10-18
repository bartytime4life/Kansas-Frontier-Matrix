<div align="center">

# 💻 Kansas Frontier Matrix — **Coding Standards & Style Guide**  
`docs/standards/coding.md`

**Master Coder Protocol (MCP-DL v6.3+) · Reproducibility · Security · Provenance · Validation**

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/)
[![Docs Validated](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/docs-validate.yml?label=Docs%20Validated&color=blue)](../../.github/workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../.github/workflows/policy-check.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate&color=green)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL&logo=github)](../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy&logo=security)](../../.github/workflows/trivy.yml)
[![Gitleaks](https://img.shields.io/badge/Secrets-Gitleaks-red)](../../.github/workflows/gitleaks.yml)
[![Security: SLSA-3 (Target)](https://img.shields.io/badge/Security-SLSA--3%20(Target)-orange)](../standards/security.md)
[![SBOM](https://img.shields.io/badge/SBOM-Syft%20%7C%20SPDX-green)](../../.github/workflows/sbom.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Coding Standards & Style Guide"
version: "v1.5.0"
last_updated: "2025-10-18"
owners: ["@kfm-architecture","@kfm-security","@kfm-data","@kfm-docs","@kfm-ai","@kfm-web"]
tags: ["coding","style","security","governance","ci","mcp","stac","reproducibility","ai","containers","web","python","typescript"]
status: "Stable"
scope: "Monorepo-Wide"
license: "MIT"
semver_policy: "MAJOR.MINOR.PATCH"
audit_framework: "MCP-DL v6.3"
ci_required_checks:
  - docs-validate
  - policy-check
  - stac-validate
  - checksums
  - codeql
  - trivy
  - gitleaks
  - pre-commit
semantic_alignment:
  - STAC 1.0
  - DCAT 2.0
  - CIDOC CRM
  - OWL-Time
  - JSON Schema
  - ISO 8601 / EPSG
  - GeoSPARQL
  - FAIR Principles
  - SLSA Level 3 (target)
---
```

---

## 📚 Overview

The **KFM Coding Standards** extend the **Master Coder Protocol (MCP)** to ensure every line of code
— from **AI pipelines** to **web visualization** — adheres to **reproducibility, provenance, security, and open governance**.

### Key Objectives

- 🔁 **Reproducibility** — deterministic, pinned builds across environments and systems.  
- 📘 **Documentation-first** — code and docs co-evolve with consistent version metadata.  
- 🧾 **Auditability** — automated pre-commit checks, typed code, logged provenance.  
- 🔗 **Provenance** — STAC lineage, checksum integrity, container SBOMs, PROV-O.  
- 🛡️ **Security** — enforced via Trivy, CodeQL, Gitleaks, OPA policy gates, and SLSA.  
- 🌍 **Open Standards** — GeoJSON, COG, CSV, STAC, JSON Schema, CIDOC CRM, DCAT.

---

## 🧩 Alignment Across the Project Stack

```mermaid
flowchart TD
  A["📦 src/ (ETL · AI · Graph · API)"] --> B["🐍 Python · Pipelines · NLP"]
  A --> C["🧠 AI/ML Models · spaCy · Transformers"]
  A --> D["🕸️ web/ (Frontend)"]
  D --> E["React · TypeScript · MapLibre · D3"]
  A --> F["🧾 docs/standards/ (Governance)"]
  F --> G["markdown_rules.md · markdown_guide.md · coding.md"]
  A --> H["🧰 .github/workflows/"]
  H --> I["docs-validate.yml · policy-check.yml · stac-validate.yml · codeql.yml · trivy.yml · gitleaks.yml"]
  A --> K["🧱 data/stac/ + metadata"]
  K --> L["STAC lineage · JSON Schema · FAIR mapping · CIDOC CRM"]
%% END OF MERMAID
```

---

## 🧭 MCP-DL Compliance Integration

| Domain           | Standard                         | Enforcement Mechanism   | Validation                   |
| :--------------- | :------------------------------- | :---------------------- | :--------------------------- |
| **Docs**         | Markdown + MCP-DL front-matter   | Pre-commit + CI + OPA   | ✅ `docs-validate.yml`        |
| **Data**         | STAC 1.0 + DCAT 2.0              | Schema & policy gates   | ✅ `stac-validate.yml`        |
| **AI Models**    | Documented model cards           | JSON/Schema checks      | ✅ `model_card.md`            |
| **Code Quality** | Black · Ruff · ESLint · Prettier | Pre-commit · CI         | ✅ `.pre-commit-config.yaml`  |
| **Security**     | CodeQL + Trivy + Gitleaks        | CI pipelines            | ✅ `codeql.yml` · `trivy.yml` |
| **Provenance**   | Checksums + STAC lineage + PROV  | Automated checks        | ✅ `make checksums`           |
| **Versioning**   | SemVer + Git tags                | Release workflow        | ✅ `release.yml`              |

---

## 🧠 AI/ML Coding Standards (`src/ai/`, `src/nlp/`, `src/enrich/`)

### Model Development

- Every model **must** have a card at `docs/templates/model_card.md` (purpose, data, metrics, bias/ethics).
- Pin model & data versions; keep `requirements-ml.txt` minimal and locked.
- Save model artifacts with **SHA-256**; include `train_manifest.json` (hashes, seed, commit, container digest, env).
- Prefer small, explicit pipeline steps; isolate feature engineering from model code.

### Reproducible Training

| Component   | Requirement                              | Validation                     |
| :---------- | :--------------------------------------- | :----------------------------- |
| Environment | Docker + `requirements-ml.txt`           | ✅ Container digest + SBOM      |
| Dataset     | Logged in STAC lineage                   | ✅ STAC validator               |
| Seed        | Fixed random seed                        | ✅ Reproducible metrics         |
| Evaluation  | Deterministic metrics (F1/PR/AUC/MAE)    | ✅ CI metrics export            |
| Bias Check  | Geography/time stratification            | ✅ Benchmark gates in CI        |

### Example (Training Workflow)

```bash
make train-nlp model=BART run_id=2025Q4
python src/ai/train.py --model bart --epochs 5 --seed 42 --save-path data/models/
make validate-nlp MODEL_ID=MODEL-2025-001-CLIMATE
```

---

## 🐍 Python Standards

### Structure & Style

- **PEP 8 + Ruff + Black**; line length ≤ 100; 4-space indent; `__all__` exported for libs.  
- **Type hints required**; `mypy --strict` on CI.  
- Favor **pure functions** and small modules; avoid side-effects; dependency injection for I/O.  
- Package layout: `src/<area>/__init__.py`, tests mirror `src/` paths under `tests/`.

### Imports, Errors, Logging

```python
from __future__ import annotations
from pathlib import Path
from typing import Final
import geopandas as gpd
import logging

DEFAULT_CRS: Final[int] = 4326
logger = logging.getLogger(__name__)

def process_layer(input_file: Path, output_dir: Path) -> Path:
    """Reproject layer and persist as GeoJSON (EPSG:4326)."""
    gdf = gpd.read_file(input_file).to_crs(epsg=DEFAULT_CRS)
    output = output_dir / f"{input_file.stem}_processed.geojson"
    gdf.to_file(output, driver="GeoJSON")
    logger.info("Processed layer=%s output=%s", input_file, output)
    return output
```

- Use `logging` (not prints).  
- Exceptions: raise concrete errors with context; never swallow; include remediation in message.  
- Paths: use `pathlib.Path`; no hard-coded absolute paths.

---

## 🌐 Web Standards (React + TypeScript + MapLibre)

### TypeScript & Structure

- **TS strict** (`"strict": true`); ESLint + Prettier; absolute imports via tsconfig paths.  
- Atomic Design: **atoms → molecules → organisms → templates → pages**.  
- Storybook or MDX for component docs; accessibility annotations included.

### Map & Timeline Integration

- Layer configs load from STAC/manifest; avoid hard-coded dates/URLs.  
- Provenance is always visible in UI (source link, license, STAC ID).  
- Timeline selection pushes URL state for deep-linking/reproducibility.

### Performance & Accessibility

- Memoize heavy components; virtualize long lists; lazy-load tiles.  
- **WCAG 2.1 AA**: keyboard-only flows, focus-visible, ARIA roles; respect `prefers-reduced-motion`.  
- Internationalization-ready: avoid text literals in logic.

---

## ⚙️ Infrastructure Standards (Make · YAML · Docker)

### Makefiles

- Provide `help` target; targets are **idempotent** and **atomic**.  
- Log start/stop timestamps and output hashes to `_reports/` or `data/work/logs/`.

### YAML & Workflows

- Pin actions by tag or SHA; set minimal **OIDC** permissions; use `concurrency` and caches.  
- Policy gates (OPA/Conftest) enforce required fields in docs/STAC and reject plaintext secrets.

### Docker

| Layer               | Rule                             | Implementation     |
| :------------------ | :------------------------------- | :----------------- |
| **Build**           | Pinned base (`python:3.11-slim`) | Multi-stage builds |
| **Run**             | Non-root user; read-only FS      | ENTRYPOINT scripts |
| **Security**        | Trivy + Syft (SBOM)              | `make scan` target |
| **Reproducibility** | Immutable tags; no `latest`      | Pinned SHA digests |

```Dockerfile
FROM python:3.11-slim AS build
RUN pip install --no-cache-dir poetry==1.8.3
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt -o /tmp/reqs.txt
RUN pip install --no-cache-dir -r /tmp/reqs.txt
```

---

## 🧾 Provenance & Metadata Practices

- Every artifact in `data/processed/` **must** include: STAC Item/Collection, license, citation, **SHA-256**.  
- ETL and model jobs write provenance to `data/work/logs/` (script + args + input/output hashes).  
- For large objects: track with **DVC/LFS** pointers and keep sidecar checksums.

**Example provenance JSON**

```json
{
  "source": "NOAA NCEI",
  "script": "src/pipelines/weather_pipeline.py",
  "hash": "sha256:abc123...",
  "datetime": "2025-10-18T22:34:00Z",
  "outputs": ["data/processed/weather_2025.geojson"]
}
```

---

## 🧪 Testing & Validation Matrix

| Category          | Target Coverage        | Tool              | Status |
| :---------------- | :--------------------- | :---------------- | :----- |
| Unit Tests        | ≥ 70%                  | pytest/jest       | ✅      |
| Integration Tests | Critical pipelines/API | pytest + fixtures | ✅      |
| Contract Tests    | APIs (FastAPI)         | Schemathesis      | ✅      |
| E2E (Web)         | Timeline ↔ Map linking | Playwright        | ✅      |
| STAC Validation   | All datasets           | stac-validator    | ✅      |
| Provenance Logs   | All outputs            | checksum verifier | ✅      |

> Add **golden tests** for deterministic snapshots (e.g., PNG exports, JSON catalogs).

---

## 🔐 Security & Secrets Hygiene

- **Never** commit secrets; use OIDC and GitHub Secrets for short-lived tokens.  
- Gitleaks runs on PRs; CI fails on exposure.  
- Enable Dependabot/Renovate; group updates weekly; run smoke tests on bump PRs.  
- Enforce **CSP/Trusted Types** in web where applicable.

---

## 🧠 MCP Compliance Summary

| Principle               | Implementation                             |
| :---------------------- | :----------------------------------------- |
| **Documentation-first** | ADRs + module READMEs + docstrings         |
| **Reproducibility**     | Containers + pinned deps + Make            |
| **Open Standards**      | STAC, GeoJSON, DCAT, CIDOC CRM, OWL-Time   |
| **Provenance**          | Checksums + STAC lineage + PROV-O          |
| **Auditability**        | CodeQL + Trivy + Gitleaks + CI gates        |

---

## 🔗 Cross-References

| File                                   | Description                              |
| :------------------------------------- | :--------------------------------------- |
| `docs/standards/security.md`           | SLSA + CodeQL + Trivy + secrets policies |
| `docs/audit/repository_compliance.md`  | Repository audit + RMI/DCI metrics       |
| `docs/standards/markdown_rules.md`     | Markdown formatting & visual style       |
| `docs/templates/model_card.md`         | AI model documentation template          |
| `docs/templates/experiment.md`         | Reproducible experiment template         |
| `data/stac/catalog.json`               | Core dataset catalog (validated nightly) |

---

## 📅 Version History

| Version | Date       | Author            | Summary                                                                                                             |
| :------ | :--------- | :---------------- | :------------------------------------------------------------------------------------------------------------------ |
| **v1.5.0** | 2025-10-18 | @kfm-architecture | Added policy gates, secrets scanning, AI/ML & web specifics, Docker hardening, golden tests, and SBOM references. |
| **v1.4.0** | 2025-10-18 | @kfm-architecture | AI/ML + Docker + STAC + testing matrix; integrated FAIR, provenance, audit refs                                    |
| **v1.3.0** | 2025-10-17 | @kfm-docs         | YAML metadata, CI snapshots, and security section                                                                   |
| **v1.2.0** | 2025-10-05 | @kfm-engineering  | TS strict, accessibility, i18n, containers, coverage goals                                                          |
| **v1.0.0** | 2025-10-04 | @kfm-team         | Initial MCP-compliant coding standards baseline                                                                     |

---

<div align="center">

**Kansas Frontier Matrix © 2025**  
💡 *Every Line Documented · Every Function Proven · Every Result Reproducible*  
📍 `docs/standards/coding.md` — Official MCP-DL v6.3 Coding & Style Standard for the Frontier Matrix Project.

</div>