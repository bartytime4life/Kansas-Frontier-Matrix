# 🧪 KFM Pipeline Tests (`src/pipelines/tests/`)

![governance](https://img.shields.io/badge/governance-CI%20gated-blue)
![policy](https://img.shields.io/badge/policy-fail--closed-critical)
![evidence](https://img.shields.io/badge/evidence-STAC%2FDCAT%2FPROV-success)

This directory contains the automated test suite for **KFM data pipelines** under `src/pipelines/`.

In KFM, pipeline tests are not “nice to have” — they are **part of the governance mechanism** that prevents:
- promoting datasets without required catalog/provenance artifacts
- publishing/leaking sensitive fields or precise sensitive locations
- shipping non-deterministic outputs (hash drift, unstable IDs)
- “works on my machine” pipeline behavior that can’t be audited later

> [!IMPORTANT]
> Treat changes in **pipeline code** and **pipeline tests** as production changes.
> If a pipeline can’t be tested deterministically with auditable artifacts, it isn’t ready to merge.

---

## 📌 What these tests guarantee

These tests focus on the “truth path” for datasets and derived artifacts:

- **raw → work → processed** transformations
- required evidence artifacts: **run record**, **validation report**, **checksums**, **STAC/DCAT/PROV**
- **promotion gates** and **policy checks** (fail-closed)
- **sensitivity handling** (redaction/generalization as first-class transformations)
- **non-regression** for previously-fixed governance bugs (esp. leakage)

```mermaid
flowchart LR
  R[Raw zone\n(manifest + source slice)] -->|ingest| W[Work zone\n(intermediates)]
  W --> VR[validation_report.json]
  W --> RR[run_record.json]
  W -->|promote| P[Processed zone\n(published artifacts)]
  P --> CS[checksums.txt]
  P --> STAC[STAC]
  P --> DCAT[DCAT]
  P --> PROV[PROV]
  P --> AUDIT[Audit event]

  %% Test layers
  U[Unit tests] -.-> VR
  I[Integration tests] -.-> P
  C[Contract tests] -.-> STAC
  C -.-> DCAT
  C -.-> PROV
  POL[Policy tests] -.-> AUDIT
  REG[Regression tests] -.-> POL
```

> [!NOTE]
> This folder is intentionally **pipeline-centric**.
> - UI/E2E tests live elsewhere (e.g., `web/` test harness).
> - API contract tests live elsewhere (e.g., `src/server/` or top-level `tests/`), but pipeline tests may include **contract assertions on artifacts that the API serves**.

---

## 🗂️ Directory layout (recommended)

> Adapt to the repo’s current conventions — this is the “ideal shape” for coverage and clarity.

```text
src/pipelines/tests/
├── README.md
├── fixtures/                       # small, versioned test inputs (NO sensitive real data)
│   ├── <dataset_id>/
│   │   ├── raw/                    # raw-like fixture(s) + source manifest stub(s)
│   │   ├── work_expected/          # optional expected validation reports / intermediate outputs
│   │   └── processed_expected/     # optional golden outputs (or hashes only)
│   └── ...
├── golden/                         # canonical expected artifacts (stable hashes + catalogs)
│   ├── <dataset_id>/
│   │   ├── checksums.txt
│   │   ├── stac/                   # Collection + Items (or snapshots)
│   │   ├── dcat/
│   │   └── prov/
│   └── ...
├── unit/                           # fast, pure-function tests
├── integration/                    # pipeline runs end-to-end on a small fixture slice
├── contract/                       # schema + cross-link validation of emitted artifacts
├── policy/                         # OPA / Conftest tests for fail-closed + redaction rules
├── regression/                     # “never break again” suites (golden leak tests, drift tests)
└── helpers/                        # test helpers (temp dirs, runners, validators)
```

---

## ✅ Test taxonomy (what goes where)

| Test type | What it proves | Typical assertions | Runs in CI? |
|---|---|---|---|
| **Unit** | logic is correct in isolation | schema mapping, type coercion, geometry helpers, ID hashing | ✅ always |
| **Integration** | pipeline job runs end-to-end on a fixed slice | stable row counts, stable checksums, required artifacts created | ✅ always (may be split/parallel) |
| **Contract** | emitted artifacts match schemas + link correctly | STAC/DCAT/PROV validate; `run_record.json` is complete; links resolve | ✅ always |
| **Policy** | governance enforcement is fail-closed | default deny; redaction rules; sensitivity controls; “cite-or-abstain” gates (where applicable) | ✅ always |
| **Regression** | previously-fixed bugs never return | “golden leak queries must fail forever”; drift thresholds; negative tests | ✅ always |
| **Performance (optional)** | you won’t DOS CI/runtime | runtime budgets, memory ceilings, file sizes | ⚠️ nightly / pre-release |
| **Determinism (optional but recommended)** | outputs are byte-/hash-stable | two runs produce identical checksums + catalogs | ⚠️ nightly / pre-release |

---

## 🧾 Required artifacts (minimum contract)

A pipeline run is only considered valid when it produces (and tests validate) the evidence artifacts below.

| Artifact | Purpose | Minimum fields / checks |
|---|---|---|
| `run_record.json` | binds code + inputs + outputs | `run_id`, `dataset_id`, input/output URIs + sha256, code version/image, `validation_report` pointer, `prov_ref` |
| `validation_report.json` | deterministic validation output | per-check pass/fail + reason, includes license + sensitivity classification |
| `checksums.txt` (or equivalent) | content integrity | sha256 for each processed artifact; verified before serving |
| **STAC** | geospatial asset catalog | collection/items validate; assets include checksums; links include DCAT “via” where applicable |
| **DCAT** | dataset discovery/interoperability | dataset entry exists; distributions link to artifacts; license + rights |
| **PROV** | lineage & auditability | links raw→processed; run/activity ID; output entities include hashes |
| **Audit event** | tamper-evident trail | promotion/audit record references `run_id` and key artifacts |

> [!TIP]
> Pipeline tests should prefer verifying **hashes + schemas + cross-links** over “exact file byte equality” unless deterministic packaging is guaranteed for that file type.

---

## 🧪 Validator coverage checklist (minimum)

Pipelines must emit a **machine-readable validation report** and tests should cover (at least):

- **Schema validation**: required fields, types, null thresholds
- **Geospatial validation**: geometry validity, CRS declared, plausible bounds/topology
- **Temporal validation**: parseable timestamps, coherent `time_range`/intervals
- **License validation**: SPDX-like ID or explicit license string; attribution where required
- **Sensitivity validation**: classification present; restricted coordinates/fields flagged; governance approval triggers
- **Catalog validation**: STAC/DCAT/PROV JSON schema validation **plus** cross-link resolution
- **Hash validation**: sha256 for every processed artifact referenced by catalogs

### Example `validation_report.json` (illustrative)

```json
{
  "ok": true,
  "dataset_id": "example_dataset",
  "checks": [
    {"id": "license.present", "ok": true, "detail": "CC-BY-4.0"},
    {"id": "sensitivity.classified", "ok": true, "detail": "public"},
    {"id": "schema.required_fields", "ok": true},
    {"id": "geospatial.geometry_valid", "ok": true},
    {"id": "catalogs.stac_valid", "ok": true},
    {"id": "catalogs.dcat_valid", "ok": true},
    {"id": "catalogs.prov_valid", "ok": true},
    {"id": "hashes.complete", "ok": true}
  ]
}
```

### Example `run_record.json` (illustrative)

```json
{
  "run_id": "run_2026-02-14T12:34:56Z",
  "dataset_id": "example_dataset",
  "inputs": [{"uri": "data/raw/example.csv", "sha256": "…"}],
  "code": {"git_sha": "…", "image": "kfm/pipeline:…"},
  "outputs": [{"uri": "data/processed/example.parquet", "sha256": "…"}],
  "validation_report": "data/work/example/validation_report.json",
  "prov_ref": "data/catalog/prov/example/run_….json"
}
```

> [!NOTE]
> The exact JSON schema for these artifacts should be treated as a **contract**. If schemas exist under `schemas/`, make contract tests validate against them.

---

## 🚦 Promotion gate checklist (must be testable)

When promoting anything to `processed/` and/or making it publicly discoverable, tests must enforce:

- [ ] License present
- [ ] Sensitivity classification present
- [ ] Schema checks **and** geospatial checks pass
- [ ] Checksums computed
- [ ] STAC/DCAT/PROV artifacts exist **and validate**
- [ ] Audit event recorded
- [ ] Human approval required when sensitivity flags demand it

---

## ⚙️ Configuration

> These are **recommended** knobs for a predictable local/CI test harness. If the repo already defines different names, prefer the repo’s canonical names.

| Variable | Meaning | Suggested default |
|---|---|---|
| `KFM_TEST_SEED` | Seed for any RNG in tests/pipelines | `0` |
| `KFM_TEST_TMPDIR` | Root temp directory for pipeline runs | system temp |
| `KFM_TEST_KEEP_TMP` | Keep temp workdir on failure (0/1) | `0` |
| `KFM_TEST_ALLOW_NETWORK` | Allow external network egress (0/1) | `0` |
| `KFM_TEST_PARALLELISM` | Parallel workers for integration tests | CI default |

---

## ▶️ Running the tests

> [!NOTE]
> The exact commands depend on the repo’s test runner.
> The snippets below assume a common setup (Python + pytest + optional OPA tooling). If this repo uses a different runner, keep the *semantics* and update the commands.

### Local (fast loop)

```bash
# Run everything in this folder
python -m pytest -q src/pipelines/tests

# Unit tests only (fast)
python -m pytest -q src/pipelines/tests/unit

# Integration tests only (pipeline runs)
python -m pytest -q src/pipelines/tests/integration

# Contract tests only (schemas + catalogs)
python -m pytest -q src/pipelines/tests/contract
```

### Policy tests (OPA / Conftest)

```bash
# OPA unit tests (policy packs)
opa test -v src/policies

# Conftest wrapper (if used)
conftest test src/policies -p src/policies
```

### “No network” mode (recommended)

Pipeline tests should be runnable without reaching external services:

- use fixture inputs (or a local cached mirror)
- fail if the test tries to egress the network unless explicitly allowed

> [!IMPORTANT]
> Never make tests depend on live upstream endpoints. That is a reliability and governance failure.

---

## 🧩 Adding a new pipeline test (thin-slice workflow)

Use this when onboarding a new dataset or adding a new transformation step.

1) **Create or update a fixture** under `fixtures/<dataset_id>/`
   - include a minimal raw-like slice
   - include a manifest stub with license + sensitivity labels (even if “public”)

2) **Pick the right test layer**
   - unit: new helper logic
   - integration: run pipeline end-to-end on the fixture slice
   - contract: validate emitted artifacts
   - policy/regression: ensure no sensitive leak and no future regressions

3) **Write the integration test** to:
   - run the pipeline in a temp workspace (never write to real `data/` unless test harness is explicitly designed for it)
   - assert the pipeline produced `run_record.json` + `validation_report.json`
   - assert stable checksums + expected counts

