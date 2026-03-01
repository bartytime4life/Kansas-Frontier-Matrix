<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/8fc07965-e8db-45b4-975f-cd18edbd604c
title: Gate A — Identity & Versioning
type: standard
version: v1
status: draft
owners: <TBD: Data Stewardship + Platform>
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - docs/data/promotion/checklists/
tags: [kfm, data, promotion, checklist, gate-a, identity, versioning, spec_hash, digests]
notes:
  - Fail-closed checklist for Promotion Contract Gate A (Identity & Versioning).
  - Keep scope limited to identity, deterministic spec hashing, and artifact digests.
[/KFM_META_BLOCK_V2] -->

# Gate A — Identity & Versioning

![status](https://img.shields.io/badge/status-draft-lightgrey)
![gate](https://img.shields.io/badge/promotion-gate%20A-blue)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)

**Purpose:** define the *minimum, testable* requirements for stable dataset identity and immutable DatasetVersion identity, so KFM can cache, cite, reproduce, and enforce policy consistently.

- **Gate type:** **hard fail** (promotion MUST NOT proceed if any required check fails)
- **Applies to:** any dataset version moving into **PROCESSED + CATALOG (+ PUBLISHED surfaces)**
- **Primary outputs:** `dataset_id`, `dataset_version_id`, `spec_hash`, and **artifact digests** (sha256)

> [!NOTE]
> This gate is intentionally narrow. Licensing, sensitivity/redaction, catalog schema validation, cross-linking, QA thresholds, run receipts, and release manifests are handled by other gates.

---

## Navigation

- [Scope](#scope)
- [Definitions](#definitions)
- [Inputs](#inputs)
- [Exit criteria](#exit-criteria)
- [Checklist](#checklist)
- [Evidence artifacts](#evidence-artifacts)
- [Automation hooks](#automation-hooks)
- [Common failures](#common-failures)
- [Change log](#change-log)

---

## Scope

### In scope

1. **Stable dataset identity**
   - dataset slug / `dataset_id` naming rules
   - identifier family conventions (URI-like, stable prefixes)

2. **Deterministic DatasetVersion identity**
   - canonical spec document exists and is hashable
   - `spec_hash` is computed deterministically using canonical JSON
   - anti–hash-drift safeguards (store canonical spec; golden tests)

3. **Artifact digest integrity**
   - all promoted artifacts have **sha256** digests recorded
   - digests are verified against the produced bytes (no mismatches)

### Out of scope

- License/rights fields and license snapshots (**Gate B**)
- Sensitivity classification and redaction/generalization obligations (**Gate C**)
- DCAT/STAC/PROV validation + link checking (**Gate D**)
- QA thresholds and validation reports (**Gate E**)
- Run receipt + audit ledger (**Gate F**)
- Release/promotion manifest creation (**Gate G**)

---

## Definitions

- **Dataset (`dataset_id`)**: a stable logical dataset identity (e.g., `noaa_ncei_storm_events`).
- **DatasetVersion (`dataset_version_id`)**: an immutable version identity for one promoted output set.
- **Spec (`spec`)**: the canonical configuration describing upstream acquisition, transforms, validation, outputs, policy intent, and cadence.
- **`spec_hash`**: `sha256(...)` computed over an **RFC 8785 canonical JSON** representation of the spec.
- **Artifact digest**: a `sha256:<hex>` digest of an artifact’s bytes; recorded anywhere an artifact is referenced (manifests, catalogs, receipts).

---

## Inputs

**Minimum required inputs to run Gate A checks:**

1. **Dataset registry entry** (or equivalent) containing:
   - `dataset_id`
   - `spec_ref` and `spec_hash`
   - `policy_label` (intent only; enforcement is a later gate)
2. **Canonical dataset spec file** (machine-readable; JSON strongly preferred for RFC 8785 canonicalization)
3. **Produced artifact list** for the candidate DatasetVersion (paths + digests + media types)

> [!TIP]
> If you are still in “draft PR before first run” stage, you can run Gate A on the spec + registry entry first, and defer artifact digests until the first controlled pipeline run produces outputs.

---

## Exit criteria

Gate A is **PASS** only if:

- A stable **`dataset_id`** exists and is *consistent* across onboarding metadata.
- A deterministic **`spec_hash`** exists and is reproducible across environments.
- A deterministic **`dataset_version_id`** exists and is derived from the spec_hashing scheme.
- All produced artifacts have **sha256 digests** and verification passes.

---

## Checklist

### A1. Dataset identity (`dataset_id`)

- [ ] **Dataset slug follows conventions** (lowercase, underscore-separated, no dates in slug)
- [ ] **`dataset_id` is stable** (changing `dataset_id` requires a governance decision + redirects/aliases; do not silently rename)
- [ ] **Identifier family conventions** used where applicable (URI-like IDs; do not embed environment-specific hostnames in canonical IDs)

**Evidence to attach (minimum):**
- registry entry (or PR diff) showing `dataset_id`

---

### A2. Canonical spec exists and is hashable

- [ ] A canonical spec document exists for this dataset family and includes (minimum):
  - [ ] upstream acquisition configuration (endpoints, parameters)
  - [ ] normalization rules
  - [ ] validation rules
  - [ ] output artifact plan
  - [ ] policy label intent (proposed label)
  - [ ] expected cadence
- [ ] The spec is represented in a format that can be canonicalized **deterministically**
  - [ ] JSON preferred (RFC 8785 canonical JSON is required for hash stability)
  - [ ] if YAML is used, there is an explicit canonicalization step to stable JSON (documented + tested)

---

### A3. `spec_hash` computation is deterministic

- [ ] `spec_hash` is computed as: `sha256(RFC8785_canonical_json(spec))`
- [ ] The hash includes the algorithm prefix: `sha256:<hex>`
- [ ] **Hashes are not computed over “pretty printed” JSON** (canonicalization is mandatory)
- [ ] The canonical spec used for hashing is stored alongside the computed `spec_hash` (so the hash can be recomputed later)

---

### A4. Hash drift prevention (“golden” stability tests)

- [ ] A *golden test* exists proving `spec_hash` is stable across OS/runtime
- [ ] Recomputing `spec_hash` from the stored canonical spec yields the same value
- [ ] Any `spec_hash` change is reviewed as a potentially breaking change (explain why the spec changed)
- [ ] The spec_hash input does not depend on clocks, random seeds, or nondeterministic ordering

---

### A5. DatasetVersion identity (`dataset_version_id`)

- [ ] A deterministic `dataset_version_id` exists for the candidate release.
- [ ] `dataset_version_id` is immutable: if any output changes, a **new** DatasetVersion is created.
- [ ] The `dataset_version_id` can be *re-derived* from recorded inputs (spec + hashing rules), not manually assigned.

> [!WARNING]
> The exact formatting of `dataset_version_id` (e.g., including cadence like `YYYY-MM` plus a short hash suffix) must be standardized across KFM. If the repo does not yet define the format, treat formatting as **PROPOSED**, but keep the *determinism* requirement as **MUST**.

---

### A6. Artifact digest integrity

For every artifact in the candidate DatasetVersion (GeoParquet/COG/PMTiles/catalog bundles/etc.):

- [ ] `sha256` digest is recorded as `sha256:<hex>`
- [ ] Digest verified against artifact bytes (no mismatch)
- [ ] Media type is recorded (minimum: for distribution + UI surfacing)
- [ ] If an artifact is a JSON bundle that must be stable, prefer producing it deterministically (stable ordering/minification) to avoid noisy diffs

---

## Evidence artifacts

> These are **examples** of evidence artifacts. Adjust filenames/paths to match your repo conventions.

| Artifact | Required | What it proves | Minimum validation |
|---|---:|---|---|
| Dataset registry entry (JSON/YAML) | ✅ | `dataset_id`, `spec_ref`, `spec_hash`, policy intent | schema validation + required keys present |
| Canonical spec file | ✅ | deterministic definition of acquisition + transforms | RFC 8785 canonicalization step + recompute hash |
| `spec_hash` output file (e.g., `spec_hash.txt`) | ✅ | the computed hash value | compare vs recomputation |
| Artifact digest manifest (paths + sha256 + media_type) | ✅ (once artifacts exist) | content-addressed integrity | recompute sha256 of each file and compare |
| (Optional) draft Promotion Manifest | ⛳ | binds DatasetVersion to artifact digests | consistency check (IDs + digests match) |

⛳ = recommended if you already generate a promotion manifest in the pipeline.

---

## Automation hooks

### CI checks (recommended mapping)

- **Spec schema validation** → fail on missing required spec fields
- **`spec_hash` golden tests** → fail if hash drifts across environments
- **Artifact digest verification** → fail if any digest mismatch or missing digest

### Minimal commands (portable)

```bash
# Compute a sha256 digest for a file (portable baseline)
sha256sum path/to/artifact.bin

# (If you have a spec_hash CLI) validate canonicalization + hash
kfm spec hash --spec path/to/spec.json --out spec_hash.txt  # TODO: replace with actual repo command
```

### Policy-as-code (optional)

If you use OPA/Conftest, Gate A can be enforced with deny-by-default rules such as:

- deny if `dataset_id` missing
- deny if `spec_hash` missing or not `sha256:<hex>`
- deny if any artifact digest missing / wrong format

> [!NOTE]
> The specific CI toolchain (Conftest/OPA, bespoke validators, etc.) is an implementation choice. What matters is that the checks are automated and fail closed.

---

## Common failures

| Failure | Symptom | Likely cause | Fix |
|---|---|---|---|
| Hash drift | `spec_hash` changes between machines | non-canonical JSON, YAML ordering, float formatting | enforce RFC 8785 canonical JSON + golden tests |
| Silent spec changes | dataset outputs change “mysteriously” | spec not stored next to hash; no review trigger | store canonical spec; treat spec changes as breaking |
| Digest mismatch | recorded digest doesn’t match bytes | artifact overwritten / non-immutable zone, or wrong file referenced | treat promoted artifacts as immutable; recompute and update manifest |
| Dataset ID rename | UI/citations break; catalogs show duplicates | `dataset_id` changed without redirect/alias | governance decision + explicit alias mapping; avoid renames |

---

## Change log

- **v1 (2026-03-01):** initial Gate A checklist draft (identity, spec_hash determinism, artifact digests).
