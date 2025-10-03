<div align="center">

# 📖 Kansas Frontier Matrix — Documentation (`/docs/`)

**Mission:** Centralize all **documentation, standards, and knowledge artifacts**  
for the Kansas Frontier Matrix (KFM) project.  

[![Build & Deploy](../.github/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![Docs Lint](../.github/workflows/docs-lint.yml/badge.svg)](../.github/workflows/docs-lint.yml)
[![Pre-commit](../.github/workflows/pre-commit.yml/badge.svg)](../.github/workflows/pre-commit.yml)
[![CodeQL](../.github/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy](../.github/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![License: Docs](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../LICENSE)

</div>

---

## 📚 Overview

The `/docs/` directory holds **all project documentation**:  
research templates, SOPs, system design notes, and contributor guides.  

It follows the **Master Coder Protocol (MCP)** principle:  
> *“Document before coding. Every artifact must be reproducible, auditable, and transparent.”*

---

## 📂 Directory Structure

```text
docs/
├─ README.md             # This file
├─ glossary.md           # Canonical cross-disciplinary definitions
├─ templates/            # MCP experiment, SOP, model_card templates
├─ architecture/         # System & data flow diagrams
├─ standards/            # Coding, data, and metadata standards
├─ design/               # UI/UX design docs
├─ integration/          # GIS, deeds, historical datasets integration guides
└─ notes/                # Research notes, references, experiments in progress


⸻

📑 Key Documents
	•	Glossary → shared terms across history, GIS, geology, archaeology, computing
	•	Templates (templates/) →
	•	experiment.md (MCP experiment log)
	•	sop.md (standard operating procedure)
	•	model_card.md (AI/ML documentation)
	•	Architecture (architecture/) → system, data, pipeline, and web flow diagrams
	•	Standards (standards/) → coding style, JSON schema, STAC compliance, metadata rules
	•	Design (design/) → UI mockups, CSS/JS patterns, accessibility rules
	•	Integration (integration/) → GIS archives, deeds, historical datasets, external APIs
	•	Notes (notes/) → lab notebook entries, hypotheses, and references

⸻

🛠 Contributing Documentation
	1.	Follow MCP templates — start with docs/templates/.
	2.	Use GitHub-friendly Markdown — code fences, tables, Mermaid diagrams (<!-- END OF MERMAID -->).
	3.	Badges & Provenance — include relevant CI badges and cite data/doc sources.
	4.	Cross-link — always link datasets ↔ STAC ↔ docs.

⸻

🧭 Navigation
	•	📖 Project Root README
	•	🗂 Data Architecture
	•	🗺 Web Docs
	•	🧩 Schemas

⸻

✅ License

All documentation is shared under CC-BY 4.0.
You are free to copy, adapt, and share, provided you give proper attribution.

⸻

Tip for contributors: Treat every .md file as a lab notebook page.
Write as if someone in 2050 will use it to reconstruct your work