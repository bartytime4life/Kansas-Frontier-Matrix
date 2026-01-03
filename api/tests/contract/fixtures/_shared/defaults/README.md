# 🧱 Shared Default Fixtures (API Contract Tests)

![tests](https://img.shields.io/badge/tests-contract-blue)
![contracts](https://img.shields.io/badge/contracts-contract--first-6f42c1)
![fixtures](https://img.shields.io/badge/fixtures-deterministic-brightgreen)

This folder contains **shared, baseline fixture fragments** used by **API contract tests** to compose request/response fixtures quickly and consistently.

> [!IMPORTANT]
> **Defaults are “boring on purpose.”** They must be stable, deterministic, and safe to reuse across many tests.

---

## 📍 Where this fits

```text
🧪 api/tests/contract/fixtures/
└── 🧩 _shared/
    ├── 🧱 defaults/          👈 you are here (baseline fragments)
    ├── 🧾 headers/           (shared header fixtures)
    ├── 📦 envelopes/         (shared response envelope shapes)
    ├── 🧭 ids/               (stable synthetic IDs)
    ├── ⏱️ time/              (stable timestamps + time windows)
    ├── 🌍 geo/               (shared geo primitives)
    └── ❗ errors/            (shared error shapes)
```

Contract tests validate the API’s behavior against **known inputs/outputs**, and these defaults are the **lowest common denominator** used to build those fixtures.

---

## ✅ What belongs in `defaults/`

Use this directory for **reusable baseline pieces** that appear everywhere, such as:

- 🧾 **Common headers** (e.g., Accept / Content-Type)
- 📦 **Standard response envelope shape** (e.g., `{ data, meta, errors }` conventions)
- 📄 **Pagination defaults** (limit/offset, cursors, meta counts)
- 🧭 **Deterministic IDs / timestamps** used across fixtures (only if truly global)
- 🧱 **Baseline “safe/public” representations** (where redaction/classification applies)

> [!TIP]
> If multiple endpoint fixtures copy/paste the same shape **3+ times**, it’s a candidate for a shared default.

---

## 🚫 What does **NOT** belong in `defaults/`

Keep this folder free of anything that is **scenario-specific** or **risky**:

- ❌ Endpoint-specific payloads (those belong with the endpoint fixtures)
- ❌ Real user data, real names, real emails, real addresses
- ❌ API keys, tokens, secrets, cookies, credentials (even fake-looking ones that resemble real patterns)
- ❌ Precise or sensitive coordinates / protected locations
- ❌ “Now” timestamps, random UUIDs, nondeterministic values

Defaults should be safe to reuse *everywhere* without surprise side effects.

---

## 🧩 How defaults are meant to be used

### The composition pattern

1. Start with a default fragment (baseline)
2. Layer in endpoint fixture specifics
3. Apply per-test overrides (the “delta”)

You should be able to read any test and quickly see **what changed** from the baseline.

#### Example (language-agnostic pseudo)

```txt
fixture = deepMerge(
  defaults.responseEnvelope,
  endpointFixtures.getThing.success,
  { data: { id: "thing_123" } }   // test-specific override
)
```

<details>
<summary><strong>✨ Suggested default fragment names (optional convention)</strong></summary>

If you’re adding new files here, consider a predictable set of names:

- `headers.json` → common request headers
- `query.json` → common query params (pagination, sorting)
- `response_envelope.json` → `{ data, meta, errors }` baseline
- `pagination_meta.json` → standard pagination metadata
- `errors.json` → common error shapes (auth, validation, not-found)

⚠️ Only add a default file if it’s genuinely reused across multiple endpoints.
</details>

---

## 🧱 “Contract-first” rules for defaults

Defaults are part of how we enforce a **contract-first** API lifecycle:

- 📜 Treat fixture shapes as *contract-aware*: they should match the OpenAPI/GraphQL contract.
- 🔁 If a contract changes, **either** it must remain backwards-compatible **or** the contract tests + fixtures must be updated alongside it.
- 🧨 If you introduce a breaking change, keep old-version fixtures intact (or version them) so clients don’t silently break.

> [!NOTE]
> Think of these defaults as the “public handshake” of the system. Small changes can ripple across many tests.

---

## 🔒 Safety, governance, and “don’t leak” rules

KFM’s CI expectations include automated checks that look for secrets, PII, and sensitive location leakage. Defaults are the easiest place to accidentally introduce something that appears *everywhere*.

**When in doubt:**
- Use synthetic values that cannot be confused with real records.
- Prefer coarse/generalized locations for any spatial examples.
- Avoid embedding sensitive classifications unless you are explicitly testing redaction/classification behavior.

✅ A good default is something we’d be comfortable shipping in a public repo.

---

## 🛠️ Adding or changing a default (checklist)

1. 🧠 **Confirm reuse**: will at least 2–3 fixtures benefit?
2. 🧱 **Keep it minimal**: only the invariant baseline.
3. 🧪 **Update tests**: make sure all contract tests still read cleanly (small deltas).
4. 🔁 **Run the contract suite** locally (and ensure CI will pass).
5. 📝 **Document intent**:
   - What problem does this default solve?
   - What should override it?
   - What should never override it?

---

## 🧭 Related references (repo-local)

- 📘 `docs/MASTER_GUIDE_v13.md` (contract-first + CI gates)
- 🧩 `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` (how to add/change endpoints)
- 🧷 `docs/governance/*` (classification / sovereignty rules, review gates)

---

## 🧹 Maintenance tips

- ✅ Prefer **small, composable fragments** over giant “one default to rule them all”.
- ✅ Keep defaults **stable**: changes here can cause widespread fixture churn.
- ✅ If you must change defaults, do it with a **clear migration path** (and update fixtures intentionally).
- ✅ Consider versioned defaults (e.g., `v1/`, `v2/`) if the API supports parallel versions.

---

### 📌 Ownership

If you’re unsure whether something belongs in `defaults/`, default to placing it in the nearest endpoint fixture and only promote it here after reuse is proven.

