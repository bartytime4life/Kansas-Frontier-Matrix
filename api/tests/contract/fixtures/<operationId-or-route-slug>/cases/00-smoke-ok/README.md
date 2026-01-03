# ✅ 00-smoke-ok — Contract Fixture (Happy Path)

![case](https://img.shields.io/badge/case-00--smoke--ok-brightgreen)
![type](https://img.shields.io/badge/type-contract%20fixture-blue)
![intent](https://img.shields.io/badge/intent-smoke%20test-informational)

> 📦 **Goal:** Provide the smallest, most reliable “green path” request/response pair for this endpoint so the contract suite can confirm the API is alive, compatible, and schema-valid.

---

## 🧭 Context

This folder lives at:

```text
api/tests/contract/fixtures/<operationId-or-route-slug>/cases/00-smoke-ok/
```

Think of this case as the **baseline** for the endpoint: the first, easiest request that *must* keep working as the contract evolves.

---

## 🎯 What this case proves

✅ **Smoke-ok** means:

- The endpoint is reachable (routing works)
- Authentication/authorization (if required) is satisfied for a minimally scoped identity
- Request shape is valid per contract
- Response is a **2xx** (typically `200`, `201`, or `204`)
- Response body (if present) matches the **contract schema**
- Response is **deterministic enough** to be asserted in CI (no flaky timestamps / random IDs without normalization)

> [!NOTE]
> This is intentionally *not* an exhaustive test. It’s a “does the contract still hold?” safety line.

---

## 🧾 Endpoint metadata

Fill these in to keep fixtures self-documenting 👇

| Field | Value |
|---|---|
| 🔖 Operation (operationId / slug) | `<operationId-or-route-slug>` |
| 🛣️ Route | `<METHOD> <PATH>` (ex: `GET /api/v1/foo/{id}`) |
| 🔐 Auth | `none` \| `bearer` \| `apiKey` \| `session` |
| ✅ Expected status | `2xx` (exact: `<200/201/204>` ) |
| 🧩 Primary response schema | `<SchemaName>` |
| 🏷️ Tags | `smoke`, `happy-path`, `contract` |

---

## 🗂️ Case contents

> [!TIP]
> Keep files **minimal**. If the harness doesn’t use a file type, don’t add it “just in case” — that becomes drift.

Recommended layout (adjust filenames to match the harness conventions used in this repo):

```text
📁 cases/00-smoke-ok/
├── 📄 README.md                 # you are here
├── 📄 request.json              # request body (optional; for POST/PUT/PATCH)
├── 📄 request.headers.json      # headers (optional)
├── 📄 request.query.json        # query params (optional)
├── 📄 request.path.json         # path params (optional)
├── 📄 response.json             # expected response body (optional for 204)
├── 📄 response.headers.json     # expected key headers (optional)
└── 📄 notes.md                  # optional: clarifications / rationale
```

### 🔎 File expectations

| File | When to include | Rules |
|---|---|---|
| `request.json` | Body endpoints | No secrets; stable values |
| `request.headers.json` | If required | Only include headers you truly need |
| `request.query.json` | If query params exist | Prefer explicit defaults |
| `request.path.json` | If path params exist | Prefer stable IDs (seeded or well-known fixtures) |
| `response.json` | Most 2xx responses | Avoid volatile fields unless normalized/ignored |
| `response.headers.json` | If headers are contract-relevant | Assert only “contracted” headers |
| `notes.md` | If anything is non-obvious | Keep it short + actionable |

---

## 🧪 Scenario definition

### ✅ Preconditions

- Environment has the minimal required dependencies (DB, services, etc.)
- Any needed seed data exists (prefer seeded fixtures over “whatever is in dev DB”)
- If auth is required, a test principal exists with the smallest scope needed

### 📤 Request (happy path)

- **Method/Path:** `<METHOD> <PATH>`
- **Auth:** `<none|bearer|...>`
- **Headers:** minimal required
- **Payload:** minimal valid payload (if applicable)

### 📥 Expected response

- **Status:** `<2xx>`
- **Schema:** `<SchemaName>`
- **Key invariants:**
  - `id` fields are stable OR validated by pattern rules
  - `timestamps` are stable OR excluded from strict equality
  - pagination defaults are explicit (if relevant)

---

## 🧬 Determinism rules (non‑negotiable)

> [!WARNING]
> Contract fixtures should be CI-safe. If this case flakes, it defeats the whole point.

✅ Do:

- Use fixed inputs (stable IDs, stable payload values)
- Prefer **explicit defaults** (page size, sort order, locale/timezone)
- If the API returns generated fields, configure the harness to:
  - ignore them, or
  - validate them with a pattern (UUID/date), or
  - assert only presence, not exact value

🚫 Don’t:

- Commit real tokens, API keys, cookies, or PII
- Depend on “current time”, random seeds, external networks, or shared dev state
- Assert entire blobs if only a few fields are meaningful contract-wise

---

## 🧰 Running the contract test

Because harnesses vary by repo, keep this section aligned with your actual runner.

### Suggested patterns

<details>
<summary>🖥️ Example commands (replace with the one that exists in this repo)</summary>

```bash
# Run all contract tests
make test-contract

# Run only this endpoint (example)
make test-contract OP=<operationId-or-route-slug>

# Run only this case (example)
make test-contract OP=<operationId-or-route-slug> CASE=00-smoke-ok
```

</details>

> [!TIP]
> If your runner supports filtering by `operationId`, always prefer that over brittle path-based filtering.

---

## ✅ Definition of done

- [ ] This case passes locally
- [ ] This case passes in CI
- [ ] No secrets / tokens / PII committed
- [ ] Response assertions are stable (no flaky fields)
- [ ] README fields are filled in (route/method/status/schema)
- [ ] If contract changed, versioning/compat checks were considered 🧾

---

## 🔗 Related docs

- 📄 `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` — use when adding/changing endpoints
- 📁 `src/server/` — canonical home for API code & contracts (OpenAPI/GraphQL)
- 🧪 `api/tests/contract/` — contract validation suite entrypoint (runner, helpers, etc.)

---

## 📝 Notes

Add quick rationale here when needed, e.g.:

- why a specific ID is chosen
- why a field is ignored
- why status is `204` vs `200`
- what seed data is assumed

