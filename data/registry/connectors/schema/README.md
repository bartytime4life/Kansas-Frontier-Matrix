# Connector Registry Schemas

`status: draft` `layer: integration` `governance: fail-closed` `format: JSON Schema`

This directory defines the **schema contracts** for KFM’s **connector registry** entries: the machine-validated configuration + metadata that tells the platform **how to acquire external data safely** (license-first, deterministic, provenance-ready) and how to route it into the Raw → Work → Processed promotion workflow.

The intent is to make adding a new upstream source mostly a matter of:
1) implementing a connector adapter, and  
2) registering it with a schema-valid config entry — **without** reinventing governance each time.

---

## What is a “connector registry entry”?

A connector registry entry is a declarative record that answers (at minimum):

- **What** upstream source we talk to (provider, dataset family, upstream IDs)
- **How** we access it (auth mode, rate limits, incremental cursor vs snapshot+diff)
- **What** we expect to pull (formats, spatial/temporal scope, backfill strategy)
- **How** we must govern it (license, attribution, sensitivity/policy label, redaction expectations)
- **What** contract it must satisfy downstream (dataset-family pipeline contract pointer; QA gates)

> **Trust membrane reminder:** Connectors run server-side (pipeline/control plane). Frontends and external clients **never** talk directly to upstreams or databases; all access remains behind the governed API + policy boundary.

---

## Scope and non-goals

### In scope ✅
- JSON Schema definitions used to validate connector registry files (YAML/JSON).
- Normalized field names, required governance fields, and versioning rules.
- CI-ready validation expectations (fail-closed).

### Out of scope ❌
- Dataset-family specific *mapping schemas* (those live with the dataset family contract, e.g., `schemas/` under that dataset’s pipeline blueprint).
- Receipts / validation reports / evidence reference schemas (these belong in their own registry areas, even though connectors must emit them).

---

## Directory layout

> This README is a scaffold. If the schema files below do not exist yet, treat them as the **target** layout.

```text
data/
└─ registry/
   └─ connectors/
      ├─ README.md                      # (recommended) overview for connector registry
      ├─ connectors.{yml,json}          # registry entries (one file or many)
      └─ schema/
         ├─ README.md                   # you are here
         ├─ connector.schema.json       # schema for a single connector entry
         ├─ registry.schema.json        # schema for the whole registry collection
         ├─ auth.schema.json            # shared auth block (none/apiKey/oauth/etc.)
         ├─ rate-limit.schema.json      # shared rate-limiting block
         ├─ backfill.schema.json        # shared backfill block
         ├─ policy-label.schema.json    # shared policy/sensitivity labeling
         └─ examples/
            ├─ connector.public.api.yaml
            └─ connector.restricted.file.yaml
```

---

## Schema versioning and compatibility

Every connector entry MUST declare:

- `schema_version`: Schema version used to validate this entry (e.g., `"1.0.0"`).
- `connector_id`: Stable, URL-safe ID (kebab-case recommended). Never re-used for a different upstream.

### Compatibility rules
- **Patch changes**: documentation fixes, clarifications, optional fields — no breaking changes.
- **Minor changes**: additive required-by-policy fields *with defaults* and migration notes.
- **Major changes**: breaking changes (renames, required field changes without defaults). Must ship:
  - a migration script or clear upgrade steps
  - dual-validate window (old + new) if feasible
  - updated golden fixtures

---

## Canonical connector record fields

Below is the **minimum recommended** field set. Your schema may extend this, but avoid source-specific one-offs; prefer generic extension blocks (`extensions.*`) with documented semantics.

### Identity and ownership

| Field | Type | Required | Notes |
|---|---:|:---:|---|
| `schema_version` | string | ✅ | SemVer string for schema selection. |
| `connector_id` | string | ✅ | Stable ID. Used in logs, receipts, and provenance. |
| `display_name` | string | ✅ | Human-readable name. |
| `owner` | object | ✅ | Responsible team/person role (not necessarily PII). |
| `tags` | array | ⬜ | Discovery tags (domain, modality: tabular/vector/raster/text). |

### Upstream source and access

| Field | Type | Required | Notes |
|---|---:|:---:|---|
| `source.provider` | string | ✅ | e.g., “USDA”, “USGS”, “Library of Congress”. |
| `source.upstream_id` | string | ⬜ | Provider dataset ID if applicable. |
| `access.kind` | string | ✅ | `api` \| `file` \| `scrape` \| `stac` \| `manual`. |
| `access.auth` | object | ✅ | Validated by `auth.schema.json`. Secrets never committed. |
| `access.rate_limit` | object | ⬜ | Validated by `rate-limit.schema.json`. |
| `access.terms_url` | string | ✅ | Where the license/terms were verified. |

