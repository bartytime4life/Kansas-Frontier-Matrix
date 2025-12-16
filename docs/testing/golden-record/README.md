---
title: "✅ KFM — Golden‑Record Data Tests (Deterministic · Schema & Value Invariants · OpenLineage+PROV)"
path: "docs/testing/golden-record/README.md"

version: "v11.2.6"
last_updated: "2025-12-16"
release_stage: "Stable / Governed"
lifecycle: "Long‑Term Support (LTS)"
review_cycle: "Quarterly · Reliability Council · FAIR+CARE Oversight"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Testing Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-golden-record-tests"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

semantic_document_id: "kfm-tests-golden-record"
doc_uuid: "urn:kfm:doc:tests-golden-record-v11.2.6"
---

<div align="center">

# ✅ **KFM — Golden‑Record Data Tests**
**Deterministic · Schema & Value Invariants · OpenLineage+PROV**

<code>docs/testing/golden-record/README.md</code>

**Purpose**  
Define a governed, deterministic test pattern for validating a tiny, stable “golden record” slice of canonical datasets in CI, with machine‑readable results and minimal lineage emission (OpenLineage + PROV).

<img alt="Status" src="https://img.shields.io/badge/status-Active%20%2F%20Canonical-2ea44f" />
<img alt="Release Stage" src="https://img.shields.io/badge/release-Stable%20%2F%20Governed-blue" />
<img alt="KFM-MDP" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-informational" />
<img alt="License" src="https://img.shields.io/badge/license-MIT-black" />

</div>

---

## 📘 Overview

A **golden‑record** test validates a tiny, stable sample of canonical rows against:

- **Schema invariants**: types, required fields, enums, geometry/CRS constraints (when applicable).
- **Value invariants**: stable keys, checksum / fingerprints, row‑count bounds, uniqueness constraints.
- **Distribution deltas**: tight tolerances on numeric columns (and/or quantiles) to catch subtle drift.

The suite is designed to be:

- **Deterministic by construction** (seeded + stable ordering + hash‑based selection).
- **Fast enough for CI** (golden slices are small; full datasets are never required in PR checks).
- **Lineage‑aware** (emits minimal OpenLineage + PROV artifacts so CI runs are auditable).
- **Governable** (baseline updates are explicit, reviewable, and reversible).

### What a golden‑record test is not

Golden‑record tests are **not** a replacement for:

- full schema validation across the entire dataset,
- full‑fidelity QA/QC pipelines,
- statistical validation on full distributions,
- human review for interpretive or culturally sensitive materials.

They are a **tripwire**: a small, high‑signal gate that fails fast when something important drifts.

---

## 🗂️ Directory Layout

~~~text
📂 docs/testing/golden-record/                     🧭 Documentation for the golden-record testing pattern
├─ 📄 README.md                                     (this file)

📂 tests/                                           🧪 Cross-cutting test suites (integration + reproducibility)
├─ 📂 golden-record/                                ✅ Golden-record suite (specs + baselines + fixtures)
│  ├─ 📂 specs/                                     🧾 Active suite: one spec per dataset describing invariants + sampling
│  ├─ 📂 examples/                                  🧾 Copy-paste starters for new datasets (not required for CI)
│  ├─ 📂 baselines/                                 🧷 Expected fingerprints / tolerances (versioned, reviewable)
│  ├─ 📂 fixtures/                                  🧫 Tiny sanitized samples (only if allowed by governance)
│  ├─ 📂 reports/                                   🧾 Local-only reports (recommended: gitignored)
│  └─ 📄 README.md                                  🧭 Suite-level notes (optional)

📂 schemas/                                         📐 JSON/JSON-LD/SHACL schemas (machine-validated contracts)
├─ 📂 json/                                         📜 JSON schemas for docs/pipelines/testing specs
│  └─ 📂 testing/
│     └─ 📄 golden-record.spec.schema.json          🧾 Schema for golden-record spec files (YAML validated as JSON)

📂 tools/                                           🧰 Tooling and utilities (validation, governance, CI helpers)
└─ 📂 validation/
   └─ 📄 kfm-grecord.py                              🧪 One-file CLI runner (validate, report, emit lineage)

📂 data/                                            📦 Data artifacts (raw/processed/stac/reports)
└─ 📂 reports/
   └─ 📂 golden-record/                              ✅ CI and local report bundles (optional to retain)

