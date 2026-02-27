<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/5f6a8d2e-3bf4-4e3b-82c4-9f7df5e3a6e1
title: apps/api/src/interfaces — Interfaces Layer
type: standard
version: v1
status: draft
owners: TODO(api-team)
created: 2026-02-27
updated: 2026-02-27
policy_label: restricted
related:
  - kfm://doc/TODO-kfm-main-guide
tags: [kfm, api, interfaces, contracts, policy]
notes:
  - This README documents the Interfaces layer (ports + contracts) for the API app.
  - Repo-specific subfolders and tooling are intentionally marked TODO until verified.
[/KFM_META_BLOCK_V2] -->

# apps/api/src/interfaces
**Purpose:** The API boundary’s *contracts + ports*: DTOs, schemas, repository interfaces, and policy adapters that keep the trust membrane intact.

[![Status](https://img.shields.io/badge/status-draft-yellow.svg)](#)
[![Layer](https://img.shields.io/badge/layer-interfaces-blue.svg)](#)
[![Policy](https://img.shields.io/badge/policy-restricted-orange.svg)](#)
[![CI](https://img.shields.io/badge/ci-TODO-lightgrey.svg)](#)

**Quick nav**
- [Why this exists](#why-this-exists)
- [What belongs here](#what-belongs-here)
- [What must not go here](#what-must-not-go-here)
- [Suggested directory layout](#suggested-directory-layout)
- [Contract rules](#contract-rules)
- [Ports and repositories](#ports-and-repositories)
- [Policy adapters](#policy-adapters)
- [Error model](#error-model)
- [Definition of Done](#definition-of-done)
- [Appendix: examples](#appendix-examples)

---

## Why this exists

KFM uses a clean layering model:

- **Domain**: pure domain models + rules  
- **Use cases**: workflows (ingest, promote, publish story, focus query)  
- **Interfaces**: **contracts** (OpenAPI DTOs, schema registries, policy adapters, repository interfaces)  
- **Infrastructure**: DBs, indexes, object storage, CI, deployment  

**Rule:** Domain logic must not talk directly to infrastructure; it talks through **interfaces**.  
This is how we preserve the **trust membrane**: clients never fetch storage/DB directly, and core logic never bypasses repository interfaces.  

> **Non-negotiable:** If you add a new storage/index/service dependency, you add it by defining a *port* here and implementing it in Infrastructure.  
> No “quick import the DB client in a use case.”

---

## What belongs here

This folder should contain **only boundary artifacts**:

### 1) API contracts
- Request/response DTOs (versioned)
- OpenAPI (or equivalent) contract artifacts
- Response metadata conventions (dataset_version_id, digests, audit_ref)
- Contract test fixtures (if stored alongside the contract)

### 2) Ports (interfaces / repositories)
- Repository interfaces used by use-cases/domain:
  - `DatasetRepository`, `CatalogRepository`, `EvidenceRepository`, `AuditRepository`, etc.
- Service ports:
  - `PolicyEvaluator` / `PolicyClient` port
  - `Clock` / `Uuid` abstraction (if you’re enforcing determinism and testability)
  - External provider ports (e.g., “CatalogStore”, “ObjectStore”) — **as interfaces only**

### 3) Schemas and registries
- JSON Schemas for:
  - run receipts / run manifests
  - policy decision objects
  - any “contract-first” artifacts that must validate in CI

### 4) Boundary mapping helpers (lightweight)
- Pure mappers:
  - Domain → DTO
  - DTO → Domain
- (No network calls, no DB calls, no filesystem writes.)

---

## What must not go here

**Exclusions (fail-closed posture):**
- No database clients, ORMs, SQL, PostGIS code
- No HTTP fetchers / SDK calls (those are *infrastructure implementations*)
- No filesystem/object storage writes
- No business logic / workflows (belongs in Use Cases)
- No UI-specific formatting rules (belongs in UI)

If you see side effects here, treat it as a layering violation.

---

## Suggested directory layout

> **NOTE:** This is a *suggested* structure until repo reality is verified.  
> Replace with the actual tree once you confirm current folders and naming conventions.

```
interfaces/
  README.md

  contracts/
    v1/
      openapi.yaml              # or openapi.json
      dto/
        dataset.ts
        stac.ts
        story.ts
        focus.ts
      errors.ts                 # stable API error model

  policy/
    PolicyDecision.ts           # policy decision + obligations shape
    PolicyClient.ts             # port: evaluate(input) -> decision

  repositories/
    DatasetRepository.ts
    EvidenceRepository.ts
    CatalogRepository.ts
    AuditLedgerRepository.ts

  schemas/
    run_receipt.v1.schema.json
    run_manifest.v1.schema.json
    policy_decision.v1.schema.json

  index.ts                      # public exports for this layer
```

---

## Contract rules

### Contract-first boundary
All clients (UI, tools, external consumers) rely on the **governed API** as the enforcement boundary.

**Contract implications:**
- Contract artifacts must be versioned (e.g., `v1/`, `v2/`).
- `/api/v1` semantics are “frozen”; only additive/backwards-compatible changes are allowed.
- Breaking changes require a new version surface.

### Required response metadata (KFM alignment)
When applicable, responses should expose:
- `dataset_version_id`
- artifact `digests` (when returning artifacts or references)
- policy-safe `policy_label`
- `audit_ref` for governed operations (e.g., Focus, Story publish)

This makes UI trust surfaces possible (evidence drawer, provenance, “what changed”).

---

## Ports and repositories

Ports are *stable abstractions* that let domain/use-cases work without knowing “how storage works.”

### Design rules
- Ports are **pure interfaces** (types + method signatures).
- Ports use **domain types** (or explicit boundary DTOs), not ORM models.
- Ports return results that preserve **auditability** (digests, ids, version ids).
- Ports must make it possible to **fail closed** (explicit `deny` / `notFound` / `policyBlocked` outcomes).

---

## Policy adapters

Policy evaluation is a first-class boundary.

### What policy returns
Policy evaluation should return:
- allow/deny
- **obligations** (e.g., redaction/generalization required)
- reason codes (for audit + policy-safe UX)

**Important:** obligations are not optional decoration — they are required to safely publish generalized outputs rather than hard-deny in many cases.

---

## Error model

Errors must avoid “ghost metadata” leakage.

### Stable error shape (recommended)
Every error response should include:
- `error_code` (stable)
- `message` (policy-safe)
- `audit_ref`
- optional `remediation` hints (safe alternatives)

Guideline:
- Align 403/404 behavior with policy to avoid revealing existence of restricted resources.

---

## Definition of Done

### For any PR touching `apps/api/src/interfaces/`
- [ ] Contract updates are versioned (no breaking changes inside existing v1 surface).
- [ ] Contract tests updated (OpenAPI validation / DTO validation / schema validation).
- [ ] Policy decision shape includes obligations + reason codes where applicable.
- [ ] Error model remains stable and policy-safe.
- [ ] No infrastructure dependencies introduced in this layer.
- [ ] Evidence-related contracts include `dataset_version_id`, digests, and `audit_ref` where applicable.
- [ ] If new capability is introduced: update directory layout and exports.

---

## Appendix: examples

### Example port (repository interface)
```ts
// repositories/DatasetRepository.ts
export interface DatasetRepository {
  listDatasets(input: {
    query?: string;
    filters?: Record<string, string | number | boolean>;
    // important for time-aware + governed behavior:
    actor: { principalId: string; role: string };
  }): Promise<{
    datasets: Array<{
      datasetId: string;
      title: string;
      latestVersionId?: string;
      policyLabel: "public" | "restricted" | "internal" | string;
    }>;
    auditRef: string;
  }>;
}
```

### Example policy decision + obligations
```ts
// policy/PolicyDecision.ts
export type PolicyObligation =
  | { type: "redact_fields"; fields: string[] }
  | { type: "generalize_geometry"; precision: "coarse" | "medium" }
  | { type: "suppress_download"; reason: string };

export interface PolicyDecision {
  decisionId: string;
  allow: boolean;
  policyLabel: string; // policy-safe label
  obligations: PolicyObligation[];
  reasonCodes: string[];
}
```

### Example stable API error shape
```ts
// contracts/v1/errors.ts
export interface ApiError {
  error_code: string;
  message: string;     // policy-safe
  audit_ref: string;
  remediation?: string[];
}
```

---

<a id="back-to-top"></a>
**Back to top:** [apps/api/src/interfaces](#appsapisrcinterfaces)
