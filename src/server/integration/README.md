# `src/server/integration` — Server Integration Layer

![Layer](https://img.shields.io/badge/layer-integration-blue)
![Governance](https://img.shields.io/badge/governance-trust--membrane%20%2B%20evidence--first-success)
![Policy](https://img.shields.io/badge/policy-OPA%20default--deny%20%2B%20fail--closed-critical)
![Tests](https://img.shields.io/badge/tests-contract%20%2B%20schema%20%2B%20policy%20regression-important)

This folder contains the **integration boundary** for the server: **ports/contracts**, **DTOs**, **schemas**, and **integration primitives** that connect KFM’s use-cases to external systems (storage, policy, catalogs, and data-source connectors) **without** pulling infrastructure concerns into business logic.

---

## ✅ Purpose

KFM’s system design is built around **clean layers** + a **trust membrane**. In practice, that means:

- **Use cases** must depend on **interfaces (ports)**, not on PostGIS/Neo4j/S3/HTTP clients directly.
- **Infrastructure** implements those ports.
- **All access crossing the trust membrane** (reads and writes) must go through **auth → policy evaluation → shaping/redaction → audit/provenance logging**, and this is **test-enforced**.

`src/server/integration` is where those stable contracts live.

---

## Scope

### ✅ What belongs here

| Category | Examples |
|---|---|
| **Ports / interfaces** | `DatasetRepository`, `PolicyClient`, `EvidenceResolverPort`, `CatalogWriterPort`, `ObjectStorePort`, etc. |
| **Contracts for connectors/adapters** | `DataSourceConnector` contract (discover → acquire → transform → validate → publish). |
| **DTOs / type definitions** | request/response payload shapes shared across layers (e.g., evidence bundles, manifests, policy input/output). |
| **Schemas** | JSON Schema / OpenAPI fragments / policy input schema, catalog schema validators, etc. |
| **Contract tests & golden files** (if your repo places them here) | tests asserting “this contract stays stable”. |

### ❌ What does NOT belong here

| Anti-goal | Put it elsewhere |
|---|---|
| Database drivers, ORMs, raw SQL | `src/server/infrastructure/...` |
| HTTP handlers / framework routes | `src/server/interfaces/...` (or equivalent) |
| Business rules / domain invariants | `src/server/domain/...` |
| Use-case orchestration | `src/server/usecases/...` |
| Secret loading, env parsing | Infrastructure/bootstrap layer |

> [!IMPORTANT]
> **Integration layer must be dependency-clean**: it may define contracts and schemas, but it must not “reach out” to the world.

---

## Non‑negotiables (KFM invariants)

> [!IMPORTANT]
> **Trust membrane**: Frontend/external clients never access databases directly; all reads/writes cross the API + policy boundary.

> [!IMPORTANT]
> **Fail‑closed governance**: If policy cannot be evaluated confidently, default to deny / redact / abstain.

> [!IMPORTANT]
> **Processed-only serving**: Only **Processed** data is queryable via the API; Raw/Work are not served to users.

> [!IMPORTANT]
> **Evidence-first**: All user-visible claims must have **traceable provenance** (dataset version + source_record_id + evidence bundle / resolver).

---

## Architecture placement

KFM is intentionally layered:

```mermaid
flowchart TB
  UI[UI / External Clients] -->|HTTP| API[Server Interfaces Layer<br/>Routes/Controllers]
  API -->|calls| UC[Use Cases / Services]
  UC -->|depends on| INT[Integration Layer<br/>Ports + Contracts + Schemas]
  INT -->|implemented by| INFRA[Infrastructure<br/>DB/Object Store/Search/OPA/HTTP Clients]

  API -->|authorize| OPA[Policy Engine (OPA)]
  API -->|audit| AUDIT[Audit/Provenance Sink]

  style INT fill:#dbeafe,stroke:#1d4ed8,stroke-width:2px
```

---

## Suggested folder layout

> [!NOTE]
> The exact tree may differ in your repo. Keep the **semantics** even if the names differ.

```text
src/server/integration/
├─ README.md                         # This file
├─ ports/                            # Pure interfaces/ports (no implementations)
│  ├─ DatasetRepository.*            # Data access contract
│  ├─ PolicyClient.*                 # OPA policy decision contract
│  ├─ EvidenceResolverPort.*         # Claim → evidence bundles
│  ├─ CatalogWriterPort.*            # DCAT/STAC/PROV emission contracts
│  └─ ObjectStorePort.*              # Blob/object storage contract
├─ connectors/                       # External data source integration contracts
│  ├─ DataSourceConnector.*          # The discover→acquire→transform→validate→publish contract
│  └─ registry/                      # Source registry config schema + types (location may vary)
├─ dto/                              # Shared payload types across layers
│  ├─ EvidenceBundle.*               # Canonical evidence packaging
│  ├─ RunManifest.*                  # Deterministic ingest manifests + checksums
│  ├─ DatasetVersionRef.*            # Stable refs to a published dataset version
│  └─ AuditEvent.*                   # What must be emitted to audit/provenance sinks
├─ schemas/                          # JSON Schema / validation definitions
│  ├─ policy_input.schema.json
│  ├─ manifest.schema.json
│  ├─ dcat_min.schema.json
│  ├─ stac_min.schema.json
│  └─ prov_min.schema.json
└─ contract-tests/                   # (Optional) tests enforcing contract stability
   ├─ api_contracts/                 # evidence resolution + redaction must hold
   └─ policy_regression/             # restricted fields must never leak
```

---

## Core contracts

### 1) Ports (examples)

These are the *minimum* kinds of ports expected for KFM server governance and evidence-first behavior:

| Port | Why it exists | Typical implementer |
|---|---|---|
| `DatasetRepository` | Use cases query dataset metadata + versions without knowing DB details | PostGIS/Neo4j adapter |
| `PolicyClient` | Standard interface for OPA checks (dataset access, redaction rules, aggregation thresholds) | OPA adapter |
| `EvidenceResolverPort` | Translates a “claim” into a canonical evidence bundle | Object store + catalog + search adapter |
| `CatalogWriterPort` | Emits schema-validated DCAT/STAC/PROV on promotion | Catalog layer adapter |
| `ObjectStorePort` | Raw/work/proc blobs + evidence bundles | S3/MinIO/FS adapter |
| `AuditSinkPort` | Append-only audit record emission | log sink / DB / object store adapter |

> [!TIP]
> Keep ports “small and boring.” Prefer many focused interfaces over one huge “God port.”

#### Example (Python-style) port definition

```python
# Example only — match your repo language
from typing import Protocol, Optional

class DatasetRepository(Protocol):
    def get_dataset(self, dataset_id: str) -> dict: ...
    def list_versions(self, dataset_id: str) -> list[dict]: ...
    def get_version(self, dataset_id: str, version_id: str) -> Optional[dict]: ...

class PolicyClient(Protocol):
    def authorize(self, input: dict) -> dict: ...
```

---

### 2) Connector contract (external data sources)

KFM ingestion is **connector-driven**. Each source is implemented as an adapter that conforms to a common contract:

**discover → acquire → transform → validate → publish**

```ts
// Canonical connector contract (language-agnostic concept)
interface DataSourceConnector {
  discover(ctx): Capabilities
  acquire(ctx, plan): RawManifest
  transform(ctx, manifest): WorkArtifacts
  validate(ctx, work): ValidationReport
  publish(ctx, work, report): DatasetVersionRef
}
```

#### Orchestration requirements

- Schedule connectors by cadence (real-time, daily, weekly, annual, static).
- Jobs must be **idempotent**: reruns never mutate a published DatasetVersion.
- Backfills are explicit runs with their own audit trail.
- Operational metadata must be recorded: run start/end, rows read/written, error counts, latency, freshness.

---

### 3) Registry-driven integrations (don’t let sources get “forgotten”)

All integrations must be tracked as **registry entries** (not ad-hoc scripts). Each registry entry should capture:

| Key | Rule of thumb |
|---|---|
| `schedule` | real-time / daily / weekly / annual / static |
| `incremental_cursor` | `modified_date` / `eventDate` / `publicationDate` when supported; otherwise snapshot+diff |
| `auth` | none (public) or OAuth/API key; secrets in vault; never committed |
| `rate_limit` | respect provider limits; exponential backoff; cache stable queries |
| `format_targets` | JSON/CSV (tabular), GeoJSON/Parquet (vectors), COG (rasters), PDF/JPEG/PNG (artifacts) |
| `policy_label` | `public` \| `restricted` \| `sensitive-location` (can vary per record) |

---

## Data zones & promotion gates (integration touchpoints)

Every dataset flows through three zones:

- **Raw (immutable)**: source-of-truth capture, append-only, checksums + raw manifest.
- **Work (normalize/enrich)**: repeatable transforms, QA staging, PROV activity, intermediate QA.
- **Processed (query-ready)**: read-optimized, indexed, governed API serving.

Promotion to Processed requires **machine-checkable** artifacts (and should be CI-enforced):

- Checksums for all raw assets (content-addressable)
- Schema validation passes; QA report stored with stable ID
- Policy labels attached (`public`/`restricted`/`sensitive-location`, etc.)
- Catalog writers succeed: DCAT/STAC/PROV well-formed and link-check clean
- API contract tests pass for queries depending on the dataset

---

## Canonical identifiers & time (what integration must preserve)

### Identifier rules (must not drift)

- Dataset IDs are **stable** (publisher + product + scope).
- DatasetVersion IDs are **content-addressed** (hash of raw manifest + metadata).
- All user-visible evidence citations reference **DatasetVersion + source_record_id(s)**.
- Places are time-valid (boundary vintages).
- Transformations always create new identifiers; never overwrite prior versions.

### Time model

- Use ISO-8601 timestamps with explicit time zones (or UTC).
- Uncertain time ranges are `[start, end]` intervals.
- For fuzzy historical sources (e.g., newspapers), store **publication date** and **event date claim** separately, each with its own provenance.

---

## Governed API touchpoints (contracts that integrations must support)

All downstream consumers use the governed API. The API is responsible for:

- policy evaluation
- evidence resolution
- query shaping/redaction
- audit logging

Typical endpoint families that depend on integration contracts:

| Endpoint family | Purpose | Key outputs |
|---|---|---|
| `/datasets`, `/catalog` | discover datasets/versions | dataset list, version refs, catalog URLs |
| `/map/tiles`, `/features` | rendering primitives from Processed | vector features, raster tiles |
| `/timeseries`, `/observations` | observations + aggregation | data + provenance |
| `/evidence/resolve` | claim → evidence packages | record IDs, snippets, media, provenance chain |
| `/focus/query` | evidence-first Q&A | answer + citations **or abstain** + audit ref |

---

## Policy-as-code integration points (OPA)

OPA policy checks typically cover:

- dataset/version access (public vs restricted)
- field-level redaction (ownership names, sensitive coordinates)
- aggregation thresholds (avoid re-identification)
- derivative publication rules (public summaries vs restricted raw)
- audit requirements (every response has audit ref + evidence bundle hash)

> [!WARNING]
> If you’re adding a new port/DTO that influences access control or evidence exposure, treat it as a **governed contract change** (see “Change management”).

---

## Evidence addressing & resolver contracts

KFM evidence must be reliably resolvable and stable. The integration layer should define:

- a canonical “evidence bundle” structure (bundle hash, artifacts, snippets, provenance chain)
- an addressing scheme that can be used in citations
- a resolver contract (e.g., “given a digest, return the bundle + metadata”)

**Recommended pattern** (conceptual):

1. content-address evidence bundles (e.g., digest)
2. stable gateway URL derived from digest
3. storage URL remains implementation detail

---

## Reliability requirements for integrations

### Determinism & idempotency

Integration outputs must be deterministic:

- Same input slice + same connector version + same rules → same checksums & manifests
- Avoid embedding “now()” or unstable fields in checksummed artifacts
- Use stable canonical serialization for hashing (see `spec_hash` style patterns if present in your repo)

### Incremental updates

Prefer conditional/incremental fetch where available:

- use provider cursors (modified date / publication date / event date)
- use HTTP conditional requests (`ETag`, `If-Modified-Since`) when supported
- fall back to snapshot+diff if no incremental support

### Rate limits and backoff

- Respect upstream provider limits
- Exponential backoff with jitter
- Cache stable query responses where safe

---

## Observability (integration must emit the right signals)

Every integration run should emit (at minimum):

- `run_id`
- `dataset_id`, `dataset_version_id`
- start/end timestamps
- rows/bytes read & written
- error counts
- freshness/lag (source timestamp vs ingest timestamp)
- evidence bundle digest(s) produced (if applicable)

> [!TIP]
> Emit these via structured logs + metrics + traces so ops can correlate “a user query” back to “what ingest run produced the evidence.”

---

## Testing & CI gates

### Minimum test plan

- **Unit**: schema mapping, type coercion, geometry validity helpers, incremental window logic
- **Integration**: run connector against a fixed small slice; assert stable checksums + counts
- **Contract**: verify API responses include provenance bundle and respect policy redaction
- **Regression**: profiling metrics stable (null rates, min/max, distinct keys) or explainably versioned

### Definition of Done (integration ticket)

- [ ] Connector implemented and registered in the data-source registry config
- [ ] Raw acquisition produces deterministic manifest + checksums
- [ ] Normalization emits canonical schema and/or STAC assets
- [ ] Validation gates implemented and enforced in CI
- [ ] Policy labels defined; restricted fields/locations redacted per rules
- [ ] Catalogs emitted (DCAT always; STAC/PROV as applicable) and link-check clean
- [ ] API contract tests pass for at least one representative query
- [ ] Backfill strategy documented (historical ranges + expected runtime)

---

## How to add a new integration (step-by-step)

> [!TIP]
> Treat every new source as a **governed deliverable**, not a “script.”

1. **Create/extend registry entry**
   - capture schedule, auth needs, cursor semantics, formats, policy_label.
2. **Define mapping + schemas**
   - canonical types, required fields, geometry/time normalization rules.
3. **Implement connector adapter**
   - conform to `DataSourceConnector`.
4. **Implement validation gates**
   - schema, geometry, time sanity, license/policy checks, provenance completeness.
5. **Emit catalogs**
   - DCAT always; STAC/PROV where applicable.
6. **Wire promotion gates**
   - CI blocks promotion if catalogs invalid or policy regression fails.
7. **Add contract tests**
   - evidence resolution and redaction behavior must be enforced.
8. **Document backfill strategy**
   - define historic coverage + batching strategy; ensure new DatasetVersions (never overwrite).

<details>
<summary><strong>Quick checklist template (copy into your PR)</strong></summary>

- [ ] Registry entry added/updated
- [ ] Connector implements DataSourceConnector
- [ ] Deterministic RawManifest + checksums
- [ ] Canonical mapping documented (fields, types, units, CRS/time)
- [ ] Validation gates + QA artifact
- [ ] Policy labels + redaction rules + regression tests
- [ ] DCAT/STAC/PROV emitters + link-check
- [ ] Evidence resolver returns bundle for representative record(s)
- [ ] API contract tests updated
- [ ] Backfill plan documented + safe to rerun

</details>

---

## Change management (contracts are governed)

When modifying any of the following, treat it as a governed change:

- any port interface signature
- DTOs used in API responses
- evidence bundle schema
- policy input/output schema
- catalog templates and required fields

Recommended approach:

1. Add fields in a backward-compatible way.
2. Mark old fields as deprecated (with an explicit reason and migration guidance).
3. Add/adjust contract tests.
4. Update versioned API docs if needed.
5. Remove only after an agreed deprecation window.

---

## Anti‑patterns (do not merge)

- ❌ Integration code that reaches into PostGIS/Neo4j/S3 directly
- ❌ Returning Raw/Work artifacts to clients “just for convenience”
- ❌ “Policy check optional” endpoints
- ❌ Non-deterministic hashing / manifests
- ❌ Silent entity merges (no confidence tracking, no provenance)
- ❌ Missing `source_record_id` on evidence citations
- ❌ Storing secrets in repo or logs

---

## Glossary (KFM terms used here)

- **Trust membrane**: boundary where auth + policy + shaping/redaction + audit/provenance must occur.
- **Raw/Work/Processed**: data zones for immutable capture → repeatable transforms → query-ready governed serving.
- **Dataset / DatasetVersion**: governed source + content-addressed version.
- **Evidence bundle**: canonical package for “show your work” (records/snippets/media/provenance chain).
- **Promotion gate**: CI-enforced rules preventing unsafe/incomplete publication.
- **Focus Mode**: evidence-first narrative interface; must cite or abstain.

---

## References (internal + standards)

- KFM Next-Gen Blueprint (clean layers, trust membrane, policy scaffolding, audit, evidence resolver)
- KFM Data Source Integration Blueprint (connector contract, data zones, promotion gates, catalogs)
- Standards commonly referenced:
  - DCAT (catalog metadata)
  - STAC (spatiotemporal asset catalog)
  - W3C PROV (provenance)
  - ISO-8601 (time)