### Acquisition behavior

| Field | Type | Required | Notes |
|---|---:|:---:|---|
| `schedule` | string | ✅ | Cron or named cadence (“annual”, “weekly”). |
| `incremental.mode` | string | ✅ | `incremental` \| `snapshot-diff`. |
| `incremental.cursor_field` | string | ⬜ | Required for incremental mode. |
| `formats.targets` | array | ✅ | e.g., `["csv","parquet","geojson","cog","pdf"]`. |
| `backfill` | object | ⬜ | Validated by `backfill.schema.json`. |

### Governance and policy

| Field | Type | Required | Notes |
|---|---:|:---:|---|
| `governance.license` | string | ✅ | SPDX when possible; otherwise descriptive + link. |
| `governance.attribution` | string | ✅ | Required attribution text or template. |
| `governance.policy_label` | string | ✅ | `public` \| `restricted` \| `sensitive-location` (extend only with review). |
| `governance.redaction_required` | boolean | ✅ | If `true`, promotion must prove redaction applied. |
| `governance.authority_notes` | string | ⬜ | “golden source” boundary notes. |

### Downstream contract pointers

| Field | Type | Required | Notes |
|---|---:|:---:|---|
| `dataset_family_id` | string | ✅ | Links connector to dataset-family contract. |
| `pipeline_contract_ref` | object | ✅ | Where to find the dataset’s `pipeline.yaml` and companion folders. |
| `qa_profile_ref` | object | ⬜ | Optional, if QA is shared across multiple datasets. |

---

## Validation and CI expectations

Connector registry validation should run in CI as a **merge-blocking gate**:

- Validate all connector entries against `connector.schema.json` (and `registry.schema.json` if used).
- Enforce **required governance fields** (license + attribution + policy label).
- Enforce deterministic, reviewable config changes:
  - stable ordering/canonicalization before hashing (where hashing is used)
  - no secrets committed (pattern checks)

### Suggested CI job shape (pseudo)

```yaml
# .github/workflows/ci.yml (illustrative)
jobs:
  validate-connectors:
    steps:
      - run: ./scripts/validate-connectors.sh
      - run: ./scripts/lint-registry.sh
      - run: ./scripts/policy-regression-tests.sh
```

---

## Example connector entry (YAML)

```yaml
schema_version: "1.0.0"
connector_id: "usda-nass-quickstats"
display_name: "USDA NASS QuickStats"
owner:
  team: "data-platform"
  contact: "governance@kfm.local"
source:
  provider: "USDA"
  upstream_id: "quickstats"
access:
  kind: "api"
  auth:
    type: "none"
  rate_limit:
    policy: "respect-upstream"
  terms_url: "https://example.org/terms"
schedule: "annual"
incremental:
  mode: "snapshot-diff"
formats:
  targets: ["json", "csv", "parquet"]
backfill:
  strategy: "range"
  start: "1950-01-01"
  end: "2025-12-31"
governance:
  license: "CC0-1.0"
  attribution: "USDA NASS QuickStats"
  policy_label: "public"
  redaction_required: false
dataset_family_id: "ag-statistics"
pipeline_contract_ref:
  path: "data/contracts/ag-statistics/pipeline.yaml"
  version_policy: "raw-immutable-processed-versioned"
```

---

## Definition of Done for adding a new connector

Use this checklist in PRs that add or change connector registry entries:

- [ ] Connector adapter implemented (integration layer) and **registered** in the connector registry.
- [ ] Raw acquisition emits a deterministic manifest + checksums (content-addressed where applicable).
- [ ] Normalization produces canonical encodings (UTF-8, WGS84 where applicable, ISO 8601 time).
- [ ] Validation gates implemented (schema, geo validity, temporal sanity, license/policy checks).
- [ ] Policy label set and (if needed) redaction rules proven via regression tests.
- [ ] Catalog outputs updated (DCAT always; STAC/PROV when applicable) and link-check clean.
- [ ] At least one integration test run against a fixed small slice with stable checksums + counts.
- [ ] Backfill strategy documented (coverage range + batching + expected runtimes).

---

## Governance escalation

If you need a new `policy_label` value or a connector that touches sensitive locations:

1) open a governance review ticket,  
2) document the rationale and mitigation, and  
3) add policy regression tests before promotion.

Fail closed by default.