<!--
File: web/src/services/README.md
Purpose: Web “services” (integration/adapters) documentation for KFM.
-->

# 🧩 `web/src/services` — Web Services (Integration Layer)

![Layer](https://img.shields.io/badge/layer-integration%20%26%20adapters-blue)
![Boundary](https://img.shields.io/badge/boundary-governed%20API%20only-critical)
![Governance](https://img.shields.io/badge/governance-fail--closed-important)

This directory is the **trust-membrane boundary** for the web client.

It contains the code that is allowed to:
- call the **KFM Governed API** (REST + optional GraphQL),
- connect to **realtime transports** (WebSocket/SSE),
- read/write **browser persistence** (IndexedDB / Cache API / storage),
- emit **telemetry** (PII-safe, schema’d),
- implement **offline-first sync** primitives.

> [!IMPORTANT]
> UI components/hooks should **depend on services**. Services should **never depend on UI**.

---

## Why this folder exists

KFM is designed around a “governed middle tier”:
- The UI is a **thin client**.
- **Policy enforcement + audit + provenance** happen at the API boundary.
- The web client should not “bypass governance” by reaching around the API.

This folder makes that boundary concrete and reviewable.

---

## Non-negotiables

> [!CAUTION]
> If you are about to violate one of these, stop and trigger a governance review.

### ✅ Allowed
- Calling `GET/POST/... /api/v1/...` endpoints.
- (Optional) Calling `/graphql` **only** when it is routed through the same governed service logic as REST.
- Fetching evidence/provenance artifacts (receipts, citations, dataset metadata) **for read-only display**.
- Emitting **schema-validated** telemetry events that avoid PII and sensitive details.

### ❌ Not allowed
- **Direct database access** of any kind (obvious, but worth stating).
- Direct calls to any LLM provider from the browser.
- Sending free-text telemetry payloads that could contain PII or sensitive locations.
- Copy/pasting “fetch() everywhere” patterns into random UI files (keep network IO centralized).

---

## Suggested directory layout

> [!NOTE]
> This is a recommended baseline. If your repo layout differs, update the tree below to match reality.

```text
web/src/services/
├─ README.md
├─ http/
│  ├─ httpClient.ts              # fetch wrapper + headers + retries + error mapping
│  ├─ requestContext.ts          # correlation IDs, auth context, locale, etc.
│  └─ errors.ts                  # ApiError, NetworkError, PolicyDeniedError, etc.
├─ api/
│  ├─ catalogService.ts          # search/catalog endpoints
│  ├─ datasetsService.ts         # datasets/tiles/metadata endpoints
│  ├─ storyService.ts            # story nodes, timeline, layers
│  ├─ focusModeService.ts        # Focus Mode query + citations
│  └─ evidenceService.ts         # receipts/provenance resolver (read-only)
├─ graphql/                      # (optional) GraphQL client + typed operations
│  ├─ client.ts
│  └─ operations/
├─ realtime/
│  ├─ websocketClient.ts         # presence, collaboration, live updates
│  └─ channels.ts                # channel names + payload schemas
├─ storage/
│  ├─ indexedDb.ts               # durable local store wrapper
│  ├─ cache.ts                   # Cache API helper
│  └─ kv.ts                      # small key/value (non-sensitive)
├─ sync/
│  ├─ queue.ts                   # offline queue + retry/backoff
│  └─ serviceWorkerBridge.ts     # background sync hooks (if used)
├─ telemetry/
│  ├─ emitter.ts                 # schema’d UI events (PII-safe)
│  ├─ schemas/                   # JSON schemas (or TS runtime validators)
│  └─ redact.ts                  # defensive redaction helpers
└─ types/
   ├─ dto.ts                     # transport DTOs
   └─ models.ts                  # client-facing models (mapped from DTOs)
```

---

## Service design rules

### 1) Services are adapters, not “business logic”
- Put **domain rules** in a domain layer (`web/src/domain/...` or feature-domain folders).
- Put **IO + mapping** in services:
  - request building,
  - response decoding,
  - error mapping,
  - retries/backoff,
  - caching/offline queue,
  - telemetry emission (PII-safe).

### 2) Every call must be traceable
At minimum, every request should carry:
- a per-request **correlation ID** (generated client-side if missing),
- auth context (if authenticated),
- a stable **client/app version** (helps audit + debugging).

> [!TIP]
> If the backend already issues a correlation ID, propagate it through subsequent calls too.

### 3) Prefer explicit typing at the boundary
- DTOs represent what the API actually sends.
- Map DTOs into client-facing models, and keep the mapping code here.

### 4) Fail closed (client-side)
The backend is designed to deny when policy is uncertain; the UI must treat deny/blocked responses as *normal*:
- show a policy-safe message,
- avoid retry storms,
- avoid “leaking” restricted details into logs/toasts.

### 5) No sensitive leakage in telemetry/logging
- Avoid free text.
- Avoid precise coordinates unless explicitly permitted by policy.
- If you must log, log **structural** facts only (event types, IDs, coarse buckets).

---

## Request context contract

Define and pass a single “request context” object to all services.

Example:

```ts
export type RequestContext = {
  baseUrl: string;

  /** Unique per user action / request chain */
  correlationId: string;

  /** Authn context (implementation-specific) */
  accessToken?: string;

  /** Locale info (optional) */
  locale?: string;
  timezone?: string;

  /** App/build metadata (optional but useful) */
  clientVersion?: string;
};
```

---

## HTTP client pattern

> [!TIP]
> Keep `fetch` usage inside `http/httpClient.ts` only.

```ts
export interface HttpClient {
  get<T>(path: string, init?: RequestInit): Promise<T>;
  post<T>(path: string, body: unknown, init?: RequestInit): Promise<T>;
  patch<T>(path: string, body: unknown, init?: RequestInit): Promise<T>;
  delete<T>(path: string, init?: RequestInit): Promise<T>;
}
```

### Error mapping
Normalize errors into a small set of types:
- `NetworkError` (offline/DNS/timeouts)
- `ApiError` (non-2xx)
- `PolicyDeniedError` (403/451/etc)
- `ConflictError` (412 precondition, ETag mismatch)

---

## Focus Mode service

Focus Mode calls are **server-side RAG + governance**; the browser sends the question + context and renders the answer + citations.

```ts
export type FocusQueryRequest = {
  question: string;
  context?: {
    bbox?: [number, number, number, number]; // optional; keep coarse if sensitive
    year?: number;
    activeLayerIds?: string[];
    selectedEntityIds?: string[];
  };
};

export type FocusQueryResponse = {
  answer_markdown: string;
  citations: Array<{
    id: string;
    label?: string;
    source_kind: "dataset" | "document" | "graph";
    source_id: string;
    snippet?: string;
    uri?: string;
  }>;
};

export async function askFocusMode(http: HttpClient, req: FocusQueryRequest) {
  // Example endpoint; keep all AI logic server-side.
  return http.post<FocusQueryResponse>("/api/v1/ai/query", req);
}
```

---

## Offline-first + sync

When a feature requires offline support:
- write **durable state** to local storage first (IndexedDB),
- enqueue an upload/sync job,
- let the sync layer flush when online (service worker optional).

Suggested primitives:
- `LocalStore` (IndexedDB)
- `SyncQueue` (retry/backoff + batching)
- `Reconciler` (handles conflict responses like 412)

---

## ETag / conditional writes

For user-editable resources (profiles, preferences, story edits), prefer:
- `GET` returns `ETag`
- `PATCH/PUT` uses `If-Match: <etag>`
- `412 Precondition Failed` triggers a merge flow

> [!NOTE]
> This avoids blind overwrites and makes conflicts explicit.

---

## Telemetry (PII-safe)

Telemetry must be **schema’d** and **defensive**.

Recommended rules:
- **no free-text**
- **no precise coordinates** unless already public + approved
- buffer events, flush on:
  - every N events,
  - `visibilitychange`,
  - periodic timer (bounded)

Example schema shape:

```ts
export type UiEvent = {
  event_name:
    | "story.next"
    | "story.prev"
    | "layer.toggle"
    | "timeline.scrub"
    | "citation.open";

  story_node_id?: string;
  timestamp_bucket: string; // e.g., "2026-02-17T15:00Z"

  // only enums / IDs / coarse buckets
  layer_id?: string;
};
```

---

## Adding a new service

1. Create `api/<thing>Service.ts`
2. Add DTO types in `types/dto.ts` (or `types/<thing>.dto.ts`)
3. Add mapping function(s) into `types/models.ts` (or `types/<thing>.mapper.ts`)
4. Add unit tests:
   - request building
   - response decoding
   - error mapping
5. Add contract tests (if you have OpenAPI/GraphQL schemas available)
6. Add telemetry events only if:
   - schema exists
   - redaction rules exist
   - governance sign-off is recorded

---

## Definition of Done checklist

- [ ] Service uses centralized `HttpClient` (no raw `fetch()` in the service)
- [ ] Typed request/response DTOs + mapping
- [ ] Correlation ID propagated
- [ ] Errors normalized into standard error types
- [ ] Telemetry (if any) is schema’d + redacted + tested
- [ ] Unit tests added
- [ ] Contract tests updated (if applicable)
- [ ] No sensitive data in logs/toasts
- [ ] Docs updated (this README + endpoint notes)

---

## Governance review triggers

Open a governance review if you:
- add a new endpoint that exposes sensitive layers/datasets
- add new telemetry fields (especially anything that could carry PII)
- add any storage of user content to the browser
- add a new realtime channel that could expose presence/scope
- introduce GraphQL queries that increase data surface area

---

## Quick troubleshooting

**“Why is the API returning 403?”**
- Treat it as policy enforcement, not “an error”. Surface a safe UI message and log the correlation ID.

**“Why does a PATCH fail with 412?”**
- You likely have an ETag conflict. Refresh the resource, merge client changes, retry with the latest ETag.

**“Why are we getting intermittent websocket disconnects?”**
- Confirm reconnect backoff is bounded and that you dedupe events after reconnect.

---

## Related (governed) docs

> [!NOTE]
> Add/replace links below to match the actual repo documentation layout.

- KFM API contracts (OpenAPI / GraphQL schema) *(not confirmed in repo)*
- Governance & policy boundary overview *(not confirmed in repo)*
- Focus Mode UI + citations behavior *(see project blueprint PDFs in repo docs)*