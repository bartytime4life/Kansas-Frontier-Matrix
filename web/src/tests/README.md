---
title: "Web UI Test Suite (web/src/tests)"
path: "web/src/tests/README.md"
version: "v0.1.0"
last_updated: "2026-01-14"
status: "draft"
doc_kind: "Runbook"
license: "TBD"
markdown_protocol_version: "1.0"
pipeline_contract_version: "v13"

# Governance / FAIR+CARE (align with repo-wide policies)
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"

doc_uuid: "urn:kfm:doc:web:tests:v0.1.0"
commit_sha: "TBD"
doc_integrity_checksum: "sha256:TBD"
---

# 🧪 Web UI Tests — `web/src/tests/`

![scope](https://img.shields.io/badge/scope-web%2Fsrc%2Ftests-blue)
![ui](https://img.shields.io/badge/ui-React%20%2B%20MapLibre-success)
![contracts](https://img.shields.io/badge/contract--first-required-brightgreen)
![provenance](https://img.shields.io/badge/provenance--first-required-8A2BE2)
![e2e](https://img.shields.io/badge/e2e-Cypress-00BFA5)

> 🎯 Goal: Keep the **map + narrative UI** correct, deterministic, and governance-compliant—especially around **contracts, provenance, and safety**.

---

## 🔎 What lives here

This folder contains **UI-focused automated tests** for code under `web/src/**`:
- ✅ Unit tests for pure utilities/helpers
- ✅ Component tests for React UI (render + interactions)
- ✅ Integration tests that stitch UI ↔ mocked API ↔ mocked map viewer
- ✅ “Governance invariants” tests (evidence links, safety redactions, opt-in AI labeling)

If you’re looking for cross-system tests (ETL/catalog/graph/API), prefer the repo’s canonical test home:
- 📁 `/tests/` (repo-wide automated tests)

---

## 🧭 Navigation

- [🚀 Quick start](#-quick-start)
- [🗂️ Folder layout](#️-folder-layout)
- [🧱 Test types](#-test-types)
- [🧩 Mocking & fixtures](#-mocking--fixtures)
- [🗺️ Map & 3D viewer testing](#️-map--3d-viewer-testing)
- [⚖️ Governance & safety gates](#️-governance--safety-gates)
- [📈 Performance & regression](#-performance--regression)
- [🧰 Troubleshooting](#-troubleshooting)
- [✅ Definition of Done](#-definition-of-done)
- [📚 Reference links](#-reference-links)

---

## 🚀 Quick start

1) **Install deps**
```bash
# pick the package manager used by this repo
npm ci
# or: pnpm install --frozen-lockfile
# or: yarn install --frozen-lockfile
```

2) **Run UI tests**
```bash
# common patterns — use whatever scripts exist in web/package.json
npm test
npm run test:watch
npm run test:ui
```

3) **Run E2E (if configured)**
```bash
# typically Cypress
npm run e2e
npm run e2e:open
```

> 📝 Tip: If you’re unsure what commands exist, open `web/package.json` and copy the `scripts.*` names.

---

## 🗂️ Folder layout

Suggested structure (adapt to actual repo conventions):

```
📁 web/
  📁 src/
    📁 tests/
      📄 README.md                  # you are here ✅
      📁 fixtures/                  # small, governed test data (GeoJSON, STAC, DCAT, PROV, story nodes)
      📁 mocks/                     # MSW handlers, API stubs, module mocks
      📁 helpers/                   # render helpers, test utils, custom matchers
      📁 setup/                     # test runner setup (dom, polyfills, matchers)
      📁 snapshots/                 # snapshot artifacts (if used)
      📄 *.test.ts                  # unit tests
      📄 *.test.tsx                 # component tests
      📄 *.integration.test.ts(x)   # integration tests
```

**Rules of thumb 🧠**
- Keep **fixtures tiny** and **versionable** (no huge rasters, no secrets).
- Prefer **behavioral assertions** over brittle snapshots.
- Anything that can be expressed as a **schema/contract check** should be a schema/contract check.

---

## 🧱 Test types

### 1) ✅ Unit tests
Use for:
- Parsing/formatting helpers
- Filtering/sorting logic
- Derived-value calculations (legend labels, timeline bucketing, etc.)

Naming:
- `something.test.ts`

### 2) 🧩 Component tests
Use for:
- React components (menus, layer toggles, story panels, charts)
- Accessibility checks (labels, roles, keyboard nav)

Naming:
- `ComponentName.test.tsx`

### 3) 🔌 Integration tests
Use for:
- “Page-level” UI flows with a mocked API
- Contract + provenance requirements (e.g., “dataset card always includes source/prov link”)

Naming:
- `feature.integration.test.tsx`

### 4) 🧾 Contract tests (UI-side)
Even though contracts are defined elsewhere, the UI should validate:
- **Incoming payloads** match expected shapes before rendering
- **Missing provenance** fails gracefully (and visibly)

Typical checks:
- “If `source_ref` is missing, UI must render a ‘Missing provenance’ warning and suppress claim display.”
- “If a Story Node is not in a published state, it must not show up in the public UI.”

### 5) 🧭 E2E tests (Cypress)
Use for:
- Real browser flows: load map, toggle layer, scrub timeline, open story, verify evidence panel

E2E should be:
- **Minimal** (smoke coverage)
- **Stable** (avoid flakiness; don’t test every pixel)
- Focused on **highest-risk journeys** and **governance gates**

---

## 🧩 Mocking & fixtures

### Fixtures ✅
Store canonical, minimal examples:
- GeoJSON FeatureCollection (tiny)
- STAC Item/Collection (tiny)
- DCAT dataset JSON-LD (tiny)
- PROV bundle JSON-LD (tiny)
- Story Node markdown/metadata (tiny)

**Fixture requirements**
- 📌 Include a stable ID (used for test assertions)
- 🧭 Include time range if UI depends on timeline
- 🗺️ Geometries must be valid (no broken polygons; correct CRS expectations)
- ⚠️ Never include secrets, private tokens, or sensitive coordinates

### API mocking (recommended)
- Use **request-level mocking** (e.g., MSW) rather than mocking every fetch call
- Keep handlers close to the feature they support

Example (illustrative):
```ts
// mocks/handlers/datasets.ts
import { http, HttpResponse } from "msw";
import datasetIndex from "../fixtures/api/datasets.index.json";

export const datasetHandlers = [
  http.get("/api/datasets", () => HttpResponse.json(datasetIndex)),
];
```

### Determinism 🍀
Make tests reproducible:
- Freeze time (`Date.now`, timers)
- Seed randomness
- Avoid network and real filesystem access
- Avoid relying on canvas/WebGL unless explicitly testing it

---

## 🗺️ Map & 3D viewer testing

KFM’s UI is map-heavy, and may use:
- **MapLibre GL JS** (2D)
- **CesiumJS** (3D terrain/globe)
- WebGL overlays (layers, markers, heatmaps)

**Preferred testing pyramid**
1) ✅ Unit test “layer config builders” (pure functions)
2) ✅ Component test “Map shell” renders controls + dispatches actions
3) ✅ Integration test “UI state → map intent” (calls layer-add/remove API)
4) 🧪 E2E smoke test “map loads and toggles a layer”

### Practical patterns
- Mock map objects behind a **thin adapter** (e.g., `MapPort` interface).
- Assert “intent” rather than pixels:
  - “Layer X added with opacity 0.7”
  - “Timeline scrub triggers data reload for [t0, t1]”
  - “Click feature opens evidence panel with citations”

<details>
<summary><strong>🧰 Example: adapter-based approach</strong> (click to expand)</summary>

```ts
// viewers/MapPort.ts
export interface MapPort {
  addLayer(spec: unknown): void;
  removeLayer(id: string): void;
  setPaintProperty(layerId: string, key: string, value: unknown): void;
}

// tests/mocks/mockMapPort.ts
export function createMockMapPort(): MapPort & { calls: any[] } {
  const calls: any[] = [];
  return {
    calls,
    addLayer: (spec) => calls.push(["addLayer", spec]),
    removeLayer: (id) => calls.push(["removeLayer", id]),
    setPaintProperty: (layerId, key, value) =>
      calls.push(["setPaintProperty", layerId, key, value]),
  };
}
```

</details>

---

## ⚖️ Governance & safety gates

The UI is not “just a frontend.” It is part of the trust boundary.

### 🧾 Evidence / provenance invariants
Tests should enforce:
- Any claim shown in UI links to governed evidence (catalog + provenance)
- UI must not “invent” facts; it can only summarize what is referenced
- Missing provenance is handled as an error state (not silently ignored)

### 🤖 AI transparency (Focus Mode)
If AI-assisted hints appear:
- Must be **opt-in** (not default)
- Must be clearly labeled as AI-generated
- Must show uncertainty/confidence indicators
- Must respect sensitivity rules

### 🛡️ Sensitive location handling
If sovereignty / sensitivity rules apply:
- UI must generalize or omit protected coordinates
- No “side channel” leaks via hover tooltips, deep links, or dev logs

### 🔐 Security-minded test coverage
Add tests for:
- Rendering untrusted HTML safely (no XSS)
- Input validation on search/filter forms
- Access-control UI states (guest vs authenticated)
- “Don’t leak secrets” checks (no tokens in logs, errors, or serialized state)

---

## 📈 Performance & regression

Performance regressions often show up as:
- Slow map interactions (pan/zoom)
- “Re-render storms” in React
- Excessive network calls when scrubbing the timeline
- Over-fetching large payloads

Suggested guardrails:
- Basic performance assertions in integration tests (e.g., “doesn’t refetch N times”)
- Snapshot only **stable** structures (schemas/config), not DOM noise
- Smoke-level visual regression tests only for critical UI (optional)

---

## 🧰 Troubleshooting

### Flaky tests 😵‍💫
Common causes:
- Uncontrolled timers
- Race conditions in async rendering
- Real WebGL/canvas usage in jsdom
- Real network calls that should be mocked

Fixes:
- Use `await` + explicit waits (not `setTimeout`)
- Mock WebGL/Map adapter
- Freeze time
- Ensure MSW handlers cover all endpoints used by the test

### “Works locally, fails in CI” 🧯
- CI usually runs headless and stricter
- Ensure tests do not rely on GPU, fonts, locale, or timezone
- Pin deterministic fixtures and avoid live data

---

## ✅ Definition of Done

Use this checklist when adding or changing tests:

- [ ] Tests cover the change at the right layer (unit/component/integration/e2e)
- [ ] Any new UI output is backed by contract/provenance expectations
- [ ] Fixtures are small, governed, and non-sensitive
- [ ] No flakiness (deterministic time, stable async)
- [ ] CI-friendly (headless, no GPU assumptions)
- [ ] Documentation updated (this README or feature README, as needed)

---

## 📚 Reference links

Repo-wide guides (update paths if structure changes):
- `../../../docs/MASTER_GUIDE_v13.md` 📘
- `../../../docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` 🧾
- `../../../docs/standards/KFM_STAC_PROFILE.md` 🗺️
- `../../../docs/standards/KFM_DCAT_PROFILE.md` 🧩
- `../../../docs/standards/KFM_PROV_PROFILE.md` 🧬
- `../../../tests/README.md` 🧪 (repo-wide test entrypoint, if present)
