# 🧠 Focus Mode

![Feature](https://img.shields.io/badge/feature-focus%20mode-2ea44f)
![UI](https://img.shields.io/badge/ui-react-61DAFB?logo=react&logoColor=white)
![Trust](https://img.shields.io/badge/trust-provenance%20first-blue)
![Governance](https://img.shields.io/badge/governance-FAIR%2BCARE-orange)
![Hard%20Gate](https://img.shields.io/badge/hard%20gate-enabled-critical)

Focus Mode is KFM’s **interactive reading experience**: a governed **Story Node** 📄 presented alongside **map 🗺️ + timeline ⏱️ context**.

**Design intent:** trust-preserving storytelling.  
**Operational rule:** *if it can’t be traced to provenance, it must not render.*

---

## 📍 Location

```text
📁 web/
  └── 📁 src/
      └── 📁 features/
          └── 📁 focus-mode/
              └── 📄 README.md  👈 you are here
```

---

## 🧭 Where Focus Mode sits in the KFM pipeline

```mermaid
flowchart LR
  A[ETL] --> B[Catalogs<br/>(STAC / DCAT / PROV)]
  B --> C[Graph]
  C --> D[API<br/>(src/server)]
  D --> E[UI<br/>(web)]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
```

> [!IMPORTANT]
> Focus Mode is the **last stage**. It must only consume governed outputs from earlier stages (especially via the **API boundary**).

---

## 🚧 Hard Gate Rules

> [!IMPORTANT]
> These are **non-negotiable invariants**. Don’t merge changes that weaken them.

### 1) Only provenance‑linked content ✅
- Story text must come from **published Story Nodes** (with citations).
- Dynamic content (maps, images, charts, overlays) must come from **cataloged data** or **graph entities** with stable IDs.
- Any UI element without a provenance reference is **blocked** (fail closed).

### 2) AI is opt‑in + transparent 🤖
- AI output must **never render by default**.
- AI output must be:
  - user-triggered (opt-in)
  - labeled as AI-generated
  - accompanied by uncertainty/confidence metadata (when available)
- AI must **respect all sensitivity/redaction rules** (no speculation that bypasses governance).

### 3) No sensitive location leaks 🛡️
- The Focus Mode map must **generalize or omit** sensitive locations according to sovereignty rules.
- Focus Mode must not become a **side‑channel** that reveals restricted coordinates (zooming, hover tooltips, network calls, cached tiles, etc.).

---

## 🎯 What Focus Mode is responsible for

- 📖 **Render Story Nodes safely**
  - deterministic, sanitized Markdown rendering
  - stable anchors for citations & entity references
- 🧷 **Evidence UX**
  - citations are clickable / traceable
  - evidence drawer/panel for sources
- 🗺️ **Map context**
  - layers are provenance-backed
  - each layer can show a “Source” tooltip linking to its catalog provenance
- ⏱️ **Timeline context**
  - story-aligned temporal navigation
  - highlights entities/events referenced in the narrative
- 🧯 **Redaction UX**
  - blurred markers / regionalization / omission + clear notices
- 📊 **Audit-friendly telemetry**
  - record user-visible governance actions (e.g., redaction notices)

---

## ❌ What Focus Mode must NOT do

- 🚫 Query the graph or databases directly (Neo4j/PostGIS/etc.)
- 🚫 Render “helpful” context that has no provenance ID
- 🚫 Auto-inject AI summaries/suggestions into the reading flow
- 🚫 Leak sensitive locations through UI behavior or metadata

---

## 📦 Inputs

### 1) Published Story Nodes (governed content)
Expected to live under:

- `docs/reports/story_nodes/published/<story_slug>/story.md`
- `docs/reports/story_nodes/published/<story_slug>/assets/*`

Story Nodes should include:
- citations for factual claims
- stable entity references (graph IDs)
- explicit separation of **fact vs interpretation** (especially if AI-assisted)

### 2) Focus Mode Context Bundle (from the governed API)
Focus Mode should request a single “bundle” that includes:
- story content (or pointer)
- entity references
- timeline items
- map layers/overlays + view constraints
- evidence list
- redaction & sensitivity flags
- optional AI capabilities (if enabled)

> [!TIP]
> Keep the UI “dumb”: redaction, access control, and contract validation belong server-side. The UI still enforces **fail-closed** behavior.

---

## 🧩 Suggested module layout

```text
📁 web/src/features/focus-mode/
├── 📄 README.md
├── 🧭 routes/
│   └── FocusModeRoute.tsx
├── 📄 FocusModePage.tsx
├── 📁 components/
│   ├── 📁 StoryNodeReader/
│   ├── 📁 EvidenceDrawer/
│   ├── 📁 MapPanel/
│   ├── 📁 TimelinePanel/
│   └── 📁 AIInsightsPanel/
├── 📁 hooks/
│   ├── useFocusModeBundle.ts
│   ├── useProvenanceGuard.ts
│   └── useRedactionPolicy.ts
├── 📁 services/
│   ├── focusModeApi.ts
│   └── telemetry.ts
├── 📁 types/
│   ├── focusMode.types.ts
│   └── storyNode.types.ts
└── 🧪 __tests__/
    ├── provenanceGuard.test.ts
    ├── redactionPolicy.test.ts
    └── focusModeBundle.contract.test.ts
```

> [!NOTE]
> Filenames can differ — the key is **feature cohesion**: everything Focus Mode owns stays in this folder.

---

## 🧾 Contracts & Types

### TypeScript sketch (client-side)

```ts
export type ProvenanceRef = {
  /** Stable ID (STAC/DCAT/PROV/Graph ID) */
  id: string;
  /** Human label for evidence UX */
  label?: string;
  /** Optional deep-link for evidence viewer */
  href?: string;
};

export type RedactionPolicy = {
  sensitivity: "open" | "restricted" | "sensitive";
  hidePreciseLocation: boolean;

  /**
   * Optional generalized geometry (region polygon, bbox, etc.)
   * Never assume this is precise. Treat as display-only.
   */
  generalizedGeometry?: unknown;

  /** UX copy shown to the user when redaction occurs */
  notice?: string;
};

export type FocusModeBundle = {
  storyNode: {
    slug: string;
    title: string;
    markdown: string;
    provenance: ProvenanceRef;

    // governance metadata (when available)
    careLabel?: string;
    sensitivity?: "open" | "restricted" | "sensitive";
    lastUpdated?: string;
  };

  entities: Array<{
    id: string;
    label: string;
    kind: "person" | "place" | "event" | "document" | "dataset" | "other";
    provenance: ProvenanceRef;
    redaction?: RedactionPolicy;
  }>;

  timeline: {
    items: Array<{
      id: string;
      label: string;
      start: string; // ISO
      end?: string;  // ISO
      provenance: ProvenanceRef;
    }>;
  };

  map: {
    layers: Array<{
      id: string;
      title: string;
      provenance: ProvenanceRef;
      config: unknown;
      redaction?: RedactionPolicy;
    }>;
    viewConstraints?: {
      maxZoom?: number;
      bounds?: unknown;
    };
  };

  evidence: {
    items: Array<{
      id: string;
      title: string;
      provenance: ProvenanceRef;
      kind?: "scan" | "photo" | "dataset" | "report" | "other";
    }>;
  };

  ai?: {
    enabled: boolean;
    capabilities: Array<string>; // e.g. ["summarize", "suggestConnections"]
  };
};
```

### Provenance guard (fail closed)
```ts
export function assertRenderable<T extends { provenance?: ProvenanceRef }>(
  item: T,
  label: string
): asserts item is T & { provenance: ProvenanceRef } {
  if (!item.provenance?.id) {
    throw new Error(`[FocusMode] Missing provenance for ${label}`);
  }
}
```

---

## 🗺️ Map + Timeline behavior

### Map panel
- Only renders layers returned by the API bundle (no hidden layers)
- Every layer has a **Source** affordance (ℹ️) that points back to provenance
- Sensitive locations render as:
  - generalized regions, or
  - blurred markers, or
  - omitted entirely
- When any sensitive layer is visible:
  - enforce view constraints (e.g., clamp zoom)
  - show a redaction notice

### Timeline panel
- Shows events connected to the story and its referenced entities
- Clicking a timeline item:
  - highlights related passages (if available)
  - highlights map features (only if allowed by redaction policy)

---

## 🧯 Redaction & Sovereignty

> [!WARNING]
> Treat the UI as an attack surface: hover tooltips, URL params, cached tiles, debug logs, and telemetry can leak restricted coordinates.

**UI safeguards (minimum):**
- Clamp zoom / restrict panning when `hidePreciseLocation` is true anywhere in view
- Never log/store raw coordinates client-side for redacted entities
- Ensure source popovers do not include restricted geometry
- Render clear notices when redaction occurs

**Telemetry (recommended):**
- `focus_mode_redaction_notice_shown`

---

## 🤖 AI in Focus Mode

AI in Focus Mode is allowed only when it follows this shape:

- ✅ user-triggered (button/menu)
- ✅ labeled “AI-generated”
- ✅ includes confidence/uncertainty (when supported)
- ✅ never bypasses redaction
- ✅ refuses to “fill gaps” when evidence is missing

Suggested UX actions:
- **Generate summary (AI)** → short summary + confidence
- **Suggest connections (AI)** → explicit hypotheses + uncertainty, never treated as fact

---

## 📊 Telemetry & Audit Trails

Focus Mode should emit events that support review and compliance:

- `focus_mode_opened`
- `focus_mode_evidence_opened`
- `focus_mode_redaction_notice_shown`
- `focus_mode_ai_hint_requested`
- `focus_mode_ai_hint_shown`

> [!TIP]
> Prefer stable IDs (story slug, entity IDs, provenance IDs). Avoid raw data payloads.

---

## 🧪 Testing

Minimum tests that protect the hard gate:

- ✅ Unit: provenance guard blocks render when provenance is missing
- ✅ Unit: redaction policy prevents coordinate display + clamps zoom
- ✅ Contract: bundle matches API schema (JSON schema validation / snapshot)
- ✅ E2E: sensitive Story Nodes do not leak coordinates via:
  - map interactions
  - tooltips
  - network calls
  - exported URLs

---

## ✅ Definition of Done (DoD) for Focus Mode changes

- [ ] Nothing renders without a provenance ID
- [ ] Redaction cannot be bypassed via UI behavior
- [ ] AI is opt-in, labeled, and includes uncertainty (when available)
- [ ] Telemetry is safe (IDs, not raw restricted data)
- [ ] Evidence UX works (citations are traceable)
- [ ] Tests updated/added to protect invariants

---

## 🔗 Related docs (repo)

From this folder, repo root is `../../../../`.

- 📘 Master Guide v13: `../../../../docs/` *(find the canonical v13 Master Guide file there)*
- 🧩 Story Node template: `../../../../docs/templates/TEMPLATE__STORY_NODE_V3.md`
- 🧾 API contract extension template: `../../../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- ⚖️ Governance: `../../../../docs/governance/ROOT_GOVERNANCE.md`
- 🛡️ Sovereignty: `../../../../docs/governance/SOVEREIGNTY.md`
- 🧪 Telemetry schemas: `../../../../schemas/telemetry/`
- 🗺️ UI schemas: `../../../../schemas/ui/`
- 🧠 Story Node schemas: `../../../../schemas/storynodes/`

---

<details>
<summary>🧰 Troubleshooting</summary>

### “Why is my layer not showing up?”
- Does it have a provenance ID?
- Is it blocked by sovereignty/redaction?
- Is it returned by the API context bundle?

### “Why is some text missing?”
- Focus Mode should fail closed if citations/provenance are missing.
- Validate Story Node citation formatting and entity tags (graph IDs).

</details>