# .github — GitHub Automation & Community Health (Kansas Frontier Matrix)

This folder is the **operational control plane** for the Kansas Frontier Matrix (KFM): CI/CD workflows, community health files, and governance guardrails.

> **Derived from KFM Master Guide v13 (draft, 2025-12-28)** — the goal is to encode “contract-first + evidence-first” work into GitHub so the repo can scale without losing provenance, ethics, or reproducibility.

---

## What this folder is responsible for

- **CI/CD**: build, test, validate catalogs/schemas, deploy, monitor, and write governance records.
- **Community health**: issue templates, PR templates, contributing hygiene, and security policy.
- **Reproducibility**: “repro-kit” environment scaffolding (e.g., local Neo4j/Docker patterns).
- **Governance enforcement**: approvals, audit artifacts, ledgers, and supply-chain checks.

If you’re looking for broader system architecture, start here:

- KFM Master Guide: `../docs/MASTER_GUIDE_v13.md`
- System deep-dive: `../Kansas Frontier Matrix System.docx`
- GitHub operations: `../Inside and Out of GitHub_ A Deep Guide for the Kansas Frontier Matrix.docx`
- Documentation standards: `../Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx`

---

## The non-negotiable pipeline ordering

Everything in CI/CD and repo policy assumes this canonical order (no “leapfrogging” stages):

```mermaid
flowchart LR
  A[ETL] --> B[STAC / DCAT / PROV catalogs]
  B --> C[Neo4j graph]
  C --> D[APIs (contract boundary)]
  D --> E[React / Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
```

**Implication for workflows:** any workflow that produces derived artifacts (data, tiles, model outputs, narrative) must also produce (or update) the **catalog + provenance** artifacts that make it admissible in later stages.

---

## Expected contents of `.github/`

> Some repos evolve; if a file isn’t present yet, treat this as the **target standard layout** for this directory.

| Path | What it’s for | Notes |
|---|---|---|
| `.github/workflows/` | GitHub Actions pipelines | CI, scheduled ingest/update, deploy gates, audit writes |
| `.github/ISSUE_TEMPLATE/` | Issue templates | Bug reports, data additions, doc changes, governance flags |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR checklist & routing | Forces evidence + contract compliance |
| `.github/CODEOWNERS` | Required reviewers | Used for governance-critical paths (schemas, catalogs, workflows) |
| `.github/SECURITY.md` | Security policy | Disclosure + response expectations |
| `.github/dependabot.yml` | Dependency updates | Optional, but recommended |
| `.github/repro-kit/` | Reproducible dev env scaffolding | Often includes Neo4j, local stack quickstarts |

---

## CI/CD lifecycle (how workflows are conceptually staged)

KFM CI/CD is designed as **phases**, so each PR or scheduled run is validated systematically:

1. **Pre-Commit**  
   Lint + validate configuration files and documentation structure (YAML, Markdown rules, schema presence).

2. **Build**  
   Create reproducible environments (container builds, consistent Python/Node toolchains).

3. **Test**  
   Unit/integration tests, catalog/schema validation, and governance checks (FAIR+CARE).

4. **Deploy**  
   Staging first; production behind approvals (and environment protections).

5. **Monitor**  
   Emit telemetry artifacts: runtime metrics, failures, performance, sustainability metrics (if enabled).

6. **Govern**  
   Write an auditable record of what changed (ledger entry with hashes, statuses, timestamps).

---

## Common workflow categories

Your repo may name these differently, but these are the patterns this folder should support:

### 1) Pull Request validation (PR gate)
Triggered by `pull_request`:

- Lint + format check (Python + Node + Markdown)
- Validate **STAC/DCAT/PROV** JSON / JSON-LD structure (schema validation)
- Run unit tests + integration tests (including small-graph integrity fixtures if configured)
- Fail fast if:
  - new dataset lacks catalog entries
  - provenance is missing
  - sensitive material violates governance rules

### 2) Scheduled data/model refresh (auto-update / orchestrator)
Triggered by `schedule` (cron) and optionally `workflow_dispatch`:

- Fetch new upstream datasets or model artifacts into a staging area
- Run validation + governance checks
- Promote to production only if all checks pass
- Tag / release if applicable

### 3) Deployment workflows (staging → production)
Triggered by `workflow_dispatch`, `push` to protected branches, or release tags:

- Deploy services (API, UI, graph ingest, tiles, etc.)
- Require approval gates for production (use GitHub Environments + reviewers)
- Produce deploy logs and governance entries

### 4) Governance + supply-chain workflows
Often run on releases/tags and/or deploys:

- SBOM generation + validation
- Signed build manifests / provenance attestations (SLSA-like patterns)
- Ledger sync / governance trail writes

---

## Governance & security controls enforced from `.github`

### Council / human approval gates
Production is not “just a green build.” Use **protected environments** and **required reviewers** for:

- Deploy-to-prod workflows
- Schema and governance policy changes
- Any change that impacts sensitive data handling

### Audit trail artifacts
Workflows should produce versioned artifacts like:

