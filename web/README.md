# KFM Web UI

The **KFM Web UI** is the browser-based interface for exploring KFM’s governed geospatial/historical knowledge system: **maps + layers + time + Story Nodes + evidence review + Focus Mode**.

KFM’s web UI is explicitly designed to be **evidence-first**: users should be able to inspect *“the map behind the map”* and trace every layer, story step, and AI-assisted answer back to governed sources and provenance.

## Table of contents

- [Non-negotiables](#non-negotiables)
- [Architecture](#architecture)
- [UI components](#ui-components)
- [Core contracts](#core-contracts)
- [Local development](#local-development)
- [Build and release](#build-and-release)
- [Testing and quality gates](#testing-and-quality-gates)
- [Security and governance](#security-and-governance)
- [Directory layout](#directory-layout)
- [Related docs](#related-docs)

## Non-negotiables

> [!IMPORTANT]
> KFM’s credibility depends on strict enforcement of its governance boundary (“trust membrane”).
> **This web UI must never bypass the governed API + policy boundary.**

**Required invariants (must remain true):**
- **No direct database access from the UI.** All reads/writes go through the **governed API gateway**, where policy checks and audit logging occur.
- **Policy fails closed.** If policy/evidence checks are uncertain, access is denied.
- **Focus Mode must cite or abstain.** If evidence is insufficient, Focus Mode returns an abstention response (not a best-guess).
- **Every Focus Mode response includes an audit reference** that can be inspected in the UI’s audit/provenance viewer.
- **Evidence must be reviewable.** Users must have a way to open a human-readable “review evidence” view for:
  - map layers / hovered features (where available)
  - Story Nodes (inline citations)
  - Focus Mode answers (footnotes + resolver links)

## Architecture

KFM is a pipeline → catalogs → stores → API → UI system. The UI sits outside storage and depends on the API gateway for both data and governance.

```mermaid
flowchart LR
  subgraph Client
    UI[KFM Web UI\nReact + TypeScript + MapLibre]
  end

  subgraph TrustMembrane[Trust membrane]
    API[API Gateway\nREST (optionally GraphQL)]
    OPA[Policy engine\nOPA/Rego]
    AUDIT[Audit + provenance services]
  end

  subgraph Stores
    PG[PostGIS\ngeo + tiles]
    G[Graph store\nNeo4j]
    S[Search/Vector]
    OBJ[Object storage\nCOGs + media]
  end

  UI --> API
  API --> OPA
  API --> AUDIT
  API --> PG
  API --> G
  API --> S
  API --> OBJ
```

## UI components

The web UI is organized around a small set of responsibilities that all tie back to evidence:

| Component | Responsibility | Evidence behavior |
|---|---|---|
| **MapCanvas** | Render the map and allow inspect/hover | Show provenance for hovered features where available |
| **LayerPanel** | Toggle/filter layers | Link each layer to dataset metadata, license, and provenance |
| **Timeline** | Control time range and playback | Record time range in `ViewState` passed to Focus Mode |
| **StoryViewer** | Render Story Nodes and steps | Display citations inline; step actions update `ViewState` |
| **FocusPanel** | Grounded Q&A (Focus Mode) | Render footnotes; link to evidence resolver views |
| **AuditDrawer** | Audit and provenance viewer | Fetch PROV chains and audit ledger entries for inspection |

## Core contracts

### ViewState

KFM uses a **ViewState** object to synchronize map/time/story context and to provide grounded context for Focus Mode queries.

```ts
export type ViewState = {
  timeRange: [string, string];
  bbox: [number, number, number, number];
  activeLayers: string[];
  storyNodeId?: string;
  storyStepId?: string;
  userRole?: string;
};
```

### Focus Mode API contract

Focus Mode queries are sent to the API gateway along with `ViewState` context.

**Endpoint (documented contract):**
- `POST /api/v1/ai/query`

**Request (shape):**
- `question`
- `context`: `{ time_range, bbox, active_layers, story_node_id }`

**Response (shape):**
- `answer_markdown`
- `citations[]`
- `audit_ref`

> [!NOTE]
> The exact citation object schema (fields beyond a reference/locator) should come from the API schema.
> The UI should treat citations as structured data and avoid assuming a single “string format”.

### Evidence references and resolution

Citations and provenance references must be resolvable (examples include):
- `prov://...`
- `stac://...`
- `dcat://...`
- `doc://...`
- `graph://...`

**Acceptance target:**
- Given any `citation.ref` in a Focus Mode answer, the UI can resolve it to a human-readable evidence view in **≤ 2 API calls**.

> [!TIP]
> Keep evidence resolution logic centralized (a single “Evidence Resolver” service/module) so that:
> - Focus Mode citations, Story Node citations, and dataset/layer citations share the same UI
> - audit/provenance links behave consistently across the app

## Local development

> [!NOTE]
> Some setup details depend on the actual `web/package.json` and repo tooling.
> The conventions below are recommended defaults; adjust to match the repo.

### Prerequisites

- Node.js (LTS recommended)
- A package manager (`npm`, `pnpm`, or `yarn`) consistent with the repo
- Access to a running KFM API gateway (plus policy engine) for non-mocked functionality

### Install

```sh
cd web
npm install
```

### Configure environment

Create a `.env.local` (or equivalent) with values appropriate for your environment.

Example (names are suggestions; use what the repo standardizes):

```ini
# Base URL for the governed API gateway
VITE_KFM_API_BASE_URL=http://localhost:8080

# Optional: auth integration (OIDC) if enabled in this environment
VITE_KFM_AUTH_ENABLED=false
VITE_KFM_OIDC_ISSUER=
VITE_KFM_OIDC_CLIENT_ID=
```

### Run the dev server

```sh
npm run dev
```

### Run against local services

For end-to-end behavior, you typically need:
- API gateway
- policy engine (OPA)
- required backing stores (depending on the feature you are working on)

See the repo’s root development runbook / compose instructions.

## Build and release

### Build a production bundle

```sh
npm run build
```

### Container build

If the repo supports containerized builds, a typical pattern is:

```sh
docker build -t kfm-web ./web
```

## Testing and quality gates

### Local checks

Typical commands (verify against `web/package.json`):

- `npm run lint`
- `npm run typecheck`
- `npm test`
- `npm run build`

### UI contract tests to keep KFM honest

Add tests that enforce KFM’s evidence guarantees:

- **Evidence resolution contract:** Given an answer with citations, the UI can resolve each `citation.ref` into a human-readable evidence card/view.
- **Cite-or-abstain UX:** If `citations` is empty (abstention), the UI clearly indicates the system is abstaining and offers next-step guidance (e.g., refine time range, activate relevant layers).
- **Audit visibility:** The UI displays `audit_ref` for Focus Mode answers and lets the user open the audit/provenance view.

### CI expectations

The broader KFM CI pipeline includes:
- validation of governed markdown / Story Nodes
- validation of STAC/DCAT/PROV artifacts
- OPA policy tests
- build artifacts including a `kfm-web` container image (if containerized builds are used)

## Security and governance

### Authentication and authorization

If enabled in your environment:
- **AuthN:** OIDC provider issues JWTs; API gateway verifies tokens.
- **AuthZ:** OPA evaluates role/attributes and enforces access rules centrally.
- Different roles may see different levels of provenance detail.

### Handling sensitive data

Some datasets may include:
- restricted access fields
- sensitive locations requiring generalized or suppressed coordinates
- aggregate-only publishing rules

The UI should:
- rely on the API for redaction and policy enforcement
- avoid client-side “workarounds” to reconstruct restricted fields
- avoid storing sensitive content in local persistence by default

### Rendering untrusted content safely

Focus Mode returns `answer_markdown`. The UI must render it in a way that prevents XSS:
- sanitize markdown/HTML output
- use an allowlist of safe elements
- treat external links cautiously

## Directory layout

Suggested `web/` layout (adapt as needed):

```text
web/
  README.md
  package.json
  tsconfig.json
  index.html
  public/
  src/
    api/                # API clients, DTOs, fetch wrappers
    components/         # reusable UI components
    features/           # map, layers, story nodes, focus mode, audit drawer
    state/              # ViewState + app state stores
    styles/
    types/
    main.tsx
  tests/
    contract/           # evidence resolution + focus mode schema tests
    unit/
```

## Related docs

- KFM Next-Gen Blueprint & Primary Guide (Web UI blueprint, trust membrane invariants, evidence UX, CI gates)
- KFM Data Source Integration Blueprint (end-to-end governance requirements impacting UI behavior)
- Repo standards and templates (Story Node v3, governed Markdown protocol, schema registries)
