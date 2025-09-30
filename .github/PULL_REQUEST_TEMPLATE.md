<div align="center">

# 🚀 Kansas-Frontier-Matrix — Pull Request Template

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../.github/workflows/automerge.yml)

**Mission:** Ensure every pull request is **reproducible, documented, and MCP-compliant**.  
This template guides contributors and reviewers in enforcing **traceability, provenance, and CI hygiene**.  

</div>

---

## 🔄 PR Lifecycle

```mermaid
flowchart LR
  A["📤 Open PR\n(link to issue/epic)"] --> B["🧪 CI: Validate\nruff · pytest · stac-validator · schema"]
  B --> C{"CI green?"}
  C -- "No" --> B1["🔁 Fix & push\naddress failures"]
  B1 --> B
  C -- "Yes" --> D["🧍 Review\nmaintainer feedback"]
  D --> E{"Approved?"}
  E -- "Changes requested" --> D1["🔁 Update PR\ncommits + docs + provenance"]
  D1 --> B
  E -- "Yes" --> F["🤖 Automerge (if labeled)\n✅ all required checks"]
  E -- "Manual merge" --> F
  F --> G["🌐 Pages / 📦 Release (if tagged)\nsite.yml · release.yml"]
  G --> H["🗺️ Roadmap sync\nmilestones/labels"]
  H --> I["✅ Close linked issues"]

<!-- END OF MERMAID -->



⸻

📝 Summary

<!-- Describe your changes in 1–3 sentences. Focus on outcomes, not just files touched. -->



⸻

🔗 Related Issues / Roadmap
	•	Closes #
	•	Relates to epic/milestone: 

⸻

📂 What Changed

<!-- High-level overview. Examples:
- Added new DEM source descriptors under `data/sources/dem/`
- Converted 1930s topo maps to COG + checksums
- Updated `roadmap.yaml` with milestone m25q4
-->



⸻

✅ Contributor Checklist

Before requesting review, confirm the following:
	•	Docs updated → added/updated README.md in affected directories
	•	Schemas validated → ran make prebuild (schema + STAC + site config check)
	•	Provenance tracked → checksums (.sha256) + STAC items added for new data
	•	Tests passing → ran pytest -q locally (if applicable)
	•	Security posture → no secrets committed; workflows least-privilege
	•	Roadmap alignment → issue/epic/milestone referenced in roadmap.yaml (if applicable)
	•	Commit hygiene → small, focused commits with imperative messages (Closes #123)
	•	Community standards → Code of Conduct & MCP values observed (reproducibility, documentation-first, provenance)

⸻

🔍 Reviewer Notes (for maintainers)
	•	✅ CI green (STAC validate, web config validate, CodeQL, Trivy, secret scanning)
	•	🔎 Provenance checks (SHA-256 + STAC metadata) for new/updated data
	•	📖 Docs & schemas updated consistently
	•	🗺️ Roadmap & labels synced (.github/roadmap/roadmap.yaml, .github/labels.yml)
	•	🎯 PR scope small and focused

⸻

📖 References
	•	Contributing Guide
	•	Code of Conduct
	•	Security Policy
	•	Roadmap

⸻

✅ Summary:
Every PR should carry docs, schemas, provenance, and reproducibility.
Respect MCP values → faster reviews, automerge eligibility, and long-term trust.