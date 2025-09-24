# 📚 Kansas-Frontier-Matrix — GitHub Workflows & Standards

This directory contains **automation, CI/CD, and governance files** for the  
[Kansas-Frontier-Matrix](https://github.com/bartytime4life/Kansas-Frontier-Matrix) project.  

The `.github/` folder centralizes **community docs, workflows, and project metadata**,  
ensuring the repository is reproducible, contributor-friendly, and NASA-grade reliable.

---

## 📖 Contents

- **README.md** — (this file) overview of `.github/`
- **workflows/** — GitHub Actions CI/CD:
  - `site.yml` → build & deploy static site (MapLibre + STAC catalog) [oai_citation:0‡Data resource analysis.pdf](file-service://file-GdS9Kcw7Xbfqpy4xwwdqWS)
  - `tests.yml` → run pytest test suite (STAC validation, sources, web assets) [oai_citation:1‡Kansas Frontier Matrix AI System – Developer Documentation.pdf](file-service://file-47B5MPBSihKB9wR6k8aFVM)
  - `sbom.yml` → generate SBOM (CycloneDX/SPDX) and security scans
  - `docs.yml` → render diagrams (Mermaid CLI) & publish developer docs
- **ISSUE_TEMPLATE/** — structured templates for bugs, features, data sources
- **PULL_REQUEST_TEMPLATE.md** — contributor checklist (tests, docs, style, provenance)
- **CODEOWNERS** — assigns review responsibility to maintainers
- **FUNDING.yml** — (optional) sponsor links for sustainability

---

## 🛰️ CI/CD Philosophy

- **Reproducibility First**: All workflows follow the *Master Coder Protocol* (MCP) [oai_citation:2‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-AJeFJoUqFfFcKmtpGMVUA4)  
  — experiment → log → validate → archive.  
- **Scientific Rigor**: Every test validates STAC 1.0.0 metadata, source integrity,  
  and provenance before merging [oai_citation:3‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6).  
- **Open Source Standards**: All Actions use open workflows, pinned versions,  
  and artifact retention for traceability.  
- **Fail-Safe**: Workflows skip gracefully if optional files are missing (scaffolding stage) .  
- **Extensible**: New workflows (AI, ETL pipelines, Docker builds) can be added modularly [oai_citation:4‡Kansas Frontier Matrix AI System – Developer Documentation.pdf](file-service://file-47B5MPBSihKB9wR6k8aFVM).  

---

## 🌐 Related Docs

- [System Design — Knowledge Hub & Ingestion Pipeline][design]
- [AI Developer Documentation — NLP, Graph, Summarization][ai-docs]
- [Design Audit — Gaps & Enhancements][audit]
- [Scientific Method / MCP Protocol][mcp]

[design]: ../Kansas%20Historical%20Knowledge%20Hub%20%E2%80%93%20System%20Design.pdf
[ai-docs]: ../Kansas%20Frontier%20Matrix%20AI%20System%20%E2%80%93%20Developer%20Documentation.pdf
[audit]: ../Kansas-Frontier-Matrix%20Design%20Audit%20%E2%80%93%20Gaps%20and%20Enhancement%20Opportunities.pdf
[mcp]: ../Scientific%20Method%20_%20Research%20_%20Master%20Coder%20Protocol%20Documentation.pdf

---

## 🤝 Contributing

- Use [CONTRIBUTING.md](../CONTRIBUTING.md) for setup, style, and PR workflow [oai_citation:5‡Foundational Templates and Glossary for Scientific Method _ Research _ Master Coder Protocol.pdf](file-service://file-XygDDSfCPa5gz3jmjRV81b).
- Follow commit guidelines (imperative mood, issue linking).
- Run `pytest` before opening a PR; CI will verify:
  - STAC schema validity
  - Source configs parse correctly
  - Web viewer core assets present
- Add/update documentation with every code or data change (docs-first ethos) [oai_citation:6‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-AJeFJoUqFfFcKmtpGMVUA4).

---

## 📜 License

MIT License (see [LICENSE](../LICENSE)).  
All data references follow original source licensing (USGS, NOAA, FEMA, KGS, etc.).

---

> 🧭 *The `.github/` directory is the governance anchor of the Kansas-Frontier-Matrix —  
> ensuring open, reproducible, and scientifically rigorous collaboration across code, data,  
> and history.* [oai_citation:7‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv) [oai_citation:8‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB)