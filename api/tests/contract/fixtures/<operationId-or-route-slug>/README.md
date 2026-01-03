# 🧪 Contract Fixtures — `<operationId-or-route-slug>`

![contract](https://img.shields.io/badge/contract-tests-blue) ![openapi](https://img.shields.io/badge/OpenAPI-contract--first-6f42c1) ![fixtures](https://img.shields.io/badge/fixtures-golden%20files-orange) ![safety](https://img.shields.io/badge/safety-no%20secrets%20%7C%20no%20PII-success)

> [!IMPORTANT]
> This folder contains **golden request/response fixtures** for **one** API operation.  
> Contract tests use these fixtures to ensure the endpoint stays **backwards-compatible**, **deterministic**, and **safe-to-publish** (no secrets / no sensitive content).

---

## 🎯 What lives here

- ✅ **Known inputs** (request fixtures)
- ✅ **Expected outputs** (response fixtures)
- ✅ **Optional assertions** beyond schema validation (sorting, stable IDs, etc.)
- ✅ **Redaction / normalization rules** for dynamic fields (timestamps, UUIDs, etc.)
- ✅ Notes about **why** the contract behaves this way (edge cases, invariants)

- ❌ No production secrets, API keys, tokens, passwords  
- ❌ No personal data (PII) or sensitive coordinates (unless explicitly redacted / generalized)  
- ❌ No “random” responses that can drift between runs (fixtures must remain stable)

---

## 🧾 Operation snapshot (fill this in ✍️)

| Field | Value |
|---|---|
| **operationId** | `<operationId>` |
| **method** | `<GET|POST|PUT|PATCH|DELETE>` |
| **path** | `/<version>/<route>` |
| **Contract source** | `src/server/contracts/<openapi-file>.(yaml|json)` *(or repo-equivalent)* |
| **Primary owner** | `@<team-or-handle>` |
| **Fixture dataset / seed** | `<fixture-dataset-id-or-seed>` |
| **Last verified** | `YYYY-MM-DD` |

> [!TIP]
> If you’re not sure what the `operationId` is: look in the OpenAPI contract for `operationId:` on this route, or check the generated OpenAPI JSON from the running service.

---

## 🏷️ Folder naming rules

This folder must be named as:

1) **Preferred:** the OpenAPI `operationId` (stable, human-readable)  
2) **Fallback:** a deterministic route slug derived from method + path

### ✅ Recommended slug algorithm (fallback)

- Start with lowercase HTTP method  
- Add path segments separated by `__`  
- Replace `{param}` segments with `by-<param>`  
- Keep only `[a-z0-9._-]` (normalize anything else)

**Example:**  
`GET /v1/stac/collections/{collectionId}` → `get__v1__stac__collections__by-collectionId`

---

## 🗂️ Suggested directory layout

```text
📁 api/tests/contract/fixtures/<operationId-or-route-slug>/
├── 📄 README.md                 # you are here ✅
├── 📄 meta.json                 # optional: fixture catalog + provenance pointers
└── 📁 cases/
    ├── 📁 happy-path/
    │   ├── 📄 request.json
    │   ├── 📄 response.json
    │   └── 📄 assertions.json   # optional
    ├── 📁 not-found/
    │   ├── 📄 request.json
    │   └── 📄 response.json
    └── 📁 validation-error/
        ├── 📄 request.json
        └── 📄 response.json
```

> [!NOTE]
> If the operation only needs **one** canonical example, you can still use `cases/happy-path/` — it scales better than placing files at the root.

---

## 🧩 Fixture formats

### `meta.json` (optional but recommended)

Use this when you want fixtures to be self-describing (and easy to lint/scan):

```json
{
  "operationId": "<operationId>",
  "method": "<METHOD>",
  "path": "/<version>/<route>",
  "contract": "src/server/contracts/<openapi-file>.yaml",
  "cases": [
    "happy-path",
    "not-found"
  ],
  "fixture_dataset": "<fixture-dataset-id-or-seed>",
  "notes": "Short rationale: what this endpoint guarantees, and what it must never leak."
}
```

### `request.json`

```json
{
  "method": "<METHOD>",
  "path": "/<version>/<route>",
  "pathParams": {
    "id": "example-id"
  },
  "query": {
    "limit": 10
  },
  "headers": {
    "accept": "application/json"
  },
  "body": null
}
```

### `response.json`

```json
{
  "status": 200,
  "headers": {
    "content-type": "application/json"
  },
  "body": {
    "example": "payload"
  }
}
```

