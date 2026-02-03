# 🧪 E2E Tests (Playwright) — Kansas Frontier Matrix

![E2E](https://img.shields.io/badge/tests-e2e-blue)
![Runner](https://img.shields.io/badge/runner-playwright-2ea44f)
![Target](https://img.shields.io/badge/target-web%20%E2%86%94%20api%20%E2%86%94%20db-orange)
![CI](https://img.shields.io/badge/ci-github%20actions-black)

End-to-end (E2E) tests validate **real user journeys** across the full KFM stack:
**Browser ➜ Web UI ➜ API ➜ Data services (PostGIS/Neo4j/etc.)**.

This suite is intentionally opinionated toward KFM’s core promises:
- ✅ **Evidence-first UX** (provenance, citations, traceability)
- ✅ **Fail-closed governance** (RBAC + OPA policy gates)
- ✅ **Map-centric reliability** (MapLibre/Cesium flows without flaky pixel tests)

---

## 📌 Table of Contents
- [🎯 What “E2E” means here](#-what-e2e-means-here)
- [⚡ Quick Start](#-quick-start)
- [🧩 Environment variables](#-environment-variables)
- [🗂️ Folder layout](#️-folder-layout)
- [🧪 Test suites](#-test-suites)
- [✍️ Writing tests](#️-writing-tests)
- [🤖 CI (GitHub Actions)](#-ci-github-actions)
- [🧯 Troubleshooting](#-troubleshooting)

---

## 🎯 What “E2E” means here

**End-to-End** tests are the last line of defense before merge/release:
- We load the **real web app** (or a build that behaves the same way).
- We interact like a user (click, search, toggle layers, submit Focus Mode queries).
- We assert:
  - UI state and UX outcomes
  - API contracts (HTTP status + payload shape)
  - security behavior (RBAC/OPA denial)
  - provenance/citation visibility in the UI

> [!NOTE]
> E2E tests should NOT replace unit/integration tests.
> Think: **few, high-value workflows** that break loudly when the product breaks.

---

## ⚡ Quick Start

### 1) Bring up the dev stack (Docker)
From repo root:

```bash
docker compose up -d
```

Common ports (typical KFM dev defaults):
- 🌐 Web: `http://localhost:3000`
- 🧠 API (FastAPI docs): `http://localhost:8000/docs`
- 🗄️ Postgres/PostGIS: `localhost:5432`
- 🕸️ Neo4j: `localhost:7474`

Sanity check:
- Open `http://localhost:8000/docs` to confirm the API is alive.
- Open the web app and confirm it can reach the API.

### 2) Install E2E dependencies
```bash
cd tests/e2e
npm ci
npx playwright install --with-deps
```

### 3) Configure environment
```bash
cp .env.example .env
```

### 4) Run tests
```bash
npm run e2e
```

Debug mode (headed + inspector):
```bash
npm run e2e:debug
```

UI mode (great for authoring):
```bash
npm run e2e:ui
```

---

## 🧩 Environment variables

We keep E2E config explicit so the same suite can run:
- locally (Docker)
- in CI (GitHub Actions)
- against a staging environment (optional)

Example `.env` (inside `tests/e2e/`):

```bash
# Web and API endpoints
E2E_BASE_URL=http://localhost:3000
E2E_API_URL=http://localhost:8000

# Optional: test users (recommended)
E2E_USER_EMAIL=e2e.viewer@local
E2E_USER_PASSWORD=viewer_password

E2E_ADMIN_EMAIL=e2e.admin@local
E2E_ADMIN_PASSWORD=admin_password

# Optional: control flake sources
E2E_DISABLE_ANIMATIONS=1
E2E_TRACE=on
E2E_VIDEO=retain-on-failure
```

> [!WARNING]
> Never use real credentials in E2E.
> Use seeded local users (or CI secrets) and keep permissions minimal.

---

## 🗂️ Folder layout

Suggested structure (keep it boring and consistent ✅):

```text
📁 tests/
  📁 e2e/
    📄 README.md               ← you are here
    📄 package.json            ← playwright + scripts
    📄 playwright.config.ts
    📁 tests/
      🧪 smoke.spec.ts
      🧪 map-layers.spec.ts
      🧪 focus-mode.spec.ts
      🧪 policy-rbac-opa.spec.ts
    📁 fixtures/
      🧷 users.json
      🧷 e2e-seed.sql
      🧷 mini-catalog.json
    📁 pages/                  ← page objects (recommended)
      📄 app.page.ts
      📄 map.page.ts
      📄 focusMode.page.ts
    📁 utils/
      🧰 api.ts
      🧰 selectors.ts
      🧰 wait.ts
```

---

## 🧪 Test suites

### ✅ Smoke (`@smoke`)
Run fast, run often:
- App loads
- API reachable
- “core chrome” visible (map container, nav/search, layer list)

### 🗺️ Map & layers
KFM is map-centric, so we validate:
- Layer toggles update the map state
- Legends or layer metadata appear
- Minimal “map is alive” checks (without brittle pixel assertions)

**Anti-flake rule:** avoid assertions like “pixel X is blue”.
Prefer:
- element visibility + stable UI state
- API-driven expectations (feature count, layer present, request completed)

### 🧠 Focus Mode / RAG flows
Validate user value + trust surface:
- Query submission works
- Response renders
- Citations / sources panel exists (and is non-empty)
- Policy behaviors: prompt injection attempts are handled safely (no UI leakage)

### 🛡️ Policy / RBAC / OPA (fail-closed)
A small number of high-signal checks:
- public user cannot access restricted pages/features
- contributor/admin differences are enforced
- “missing metadata / forbidden dataset” is blocked (where applicable)

---

## ✍️ Writing tests

### ✅ Selector strategy (mandatory)
Use stable selectors in the web UI:
- `data-testid="kfm-map"`
- `data-testid="layer-toggle-historic-trails"`
- `data-testid="focus-mode-input"`

Do **not** target:
- autogenerated classnames
- deep CSS selectors
- fragile text content (unless the text is a product requirement)

Example:
```ts
await page.getByTestId('focus-mode-input').fill('What changed in 1880?');
await page.getByTestId('focus-mode-submit').click();
await expect(page.getByTestId('focus-mode-answer')).toBeVisible();
```

### 🗺️ MapLibre/Cesium: keep assertions deterministic
Recommended patterns:
- Wait for UI “ready” states (loading spinner disappears)
- Assert layer toggles change the **legend** or **layer list state**
- When you must validate map output, validate **data-driven** outcomes:
  - API request fired for tiles/features
  - selected feature panel shows expected IDs/metadata
  - timeline filter reduces result count

> [!TIP]
> Consider exposing a dev-only hook like `window.__KFM__` with a small, safe test surface
> (e.g., current map mode, active layers, last query metadata). This dramatically reduces flake.

### 🧱 Test data: prefer a “mini KFM world”
E2E tests need **predictable data**:
- a small set of curated datasets
- seeded users with known roles
- stable time ranges and bounding boxes

Good: `fixtures/mini-catalog.json` + seed step  
Bad: “whatever is currently in the DB” (flake city 😅)

---

## 🤖 CI (GitHub Actions)

<details>
<summary>📦 Example workflow snippet</summary>

```yaml
name: e2e

on:
  pull_request:
  push:
    branches: [main]

jobs:
  e2e:
    runs-on: ubuntu-latest
    timeout-minutes: 30

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: "20"

      # Bring up KFM stack
      - name: Start stack
        run: docker compose up -d --build

      # Wait for API docs page (simple readiness probe)
      - name: Wait for API
        run: |
          for i in {1..60}; do
            if curl -fsS http://localhost:8000/docs >/dev/null; then
              exit 0
            fi
            sleep 2
          done
          echo "API did not become ready in time"
          docker compose ps
          docker compose logs --no-color | tail -n 200
          exit 1

      - name: Install e2e deps
        working-directory: tests/e2e
        run: |
          npm ci
          npx playwright install --with-deps

      - name: Run e2e
        working-directory: tests/e2e
        env:
          E2E_BASE_URL: http://localhost:3000
          E2E_API_URL: http://localhost:8000
        run: npm run e2e

      - name: Upload Playwright report
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: playwright-report
          path: tests/e2e/playwright-report

      - name: Shutdown stack
        if: always()
        run: docker compose down -v
```
</details>

---

## 🧯 Troubleshooting

### 🧷 Port conflicts (5432 / 7474 / 8000 / 3000)
If you already have services running locally, you may see bind errors.
Fix options:
- stop the local service
- or change host port mappings in `docker-compose.yml`

### 🐢 Containers slow / OOM / killed
Map + DB + search can be heavy.
- increase Docker memory
- reduce dataset size for E2E seed pack
- keep E2E stack minimal (only services needed for tests)

### 🧊 Flaky UI due to animations / WebGL timing
- disable animations for tests (CSS + `prefers-reduced-motion`)
- avoid pixel-based map assertions
- keep 3D tests separate (or skip in CI if GPU acceleration isn’t available)

### 🔌 “Web loads but API calls fail”
- confirm API: `http://localhost:8000/docs`
- confirm proxy/CORS env vars (see `.env.example` in repo root)
- check `docker compose logs api` and `docker compose logs web`

---

## ✅ Definition of Done (DoD) for new E2E tests

- [ ] Uses `data-testid` selectors
- [ ] Deterministic data (seeded fixtures)
- [ ] Produces useful artifacts (trace/video on failure)
- [ ] Fast enough to run on PRs (keep non-critical suites optional)
- [ ] Validates a real user-facing promise (not implementation trivia)