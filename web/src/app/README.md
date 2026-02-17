# KFM Web UI — App Wiring Layer (`web/src/app/`) ️

![Governed](https://img.shields.io/badge/status-governed-2563eb)
![Evidence-first](https://img.shields.io/badge/evidence--first-required-0f766e)
![Trust membrane](https://img.shields.io/badge/trust%20membrane-enforced-16a34a)
![Fail-closed](https://img.shields.io/badge/policy-default%20deny-111827)
![Frontend](https://img.shields.io/badge/frontend-React%20%2B%20TypeScript-0ea5e9)

`web/src/app/` is the **composition root** for KFM-Web: routing, top-level layout, and global providers.

> [!IMPORTANT]
> This directory is a **governance surface**.
> If it becomes a place where ad-hoc network calls, hidden side effects, or “quick fixes” land,
> KFM’s trust membrane and evidence-first UX will regress.

---

## Table of contents

- [Governance header](#governance-header)
- [What belongs here](#what-belongs-here)
- [What must *not* belong here](#what-must-not-belong-here)
- [Boot flow and responsibilities](#boot-flow-and-responsibilities)
- [Directory layout](#directory-layout)
- [Routing rules](#routing-rules)
- [Providers rules](#providers-rules)
- [Layout rules](#layout-rules)
- [Policy/denial UX rules](#policydenial-ux-rules)
- [Definition of Done](#definition-of-done)
- [Verification steps](#verification-steps)
- [Governed references](#governed-references)

---

## Governance header

| Field | Value |
|---|---|
| Document | `web/src/app/README.md` |
| Status | **Governed** (UI trust surface) |
| Scope | Route tree · app shell/layout · global providers · error boundaries |
| Version | `v1.0.0` |
| Effective date | 2026-02-17 (America/Chicago) |
| Owners | `.github/CODEOWNERS` *(required; if missing → governance gap)* |
| Review triggers | Routing changes · Provider changes · App shell layout changes · Cross-cutting error/telemetry changes |

> [!WARNING]
> **Fail-closed UI rule:** if the app cannot safely prove/resolve something (evidence, permission, integrity),
> it must **abstain, deny, or degrade gracefully** — never “fill in the blanks.”

---

## What belongs here

✅ This folder is for **wiring**:

- **Route definitions** (what screens exist, and how they are reached)
- **App shell** (global layout regions like map canvas, side panels, top bars)
- **Global providers** (theme, router, query client, state store, feature flags, i18n)
- **Top-level error boundaries** and app-wide fallbacks
- **Composition of feature modules** (import and place them, but do not implement features here)

Think: *“glue code that makes the UI boot predictably.”*

---

## What must *not* belong here

❌ The following are governance risks and should not be added under `src/app/`:

- **Direct network calls** (use `src/services/**` only)
- **Business logic** (belongs in feature modules; keep app wiring thin)
- **Contract definitions** (governed DTOs live in `src/contracts/**`)
- **Hidden persistence** of sensitive payloads (never cache restricted responses in `localStorage` / `sessionStorage` / `IndexedDB`)
- **UI-only “policy workarounds”** (never attempt to reconstruct denied fields by joining endpoints)

> [!CAUTION]
> “It’s just one fetch” is how trust membranes die.

---

## Boot flow and responsibilities

A healthy boot flow keeps concerns separated:

```mermaid
flowchart TD
  MAIN[Entry: src/main.tsx or equivalent] --> PROVIDERS[AppProviders]
  PROVIDERS --> ROUTER[Router + routes]
  ROUTER --> SHELL[AppShell / Layout]
  SHELL --> MAP[Map surface]
  SHELL --> PANELS[Panels: Layers · Story · Focus · Evidence · Audit]
  PANELS --> FEATURES[Feature modules]

  FEATURES -->|network IO (only)| SERVICES[src/services/**]
  SERVICES --> API[Governed API Gateway]
```

**Key idea:** `src/app/` composes the UI, but it must not become the place where IO or data shaping happens.

---

## Directory layout

> [!NOTE]
> This is the **recommended** layout aligned with `web/README.md`. If the repo differs, document the mapping.

```text
web/src/app/
├─ README.md
├─ App.tsx              # App shell composition (layout + top-level surfaces)
├─ router.tsx           # Route config (paths → screens)
├─ providers.tsx        # Global providers and their ordering
└─ layout/
   ├─ AppLayout.tsx     # Defines primary regions (map + panels)
   ├─ ShellChrome.tsx   # Navigation chrome (if any)
   └─ ErrorBoundary.tsx # Top-level error boundary
```

### Boundary reminder

- **Contracts**: `web/src/contracts/**` *(governed; change carefully)*
- **Network**: `web/src/services/**` *(the only fetch/XHR boundary)*
- **Reusable UI**: `web/src/components/**`
- **Feature modules**: `web/src/features/**` *(if used)*

---

## Routing rules

Routing is where KFM establishes **reproducibility**.

### Rules

- Routes must be **deterministic** and reviewable (no hidden route generation).
- If a route changes the user’s **view context** (time/layers/bbox), it must do so via the canonical **ViewState** helpers (from `src/contracts/**`).
- “Deep links” must be stable enough to reproduce a view for Story Nodes and audit review.

### Preferred pattern

- Define a small set of top-level route groups:
  - `/(map)` — map exploration
  - `/(story)` — Story Node playback
  - `/(focus)` — Focus Mode entry points
  - `/(evidence)` — evidence resolver views
  - `/(audit)` — audit reference views

> [!TIP]
> When possible, keep URLs declarative: the URL should describe a view, not a hidden UI state.

---

## Providers rules

The provider stack is part of the trust membrane.

### Provider ordering checklist (example)

- ErrorBoundary (outermost)
- Auth/session provider (token handling; browser-safe)
- Policy/entitlements provider (UI-level hints only; server is source of truth)
- State store provider (if used)
- Query client provider (if used)
- Router provider
- Theme/i18n providers

### Hard rules

- Providers must not fetch data “just because they can.”
- Providers must not store restricted payloads in persistent browser storage.
- Providers must not weaken CSP / security headers / allowed origins.

---

## Layout rules

KFM’s UI is not “pages with widgets.” It is a **map-first workspace** with evidence attached.

### Layout invariants

- Map state (camera/time/layers) must be **inspectable**.
- Evidence affordances must remain reachable in every primary surface:
  - layer metadata → evidence
  - story claims → citations
  - focus answers → citations + `audit_ref`

### Accessibility requirements (minimum)

- All interactive UI regions are reachable by keyboard.
- Focus Mode panel is navigable without the map.
- Citation links have descriptive text (not just “click here”).

---

## Policy/denial UX rules

Denials are not exceptions; they are normal outcomes.

### Required behaviors

- Treat `deny` / `abstain` as first-class UI states.
- Explain *what happened* in safe terms (no leaking policy inputs).
- Offer safe refinement hints:
  - “Narrow your time range”
  - “Select fewer layers”
  - “Zoom to a smaller area”

### Forbidden behaviors

- Retrying alternate endpoints until something leaks.
- Attempting to infer denied fields from partially allowed responses.

---

## Definition of Done

Any PR that changes code under `web/src/app/` must satisfy:

- [ ] No new network IO paths added (verify fetch/XHR stays in `src/services/**`)
- [ ] Routing changes are documented and include tests/coverage
- [ ] Provider changes include rationale and do not introduce hidden side effects
- [ ] UI fallbacks handle deny/abstain safely
- [ ] Evidence affordances remain reachable (manual check + tests if applicable)
- [ ] No sensitive payloads persisted client-side

---

## Verification steps

Minimum work to confirm this README matches repo reality:

1. Confirm the actual entrypoint file (`src/main.tsx`, `src/index.tsx`, Next.js `app/`, etc.).
2. Confirm router library (React Router / Next.js router / other).
3. Confirm provider stack and where auth/policy scoping occurs.
4. Confirm `src/services/**` is the *only* IO boundary and enforce it with a lint/test rule.

---

## Governed references

- `web/README.md` — Web UI invariants, contracts, and trust membrane expectations.
- `src/README.md` — Backend trust membrane and cite-or-abstain enforcement.
- `.github/README.md` — CI and governance gatehouse.
