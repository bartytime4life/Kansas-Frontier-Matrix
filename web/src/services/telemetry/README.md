# 🛰️ Telemetry Service (`web/src/services/telemetry`)

![Telemetry](https://img.shields.io/badge/telemetry-governed-blue)
![Contract-first](https://img.shields.io/badge/contract--first-schema%20driven-success)
![Governance](https://img.shields.io/badge/governance-audit%20ready-purple)
![Privacy](https://img.shields.io/badge/privacy-data%20minimized-critical)
![UI](https://img.shields.io/badge/ui-React%20%2B%20MapLibre-informational)

> 📍 **Path:** `web/src/services/telemetry/`  
> This module centralizes **client-side telemetry** for Kansas Frontier Matrix (KFM): usage analytics, performance signals, and governance-grade audit events.

---

## ✨ What “telemetry” means in KFM

Telemetry in KFM is designed to:
- provide **usage analytics hooks** while ensuring the UI causes **no data leakage** (e.g., it must respect redaction rules and maintain audit logs for interactions) [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- strengthen **telemetry-driven governance** by logging events when sensitive data is accessed, when redactions occur, or when publication is blocked by policy [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- support **audit trails** that let us answer “who saw what and why” — including Focus Mode events like `focus_mode_redaction_notice_shown` [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### ✅ Non-goals (hard “no” 🚫)
- ad-tech tracking, fingerprinting, cross-site identifiers
- logging raw dataset contents, protected coordinates, or sensitive user text
- bypassing the governed backend boundary (no direct-to-db / direct-to-graph shortcuts)

---

## 🗂️ Suggested module layout

> 🧠 This is a *recommended* structure for the telemetry service. Align file names to the actual implementation if they differ.

```text
📁 web/
  📁 src/
    📁 services/
      📁 telemetry/
        📄 README.md          👈 you are here
        📄 index.ts           # public API surface (track/audit/flush)
        📄 transport.ts       # batching + POST to governed API ingest
        📄 sanitize.ts        # remove PII / generalize sensitive fields
        📄 context.ts         # session/build/route context helpers
        📄 schemas.ts         # (optional) local schema mapping helpers
        📄 __tests__/         # schema + sanitization + batching tests
```

---

## 🧭 Where telemetry sits in the KFM pipeline

KFM has a non-negotiable pipeline ordering:  
**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode** [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

And an explicit **API boundary rule**:  
The frontend UI **must never query Neo4j directly**; all access goes through the governed API (`src/server/`). [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Telemetry follows the same intent:
- **UI emits events**
- **governed API ingests** (auth, validation, redaction, policy, retention)

```mermaid
flowchart LR
  subgraph Web["🌐 Web UI"]
    UI["React UI<br/>(Map • Story Nodes • Focus Mode)"]
    TS["🛰️ Telemetry Service<br/>(web/src/services/telemetry)"]
    UI -->|track(...) / audit(...) (non-blocking)| TS
  end

  subgraph API["🔐 Governed API (src/server)"]
    ING["Telemetry ingest<br/>(auth • validation • policy)"]
  end

  subgraph Store["🧾 Storage & Dashboards"]
    EVT["Event Store"]
    GOV["Governance Dashboards<br/>(FAIR/CARE signals)"]
  end

  TS -->|POST (batched)| ING --> EVT --> GOV
```

---

## 🧱 Contracts, schemas, and CI validation

### 📌 Repo-level contracts
Telemetry contracts are expected under:

- `schemas/telemetry/` — “Telemetry and event schemas” [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### ✅ CI enforcement (why schemas matter)
KFM CI validates structured outputs via JSON Schema; **telemetry JSON** (and UI config JSON) is validated **if schemas exist**. [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**Implication:** treat telemetry payloads as **contracted data**, not free-form console logs.

---

## 🧪 Event envelope (recommended)

> 🧩 Your actual event shape should be whatever `schemas/telemetry/` defines. This is a safe baseline that tends to work well.

```ts
export type TelemetryLevel = "usage" | "audit" | "perf" | "error";

export type TelemetryEnvelope<TPayload extends Record<string, unknown>> = {
  event: string;                 // snake_case preferred (see example below)
  ts: string;                    // ISO-8601 UTC timestamp
  level: TelemetryLevel;

  context: {
    session_id: string;          // random UUID (per tab or per session)
    route?: string;              // "/focus/..." etc
    build?: { version: string; commit?: string };

    // Avoid stable device IDs; prefer server-provided, pseudonymous actor IDs
    actor?: { id?: string; role?: string };
  };

  payload: TPayload;             // schema-controlled fields only
  classification?: string;       // "public" | "restricted" | ...
  sovereignty?: { tags?: string[] };
};
```

---

## 🛡️ Privacy, sovereignty, and “don’t leak” rules

### 🧷 Classification & sovereignty propagation
KFM enforces end-to-end governance: **no output artifact can be less restricted than its inputs**, and the UI must implement safeguards (e.g., blurring/generalizing sensitive map locations). [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**Telemetry is an output artifact.** Therefore:
- If an interaction involves sensitive/restricted content, telemetry must not “downgrade” it.
- Prefer **policy outcomes** (e.g., “redaction happened”) over raw details (e.g., exact coordinates).

### 🧠 “Metadata can be sensitive too”
Digital systems can infer private information by tracking individuals and analyzing metadata and behavior patterns. [oai_citation:8‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)

Practical rules:
- ❌ don’t store stable device identifiers (fingerprinting)
- ❌ don’t log raw lat/lon for protected contexts
- ❌ don’t capture free-text fields unless a governance review explicitly approves it
- ✅ default to **data minimization + pseudonymization** as privacy-by-design tactics [oai_citation:9‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)

### 🧯 Redaction must not be bypassable
Telemetry should help prove we didn’t leak data. The UI is expected to respect redaction rules (no map zoom bypass) and maintain audit logs for interactions. [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧾 Governance-grade audit events

KFM explicitly calls out strengthening telemetry signals as a governance mechanism:
- log when sensitive data is accessed
- log when redactions occur
- log when publication is blocked by policy [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### ⭐ Canonical example: Focus Mode redaction notice
KFM’s Master Guide gives a concrete audit-trail example event:

- `focus_mode_redaction_notice_shown` — emitted when Focus Mode withholds or generalizes data [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Recommended minimal payload (⚖️ “signal, not data”):

```json
{
  "event": "focus_mode_redaction_notice_shown",
  "level": "audit",
  "payload": {
    "story_node_id": "sn_0142",
    "redaction": "generalize_location",
    "reason": "sovereignty_policy",
    "layer_id": "layer_indigenous_heritage"
  }
}
```

---

## 🧩 How UI code should use this service

> ⚠️ Keep call sites **simple**. This service should handle queuing, sanitization, shaping, batching, and transport.

### Typical usage patterns

```ts
import { telemetry } from "@/services/telemetry";

// ✅ Usage event (non-sensitive)
telemetry.track("map_layer_toggled", {
  layer_id: "air_quality_pm25",
  enabled: true,
});

// ✅ Governance/audit event
telemetry.audit("focus_mode_redaction_notice_shown", {
  story_node_id: "sn_0142",
  redaction: "generalize_location",
  reason: "sovereignty_policy",
});
```

### Recommended integration points 🔌
- 🗺️ Map UI: layer toggles, basemap switches, “open legend”, “open filter”
- 📖 Story Nodes: open, cite-click, evidence panel open
- 🔍 Focus Mode: “attempted restricted access”, redaction notice shown
- ♿ Accessibility & reliability: a11y violations (counts only), error boundary, perf marks

---

## ➕ Adding a new telemetry event (checklist)

### 1) Decide the event level
- `usage`: UX/product signals (lowest sensitivity)
- `perf`: performance timings/marks (sanitized)
- `error`: client errors (sanitized)
- `audit`: governance / sensitive workflows

### 2) Write the schema first (contract-first 🧩)
Create/update JSON Schema under `schemas/telemetry/` [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> Expect CI gates when schemas exist: telemetry JSON can be validated in CI. [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 3) Add the emitter call
Prefer:
- ✅ stable IDs (`layer_id`, `story_node_id`)
- ✅ booleans, enums, coarse categories
- ❌ raw content, raw coordinates, raw queries

### 4) Add tests 🧪
- schema validation (golden event)
- sanitization tests (PII stripping / generalization)
- batching/flush tests (no UI blocking)

### 5) Update dashboards / governance mappings 📊
If it’s an audit signal, ensure it’s discoverable and actionable for governance monitoring. [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧰 Local dev tips

<details>
<summary><strong>🔎 Debugging outgoing events</strong></summary>

Common dev patterns:
- log emitted events to console in dev builds (avoid production noise)
- add a “telemetry debug panel” showing queue contents
- provide a `telemetry.flush()` action for smoke tests

</details>

<details>
<summary><strong>🧪 Smoke test flow</strong></summary>

1. Trigger a safe usage event (toggle a non-sensitive layer)
2. Trigger a Focus Mode redaction (if available)
3. Confirm:
   - events are emitted (and batched)
   - payload contains no secrets/PII
   - audit events are minimal and classification-aware

</details>

---

## 📚 Project references (why we’re strict)

- **Pipeline + API boundary:** UI must go through governed API; never direct Neo4j access. [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **UI must not leak data + must keep audit logs:** respect redaction rules and keep interaction logs. [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Telemetry-driven governance:** log sensitive access/redactions/policy blocks for FAIR/CARE monitoring. [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Audit trail example event:** `focus_mode_redaction_notice_shown` supports “who saw what and why”. [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Schema validation gates:** telemetry JSON can be CI-validated when schemas exist. [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Privacy principle:** metadata can enable tracking/inference; prefer data minimization + pseudonymization. [oai_citation:21‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ) [oai_citation:22‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)
