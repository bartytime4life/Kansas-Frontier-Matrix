<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/f198c44a-6fb6-40e0-89e0-3f37f76e7742
title: data/ — Governed dataset artifacts + catalogs (Truth Path)
type: standard
version: v2
status: draft
owners: KFM Data Stewardship (resolve via CODEOWNERS)
created: 2026-02-22
updated: 2026-02-27
policy_label: public
related:
  - ../README.md
  - ../.github/README.md
  - ../configs/README.md
  - ../contracts/README.md
  - ../docs/governance/
tags:
  - kfm
  - data
  - governance
  - promotion-contract
  - catalogs
  - evidence
  - provenance
notes:
  - Documents the canonical “truth path” layout + required artifacts for promotion eligibility.
  - Written to be CI/validator-friendly (fail-closed, deterministic paths).
  - This README is a target contract; confirm repo reality and adjust path names only with a governed migration plan.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/` — Governed dataset artifacts + catalogs
Governed dataset artifacts + catalogs for the KFM Truth Path:

**RAW → WORK → QUARANTINE → PROCESSED → CATALOG → PUBLISHED**  
…and an append-only **AUDIT** trail that makes every promotion and user-visible claim reviewable.

**Status:** draft • **Owners:** KFM Data Stewardship • **Last updated:** 2026-02-27

![status](https://img.shields.io/badge/status-draft-yellow)
![governance](https://img.shields.io/badge/governance-fail--closed-critical)
![policy](https://img.shields.io/badge/policy-default--deny-critical)
![truth-path](https://img.shields.io/badge/truth%20path-RAW→WORK→QUARANTINE→PROCESSED→CATALOG→PUBLISHED-blue)
![catalogs](https://img.shields.io/badge/catalogs-DCAT%20%7C%20STAC%20%7C%20PROV-informational)
![identity](https://img.shields.io/badge/identity-spec__hash%20anchored-important)

> [!IMPORTANT]
> **This directory is canonical truth.**  
> Databases/search/tiles are rebuildable projections. If a projection disagrees with `data/processed` + `data/catalog`, the **catalog + processed artifacts win**.

---

## Quick navigation

- [Truth status legend](#truth-status-legend)
- [Directory contract](#directory-contract)
- [Repo reality check](#repo-reality-check)
- [What goes where](#what-goes-where)
- [Truth path diagram](#truth-path-diagram)
- [Directory layout](#directory-layout)
- [Canonical path convention](#canonical-path-convention)
- [Zone contracts](#zone-contracts)
- [Dataset specs](#dataset-specs)
- [Source registry](#source-registry)
- [Anchor register](#anchor-register)
- [Quarantine workflow](#quarantine-workflow)
- [Promotion Contract gates](#promotion-contract-gates)
- [Catalog triplet](#catalog-triplet)
- [Checksums and digests](#checksums-and-digests)
- [Policy labels and sensitive data](#policy-labels-and-sensitive-data)
- [Definition of Done](#definition-of-done)
- [Appendix templates](#appendix-templates)

---

## Truth status legend

- **CONFIRMED (design):** required KFM posture (must hold regardless of stack)
- **UNKNOWN (repo):** not verified on this branch (treat as TODO; fail-closed)
- **PROPOSED:** a recommended template/pattern (adopt only after review)

> [!NOTE]
> This README is a **contract target** for the truth path.  
> If your branch differs, update this README and any validators together as a governed change.

---

## Directory contract

### Purpose
`data/` holds the **governed artifacts** that make KFM reproducible and auditable:
- dataset onboarding specs (inputs to deterministic identity)
- source registry entries (rights + sensitivity + access posture)
- immutable acquisitions (RAW)
- intermediate transforms and QA outputs (WORK)
- blocked artifacts with remediation (QUARANTINE)
- publishable, immutable artifacts (PROCESSED)
- canonical metadata + lineage (CATALOG: DCAT + STAC + PROV + receipts)
- distribution-ready outputs (PUBLISHED, policy/rights filtered)
- append-only audit ledger segments (AUDIT)

### Where this fits
`data/` sits on the **canonical side** of the trust membrane:
- **Pipelines** write here (or to equivalent object-store prefixes).
- **Governed APIs** serve only **promoted** versions that have passed gates and have catalogs/receipts.
- **Apps/UI** never read from here directly.

### Acceptable inputs
- Small, reviewable metadata (specs/registry/receipts/manifests/catalog JSON)
- Checksums and validation reports
- Approved dataset artifacts *when policy allows storing them in-repo* (often it will not)

### Exclusions
- **Secrets** (keys, tokens, credentials)
- **PII** (unless explicitly restricted and governed outside of git; even then prefer external storage)
- **Exact coordinates for sensitive locations** in public/publishable paths
- Large binaries when the repo is not meant to store them (use object storage; keep digests + pointers here)

> [!WARNING]
> If it would be unsafe to paste into a public issue, it does not belong in public-labeled areas of `data/`.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Repo reality check

KFM can store the **full truth path** in object storage in production, while the git repo stores:
- specs + registries + catalogs + receipts + digests
- bounded fixtures for tests

Before enforcing gates, verify what your branch actually contains:

```bash
# Show top-level shape
find data -maxdepth 2 -type d -print

