# 🧰 Dev Shared Components (KFM) — `web/src/components/dev/shared/`

![scope](https://img.shields.io/badge/scope-dev--only-orange)
![ui](https://img.shields.io/badge/UI-React%20%2B%20TypeScript-61dafb)
![maps](https://img.shields.io/badge/maps-MapLibre%20%2B%20Cesium-7b68ee)
![principle](https://img.shields.io/badge/principle-provenance--first-2ea44f)

Shared, **developer-only** UI building blocks used across KFM’s internal debug / diagnostics surfaces (panels, inspectors, sandbox pages, and dev utilities).  
These are meant to be **small, composable, and consistent**—think “LEGO bricks” 🧱 for building dev tooling quickly without reinventing layout, formatting, or safety guardrails.

---

## 🧭 Quick links

- ⬆️ Back to repo root: [`../../../../../README.md`](../../../../../README.md)
- 🗺️ Components overview (recommended): `web/src/components/README.md`
- 🧪 Dev tooling entrypoint (recommended): `web/src/components/dev/README.md`

> **Rule of thumb ✅**  
> If a dev page needs a panel, table-ish layout, JSON viewer, code block, key/value rows, or “inspector” chrome—**use components from here** instead of rolling custom UI.

---

## 🎯 Goals

### ✅ What this folder is for
- **Reusable dev UI primitives**: panels, sections, rows, badges, tabs, split panes, toolbars 🧩
- **Data introspection helpers**: JSON rendering, “copy to clipboard”, query previews, request/response viewers 🧾
- **Safety-first debug UX**: redaction helpers, “dev-only” gates, error boundaries 🧯
- **Consistent look & feel**: so all dev tooling feels like one coherent system (even if it’s quick-n-dirty)

### 🚫 What this folder is NOT for
- **Production UI** components (those belong in non-`dev/` component directories)
- **Domain-specific** dev components (maps-only, focus-mode-only, pipeline-only) → put those under `web/src/components/dev/<domain>/`
- Anything that **requires secrets**, prints tokens, or dumps sensitive payloads without redaction 🔒

---

## 🧱 Design principles (keep us sane)

### 1) Dev-only ≠ no standards 🧠
Even dev UI should be:
- Accessible enough to navigate with keyboard
- Deterministic enough to test
- Clear enough to avoid misreads during debugging

### 2) Composition over configuration 🧩
Prefer:
- `DevPanel` + `DevSection` + `DevKV` + `DevJSON`
over:
- one mega component with 40 props

### 3) “One fact, one place” 📍
Shared formatting patterns (timestamps, IDs, bbox formatting, layer lists, etc.) should live **here** so all dev surfaces tell the same story.

### 4) Provenance-first by default 🧾🗺️
KFM is “the map behind the map.”  
Even in dev tooling, treat data as:
- **versioned**
- **traceable**
- **governed**
- **displayed with enough context to audit**

---

## 🗂️ Suggested folder layout

> This is the **intended** structure for the shared kit. Actual files may vary, but try to keep the shape consistent.

```text
web/src/components/dev/shared/
├─ README.md
├─ index.ts
├─ DevOnly.tsx            # gating helper (DEV builds / flags)
├─ DevPanel.tsx           # container chrome (title, actions)
├─ DevSection.tsx         # section headings + spacing
├─ DevKV.tsx              # key/value rows (labels + values)
├─ DevJSON.tsx            # JSON viewer + copy
├─ DevCodeBlock.tsx       # formatted code (wrap/copy)
├─ DevTabs.tsx            # tabs for inspectors
├─ DevBadge.tsx           # tiny status pills
├─ DevErrorBoundary.tsx   # dev-safe boundary + report
└─ styles/
   └─ devShared.css       # minimal styling hooks (prefer global tokens)
```

---

## 🧪 Dev gating patterns (do not ship dev UI)

Dev components must be **tree-shakeable** and **guarded** so they don’t appear in prod builds.

### Recommended: `DevOnly` wrapper
```tsx
// DevOnly.tsx (concept)
export function DevOnly({ children }: { children: React.ReactNode }) {
  // Vite: import.meta.env.DEV
  // CRA/Webpack: process.env.NODE_ENV !== 'production'
  const isDev =
    (typeof import.meta !== "undefined" && (import.meta as any).env?.DEV) ||
    (typeof process !== "undefined" && process.env?.NODE_ENV !== "production");

  if (!isDev) return null;
  return <>{children}</>;
}
```

### Optional: route-level lazy loading 🚀
If a dev inspector is heavy (tile inspector, raw payload viewer), prefer lazy routes:
```tsx
const DevToolsPage = React.lazy(() => import("../DevToolsPage"));
```

---

## 🧩 Usage examples

### ✅ Standard “inspector” panel
```tsx
import { DevPanel, DevSection, DevKV, DevJSON } from "./";

export function DatasetInspector({ dataset }: { dataset: any }) {
  return (
    <DevPanel title="Dataset Inspector" rightActions={<button>Copy ID</button>}>
      <DevSection title="Summary">
        <DevKV label="Dataset ID" value={dataset.id} />
        <DevKV label="Version" value={dataset.version} />
        <DevKV label="License" value={dataset.license ?? "—"} />
      </DevSection>

      <DevSection title="Raw payload">
        <DevJSON value={dataset} />
      </DevSection>
    </DevPanel>
  );
}
```

### ✅ Map debugging helpers (2D/3D friendly 🗺️🌎)
When building dev tools that touch MapLibre/Cesium, keep them:
- **read-only by default** (inspect state, don’t mutate)
- explicit about side-effects (“Apply filter”, “Rebuild layers”, etc.)
- reversible (reset buttons, snapshot/restore)

---

## 🧾 Provenance-first UI conventions (dev edition)

When you display any **data-backed** object in dev UI, try to include:

- **Stable identifier** (dataset ID, feature ID, story node ID)
- **Version / timestamp** (when applicable)
- **Source hint** (pipeline stage, endpoint name, layer name)
- **Governance hint** (public/restricted, CARE label, redaction applied)
- **Links** (to dataset page / metadata page / API endpoint docs)

### Suggested component contract: `ProvenanceMini`
If you build a provenance widget here, keep it tiny and universal:

```ts
export type ProvenanceMini = {
  id?: string;              // dataset/story/feature id
  version?: string;         // semver or commit-ish
  fetchedAt?: string;       // ISO timestamp
  source?: string;          // "api:v1/datasets/{id}"
  license?: string;         // "CC-BY-4.0" etc
  careLabel?: "Public" | "Restricted" | "Sensitive" | string;
  redacted?: boolean;
};
```

---

## 🔒 Privacy & governance (even in dev)

> **Dev UI should never become an accidental data exfiltration surface.** 🧯

**Do:**
- Redact obvious secrets (tokens, cookies, API keys)
- Truncate huge payloads by default (expand-on-demand)
- Prefer “copy sanitized” buttons for JSON/code
- Label sensitive objects clearly (CARE / restricted / internal)

**Don’t:**
- Dump full request headers automatically
- Print entire auth context to console
- Render user-submitted HTML unsafely

---

## 🎨 Styling rules (keep it boring ✨)

- Prefer **semantic HTML** + lightweight CSS modules or a small shared stylesheet
- Reuse existing spacing + typography tokens (avoid inventing new ones)
- Avoid bespoke colors for meaning—use **icons + text** for clarity ♿
- Keep layouts responsive (dev tooling is used on laptops *and* ultrawides)

---

## ✅ Contribution checklist

Before merging a new shared dev component:

- [ ] **Name is generic** enough for reuse across dev tools
- [ ] Component is **presentational-first** (data fetching stays outside)
- [ ] Has a minimal **story/demo usage** somewhere (dev page, sandbox route, etc.)
- [ ] Includes a **safe default** (redaction, truncation, fallback UI)
- [ ] Keyboard-focusable controls (tabs/buttons) work as expected ⌨️
- [ ] Exported from `index.ts` (and doesn’t create circular deps)

---

## 🧯 Troubleshooting

### HMR isn’t updating
- Confirm your dev server supports Hot Module Replacement (HMR) 🔥
- If running in Docker, ensure volume mounts are correct and the container sees file changes

### Port conflicts
- If `3000/8000/5432` are in use, either stop the conflicting service or remap ports in compose

---

## 🧠 Philosophy note (why we care)
KFM’s dev tooling is not “extra.” It’s part of the system’s trust story: debugging, auditing, and explaining *why* the map shows what it shows.

When in doubt:
- show the metadata 🧾
- show the lineage 🔗
- show the boundary between UI and API 🧱
