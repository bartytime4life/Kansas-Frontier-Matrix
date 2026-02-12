# 🔎 KFM Search Adapter

![Layer](https://img.shields.io/badge/layer-adapter-informational)
![Scope](https://img.shields.io/badge/scope-search%20%2B%20retrieval-blue)
![Governance](https://img.shields.io/badge/governed-yes-brightgreen)
![Trust%20Membrane](https://img.shields.io/badge/trust%20membrane-enforced-critical)

This directory contains the **Search Adapter(s)** for Kansas Frontier Matrix (KFM): code that integrates the **Use Case / Service layer** with a **search index** (commonly OpenSearch/Elasticsearch) for full-text and semantic retrieval.

> [!IMPORTANT]
> **Trust membrane invariant:** the UI never talks to search infrastructure directly. All client access goes through the governed API boundary, where validation + policy enforcement live.

---

## ✅ What this adapter is responsible for

**Adapter responsibilities (do):**
- Translate a **domain-level** `SearchQuery` into the backend’s query DSL (OpenSearch/Elasticsearch).
- Execute the query with **conservative guardrails** (timeouts, max page size, fail-closed behavior).
- Normalize results into a stable `SearchResult` shape (hits, scores, highlights, facets).
- Return enough metadata for **provenance-first** downstream behaviors (e.g., citations / evidence links).

**Non-responsibilities (do not):**
- Enforce authorization rules (that belongs to policy enforcement at the API/use-case boundary).
- Contain domain entities/models (those belong in the Domain layer).
- Bypass repository/port interfaces to call infrastructure directly.

> [!NOTE]
> Keep the adapter intentionally “dumb”: transform/execute/normalize. Governance checks should be upstream, but the adapter must still be defensive (rate limits, caps, “fail closed”).

---

## 🧱 Architecture placement

```mermaid
flowchart LR
  UI["Frontend UI (React/MapLibre)"] --> API["Governed API Boundary (REST/GraphQL)"]
  API --> POLICY["Policy Engine (OPA / policy-as-code)"]
  POLICY --> UC["Use Case: Search / Retrieval"]
  UC --> PORT["Port/Interface: SearchPort"]
  PORT --> ADAPTER["Adapter: OpenSearch/Elasticsearch"]
  ADAPTER --> INDEX["Search Index (Text + Vector)"]
```

### Layering rules (enforced by convention + CI)
- **Domain layer**: pure types/entities (no HTTP clients, no OpenSearch SDKs).
- **Use Case layer**: workflows and orchestration; calls only abstract ports.
- **Adapter layer (this folder)**: implements ports; owns translation to/from infrastructure.
- **Infrastructure**: concrete clients, connection pools, TLS/auth, container wiring.

---

## 📜 Contract-first: the Search Port

> [!TIP]
> If you’re adding or changing behavior, start by updating the **port contract** (types + tests), not the OpenSearch query JSON.

### Minimal port (suggested shape)

```python
from dataclasses import dataclass
from typing import Any, Mapping, Sequence, Protocol, Optional

@dataclass(frozen=True)
class SearchQuery:
    text: str
    limit: int = 20
    offset: int = 0
    filters: Mapping[str, Any] = None
    # Optional: vector / hybrid retrieval
    embedding: Optional[Sequence[float]] = None
    embedding_field: Optional[str] = None

@dataclass(frozen=True)
class SearchHit:
    id: str
    kind: str
    score: float
    title: Optional[str] = None
    snippet: Optional[str] = None
    # Required for provenance-first behaviors:
    provenance_refs: Sequence[str] = ()

@dataclass(frozen=True)
class SearchResult:
    hits: Sequence[SearchHit]
    total: int
    took_ms: Optional[int] = None

class SearchPort(Protocol):
    def search(self, q: SearchQuery, *, request_id: str, actor: str) -> SearchResult:
        """Execute a governed search request."""
```

> [!WARNING]
> The exact types/names in your repo may differ. **Do not** treat the above as authoritative unless the repo already defines it.
> This README describes **intent + invariants**, and provides a contract shape that aligns with KFM’s clean architecture.

---

## 🗂️ Indexed document model (recommended)

To support “provenance-first” retrieval, each indexed document should carry **stable identifiers** and **evidence pointers**.

| Field | Type | Why it exists |
|---|---:|---|
| `id` | string | Stable internal ID (used for hydration via DB/API) |
| `kind` | string | Document class (`dataset`, `story_node`, `feature`, etc.) |
| `title` | string | UI display + boosted relevance |
| `body` | string | Full-text search |
| `tags` | string[] | Facets + policy labeling |
| `time_range` | object | Temporal filtering (year/epoch ranges) |
| `bbox` | object | Spatial filtering (map bounds / region queries) |
| `provenance_refs` | string[] | Citation pointers (STAC/DCAT/PROV IDs, story IDs, etc.) |
| `sensitivity` | string | Policy gating + redaction tier (`public`, `restricted`, `sensitive`) |

---

## 🔍 Query semantics

### 1) Keyword search (full-text)
- Use `multi_match` over `title`, `body`, and curated fields.
- Prefer query-time boosts over field duplication.

### 2) Filters (structured)
Common filters include:
- `kind in [...]`
- tag constraints
- time range overlaps
- spatial intersection / bbox

### 3) Vector / hybrid retrieval (Focus Mode ready)
- Optional `embedding` in the query enables vector similarity.
- Hybrid retrieval merges text + vector results (with a stable merge strategy and caps).

<details>
<summary><strong>Example (illustrative) OpenSearch-style query DSL</strong></summary>

```json
{
  "size": 20,
  "from": 0,
  "query": {
    "bool": {
      "must": [
        { "multi_match": { "query": "railroad", "fields": ["title^3", "body"] } }
      ],
      "filter": [
        { "terms": { "kind": ["story_node", "dataset"] } }
      ]
    }
  },
  "highlight": {
    "fields": { "body": {} }
  }
}
```

```json
{
  "size": 10,
  "query": {
    "knn": {
      "embedding": {
        "vector": [0.1, 0.2, 0.3],
        "k": 10
      }
    }
  }
}
```

</details>

> [!IMPORTANT]
> If vector search is enabled, treat it as a **derived cache**: it must be rebuildable from `data/processed` + catalog artifacts, and must never become the source-of-truth.

---

## ⚙️ Configuration

> [!NOTE]
> Names below are **recommended**. If your repo already defines environment keys, follow the repo.

| Env var | Example | Notes |
|---|---|---|
| `SEARCH_BACKEND` | `opensearch` | Allows swap to `mock` in tests |
| `OPENSEARCH_URL` | `https://opensearch:9200` | Use TLS in non-dev |
| `OPENSEARCH_USERNAME` | `kfm_search` | Least-privileged service account |
| `OPENSEARCH_PASSWORD` | `********` | Never commit; use secrets |
| `OPENSEARCH_INDEX` | `kfm-main` | Prefer alias-based versioning (`kfm-main -> kfm-main-v3`) |
| `SEARCH_TIMEOUT_MS` | `1500` | Fail fast; callers can retry |
| `SEARCH_MAX_LIMIT` | `100` | Cap to prevent abuse |

---

## 🧪 Local development

### If using docker-compose
- Ensure the search index service is part of the dev stack (or available externally).
- Validate that the API can reach it (network + TLS settings).

**Quick smoke checks**
- Search health endpoint (if implemented): `GET /health/search`
- Search endpoint (if implemented): `GET /search?q=railroad`

> [!TIP]
> If the UI “search” feature is slow, measure:
> 1) index latency (`took_ms`)
> 2) API overhead (serialization/policy)
> 3) UI render time

---

## 🧾 Observability & audit

Minimum logging fields (structured logs recommended):
- `request_id` (propagate from API boundary)
- `actor` (system/user/service)
- `query_kind` (`text`, `vector`, `hybrid`)
- `limit`, `offset`
- `policy_decision_id` (link to OPA eval) when applicable
- `took_ms`

> [!WARNING]
> Do **not** log raw queries or embeddings if they may contain sensitive user content. Prefer hashed/length-only telemetry.

---

## 🔐 Security notes

- Use TLS to the search backend outside local dev.
- Apply least-privilege credentials (read-only for query adapters; separate writer identity for indexers).
- Enforce:
  - request caps (`SEARCH_MAX_LIMIT`)
  - timeouts (`SEARCH_TIMEOUT_MS`)
  - allowlisted fields for filters/sorts (avoid query-injection-by-DSL)

---

## ⚖️ Governance & FAIR/CARE alignment

This adapter is part of the platform’s governed runtime surface:
- It must support **provenance-first retrieval** (return `provenance_refs` so answers can be cited).
- It must support **sensitivity-aware** access patterns (filter or redact restricted docs).
- It must “fail closed” when required policy context is missing.

> [!IMPORTANT]
> If a record is marked sensitive/culturally restricted, **do not** return precise locations or excerpts by default.
> Return an abstracted hit (title + “restricted”) and require explicit elevated authorization pathways.

---

## ✅ Definition of Done (DoD)

- [ ] Port interface exists and is stable (typed, documented).
- [ ] Adapter implements the port without leaking infrastructure concerns into Domain/Use Cases.
- [ ] Contract tests cover: paging, caps, timeout behavior, empty result sets, malformed filters.
- [ ] Integration tests run against a dev OpenSearch/Elasticsearch container (optional in CI, required locally).
- [ ] Provenance pointers returned for all hits (or an explicit reason when unavailable).
- [ ] Policy integration is respected (no bypass path).
- [ ] README links are valid and no lint/link checks fail.

---

## 🕰️ Version history

| Version | Date | Summary | Author |
|---:|---|---|---|
| v0.1 | 2026-02-12 | Initial adapter README (contracts + invariants) | KFM AI assistant |
