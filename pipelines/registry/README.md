<!--
File: pipelines/registry/README.md
KFM: Kansas Frontier Matrix
Last updated: 2026-02-16
Status: Governed artifact (changes impact system behavior)
-->

# 🧭 KFM Pipeline Registry

![Governed](https://img.shields.io/badge/governed-yes-2ea44f)
![Evidence-first](https://img.shields.io/badge/evidence--first-required-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-6f42c1)
![Fail closed](https://img.shields.io/badge/policy-fail--closed-critical)
![Deterministic](https://img.shields.io/badge/runs-deterministic-informational)

> [!IMPORTANT]
> **This registry is part of KFM’s control plane.**  
> It defines *what pipelines exist* and *what they are allowed to produce/promote*.  
> Changes here should be treated like production changes.

---

## Why this exists

KFM uses a **plugin-style pipeline architecture**: new pipelines should be “drop-in” (add code + add a registry entry) without changing a central engine. The registry is the discoverable, reviewable index that makes this possible.

This registry also supports KFM’s governed promise: pipelines aren’t “just ETL”—they must produce **versioned artifacts** plus **catalog + provenance records** so outputs stay auditable and safe to share.

---

## What the registry is (and is not)

### ✅ It *is*
- A **machine-readable index** of pipelines (schedule/trigger, owners, inputs/outputs, policy label, required catalogs).
- A **governance contract** for promotion (what must exist before processed/public release).
- A **review surface** for risk: licensing, sensitivity, access constraints, and “default-deny” expectations.
- A **bridge** between:
  - pipeline implementations (`src/pipelines/...`)
  - pipeline specs/docs (`docs/pipelines/...`)
  - catalogs (`data/**/catalog/{dcat,stac,prov}/...` or equivalent)
  - promotion/audit workflows (PR-based)

### ❌ It is *not*
- A secrets store (no API keys, tokens, passwords—ever).
- An orchestrator implementation (Airflow/K8s runners live elsewhere).
- A replacement for dataset catalogs (DCAT/STAC/PROV are still authoritative for published assets).

---

## Repository layout

> [!NOTE]
> This tree shows the **intended** control-plane layout for registry-driven pipelines.
> Some adjacent paths may live elsewhere depending on repo conventions.

```text
pipelines/
  registry/
    README.md                         # <-- you are here
    manifest.yaml                     # Top-level pipeline index (human + machine readable)
    pipelines/                        # One YAML per pipeline (stable IDs)
      hydrology.nwis_watcher.yaml
      air_quality.fusion.yaml
      ...
    schemas/
      pipeline-entry.schema.json      # JSON Schema for pipeline entries
      manifest.schema.json            # JSON Schema for manifest.yaml
    teams/
      owners.yaml                     # Optional: team ownership + escalation map
```

Related (typical KFM layout):

```text
src/pipelines/                        # Implementations (watchers, batch ETL, simulations)
docs/pipelines/                       # Specs / runbooks (CI-ready)
data/<domain>/{raw,work,processed}/   # Immutable zones (raw read-only; processed versioned)
data/<domain>/catalog/{dcat,stac,prov}/
tools/validation/catalog_qa/          # Catalog QA “quick gate” (STAC/DCAT/PROV)
```

---

## Registry “contract” (core invariants)

> [!IMPORTANT]
> If a pipeline cannot satisfy these, it should **not** be registered as promotable.

### 1) Deterministic + replay-safe
- Same inputs + same config ⇒ same outputs (byte-identical where feasible).
- Pipelines must be idempotent: reruns should detect “no changes” and avoid duplicating output.

### 2) No ad-hoc edits
- Processed outputs must **never** be manually edited in-place.
- Fix the pipeline or raw inputs and re-run.

### 3) Catalog-first, stores derived from catalogs
- Promotion updates catalogs (**DCAT always; STAC/PROV as applicable**).
- Downstream indexes/stores are built *from catalogs*, not handwritten transformations.

### 4) Policy is enforced at promotion time
- Promotion requires explicit license + attribution + policy labeling.
- Sensitive triggers force review / redaction / generalization (default deny if uncertain).

### 5) Trust membrane preserved
- Frontends and external clients never access databases directly.
- All access flows through governed APIs + policy boundary.

---

## Registry data model

Each pipeline has a **stable pipeline_id** and a **pipeline spec** (YAML). A `manifest.yaml` collects discoverable pipeline entries for runners and CI.

### Pipeline entry schema (minimum)

| Field | Type | Required | Description |
|---|---:|:---:|---|
| `schema_version` | int | ✅ | Registry schema version for forward compatibility |
| `pipeline_id` | string | ✅ | Stable ID: `{domain}.{name}` (e.g., `hydrology.nwis_watcher`) |
| `title` | string | ✅ | Human-readable title |
| `kind` | enum | ✅ | `watcher` \| `batch` \| `simulation` \| `oneoff` |
| `status` | enum | ✅ | `draft` \| `active` \| `deprecated` |
| `owners` | object | ✅ | Team + maintainer contact (no secrets) |
| `schedule` | object | ✅* | Cron/interval OR event trigger (*required unless `oneoff`) |
| `inputs` | object | ✅ | Dataset IDs + raw zone paths (read-only) |
| `outputs` | object | ✅ | Processed artifacts + catalog outputs |
| `catalogs` | object | ✅ | DCAT/STAC/PROV emission expectations |
| `policy` | object | ✅ | Policy label + sensitivity triggers + redaction strategy |
| `validation_gates` | array | ✅ | Gates required to pass before promotion |
| `tests` | object | ✅ | Unit/integration/contract expectations |
| `links` | object | ✅ | Pointers to code + docs paths |

---

## Example pipeline entry

Create a file: `pipelines/registry/pipelines/hydrology.nwis_watcher.yaml`

```yaml
schema_version: 1

pipeline_id: hydrology.nwis_watcher
title: "NWIS Watcher — USGS Real-Time & Daily Hydrology for Kansas"
kind: watcher
status: draft

owners:
  team: hydrology
  maintainer: "TBD (not confirmed in repo)"
  escalation: "TBD (not confirmed in repo)"

schedule:
  mode: cron
  cron: "0 * * * *"   # hourly
  timezone: "America/Chicago"

inputs:
  dataset_ids:
    - usgs.nwis.iv
    - usgs.nwis.dv
  raw_paths:
    - "data/hydrology/raw/nwis/**"

outputs:
  processed_paths:
    - "data/hydrology/processed/nwis/**"
  work_paths:
    - "data/hydrology/work/nwis/**"

catalogs:
  dcat:
    required: true
    out_paths:
      - "data/hydrology/catalog/dcat/**"
  stac:
    required: true
    out_paths:
      - "data/hydrology/catalog/stac/**"
  prov:
    required: true
    out_paths:
      - "data/hydrology/catalog/prov/**"

policy:
  label: public              # public | restricted | sensitive-location
  sensitive_triggers:
    - type: none
  redaction:
    strategy: none           # none | aggregate | mask | jitter | omit_fields
  license:
    spdx: "CC0-1.0 (example)"
    attribution: "USGS (example)"

validation_gates:
  - schema_required_fields
  - temporal_sanity
  - license_attribution_present
  - provenance_complete
  - catalog_linkcheck

tests:
  unit: ["src/pipelines/hydrology/nwis_watcher/tests/unit/**"]
  integration: ["src/pipelines/hydrology/nwis_watcher/tests/integration/**"]
  contract: ["docs/pipelines/hydrology/nwis_watcher/contract-tests.md"]

links:
  code: "src/pipelines/hydrology/nwis_watcher/"
  docs: "docs/pipelines/hydrology/nwis_watcher/README.md"
```

> [!TIP]
> Keep entries boring and auditable. If a reviewer can’t tell *what comes in*, *what goes out*, and *what rules apply*, the pipeline isn’t ready for registration.

---

## `manifest.yaml` (pipeline discovery index)

`manifest.yaml` is the **runner-facing** list of pipelines. It should be:
- easy to diff in PRs
- stable in ordering
- validated in CI

Example:

```yaml
schema_version: 1
generated_by: "manual"
pipelines:
  - pipeline_id: hydrology.nwis_watcher
    status: draft
    entry_path: "pipelines/registry/pipelines/hydrology.nwis_watcher.yaml"
  - pipeline_id: air_quality.fusion
    status: active
    entry_path: "pipelines/registry/pipelines/air_quality.fusion.yaml"
```

---

## Promotion requirements (fail-closed)

A pipeline may run in `draft` mode without full promotion, but **promotion to processed/public** must be gated.

### Required validation gates (minimum)

- [ ] Row-level schema validation (required fields, types, coercions documented)
- [ ] Spatial/geometric validity (where applicable) and bounds checks
- [ ] Temporal consistency (no impossible dates; no negative durations)
- [ ] License + attribution captured (and policy labels defined)
- [ ] Provenance completeness for promoted artifacts (PROV chain + deterministic checksums)
- [ ] Catalog outputs emitted and cross-linked (DCAT always; STAC/PROV as applicable)

> [!WARNING]
> If any gate is “unknown”, treat it as **fail**. “Unknown” must never become “allowed.”

---

## CI wiring expectations

Typical CI stages for a pipeline PR:

1. **Registry validation**
   - Validate `manifest.yaml` + `pipelines/*.yaml` against JSON Schemas
   - Enforce stable ordering / formatting

2. **Catalog QA quick gate**
   - Fast checks for missing license/providers/extensions and dead links
   - Run before deeper schema validation

3. **Pipeline tests**
   - Unit tests (mapping/coercion logic; helpers)
   - Integration tests on a fixed small slice (stable checksums + counts)
   - Contract tests (API responses include provenance bundle + policy redaction behavior)

4. **Promotion PR (optional automation)**
   - Watcher runs → writes deterministic artifacts → emits catalogs → opens PR
   - Merge == promotion (with required checks)

---

## Adding a new pipeline (checklist)

### Step 0 — Decide the pipeline “kind”
- `watcher`: periodic pull/ingest from upstream
- `batch`: scheduled transformations/backfills
- `simulation`: scenario outputs (must still be versioned + prov)
- `oneoff`: special runs, typically not promotable by default

### Step 1 — Create implementation + docs
- [ ] Code under `src/pipelines/<domain>/<name>/`
- [ ] Spec/runbook under `docs/pipelines/<domain>/<name>/README.md`
- [ ] Tests included (unit + integration at minimum)

### Step 2 — Create registry entry
- [ ] Add `pipelines/registry/pipelines/<pipeline_id>.yaml`
- [ ] Add entry in `pipelines/registry/manifest.yaml`

### Step 3 — Ensure promotion gates are satisfied
- [ ] Deterministic raw manifest + checksums
- [ ] Canonical normalization outputs
- [ ] Validation gates enforced in CI
- [ ] Policy labels defined; restricted fields handled
- [ ] Catalogs emitted (DCAT always; STAC/PROV when applicable)
- [ ] API contract tests pass (at least one representative query)

### Step 4 — Governance review triggers
If any apply, require explicit review notes in the PR:
- [ ] culturally restricted knowledge
- [ ] archaeological/protected site risk
- [ ] private individual data
- [ ] precise locations that increase harm risk
- [ ] unclear upstream license

---

## Provenance expectations (PROV)

Pipelines should emit provenance such that a consumer can answer:

- What inputs produced this output?
- What code + config + version was used?
- When did the run occur, and who/what ran it?
- What validations passed/failed?

**Publishing pattern (recommended):**
- Store provenance as **sidecar JSON-LD** next to outputs and/or as a dedicated provenance graph.
- Ensure provenance can be retrieved by resource identity (e.g., `?prov` endpoint convention) in API layer.

---

## Interoperability notes (DCAT/STAC)

- **DCAT** is the baseline dataset catalog format for discoverability and licensing clarity.
- **STAC** supports spatial/temporal asset discovery for map/timeline UX.
- **PROV** links the transformation chain so “evidence-first” outputs stay auditable.

If bridging external catalogs:
- DCAT can interoperate with tools like CKAN/GeoNetwork ecosystems via DCAT feeds and harvesting.

---

## FAQ

<details>
<summary><strong>Where do secrets go?</strong></summary>

Not in this registry. Use your platform secret manager (vault/KMS) and reference secret *names* in runtime configs stored outside the repo (or in encrypted CI variables), never the values.

</details>

<details>
<summary><strong>Can a pipeline be registered as <code>active</code> without STAC?</strong></summary>

Yes, if the pipeline outputs are non-spatial. DCAT is still expected for promoted datasets; STAC is “as applicable.”

</details>

<details>
<summary><strong>Do we need Airflow?</strong></summary>

Not necessarily. A simple registry-driven runner (loop/Makefile/K8s CronJobs) is acceptable if determinism + gating remain intact.

</details>

---

## See also

- `docs/pipelines/` — pipeline specs and runbooks
- `tools/validation/` — validation gates and catalog QA
- `docs/standards/` — governed documentation protocol (Story Nodes, etc.)
- `docs/security/` — supply-chain + policy-as-code practices