- build manifests (hashes)
- SBOM outputs
- governance ledger entries (what changed + when + status)
- redaction/audit signals when sensitive material is involved

### Sovereignty & sensitive-data safety
If your workflows touch anything potentially sensitive (e.g., culturally restricted sites, private landowner data, vulnerable locations), ensure:

- **precision masking** / generalization where required
- explicit labeling (CARE labels / sensitivity fields)
- extra review triggers (CODEOWNERS + approvals)

---

## Secrets & environment configuration

Workflows should rely on **environment variables and secrets** (never hardcode):

- Neo4j connection (e.g., `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASSWORD`)
- Deployment credentials / tokens (scoped + rotated)
- API keys for upstream data pulls (if any)

Recommended repo patterns:

- `../.env.example` for local development defaults
- `.github/repro-kit/` for reproducible local stack docs (Neo4j in Docker, etc.)

---

## Local workflow development tips

You should be able to validate most workflow logic without burning CI minutes:

- Run linters locally (Python + Node).
- Validate JSON/JSON-LD schema locally when editing catalogs.
- Validate Markdown structure locally if your repo enforces templates.

Optional tooling that helps:
- `act` (simulate GitHub Actions locally)
- `shellcheck` (if workflows call shell scripts)
- `yamllint` (for workflow YAML hygiene)

---

## PR checklist for `.github` changes

Use this checklist whenever you modify workflows/templates/policies:

- [ ] Workflow YAML validates (syntax + lint).
- [ ] Any new workflow has clear triggers (`pull_request`, `push`, `schedule`, `workflow_dispatch`) and is documented here.
- [ ] Security posture preserved: least-privilege permissions, no plaintext secrets, no unsafe logging.
- [ ] Governance maintained: changes still produce required audit artifacts (ledger/telemetry) where applicable.
- [ ] Changes do not bypass the canonical pipeline ordering.
- [ ] CODEOWNERS updated if governance-critical paths changed.
- [ ] If the workflow affects data publication, it enforces catalog + provenance updates (STAC/DCAT/PROV).

---

## Project reference library

These files support contributor onboarding and the engineering standards behind KFM. If you store these PDFs elsewhere, update the paths. Suggested home: `../docs/library/`.

<details>
<summary><strong>Architecture, governance, and engineering standards</strong></summary>

- `../Kansas Frontier Matrix System.docx`
- `../Inside and Out of GitHub_ A Deep Guide for the Kansas Frontier Matrix.docx`
- `../Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx`
- `../Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `../clean-architectures-in-python.pdf`
- `../Command Line Kung Fu_ Bash Scripting Tricks, Linux Shell Programming Tips, and Bash One-liners - Command_Line_Kung_Fu_Bash_Scripting_Tricks,_Linux_Shell_Program.pdf`

</details>

<details>
<summary><strong>Geospatial, GIS, mapping, and remote sensing</strong></summary>

- `../Geographic Information System Basics - geographic-information-system-basics.pdf`
- `../geoprocessing-with-python.pdf`
- `../python-geospatial-analysis-cookbook.pdf`
- `../making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `../Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `../Google Earth Engine Applications.pdf`
- `../Google Maps API Succinctly - google_maps_api_succinctly.pdf`
- `../google-maps-javascript-api-cookbook.pdf`

</details>

<details>
<summary><strong>Web UI, visualization, and graphics</strong></summary>

- `../responsive-web-design-with-html5-and-css3.pdf`
- `../webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `../Computer Graphics using JAVA 2D & 3D.pdf`

</details>

<details>
<summary><strong>Databases and scalable data management</strong></summary>

- `../PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `../MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf`
- `../Scalable Data Management for Future Hardware.pdf`

</details>

<details>
<summary><strong>JavaScript/Node toolchain</strong></summary>

- `../Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf`

</details>

<details>
<summary><strong>Statistics, experimental design, regression, and Bayesian methods</strong></summary>

- `../Understanding Statistics & Experimental Design.pdf`
- `../Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf`
- `../regression-analysis-with-python.pdf`
- `../Bayesian computational methods.pdf`
- `../graphical-data-analysis-with-r.pdf`

</details>

<details>
<summary><strong>AI, data mining, and neural networks</strong></summary>

- `../deep-learning-in-python-prerequisites.pdf`
- `../AI Foundations of Computational Agents 3rd Ed.pdf`
- `../Data Mining Concepts & applictions.pdf`
- `../Artificial-neural-networks-an-introduction.pdf`
- `../Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf`

</details>

<details>
<summary><strong>Advanced math / optimization / graphs (supporting theory)</strong></summary>

- `../Generalized Topology Optimization for Structural Design.pdf`
- `../Spectral Geometry of Graphs.pdf`

</details>

<details>
<summary><strong>Compilers and language tooling (useful for DSLs & contracts)</strong></summary>

- `../implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf`

</details>

---

## License & content note

If this repository is public/open-source, verify that any non-original PDFs and commercial book content are stored and distributed in compliance with their licenses. If not, replace PDFs with:
- citations,
- purchase/official links,
- or internal-only storage references.
