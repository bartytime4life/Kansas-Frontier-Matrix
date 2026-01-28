# 🧰 `setup-kfm` — GitHub Action (Composite)

![GitHub Action](https://img.shields.io/badge/GitHub%20Action-composite-2ea44f)
![Scope](https://img.shields.io/badge/scope-internal%20CI%2FCD-blue)
![KFM](https://img.shields.io/badge/KFM-provenance--first-7a5cff)

A **local composite action** used by KFM workflows to standardize CI setup across jobs (Python 🐍 + Node 🟩 + policy checks 🛡️ + optional Docker 🐳).

> ✅ Use this to keep workflow files clean, consistent, and reproducible across the repo.

---

## 📁 Where this lives

```text
📦 .github/
└── ⚙️ actions/
    └── 🧰 setup-kfm/
        ├── action.yml
        └── README.md   👈 you are here
```

---

## ✨ What this action does

Depending on the inputs you enable, `setup-kfm` typically:

- 🐍 Sets up **Python** for the backend (tests, lint, tooling)
- 🟩 Sets up **Node.js** for the frontend (tests, lint, builds)
- 🧠 Warms up **dependency caches** (pip/poetry/uv + npm/pnpm/yarn) for faster CI
- 🗺️ Installs common **geospatial system dependencies** (optional) for GIS-heavy Python packages
- 🛡️ Installs **Conftest/OPA tooling** (optional) for policy & compliance checks
- 🐳 Optionally boots a **Docker Compose** stack for integration tests (PostGIS/Neo4j/API/Web)

> 🎯 Goal: one reusable “setup step” across `lint`, `test`, `build`, and `policy` workflows.

---

## ✅ Requirements

- **Checkout first**: you should run `actions/checkout` before using this action.
- **Recommended runner**: `ubuntu-latest` (best support for apt-based system deps and Docker).
- **Docker**: only required if you enable Compose-based integration tests.

---

## 🚀 Quickstart

### Minimal (Python + Node)

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: 📥 Checkout
        uses: actions/checkout@v4

      - name: 🧰 Setup KFM
        uses: ./.github/actions/setup-kfm
        with:
          python-version: "3.11"
          node-version: "20"
          cache: "true"

      - name: 🧪 Backend tests
        working-directory: api
        run: pytest -q

      - name: 🧪 Frontend tests
        working-directory: web
        run: npm test -- --watch=false
```

### With Docker Compose (integration-style)

```yaml
jobs:
  integration:
    runs-on: ubuntu-latest
    steps:
      - name: 📥 Checkout
        uses: actions/checkout@v4

      - name: 🧰 Setup KFM (Compose)
        uses: ./.github/actions/setup-kfm
        with:
          enable-docker-compose: "true"
          compose-file: "docker-compose.yml"
          compose-up-args: "--build -d"

      - name: 🧪 API tests (inside container)
        run: docker compose exec -T api pytest -q
```

---

## 🔧 Inputs

> **Source of truth:** `action.yml` ✅  
> This table documents the **intended contract**. If you change behavior, update both `action.yml` + this README.

| Input | Type | Default | What it controls |
|------|------|---------|------------------|
| `python-version` | string | `3.11` | Python version for backend tooling/tests |
| `node-version` | string | `20` | Node version for frontend tooling/tests |
| `cache` | string (`"true"`/`"false"`) | `"true"` | Enables dependency caching |
| `backend-path` | string | `api` | Backend directory |
| `frontend-path` | string | `web` | Frontend directory |
| `install-backend` | string | `"true"` | Install backend deps (pip/poetry/uv) |
| `install-frontend` | string | `"true"` | Install frontend deps (npm/pnpm/yarn) |
| `install-geospatial-deps` | string | `"false"` | Installs GIS system packages (GDAL/GEOS/PROJ, etc.) |
| `enable-conftest` | string | `"true"` | Installs/uses Conftest policy tooling |
| `conftest-version` | string | `"latest"` | Pins Conftest version (recommended for stability) |
| `enable-docker-compose` | string | `"false"` | Brings up Docker Compose services |
| `compose-file` | string | `docker-compose.yml` | Compose file path |
| `compose-up-args` | string | `--build -d` | Args passed to `docker compose up` |
| `compose-services` | string | `""` | Optional service list (space-separated); empty = all |

---

## 📤 Outputs

If implemented in `action.yml`, these outputs help downstream steps:

| Output | Example | Notes |
|--------|---------|------|
| `python-version` | `3.11.7` | Resolved version installed |
| `node-version` | `20.11.1` | Resolved version installed |
| `conftest-version` | `0.56.0` | Useful when pinned |
| `cache-hit-python` | `true` | If using `actions/cache` |
| `cache-hit-node` | `true` | If using `actions/cache` |

---

## 🧪 Common CI patterns (copy/paste)

<details>
<summary><strong>🧹 Lint (Python + JS)</strong></summary>

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: ./.github/actions/setup-kfm
        with:
          python-version: "3.11"
          node-version: "20"
          cache: "true"

      - name: 🐍 Python format/lint
        working-directory: api
        run: |
          black --check .
          flake8 .

      - name: 🟩 JS lint
        working-directory: web
        run: npm run lint
```
</details>

<details>
<summary><strong>🛡️ Policy gate (Conftest)</strong></summary>

```yaml
jobs:
  policy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: ./.github/actions/setup-kfm
        with:
          enable-conftest: "true"
          conftest-version: "latest"

      - name: 🛡️ Run policy checks
        run: conftest test .
```
</details>

<details>
<summary><strong>🐳 Integration tests (Compose stack)</strong></summary>

```yaml
jobs:
  integration:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: ./.github/actions/setup-kfm
        with:
          enable-docker-compose: "true"
          compose-file: "docker-compose.yml"
          compose-up-args: "--build -d"
          # compose-services: "db graph api"   # optional

      - name: 🔎 Show running containers
        run: docker compose ps

      - name: 🧪 API tests in container
        run: docker compose exec -T api pytest -q

      - name: 🧾 Logs on failure
        if: failure()
        run: docker compose logs --no-color --tail=200
```
</details>

---

## 🧠 Why KFM uses this (design intent)

KFM’s CI commonly runs a mix of:

- 🧪 **Backend tests** (`pytest`)
- 🧪 **Frontend tests** (`npm test` or equivalent)
- 🧹 **Linters/formatters** (e.g., `black`, `flake8`, `eslint`, `prettier`)
- 🛡️ **Policy checks** (e.g., `conftest test .` to validate repository rules, metadata, governance)

This action exists so those workflows don’t each reinvent environment setup.

---

## 🧯 Troubleshooting

### 🗺️ “GDAL/GEOS/PROJ build failed” (Python geospatial deps)
- Enable `install-geospatial-deps: "true"` (if supported)
- Confirm you’re running on `ubuntu-latest`
- If you pin wheels or use `pyproject.toml`, ensure CI installs the matching system libs

### 🐳 Docker Compose is flaky / services not ready
- Add a small health/wait step (polling DB ports) before running tests
- Always print logs on failure:
  - `docker compose logs --tail=200 --no-color`

### 🧊 Cache not helping
- Ensure cache keys include lockfiles (`poetry.lock`, `requirements*.txt`, `package-lock.json`, `pnpm-lock.yaml`, etc.)
- Don’t mix `npm install` and `npm ci` across runs (prefer **`npm ci`** in CI)

---

## 🔐 Security notes

- ✅ Prefer pinning third-party actions (when used) to a SHA for supply-chain safety
- 🚫 Never echo secrets into logs
- 🧽 Keep “setup” steps separate from “deploy” steps so permissions remain minimal

---

## 🧩 Maintenance checklist

- [ ] If you change inputs/outputs in `action.yml`, update this README
- [ ] Keep tool versions pinned where CI stability matters
- [ ] Add a small test workflow that only validates this action runs end-to-end

---

## 📜 License

This is an internal repo action. The project’s root `LICENSE` applies unless stated otherwise.
