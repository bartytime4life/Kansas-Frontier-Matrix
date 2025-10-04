<div align="center">

# 🗂️ Kansas Frontier Matrix — Templates (`/docs/templates/`)

**Mission:** Provide reusable **templates and boilerplates** for experiments,  
standard operating procedures, model cards, and architectural decisions —  
ensuring **reproducibility, clarity, and MCP compliance**.  

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)  
[![Templates](https://img.shields.io/badge/Templates-Standardized-green)](README.md)  
[![Version Control](https://img.shields.io/badge/Tracked-Git%20%26%20Provenance-orange)](README.md)  

</div>

---

## 🎯 Purpose

The `/docs/templates/` directory provides **ready-to-use documentation templates**  
for contributors and maintainers. These templates enforce consistent structure  
and traceability across **scientific method workflows**, **technical design notes**,  
and **code/data standards**.  

By following these templates, every artifact in the Kansas Frontier Matrix (KFM)  
becomes:
- **Auditable** → clearly linked to provenance and references.  
- **Reproducible** → structured so others can repeat the process.  
- **Interoperable** → aligned with MCP, STAC, and ontology standards.  
- **Readable** → professional, GitHub-friendly, and accessible.  

---

## 📚 Contents

```text
docs/templates/
├── README.md             # Index (this file)
├── experiment.md          # MCP-style research experiment log
├── sop.md                 # Standard Operating Procedure template
├── model_card.md          # AI/ML model card template
├── adr.md                 # Architecture Decision Record template
├── dataset.md             # Dataset descriptor template (metadata-driven)
├── provenance.md          # Provenance & checksum log template
└── checklist.md           # Contributor & review checklist template


⸻

🗂️ Key Templates
	•	experiment.md
Hypothesis-driven MCP experiment log (Problem → Hypothesis → Method → Results → Conclusion).
	•	sop.md
Step-by-step reproducible procedure for tasks (ETL, STAC validation, data ingestion).
	•	model_card.md
Documentation for AI/ML models (purpose, training data, biases, metrics, limits).
	•	adr.md
Architecture Decision Record for logging major system design choices.
	•	dataset.md
Dataset descriptor template (ID, source, license, spatial/temporal extent, schema).
	•	provenance.md
Template for logging checksums, versions, and dataset provenance.
	•	checklist.md
Contributor/reviewer checklist to ensure MCP, CI/CD, and standards compliance.

⸻

🧭 Usage
	1.	Copy the relevant template into your working doc.
	2.	Fill in required fields (hypothesis, dataset IDs, provenance).
	3.	Link the finished doc back to related architecture or data dirs.
	4.	Commit under version control so the artifact becomes auditable.
	5.	Promote notes/experiments into stable documentation once peer-reviewed.

⸻

🔗 Related Docs
	•	Standards
	•	Architecture
	•	Design
	•	Integration

⸻


<div align="center">


🗂️ Templates are the scaffolding of MCP reproducibility.
Every experiment, SOP, and decision begins here.

</div>