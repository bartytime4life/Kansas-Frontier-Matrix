# 📡 Telemetry Adapter (Web)

![status](https://img.shields.io/badge/status-active%20spec-blue)
![layer](https://img.shields.io/badge/layer-adapter%20%2F%20integration-6f42c1)
![principles](https://img.shields.io/badge/principles-provenance--first%20%7C%20contract--first%20%7C%20privacy--first-2ea44f)
![governance](https://img.shields.io/badge/governance-audit%20%26%20sovereignty-ff8c00)

> **What this is:** the **single** place the KFM Web UI emits telemetry.  
> **What this is not:** a “sprinkle analytics anywhere” free‑for‑all.

---

## 🎯 Goals

Telemetry in KFM is **not just product analytics**. It exists for:

- **Governance-grade audit trails** (especially around *sensitive data* + Focus Mode redactions)  
- **Operational observability** (errors, performance, WebGL stability, API latency)  
- **User experience & mapping usability** (what’s used, what’s confusing, what’s slow)  
- **Research-ready measurement** (events structured for reproducible analysis, not vibes)

> [!IMPORTANT]
> Treat telemetry as **governed data**. The *logs themselves* can be sensitive.

---

## 🧱 Where this fits in the architecture

KFM’s canonical pipeline ordering is:

`ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode`

Telemetry is a **cross-cutting signal layer** that must never violate the boundary rules of the pipeline. In practice:

- The UI should only reference **stable identifiers** (catalog/graph/API IDs), not raw source artifacts.
- Telemetry must never become a **side-channel** for sensitive data (e.g., “accidentally” logging precise coordinates).

This folder implements an **Adapter**: it translates UI intents into a consistent event contract and forwards them to a configured **sink** (HTTP, console, noop, etc.).

---

## 🗂️ Suggested folder layout (typical)

> This README documents the *contract* and *expected patterns*. Your actual filenames may differ.

```text
📁 web/
  📁 src/
    📁 adapters/
      📁 telemetry/
        📄 README.md          👈 you are here
        📄 index.ts           (public exports)
        📄 types.ts           (event + context types)
        📁 sinks/
          📄 noop.ts          (tests / disabled)
          📄 console.ts       (local dev)
          📄 http.ts          (production ingestion)
        📁 __tests__/
          📄 telemetry.test.ts
```

---

## 🔁 Event flow

```mermaid
flowchart LR
  UI[🧭 UI Components] -->|track()| A[📡 Telemetry Adapter]
  A --> Q[(🗃️ Queue / Batch)]
  Q -->|flush| S{{🚚 Sink}}
  S -->|ingest| API[🌐 Telemetry Endpoint]
  API --> Store[(📦 Audit/Observability Store)]
  Store --> Dash[📊 Dashboards & Governance Views]
```

---

## 🧾 Telemetry contract

### ✅ Event envelope (minimum)

Telemetry events must be **schema-friendly** and **analysis-ready**.

```ts
export type TelemetryEventName =
  | "ui_page_view"
  | "ui_map_layer_toggle"
  | "ui_map_pan_zoom"
  | "ui_search_execute"
  | "story_node_open"
  | "focus_mode_enter"
  | "focus_mode_exit"
  | "focus_mode_redaction_notice_shown"
  | "governance_sensitive_access_attempt"
  | "error_boundary_triggered"
  | "perf_web_vitals"
  | string; // allow extension, but prefer enumerating

export type TelemetrySeverity = "debug" | "info" | "warn" | "error";

export interface TelemetryEvent {
  v: 1;                         // schema version
  name: TelemetryEventName;      // stable event name
  ts: string;                    // ISO-8601 timestamp
  severity?: TelemetrySeverity;

  // ✅ stable IDs only
  session_id: string;            // random UUID per session
  actor_id?: string;             // OPTIONAL; pseudonymous (see privacy rules)

  // ✅ context required for debugging + analysis
  context: {
    app: "web";
    env: "local" | "dev" | "staging" | "prod" | string;
    build_id?: string;           // git SHA / build number
    route?: string;

    viewport?: { w: number; h: number; dpr?: number };
    locale?: string;
    tz?: string;
  };

  // ✅ event-specific payload (strictly governed)
  props?: Record<string, unknown>;

  // ✅ governance signals (when relevant)
  governance?: {
    classification?: "public" | "restricted" | "confidential" | string;
    redaction_applied?: boolean;
    decision?: "allow" | "block" | "degrade";
    policy_id?: string;
  };
}
```

### ✅ Naming rules

- Prefer **snake_case** event names for consistency with governance examples (e.g., `focus_mode_redaction_notice_shown`).
- Names should be:
  - **Stable** (don’t rename casually)
  - **Action-oriented** (verb present)
  - **Non-PII** (never embed user content)

---

## 🧠 Public API (what UI code should call)

A minimal adapter API should cover:

- `track(name, props?, options?)`
- `setContext(partialContext)`
- `identify(actorId)` *(optional, pseudonymous only)*
- `flush()` *(best-effort)*
- `enable()/disable()` *(feature flag + consent)*

### Example usage

```ts
import { telemetry } from "./"; // or "@/adapters/telemetry"

telemetry.track("ui_page_view", {
  route: "/atlas",
  referrer: document.referrer ? "present" : "none", // ✅ do not log full URL if it can leak info
});

telemetry.track("ui_map_layer_toggle", {
  layer_id: "dcat:ks:historic_parcels:v3",  // ✅ stable dataset/layer ID
  enabled: true,
});

telemetry.track("focus_mode_redaction_notice_shown", {
  redaction_type: "location_generalized",
  reason: "sensitive_layer_policy",
});
```

> [!TIP]
> If you *must* compute expensive props, make them **lazy** so disabled telemetry doesn’t cost time.

---

## 🧭 Event taxonomy (recommended)

| Category | Examples | Purpose |
|---|---|---|
| 🧭 UI navigation | `ui_page_view`, `story_node_open` | Understand flow + drop-off |
| 🗺️ Map interaction | `ui_map_pan_zoom`, `ui_map_layer_toggle` | Usability + performance |
| 🔎 Search/query | `ui_search_execute` | Relevance + discoverability |
| 🧠 Focus Mode | `focus_mode_enter`, `focus_mode_redaction_notice_shown` | Governance + trust |
| ⚖️ Governance | `governance_sensitive_access_attempt` | “Who saw what and why” |
| 💥 Errors | `error_boundary_triggered` | Reliability + triage |
| ⚡ Performance | `perf_web_vitals`, `webgl_context_lost` | Regression detection |

---

## ⚖️ Governance & sovereignty rules (non-negotiable)

### 1) No sensitive location leaks (including via telemetry)
- **Never** log raw lat/lon for sensitive layers.
- Prefer:
  - coarse bounding boxes (rounded),
  - low-precision geohash / grid cell,
  - or “interaction happened” without coordinates.

> [!CAUTION]
> Telemetry can become a **side-channel**. Treat it like an export surface.

### 2) Stable identifiers > raw values
If you need to reference something:
- ✅ `layer_id`, `dataset_id`, `graph_node_id`, `prov_bundle_id`
- ❌ full text from user inputs, full URLs, raw geometry, raw addresses

### 3) Redaction is a first-class signal
When the UI degrades or withholds information:
- emit an explicit governance event like:
  - `focus_mode_redaction_notice_shown`
  - `governance_sensitive_access_attempt { decision: "degrade" | "block" }`

### 4) Consent and user autonomy
Telemetry should support:
- **opt-in / opt-out** (where required or appropriate)
- clear purpose limitation (UX + governance, not surveillance)
- minimal retention + access control on the receiving side

---

## 🔐 Privacy & pseudonymization (practical rules)

### ✅ Allowed
- Random `session_id` per session
- Coarse device context (viewport size, DPR)
- Performance metrics (web vitals, timings)
- Stable dataset/layer IDs (as governed identifiers)

### ❌ Never log
- names, emails, phone numbers
- full search strings (unless explicitly approved + scrubbed)
- full referrer URLs (can leak sensitive paths/query params)
- access tokens, auth headers, cookies
- raw GPS location

### Pseudonymous actor IDs
If you must correlate behavior across sessions, use:
- a **server-issued pseudonymous ID**, or  
- a **one-way hash** with rotation/salt strategy managed server-side.

> [!IMPORTANT]
> Don’t invent cryptography in the UI. If correlation is required, define it as an explicit contract with backend governance.

---

## ⚡ Performance & reliability (don’t hurt the UI)

Telemetry must be **best-effort** and never block critical rendering:

- Batch events (queue + periodic flush)
- Use `navigator.sendBeacon()` on unload where available
- Use sampling for high-frequency events (`ui_map_pan_zoom`)
- Drop events when offline or queue limit exceeded (with counters)

> [!NOTE]
> Prefer “measure less, measure better” over firehose logging.

---

## 🧪 Testing strategy

### Unit tests
- Default sink should be **Noop** in test environments.
- Provide a deterministic “in-memory sink” for assertions.

```ts
const sink = createInMemorySink();
const telemetry = createTelemetry({ sink });

telemetry.track("ui_page_view", { route: "/atlas" });

expect(sink.events).toHaveLength(1);
expect(sink.events[0].name).toBe("ui_page_view");
```

### Contract tests
If you maintain JSON Schemas (recommended), validate:
- event envelope
- per-event props
- versioning behavior (`v` increments only on breaking changes)

---

## 📊 Analytics-ready by design (avoid bad science)

Telemetry often powers decisions. To keep it defensible:

- Define metrics *before* comparing variants (avoid p-hacking / multiple testing traps)
- Prefer stable definitions (same denominator, same units)
- Keep raw events immutable; do derived metrics in downstream jobs
- Use holdouts / out-of-sample checks when modeling (regression/classification)

> [!TIP]
> If you run experiments, keep a lightweight “analysis plan” alongside the change (what metric, why, stopping rule).

---

## 🧯 Troubleshooting

**No events in dev?**
- Telemetry may be disabled by default (Noop sink).
- Check feature flags / environment config.
- Ensure ad blockers aren’t blocking the ingestion endpoint.

**Events missing on navigation/unload?**
- Use `sendBeacon` or flush earlier (don’t wait until the tab closes).
- Reduce payload size.

**Sensitive data concerns?**
- Assume everything logged can eventually be reviewed.
- If you’re unsure: log a stable ID + classification, not the raw value.

---

## ✅ PR checklist (telemetry changes)

- [ ] Event name follows naming rules and is added to the taxonomy (if not already present)
- [ ] Payload uses stable identifiers; no raw sensitive values
- [ ] High-frequency events are sampled or aggregated
- [ ] Governance/redaction events are emitted when relevant
- [ ] Tests updated/added (adapter + sink)
- [ ] Documentation updated (this README if behavior changes)

---

## 📚 Design influences used in this adapter (project library)

<details>
<summary>Expand for the “why” behind these rules 🧠</summary>

- **KFM governance + Focus Mode** → audit trails, redaction signals, “who saw what and why”
- **Data Spaces / policy-aware logs** → access-controlled, context-aware logging, pseudonymization patterns
- **Digital Humanism / AI governance** → transparency, accountability, user autonomy, anti-surveillance posture
- **Statistics & experimental design** → resist multiple-testing pitfalls; define metrics before comparing
- **Scalable data & stream processing** → reduce at source, batch/summarize, avoid firehose defaults
- **Web performance + WebGL stability** → measure context loss, render regressions, device constraints
- **Cartography / public release practices** → remove or generalize sensitive map features to protect people

</details>

