# Evidence UI Components (`web/src/components/evidence`)

![Governed](https://img.shields.io/badge/Governed-Yes-2ea44f)
![Evidence-first](https://img.shields.io/badge/Evidence--first-Required-blue)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Aligned-6f42c1)
![Trust%20Membrane](https://img.shields.io/badge/Trust%20Membrane-Enforced-ff7a18)

**Purpose:** This folder contains **UI building blocks** for rendering **citations, provenance, trust/sensitivity cues, and “not confirmed” warnings** across the KFM web app.

KFM’s promise is simple: **no black boxes**. If a claim, layer, or number can’t be traced to approved sources or reproducible transforms, the UI must label it clearly (e.g., **“not confirmed”**) and show what evidence *is* available. Evidence components are how we make that promise visible—everywhere. ✅

---

## Why this exists

KFM is a governed spatio-temporal system (“data → pipeline → catalogs/provenance → APIs → UI/Focus Mode”). This directory implements the **UI end of that truth path**, ensuring users can always:

- **See sources** (citations / datasets / documents)
- **See lineage** (pipeline steps & transforms)
- **See constraints** (license + sensitivity / CARE restrictions)
- **See uncertainty** (“not confirmed” / partial evidence)
- **Export evidence** (copy citations, download provenance, share safe summaries)

> **Trust membrane rule:** the frontend never accesses databases directly. Evidence UI consumes **governed API outputs** (or pre-fetched props) and only renders what policy allows.

---

## What belongs here (and what does not)

### ✅ Belongs here
- **Presentational** React components for:
  - citations
  - provenance timelines
  - trust badges
  - license chips
  - sensitivity/redaction banners
  - “not confirmed” callouts
- Small formatting helpers (e.g., `formatLocator`, `formatConfidenceLabel`)

### ❌ Does *not* belong here
- API clients, GraphQL queries, fetch logic (put in a data layer/hook, e.g. `web/src/services/*` or `web/src/hooks/*`)
- Policy decisions (policy is enforced server-side; UI only *reflects* it)
- Any logic that could accidentally reveal restricted content (e.g., “just show coords if present”)

---

## Component inventory (recommended baseline)

> **Note:** Filenames below are a **suggested** inventory and may need to be aligned with the existing codebase (**not confirmed in repo**).

| Component | Primary job | Typical placements |
|---|---|---|
| `EvidenceDock` | “One-stop” expandable panel combining badges + citations + provenance | Focus Mode answers, Story Nodes, Map layer inspector |
| `CitationList` | Render a list of citations with stable ordering and safe links | Anywhere evidence is displayed |
| `CitationInline` | Inline “¹²³” markers + hover/press popover | Longform narratives, Focus Mode paragraphs |
| `CitationPopover` | Small, accessible popover with citation metadata | Inline citation UX |
| `ProvenanceTimeline` | Visual lineage / transforms / QA gates | Dataset detail pages, exports |
| `TrustBadge` | At-a-glance trust indicator (validated / partial / unknown) | Cards, headers, layer legends |
| `SensitivityBanner` | Indicates redaction/generalization and why | Archaeology, sensitive locations |
| `LicenseChips` | License / usage constraints | Dataset pages, downloads |
| `NotConfirmedCallout` | “This is not confirmed” standard callout | Focus Mode, dashboards |

---

## Data contracts (UI-facing types)

Evidence UI should be **data-source agnostic**: it renders a single normalized payload, regardless of whether the backend is REST, GraphQL, or precomputed Story Node JSON.

### `EvidenceBundle` (proposed)
```ts
export type EvidenceBundle = {
  /** Stable ID for the thing being explained (layer, claim, dataset, story node section) */
  subjectId: string;

  /** Short UI summary, optional */
  summary?: string;

  /** Evidence / citations */
  citations: Citation[];

  /** Provenance / lineage steps (sanitized per policy) */
  provenance?: ProvenanceStep[];

  /** Trust & uncertainty */
  trust: {
    level: "validated" | "processed" | "raw" | "unknown";
    confidence?: number; // 0..1 (optional)
    flags?: Array<"partial-evidence" | "conflicting-sources" | "derived-output" | "human-reviewed">;
  };

  /** Policy-facing constraints surfaced to UI */
  governance: {
    sensitivity: "open" | "restricted" | "sensitive";
    redactionApplied?: boolean;
    license?: string;
    sharePolicy?: "public" | "registered" | "partner" | "internal";
  };

  /** Optional UI-safe excerpts */
  excerpts?: Array<{
    citationId: string;
    text: string; // must already be sanitized
    locator?: Locator;
  }>;
};

export type Citation = {
  id: string;
  title: string;
  creators?: string[];
  year?: string | number;
  type: "archive" | "dataset" | "paper" | "map" | "web" | "oral-history" | "unknown";
  uri?: string;           // only if allowed by governance
  accessedAt?: string;    // ISO date
  locator?: Locator;      // page, figure, timestamp, etc.
  license?: string;
  notes?: string;         // UI-safe
};

export type Locator =
  | { kind: "page"; page: number }
  | { kind: "pages"; from: number; to: number }
  | { kind: "figure"; label: string }
  | { kind: "table"; label: string }
  | { kind: "timestamp"; seconds: number }
  | { kind: "section"; label: string };

export type ProvenanceStep = {
  id: string;
  at?: string; // ISO date/time
  actor?: string; // pipeline job / user / system component
  action:
    | "ingest"
    | "validate"
    | "transform"
    | "enrich"
    | "catalog"
    | "publish"
    | "redact"
    | "review"
    | "unknown";
  description?: string; // UI-safe
  inputs?: string[];    // artifact IDs, if allowed
  outputs?: string[];   // artifact IDs, if allowed
  qa?: Array<{ check: string; status: "pass" | "warn" | "fail" }>;
};
```

### Contract rules
- **UI must not compute “trust”** from raw data. Trust arrives as a governed field.
- **No raw coordinates** for restricted/sensitive items unless policy explicitly allows it.
- **Order is stable**: citations displayed in a deterministic order (e.g., rank + title + year).

---

## UX rules (non-negotiable)

### 1) Progressive disclosure
Users should get the “truth at a glance,” then drill down.

At minimum, render:
- Evidence count (e.g., **“3 sources”**)
- Trust level (badge)
- Sensitivity status (banner if not open)
- A “view details” affordance

### 2) “Not confirmed” has one canonical pattern
If `trust.level === "unknown"` **or** the backend flags `partial-evidence`, show:

- A consistent title: **Not confirmed**
- A short explanation: “This output cannot currently be traced to an approved source or reproducible run.”
- What *is* known: show available citations/provenance (if any)
- Next action: “View evidence” / “Request review” (if product supports)

### 3) Sensitivity-aware rendering
If `governance.sensitivity !== "open"`:
- Never render fine-grained location, exact site names (if restricted), or links that bypass policy
- Render **why** redaction happened (if backend provides a safe reason)
- Provide a “How to request access” link (route TBD; **not confirmed in repo**)

---

## Accessibility & safety checklist

### Accessibility (A11y)
- All interactive evidence elements are reachable by keyboard
- Popovers have correct ARIA semantics (`role="dialog"` or `role="tooltip"` as appropriate)
- Badges/icons are never color-only; always include text labels
- Citation links have descriptive names (“Open source: …” not “click here”)

### Security
- Never render unsanitized HTML excerpts
- External links must use `rel="noopener noreferrer"` and `target="_blank"` only when necessary
- Treat evidence payload as **untrusted input** (defensive rendering)

---

## Recommended folder layout

```text
web/
└─ src/
   └─ components/
      └─ evidence/
         ├─ README.md
         ├─ index.ts
         ├─ types.ts
         ├─ EvidenceDock.tsx
         ├─ CitationList.tsx
         ├─ CitationInline.tsx
         ├─ CitationPopover.tsx
         ├─ ProvenanceTimeline.tsx
         ├─ TrustBadge.tsx
         ├─ SensitivityBanner.tsx
         ├─ LicenseChips.tsx
         ├─ NotConfirmedCallout.tsx
         └─ __tests__/
            ├─ EvidenceDock.test.tsx
            ├─ CitationList.test.tsx
            └─ a11y.test.tsx
```

---

## Usage examples

### Example: Map layer inspector
```tsx
import { EvidenceDock } from "./EvidenceDock";
import type { EvidenceBundle } from "./types";

export function LayerEvidencePanel({ evidence }: { evidence: EvidenceBundle }) {
  return (
    <EvidenceDock
      evidence={evidence}
      context="map-layer"
      defaultOpen={false}
      density="compact"
    />
  );
}
```

### Example: Inline citations in Story Node text
```tsx
import { CitationInline } from "./CitationInline";

export function ParagraphWithCites() {
  return (
    <p>
      Railroad expansion accelerated settlement patterns
      <CitationInline citeIds={["cite-001", "cite-004"]} /> across the corridor.
    </p>
  );
}
```

---

## Component behavior: EvidenceDock (suggested spec)

**Inputs**
- `evidence: EvidenceBundle`
- `context: "focus-mode" | "story-node" | "map-layer" | "dataset-detail" | string`
- `defaultOpen?: boolean`
- `density?: "compact" | "comfortable"`

**Renders**
- Header row with:
  - `TrustBadge`
  - Evidence count
  - `LicenseChips` (if present)
  - Sensitivity indicator/badge
- Expandable sections:
  - “Citations”
  - “Provenance”
  - “Notes / excerpts” (if present and policy allows)
- If `trust.level === "unknown"`, show `NotConfirmedCallout` at top

---

## Mermaid: UI evidence flow

```mermaid
flowchart LR
  U[User opens\nLayer/Answer/Story] --> UI[EvidenceDock\n& related components]
  UI -->|props| E[EvidenceBundle]
  E -->|provided by| API[Governed API Gateway]
  API -->|policy + redaction| S[Sanitized Evidence\n(citations + provenance)]
  S --> UI
  UI --> X[Exports / Copy citation\n(only allowed fields)]
```

---

## Testing strategy (minimum)

### Unit tests
- Stable ordering of citations
- Correct rendering for each `trust.level`
- Redaction/sensitivity states don’t leak prohibited fields
- Locator formatting (page ranges, figures, timestamps)

### Accessibility tests
- Popovers and docks are keyboard accessible
- ARIA roles/labels present
- Focus management correct on open/close

### Contract tests (recommended)
- Validate `EvidenceBundle` schema at the boundary (runtime validation like Zod, if used — **not confirmed in repo**)
- Snapshot tests for “not confirmed” rendering

---

## Definition of Done

- [ ] Evidence UI can render **citations + trust + sensitivity** for:
  - [ ] Map layer inspector
  - [ ] Focus Mode answer panel
  - [ ] Story Node page section
- [ ] “Not confirmed” appears whenever required (and never silently fails)
- [ ] No direct DB access; data arrives via props or governed API client
- [ ] A11y checks pass (keyboard + screen reader basics)
- [ ] No sensitive fields rendered when `sensitivity !== "open"`
- [ ] Tests added (unit + a11y)
- [ ] Storybook/examples (if present in repo — **not confirmed in repo**) updated

---

## Related docs (update paths as needed)

- KFM system blueprint: architecture, governance gates, truth path (**source doc in project assets**)  
- KFM vision brief: evidence-first promise, “not confirmed” behavior, governed sharing (**source doc in project assets**)  
- Frontend conventions: React/TypeScript project guidelines (**source doc in project assets**)

---

## Governance note

If you are adding a new evidence UI pattern that could affect:
- how sensitive content is displayed,
- how trust levels are communicated,
- what gets exported/shared,

…treat it as a **governed change**. Add tests and route through governance review.

✅ **When in doubt:** show less detail, and explain why.
