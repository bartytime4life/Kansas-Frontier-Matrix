# 🚫🧪 Contract Case: `POST /v1/layers` — Invalid Body

![contract](https://img.shields.io/badge/tests-contract-blue?style=flat-square)
![negative](https://img.shields.io/badge/case-negative-red?style=flat-square)
![endpoint](https://img.shields.io/badge/endpoint-POST%20%2Fv1%2Flayers-6f42c1?style=flat-square)
![version](https://img.shields.io/badge/api-v1-black?style=flat-square)

> 🎯 **Purpose:** Prove the API rejects malformed / schema-invalid request bodies for `POST /v1/layers` and returns a **stable, contract-defined** validation error (no side effects, no stack traces).

---

## 📌 At a glance

| Item | Value |
|---|---|
| Case ID | `POST__v1_layers__invalid_body` |
| Method | `POST` |
| Path | `/v1/layers` |
| Category | Request validation (negative) |
| Expected result | `4xx` + structured error payload (as defined by the API contract) |
| Must NOT happen | Layer creation / persistence / background jobs triggered ✅ |

---

## 🧠 Why this contract case exists

This repo follows a **contract-first** approach: schemas + API specs are treated as **first-class artifacts**, and changes to them require deliberate versioning and compatibility decisions. That means **invalid inputs must fail deterministically**, and the failure format must remain consistent for clients and tooling. 🧱📜

---

## ✅ Scenario definition (Given / When / Then)

### Given
- The client is **authorized enough** to reach request validation (i.e., auth should not be the reason the request fails).
- The API server is running with the current contract loaded (OpenAPI / schema layer).

### When
- A request is made to `POST /v1/layers` with a JSON body that violates the request schema, such as:
  - missing required fields
  - wrong data types (string where number is required, etc.)
  - invalid enum values
  - wrong nesting / shape
  - unexpected nulls where forbidden

### Then
- The API responds with:
  - a **4xx** validation-style status code (commonly `400` or `422`, depending on the service’s contract), **and**
  - a **machine-readable** JSON error body (shape defined by the API contract / captured in fixtures)
- The API does **not** create a layer, mutate state, enqueue jobs, or return an internal stack trace.

---

## 📂 Files in this case folder

> 🔍 The contract runner for this repo reads fixtures from this folder. Keep them small and deterministic.

Typical contents:

```text
📁 api/tests/contract/cases/POST__v1_layers__invalid_body/
├── README.md                    👈 you are here
├── request.json                 📨 the intentionally invalid request payload
├── expected.response.json       🧾 expected error response payload (contract-locked)
├── expected.status.txt          🔢 expected HTTP status code (if your runner separates it)
└── meta.json / headers.json     🧩 optional (auth headers, content-type, notes)
```

> 📝 If your runner uses different filenames, follow what already exists in this folder and keep the README aligned with the real fixture names.

---

## 📨 Request (invalid)

- **Content-Type:** `application/json`
- **Body:** intentionally violates the `POST /v1/layers` request schema

<details>
  <summary>🧪 Example invalid payload patterns (illustrative only)</summary>

```json
{}
```

```json
{
  "name": 123,
  "source": null,
  "type": "definitely-not-a-valid-enum"
}
```

> ✅ Pick **one** deterministic invalid pattern in `request.json` and keep it stable.
</details>

---

## 🧾 Expected response (validation error)

This case asserts the API returns a stable, contract-defined validation response.

**Hard requirements:**
- **4xx** response (no 5xx)
- **JSON** error body
- No internal stack trace / debug dump
- Contains enough detail for clients to correct the request (at least a message + path/field info)

<details>
  <summary>📦 Example validation response shapes (illustrative only)</summary>

### Example A: “details” array (FastAPI-style)
```json
{
  "detail": [
    {
      "loc": ["body", "name"],
      "msg": "Field required",
      "type": "missing"
    }
  ]
}
```

### Example B: “error” envelope (custom API style)
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request body failed validation",
    "details": [
      { "path": "/name", "issue": "required" }
    ]
  }
}
```
</details>

> 🔒 **Source of truth:** the expected status/body should match the fixtures in this folder **and** the service’s OpenAPI/contract definitions for `POST /v1/layers`.

---

## 🏃 How to run (locally)

Because teams wire contract runners differently, use this pattern:

1) **Find the contract test command**
```bash
# from repo root
rg -n "contract" api/package.json api/pyproject.toml api/Makefile api/README.md || true
```

2) **Run contract tests**
- Run the repo’s contract test target/script (whatever you find in step 1).

3) **Run just this case (if supported)**
Common patterns include:
```bash
# pytest-style (example)
pytest -k POST__v1_layers__invalid_body
```

```bash
# node-style (example)
npm run test:contract -- POST__v1_layers__invalid_body
```

> ✅ If your runner doesn’t support filtering, run the whole contract suite and confirm this case passes.

---

## 🔁 When to update this case

Update this case if you change any of the following:
- `POST /v1/layers` request schema (required fields, types, enums, nesting)
- global validation error formatting / error envelope
- status code policy for invalid bodies (e.g., `400` → `422`)

**Update checklist:**
- [ ] Ensure `request.json` is still **invalid** under the *new* schema
- [ ] Update `expected.*` fixtures to match the new contract behavior
- [ ] If the change is breaking for clients, consider **API versioning** (v2 path, negotiation, or deprecation plan) 🧭

---

## 🧯 Troubleshooting

### “This case started failing, but only because the error message wording changed”
- If the contract promises stable human-readable strings, update fixtures accordingly.
- If the contract only promises machine codes/paths, prefer asserting those instead (to avoid brittle tests).

### “It returns 401/403 instead of a validation error”
- Ensure the test harness authenticates sufficiently to reach request parsing/validation.
- This case is about **body validation**, not auth.

### “It returns 500”
- That’s a bug or missing validation guardrail. 🚨  
  Invalid user input should never crash the service.

---

## 🔗 Related contract artifacts (where to look)

To find the canonical definition for this endpoint in the repo:

```bash
# from repo root
rg -n "(/v1/layers|POST\\s+/v1/layers|post:\\s*/v1/layers)" -S .
```

Typical locations (project-dependent):
- OpenAPI spec (YAML/JSON)
- Request/response JSON Schemas
- Server route handler for `/v1/layers`

---

🧩 **Reminder:** A negative contract case is a guardrail — it proves the system fails **cleanly**, **predictably**, and **without side effects** when clients send bad input.

