# Policy Adapter 🛡️ (`src/adapters/policy`)

![Layer](https://img.shields.io/badge/layer-adapter-blue)
![Trust Membrane](https://img.shields.io/badge/governance-trust%20membrane-critical)
![PDP](https://img.shields.io/badge/policy%20engine-OPA-informational)

This directory contains the **policy adapter(s)** that implement KFM’s **Policy Port** (aka “Policy Decision Port”) by calling a **Policy Decision Point (PDP)** such as **OPA** (Open Policy Agent). The adapter is part of the system’s **trust membrane**: all sensitive access and AI output must pass through governed policy evaluation before it can be returned to clients.

> [!IMPORTANT]
> **Fail closed. Default deny.** If the policy engine cannot be reached or returns an invalid decision, this adapter must treat the decision as **DENY** (unless an explicitly reviewed exception exists).

> [!NOTE]
> Method names / port names / env var names are **conventions** in this README. If the repo already defines interfaces, treat this file as documentation of *intent* and align names to the existing contracts.

---

## Why this exists

KFM’s architecture describes policy checks at multiple gates:
- **Data access** (datasets / layers / graph entities)
- **Story Node exposure** (narratives may be restricted)
- **Focus Mode AI output validation** (e.g., “cite or abstain”, sensitive content rules)

This adapter is how those checks are performed at runtime — without leaking policy concerns into the Domain layer.

---

## Architecture placement

```mermaid
flowchart LR
  UI[Web UI (React/TS)] --> API[API Gateway (FastAPI)]
  API -->|PolicyPort calls| PAD[Policy Adapter<br/>(this directory)]
  PAD -->|structured input| PDP[OPA / PDP]
  API --> DATA[(PostGIS / Neo4j / Search)]
  API --> AUDIT[(Audit Ledger / Provenance Logs)]
  PDP -->|decision + obligations| PAD
  PAD -->|allow/deny + redactions + reason codes| API
```

**Boundary rules (non-negotiable):**
- The **UI never talks to databases directly** — only the governed API.
- The **API routes / use-cases call the Policy Port**; this adapter implements it.
- Core logic must never “skip” policy checks for convenience.

---

## Repository layout context

| Path | What it is | Owned by |
|---|---|---|
| `policy/` | Policy-as-code packages (OPA/Rego). Example: `data_access.rego`, `ai_output.rego`, `story_node.rego` | Governance + Engineering |
| `src/adapters/policy/` | Runtime adapter(s) that evaluate policy decisions | Engineering |
| `src/domain/` | Pure domain models/entities (no HTTP/DB/OPA deps) | Engineering |
| `src/usecases/` | Workflows that call ports (including Policy Port) | Engineering |

---

## Responsibilities

### 1) Evaluate authorization decisions
Typical checks:
- Can `principal` perform `action` on `resource`?
- Can a user access a dataset/layer tagged with sensitivity constraints?

### 2) Return *obligations*, not just allow/deny
A decision may include:
- **Redactions** (remove/blur sensitive fields)
- **Precision downgrades** (e.g., reduce coordinate precision)
- **Watermarking or labeling requirements**
- **Audit requirements** (must log provenance entry)

### 3) Support Focus Mode output gating
Focus Mode pipeline includes a post-generation policy check that can **block** or **sanitize** AI output before it is returned to the UI.

---

## Policy decision types

| Decision | Typical Query | Primary Inputs | Typical Outputs |
|---|---|---|---|
| Data access | “May user read dataset X?” | principal claims, dataset id/tags, action | allow/deny, reason, obligations |
| Story Node exposure | “May user view story node Y?” | principal claims, story node id/tags | allow/deny, redactions |
| AI output validation | “Is this answer allowed to ship?” | principal claims, draft answer, citations list, sensitivity context | allow/deny, required edits, blocked spans |

---

## Adapter contract (recommended)

### PolicyInput (suggested shape)

```json
{
  "request_id": "uuid-or-trace-id",
  "principal": {
    "subject": "user-id-or-service-id",
    "roles": ["reader"],
    "org": "optional-org",
    "claims": {
      "scopes": ["catalog:read"]
    }
  },
  "action": "read",
  "resource": {
    "type": "dataset",
    "id": "dcat:dataset:xyz",
    "tags": ["public", "historical"]
  },
  "context": {
    "ip": "optional",
    "ui_surface": "focus_mode",
    "time_utc": "2026-02-12T12:00:00Z"
  }
}
```

### PolicyDecision (suggested shape)

```json
{
  "allow": false,
  "reason_code": "SENSITIVE_LOCATION",
  "message": "Access denied by policy.",
  "obligations": [
    {
      "type": "redact",
      "path": "$.geometry.coordinates",
      "mode": "downgrade_precision",
      "precision": 2
    }
  ],
  "policy": {
    "package": "policy/data_access.rego",
    "revision": "git:abcdef123",
    "engine": "opa"
  }
}
```

> [!TIP]
> Keep `reason_code` stable and machine-readable; treat `message` as user-facing and localizable.

---

## OPA integration patterns

This adapter should support at least one of these execution modes:

1) **Sidecar PDP** (HTTP call to OPA Data API)  
2) **In-process** (embedded OPA/WASM) *(optional)*

> [!WARNING]
> If you add an “in-process” mode, ensure policy bundles are still **versioned** and the running policy revision is auditable.

---

## Configuration (recommended)

| Setting | Example | Meaning |
|---|---|---|
| `KFM_POLICY_MODE` | `opa` / `noop` | `opa` enforces; `noop` is for local/dev only (must not be enabled in production) |
| `OPA_URL` | `http://opa:8181` | Base URL for PDP when running sidecar |
| `OPA_QUERY_DATA_ACCESS` | `/v1/data/kfm/data_access/allow` | Data access query path |
| `OPA_QUERY_AI_OUTPUT` | `/v1/data/kfm/ai_output/validate` | AI output gating query path |
| `POLICY_FAIL_MODE` | `closed` | `closed` = deny on errors/timeouts |

---

## Auditing requirements

Every policy evaluation that gates user-visible output should emit an audit/provenance event that includes:
- `request_id` / correlation id
- decision (allow/deny)
- `reason_code`
- obligations applied (if any)
- **policy revision** (bundle hash or git commit)
- minimal principal info (avoid storing PII unless governed)

---

## How to change policy safely

1) Update the relevant Rego in `policy/`.
2) Add/update OPA unit tests (allow/deny fixtures).
3) If the decision schema changes, update adapter mapping + contract tests.
4) Run the full policy test suite + API integration tests.
5) Ensure audit fields still include policy revision.
6) If policy affects sensitive/Indigenous-related data, trigger governance review.

---

## Testing matrix

| Test Type | What it protects | Where |
|---|---|---|
| Unit tests | Adapter maps input → PDP request → decision correctly | `src/adapters/policy/**/test_*` |
| Contract tests | Decision schema stability for API consumers | `src/**/contract_tests` |
| Integration tests | Real OPA container returns expected decisions | `tests/integration/policy_*` |
| Policy unit tests | Rego rules behave (deny by default, explicit allow) | `policy/**` |

> [!IMPORTANT]
> “Policy regressions” are expected risk. Treat policy tests as mandatory CI gates.

---

## Common pitfalls

- **Fail-open on timeout** (do not do this).
- Logging raw AI outputs or sensitive resource attributes without governance approval.
- Letting UI or service code “work around” policy checks.
- Returning only “403 Forbidden” without a stable `reason_code` for debugging/audit.

---

## See also

- `policy/README.md` (policy-as-code overview)
- `docs/architecture/` (trust membrane + clean architecture)
- `docs/ci/` (policy test gates, PR checklist)
