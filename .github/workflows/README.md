<!-- .github/workflows/README.md -->

# ⚙️ GitHub Actions Workflows (CI/CD)

> **Folder:** `.github/workflows/` 📁  
> **Purpose:** Automated quality + governance gates for the Kansas Frontier Matrix (KFM) monorepo.

<p align="center">
  <a href="../../README.md">🏠 Repo Home</a> •
  <a href="../../CONTRIBUTING.md">🤝 Contributing</a> •
  <a href="../../docs/">📚 Docs</a> •
  <a href="../../policy/">🛡️ Policy</a>
</p>

---

## 🧭 What lives in this folder?

This folder contains the GitHub Actions workflow definitions that run on **push** and **pull requests** to keep KFM’s code, data, and narratives *verifiable + compliant* (tests, linting, and CI/CD orchestration).:contentReference[oaicite:0]{index=0}

KFM is a **monorepo** (backend + frontend + pipelines + governed data/docs), so CI must validate *multiple subsystems* together.:contentReference[oaicite:1]{index=1}

---

## ✅ Non‑negotiable principle: “Fail Closed” 🧱

> [!IMPORTANT]
> If a check fails, **the merge should be blocked** — especially governance/policy checks. This is intentional: incomplete or non‑compliant contributions must not land on `main`.:contentReference[oaicite:2]{index=2}

---

## 🧪 What CI should enforce (KFM “definition of done”)

KFM’s CI gates aren’t just “tests pass” — they include **policy-as-code** and **evidence-first publishing**.

### 1) 🧩 Code Quality Gates (API + UI)
- ✅ Backend tests (e.g., `pytest`):contentReference[oaicite:3]{index=3}
- ✅ Frontend tests (e.g., `npm test`):contentReference[oaicite:4]{index=4}
- ✅ Linters/formatters (Python + JS) such as `black --check`, `flake8`, `eslint`, `prettier`:contentReference[oaicite:5]{index=5}

### 2) 🛡️ Governance Gates (OPA/Rego via Conftest)
- ✅ CI runs **Conftest** against `policy/*.rego` to prevent merges that violate governance requirements (e.g., missing license metadata, missing provenance artifacts, disallowed AI prompt text).:contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}

Example failure pattern you’ll see in CI logs:
- `Dataset "mydata" is missing required field "license"`:contentReference[oaicite:8]{index=8}

### 3) 📚 Docs + Story Node Governance
- ✅ Markdown protocol validation (YAML front‑matter + required sections):contentReference[oaicite:9]{index=9}
- ✅ Link/reference validation (no broken internal links, citations, or references):contentReference[oaicite:10]{index=10}

### 4) 🗂️ Data Evidence Gates (Schemas + Provenance)
- ✅ JSON schema validation for structured artifacts:
  - STAC, DCAT, PROV (and Story Node schemas when applicable):contentReference[oaicite:11]{index=11}
- ✅ Classification + sovereignty checks (no “downgrade” of sensitive inputs to public outputs):contentReference[oaicite:12]{index=12}

### 5) 🔒 Security & Safety Gates
- ✅ Secret scanning (no tokens, passwords, keys committed):contentReference[oaicite:13]{index=13}
- ✅ PII / sensitive data scanning (including sensitive coordinates):contentReference[oaicite:14]{index=14}
- ✅ Classification consistency checks (prevent accidental exposure):contentReference[oaicite:15]{index=15}

### 6) 🧾 Release-time provenance (optional, but recommended)
Some steps belong at **release time**, not every PR:
- 🔏 Signed artifacts + SBOMs + provenance attestations:contentReference[oaicite:16]{index=16}

---

## 🗺️ Pipeline invariants CI must not violate

> [!NOTE]
> KFM’s pipeline ordering is **inviolable** (ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode). Workflows should reinforce this ordering with validation gates, not bypass it.:contentReference[oaicite:17]{index=17}

---

## 🧰 Workflow map (recommended file set)

> [!TIP]
> If you don’t have all of these yet, start with **`ci.yml` + `policy.yml`** and expand over time.

| Workflow file 🧾 | What it does ✅ | Typical triggers ⏱️ |
|---|---|---|
| `ci.yml` | Main PR gate: API tests + UI tests + lint/format + lightweight smoke checks | `pull_request`, `push` |
| `policy.yml` | Runs Conftest (OPA/Rego) governance rules against repo changes | `pull_request`, `push` |
| `docs.yml` | Markdown protocol checks + link validation | `pull_request` (paths: `docs/**`) |
| `schemas.yml` | Validate STAC/DCAT/PROV + other JSON schema artifacts | `pull_request` (paths: `data/**`, `schemas/**`) |
| `security.yml` | Secrets/PII/sensitive-location scans + dependency review | `pull_request`, `schedule` |
| `docker.yml` | Build Docker images (API/Web) and optionally push to registry after merge | `push` (main), `workflow_dispatch` |
| `release.yml` | Tag/release workflow: SBOM + signing + provenance attestations | `workflow_dispatch`, `release`, tags |

