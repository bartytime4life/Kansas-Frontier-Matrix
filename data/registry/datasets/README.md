# Dataset Registry (`data/registry/datasets/`)
Canonical dataset onboarding specs (machine-readable) that define what KFM is allowed to ingest, validate, version, and publish.

**Status:** Draft (governed) • **Owners:** Data Stewardship + Platform • **Policy:** public • **Last reviewed:** 2026-02-22  
`fail-closed` `spec-hash` `contract-first` `catalog-triplet`

- [What lives here](#what-lives-here)
- [How it fits the KFM system](#how-it-fits-the-kfm-system)
- [Directory layout](#directory-layout)
- [Dataset identity and naming](#dataset-identity-and-naming)
- [Dataset spec requirements](#dataset-spec-requirements)
- [How to add or change a dataset](#how-to-add-or-change-a-dataset)
- [Governance and promotion gates](#governance-and-promotion-gates)
- [Sensitive / restricted data rules](#sensitive--restricted-data-rules)
- [CI checks recommended for this folder](#ci-checks-recommended-for-this-folder)
- [Appendix](#appendix)

---

## What lives here

This folder is the **allow-list and configuration source of truth** for datasets in KFM.

**This registry should contain:**
- **Canonical dataset onboarding specs** (valid JSON) used to compute `spec_hash` and derive an immutable `dataset_version_id`.
- Optional **human docs** per dataset (notes/runbook), separate from the canonical JSON.
- Small **fixtures + expectations** for CI validation (schema, policy, metadata link checks).

**This registry should not contain:**
- Raw/processed data files (those belong in `data/raw/`, `data/work/`, `data/processed/`, `data/catalog/`).
- Secrets (tokens, credentials, signed URLs).
- “Temporary” specs that haven’t cleared license + sensitivity review.

> NOTE  
> Updating a spec is not a trivial edit: it changes `spec_hash` → produces a new `dataset_version_id` → triggers a new governed release path.

[Back to top](#dataset-registry-dataregistrydatasets)

---

## How it fits the KFM system

```mermaid
flowchart TD
  A[Dataset spec JSON<br/>data/registry/datasets/&lt;dataset_slug&gt;/spec.json] --> B[Canonicalize<br/>RFC8785 JSON]
  B --> C[spec_hash]
  C --> D[dataset_version_id]
  A --> E[Ingest + transform pipeline<br/>raw → work → processed]
  E --> F[run_receipt<br/>inputs/outputs + digests]
  E --> G[Processed artifacts<br/>GeoParquet / PMTiles / COG / …]
  G --> H[Catalog triplet<br/>DCAT + STAC + PROV]
  H --> I[Governed APIs<br/>catalog + evidence resolver]
  I --> J[Map Explorer + Story Nodes + Focus Mode]

  subgraph Promotion gates (fail-closed)
    F
    H
  end
```

Key idea: **the spec in this folder is the canonical contract** that ties together:
- ingestion configuration (upstream endpoints + parameters)
- normalization rules
- validation + schema checks
- output artifact plan (what files are produced and where they land)
- intended sensitivity policy label and obligations

[Back to top](#dataset-registry-dataregistrydatasets)

---

## Directory layout

> This README documents a **recommended** layout inside `data/registry/datasets/`.  
> If your repo uses a different convention, keep the invariants (canonical JSON spec + stable slug + CI validation).

```text
data/registry/datasets/
  README.md

  <dataset_slug>/
    spec.json                 # canonical dataset onboarding spec (valid JSON)
    README.md                 # optional human notes/runbook (NOT used for spec_hash)
    fixtures/                 # optional: small samples for CI (no sensitive data)
    expectations/             # optional: expected checks, link targets, etc.
```

Recommended naming: the directory name **must exactly equal** `dataset_slug` in `spec.json`.

[Back to top](#dataset-registry-dataregistrydatasets)

---

## Dataset identity and naming

### `dataset_slug` rules (summary)
- lowercase
- words separated by underscores
- include upstream authority when helpful
- **do not include a date** in the slug (dates belong in versions)

Examples:
- `usgs_nwis_kansas`
- `noaa_ncei_storm_events`
- `fema_disaster_declarations`

### Version identity (summary)
A dataset version is derived from the canonical spec:
- `spec_hash` = hash of canonicalized JSON
- `dataset_version_id` = immutable identifier derived from `spec_hash` (format defined by the spec-hash library / tooling)

[Back to top](#dataset-registry-dataregistrydatasets)

---

## Dataset spec requirements

The canonical spec:
- MUST be **valid JSON** (preferred)
- MUST be canonicalizable (stable across platforms)
- MUST NOT include credentials/secrets

A minimal spec should include (names are illustrative; use the repo’s schema if present):

```json
{
  "kfm_spec_version": "v1",
  "dataset_slug": "example_dataset_slug",
  "title": "Human-friendly dataset title",

  "upstream": {
    "authority": "Upstream authority name",
    "access_method": "bulk_csv | api | s3 | arcgis_rest | ...",
    "endpoints": [
      {
        "name": "primary",
        "url": "https://example.invalid/endpoint",
        "parameters": {}
      }
    ],
    "cadence": "monthly | weekly | daily | ad_hoc",
    "terms_snapshot": {
      "license": "SPDX id or project-controlled token",
      "retrieved_at": "YYYY-MM-DD"
    }
  },

  "sensitivity": {
    "policy_label_intent": "public | restricted | ...",
    "pii_risk": "low | medium | high",
    "sensitive_location_risk": "low | medium | high",
    "obligations": []
  },

  "normalization": {
    "canonical_fields": {},
    "units": {},
    "crs": "EPSG:4326"
  },

  "validation": {
    "schema": "contracts/schemas/<dataset>.schema.json",
    "checks": [
      { "name": "required_fields_present", "threshold": 0.99 }
    ]
  },

  "outputs": [
    {
      "artifact_type": "geoparquet",
      "path": "data/processed/<dataset_slug>/<dataset_version_id>/data.parquet"
    }
  ]
}
```

**Rules of thumb:**
- Treat this spec as **policy-relevant**: a spec that points at a new endpoint or changes selection parameters can change what KFM collects.
- Put “human narrative” in `README.md` next to `spec.json`, not inside the JSON.
- Keep URLs real in implementation; placeholders (like `example.invalid`) are allowed in templates, not releases.
- If license is unclear: **do not publish** (quarantine until resolved).

[Back to top](#dataset-registry-dataregistrydatasets)

---

## How to add or change a dataset

### 1) Create the dataset directory
```text
data/registry/datasets/<dataset_slug>/
```

### 2) Add the canonical spec (`spec.json`)
Minimum: upstream + terms snapshot + sensitivity intent + validation + outputs.

Checklist:
- [ ] `dataset_slug` matches directory name
- [ ] `terms_snapshot.license` is present and reviewable
- [ ] `terms_snapshot.retrieved_at` is present (YYYY-MM-DD)
- [ ] No credentials embedded in `url` or `parameters`
- [ ] `policy_label_intent` reflects the intended release posture
- [ ] Output paths are versioned with `<dataset_version_id>`

### 3) Add fixtures/expectations (recommended)
Include only small samples suitable for CI.
- fixtures should avoid sensitive data
- expectations should encode what “pass” means (thresholds, required fields, etc.)

### 4) Run local validation (if tooling exists)
Example (adapt to repo tooling):
```bash
# validate JSON syntax + schema
make validate-dataset-spec DATASET=<dataset_slug>

# run policy tests against fixtures
make test-policy DATASET=<dataset_slug>

# run link checks (catalog cross-links, if generated in CI)
make linkcheck DATASET=<dataset_slug>
```

### 5) Open a PR
A “good” dataset PR usually includes:
- dataset spec (this folder)
- schema or contract updates (`contracts/schemas/…`) when needed
- fixture + expectation data for CI
- any required policy fixtures/tests (OPA/Rego) if access rules are non-trivial

[Back to top](#dataset-registry-dataregistrydatasets)

---

## Governance and promotion gates

KFM promotion is intended to be **social + technical**, not ad hoc:
1. Contributor proposes (PR)
2. CI validates (schemas, policy tests, spec_hash stability, link checks)
3. Steward reviews (license + sensitivity + policy label)
4. Operator runs pipeline in controlled environment
5. Outputs land in processed + catalog zones
6. A release/promotion manifest records artifacts + digests

Promotion gates are fail-closed by default. At minimum, ensure:
- identity + versioning are stable
- licensing/rights are explicit
- sensitivity classification exists (and redaction plan if needed)
- catalog triplet is produced and cross-linked
- run receipts include digests and environment info
- policy tests pass with fixtures

[Back to top](#dataset-registry-dataregistrydatasets)

---

## Sensitive / restricted data rules

If a dataset involves:
- precise locations of vulnerable sites
- restricted cultural information
- private individuals
- or any high-risk infrastructure detail

Then:
- default to **restricted** and fail closed until a release decision exists
- consider publishing a **public generalized** derivative instead
- record obligations (e.g., geometry generalization method) and ensure the policy layer enforces them
- ensure Story content and Focus Mode outputs cannot leak restricted existence through errors or side channels

[Back to top](#dataset-registry-dataregistrydatasets)

---

## CI checks recommended for this folder

Recommended automated checks (fail PR if any fail):
- **JSON validity** for all `spec.json`
- **Schema validation** for the dataset spec structure (if a schema exists)
- **Slug consistency**: folder name == `dataset_slug`
- **No secrets**: scan URLs/params for tokens, signed query strings, or common credential patterns
- **Allowed policy labels only** (controlled vocabulary)
- **Output path sanity**: enforce `<dataset_version_id>` usage; forbid writing into unversioned locations
- **spec_hash stability test**: canonicalization produces identical hash across environments
- Optional: ensure referenced files exist (schema paths, contracts paths)

[Back to top](#dataset-registry-dataregistrydatasets)

---

## Appendix

### Related standards and templates (expected elsewhere in repo)
- `docs/standards/KFM_STAC_PROFILE.md`
- `docs/standards/KFM_DCAT_PROFILE.md`
- `docs/standards/KFM_PROV_PROFILE.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`

### Metadata
<details>
<summary>Metadata (KFM MetaBlock v2)</summary>

[KFM_META_BLOCK_V2]
doc_id: kfm://doc/datasets-registry-readme@v1
title: Dataset Registry README
type: guide
version: v1
status: draft
owners: Data Stewardship + Platform
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related:
  - kfm://dataset/
tags:
  - kfm
  - registry
  - datasets
  - governance
notes:
  - Canonical dataset specs here must be valid JSON and treated as governed inputs.
[/KFM_META_BLOCK_V2]

</details>