4) **Write contract tests** to:
   - validate STAC/DCAT/PROV schemas
   - validate cross-links (e.g., STAC ↔ DCAT ↔ PROV pointers)
   - validate hash presence for each artifact referenced by catalogs

5) **Add policy + regression tests** (required when data can be sensitive)
   - add “golden leak” tests for any previously identified leak patterns
   - add negative tests for sensitive-location precision rules

6) **Update golden artifacts** (if used)
   - commit only what is safe to commit (often catalogs + checksums)
   - do **not** commit restricted/sensitive raw data

---

## 🧷 Updating / regenerating golden artifacts

> [!WARNING]
> Golden artifacts are only useful if they stay **small**, **reviewable**, and **safe to publish**.
> Prefer committing **catalogs + checksums** over committing large processed binaries.

Recommended pattern:

- Commit:
  - catalog JSON (STAC/DCAT/PROV) that is already intended to be public
  - checksums manifests
  - small synthetic processed artifacts (only when truly necessary)
- Do **not** commit:
  - real restricted/sensitive raw inputs
  - large processed datasets that belong in object storage
  - secrets, tokens, or endpoint URLs that should be vault-managed

<details>
<summary><strong>Example: regenerate golden catalogs + checksums (illustrative)</strong></summary>

```bash
# 1) Run the pipeline on the fixture
python -m kfm.pipelines.run --dataset <dataset_id> --input src/pipelines/tests/fixtures/<dataset_id>/raw --out /tmp/kfm-test-out

# 2) Copy the emitted catalogs + checksums into golden/
rsync -a /tmp/kfm-test-out/catalog/ src/pipelines/tests/golden/<dataset_id>/
cp /tmp/kfm-test-out/checksums.txt src/pipelines/tests/golden/<dataset_id>/checksums.txt

# 3) Re-run contract tests to confirm schemas + cross-links
python -m pytest -q src/pipelines/tests/contract -k <dataset_id>
```

