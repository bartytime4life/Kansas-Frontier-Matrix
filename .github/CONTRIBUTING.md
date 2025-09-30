<div align="center">

# 🤝 Kansas-Frontier-Matrix — Contributing Guide

**Mission:** Empower contributors to build Kansas-Frontier-Matrix  
with **reproducibility, provenance, and documentation-first practices**.  

This project follows **MCP (Master Coder Protocol)**:  
every dataset, script, and workflow must be **documented, reproducible, and auditable**.  

</div>

---

## 🚀 Quick Start

1. **Fork the repo** → create a feature branch  
2. Make small, focused commits with descriptive messages  
3. Run hygiene locally before pushing:

```bash
pre-commit run -a
make prebuild     # schema + STAC validation + site fallback

	4.	Push branch → open a Pull Request (PR) → request review

⸻

🔄 Contribution Lifecycle

flowchart LR
  A["Fork & branch"] --> B["🧑‍💻 Develop\n(small, documented commits)"]
  B --> C["🧹 Run hygiene\n(pre-commit, make prebuild)"]
  C --> D["📤 Open PR\nlinked to issue"]
  D --> E["🤝 Review\nmaintainers enforce MCP"]
  E --> F["✅ Merge\nsquash or rebase to main"]

<!-- END OF MERMAID -->



⸻

📋 Expectations

Commits
	•	Use imperative tense: Fix STAC schema validation
	•	Link issues: Closes #123 or Relates to #456
	•	Keep PRs small + focused

Documentation
	•	Every new dataset → update/add README.md in the relevant directory
	•	Every new config/schema → update corresponding .schema.json
	•	Roadmap-aligned work → update roadmap.yaml

Provenance
	•	New rasters → include .sha256 checksum + STAC item
	•	New sources → add data/sources/*.json descriptor
	•	Experiments → log via docs/templates/experiment.md

⸻

🧪 Testing & Validation

Before PRs:

make prebuild          # schema + STAC validation
pytest -q              # if tests/ exist
mkdocs build -q        # if docs/ exist

CI will run:
	•	STAC validation (stac-validate.yml)
	•	Web config validation (web-config-validate.yml)
	•	Tests (ci.yml, tests.yml)
	•	Security scans (CodeQL, Trivy, secret scanning)

⸻

🛡️ Review & Governance
	•	PRs require at least one maintainer review
	•	Branch protection → main requires CI green + schema checks + CodeQL
	•	Automerge only for Dependabot minor/patch PRs with label + passing CI

⸻

🧭 Community Norms
	•	Respect the Code of Conduct
	•	Follow Security Policy for sensitive disclosures
	•	Uphold MCP values:
	•	Reproducibility → make targets, not one-off commands
	•	Documentation-first → update READMEs + schemas before merge
	•	Provenance → every artifact traceable to its source

⸻

🗂️ Where to Start
	•	New datasets → data/sources/
	•	Schemas → src/kansas_geo_timeline/schemas/
	•	Workflows → .github/workflows/
	•	Roadmap items → .github/roadmap/roadmap.yaml

⸻

✅ Summary:
Contributing to Kansas-Frontier-Matrix means following MCP principles:
document everything, keep it reproducible, and ensure provenance.
Together we build a mission-grade, auditable knowledge hub for Kansas.