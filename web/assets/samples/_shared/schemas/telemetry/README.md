<div align="center">

# 📡 Telemetry Schemas (Web Samples)

**Contract-first event envelopes + governance signals for Kansas Frontier Matrix (KFM)** 🧭⚖️

![Contract-first](https://img.shields.io/badge/contract--first-JSON%20Schema-0b7285?style=flat&logo=json)
![Governance](https://img.shields.io/badge/governance-audit%20%2B%20signals-5c7cfa?style=flat)
![Privacy](https://img.shields.io/badge/privacy-data%20minimization-2f9e44?style=flat)
![Traceability](https://img.shields.io/badge/traceability-provenance--linked-7950f2?style=flat)

</div>

> [!IMPORTANT]
> KFM telemetry is **governance-grade instrumentation** (auditability + safety + compliance), not “track everything” analytics. 📎✅  
> Emit **only what we can defend** (minimal, explainable, policy-aware, and schema-validated).

---

## 🧭 What this folder is

This directory contains **shared telemetry JSON Schemas and examples** used by the KFM web samples to:
- ✅ Validate telemetry event payloads in a **contract-first** way
- ✅ Provide **sample event fixtures** for UI demos/tests
- ✅ Keep client-side telemetry aligned with governed system rules (Focus Mode, redactions, publication gates) 🔒

> [!NOTE]
> The **canonical** telemetry contracts live under `schemas/telemetry/` at the repo root.  
> This folder is a **web-facing mirror / sample bundle** to keep the UI honest and testable.

---

## 🗺️ Where telemetry fits (big picture)

```mermaid
flowchart LR
  PIPE[🧪 Pipelines] -->|emit events| EVT[📡 Telemetry Event]
  API[🧩 API Layer] -->|emit events| EVT
  UI[🌐 Web UI] -->|emit events| EVT

  EVT --> STORE[(🗄️ Event Store / Logs)]
  STORE --> SIG[📈 Signals (derived)]
  SIG --> DASH[📊 Governance Dashboards]
  SIG --> ALERT[🚨 Alerts / Review Gates]
```

Telemetry events become **signals** (dashboards/alerts) that help answer governance questions like:
- “Who saw what and why?” 🕵️‍♀️
- “When did redactions occur (and which policy drove them)?” 🧾
- “Was publication blocked (and by what rule)?” 🚫📣

---

## 📦 Typical contents

> This folder may include some or all of the following patterns (depending on the sample pack):

```text
📁 web/assets/samples/_shared/schemas/telemetry/
├── 📄 README.md
├── 📄 *.schema.json                 # JSON Schema contracts
├── 📁 events/                       # Event-specific schemas (payload contracts)
│   └── 📄 <event_name>.schema.json
└── 📁 examples/                     # Example events validated by schema
    └── 📄 <event_name>.example.json
```

---

## 🧱 Event contract model

KFM telemetry is built around a **stable envelope** + **event-specific payload**:

- **Envelope** = common metadata for correlation, governance, and validation
- **Payload** = event-specific fields, validated by an event schema

### ✅ Required envelope fields (recommended baseline)

| Field | Type | Required | Why it exists 🧠 |
|---|---|---:|---|
| `schema_version` | `string` | ✅ | Contract-first: explicit schema version (SemVer recommended) |
| `event_id` | `string` | ✅ | Idempotency + audit trace (UUID/ULID) |
| `event_name` | `string` | ✅ | Stable identifier (see naming rules) |
| `occurred_at` | `string` | ✅ | Ordering + governance timelines (RFC3339) |
| `source` | `object` | ✅ | Component attribution (`web`, `api`, `pipeline`, etc.) |
| `classification` | `object` | ✅ | Sovereignty + sensitivity propagation guardrail 🔒 |
| `payload` | `object` | ✅ | Event-specific data (validated) |
| `context` | `object` | ➖ | Correlation: dataset/story/prov references |
| `actor` | `object` | ➖ | Accountability without PII (pseudonymous) |
| `trace` | `object` | ➖ | Trace correlation (`trace_id`, `span_id`, request ids) |

> [!TIP]
> If you’re unsure whether something belongs in telemetry, start by asking:
> **“Can we explain why we collected this field?”**  
> If not, don’t emit it. 🙅

---

## 🏷️ Event naming conventions

Keep event names:
- ✅ **snake_case**
- ✅ **stable and descriptive**
- ✅ aligned with user-visible governance moments (especially Focus Mode)

Suggested pattern:
- `domain_action_subject` (e.g., `focus_mode_redaction_notice_shown`)
- `policy_action` (e.g., `publication_blocked_by_policy`)
- `access_action_subject` (e.g., `sensitive_layer_access_attempted`)

### 🚫 Avoid
- Names tied to implementation details (`button_clicked_v2`)
- Overly generic names (`event_happened`)
- Anything that implies raw sensitive content is logged (`secret_location_viewed`)  

---

## ⚖️ Governance + sovereignty rules (non-negotiable)

### 1) 🧼 Data minimization (privacy-by-design)
- Do **not** emit PII (names, emails, freeform text, raw queries, exact coordinates tied to protected locations, etc.)
- Prefer **categorical flags** and **policy references** over raw values

### 2) 🧯 Classification consistency
Every event must declare a **classification level** and must never “downgrade” sensitivity.

Example levels (adjust to project policy):
- `public`
- `internal`
- `restricted`

Recommended structure:

```json
{
  "classification": {
    "level": "public",
    "reason": "UI notice only; contains no sensitive coordinates or identifiers"
  }
}
```

### 3) 🧾 Policy-aware payloads for governance events
If an event is about redaction, access control, or publication gating, include:
- `policy_id`
- `decision` (e.g., `allow | deny | redact | block`)
- `reason_code` (short, enumerated)
- `redaction_type` (if applicable)

---

## 🧪 Example event

### `focus_mode_redaction_notice_shown` (audit trail)

```json
{
  "schema_version": "kfm.telemetry.event@1.0.0",
  "event_id": "01J0Z2E2N6R8W4QWZQ7D6Y8K9M",
  "event_name": "focus_mode_redaction_notice_shown",
  "occurred_at": "2026-01-18T00:00:00.000Z",
  "source": {
    "component": "web",
    "module": "focus_mode",
    "build": "dev"
  },
  "classification": {
    "level": "public",
    "reason": "Notice-only event; no sensitive payload values."
  },
  "context": {
    "story_node_id": "example_story_slug",
    "dataset_id": "kfm.ks.example.dataset.v1"
  },
  "payload": {
    "policy_id": "sovereignty.sensitive_locations",
    "decision": "redact",
    "redaction_type": "generalize",
    "withheld_fields": ["geometry.coordinates"]
  }
}
```

---

## ✅ Validation expectations

Telemetry is “real” only if it’s validated.

### What “good” looks like
- ✅ Events validate against JSON Schema
- ✅ Breaking changes trigger version bumps
- ✅ Examples in `examples/` validate in CI
- ✅ Governance-related events include `policy_id` + decision metadata

### Suggested local validation (choose your validator)
- **Node:** Ajv (common for JSON Schema)
- **Python:** `jsonschema`
- **Any:** JSON Schema draft-compatible validator used elsewhere in KFM

> [!NOTE]
> If schemas exist for telemetry/UI config, they should be validated alongside STAC/DCAT/PROV and Story Node schemas in CI.

---

## 🧩 Adding a new telemetry event (checklist)

1) 🧾 **Define** the event name + intent (what question does it answer?)
2) 🧱 **Create** the event payload schema: `events/<event_name>.schema.json`
3) 🧪 **Add** a validated example: `examples/<event_name>.example.json`
4) 🔒 **Classify** the data (what level, why, and how do we avoid sensitive leakage?)
5) 🧰 **Wire** emission through approved boundaries (UI → API, not UI → graph directly)
6) ✅ **Add tests** so schema validation runs in CI

---

## 🧠 FAQ

### “Should we include user identifiers?”
Only if:
- It’s strictly necessary for governance/audit
- It’s pseudonymous (hashed/opaque) and policy-approved
- It does not introduce PII or re-identification risk

### “Where do we put dataset/story/provenance references?”
Use `context`:
- `dataset_id` (stable KFM dataset identifier)
- `story_node_id` (slug/ID)
- `prov_activity_id` (if available)

---

## 🔗 Related docs (repo-relative)

- 📘 Master Guide (v13): `../../../../../../docs/MASTER_GUIDE_v13.md`
- ⚖️ Governance: `../../../../../../docs/governance/ROOT_GOVERNANCE.md`
- 🧭 Sovereignty: `../../../../../../docs/governance/SOVEREIGNTY.md`
- 🧾 Telemetry canonical schemas: `../../../../../../schemas/telemetry/`

---

## 🛠️ TODOs (nice-to-have)

- [ ] Add a “signal catalog” (mapping events → dashboards/alerts) 📈
- [ ] Add schema generation for typed clients (TS types, Python models) 🧬
- [ ] Add retention guidance per event class (security vs ops vs product) 🗄️
