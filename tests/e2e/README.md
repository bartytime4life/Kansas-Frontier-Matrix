# 🧪 End-to-End (E2E) Tests — Kansas Frontier Matrix (KFM)

![E2E](https://img.shields.io/badge/tests-e2e-blue)
![Docker](https://img.shields.io/badge/docker-compose-2496ED?logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/backend-FastAPI-009688?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/frontend-React-61DAFB?logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/lang-TypeScript-3178C6?logo=typescript&logoColor=white)
![PostGIS](https://img.shields.io/badge/db-PostGIS-4169E1?logo=postgresql&logoColor=white)
![Neo4j](https://img.shields.io/badge/graph-Neo4j-008CC1?logo=neo4j&logoColor=white)

> [!IMPORTANT]
> E2E tests are the “prove it works” layer: they validate the **full pipeline → DB → API → UI** behavior (not just isolated functions).
> KFM’s architecture is **provenance-first** and **policy-governed** — this suite should protect those guarantees.

---

## 📍 What lives here?

This folder contains browser-driven “real user flow” tests against a running local stack (Docker Compose).

```text
📦 Kansas-Frontier-Matrix/
└─ 📁 tests/
   └─ 📁 e2e/
      ├─ 📄 README.md                👈 you are here
      ├─ 📁 specs/                   ✅ user journeys (smoke, map, story, search)
      ├─ 📁 fixtures/                🧬 deterministic seed data (small & safe)
      ├─ 📁 helpers/                 🧰 selectors, waits, auth helpers, API helpers
      ├─ 📁 artifacts/               📸 screenshots, traces, videos (gitignored)
      ├─ 📄 playwright.config.ts     (recommended) 🕹️
      └─ 📄 package.json             (if E2E suite is a mini workspace)
```

> [!NOTE]
> If your repo uses Cypress (or another runner), keep the **same conventions** below and just map commands/config accordingly.

---

## 🎯 Goals & scope

### ✅ This suite should catch…
- **UI ↔ API integration breaks** (UI calls fail, schema changes, auth errors)
- **Critical map flows** (Map loads, layers toggle, features selectable)
- **Timeline/story sync issues** (changing time updates map + story panel state)
- **Search + navigation regressions** (search results, story routing, deep links)
- **Governance-facing UX** (licenses/provenance visible where expected; “fail closed” behavior is enforced)

### 🚫 This suite should NOT try to…
- Replace unit tests (keep E2E lean)
- Pixel-perfect validate cartography (canvas maps are hard to assert; use stable signals)
- Load massive datasets (use small fixtures and deterministic seeds)

---

## 🧩 System Under Test (SUT)

KFM is a **monorepo** with a backend API and a React+TypeScript frontend.

Typical local endpoints (from Docker Compose defaults):
- 🌐 **Web UI**: `http://localhost:3000`
- 🧠 **API (FastAPI)**: `http://localhost:8000` (Swagger docs at `/docs`)
- 🗺️ **PostGIS (Postgres)**: `localhost:5432`
- 🕸️ **Neo4j Browser**: `http://localhost:7474`

> [!TIP]
> E2E tests should treat the UI as the user’s entry point.
> The UI must never “talk to the DB directly” — all access must flow through the API.

---

## ⚡ Quickstart (local)

### 1) Start the full stack
From repo root:

```bash
# Newer Docker:
docker compose up -d --build

# Older Docker:
docker-compose up -d --build
```

### 2) Confirm services are up
```bash
# API ready?
curl -fsS http://localhost:8000/docs >/dev/null && echo "✅ API up"

# UI ready? (basic check)
curl -fsS http://localhost:3000 >/dev/null && echo "✅ UI up"
```

### 3) Run E2E tests
Pick one of the following patterns (depends on how the repo is wired):

#### Option A — E2E suite has its own package.json (recommended)
```bash
cd tests/e2e
npm ci
# If using Playwright:
npx playwright install --with-deps
npx playwright test
```

#### Option B — Repo root scripts
```bash
# Examples (use whatever exists in package.json)
npm run test:e2e
# or
pnpm test:e2e
# or
yarn test:e2e
```

> [!WARNING]
> If ports `3000/8000/5432/7474` are already in use, Docker Compose will conflict.
> Stop the conflicting service or change the host port mapping.

---

## 🧠 Recommended runner: Playwright 🕹️

Playwright is a strong fit for KFM because the UI is React + TypeScript, and KFM’s “map + timeline + story” UX benefits from:
- reliable waits
- traces & videos
- multi-browser projects

**Suggested base URL env vars**
```bash
# For local runs
export KFM_WEB_BASE_URL="http://localhost:3000"
export KFM_API_BASE_URL="http://localhost:8000"
```

**Headed mode + debug**
```bash
cd tests/e2e
npx playwright test --headed
npx playwright test --debug
```

**Show HTML report**
```bash
npx playwright show-report
```

---

## 🧪 Test design rules (KFM-flavored)

### 1) Prefer “smoke + critical flows” ✅
Keep E2E lean and meaningful. A good minimum suite:
- **Smoke**: app boots, map mounts, no console errors
- **Layer toggle**: enable “Historic Trails” layer, verify UI state + network call succeeds
- **Timeline**: change year, verify the store-driven UI updates (map + story panel)
- **Feature click**: click a visible feature, verify popup/details panel renders
- **Search**: search for a known term, navigate to a result, verify route loads
- **Provenance**: open a dataset/story detail and verify license/provenance block exists

### 2) Stable selectors only 🧷
Use `data-testid` for all E2E selectors—never fragile CSS chains.

**Suggested test IDs based on KFM UI components**
| UI area | `data-testid` |
|---|---|
| App shell | `app-shell` |
| Map container | `map-viewer` |
| Layer control | `layer-control` |
| Timeline slider | `timeline-slider` |
| Story panel | `story-panel` |
| Search input | `search-input` |
| Search results | `search-results` |
| Dataset panel | `dataset-panel` |
| Provenance block | `provenance-block` |

> [!TIP]
> If MapLibre/Cesium rendering is hard to assert, expose a small readiness hook:
> - `window.__KFM_READY__ = true` after map init
> - or add a hidden `data-testid="map-ready"` element when layers finish loading

### 3) Deterministic test data 🧬
KFM emphasizes reproducibility. E2E tests must be:
- deterministic
- idempotent
- safe to run on CI

**Rules**
- Use small “fixture datasets” checked into `tests/e2e/fixtures/`
- Prefer a dedicated test dataset namespace (e.g., `kfm_e2e_*`)
- Never rely on external APIs unless explicitly mocked/stubbed
- If randomness exists (IDs, timestamps), seed it or normalize it

---

## 🧰 Data seeding strategies

Pick one pattern and stick to it:

### 🟢 Pattern A — Seed via API (preferred)
- Add a `/dev/seed` endpoint guarded by environment (dev/test only)
- E2E calls seed endpoint at test start
- Keeps DB schema + domain rules centralized in backend

### 🟡 Pattern B — Seed via pipeline scripts
- Run a minimal pipeline using files in `data/raw → data/processed`
- Load into PostGIS/Neo4j
- Best when you want to test *the ingestion contract* too

### 🟠 Pattern C — SQL/Cypher direct seed (only for ultra-minimal fixtures)
- Fast but risks bypassing backend validation rules
- If used, keep it tiny and document assumptions

> [!CAUTION]
> Don’t “teach” contributors that bypassing provenance/metadata is okay.
> Even test data should model the pipeline: **Raw → Processed → Catalog/Prov → DB → API → UI**.

---

## 🧯 Flake prevention (maps + async UIs)

Mapping UIs are inherently async. To keep tests stable:

- Wait for **explicit readiness signals** (preferred)
- Assert against **UI state** (layer control toggled, legend item visible)
- Assert against **API responses** (network request returned 200)
- Avoid “sleep(5000)” whenever possible

**Examples of stable waits**
- `waitForResponse()` on key API endpoints (e.g., `/tiles/*`, `/search`, `/datasets`)
- `expect(locator).toBeVisible()` for story panel sections after navigation
- A `map-ready` sentinel in DOM

---

## 📦 Artifacts & debugging

Store artifacts locally for fast debugging:
- screenshots on failure
- traces for flaky tests
- videos for CI

Suggested `.gitignore` entries:
```gitignore
tests/e2e/artifacts/
tests/e2e/playwright-report/
tests/e2e/test-results/
```

---

## 🧬 CI expectations

KFM’s CI philosophy is “**fail closed**”:
- if checks fail, merges are blocked
- tests should be runnable locally in the same way CI runs them

**Recommended pipeline shape**
1. Lint/format (backend + frontend)
2. Unit tests (pytest, frontend tests)
3. Policy checks (e.g., conftest)
4. E2E (headless, artifacts on fail)

> [!NOTE]
> If E2E is too slow for every PR, consider:
> - PR: run “smoke” E2E only
> - Nightly: run full matrix (multi-browser, heavier flows)

---

## 🔗 Related test suites (nearby)

From repo root (common patterns):
```bash
# Backend tests (FastAPI / pytest)
docker-compose exec api pytest

# Frontend tests (React)
cd web && npm test

# Policy checks (Conftest / OPA-style)
conftest test .
```

---

## 🧯 Troubleshooting

### 🔌 Port conflicts
If you see errors binding:
- `5432` (Postgres/PostGIS)
- `7474` (Neo4j)
- `8000` (API)
- `3000` (web)

Stop the conflicting process or remap ports in `docker-compose.yml`.

### 🐳 Docker is slow / containers get killed
- increase Docker memory/CPU
- large datasets can overwhelm default limits (E2E should use small fixtures)

### 🧱 UI doesn’t hot reload / files not updating
If developing alongside E2E runs, ensure the `web/src` volume mount works.
This can be OS-dependent (especially on Windows path mounts).

---

## 🗺️ Roadmap ideas (good “next tests”)

- 🧭 **Deep-link routes**: open `/stories/:id` directly, ensure map sync
- 🧷 **State persistence**: refresh page, verify selected layer/time persists (if intended)
- 🛡️ **Access control**: sensitive layers are hidden unless authorized (CARE compliance)
- 🧾 **Provenance UI**: dataset panel shows license + source citations consistently
- 🧠 **AI assistant “Focus Mode”**: answers include references and refuse forbidden requests

---

## 🤝 Contributing

- Add E2E tests when you introduce a new user-facing flow or a risky integration point.
- Keep tests **readable** and **deterministic**.
- Prefer building small helper utilities over copy/pasting selector logic.

> [!TIP]
> If you’re not sure where a new E2E test belongs, start in `specs/smoke.spec.ts` and refactor into feature files once it grows.