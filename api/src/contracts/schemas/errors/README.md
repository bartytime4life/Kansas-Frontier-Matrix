# 🚨 API Error Schemas (Contract)  
📍 Path: `api/src/contracts/schemas/errors/`

These JSON Schemas define the **canonical error response shapes** for the governed KFM API.  
They are treated as **contract artifacts**: machine-validated interface definitions that must be versioned and honored. :contentReference[oaicite:0]{index=0}

---

## ✨ Why this folder exists (contract-first, not “docs-later”)

KFM runs **contract-first**: schemas + API contracts are **first-class repo artifacts**. Development starts from the contract, and any change triggers compatibility/versioning checks. :contentReference[oaicite:1]{index=1}

Also: the **UI ↔ API boundary is non-negotiable**—the UI never bypasses the governed API. That makes error shapes *part of the boundary contract* and therefore must remain stable. :contentReference[oaicite:2]{index=2}

---

## 🗂️ What should live here

📁 `api/src/contracts/schemas/errors/`  
- 📄 `README.md` (this file)  
- 📄 JSON Schemas for:
  - ✅ **Base error envelope** (all error responses)
  - ✅ **Validation errors** (field-level problems)
  - ✅ Optional specializations (auth, rate limit, not found) *if the base schema can’t express it cleanly*

> **Rule of thumb:** Prefer **one stable envelope** + **error codes** over many bespoke shapes.

---

## 🧱 Contract artifact rules (the “do not break” posture)

A “contract artifact” is a machine-validated schema/spec that defines an interface (JSON Schema, OpenAPI, etc.), and **must be versioned** with **no breaking changes without a version bump**. :contentReference[oaicite:3]{index=3}

For KFM APIs specifically: APIs must remain backwards-compatible unless a version bump is declared, and contract changes are tested against known inputs/outputs. :contentReference[oaicite:4]{index=4}

---

## ✅ Error response contract (recommended standard)

### 🎁 Base envelope: `ErrorResponse`

**Top-level**
- `requestId` *(string)* — correlation ID (support + logs)  
- `status` *(integer)* — HTTP status code  
- `code` *(string)* — stable machine-readable error code  
- `message` *(string)* — user-safe, human-readable summary  
- `details` *(object | null)* — optional, **client-actionable** structured details  
- `meta` *(object | null)* — optional metadata (timestamps, retry hints)

### 📌 Example (generic error)
```json
{
  "requestId": "req_01HTYQ7YF8KZ9C3GQ8B8P2K8GZ",
  "status": 500,
  "code": "KFM_INTERNAL_ERROR",
  "message": "Something went wrong on our side. Please try again.",
  "details": null,
  "meta": {
    "retryable": true
  }
}
```

---

## 🧾 Validation errors (client-fixable)

### ✅ Validation envelope: `ValidationErrorResponse`

Use the same envelope, but include structured field issues:

- `details.invalidFields[]`
  - `path` *(string)* — JSON path or dot path (e.g., `filters.dateRange.start`)
  - `reason` *(string)* — what failed (human-safe)
  - `expected` *(string | null)* — optional constraint description
  - `received` *(string | null)* — optional *safe* value hint (⚠️ see security rules)

### 📌 Example (400 validation)
```json
{
  "requestId": "req_01HTYQ8A6N9H0ZP8M6V8K2F4XN",
  "status": 400,
  "code": "KFM_VALIDATION_FAILED",
  "message": "Some inputs are invalid. Please review the highlighted fields and try again.",
  "details": {
    "invalidFields": [
      {
        "path": "filters.dateRange.start",
        "reason": "Must be an ISO-8601 date (YYYY-MM-DD).",
        "expected": "date",
        "received": "13/32/2025"
      }
    ]
  },
  "meta": {
    "retryable": false
  }
}
```

---

## 🧠 Error code conventions

### ✅ Format
Use stable, searchable codes:

`KFM_<DOMAIN>_<CATEGORY>_<NAME>`

Examples:
- `KFM_AUTH_UNAUTHORIZED`
- `KFM_AUTH_FORBIDDEN`
- `KFM_RATE_LIMIT_EXCEEDED`
- `KFM_RESOURCE_NOT_FOUND`
- `KFM_VALIDATION_FAILED`
- `KFM_CONFLICT_VERSION_MISMATCH`

### 🧩 Categories (suggested)
- `AUTH` — authentication/authorization
- `VALIDATION` — input problems
- `RESOURCE` — not found / missing
- `CONFLICT` — concurrency/versioning conflicts
- `RATE_LIMIT` — throttling
- `INTERNAL` — unexpected server failures
- `DEPENDENCY` — upstream system failures

> Keep codes stable. If wording changes, change `message`, not `code`.

---

## 🔒 Security, governance, and sovereignty rules (errors are not exempt)

### 🧱 API boundary enforcement
Because the UI must route through the governed API layer, the API is responsible for enforcing access control, redaction, and schema consistency. Errors are part of what the UI sees—so they must uphold the same enforcement expectations. :contentReference[oaicite:5]{index=5}

### 🪶 Sovereignty & classification propagation
KFM requires that **no output artifact can be less restricted than its inputs**. Don’t leak restricted info in error payloads (even “helpful” debugging). :contentReference[oaicite:6]{index=6}

