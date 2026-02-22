# apps

Deployable runtime applications for Kansas Frontier Matrix (KFM): the **governed API**, the **map/story/focus UI**, and the **pipeline + indexing worker**.

**Status:** draft  
**Owners:** see `CODEOWNERS` (or add owners here)  
**Last updated:** 2026-02-22

<!-- Badges (add once workflow names/paths are known):
[![CI](...)](...)
[![Security](...)](...)
[![Docs](...)](...)
-->

## Quick navigation

- [What lives in `apps/`](#what-lives-in-apps)
- [Directory layout](#directory-layout)
- [Runtime contract](#runtime-contract)
- [App responsibilities](#app-responsibilities)
  - [`apps/api`](#appsapi)
  - [`apps/ui`](#appsui)
  - [`apps/worker`](#appsworker)
- [Development](#development)
- [CI gates](#ci-gates)
- [Security and governance](#security-and-governance)
- [Release and deployment](#release-and-deployment)
- [Definition of Done](#definition-of-done)
- [Appendix: Glossary](#appendix-glossary)

---

## What lives in `apps/`

This directory is for **deployable runtime surfaces**:

- **`apps/api/`** — the governed API boundary (“trust membrane”) where policy, evidence resolution, and auditability are enforced.
- **`apps/ui/`** — the governed client UI: Map Explorer + Story Mode + Focus Mode (and restricted admin/steward surfaces).
- **`apps/worker/`** — pipeline runner + index builders; moves data through the truth path and (re)builds projections.

Shared, reusable logic should live in `../packages/` (domain, use cases, policy engine, evidence, catalog, shared DTOs/schemas). Applications should mostly be **composition + adapters**, not the home of core domain logic.

---

## Directory layout

This README assumes the `apps/` subtree looks like this (adapt if your repo differs):

~~~text
repo/
  apps/
    api/                  # governed API (interfaces + adapters)
    ui/                   # map/story/focus frontend
    worker/               # pipeline runner + index builders
    README.md             # (this file)
~~~

---

## Runtime contract

### Trust membrane and truth path (conceptual)

`apps/` exists to make two system invariants easy to enforce:

1) **Trust membrane**  
   External clients never access storage directly. The API enforces policy/provenance consistently.

2) **Truth path**  
   Data and evidence flow through lifecycle zones (RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → runtime surfaces). Projections (DB/search/tiles) must be rebuildable from canonical artifacts.

~~~mermaid
flowchart LR
  UI[apps/ui<br/>Map · Story · Focus] --> API[apps/api<br/>Governed API<br/>Policy + Evidence]
  API --> UI

  W[apps/worker<br/>Pipelines + Indexers] --> RAW[RAW]
  W --> WORK[WORK/QUARANTINE]
  W --> PROC[PROCESSED]
  W --> CAT[CATALOG/TRIPLET]
  W --> AUD[Audit ledger]

  CAT --> DB[PostGIS<br/>rebuildable]
  CAT --> SEARCH[Search index<br/>rebuildable]
  PROC --> TILES[Tiles<br/>rebuildable]

  DB --> API
  SEARCH --> API
  TILES --> API
  API --> AUD
~~~

### Cross-app contract surfaces (owned elsewhere)

These are shared contracts that apps should consume rather than redefine:

- **OpenAPI / DTO schemas** (API contract-first)
- **Policy labels + obligations**
- **EvidenceRef → EvidenceBundle resolution**
- **Catalog triplet validation (DCAT/STAC/PROV)**
- **Promotion manifests + run receipts**

Look for these under `../packages/` and `../data/` (exact locations may vary by repo).

---

## App responsibilities

### Summary table

| App | Primary purpose | Must | Must not |
|---|---|---|---|
| `apps/api` | Governed API boundary | Enforce policy consistently; return policy-safe metadata for reproducibility; provide evidence resolution + audit references | Leak restricted existence; bypass policy pack; embed domain logic that belongs in `packages/` |
| `apps/ui` | Governed client UI | Never embed privileged credentials; make trust visible (evidence drawer, dataset version, policy notices); block publishing when citations don’t resolve | Read from storage directly; hide governance; publish stories without resolvable evidence |
| `apps/worker` | Pipelines + index builders | Treat canonical artifacts as immutable; quarantine on failure; emit run receipts/manifests; rebuild projections from canonical sources | Treat projection stores as source of truth; “patch” published data without promotion gates |

---

## `apps/api`

The API is the **policy boundary** and the place where policy + evidence + auditing converge.

Typical API responsibilities:

- Dataset discovery (catalog-backed; role/policy filtered)
- Spatial/temporal querying (bbox/time/filter), returning policy-safe results
- Tile delivery (policy-safe tiles; cache varies by role/policy)
- Evidence resolution: EvidenceRef → EvidenceBundle
- Lineage/status endpoints for UI trust surfaces
- Focus Mode request handling with cite-or-abstain + audit receipts

Implementation guidance:

- Keep core business logic in `../packages/…` and use the API as a thin orchestration layer.
- Treat the OpenAPI contract as a **first-class governed artifact** (versioned, reviewed, and tested).

Suggested docs inside `apps/api/` (create if missing):

- `apps/api/README.md` — local run, env vars, endpoints, contract links
- `apps/api/openapi/` (or `../contracts/openapi/`) — spec source-of-truth
- `apps/api/tests/contract/` — contract tests for evidence resolver, policy envelopes, etc.

[Back to top](#apps)

---

## `apps/ui`

The UI is a **governed client**, not a privileged operator.

Core surfaces typically include:

- **Map Explorer** (primary)
- **Story Mode** (narratives with citations + map-state replay)
- **Catalog** (dataset discovery)
- **Focus Mode** (evidence-led Q&A with cite-or-abstain + audit refs)
- **Admin/Steward** (restricted governance tools)

UI hard requirements:

- No privileged credentials in the client.
- Trust surfaces are visible: evidence/provenance drawer accessible from map layers and story claims; dataset version labels; explicit policy notices; “what changed?” diffs; automation status badges.
- Publishing should be blocked if citations fail to resolve.

Suggested docs inside `apps/ui/` (create if missing):

- `apps/ui/README.md` — dev server, build, routes, a11y, trust surfaces checklist
- `apps/ui/docs/` — UX contracts for evidence drawer, policy notices, story publishing gates

[Back to top](#apps)

---

## `apps/worker`

The worker is responsible for:

- Running ingestion/normalization pipelines
- Writing artifacts into the lifecycle zones (RAW/WORK/PROCESSED)
- Generating catalogs (DCAT/STAC/PROV) and run receipts
- Building rebuildable projections (PostGIS/search/graph/tiles) from promoted artifacts
- Producing promotion manifests and driving promotion gates

Design principles:

- Canonical stores (object storage + catalogs + audit ledger) must be sufficient to rebuild everything else.
- Projection stores are rebuildable; they never become the source of truth.
- Failures should route to quarantine with actionable QA artifacts; no partial promotion.

Suggested docs inside `apps/worker/` (create if missing):

- `apps/worker/README.md` — how to run pipelines, where artifacts land, how to rebuild indexes
- `apps/worker/runbooks/` — incident procedures (rebuild, rollback, quarantine triage)

[Back to top](#apps)

---

## Development

This repo’s exact tooling may vary. Prefer app-local READMEs for concrete commands and ports.

### Common patterns

- Install dependencies once (workspace/root), then run per-app dev servers.
- Keep secrets out of the repo; use `.env` or secret managers per environment.
- Run policy tests and contract tests locally before PRs if available.

~~~bash
# Example flow (adapt to your tooling)
cd apps/api
# install deps
# run dev server
# run unit + integration tests

cd ../ui
# run dev server

cd ../worker
# run pipeline / index rebuild tasks
~~~

---

## CI gates

CI should fail closed and enforce governance invariants. Typical gates include:

- Lint + typecheck
- Unit tests
- Catalog validation (DCAT/STAC/PROV)
- Link-check citations / evidence references
- Policy tests (default deny + fixtures)
- Spec hash drift checks
- Evidence resolver contract tests
- (Optional) Focus Mode evaluation harness

If your repo does not yet implement these gates, treat this as a target checklist to encode in CI.

---

## Security and governance

Non-negotiable rules for `apps/`:

- **UI never embeds privileged credentials** and never bypasses the API boundary.
- **API enforces policy** and returns policy-safe error messages that do not leak restricted existence.
- **Worker promotes deterministically**: immutable artifacts + digests + run receipts + approvals where required.
- **Sensitive locations / vulnerable infrastructure**: default to generalized outputs + explicit policy notices; do not ship precise geometry to public surfaces.

---

## Release and deployment

`apps/` are deployable units and should have:

- Versioned artifacts (images/bundles) with reproducible builds
- GitOps-managed environment manifests (see `../ops/` if present)
- Rollback strategy (especially for API/UI) and rebuild strategy (especially for worker/indexers)

---

## Definition of Done

### Any change under `apps/` is “done” when:

- [ ] Does not violate trust membrane (no client-to-storage shortcuts)
- [ ] Does not introduce policy bypass paths
- [ ] Preserves reproducibility (dataset versions + evidence refs + digests where applicable)
- [ ] Includes tests (unit + contract/integration where relevant)
- [ ] Updates app-local docs (`apps/*/README.md`) if behavior changed
- [ ] CI gates remain green (or are updated to reflect new contracts)

### API-specific

- [ ] OpenAPI/contract updated (if public surface changed)
- [ ] Contract tests updated/added (especially evidence/policy envelope)
- [ ] Audit logging + policy-safe errors verified

### UI-specific

- [ ] Trust surfaces preserved (evidence drawer, policy notices, dataset versions)
- [ ] Accessibility minimums maintained
- [ ] Story publishing gates block unresolved citations

### Worker-specific

- [ ] Promotion gates enforced (no partial promotion)
- [ ] Run receipts/manifests emitted for new/changed outputs
- [ ] Projection rebuild still possible from canonical artifacts

---

## Appendix: Glossary

- **Truth path:** Ordered lifecycle from acquisition through RAW/WORK/PROCESSED/CATALOG to published surfaces.
- **Trust membrane:** Boundary preventing clients from direct storage access and enforcing policy/provenance in governed APIs.
- **Run receipt:** Immutable record of a run (inputs/outputs by digest, environment capture, validation results, policy decisions).

[Back to top](#apps)
