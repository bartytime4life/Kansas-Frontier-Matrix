<!--
Path: tests/fixtures/README.md
Purpose: Governed, deterministic test fixtures for Kansas Frontier Matrix (KFM)
-->

![governed](https://img.shields.io/badge/governed-evidence--first-brightgreen)
![tests](https://img.shields.io/badge/tests-fixtures-informational)

# Test Fixtures

This directory contains **deterministic, minimal, reviewable** fixture data used by automated tests across KFM.

Fixtures are treated as **governed artifacts** because they shape system behavior (especially around policy enforcement, provenance, and redaction). Keep them small, explicit, and safe.

---

## Contents

- [What belongs here](#what-belongs-here)
- [What must not be here](#what-must-not-be-here)
- [Fixture taxonomy](#fixture-taxonomy)
- [Directory layout](#directory-layout)
- [Fixture metadata](#fixture-metadata)
- [Rules](#rules)
  - [Determinism rules](#determinism-rules)
  - [Geospatial rules](#geospatial-rules)
  - [Governance & sensitivity rules](#governance--sensitivity-rules)
- [How to add a fixture](#how-to-add-a-fixture)
- [How to use fixtures in tests](#how-to-use-fixtures-in-tests)
- [Fixture change policy](#fixture-change-policy)
- [FAQ](#faq)

---

## What belongs here

✅ Put fixture files here when they are:

- **Synthetic or safely derived** (licensed/redistributable; no restricted content).
- **Small** (fast test runs; small diffs; easy review).
- **Deterministic** (stable ordering, stable IDs, stable timestamps, stable randomness).
- **Purpose-built** (each fixture exists to validate a specific behavior).
- **Auditable** (metadata describes why it exists and how it was produced).

---

## What must not be here

> [!IMPORTANT]
> Never commit real secrets, personal data, or restricted site coordinates into fixtures—tests run everywhere, and fixtures get copied everywhere.

🚫 Do **not** include:

- **Credentials** (API keys, tokens, passwords, private keys).
- **Real PII** (names/emails/phone numbers of private individuals).
- **Restricted location data** (precise coordinates for sensitive cultural/archaeological sites).
- **Non-redistributable source content** (unclear license, “for internal use only”, etc.).
- **Giant datasets** (use generators or subset scripts instead).

---

## Fixture taxonomy

| Fixture type | Purpose | Typical formats | Example contents |
|---|---|---|---|
| **Unit fixtures** | Validate pure domain logic (no I/O) | JSON, YAML | Entities, timelines, small tables |
| **Integration fixtures** | Validate adapters (DB, graph, object store, filesystem) | SQL, Cypher, JSONL | PostGIS seed data, Neo4j seed data |
| **Contract fixtures** | Validate API contracts and policy boundaries | JSON, GraphQL, HAR | Request/response snapshots, schema examples |
| **Pipeline fixtures** | Validate transforms and validators | JSON/GeoJSON, CSV, Parquet (small), YAML | raw→processed expected outputs |
| **Policy fixtures** | Validate “deny-by-default”, redaction, and leak prevention | GeoJSON, JSON | “known leak” negative cases; access denied cases |

---

## Directory layout

This is the **recommended** structure. If the repo uses a different layout, update this README so it stays true.

```text
tests/
  fixtures/
    README.md

    manifest/
      fixtures.manifest.yaml          # optional registry of fixture sets

    geo/
      geojson/
      bbox/
      invalid/                        # intentionally invalid geometries for negative tests

    catalogs/
      stac/
      dcat/
      prov/

    policy/
      allow/
      deny/
      known-leaks/                    # negative fixtures: prove we *do not* leak

    db/
      postgis/
      neo4j/

    api/
      rest/
      graphql/

    ui/
      playwright/                     # storage state, minimal snapshots (if used)

    _generated/                       # gitignored; build-time outputs only
```

> [!TIP]
> If you’re unsure where a fixture belongs, choose the folder matching the **behavior under test** (policy vs. catalog vs. db), not the file format.

---

## Fixture metadata

Every fixture set should have a small sidecar metadata file so reviewers can quickly assess safety and intent.

### Minimal metadata (recommended)

Create a `*.fixture.yaml` (or `*.fixture.json`) next to the fixture file(s):

```yaml
# Example: tests/fixtures/policy/known-leaks/restricted_points.fixture.yaml
fixture_id: policy.known-leaks.restricted_points.v1
title: "Policy negative: restricted points must be redacted/denied"
purpose: "Ensure policy denies asset access and prevents coordinate leakage."
origin:
  kind: synthetic
  notes: "Coordinates are fabricated; NOT real sites."
license: "CC0-1.0"
sensitivity:
  classification: test-only
  contains_restricted_patterns: true
  mitigation: "Use fabricated coords; verify API returns generalized/withheld outputs."
formats:
  - file: restricted_points.geojson
    media_type: application/geo+json
    sha256: "<fill on commit>"
assumptions:
  - "Policy evaluation is default-deny on ambiguity."
  - "Redaction/generalization is enforced before responses leave the API boundary."
```

> [!NOTE]
> If you don’t have a hashing helper yet, you can temporarily set `sha256: "TBD"` **only for local WIP branches**. Do not merge with missing digests unless your repo rules explicitly allow it.

---

## Rules

### Determinism rules

- Prefer **static files** over generators *unless* the fixture would be large.
- If generating, require a **fixed seed** and commit the generator script + expected outputs.
- Avoid embedding current time; use fixed timestamps (e.g., `1970-01-01T00:00:00Z`).
- Ensure stable ordering for:
  - JSON object keys (canonicalize if your tests compare raw text)
  - arrays of features/records (sort by stable IDs)
- Keep fixtures small enough to diff in PR review.

### Geospatial rules

- Default CRS for GeoJSON fixtures: **WGS84 (EPSG:4326)**.
- Validate fixture geometry where appropriate (and include invalid cases under `geo/invalid/`).
- Keep extents small and explicit (include bbox files when helpful).
- For “redaction” tests, use **fabricated** points, and test:
  - denial modes (no access)
  - generalization modes (coarsened coordinates)
  - metadata-only stubs (allowed to discover, not allowed to fetch)

### Governance & sensitivity rules

> [!WARNING]
> If a fixture could be sensitive in the real world, treat it as sensitive in tests too.

- Fixtures that simulate restricted material must be **synthetic**.
- Model policy behavior explicitly:
  - allow cases → return full assets
  - deny cases → return metadata stub only
  - “known leaks” → ensure outputs do *not* contain sensitive details
- Never include “real-but-small” restricted coordinates. Small is still a leak.

---

## How to add a fixture

1) Pick a **fixture_id**  
Use a stable naming pattern:
- `domain.subdomain.name.vN`  
Examples:
- `catalogs.stac.minimal_collection.v1`
- `db.postgis.rooms_seed.v1`
- `policy.known-leaks.restricted_points.v1`

2) Create the fixture file(s)  
Keep them minimal. Prefer:
- `*.json`, `*.geojson`, `*.yaml`, `*.jsonl`
- `*.sql` / `*.cypher` only when you need to exercise the DB adapter

3) Add the metadata sidecar  
Add `*.fixture.yaml` (recommended) describing intent, origin, license, and sensitivity.

4) Add/extend tests that consume it  
Fixture files without tests quickly become dead weight.

5) Add a negative test when relevant  
Especially for policy and redaction. (“Known leak” fixtures exist to prove we don’t regress.)

### Definition of Done

- [ ] Fixture is **minimal** and **deterministic**
- [ ] Fixture has a **metadata sidecar**
- [ ] Fixture is **synthetic or redistributable**
- [ ] A test exercises it and asserts the intended behavior
- [ ] If sensitive-pattern simulation: tests verify **deny/redact** behavior

---

## How to use fixtures in tests

### Python example (pytest-style)

```python
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"

def load_fixture_json(rel_path: str) -> Any:
    p = FIXTURES_DIR / rel_path
    return json.loads(p.read_text(encoding="utf-8"))
```

Usage:

```python
def test_policy_denies_known_leak_points(client):
    payload = load_fixture_json("policy/known-leaks/restricted_points.request.json")
    resp = client.post("/api/whatever", json=payload)
    assert resp.status_code in (403, 404)
```

### Node/TypeScript example (Jest-style)

```ts
import fs from "node:fs";
import path from "node:path";

export const FIXTURES_DIR = path.join(__dirname, "..", "fixtures");

export function loadFixtureJson(relPath: string): unknown {
  const p = path.join(FIXTURES_DIR, relPath);
  return JSON.parse(fs.readFileSync(p, "utf8"));
}
```

Usage:

```ts
test("policy denies known leak fixture", async () => {
  const req = loadFixtureJson("policy/known-leaks/restricted_points.request.json");
  // call API client with req...
});
```

---

## Fixture change policy

- **Breaking changes** to fixture meaning require a **new version** (`v2`, `v3`, …).
- If you change formatting only (whitespace/key ordering), prefer keeping semantic equivalence.
- If you update expected outputs:
  - confirm the change is intended
  - note the reason in the PR description
  - ensure you didn’t mask a regression

> [!TIP]
> If a test failure is caused by fixture drift (not behavior drift), consider whether the fixture is too coupled to implementation details. Prefer behavior-facing fixtures.

---

## FAQ

### Why do we have negative “known leak” fixtures?
To prevent regressions where policy changes accidentally allow sensitive details to escape. These fixtures are designed to fail open systems and pass only when deny/redact behavior is correct.

### Are fixtures “just test data”?
Not in KFM. Fixtures influence governance behaviors, provenance expectations, and policy enforcement. Treat them as governed artifacts.

### Can we store real Kansas locations if they’re public?
Only if:
- the license is explicit and compatible, and
- the content does not increase risk (no restricted sites), and
- the fixture metadata documents provenance and license clearly.

When in doubt: use synthetic data and/or generalize.

---