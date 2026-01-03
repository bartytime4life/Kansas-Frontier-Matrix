# 🧪 GraphQL Contract Test Operations

![GraphQL](https://img.shields.io/badge/GraphQL-operations-E10098?logo=graphql&logoColor=white)
![Contract Tests](https://img.shields.io/badge/contract-tests-✅-success)
![Backwards Compatible](https://img.shields.io/badge/backwards--compatible-required-blue)
![Deterministic](https://img.shields.io/badge/deterministic-outputs-important)

Welcome! 👋 This folder contains the **canonical GraphQL operations** (queries + mutations) that our **contract test suite** executes to ensure the API behaves as expected for **known inputs → known outputs**.

> ✅ Goal: Catch breaking changes **before** they hit the UI or downstream systems.  
> 🧱 Philosophy: **Contract-first** — operations here represent “what clients rely on”.

---

## 📌 Quick navigation

- [Why this folder exists](#-why-this-folder-exists)
- [What belongs here](#-what-belongs-here)
- [Recommended structure](#-recommended-structure)
- [Operation conventions](#-operation-conventions)
- [Add a new operation](#-add-a-new-operation)
- [Update an operation safely](#-update-an-operation-safely)
- [Run locally](#-run-locally)
- [Troubleshooting](#-troubleshooting)
- [PR checklist](#-pr-checklist)

---

## 🎯 Why this folder exists

GraphQL schema linting is useful… but it’s not enough.

Contract operations validate **real behavior**:
- Resolver output shapes 🧩
- Required fields ✅
- Authorization/redaction expectations 🔐
- Pagination + sorting stability 📚
- Error behavior consistency ⚠️

In CI, these operations are executed against a test environment (or mocked fixtures), and responses are validated so that “silent breakage” doesn’t slip into main. 🚦

---

## ✅ What belongs here

This directory should contain **client-representative** operations that are:
- **Stable** (not experimental)
- **Deterministic** (same input ⇒ same output)
- **Minimal** (request only what’s needed for the contract)

Typical artifacts per operation:
- `*.graphql` operation document
- `variables.*` file (JSON preferred)
- `expected.*` snapshot (JSON) *or* matcher-based contract file

> ⚠️ Keep secrets, tokens, private keys, or real PII **out** of this folder.

---

## 🗂️ Recommended structure

Follow the existing local convention in this repo. If you’re adding new operations, the *recommended* scalable layout is **one folder per operation**:

```text
📁 api/
└─📁 tests/
  └─📁 contract/
    └─📁 graphql/
      └─📁 operations/
        ├─📄 README.md  👈 you are here
        ├─📁 GetSomething/
        │  ├─📄 operation.graphql
        │  ├─📄 variables.json
        │  ├─📄 expected.json
        │  └─📄 notes.md            # optional: context + business meaning
        └─📁 MutateSomething/
           ├─📄 operation.graphql
           ├─📄 variables.json
           ├─📄 expected.json
           └─📄 matchers.json       # optional: tolerant matching rules
```

If the repo uses a **flat layout**, that’s also acceptable:

```text
📁 operations/
├─📄 GetSomething.graphql
├─📄 GetSomething.variables.json
├─📄 GetSomething.expected.json
```

---

## 🧩 Operation conventions

### 1) Naming
- ✅ **Operation name is required** (GraphQL best practice + helps reporting)
- ✅ Use **PascalCase** for operation names
- ✅ Keep folder/file names aligned with the operation name

Examples:
- `query GetMapLayers { ... }`
- `mutation UpdateUserPreferences { ... }`

---

### 2) Deterministic outputs (avoid flaky tests 😵‍💫)
To keep contract tests stable:
- Prefer queries that return **deterministically ordered** lists  
  - Use explicit `orderBy`, `sort`, or stable pagination whenever available
- Avoid volatile fields unless you can match loosely:
  - `createdAt`, `updatedAt`, “lastSeen”, random IDs, server timestamps
- If you must include volatile fields:
  - Use matchers (regex/range) or omit them from strict snapshot comparison

---

### 3) Use variables (don’t hardcode values)
✅ Do this:
```graphql
query GetLayer($id: ID!) {
  layer(id: $id) { id name }
}
```

❌ Not this:
```graphql
query GetLayer {
  layer(id: "123") { id name }
}
```

Variables make operations reusable and reduce churn in snapshots.

---

### 4) Keep selection sets tight ✂️
Contract operations are **not** “dump everything” queries.

A good rule:
- Request the minimum fields needed to represent the contract
- Add deeper fields only when they’re part of a stable client dependency

---

### 5) Unions/interfaces: include `__typename`
For stable matching + readability:
```graphql
... on SomeType { __typename id }
```

---

## ➕ Add a new operation

### Step-by-step 🚀

1) **Create a new operation folder**
```text
📁 operations/
└─📁 MyNewOperation/
```

2) **Add the GraphQL document**
`operation.graphql` (recommended file name)

```graphql
# Contract Operation: MyNewOperation
# Purpose: Describe what client behavior this protects.
# Owner: @team-or-handle
# Notes: Keep deterministic & minimal.

query MyNewOperation($input: MyInput!) {
  myField(input: $input) {
    id
    name
  }
}
```

3) **Add variables**
`variables.json`
```json
{
  "input": {
    "example": "value"
  }
}
```

4) **Generate expected output**
Run the contract test runner to record the snapshot, or capture the response and store it as:
- `expected.json` (strict snapshot), or
- `matchers.json` (tolerant matching), depending on harness rules.

5) **Verify locally**
Run the GraphQL contract test suite and confirm:
- ✅ passes locally
- ✅ passes in CI
- ✅ no secrets / PII

---

## ♻️ Update an operation safely

### ✅ Non-breaking change
Examples:
- Adding fields to a response the client expects ✅
- Adding new optional arguments ✅

Process:
1) Update `operation.graphql`
2) Update `expected.json` (or matchers)
3) Ensure older clients are not broken

### ⚠️ Potential breaking change
Examples:
- Removing/renaming fields
- Changing field types
- Changing semantics of outputs clients depend on

Safer pattern:
- Keep the old operation (or introduce a versioned alternative)  
  e.g. `GetLayer_v2` / `layerV2` / new versioned endpoint strategy

> If you’re making breaking API changes, treat it as a **versioning event**, not just a snapshot update.

---

## 🏃 Run locally

Because contract runners vary by repo, use the project’s existing test entrypoint. Common patterns:

```bash
# Option A: JS/TS monorepo
npm run test:contract -- graphql

# Option B: pnpm
pnpm test:contract graphql

# Option C: Python
pytest -k contract_graphql
```

If you’re not sure which command is wired up:
- search package scripts / Makefile targets for: `contract`, `graphql`, `pact`, `snapshot`

---

## 🧯 Troubleshooting

<details>
<summary><strong>“Cannot query field … on type …”</strong> (schema mismatch)</summary>

- The operation is out of date vs the schema.
- Update the operation **or** update the schema/SDL and ensure compatibility.
</details>

<details>
<summary><strong>Snapshots failing due to ordering</strong> (flaky list results)</summary>

- Add explicit ordering arguments if the API supports them.
- If not supported, consider adding stable ordering server-side for contract endpoints.
</details>

<details>
<summary><strong>Unauthorized / forbidden responses</strong></summary>

- Ensure the contract harness is providing required auth context.
- If the operation is meant to be public, verify auth requirements did not accidentally tighten.
</details>

<details>
<summary><strong>Volatile fields breaking snapshots</strong> (timestamps, IDs, etc.)</summary>

- Prefer omitting volatile fields.
- Otherwise introduce matchers / partial snapshot comparison.
</details>

---

## ✅ PR checklist

Before merging changes in this folder:

- [ ] Operation has a clear, unique **operation name**
- [ ] Operation is **minimal** but covers the real client dependency
- [ ] Uses **variables** (no hardcoded IDs unless justified)
- [ ] Response is **deterministic** (sorting/pagination stable)
- [ ] `expected.json` (and/or matchers) updated intentionally
- [ ] No secrets, tokens, real PII, or sensitive coordinates included 🔐
- [ ] Contract tests pass locally and in CI 🚦

---

## 📎 Related pointers

- 📜 GraphQL schema/SDL should live in the server “contracts” area (e.g. `src/server/contracts/` or equivalent).
- 🧱 If you’re changing API shape/behavior, be sure you’re aligning with the repo’s **contract-first** and **versioning** rules.

Happy testing! 🧪✨