---

## 🧑‍💻 Run the same checks locally (fast feedback)

### 🐍 Backend (FastAPI) — tests
```bash
docker-compose exec api pytest
```
(Backend tests in CI are expected to use `pytest`.):contentReference[oaicite:18]{index=18}

### 🌐 Frontend (React/TS) — tests
```bash
cd web
npm test
```
(Frontend tests are expected in CI.):contentReference[oaicite:19]{index=19}

### 🛡️ Policy checks — Conftest
```bash
conftest test .
```
(Use this to reproduce CI policy failures locally.):contentReference[oaicite:20]{index=20}

---

## 🧯 Troubleshooting CI failures (common patterns)

### ❌ “Policy checks” failed
- **Most common causes**
  - Missing license field in dataset metadata
  - Missing provenance artifact (PROV) for a processed output
  - Sensitive classification “downgrade” detected
- **What to do**
  - Read the CI log line: Conftest usually tells you *exactly* which rule + file failed:contentReference[oaicite:21]{index=21}
  - Fix the artifact (metadata/provenance/classification), then re-run:
    - `conftest test .`:contentReference[oaicite:22]{index=22}

### ❌ Docs check failed (front‑matter / missing sections / broken links)
- Ensure YAML front‑matter is valid and required sections exist:contentReference[oaicite:23]{index=23}
- Fix broken internal references (moved files, renamed anchors):contentReference[oaicite:24]{index=24}

### ❌ Secrets / PII / sensitive content flagged
- Remove the secret from git history (if needed), rotate the key, and prefer GitHub Secrets
- Validate data contributions for inadvertent PII / sensitive coordinates:contentReference[oaicite:25]{index=25}

---

## 🔐 Secrets & permissions (workflow hygiene)

> [!WARNING]
> Never commit secrets. CI is expected to scan for secrets and fail builds when found.:contentReference[oaicite:26]{index=26}

**Common secrets you may need** (varies by workflow):
- `GHCR_TOKEN` / registry credentials (for Docker pushes)
- `CODECOV_TOKEN` (if using external coverage reporting)
- `OPENAI_API_KEY` (only if you run *non-default* CI jobs that require it — most CI should mock AI calls)

✅ Prefer GitHub’s `GITHUB_TOKEN` wherever possible and grant minimal permissions per workflow.

---

## 🧱 Conventions for adding/editing workflows

### ✅ Keep workflows KFM‑aligned
- Use **path filters** to avoid running heavy checks on unrelated changes
- Keep jobs **deterministic** and cache dependencies (pip/npm)
- Prefer **small fixture datasets** for graph/API integration tests (don’t pull huge real data in PR checks)
- Treat governance checks as **required** status checks (“fail closed”):contentReference[oaicite:27]{index=27}

### 🧩 Suggested patterns
- `concurrency:` cancel outdated PR runs
- “Reusable workflows” for shared steps across `ci.yml`, `docs.yml`, etc.
- Pin third-party actions to major versions (or SHAs for high assurance)

---

## 📎 Design references (why CI is strict)

- CI includes tests, linting, Conftest policy enforcement, and may build Docker images post‑merge:contentReference[oaicite:28]{index=28}
- Governance policies are “policy-as-code” (OPA/Rego) and CI enforcement uses Conftest to block non‑compliant merges:contentReference[oaicite:29]{index=29}
- Minimum CI gates include docs validation, schema validation, security scans, and classification consistency checks:contentReference[oaicite:30]{index=30}
- Pipeline ordering is absolute; workflows should validate artifacts at the correct boundaries:contentReference[oaicite:31]{index=31}

---

## 🧾 Quick folder view

```text
📁 .github/
└── 📁 workflows/
    ├── 🧪 ci.yml
    ├── 🛡️ policy.yml
    ├── 📚 docs.yml
    ├── 🗂️ schemas.yml
    ├── 🔒 security.yml
    ├── 🐳 docker.yml
    ├── 🏷️ release.yml
    └── 📄 README.md   👈 you are here
```

---

<details>
<summary>🏷️ Badge template (optional)</summary>

> Replace `OWNER/REPO` + workflow filenames to match your repo.

```md
![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)
![Policy](https://github.com/OWNER/REPO/actions/workflows/policy.yml/badge.svg)
![Docs](https://github.com/OWNER/REPO/actions/workflows/docs.yml/badge.svg)
![Security](https://github.com/OWNER/REPO/actions/workflows/security.yml/badge.svg)
```

</details>
