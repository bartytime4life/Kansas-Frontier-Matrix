<!--
File: tests/data/README.md
Project: Kansas Frontier Matrix (KFM)
Purpose: Governed, deterministic test fixtures for CI + local testing
Last-updated: 2026-02-14
-->

# `tests/data` — KFM Test Fixtures

![governed](https://img.shields.io/badge/governed-yes-blue)
![deterministic](https://img.shields.io/badge/deterministic-required-brightgreen)
![no-pii](https://img.shields.io/badge/no%20PII-required-orange)
![ci-fast](https://img.shields.io/badge/CI-fast%20fixtures-success)

This directory contains **small, deterministic, synthetic** data fixtures used by KFM automated tests (unit, contract, integration, and policy tests). The goal is to keep CI **fast** and to make governance rules **testable** and **repeatable**.

> ✅ **Rule of thumb:** If a fixture would be “unsafe” or “too large” to ship to every developer laptop and CI run, it does **not** belong here.

---

## Contents

- [Why this folder exists](#why-this-folder-exists)
- [Non-negotiable rules](#non-negotiable-rules)
- [What belongs here](#what-belongs-here)
- [Directory layout](#directory-layout)
- [Fixture manifest](#fixture-manifest)
- [Naming conventions](#naming-conventions)
- [Determinism, digests, and golden vectors](#determinism-digests-and-golden-vectors)
- [How tests should use fixtures](#how-tests-should-use-fixtures)
- [Adding or updating fixtures](#adding-or-updating-fixtures)
- [Safety, sensitivity, and CARE/FAIR notes](#safety-sensitivity-and-carefair-notes)
- [Maintenance rules](#maintenance-rules)
- [Appendix: Example objects](#appendix-example-objects)

---

## Why this folder exists

KFM is a **governed** system: requests must be policy-checked, provenance must be resolvable, and outputs must cite evidence or abstain. Tests should **prove** those invariants with concrete data and expected outcomes.

This folder enables tests that validate:

- **Schema correctness** (required fields, ID patterns, provenance blocks)
- **Policy gates** (default deny; “No Source, No Answer”)
- **Provenance integrity** (`spec_hash` reproducibility; artifact digest matches)
- **Catalog minimums** (STAC/DCAT/PROV are present for publishable artifacts)
- **Sensitivity handling** (no leaking precise restricted locations; generalized geometry where required)

---

## Non-negotiable rules

> These rules are strict because fixtures are “quietly powerful” — they shape what CI accepts.

### 1) Synthetic-first (no real sensitive data)

- ✅ Use synthetic data designed to exercise code paths.
- ✅ If you must mirror a real structure (e.g., a STAC Item), keep values fake.
- ❌ Never include secrets (API keys, tokens, credentials), even if expired.
- ❌ Never include private individuals’ info, private landowner details, or precise restricted site coordinates.

### 2) Small + fast

- Keep fixtures tiny and CI-friendly.
- Prefer **1–50 rows/features**, not thousands.
- Prefer text formats (JSON/CSV/GeoJSON) over heavy binaries.
- If a binary is unavoidable, keep it extremely small and clearly justified.

### 3) Deterministic bytes

Fixtures must not “wiggle” between runs:

- Stable ordering of keys (for JSON) and stable line endings (`\n`).
- Fixed timestamps where used (do not embed “now”).
- No random values unless seeded and recorded.

### 4) Every fixture is self-describing

Every fixture must be discoverable via:
- a **manifest entry** (preferred), and/or
- a local **README** inside the fixture folder (only when needed)

### 5) License + sensitivity are always declared

Even for synthetic data, we still declare:
- `license` (use `CC0-1.0` for purely synthetic fixtures unless there is a reason not to)
- `sensitivity` (`public` for synthetic fixtures unless explicitly modeling restricted behavior)

---

## What belongs here

| Fixture category | Purpose | Typical tests |
|---|---|---|
| **Schema fixtures** | Validate JSON schema rules (required fields, ID formats, provenance blocks) | schema/unit tests |
| **Policy fixtures** | Validate default-deny and cite-or-abstain decision logic | OPA/unit + contract tests |
| **Provenance fixtures** | Validate receipts, lineage, hashes, and integrity checks | provenance/unit + integration |
| **Catalog fixtures** | Minimal STAC/DCAT/PROV examples for publish prerequisites | catalog/contract tests |
| **Geospatial fixtures** | Small GeoJSON/WKT/time range examples for spatial-temporal logic | domain/unit tests |
| **API golden responses** | Stable expected payloads (with citations/audit refs) | contract tests |

> Production datasets belong in the governed `data/` zones (raw/work/processed/catalogs). This directory is **test-only**.

---

## Directory layout

This is the **recommended** structure for `tests/data/` in KFM:

```text
tests/data/
  README.md

  manifest.json                 # authoritative index of fixtures + digests

  fixtures/
    catalogs/
      stac/                      # minimal STAC Collections/Items (valid/invalid)
      dcat/                      # minimal DCAT dataset records (valid/invalid)
      prov/                      # minimal PROV docs used as publish prerequisites
    provenance/
      run_receipts/              # run receipt examples (pass/fail)
      spec_hash_vectors/         # canonicalization inputs + expected spec_hash outputs
      digest_vectors/            # file digest examples + expected values
    policy/
      inputs/                    # policy input objects (actor/resource/answer)
      expected/                  # expected allow/deny outputs (or snapshots)
    geo/
      geojson/                   # tiny GeoJSON features (points/lines/polys)
      wkt/                       # tiny WKT examples
      time/                      # time-range fixtures
    api/
      responses/                 # golden response JSON for contract tests (if used)

  golden/
    README.md                    # what “golden” means in this repo (optional)
```

If your repo does not yet contain some of these folders, create them when introducing the first fixture of that type.

---

## Fixture manifest

`manifest.json` is the **index** of all fixtures in this folder. It enables:

- quick discovery (`id → path`)
- reproducibility (`sha256` / byte size)
- lightweight governance (license/sensitivity declared everywhere)

### Manifest contract (recommended)

**File:** `tests/data/manifest.json`

```json
{
  "manifest_version": "1",
  "generated_at": "2026-02-14T00:00:00Z",
  "fixtures": [
    {
      "id": "kfm.fixture.provenance.run_receipt.pass.v1",
      "path": "fixtures/provenance/run_receipts/run_receipt_pass.json",
      "sha256": "3c8b4d16c6ab0e7b74e5b0b05b35f3c0e5c1b3cf1df7f2a1f4a2bb4a4e9b7c11",
      "bytes": 742,
      "license": "CC0-1.0",
      "sensitivity": "public",
      "purpose": "Golden pass case for receipt schema validation",
      "tags": ["provenance", "run_receipt", "pass"]
    }
  ]
}
```

### Required fields

Every `fixtures[]` entry MUST include:

- `id` (stable ID; see [Naming conventions](#naming-conventions))
- `path` (relative to `tests/data/`)
- `sha256`
- `bytes`
- `license`
- `sensitivity`
- `purpose`

---

## Naming conventions

Stable names make tests and reviews easier.

### Fixture IDs

Use a reverse-domain-ish stable identifier:

```
kfm.fixture.<category>.<name>.<variant>.v<major>
```

Examples:
- `kfm.fixture.catalogs.stac.collection.minimal.valid.v1`
- `kfm.fixture.catalogs.dcat.dataset.minimal.missing_license.v1`
- `kfm.fixture.provenance.spec_hash.vector.basic.v1`
- `kfm.fixture.policy.kfm_ai.deny_without_citations.v1`

### File names

Use `snake_case` and be explicit about pass/fail:

- `*_pass.json`
- `*_fail_missing_license.json`
- `*_fail_bad_geometry.json`

---

## Determinism, digests, and golden vectors

KFM tests often rely on **integrity properties**:

- The same canonical spec produces the same `spec_hash`.
- A catalog-advertised digest matches the computed file digest.
- Policy behavior stays stable across refactors.

### SHA-256 digest computation

Use one of:

**Linux:**
```bash
sha256sum path/to/file
```

**macOS:**
```bash
shasum -a 256 path/to/file
```

**Portable (Python):**
```python
import hashlib, pathlib

p = pathlib.Path("path/to/file")
h = hashlib.sha256(p.read_bytes()).hexdigest()
print(h)
```

### Golden vectors

“Golden vectors” are fixtures whose **expected outputs must never change** without an intentional review.

Examples:
- `spec_hash_vectors/*` (input → expected hash)
- `digest_vectors/*` (file → expected sha256)
- `api/responses/*` (expected response snapshots)

When a golden vector changes:
- update the fixture
- update the test expectation
- document **why the change is correct** in the PR description

---

## How tests should use fixtures

### Path access rule

Tests should access fixtures **relative to this folder** (not via absolute paths). A typical pattern:

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"   # tests/data
FIXTURES = DATA_DIR / "fixtures"
```

### “Do not bake environment assumptions” rule

Fixtures must be readable in:
- local dev
- CI runners
- containers
- offline mode

So, tests should not rely on:
- network calls
- current time
- system locale
- external services

### Policy test usage (OPA / Conftest style)

If policy fixtures are used for OPA tests, keep it explicit:

- `fixtures/policy/inputs/*.json` → policy input objects
- `fixtures/policy/expected/*.json` → expected allow/deny outputs (or snapshots)

---

## Adding or updating fixtures

### ✅ Definition of Done (fixture PR)

- [ ] Fixture is **synthetic** and contains **no secrets** and **no PII**
- [ ] Fixture is **small** (justify if > 200 KB)
- [ ] Fixture is **deterministic** (stable ordering, stable timestamps)
- [ ] `license` and `sensitivity` are declared in `manifest.json`
- [ ] `sha256` and `bytes` in `manifest.json` match the committed file
- [ ] A test references the fixture and asserts something meaningful (not “loads successfully”)
- [ ] If the fixture is “golden,” the PR explains why the new expected value is correct

### Step-by-step workflow

1. Pick the right folder under `fixtures/` (or create it).
2. Add the new fixture file(s).
3. Compute `sha256` and `bytes`.
4. Add a new entry to `manifest.json`.
5. Add/extend tests to use the fixture.
6. Run the test suite locally (or in the repo’s container workflow).
7. Ensure CI passes.

---

## Safety, sensitivity, and CARE/FAIR notes

KFM handles potentially sensitive material (e.g., private ownership, precise archaeological site locations, and certain safety indicators). Even in tests, we avoid embedding anything that could normalize unsafe patterns.

### Practical safety rules for fixtures

- Use **generalized** geometries when modeling restricted behavior:
  - Example: use a bounding box or coarse polygon instead of precise points.
- Use fake place names and fake identifiers.
- Prefer `public` sensitivity for synthetic fixtures.
- When modeling restricted cases, label explicitly (but keep the values fake).

> If a fixture *needs* to represent a sensitive scenario, do it with **synthetic values** and ensure the policy path denies/filters appropriately.

---

## Maintenance rules

### Keep fixtures prunable

If code changes make a fixture unnecessary, remove it and its manifest entry.

### Avoid fixture sprawl

Before adding a new fixture:
- check whether an existing one can be extended
- prefer parameterized tests over new files when reasonable

### Never “fix tests by weakening fixtures”

If a governance rule breaks tests, the correct outcomes are:
- update the implementation to match the rule, or
- explicitly change the rule (policy/schema) with review and updated tests

---

## Appendix: Example objects

<details>
  <summary><strong>Example: run receipt (minimal synthetic)</strong></summary>

```json
{
  "example": "kfm.run_receipt.v1",
  "fetched_at": "2026-02-13T00:00:00Z",
  "accessURL": "https://example.org/source",
  "etag": "W/\"abc123\"",
  "last_modified": "Wed, 12 Feb 2026 00:00:00 GMT",
  "spec_hash": "sha256:1111111111111111111111111111111111111111111111111111111111111111",
  "artifact_digest": "sha256:2222222222222222222222222222222222222222222222222222222222222222",
  "tool_versions": { "pipeline": "1.0.0" },
  "policy_gate": {
    "status": "pass",
    "checks": ["license_present", "stac_present"]
  }
}
```

</details>

<details>
  <summary><strong>Example: spec_hash golden vector format</strong></summary>

```json
{
  "id": "kfm.fixture.provenance.spec_hash.vector.basic.v1",
  "canonical_input_json": {
    "dataset_id": "example_dataset",
    "license": "CC-BY-4.0",
    "source": { "type": "http", "uri": "https://example.org/source.csv" }
  },
  "expected_spec_hash": "sha256:3333333333333333333333333333333333333333333333333333333333333333"
}
```

</details>

