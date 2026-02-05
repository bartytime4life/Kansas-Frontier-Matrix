# 🔎 SearchBar 🧭  
> **KFM Web UI component** for searching the **Data Catalog** (datasets) and **full-text/knowledge** (documents, Story Nodes, etc.) — without breaking the API boundary.

![React](https://img.shields.io/badge/React-UI-61DAFB?logo=react&logoColor=000)
![TypeScript](https://img.shields.io/badge/TypeScript-Typed-3178C6?logo=typescript&logoColor=fff)
![A11y](https://img.shields.io/badge/Accessibility-Keyboard%20First-0B7285)
![KFM](https://img.shields.io/badge/KFM-Evidence--First-2B8A3E)

📍 **Location:** `web/src/components/SearchBar/README.md`  
🧱 **Layering rule:** UI ➜ API ➜ Datastores (**no direct PostGIS/Neo4j/Search Index calls from UI**)  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## ✨ What this component is (and isn’t)

### ✅ Responsibilities
- Provide a **fast, accessible search input** with optional suggestions/autocomplete.
- Support **catalog discovery** (datasets) via the API catalog search endpoint.  [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Optionally support **full-text search** (documents / Story Nodes / index-backed results) when the API exposes it (example mentioned as `/search?q=...`).  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Allow **geo-temporal scoping** (bbox from map viewport + time range from timeline) so users can answer:  
  “What data exists **here** and **then**?”

### ❌ Non-goals
- ❌ Does not implement RAG / Focus Mode itself (that’s server orchestration).  
- ❌ Does not query databases directly (API is the enforcement layer).  [oai_citation:3‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- ❌ Does not “invent” metadata; all displayed dataset/doc details come from governed sources (catalog/graph/index).

---

## 🧠 Why SearchBar matters in KFM

KFM’s “Truth Path” expects evidence to flow **Raw ➜ Processed ➜ Catalog ➜ Databases ➜ API ➜ UI/AI**. The SearchBar is one of the primary entry points into that pipeline: it helps users *discover what exists* before they explore maps, timelines, or Focus Mode answers.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Also: KFM’s AI philosophy is **evidence-first** with **clickable citations** where possible; SearchBar results should reinforce trust by showing **provenance signals** (source, license, coverage, dataset IDs).  [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🗺️ Data flow diagram

```mermaid
flowchart LR
  U[👤 User] --> SB[🔎 SearchBar]
  SB -->|GET /api/v1/catalog/search| API[⚙️ KFM API]
  SB -->|GET /search?q=... (if enabled)| API

  API --> CAT[(🗂️ Catalog: DCAT/STAC)]
  API --> IDX[(📚 Search Index / Vectors)]
  API --> KG[(🧩 Knowledge Graph)]
  API --> GIS[(🌍 PostGIS)]

  API --> SB
  SB --> UI[🧱 UI: Results List / Suggestions]
```

---

## 🔌 API Contract (front-end expectations)

### 1) Catalog search (datasets)
KFM documentation explicitly describes a dataset catalog search endpoint:  
`GET /api/v1/catalog/search` supporting keyword search and geo-temporal filters.  [oai_citation:6‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

**Recommended query params**
- `q` — keyword(s) (topic, dataset title, org, etc.)
- `bbox` — `minLon,minLat,maxLon,maxLat` (map viewport or drawn extent)
- `time_start`, `time_end` — ISO-8601 timestamps (timeline window)
- `limit`, `offset` — pagination
- (Optional) `type`, `theme`, `license`, `provider`, `has_assets=true`

**Example**
```http
GET /api/v1/catalog/search?q=railroad&bbox=-102.05,36.99,-94.60,40.00&time_start=1860-01-01&time_end=1900-12-31&limit=20
```

### 2) Full-text search (documents / index)
The blueprint mentions trying an endpoint like `/search?q=railroad` “if it exists” to evaluate full-text search behavior.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**SearchBar stance:** treat this as **optional capability** behind a feature flag (or `scope` switch).

---

## 🧩 Component API (Props)

> The repo blueprint describes `SearchBar` as a reusable component under `web/src/components/` alongside MapViewer, TimelineSlider, StoryPanel, LayerControl, etc.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Below is the **recommended** prop contract (keep it boring + predictable ✅):

| Prop | Type | Default | What it does |
|---|---|---:|---|
| `value` | `string` | `""` | Controlled input value |
| `onChange` | `(value: string) => void` | — | Fires on input change |
| `onSubmit` | `(query: SearchQuery) => void` | — | Fires on Enter / submit |
| `scope` | `"catalog" \| "fulltext" \| "all"` | `"catalog"` | Which backend search to use |
| `bbox` | `[minLon, minLat, maxLon, maxLat] \| null` | `null` | Geo filter from map |
| `timeRange` | `{ start?: string; end?: string } \| null` | `null` | Time filter from timeline |
| `debounceMs` | `number` | `250` | Debounce for suggestion fetch |
| `minChars` | `number` | `2` | Don’t query until N chars |
| `showSuggestions` | `boolean` | `true` | Enables suggestions dropdown |
| `loading` | `boolean` | `false` | External loading state |
| `disabled` | `boolean` | `false` | Disables input |
| `placeholder` | `string` | `"Search datasets & sources…"` | Input placeholder |
| `className` | `string` | `""` | Optional wrapper class |
| `onResultSelect` | `(result: SearchResult) => void` | — | Called on clicking/Enter on a result |
| `renderResult` | `(result: SearchResult) => ReactNode` | — | Override result rendering |

**Recommended type shapes**
```ts
export type SearchScope = "catalog" | "fulltext" | "all";

export type SearchQuery = {
  q: string;
  scope: SearchScope;
  bbox?: [number, number, number, number];
  time_start?: string;
  time_end?: string;
};

export type SearchResult =
  | {
      kind: "dataset";
      id: string; // e.g. "ks_hydrology_1880"
      title: string;
      description?: string;
      license?: string;
      temporal?: { start?: string; end?: string };
      spatial?: { bbox?: [number, number, number, number] };
      provenance?: { provider?: string; source?: string };
    }
  | {
      kind: "document" | "story";
      id: string;
      title: string;
      snippet?: string;
      provenance?: { source?: string; citation?: string };
    };
```

---

## 🧪 Usage examples

### Basic (catalog-only)
```tsx
import { SearchBar } from "./SearchBar";

export function CatalogSearchPanel() {
  const [value, setValue] = useState("");

  return (
    <SearchBar
      value={value}
      onChange={setValue}
      scope="catalog"
      onSubmit={(q) => {
        // call your API adapter (or dispatch redux action)
        // GET /api/v1/catalog/search
        console.log("submit", q);
      }}
    />
  );
}
```

### Scoped by map + timeline (recommended KFM feel)
```tsx
<SearchBar
  value={query}
  onChange={setQuery}
  scope="catalog"
  bbox={mapViewportBbox}
  timeRange={{ start: timelineStartISO, end: timelineEndISO }}
  onSubmit={(q) => runCatalogSearch(q)}
/>
```

---

## ♿ Accessibility requirements (non-negotiable)

Design SearchBar as a **keyboard-first “combobox”** pattern when suggestions are enabled:

### ✅ Checklist
- [ ] Visible `<label>` OR `aria-label` (avoid label-less inputs).
- [ ] Use `role="combobox"` on the input when suggestions exist.
- [ ] Suggestions container uses `role="listbox"`.
- [ ] Each suggestion uses `role="option"`.
- [ ] Arrow keys move active option; Enter selects; Esc closes.
- [ ] `aria-expanded`, `aria-controls`, and `aria-activedescendant` are correct.
- [ ] Screen-reader friendly status text for loading/empty/error (polite live region).
- [ ] Focus is never trapped; Tab exits normally.

> KFM UI changes get extra scrutiny for accessibility, especially where navigation and discoverability are core.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## ⚡ Performance expectations

Search can get expensive quickly (especially if it fans out into hybrid retrieval). Even the AI pipeline calls out **context size + caching** strategies to keep the platform responsive.  [oai_citation:10‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### UI-side performance guardrails
- **Debounce** keystrokes (`debounceMs`).
- **Min chars** before querying (`minChars`).
- **Cancel in-flight** requests when query changes (AbortController).
- **Cache** last N queries in-memory for the session (optional).
- **Pagination**: never render thousands of results in the dropdown.

---

## 🔐 Security & governance notes

KFM’s architecture enforces a strict boundary: the UI calls the API, and the API handles retrieval, policy, and sanitization.  [oai_citation:11‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### UI responsibilities
- Treat all result fields as **untrusted** and render safely (no `dangerouslySetInnerHTML`).
- Never embed raw HTML snippets from search results.
- Never store sensitive queries in persistent storage unless explicitly approved.

### API-side realities (that the UI should anticipate)
- Focus Mode requests include a **Prompt Gate** to reduce prompt injection / malicious input before an LLM sees it.  [oai_citation:12‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
  *Implication:* UI should still keep inputs clean, but assume the API is the policy engine.

---

## 🌐 Internationalization (i18n)

If/when KFM enables multilingual UX, SearchBar should:
- Use translation keys for placeholder text, button labels, and status messages.
- Keep strings in a central resource system (React i18n layer), not hard-coded.  [oai_citation:13‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)

---

## 🧱 Suggested folder layout

> Your actual structure may differ — this is a “good default” 🧩

```text
web/src/components/SearchBar/
├─ SearchBar.tsx
├─ SearchBar.types.ts
├─ SearchBar.module.css
├─ SearchBar.test.tsx
└─ README.md  👈 you are here
```

---

## ✅ Testing guidance

At minimum:
- Unit tests for keyboard navigation (ArrowUp/Down, Enter, Esc).
- Tests for debounce + cancelation (no stale results applied).
- Tests for empty/error states.
- Snapshot tests only if they add value (prefer behavior tests).

> KFM emphasizes reliability with CI quality gates; UI components should be testable and deterministic.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧯 Troubleshooting

### “Search returns nothing”
- Confirm backend is running and the endpoint exists:
  - Swagger UI: `http://localhost:8000/docs` (when available).  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Verify you’re sending bbox/time in the expected format.
- If using full-text scope, confirm `/search` (or equivalent) is implemented/enabled.  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### “Dropdown flickers / stale results show”
- Ensure AbortController cancels prior calls.
- Ensure you only set results for the **latest** request token.

---

## 📚 References (project files)

- **Kansas Frontier Matrix Comprehensive System Documentation** — API endpoints, Focus Mode layering, citations, Prompt Gate, and UI component inventory.  [oai_citation:17‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:18‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:19‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:20‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- **Web Design (reference)** — i18n concepts and UI text management patterns (adapt as needed for React).  [oai_citation:22‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)  [oai_citation:23‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)  
- **Professional Web Design: Techniques & Templates** — layout consistency, component documentation patterns.  [oai_citation:24‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- **Learn to Code HTML & CSS** — semantic structure + baseline accessibility practices.  [oai_citation:25‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- **Node.js / React / CSS / HTML** — general stack alignment reference.  [oai_citation:26‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  
- **Indigenous Statistics** — keep “discoverability” and representation sensitive; avoid flattening community context into simplistic labels.  [oai_citation:27‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)  

---

## 🧭 Maintainer notes (tiny but important)

- If you add new search scopes/filters, update:
  - the prop types
  - the query serializer
  - tests for keyboard + a11y states
  - this README ✅
