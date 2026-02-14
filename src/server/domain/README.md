# Domain Layer (src/server/domain)

**🧠 Layer:** Domain • **✅ Purity:** deterministic + no I/O • **🧪 Tests:** pure unit tests • **🧾 Governance:** evidence-first & provenance-first

This directory holds the **inner core** of the KFM backend: the domain model (entities + value objects), invariants, and domain events.
If you’re changing code here, you are changing **what things *are*** and **what must always be true**, independent of storage, APIs, or UI.

> [!IMPORTANT]
> **No I/O in Domain.** No database calls, HTTP, filesystem, policy engine calls, env/config parsing, logging/metrics, schedulers, or network clients.
> If your change needs any of those, move it to a higher layer and keep Domain pure.

---

## Table of Contents

- [Architecture Contract](#architecture-contract)
- [What Lives Here](#what-lives-here)
- [What Must Not Live Here](#what-must-not-live-here)
- [Directory Layout](#directory-layout)
- [Core Domain Concepts](#core-domain-concepts)
- [Cross-Cutting Invariants](#cross-cutting-invariants)
- [Design and Modeling Guidelines](#design-and-modeling-guidelines)
- [Testing Strategy](#testing-strategy)
- [PR Checklist](#pr-checklist)
- [Glossary](#glossary)
- [References](#references)

---

## Architecture Contract

KFM is implemented using **clean layers**. This folder is the **innermost** layer.

```mermaid
flowchart TB
  %% Outer systems
  UI[Web UI] --> API[API Gateway / Controllers]
  API --> PDP[Policy PDP (OPA/Rego)]
  API --> AUDIT[Audit Ledger]

  %% Backend clean layers
  API --> UC[Use Cases]
  UC --> D[Domain]
  API --> INFRA[Infrastructure Adapters]
  INFRA --> PORTS[Interfaces / Ports]
  PORTS --> D

  %% Key note
  %% Domain MUST NOT depend on UC/PORTS/INFRA/API/PDP.
```

### Layer responsibilities (quick map)

| Layer | What belongs there | Test focus |
|---|---|---|
| **Domain** | Entities, value objects, invariants, domain events, pure domain services | **Pure unit tests** |
| **Use Cases** | Workflows + business rules (promotion, evidence resolution, story build, query flows) | Use-case tests w/ mocked ports |
| **Interfaces / Ports** | Repository interfaces, adapter contracts, DTOs, schemas/contracts | Contract + schema tests |
| **Infrastructure** | DB clients, API handlers, OPA adapters, search/graph adapters, queues | Integration + end-to-end tests |

> [!IMPORTANT]
> The **trust membrane** (authn/authz, policy evaluation, redaction, audit/provenance logging) is enforced **outside** Domain.
> Domain supports this by making provenance/evidence/sensitivity representable, but Domain does **not** evaluate policy.

---

## What Lives Here

- **Entities**: identity-bearing concepts (e.g., `Dataset`, `DatasetVersion`, `Place`, `Event`, `Observation`, `Artifact`)
- **Value Objects**: immutable meaning-carrying types (e.g., `TimeRange`, `Geometry`, `BBox`, `EvidenceRef`, `AuditRef`, `LicenseRef`)
- **Invariants / guards**: validation rules and constructors/factories that prevent invalid states
- **Domain services**: pure functions for rules that don’t fit a single entity
- **Domain events**: immutable “something happened” facts (pure data)

---

## What Must Not Live Here

- Storage concerns: ORM models, SQL queries, PostGIS/Neo4j specifics, migration logic
- API concerns: HTTP handlers, request/response DTOs, GraphQL resolvers, status codes
- Policy execution: OPA clients, auth token parsing, permission checks
- Runtime wiring: dependency injection, config, env vars, secrets, service discovery
- Operational side-effects: logging, metrics, tracing, queues, cron/schedulers

---

## Directory Layout

> This is a **recommended** structure. If the repo differs, update this README to match the real tree.

```text
src/server/domain/
├── README.md
├── entities/               # Identity-bearing domain entities (Place, Event, Dataset, …)
├── value-objects/          # Immutable types (IDs, time, geometry, evidence, …)
├── events/                 # Domain events (pure data)
├── services/               # Pure domain services (no I/O)
├── errors/                 # Domain error types (stable & serializable)
├── invariants/             # Guards/validators shared across domain types
└── index.*                 # Public exports for this layer
```

<details>
<summary>Why this structure?</summary>

- **Entities vs value-objects** keeps modeling crisp and avoids “god objects.”
- **Events** let downstream layers react without injecting side effects into Domain.
- **Errors** standardize failure modes so Use Cases can map errors to policy/audit/API behavior.

</details>

---

## Core Domain Concepts

KFM’s engineered integration blueprint explicitly names a starting set of canonical entities:

- `Place`
- `Event`
- `Observation`
- `Artifact`
- `Dataset`
- `DatasetVersion`

…and calls out invariants including **time validity** and **provenance requirements**.

### Entities (canonical starting set)

| Entity | Represents | Typical invariants (non-exhaustive) |
|---|---|---|
| `Dataset` | A governed dataset concept (“NOAA NCEI”, “Kansas Mesonet”, “NHGIS”, …) | `dataset_id` present; license/rights present; policy label present |
| `DatasetVersion` | An immutable version of a dataset (unit of evidence) | stable `dataset_version_id`; provenance/run refs present; checksums present (when promoted) |
| `Artifact` | Evidence object (PDF, scan, GeoTIFF/COG, Parquet, …) | stable URI; media type known; checksum known (when promoted) |
| `Place` | Location (point/line/polygon) + metadata | geometry valid; CRS explicit; uncertainty representable |
| `Event` | Something happening over time (and often space) | `time_range` valid; optional geometry valid; type taxonomy stable |
| `Observation` | Measured/observed fact tied to time/place/dataset | evidence refs resolvable to dataset version + record(s) |

### Value objects (cross-cutting)

| Value object | Purpose | Notes |
|---|---|---|
| `*Id` (e.g., `DatasetId`, `EventId`) | Stable identity | Prefer opaque strings; do not bake infrastructure semantics into IDs |
| `TimeInstant` / `TimeRange` | Temporal modeling | Prefer ISO 8601 at boundaries; preserve timezone or UTC |
| `Geometry` / `BBox` | Spatial modeling | Prefer canonical WGS84 representation; validate polygons |
| `LicenseRef` / `Rights` | Legal metadata | Encodes license + attribution requirements |
| `SensitivityLabel` / `PolicyLabel` | Sensitivity + access class | Drives redaction and policy checks outside Domain |
| `EvidenceRef` | “This claim came from *this* dataset version and *these* record(s)” | Must be resolvable by evidence APIs |
| `AuditRef` | Reference to an audit ledger entry | Returned to UI/Focus Mode as part of evidence UX |

### Dataset versioning and evidence identifiers

Domain should make it *possible* (and easy) for higher layers to enforce deterministic identity and evidence:

- `DatasetVersion` is the **unit of evidence**: it represents a specific, immutable slice/run/version.
- A version identifier is typically implemented as a **content hash** of an immutable manifest (implementation detail in pipelines/use-cases).
- `source_record_id` must be **stable per upstream semantics** and is used in citations/evidence references.
- Record-level sensitivity can require **per-record policy labels** (e.g., `public`, `restricted`, `sensitive-location`).
- Event time modeling must support start/end ranges and preserve a timezone or UTC when provided.

---

## Cross-Cutting Invariants

### Evidence-first invariants (system contract support)

> [!IMPORTANT]
> **Evidence-first** is not a slogan. Domain should make it hard to represent user-visible claims without evidence.

Recommended domain rules:

- Every entity that can become **user-visible** should carry `evidence: EvidenceRef[]` (or an equivalent pattern).
- `EvidenceRef` should include the minimum to resolve:
  - `dataset_id`
  - `dataset_version_id` (or digest)
  - `source_record_id` (and/or stable locators: row/field, geometry id, page/span, etc.)

### Temporal invariants

- `TimeRange.start <= TimeRange.end`
- Historic datasets should not produce “future” times unless explicitly modeled as forecasts.
- Durations cannot be negative.

### Spatial invariants

- Geometry validity matters (e.g., polygons not self-intersecting).
- Canonical spatial representation should support interoperable delivery and validation.
- Sensitive-location modeling must support **generalization** and/or **uncertainty** (do not force high precision into the model).

### Licensing and rights invariants

- `Dataset` and `DatasetVersion` must carry rights metadata, even if “unknown” (unknown should be treated as **restricted** by policy).
- Attribution requirements must be representable (so UI/Focus Mode can cite correctly).

### Sensitivity and redaction invariants

- Every dataset/version (and sometimes record) must carry a `policy_label`.
- The model must support “sensitive location” handling (e.g., generalized geometry, withheld coordinates, or uncertainty envelopes).
- Redaction is applied outside Domain, but Domain must represent the **intent** and **classification**.

---

## Design and Modeling Guidelines

### 1) Constructors must enforce invariants

Prefer constructors/factories that **cannot create invalid objects**.

```ts
// Example (TypeScript for readability; adapt to your server language)
export class TimeRange {
  private constructor(
    readonly startIso: string,
    readonly endIso: string,
  ) {}

  static create(startIso: string, endIso: string): TimeRange {
    if (startIso > endIso) {
      throw new DomainError("InvalidTimeRange", { startIso, endIso });
    }
    return new TimeRange(startIso, endIso);
  }
}
```

### 2) Keep Domain types serializable

- Domain objects should round-trip to plain data structures without hidden state.
- Avoid embedding functions, live handles, or framework objects.

### 3) Prefer explicit errors over runtime exceptions (recommended)

- Use `Result<T, DomainError>` / `Either` / explicit error returns (depending on language conventions).
- Domain errors must be **stable** and map cleanly to API/policy behavior.

### 4) Canonical encodings for interoperability

When Domain accepts boundary-crossing values, prefer canonical forms:

- **Text:** UTF-8
- **Time:** ISO 8601
- **Geometry:** WGS84 (or explicitly modeled CRS + transformation outside Domain)

### 5) Enforce import boundaries (recommended)

Keep the boundary “honest” with tooling. Examples:

- **ESLint**: `no-restricted-imports` preventing Domain from importing `../usecases`, `../infrastructure`, `../adapters`, etc.
- **TypeScript project references** (or language equivalent): compile Domain as a separate unit.
- **Architecture tests** (optional): a test that asserts no forbidden imports.

<details>
<summary>Example ESLint boundary rule (illustrative)</summary>

```js
// .eslintrc.js (illustrative; adapt to your repo)
module.exports = {
  rules: {
    "no-restricted-imports": [
      "error",
      {
        patterns: [
          {
            group: [
              "**/src/server/usecases/**",
              "**/src/server/infrastructure/**",
              "**/src/server/adapters/**",
              "**/src/server/interfaces/**",
            ],
            message: "Domain must not import from outer layers.",
          },
        ],
      },
    ],
  },
};
```

</details>

---

## Testing Strategy

Domain tests are **pure unit tests**.

Recommended test categories:

- **Invariant tests:** constructors reject invalid inputs (time ranges, geometry).
- **Serialization tests:** domain objects serialize/deserialize without loss.
- **Edge-case tests:** time boundaries, empty evidence arrays (should be invalid if required), invalid CRS/geometry.

---

## PR Checklist

- [ ] No I/O added (DB/HTTP/fs/OPA/logging/etc.)
- [ ] No new dependencies without strong justification
- [ ] New/changed entities enforce invariants via constructors/factories
- [ ] New/changed domain logic has unit tests
- [ ] Evidence/provenance requirements remain representable and resolvable
- [ ] Sensitivity/policy label implications reviewed (especially for location precision)
- [ ] Public exports updated (`index.*`), if applicable
- [ ] If domain types changed, validate impacted contracts in outer layers (ports/DTOs/schemas)

---

## Glossary

- **Entity:** Identity-bearing domain object (persists across time even if attributes change).
- **Value object:** Immutable meaning-carrying type defined by its value (TimeRange, Geometry).
- **Invariant:** Rule that must always hold for a valid domain state.
- **EvidenceRef:** Pointer to dataset version + record(s) supporting a claim.
- **Trust membrane:** Governed boundary where policy, redaction, and audit are enforced.

---

## References

- **KFM Next-Gen Blueprint & Primary Guide (2026-02-12)** — trust membrane + clean layers + cite-or-abstain.
- **KFM Data Source Integration Blueprint (2026-02-12)** — canonical entities + time validity + provenance requirements.

