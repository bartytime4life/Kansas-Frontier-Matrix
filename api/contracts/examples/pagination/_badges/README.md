---
title: "🏷️ Pagination Badges"
path: "api/contracts/examples/pagination/_badges/README.md"
version: "0.1.0"
last_updated: "2026-01-24"
status: "draft"
---

<!-- markdownlint-disable MD033 -->

# 🏷️ Pagination Badges

Local **SVG badges** used by the **pagination contract examples** (`api/contracts/examples/pagination/`) so readers can scan a doc and instantly understand the paging model + guarantees.

> [!NOTE]
> KFM leans hard on **REST + GraphQL** for UI ↔ backend interaction, and GraphQL list fields should be **paginated** to avoid runaway/expensive queries. Badges make those choices visible at a glance.

---

## 📌 Why these exist

✅ Badges help us quickly communicate things like:

- **Pagination strategy** (cursor vs offset vs GraphQL connection)
- **Stability & consistency** (stable ordering, snapshot-consistent vs live/streaming)
- **UX expectations** (infinite scroll friendly, “Load more”, total count present/omitted)
- **Policy + safety defaults** (rate limiting, policy-gated result sets)

In KFM, “small UX details” become “big correctness details” once you have:
- large geospatial layers,
- high-cardinality catalog/search results,
- multi-user roles & sensitive classifications,
- and an AI layer that may request/consume lists of evidence sources.

---

## 🚀 Quick usage

### From a sibling doc (most common)
Example from `api/contracts/examples/pagination/README.md` (or any other file at the same level):

```md
<!-- Badge row (preferred) -->
<img src="./_badges/cursor.svg" alt="Cursor pagination" height="20" />
<img src="./_badges/stable-order.svg" alt="Stable ordering" height="20" />
<img src="./_badges/no-total-count.svg" alt="No total count" height="20" />
<img src="./_badges/bounded-limit.svg" alt="Bounded page size" height="20" />
```

### From inside this folder
```md
<img src="./cursor.svg" alt="Cursor pagination" height="20" />
```

> [!TIP]
> Use `<img ... height="20" />` instead of `![]()` so all badges render at a consistent size across GitHub + doc tooling.

---

## 🧱 Folder layout

```text
api/
└─ 📜 contracts/
   └─ 🧪 examples/
      └─ 📑 pagination/
         ├─ 📄 README.md                     # 📘 Pagination examples index (cursor/offset/since) + contract/testing notes
         └─ 🏷️ _badges/                      # ← you are here ✅ 📌 Small SVG badges used in docs to label pagination behavior
            ├─ ✅📄 README.md                 # 📘 Badge usage: where to embed, naming rules, and when to use each badge
            ├─ 🏷️🖼️ cursor.svg               # Cursor-based pagination badge (opaque cursor token; stable ordering required)
            ├─ 🏷️🖼️ offset.svg               # Offset/limit pagination badge (simple; can drift on inserts)
            ├─ 🏷️🖼️ relay.svg                # Relay-style cursor badge (edges/nodes/pageInfo conventions)
            ├─ 🏷️🖼️ stable-order.svg          # Stable ordering badge (sort keys guarantee deterministic page boundaries)
            ├─ 🏷️🖼️ snapshot.svg              # Snapshot paging badge (query runs against a fixed snapshot/version)
            ├─ 🏷️🖼️ live.svg                  # Live paging badge (dataset can change while paging; expect drift)
            ├─ 🏷️🖼️ total-count.svg           # Total count available badge (returns total or estimate)
            ├─ 🏷️🖼️ no-total-count.svg        # No total count badge (omit totals for perf/safety reasons)
            ├─ 🏷️🖼️ links-body.svg            # Pagination links in response body badge (next/prev URLs in JSON)
            ├─ 🏷️🖼️ link-header.svg           # Pagination links in HTTP Link header badge
            ├─ 🏷️🖼️ bounded-limit.svg          # Max page size enforced badge (server clamps limit)
            ├─ 🏷️🖼️ policy-gated.svg           # Policy-gated paging badge (results/page size constrained by auth/policy)
            └─ 🏷️🖼️ rate-limited.svg           # Rate-limited paging badge (429 possible; Retry-After guidance)
```

