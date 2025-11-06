---
title: "🤝 Kansas Frontier Matrix — Contribution Guidelines (MCP-DL v6.3 · Platinum README v7.1)"
path: "CONTRIBUTING.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v9.7.0/sbom.spdx.json"
manifest_ref: "releases/v9.7.0/manifest.zip"
telemetry_ref: "releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-contributing-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🤝 **Kansas Frontier Matrix — Contribution Guidelines**
`CONTRIBUTING.md`

**Purpose:** Define a **documentation-first**, **FAIR+CARE-aligned** process for contributing code, data, and documentation to the Kansas Frontier Matrix (KFM).  
All contributions are validated by CI/CD and logged in governance ledgers to ensure **reproducibility**, **traceability**, and **ethical compliance**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](docs/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](docs/standards/faircare.md)
[![Status: Active](https://img.shields.io/badge/Status-Automated-success)]()

</div>

---

## 📘 Overview

KFM operates as a **single MCP-governed monorepo**. All changes must be:  
- Documented (YAML front-matter + README updates)  
- Validated (schema, FAIR+CARE, security)  
- Traceable (commit SHA, telemetry, governance ledgers)

---

## 🗂️ Repository Layout

```
KansasFrontierMatrix/
├── src/             # ETL/AI logic, API, graph integration
├── web/             # React + MapLibre application
├── data/            # Raw→processed data & STAC
├── docs/            # Standards, templates, pipelines, reports
├── tools/           # Ingest/validation utilities
├── tests/           # Unit & integration suites
├── .github/         # Workflows & issue templates
├── Makefile         # Orchestration entrypoints
└── CONTRIBUTING.md  # This file
```

---

## 📜 Guiding Principles

1. **Documentation-First:** Ship docs and manifests in the same PR as code/data.  
2. **Reproducibility:** Provide commands, parameters, dataset URLs, and environment notes.  
3. **Open Standards:** Markdown, JSON/YAML, GeoJSON/GeoTIFF, STAC/DCAT, SPDX.  
4. **FAIR+CARE:** Respect open data ethics and Indigenous data sovereignty.  
5. **Transparency:** Use semantic versioning, changelogs, and provenance.  
6. **Validation:** Merges require green CI across docs/data/code/security.

---

## 🪶 Workflow for Contributions

### 1) Create a Topic Branch

```bash
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix
git checkout -b feature/<short-description>
```

**Branch prefixes:** `feature/` · `fix/` · `docs/` · `data/` · `test/`.

---

### 2) Prepare the Change

#### 🧾 Code
- Follow **PEP 8** (Python) and **ESLint**/**Prettier** (JS/TS).  
- Include `README.md` in new modules and **docstrings** for public APIs.  
- Add tests under `tests/` and run:
  ```bash
  make test
  ```

#### 🗺 Data
- Add a **source manifest** in `data/sources/*.json`:

```json
{
  "id": "usgs_soils_1937",
  "title": "Historic Soil Survey Map (1937)",
  "description": "Digitized soil survey layer for western Kansas.",
  "type": "raster",
  "spatial": [-102.05, 37.0, -94.6, 40.0],
  "temporal": { "start": "1937-01-01", "end": "1937-12-31" },
  "license": "Public Domain",
  "provenance": "USGS Historical Map Archive",
  "checksum": "sha256-<hex>",
  "updated": "2025-11-05"
}
```

- Rasters → **COG** (WGS84/EPSG:4326).  
- Vectors → **GeoJSON**.  
- Validate:
  ```bash
  make validate
  ```

#### 🤖 AI / Models
- Document with `docs/templates/model_card.md` (intended use, data, params, metrics, bias/ethics).  
- Place outputs in `src/ai/models/<model_name>/`.

---

## ✏️ Documentation Requirements

| Change Type | Doc Location | Example |
|-------------|--------------|---------|
| New pipeline | `src/pipelines/<name>/README.md` | ETL for NOAA climate |
| New dataset | `data/sources/<id>.json` | `noaa_storms_1950_2025.json` |
| Feature/UI  | `web/src/components/<feature>/README.md` | Timeline animation |
| AI model     | `src/ai/models/<model>/README.md` | Focus Transformer v1 |

**All docs** must follow `docs/standards/markdown_rules.md` and include YAML front-matter, badges, TOC (when long), and version history.

---

## 🧪 Local Validation Before PR

```bash
make lint       # docs + code format checks
make validate   # STAC/DCAT + FAIR+CARE + contracts
make test       # unit/integration suites
```

Commit only after all pass:

```bash
git add .
git commit -m "data: add NOAA storms (FAIR+CARE + STAC validated)"
git push origin feature/noaa-storms
```

---

## 🔀 Pull Request Checklist

- Clear **summary** (what/why/how)  
- Updated READMEs / manifests  
- Linked issues (e.g., *Closes #42*)  
- All CI checks passing (badges appear in PR)

**Automated checks include:**
- STAC/DCAT schema validation  
- FAIR+CARE audit  
- Markdown/YAML lint  
- CodeQL & Trivy security scans  
- Build & deploy (preview)

---

## 🧩 Issue Templates

Located in `.github/ISSUE_TEMPLATE/`:

| Template | Use |
|----------|-----|
| `data_submission.yml` | New dataset or STAC Item |
| `feature_request.yaml` | Feature or improvement request |
| `bug_report.yaml` | Reproducible defect report |
| `governance_form.yml` | FAIR+CARE or ethics review |

> Use **“N/A”** instead of “None” in dropdowns to avoid YAML parsing issues.

---

## 🔒 Governance & Ethics

Contributors must uphold:

- **Open Data Ethics:** Respect licensing, attribution, and community ownership.  
- **Indigenous Data Sovereignty:** Apply CARE reviews for cultural datasets.  
- **Transparency:** Public logs for versioning, authorship, and provenance.

Breaches result in retraction and sanction per the **Governance Charter**.

---

## 🧾 Conventional Commits

| Type | Example | Purpose |
|------|---------|---------|
| `feat:` | `feat: add historic tornado layer` | New feature |
| `fix:` | `fix: timeline scroll bug` | Bug fix |
| `docs:` | `docs: update architecture diagrams` | Docs update |
| `data:` | `data: integrate NOAA precipitation set` | Dataset add/update |
| `test:` | `test: add API schema validation` | New tests |
| `refactor:` | `refactor: optimize ETL pipeline` | Non-breaking improvements |

---

## ⚙️ CI/CD Workflows (Workflow → Artifact Map)

| Workflow | Purpose | Primary Artifacts |
|----------|---------|-------------------|
| `stac-validate.yml` | STAC 1.0.0 validation | `reports/self-validation/stac/_summary.json` |
| `faircare-validate.yml` | FAIR+CARE audits & contracts | `reports/fair/faircare_summary.json` |
| `docs-lint.yml` | Markdown/YAML/JSON lint | `reports/self-validation/docs/lint_summary.json` |
| `codeql.yml` | Static code analysis | SARIF reports (`reports/security/codeql/`) |
| `trivy.yml` | Container/dependency scanning | `reports/security/trivy/*.json` |
| `build-and-deploy.yml` | Frontend build/deploy | `docs/reports/telemetry/build_metrics.json` |

---

## 🧭 Support & Questions

- 📘 Docs Index: `docs/README.md`  
- 🗺️ Data: `data/sources/README.md` (if present)  
- 💬 Discussions: GitHub Discussions  
- ⚖️ Governance: `docs/standards/governance/ROOT-GOVERNANCE.md`

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Alignment to MCP-DL v6.3; added workflow→artifact map and telemetry schema. |
| v9.5.0 | 2025-10-20 | A. Barta | Improved FAIR+CARE guidance and dataset manifest example. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Initial contributor guide under MCP. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Documentation Index](docs/README.md) · [Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
