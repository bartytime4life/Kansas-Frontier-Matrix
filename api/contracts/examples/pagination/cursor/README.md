# Cursor Pagination (Keyset) Contract 🧭✨

![contract](https://img.shields.io/badge/contract-example-blue)
![pagination](https://img.shields.io/badge/pagination-cursor%20%2F%20keyset-informational)
![applies](https://img.shields.io/badge/applies%20to-REST%20%2B%20GraphQL-success)
![ux](https://img.shields.io/badge/UI-infinite%20scroll%20friendly-brightgreen)

> [!NOTE]
> This is an **example contract** for **cursor-based pagination** across KFM list endpoints.  
> Treat cursors as **opaque** (do not parse, do not modify) ✅

> [!IMPORTANT]
> Cursor pagination is the default for **large datasets, timeline feeds, map-layer listings, graph traversals**, and anything that can grow unbounded.  
> Offset pagination is allowed only for small, bounded lists (admin/debug tooling, tiny enums, etc.) ⚖️

---

## 🧾 Policy metadata

| Field | Value |
|------|-------|
| File | `api/contracts/examples/pagination/cursor/README.md` |
| Status | ✅ Active (example) |
| Last updated | `2026-01-24` |
| Pagination type | Cursor / keyset |
| Cursor type | Opaque token (base64url + signature recommended) |
| Default limit | `50` |
| Max limit | `250` (server enforced) |
| Stable ordering | Required (`sort` + `id` tie-breaker) |

---

## 📍 Location (repo map)

```text
📦 api/
└─ 📜 contracts/
   └─ 🧪 examples/
      └─ 📄 pagination/
         ├─ 🧭 cursor/
         │  └─ README.md   👈 you are here
         └─ 🔢 offset/     (optional companion example)
```

---

## 🎯 Goals

- **Fast** paging for large collections (no `OFFSET n` scans) ⚡
- **Stable** ordering that avoids duplicates/holes as much as possible
- **API-boundary safe**: redaction/ACLs apply before paging (fail-closed posture) 🔒
- **UI-friendly**: supports infinite scroll + “load newer/older” flows 🧩
- Works for both **REST** and **GraphQL** list patterns 🌐

## 🚫 Non-goals

- Exact totals for huge lists (expensive). We prefer `has_more` over `total_count`.
- “Jump to page N” (cursor pagination is sequential by design).

---

## 🧠 Contract overview

### ✅ Recommended envelope

All cursor-paged list endpoints return a consistent envelope:

```json
{
  "data": [],
  "page": {
    "limit": 50,
    "returned": 50,
    "next_cursor": "opaque",
    "prev_cursor": "opaque_or_null",
    "has_next": true,
    "has_prev": false,
    "as_of": "2026-01-24T18:41:03.221Z"
  },
  "links": {
    "self": "/api/v1/catalog/items?kind=dataset&sort=-updated_at,id&limit=50",
    "next": "/api/v1/catalog/items?kind=dataset&sort=-updated_at,id&limit=50&cursor=opaque",
    "prev": null
  },
  "meta": {
    "request_id": "req_01J2Q7B2S9N4Q2C2Q9KZ8D4H8A",
    "warnings": []
  }
}
```

> [!TIP]
> Prefer **additive changes** only (new optional fields) to avoid breaking clients ✅  
> Never rename `next_cursor`/`prev_cursor` once published.

---

## 🧩 REST contract

### Request (GET)

**Pattern**
- `GET /api/v1/<resource>?limit=<int>&cursor=<string>&sort=<string>&...filters`

**Query parameters**
- `limit` (int, optional)  
  - Default: `50`
  - Max: `250`
- `cursor` (string, optional)  
  - Opaque paging token returned by the server
- `direction` (string, optional)  
  - Values: `next | prev`  
  - Default: `next`
- `sort` (string, optional)  
  - Default: `-updated_at,id`  
  - Rules:
    - MUST include a **unique tie-breaker** (usually `id`)
    - MUST be deterministic across pages
- `as_of` (RFC3339 timestamp, optional)  
  - Pins the list to a snapshot for consistent scrolling (recommended for timelines/infinite scroll)
- `...filters` (optional)  
  - Any filters supported by the resource (e.g., `kind=dataset`, `bbox=...`, `q=...`)

> [!IMPORTANT]
> **Filters + sort MUST remain identical** across page requests.  
> If you change filters or sort, start a new paging session (omit `cursor`).

---

### Response (200)

**`page` object**
- `limit`: requested limit (or clamped)
- `returned`: number of items returned in this response
- `next_cursor`: token to fetch the next page (or `null` if none)
- `prev_cursor`: token to fetch the previous page (or `null` if none / unsupported)
- `has_next`: boolean
- `has_prev`: boolean
- `as_of`: server snapshot timestamp used to compute this page

> [!NOTE]
> Cursor pagination can support “previous page” in two ways:
> - **True reverse cursor** (`direction=prev`) ✅
> - Or **client-side caching** of earlier pages (common for infinite scroll) 🧠

---

### Errors

All errors should use a consistent envelope (example):

```json
{
  "error": {
    "code": "CURSOR_INVALID",
    "message": "Cursor is malformed or cannot be verified.",
    "details": {
      "hint": "Restart pagination without cursor; ensure filters + sort match."
    }
  },
  "meta": {
    "request_id": "req_01J2Q7C0P9EX0F2G2AXN9H0M3C"
  }
}
```

**Recommended cursor-related error codes**
- `CURSOR_INVALID` (400) — malformed / signature mismatch / wrong shape
- `CURSOR_EXPIRED` (410) — cursor TTL exceeded (or server rotated signing key)
- `CURSOR_MISMATCH` (409) — cursor doesn’t match the current query fingerprint (filters/sort/tenant)
- `LIMIT_TOO_LARGE` (400) — client requested > max
- `SORT_UNSUPPORTED` (400) — sort field not allowed for this resource

---

## 🧪 End-to-end examples

### Example 1 — First page (no cursor) ✅

```bash
curl -sS \
  "https://kfm.local/api/v1/catalog/items?kind=dataset&sort=-updated_at,id&limit=2"
```

```json
{
  "data": [
    {
      "id": "cat_01J2Q7D4R8Q9X1A3B2C4D5E6F7",
      "kind": "dataset",
      "title": "Example Dataset A",
      "updated_at": "2026-01-24T18:40:12.002Z",
      "links": {
        "dcat": "/data/catalog/dcat/dataset/cat_01J2Q7D4R8Q9X1A3B2C4D5E6F7.json",
        "stac": "/data/catalog/stac/collections/cat_01J2Q7D4R8Q9X1A3B2C4D5E6F7.json",
        "prov": "/data/catalog/prov/runs/run_01J2Q6ZZZZZZZZZZZZZZZZZZZZ.json"
      }
    },
    {
      "id": "cat_01J2Q7D1M0N9X9A8B7C6D5E4F3",
      "kind": "dataset",
      "title": "Example Dataset B",
      "updated_at": "2026-01-24T18:39:58.441Z",
      "links": {
        "dcat": "/data/catalog/dcat/dataset/cat_01J2Q7D1M0N9X9A8B7C6D5E4F3.json",
        "stac": "/data/catalog/stac/collections/cat_01J2Q7D1M0N9X9A8B7C6D5E4F3.json",
        "prov": "/data/catalog/prov/runs/run_01J2Q6YYYYYYYYYYYYYYYYYYYYYY.json"
      }
    }
  ],
  "page": {
    "limit": 2,
    "returned": 2,
    "next_cursor": "eyJ2IjoxLCJzIjoiLXVwZGF0ZWRfYXQsaWQiLCJwIjpbIjIwMjYtMDEtMjRUMTg6Mzk6NTguNDQxWiIsImNhdF8wMUoyUTdEMU0wTjlYOUE4QjdDNkQ1RTRGMyJdLCJxIjoiZ3U0N0tGRiJ9.r4pFzqJmQe3u",
    "prev_cursor": null,
    "has_next": true,
    "has_prev": false,
    "as_of": "2026-01-24T18:41:03.221Z"
  },
  "links": {
    "self": "/api/v1/catalog/items?kind=dataset&sort=-updated_at,id&limit=2",
    "next": "/api/v1/catalog/items?kind=dataset&sort=-updated_at,id&limit=2&cursor=eyJ2IjoxLCJzIjoiLXVwZGF0ZWRfYXQsaWQiLCJwIjpbIjIwMjYtMDEtMjRUMTg6Mzk6NTguNDQxWiIsImNhdF8wMUoyUTdEMU0wTjlYOUE4QjdDNkQ1RTRGMyJdLCJxIjoiZ3U0N0tGRiJ9.r4pFzqJmQe3u",
    "prev": null
  },
  "meta": {
    "request_id": "req_01J2Q7E2V6F7G8H9J0K1L2M3N4",
    "warnings": []
  }
}
```

---

### Example 2 — Next page (use `next_cursor`) ▶️

```bash
curl -sS \
  "https://kfm.local/api/v1/catalog/items?kind=dataset&sort=-updated_at,id&limit=2&cursor=eyJ2IjoxLCJzIjoiLXVwZGF0ZWRfYXQsaWQiLCJwIjpbIjIwMjYtMDEtMjRUMTg6Mzk6NTguNDQxWiIsImNhdF8wMUoyUTdEMU0wTjlYOUE4QjdDNkQ1RTRGMyJdLCJxIjoiZ3U0N0tGRiJ9.r4pFzqJmQe3u"
```

Response includes a **new** `next_cursor` until `has_next=false`.

---

### Example 3 — Reverse paging (`direction=prev`) ⏪

```bash
curl -sS \
  "https://kfm.local/api/v1/catalog/items?kind=dataset&sort=-updated_at,id&limit=2&direction=prev&cursor=<prev_cursor_from_later_page>"
```

> [!TIP]
> Reverse paging is most useful for:
> - “Load newer” vs “Load older” timeline toggles 🕰️
> - Chat/history feeds
> - Audit/event streams

---

## 🧬 GraphQL contract (Relay-ish connection)

Cursor pagination is the default for GraphQL lists.

```graphql
query Datasets($first: Int!, $after: String, $asOf: DateTime) {
  datasets(first: $first, after: $after, asOf: $asOf, sort: UPDATED_AT_DESC) {
    edges {
      cursor
      node {
        id
        title
        updatedAt
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

> [!IMPORTANT]
> GraphQL servers should enforce **depth + cost + result size** limits to prevent “infinite queries” 🔥

---

## 🔐 Cursor design guidance (server-side)

### 1) Keep it opaque
- Clients treat `cursor` as a black box.
- Cursor MAY contain internal state (sort keys, snapshot, query fingerprint).

### 2) Sign it (and optionally encrypt it)
Recommended token approach:
- `base64url(payload_json) + "." + base64url(hmac_sha256(payload, secret))`

Why?
- Prevents tampering
- Lets the server bind cursors to a query fingerprint (`filters + sort + principal + tenant`)

### 3) Always include a deterministic tie-breaker
If sorting by a non-unique field (`updated_at`, `event_date`, etc.), **append `id`**:
- `ORDER BY updated_at DESC, id DESC`

### 4) Prefer snapshot pinning for UX stability
Include `as_of` in the cursor payload and return it in the response:
- avoids duplicates/holes when underlying data changes mid-scroll
- improves “story node” + “timeline scrubber” UX 🎛️

---

## 🛠️ Implementation notes (PostGIS + Neo4j friendly)

### Postgres/PostGIS (keyset pagination)
For descending sort (`-updated_at,id`):

```sql
SELECT *
FROM catalog_items
WHERE kind = :kind
  AND (updated_at, id) < (:cursor_updated_at, :cursor_id)
ORDER BY updated_at DESC, id DESC
LIMIT :limit_plus_one;
```

### Neo4j (keyset pagination)
For nodes with `updated_at` + `id`:

```cypher
MATCH (n:Dataset)
WHERE n.kind = $kind
  AND (
    n.updated_at < $cursorUpdatedAt OR
    (n.updated_at = $cursorUpdatedAt AND n.id < $cursorId)
  )
RETURN n
ORDER BY n.updated_at DESC, n.id DESC
LIMIT $limitPlusOne;
```

> [!NOTE]
> Cursor comparisons MUST match the sort direction:
> - For `DESC`, use `<`
> - For `ASC`, use `>`

---

## 🧑‍💻 Client loop examples

### JavaScript (simple “fetch all pages”)
```js
let cursor = null;
const all = [];

while (true) {
  const url = new URL("https://kfm.local/api/v1/catalog/items");
  url.searchParams.set("kind", "dataset");
  url.searchParams.set("sort", "-updated_at,id");
  url.searchParams.set("limit", "50");
  if (cursor) url.searchParams.set("cursor", cursor);

  const res = await fetch(url);
  const body = await res.json();

  all.push(...body.data);

  if (!body.page?.has_next || !body.page?.next_cursor) break;
  cursor = body.page.next_cursor;
}
```

### Python (requests)
```python
import requests

cursor = None
items = []

while True:
    params = {"kind": "dataset", "sort": "-updated_at,id", "limit": 50}
    if cursor:
        params["cursor"] = cursor

    r = requests.get("https://kfm.local/api/v1/catalog/items", params=params, timeout=30)
    r.raise_for_status()
    body = r.json()

    items.extend(body["data"])

    page = body.get("page", {})
    if not page.get("has_next") or not page.get("next_cursor"):
        break

    cursor = page["next_cursor"]
```

---

## 🧯 Edge cases & gotchas

- **Changing filters** mid-pagination invalidates the cursor → start over 🔁
- **Sorting by non-unique fields** without a tie-breaker causes duplicates/missing items ❌
- **Permissions/redactions**: cursor results must be computed *after* policy filtering 🔒
- **Data mutations** during scroll: prefer `as_of` pinning for consistent UX 🧊
- **Totals**: avoid `total_count` unless explicitly requested (and cached) 🧮

---

## 🧷 Definition of Done ✅

- [ ] Cursor is **opaque** and treated as such by clients
- [ ] Cursor token is **signed** (and optionally encrypted)
- [ ] Sort order is **stable** and includes a **tie-breaker** (`id`)
- [ ] Max `limit` is enforced server-side
- [ ] Response includes `next_cursor`, `has_next`, and `as_of`
- [ ] GraphQL list fields expose Relay-style pagination (`edges/pageInfo`)
- [ ] Cursor errors return consistent error codes + `request_id`
- [ ] Example requests/responses stay valid after additive schema evolution

---

## 📎 Related examples

- 🔢 Offset pagination (if present): `../offset/README.md`
- 🧪 Contract conventions: `../../../README.md` (if present)