# Find dataset specs and source registry entries
ls -la data/specs 2>/dev/null || true
ls -la data/registry/sources 2>/dev/null || true

# Find catalogs and promotion manifests (if any exist)
find data/catalog -maxdepth 4 -name 'promotion_manifest*.json' -print 2>/dev/null

# Confirm quarantine exists (directory or state approach)
ls -la data/quarantine 2>/dev/null || true
```

> [!IMPORTANT]
> If your repo uses a different prefix (e.g., `storage/`, `artifacts/`, or an object-store bucket mapping),
> treat this README as the **semantic contract** and map the paths accordingly—do not silently invent new meanings.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## What goes where

| Area | Purpose | Mutability | Must include (minimum) |
|---|---|---:|---|
| `data/specs/` | Dataset onboarding specs (inputs to `spec_hash`) | editable (versioned) | dataset_slug, sources, transforms, outputs, default policy label |
| `data/registry/sources/` | Source registry (rights/sensitivity/access posture) | editable | license/terms snapshot pointer, sensitivity intent, cadence, QA notes |
| `data/registry/anchors/` | Anchor dataset register (Tier 0/1/…) | editable (versioned) | anchors list + CI validation against sources/specs |
| `data/fixtures/` | Small fixtures for tests/eval | editable | bounded samples + expected outputs |
| `data/raw/` | Immutable acquisitions (append-only) | append-only | acquisition manifest, terms snapshot(s), raw artifacts, checksums |
| `data/work/` | Intermediate transforms + QA outputs | append-only per run | artifacts, QA outputs, checksums, run receipt pointer (or copy) |
| `data/quarantine/` | Failed gates (blocked from promotion) | append-only | reason + remediation plan + owner, diagnostics (bounded), checksums |
| `data/processed/` | Publishable artifacts (immutable per DatasetVersion) | immutable per version | artifacts, checksums, runtime metadata, QA report |
| `data/catalog/` | Canonical metadata + lineage (triplet + receipts + promotion manifest) | immutable per version | DCAT + STAC + PROV, run receipts, promotion manifest, link validation |
| `data/published/` | Export/distribution-ready (policy/rights filtered) | immutable per version | exports + attribution bundle (if allowed), checksums |
| `data/audit/` | Append-only audit ledger segments | append-only | ledger segments, references to approvals/decisions (policy-safe) |

> [!WARNING]
> **RAW is append-only.** Never “fix” a RAW acquisition in place.  
> If upstream content is wrong, create a new DatasetVersion/acquisition, quarantine the bad one, and supersede it via catalog/provenance.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Truth path diagram

```mermaid
flowchart LR
  U[Upstream sources] --> R[RAW]
  R --> W[WORK]
  W --> P[PROCESSED]
  P --> C[CATALOG triplet]
  C --> PUB[PUBLISHED]
  C --> IDX[Rebuildable projections]
  IDX --> API[Governed API]
  API --> UI[Map Story Focus]

  W --> Q[QUARANTINE]
  Q -. blocks promotion .-> P

  C --> AUD[Audit ledger]
  API --> AUD
