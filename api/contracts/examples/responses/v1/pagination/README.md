# 📦 Pagination Response Examples (v1)

![API](https://img.shields.io/badge/API-v1-2ea44f) ![Contract](https://img.shields.io/badge/Contract-pagination-blue) ![Format](https://img.shields.io/badge/Format-JSON-lightgrey) ![Strategy](https://img.shields.io/badge/Strategy-cursor%20%28keyset%29-ff69b4)

> [!IMPORTANT]
> In KFM, **list-style endpoints MUST paginate** (REST + GraphQL list fields). This keeps the platform fast, safe, and predictable for the web UI, mobile/AR clients, scripts, and future federation nodes.

---

## 📁 Folder (this README lives here)

```text
📁 api/contracts/examples/responses/v1/pagination/
└── 📄 README.md   👈 you are here
```

### ✅ Recommended canonical example set (add these JSON files next)

```text
📁 api/contracts/examples/responses/v1/pagination/
├── 📄 README.md
├── 🧪 cursor.first-page.json          # ✅ first page (no cursor param)
├── 🧪 cursor.next-page.json           # ➡️ middle page (cursor provided)
├── 🧪 cursor.last-page.json           # 🏁 last page (next_cursor = null)
├── 🧪 cursor.empty.json               # 🫙 empty result set
└── 🧪 cursor.with-total.json          # 🔢 includes total (include_total=true)
```

> [!NOTE]
> The filenames above are a **project convention** for contract examples. If your repo uses a different naming scheme, keep the **scenarios** but rename freely.

---

## 🧭 Quick navigation

- [🎯 Goal & scope](#-goal--scope)
- [🧩 Contract shape](#-contract-shape)
- [🔎 Query parameters](#-query-parameters)
- [🧪 Examples](#-examples)
- [🧰 Client checklist](#-client-checklist)
- [⚠️ Gotchas & design notes](#️-gotchas--design-notes)
- [🧬 GraphQL crosswalk](#-graphql-crosswalk)

---

## 🎯 Goal & scope

This folder documents the **standard pagination block** used across **KFM v1** list responses.

KFM is **catalog-driven / evidence-first** and enforces **policy + redaction at the API boundary**, so pagination needs to work even when:
- results are filtered by **classification / permissions** 🔐  
- the backend is **heterogeneous** (PostGIS + Neo4j + catalogs) 🧩  
- queries can be **federated** later (multi-node “Frontier Matrix” network) 🌐

This README is **normative** for response shape and semantics (so tests + clients can rely on it).

---

## 🧩 Contract shape

### ✅ Minimal paginated list response (recommended envelope)

> Your endpoint’s payload key may vary (`items`, `datasets`, `features`, etc.).  
> **What must be consistent** is the `pagination` block and `links`.

```json
{
  "items": [],
  "pagination": {
    "mode": "cursor",
    "limit": 50,
    "returned": 0,
    "next_cursor": null,
    "prev_cursor": null,
    "has_next": false,
    "has_prev": false,
    "total": null,
    "sort": "updated_at:desc,id:asc"
  },
  "links": [
    { "rel": "self", "href": "/v1/example?limit=50&sort=updated_at:desc,id:asc", "type": "application/json" }
  ],
  "meta": {
    "request_id": "req_example_123"
  }
}
```

> [!TIP]
> `links` intentionally uses a **STAC-style link shape** (`rel`, `href`, `type`) so clients can reuse link-handling logic across catalog responses.

---

### 🧱 `pagination` object (v1)

| Field | Type | Required | Meaning |
|---|---:|:---:|---|
| `mode` | `"cursor"` | ✅ | Pagination style for v1 (keyset/cursor). |
| `limit` | `integer` | ✅ | Requested page size (server may clamp). |
| `returned` | `integer` | ✅ | Number of items actually returned in this response. |
| `next_cursor` | `string \| null` | ✅ | Opaque token for the next page (pass as `cursor`). |
| `prev_cursor` | `string \| null` | ✅ | Opaque token for the previous page (optional support). |
| `has_next` | `boolean` | ✅ | Convenience flag: `next_cursor !== null`. |
| `has_prev` | `boolean` | ✅ | Convenience flag: `prev_cursor !== null`. |
| `total` | `integer \| null` | ➖ | Total matching items **after policy/redaction**. `null` unless requested & allowed. |
| `sort` | `string` | ✅ | Canonical, stable sort applied. MUST include a deterministic tie-breaker (usually `id`). |

> [!IMPORTANT]
> **Cursors are opaque**. Clients must treat them as an unstructured string and never decode/inspect them.

---

### 🔗 `links[]` objects

| Field | Type | Required | Meaning |
|---|---:|:---:|---|
| `rel` | `"self" \| "next" \| "prev" \| "first"` | ✅ | Link relationship. |
| `href` | `string` | ✅ | Fully qualified or relative URL. |
| `type` | `string` | ➖ | MIME type (recommended: `application/json`). |
| `method` | `string` | ➖ | Defaults to `GET` if omitted. |
| `title` | `string` | ➖ | Optional human label. |

---

## 🔎 Query parameters

### Required/standard

| Param | Type | Default | Notes |
|---|---:|---:|---|
| `limit` | int | `50` | Server clamps to a max (recommend `250`). |
| `cursor` | string | _none_ | Cursor from `pagination.next_cursor` (or `prev_cursor`). |
| `sort` | string | endpoint-defined | Must be stable. Recommend always appending `,id:asc`. |

### Optional (recommended)

| Param | Type | Default | Notes |
|---|---:|---:|---|
| `include_total` | boolean | `false` | If `true`, server may compute `pagination.total` (post-policy). |
| `direction` | `"next" \| "prev"` | `next` | If you support `prev_cursor`, this disambiguates navigation. |

> [!NOTE]
> Many KFM endpoints will also include domain params (`q`, `bbox`, `time`, `dataset_id`, etc.).  
> Those are **endpoint-specific**, but MUST be carried forward in `links.next.href`.

---

## 🧪 Examples

Below are copy/paste examples you can promote into JSON files in this folder.

> [!NOTE]
> IDs/timestamps are illustrative. Cursor values are intentionally opaque “token-like” strings.

---

### ✅ Example 1 — First page (`cursor` omitted)

<details>
<summary><strong>cursor.first-page.json</strong> (click to expand)</summary>

```json
{
  "items": [
    {
      "id": "kfm.dataset.demo.0003",
      "title": "Kansas River Gauge Stations (Demo)",
      "updated_at": "2026-01-20T15:10:00Z"
    },
    {
      "id": "kfm.dataset.demo.0002",
      "title": "County Boundaries (Demo)",
      "updated_at": "2026-01-18T09:30:00Z"
    }
  ],
  "pagination": {
    "mode": "cursor",
    "limit": 2,
    "returned": 2,
    "next_cursor": "eyJzIjoiMjAyNi0wMS0xOFQwOTozMDowMFoiLCJpZCI6ImtmbS5kYXRhc2V0LmRlbW8uMDAwMiJ9",
    "prev_cursor": null,
    "has_next": true,
    "has_prev": false,
    "total": null,
    "sort": "updated_at:desc,id:asc"
  },
  "links": [
    {
      "rel": "self",
      "href": "/v1/datasets?limit=2&sort=updated_at:desc,id:asc",
      "type": "application/json"
    },
    {
      "rel": "next",
      "href": "/v1/datasets?limit=2&sort=updated_at:desc,id:asc&cursor=eyJzIjoiMjAyNi0wMS0xOFQwOTozMDowMFoiLCJpZCI6ImtmbS5kYXRhc2V0LmRlbW8uMDAwMiJ9",
      "type": "application/json"
    }
  ],
  "meta": {
    "request_id": "req_01_demo_first"
  }
}
```

</details>

---

### ➡️ Example 2 — Middle page (`cursor` provided)

<details>
<summary><strong>cursor.next-page.json</strong> (click to expand)</summary>

```json
{
  "items": [
    {
      "id": "kfm.dataset.demo.0001",
      "title": "Historical Rail Lines (Demo)",
      "updated_at": "2026-01-10T12:00:00Z"
    },
    {
      "id": "kfm.dataset.demo.0000",
      "title": "Landcover 1990–2020 (Demo)",
      "updated_at": "2026-01-02T08:45:00Z"
    }
  ],
  "pagination": {
    "mode": "cursor",
    "limit": 2,
    "returned": 2,
    "next_cursor": "eyJzIjoiMjAyNi0wMS0wMlQwODo0NTowMFoiLCJpZCI6ImtmbS5kYXRhc2V0LmRlbW8uMDAwMCJ9",
    "prev_cursor": "eyJzIjoiMjAyNi0wMS0xOFQwOTozMDowMFoiLCJpZCI6ImtmbS5kYXRhc2V0LmRlbW8uMDAwMiJ9",
    "has_next": true,
    "has_prev": true,
    "total": null,
    "sort": "updated_at:desc,id:asc"
  },
  "links": [
    {
      "rel": "self",
      "href": "/v1/datasets?limit=2&sort=updated_at:desc,id:asc&cursor=eyJzIjoiMjAyNi0wMS0xOFQwOTozMDowMFoiLCJpZCI6ImtmbS5kYXRhc2V0LmRlbW8uMDAwMiJ9",
      "type": "application/json"
    },
    {
      "rel": "prev",
      "href": "/v1/datasets?limit=2&sort=updated_at:desc,id:asc&direction=prev&cursor=eyJzIjoiMjAyNi0wMS0xOFQwOTozMDowMFoiLCJpZCI6ImtmbS5kYXRhc2V0LmRlbW8uMDAwMiJ9",
      "type": "application/json"
    },
    {
      "rel": "next",
      "href": "/v1/datasets?limit=2&sort=updated_at:desc,id:asc&cursor=eyJzIjoiMjAyNi0wMS0wMlQwODo0NTowMFoiLCJpZCI6ImtmbS5kYXRhc2V0LmRlbW8uMDAwMCJ9",
      "type": "application/json"
    }
  ],
  "meta": {
    "request_id": "req_02_demo_middle"
  }
}
```

</details>

---

### 🏁 Example 3 — Last page (`next_cursor = null`)

<details>
<summary><strong>cursor.last-page.json</strong> (click to expand)</summary>

```json
{
  "items": [
    {
      "id": "kfm.dataset.demo.0000",
      "title": "Landcover 1990–2020 (Demo)",
      "updated_at": "2026-01-02T08:45:00Z"
    }
  ],
  "pagination": {
    "mode": "cursor",
    "limit": 2,
    "returned": 1,
    "next_cursor": null,
    "prev_cursor": "eyJzIjoiMjAyNi0wMS0xMFQxMjowMDowMFoiLCJpZCI6ImtmbS5kYXRhc2V0LmRlbW8uMDAwMSJ9",
    "has_next": false,
    "has_prev": true,
    "total": null,
    "sort": "updated_at:desc,id:asc"
  },
  "links": [
    {
      "rel": "self",
      "href": "/v1/datasets?limit=2&sort=updated_at:desc,id:asc&cursor=eyJzIjoiMjAyNi0wMS0wMlQwODo0NTowMFoiLCJpZCI6ImtmbS5kYXRhc2V0LmRlbW8uMDAwMCJ9",
      "type": "application/json"
    },
    {
      "rel": "prev",
      "href": "/v1/datasets?limit=2&sort=updated_at:desc,id:asc&direction=prev&cursor=eyJzIjoiMjAyNi0wMS0xMFQxMjowMDowMFoiLCJpZCI6ImtmbS5kYXRhc2V0LmRlbW8uMDAwMSJ9",
      "type": "application/json"
    }
  ],
  "meta": {
    "request_id": "req_03_demo_last"
  }
}
```

</details>

---

### 🫙 Example 4 — Empty result set

<details>
<summary><strong>cursor.empty.json</strong> (click to expand)</summary>

```json
{
  "items": [],
  "pagination": {
    "mode": "cursor",
    "limit": 50,
    "returned": 0,
    "next_cursor": null,
    "prev_cursor": null,
    "has_next": false,
    "has_prev": false,
    "total": null,
    "sort": "updated_at:desc,id:asc"
  },
  "links": [
    { "rel": "self", "href": "/v1/datasets?limit=50&sort=updated_at:desc,id:asc&q=does-not-match", "type": "application/json" }
  ],
  "meta": {
    "request_id": "req_04_demo_empty"
  }
}
```

</details>

---

### 🔢 Example 5 — With total (`include_total=true`)

<details>
<summary><strong>cursor.with-total.json</strong> (click to expand)</summary>

```json
{
  "items": [
    { "id": "kfm.dataset.demo.0003", "title": "Kansas River Gauge Stations (Demo)", "updated_at": "2026-01-20T15:10:00Z" },
    { "id": "kfm.dataset.demo.0002", "title": "County Boundaries (Demo)", "updated_at": "2026-01-18T09:30:00Z" }
  ],
  "pagination": {
    "mode": "cursor",
    "limit": 2,
    "returned": 2,
    "next_cursor": "eyJzIjoiMjAyNi0wMS0xOFQwOTozMDowMFoiLCJpZCI6ImtmbS5kYXRhc2V0LmRlbW8uMDAwMiJ9",
    "prev_cursor": null,
    "has_next": true,
    "has_prev": false,
    "total": 4,
    "sort": "updated_at:desc,id:asc"
  },
  "links": [
    {
      "rel": "self",
      "href": "/v1/datasets?limit=2&sort=updated_at:desc,id:asc&include_total=true",
      "type": "application/json"
    },
    {
      "rel": "next",
      "href": "/v1/datasets?limit=2&sort=updated_at:desc,id:asc&include_total=true&cursor=eyJzIjoiMjAyNi0wMS0xOFQwOTozMDowMFoiLCJpZCI6ImtmbS5kYXRhc2V0LmRlbW8uMDAwMiJ9",
      "type": "application/json"
    }
  ],
  "meta": {
    "request_id": "req_05_demo_total",
    "notes": "total is post-policy (after classification/redaction)"
  }
}
```

</details>

---

## 🧰 Client checklist

✅ **Do this**
- Use `links` (rel=`next`/`prev`) rather than constructing URLs by hand.
- Treat `next_cursor` / `prev_cursor` as opaque.
- Stop paging when `has_next=false` (or `next_cursor=null`).
- Expect `total` to be `null` unless you explicitly request it **and** policy allows it.
- Store `sort` (or echo it) so a user can reproduce a result set later.

❌ **Avoid this**
- Don’t assume cursors are stable across users/roles (policy context can change).
- Don’t switch `sort` mid-walk (you will get duplicates/misses).
- Don’t fetch “everything” in one request (KFM endpoints should clamp `limit`).

---

## ⚠️ Gotchas & design notes

### 1) Governance + redaction affects totals (and sometimes cursors) 🔐
KFM enforces classification and redaction at the API boundary. That means:
- `pagination.total` (when present) is **post-policy**.
- Some records may be omitted entirely (not “masked”), so clients should not infer that “missing” IDs exist.

### 2) Always require a deterministic sort 🎯
For keyset pagination to be correct, the server must apply a stable ordering:
- **Include a tie-breaker** (usually `id`) to avoid “random” ordering when timestamps match.
- Prefer monotonic-ish fields (`updated_at`, `created_at`, `id`).

### 3) Cursor tokens may be signed 🧾
Implementations often sign/encrypt cursors to prevent tampering. If a cursor is invalid:
- return a **400** with the standard v1 error contract (see `api/contracts/examples/responses/v1/errors/`).

### 4) GeoJSON and STAC responses can still use this block 🗺️
If an endpoint returns GeoJSON:
```json
{
  "type": "FeatureCollection",
  "features": [],
  "pagination": { "...": "..." },
  "links": []
}
```
This is compatible with JSON extension patterns used in KFM’s standards-driven ecosystem.

---

## 🧬 GraphQL crosswalk

KFM supports GraphQL for graph-shaped queries; GraphQL lists should follow a connection-style pattern.

**Mapping:**
- `pagination.next_cursor` → `pageInfo.endCursor`
- `pagination.has_next` → `pageInfo.hasNextPage`
- `pagination.prev_cursor` → `pageInfo.startCursor` (optional)
- `pagination.has_prev` → `pageInfo.hasPreviousPage` (optional)

Example (conceptual):

```graphql
query {
  datasets(first: 50, after: "CURSOR") {
    edges { node { id title } }
    pageInfo { endCursor hasNextPage }
  }
}
```

> [!TIP]
> Even if the REST and GraphQL shapes differ, keep cursor semantics consistent so clients can share paging logic.

---

## 🧾 Versioning rules

- Adding **optional** fields to `pagination` is non-breaking within v1 ✅  
- Changing field names/types, or changing cursor semantics, is **breaking** → bump to `/v2/` 🚨
- Update examples **and** schemas together (contract-first discipline).

---
y
