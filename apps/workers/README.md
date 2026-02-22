# apps/workers

Background/edge workers that run KFM ingestion, validation, indexing, and governance automation — **producing governed artifacts** (run receipts, catalogs, provenance) and **never bypassing policy**.

**Status:** draft • **Owners:** KFM Platform (TBD) • **Policy:** internal  
**Badges (expected):** CI • policy-tests • contract-tests • linkcheck • security

---

## Navigate

- [What belongs here](#what-belongs-here)
- [Repo context](#repo-context-reference)
- [How workers fit into KFM](#how-workers-fit-into-kfm)
- [Worker types](#worker-types)
- [Hard requirements](#hard-requirements)
- [Contracts emitted by workers](#contracts-emitted-by-workers)
- [Local development](#local-development)
- [Deployment](#deployment)
- [Observability](#observability)
- [Security and governance](#security-and-governance)
- [Add a new worker](#add-a-new-worker)
- [Definition of done](#definition-of-done)

---

## What belongs here

This folder is for **non-interactive compute** that:

- **Acquires** upstream data (connectors, snapshotters).
- **Transforms** and validates data (normalization, QA, redaction candidates).
- **Builds projections** from promoted artifacts (PostGIS/search/graph/tiles indexes).
- **Automates governance workflows** (e.g., create a *draft PR* when a material change is detected).

If a component needs to serve end-user requests, it belongs in the **governed API** (not here). If it renders UI, it belongs in the **frontend** (not here).

> NOTE  
> Some KFM blueprints refer to this area as `apps/worker/` (singular). This repo uses `apps/workers/` (plural) — treat them as the same conceptual component boundary.

[Back to top](#appsworkers)

---

## Repo context (reference)

The KFM blueprint recommends separating API/UI/worker apps from shared packages, and keeping governed artifacts (contracts, policy, data specs, stories) alongside code. This folder is the **worker** slice of that layout.

```text
repo/
  apps/
    api/
    ui/
    workers/
  packages/
    domain/
    usecases/
    policy/
    evidence/
    catalog/
    shared/
  data/
    specs/
    fixtures/
  policy/
    rego/
    fixtures/
    tests/
  contracts/
    schemas/
    openapi/
  docs/
    stories/
    adr/
    standards/
```

> NOTE  
> Treat this as a *reference layout*. If the repo differs, keep this README accurate to what exists.

[Back to top](#appsworkers)

---

## How workers fit into KFM

Workers operate on the **truth path** (RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED) and/or on **rebuildable projections** (PostGIS/search/graph/tiles). They should be designed so the system can always rebuild projections from canonical artifacts.

```mermaid
flowchart LR
  A[Upstream sources] --> B[Connectors and watchers]
  B --> C[RAW zone<br/>immutable artifacts and checksums]
  C --> D[WORK or QUARANTINE<br/>normalize, QA, redaction candidates]
  D --> E[PROCESSED<br/>publishable artifacts]
  E --> F[CATALOG/TRIPLET<br/>DCAT + STAC + PROV + run receipts]
  F --> G[Index builders<br/>PostGIS, search, graph, tiles]
  F --> H[Governed API<br/>policy enforcement + evidence resolver]
  G --> H
  H --> I[UI surfaces<br/>Map + Story + Focus]
```

**Key idea:** workers are *producers* of governed evidence and rebuildable projections; they are not the policy boundary themselves.

[Back to top](#appsworkers)

---

## Worker types

Use these buckets when naming workers and deciding runtime characteristics:

1. **Connectors / snapshotters**
   - Fetch upstream files/APIs, snapshot terms, write to RAW.
2. **Pipeline runners**
   - Normalize in WORK, produce QA + redaction candidates, write PROCESSED.
3. **Catalog builders**
   - Generate/validate DCAT + STAC + PROV; enforce cross-links; emit run receipts.
4. **Index builders (rebuildable)**
   - Build projections (DB/search/graph/tiles) from promoted artifacts.
5. **Automation / governance bots**
   - Detect changes, create draft PRs, open review tickets, or re-run validations.

Each worker should be explicit about:
- **Trigger**: schedule, queue event, webhook, manual run.
- **Inputs/outputs**: zones touched and artifact types produced.
- **Policy posture**: labels/obligations it must apply or enforce.
- **Idempotency strategy**: retries safe, duplicates safe, deterministic identifiers.

[Back to top](#appsworkers)

---

## Hard requirements

### Trust membrane and layering

Workers must respect KFM’s clean layering:

- Domain logic remains pure and should not talk to infrastructure directly.
- Storage and external systems must be reached through **interfaces/contracts** so policy and provenance checks cannot be bypassed.

### Truth path discipline

- **RAW is append-only**: do not mutate; supersede with a new acquisition.
- **QUARANTINE means “do not promote”** until validation/rights/sensitivity issues are resolved.
- Promotion must be **fail-closed**: if required gates/receipts/catalogs don’t exist or don’t validate, nothing moves forward.

### Run receipts for everything that matters

Every worker that performs a governed action must emit a **run receipt** capturing (at minimum):

- run_id, run_type, dataset identifiers (if applicable)
- inputs and outputs with digests
- validation status and report references
- policy decision (label + obligations)
- environment (commit, container digest, runtime, parameters)
- timestamps

(See “Contracts emitted by workers”.)

[Back to top](#appsworkers)

---

## Contracts emitted by workers

Workers are required to emit (or update) governed artifacts. The exact schemas live in the repo’s `contracts/` area (or equivalent), but the conceptual outputs are:

### Run receipt (run_record)

An immutable record of **what ran**, **with what inputs**, **producing which outputs**, **under which policy**.

Minimum conventions:
- **Digest-addressed artifacts** (`sha256:...`) for inputs/outputs.
- **Deterministic IDs** where possible (e.g., dataset_version derived from canonical spec hash).
- **Policy-safe logging**: do not leak restricted metadata in receipts or logs.

### Discovery envelope (for watchers)

If you build a watcher/connector that detects new upstream material, emit a discovery envelope that includes:
- `source_id` and `observed_at`
- `kfm_idempotency_key` (for safe retries and dedupe)
- `spec_ref` (what onboarding spec this maps to)
- `artifact_ref` (what was observed/fetched)

### Promotion manifest (when proposing a promotion)

Workers should never “silently promote” data. A promotion manifest plus receipts and validations are the evidence needed for review and release gates.

[Back to top](#appsworkers)

---

## Local development

This repo does not assume a single runtime for all workers (some may be containerized jobs, some may be edge workers, some may be queue consumers).

Minimum expectation for each worker subfolder:

- A **worker README** with:
  - prerequisites
  - local run command(s)
  - how to run tests
  - how to generate/validate receipts locally
- A **config reference**:
  - environment variables
  - required secrets (names only; no values)
  - safe defaults for dev

Suggested conventions (PROPOSED):
- Provide `make dev`, `make test`, and `make lint` (or `npm run ...` equivalents).
- Provide a “dry-run” mode that emits receipts without writing outputs.

[Back to top](#appsworkers)

---

## Deployment

Workers may deploy as one of:

- **Kubernetes Jobs / CronJobs** for scheduled pipeline runs.
- **Queue consumers** for event-driven ingestion or index rebuilds.
- **Edge workers** (e.g., Cloudflare Worker style) for lightweight discovery hooks.
- **CI-triggered automations** for draft PR creation and validation reporting.

Whatever the runtime:
- pin container images by **digest**
- record the digest in the run receipt
- keep an explicit rollback path (re-run previous promoted version; rebuild projections)

[Back to top](#appsworkers)

---

## Observability

Workers must be observable without leaking sensitive data.

Minimum signals:
- structured logs with run_id correlation
- metrics: success/fail counts, duration, input/output sizes, queue lag (if applicable)
- validation metrics: pass rate, failure categories, “materiality” decisions

Operational rules:
- QUARANTINE is a first-class outcome; do not treat it as “success”.
- retries must be bounded; DLQs must exist for queue-based workers.

[Back to top](#appsworkers)

---

## Security and governance

### Policy-as-code (shared semantics)

- The **same policy semantics** must apply in CI and runtime (or policy guarantees are meaningless).
- UI displays policy badges/notices but **never makes policy decisions**.

### Sensitivity defaults

- Default to deny for sensitive-location / restricted materials unless explicitly allowed.
- Prefer producing a separate `public_generalized` representation when public output is allowed but precise locations are not.
- Never embed precise coordinates in narratives or outputs unless policy allows and obligations are satisfied.

### Credentials and secrets

- Do not embed credentials in dataset specs or config committed to the repo.
- Prefer short-lived credentials and workload identity where possible.
- Make secrets discoverable by **name**, not value.

[Back to top](#appsworkers)

---

## Add a new worker

### 1) Define scope and contract surfaces

- What zone(s) does it touch?
- What artifacts does it read/write?
- What receipts/manifests does it emit?
- What policy labels and obligations can apply?

### 2) Implement idempotency + determinism

- stable IDs for datasets/artifacts
- dedupe keys for watcher events
- safe retries (no double-writes; append-only where required)

### 3) Wire policy + validation gates

- schema validation for inputs/outputs
- policy fixtures + contract tests
- fail-closed behavior

### 4) Ship with documentation

Each worker subfolder must include:
- `README.md` (run/test/deploy)
- a minimal architecture diagram
- example receipts (valid + invalid) for CI tests (redacted)

### 5) Add operational safety

- bounded retries + DLQ
- kill switch support (repo flag and/or secret) for emergency stop
- runbook pointer (incident + rollback)

[Back to top](#appsworkers)

---

## Definition of done

A worker is “done” when all are true:

- [ ] Runs are deterministic enough to reproduce outputs from the same inputs.
- [ ] Emits run receipts for every governed run (and stores them in the expected ledger location).
- [ ] Produces or references validation reports; failures are actionable.
- [ ] Policy checks are enforced (CI + runtime); default deny is supported.
- [ ] No secrets are committed; logs/receipts are policy-safe.
- [ ] Idempotency is implemented; retries do not corrupt truth path zones.
- [ ] Has tests: unit + contract (schemas/policy) + at least one integration happy path.
- [ ] Has docs: per-worker README + config reference + operational notes.

[Back to top](#appsworkers)
