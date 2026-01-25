# GraphQL Pagination Contracts (Examples) 🔁🧩

![Contract](https://img.shields.io/badge/contract-first-blue)
![GraphQL](https://img.shields.io/badge/GraphQL-pagination-purple)
![KFM](https://img.shields.io/badge/KFM-governed%20API-2ea44f)
![Status](https://img.shields.io/badge/examples-reference%20implementation%20style-informational)

> 📌 **Goal:** Provide a **copy/paste-ready** pagination contract + examples for the **Kansas Frontier Matrix (KFM)** GraphQL API—built for **high-scale lists**, **knowledge-graph traversal**, and **governed, evidence-first data**.

---

## Why pagination is non-negotiable in KFM 🚦

KFM’s GraphQL layer is designed for **semantic queries** across a connected graph (people ⇄ events ⇄ places ⇄ datasets). That’s powerful… and also a risk if lists are unbounded.

Pagination protects:
- 🧠 **Back-end resources** (Neo4j + PostGIS + caches)
- 🕸️ **Graph traversal complexity** (depth & fan-out)
- 🧑‍⚖️ **Governance rules** (classification, access control, redaction)
- 🧾 **Auditability** (stable, repeatable, contract-first behavior)

---

## 📁 Where this doc lives

```text
api/
└─ 📜 contracts/
   └─ 🧪 examples/
      └─ 📑 pagination/
         └─ 🧬 graphql/
            └─ 📄 README.md   # 👈 you are here 📌 GraphQL pagination examples (Relay pageInfo, cursors, edges/nodes, limits)
```

> Tip: Keep this file “example-contract-quality” even if the runtime schema changes. The intent is **to standardize patterns** across types.

---

## Pagination standards ✅

### ✅ Preferred: Cursor-based pagination (Relay-style connections)
Use:
- `first` + `after` (forward pagination)
- `last` + `before` (reverse pagination)

Return:
- `edges { cursor, node }`
- `pageInfo { startCursor, endCursor, hasNextPage, hasPreviousPage }`
- optional `totalCount`

### ⚠️ Allowed (limited cases): offset pagination
Offset-based pagination (`limit` + `offset`) can be acceptable for:
- small bounded tables
- admin-only tooling
- stable, non-relational list endpoints

But for graph relationships, **cursor pagination is the default**.

### ❌ Avoid
- Returning **raw arrays** for large relationships
- “Give me everything” fields (even internally)
- Cursors that are not stable against ordering/filter changes

---

## Contract: connection primitives 🧱

### Rules of the road 🛣️
- `first` and `last` **MUST NOT** be used together
- `after` is only valid with `first`
- `before` is only valid with `last`
- If a collection can exceed a small threshold, it **MUST** be a connection

---

## GraphQL SDL (reference contract) 📜

> This SDL is **pattern-focused**. You’ll still define per-type Connections (GraphQL has no generics).

<details>
<summary><strong>📌 Show SDL</strong></summary>

```graphql
"""
Opaque cursor token (treat as an uninspectable string on clients).
Implementation may be base64url(JSON).
"""
scalar Cursor

scalar DateTime

enum SortDirection {
  ASC
  DESC
}

"""
Standard paging args. Use forward paging (first/after) by default.
Reverse paging is supported with last/before for UI "scroll-up" patterns.
"""
input PageArgs {
  first: Int = 25
  after: Cursor
  last: Int
  before: Cursor
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: Cursor
  endCursor: Cursor
}
```
</details>

---

## Example: `Person.events` as a Connection 🧑‍🌾➡️📅

> Docs and prototypes often show list fields like `events: [Event!]!` for readability.  
> In KFM contracts: **that list becomes a connection**.

### Event ordering & filtering 🎛️

```graphql
enum EventOrderField {
  DATE
  TITLE
  CREATED_AT
}

input EventOrderBy {
  field: EventOrderField! = DATE
  direction: SortDirection! = ASC
}

input EventFilter {
  q: String
  from: DateTime
  to: DateTime
  placeId: ID
}
```

### Event connection types 🔗

```graphql
type Event {
  id: ID!
  title: String!
  date: DateTime
  # 🚫 Avoid large nested arrays here — use connections again if needed.
}

type EventEdge {
  cursor: Cursor!
  node: Event!
}

type EventConnection {
  edges: [EventEdge!]!
  pageInfo: PageInfo!
  """
  Optional because counts can be expensive (and can leak info under access control).
  If omitted/null, clients must behave gracefully.
  """
  totalCount: Int
}
```

### Person type (field-level contract)
```graphql
type Person {
  id: ID!
  name: String!

  events(
    page: PageArgs = {}
    orderBy: EventOrderBy = {}
    filter: EventFilter
  ): EventConnection!
}
```

---

## Cursor contract (server behavior) 🔐

### Cursor MUST be…
- **Opaque** (client treats it like a token)
- **Deterministic** (same query + same state ⇒ stable pagination)
- **Order-aware** (encodes the sort key + tie-breaker)

### Recommended encoding (implementation detail)
Use a base64url(JSON) payload like:

```json
{
  "v": 1,
  "scope": "Person.events",
  "order": ["DATE:ASC", "ID:ASC"],
  "filterHash": "sha256:…",
  "last": { "date": "1856-05-24T00:00:00Z", "id": "evt_01H…" }
}
```

✅ Includes:
- a version `v`
- a scope or field identity
- ordering (primary + tie-break)
- filter binding via `filterHash`
- last-seen values

---

## Example Queries ✅

### 1) Fetch the first page of events for a person 🧑‍⚖️

```graphql
query PersonEvents_FirstPage($name: String!, $first: Int!) {
  person(name: $name) {
    id
    name
    events(
      page: { first: $first }
      orderBy: { field: DATE, direction: ASC }
    ) {
      edges {
        cursor
        node { id title date }
      }
      pageInfo { hasNextPage endCursor }
      totalCount
    }
  }
}
```

**Variables**
```json
{ "name": "John Brown", "first": 10 }
```

### 2) Fetch the next page using `endCursor` ➡️

```graphql
query PersonEvents_NextPage($name: String!, $first: Int!, $after: Cursor) {
  person(name: $name) {
    id
    events(
      page: { first: $first, after: $after }
      orderBy: { field: DATE, direction: ASC }
    ) {
      edges { cursor node { id title date } }
      pageInfo { hasNextPage endCursor }
    }
  }
}
```

**Variables**
```json
{
  "name": "John Brown",
  "first": 10,
  "after": "CURSOR_FROM_PREVIOUS_PAGE_ENDCURSOR"
}
```

---

## HTTP request shape (GraphQL over POST) 🌐

> Path varies by deployment. Many setups use `/graphql`.

```bash
curl -s -X POST "$KFM_API_URL/graphql" \
  -H "content-type: application/json" \
  -H "x-request-id: demo-pagination-001" \
  -d '{
    "query": "query PersonEvents_FirstPage($name: String!, $first: Int!) { person(name: $name) { id name events(page: { first: $first }, orderBy: { field: DATE, direction: ASC }) { edges { cursor node { id title date } } pageInfo { hasNextPage endCursor } } } }",
    "variables": { "name": "John Brown", "first": 10 }
  }'
```

---

## Error contract (stable codes) 🧯

GraphQL errors SHOULD include stable `extensions.code` values for clients:

| Case | `extensions.code` | Notes |
|---|---|---|
| Cursor malformed / not decodable | `KFM_PAGINATION_INVALID_CURSOR` | fail closed |
| Cursor doesn't match filter/order | `KFM_PAGINATION_CURSOR_SCOPE_MISMATCH` | prevents data drift |
| Page size too large | `KFM_PAGINATION_PAGE_SIZE_EXCEEDED` | enforce max |
| Conflicting args (`first` + `last`) | `KFM_PAGINATION_ARGUMENT_CONFLICT` | validation |
| Access denied by policy | `KFM_POLICY_DENY` | do not leak sensitive counts |

**Example error**
```json
{
  "errors": [
    {
      "message": "Invalid cursor",
      "extensions": {
        "code": "KFM_PAGINATION_INVALID_CURSOR",
        "hint": "Cursor is malformed or expired for this query scope."
      }
    }
  ],
  "data": null
}
```

---

## Performance + safety knobs 🔧🛡️

### Recommended limits
- `defaultPageSize`: 25
- `maxPageSize`: 100 (or lower for heavy nodes)
- `maxDepth`: enforce query depth limits (graph fan-out risk)
- `maxComplexity`: optionally score queries (edges × nested selections)

### Notes for geospatial + big data 🛰️
- GraphQL should usually return **metadata and links** for large rasters (COGs, tiles, etc.)
- Feature-scale data should typically come from:
  - vector tile endpoints
  - “subset by bbox/time” REST endpoints
  - OGC-compatible interfaces (where enabled)

---

## Governance alignment (KFM-style) ⚖️🧾

Pagination MUST respect:
- **Classification** (public/sensitive/confidential)
- **Redaction rules** (e.g., fuzz coordinates)
- **No bypassing the API boundary** (UI never hits DB/graph directly)

Practical implications:
- `totalCount` may be `null` if policy blocks exposing magnitude
- list edges may be filtered per-user/role without revealing hidden items
- cursor scope binding (`filterHash`) prevents cursor reuse across different filters

---

## Implementation notes (resolver-friendly) 🧠⚙️

### Neo4j-backed connections
- Use deterministic ordering: `ORDER BY <field>, id`
- Cursor stores the last-seen ordered fields
- Prefer indexed fields for sort keys

### PostGIS-backed connections
- Keep pagination based on stable keys:
  - `created_at + id` or `date + id`
- Avoid offset for large tables (it degrades quickly)

### Anti-N+1
Use batching (DataLoader pattern) for:
- nested edges
- repeated lookups of referenced datasets, places, etc.

---

## Contract tests (add these to CI) 🧪✅

- [ ] Same query + same cursor ⇒ returns consistent next page
- [ ] No duplicates across pages
- [ ] `hasNextPage` is correct when last page is reached
- [ ] Invalid cursor returns stable `extensions.code`
- [ ] Cursor scope mismatch fails closed
- [ ] Max page size is enforced
- [ ] Policy-denied objects are not leaked via counts or cursors

---

## Quick checklist for adding a new paginated field 🧰

- [ ] Define `XEdge`, `XConnection`, and add `pageInfo`
- [ ] Add `orderBy` with a deterministic default
- [ ] Add `filter` (even if minimal) to avoid future breaking changes
- [ ] Ensure cursor includes tie-breaker (`id`)
- [ ] Add contract tests + a sample query here

---

## FAQ 🙋‍♂️

**Why not always include `totalCount`?**  
Counts can be expensive and can leak sensitive info (e.g., “how many restricted datasets exist”). Make it optional.

**Can cursors expire?**  
Yes. If upstream data is mutable, cursors may eventually become invalid. If so, return `KFM_PAGINATION_INVALID_CURSOR` with a recovery hint (restart from first page).

**Should clients decode cursors?**  
No. Treat cursors as opaque.

---

🧭 **Next:** Add sibling docs for REST pagination and UI infinite-scroll patterns so the whole platform uses one mental model.