### `assertions.json` (optional)

Use this when schema validation isn’t enough (e.g., stable ordering, derived fields, redaction guarantees):

```json
{
  "jsonpath": [
    { "path": "$.items", "rule": "sorted_by", "value": "id" },
    { "path": "$.provenance", "rule": "exists" }
  ],
  "invariants": [
    "no_secrets",
    "no_pii",
    "no_sensitive_coordinates"
  ]
}
```

> [!TIP]
> Keep assertions **contract-level** (shape + invariants). Avoid asserting internal implementation details.

---

## 🧼 Normalization rules (avoid flaky fixtures)

Many APIs include **legit** dynamic data (timestamps, UUIDs, generated filenames). Flaky fixtures break trust.

Recommended approach:

- Prefer **schema validation** + **invariants** over byte-for-byte equality
- If golden-file comparison is used, **normalize** fields that are expected to vary

### Common “dynamic” fields to normalize

- `createdAt`, `updatedAt`, `generatedAt`
- `requestId`, `traceId`
- UUIDs that are not semantically meaningful
- Signed URLs / expiring links
- Geo precision that can change due to formatting (rounding)

### Suggested placeholder tokens (if your runner supports it)

- `__ANY_UUID__`
- `__ISO_DATETIME__`
- `__ANY_STRING__`
- `__REDACTED__`

> [!IMPORTANT]
> Never normalize away **safety-critical** checks.  
> Example: if a field must be redacted, assert it is redacted (don’t ignore it).

---

## 🔒 Safety, governance, and “don’t leak data” rules

Because fixtures are committed to the repo, treat them like **published artifacts**:

- 🔐 **No secrets** (keys, tokens, passwords, cookies)
- 🧍 **No PII** (names, emails, phone numbers, addresses, personal identifiers)
- 📍 **No sensitive locations** (precise coordinates where policy requires generalization)
- 🏷️ Keep any “classification” markers consistent with the most restrictive upstream input

**If you must include realistic content:**
- Use synthetic or heavily redacted samples
- Prefer broad/generalized geometry (e.g., bounding boxes, rounded coordinates)
- Leave a note in `meta.json` explaining the redaction strategy

---

## ♻️ When to update these fixtures

Update fixtures when:

- ✅ The OpenAPI contract changes (new fields, renamed fields, new status codes)
- ✅ The endpoint output changes in a backwards-compatible way (new optional fields)
- ✅ Redaction or governance rules change
- ✅ A bug fix changes canonical behavior (and should be locked in)

> [!WARNING]
> If the change is **breaking** (removing fields, changing required behavior), treat it as a **version bump** or a new endpoint variant — don’t silently overwrite fixtures that represent a stable contract.

---

## ✅ PR checklist (quick gate)

- [ ] Contract updated **first** (OpenAPI/GraphQL) 🧾
- [ ] Fixture payloads are **minimal** but representative 🎯
- [ ] Fixtures are **deterministic** (no `now()`, no random drift) 🧊
- [ ] No secrets / PII / sensitive coordinates 🔒
- [ ] New/changed cases documented in this README 📝
- [ ] Contract tests pass locally + in CI 🧪

---

## 🧯 Troubleshooting

<details>
<summary><strong>Fixtures keep failing because timestamps/IDs change</strong> ⏱️</summary>

- Ensure your test environment uses a fixed clock (or known seed)
- Normalize volatile fields (timestamps, request IDs) **only if** they’re not contract-critical
- Prefer schema validation + invariants if possible

</details>

<details>
<summary><strong>Fixture diffs are huge</strong> 📦</summary>

- Reduce payload size: smaller limits, narrower query, fewer nested objects
- Store only the contract-relevant subset (don’t snapshot entire datasets)
- Add a targeted invariant test instead of snapshotting everything

</details>

<details>
<summary><strong>Governance scan flags the fixture</strong> 🚨</summary>

- Remove secrets immediately and rotate if needed
- Redact or synthesize PII-like fields
- Generalize coordinates and document the approach in <code>meta.json</code>

</details>

---

## 📎 Notes specific to this operation (optional)

Use this space to record any endpoint-specific “why”:

- Expected ordering guarantees (e.g., sorted by `id`)
- Known edge cases (empty result sets, pagination boundaries)
- Security model expectations (auth required, scopes, redaction)
- Provenance expectations (e.g., response must include catalog/prov links)

🧠 **Keep it short, but keep it honest.**

