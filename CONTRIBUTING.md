---
title: "🤝 Kansas Frontier Matrix — Contribution Guidelines (MCP-DL v6.3 / Platinum README v7.1)"
path: "CONTRIBUTING.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
sbom_ref: "releases/v9.7.0/sbom.spdx.json"
manifest_ref: "releases/v9.7.0/manifest.zip"
license_ref: "LICENSE"
---

<div align="center">

# 🤝 **Kansas Frontier Matrix — Contribution Guidelines**
`CONTRIBUTING.md`

**Purpose:** Provide a reproducible, documentation-first framework for contributing to the Kansas Frontier Matrix (KFM) project.  
All contributions must align with the **Master Coder Protocol (MCP v6.3)**, **FAIR+CARE** standards, and the **Diamond⁹ Ω / Crown∞Ω** certification criteria.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](docs/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](docs/standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📜 Guiding Principles

1. **Documentation-First:** Every change, feature, or dataset addition must include updated or new documentation (README, schema, or manifest) as part of the same commit.
2. **Reproducibility:** Contributions must include enough context (commands, parameters, dataset URLs, or workflow steps) for others to replicate results exactly.
3. **Open Standards:** Use open, machine-readable formats (Markdown, JSON, YAML, GeoJSON, CSV). Avoid proprietary file types.
4. **FAIR+CARE Compliance:** Ensure all data and methods are Findable, Accessible, Interoperable, Reusable, and ethically governed.
5. **Transparency:** Use explicit versioning, changelogs, and provenance. Every dataset or feature must declare its source and license.
6. **Validation:** CI/CD workflows validate code, data, and documentation automatically. No change merges without passing checks.

---

## 🧱 Repository Structure

All contributions must follow the existing **monorepo layout** for maintainability and provenance tracking:

```
KansasFrontierMatrix/
├── src/             # Code (AI, pipelines, APIs)
├── web/             # Web app (React + MapLibre)
├── data/            # Datasets and metadata
├── docs/            # Documentation and templates
├── tools/           # Utility scripts
├── tests/           # Validation suites
├── .github/         # CI/CD workflows and issue templates
├── Makefile         # Automation and orchestration
└── CONTRIBUTING.md  # This file
```

When adding files, ensure the correct placement and naming conventions (e.g., lowercase with underscores, meaningful prefixes, no spaces).

---

## 🪶 How to Contribute

### 1. Fork and Clone the Repository

```bash
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix
git checkout -b feature/<short-description>
```

Name your branch with a **clear, lowercase prefix**:
- `feature/` for new features  
- `fix/` for bug fixes  
- `docs/` for documentation updates  
- `data/` for dataset additions  
- `test/` for validation scripts

---

### 2. Prepare Your Contribution

#### 🧾 Code Contributions
- Follow **PEP 8** for Python and **ESLint** for JavaScript/TypeScript.
- Each new module must include:
  - A `README.md` describing its purpose and usage.
  - Logging that supports MCP audit trails.
  - Inline docstrings for all functions and classes.
- Test your code locally:
  ```bash
  make test
  ```
  or run targeted tests from the `tests/` directory.

#### 🗺 Data Contributions
- Add a manifest file to `data/sources/` using the JSON format below:

```json
{
  "id": "usgs_soils_1937",
  "title": "Historic Soil Survey Map (1937)",
  "description": "Digitized soil survey layer for western Kansas.",
  "type": "raster",
  "spatial": [-102.05, 37.0, -94.6, 40.0],
  "temporal": {"start": "1937-01-01", "end": "1937-12-31"},
  "license": "Public Domain",
  "provenance": "USGS Historical Map Archive",
  "checksum": "sha256-<hash>",
  "updated": "2025-11-05"
}
```

- For raster data, produce a **Cloud-Optimized GeoTIFF (COG)** in WGS84 (EPSG:4326).  
- For vector data, convert to **GeoJSON**.
- Validate with:
  ```bash
  make validate
  ```

#### 🧠 AI / Model Contributions
- Document all experiments using `docs/templates/model_card.md`.  
- Include:
  - Training dataset reference
  - Hyperparameters
  - Performance metrics
  - Ethical considerations
- Store outputs in `src/ai/models/<model_name>/`.

---

### 3. Documentation Updates

Every contribution must include clear documentation.  
Depending on scope:

| Type | Where to Document | Example |
|------|--------------------|----------|
| New pipeline | `src/pipelines/<name>/README.md` | “ETL Workflow for NOAA Climate Data” |
| New dataset | `data/sources/<dataset>.json` | “NOAA Kansas Temperature Normals” |
| Feature/UI | `web/src/components/<feature>/README.md` | “Timeline Animation Component” |
| AI model | `src/ai/models/<model>/README.md` | “Focus Transformer v1” |

All docs must follow **`docs/standards/markdown_rules.md`** for structure, titles, and badges.

---

### 4. Run Local Validation

Before submitting, ensure your contribution passes:

```bash
make lint
make validate
make test
```

These commands will:
- Lint code (Python/JS)
- Validate STAC/DCAT metadata
- Run FAIR+CARE compliance checks
- Execute test suites

If all succeed, commit your changes:

```bash
git add .
git commit -m "feature: added historical flood dataset (validated STAC/DCAT)"
git push origin feature/historical-flood-layer
```

---

### 5. Submit a Pull Request

Open a PR via GitHub. Each PR should include:
- A **summary of changes** (what/why/how)
- Updated READMEs or dataset manifests
- Reference to related issues (e.g., “Closes #42”)
- CI passing badge (automatically verified)

PRs trigger automated checks:
- STAC/DCAT schema validation
- FAIR+CARE audit
- CodeQL and Trivy security scans
- STAC-validate and Docs-lint workflows

No merge occurs until **all checks pass**.

---

## 🧩 Issue & Template System

All new issues and PRs use structured YAML-based templates in `.github/ISSUE_TEMPLATE/`.

**Examples:**
- `data_submission.yml` — for new datasets  
- `feature_request.yml` — for feature ideas  
- `bug_report.yml` — for errors or inconsistencies  

Each template enforces the inclusion of metadata like dataset provenance, expected outcomes, and FAIR+CARE implications.

---

## 🔒 Governance and Ethics

All contributors must agree to uphold:
- **Open Data Ethics:** Respect data ownership, Indigenous sovereignty, and attribution.  
- **No Proprietary Data:** Only submit data that is public domain or CC-licensed.  
- **Cultural Sensitivity:** Clearly flag datasets involving Indigenous lands, treaties, or cultural materials with CARE annotations.  
- **Transparency:** All contributions are publicly logged with versioning, authorship, and provenance.  

Violations of data ethics or licensing terms will result in immediate retraction of content and contributor suspension per the **KFM Governance Charter**.

---

## 🧾 Commit Conventions

Follow the **Conventional Commits** format:

| Type | Example | Purpose |
|------|----------|----------|
| `feat:` | `feat: add historic tornado layer` | New feature |
| `fix:` | `fix: resolve timeline scroll bug` | Bug fix |
| `docs:` | `docs: update architecture diagrams` | Documentation change |
| `data:` | `data: integrate NOAA precipitation set` | Dataset addition |
| `test:` | `test: add API schema validation` | New test coverage |
| `refactor:` | `refactor: optimize ETL pipeline` | Non-breaking code improvement |

Use semantic prefixes and write concise, descriptive messages.

---

## 🧮 Validation & CI/CD Workflows

CI workflows automatically validate every contribution:

| Workflow | Purpose |
|-----------|----------|
| `stac-validate.yml` | Verifies STAC 1.0.0 JSON schema compliance |
| `faircare-validate.yml` | Audits FAIR+CARE principles |
| `docs-lint.yml` | Enforces Markdown and formatting standards |
| `codeql.yml` | Performs security scanning |
| `trivy.yml` | Detects vulnerabilities in dependencies |
| `build-and-deploy.yml` | Builds frontend and deploys static site (MapLibre) |

Check workflow results in your PR before merging.

---

## 🧭 Support and Questions

Need help?
- 📘 **Documentation:** [docs/README.md](docs/README.md)  
- 🗺️ **Data Sources:** [data/sources/README.md](data/sources/README.md)  
- 💬 **Discussions:** Use [GitHub Discussions](https://github.com/bartytime4life/Kansas-Frontier-Matrix/discussions)  
- 🧩 **Governance:** [ROOT-GOVERNANCE.md](docs/standards/governance/ROOT-GOVERNANCE.md)

---

<div align="center">

**© 2025 Kansas Frontier Matrix**  
Contributions licensed under **MIT** (code) and **CC-BY 4.0** (docs/data).  
Built under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

</div>
