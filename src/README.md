# src

This directory contains **KFM executable code**. It is intentionally split into three areas:

- `src/pipelines/` — ingestion + transformation jobs that produce governed outputs
- `src/graph/` — knowledge graph build and maintenance utilities
- `src/server/` — the governed API boundary and request-path governance

> [!IMPORTANT]
> KFM’s **trust membrane** is a build invariant:
> - The frontend does not access databases directly.
> - Every data, story, and AI request is policy-evaluated.
> - Backend logic uses repository interfaces and does not bypass them.
> - Audit and provenance are produced as part of normal request handling.
>
> If you are about to “just query the DB from the UI” or “just write a quick script that skips catalogs,” stop and route it through the intended layer.

---

## Directory map

```text
src/
├── pipelines/   # ETL jobs, data transformations, validators, catalog writers
├── graph/       # Graph build, imports/exports, constraints, alignment utilities
└── server/      # Governed API service + policy/audit integration
```

---

## What goes where

| Path | What it is | Primary outputs |
|---|---|---|
| `src/pipelines/` | Connector-driven ingestion + processing (raw → work → processed) | Processed artifacts + run records + validation reports + catalogs |
| `src/graph/` | Builds/updates graph representations from processed zone | Graph import artifacts and constraint checks |
| `src/server/` | Governed API boundary enforcing auth, policy, audit, evidence resolution | API responses with citations + `audit_ref` |

---

## Guardrails

### Do not cross layers

KFM’s backend uses Clean Architecture boundaries. Keep code in the *lowest* layer that can correctly own it.

<details>
<summary><strong>Recommended layering inside <code>src/server/</code></strong></summary>

A typical layout inside `src/server/` should mirror clean layers:

```text
src/server/
├── domain/            # entities + invariants (no DB, no HTTP)
├── usecases/          # workflows and business rules (depends on domain + ports)
├── integration/       # ports/contracts/DTOs (interfaces; schema/contract tests)
└── infrastructure/    # concrete adapters: DB clients, HTTP handlers, OPA client, audit logger
```

Rules of thumb:

- **Domain**: zero framework imports; deterministic logic; easiest to unit test.
- **Use cases**: orchestrate domain logic; talk only to interfaces/ports.
- **Integration**: defines contracts the outside world must follow.
- **Infrastructure**: the only place that knows PostGIS/Neo4j/search/object store specifics.

If your current repo layout differs, align the code to these boundaries or update this README to match reality.

</details>

### Treat pipelines as governed manufacturing

Pipelines are not “scripts.” They are the manufacturing line that produces publishable artifacts. The safe default is the connector pattern:

- discover → acquire → normalize → validate → enrich → publish

and publish means:

- promote to **Processed**
- update catalogs (DCAT/STAC/PROV as applicable)
- trigger index refresh (graph/search) when needed

---

## `src/pipelines/`

### Responsibilities

- Acquire source data into **Raw** (immutable, append-only capture).
- Transform and QA in **Work** (intermediate, repeatable).
- Publish governed artifacts to **Processed** (query-ready, cataloged, checksummed).
- Emit **run records** and **validation reports** so CI can enforce promotion gates.

### Definition of done for a pipeline change

- [ ] Inputs are versioned (content-addressable or checksum-manifested)
- [ ] Required validations are implemented and fail loudly
- [ ] Outputs are deterministic for the same inputs + code revision
- [ ] Catalogs are generated/updated as required (DCAT always; STAC/PROV as applicable)
- [ ] Policy labels are assigned and redaction is applied where required
- [ ] Tests exist: unit + integration slice + contract expectations

---

## `src/graph/`

### Responsibilities

- Build and update graph structures from **Processed** artifacts only.
- Enforce constraints that prevent “story-shaped” contradictions:
  - time validity
  - identity stability
  - provenance linkability
- Generate import/export artifacts and any post-import steps (if used).

### Common anti-patterns

- Building graph directly from `data/work/` intermediates
- Creating edges without preserving the source record IDs needed for evidence citations

---

## `src/server/`

### Responsibilities

`src/server/` is the **governed boundary**. It is where:

- authn/authz + policy checks run
- request shaping/redaction occurs
- audit/provenance logging is written
- evidence resolution endpoints live
- the UI and external clients interact with KFM

### Adding a new API capability

Use this checklist to keep changes reviewable and compliant:

- [ ] Add or update **domain** entity/value object and invariants if needed
- [ ] Implement a **use case** that expresses the workflow
- [ ] Define/extend a **port/contract** in `integration/`
- [ ] Implement the adapter in **infrastructure** (DB/graph/search/OPA/audit)
- [ ] Wire into the HTTP layer (routes/handlers)
- [ ] Add policy checks (default deny) for the new access pattern
- [ ] Ensure responses include provenance/citations and an `audit_ref`
- [ ] Add tests:
  - domain unit tests
  - use case tests with mocked ports
  - contract/schema tests
  - integration or smoke tests for the end-to-end path

---

## Testing expectations

| Area | Minimum tests expected |
|---|---|
| Domain | pure unit tests |
| Use cases | use-case tests with mocked ports |
| Integration | contract tests, schema tests |
| Infrastructure | integration tests + end-to-end smoke tests |

---

## Local development reminder

Use the repo’s documented compose workflow (see the top-level README and `docs/` runbooks):

```bash
cp .env.example .env
docker compose up --build
```

---

## References in this repo

- `docs/MASTER_GUIDE_v13.md` — canonical repo structure and documentation protocol
- `docs/architecture/` — architecture blueprints and ADRs
- `policy/` — OPA policies (default deny) and regression tests
- `schemas/` — schemas for story nodes, catalogs, and telemetry