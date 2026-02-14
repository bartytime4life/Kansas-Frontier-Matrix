<!--
File: src/server/usecases/README.md
Layer: Use Cases / Application Services
Status: Governed engineering documentation
-->

# Server Use Cases (`src/server/usecases`)

![Layer](https://img.shields.io/badge/clean%20architecture-usecases-blue)
![Governance](https://img.shields.io/badge/governed-yes-4c1)
![Policy](https://img.shields.io/badge/OPA-default%20deny-important)
![Evidence](https://img.shields.io/badge/evidence-first-required-orange)
![Trust Membrane](https://img.shields.io/badge/trust%20membrane-enforced-critical)

This directory contains **KFM server “Use Cases”** (a.k.a. *Application Services*): the workflows and business rules that sit **between** inbound adapters (HTTP/GraphQL handlers) and outbound adapters (DB/search/graph/object-store clients).

Use cases are where KFM’s **governance invariants become executable**: policy checks, evidence/citation requirements, audit logging, provenance assembly, and sensitivity/redaction are enforced here (or *explicitly* orchestrated from here via ports).

---

## Table of contents

- [Non-negotiables](#non-negotiables)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Architecture boundary](#architecture-boundary)
  - [Trust membrane rules](#trust-membrane-rules)
  - [Clean-layer dependency rules](#clean-layer-dependency-rules)
- [Directory conventions](#directory-conventions)
- [Standard use case shape](#standard-use-case-shape)
- [Request context contract](#request-context-contract)
- [Policy enforcement](#policy-enforcement)
- [Evidence, provenance, and resolvers](#evidence-provenance-and-resolvers)
- [Audit logging](#audit-logging)
- [Sensitivity & redaction](#sensitivity--redaction)
- [Deterministic IDs & caching](#deterministic-ids--caching)
- [Error handling](#error-handling)
- [Testing strategy](#testing-strategy)
- [Observability](#observability)
- [Adding a new use case](#adding-a-new-use-case)
- [Definition of Done](#definition-of-done)
- [Review checklist](#review-checklist)
- [Glossary](#glossary)
- [References](#references)

---

## Non-negotiables

> [!IMPORTANT]
> These are *platform contracts* — not optional conventions.

1. **No UI direct database access.** All access is mediated by the governed API boundary.
2. **Fail-closed policy.** If policy evaluation fails or is uncertain, **deny**.
3. **Processed zone is the only source of truth.** The API serves from processed catalogs only.
4. **Evidence-first outputs.** If a response makes non-trivial claims, it must provide resolvable evidence refs.
5. **Focus Mode must cite or abstain**, and must return an **audit reference** for every response.

> Tip: If you’re unsure whether something should be enforced here or in an adapter, default to enforcement in the use case (or an explicitly invoked policy/audit/evidence helper used by the use case). The adapter should be thin.

---

## What belongs here

Use cases should:
- Orchestrate **workflows** that combine multiple domain operations and persistence calls.
- Enforce **business rules** and **governance rules** (policy, evidence, sensitivity).
- Convert domain decisions into **integration DTOs** (without importing adapter frameworks).
- Produce **audit + provenance hooks** (or trigger them via ports).
- Remain testable with **mocked ports** and deterministic inputs.

Typical KFM use cases (illustrative):
- `queryFocusMode` (governed Q&A: retrieve evidence → draft → policy validate → audit append)
- `getStoryNode` / `listStoryNodes`
- `publishStoryNode` (governed content publish)
- `queryMapFeatures` / `getLayerMetadata` / `getTile`
- `resolveEvidence` (STAC/DCAT/PROV/doc/graph resolvers)
- `requestDatasetPromotion` (admin-only; gates; audit)

---

## What does not belong here

Use cases **must not**:
- Contain HTTP framework objects (e.g., `req/res`, routers, middleware).
- Instantiate DB clients, ORMs, HTTP clients, or SDKs directly.
- Read secrets from the environment directly (prefer injected config/ports).
- Implement storage-specific query syntax (SQL, Cypher, OpenSearch DSL, S3 APIs).
- Skip governance because “the adapter already checked it”.

> [!CAUTION]
> If you import from infrastructure/adapters, you are probably breaking the trust membrane and clean-layer contract.

---

## Architecture boundary

### Trust membrane rules

The trust membrane is the boundary where governance is enforced; it must be “designed in,” not bolted on later.

**Implications for use cases:**
- Every request that touches data/stories/AI must be **policy-evaluated**.
- Use cases must use **ports** (repository interfaces) and **cannot bypass them**.
- **Audit + provenance** should be produced as part of the normal request path.

### Clean-layer dependency rules

KFM’s canonical backend layout is organized as:

- **Domain**: entities/value objects + invariants
- **Use Cases**: workflows + business rules (**this folder**)
- **Integration**: ports/contracts + DTOs
- **Infrastructure**: DB clients, API handlers, OPA adapters, external SDKs

> [!NOTE]
> These are logical layers. The exact directory names in this repo should match the clean-layer contract.

---

## Directory conventions

Recommended organization (adjust to actual repo conventions):

```text
src/server/usecases/                                 # Application use-cases (orchestration layer; ports in, ports out)
├─ README.md                                         # Use-case conventions, folder rules, testing strategy, invariants
│
├─ _shared/                                          # Shared pure helpers used across multiple use-cases
│  ├─ errors/                                        # Shared error helpers (typed failures, mapping, normalization)
│  ├─ policy/                                        # Policy helper wrappers (still evaluated via ports; no direct OPA calls)
│  ├─ evidence/                                      # Evidence pack assembly helpers (bundling, normalization, limits)
│  ├─ audit/                                         # Audit helpers (emit records/events via ports; no storage here)
│  ├─ validation/                                    # Input validation utilities (schemas + friendly errors)
│  ├─ pagination/                                    # Cursor/limit helpers (stable ordering guarantees)
│  └─ time/                                          # Deterministic clock helpers (injectable; test-friendly)
│
├─ ai/                                               # AI-facing orchestrations (Focus Mode boundary)
│  └─ queryFocusMode/                                # “Ask Focus Mode” use-case (governed: cite-or-abstain + audit)
│     ├─ index.ts                                    # Public entrypoint/re-exports
│     ├─ types.ts                                    # DTOs + port contracts specific to this use-case
│     ├─ schema.ts                                   # Input/output validation (request/response envelopes)
│     ├─ usecase.ts                                  # Orchestrator: validate → policy → retrieve → assemble → respond
│     ├─ assembleEvidence.ts                         # Evidence bundle builder (dedupe, cap, ordering, sensitivity filtering)
│     └─ __tests__/                                  # Unit tests (determinism, policy wiring, edge cases)
│
├─ stories/                                          # Story Node use-cases (read + publish lifecycle)
│  ├─ getStoryNode/                                  # Fetch/resolve Story Node + assets + citations (policy-filtered)
│  ├─ publishStoryNode/                              # Promote draft → published (checks: citations, licensing, policy, audit)
│  └─ __tests__/                                     # Story use-case tests (happy/deny/redaction paths)
│
├─ layers/                                           # Map layer use-cases (metadata + feature querying)
│  ├─ getLayerMetadata/                              # Layer metadata (style/tiles/attribution/sensitivity)
│  ├─ queryMapFeatures/                              # Feature queries (bbox/time filters; policy applied; stable paging)
│  └─ __tests__/                                     # Layer use-case tests (filters, paging, policy enforcement)
│
└─ evidence/                                         # Evidence resolution use-cases
   ├─ resolveEvidence/                               # Resolve CitationRef/EvidenceRef → EvidenceBundle (policy-filtered)
   └─ __tests__/                                     # Evidence use-case tests (resolution, errors, redaction, caching behavior)
```

### Naming

- Use **verbNoun** for use cases: `getStoryNode`, `publishStoryNode`, `queryFocusMode`.
- Use folders to keep related files together (types, schema, usecase, tests).
- Prefer `index.ts` to export the public API of a use case folder.

---

## Standard use case shape

Use cases should have a consistent, test-friendly signature:

- Input DTO (`Input`)
- Output DTO (`Output`)
- Request context (`ctx`)
- Dependencies injected as a `deps` object containing **ports** and configuration

<details>
<summary><strong>Suggested TypeScript shape (illustrative)</strong></summary>

```ts
// NOTE: Names are illustrative; adapt to actual repo conventions.

export type RequestContext = {
  requestId: string;
  actor: { role: "public" | "reviewer" | "admin"; subject?: string; claims?: Record<string, unknown> };
  viewState?: { timeRange?: [string, string]; bbox?: [number, number, number, number]; activeLayers?: string[] };
  now: string; // ISO 8601, injected (no Date.now() inside core logic)
};

export type UseCase<I, O> = (input: I, ctx: RequestContext) => Promise<O>;

export type Deps = {
  policy: PolicyPort;
  audit: AuditPort;
  evidence: EvidencePort;
  // repositories / gateways:
  datasets: DatasetRepoPort;
  stories: StoryRepoPort;
  search: SearchPort;
  graph: GraphPort;
};

export const makeGetStoryNode = (deps: Deps): UseCase<{ storyId: string }, { story: unknown }> =>
  async (input, ctx) => {
    await deps.policy.authorizeOrThrow({ action: "story.read", input, ctx });

    const story = await deps.stories.getById(input.storyId);
    if (!story) throw new NotFoundError("StoryNotFound", { storyId: input.storyId });

    // Optionally attach provenance links / audit trail pointers.
    return { story };
  };
```
</details>

### Determinism

Use cases should be deterministic given:
- `input`
- `ctx` (including `ctx.now`)
- the data returned by ports

Avoid nondeterminism:
- Random IDs in outputs (unless explicitly required and audited)
- `Date.now()` / `new Date()` inside use case logic
- Unbounded queries (no limits, no cursors)

---

## Request context contract

Use cases should receive the minimum context needed to:
- Evaluate policy
- Assemble evidence packs/citations
- Record audit events
- Provide deterministic timestamps and correlation IDs

**Minimum recommended `ctx` fields**
- `requestId` / `correlationId`
- `actor` identity + role + claims
- `viewState` (for map/time/story context; used heavily in Focus Mode)
- `now` (ISO-8601 timestamp injected by adapter)

> [!TIP]
> If the UI passes a `ViewState` (time range, bbox, active layers, story node id), treat it as first-class context for evidence retrieval and for audit trails.

---

## Policy enforcement

### Fail-closed behavior

Policy is evaluated using OPA/Rego with **default deny**.

Use cases must:
- Call policy authorization at the start of workflows (or earlier in an adapter, but never *only* there).
- Validate outputs when required (notably for Focus Mode / AI outputs).
- Treat policy system errors as denial (**fail closed**).

### Recommended pattern

- `authorizeOrThrow(...)` early
- `validateOutputOrThrow(...)` before returning for governed outputs (AI, story publish, evidence resolution)
- include policy decision refs in audit records

<details>
<summary><strong>Policy input shaping (illustrative)</strong></summary>

```ts
type PolicyInput = {
  actor: { role: string; attributes?: Record<string, unknown> };
  request: { endpoint: string; action: string; context: Record<string, unknown> };
  resource?: Record<string, unknown>;
  answer?: { hasCitations?: boolean; sensitivityOk?: boolean; citations?: unknown[] };
};
```
</details>

---

## Evidence, provenance, and resolvers

KFM requires evidence-first outputs. Practically:

- Every citation/provenance reference must be **resolvable** via API endpoints (e.g., `prov://`, `stac://`, `dcat://`, `doc://`, `graph://`).
- The UI must offer “Review Evidence” for map layers and Focus Mode answers.
- A Focus Mode answer must be **auditable outside the UI** (exportable citation list).

### Evidence packs (use-case responsibility)

For governed responses, the use case should assemble an **evidence pack** that includes:
- Stable locators (dataset ids, STAC item/collection ids, PROV ids, doc spans/pages, graph ids)
- Any computed summaries (counts/trends) plus their query provenance
- The policy decision outcome

### Evidence resolver use cases

This folder should include use cases (or helpers) that back evidence endpoints such as:

- `GET /api/v1/evidence/dcat/{id}`
- `GET /api/v1/evidence/stac/{id}`
- `GET /api/v1/evidence/prov/{id}`
- `GET /api/v1/evidence/doc/{id}?page=...&span=...`
- `GET /api/v1/evidence/graph/{id}`

> [!IMPORTANT]
> Acceptance criterion: “Given any `citation.ref` in a Focus Mode answer, the UI can resolve it to a human-readable evidence view in **≤ 2 API calls**.”

---

## Audit logging

The audit ledger is the immutable record of:
- What was requested
- What evidence was used/produced
- What policy decisions were applied
- What outputs were returned (or why the system abstained/denied)

Use cases must:
- Append audit events for governed operations (AI answers, story publish, dataset promotion, restricted evidence resolution).
- Return an `audit_ref` in responses where required (especially Focus Mode).
- Prefer append-only semantics and tamper-evident storage patterns (implementation is via ports).

> [!NOTE]
> If you’re adding a new use case that returns derived facts or makes decisions, consider whether it needs an audit event and/or an audit reference returned to the caller.

---

## Sensitivity & redaction

KFM includes governance for culturally sensitive knowledge and precise locations.

Use cases must:
- Consult policy labels / dataset classifications via ports
- Apply redaction rules consistently
- Prefer serving generalized derivatives to public roles
- Require elevated grants/roles for precise or restricted data
- Ensure both generalized and precise artifacts have separate provenance chains (document transformation/redaction)

> [!CAUTION]
> Never “helpfully” bypass redaction because “the data is in the DB anyway.” That violates KFM’s governance model and trust contract.

---

## Deterministic IDs & caching

### Deterministic identity

KFM uses deterministic IDs/hashes to support:
- reproducible evidence packs
- stable citations
- cache keys (ETag / Last-Modified)
- provenance equivalence checks

**Recommended:**
- Use canonical JSON hashing for “spec hashes” (e.g., RFC 8785 JCS) when generating stable identifiers for specs/build recipes.
- Include schema identifiers and recipe versions where applicable.

### Caching guidance

Use cases should:
- Be explicit about pagination (cursor/limit)
- Avoid unbounded scans
- Prefer read models/materialized views (via ports) for heavy queries
- Use stable cache keys only when underlying provenance/version can be captured in the audit record

---

## Error handling

### Principles

- Prefer **typed errors** (domain errors vs policy denies vs validation errors).
- Fail closed on policy uncertainty.
- For governed responses, return “abstain” (with explanation + audit ref) when evidence is insufficient or not valid for the actor/context.

### Suggested error taxonomy (illustrative)

| Error kind | Example | Typical HTTP mapping (adapter responsibility) |
|---|---|---|
| ValidationError | invalid bbox/timeRange | 400 |
| PolicyDenied | default deny, missing grant | 403 |
| NotFound | story/dataset missing | 404 |
| Conflict | concurrent publish conflict | 409 |
| UpstreamUnavailable | search/graph down | 503 |
| EvidenceInsufficient (AI) | cannot cite | 200/422 (repo choice) but must include abstain + audit_ref |

> [!IMPORTANT]
> Do **not** return partial sensitive data “with a warning.” If the policy outcome is deny, the output is deny.

---

## Testing strategy

Use cases are required to be testable without infrastructure.

### Minimum tests expected

1. **Use-case tests with mocked ports**
   - authorization called
   - redaction applied
   - evidence pack assembled (when required)
   - audit event appended (when required)
2. **Schema/contract tests**
   - request/response DTOs conform to JSON schema/OpenAPI/GraphQL definitions
3. **Regression/golden tests** (for governed AI outputs)
   - cite-or-abstain behavior preserved
   - required citation refs resolvable shape preserved
4. **Policy tests**
   - OPA rules: default deny, cite-or-abstain enforcement, sensitivity constraints

> [!TIP]
> If a use case introduces a new output field, add it to contract tests and verify it appears in evidence/audit packs where relevant.

---

## Observability

Use cases should produce structured events (via injected logger/telemetry port or adapter-provided context):

- Correlation/request id
- Actor role (not PII)
- Dataset/story identifiers (stable IDs)
- Policy decision id/summary
- Audit reference
- Timing information (span start/end)
- Evidence pack size & resolver refs (counts only)

Avoid logging:
- secrets
- precise restricted locations for public users
- raw document content unless explicitly allowed and audited

---

## Adding a new use case

1. **Create folder** under the appropriate domain area.
2. Define:
   - `types.ts` (Input/Output)
   - `schema.ts` (validation)
   - `usecase.ts` (workflow)
   - `index.ts` (exports)
3. Identify ports needed (add to integration layer if missing).
4. Implement workflow:
   - authorize (policy)
   - retrieve/compute (ports)
   - apply redaction rules (if applicable)
   - assemble evidence refs (if output requires claims)
   - validate output invariants (policy / cite-or-abstain)
   - append audit event (if required)
5. Add tests:
   - unit test with mocked ports
   - contract/schema test
   - policy test updates if needed
6. Update wiring:
   - adapter/controller routes call the use case (no business logic in adapter)
7. Update docs:
   - link the use case from relevant layer READMEs or API docs

---

## Definition of Done

> [!CHECKLIST]
> A use case is “done” only if:

- [ ] **Architecture**: No imports from infrastructure/adapters; only domain + integration contracts.
- [ ] **Policy**: Authorization enforced; fail-closed on policy errors.
- [ ] **Evidence**: Outputs that make claims include resolvable citation/provenance refs.
- [ ] **Focus Mode** (if applicable): cite-or-abstain; returns `audit_ref` every time; no external browsing.
- [ ] **Audit**: audit event appended for governed operations.
- [ ] **Sensitivity**: redaction/generalization applied per role/policy labels.
- [ ] **Determinism**: no random/time nondeterminism; uses `ctx.now`.
- [ ] **Tests**: unit tests with mocked ports + contract/schema tests.
- [ ] **Docs**: README/API contract updated when new endpoint or contract fields are introduced.

---

## Review checklist

Before merging:
- [ ] Can I point to where policy is called and what happens on policy failure?
- [ ] If the request is public-role, is there *any* path that could return restricted geometry or restricted details?
- [ ] If the output includes citations, can each `citation.ref` be resolved by an evidence resolver use case?
- [ ] Is the processed zone the only source used for responses?
- [ ] Are audit events written for governed outcomes, and is `audit_ref` returned where required?
- [ ] Are tests strong enough to prevent regression of cite-or-abstain and redaction?
- [ ] Are dependency boundaries respected?

---

## Glossary

- **Use case**: A workflow/business operation triggered by an API request; orchestrates domain + ports.
- **Port**: Interface for an external dependency (DB, search, graph, object storage, policy, audit).
- **Adapter**: Concrete implementation of a port (e.g., PostGIS repo, Neo4j client, OpenSearch client).
- **Trust membrane**: Governance boundary where all access/policy/evidence rules are enforced.
- **Evidence pack**: Structured bundle of evidence objects/locators used to justify outputs.
- **Citation ref**: Stable locator that can be resolved via evidence endpoints.
- **Audit ledger**: Append-only log of requests, evidence, policy decisions, and outputs/abstentions.
- **Processed zone**: Validated/published data zone; the only zone the API should serve from.

---

## References

These are the design sources that define the invariants this folder must uphold:

- KFM Next-Generation Blueprint & Primary Guide (2026-02-12)
- KFM Data Source Integration Blueprint (2026-02-12)
- KFM Comprehensive / Unified Technical Blueprints (governance + repo layout)

(See project docs for the authoritative versions and acceptance criteria.)

