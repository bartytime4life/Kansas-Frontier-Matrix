# Components (`web/src/components`)

![Governed](https://img.shields.io/badge/governed-evidence--first-2ea44f)
![UI](https://img.shields.io/badge/ui-react%20%2B%20typescript-0b74de)
![Map-first](https://img.shields.io/badge/map--first-MapLibre%20%2B%20Cesium-6f42c1)
![Fail-closed](https://img.shields.io/badge/policy-fail--closed-critical)

Shared, reusable UI components for the **KFM Web** application.

> [!IMPORTANT]  
> **KFM is evidence-first.** Components must help users understand *why* something is believed (citations, provenance, uncertainty), and they must **fail closed** (render “untrusted/unknown”) when evidence cannot be validated.

---

## What belongs here

Put components here when they are:

- **Reusable** across multiple pages/features
- **UI-first** (rendering + interaction), not long-running workflows
- **Safe-by-design** (no hidden side effects; no direct access to sensitive systems)
- **Provenance-aware** when displaying claims (maps, numbers, summaries, AI output)

Common examples:

- **Evidence surfaces** (receipts, provenance drawers, citations UI, trust badges)
- **Map UI components** (layer toggles, legends, timelines, scale bars, hover inspectors)
- **Story Node UI** building blocks (narrative panels, next/prev nav, media cards)
- **Accessibility primitives** (skip links, landmarks wrappers, keyboard helpers)

---

## What does not belong here

- ❌ **Direct database access** (never)
- ❌ **Secrets** (tokens, keys, credentials) or security-sensitive computations
- ❌ **Business workflows** (dataset promotion, policy decisions, ingestion orchestration)
- ❌ “Smart” components that **fetch from arbitrary URLs** without going through the governed API boundary

> [!NOTE]  
> Any network access in the frontend must go through the **governed API** (trust membrane). If you *think* you need to call a storage bucket or database from a component, stop and route through the API boundary instead. *(Exact client path may vary by repo wiring.)*

---

## Directory layout

### Canonical per-component folder pattern

Each component lives in its own folder, with colocated types, styles, tests, and docs.

```text
web/src/components/
├── README.md                         # (this file)
├── <ComponentName>/
│   ├── <ComponentName>.tsx           # main component
│   ├── <ComponentName>.test.tsx      # unit tests (if applicable)
│   ├── <ComponentName>.stories.tsx   # Storybook story (if Storybook enabled)
│   ├── styles.(css|module.css|scss)  # styles (follow repo standard)
│   ├── types.ts                      # exported types (optional)
│   ├── index.ts                      # re-export surface
│   └── README.md                     # component-level contract + usage notes
└── ...
```

### Example referenced in KFM docs (may or may not be present yet)

```text
web/src/components/
└── ReceiptViewer/                    # safe, read-only evidence/receipt renderer
    ├── ReceiptViewer.tsx
    ├── ReceiptViewer.css
    └── README.md
```

> [!CAUTION]  
> If a component folder structure differs in the current repo, **follow the repo**.  
> This README documents the **intended standard** and the direction we converge toward.

---

## Component design principles

### 1) Evidence-first UX

If the UI displays *facts*, it should also display:

- **Citations** (what source(s) support this?)
- **Provenance** (what dataset version / run produced it?)
- **Uncertainty** (confidence, caveats, redactions)
- **Policy outcome** (why something is withheld or generalized)

**Rule of thumb:** if a user could screenshot a claim, the screenshot should carry enough context to trace the evidence path.

### 2) Fail-closed rendering

When evidence validation fails (schema mismatch, missing signature, missing source references):

- Render **Untrusted / Unknown**
- Do **not** “best effort” parse or infer critical fields
- Offer a safe route to inspect raw data (collapsed JSON view, truncated)

### 3) Trust membrane respect

Components should be **pure renderers** of already-governed data:

- Prefer: `Component(props)` receives a typed model already filtered/redacted by API policy.
- Avoid: components that fetch, merge, or “repair” untrusted payloads inline.

### 4) Accessibility is non-negotiable

- Keyboard-first interactions
- Clear focus management
- Semantic landmarks, headings, and tables
- Screen reader compatibility for maps (ARIA labels + text alternatives)

### 5) Performance as a feature

Map + timeline UIs can be expensive. Favor:

- Stable references (`useRef`) for map/engine instances
- Memoization and selective rendering
- Virtualized lists for large tables
- Avoiding deep prop drilling for high-frequency signals (mousemove, map events)

---

## Imports and boundaries

### Preferred dependency direction

```mermaid
flowchart LR
  A[Components] --> B[Hooks / View-models]
  B --> C[Governed API client]
  C --> D[API Gateway + Policy (OPA)]
  D --> E[Storage: PostGIS / Object Store / Graph / Search]
  D --> F[Evidence Resolver + Provenance]
  F --> C
  C --> B
  B --> A
```

### Anti-patterns

- Importing server-only code into the browser bundle
- Reading environment secrets directly in components
- Calling unverified third-party endpoints from UI without policy mediation

---

## Evidence surfaces

Evidence surfaces are components designed to “show your work” to the user.

### ReceiptViewer (reference contract)

A safe receipt viewer follows this trust chain:

1. **Validate schema**  
2. **Verify signature**  
3. **Render** (with explicit status)

> [!IMPORTANT]  
> Evidence surfaces must be safe, **read-only**, and resistant to malformed input.

**Recommended blocks:**

- Status pill: `Valid/Invalid` · `Verified/Unverified`
- Inputs table: type-aware renderers
- Signatures panel: signer, thumbprint, issuance/expiry, verification result
- Links panel: safe external links only
- JSON viewer: collapsed by default; truncation for very large blobs

**Guardrails:**

- Never use `dangerouslySetInnerHTML`
- Validate before computing derived views
- External links: `target="_blank"` + `rel="noopener noreferrer"`

<details>
<summary><strong>Minimal component “contract” template</strong></summary>

```ts
export type ReceiptViewerProps = {
  schema: object;       // JSON Schema (AJV-compatible)
  data: unknown;        // raw receipt/manifest payload
  compact?: boolean;    // e.g., PR previews
  onAction?: (type: string, payload?: unknown) => void;
}
```
</details>

---

## Styling conventions

Follow the repository styling standard (CSS Modules, plain CSS, SCSS, CSS-in-JS, etc.).

Minimum expectations:

- Styles are **colocated** with the component
- Class names are stable and readable
- Don’t couple behavior to styling (no “CSS as logic”)
- Avoid global styles unless the repo explicitly uses a design system

---

## Security checklist for UI components

- [ ] No `dangerouslySetInnerHTML` (or sanitize with a vetted sanitizer if unavoidable)
- [ ] External links use `rel="noopener noreferrer"`
- [ ] Large payloads are rendered safely (truncate / collapse / lazy render)
- [ ] No PII in telemetry events; log structural events only
- [ ] Error states do not leak secrets or internal stack traces

---

## Accessibility checklist

- [ ] Correct semantic element (`button` for buttons, `nav` for navigation, etc.)
- [ ] Interactive elements are keyboard reachable
- [ ] Visible focus indicator
- [ ] ARIA labels only when semantics are insufficient
- [ ] Tables use proper `thead/tbody` and headers
- [ ] Color is never the only carrier of meaning

---

## Testing and Definition of Done

### When a component is “done”

- [ ] Types: exported props + key models are typed (no unbounded `any`)
- [ ] Docs: component has a short `README.md` explaining purpose and usage
- [ ] Tests: unit tests exist for non-trivial logic and critical rendering states
- [ ] A11y: validated with at least one automated check and a keyboard pass
- [ ] Security: guardrails followed (especially for evidence surfaces)
- [ ] Performance: no obvious render thrash on map/timeline interactions

### Evidence surface DoD (additional)

- [ ] Schema validation is enforced before rendering “trusted” UI
- [ ] Signature verification result is displayed and defaults to “unverified”
- [ ] Fail-closed: invalid/unverified payloads never display green/approved affordances
- [ ] Raw view exists (collapsed JSON; safe truncation)

---

## Contributing notes

- Prefer small, reviewable components.
- Prefer composition over inheritance.
- Keep components **deterministic**: given the same props, they should render the same output.
- If the component influences “public narrative” (Story Nodes, summaries, maps), treat the output as a **governed artifact**: cite, qualify, and respect sensitivity flags.

---

## Suggested component README template

Create `web/src/components/<ComponentName>/README.md` with:

- **Purpose**
- **Inputs/props**
- **Outputs/states**
- **Security notes**
- **Accessibility notes**
- **Example usage**
- **Test coverage expectations**