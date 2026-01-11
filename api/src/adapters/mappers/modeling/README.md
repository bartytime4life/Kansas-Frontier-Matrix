---
title: "🧪 Modeling Mappers — Evidence Artifacts ↔ Domain (Uncertainty • Reproducibility • Provenance)"
path: "api/src/adapters/mappers/modeling/README.md"
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
![Module](https://img.shields.io/badge/module-mappers%2Fmodeling-7b2cbf)
![Discipline](https://img.shields.io/badge/discipline-modeling%20%26%20simulation-0ea5e9)
![Evidence](https://img.shields.io/badge/rule-evidence--first-f97316)
![Repro](https://img.shields.io/badge/rule-reproducible%20runs-22c55e)
![Uncertainty](https://img.shields.io/badge/outputs-uncertainty%20included-111827)
![Safety](https://img.shields.io/badge/safety-no%20I%2FO%20%7C%20no%20secrets-ef4444)

# 🧪 Modeling Mappers (`api/src/adapters/mappers/modeling/`)

This folder contains **pure, deterministic** mapping utilities for *modeling & simulation outputs* (“evidence artifacts”) at the API boundary.

Modeling mappers translate between:
- 🧠 **Domain results** (runs, experiments, analyses)  
  → 📦 **Stable, client-safe DTOs** (REST/GraphQL/event outputs)
- 📦 **Inbound modeling requests** (params, ROI, time windows)  
  → 🧠 **Domain commands/queries**
- 🧾 **Provenance + catalog references** (STAC/DCAT/PROV IDs)  
  → embedded metadata that keeps results auditable
- 📈 **Uncertainty & diagnostics** (CI/credible intervals, residual summaries, confusion matrices, etc.)  
  → consistent summary shapes (no hand-wavy “confidence”)

> [!IMPORTANT]
> Modeling mappers are an **anti-corruption layer** for science-grade outputs:
> - ✅ map + validate + normalize + annotate
> - ✅ enforce reproducibility metadata (run IDs, hashes, versions)
> - ✅ enforce uncertainty semantics (what kind, what units, what meaning)
> - ❌ no DB/Neo4j/PostGIS access
> - ❌ no filesystem/network calls
> - ❌ no “current time” generation (inject timestamps from services)
> - ❌ no business decisions (“what should we run?”) — services decide

---

## 🔗 Neighbor links

- 📦 Parent: `📁 api/src/adapters/mappers/README.md`
- 🧰 Shared primitives: `📁 api/src/adapters/mappers/common/README.md`
- 🗺️ Geo helpers (ROI, bbox, CRS): `📁 api/src/adapters/mappers/geo/README.md`
- 📚 Catalog mappers (STAC/DCAT/PROV): `📁 api/src/adapters/mappers/catalog/README.md`
- 🛬 Inbound adapters: `📁 api/src/adapters/inbound/README.md`
- 🛫 Outbound adapters: `📁 api/src/adapters/outbound/README.md`
- 🧯 Adapter errors: `📄 api/src/adapters/errors.py`

---

## 🧭 Table of contents

- [📁 Folder map](#-folder-map)
- [🎯 What belongs here](#-what-belongs-here)
- [🧠 Modeling artifacts KFM should treat as “evidence”](#-modeling-artifacts-kfm-should-treat-as-evidence)
- [📦 Canonical evidence DTO shape](#-canonical-evidence-dto-shape)
- [🎛️ Parameters, hashes, and reproducibility](#️-parameters-hashes-and-reproducibility)
- [📈 Uncertainty & diagnostics mapping](#-uncertainty--diagnostics-mapping)
- [🗺️ Spatial & temporal semantics](#️-spatial--temporal-semantics)
- [📤 Outputs, assets, and payload size](#-outputs-assets-and-payload-size)
- [🔐 Classification, redaction, and safety](#-classification-redaction-and-safety)
- [🧯 Error codes](#-error-codes)
- [🧪 Testing strategy](#-testing-strategy)
- [🧑‍💻 Templates](#-templates)
- [✅ Definition of done](#-definition-of-done)
- [📚 Project bookshelf](#-project-bookshelf)

---

## 📁 Folder map

```text
📁 api/
  📁 src/
    📁 adapters/
      📁 mappers/
        📁 modeling/                     🧪 modeling & simulation mapping (pure)
          📄 README.md                   👈 you are here
          📄 __init__.py                 🧬 package init (optional)

          📄 requests.py                 🧾 inbound DTO → domain commands/queries
          📄 results.py                  📤 domain results → response DTOs
          📄 metrics.py                  📈 metrics + diagnostics shaping
          📄 uncertainty.py              🎲 CI/credible intervals + error bounds
          📄 artifacts.py                📦 asset refs (plots, COGs, CSV, parquet) + safe href rules
          📄 manifests.py                🗃️ run manifests (params_hash, data_hash, versions)
          📄 normalize.py                🧼 stable normalization (floats, enums, time)
          📄 validate.py                 ✅ pure validation (ranges, required fields)
          📄 errors.py                   🧯 modeling-mapper error codes (optional)
```

> [!TIP]
> If your repo uses different filenames, keep the *separation by concern*:
> `requests / results / uncertainty / manifests / artifacts`.

---

## 🎯 What belongs here

### ✅ In scope
- “Evidence artifact” DTOs (summary + detail variants)
- Stable `run_id`, `model_id`, `params_hash`, `data_hash` shaping
- Strict mapping for modeling inputs:
  - ROI (bbox/polygon), CRS, time range
  - parameter sets + units
  - seeds and reproducibility flags
- Standardized metrics and diagnostics:
  - regression metrics (RMSE, MAE, R², residual summaries)
  - classification metrics (precision/recall/F1, confusion matrix summary)
  - Bayesian summaries (posterior mean/median, HDI/credible interval)
  - simulation diagnostics (convergence flags, step size, stability notes)
- Uncertainty objects (explicit semantics + units)
- Asset reference shaping (plots and large arrays are links, not inline blobs)
- Provenance/citations fields (STAC/DCAT/PROV refs, method disclosure)

### ❌ Out of scope
- Running simulations
- Training models
- Querying PostGIS/Neo4j
- Exporting COGs/tiles
- Writing STAC/DCAT/PROV JSON to storage (catalog mappers + outbound handle that)
- Any “helpful” guessing that changes meaning (units/CRS/timezone)

---

## 🧠 Modeling artifacts KFM should treat as “evidence”

Modeling results should be considered **publishable artifacts** (like datasets), not “temporary responses”:

- 🧪 **Scientific simulations** (forward models, scenario runs, numerical solvers)
- 📈 **Regression & statistical analyses** (linear/logistic, diagnostics, residual analysis)
- 🎲 **Bayesian inference outputs** (posterior summaries, credible intervals, priors)
- 🤖 **Machine learning training runs** (model versioning, dataset splits, metrics)
- 🛰️ **Remote sensing classifications** (accuracy assessment + uncertainty)
- 🧠 **Graph analytics results** (centrality/community outputs as derived evidence)
- 🧱 **Optimization results** (topology optimization outputs, objective/constraints, convergence)
- 🗺️ **Geospatial transformations** that imply claims (change detection, suitability scoring)

> [!NOTE]
> If a result changes an interpretation, it should carry the metadata of a dataset:
> *inputs, method, parameters, uncertainty, and provenance refs* 🧾

---

## 📦 Canonical evidence DTO shape

KFM-friendly evidence outputs should be predictable, and “refs-first”.

### ✅ Recommended top-level fields

```json
{
  "kind": "model_run",
  "run_id": "run_...",
  "model": {
    "model_id": "landcover_rf_v3",
    "model_version": "3.2.1",
    "method": "random_forest",
    "software_versions": {
      "pipeline": "kfm-pipeline@abc123",
      "python": "3.11.x"
    }
  },
  "inputs": {
    "data_refs": [
      { "stac_item_id": "stac_item_...", "role": "training" }
    ],
    "roi": { "bbox": [-99, 37, -94, 40], "crs": "EPSG:4326" },
    "time_range": { "start": "1870-01-01T00:00:00Z", "end": "1870-12-31T23:59:59Z" }
  },
  "parameters": {
    "params_hash": "sha256:...",
    "summary": { "n_trees": 500, "max_depth": 12 }
  },
  "results": {
    "metrics": { "accuracy": 0.91, "f1_macro": 0.88 },
    "uncertainty": [
      { "kind": "confidence_interval", "level": 0.95, "value": { "low": 0.89, "high": 0.93 }, "units": "probability" }
    ]
  },
  "artifacts": {
    "asset_links": [
      { "rel": "preview", "href": "s3://.../preview.png", "type": "image/png" },
      { "rel": "data", "href": "s3://.../output.tif", "type": "image/tiff; application=geotiff; profile=cloud-optimized" }
    ]
  },
  "provenance": {
    "prov_activity_id": "prov_act_...",
    "prov_bundle_id": "prov_bundle_...",
    "dcat_dataset_id": "dcat_...",
    "stac_item_id": "stac_item_output_..."
  },
  "classification": "public",
  "redaction_notes": []
}
```

> [!TIP]
> Return **summaries** inline. Put heavy arrays/rasters/plots in storage and reference them via STAC assets and safe hrefs 📦🔗

---

## 🎛️ Parameters, hashes, and reproducibility

### Why this matters 🧬
Modeling results are only trustworthy if they can be reproduced or at least audited.

**Modeling mappers should shape and preserve:**
- `params_hash` — stable fingerprint of normalized parameters
- `data_hash` / `input_refs` — stable identifiers to inputs
- `run_id` — stable ID (not random unless supplied by domain)
- `seed` — when applicable
- `environment` / `software_versions` — pipeline version, dependencies (when available)
- `runtime_profile` — optional summary (elapsed time, hardware hints), but never secrets

### Normalization rules (recommended)
- sort keys deterministically
- normalize floats (avoid `repr()` drift)
- forbid NaN/inf
- strip/normalize strings
- allowlist enums (method names, metrics names)

> [!CAUTION]
> If a mapper changes floats differently on two machines, hashes will differ and provenance breaks. Keep float formatting stable.

---

## 📈 Uncertainty & diagnostics mapping

Modeling outputs without uncertainty are “pretty pictures” — not evidence.

### Uncertainty kinds to support 🎲
- 📊 `confidence_interval` (frequentist)
- 🎲 `credible_interval` (Bayesian)
- 🧮 `standard_error` / `std_dev`
- 🧊 `error_bound` (numerical)
- ✅ `confusion_matrix_summary` (classification; include labels + counts, not huge matrices by default)

### Rules (must be explicit)
- include `kind`, `level` (where relevant), and `units`
- never label something “confidence” without specifying *what* it means
- if a metric is computed on a subset/split, state the split (`train/val/test`)
- include diagnostic flags (e.g., `converged`, `diverged`, `ill_conditioned`, `non_identifiable`)

> [!TIP]
> For Bayesian outputs, clearly separate:
> - prior description (or `prior_ref`)
> - posterior summary
> - sampling diagnostics (effective sample size, R-hat) if available

---

## 🗺️ Spatial & temporal semantics

Modeling often depends on where and when:

### ROI (region of interest) 🗺️
- support bbox + polygon ROI (if the project supports it)
- carry CRS explicitly
- if ROI is generalized/redacted, mark it (and never “increase precision” later)

### Time semantics ⏳
- ISO-8601 on the wire
- normalize to UTC internally
- support “fuzzy” time when historically uncertain:
  - `start`, `end`, `certainty`, `source_ref`
- avoid inventing precision (no fake timestamps)

---

## 📤 Outputs, assets, and payload size

### The cardinal rule 🧱
**Do not inline huge outputs in API responses.**

Instead:
- emit a small summary DTO
- store heavy artifacts in storage
- reference them:
  - as `asset_links[]`
  - and via STAC assets/catalog refs

Common artifact types:
- 🧊 COG rasters (GeoTIFF)
- 🧱 MVT tileset references
- 📄 CSV/parquet tables (metrics, time series)
- 🖼️ PNG/JPEG previews
- 📄 PDF reports
- 🧪 JSON manifests (run config + hashes)
- 📈 plot images (residual plots, calibration curves, ROC/PR)

> [!TIP]
> Include a **thumbnail/preview** asset whenever possible. Humans trust what they can see 👀

---

## 🔐 Classification, redaction, and safety

Modeling outputs can leak sensitive info by inference:
- precise locations
- rare event patterns
- individual-level measurements (even if anonymized poorly)

Mapper-level safety rules:
- never downgrade classification
- propagate redaction notes
- enforce precision policies on geo fields
- do not log raw payloads (use sanitized views)
- do not embed signed URLs/tokens in hrefs (emit references instead)

---

## 🧯 Error codes

Keep mapper errors stable and boring:

- `INVALID_MODEL_ID`
- `INVALID_RUN_ID`
- `INVALID_PARAMS`
- `INVALID_UNITS`
- `INVALID_TIME_RANGE`
- `INVALID_ROI`
- `INVALID_METRIC`
- `INVALID_UNCERTAINTY`
- `PAYLOAD_TOO_LARGE`
- `UNSAFE_HREF`
- `CLASSIFICATION_DOWNGRADE_ATTEMPT`

> [!IMPORTANT]
> Treat error codes like API surface. Changing them is a breaking change 📜💥

---

## 🧪 Testing strategy

### ✅ Unit tests
- deterministic hashing (same params → same hash)
- uncertainty mapping correctness (kind/level/units)
- metric naming allowlists
- ROI/time validation edge cases
- “classification never downgrades”

### ✅ Golden fixtures
```text
🧪 tests/
  📁 fixtures/
    📁 modeling/
      📄 model_run_summary_regression_v1.json
      📄 model_run_summary_bayes_v1.json
      📄 model_run_summary_classification_v1.json
      📄 simulation_run_summary_v1.json
      📄 optimization_run_summary_v1.json
      📄 problem_invalid_params.json
      📄 problem_invalid_uncertainty.json
```

### ✅ Property tests (optional, high value)
- parameter normalization is stable across ordering changes
- float normalization is stable across platforms
- “refs-first”: asset links never include secret-like query params

---

## 🧑‍💻 Templates

### 1) Evidence summary DTO (illustrative) 🧾
```python
# 📄 api/src/adapters/mappers/modeling/results.py

from dataclasses import dataclass
from typing import Any, Optional

@dataclass(frozen=True)
class EvidenceSummaryDTO:
    kind: str
    run_id: str
    model_id: str
    model_version: Optional[str]
    params_hash: str
    data_refs: list[dict[str, Any]]
    metrics: dict[str, Any]
    uncertainty: list[dict[str, Any]]
    asset_links: list[dict[str, str]]
    provenance: dict[str, str]
    classification: Optional[str] = None
    redaction_notes: list[str] = None
```

### 2) Mapping a domain “run” to an evidence summary 📤
```python
# 📄 api/src/adapters/mappers/modeling/results.py

def to_evidence_summary(domain_run) -> EvidenceSummaryDTO:
    # domain_run is produced by services/use-cases (already validated at business level)
    return EvidenceSummaryDTO(
        kind=domain_run.kind,
        run_id=domain_run.run_id,
        model_id=domain_run.model.model_id,
        model_version=getattr(domain_run.model, "model_version", None),
        params_hash=domain_run.params_hash,
        data_refs=[r.to_ref_dict() for r in domain_run.input_refs],
        metrics=dict(domain_run.metrics),
        uncertainty=[u.to_dict() for u in getattr(domain_run, "uncertainty", [])],
        asset_links=[a.to_link_dict() for a in getattr(domain_run, "asset_links", [])],
        provenance={
            "stac_item_id": getattr(domain_run.provenance, "stac_item_id", ""),
            "dcat_dataset_id": getattr(domain_run.provenance, "dcat_dataset_id", ""),
            "prov_activity_id": getattr(domain_run.provenance, "prov_activity_id", ""),
            "prov_bundle_id": getattr(domain_run.provenance, "prov_bundle_id", ""),
        },
        classification=getattr(domain_run, "classification", None),
        redaction_notes=list(getattr(domain_run, "redaction_notes", [])),
    )
```

### 3) Stable parameter hashing helper (delegates to common) #️⃣
```python
# 📄 api/src/adapters/mappers/modeling/manifests.py

from typing import Any, Dict
# from api.src.adapters.mappers.common.hashing import stable_hash_dict  # recommended

def normalize_params(params: Dict[str, Any]) -> Dict[str, Any]:
    # Minimal normalization: sort keys; coerce simple scalar types.
    # Real implementation should:
    # - normalize floats deterministically
    # - enforce allowlists for enums/units
    # - reject NaN/inf
    return dict(sorted(params.items(), key=lambda kv: kv[0]))

def params_fingerprint(params: Dict[str, Any]) -> str:
    normalized = normalize_params(params)
    # return stable_hash_dict(normalized)
    # placeholder:
    import hashlib, json
    payload = json.dumps(normalized, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()
```

> [!NOTE]
> Keep hashing deterministic and consistent with `mappers/common/` so all mappers agree on fingerprints.

---

## ✅ Definition of done

For any new/changed modeling mapper:

- [ ] Pure mapping (no I/O, no driver objects)
- [ ] Repro metadata included (run_id, model_id/version, params_hash, input refs)
- [ ] Uncertainty semantics explicit (kind, level, units)
- [ ] Diagnostics included when available (convergence, split info)
- [ ] Outputs are refs-first (large artifacts are links, not inline blobs)
- [ ] Catalog/provenance refs included (STAC/DCAT/PROV)
- [ ] Classification/redaction propagation enforced (no downgrade)
- [ ] Stable error codes and safe messages
- [ ] Unit tests + golden fixtures added
- [ ] Docs/examples updated with contract changes

---

## 📚 Project bookshelf

<details>
<summary>📚 Click to expand — how the full project library informs modeling mapper rules</summary>

### 🧪 Modeling, simulation, statistics, and uncertainty (core)
- 📄 **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf** → reproducibility norms, verification/validation mindset, run documentation
- 📄 **Understanding Statistics & Experimental Design.pdf** → experimental discipline, assumptions, reporting standards
- 📄 **regression-analysis-with-python.pdf** → regression outputs, diagnostics shaping, metrics vocabulary
- 📄 **Regression analysis using Python - slides-linear-regression.pdf** → compact summaries and reporting conventions
- 📄 **think-bayes-bayesian-statistics-in-python.pdf** → credible intervals, priors/posteriors, uncertainty semantics
- 📄 **graphical-data-analysis-with-r.pdf** → exploratory outputs as evidence artifacts (summaries + plots as assets)
- 📄 **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf** → ML run/version metadata, metrics and evaluation artifacts *(library item)*

### 🛰️ Remote sensing (model outputs must carry accuracy/uncertainty)
- 📄 **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf** → classification products, accuracy assessment expectations, long-running workflows

### 🕸️ Graph & optimization (derived results are evidence too)
- 📄 **Spectral Geometry of Graphs.pdf** → graph-derived measures; encourages careful definitions and reproducible summaries
- 📄 **Generalized Topology Optimization for Structural Design.pdf** → optimization runs: objectives/constraints/convergence + parameter tracking

### 🗺️ Geospatial representation (ROIs, precision, map-facing outputs)
- 📄 **python-geospatial-analysis-cookbook.pdf** → CRS hygiene, geometry conventions, practical GIS output shaping
- 📄 **making-maps-a-visual-guide-to-map-design-for-gis.pdf** → representation matters; avoid misleading precision; include previews/thumbnails
- 📄 **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf** → scale/context and privacy implications; mobile delivery constraints
- 📄 **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf** → correct preview asset typing and compression tradeoffs
- 📄 **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf** → interactive client needs; avoid bloated payloads
- 📄 **responsive-web-design-with-html5-and-css3.pdf** → predictable web contracts; stable DTO shapes

### 🗄️ Data systems & scaling (why refs-first + deterministic outputs)
- 📄 **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf** → typing discipline; careful numeric/time handling
- 📄 **Scalable Data Management for Future Hardware.pdf** → performance constraints; stable caching keys; avoid repeated serialization
- 📄 **Data Spaces.pdf** → interoperability/federation framing; metadata as glue across systems

### 🧠 Humanism, accountability, and governance (why provenance is required)
- 📄 **Introduction to Digital Humanism.pdf** → transparency and human-facing accountability
- 📄 **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf** → accountability expectations for ML-derived claims
- 📄 **Principles of Biological Autonomy - book_9780262381833.pdf** → systems thinking; track “why/how” metadata for adaptive behavior

### 🛡️ Security mindset (why safe hrefs and sanitized logs exist)
- 📄 **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf** → threat modeling for input validation, exfiltration risks
- 📄 **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf** → adversarial thinking; don’t trust inputs; don’t leak secrets

### 🧵 Concurrency/distributed runs (why explicit time/IDs matter)
- 📄 **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf** → distributed execution: retries, idempotency, determinism

### 🧩 Project direction docs (how modeling fits KFM)
- 📄 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx** → system boundaries, API pipeline placement
- 📄 **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx** → future-facing modeling/analysis integration direction

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

