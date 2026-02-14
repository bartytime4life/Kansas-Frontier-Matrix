# KFM Pipeline Validation ✅🧪 (CI Gates + Promotion Contract)

![Governance](https://img.shields.io/badge/governance-fail--closed-critical)
![Promotion](https://img.shields.io/badge/promotion-blocked_without_STAC%2FDCAT%2FPROV-blue)
![Provenance](https://img.shields.io/badge/provenance-PROV%20required-informational)
![Catalog](https://img.shields.io/badge/catalog-STAC%20%7C%20DCAT-informational)
![Policy](https://img.shields.io/badge/policy-OPA%2FRego-informational)

> [!IMPORTANT]
> **This folder defines and documents KFM’s validation gates.**  
> Validation is not “nice-to-have” — it is a **credibility boundary**. Anything that can be **served, cited, or narrated** must be verifiable via machine-checkable artifacts.

---

## What this directory is

`src/pipelines/validation/` is the **validation layer for pipeline outputs** and **governed artifacts**.

It exists to guarantee:

- **Data truth path** is followed (Raw → Work → Processed → Catalogs → API).
- **Promotion is blocked** unless required artifacts exist and validate.
- **Policy fails closed** (missing/invalid inputs mean deny).
- **Evidence-first** outputs remain auditable (datasets, story nodes, Focus Mode answers).

### Who should read this?

- Pipeline developers (ingest/normalize/transform/promote jobs)
- CI/CD maintainers (merge gates + release gates)
- Data stewards / governance reviewers (sensitivity + redaction + approvals)
- API/UX engineers who rely on catalogs/provenance being present and resolvable

---

## Contents

- [Truth path and data zones](#truth-path-and-data-zones)
- [Promotion gate CI checklist](#promotion-gate-ci-enforced)
- [Artifacts and contracts](#artifacts-and-contracts)
- [Validator taxonomy](#validator-taxonomy)
- [Policy-as-code integration](#policy-as-code-integration)
- [How to run validations](#how-to-run-validations)
- [How to add a validator](#how-to-add-a-validator)
- [Dataset integration Definition of Done](#dataset-integration-definition-of-done)
- [Sensitivity and redaction](#sensitivity-and-redaction)
- [CI hardening baseline](#ci-hardening-baseline)
- [Troubleshooting](#troubleshooting)
- [Governance and change control](#governance-and-change-control)

---

## Truth path and data zones

KFM’s publishable lineage is **not negotiable**:

```mermaid
flowchart LR
  Raw[Raw Zone\n(immutable capture)] --> Work[Work Zone\n(repeatable transforms + QA)]
  Work --> Processed[Processed Zone\n(publishable artifacts)]
  Processed --> Catalogs[Catalog Zone\nSTAC/DCAT/PROV + checksums]
  Catalogs --> API[Governed API Boundary\n(Trust Membrane + Policy)]
  API --> UI[UI / Stories]
  UI --> Focus[Focus Mode\n(cite or abstain)]
```

### Zone invariants

- **Raw**: immutable source drops or fetch manifests. Append-only. No transforms.
- **Work**: intermediate artifacts + QA outputs. May be regenerated.
- **Processed**: **only publishable** zone. Must be checksummed and cataloged.
- **Catalog**: machine-readable DCAT/STAC/PROV entries that runtime services consume.

> [!NOTE]
> Any “shortcut” that serves raw/work data directly is considered a **trust membrane bypass** and must fail CI.

---

## Promotion gate CI-enforced

### Promotion gate (minimum)

Promotion to `processed/` **MUST** be blocked unless all of the following are true:

1. License present
2. Sensitivity classification present
3. Schema + geospatial checks pass
4. Checksums computed and referenced
5. STAC/DCAT/PROV artifacts exist **and validate**
6. Audit event recorded
7. Human approval recorded if sensitive

### Expanded promotion checklist (recommended)

This is the “no missing aspects” checklist we expect CI to enforce for every dataset promotion:

| Gate | Requirement | Evidence artifact(s) | Typical validator(s) |
|---|---|---|---|
| **G0** | **Fail-closed**: missing required inputs = deny promotion | CI logs + validation report | Runner / aggregator |
| **G1** | Raw assets checksummed and content-addressable | `checksums.txt` / manifest hashes | `V.HASH.*` |
| **G2** | Raw manifest schema valid | `data/raw/**/manifest.(yml|json)` | `V.SCHEMA.manifest` |
| **G3** | License captured and allowed | manifest + DCAT `license` | `V.LICENSE.*` |
| **G4** | Sensitivity classification captured | manifest + validation report + policy labels | `V.SENS.*` |
| **G5** | Schema validation passes; QA report stored with stable ID | `validation_report.json` (+ stable id) | `V.QA.*` |
| **G6** | Spatial/temporal sanity checks pass (when applicable) | report metrics + derived extents | `V.GEO.*`, `V.TIME.*` |
| **G7** | Catalog writers succeeded and are link-check clean | `data/catalog/{dcat,stac,prov}/...` | `V.CAT.*` |
| **G8** | STAC/DCAT/PROV cross-linking is correct | DCAT ↔ STAC ↔ PROV links | `V.CAT.links` |
| **G9** | Contract tests for API queries depending on dataset pass | contract test outputs | `V.CONTRACT.api` |
| **G10** | Audit ledger event exists and references `run_id` | audit record + run record | `V.AUDIT.*` |
| **G11** | If sensitivity not `public`, promotion requires steward review | approval record + audit event | `V.GOV.approval` |

> [!IMPORTANT]
> “Promotion gate” is not just validation — it is the **publish rule**. If any gate fails, the dataset stays in **work** and is not served.

---

## Artifacts and contracts

Validation is only as good as the artifacts it requires. KFM treats the following as **governed**.

### Canonical repo layout (expected)

This README assumes the canonical top-level layout used across KFM:

```text
repo/
├─ data/
│  ├─ raw/           # immutable captures + fetch manifests
│  ├─ work/          # intermediate artifacts + QA reports
│  ├─ processed/     # publishable artifacts (checksummed)
│  └─ catalog/
│     ├─ dcat/
│     ├─ stac/
│     └─ prov/
├─ schemas/          # JSON Schemas (governed)
├─ policy/           # OPA bundles + tests (governed)
├─ src/
│  └─ pipelines/
│     └─ validation/ # ← you are here
└─ .github/workflows/
```

> [!NOTE]
> If your repo differs, adjust paths in CI + this README. The invariants do **not** change.

---

### Required pipeline artifacts

#### `run_record.json` (required for every pipeline run)

A pipeline run must emit a **run record** containing:

- `run_id`, `dataset_id`, `version`
- `started_at`, `ended_at`
- `inputs[]` and `outputs[]` with `sha256`
- `code.git_sha` and `code.image`
- references to:
  - `validation_report` (work zone)
  - `checksums_ref` (processed)
  - `stac_ref`, `dcat_ref`, `prov_ref` (catalog zone)
- `timestamp`

> [!TIP]
> Treat `run_record.json` as the “receipt header” and `validation_report.json` as the “receipt body”.

#### `validation_report.json` (required for every pipeline run)

A run must also emit a **validation report** that:

- summarizes all checks performed
- records policy labels and sensitivity results
- is stable-ID addressable (recommended)
- is machine-readable and CI-friendly

✅ **Minimum expectation:** validation report exists, is parseable, and contains pass/fail per gate.

---

### Dataset raw manifest (required before ingest)

Raw manifests declare what will be ingested and provide:

- dataset identity (`dataset_id`, `version`)
- source URL / source info
- expected files + hashes
- license
- sensitivity level + flags

This enables CI to validate manifests **before** any pipeline job runs.

---

### Catalog artifacts (required before publish)

Promotion requires machine-readable catalogs:

- **DCAT**: dataset-level metadata (publisher, license, contacts, temporal/spatial, distributions)
- **STAC**: geospatial assets (Collections + Items + Assets)
- **PROV**: lineage of every derived artifact (inputs → activities → outputs)

> [!IMPORTANT]
> Catalog artifacts must be **well-formed AND link-check clean**, including cross-links between DCAT ↔ STAC ↔ PROV.

---

## Validator taxonomy

### Validation categories

| Category | Goal | Typical checks |
|---|---|---|
| Schema | Validate structure | JSON Schema checks for manifests, run records, reports, catalogs |
| Geo | Validate geometry/spatial metadata | bbox validity, CRS sanity, topology validity, STAC spatial extent |
| Time | Validate temporal coverage | time_range present, order correct, STAC temporal interval |
| Hash | Ensure content integrity | sha256 present, checksums match, manifest matches outputs |
| Catalog | Ensure discoverability | DCAT required fields, STAC required fields, PROV minimum fields |
| Provenance | Ensure lineage | PROV activity/agent/entity relationships are complete |
| Policy | Ensure governance rules | deny-by-default, sensitivity rules, cite-or-abstain |
| Contract | Ensure runtime stability | API contract tests for dataset queries |
| Audit | Ensure traceability | audit record exists, references run_id, contains decision outcome |
| Safety | Prevent harmful disclosure | sensitive-location rules, redaction required, human approval |

### Validation result model (recommended)

Each check should emit a normalized result:

```json
{
  "check_id": "V.CAT.STAC.collection",
  "status": "pass|fail|warn",
  "severity": "error|warning|info",
  "message": "Human-readable reason",
  "artifacts": [
    {"ref": "data/catalog/stac/example/collection.json", "sha256": "..."}
  ],
  "metrics": {"count": 12},
  "evidence_refs": ["prov://...", "dcat://...", "stac://..."]
}
```

> [!IMPORTANT]
> **Promotion is fail-closed**: any `fail` with `severity=error` MUST block promotion.

---

## Policy-as-code integration

Validation gates are reinforced by **OPA/Rego policy**, which provides:

- central enforcement for trust membrane rules
- deny-by-default behavior
- regression-tested policies

### Expected policy patterns

- **Default deny** (`default allow := false`)
- Explicit allow conditions
- Unit tests for deny conditions (missing citations, missing sensitivity, etc.)

<details>
<summary><strong>Illustrative policy input schema (example)</strong></summary>

```json
{
  "actor": {"role":"public|reviewer|admin", "attributes": {}},
  "request": {"endpoint":"/api/v1/ai/query", "context": {}},
  "answer": {
    "text":"...",
    "has_citations": true,
    "citations":[{"id":"c1"}],
    "sensitivity_ok": true
  }
}
```

</details>

<details>
<summary><strong>Illustrative cite-or-abstain rule (example)</strong></summary>

```rego
package kfm.ai

default allow := false

allow if {
  input.answer.has_citations == true
  input.answer.sensitivity_ok == true
}
```

</details>

---

## How to run validations

> [!NOTE]
> Exact commands may differ by repo implementation. The patterns below are the intended usage.

### Recommended: one “acceptance harness” entrypoint

A single harness should run:

- STAC validation
- DCAT validation
- PROV minimum fields validation
- policy unit tests (`opa test`)
- conftest policy checks (if used)
- checksum verification
- (optional) provenance attestation verification
- (optional) reproducibility check via canonical `spec_hash`

**Expected ergonomics**:
- CI: a reusable workflow step / composite action
- Local: `make verify` (or equivalent)

### Direct tool runs (common)

```bash
# OPA policy unit tests
opa test policy -v

# Catalog validations (examples; tool choice may vary)
stac-validator data/catalog/stac/<dataset_id>/collection.json
# dcat validation tool (repo-defined)
# prov validation tool (repo-defined)
```

### Smoke testing a single dataset run

Given a dataset id/version:

1. Confirm `data/work/<dataset_id>/validation_report.json` exists
2. Confirm `data/work/<dataset_id>/run_record.json` exists
3. Confirm `data/processed/<dataset_id>/checksums.txt` exists
4. Confirm DCAT/STAC/PROV artifacts exist under `data/catalog/`
5. Run the validation harness

---

## How to add a validator

### Design rules (non-negotiable)

A new validator MUST:

- be deterministic (same inputs → same output)
- avoid network access during validation (unless explicitly allowed + cached)
- emit normalized results with stable IDs
- produce actionable failure messages
- include tests + fixtures

### Minimal steps checklist

- [ ] Pick a `check_id` and category (see taxonomy)
- [ ] Implement validator function/module
- [ ] Add fixture set (pass + fail + edge cases)
- [ ] Add unit tests
- [ ] Add CI wiring so it runs on relevant changes
- [ ] Ensure failures block promotion when appropriate
- [ ] Document the check in this README (or linked registry)

---

## Dataset integration Definition of Done

When adding a new dataset source/pipeline, the work is not “done” until:

### Artifacts

- [ ] Raw manifest exists and schema-valid
- [ ] Raw assets are hashed and addressable by content hash
- [ ] Work zone contains run record + validation report
- [ ] Processed zone contains publishable artifacts + checksums
- [ ] Catalog zone contains DCAT + (if spatial) STAC + PROV
- [ ] Catalog artifacts are link-check clean and cross-linked

### Governance

- [ ] License present and compliant
- [ ] Sensitivity classification present + policy labels attached
- [ ] Sensitive datasets have documented redaction step (if needed)
- [ ] Human approval recorded when required

### Runtime stability

- [ ] Contract tests for dependent API queries pass
- [ ] Audit ledger event exists for promotion and references run_id

---

## Sensitivity and redaction

### Sensitivity is a first-class control

Validation must explicitly classify datasets and outputs. Suggested classes:

- `public`
- `restricted`
- `sensitive-location`
- `culturally_sensitive`
- `pii_risk`

> [!IMPORTANT]
> If sensitivity flags are triggered, pipelines MUST route to governance review.
> Public promotion MUST require approval and/or redaction (depending on policy).

### Redaction as a first-class transformation

Redaction is not a UI trick. It is:

- a pipeline activity (`redaction_job`)
- recorded in PROV (inputs → activity → redacted outputs)
- subject to the same checksums + catalog rules as any other transform

---

## CI hardening baseline

Recommended minimal CI set:

- **Docs**: lint + link-check + template validator
- **Stories**: Story Node template validator + citation resolution
- **Data**: STAC/DCAT/PROV validation + checksums verification
- **Policy**: `opa test` policy `-v`
- **Supply chain**: SBOM + provenance attestation (where adopted)

> [!TIP]
> Treat schemas, policies, and templates as “production changes.” Breaking changes require review + versioning.

---

## Troubleshooting

### Promotion fails because “catalog missing”
- Check that DCAT entry exists and is well-formed.
- If the dataset is spatial, ensure STAC Collection + Items exist.
- Ensure PROV chain exists and references the run and artifacts.
- Ensure link-check passes (cross-links between catalogs resolve).

### Promotion fails because “sensitivity missing”
- Ensure manifest includes sensitivity level.
- Ensure validation report includes sensitivity classification result.
- Ensure policy labels are present.

### Checksums mismatch
- Confirm raw expected files match actual downloads.
- Confirm processed artifact checksums were recomputed after any transform.
- Confirm you’re validating the correct version_id/run_id.

---

## Governance and change control

### What counts as a governed change?

Any change that affects:

- schemas (`schemas/`)
- promotion gate logic
- validation thresholds/rules
- policy bundles/tests (`policy/`)
- Story Node template rules
- evidence/citation resolution rules

### Required process (minimum)

- [ ] PR includes validation updates + tests
- [ ] CI proves fail-closed behavior still holds
- [ ] Version bumps for schemas/policies when breaking
- [ ] ADR entry for major behavioral changes (recommended)

---

## Appendix: Verification checklist (repo alignment)

Because some elements may be implemented differently, verify:

- [ ] Where schemas live (`schemas/` vs `src/pipelines/validation/schemas/`)
- [ ] Where policy bundles live (`policy/` and test layout)
- [ ] Actual harness command (`make verify`, `scripts/validate`, etc.)
- [ ] The canonical file names and exact output paths for:
  - `run_record.json`
  - `validation_report.json`
  - `checksums.txt`
  - catalog output directories

> [!NOTE]
> The invariants and promotion gates above are the authoritative behavior; file paths and tooling wrappers may vary.

