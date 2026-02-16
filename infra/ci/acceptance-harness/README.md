<!--
File: infra/ci/acceptance-harness/README.md
Purpose: Merge-blocking acceptance harness (governance enforcement).
-->

# ✅ KFM Acceptance Harness (Merge‑Blocking)

![Governance Enforced](https://img.shields.io/badge/governance-enforced-critical)
![Fail Closed](https://img.shields.io/badge/posture-fail--closed-critical)
![Merge Blocking](https://img.shields.io/badge/CI-merge--blocking-important)
![Deterministic](https://img.shields.io/badge/artifacts-deterministic-blue)
![Trust Membrane](https://img.shields.io/badge/architecture-trust--membrane-blue)

This directory defines **KFM’s merge-blocking acceptance harness**: the minimal set of automated checks that make the repo’s governance claims *measurable* and *enforced*.

If these checks aren’t running (and required by branch protection), “governance” becomes **policy-by-document**.

---

## What this harness guarantees

> [!IMPORTANT]
> This harness is designed to be **fail-closed**: missing evidence, missing schemas, missing licenses, unknown policy inputs, or ambiguity must result in **failure**, not a warning.

### Non‑negotiable invariants enforced here

- **Contracts first**: receipts/manifests/catalogs must validate against their schemas.
- **Deterministic identity**: JSON contracts that are hashed must be canonicalized consistently (e.g., RFC 8785 JCS) and hashed deterministically.
- **Catalog integrity**: STAC/DCAT/PROV must validate and cross-link cleanly.
- **Geospatial validity**: GeoJSON/GeoParquet/COG outputs must pass format-level validation.
- **Policy-as-code**: OPA/Rego policies must be tested (golden fixtures) and must be versioned.
- **Trust membrane**: clients (UI/external) must not bypass the governed API boundary to touch DB/object stores directly.
- **Smoke “stack-first” proof**: at least one end-to-end smoke run that boots the stack (or stub) and performs an anchor “promotion” **dry run**.

---

## Directory layout

> [!NOTE]
> This is the *recommended* harness structure. If your repo differs, align paths over time (don’t silently drift).

```text
infra/ci/acceptance-harness/
├─ README.md                    # you are here
├─ Makefile                     # optional: local + CI entrypoints
├─ run.sh                       # optional: single “do the right thing” entrypoint
├─ tools/                       # pinned tool versions + wrappers
│  ├─ versions.lock             # pin conftest/cosign/stac-validator/etc
│  └─ bin/                      # small wrapper scripts (stable CLI)
├─ schemas/                     # contract schemas (JSON Schema, etc.)
│  ├─ run_receipt.schema.json
│  ├─ run_manifest.schema.json
│  ├─ validation_report.schema.json
│  └─ evidence_ref.schema.json
├─ policies/                    # OPA/Rego policy pack (versioned)
│  ├─ README.md                 # policy pack notes + versioning
│  ├─ receipt.rego
│  ├─ promotion.rego
│  └─ *_test.rego               # unit tests (golden pass/fail)
├─ validators/                  # format/catalog validators (wrappers)
│  ├─ geo/                      # GeoJSON / GeoParquet / COG
│  ├─ catalog/                  # STAC / DCAT / PROV + cross-link checks
│  └─ security/                 # optional: SBOM/license scanning gates
├─ fixtures/                    # regression fixtures for policies/validators
│  ├─ pass/
│  └─ fail/
├─ smoke/                       # end-to-end smoke checks
│  ├─ compose/                  # docker compose / podman-compose definitions
│  └─ tests/                    # API-level smoke tests (black-box)
└─ out/                         # generated reports (gitignored)
   ├─ junit/
   ├─ reports/
   └─ logs/
```

---

## What runs in the harness

| Stage | Purpose | Typical inputs | Output artifacts |
|---|---|---|---|
| **Lint / formatting** | Keep changes reviewable and consistent | repo code + docs | linter logs, SARIF (optional) |
| **Schema validation (P0)** | Ensure receipts/manifests/catalogs match contracts | `run_receipt.json`, `run_manifest.json`, STAC/DCAT/PROV docs | `validation_report.json`, JUnit |
| **Policy tests (P0)** | Prevent policy drift and enforce default-deny | Rego policies + fixtures | conftest output, JUnit |
| **Geo validators (P0)** | Ensure spatial outputs are valid per standard | GeoJSON / GeoParquet / COG | validator reports |
| **Catalog integrity (P0)** | Validate STAC/DCAT/PROV and cross-links | `data/catalog/**` | link-check report |
| **Smoke stack (P0)** | Prove “stack-first” + dry-run promotion path | docker compose + API | smoke logs + artifacts |
| **Supply-chain verify (P0+)** | Verify attestations/digests if enabled | OCI digests + cosign | verification logs |

> [!TIP]
> Keep the harness **fast by default**, with an explicit “full” mode for heavy checks:
> - `FAST=1` for PRs (default)
> - `FULL=1` for nightly or release lanes

---

## Entry points

### Preferred (top-level) entrypoint

In the repo root `Makefile` (recommended), provide:

- `make verify` → runs this acceptance harness (merge-blocking)
- `make verify-fast` → PR default
- `make verify-full` → nightly/release

### Local entrypoint (this directory)

If you add one command here, make it:

```bash
./infra/ci/acceptance-harness/run.sh
```

…and ensure it is stable and CI-friendly (exit codes, no prompts, deterministic output).

---

## Running locally

> [!IMPORTANT]
> Local runs must match CI behavior. Pin tool versions and run validators via wrappers in `tools/bin/` so your laptop and CI don’t disagree.

### Minimal (fast) run

```bash
# from repo root
make verify-fast
```

### Full run (includes smoke)

```bash
# from repo root
make verify-full
```

### Run a single stage

```bash
make verify-schema
make verify-policy
make verify-geo
make verify-catalog
make verify-smoke
```

---

## CI integration (example)

> [!NOTE]
> This is an example GitHub Actions snippet. Adapt to your CI system if different.

```yaml
name: acceptance

on:
  pull_request:
  push:
    branches: [ main ]

jobs:
  acceptance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Optional: fail-closed kill switch
      - name: Kill switch check
        run: |
          if [ -f .github/KILL_SWITCH ] || [ "${DEPLOY_KILL_SWITCH}" = "1" ]; then
            echo "KILL_SWITCH_ACTIVE"
            exit 1
          fi

      - name: Run acceptance harness (merge-blocking)
        run: make verify-fast

      - name: Upload harness artifacts
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: acceptance-artifacts
          path: infra/ci/acceptance-harness/out/
```

---

## Artifacts this harness should produce

> [!IMPORTANT]
> The harness should output **machine-readable artifacts** for audits and debugging.

Recommended stable artifact set (in `infra/ci/acceptance-harness/out/`):

- `reports/validation_report.json` (schema + validator results)
- `reports/policy_report.json` (conftest output summary)
- `junit/*.xml` (CI-friendly pass/fail reporting)
- `logs/*.log` (human debugging)
- `manifests/run_manifest.jcs.json` (canonicalized JSON when used for hashing)
- `digests/*.sha256` (stable digests for key artifacts)

---

## How to extend the harness safely

### Add a new schema (contract-first)

1. Add JSON Schema under `schemas/`.
2. Add a **minimal pass fixture** and at least **one fail fixture** under `fixtures/`.
3. Wire the schema into the schema-validation stage.
4. Ensure reports include:
   - schema name/version
   - file(s) validated
   - error list (path + message)

### Add a new policy

> [!IMPORTANT]
> Policies must remain **small and composable** (one file per concern), and must ship with `_test.rego` unit tests to prevent silent drift.

1. Add `policies/<name>.rego`
2. Add `policies/<name>_test.rego` with golden pass/fail cases.
3. Add fixtures that match the real production inputs (receipts/manifests/catalogs).
4. Version the policy pack and ensure receipts/manifests can reference the policy version used.

### Add a new validator (geo/catalog)

- Prefer wrapper scripts in `validators/**` that:
  - pin the underlying tool version (via `tools/`)
  - emit JSON reports in a stable format
  - return non-zero exit codes on failure

---

## Smoke test expectations

The smoke test is the “credibility proof” that the system is runnable end-to-end.

Minimum smoke requirements:

- Boots the stack (or stub stack) via compose
- Calls the system through the **governed API** (not direct DB access)
- Runs **one anchor dataset promotion** in **dry-run** mode
- Produces receipts/reports and exits cleanly

### Suggested smoke flow

```mermaid
flowchart LR
  PR[Pull Request] --> CI[CI Job]
  CI --> Harness[Acceptance Harness]
  Harness --> Compose[Bring up stack (compose)]
  Compose --> API[Call governed API]
  API --> DryRun[Anchor promotion (dry-run)]
  DryRun --> Reports[Emit reports + receipts]
  Reports --> Gate{All green?}
  Gate -->|yes| Merge[Merge allowed]
  Gate -->|no| Block[Merge blocked]
```

---

## Trust membrane checks

> [!WARNING]
> Any bypass that allows UI or external clients to reach databases/object stores directly is a governance failure.

Recommended checks:

- **Network isolation assertions** in compose (DB not published; private network)
- **Contract test**: UI cannot connect to DB host/port (negative test)
- **API-only rule**: smoke tests must only use public API endpoints

---

## Sensitivity and “known leak” regression fixtures

If the system has **sensitivity classes** or redaction/generalization logic, add:

- explicit **negative fixtures** (“known leak fixtures”) that must fail
- policy tests that deny on uncertainty
- smoke cases that confirm sensitive material is not returned

---

## Definition of Done (DoD)

- [ ] Harness can be run locally (`make verify-fast`)
- [ ] Harness is required by branch protection (merge-blocking)
- [ ] Deterministic outputs (stable ordering + pinned tool versions)
- [ ] Schemas + fixtures exist for each contract type validated
- [ ] Policy pack includes `_test.rego` tests and is versioned
- [ ] Smoke test exists and performs anchor promotion dry-run
- [ ] Reports are produced in `infra/ci/acceptance-harness/out/` and uploaded by CI
- [ ] README updated if contract surface changes

---

## References

External standards & specs (stable sources):

- RFC 7946 (GeoJSON) — https://www.rfc-editor.org/rfc/rfc7946
- RFC 8785 (JCS JSON Canonicalization) — https://www.rfc-editor.org/rfc/rfc8785
- DCAT v3 — https://www.w3.org/TR/vocab-dcat-3/
- W3C PROV overview — https://www.w3.org/TR/prov-overview/
- GeoParquet — https://geoparquet.org/releases/
- OGC Cloud Optimized GeoTIFF (COG) — https://www.ogc.org/standards/ogc-cloud-optimized-geotiff/
- STAC — https://stacspec.org/en/about/stac-spec/

Repo-local docs (adjust if paths change):

- DCAT profile — `docs/standards/KFM_DCAT_PROFILE.md`
- System overview — `docs/architecture/system_overview.md`
