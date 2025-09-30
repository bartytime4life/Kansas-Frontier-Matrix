<div align="center">

# 🧩 Kansas-Frontier-Matrix — GitHub Workflows (`.github/workflows/`)

**Mission:** Automate **CI/CD, validation, security, and release**  
so every change is **reproducible, auditable, and safe-by-default**.

[![Site](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](./site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](./stac-validate.yml)
[![STAC Badges](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](./stac-badges.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](./codeql.yml)

📌 **Fail fast** (lint, schemas, STAC) before heavy work  
📌 **Least-privilege** tokens + safe on PRs (no writes)  
📌 **Artifacted** logs/reports for audit + debugging

</div>

---

## 🔄 Workflow Lifecycle

```mermaid
flowchart LR
  A["Push / PR / Tag / Manual"] --> B["Config & Schema checks\n(web-config-validate, stac-validate)"]
  A --> C["CI / Tests\n(ruff, pytest, mypy?)"]
  B --> D["Render configs\n(stac.yml → app.config.json)"]
  D --> E["Publish site\n(site.yml → Pages)"]
  A --> F["Security & SBOM\n(codeql, trivy, sbom)"]
  A --> G["Containers\n(docker → GHCR)"]
  A --> H["Badges & Reports\n(stac-badges)"]
  A --> I["Release\n(tag vX.Y.Z → assets)"]

<!-- END OF MERMAID -->


Safety: Writers (Pages, GHCR, Releases) never execute on PRs. Each workflow sets minimal permissions:.

⸻

📚 Index (what runs where)

Workflow	Purpose	Triggers (paths)	Outputs / artifacts
CI (ci.yml)	Python lint/tests (ruff/pytest), optional mypy; light web smoke	src/**, tests/**, pyproject.toml, requirements*	JUnit/coverage in .artifacts/, run summary
Tests (tests.yml)	Quick test matrix	tests/**	pytest-report.xml, coverage (if enabled)
Web Config Validate	JSON lint + $schema validate; targeted tests	web/**.json, web/config/**, tests/**	step summaries, pytest-web-configs.xml
STAC Validate	stac-validator → pystac fallback; HTTP/asset checks	stac/**	.artifacts/stac_validator.txt, link reports
STAC & Config Render (stac.yml)	Validate STAC, then render web/app.config.json; schema-check result	stac/**, src/**, web/**	.artifacts/stac_report.json, web/app.config.json
STAC Badges	Produce Shields-ready JSON for catalog coverage	stac/**, data/sources/**	web/badges/*.json, build/stac_report.json
Site (Pages) (site.yml)	Build & deploy MapLibre site; optional link check	web/**, stac/**, mkdocs.yml	_site/ artifact → Pages
Docker (docker.yml)	Multi-arch Buildx → GHCR; provenance; Trivy image scan	docker/**, Dockerfile	image tags, trivy-image.sarif
SBOM (sbom.yml)	CycloneDX/SPDX for repo (and image if present)	push/schedule/manual	artifacts/sbom/**
CodeQL (codeql.yml)	Static analysis (Python, JS/TS)	push/PR/schedule	Code scanning alerts (SARIF)
Trivy (trivy.yml)	FS/config/image scans; SBOMs; SARIF	push/PR/schedule	trivy-*.sarif, SBOM JSON
Secret Scanning	Gitleaks for secrets in diffs/history	push/PR/schedule	gitleaks.sarif
OpenSSF Scorecard	Repo health/security checks	push/PR/weekly	scorecard.sarif
Release (release.yml)	Tag-driven build (sdist+wheel); checksums; optional SBOM; GH Release	tags v*	dist/**, CHECKSUMS.txt
Roadmap Sync (roadmap.yml)	Parse .github/roadmap/roadmap.yaml → labels/milestones/issues	roadmap changes/manual	build/roadmap-sync.log
Labels Sync (labels.yml)	Sync labels from .github/labels.yml	push/manual	—
Automerge	Label-gated auto-merge once checks pass	PR labeled automerge	—
Close Stale / Issue Lock	Mark/close inactive items; lock closed issues after inactivity	nightly/manual	bot comments
Link Check (optional)	Lychee across README/docs/web	push/PR	lychee.md, results.json


⸻

🔁 Reusable Patterns (copy-paste)

1) Concurrency guard

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

2) Least-privilege permissions

permissions:
  contents: read
  actions: read
  security-events: write   # only when uploading SARIF
  pages: write             # only in site.yml deploy job
  id-token: write          # only for OIDC publish/attest
  packages: write          # only for GHCR on default branch

3) Python + caches

- uses: actions/setup-python@v5
  with:
    python-version: '3.11'
    cache: 'pip'
    cache-dependency-path: |
      requirements*.txt
      pyproject.toml
- run: pip install -r requirements.txt
- run: ruff check .
- run: pytest -q --maxfail=1 --disable-warnings

4) JSON schema validation (web/STAC)

- name: JSON lint
  run: jq -e . web/app.config.json > /dev/null
- name: Schema validate
  run: python -m jsonschema -i web/app.config.json web/schema/app.schema.json

5) STAC validate (robust)

- name: stac-validator (recursive)
  run: stac-validator --recursive stac/catalog.json | tee .artifacts/stac_validator.txt
- name: pystac fallback
  run: python -m scripts.stac_fallback_validate stac/catalog.json

6) Pages deploy (safe on PRs)

permissions: { contents: read, pages: write, id-token: write }
# …
- uses: actions/upload-pages-artifact@v3
  with: { path: _site }
- uses: actions/deploy-pages@v4
  if: github.ref == 'refs/heads/main' && github.event_name != 'pull_request'

7) Docker Buildx + cache + provenance

- uses: docker/setup-buildx-action@v3
- uses: docker/login-action@v3
  if: github.ref == 'refs/heads/main'
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}
- uses: docker/build-push-action@v6
  with:
    context: .
    file: docker/Dockerfile
    platforms: linux/amd64,linux/arm64
    push: ${{ github.ref == 'refs/heads/main' }}
    provenance: true
    tags: ghcr.io/${{ github.repository }}:edge
    cache-from: type=gha
    cache-to: type=gha,mode=max

8) Trivy → SARIF

permissions: { contents: read, security-events: write }
- uses: aquasecurity/trivy-action@0.24.0
  with:
    scan-type: fs
    format: sarif
    output: trivy-fs.sarif
- uses: github/codeql-action/upload-sarif@v3
  with: { sarif_file: trivy-fs.sarif }


⸻

🧭 Conventions We Enforce
	•	Schema-first: JSON/YAML configs linted + schema-validated before builds.
	•	Geo deps on demand: GDAL/PROJ installed only where needed.
	•	Cache discipline: caches keyed to lockfiles/requirements.
	•	Artifacts always: tests, STAC reports, and renders go to .artifacts/ (or _site/).
	•	Branch safety: any writer (Pages, GHCR, Releases) is gated to default branch/tags; never writes on PRs.
	•	Run summaries: “What changed / validated / next steps” in job summaries.

⸻

👩‍💻 Typical Developer Flows
	•	Add or modify a web layer → edit stac/** + web/config/**
→ web-config-validate.yml + stac-validate.yml fail fast
→ stac.yml renders web/app.config.json
→ site.yml publishes to Pages (main only).
	•	Touch STAC items → stac-validate.yml + stac-badges.yml run; badges updated in web/badges/.
	•	Release Python package → tag vX.Y.Z → release.yml builds sdist/wheel + checksums (+ optional SBOM), creates GitHub Release.
	•	Security posture → trivy.yml, secret-scanning.yml, codeql.yml, ossf-scorecard.yml produce SARIF; view in Security → Code scanning.

⸻

🧯 Troubleshooting (fast answers)
	•	Mermaid errors in README → Quote labels with punctuation and use \n for newlines.
	•	Pages deploy is empty → Ensure site writes to _site/ and upload step uses that path.
	•	STAC link flakiness → Prefer validating local/relative assets in CI; gate remote link checks behind a flag.
	•	GHCR push denied on PR → Expected; publishers run only on default branch.
	•	SARIF not visible → Set permissions.security-events: write and correct upload path.
	•	Slow jobs → Keep caches warm with accurate keys; avoid unnecessary cache busting.

⸻

🗂️ File Map (this folder)

.github/workflows/
├── ci.yml
├── tests.yml
├── web-config-validate.yml
├── stac-validate.yml
├── stac.yml
├── stac-badges.yml
├── site.yml
├── docker.yml
├── sbom.yml
├── codeql.yml
├── trivy.yml
├── secret-scanning.yml
├── ossf-scorecard.yml
├── release.yml
├── roadmap.yml
├── labels.yml
├── automerge.yml
├── close-stale.yml
├── issue-lock.yml
├── pr-labeler.yml
├── link-check.yml            # optional
└── README.md                 # (this file)


⸻

✅ Summary:
.github/workflows/ is the automation backbone of Frontier-Matrix.
Workflows are pinned, least-privilege, and fail fast with rich artifacts —
enforcing MCP principles of reproducibility, provenance, and safety.