```

> [!NOTE]
> Only **promoted DatasetVersions** (processed + validated catalogs + receipts + policy label) are eligible to appear in runtime surfaces.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Directory layout

This is the **recommended contract layout** for the truth path. Use it as the basis for validators and CI gates.

```text
data/                                                   # Governed truth path + registries
├─ README.md
│
├─ specs/                                                # Dataset onboarding specs (inputs to spec_hash; deterministic)
│  ├─ README.md
│  ├─ <dataset_slug>.v1.json                             # Canonical dataset spec (versioned)
│  └─ _schemas/                                          # OPTIONAL: schemas for dataset specs (or reference contracts/)
│     └─ kfm.dataset_spec.v1.schema.json
│
├─ registry/                                             # Canonical registries (governed)
│  ├─ README.md
│  ├─ sources/
│  │  ├─ <source_id>.v1.yml                              # Source registry entry (human editable)
│  │  └─ <source_id>.v1.json                             # OPTIONAL: normalized export (generated)
│  └─ anchors/
│     ├─ anchors.v1.json                                 # Anchor register (Tier 0/1/2/R)
│     └─ _schemas/
│        └─ kfm.anchor_register.v1.schema.json
│
├─ fixtures/                                             # Small fixtures for tests/evals (bounded; synthetic preferred)
│  ├─ README.md
│  ├─ sample_dataset/
│  ├─ sample_catalog_triplet/
│  └─ golden/                                            # expected outputs for validators
│
├─ raw/                                                  # Immutable acquisitions (append-only; never served)
│  └─ <dataset_slug>/
│     └─ <dataset_version_id>/                           # Stable version identity (spec_hash anchored)
│        ├─ acquisition_manifest.v1.json                 # Capture manifest (license/sensitivity required)
│        ├─ terms_snapshot/                              # Terms/license snapshot(s) captured at acquisition time
│        │  └─ <captured_at>.txt|html|pdf
│        ├─ artifacts/                                   # Original payload (never modified)
│        ├─ checksums.v1.json                            # Digests for raw artifacts
│        └─ notes.md                                     # OPTIONAL: human notes (policy-safe)
│
├─ work/                                                 # Regeneratable intermediates (never served; run-scoped)
│  └─ <dataset_slug>/
│     └─ <dataset_version_id>/
│        ├─ runs/
│        │  └─ <run_id>/                                 # One pipeline work run
│        │     ├─ artifacts/                             # Intermediate outputs (bounded; reproducible)
│        │     ├─ qa/                                    # Validation/QC outputs (schema/geo/time/license/policy checks)
│        │     ├─ checksums.v1.json                      # Digests for work artifacts
│        │     └─ run_receipt.ref.json                   # POINTER or copy of the run receipt (see catalog/ too)
│        └─ summary.json                                 # OPTIONAL: aggregated status across runs (generated)
│
├─ quarantine/                                           # Failed gates (never served; never promoted)
│  └─ <dataset_slug>/
│     └─ <dataset_version_id>/
│        ├─ reason.v1.json                               # REQUIRED: reason code + remediation plan + owner
│        ├─ diagnostics/                                 # Debug artifacts (bounded; synthetic where possible)
│        ├─ checksums.v1.json                            # Digests for quarantine artifacts
│        └─ supersedes.json                              # OPTIONAL: points to replacement DatasetVersion(s)
│
├─ processed/                                            # Publishable artifacts — immutable per DatasetVersion
│  └─ <dataset_slug>/
│     └─ <dataset_version_id>/
│        ├─ artifacts/                                   # Data products (GeoParquet, PMTiles, COG, JSONL, PDF…)
│        ├─ checksums.v1.json                            # Digests for processed artifacts (required)
│        ├─ runtime_metadata.v1.json                     # Bounds, schema refs, policy label, evidence refs
│        └─ qa/
│           ├─ validation_report.v1.json                 # REQUIRED for promotion gates
│           └─ profiles_used.v1.json                     # OPTIONAL: what profile set validated this version
│
├─ catalog/                                              # Canonical metadata + lineage (validated + cross-linked)
│  └─ <dataset_slug>/
│     └─ <dataset_version_id>/
│        ├─ dcat.jsonld                                  # DCAT dataset/distribution record(s)
│        ├─ stac/
│        │  ├─ collection.json                           # STAC Collection
│        │  └─ items/                                    # STAC Items (one file per item)
│        ├─ prov/
│        │  └─ prov.jsonld                               # PROV bundle linking raw → work → processed
│        ├─ run_receipts/                                # Receipts/manifests used as promotion evidence
│        │  └─ <run_id>.json
│        ├─ promotion_manifest.v1.json                   # Roll-up manifest tying catalogs/receipts/checksums together
│        ├─ linkcheck_report.v1.json                     # OPTIONAL: generated linkcheck outputs (CI artifact)
│        └─ checksums.v1.json                            # OPTIONAL: digest roll-up for catalog artifacts
│
├─ published/                                            # Export/distribution-ready outputs (policy/rights filtered)
│  └─ <dataset_slug>/
│     └─ <dataset_version_id>/
│        ├─ exports/                                     # Allowed exports (CSV/GeoJSON/packages/tilesets)
│        ├─ attribution/                                 # Auto-generated attribution bundle (license + notices)
│        └─ checksums.v1.json
│
└─ audit/                                                # Append-only audit records (often stored outside git in prod)
   ├─ README.md
   └─ ledger/
      └─ <year>/<month>/
         └─ append-only.log                              # Append-only ledger segments (policy-safe; access-controlled)
