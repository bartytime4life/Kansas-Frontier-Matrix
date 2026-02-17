# UI Tests (KFM) — `tests/ui/`

![Governed](https://img.shields.io/badge/Governed-Evidence--first-2955C)
![UI](https://img.shields.io/badge/UI-Map--first-Orange)
![E2E](https://img.shields.io/badge/E2E-Playwright-informational)
![A11y](https://img.shields.io/badge/A11y-WCAG%202.2%20AA-important)

Governed end-to-end and UI-integration tests for Kansas Frontier Matrix (KFM).

> ⚠️ **Governance note**
>
> UI tests are *governed artifacts* when they validate behavior that affects public narratives, datasets, or sensitive locations.
> - Do **not** bypass the **trust membrane** (no direct DB/object-store access).
> - Do **not** introduce or leak sensitive coordinates/PII in fixtures, traces, videos, or screenshots.
> - Prefer **synthetic** or explicitly **public** test datasets and enforce redaction checks.

---

## Table of Contents

- [What lives here](#what-lives-here)
- [Core principles](#core-principles)
- [Tooling](#tooling)
- [Directory layout](#directory-layout)
- [Quick start](#quick-start)
- [Environment variables](#environment-variables)
- [Writing good UI tests](#writing-good-ui-tests)
- [Map & WebGL guidance](#map--webgl-guidance)
- [Governance and sensitivity rules](#governance-and-sensitivity-rules)
- [Accessibility testing](#accessibility-testing)
- [CI expectations](#ci-expectations)
- [Troubleshooting](#troubleshooting)
- [Related docs](#related-docs)

---

## What lives here

This folder is for UI-level tests that validate **user-visible, contract-driven behavior** across the KFM web experiences:

- Map-first UI (MapLibre GL JS)
- 3D/terrain/globe UI (CesiumJS) *(if enabled in the running app)*
- Story Nodes (narrative rail + map/timeline synchronization)
- Focus Mode UI behaviors (citation drawer, “not confirmed” labeling, offline-first behaviors) *(when present)*

**Out of scope (usually elsewhere):**
- Pure unit tests for domain logic
- Backend contract tests (OpenAPI/GraphQL)
- Data pipeline QA gates (STAC/DCAT/PROV validation)

---

## Core principles

| Principle | What it means in tests | Practical rule |
|---|---|---|
| Trust membrane | UI behaves like a real client | Only call the governed API base URL; block unexpected egress |
| Evidence-first UX | Claims are traceable | Verify citation/provenance UI surfaces exist where required |
| Deterministic | CI must be stable | Avoid flaky waits; prefer explicit “idle/ready” signals |
| Safety | Avoid harm & leakage | Scrub artifacts; use public/synthetic fixtures only |
| Accessibility | Keyboard + screen readers | Include automated a11y checks + a small manual checklist |

---

## Tooling

KFM’s UI automation should use **Playwright** for browser-level coverage, including WebGL map/globe workflows.

> If your repo currently uses a different runner (Cypress/Webdriver/etc.), keep this README as the target state and align scripts/configs accordingly.

**Suggested layers (not all may be present yet):**

| Layer | Typical target | Suggested tool(s) |
|---|---|---|
| Smoke E2E | “App boots + map renders + basic navigation” | Playwright |
| Map/Story E2E | Timeline + layers + Story Node navigation | Playwright |
| Visual regression (scoped) | Map overlay placement / key UI panels | Playwright screenshots (goldens) |
| Offline checks (scoped) | Service worker/cache behavior | Playwright + network offline |
| A11y checks | WCAG/WAI-ARIA regressions | axe (via Playwright) + manual passes |

---

## Directory layout

> This is the **intended** layout. If you don’t have these yet, add them incrementally.

```text
tests/
  ui/
    README.md
    playwright.config.ts              # (recommended) unified config
    package.json                      # (optional) if tests are isolated
    specs/
      smoke.spec.ts
      map/
        layer-toggle.spec.ts
        timeline-scrub.spec.ts
      story/
        story-node-navigation.spec.ts
      focus/
        focus-mode-citations.spec.ts
    fixtures/
      users.json
      public-datasets.json
      story-nodes/
    helpers/
      selectors.ts
      api.ts
      waiters.ts
      maplibre.ts
      cesium.ts
    snapshots/                        # golden screenshots (scoped!)
    artifacts/                        # test output (gitignored)
      traces/
      videos/
      screenshots/
```

---

## Quick start

### 1) Start the KFM stack (local)

Use your project’s local orchestration (often Docker Compose). Example:

```bash
# from repo root (example)
docker compose up -d
```

Confirm you can open the web app in a browser.

### 2) Install test deps

If `tests/ui` is its own package:

```bash
cd tests/ui
npm ci
npx playwright install --with-deps
```

If UI tests are part of a monorepo, use the workspace tool your repo standardizes on (npm/pnpm/yarn) and run the equivalent install.

### 3) Run tests

```bash
# from tests/ui
BASE_URL="http://localhost:3000" npx playwright test
```

Run a small suite:

```bash
npx playwright test specs/smoke.spec.ts
```

Open the Playwright report:

```bash
npx playwright show-report
```

---

## Environment variables

| Variable | Example | Purpose |
|---|---|---|
| `BASE_URL` | `http://localhost:3000` | Web app under test |
| `API_BASE_URL` | `http://localhost:8000` | Governed API base (optional if app derives it) |
| `KFM_TEST_PROFILE` | `local` / `ci` | Toggle timeouts, retries, artifact retention |
| `KFM_TEST_USER` | `test.user@example.org` | Test account (must be non-production) |
| `KFM_TEST_PASSWORD` | `***` | Supplied via secrets in CI |
| `KFM_DATASET_SET` | `public_minimal` | Forces known-safe dataset bundle |
| `KFM_BLOCK_EGRESS` | `1` | Block non-allowlisted network traffic (recommended) |

<details>
<summary><strong>Recommended: network allowlist in Playwright</strong></summary>

Use a strict allowlist so UI tests *cannot* accidentally call raw object storage, third-party endpoints, or internal services.

```ts
// helpers/network-allowlist.ts (example)
const ALLOW = [
  process.env.BASE_URL!,
  process.env.API_BASE_URL!,
  "https://fonts.gstatic.com", // if needed
];

export function isAllowed(url: string) {
  return ALLOW.some(prefix => url.startsWith(prefix));
}
```

```ts
// in a test setup (example)
await page.route("**/*", async (route) => {
  const url = route.request().url();
  if (!isAllowed(url)) return route.abort();
  return route.continue();
});
```

</details>

---

## Writing good UI tests

### Conventions

- **Spec naming:** `feature.area.behavior.spec.ts`
- **Prefer user-facing assertions:** “Provenance drawer shows a dataset badge” > “function X called”
- **Avoid brittle selectors:** prefer `data-testid` or accessible roles/labels

**Selector standard (recommended):**

```tsx
<button data-testid="layer-toggle-historic-trails">Historic Trails</button>
```

```ts
await page.getByTestId("layer-toggle-historic-trails").click();
```

### Anti-flake checklist ✅

- [ ] Wait on explicit app signals (e.g., “map idle”, “layers loaded”) not arbitrary sleeps
- [ ] Freeze time where needed (use Playwright time mocking if applicable)
- [ ] Fix viewport size for screenshots
- [ ] Disable animations/transitions in test mode (CSS class or config flag)
- [ ] Use deterministic test datasets and stable Story Node fixtures

---

## Map & WebGL guidance

Map/globe UIs are **high-value** and **high-flake** if tested naïvely. Keep these rules:

### 1) Prefer “camera-path” snapshot tests only where necessary

Visual tests should be:
- **few**
- **focused**
- **deterministic**

Good snapshot targets:
- overlay badge placement
- legend/provenance drawer
- Story Node keyframes

Bad snapshot targets:
- full basemap tiles (often non-deterministic)
- animated transitions
- dense label fields

### 2) Stabilize render conditions

Recommended settings:
- fixed viewport (e.g., 1280×720)
- fixed device scale factor
- disable motion (reduce animations)
- wait for “idle” signals before asserting

<details>
<summary><strong>Example: wait for MapLibre “idle”</strong></summary>

```ts
// helpers/maplibre.ts (example approach)
// Requires your app to expose a test hook OR for you to wait on a DOM signal
export async function waitForMapIdle(page) {
  await page.waitForFunction(() => (window as any).__KFM_TEST__?.mapIdle === true);
}
```

</details>

### 3) Don’t assert raw coordinates unless the feature is explicitly non-sensitive

If a UI shows coordinates:
- tests must validate **redaction/generalization** rules for protected content
- tests must validate role-based access (authorized vs unauthorized views)

---

## Governance and sensitivity rules

### Test data rules (hard gate)

- ✅ Use **synthetic** fixtures or explicitly **public** datasets
- ✅ Keep any real place/person references generic unless they are in approved public corpora
- ❌ No private individuals’ data
- ❌ No precise site locations that increase risk
- ❌ No “real” API tokens committed to git

### Artifact hygiene (hard gate)

Before uploading CI artifacts (traces/videos/screenshots):
- [ ] Strip query strings containing tokens
- [ ] Mask emails/usernames unless they are test-only accounts
- [ ] Avoid screenshots that expose sensitive layers/coordinates
- [ ] Prefer short retention for artifacts in CI (esp. PRs from forks)

---

## Accessibility testing

Minimum expectations:
- keyboard operability (tab order, visible focus)
- meaningful ARIA labels for dynamic controls
- no focus traps when hiding/showing panels
- “Exit Focus Mode” is always reachable by keyboard (if Focus Mode exists)

Automate what you can (axe), but maintain a small manual checklist:

- [ ] Can complete core flows without a mouse
- [ ] Focus indicator is visible on interactive elements
- [ ] Dialogs trap focus appropriately and restore focus on close
- [ ] Live regions don’t spam announcements (timers especially)

---

## CI expectations

UI tests should run in CI in a **repeatable** environment.

### Suggested CI stages

```mermaid
flowchart LR
  A[Lint + Typecheck] --> B[Unit/Component Tests]
  B --> C[Spin up KFM stack (ephemeral)]
  C --> D[UI E2E (Playwright)]
  D --> E[Upload sanitized artifacts]
  E --> F[Publish report + status]
```

### Required pass/fail signals

- Smoke suite passes on every PR
- Flake rate is monitored (retries are not a substitute for stability)
- Visual diffs require explicit review (goldens updated intentionally)

---

## Troubleshooting

<details>
<summary><strong>WebGL screenshot diffs across machines</strong></summary>

- Ensure fixed viewport and disabled animations
- Prefer running CI with consistent browser + flags
- Keep screenshot scope small (UI panels > full basemaps)
</details>

<details>
<summary><strong>Tests hang waiting for “map ready”</strong></summary>

- Verify the app exposes a test hook or DOM-ready signal
- Add explicit waits for layer load events (not time-based sleeps)
- Confirm the dataset set is available and API is reachable
</details>

<details>
<summary><strong>Service worker/offline tests behave inconsistently</strong></summary>

- Use a clean browser context per test
- Clear storage between tests (IndexedDB/localStorage)
- Prefer a dedicated “offline.spec.ts” suite that runs serially
</details>

---

## Related docs

These docs (if present in your repo) define the expectations these tests enforce:

- `docs/architecture/*` — trust membrane, API contracts, client boundaries
- `docs/patterns/*` — UI patterns (Story Nodes, Focus Mode, provenance UX)
- `schemas/*` — JSON Schemas that UI events/features must validate against
- `web/*` — UI implementation (React/TypeScript + MapLibre/Cesium integrations)

---

## Definition of Done for new UI test coverage ✅

When adding a new UI feature or workflow, ensure:

- [ ] A smoke or happy-path test exists (Playwright)
- [ ] Sensitive info is not exposed in logs/screenshots/traces
- [ ] Provenance/citation UI is validated where the feature surfaces claims/layers
- [ ] Accessibility check added (automated and/or manual checklist updated)
- [ ] Tests run headless in CI and are stable (no arbitrary sleeps)
- [ ] If a schema is involved, fixtures validate and CI enforces validation