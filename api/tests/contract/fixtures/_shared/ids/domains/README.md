# 🧩 Domain IDs — Shared Contract Fixtures

![tests](https://img.shields.io/badge/tests-contract-blue)
![fixtures](https://img.shields.io/badge/fixtures-_shared-success)
![stability](https://img.shields.io/badge/ids-stable%20%26%20deterministic-purple)

> [!IMPORTANT]
> These IDs are **part of the contract-test “known inputs” surface**.  
> Treat them like you’d treat an API schema: **stable, deliberate, and version-aware** ✅

---

## 📘 Overview

### 🎯 Purpose
This folder is the **single source of truth** for **Domain IDs** used by **API contract tests**.

Contract tests are designed to validate that API endpoints respond correctly given **known inputs**. Domain IDs are one of those inputs. If domain identifiers change randomly (or differ across fixtures), contract tests become flaky and stop measuring what they’re meant to measure.

### ✅ Scope
| In Scope ✅ | Out of Scope ❌ |
|---|---|
| Canonical **test-only** Domain IDs | Full domain payload fixtures (those live elsewhere) |
| Deterministic IDs referenced across many tests | Runtime ID generation (never do this in contract fixtures) |
| Naming + governance rules for IDs | Production/staging IDs and environment-specific IDs |

### 👥 Audience
- API engineers writing/maintaining **contract tests**
- Contributors adding new **domains** that must be reachable via contract fixtures
- CI maintainers who care about determinism & reproducibility

### 📚 Definitions
- **Domain**: A top-level KFM functional/data module (e.g., “air-quality”, “land-treaties”, “soils”).  
- **Domain ID**: The canonical identifier used by the API to reference a domain (often appears in URLs, query params, or relationship fields).
- **Contract fixtures**: Test artifacts that represent **known inputs/outputs** to validate the API contract.

---

## 🗂️ Directory Layout


```text
🧪 api/                                      🧱 API service root
└── 🧫 tests/                                 🔬 Automated test suites
    └── 📜 contract/                          🤝 Schema/contract-driven tests
        └── 📦 fixtures/                      🧷 Golden inputs/outputs for contract tests
            └── ♻️ _shared/                   🧰 Reusable fixture fragments (global)
                └── 🪪 ids/                   🏷️ Canonical identifiers used across tests
                    └── 🌐 domains/           🗺️ Domain identifiers (this folder)
                        ├── 📘 README.md      👈 Rules + usage (you are here)
                        ├── 🧾 <domain-slug>.<ext>  🔒 One domain’s frozen ID fixture
                        └── ✨ ...            ➕ Additional domain ID fixtures
```

> [!NOTE]
> The exact file extension(s) in this folder may vary by implementation (JSON/TS/YAML/etc).  
> The **invariants below** must hold regardless of format.

---

## 🔒 Invariants (Non‑Negotiables)

✅ **Stable**  
- IDs in this folder **must not change** casually (or “because a refactor happened”).

✅ **Deterministic**  
- IDs must be the same across:
  - machines
  - CI runs
  - branches
  - replays of fixtures

✅ **Contract-aligned**  
- IDs must match the **API contract’s expected format** (e.g., UUID, ULID, slug-id).  
- If the contract says `uuid`, use a UUID here — don’t improvise.

✅ **Test-only / non-production**  
- Never copy real production IDs into fixtures.
- Never use secrets, private identifiers, or “live” environment references.

✅ **No runtime generation**  
- Don’t call `randomUUID()`, `uuidv4()`, etc. during test execution for contract fixtures.
- Generate once, then **freeze** the value in this folder.

✅ **No duplication**  
- If tests need a domain ID, they should reference it from here rather than hardcoding the string in multiple places.

---

## 🧪 Typical Usage Patterns

### Pattern A — Import/Require the ID (preferred)
Use the shared registry so tests don’t scatter magic strings.

```ts
// pseudo-code (adapt to your test runner / language)
// import { DOMAIN_IDS } from "api/tests/contract/fixtures/_shared/ids/domains";

const domainId = DOMAIN_IDS["air-quality"]; // example slug key
const res = await api.get(`/v1/domains/${domainId}`);
expect(res.status).toBe(200);
```

### Pattern B — Reference from other fixtures
When authoring request/response fixtures, prefer referencing the canonical domain ID from this folder (mechanism depends on your fixture loader).

```json
{
  "domainId": "<use shared domain id here>",
  "note": "Do not inline raw IDs unless there is no shared mechanism available."
}
```

<details>
  <summary>💡 Why the “shared registry” pattern matters</summary>

- Prevents subtle mismatches (two fixtures “mean the same domain” but use different IDs).
- Makes refactors safer (you update one canonical spot, not 30 files).
- Keeps contract tests focused on API behavior, not fixture drift.

</details>

---

## ➕ Adding a New Domain ID

1) **Pick a domain slug** 🏷️  
   - Use a stable, human-readable key (typically `kebab-case`), e.g.:
     - `air-quality`
     - `land-treaties`
     - `soils-sda`

2) **Generate a stable ID** 🧬  
   - Must comply with the API contract (UUID/ULID/etc).
   - Generate once, then commit.

3) **Create the new fixture file** 📄  
   - Recommended naming: `<domain-slug>.<ext>`
   - Keep the content minimal: ID + optional small metadata *only if it helps tests*.

4) **Wire it into your “shared map” (if applicable)** 🧷  
   - If this folder has an index/registry file, update it.
   - If tests auto-discover fixtures, follow that convention.

5) **Update/extend contract tests** 🧪  
   - Add tests that reference the new ID.
   - Ensure the API can resolve the domain in the contract test environment (seed/mocks).

6) **Run the contract suite locally** ✅  
   - Fix determinism issues immediately (no “works on my machine”).

---

## 🧨 Changing or Removing an Existing Domain ID

> [!WARNING]
> Changing an existing Domain ID is usually a **breaking change** for contract fixtures.  
> Do it only if you **intend** to break compatibility and have coordinated the change.

If you must change/remove an ID:
- Update **every dependent fixture** and **every contract test** that references it.
- Ensure API contract expectations still hold (or version accordingly).
- Prefer migrations/aliases at the API layer if backward compatibility is required.

---

## ✅ Definition of Done (Checklist)

- [ ] New domain slug is clear and consistently named (kebab-case recommended)
- [ ] Domain ID matches the API contract’s ID format
- [ ] ID is committed as a **stable literal** (no runtime generation)
- [ ] Tests reference the shared ID (no duplicated magic strings)
- [ ] Contract test environment can resolve the domain (seed/mocks updated)
- [ ] Contract suite passes locally + in CI

---

## 🔗 Related Artifacts (Repo Paths)

- 📘 Master contract/governance: `docs/MASTER_GUIDE_v13.md`
- 🧾 API contract change workflow: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- 📚 Domain module documentation (examples):
  - `docs/data/air-quality/README.md`
  - `docs/data/historical/land-treaties/README.md`
  - `docs/data/soils/sda/README.md`

---

## 🆘 Troubleshooting

**❓ Contract test fails with 404 / “domain not found”**
- The ID exists in fixtures but the API test environment doesn’t have matching seed/mocks.
- Ensure the contract test harness loads domain seed data aligned with these IDs.

**❓ Snapshot mismatch**
- Confirm whether the API contract changed (expected) or fixtures drifted (unintended).
- If it’s an intentional contract change, update tests + fixtures together.

**❓ Someone hardcoded a domainId in a test**
- Replace the literal string with a reference to this folder.
- Add a quick lint/check (optional) to discourage future duplication.

---

