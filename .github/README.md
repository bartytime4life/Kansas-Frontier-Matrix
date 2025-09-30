<div align="center">

# ⚙️ Kansas-Frontier-Matrix — GitHub Automation (`.github/`)

**Mission:** Centralize **automation, CI/CD, and governance assets**  
that keep this repository **reproducible, secure, and contributor-friendly**.  

Everything under `.github/**` exists to enforce the project’s  
**Master Coder Protocol (MCP)** standards: reproducibility, provenance, and safety.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](../.github/workflows/stac-badges.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)

</div>

---

## 🔄 Automation Lifecycle

```mermaid
flowchart TD
  A["Local dev\n(make, pre-commit)"] --> B["CI jobs\n(.github/workflows)"]
  B --> C["Validation\n(STAC, schemas, tests)"]
  C --> D["Build\n(MapLibre site, configs)"]
  D --> E["Artifacts\n(Pages, reports, badges)"]
  E --> F["Governance\n(PR templates, dependabot, security)"]

<!-- END OF MERMAID -->



⸻

📂 Contents

.github/
├── workflows/            # GitHub Actions (CI/CD)
│   ├── site.yml          # Build & deploy MapLibre site
│   ├── stac-badges.yml   # Generate STAC coverage badges
│   ├── codeql.yml        # Static analysis (Python + JS/TS)
│   ├── automerge.yml     # Guarded auto-merge for green PRs
│   └── tests.yml         # (optional) lint + schema + unit tests
├── ISSUE_TEMPLATE/       # Structured issue templates
├── PULL_REQUEST_TEMPLATE.md
├── SECURITY.md           # Vulnerability reporting policy
└── dependabot.yml        # Automated dependency updates


⸻

🚀 CI/CD Principles
	•	Reproducible → workflows call make targets (make stac, make site), so CI = local.
	•	Fail-safe → jobs gracefully skip if inputs missing.
	•	Minimal → actions pinned, least-privilege permissions.
	•	Fast feedback → lint + STAC/schema checks before heavy builds.
	•	Artifacted → validation reports, site bundles, and badges uploaded.

⸻

🧪 Workflows at a Glance

Workflow	Purpose	Triggers
Site	Build & deploy web/ (MapLibre + configs)	push→main, manual
STAC Badges	Generate & commit coverage badges	schedule, manual
CodeQL	Static analysis (Python + JS/TS)	push, PR, schedule
Auto-merge	Merge passing PRs with label	pull_request
Tests	Lint + schema + unit tests (if present)	pull_request, manual


⸻

🔁 Dependency Management
	•	Ecosystems: Actions, npm (web), pip, docker
	•	Cadence: weekly (routine), daily (security advisories)
	•	Noise control: group minor/patch versions where supported

⸻

🔐 Security Posture
	•	📜 See SECURITY.md for reporting process
	•	🔍 CodeQL runs for Python + JS/TS
	•	🔑 No long-lived repo-wide secrets; scoped job tokens only
	•	🔒 Minimal permissions on all workflows

⸻

🧰 Local Pre-flight (Match CI)

# Hygiene checks
pre-commit run -a

# Validation checks
make prebuild

# Optional
pytest -q      # if tests/ exist
mkdocs build   # if docs/ exist

If pre-commit isn’t installed:

pipx install pre-commit && pre-commit install


⸻

📝 Governance Standards
	•	Branch protection → main requires CI green + reviews
	•	Commits → imperative style + linked issue refs
	•	Schemas everywhere → update + validate via CI
	•	Badges → generated, never hand-edited (web/badges/)
	•	Artifacts → large rasters in LFS/DVC; configs + STAC JSON tracked in-repo

⸻

✅ Summary:
.github/ is the automation + governance backbone of Kansas-Frontier-Matrix.
Workflows, templates, and policies here enforce MCP principles:
reproducibility, provenance, and safety-first collaboration.