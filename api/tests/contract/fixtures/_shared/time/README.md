<!-- 📍 Path: api/tests/contract/fixtures/_shared/time/README.md -->

# ⏱️ Shared Time Fixtures

![contract-tests](https://img.shields.io/badge/tests-contract-blue)
![utc](https://img.shields.io/badge/time-UTC-success)
![iso8601](https://img.shields.io/badge/format-ISO%208601-informational)
![deterministic](https://img.shields.io/badge/goal-deterministic%20fixtures-brightgreen)

Shared, canonical **time fixtures** (timestamps, date ranges, and tricky edge-cases) used across **API contract tests**.

> [!NOTE]
> Contract tests are part of our CI gates and validate that endpoints respond correctly for known inputs, while schemas (OpenAPI/GraphQL) are linted as part of the workflow.:contentReference[oaicite:0]{index=0}  
> This repo is **contract-first**: contracts/schemas are treated as first-class artifacts, with strict compatibility expectations when they change.:contentReference[oaicite:1]{index=1}

---

## 🧭 Table of Contents

- [Why this exists](#-why-this-exists)
- [Where this fits](#-where-this-fits)
- [Time standards we use](#-time-standards-we-use)
- [Recommended fixture shape](#-recommended-fixture-shape)
- [Suggested fixture catalog](#-suggested-fixture-catalog)
- [Usage patterns](#-usage-patterns)
- [Range semantics](#-range-semantics)
- [Gotchas](#-gotchas)
- [Add / change checklist](#-add--change-checklist)
- [Sources](#-sources)

---

## 🎯 Why this exists

Time is deceptively hard:
- **DST changes**, **time zones**, **leap years**, and even “months” being different lengths can break assumptions fast.:contentReference[oaicite:2]{index=2}
- If contract tests pull “now” from the wall clock, they become flaky and non-reproducible (especially in CI).

This folder keeps contract tests:
- ✅ **Deterministic** (same inputs ⇒ same outputs), aligned with the project’s “deterministic pipeline” principle:contentReference[oaicite:3]{index=3} and reproducible practices (avoid nondeterminism).:contentReference[oaicite:4]{index=4}
- ✅ **Timezone-safe** (UTC-first; no implicit locale parsing)
- ✅ **Schema-stable** (timestamps are part of the contract; format drift is a breaking change)

Also: the KFM system has explicit temporal UX (timeline controls / time sliders), which makes timestamp correctness extra important across layers and interactions.:contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}

---

## 🧩 Where this fits

```text
📁 api/                                 🧠 API workspace root
└── 📁 tests/                           🧪 Automated test suites
    └── 📁 contract/                    📜 Contract / schema-driven tests
        └── 📁 fixtures/                📦 File-based request/response fixtures
            └── 📁 _shared/             🧩 Reusable fixture building blocks
                └── 📁 time/            ⏱️ Canonical time fixtures (UTC/DST/ranges)
                    └── 📄 README.md    🗺️ Conventions + examples for time fixtures (you are here)
```

> [!TIP]
> In the v13 repo organization, server-side API code is expected under `src/server/` and contracts under `src/server/contracts/` (where applicable).:contentReference[oaicite:7]{index=7}  
> This folder is still useful even when contracts live elsewhere—because contract tests still need **stable fixture time values**.

---

## 🕰️ Time standards we use

### ✅ Canonical representations

1) **ISO 8601 datetime strings**  
   - Use explicit timezone (prefer `Z` / UTC).
   - ISO strings are a standard way to represent datetimes in systems and tooling; keep them consistent and parseable.:contentReference[oaicite:8]{index=8}

2) **Epoch milliseconds (Unix ms)**  
   - Milliseconds since **00:00:00 UTC on 1 January 1970**.:contentReference[oaicite:9]{index=9}
   - This aligns cleanly with typical JS timestamp handling (ms since epoch).:contentReference[oaicite:10]{index=10}

> [!NOTE]
> A practical pattern (used widely in time-series tooling) is to store both a human-readable datetime string **and** its epoch-ms equivalent.:contentReference[oaicite:11]{index=11}

---

## 🧱 Recommended fixture shape

Keep fixtures **boring and explicit**. When possible, store UTC ISO + epoch-ms together:

```json
{
  "id": "millennium_utc",
  "iso": "2000-01-01T00:00:00.000Z",
  "epoch_ms": 946684800000,
  "notes": "Stable baseline instant in UTC"
}
```

### Optional fields (only when needed)
- `local`: an ISO string with an explicit offset (e.g., `-05:00`)
- `tz`: an IANA timezone (only if a test truly needs it; offsets are usually enough)
- `tags`: list of strings (e.g., `["dst", "boundary"]`)

---

## 🗂️ Suggested fixture catalog

> [!IMPORTANT]
> The files below are **recommended** structure. Add only what the contract tests actually need.

```text
📁 time/
  📄 README.md
  📄 instants.json        ⭐ canonical instants
  📄 ranges.json          ⭐ canonical [start,end) ranges
  📄 tz_edges.json        ⭐ DST / offset edge cases
  📄 index.(ts|py)         (optional) convenience re-exports
```

### ⭐ `instants.json` (example)

```json
[
  {
    "id": "epoch_start",
    "iso": "1970-01-01T00:00:00.000Z",
    "epoch_ms": 0,
    "notes": "Unix epoch start"
  },
  {
    "id": "millennium_utc",
    "iso": "2000-01-01T00:00:00.000Z",
    "epoch_ms": 946684800000,
    "notes": "Stable baseline instant"
  },
  {
    "id": "leap_day_midday",
    "iso": "2016-02-29T12:34:56.789Z",
    "epoch_ms": 1456749296789,
    "notes": "Leap-day coverage"
  },
  {
    "id": "end_of_year_utc",
    "iso": "2023-12-31T23:59:59.999Z",
    "epoch_ms": 1704067199999,
    "notes": "Boundary instant (just before 2024-01-01)"
  }
]
```

### ⭐ `tz_edges.json` (example)

DST tests should never rely on implicit locale parsing. Store the **local offset form** and the **normalized UTC form**:

```json
[
  {
    "id": "dst_spring_forward_pre_gap",
    "local": "2024-03-10T01:59:59-06:00",
    "iso": "2024-03-10T07:59:59.000Z",
    "epoch_ms": 1710057599000,
    "tags": ["dst", "spring-forward"],
    "notes": "Just before the spring-forward gap (offset explicit)"
  },
  {
    "id": "dst_spring_forward_post_gap",
    "local": "2024-03-10T03:00:00-05:00",
    "iso": "2024-03-10T08:00:00.000Z",
    "epoch_ms": 1710057600000,
    "tags": ["dst", "spring-forward"],
    "notes": "First representable local time after the gap"
  },
  {
    "id": "dst_fall_back_pre_repeat",
    "local": "2024-11-03T01:59:59-05:00",
    "iso": "2024-11-03T06:59:59.000Z",
    "epoch_ms": 1730617199000,
    "tags": ["dst", "fall-back"],
    "notes": "Just before fall-back repeat hour"
  },
  {
    "id": "dst_fall_back_post_repeat",
    "local": "2024-11-03T01:00:00-06:00",
    "iso": "2024-11-03T07:00:00.000Z",
    "epoch_ms": 1730617200000,
    "tags": ["dst", "fall-back"],
    "notes": "Same wall-clock hour occurs again, but with different offset"
  }
]
```

### ⭐ `ranges.json` (example)

```json
[
  {
    "id": "one_day_2024_01_01_utc",
    "start": { "iso": "2024-01-01T00:00:00.000Z", "epoch_ms": 1704067200000 },
    "end": { "iso": "2024-01-02T00:00:00.000Z", "epoch_ms": 1704153600000 },
    "semantics": "[start,end) inclusive start, exclusive end",
    "notes": "A clean full-day UTC range"
  }
]
```

---

## 🧰 Usage patterns

### 🟦 JavaScript / TypeScript

```ts
// Example (ESM): load shared time instants
import instants from "./instants.json" assert { type: "json" };

const t0 = instants.find(x => x.id === "millennium_utc");
if (!t0) throw new Error("Missing fixture: millennium_utc");

// Use in request params / expected response fields
expect(response.body.created_at).toBe(t0.iso);
expect(response.body.created_at_ms).toBe(t0.epoch_ms);
```

### 🐍 Python

```py
import json
from pathlib import Path

TIME_DIR = Path(__file__).resolve().parent
INSTANTS = json.loads((TIME_DIR / "instants.json").read_text(encoding="utf-8"))

def instant(id_: str) -> dict:
    return next(x for x in INSTANTS if x["id"] == id_)
```

### 🧪 If you freeze time (any framework)

If a test framework uses a **time-freeze** helper (mock clock / monkeypatch / dependency injection), ensure:
- it is **function-scoped** (reset per test)
- it **cleans up** after itself

This mirrors best practice in fixture design: run per test and revert state after yielding control, leaving the system as it was before the test.:contentReference[oaicite:12]{index=12}

---

## 📏 Range semantics

### Prefer half-open intervals: `[start, end)`

Half-open ranges avoid “inclusive end” foot-guns (especially with sub-second precision). A classic example in time filtering is:

- ✅ `x >= start AND x < start + interval`  
- 🚫 Avoid “inclusive end” patterns that accidentally include the next boundary instant:contentReference[oaicite:13]{index=13}:contentReference[oaicite:14]{index=14}

If the API contract uses a different convention, **document it explicitly** in the fixture (`semantics` field).

---

## ⚠️ Gotchas

- 🕳️ **DST gaps**: some local times do not exist (spring-forward).  
- 🔁 **DST repeats**: some local times happen twice (fall-back).  
- 🗓️ **Calendar quirks**: leap years, month lengths, etc.  
- 🌍 **Time zones**: never parse timestamps without offsets/timezone—make it explicit.

Time/date values require special handling across these concerns; don’t “wing it” with implicit defaults.:contentReference[oaicite:15]{index=15}

---

## ✅ Add / change checklist

When adding or editing time fixtures:

- [ ] 🔒 Use **synthetic** values (no secrets, no PII; fixtures must be safe to publish)
- [ ] 🧾 Provide both `iso` (UTC `Z`) and `epoch_ms` when possible
- [ ] 🧠 If you include a local time, include an **explicit offset** (e.g., `-06:00`)
- [ ] 🧪 Add/adjust contract tests that use the new fixture
- [ ] 🧷 If the timestamp format changes, treat it as a **contract change** and update schema + tests accordingly (contract-first discipline).:contentReference[oaicite:16]{index=16}

---

## 📚 Sources

- KFM repo governance (contract-first, deterministic pipeline, contract tests in CI):​:contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18}
- Canonical subsystem homes (`src/server/`, `src/server/contracts/`):​:contentReference[oaicite:19]{index=19}
- Epoch-ms definition and pairing datetime strings with time_start:​:contentReference[oaicite:20]{index=20}:contentReference[oaicite:21]{index=21}
- ISO 8601 datetime guidance:​:contentReference[oaicite:22]{index=22}
- Time-series/time-date pitfalls (DST, leap years, time zones):​:contentReference[oaicite:23]{index=23}
- Half-open range rationale for date/time precision:​:contentReference[oaicite:24]{index=24}:contentReference[oaicite:25]{index=25}
- Fixture design pattern (scope + cleanup after yield):​:contentReference[oaicite:26]{index=26}

