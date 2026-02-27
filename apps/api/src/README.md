<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/69506857-003b-4561-a116-e6dcee02afce
title: apps/api/src — Governed API source
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-26
updated: 2026-02-26
policy_label: public
related:
  - ../../../README.md
  - ../README.md
  - ../../../docs/ (TODO: confirm paths)
tags: [kfm, api, governance, contracts]
notes:
  - This README documents *what belongs in src/* and the non-negotiable governance invariants for the API boundary.
  - Repo-specific run commands belong in the service-level README (../README.md).
[/KFM_META_BLOCK_V2] -->

# Governed API — Source (`apps/api/src`)
Contract-first enforcement boundary for datasets, STAC, evidence resolution, story nodes, and Focus Mode.

**Status:** draft · **Owners:** TBD

![CI](https://img.shields.io/badge/CI-TODO-lightgrey)
![API](https://img.shields.io/badge/API-%2Fapi%2Fv1-blue)
![Contracts](https://img.shields.io/badge/contracts-contract--first-brightgreen)
![Policy](https://img.shields.io/badge/policy-default--deny-orange)
![Audit](https://img.shields.io/badge/audit-required-red)

> **NOTE**
> This folder is the *governed API boundary*. If you’re looking for how to run the service locally, start at **`apps/api/README.md`** (one level up).

## Navigate
- [Purpose](#purpose)
- [Where this fits](#where-this-fits)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Minimal endpoint set](#minimal-endpoint-set)
- [Contracts and response conventions](#contracts-and-response-conventions)
- [Catalogs as contract surfaces](#catalogs-as-contract-surfaces)
- [Proposed source layout](#proposed-source-layout)
- [How to add or change an endpoint](#how-to-add-or-change-an-endpoint)
- [PR Definition of Done](#pr-definition-of-done)

---

## Purpose
This directory contains the implementation of the **governed API**, which is the system’s **enforcement boundary**. It is responsible for applying:
- policy decisions and redactions
- API/version semantics
- evidence resolution (citations must be resolvable)
- audit emission for governed operations

In other words: this is the layer where “governance becomes behavior,” not a doc promise.

---

## Where this fits
KFM’s architecture is designed so that **clients never reach storage directly**. The API boundary sits between:
- canonical artifacts and catalogs (DCAT/STAC/PROV)
- rebuildable projections (PostGIS/search/graph/tile caches)
- and all user-facing surfaces (Map UI, Story Mode, Focus Mode)

If your repo uses a monorepo layout (e.g., `apps/api`), this folder is the *API code* for that app. In older/alternate layouts, you may see the API boundary described as `src/server/`; treat these as the same conceptual boundary (this folder) and avoid duplicating API implementations.

---

## Non-negotiable invariants
These are the “trust membrane” rules. If any are unclear in code, **fail closed** until clarified.

### Trust membrane
- **Frontend/UI must not** access databases, object storage, or indexes directly.
- All user-facing data retrieval must flow through this governed API boundary.

### Layering
- Keep a clean separation:
  - **Domain** (pure models + rules)
  - **Use cases** (workflows)
  - **Interfaces** (contracts, repositories, policy adapters)
  - **Infrastructure** (datastores, indexes, deployment)
- Domain logic **must not** talk directly to infrastructure; it goes through interfaces.

### Policy-as-code consistency
- **The same policy semantics must hold in CI and runtime** (or at least the same fixtures + outcomes), otherwise CI guarantees are meaningless.
- Policy decisions happen here (API) and in evidence resolution; the UI only *renders* policy outcomes (badges/notices), it does not decide.

### Sensitive data posture
- Default-deny for sensitive/restricted datasets and sensitive locations.
- Prefer **separate public_generalized dataset versions** if any public representation is allowed.
- Do not embed precise coordinates in Story Nodes or Focus Mode outputs unless policy explicitly allows.
- Treat redaction/generalization as first-class transforms recorded in provenance.

### No “ghost metadata”
- Abstention is a feature: when withholding, explain *why* in policy-safe terms and return an `audit_ref`.
- Avoid behavior differences that leak restricted existence (including via errors).

### Versioning discipline
- Freeze `/api/v1` semantics; only add backward-compatible fields.
- Introduce `/api/v2` only for breaking changes.
- Version the schemas used by the system’s contract surfaces (DCAT/STAC/PROV and Story Node templates).

### Audit and observability
- Every governed operation must emit an audit record including:
  - who / what / when / why
  - inputs/outputs by digest
  - policy decision details (allow/deny, obligations, reason codes)
- Audit logs are sensitive: apply redaction and retention policy.

---

## Minimal endpoint set
A “buildable v1” endpoint set for KFM-style governed surfaces:

| Endpoint | Purpose | Notes |
|---|---|---|
| `GET /api/v1/datasets` | Dataset discovery and version listing | DCAT-backed; supports filters/facets/search |
| `GET /api/v1/stac/collections` | STAC collection access | Policy filter applied server-side |
| `GET /api/v1/stac/items` | STAC item search/query | bbox/time/collection; policy filter applied before returning assets |
| `POST /api/v1/evidence/resolve` | Resolve citations/evidence references | Returns bundle digest + policy decision results |
| `GET /api/v1/story` / `POST /api/v1/story` | Story Node list + create | Versioned; publish requires citations + review state |
| `GET /api/v1/story/{id}` / `PUT /api/v1/story/{id}` | Story Node read/update | Versioned; review/publish gate enforced |
| `POST /api/v1/focus/ask` | Governed Focus Mode Q&A | Must return citations or abstain + `audit_ref` |
| `GET /api/v1/lineage/status` | Pipeline health/freshness | Feeds UI trust badges |
| `GET /api/v1/lineage/stream` | Lineage stream (e.g., SSE) | Feeds UI trust surfaces |

Optional (depending on tile strategy):

| Endpoint | When used |
|---|---|
| `GET /api/v1/tiles/{layer}/{z}/{x}/{y}.pbf` | Dynamic vector tiles |
| `GET /assets/pmtiles/{dataset_version_id}/{layer}.pmtiles` | Static PMTiles bundles (policy-gated or public-only) |

---

## Contracts and response conventions

### Required response fields
Every response should include (when applicable):
- `dataset_version_id`
- artifact digests
- a **public-safe** `policy_label`
- `audit_ref` for governed operations (Focus Mode, publish/review actions, evidence resolution, etc.)

### Stable error model
Errors must use a stable, policy-safe model and include `audit_ref` for support and steward review.

<details>
<summary>Example error payload (shape)</summary>

```json
{
  "error_code": "POLICY_DENY",
  "message": "Restricted evidence not available to your role.",
  "audit_ref": "kfm://audit/...",
  "remediation": [
    "Try a broader time range.",
    "Switch to public datasets.",
    "Request steward review with the audit_ref."
  ]
}
```
</details>

### Avoiding restricted-existence leaks
- Ensure that 403/404 behavior does not differ in a way that confirms a restricted resource exists.
- Do not return partial “ghost metadata” for restricted resources unless policy explicitly allows it.

---

## Catalogs as contract surfaces
Catalogs are not “nice metadata.” They are **the canonical interface** between pipeline outputs and runtime surfaces.

- **DCAT**: dataset identity, publisher, license/rights, distributions
- **STAC**: assets, spatiotemporal extents, file locations
- **PROV**: lineage (inputs, tools, parameters, activities/agents)

The API should treat these as contract surfaces: validate, version, and rely on them consistently.

---

## Proposed source layout
Actual layout may differ; this is a recommended, reviewable structure that keeps governance explicit.

```text
apps/api/src/                                         # Governed API service (policy-enforced, evidence-first)
├── README.md                                          # You are here (run, env, contracts, policy, receipts, CI)
├── api/                                               # HTTP boundary (routing/controllers only)
│   └── routes/                                        # Versioned route modules (thin, no business logic)
│       ├── datasets.*                                  # /api/v1/datasets (catalog browsing + dataset details)
│       ├── stac.*                                      # /api/v1/stac/* (STAC access, profile constrained)
│       ├── evidence.*                                  # /api/v1/evidence/resolve (EvidenceRef → bundle)
│       ├── story.*                                     # /api/v1/story* (story nodes, publish/read, citation wiring)
│       ├── focus.*                                     # /api/v1/focus/ask (cite-or-abstain orchestration boundary)
│       └── lineage.*                                   # /api/v1/lineage/* (PROV/lineage queries, policy-gated)
├── contracts/                                         # Contract surface (spec-first + validation)
│   ├── openapi/                                        # OpenAPI (or equivalent) specifications (versioned)
│   └── schemas/                                        # JSON Schemas for request/response payloads (shared contracts)
├── policy/                                            # Policy integration (PDP + fixtures)
│   ├── pdp/                                            # OPA adapter / PDP client (decision + obligations)
│   └── fixtures/                                       # Allow/deny fixtures + obligations cases (tests + regression)
├── domain/                                            # Pure domain layer (no IO)
│   ├── models/                                         # Dataset, DatasetVersion, EvidenceBundle, StoryNode, etc.
│   └── rules/                                          # Pure rules (invariants, validation helpers, semantics)
├── usecases/                                          # Application workflows (policy-aware orchestration)
│   ├── resolveEvidence.*                               # EvidenceRef -> EvidenceBundle (receipts + obligations)
│   ├── publishStory.*                                  # Publish flow with citation resolution + audit events
│   └── focusAsk.*                                      # Focus orchestration + citation handshake (fail-closed)
├── interfaces/                                        # Ports (dependency inversion)
│   ├── repos/                                          # Repository interfaces (datasets, bundles, stories, lineage)
│   └── adapters/                                       # External interfaces (catalog loaders, policy, clock, id gen)
├── infra/                                             # Adapters/implementations (IO lives here)
│   ├── catalogs/                                       # DCAT/STAC/PROV readers/writers (if colocated here)
│   └── stores/                                         # PostGIS/search/graph adapters (never called by UI directly)
└── observability/                                     # Governed telemetry (redaction-aware)
    ├── audit/                                          # Audit record builder + sink (immutable events)
    ├── metrics/                                        # Counters/histograms/timers (policy-safe labels)
    ├── logging/                                        # Structured logs with redaction hooks
    └── ...                                             # Add tracing/propagation helpers if/when used
```

> **TIP**
> Keep API route handlers thin. Push meaning into **use cases** and enforce policy/audit in one place, so it’s hard to “forget governance” when adding features.

---

## How to add or change an endpoint
This repo follows **contract-first** behavior.

1. **Add/modify the contract artifact**
   - OpenAPI/SDL + JSON Schemas for request/response.
2. **Implement the route handler**
   - Validate inputs at the boundary.
3. **Apply policy before returning any data**
   - Prefer “deny with safe message + `audit_ref`” over partial leakage.
4. **Emit audit events**
   - Include digests and policy decision details.
5. **Add CI guards**
   - schema validation
   - policy fixture tests (allow/deny + obligations)
   - regression tests for “no restricted-existence leak” behavior
6. **Update trust surfaces**
   - ensure outputs enable Evidence Drawer / provenance inspection
   - ensure story publish and focus answers resolve citations via evidence resolver

---

## PR Definition of Done
Use this list to keep PRs reviewable and governance-safe.

- [ ] Contract updated first (OpenAPI/SDL + JSON Schema)
- [ ] Backward compatibility preserved for `/api/v1` (or new `/api/v2` introduced)
- [ ] Policy enforcement added/updated with fixtures-driven tests
- [ ] No new direct storage/index access from client surfaces (trust membrane intact)
- [ ] Audit records emitted for governed operations (`audit_ref` returned where required)
- [ ] Errors are policy-safe and do not leak restricted existence
- [ ] Story/Fo​​cus outputs include resolvable citations (or abstain)
- [ ] README/docs updated if the behavior changes contract surfaces

---

<a id="back-to-top"></a>
**Back to top:** [Navigate](#navigate)
