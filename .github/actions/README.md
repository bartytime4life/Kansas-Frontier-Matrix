# 🧩 `.github/actions/` — Reusable GitHub Actions (KFM CI/CD Building Blocks)

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-local%20actions-blue?logo=githubactions)
![CI/CD](https://img.shields.io/badge/CI%2FCD-automation%20first-success)
![Security](https://img.shields.io/badge/security-least%20privilege-important)

Welcome to the **local Actions library** for the Kansas Frontier Matrix (KFM) repo.  
This folder is where we keep **reusable, versioned, reviewable automation blocks** (usually **composite actions**) that power our workflows in:

📁 `.github/workflows/`

> ✅ Why local actions?  
> - **Consistency** across workflows (one lint/test setup, many pipelines)  
> - **Less copy/paste YAML** (and fewer subtle differences)  
> - **Easier upgrades** (update once → all workflows inherit)  
> - **KFM-friendly automation** (policy checks, Docker builds, deploy gates)

---

## 🧭 Quick start: using a local action in a workflow

In a workflow file (example: `.github/workflows/ci.yml`):

```yaml
jobs:
  backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Local action reference 👇 (path is relative to repo root)
      - name: Setup Python + deps
        uses: ./.github/actions/setup-python

      - name: Run tests
        run: pytest -q
```

---

## 🗂️ Recommended folder layout

Each action lives in its own folder:

```text
.github/actions/
  README.md                👈 you are here
  <action-name>/
    action.yml             ✅ required
    README.md              ✅ required (action-specific docs)
    src/                   (optional) scripts used by composite action
```

### ✅ Naming convention
Keep names:
- **kebab-case**
- **verb-first**
- scoped when helpful (ex: `kfm-opa-policy-check`)

Examples:
- `setup-python`
- `setup-node`
- `docker-build-push`
- `compose-smoke-test`
- `opa-conftest-policy`

---

## 🧱 How KFM uses these actions

KFM’s architecture and tooling typically needs CI/CD to orchestrate:

- 🧪 unit + integration testing
- 🧹 formatting + linting
- 🐳 Docker image builds for services (ex: `api`, `web`)
- 🔐 policy gates (OPA/Conftest) for governance + safety checks
- 🚀 deploy steps (staging → production) with Infrastructure-as-Code (IaC)

### 🧠 Pipeline mental model (high-level)

```mermaid
flowchart TD
  A[PR / Push] --> B[Fast Checks<br/>lint • format • unit tests]
  B --> C[Policy Gates<br/>OPA/Conftest • metadata rules]
  C --> D[Build Artifacts<br/>Docker images • web bundle]
  D --> E[Integration Smoke<br/>docker compose up • health checks]
  E --> F{Deploy?}
  F -->|staging| G[Deploy Staging<br/>IaC / scripts]
  F -->|prod (gated)| H[Deploy Prod<br/>Approvals + environments]
```

Local actions are the **lego bricks** used to assemble that pipeline.

---

## 📚 Action catalog

> ℹ️ This section is intentionally lightweight:  
> **the source of truth is the folders in `.github/actions/*/`**.

### What every action must include ✅
- `action.yml` with:
  - `name`, `description`
  - `runs: using: composite`
  - explicit `inputs` and `outputs` (when relevant)
- `README.md` inside the action folder describing:
  - purpose
  - inputs/outputs
  - example usage snippet
  - troubleshooting

### Optional but encouraged ⭐
- A `src/` folder with scripts to keep `action.yml` clean
- Small, composable actions (prefer 1 responsibility)
- A minimal `permissions:` footprint in workflows that call the action

---

## 🔒 Security + governance rules (non-negotiable)

### 1) Least privilege by default 🛡️
Workflows that use these actions should set:

```yaml
permissions:
  contents: read
```

…and only elevate when necessary (ex: `packages: write` for GHCR pushes).

### 2) Secrets handling 🔐
- Never echo secrets
- Prefer masked env vars and GitHub Secrets
- If deploying (SSH / cloud), keep credentials **only** in:
  - `GitHub Environments`
  - `GitHub Secrets`
  - OIDC (preferred if cloud supports it)

### 3) Policy gates (KFM-style) ✅
If the repo includes governance rules (metadata, licensing, provenance, safety), local actions should support:
- running **Conftest**
- running **OPA** tests
- failing fast with clear messages

> Tip: If a policy fails, the workflow should point to the exact rule + file to fix.

---

## 🛠️ Creating a new local action (template)

1) Create a folder:
```bash
mkdir -p .github/actions/<action-name>
```

2) Add `action.yml` (composite action template):
```yaml
name: "<action-name>"
description: "Describe what this action does (1 sentence)."
inputs:
  example_input:
    description: "Example input."
    required: false
    default: ""
runs:
  using: "composite"
  steps:
    - name: Do the thing
      shell: bash
      run: |
        echo "Hello from <action-name>"
```

3) Add `README.md` inside the action folder with:
- what it does
- inputs/outputs
- example workflow usage
- common failure modes

---

## 🧪 Local debugging tips

### Run workflows locally (optional)
If you use `act`, you can simulate GitHub Actions runs locally (useful for faster iteration).

> ⚠️ Caveat: service containers + networking can differ from GitHub-hosted runners.

### Prefer “thin actions”
If an action grows too large:
- split it into smaller actions
- or move complex logic into scripts in `src/`

---

## ✅ Definition of done for CI/CD actions

An action is “done” when:
- ✅ has docs
- ✅ has deterministic output
- ✅ fails loudly and clearly
- ✅ avoids hidden side effects
- ✅ supports KFM’s automation-first pipeline philosophy

---

## 🔁 Related folders

- 📁 `.github/workflows/` — pipeline definitions that call these actions
- 📁 `infra/` / `k8s/` (if present) — deployment & IaC
- 📁 `api/` / `web/` (if present) — service Docker builds + tests

---

## 🧾 License / attribution

These local actions are part of the KFM repository and follow the repo’s license and contribution rules.