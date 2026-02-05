# 🧠 Focus Mode Hooks (`web/src/hooks/focus-mode`)

![React](https://img.shields.io/badge/React-Hooks-61DAFB?logo=react&logoColor=000)
![TypeScript](https://img.shields.io/badge/TypeScript-Strict-3178C6?logo=typescript&logoColor=fff)
![Governance](https://img.shields.io/badge/Governance-Provenance%20First-0B5FFF)
![AI](https://img.shields.io/badge/AI-Evidence%20First-111)

These hooks power **Focus Mode** — the interactive experience where a **Story Node** is presented alongside **map 🗺️ + timeline ⏳ context**, with an AI assistant that must **cite sources** and respect **governance + sovereignty** rules.

---

## 🎯 What this folder is for

This directory exists to make Focus Mode:

- **Composable** (small hooks > giant components)
- **Testable** (pure helpers + MSW-friendly fetch wrappers)
- **Governed-by-default** (fail-closed if citations / provenance guarantees are missing)
- **API-boundary-safe** (no direct DB/graph calls from the browser)

> 🧷 Rule of thumb: the UI should “ask questions” — the backend should “know things”.

---

## 🗂️ Suggested structure

> Your actual filenames may vary — this is the intended mental model.

```text
web/src/hooks/focus-mode/
├─ README.md 🧠
├─ index.ts 📦
├─ useFocusModeChat.ts 💬         # chat state + send/cancel
├─ useFocusModeQuery.ts 🔎        # request/response wrapper (non-stream)
├─ useFocusModeStream.ts 🌊       # streaming transport (SSE/fetch stream)
├─ useFocusModeCitations.ts 🧾    # parse + normalize citation markers/metadata
├─ useFocusModeContext.ts 🧭      # map/timeline/story-node context wiring
├─ useFocusModePolicy.ts 🛡️       # UI-side “hard gate” helpers (safe display)
└─ __tests__/ 🧪
   ├─ citations.test.ts
   └─ chat.test.ts
```

---

## 🧭 Non‑negotiable invariants (KFM rules, enforced in UI *and* backend)

### ✅ 1) API boundary only
The browser **must not** query Neo4j/PostGIS/search indexes directly.  
All access goes through the governed API layer. ⚙️

### ✅ 2) Evidence-first UX
Focus Mode should **not** display factual answers without citations.  
If citations are missing, treat it as a **policy failure** and fail closed. 🔒

### ✅ 3) Opt‑in AI + transparency
Any AI-generated content must be:
- user-triggered (opt-in),
- clearly labeled 🏷️,
- accompanied by confidence/uncertainty metadata when available.

### ✅ 4) No sensitive location leaks
If the system classifies location detail as sensitive, UI must not “reconstruct” or reveal it.  
(Do not display raw coords if the backend generalized/omitted them.) 🫥

---

## 🧩 Hook responsibilities (recommended split)

### `useFocusModeChat` 💬
Owns the conversation lifecycle:
- messages: user + assistant turns
- send(question)
- cancel() (AbortController)
- status: `idle | loading | streaming | error`
- persistent session context (if your app uses a sessionId)

### `useFocusModeQuery` 🔎
A thin, testable wrapper around your Focus Mode API:
- `query(question, context)` → `{ answer, citations, sessionId, ... }`
- normalizes errors into a stable shape for UI

### `useFocusModeStream` 🌊
Streaming transport layer:
- Server-Sent Events (SSE) **or**
- fetch streaming (`ReadableStream`)  
Should emit incremental tokens/chunks and a final “done” event.

### `useFocusModeCitations` 🧾
Keeps citation handling deterministic:
- parses numeric markers like `[1] [2]`
- maps markers → citation metadata
- provides render-friendly outputs (footnote list, source badges, etc.)

### `useFocusModeContext` 🧭
Bridges UI context into AI requests:
- active Story Node id
- selected entities (place/event/document ids)
- map viewport / bbox
- timeline time range

### `useFocusModePolicy` 🛡️
UI hard-gates:
- `requireCitations(answer, citations)` (fail closed)
- `sanitizeDisplayText(answer)` (escape/strip unsafe formatting if needed)
- `shouldShowAiHint({ optIn, labeled, confidence })`

---

## 🔌 Backend contract (how hooks should think about the API)

KFM supports a “governed AI” flow where the frontend posts a question, backend runs retrieval + policy gates, and returns:

- **Answer text** with citation markers (e.g., `...drought conditions[1]...`)
- **Citation metadata** (source mapping for `[1]`, `[2]`, …)
- Optional: session id, debug provenance ids, streaming channel id, etc.

### Endpoints (common patterns)
Your deployment may expose either (or both):

- `POST /focus-mode/query` (UI-friendly alias / BFF route)
- `POST /api/v1/ai/query` (versioned API)
- `GET|POST /api/v1/ai/stream` (streaming)

> 🧠 Keep endpoint choice *behind* the hook — components should never care.

---

## 🧱 Types (recommended)

> These types are intentionally conservative and future-proof.

```ts
export type FocusModeRole = "user" | "assistant" | "system";

export type FocusModeMessage = {
  id: string;
  role: FocusModeRole;
  content: string;
  createdAt: string; // ISO
};

export type FocusModeContext = {
  storyNodeId?: string;         // provenance-linked Story Node
  entityIds?: string[];         // graph ids (place/event/document/etc.)
  bbox?: [number, number, number, number]; // [west,south,east,north]
  timeRange?: { start: string; end: string }; // ISO dates
};

export type FocusModeCitation = {
  n: number;                    // 1..N marker
  title: string;
  kind?: "document" | "dataset" | "graph" | "story_node" | "external";
  refId?: string;               // stable id (doc id / dataset id / node id)
  url?: string;                 // optional deep link
  snippet?: string;             // optional excerpt
};

export type FocusModeQueryResponse = {
  answer: string;               // includes markers like [1]
  citations: FocusModeCitation[];
  sessionId?: string;
  provenanceId?: string;        // optional audit trail pointer
};
```

---

## 🧪 Usage example (non-stream)

```tsx
import { useFocusModeChat } from "@/hooks/focus-mode";

export function FocusModePanel() {
  const { messages, send, cancel, status, error } = useFocusModeChat({
    context: { storyNodeId: "sn_ks_frontier_001" },
  });

  return (
    <section>
      <header>
        <h2>Focus Mode</h2>
        {status === "loading" && <span>Thinking…</span>}
        {status === "streaming" && <span>Streaming…</span>}
        {error && <span role="alert">{error.message}</span>}
      </header>

      <ol>
        {messages.map(m => (
          <li key={m.id}>
            <strong>{m.role}:</strong> {m.content}
          </li>
        ))}
      </ol>

      <footer>
        <button onClick={() => send("What happened during the 1930s drought?")}>
          Ask
        </button>
        <button onClick={cancel} disabled={status !== "loading" && status !== "streaming"}>
          Cancel
        </button>
      </footer>
    </section>
  );
}
```

---

## 🌊 Usage example (streaming)

```ts
const { streamAnswer, cancel } = useFocusModeStream();

const run = async () => {
  const chunks: string[] = [];
  await streamAnswer(
    { question: "Summarize this Story Node with citations.", context: { storyNodeId } },
    {
      onToken: (t) => chunks.push(t),
      onDone: (final) => console.log("done", final),
      onError: (e) => console.error(e),
    }
  );
};
```

---

## 🧾 Citation rendering pattern (the UI contract)

### What the model returns
- Inline numeric markers: `...[1] ...[2]`
- Citation list entries that explain what `[1]` and `[2]` refer to

### What the UI must do
- Render markers as clickable footnotes 🔗
- Provide source metadata: title, dataset id, doc id, etc.
- Never show “source-less” factual content

<details>
<summary>🧩 Minimal citation parser (marker extraction)</summary>

```ts
const CITATION_RE = /\[(\d+)\]/g;

export function extractCitationNumbers(answer: string): number[] {
  const out = new Set<number>();
  let m: RegExpExecArray | null;
  while ((m = CITATION_RE.exec(answer)) !== null) {
    out.add(Number(m[1]));
  }
  return [...out].sort((a, b) => a - b);
}
```

</details>

---

## 🛡️ UI hard-gates (fail closed)

### ✅ Gate 1: No-citation → no display
If the backend returns an “answer” without citations:
- do **not** render it as factual output
- show a policy error state (“No source, no answer”)

### ✅ Gate 2: Only provenance-linked content in Focus Mode
If something lacks a stable id / provenance pointer:
- keep it out of Focus Mode surfaces (map popups, timeline panels, Story Node panels)

### ✅ Gate 3: Sensitive map handling
If the API provides generalized geometry:
- respect it
- don’t try to “improve precision” client-side

---

## 🧪 Testing guidance

### Unit tests (fast)
- citation extraction + mapping
- policy gates (`requireCitations`)
- reducer/state transitions (chat hook)

### Integration tests (realistic)
- mock API with MSW
- validate abort/cancel behavior
- validate streaming event ordering

> 🧪 Tip: treat “missing citations” as a **test fixture**, not a rare edge case.

---

## 🧰 Contributing to this folder

When adding a new hook:

- ✅ keep it framework-native (React hooks only; no hidden singletons)
- ✅ keep fetch calls behind a single client wrapper
- ✅ make it deterministic (pure helpers for parsing/policy)
- ✅ document the contract here (what it returns, what it assumes)
- ✅ add tests for governance failures 🔒

---

## 🔗 Related concepts (for orientation)

- **Story Nodes** 📝: machine-ingestible narrative + citations + semantic entity references  
- **Focus Mode** 🔍: Story Node + map/timeline context, governed interaction surface  
- **Provenance** ⛓️: everything must be traceable back to catalog/graph evidence

---