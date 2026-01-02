# 🧪 API Test Fixtures (`api/tests/fixtures/`)

![Path](https://img.shields.io/badge/path-api%2Ftests%2Ffixtures-blue)
![Contract-First](https://img.shields.io/badge/contract--first-required-success)
![Deterministic](https://img.shields.io/badge/deterministic-fixtures_only-brightgreen)
![Safety](https://img.shields.io/badge/security-no_secrets%20%7C%20no_PII-critical)
![Formats](https://img.shields.io/badge/formats-json%20%7C%20geojson%20%7C%20stac%20%7C%20dcat%20%7C%20prov-informational)

This folder contains **file-based fixtures** used by API tests (unit, integration, and contract tests). Fixtures are **deliberately small, deterministic, and sanitized** so tests stay stable and governance-safe.

---

## ✅ What belongs here

| ✅ Put in fixtures | ❌ Don’t put in fixtures |
|---|---|
| Canonical request bodies (JSON) | Real credentials, API keys, tokens, cookies |
| Canonical response bodies (JSON) / snapshots | Real user data / PII (names, emails, phone #s) |
| GeoJSON samples (Feature / FeatureCollection) | Exact sensitive coordinates (protected sites, private parcels) |
| STAC/DCAT/PROV sample records (minimal, valid) | Huge rasters, raw imagery, production exports |
| Error payload examples (400/401/403/404/422/500) | Anything that would fail secret/PII/sensitivity scans |
| “Redaction expected” examples (public vs authorized views) | Randomized outputs / non-deterministic timestamps |

> ⚠️ **Golden rule:** If it could change across machines, timezones, or runs — it doesn’t belong in a committed fixture.

---

## 🗂️ Suggested structure

Use (or evolve toward) a structure like this as fixtures grow:

```text
api/tests/fixtures/
├── 📁 http/
│   ├── 📁 requests/
│   └── 📁 responses/
├── 📁 geo/
│   ├── 📁 geojson/
│   └── 📁 tiles/               # (optional) tiny mock tilejson, not real tiles
├── 📁 catalogs/
│   ├── 📁 stac/
│   ├── 📁 dcat/
│   └── 📁 prov/
├── 📁 auth/
│   ├── 📁 tokens/              # mocked tokens only (never real)
│   └── 📁 policies/            # example policy inputs/outputs (if applicable)
├── 📁 errors/
└── 📄 README.md                # 👈 you are here
```

If the repo already uses a different layout, **follow the existing convention** and update this README to match.

---

## 🏷️ Naming conventions

Pick names that are searchable, stable, and readable in test output.

### Recommended filename pattern

```text
<METHOD>__<route_or_feature>__<status>__<scenario>__v<contractVersion>.<ext>
```

Examples:

- `GET__layers__200__happy_path__v1.json`
- `POST__search__422__invalid_bbox__v1.json`
- `GET__stac_items__200__filters_datetime__v1.json`
- `GET__storynode__403__sovereignty_redacted__v1.json`
- `FeatureCollection__counties__minimal__v1.geojson`

### Formatting rules (quick checklist)

- ✅ UTF-8, LF line endings, newline at EOF  
- ✅ Pretty-print JSON (stable indentation)  
- ✅ Stable key ordering **if your tooling supports it** (helps diff + reviews)  
- ✅ No “now()” timestamps — use fixed ISO strings  
- ✅ No random IDs — use stable IDs (`test_*`, `fixture_*`)  

---

## 🧷 Fixture “quality gates” (must pass)

Before committing a new fixture, ensure:

- [ ] **Contract-aligned:** matches the API schema/contract the test is validating  
- [ ] **Deterministic:** stable IDs, stable ordering, fixed timestamps  
- [ ] **Minimal:** includes only fields needed for the behavior under test  
- [ ] **Sanitized:** no secrets, no PII, no sensitive locations  
- [ ] **Purposeful:** filename + scenario clearly explain why it exists  
- [ ] **Reviewed:** changes are easy to diff; no giant blobs  

---

## 🛡️ Governance & safety rules (KFM-style)

Fixtures are treated like publishable artifacts:

- 🔒 **No secrets**: if a test needs auth, use **mock tokens** and/or stubs.
- 🧑‍⚖️ **No PII / sensitive content**: fixtures must not contain personal identifiers or protected site locations.
- 🗺️ **Sensitive coordinates**: when a test needs geospatial realism, use **generalized** or synthetic coordinates and keep precision low.
- 🧾 **Redaction tests are encouraged**: store “public view” fixtures alongside “authorized view” fixtures to prove access control.

> ✅ If you’re unsure whether something is sensitive, treat it as sensitive and either redact/generalize it or ask for a governance review.

---

## ➕ Adding a new fixture (workflow)

1. **Start from the contract**
   - Identify the endpoint + version you’re testing.
   - Confirm the schema fields you actually need.

2. **Capture or synthesize**
   - Prefer **synthetic minimal data**.
   - If capturing from a real response, **sanitize immediately** (before commit).

3. **Normalize for determinism**
   - Replace timestamps with fixed ISO strings.
   - Replace IDs with stable deterministic IDs.
   - Sort arrays when order is not meaningful (or assert order explicitly in tests).

4. **Place it & reference it**
   - Put the fixture in the best-matching subfolder.
   - Update/add tests to load it by relative path.

5. **Add an error fixture too (when relevant)**
   - If you add a “happy path,” consider adding the most likely validation failure fixture.

---

## 🧰 Loading fixtures in tests (patterns)

<details>
<summary><strong>🐍 Python (example pattern)</strong></summary>

```python
from pathlib import Path
import json

FIXTURES = Path(__file__).resolve().parent / "fixtures"

def load_json(*parts: str) -> dict:
    path = FIXTURES.joinpath(*parts)
    return json.loads(path.read_text(encoding="utf-8"))

# usage:
payload = load_json("http", "requests", "GET__layers__200__happy_path__v1.json")
```
</details>

<details>
<summary><strong>🟦 Node/TS (example pattern)</strong></summary>

```ts
import fs from "node:fs";
import path from "node:path";

const FIXTURES = path.resolve(__dirname, "fixtures");

export function loadJson(...parts: string[]) {
  const p = path.join(FIXTURES, ...parts);
  return JSON.parse(fs.readFileSync(p, "utf-8"));
}

// usage:
const payload = loadJson("http", "responses", "GET__layers__200__happy_path__v1.json");
```
</details>

---

## 🧭 Related docs & pointers

- 📄 `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` — use when adding/changing endpoints  
- 📄 `docs/standards/` — STAC / DCAT / PROV expectations  
- 📄 `docs/governance/` — FAIR+CARE, sovereignty rules, review gates  
- 📄 `CONTRIBUTING.md` — how to run tests and submit PRs

---

## 🧩 FAQ

### “Why not generate fixtures on the fly?”
Generated fixtures often introduce:
- time-based drift,
- random IDs,
- environment-specific ordering,
- accidental leakage of sensitive content.

Committed fixtures keep tests **repeatable**, **reviewable**, and **governable**.

### “Can I add large fixtures?”
If it’s larger than needed for the test, it’s too large. Prefer:
- minimal slices,
- reduced geometry,
- a few representative records,
- or a mocked/stubbed backend response.
