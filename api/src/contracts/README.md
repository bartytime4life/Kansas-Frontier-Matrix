<!-- 📍 Path: api/src/contracts/README.md -->

# 📜 API Contracts

![Contract-First](https://img.shields.io/badge/Contract--First-Required-2ea44f)
![Backwards-Compatible](https://img.shields.io/badge/Backwards%20Compatible-Default-2ea44f)
![Governed-API](https://img.shields.io/badge/Governed%20API-Redaction%20%2B%20Consistency-0969da)

**This folder is the source of truth for the “public shape” of the API** — the machine-validated contracts that define what clients can send and what they can expect back. ✅

> If it’s not in a contract, it’s not an API promise.  
> If it’s in a contract, implementations must honor it (or version it).

---

## 📌 Contents

- [What counts as a “contract” here?](#-what-counts-as-a-contract-here)
- [What lives here vs. what doesn’t](#-what-lives-here-vs-what-doesnt)
- [Suggested folder layout](#-suggested-folder-layout)
- [Compatibility & versioning rules](#-compatibility--versioning-rules)
- [How to add/change an endpoint](#-how-to-addchange-an-endpoint)
- [Validation & CI expectations](#-validation--ci-expectations)
- [Definition of Done](#-definition-of-done)
- [FAQ](#-faq)

---

## 🧾 What counts as a “contract” here?

A **contract artifact** is any *machine-validated* specification that defines an interface boundary, such as:

- **HTTP API contracts** (e.g., OpenAPI YAML/JSON)
- **GraphQL schema contracts** (SDL)
- **Reusable payload schemas** (e.g., JSON Schema for request/response bodies)
- **Async/event contracts** for queues/streams (message topics + payload shape)
- **Examples** that pair with the above contracts (golden payloads, fixtures)

This folder exists to keep the API boundary explicit, reviewable, and testable. 🔍

---

## ✅ What lives here vs. what doesn’t

| ✅ Put it here | 🚫 Don’t put it here |
|---|---|
| API specs (OpenAPI / GraphQL SDL) | Controller/service/business logic |
| Request/response schema definitions | Database schema / migrations |
| Event message schemas (queue/stream payloads) | ORM models / persistence code |
| Contract examples & fixtures | UI data-fetch logic / direct DB access |
| Contract-level “breaking change” notes | One-off scripts without validation |

> ⚠️ **Rule of thumb:**  
> If a *client* needs it to integrate safely, it belongs in **contracts**.  
> If only the *server implementation* needs it, it belongs elsewhere.

---

## 🗂️ Suggested folder layout

> Your exact structure may vary — this is the recommended “clean boundary” split.

```text
📦 api/
└─ 🧩 src/
   └─ 📜 contracts/                               # 🧱 contract-first boundary (source of truth)
      ├─ 📘 README.md                             # 👈 you are here
      ├─ 🌐 http/                                 # 🛰️ REST surface contracts
      │  ├─ 🧾 openapi.yaml                        # 🔎 canonical OpenAPI spec
      │  └─ 🧭 paths/                              # 🧩 optional split by domain/resource
      ├─ 🧬 graphql/                               # 🧠 GraphQL SDL (if used)
      │  └─ 🧬 schema.graphql                      # 🧷 schema + types + operations
      ├─ 🧱 schemas/                               # 📦 reusable payload schemas (http + events)
      │  ├─ 🧰 common/                             # ♻️ shared primitives (paging/errors/ids)
      │  └─ 🗺️ domain/                             # 🧬 domain shapes (feature/time-series/etc.)
      ├─ 📣 events/                                # 🛰️ async contracts (queues/streams)
      │  ├─ 🗞️ topics.md                           # 🧾 topic registry (optional)
      │  └─ 📮 payloads/                           # 🧬 message schemas (versioned)
      └─ 🧪 examples/                              # 🎯 canonical request/response payloads
         ├─ 🌐 http/                               # 🧾 request/response examples (golden)
         └─ 📣 events/                             # 🧾 event examples (golden)
```

---

## 🔒 Compatibility & versioning rules

### ✅ Default posture: backwards-compatible
Unless explicitly versioned, **assume clients already depend on the current contract**.

**Backwards-compatible changes (usually OK):**
- Adding new optional fields
- Adding new endpoints/resources
- Widening enums carefully (when clients tolerate unknown values)
- Marking fields as deprecated (with a runway)

**Breaking changes (require a version bump strategy):**
- Removing or renaming fields
- Changing field meaning, type, or required/optional status
- Changing error shapes clients depend on
- Changing pagination/sorting semantics
- Changing auth requirements or permission semantics

### 🧭 How we version
Use whichever versioning mechanism the API surface already follows (pick one and stay consistent):

- **Path versioning:** `/v1/...`, `/v2/...`
- **Header/content negotiation:** `Accept: application/vnd.kfm.v1+json`
- **Schema versioning:** explicit `contract_version` field in metadata (when needed)

> ⚠️ If you’re about to break a contract, treat it like a governance event:  
> document the change, version it, and protect it with contract tests.

---

## 🛠️ How to add/change an endpoint

### 1) Start with the contract (not the implementation) 🧱
- Add/update the relevant contract artifact (OpenAPI / SDL / JSON Schema).
- Add at least one **example payload** for request + response.

### 2) Write a contract change note 📝
Use the repo’s contract-change template when present:

- `../../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

> This forces us to record: *what changed*, *why*, *compat impact*, and *how to validate*.

### 3) Add/Update contract tests 🧪
Your goal: **prove the implementation matches the contract**.

Common patterns:
- Validate responses against schema in tests
- Snapshot examples as golden files
- Validate error envelopes and status codes
- Ensure pagination/meta fields match the spec

### 4) Implement behind the contract 🧩
Implementation should transform internal/domain data into the contract-defined shapes.
Keep “contract DTOs” at the edges — don’t leak DB/ORM objects across the boundary.

### 5) Validate locally (same checks CI runs) ✅
Run contract validators + tests before opening a PR.

---

## 🧪 Validation & CI expectations

Contracts should be **machine-validated** and **repeatable**.

Typical checks (adapt to whatever tooling exists in this repo):
- OpenAPI validation (schema correctness, refs resolve)
- Schema validation for examples (examples conform)
- Contract drift checks (implementation responses conform)
- Linting rules (naming, casing, required metadata)
- Governance flags (deprecations + version bumps documented)

> 💡 If a contract changes and CI doesn’t notice, CI is incomplete.

---

## ✅ Definition of Done

**When you touch anything in `api/src/contracts/`, you’re done when:**

- [ ] Contract artifact updated (OpenAPI/SDL/Schema)
- [ ] Compatibility impact declared (**compatible** / **breaking**)
- [ ] Breaking changes are versioned (or blocked)
- [ ] Examples added/updated and validated against schema
- [ ] Contract tests updated/added
- [ ] Implementation matches contract (no drift)
- [ ] Any redaction/classification needs are reflected at the API boundary
- [ ] Docs/template entry completed (if applicable)

---

## ❓ FAQ

### Why are contracts treated like “first-class code”?
Because they’re the safest integration boundary: clients, services, and UI can rely on them without peeking into implementation details.

### Can the UI query the graph/database directly?
No. All client-facing data access must go through the governed API layer so we can enforce consistency, access controls, and redaction.

### Do we store generated types here?
Only if the repo explicitly chooses to version generated artifacts. Otherwise, keep **contracts** here and generate types during build/dev workflows.

---

## 🔗 Related docs

- 📘 System pipeline & contract-first standards: `../../../docs/MASTER_GUIDE_v13.md`
- 🧭 Architecture & subsystem boundaries: `../../../docs/architecture/`
- 🧩 Contract change template: `../../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- ⚖️ Governance & review gates: `../../../docs/governance/`

---