📂 .github/workflows/                               🤖 CI workflows (linting, tests, audits)
├─ 📄 kfm-ci.yml                                     🔒 Primary CI workflow (calls golden-record job)
└─ 📄 golden-record.yml                              ✅ Optional dedicated workflow for golden-record suite
~~~

Notes:

- KFM uses top-level <code>tests/</code>, <code>schemas/</code>, and <code>tools/</code> directories. Align golden-record assets to these conventions.
- If your repository consolidates validation CLIs elsewhere (for example, <code>tools/cli/</code>), keep the interfaces the same and update this layout.

---

## 🧭 Context

### Where this fits in the KFM pipeline

Golden‑record tests sit at the **promotion boundary**:

1. ETL emits canonical outputs (data + STAC/DCAT + PROV).
2. Golden‑record tests validate small but representative slices.
3. CI gates promotion; only then do artifacts move toward release packaging and publication.

This complements (not replaces) larger checks such as:

- STAC/DCAT schema validation,
- provenance graph diffing,
- domain QA suites (spatial validity, temporal sanity, deduplication),
- release-level SBOM/manifest/signing workflows.

### When to add a golden-record test

Add a golden‑record test when:

- a dataset is **business‑critical** (feeds Story Nodes, Focus Mode, or public-facing layers),
- schema stability matters (a downstream consumer depends on exact fields),
- “silent drift” is likely (upstream vendor updates, changed joins, new normalization logic),
- a dataset has governance risk (license/attribution fields must remain correct).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A[Canonical dataset output<br/>data/processed + data/stac] --> B[Golden Spec<br/>tests/golden-record/specs/*.yml]
  B --> C[Deterministic Sampler<br/>hash-stable selection]
  C --> D[Invariant Checks<br/>schema + keys + bounds]
  C --> E[Distribution Checks<br/>quantiles + tolerances]
  D --> F[Test Report Bundle<br/>JSON + JUnit + Markdown]
  E --> F
  F --> G[Lineage Emitters<br/>OpenLineage + PROV]
  G --> H[CI Gate<br/>GitHub Checks]
~~~

---

## 🧪 Validation & CI/CD

### Quickstart (local)

Run a single spec:

~~~bash
python tools/validation/kfm-grecord.py run \
  --spec tests/golden-record/examples/soils.yml \
  --baseline tests/golden-record/baselines/soils.baseline.json \
  --report-dir data/reports/golden-record/soils
~~~

Run all golden-record specs:

~~~bash
python tools/validation/kfm-grecord.py run-all \
  --spec-dir tests/golden-record/specs \
  --baseline-dir tests/golden-record/baselines \
  --report-dir data/reports/golden-record/_all
~~~

Recommended (if your Makefile supports it):

~~~bash
make test-golden
~~~

### CI integration (GitHub Actions)

Golden‑record tests SHOULD run on:

- pull requests targeting <code>main</code> or <code>develop</code>,
- merges to protected branches,
- release candidate builds.

A minimal CI job looks like:

~~~yaml
# .github/workflows/kfm-ci.yml (excerpt)
jobs:
  golden_record:
    name: golden-record
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install
        run: |
          python -m pip install -U pip
          pip install -r requirements.txt
      - name: Run golden-record suite
        run: |
          python tools/validation/kfm-grecord.py run-all \
            --spec-dir tests/golden-record/specs \
            --baseline-dir tests/golden-record/baselines \
            --report-dir data/reports/golden-record/_ci
      - name: Upload reports
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: golden-record-reports
          path: data/reports/golden-record/_ci
~~~

### Determinism requirements (non-negotiable)

A golden‑record runner MUST:

1. **Sort deterministically** before any sampling or aggregation.
2. Use a **stable selection algorithm** (hash‑based, not order‑dependent random sampling).
3. Pin or record:
   - seed,
   - spec hash,
   - code version (commit SHA),
   - dependency set (lockfile or <code>pip freeze</code> output),
   - environment identity (container digest, if used).

### Interpreting failures (make CI actionable)

A failure SHOULD be classified into one of these buckets:

- **Schema break**: missing/renamed columns, type drift, enum expansion.
- **Key break**: primary key nulls, duplicates, or key-format changes.
- **Row-count drift**: unexpected loss/gain beyond bounds.
- **Value drift**: per-row fingerprint mismatch for sampled keys.
- **Distribution drift**: numeric tolerance exceeded (mean/quantiles).

Recommended developer workflow:

1. Open <code>report.md</code> first (human summary).
2. Inspect <code>summary.json</code> for the exact failed check IDs.
3. If expected, regenerate baseline via governed update.
4. If unexpected, treat as a pipeline regression (block promotion).

### Failure behavior (fail fast, emit artifacts)

On failure, the runner MUST emit:

- a machine summary: <code>summary.json</code>
- a CI-friendly report: <code>junit.xml</code>
- a short human report: <code>report.md</code>
- lineage artifacts (when enabled): <code>openlineage.json</code>, <code>prov.jsonld</code>

And MUST exit non‑zero so CI blocks promotion.

---

## 📦 Data & Metadata

### Golden spec format

Each dataset under test has one YAML spec file, validated against a JSON Schema.

Recommended spec location:
- <code>tests/golden-record/specs/&lt;dataset_id&gt;.yml</code>

Optional starter examples:
- <code>tests/golden-record/examples/&lt;dataset_id&gt;.yml</code>

Minimum required fields (pattern-level contract):

- <code>id</code>: stable test identifier (used in reports and lineage)
- <code>dataset</code>: how to locate the dataset (file path or catalog reference)
- <code>primary_key</code>: one or more columns that uniquely identify records
- <code>sampling</code>: deterministic sample strategy (seed, size, method)
- <code>schema</code>: schema reference or inline invariants
- <code>invariants</code>: required constraints and tolerances
- <code>checksums</code>: baseline pointer and fingerprint policy
- <code>lineage</code>: enable/disable OpenLineage + PROV emission

### Minimal JSON Schema (illustrative)

This is the minimal shape the spec schema SHOULD enforce (extend as needed):

~~~json
{
  "type": "object",
  "required": ["id", "dataset", "primary_key", "sampling", "invariants"],
  "properties": {
    "id": { "type": "string" },
    "description": { "type": "string" },
    "dataset": {
      "type": "object",
      "required": ["kind", "uri"],
      "properties": {
        "kind": { "type": "string", "enum": ["file", "stac", "dcat"] },
        "uri": { "type": "string" },
        "format": { "type": "string" }
      }
    },
    "primary_key": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1
    },
    "sampling": {
      "type": "object",
      "required": ["method", "seed", "sample_size"],
      "properties": {
        "method": { "type": "string", "enum": ["hash"] },
        "seed": { "type": "integer" },
        "sample_size": { "type": "integer", "minimum": 1 },
        "sticky_keys": { "type": "boolean" }
      }
    },
    "invariants": { "type": "object" },
    "lineage": { "type": "object" }
  }
}
~~~

### Example spec (soils.yml)

~~~yaml
id: kfm-soils-golden
description: Golden-record invariants for the canonical soils layer (processed output).
dataset:
  kind: file
  uri: data/processed/soil/soils.parquet
  format: parquet

primary_key: [soil_id]

sampling:
  method: hash
  seed: 42
  sample_size: 200
  sticky_keys: true          # keep prior sampled keys if still present (reduces churn)

schema:
  mode: columns
  required:
    - soil_id
    - h3_r8
    - soil_ph               # example numeric field (replace with a real column)
  types:
    soil_id: string
    h3_r8: string
    soil_ph: number

invariants:
  row_count:
    min: 1000
  unique:
    - [soil_id]
  not_null:
    - soil_id
    - h3_r8
  ranges:
    soil_ph:
      min: 0
      max: 14
  distribution:
    soil_ph:
      mean_rel_tol: 0.05
      p50_abs_tol: 0.2
      p95_abs_tol: 0.5

checksums:
  baseline_ref: tests/golden-record/baselines/soils.baseline.json
  fingerprint:
    method: row-hash
    float_round: 3

lineage:
  emit_openlineage: true
  emit_prov_jsonld: true
  job_namespace: kfm
  job_name: golden-record/soils
~~~

Important:

- Prefer invariants that remain stable across time and environments.
- For sensitive datasets, do not persist raw values in baselines; persist hashes and aggregates only.

### Baseline format

A baseline file stores the expected fingerprint/tolerances derived from the spec at a known-good point.

Recommended baseline location:
- <code>tests/golden-record/baselines/&lt;dataset_id&gt;.baseline.json</code>

Minimum recommended baseline contents:

- <code>spec_sha256</code>: hash of the spec file (guards against hidden spec edits)
- <code>sampling</code>: resolved sampling parameters (seed, size, method)
- <code>expected</code>:
  - row_count bounds or exact count (if appropriate),
  - sampled primary keys (or hashed keys),
  - per-row fingerprints (optional but high-signal),
  - summary stats (min/max/mean/quantiles) for watched numeric columns.

Example (baseline skeleton):

~~~json
{
  "id": "kfm-soils-golden",
  "spec_sha256": "SHA256_OF_SPEC_CANONICAL_FORM",
  "created_at": "2025-12-16T00:00:00Z",
  "sampling": {
    "method": "hash",
    "seed": 42,
    "sample_size": 200,
    "sticky_keys": true
  },
  "expected": {
    "row_count": { "min": 1000 },
    "sample_keys_sha256": "SHA256_OF_CANONICAL_KEY_LIST",
    "row_fingerprints_sha256": "SHA256_OF_CANONICAL_ROW_HASH_MAP",
    "stats": {
      "soil_ph": {
        "mean": 6.7,
        "p50": 6.5,
        "p95": 7.8
      }
    }
  }
}
~~~

### Canonicalization and fingerprinting rules

To keep hashes stable, the runner SHOULD define a canonicalization policy:

- **Columns**: explicit include list, stable ordering.
- **Strings**: normalize Unicode; trim only if domain-approved.
- **Numbers**: round floats to a fixed precision (spec-controlled) before hashing.
- **Nulls**: represent consistently (for example, JSON null).
- **Timestamps**: normalize to UTC with explicit format if included at all.
- **Geometries**: avoid hashing raw coordinate arrays unless you define canonical WKT/WKB policy.

### Deterministic sampling algorithm

To be stable across runtimes, the sampler SHOULD use **hash ranking**:

1. Build a canonical primary key string for each row (join keys with a delimiter).
2. Compute <code>sha256(seed || ":" || key_string)</code>.
3. Sort by digest ascending.
4. Select the first <code>sample_size</code> keys.

If <code>sticky_keys</code> is enabled:

- carry forward prior sampled keys that still exist,
- fill any remaining slots using hash ranking.

This reduces noisy diffs while still catching true drift.

### Updating baselines (governed)

Baseline updates MUST be explicit and reviewable:

- Generated only via an update command (never as a side effect of <code>run</code>).
- Committed as a normal PR change with:
  - a short written rationale,
  - links to upstream change notes (if applicable),
  - before/after report artifacts attached to the PR.

Recommended command shape:

~~~bash
python tools/validation/kfm-grecord.py update-baseline \
  --spec tests/golden-record/examples/soils.yml \
  --baseline tests/golden-record/baselines/soils.baseline.json \
  --reason "Upstream reprocessing: fixed join keys for soil_id normalization" \
  --report-dir data/reports/golden-record/soils_update
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Golden‑record tests SHOULD integrate with KFM catalog and lineage norms.

### STAC

- Treat golden‑record reports as **QA assets** for the dataset under test.
- Store reports as sidecar artifacts (CI artifacts, or under <code>data/reports/</code> if retained).
- When publishing QA, attach assets to the appropriate STAC Item(s) or Collection metadata.

Example STAC asset attachment (illustrative):

~~~json
{
  "assets": {
    "qa_golden_record": {
      "href": "data/reports/golden-record/soils/summary.json",
      "type": "application/json",
      "roles": ["qa", "metadata"],
      "title": "Golden-record CI summary"
    }
  },
  "properties": {
    "kfm:qa_golden_record": {
      "status": "pass",
      "spec_id": "kfm-soils-golden",
      "baseline_sha256": "SHA256_OF_BASELINE"
    }
  }
}
~~~

### DCAT

If a dataset is exported to DCAT:

- represent golden-record reports as a related Distribution or documentation link,
- keep the distribution checksum and media type explicit.

### Minimal OpenLineage event (illustrative)

~~~json
{
  "eventType": "COMPLETE",
  "eventTime": "2025-12-16T00:00:00Z",
  "run": { "runId": "RUN_UUID" },
  "job": { "namespace": "kfm", "name": "golden-record/soils" },
  "inputs": [
    { "namespace": "kfm", "name": "data/processed/soil/soils.parquet" }
  ],
  "outputs": [
    { "namespace": "kfm", "name": "data/reports/golden-record/soils/summary.json" }
  ]
}
~~~

### PROV-O (minimal JSON-LD sketch)

~~~json
{
  "@context": { "prov": "http://www.w3.org/ns/prov#" },
  "@id": "urn:kfm:prov:golden-record:soils:RUN_UUID",
  "@type": "prov:Bundle",
  "prov:activity": {
    "@id": "urn:kfm:activity:golden-record:soils:RUN_UUID",
    "@type": "prov:Activity"
  }
}
~~~

Recommended output location (CI artifact or retained report bundle):

- <code>data/reports/golden-record/&lt;id&gt;/openlineage.json</code>
- <code>data/reports/golden-record/&lt;id&gt;/prov.jsonld</code>

---

## 🧱 Architecture

### Runner responsibilities

A compliant golden-record runner MUST implement:

1. **Spec parsing + schema validation**
   - Validate YAML spec against <code>schemas/json/testing/golden-record.spec.schema.json</code>.
2. **Dataset resolution**
   - Load dataset from the configured source (file path or catalog reference).
3. **Canonicalization**
   - Stable column ordering; stable primary-key string formation; stable float formatting.
4. **Sampling**
   - Deterministic selection (hash ranking); optional sticky keys.
5. **Checks**
   - Schema invariants
   - Value invariants
   - Distribution deltas
6. **Reporting**
   - Machine summary + CI JUnit + small human report
7. **Lineage**
   - Minimal OpenLineage + PROV emission (toggleable)

### Suggested check taxonomy (standardized names)

Use a stable naming convention so downstream tooling can aggregate across datasets:

- <code>schema.required_columns</code>
- <code>schema.type_check</code>
- <code>keys.uniqueness</code>
- <code>values.not_null</code>
- <code>values.range</code>
- <code>distribution.mean_rel</code>
- <code>distribution.quantile_abs</code>
- <code>fingerprint.sample_keys</code>
- <code>fingerprint.row_hashes</code>

### Output bundle contract (minimal)

The report directory SHOULD contain:

- <code>summary.json</code> (machine)
- <code>junit.xml</code> (CI)
- <code>report.md</code> (human)
- <code>openlineage.json</code> (optional)
- <code>prov.jsonld</code> (optional)
- <code>inputs.json</code> (resolved dataset URI, spec hash, baseline hash, runner version)

---

## ⚖ FAIR+CARE & Governance

Golden‑record tests are governance‑sensitive because they can unintentionally persist data samples.

### Privacy and sovereignty safeguards

- If the dataset contains **restricted, sensitive, or sovereignty‑protected** information:
  - DO NOT store raw row samples in <code>tests/fixtures/</code>.
  - Prefer hashed fingerprints, counts, and aggregated statistics only.
  - Keep baselines free of names, addresses, or precise locations unless explicitly permitted.

### Review expectations

- Baseline updates are treated as **data changes** and require the same review rigor as ETL changes.
- Tests that govern public‑facing layers SHOULD be reviewed on the stated quarterly cycle and after major upstream data revisions.

### “Pass” does not mean “safe to publish”

A passing golden‑record suite indicates:

- key invariants held within tolerances for a stable sample.

It does not guarantee:

- correctness across the full dataset,
- absence of bias,
- suitability for interpretive Story Nodes without domain review.

---

## 🕰️ Version History

| Version | Date | Change | Author |
|---|---:|---|---|
| v11.2.6 | 2025-12-16 | Initial canonical pattern for deterministic golden‑record tests; defines baseline update governance guidance; documents minimal OpenLineage + PROV emission. | KFM Maintainers |

---

<div align="center">

📌 **Docs Root** · <a href="../../README.md">docs/README.md</a>  
📐 **Standards Index** · <a href="../../standards/README.md">docs/standards/README.md</a> · 🧩 <a href="../../templates/README.md">Templates Index</a>  
🤖 <a href="../../workflows/README.md">CI/CD Workflows</a> · 📈 <a href="../../standards/telemetry_standards.md">Telemetry Standard</a> · 📊 <a href="../../standards/telemetry/README.md">Telemetry Docs</a>  
🛡️ <a href="../../standards/ui_accessibility.md">UI Accessibility Standard</a> · 🔐 <a href="../../security/SECURITY.md">Security Policy</a>  
⚖ <a href="../../standards/governance/ROOT-GOVERNANCE.md">Governance Charter</a> · 🌱 <a href="../../standards/governance/FAIRCARE-GUIDE.md">FAIR+CARE Guide</a> · 🪶 <a href="../../standards/governance/INDIGENOUS-DATA-PROTECTION.md">Indigenous Data Protection</a>

© 2025 Kansas Frontier Matrix — MIT  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · KFM‑OP v11 · KFM‑PDC v11

</div>