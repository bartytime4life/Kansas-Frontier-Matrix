---
title: "🧰 Common Mapper Utilities — Normalization • Validation • IDs • Time • Units"
path: "api/src/adapters/mappers/common/README.md"
version: "v0.1.0"
last_updated: "2026-01-11"
status: "draft"
doc_kind: "Module README"
license: "CC-BY-4.0"

# KFM governance header
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
pipeline_ordering: "ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode"
---

![Layer](https://img.shields.io/badge/layer-adapters-informational)
![Module](https://img.shields.io/badge/module-mappers%2Fcommon-7b2cbf)
![Principle](https://img.shields.io/badge/principle-pure%20functions-blue)
![Principle](https://img.shields.io/badge/principle-deterministic-orange)
![Quality](https://img.shields.io/badge/quality-contract--first-0ea5e9)
![Safety](https://img.shields.io/badge/safety-no%20I%2FO%20%7C%20no%20secrets-ef4444)

# 🧰 Common Mappers (`api/src/adapters/mappers/common/`)

This folder is the **shared toolbox** for all mappers (HTTP/GraphQL/events/geo/catalog).  
It contains **small, pure, reusable** helpers that enforce consistent behavior across the API boundary:

- 🆔 stable IDs & hashing
- ⏳ time parsing & normalization
- 📏 units & numeric coercion
- 🧭 bbox/CRS-safe parsing primitives (the *generic* bits)
- 🔐 classification/redaction propagation helpers
- 🧼 string normalization & enum canonicalization
- ✅ validation primitives and “boring” mapper errors

> [!IMPORTANT]
> **Common** is where we eliminate drift. If “bbox parsing” or “time normalization” is duplicated in three endpoints, it belongs here.

---

## 🔗 Neighbor links

- 📦 Parent: `📁 api/src/adapters/mappers/README.md`
- 📚 Catalog mappers: `📁 api/src/adapters/mappers/catalog/README.md`
- 🛬 Inbound: `📁 api/src/adapters/inbound/README.md`
- 🛫 Outbound: `📁 api/src/adapters/outbound/README.md`
- 🧯 Errors: `📄 api/src/adapters/errors.py`

---

## 📁 Folder map (emoji layout)

```text
📁 api/
  📁 src/
    📁 adapters/
      📁 mappers/
        📁 common/                          🧰 shared mapping primitives (pure)
          📄 README.md                      👈 you are here
          📄 __init__.py                    🧬 package init (optional)
          📄 ids.py                         🆔 stable IDs + slug helpers
          📄 hashing.py                     #️⃣ stable hashing / fingerprints
          📄 time.py                         ⏳ ISO-8601 parsing, UTC normalization, fuzzy ranges
          📄 units.py                        📏 numeric coercion + units utilities
          📄 classification.py               🔐 classification/redaction merge + guards
          📄 strings.py                      🧼 normalization (trim, casefold, safe charset)
          📄 enums.py                        🧾 enum canonicalization + versioned mappings
          📄 validate.py                     ✅ reusable validation functions
          📄 hrefs.py                        🔗 safe href/url/path validators (no secret leaks)
          📄 ordering.py                     🔢 deterministic ordering helpers for JSON outputs
          📄 errors.py                       🧯 MapperError types/codes (no stack traces)
```

> [!TIP]
> “Common” should stay **small and stable**. If it grows into a giant utils dump, split by theme (`time/`, `geo/`, `policy/`) with strict ownership.

---

## 🎯 What “common” is for (and what it is not)

### ✅ In scope
- Tiny pure functions shared across many mappers
- Canonical normalization rules (time, bbox, IDs, strings)
- Deterministic ordering helpers (for stable JSON fixtures)
- Validation primitives (range checks, required fields, safe href checks)
- “Never downgrade classification” enforcement helpers

### ❌ Out of scope
- Any I/O (DB, HTTP, filesystem, env vars)
- Business rules (“what should we do with this request?”)
- Framework objects (FastAPI Request, Response, Depends…)
- “Smart” heuristics (“guess the CRS” / “infer the unit” unless explicitly allowed)

---

## ✅ Non‑negotiables (common rules)

> [!IMPORTANT]
> All functions here must be:
> - 🧼 **Pure** (no I/O)
> - 🔁 **Deterministic** (same inputs → same outputs)
> - 🔍 **Auditable** (clear behavior; no hidden globals)
> - 🧪 **Easy to unit test** (no fixtures needed)

### “No hidden time” rule ⛔⏱️
- ❌ no `datetime.now()` / `time.time()` inside mapping helpers
- ✅ accept `now` as an injected parameter if needed

### “No secret leakage” rule ⛔🔑
- Don’t allow hrefs/paths that contain:
  - access tokens
  - embedded credentials
  - signed query params (unless explicitly permitted in higher layers)

---

## 🧩 Common primitives you should expect to find (or add)

### 🆔 Stable IDs (`ids.py`)
**Why:** catalogs/graph/provenance require stable references.

What belongs here:
- `slugify(text) -> str`
- `stable_id(prefix, *parts) -> str`
- `versioned_id(base_id, version) -> str`

Rules:
- normalize inputs (trim + casefold) before hashing
- avoid locale-sensitive transforms
- keep IDs URL-safe (`[a-z0-9-_]`)

---

### #️⃣ Hashing & fingerprints (`hashing.py`)
**Why:** derived artifacts need reproducible identity.

What belongs here:
- `stable_hash_dict(obj) -> str` (canonical JSON serialization)
- `fingerprint_params(params) -> str` (sorted keys, stable float formatting)
- `hash_bytes(data) -> str`

Rules:
- stable key ordering
- stable float normalization (avoid `repr()` surprises)
- stable encoding (`utf-8`)

---

### ⏳ Time parsing & normalization (`time.py`)
**Why:** KFM is timeline-heavy; precision matters.

What belongs here:
- `parse_iso8601(s) -> datetime`
- `ensure_utc(dt) -> datetime`
- `normalize_interval(start, end) -> (start, end)`
- `parse_fuzzy_date(s) -> FuzzyDateRange` *(only if the project supports it)*

Rules:
- clearly document timezone behavior
- never fabricate precision for uncertain historical dates
- allow “open intervals” where appropriate (e.g., `end=None`)

---

### 📏 Units & numeric coercion (`units.py`)
**Why:** consistent units prevent silent corruption.

What belongs here:
- `to_float(s) -> float` with strict validation
- `clamp(value, min, max) -> value`
- `safe_int(value) -> int` (reject “1e3” unless explicitly allowed)
- `meters_to_degrees_at_lat(...)` *(only if needed and well-documented)*

Rules:
- reject NaN/inf
- enforce ranges early (bbox sizes, limits, zoom, etc.)

---

### 🔐 Classification & redaction propagation (`classification.py`)
**Why:** derived outputs must not be less restricted than inputs.

What belongs here:
- `merge_classification(a, b) -> classification`
- `assert_no_downgrade(input_cls, output_cls)`
- `merge_redaction_notes(list_a, list_b) -> list`

Rules:
- “max restriction wins”
- redaction notes append-only (no silent drops)

---

### 🧼 String normalization (`strings.py`)
**Why:** reliable mapping and stable IDs.

What belongs here:
- `normalize_whitespace(s)`
- `casefold_safe(s)`
- `strip_control_chars(s)`
- `ensure_ascii_slug(s)` *(if required for certain IDs)*

Rules:
- document any lossy transformations
- never “correct spelling” inside mappers

---

### 🧾 Enum canonicalization (`enums.py`)
**Why:** wire contracts evolve; domain needs stable values.

What belongs here:
- `canon_format("GeoJSON") -> "geojson"`
- versioned mappings: `V1_FORMATS`, `V2_FORMATS`
- `validate_enum(value, allowed)`

Rules:
- strict: reject unknown values (unless the contract explicitly allows forward-compat)
- keep compatibility maps versioned

---

### 🔗 Safe href validation (`hrefs.py`)
**Why:** catalogs can become exfiltration vectors.

What belongs here:
- `is_safe_href(href) -> bool`
- `assert_safe_href(href)`
- `redact_sensitive_query_params(href) -> href`

Rules:
- forbid `user:pass@host`
- forbid token-like query params by default (`token=`, `sig=`, `X-Amz-Signature=`, etc.)
- allowlist schemes (`https`, `s3`, `file` in dev) with explicit config above this layer

---

### 🔢 Deterministic ordering (`ordering.py`)
**Why:** stable JSON = stable tests + stable hashing.

What belongs here:
- `sorted_dict(obj) -> OrderedDict`
- `sort_assets(assets_dict) -> dict`
- stable list sort helpers for links, roles, etc.

Rules:
- never rely on interpreter dict order assumptions for canonicalization logic
- be explicit in how ties are handled

---

### ✅ Validation primitives (`validate.py`)
**Why:** consistent boundary hardening.

What belongs here:
- `require(condition, code, field, detail)`
- `require_non_empty(s, field)`
- `require_in_range(x, min, max, field)`
- `validate_bbox(minx, miny, maxx, maxy)` *(generic ordering + range checks)*

Rules:
- mapper errors should be **typed and boring**
- include field paths for client-friendly responses

---

## 🧯 Mapper errors (keep them boring)

Prefer codes that are:
- stable across refactors
- easy to search in logs
- easy to document in OpenAPI examples

Examples:
- `INVALID_BBOX`
- `INVALID_TIME`
- `INVALID_ENUM`
- `UNSAFE_HREF`
- `CLASSIFICATION_DOWNGRADE_ATTEMPT`

> [!TIP]
> Put these codes in one place and treat them like an API surface. Changing codes is a breaking change 📜💥

---

## 🧪 Testing (common should be the easiest layer to test)

Recommended test structure:
```text
🧪 tests/
  📁 mappers/
    📁 common/
      📄 test_ids.py
      📄 test_hashing.py
      📄 test_time.py
      📄 test_classification.py
      📄 test_hrefs.py
```

Suggested test style:
- ✅ table-driven tests
- ✅ edge cases (empty strings, weird unicode, NaN/inf, timezone offsets)
- ✅ property tests (optional): “classification never downgrades”, “hash is stable”

---

## 🧱 Templates (copy/paste)

### 1) “Require” helper pattern ✅

```python
# 📄 api/src/adapters/mappers/common/validate.py

from dataclasses import dataclass

@dataclass(frozen=True)
class MapperError(Exception):
    code: str
    field: str | None = None
    detail: str | None = None

def require(condition: bool, *, code: str, field: str | None = None, detail: str | None = None) -> None:
    if not condition:
        raise MapperError(code=code, field=field, detail=detail)
```

### 2) Canonical JSON hashing (stable fingerprint) #️⃣

```python
# 📄 api/src/adapters/mappers/common/hashing.py

import hashlib
import json
from typing import Any

def stable_hash_dict(obj: Any) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
```

### 3) Safe href guard 🔗

```python
# 📄 api/src/adapters/mappers/common/hrefs.py

import re
from .validate import require

_SUSPECT_PARAMS = re.compile(r"(token|sig|signature|apikey|api_key|password|secret)=", re.IGNORECASE)

def assert_safe_href(href: str) -> None:
    require("@" not in href.split("://", 1)[-1].split("/", 1)[0], code="UNSAFE_HREF", field="href",
            detail="href must not contain embedded credentials")
    require(not _SUSPECT_PARAMS.search(href), code="UNSAFE_HREF", field="href",
            detail="href must not contain secret-like query params")
```

> [!NOTE]
> These are intentionally minimal. In real code, you’ll likely parse URLs properly and enforce scheme allowlists.

---

## ✅ Definition of done (for adding/modifying `common/` helpers)

- [ ] Function is pure and deterministic
- [ ] Behavior is documented (docstring + examples if non-obvious)
- [ ] Includes unit tests (edge cases included)
- [ ] Does not create “policy drift” (used consistently across mappers)
- [ ] Error codes are stable and documented
- [ ] No new “god util” patterns introduced (keep modules small & themed)

---

## 📚 Project bookshelf (all project files, mapped to “common” needs)

<details>
<summary>📚 Click to expand — how the full project library informs common mapper rules</summary>

### 🧭 KFM architecture, governance, and documentation discipline
- 📄 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx** → layered boundaries, stable contracts, governed pipeline expectations
- 📄 **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx** → forward compatibility, performance/scale goals, interoperability direction
- 📄 **MARKDOWN_GUIDE_v13.md.gdoc** → repo conventions, pipeline ordering language, contract-first docs style
- 📄 **Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx** → consistent doc structure, checklists, and conventions

### 🗺️ Geospatial IO & representation (why bbox/time/format validation is strict)
- 📄 **python-geospatial-analysis-cookbook.pdf** → practical GIS parsing/format norms; CRS hygiene patterns
- 📄 **making-maps-a-visual-guide-to-map-design-for-gis.pdf** → representation matters; avoid misleading precision; provide thumbnails/overviews
- 📄 **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf** → scale/context sensitivity; mobile constraints; privacy implications
- 📄 **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf** → correct media typing; stable handling of image derivatives
- 📄 **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf** → asset typing and consistent data shaping for interactive clients
- 📄 **responsive-web-design-with-html5-and-css3.pdf** → predictable contracts for web clients; stable enum canonicalization

### 🛰️ Remote sensing / Earth Engine (why provenance + uncertainty support exists)
- 📄 **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf** → EO outputs are models; track parameters, sources, and accuracy

### 🧪 Modeling, stats, and uncertainty (why we don’t fake precision)
- 📄 **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf** → reproducibility mindset; deterministic runs; declared inputs/outputs
- 📄 **Understanding Statistics & Experimental Design.pdf** → valid inference requires explicit assumptions; be precise about intervals and uncertainty
- 📄 **regression-analysis-with-python.pdf** → model artifacts need parameters + diagnostics metadata
- 📄 **Regression analysis using Python - slides-linear-regression.pdf** → compact reporting patterns; stable “evidence artifacts”
- 📄 **think-bayes-bayesian-statistics-in-python.pdf** → uncertainty is a first-class output; credible intervals need clear semantics
- 📄 **graphical-data-analysis-with-r.pdf** → exploratory artifacts should still be traceable; avoid narrative without references
- 📄 **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf** → model/version tracking; dataset splits/params as stable metadata

### 🗄️ Data systems, scaling, interoperability (why deterministic ordering + hashing matters)
- 📄 **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf** → stable typing; careful conversions; avoid silent coercions
- 📄 **Scalable Data Management for Future Hardware.pdf** → performance constraints; caching keys must be stable; avoid repeated serialization
- 📄 **Data Spaces.pdf** → interoperability & federation; metadata glue requires strict normalization

### 🕸️ Graph/optimization (why IDs and references must be stable)
- 📄 **Spectral Geometry of Graphs.pdf** → graph artifacts depend on stable definitions/encodings
- 📄 **Generalized Topology Optimization for Structural Design.pdf** → optimization runs produce paramized outputs; stable fingerprints are essential

### 🧠 Humanism + law foundations (why transparency & accountability are enforced)
- 📄 **Introduction to Digital Humanism.pdf** → human-centered accountability; explainable metadata choices
- 📄 **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf** → governance expectations for ML outputs; traceability norms
- 📄 **Principles of Biological Autonomy - book_9780262381833.pdf** → systems thinking; keep “why/how” metadata for adaptive behavior

### 🛡️ Security mindset (why href validation exists)
- 📄 **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf** → threat modeling; don’t leak secrets via metadata or logs
- 📄 **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf** → adversarial thinking; validate inputs and avoid “clever parsing”

### 🧵 Concurrency / distributed execution (why “no hidden now()” is a rule)
- 📄 **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf** → distributed runs require explicit time semantics and stable IDs

### 🧰 Programming compendium shelf (implementation reference)
- 📄 **A programming Books.pdf**
- 📄 **B-C programming Books.pdf**
- 📄 **D-E programming Books.pdf**
- 📄 **F-H programming Books.pdf**
- 📄 **I-L programming Books.pdf**
- 📄 **M-N programming Books.pdf**
- 📄 **O-R programming Books.pdf**
- 📄 **S-T programming Books.pdf**
- 📄 **U-X programming Books.pdf**

</details>