```

> [!IMPORTANT]
> If artifacts live outside git (recommended for most real datasets), these paths map cleanly to object storage prefixes.
> The repo can still store **specs + registries + manifests + catalogs + receipts + digests** to preserve auditability.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Canonical path convention

KFM uses predictable paths so CI, policy, and evidence resolution can be deterministic.

### Canonical path patterns (zones)
- `specs/<dataset_slug>.v1.json`
- `registry/sources/<source_id>.v1.yml`
- `registry/anchors/anchors.v1.json`

- `raw/<dataset_slug>/<dataset_version_id>/acquisition_manifest.v1.json`
- `raw/<dataset_slug>/<dataset_version_id>/artifacts/*`
- `raw/<dataset_slug>/<dataset_version_id>/checksums.v1.json`

- `work/<dataset_slug>/<dataset_version_id>/runs/<run_id>/artifacts/*`
- `work/<dataset_slug>/<dataset_version_id>/runs/<run_id>/qa/*`
- `work/<dataset_slug>/<dataset_version_id>/runs/<run_id>/checksums.v1.json`

- `quarantine/<dataset_slug>/<dataset_version_id>/reason.v1.json`

- `processed/<dataset_slug>/<dataset_version_id>/artifacts/*`
- `processed/<dataset_slug>/<dataset_version_id>/checksums.v1.json`
- `processed/<dataset_slug>/<dataset_version_id>/qa/validation_report.v1.json`

- `catalog/<dataset_slug>/<dataset_version_id>/dcat.jsonld`
- `catalog/<dataset_slug>/<dataset_version_id>/stac/collection.json`
- `catalog/<dataset_slug>/<dataset_version_id>/prov/prov.jsonld`
- `catalog/<dataset_slug>/<dataset_version_id>/run_receipts/<run_id>.json`
- `catalog/<dataset_slug>/<dataset_version_id>/promotion_manifest.v1.json`

- `published/<dataset_slug>/<dataset_version_id>/exports/*`

### Canonical rules (enforced by validators / promotion gates)
- `raw/`, `work/`, `quarantine/`, `processed/`, `catalog/`, `published/`, `audit/` are **reserved** zone names.
- `dataset_slug` is stable and does **not** encode dates.
- `dataset_version_id` is derived deterministically from the dataset spec (`spec_hash` posture).
- Every artifact referenced by catalogs/receipts has a digest.
- Catalogs cross-link and validate as a triplet.
- Quarantined versions **must not** be served or promoted.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Zone contracts

| Zone | Primary goal | Allowed contents | Not allowed | “Serve/publish eligible?” |
|---|---|---|---|---|
| RAW | Preserve upstream truth | as-received payload + manifest + terms snapshot + digests | edits-in-place | ❌ |
| WORK | Normalize + validate + draft redactions | intermediate transforms + QA + candidates | skipping QA, “manual fixes” without provenance | ❌ |
| QUARANTINE | Fail closed safely | reason + remediation + diagnostics (bounded) | promotion shortcuts | ❌ |
| PROCESSED | Publishable outputs | KFM-approved formats + digests + runtime metadata | missing digests/metadata | ✅ (only with catalogs + receipts + pass gates) |
| CATALOG | Canonical evidence surface | DCAT + STAC + PROV + receipts + promotion manifest | unvalidated catalogs, broken links | ✅ |
| PUBLISHED | Distribution-ready | policy/rights-filtered exports | leaking restricted details | ✅ (policy-limited) |
| AUDIT | Reviewability | append-only ledger segments | deletion/rewrites | N/A |

---

## Dataset specs

Dataset specs are **inputs** to deterministic identity and pipeline behavior.

**Location:** `data/specs/<dataset_slug>.v1.json`

Minimum fields (recommended):
- `kfm_dataset_spec_version`
- `dataset_slug`, `title`
- `sources[]` (kind, uri/identifier, terms snapshot requirement)
- `transforms[]` (container digest pinned, params)
- `outputs[]` (zone=processed paths + media types)
- `policy.default_policy_label`

> [!IMPORTANT]
> Changing a dataset spec changes identity inputs.  
> Any change that affects `spec_hash` must be treated as a **new DatasetVersion** and must be audit-visible.

---

## Source registry

Every upstream **source** must have a machine-readable registry entry; it is a promotion input (not optional documentation).

**Location:** `data/registry/sources/<source_id>.v1.yml`

Minimum fields:
- `source_id` (stable)
- `name`, `authority`, `domain`
- `access_method` (api/bulk/portal/manual/scrape)
- `cadence`
- `license_terms_snapshot` (what/when/where captured)
- `sensitivity_intent` (policy label intent)
- `connector_spec` (non-secret)
- `known_limitations` + `qa_checks`

---

## Anchor register

The anchor register makes the “build-first” dataset set enforceable.

**Location:** `data/registry/anchors/anchors.v1.json`

Validation expectations:
- every anchor references an existing `source_id` entry
- every anchor references an existing dataset spec
- anchors requiring restricted handling must declare derivative expectations (e.g., public_generalized spec exists)

> [!NOTE]
> The anchor register is a **CI gate input**: it prevents drift between “what we claim are anchors” and “what is actually onboarded.”

---

## Quarantine workflow

Quarantine triggers include:
- unclear licensing / rights
- validation failures (schema/geo/time)
- sensitivity concerns (restricted/sensitive location)
- upstream instability preventing reproducible acquisition

Quarantine requires:
- `reason.v1.json` with a reason code + remediation plan + owner
- checksums for any diagnostic artifacts
- explicit supersession pointers if replaced

> [!WARNING]
> Do not “temporarily promote” quarantined items.

---

## Promotion Contract gates

Promotion MUST be blocked unless required artifacts exist **and validate**. These gates are the basis of CI checks and steward review.

### Gate A — Identity and versioning
- Dataset ID and slug are stable.
- DatasetVersion is immutable and derived from deterministic `spec_hash`.

### Gate B — Licensing and rights metadata
- License is explicit and compatible with intended use.
- Rights-holder and attribution requirements are captured.
- If unclear: quarantine (fail closed).

### Gate C — Sensitivity classification and redaction plan
- `policy_label` assigned.
- For restricted/sensitive-location: a redaction/generalization plan exists and is recorded in PROV.

### Gate D — Catalog triplet validation
- DCAT record exists and validates under profile.
- STAC collection/items exist (if applicable) and validate.
- PROV bundle exists and validates.
- Cross-links are present and resolvable.

### Gate E — Run receipt and checksums
- Run receipts exist for producing runs.
- Inputs and outputs are enumerated with digests.
- Environment recorded (container image digest, params digest, git ref).

### Gate F — Policy tests and contract tests
- Policy tests pass (fixtures-driven).
- Evidence resolver can resolve at least one EvidenceRef in CI.
- Schemas and contracts validate.

> [!TIP]
> Treat the gate set as **non-skippable**. Use a single always-runs “gate summary” check as the branch protection requirement.

---

## Catalog triplet

The triplet is KFM’s interoperability + evidence surface:

- **DCAT**: dataset identity, publisher, license/rights, distributions
- **STAC**: assets, spatiotemporal extents, hrefs + checksums, policy-consistent geometry/bbox
- **PROV**: lineage (raw → work → processed), agents, activities, parameters, approvals

Minimum expectations:
- All three exist where applicable and validate under KFM profiles.
- All three include:
  - `kfm:dataset_id`
  - `kfm:dataset_version_id`
  - `kfm:policy_label`
- All cross-links resolve deterministically (no guessing).
- EvidenceRefs used by stories/focus map into these objects.

---

## Checksums and digests

Rules:
- Every artifact gets a digest (prefer `sha256`).
- Digests are recorded in:
  - zone-adjacent `checksums.v1.json`
  - run receipts (`catalog/.../run_receipts/<run_id>.json`)
  - promotion manifest roll-up (`promotion_manifest.v1.json`)

Recommended `checksums.v1.json` structure:

```json
{
  "kfm_checksums_version": "v1",
  "algorithm": "sha256",
  "artifacts": [
    { "path": "artifacts/events.parquet", "digest": "sha256:..." },
    { "path": "qa/validation_report.v1.json", "digest": "sha256:..." }
  ]
}
```

> [!IMPORTANT]
> Checksums are integrity controls and audit anchors. Missing or mismatched digests are promotion blockers.

---

## Policy labels and sensitive data

Starter labels (extend via controlled vocab):
- `public`
- `public_generalized`
- `restricted`
- `restricted_sensitive_location`
- `internal`
- `embargoed`
- `quarantine`

Default-safe rules:
- Default deny for sensitive-location and restricted data unless policy explicitly allows.
- If any public representation is allowed, publish a **separate** `public_generalized` derivative.
- Never embed precise coordinates in Story Nodes or Focus outputs unless policy explicitly allows.
- Generalization/redaction is a first-class transform recorded in PROV.

---

## Definition of Done

A dataset integration (or new DatasetVersion) is DONE only when:

### Onboarding
- [ ] Source registry entry exists (`data/registry/sources/*`) with terms snapshot pointer and sensitivity intent.
- [ ] Dataset spec exists (`data/specs/*`) and `spec_hash` stability is tested.
- [ ] RAW acquisition includes manifest + terms snapshot + digests.
- [ ] WORK run(s) emit QA artifacts + digests + run receipt references.
- [ ] Failures are quarantined with reason + remediation plan.

### Promotion eligibility
- [ ] PROCESSED artifacts exist and are digest-addressed.
- [ ] CATALOG triplet validates and cross-links (DCAT/STAC/PROV).
- [ ] Run receipts exist and enumerate input/output digests.
- [ ] Promotion manifest exists and ties everything together.
- [ ] At least one EvidenceRef resolves successfully in CI (smoke test).
- [ ] Policy label reviewed where required (steward workflow).
- [ ] Changelog entry exists if this is a governed release/promotion.

---

## Appendix templates

<details>
<summary><strong>Template: Dataset spec (JSON)</strong></summary>

```json
{
  "kfm_dataset_spec_version": "v1",
  "dataset_slug": "example_dataset",
  "title": "Example Dataset",
  "sources": [
    {
      "kind": "bulk",
      "uri": "https://example.invalid/data.zip",
      "terms_snapshot_required": true,
      "schedule": "cron(0 3 * * *)"
    }
  ],
  "transforms": [
    {
      "name": "normalize",
      "container_image": "sha256:<pinned_image_digest>",
      "params": { "crs": "EPSG:4326", "schema_version": "v1" }
    }
  ],
  "outputs": [
    { "zone": "processed", "path": "artifacts/data.geoparquet", "media_type": "application/x-parquet" }
  ],
  "policy": { "default_policy_label": "public" }
}
```
</details>

<details>
<summary><strong>Template: Source registry entry (YAML)</strong></summary>

```yaml
source_id: usgs_waterdata_nwis
name: USGS WaterData (NWIS)
authority: USGS
domain: hydrology
access_method: api
cadence: daily
license_terms_snapshot:
  kind: public_domain
  captured_at: "2026-02-22"
  path_hint: "data/raw/usgs_waterdata_nwis/<dataset_version_id>/terms_snapshot/..."
sensitivity_intent: public
connector_spec:
  type: http_api
  base_url: "https://example.invalid/"
credentials:
  strategy: secrets_manager
known_limitations:
  - missing_values_present
qa_checks:
  - validate_lat_lon_bounds
  - validate_time_series_gaps
```
</details>

<details>
<summary><strong>Template: Acquisition manifest (JSON)</strong></summary>

```json
{
  "kfm_acquisition_manifest_version": "v1",
  "dataset_slug": "example_dataset",
  "dataset_version_id": "2026-02.abcd1234",
  "source_id": "example_source",
  "fetched_at": "2026-02-22T12:00:00Z",
  "license_terms_snapshot": {
    "captured_at": "2026-02-22T12:00:00Z",
    "paths": ["terms_snapshot/2026-02-22T12-00Z.txt"]
  },
  "policy": { "sensitivity_intent": "public" },
  "artifacts": [
    { "path": "artifacts/source.csv", "media_type": "text/csv" }
  ],
  "notes": "RAW is append-only; supersede with a new DatasetVersion if needed."
}
```
</details>

<details>
<summary><strong>Template: Quarantine reason (JSON)</strong></summary>

```json
{
  "kfm_quarantine_reason_version": "v1",
  "dataset_slug": "example_dataset",
  "dataset_version_id": "2026-02.abcd1234",
  "reason_code": "RIGHTS_UNCLEAR|VALIDATION_FAIL|SENSITIVE_LOCATION|OTHER",
  "summary": "Short policy-safe summary of why this version is blocked.",
  "remediation_plan": {
    "owner": "team-or-person",
    "next_steps": ["Capture license terms snapshot", "Add generalization transform", "Re-run validation"],
    "target_date": "2026-03-15"
  },
  "created_at": "2026-02-22T13:00:00Z"
}
```
</details>

<details>
<summary><strong>Template: Validation report (JSON)</strong></summary>

```json
{
  "kfm_validation_report_version": "v1",
  "dataset_slug": "example_dataset",
  "dataset_version_id": "2026-02.abcd1234",
  "status": "pass|degraded|fail",
  "checks": [
    { "name": "schema", "status": "pass", "details": {} },
    { "name": "spatial_bounds", "status": "pass", "details": {} },
    { "name": "temporal_coverage", "status": "degraded", "details": { "missing_pct": 0.02 } },
    { "name": "rights", "status": "pass", "details": {} },
    { "name": "policy", "status": "pass", "details": { "policy_label": "public" } }
  ],
  "generated_at": "2026-02-22T14:00:00Z"
}
```
</details>

<details>
<summary><strong>Template: Run receipt (JSON)</strong></summary>

```json
{
  "kfm_run_receipt_version": "v1",
  "run_id": "kfm://run/2026-02-22T12:00:00Z.example.abcd",
  "kind": "pipeline|index|story_publish|focus",
  "dataset_slug": "example_dataset",
  "dataset_version_id": "2026-02.abcd1234",
  "inputs": [
    { "href": "raw/example_dataset/2026-02.abcd1234/artifacts/source.csv", "digest": "sha256:..." }
  ],
  "outputs": [
    { "href": "processed/example_dataset/2026-02.abcd1234/artifacts/data.geoparquet", "digest": "sha256:..." }
  ],
  "checks": { "qa_status": "pass", "catalog_valid": true, "links_ok": true },
  "policy": { "policy_label": "public", "decision_id": "kfm://policy_decision/xyz", "obligations": [] },
  "environment": {
    "git_commit": "<commit>",
    "container_image": "sha256:<image_digest>",
    "parameters_digest": "sha256:<params_digest>"
  },
  "timestamps": { "started_at": "2026-02-22T12:00:00Z", "ended_at": "2026-02-22T12:10:00Z" },
  "audit_ref": "kfm://audit/entry/123"
}
```
</details>

<details>
<summary><strong>Template: Promotion manifest (JSON)</strong></summary>

```json
{
  "kfm_promotion_manifest_version": "v1",
  "dataset_slug": "example_dataset",
  "dataset_version_id": "2026-02.abcd1234",
  "spec_hash": "sha256:abcd1234",
  "released_at": "2026-02-22T13:00:00Z",
  "artifacts": [
    { "path": "artifacts/data.geoparquet", "digest": "sha256:...", "media_type": "application/x-parquet" }
  ],
  "catalogs": [
    { "path": "dcat.jsonld", "digest": "sha256:..." },
    { "path": "stac/collection.json", "digest": "sha256:..." },
    { "path": "prov/prov.jsonld", "digest": "sha256:..." }
  ],
  "qa": { "status": "pass", "report_digest": "sha256:..." },
  "policy": { "policy_label": "public", "decision_id": "kfm://policy_decision/xyz" },
  "approvals": [
    { "role": "steward", "principal": "<id>", "approved_at": "2026-02-22T12:59:00Z" }
  ]
}
```
</details>

<p align="right"><a href="#top">Back to top ↑</a></p>
