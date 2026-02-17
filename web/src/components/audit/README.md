# `web/src/components/audit/` — Audit UI (safe audit trail) 🧾🔍

![Governed](https://img.shields.io/badge/governed--artifact-critical)
![Audit](https://img.shields.io/badge/audit-audit__ref%20always-6a5acd)
![Safe Fields Only](https://img.shields.io/badge/safety-safe%20fields%20only-111827)
![Trust Membrane](https://img.shields.io/badge/trust%20membrane-enforced-16a34a)
![Fail-Closed](https://img.shields.io/badge/policy-default%20deny-111827)

KFM’s Web UI is a **product trust surface**, and audit is one of the core “show your work” affordances.
This folder defines the **Audit UI** that renders an `audit_ref` into an inspectable, policy-safe audit view.

> [!IMPORTANT]
> **Audit UI must never leak restricted data.**
> It must show *request context and policy outcomes* using **safe fields only**, and expose the `audit_ref` as a stable review hook.

---

## Governance header

| Field | Value |
|---|---|
| Document | `web/src/components/audit/README.md` |
| Status | **Governed** (UI trust surface contract) |
| Version | `v1.0.0` |
| Effective date | `2026-02-16` (America/Chicago) |
| Owners | `.github/CODEOWNERS` *(required; if missing, treat as governance gap)* |
| Applies to | audit UI components, safe-field rendering rules, UI error/deny/abstain behavior |
| Depends on | `web/README.md` (UI invariants + boundaries), governed API contract (`audit_ref` + safe audit view) |
| Default posture | **fail closed** (deny by default when policy/proofs are missing) |

---

## What this folder is responsible for

The Audit UI exists to answer (safely):

- **What happened?** (request type, time, status)
- **What did policy decide?** (allow/deny/abstain + safe explanation signals)
- **What was the user’s view context?** (bounded, public metadata only — e.g., `ViewState`)
- **What should a reviewer use to trace it?** (`audit_ref`, and any safe cross-links to evidence/provenance)

This aligns with KFM-Web’s core rule: **Focus Mode and other governed outputs must surface `audit_ref` prominently, and preserve the audit trail even when abstaining.**  [oai_citation:1‡GitHub](https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/main/web/README.md)

---

## Non-goals

- **Enforcing authorization** in the browser (that belongs to the governed API + policy boundary).
- Rendering any “raw” policy traces, DB queries, or internal identifiers that could leak implementation or sensitive data.
- Reconstructing denied info via alternate endpoints, cached payloads, or inference.
- Storing audit payloads in persistent client storage “just in case.”

> [!WARNING]
> The UI must not “work around” denials or missing proofs.
> If access is denied or evidence cannot be safely shown, **that is a correct outcome**.

---

## Trust membrane and audit data flow

KFM-Web is not allowed to access internal stores directly. Audit inspection is **always mediated** by the governed API, which returns a **sanitized** (policy-scoped) audit view.  [oai_citation:2‡GitHub](https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/main/web/README.md)

```mermaid
sequenceDiagram
  participant U as User
  participant UI as KFM-Web (React+TS)
  participant API as Governed API Gateway
  participant PDP as Policy (OPA/Rego)
  participant AUD as Audit Ledger (append-only)

  U->>UI: Action (Focus / Evidence click / Map inspect)
  UI->>API: Request (auth, view context)
  API->>PDP: Evaluate (allow/deny + obligations)
  API->>AUD: Append audit event (internal)
  API-->>UI: Response + audit_ref (always; or abstain/deny)
  UI->>API: Fetch safe audit view (audit_ref)
  API-->>UI: Safe audit view (redacted/scoped)
```

---

## UI contract

### 1) `audit_ref` must be visible and copyable

Every surface that returns an `audit_ref` must render it prominently:
- as text (not hidden behind an “advanced” menu),
- with a one-click copy control,
- and a one-click “Open Audit” affordance.

### 2) Safe fields only (hard rule)

Audit UX must show:
- request context (**safe fields only**),
- policy outcomes (**safe fields only**),
- and `audit_ref` as a stable review hook.  [oai_citation:3‡GitHub](https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/main/web/README.md)

#### Safe vs unsafe examples

| Category | Safe to display | Never display |
|---|---|---|
| Identity | `audit_ref`, timestamps, request kind, UI version | tokens, cookies, auth headers, API keys |
| View context | `ViewState` snapshot (bbox/time/layers as *public metadata*) | precise sensitive locations *(unless policy explicitly permits)*, raw feature payloads |
| Policy | allow/deny/abstain, safe reason codes, obligations (public) | full rule traces, internal store names/paths, debugging dumps |
| Evidence linkage | citation refs, evidence bundle digests (if policy-safe) | raw evidence bodies for restricted documents/assets |
| Actors | role labels if policy-safe (“researcher”, “public”), system agent IDs | PII (emails, IPs), internal user identifiers |

> [!IMPORTANT]
> **Defense in depth:** the server should sanitize the audit view, but the UI must still defensively render
> (e.g., never “pretty print the entire JSON blob” unless it is explicitly designated sanitized).

### 3) Fail-closed UI behavior

Audit UI must treat “no data” as a governance outcome, not as something to “fix” client-side:

- If the audit endpoint returns **deny** → show a deny state (no fallback).
- If the audit record is **missing** → show “not found” and preserve the `audit_ref` for review.
- If the audit view is **redacted** → show clear “redacted/generalized” badges.

---

## Recommended UI shape

> [!NOTE]
> Component names below are recommendations for organization. If your repo uses different names,
> keep the boundaries and the safe-field rules intact.

### Folder layout (recommended)

```text
web/src/components/audit/
├─ README.md                  # this file (governed)
├─ AuditDrawer.tsx            # main audit surface (safe fields only)
├─ AuditRefPill.tsx           # compact audit_ref display + copy/open
├─ AuditSummaryCard.tsx       # high-level status + timestamps
├─ PolicyDecisionPanel.tsx    # safe policy outcomes + obligations
├─ RequestContextPanel.tsx    # safe request + ViewState context
├─ IntegrityPanel.tsx         # digests/verification badges (when present)
├─ RedactionBanner.tsx        # “redacted/generalized” indicators
├─ types.ts                   # UI-local types (prefer importing governed contracts)
└─ __tests__/
   ├─ safeFieldRendering.test.tsx
   └─ auditStates.test.tsx
```

---

## Contracts

### ViewState (dependency)

Audit replay and context rendering should reuse the governed `ViewState` contract defined for KFM-Web.  [oai_citation:4‡GitHub](https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/main/web/README.md)

### Audit view DTO (proposed UI-facing contract)

> [!IMPORTANT]
> **Verify the actual shape in the governed API contract.**
> This section defines the *minimum UI needs* and how to version it.

```ts
// Proposed: AuditViewV1 (UI-facing, sanitized)
// Source of truth should live under: web/src/contracts/audit.ts (recommended).
export type AuditViewV1 = {
  v: 1;

  // Stable reference returned by governed responses:
  audit_ref: string;

  // When the audit event was recorded (policy-safe):
  created_at: string; // ISO 8601

  // High-level classification:
  kind: "focus" | "evidence_resolve" | "story" | "map" | "api" | "other";

  // Outcome summary (UI-safe):
  status: "ok" | "abstain" | "deny" | "error";

  // Safe request context (public metadata only):
  view?: {
    v: 1;
    timeRange: [string, string];
    bbox: [number, number, number, number];
    activeLayers: string[];
    story?: { nodeId: string; stepId?: string };
    viewId?: string;
  };

  // Policy-safe decision signals:
  policy?: {
    decision: "allow" | "deny";
    // Use stable reason codes or short, policy-approved messages:
    reason_codes?: string[];
    // Non-sensitive obligations (e.g., "show_redaction_banner"):
    obligations?: string[];
    // Optional: policy bundle/version identifiers, if policy allows:
    policy_version?: string;
  };

  // Optional safe linkage (only if policy permits):
  links?: {
    citations?: string[]; // citation refs (scheme://…)
    prov_refs?: string[]; // prov://…
    evidence_digests?: string[]; // sha256:…
  };

  // Optional server metadata (safe fields only):
  server?: {
    api_version?: string;
  };

  // Optional redaction indicator:
  redaction?: {
    present: boolean;
    // Stable, non-leaky summary labels:
    classes?: Array<"location_generalized" | "field_removed" | "license_withheld" | "other">;
  };
};
```

---

## UX states (must exist)

### Loading
- Show skeleton UI (do not flash raw values).
- Keep `audit_ref` visible even while loading details.

### OK
- Show summary → context → policy → integrity.

### Abstain
- Show abstain badge + safe reason codes (if present).
- Provide links back to “narrow your view” (time/layers) where appropriate (no guessing).

### Deny
- Show deny status plainly.
- Do not attempt alternate endpoints or “try harder” logic.
- Keep `audit_ref` visible.

### Error / Not found
- Preserve `audit_ref`.
- Offer a “Copy audit_ref” button and a safe retry.

---

## Integration points

Audit UI is typically opened from:

- **Focus Mode** (answer includes `audit_ref`)
- **Evidence drawer** (especially on denial/redaction)
- **Story playback** (step execution audit)
- **Map inspection / layer actions** (when governed calls are made)

> [!IMPORTANT]
> **No network IO inside components.**
> Fetching audit views belongs in `web/src/services/**` (e.g., `auditClient.ts`) and is then passed in
> via hooks/props.  [oai_citation:5‡GitHub](https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/main/web/README.md)

---

## Testing and Definition of Done

### Required tests

- **Safe field rendering**
  - [ ] UI never renders forbidden keys (token-like, PII-like, raw evidence bodies)
  - [ ] Redaction banner shows when `redaction.present = true`

- **State handling**
  - [ ] loading → ok
  - [ ] loading → deny
  - [ ] loading → abstain
  - [ ] loading → not found / error (and `audit_ref` remains visible)

- **Trust membrane lint (recommended)**
  - [ ] no `fetch(` / `axios` / XHR usage in `web/src/components/**`
  - [ ] network calls exist only in `web/src/services/**`  [oai_citation:6‡GitHub](https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/main/web/README.md)

### Accessibility

- [ ] keyboard reachable copy button and “Open audit” affordance
- [ ] status badges have text equivalents (not color-only)
- [ ] screen-reader-friendly headings and landmarks

---

## Security notes

> [!WARNING]
> UI code runs in an adversarial environment.
> Assume anything shipped to the client can be inspected and modified.  [oai_citation:7‡GitHub](https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/main/web/README.md)

- Do not log audit payloads verbatim.
- Do not persist audit payloads in browser storage.
- Prefer short-lived, gateway-managed auth; treat tokens as opaque.
- If the audit view includes links, only route through the governed API (no direct object store links).

---

## References

- KFM root invariants: `../../../../README.md`
- KFM-Web invariants and contracts: `../../../README.md`
- Repo governance and enforced gates: `../../../../.github/README.md`
- Docs governance rules: `../../../../docs/README.md`
