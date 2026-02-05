# 🧠 Focus Mode (`web/src/features/focusMode`)

![status](https://img.shields.io/badge/status-active-success)
![ui](https://img.shields.io/badge/ui-React%20%2B%20TypeScript-blue)
![principle](https://img.shields.io/badge/principle-evidence--first-important)
![governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-informational)
![provenance](https://img.shields.io/badge/provenance-PROV%20%7C%20STAC%20%7C%20DCAT-9cf)

> **Focus Mode** is the trust-first “interactive reading” experience: a **Story Node** 📜 is presented alongside **map** 🗺️ + **timeline** 🕰️ context, with an optional **AI assistant** that must stay grounded in sources (and must *fail closed* if it can’t).

---

## 📌 What lives in this folder?

This feature module owns the **Focus Mode UI** experience:

- 🧾 **Story context capture** (which story node the user is reading, what map/timeline scope is active)
- 💬 **Ask panel** (the Focus Mode AI chat / Q&A panel)
- 🧩 **Citation rendering** (clickable footnotes, source cards, provenance views)
- 🛡️ **Fail-closed UX** (missing provenance / missing citations / policy-blocked responses)
- ♿ **Accessibility + keyboard navigation** for an analysis-heavy UI

This folder does **not** own:

- 🗃️ Database queries (Neo4j/PostGIS)  
- 🧠 LLM calls (Ollama or other)  
- 🔐 Policy enforcement / governance gates  

Those are handled behind the governed **API layer**.

---

## 🧭 Key principles (non-negotiable)

### 🚦 Hard gates

Focus Mode is intentionally strict:

- **No provenance → no UI surface**
- **No citations → no answer**
- **Sensitive data → generalized/redacted**
- **AI is opt-in, labeled, and never “silently” edits the narrative**
- **When in doubt: fail closed, show a helpful next action**

### 🧱 Layering rule

The web app must **never** talk to the knowledge stores or LLM directly.

✅ Web UI → API → (Neo4j/PostGIS/Index/LLM)  
❌ Web UI → Neo4j/PostGIS/LLM

---

## 🧩 Suggested module layout

> Your repo may differ—treat this as a *target shape* that keeps Focus Mode coherent.

```text
📦 web/src/features/focusMode/
├─ 📄 README.md
├─ 📁 components/
│  ├─ 🧩 FocusModePanel.tsx           # Container: story context + chat + citations
│  ├─ 🧩 FocusChatThread.tsx          # Message list + streaming display
│  ├─ 🧩 FocusComposer.tsx            # Input box + prompt helpers + submit
│  ├─ 🧩 CitationFootnotes.tsx        # [1][2] markers → clickable refs
│  ├─ 🧩 CitationDrawer.tsx           # Source cards + provenance detail
│  ├─ 🧩 ProvenanceBadge.tsx          # “Verified / Redacted / Blocked” labeling
│  └─ 🧩 ReasoningDrawer.tsx          # Optional “Show reasoning” surface (if enabled)
├─ 📁 api/
│  ├─ 🔌 focusModeClient.ts           # fetch wrappers for query/stream/suggestions
│  └─ 🧾 focusModeContracts.ts        # UI-side types mirroring server contract
├─ 📁 state/
│  ├─ 🗂️ focusModeSlice.ts            # threads, messages, citations, ui flags
│  └─ 🪝 useFocusMode.ts              # hooks: selectors + actions
├─ 📁 utils/
│  ├─ 🧪 parseCitations.ts            # robust citation parsing + mapping
│  ├─ 🧼 sanitizeAnswer.ts            # safe markdown/render pipeline
│  └─ 🧯 redactSensitive.ts           # UI-side redaction helpers (defense in depth)
└─ 📁 __tests__/
   ├─ 🧪 parseCitations.test.ts
   ├─ 🧪 focusModeClient.test.ts
   └─ 🧪 focusModeGates.test.ts
```

---

## 🏗️ Architecture at a glance

```mermaid
flowchart LR
  subgraph WEB[🌐 Web UI (React/TS)]
    SN[📜 Story Node Viewer]
    MAP[🗺️ Map Context]
    TL[🕰️ Timeline Context]
    FM[🧠 Focus Mode Panel]
  end

  subgraph API[🧩 Governed API Layer]
    ORCH[🔁 Focus Orchestrator]
    POL[🛡️ Policy Gate]
  end

  subgraph STORES[🗃️ Knowledge Stores]
    KG[(Neo4j)]
    PG[(PostGIS)]
    IDX[(Doc/Vector Index)]
  end

  LLM[(🧠 LLM Runtime)]

  SN --> FM
  MAP --> FM
  TL --> FM

  FM -->|query/stream| ORCH
  ORCH --> KG
  ORCH --> PG
  ORCH --> IDX
  ORCH --> LLM
  ORCH --> POL
  POL -->|answer + citations + provenance + policy flags| FM
```

---

## 🔌 API touchpoints (frontend expectations)

> Exact routes live in the server’s OpenAPI/route docs. The frontend should treat these as **contract-driven**.

Common endpoints:

- `POST /api/v1/ai/query`  
  - Non-streaming Q&A (returns full answer + citations)
- `POST /api/v1/ai/stream`  
  - Streaming Q&A (SSE/chunked response)
- `GET /api/v1/ai/suggestions?context=...`  
  - Suggest next questions / prompts for the current story context

### ✅ Focus Mode request: context is part of the question

Your UI should send enough context for retrieval to be accurate, without leaking sensitive details:

- story node ID / slug
- time range (coarse)
- map viewport (coarse bbox)
- selected entities / layers
- governance context / visibility class (if available)

### ✅ Focus Mode response: always includes citations + policy info

The UI should expect:

- `answer` (markdown or plain text)
- `citations[]` (structured)
- `provenance[]` / `sources[]` (structured, resolvable)
- `policy` (allow / redact / block + reasons)
- `trace` (request ID, timestamps, model metadata) if enabled

> **UI rule:** if the response has no usable citations, treat it as **non-compliant** and show the “No Source, No Answer” UX.

---

## 🧾 Citations & provenance UX

### 🎯 What we render

- Inline markers like `[1]`, `[2]`, … (or other agreed marker style)
- A footnotes area with **clickable** references
- A right-side (or bottom) drawer with:
  - source title
  - source type (Story Node / Dataset / Document / Graph Node)
  - excerpt/snippet (if allowed)
  - provenance chain (PROV-style, if present)
  - classification badges (public/internal/sensitive)

### 🧠 Parsing rules (recommended)

- Treat citation markers as *references*, not content:
  - Never allow markers to become executable HTML
  - Never allow “source cards” to render unsanitized markdown from the server
- Be resilient:
  - `answer` contains markers but `citations[]` missing → show error state
  - `citations[]` present but markers missing → render citations as “Sources” section

---

## 🧠 AI transparency & user control

Focus Mode AI must be:

- ✅ **opt-in** (user intentionally enters Focus Mode / clicks “Ask”)
- ✅ clearly labeled **AI-generated**
- ✅ grounded with citations and provenance
- ✅ optionally “explainable” via a **Show reasoning** toggle, if enabled

> **Important:** “Show reasoning” must never leak sensitive locations, restricted metadata, or any data that policy would otherwise hide.

---

## 🔒 Sensitive data, sovereignty, and safe display

Focus Mode must protect sensitive contexts, including:

- archeological site precision
- sacred lands / sensitive locations
- any data labeled internal/sensitive by governance rules

Recommended UI patterns:

- 🫥 **Generalize** location data (county/region level) when sensitivity is present
- 🧊 **Blur** or “fuzz” map markers for protected coordinates
- 🚫 **Disable** copy/export for restricted fields
- 🏷️ Always surface **classification badges** near sources and answers
- 🧾 Provide a “Why is this hidden?” explanation tied to policy codes

---

## 🧠 State management model

Focus Mode tends to behave like a “threaded chat bound to context”.

Suggested state shape:

- multiple threads per Story Node (optional)
- active thread ID
- messages ordered by time
- citations mapped by message ID
- UI flags: streaming, blocked, redacted, showReasoning, drawerOpen, etc.

> Tip: treat the **story node ID + time range + viewport** as the “context key” for thread grouping. This makes history predictable.

---

## ⚡ Performance & streaming

### 🧵 Streaming UX

If streaming is enabled:

- render partial tokens as they arrive
- do not “lock up” the story reader while generating
- finalize citation linking after completion (or progressively if the contract supports it)

### 🧠 Caching-friendly behavior

The backend may cache context for repeated questions; the frontend should help by:

- reusing a `threadId` / `conversationId` (if supported)
- sending stable context IDs (story node IDs, dataset IDs), not raw blobs
- avoiding repeated requests on fast UI events (debounce viewport changes)

---

## 🧪 Testing checklist

### Unit tests
- citation parser (markers → footnotes)
- “No Source, No Answer” gate (missing citations)
- redaction rendering (blocked/redacted states)
- sanitizer (no HTML/script execution)

### Integration tests
- mock API query response with citations + provenance
- mock policy block response (ensure UI fails closed)
- streaming response completion (ensure final message is stable)

### UX regression
- keyboard-only navigation through:
  - story node
  - focus panel
  - citations drawer
- screen reader labels for:
  - send button
  - citations list
  - policy badges

---

## ✅ Definition of Done (DoD)

A Focus Mode PR is “done” when:

- [ ] Answer rendering is safe (sanitized) and accessible
- [ ] “No Source, No Answer” is enforced in UI
- [ ] Citations are clickable and resolve to a source card
- [ ] Sensitive location display is generalized/redacted when required
- [ ] UI never talks directly to DBs or LLM
- [ ] Unit + integration tests cover gates + citation parsing
- [ ] Docs updated (this README + any contract docs)

---

## 🧰 Troubleshooting

### “Answer returned, but no citations”
- Treat as contract violation → show “No Source, No Answer”
- Provide CTA:
  - “Try a narrower question”
  - “Open Sources”
  - “Ask for quotes / dataset rows”

### “Streaming freezes”
- Ensure request cancellation is supported (AbortController)
- Ensure UI can re-render partial content without heavy markdown parsing each chunk

### “Policy blocked the response”
- Render a blocked card with:
  - policy reason codes
  - what the user can do next (broaden region, request aggregated stats, etc.)

---

## 🔗 Related docs (recommended reading)

- 📘 `docs/MASTER_GUIDE_v13.md`
- 🧱 `docs/architecture/system_overview.md`
- 🧠 `docs/architecture/AI_SYSTEM_OVERVIEW.md`
- 🧾 `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- 🔌 `src/server/api/README.md` (API contract + routes)
- 🗺️ `docs/architecture/ai/OLLAMA_INTEGRATION.md` (if present)

---

## 🧾 Glossary

- **Story Node**: a narrative unit with strict citations, metadata, and provenance.
- **Provenance**: chain-of-custody from raw → processed → catalog → API → UI.
- **Hard gate**: an enforcement rule that must fail closed (no silent degradation).
- **FAIR + CARE**: governance principles used to balance openness with community rights and safety.

---
