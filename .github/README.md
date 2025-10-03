<div align="center">

# ⚙️ Kansas-Frontier-Matrix — GitHub Automation & Governance (`.github/`)

**Mission:** Centralize all **automation, CI/CD, and governance assets**  
that keep this repository **reproducible, secure, and contributor-friendly**.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)  
[![Trivy Security Scan](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../.github/workflows/pre-commit.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../.github/workflows/automerge.yml)  
[![Docs Check](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/docs.yml/badge.svg)](../.github/workflows/docs.yml)  
[![License](https://img.shields.io/badge/License-MIT%20%2B%20CC--BY-blue)](/LICENSE)  
[![MCP Aligned](https://img.shields.io/badge/Docs-MCP%20Protocol-green)](/docs/)  

</div>

---

## 📚 Contents

- [Overview](#-overview)
- [Workflows](#-workflows)
- [Templates](#-templates)
- [Badges & Status](#-badges--status)
- [MCP Governance](#-mcp-governance)
- [Contributing](#-contributing)

---

## 🚀 Overview

The `.github/` directory contains all **repository-level automation and templates** that ensure  
the **Kansas Frontier Matrix** remains:

- 🧪 **Reproducible** — workflows validate data, STAC catalogs, and experiments [oai_citation:5‡File and Data Architecture for the Kansas Frontier Matrix Project.pdf](file-service://file-3dXLjptkFjdMerKJTvzzW7)  
- 🔐 **Secure** — CodeQL and Trivy scans protect against vulnerabilities [oai_citation:6‡Generate architecture file.pdf](file-service://file-Efds5c6rLayShGSZRCjLBa)  
- 📜 **Documented** — contributions follow MCP (Master Coder Protocol) rules for clarity [oai_citation:7‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
- 🤝 **Contributor-friendly** — PR templates, issue templates, and automerge policies streamline work  

---

## 🔄 Workflows

Located in `.github/workflows/`:

- **`site.yml`** → Build & deploy the static web viewer (React + MapLibreGL).  
- **`stac-validate.yml`** → Validate all STAC Items & Collections for compliance.  
- **`codeql.yml`** → Run GitHub CodeQL static analysis (Python + JS).  
- **`trivy.yml`** → Run container & dependency security scans.  
- **`pre-commit.yml`** → Enforce linting, formatting, schema checks.  
- **`automerge.yml`** → Automerge PRs with passing checks & approvals.  
- **`docs.yml`** → Ensure all documentation builds & passes link checks.  

Each workflow is **version-pinned, containerized, and CI/CD-ready** for full reproducibility [oai_citation:8‡Generate architecture file.pdf](file-service://file-Efds5c6rLayShGSZRCjLBa).  

---

## 📝 Templates

- **Pull Request Template** — prompts contributors to include:
  - ✅ Linked issue(s)  
  - ✅ Source metadata (provenance, license, citation)  
  - ✅ Tests & validation evidence  

- **Issue Templates**  
  - 🐛 **Bug Report** — clear repro steps, environment, screenshots.  
  - 💡 **Feature Request** — structured proposal w/ rationale.  
  - 📊 **Data Addition** — enforce metadata & provenance before merging.  

Templates enforce **MCP documentation-first discipline** [oai_citation:9‡Kansas Frontier Matrix – Monorepo Repository Design.pdf](file-service://file-AyrVktEWfFAidjtGFw9NEH).  

---

## 🏅 Badges & Status

Every workflow publishes **status badges** at the repo level.  
These badges reflect:
- Data pipeline integrity (STAC validation)  
- Build & deploy success  
- Code & container security  
- Documentation health  

If any badge **fails red**, contributions are blocked until resolved.

---

## 📐 MCP Governance

This repo adheres to **Master Coder Protocol (MCP)**:

- **Experiments** logged in `docs/experiment.md` (Problem → Hypothesis → Method → Data → Results).  
- **SOPs** in `docs/sop.md` for reproducible processes.  
- **Model Cards** in `docs/model_card.md` describing AI/ML models used.  
- **Architecture Docs** version-controlled (`docs/architecture.md`, `docs/glossary.md`).  

Every CI/CD workflow embeds **provenance logging**, checksums, and auditability [oai_citation:10‡Kansas Data Resources for Frontier-Matrix Project.pdf](file-service://file-Q9AC5RwLTeV6QgadxHDf5P) [oai_citation:11‡File and Data Architecture for the Kansas Frontier Matrix Project.pdf](file-service://file-3dXLjptkFjdMerKJTvzzW7).  

---

## 🤝 Contributing

Contributions welcome! Please follow:

1. Fork & branch from `main`.  
2. Run `make tests` to verify data + code integrity.  
3. Use PR templates — include provenance for all new datasets.  
4. Expect CI to enforce MCP standards — failing CI = blocked merge.  

See [CONTRIBUTING.md](/CONTRIBUTING.md) for details.  

---

<div align="center">

💡 **In short:**  
This `.github/` folder is the **automation nerve center** of the Kansas Frontier Matrix,  
ensuring everything is **traceable, secure, reproducible, and community-driven**.  

</div>