---

## 🧾 Badge catalog

> [!WARNING]
> If an SVG listed below doesn’t exist yet, treat this README as the **contract for what to add next**.

| Badge (preview) | File | Means | Use when |
|---:|---|---|---|
| <img src="./cursor.svg" alt="Cursor pagination" height="20" /> | `cursor.svg` | Cursor / keyset pagination (opaque cursor) | Infinite scroll, search results, “next page” tokens, large datasets |
| <img src="./offset.svg" alt="Offset pagination" height="20" /> | `offset.svg` | Offset / page-number pagination | Admin tooling, small datasets, analytics-like screens |
| <img src="./relay.svg" alt="GraphQL connection" height="20" /> | `relay.svg` | GraphQL **Connection** pattern (Relay-style) | GraphQL list fields (`edges/node/pageInfo`) |
| <img src="./stable-order.svg" alt="Stable ordering" height="20" /> | `stable-order.svg` | Stable deterministic ordering enforced | Any paginated endpoint where duplicateś duplicates/missing results are unacceptable |
| <img src="./snapshot.svg" alt="Snapshot consistent" height="20" /> | `snapshot.svg` | Snapshot-consistent paging (cursor anchored to an `as_of` / snapshot id) | Auditability, exports, research/citation workflows |
| <img src="./live.svg" alt="Live feed" height="20" /> | `live.svg` | Live/streaming paging (best-effort; results may change between pages) | Real-time layers, “since=timestamp” feeds, dashboards |
| <img src="./total-count.svg" alt="Total count included" height="20" /> | `total-count.svg` | Response includes `total_count` (or equivalent) | Small-to-medium result sets, UX needs page counts |
| <img src="./no-total-count.svg" alt="No total count" height="20" /> | `no-total-count.svg` | Total count is intentionally omitted | Performance, large search results, or to reduce info leakage |
| <img src="./links-body.svg" alt="Links in body" height="20" /> | `links-body.svg` | `links[]` in response body (`rel=next/prev`) | STAC/OGC-ish patterns, hypermedia-friendly APIs |
| <img src="./link-header.svg" alt="HTTP Link header" height="20" /> | `link-header.svg` | HTTP `Link` header pagination (`rel="next"`) | Strict HTTP clients, caching layers, gateway-friendly patterns |
| <img src="./bounded-limit.svg" alt="Bounded page size" height="20" /> | `bounded-limit.svg` | Server enforces page size bounds (min/max) | Always—prevents abuse + protects DB/query engines |
| <img src="./policy-gated.svg" alt="Policy gated" height="20" /> | `policy-gated.svg` | Results are filtered by classification / role / policy | Sensitive layers, sovereignty constraints, restricted datasets |
| <img src="./rate-limited.svg" alt="Rate limited" height="20" /> | `rate-limited.svg` | Endpoint is rate limited (429s are expected) | Public endpoints, expensive queries, AI-assisted endpoints |

---

## 🧠 Badge semantics (what they *actually* imply)

### 🧭 Cursor pagination (`cursor.svg`)
A “cursor” badge implies:
- Request uses something like `?cursor=...&limit=...` or POST body includes `cursor`.
- Cursor is **opaque** (treat as token, not raw offsets).
- Response supplies a **next cursor**, either:
  - `page.next_cursor`, or
  - `links[]` with `rel=next`, or
  - `Link` header with `rel="next"`.

### 🧮 Offset pagination (`offset.svg`)
An “offset” badge implies:
- Request uses `?offset=&limit=` or `?page=&page_size=`.
- Offset pagination must be paired with a **stable sort** (or you can drift).

### 🔗 GraphQL connection (`relay.svg`)
A “relay” badge implies:
- Connection fields follow the pattern:

```graphql
type ThingConnection {
  edges: [ThingEdge!]!
  pageInfo: PageInfo!
}

type ThingEdge {
  cursor: String!
  node: Thing!
}
```

…and callers use `first/after` (and optionally `last/before`).