</details>

---

## 🔒 Test data governance (sensitivity rules)

Test fixtures must follow the project’s sensitivity handling expectations:

- **No real restricted fields** (owner names, protected health small counts, etc.)
- **No precise sensitive locations** (archaeological sites, sensitive species) unless they are already public and explicitly permitted
- prefer **synthetic** or **anonymized** fixtures and validate redaction/generalization logic

Recommended sensitivity classes for fixtures:

| Class | Allowed in fixtures? | Notes |
|---|---|---|
| `Public` | ✅ yes | safe to publish without redaction |
| `Restricted` | ⚠️ synthetic only | do not store real owner/identity fields |
| `Sensitive-location` | ⚠️ synthetic + generalized | coordinates must be generalized/suppressed in outputs |
| `Aggregate-only` | ⚠️ synthetic | enforce small-count thresholds |

> [!IMPORTANT]
> Redaction is a **first-class transformation**: the raw dataset remains immutable; the redacted derivative is a separate dataset/version with its own PROV chain.

---

## 🧨 Policy regression suite (non-negotiable)

The policy regression suite exists to make leaks and governance failures **non-recurrent**.

Minimum expectations:

- **Golden queries that previously leaked restricted fields must fail forever**
- **Negative tests**: sensitive-location layers must not be returned at high precision to unauthorized roles
- **Field-level tests**: restricted fields must be redacted (owner names, exact coordinates, etc.)
- **Audit integrity tests**: responses and/or published outputs must include audit/evidence references (as required by the subsystem)

