# KFM API

> **Kansas Frontier Matrix (KFM) — Unified API Gateway**  
> FastAPI-backed **REST** (versioned + OpenAPI) + optional **GraphQL**, enforcing KFM’s **trust membrane**, **policy-as-code**, and **provenance-first** governance.

![API](https://img.shields.io/badge/API-REST%20%2B%20GraphQL%20(optional)-informational)
![Contract](https://img.shields.io/badge/Contract-OpenAPI%20(enforced)-blue)
![Governance](https://img.shields.io/badge/Governance-Policy%20%2B%20Provenance-critical)
![Trust](https://img.shields.io/badge/Rule-Trust%20Membrane-critical)
![Policy](https://img.shields.io/badge/Policy-OPA%20%2F%20Rego-9cf)
![Provenance](https://img.shields.io/badge/Provenance-PROV%20%2B%20Catalogs-success)

---

## 📌 Document Metadata

| Field | Value |
|---|---|
| Artifact | `api/README.md` *(legacy location; v13+ canonical homes are typically `docs/` (API docs) + `src/server/` (API code) — see “Repo layout”)* |
| Audience | Backend / full-stack contributors |
| Status | Draft (**project-doc grounded**; remaining repo-specific unknowns are marked) |
| Governance | Governed doc — align with `docs/MASTER_GUIDE_v13.md`, `docs/standards/*`, `docs/templates/*` |
| Sensitivity | Public by default **unless** policy marks endpoints/datasets as restricted |
| Key principle | **No client or UI talks to databases directly** — all access is mediated by this API gateway |

> [!IMPORTANT]
> If you see “(verify in repo)”, it’s an intentional uncertainty marker. Replace only after checking code/config (`docker-compose.yml`, `.env`, routers, schema files, policy bundle).

---

## ✅ Non‑Negotiable Invariants

> [!WARNING]
> These are governance + architecture invariants (not “style preferences”).

### 1) Trust membrane (API is the only ingress to data stores)

- **UI / external clients** must never query PostGIS / Neo4j / search indexes directly.
- Backend **route handlers** must never contain business rules or embed direct SQL/Cypher.
- Core logic must use repository **ports/interfaces**; infrastructure implements adapters.

### 2) Canonical pipeline ordering (data → narrative)

KFM’s ordering is absolute:

**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**.

### 3) Contract‑first API (OpenAPI is enforced)

- Schemas + API contracts are **first-class artifacts**.
- Breaking changes require a **version bump** and compatibility checks (OpenAPI/GraphQL + contract tests).

### 4) Classification propagation

Sensitive data **must not become less restricted downstream** (including AI summaries, story nodes, derived layers, exports).

---

## 🧭 What This API Is

KFM’s backend API is a **single, unified gateway** for all clients:

- Web UI (`web/`, React + MapLibre)
- External scripts / researchers
- Internal tooling (pipelines, validators)
- Focus Mode (governed AI/Q&A)

The gateway hides internal complexity (PostGIS, Neo4j, search, AI), while enforcing:

- authentication/authorization (when enabled)
- policy checks (request + response)
- validation and consistent contracts
- provenance + audit logging for high-impact outputs

> [!TIP]
> Think “**trust gate**”: clients call the API; the API orchestrates internal services; responses come back policy-checked.

---

## 🧱 Architecture Boundaries

KFM follows layered clean architecture. The FastAPI gateway is an **outer interface/adaptor** and must not contain business rules.

### Layer responsibilities at a glance

| Layer | What belongs here | Must NOT depend on |
|---|---|---|
| Domain | Pure entities + domain rules | FastAPI, DB drivers, UI |
| Use Case / Service | Workflows, orchestration, policy/provenance hooks | Concrete DB implementations, web framework |
| Integration / Interface | Repository interfaces, ports, adapter contracts | Concrete infra |
| Infrastructure | PostGIS/Neo4j/search implementations, FastAPI wiring, deployment | — |

### Request flow

```mermaid
flowchart LR
  Client[Client: UI / External Script] -->|REST / GraphQL| API[FastAPI Gateway]

  API --> Auth[AuthN/AuthZ (if enabled)]
  Auth --> Policy[Policy Engine (OPA / policy-as-code)]
  Policy --> Routes[Routes / Controllers]

  Routes --> UseCases[Use Case / Services]
  UseCases --> Ports[Repo Interfaces / Ports]

  Ports --> PostGIS[(PostGIS)]
  Ports --> Neo4j[(Neo4j)]
  Ports --> Search[(Search Index)]

  UseCases --> Prov[Provenance/Audit Logging]
  UseCases -->|optional| AI[Focus Mode AI Service]

  Prov --> Routes
  AI --> Policy
  Routes --> API --> Client