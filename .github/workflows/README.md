# Kansas-Frontier-Matrix — GitHub Workflows

This folder (`.github/workflows/`) contains all **CI/CD automation** for the project.  
Workflows are written in **GitHub Actions YAML** and kept modular so each area of the repo is tested and deployed independently.

---

## Workflows

### [`ci.yml`](ci.yml)
Runs the **pytest suite** (STAC + data sources + web configs) on:
- Pushes/PRs that touch `stac/**`, `data/**`, `web/**`, `scripts/**`, or `tests/**`
- Also triggered on changes to `pyproject.toml`, `requirements.txt`, and this workflow itself

**Jobs**
- **Install deps** (`pip`, `pytest`, `jsonschema`)
- **Run tests** with JUnit XML report
- **Upload artifacts** for CI dashboards

### [`web-config-validate.yml`](web-config-validate.yml)
Lightweight validator for **web configs**:
- Runs only when `web/app.config.json`, `web/layers.json`, or their schemas/tests change
- Uses `pytest -k web_configs` to quickly catch schema violations

**Purpose**
- Provides **fast feedback** on JSON Schema errors
- Prevents broken config merges before full CI runs

### [`site.yml`](site.yml)
Builds and deploys the **static site (MapLibre viewer)** to **GitHub Pages**.

**Triggered by:**
- Pushes to `main` affecting `web/**`, `stac/**`, or `data/sources/**`
- Manual dispatch (`workflow_dispatch`)

**Steps**
1. Checkout repo
2. Run **pytest -k web_configs** (ensure configs are valid)
3. Build site:
   - Prefer `make site` if Makefile target exists
   - Fallback: copy `web/` into `_site/`
4. Upload `_site/` artifact
5. Deploy to Pages

### *(Optional)* [`link-check.yml`](link-check.yml)
(Not enabled by default.)  
Runs **Lychee** link checker against Markdown/HTML files to catch broken URLs.

---

## Supporting Files

- **[dependabot.yml](../dependabot.yml)** → weekly updates for GitHub Actions + Python deps
- **[CODEOWNERS](../CODEOWNERS)** → defines default reviewers for areas of the repo
- **ISSUE_TEMPLATE/** → templates for bug reports, data additions, and experiments
- **PULL_REQUEST_TEMPLATE.md** → PR checklist for reproducibility and validation

---

## Philosophy

- **Fail fast** on schema / config errors (web-config-validate)  
- **Mission-grade validation** across data + metadata (ci.yml)  
- **Automated deploys** for reproducible web maps (site.yml)  
- **Light dependencies** (pytest + jsonschema only) for quick, reliable runs  

---

## Next Steps

- [ ] Add **branch protection rules** requiring all jobs green before merge  
- [ ] Add **release workflow** to package STAC + web configs into tagged GitHub Releases  
- [ ] Optionally enable **link-check.yml** for README + docs integrity  

---

🚀 With these workflows, every commit is validated, every config is schema-checked, and every deployment is reproducible.  
