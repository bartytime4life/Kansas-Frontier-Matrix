# `tests/data/` — Test Fixtures & Governed Sample Data 🌾🧪

![Governed](https://img.shields.io/badge/Governed-FAIR%2BCARE-blue)
![Evidence-first](https://img.shields.io/badge/Evidence--first-required-success)
![Deterministic](https://img.shields.io/badge/Deterministic-fixtures-important)

This directory contains **small, deterministic, test-only datasets** used to validate KFM pipelines, services, APIs, and UI behaviors **without** relying on external networks, partner systems, or production databases.

> [!IMPORTANT]
> **No production exports belong here.**  
> This folder must remain safe to publish (open-source-friendly) unless explicitly marked otherwise and protected by repository access controls.

---

## What belongs here ✅

| Category | Examples | Why |
|---|---|---|
| Minimal fixtures | tiny CSV/GeoJSON/JSON used by unit tests | fast, deterministic |
| Golden snapshots | expected outputs (“known good”) | regression detection |
| Edge-case samples | malformed geometries, missing dates, weird encodings | harden validators |
| Redaction examples | “before/after” generalized geometries or removed fields | governance testing |
| Synthetic data | generated entities/events/locations | avoids privacy & cultural risk |

---

## What does **not** belong here ❌

- **Real personal data** (names, emails, phone numbers, addresses, free-text notes from individuals).
- **Sensitive site locations** (e.g., exact archaeological coordinates; culturally restricted info).
- **Partner-restricted datasets** unless:
  - license explicitly allows inclusion in this repository, and
  - governance review approves inclusion, and
  - access controls are in place (if required).
- **Large blobs** (full rasters, multi-GB shapefiles, raw satellite stacks).
- **Anything that forces tests to call the public internet** (tests must be offline-capable).

> [!WARNING]
> If a test requires “realism,” prefer **small extracts** + **synthetic augmentation** + **documented assumptions**.  
> Never trade safety and licensing clarity for realism.

---

## Governance rules (non-negotiable) 🛡️

All files in `tests/data/` must comply with these principles:

1. **Evidence-first & traceability**
   - Every fixture must have a clear origin story (even synthetic ones).
   - Every non-trivial fixture must be registered in the **Fixture Manifest** (below).

2. **FAIR + CARE alignment**
   - Metadata must include license, provenance, and any constraints.
   - If data could represent sensitive knowledge, it must be **generalized/redacted**.

3. **Sensitivity handling**
   - If a point/line/polygon is derived from a sensitive location, store **generalized geometry**:
     - reduce coordinate precision,
     - snap to grid,
     - aggregate to bounding box or centroid jitter,
     - or replace with synthetic stand-ins.

4. **Trust membrane preserved**
   - Fixtures must be used through test adapters/repository interfaces.
   - Tests should not “reach around” governance by querying DBs directly unless the test is explicitly about DB adapters **and** is isolated in integration tests.

---

## Directory layout 📁

> This layout is the **recommended** structure. If the repo differs, update this README to match reality.

```text
tests/
└── data/
    ├── README.md                      # you are here
    ├── manifest.yml                   # required: fixture registry (see below)
    │
    ├── fixtures/                      # small inputs for unit/integration tests
    │   ├── tabular/                   # CSV/TSV/Parquet-mini
    │   ├── geojson/                   # GeoJSON fixtures (small)
    │   └── json/                      # API payload fixtures (JSON)
    │
    ├── golden/                        # expected outputs (snapshots)
    │   ├── pipeline/                  # pipeline stage outputs
    │   └── api/                       # API response snapshots
    │
    ├── redaction/                     # governance tests (before/after examples)
    │   ├── before/                    # should never be sensitive in reality; use synthetic
    │   └── after/                     # generalized/redacted safe versions
    │
    └── docs/                          # optional: fixture-specific notes & diagrams
        └── <fixture-id>.md
```

---

## Fixture Manifest (`tests/data/manifest.yml`) 📌

The manifest is the **registry of truth** for this folder: it tells tests (and reviewers) what each file is, where it came from, and how it may be used.

### Minimal schema (recommended)

```yaml
version: 1

fixtures:
  - id: example_roads_small_v1
    description: "Tiny road network subset for routing tests (synthetic)."
    paths:
      - "fixtures/geojson/roads_small_v1.geojson"
    format: "geojson"
    license:
      spdx: "CC0-1.0"
      notes: "Synthetic; safe to redistribute."
    provenance:
      origin: "synthetic"
      generated_by: "scripts/generate_test_roads.py"
      generated_at: "2026-02-16"
    sensitivity:
      classification: "public"          # public | internal | sensitive | restricted
      handling: "none"                 # none | generalized | redacted | permissioned
    used_by:
      - "tests/routing/test_shortest_path.py::test_basic_route"
    guarantees:
      deterministic: true
      max_runtime_ms: 200
```

### Required fields checklist

- [ ] `id` (stable, unique)
- [ ] `paths` (relative paths)
- [ ] `format` (csv|tsv|json|geojson|ndjson|parquet|…)
- [ ] `license` (SPDX where possible)
- [ ] `provenance` (origin + generator or source reference)
- [ ] `sensitivity` (classification + handling)
- [ ] `used_by` (at least one test reference)

> [!TIP]
> If a fixture is generated, prefer committing:
> - the **small generated artifact**, and
> - the **generator script** (or documented command) so it can be reproduced.

---

## File naming conventions 🏷️

Use stable, descriptive names:

```text
<domain>_<shape>_<size>_v<major>[.<ext>]
```

Examples:

- `events_temporal_micro_v1.json`
- `counties_bbox_small_v2.geojson`
- `catalog_minimal_v1.ndjson`

Rules:
- Use lowercase + underscores.
- Include a version bump when semantics change (`v1` → `v2`).
- Keep file names aligned with manifest `id`.

---

## Geospatial fixture rules 🌐

| Rule | Why |
|---|---|
| Prefer EPSG:4326 (WGS84) unless a test is explicitly projection-focused | avoids confusion |
| Keep geometry counts small | performance + readability |
| Include at least one invalid geometry fixture (separate file) | validator coverage |
| Reduce precision for generalized locations | safety & governance |
| Avoid “real” sensitive points even if public in another context | risk minimization |

### Suggested generalization patterns

- **Precision drop:** 6 decimals → 3 decimals (≈ 100m) or worse if needed  
- **Grid snap:** snap to a fixed grid size (e.g., 1km)
- **Jitter:** random offset with a fixed seed + bounded radius
- **Aggregation:** replace a point with a polygon bbox centroid or a coarse polygon

---

## Determinism & test stability ⏱️

To keep CI stable:

- Fix random seeds (`SEED=42`) for synthetic generators.
- Don’t use “current time” unless you freeze it in the test.
- Keep fixtures **tiny** and tests **fast**.
- If a golden snapshot changes, treat it as a breaking change:
  - update manifest notes,
  - explain why,
  - link to the test(s) impacted.

---

## Adding or updating fixtures ✅ (Definition of Done)

- [ ] Fixture file is **small**, **safe**, and **offline-capable**
- [ ] License is explicit (SPDX if possible)
- [ ] Provenance is documented (source or generator)
- [ ] Sensitivity classification set + handling described
- [ ] `manifest.yml` updated
- [ ] Tests updated/added and pass locally
- [ ] CI passes (including any fixture lint checks)
- [ ] If the fixture models historically/culturally sensitive content: flagged for governance review

---

## Suggested CI guardrails (optional but recommended) 🤖

If not already present, add a lightweight CI check that fails when:

- `tests/data/manifest.yml` missing or invalid
- new files not registered in the manifest
- any file exceeds size threshold (e.g., 5–10 MB)
- disallowed file types are added (e.g., `.sqlite`, `.pdf`, `.tif` unless explicitly permitted)

---

## Reference (project principles)

This folder follows KFM’s overarching principles:

- Governed, evidence-first “truth path”
- FAIR + CARE aligned metadata and handling
- Sensitivity-aware sharing
- Trust membrane preserved (no direct DB access from clients)

If you change the rules here, treat it as a **governance-impacting change**.