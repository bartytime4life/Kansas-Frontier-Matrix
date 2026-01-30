---
title: ".github/actions"
description: "Repo-local reusable GitHub Actions for Kansas Frontier Matrix"
status: "active"
owner: "Maintainers"
last_updated: "2026-01-30"
---

# 🧩 `.github/actions` — Local Reusable GitHub Actions

![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)
![Policy as Code](https://img.shields.io/badge/Policy%20as%20Code-Conftest%20%2B%20OPA-7B42BC?logo=openpolicyagent&logoColor=white)
![Monorepo](https://img.shields.io/badge/Repo-Monorepo-0B7285?logo=git&logoColor=white)
![Dev Env](https://img.shields.io/badge/Dev-Docker%20Compose-2496ED?logo=docker&logoColor=white)

> [!NOTE]
> This folder holds **repo-local Actions** (mostly **composite actions**) that are reused by workflows in [`../workflows/`](../workflows/).
> The goal: **less YAML duplication**, **more consistency**, and **one place** to evolve CI building blocks. 🧱✨

---

## 🧭 Quick navigation

- 🔁 CI/CD entrypoints (workflows): [`../workflows/`](../workflows/)
- 🤝 Contribution rules: [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md)
- 🛡️ Governance policies (Rego): [`../../policy/`](../../policy/)
- 📚 Docs hub: [`../../docs/`](../../docs/)
- 🏠 Project README: [`../../README.md`](../../README.md)

---

## 🎯 Why local actions?

KFM CI is designed to enforce a few consistent “gates” on pull requests:

- ✅ **Linting / formatting**
- ✅ **Backend + frontend tests**
- ✅ **Policy-as-code checks** (Conftest + Rego), e.g., metadata/license requirements
- ✅ **(Optional) Build steps** like Docker image builds/pushes after merges

Local actions let us implement these checks once, then reuse them across multiple workflows (backend, frontend, docs, data) without copy/paste drift.

> [!TIP]
> Keep workflows boring. Put reusable logic here. Put “what runs when” in `.github/workflows/*.yml`. 😌

---

## 🧱 How this fits into KFM CI

```mermaid
flowchart LR
  PR[Pull Request] --> Lint[Lint & Format Checks]
  Lint --> Tests[Unit / Integration Tests]
  Tests --> Policy[Policy-as-Code (Conftest)]
  Policy --> Build[Build (optional)]
  Build --> Deploy[Deploy (optional)]
```

---

## 📁 Directory conventions

Each action lives in its own folder:

```
.github/
  workflows/                 # CI/CD entrypoints (pipelines)
  actions/                   # Reusable building blocks (this folder)
    <action-name>/           # kebab-case
      action.yml             # required
      README.md              # required (usage + inputs/outputs)
      scripts/               # optional (bash/python/node helpers)
      tests/                 # optional (self-tests)
```

### ✅ Naming rules

- Use **kebab-case**: `policy-conftest`, `python-quality`, `docker-buildx`
- Prefer **verbs**: `run-*`, `validate-*`, `setup-*`
- Keep actions **single-responsibility** (small + composable) 🧩

---

## 🧩 Action standards

### Composite actions by default 🧰

Prefer composite actions unless you **must** ship a Docker container.

Composite checklist:

- ✅ `runs.using: "composite"`
- ✅ Shell steps use `bash` + `set -euo pipefail`
- ✅ Inputs are documented (with sane defaults)
- ✅ Behavior is deterministic (pin versions; avoid floating tags)
- ✅ No secrets printed (ever) 🔒

### Pin external actions 🔒

When workflows use third‑party actions, prefer pinning by **commit SHA** (supply‑chain hygiene).
If you use tags, document why in the workflow.

### Logs that are easy to read 👀

Use GitHub log groups:

```bash
echo "::group::Conftest policy checks"
# ...
echo "::endgroup::"
```

…and add failure output that answers: **what failed + how to fix locally**.

---

## ➕ Creating a new action

1. Create a folder:

   ```
   .github/actions/<action-name>/
   ```

2. Add `action.yml`.
3. Add `README.md` for that action (copy template below).
4. Wire it into one or more workflows in `../workflows/`.
5. Update **Action Catalog** in *this* README.

> [!IMPORTANT]
> If an action enforces governance (policies / provenance / metadata), treat changes like API changes:
> update docs + keep backward compatibility when possible. 🧾

---

## 🧪 Debugging CI locally

Even with GitHub Actions, you should be able to reproduce most failures locally.

### Backend tests 🐍

```bash
docker-compose exec api pytest
```

### Frontend checks 🌐 (example)

```bash
docker-compose exec web npm test
docker-compose exec web npm run lint -- --fix
```

### Policy checks 🛡️ (Conftest)

```bash
conftest test .
# or narrow to a target:
conftest test data/processed/some_dataset.*
```

> [!NOTE]
> If CI fails on a policy rule (e.g., “dataset missing license”), the fix is usually in metadata (or a missing artifact), not in code.

---

## 🗂️ Action Catalog

> [!TIP]
> Keep this table current — it becomes the “API surface” of our CI building blocks. 🧠

| Action 📦 | What it does ✅ | Used by 🔁 | Status 🚦 |
|---|---|---|---|
| *(add yours)* | *(describe in 1 line)* | `ci.yml`, `policy.yml`, … | 🟡 planned |
| `policy-conftest` | Run Rego policy checks via Conftest | PR validation | 🟡 planned |
| `python-quality` | Run `black/flake8` + `pytest` (or call `make ci-python`) | Backend CI | 🟡 planned |
| `frontend-quality` | Run `npm ci` + `npm test` + `npm run build` | Frontend CI | 🟡 planned |
| `docs-quality` | Markdown lint + front‑matter validation + link checks | Docs CI | 🟡 planned |
| `docker-buildx` | Build (and optionally push) Docker images | Main branch | 🟡 planned |

---

## 🧾 Template: `action.yml` (composite)

```yaml
name: "Example Action"
description: "One-line description of what this action does"

inputs:
  example_input:
    description: "What this input controls"
    required: false
    default: "true"

runs:
  using: "composite"
  steps:
    - name: Do the thing
      shell: bash
      run: |
        set -euo pipefail
        echo "Running example action..."
```

---

## 📄 Template: per-action `README.md`

Each action folder should include a minimal README containing:

- 🎯 Purpose (what it does / why it exists)
- 🧾 Inputs / outputs (table preferred)
- 🧪 Example usage snippet (`uses: ./.github/actions/<name>`)
- 🧰 “Run locally” instructions
- 🧯 Failure modes (“If you see X, do Y”)

---

## 🔐 Security + permissions checklist

- 🔒 Follow least privilege in workflows (`permissions:` minimized)
- 🧯 Don’t echo secrets; avoid `set -x`
- 🧾 Prefer verified/pinned dependencies
- 🧪 Validate inputs (don’t trust workflow-provided strings blindly)
- 🧹 Avoid writing untrusted input into `$GITHUB_ENV` or `$GITHUB_OUTPUT` without sanitizing

---

## 🔗 Related

- CI entrypoints: [`../workflows/`](../workflows/)
- Governance policies: [`../../policy/`](../../policy/)
- Developer workflow: [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md)