### 🧊 Snapshot consistency (`snapshot.svg`)
A “snapshot” badge implies:
- Page 1 and page 2 describe the **same logical list** even if underlying data changes.
- Cursor is anchored to a stable marker like `as_of` or `snapshot_id`.

### 📡 Live / streaming (`live.svg`)
A “live” badge implies:
- Data may be changing quickly.
- Caller should tolerate:
  - duplicates,
  - missing items,
  - shifting totals (usually no totals).

### 🧷 Stable ordering (`stable-order.svg`)
A “stable-order” badge implies:
- Sort is deterministic, and includes a **tie-breaker** (e.g., `ORDER BY updated_at DESC, id DESC`).
- Without it, paging can **skip** or **duplicate** results.

### 🔢 Total count (`total-count.svg`) vs 🙈 No total (`no-total-count.svg`)
- `total-count` implies a **true** (not “maybe”) count is provided.
- `no-total-count` implies count is intentionally omitted for:
  - performance,
  - large searches,
  - or reducing sensitive inference.

---

## 🧩 Recommended badge “packs” (copy/paste)

### 1) Public search results (fast + safe)
```md
<img src="./_badges/cursor.svg" alt="Cursor pagination" height="20" />
<img src="./_badges/stable-order.svg" alt="Stable ordering" height="20" />
<img src="./_badges/no-total-count.svg" alt="No total count" height="20" />
<img src="./_badges/bounded-limit.svg" alt="Bounded page size" height="20" />
<img src="./_badges/rate-limited.svg" alt="Rate limited" height="20" />
```

### 2) Admin table view (page counts are useful)
```md
<img src="./_badges/offset.svg" alt="Offset pagination" height="20" />
<img src="./_badges/stable-order.svg" alt="Stable ordering" height="20" />
<img src="./_badges/total-count.svg" alt="Total count included" height="20" />
<img src="./_badges/bounded-limit.svg" alt="Bounded page size" height="20" />
```

### 3) GraphQL list fields (don’t melt Neo4j/Postgres)
```md
<img src="./_badges/relay.svg" alt="GraphQL connection" height="20" />
<img src="./_badges/cursor.svg" alt="Cursor pagination" height="20" />
<img src="./_badges/stable-order.svg" alt="Stable ordering" height="20" />
<img src="./_badges/bounded-limit.svg" alt="Bounded page size" height="20" />
```

### 4) Real-time feeds (windowed/live)
```md
<img src="./_badges/live.svg" alt="Live feed" height="20" />
<img src="./_badges/no-total-count.svg" alt="No total count" height="20" />
<img src="./_badges/bounded-limit.svg" alt="Bounded page size" height="20" />
```

---

## 🛠️ Adding a new badge

1. **Name** it in `kebab-case` as `*.svg`
2. Keep it **short** (badge-sized) and readable at **20px height**
3. Add a row to the **Badge catalog** table
4. Prefer **local SVGs** (don’t depend on external badge services in long-lived contracts)

> [!TIP]
> Keep badges **semantic**, not decorative. If a badge can’t be mapped to a contract behavior, it doesn’t belong here.

---

## ✅ Definition of done (DoD)

- [ ] Badge SVG exists in this folder
- [ ] Badge is listed in the catalog table
- [ ] Badge has meaningful `alt=""` text in examples
- [ ] Badge semantics are described (or referenced) above
- [ ] At least one pagination example doc uses it correctly

---

## 🔒 Security & governance reminders (pagination-specific)

> [!IMPORTANT]
> Pagination tokens **must not** become a side-channel.

Common guardrails (especially for `policy-gated` endpoints):
- bind cursors to **filters + policy scope** (don’t let a token leak cross-tenant results),
- avoid returning `total_count` when it increases inference risk,
- enforce `bounded-limit` always,
- rate limit public endpoints.

---

## 📚 See also

- `api/contracts/examples/pagination/README.md` 📄
- `api/scripts/policy/README.md` 🧾 (policy gates that may influence what pagination can expose)
- `docs/architecture/*` 🏛️ (REST/GraphQL shape + performance constraints)