### 🕵️ Secrets + PII awareness (CI will scan)
CI includes automated scans for secrets, personal data, sensitive locations, and classification consistency. Error examples and fixtures are scanned too—so keep them clean. :contentReference[oaicite:7]{index=7}

**Practical rules**
- ✅ **Never** include stack traces, raw SQL, internal hostnames, tokens, or secrets in responses.
- ✅ For 5xx: keep `message` generic; rely on `requestId` for support correlation.
- ✅ In `details.received`: include only safe hints (avoid full emails, names, coordinates, or identifiers).
- ✅ If the failure involves protected locations or sensitive datasets: return a generic message and do not echo the sensitive values.

---

## 🧑‍🤝‍🧑 Human-centered messaging guidelines

Even in technical docs and user-facing output, KFM expects a respectful tone that focuses on human context—explaining not only *what* happened but *why it helps the user or system goals*. Apply that to error `message` content. :contentReference[oaicite:8]{index=8}

**Messaging checklist**
- ✅ Plain language (no internal jargon)
- ✅ Actionable next step when possible (“Check dates”, “Sign in again”, “Try later”)
- ✅ No blame (“You did X wrong”) → prefer “We couldn’t process X”
- ✅ Avoid exposing sensitive implementation details

---

## 🔄 Versioning policy (breaking changes are real)

Any breaking change to an API requires a new versioned endpoint or negotiation strategy; e.g., introduce `v2` at a new path and retain `v1` (or sunset with notice). The OpenAPI definition is the contract; breaking it means incrementing the version. :contentReference[oaicite:9]{index=9}

### ✅ What counts as breaking for error schemas?
- ❌ Renaming fields
- ❌ Changing types (string → object)
- ❌ Removing fields that clients may rely on
- ❌ Changing semantics of `code` values

### ✅ What is typically non-breaking?
- ✅ Adding **optional** fields
- ✅ Adding **new** error codes (keeping old ones)
- ✅ Adding **new** `details.*` sub-objects that are optional

> If in doubt: treat it as breaking, and version accordingly.

---

## 🧪 CI + contract tests expectations (how this stays enforced)

KFM CI performs:
- ✅ JSON Schema validation for structured outputs (schemas must remain correct) :contentReference[oaicite:10]{index=10}
- ✅ API contract tests ensuring endpoints respond as expected and changes remain compatible (or tests are updated intentionally) :contentReference[oaicite:11]{index=11}
- ✅ Security/governance scans for secrets + PII + sensitive content + classification consistency :contentReference[oaicite:12]{index=12}

Also: contributions must pass validation gates enforcing invariants; failures block merges. :contentReference[oaicite:13]{index=13}

---

## 🧩 OpenAPI wiring pattern (how endpoints should reference these)

**Intent:** every endpoint’s error responses should reference the schemas here so the contract is centralized.

```yaml
# Pseudocode snippet (structure only)
responses:
  "400":
    description: Validation failed
    content:
      application/json:
        schema:
          $ref: "./schemas/errors/ValidationErrorResponse.schema.json"
  "401":
    description: Unauthorized
    content:
      application/json:
        schema:
          $ref: "./schemas/errors/ErrorResponse.schema.json"
  "500":
    description: Internal error
    content:
      application/json:
        schema:
          $ref: "./schemas/errors/ErrorResponse.schema.json"
```

> Keep the **shape stable**. Use `code` to express specificity.

---

## ✅ Contributor checklist (when you touch error contracts)

- [ ] 🧠 Start from the contract (schema + OpenAPI), not implementation. :contentReference[oaicite:14]{index=14}
- [ ] 🧱 Confirm the change is non-breaking; if breaking, plan `/vN/` versioning. :contentReference[oaicite:15]{index=15}
- [ ] 🧪 Add/update API contract tests to lock behavior. :contentReference[oaicite:16]{index=16}
- [ ] 🧾 Ensure JSON Schema validation passes. :contentReference[oaicite:17]{index=17}
- [ ] 🔒 Verify no secrets/PII/sensitive locations appear in payloads/examples. :contentReference[oaicite:18]{index=18}
- [ ] 🧑‍🤝‍🧑 Ensure `message` is respectful + actionable. :contentReference[oaicite:19]{index=19}

---

## 📚 Related KFM invariants (why errors matter beyond “API cosmetics”)

- Pipeline ordering is strict, and the API is the boundary before UI consumption. :contentReference[oaicite:20]{index=20}
- The UI must not bypass the governed API layer. :contentReference[oaicite:21]{index=21}
- Sovereignty/classification cannot be downgraded through outputs (including error payloads). :contentReference[oaicite:22]{index=22}

---

## 🧭 Next additions (optional but recommended)

📌 If not already present in this folder, consider adding:
- `ErrorResponse.schema.json`
- `ValidationErrorResponse.schema.json`
- `ErrorCode.enum.json` (or a generated reference list)
- `examples/` fixtures used by contract tests (sanitize hard!)

---

> 🧩 Bottom line: Errors are **part of the governed interface**, not an afterthought. Treat them like a public API surface—because they are.

