# KFM Server

This directory is the canonical home for the **KFM API layer**.

The API layer is the **contracted access boundary** between KFM back-end systems (catalogs + graph) and
front-end or external consumers. It should remain stable, versioned, and test-protected.

> Note: This README intentionally contains **no YAML front-matter**. Repo lint rules for v13 readiness
> enforce “no YAML front-matter in code files”.

---

## 📘 Overview

### Purpose

- Provide a **controlled, versioned contract** for accessing KFM data and derived products.
- Mediate access to:
  - **Catalogs** (STAC / DCAT / PROV)
  - **Graph** (Neo4j) via server-side queries
- Enforce **governance rules** at the API boundary (security, redaction/generalization, provenance).

### Where this fits in the pipeline

KFM’s canonical pipeline ordering is:

~~~text
ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode
~~~

This server implements the **APIs** stage.

---

## 🧭 Key invariants

These are non-negotiable expectations for API behavior:

- **Contract-first:** REST/GraphQL contracts are treated as versioned interfaces. Changes must not
  silently break clients.
- **Provenance-first:** if an API response will be used for Story Nodes / Focus Mode, it must include
  the identifiers needed to trace claims back to underlying evidence (e.g., asset/dataset/run IDs).
- **Sensitive data handling:** apply redaction/generalization rules server-side (not in the UI).
- **Determinism support:** endpoints that expose pipeline outputs should be consistent with the
  deterministic/idempotent nature of upstream ETL and catalog generation.

---

## 🗂️ Directory layout

### This directory

- `src/server/` is the canonical location for the API layer implementation and API schemas.

### Suggested structure

Actual structure may vary; treat this as the preferred convention:

~~~text
📁 src/server/
├── 📄 README.md
├── 📁 contracts/                 # API contracts (OpenAPI + GraphQL)
│   ├── 📄 openapi.yaml            # REST contract (example name)
│   └── 📄 schema.graphql          # GraphQL contract (example name)
├── 📁 src/                        # Server implementation (handlers/resolvers/middleware)
├── 📁 adapters/                   # External system adapters (graph, catalogs, storage)
└── 📁 tests/                      # Contract + integration tests (or use top-level tests/)
~~~

---

## 📜 Contracts

KFM treats API definitions as **versioned contracts**.

- REST is documented via **OpenAPI** (YAML or JSON).
- GraphQL is defined via a **GraphQL schema**.

**When adding or changing an endpoint:**
1. Update the contract (OpenAPI / GraphQL schema) first or alongside code.
2. Implement the handler/resolver to match the contract exactly.
3. Add/adjust tests so CI can detect contract drift.
4. Update human-readable API docs under `docs/api/` if present.

---

## 🔐 Security, sensitivity, and redaction

The API layer is responsible for enforcing policy-related behavior, including (as applicable):

- authentication and authorization
- redaction of restricted fields
- generalization (coarsening) of sensitive locations or attributes
- audit/log hooks (if implemented in this repo)

Do **not** rely on the front-end to “hide” sensitive information—ensure restricted data never reaches
unauthorized clients.

---

## 🧠 Story Node and Focus Mode integration

If an endpoint feeds Story Nodes or Focus Mode experiences, the response should be designed to:

- include **provenance references** sufficient to trace narrative claims to evidence artifacts
- support “data-derived vs inferred” separation where AI-generated text or predictions are used
- avoid surfacing uncited narrative statements

---

## 🧪 Validation and CI expectations

The v13 readiness CI mapping calls out these minimum gates (where applicable):

- API contract tests
- schema validation
- security and sovereignty scanning gates
- markdown protocol validation (for governed docs under `docs/`)

For API work, expect to run:
- contract validation (OpenAPI / GraphQL schema lint)
- unit + integration tests
- (optional) snapshot/fixture tests to prevent silent response drift

---

## 🧰 Local development

Local commands are **repo-specific** and not defined in the provided materials.

Use the repo’s canonical developer entrypoints (often top-level docs/scripts). If none exist yet,
consider adding a minimal runbook under `docs/` and linking it here.

---

## 🧭 Troubleshooting checklist

- Contract mismatch: does the response shape still match OpenAPI/GraphQL?
- Provenance missing: does the payload include the evidence IDs required for UI / Focus Mode?
- Sensitive leak: are redaction/generalization rules being applied server-side?
- Breaking change: did you bump the API version or deprecate fields safely?

---

## 📎 References in this repo

- Master pipeline + invariants: `docs/MASTER_GUIDE_v12.md`
- API change proposals: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Versioning expectations: `docs/api/` (if present) and contract specs under `src/server/`
~~~