---

## ♻️ Determinism, checksums, and stable IDs

Non-determinism is a governance risk because it breaks auditability and reproducibility.

Recommended practices for pipelines and tests:

- compute sha256 for every processed artifact and store it in `checksums.txt` (or an equivalent manifest)
- ensure catalogs reference artifact hashes (directly or indirectly)
- use canonical JSON hashing (**JCS / RFC 8785**) to compute stable `spec_hash` values where IDs or policies depend on JSON payloads
- ensure repeated pipeline runs on the same inputs produce stable outputs (or document why they don’t and version appropriately)

---

## 🧱 CI integration (recommended)

> [!IMPORTANT]
> CI is expected to act as a **hard gate** for governed artifacts (pipelines, catalogs, policy).
> If you are modifying pipeline behavior, you should expect CI to require **unit + integration + contract + policy** coverage.

A recommended CI shape (conceptually):

1. **Lint + static checks** (formatting, imports, forbidden patterns)
2. **Unit tests** (fast, deterministic)
3. **Integration tests** (run pipeline on fixtures; capture outputs as build artifacts)
4. **Contract tests** (schemas + cross-links: STAC/DCAT/PROV + run_record/validation_report)
5. **Policy tests** (OPA/Conftest default deny + redaction rules)
6. **Regression suite** (golden leak tests, drift checks)
7. (Optional) **Determinism job** (rerun pipeline and compare checksums/catalogs)
8. Publish CI artifacts (logs, run_record, validation_report) for reviewer/auditor inspection

<details>
<summary><strong>Suggested CI artifacts to upload for every integration run</strong></summary>

- `run_record.json`
- `validation_report.json`
- `checksums.txt`
- emitted `stac/`, `dcat/`, `prov/` outputs
- pipeline logs (with a stable `run_id`)

</details>

---

## 🧯 Troubleshooting

### Common failures and what they mean

| Symptom | Likely cause | Fix |
|---|---|---|
| Promotion gate failure: missing license/sensitivity | fixture or mapping missing required metadata | add license + sensitivity to manifest and emitted catalogs |
| STAC/DCAT/PROV schema failures | catalog generator drift or invalid fields | fix generator; update schema; add regression test |
| Hash mismatch / drift | non-deterministic encoding, timestamp fields, unordered JSON | pin creation options; canonicalize JSON; sort keys; add determinism test |
| Policy test fails open | policy default allow or missing deny rule | enforce default deny; add explicit allow conditions |
| Integration test flaky | depends on clock/network/random order | freeze time; disable network; use seeded RNG; sort inputs |

### Where to look

- `validation_report.json` for the first failing validation check
- `run_record.json` to confirm which inputs/outputs were actually used
- diff the generated catalogs under `work/` against `golden/`

---

## 🧭 Definition of Done (pipeline PR)

A pipeline PR is **not** merge-ready until:

- [ ] Unit + integration + contract tests updated/added (as applicable)
- [ ] Promotion gate checklist is satisfied and test-covered
- [ ] No sensitive data is committed to the repo
- [ ] Policy tests updated (when sensitivity/publishing surface changed)
- [ ] Regression tests added for any bug fix involving leaks, schema drift, or determinism
- [ ] Artifacts are reproducible and auditable (hashes + run record + PROV)

---

## 📚 References (repo-local)

- `docs/architecture/` — system invariants, CI hardening, trust membrane (if present)
- `schemas/` — JSON Schemas for STAC/DCAT/PROV and governed artifacts
- `src/policies/` — OPA/Rego policy packs and tests (if present)
- `data/README.md` — data zones (`raw/`, `work/`, `processed/`) and catalog conventions (if present)

