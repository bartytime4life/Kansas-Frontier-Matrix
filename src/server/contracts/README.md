# Server Contracts (Trust Membrane)

![governed](https://img.shields.io/badge/status-governed%20artifact-2b6cb0)
![contract-first](https://img.shields.io/badge/discipline-contract--first-2f855a)
![fail-closed](https://img.shields.io/badge/policy-fail--closed-c53030)

> [!IMPORTANT]
> This directory defines **KFM’s server boundary**: the machine-readable contracts that every client (UI, tools, pipelines, and external consumers) must use.
> A change here is a **governed change**. Treat it like a production change.

---

## Why this folder exists

KFM’s credibility depends on enforcing a policy-governed API boundary (the **trust membrane**):

- **No UI direct database access** (all reads/writes flow through the governed API boundary).
- **Fail-closed policy enforcement** (if policy evaluation, validation, or evidence resolution fails, the request must not “partially succeed”).
- **Evidence-first answers**: Focus Mode must **cite or abstain**, and responses must be auditable.
- **Catalog/provenance-gated publishing**: datasets and layers are not “publicly real” unless they have validated STAC/DCAT/PROV + checksums.

This folder is the canonical home for server-facing contracts (OpenAPI, GraphQL SDL, JSON Schemas, policy input schemas, event envelopes, and examples).

> [!NOTE]
> Repo structure guidance explicitly calls out `src/server/` as the sole home for API code, with API contracts living under `src/server/contracts/` (or an equivalent subfolder).

---

## Scope

This directory is **contracts only**:

- ✅ **Allowed**: OpenAPI, GraphQL SDL, JSON Schema, Rego policy bundles (or references), contract fixtures, compatibility notes, and generated type artifacts.
- ❌ **Not allowed**: business logic, database queries, service implementations, and UI code.

If you need to change server behavior, do it in code **and** update the contract artifacts here (plus tests) in the same PR.

---

## Contract taxonomy

| Contract type | What it governs | Typical artifacts | Primary consumers |
|---|---|---|---|
| **HTTP API** | External REST endpoints, request/response bodies, errors, auth, pagination | `openapi/*.yaml` (OpenAPI 3.1) | Web UI, SDKs, integrations |
| **GraphQL** | Schema evolution, types, queries/mutations, deprecations | `graphql/schema.graphql` (SDL) | Web UI, power users, tooling |
| **Domain payload schemas** | Reusable shapes shared across endpoints (e.g., citations, evidence, audit) | `schemas/*.schema.json` | API implementation + tests |
| **Governance & policy inputs** | What the policy engine evaluates (roles, request context, sensitivity) | `policy/input.schema.json`, `policy/*.rego` | API gateway/middleware, CI |
| **Event envelopes** | Audit events, telemetry events, internal bus messages | `events/*.schema.json` | Observability pipeline, audit ledger |
| **Examples/fixtures** | Golden request/response examples used in contract tests | `examples/*` | CI, local dev |

---

## Expected directory layout

This layout is intentionally explicit so humans and CI can find the authoritative spec quickly.

```text
src/server/contracts/                               # Public contracts: API boundaries, schemas, policy I/O, and examples
├─ README.md                                        # How contracts are versioned, validated, and enforced (CI gates)
│
├─ openapi/                                         # REST boundary (OpenAPI 3.1)
│  ├─ kfm.openapi.yaml                               # Canonical REST contract (paths, components, auth, errors)
│  └─ overlays/                                     # Optional: per-env overlays (servers/auth tweaks; must not break contract)
│
├─ graphql/                                         # Optional GraphQL boundary (if enabled)
│  └─ schema.graphql                                # GraphQL SDL (types/queries/mutations; contract snapshot)
│
├─ schemas/                                         # JSON Schemas for governed payloads (request/response/event contracts)
│  ├─ common/                                       # Shared envelopes + primitives used across the API
│  │  ├─ error.schema.json                          # Standard error envelope (code/message/details/trace_id)
│  │  ├─ pagination.schema.json                     # Pagination contract (cursor/limit/next, totals if allowed)
│  │  ├─ citation.schema.json                       # CitationRef/EvidenceRef (stable IDs + resolver hints)
│  │  ├─ evidence.schema.json                       # EvidenceRecord/EvidenceBundle (what citations resolve to)
│  │  ├─ audit.schema.json                          # AuditRecord (who/what/when/decision + refs)
│  │  └─ sensitivity.schema.json                    # Sensitivity labels + handling rules (classification + redaction hints)
│  │
│  ├─ focus/                                        # Focus Mode contracts (governed AI boundary)
│  │  ├─ focusQuery.schema.json                     # Focus request envelope (query, scope, policy context)
│  │  └─ focusAnswer.schema.json                    # Focus answer envelope (cite-or-abstain + audit_ref required)
│  │
│  ├─ catalog/                                      # Catalog-serving contracts (datasets/layers exposed to UI/clients)
│  │  ├─ dataset.schema.json                        # DatasetSummary/DatasetDetail (metadata + links + sensitivity)
│  │  └─ layer.schema.json                          # LayerSummary/LayerDetail (map-ready layer descriptors)
│  │
│  └─ pipeline/                                     # Pipeline output contracts (traceability + validation)
│     ├─ run_record.schema.json                     # (Recommended) pipeline run record (inputs/outputs/digests/provenance)
│     └─ validation_report.schema.json              # Validator output (errors/warnings + machine-readable details)
│
├─ policy/                                          # Policy contract: what the service sends to OPA + bundled examples
│  ├─ input.schema.json                              # OPA input shape (actor/request/resource/answer/context)
│  ├─ bundles/                                      # Example policy bundles for contract testing / reference implementations
│  │  ├─ kfm_ai.rego                                 # Example: cite-or-abstain + default deny for Focus
│  │  └─ kfm_catalog.rego                             # Example: sensitivity gating + redaction behavior
│  └─ tests/                                        # OPA unit tests for bundled examples (if shipped here)
│     └─ *.rego                                      # Rego tests (opa test …)
│
├─ events/                                          # Event envelopes (append-only, schema-validated)
│  ├─ audit_event.schema.json                       # Audit append-only event (decision log event contract)
│  └─ telemetry_event.schema.json                   # Minimal telemetry envelope (low-sensitivity, bounded fields)
│
└─ examples/                                        # Canonical example payloads (used by docs + tests)
   ├─ focus/
   │  ├─ query.json                                 # Example Focus request
   │  ├─ answer_with_citations.json                 # Example allowed answer (citations + evidence refs present)
   │  └─ answer_abstain.json                        # Example abstain response (reason + audit_ref; no unsupported claims)
   └─ errors/
      ├─ forbidden.json                             # Example 403 error envelope (policy denied)
      └─ validation_failed.json                     # Example 422 error envelope (schema/contract violations)
```

> [!TIP]
> If your current repo doesn’t have some of these folders yet, **add them as you introduce the corresponding contract type** (don’t scatter contracts across unrelated directories).

---

## Non-negotiables (system-level contract invariants)

These invariants are enforced **through contracts + CI gates**:

1. **Trust membrane**: clients cannot bypass policy by talking directly to databases or internal stores.
2. **Fail closed**: policy/validation failures must deny the request, not degrade into best-effort behavior.
3. **Cite-or-abstain** (Focus Mode): responses must include citations **or** explicitly abstain, and must include an audit reference.
4. **Catalog/provenance required to publish**: no dataset/layer promotion without validated STAC/DCAT/PROV and checksums.

---

## Promotion Contract (publish gate)

KFM treats “promotion to processed/public” as a **fail‑closed contract**, not a best-effort convenience.

At minimum, promotion should be blocked unless all of the following are true:

1. **License present**
2. **Sensitivity classification present**
3. **Schema + geospatial checks pass**
4. **Checksums computed**
5. **STAC/DCAT/PROV exist and validate**
6. **Audit event recorded**
7. **Human approval** when sensitive triggers fire

This folder may include the schemas and/or API payload contracts that make those checks machine‑enforceable.

---

## API contract rules

### REST: OpenAPI is the source of truth

- **OpenAPI is a governed artifact**.
- For `/api/v1`, changes are **no-breaking-change by default**.
- Breaking changes require an explicit version bump (e.g., `/api/v2`) and a migration plan.

> [!IMPORTANT]
> Do not “silently break” clients by changing response shapes, meaning, or required fields in-place.

### GraphQL: evolve by deprecation

If GraphQL is enabled:

- Prefer **additive changes**.
- Use `@deprecated` to schedule removals.
- Use schema diff tooling in CI to detect breaking changes.

---

## Evidence & audit contracts

### Evidence references must be resolvable

Contracts must ensure **every provenance/citation reference is resolvable via an API endpoint**, not just a string pasted into markdown.

Common resolver schemes include:

- `prov://…`
- `stac://…`
- `dcat://…`
- `doc://…`
- `graph://…`

A common pattern is a single resolver endpoint that accepts a small allow-list of evidence kinds (e.g., `dcat | stac | prov | doc | graph`).

### Citations must be resolvable (UI acceptance criterion)

The server must return citations as structured references that the UI can resolve to a human-readable evidence view.

**Acceptance criterion (contract-level):**

- Given any `citation.ref` in a Focus Mode answer, the UI can resolve it to an evidence view in **≤ 2 API calls**.

### Required response fields (Focus Mode)

A Focus Mode answer is governed output. At minimum, the response schema must support:

- `answer_markdown` (renderable)
- `citations[]` (may be empty only for abstentions)
- `audit_ref` (always present)

**Recommended abstain response (shape):**

```json
{
  "answer_markdown": "I can't answer that from the verified KFM sources available for this view. Try narrowing the time range or selecting relevant layers.",
  "citations": [],
  "audit_ref": "audit_..."
}
```

---

## Error contract (standard envelope)

All endpoints must use a consistent error envelope so:

- clients can reliably display errors,
- policy denials are distinguishable from validation failures,
- audit logs can classify failures.

**Minimal recommended shape:**

```json
{
  "error": {
    "code": "POLICY_DENY|VALIDATION_FAILED|NOT_FOUND|CONFLICT|INTERNAL",
    "message": "Human-readable summary",
    "details": { "field": "optional machine details" },
    "request_id": "req_...",
    "audit_ref": "audit_..." 
  }
}
```

> [!NOTE]
> If an error is part of an audited workflow (e.g., AI query denied), include `audit_ref` so reviewers can trace it.

---

## Schema governance

Schemas are treated as **governed artifacts**:

- Changes should be reviewed and versioned.
- Breaking schema changes should come with a migration strategy (and scripts where applicable).

---

## Deterministic identity (spec_hash) and versioning

KFM’s governance model relies on deterministic identities for artifacts and their governing specs.

**Recommended rule:**

- `spec_hash = sha256(canonical_json(spec))`

Where **canonical_json** uses a deterministic canonicalization scheme (e.g., RFC 8785 / JCS for JSON).

### Versioning policy

| What changes | Allowed in-place? | Required action |
|---|---:|---|
| Add optional fields | ✅ | Add tests + examples |
| Add new endpoint | ✅ | Add contract + fixtures |
| Change meaning of an existing field | ❌ | New version (`/api/v2`) or new field |
| Remove a field | ❌ | Deprecate first; remove in major version |
| Tighten validation (more rejects) | ⚠️ | Treat as breaking unless proven safe |

---

## Security & sensitivity contracts

KFM serves data with varying sensitivity (PII risk, culturally sensitive locations, restricted layers).

**Contracts must make sensitivity explicit**:

- Use a **sensitivity label** on datasets/layers/records where applicable.
- Ensure policy can enforce redaction/generalization at query time.
- Never include secrets in this folder (or anywhere in git).

### Common sensitivity labels

You may see (or adopt) labels such as:

- `public`
- `restricted`
- `sensitive-location`
- `culturally_sensitive`
- `pii_risk`

> [!CAUTION]
> If a contract change could increase location precision or expose restricted attributes, route the PR through governance review.

---

## Change workflow (PR checklist)

When you change anything under `src/server/contracts/`, your PR must include:

- [ ] **Updated contract artifact(s)** (OpenAPI/SDL/Schema/Policy)
- [ ] **Updated examples/fixtures** showing the new behavior
- [ ] **Contract tests** proving backward compatibility (or explicit `/api/v2` bump)
- [ ] **OPA/Rego tests** for policy changes (default deny remains intact)
- [ ] **Evidence resolution tests** (citations resolve; abstentions behave correctly)
- [ ] **Changelog entry** (if your repo tracks contract changes)

<details>
<summary><strong>Definition of Done (contracts)</strong></summary>

- [ ] OpenAPI validates and is lint-clean.
- [ ] JSON Schemas validate and are referenced from OpenAPI/GraphQL (no orphan schemas).
- [ ] Policy input schema matches the middleware integration.
- [ ] Policy bundle passes unit tests.
- [ ] “Golden” example payloads are updated and used in CI.
- [ ] No breaking change merged into `/api/v1`.

</details>

---

## CI gates (minimum recommended)

CI should block merges when any governed contract is invalid or incompatible:

1. **OpenAPI validation** (schema validity + required fields)
2. **JSON Schema validation** (payload schemas + cross-reference integrity)
3. **Policy tests** (OPA/Rego and/or Conftest; default deny; cite-or-abstain)
4. **Promotion gate checks** (license/sensitivity/catalogs/checksums/audit)
5. **Contract tests** (known inputs/outputs; compatibility)
6. **Provenance + redaction checks** (API responses include evidence/provenance bundle; policy redaction applied)
7. **Evidence resolution check** (citations resolvable; no dead refs)
8. **Link-check** for referenced governed artifacts (docs, catalogs) where applicable

---

## References

These documents define the platform expectations this folder implements:

- **KFM Next‑Gen Blueprint & Primary Guide** (2026‑02‑12)
- **KFM Data Source Integration Blueprint** (v1.0, 2026‑02‑12)
- **KFM Integration Report (New Ideas 2‑8‑26)** (deterministic IDs, receipts, fail‑closed lifecycle)
- Repository documentation on canonical subsystem homes and governed artifacts

Primary external standards commonly used by these contracts:

- OpenAPI 3.1
- JSON Schema
- OPA / Rego
- STAC, DCAT, PROV
- RFC 8785 (JSON Canonicalization Scheme)
- CloudEvents (if event envelopes are used)

