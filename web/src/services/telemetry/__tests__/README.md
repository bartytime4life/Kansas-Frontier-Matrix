# 🧪 Telemetry Service Tests (Web)

> **Path:** `web/src/services/telemetry/__tests__/`  
> **Goal:** Keep telemetry **contract-first**, **privacy-safe**, and **deterministic** ✅

---

## 📌 Why these tests exist

Telemetry in KFM isn’t just “analytics” — it’s part of **governance + traceability**:

- **Contract-first:** telemetry payloads must match the repo’s schemas (see `schemas/telemetry/`) 🧾
- **Safety-first:** telemetry must never become a side-channel for sensitive locations, personal data, or secrets 🔒
- **Evidence-first:** events should be precise, reproducible, and debuggable (no “mystery” side effects) 🧠

> [!IMPORTANT]
> If you change an event payload, you **must** update:
> 1) the schema in `schemas/telemetry/`  
> 2) the builder/type in `web/src/services/telemetry/`  
> 3) tests in this folder  
> Otherwise CI *should* fail (schema + governance gates).

---

## 🗺️ Quick links

- 🛰️ Telemetry service code: [`web/src/services/telemetry/`](../)
- 🧾 Telemetry schemas (source of truth): [`schemas/telemetry/`](../../../../../schemas/telemetry/)
- 📚 Repo master guide (contract-first + CI gates): [`docs/MASTER_GUIDE_v13.md`](../../../../../docs/MASTER_GUIDE_v13.md)

---

## 🧩 Test matrix

| Category | What we guarantee | Typical failures it catches |
|---|---|---|
| 🧾 **Schema / contract** | Every event payload conforms to the JSON Schema in `schemas/telemetry/` | Missing required fields, wrong types, version drift |
| 🔒 **Privacy / governance** | No PII, no secrets, no sensitive location leakage, no classification “downgrade” | Raw coordinates logged, user identifiers leaked, forbidden fields present |
| 📦 **Transport semantics** | Batching, retry, flush-on-exit, offline/queue behavior stays predictable | Silent drops, infinite retries, double-send |
| 🧭 **Context integrity** | Events include consistent context (route, map state, feature IDs, doc refs) *without* leaking restricted data | “Unknown” context, inconsistent IDs, unbounded payloads |
| 🧯 **Failure behavior** | Telemetry never breaks UX (fail-closed, doesn’t throw into UI) | Unhandled promise rejections, render crashes, hard dependency on network |

---

## ▶️ Running the tests

Because KFM can be run in different dev setups, use the command style your workspace uses. Here are common patterns:

```bash
# From repo root (common monorepo style)
pnpm -C web test

# Or:
npm --prefix web test

# Or:
yarn --cwd web test
```

### Run only telemetry-related tests (recommended)
```bash
# Examples (adjust to your runner's filtering rules)
pnpm -C web test telemetry
npm --prefix web test -- telemetry
yarn --cwd web test telemetry
```

> [!TIP]
> If you’re not sure which test runner is used (Jest vs Vitest), look for:
> - `web/package.json` scripts
> - `vitest.config.*` or `jest.config.*`
> - imports like `vitest` (`vi`) or `jest`

---

## 🧾 Contract-first testing pattern

The **schema is the source of truth**. A good telemetry test checks:

1) the builder returns a payload  
2) payload validates against the JSON Schema  
3) payload does **not** contain disallowed data (privacy guardrails)

### Example: schema validation (pattern)
```ts
// Pseudocode-ish example (works similarly in Jest or Vitest)
import Ajv from "ajv";
// import schema from "../../../../../schemas/telemetry/<your-event>.schema.json";
// import { buildYourEvent } from "../<event-builder>";

describe("telemetry/<your-event>", () => {
  it("matches JSON Schema", () => {
    const payload = buildYourEvent({ /* test inputs */ });

    const ajv = new Ajv({ allErrors: true, strict: true });
    const validate = ajv.compile(schema);

    const ok = validate(payload);
    expect(ok).toBe(true);

    if (!ok) {
      // Helpful failure output
      console.log(validate.errors);
    }
  });
});
```

> [!NOTE]
> If the codebase uses a different validator (e.g., Zod), keep the same idea:
> **validate the payload against a versioned contract** and fail loud on drift.

---

## 🔒 Privacy & governance guardrails

Telemetry must *never* contain:

- 🧍 **PII** (names, emails, phone numbers, addresses)
- 🔑 **secrets** (tokens, API keys, auth headers, cookies)
- 📍 **sensitive locations** at high precision (when sovereignty rules apply)
- 🧾 **restricted content** that is suppressed/redacted in the UI

### Suggested anti-leak tests
Add tests that assert the payload **does not** include:
- raw `Authorization` headers
- full request bodies
- exact lat/lng (unless explicitly allowed + classified)
- free-form text fields that could accidentally carry user input

Example pattern:
```ts
expect(JSON.stringify(payload)).not.toMatch(/authorization/i);
expect(JSON.stringify(payload)).not.toMatch(/api[_-]?key/i);
expect(JSON.stringify(payload)).not.toMatch(/bearer\s+/i);
```

> [!IMPORTANT]
> Privacy tests should be *cheap* and *paranoid*. It’s OK to have multiple redundant checks here.

---

## 🧰 Fixtures & helpers

Prefer small, explicit fixtures instead of huge snapshots:

- ✅ “Minimum valid event” fixture (only required fields)
- ✅ “Typical UI context” fixture (route, map mode, layer toggles)
- ✅ “Governance-sensitive” fixture (restricted dataset / redacted location)

Recommended helper ideas:
- `makeTestClock()` → deterministic timestamps
- `makeTelemetryContext()` → stable context IDs
- `makeTransportMock()` → intercept `fetch` / `sendBeacon`
- `assertNoPII(payload)` → centralized privacy assertions

---

## ➕ Adding a new telemetry event

Use this checklist to keep the repo consistent:

### ✅ Implementation checklist
- [ ] Define/update schema: `schemas/telemetry/<event>.schema.json`
- [ ] Implement builder/type: `web/src/services/telemetry/...`
- [ ] Add schema test in `__tests__/`
- [ ] Add privacy anti-leak test
- [ ] Add transport test **if** this event changes delivery behavior (batching/retry)
- [ ] Keep payload small + bounded (no unbounded arrays or raw text dumps)

### ✅ Naming + versioning tips
- Use stable, descriptive names (e.g., `focus_mode.enter`, `map.layer.toggle`)
- Version event payloads deliberately (schema versioning > guessing)
- Never silently repurpose old fields — add new fields + keep backwards compatibility when possible

---

## 🧯 Debugging tips

If tests fail unexpectedly:

- 🕒 **Time-dependent failures:** ensure timers are mocked/frozen (no real `Date.now()`)
- 🌐 **Network calls:** ensure transport is mocked (no real `fetch`/`beacon`)
- 🧾 **Schema failures:** print schema errors (AJV can show the exact path)
- 📦 **Flaky batching:** run in serial for transport tests (avoid parallel flush races)

---

## ✅ Definition of Done (Telemetry PRs)

- [ ] Event schema added/updated in `schemas/telemetry/`
- [ ] Tests cover: schema validation + privacy guardrails
- [ ] No real network calls in unit tests
- [ ] Deterministic output (time/randomness controlled)
- [ ] Payload size is bounded + reviewed for sensitive fields
- [ ] CI passes (schema + governance gates)

---

### 🧭 Maintainers’ note

This folder is intentionally strict. Telemetry is a **governance surface** — treat changes like an API change. 🚦