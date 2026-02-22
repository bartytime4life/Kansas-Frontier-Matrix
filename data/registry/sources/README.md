# Sources Registry
Machine-readable inventory of upstream data sources used by Kansas Frontier Matrix (KFM).

**Status:** DRAFT (vNext) • **Owners:** TBD (Data Stewardship / Governance) • **Scope:** `data/registry/sources/`

![status](https://img.shields.io/badge/status-draft-lightgrey)
![registry](https://img.shields.io/badge/registry-sources-blue)
![governance](https://img.shields.io/badge/governance-fail--closed-critical)
![metadata](https://img.shields.io/badge/metadata-machine--readable-success)

---

## Navigation
- [Why this exists](#why-this-exists)
- [What belongs in the sources registry](#what-belongs-in-the-sources-registry)
- [Required fields](#required-fields)
- [Recommended fields](#recommended-fields)
- [Controlled vocabularies](#controlled-vocabularies)
- [Folder contents](#folder-contents)
- [How the registry is used](#how-the-registry-is-used)
- [Add or update a source](#add-or-update-a-source)
- [Validation and gates](#validation-and-gates)
- [References](#references)

---

## Why this exists

The Sources Registry is the **authoritative, machine-readable** inventory of *upstream sources* (agencies, archives, portals, APIs, bulk dumps, etc.) that feed KFM datasets.

A source entry is not “just documentation” — it is an **input to governance and promotion gates** (license, sensitivity, access constraints, and QA expectations must be explicit).

> [!IMPORTANT]
> If a source is used by a dataset, it **must** have a registry entry with stable identity, rights/terms, sensitivity intent, and a minimal QA plan. If any of those are unknown, treat the source as **not promotable** until resolved.

[Back to top](#sources-registry)

---

## What belongs in the sources registry

A **source** in KFM is the upstream authority + access channel(s) from which KFM acquires data, such as:
- Federal/state/local agencies (public domain or governed terms)
- University/academic distributions (often attribution/terms)
- Archives and media repositories (rights-sensitive)
- Partner datasets (restricted/embargoed)
- Portals providing WMS/WFS/tiles (access controls vary)
- Manual ingest sources (e.g., digitized scans, curated CSVs)

A source entry describes *how KFM is allowed to use it* and *how KFM will acquire and validate it*.

A source entry is referenced by:
- dataset specs / pipeline blueprints
- acquisition connectors
- promotion PRs and run receipts
- catalog records (DCAT / STAC / PROV)

[Back to top](#sources-registry)

---

## Required fields

Every source entry MUST include, at minimum:

| Field | Type | Meaning | Notes |
|---|---:|---|---|
| `source_id` | string | **Stable** unique identifier | Stable across time; do not encode versions |
| `name` | string | Human-friendly name | Display name for UI + docs |
| `authority` | string | Owning org / authoritative publisher | E.g., “USGS”, “NOAA NCEI” |
| `domain` | string | High-level domain category | Use controlled vocab (see below) |
| `access_method` | string | How data is obtained | e.g., `api`, `bulk`, `portal`, `manual`, `scrape` |
| `cadence` | string | Expected update cadence | e.g., `daily`, `monthly`, `annual`, `occasional` |
| `license_rights` | string | Rights summary | e.g., `public_domain`, `CC-BY-4.0`, “NHGIS terms” |
| `terms_snapshot` | object | Evidence of rights/terms at a point in time | Path/URI + digest (no secrets) |
| `sensitivity` | string | Intended policy label | Use controlled vocab (see below) |
| `connector` | object | Connector spec reference | `type` + reference (path/URI); may be `none` |
| `credentials_strategy` | string | How auth is handled (if any) | Never store secrets here |
| `qa_checks` | array[string] | Known checks/expectations | Keep short, testable, and source-specific |
| `notes` | string | Limitations, caveats, quirks | “Known limitations” lives here |

### Minimal entry template (YAML)
~~~yaml
source_id: example_source_id
name: Example Source Display Name
authority: Example Authority
domain: history
access_method: api
cadence: monthly
license_rights: public_domain
terms_snapshot:
  kind: doc
  ref: evidence/terms/example_source_id/2026-01-15.pdf
  digest: sha256:REPLACE_ME
sensitivity: public
connector:
  type: spec
  ref: connectors/example_source_id.md
credentials_strategy: none
qa_checks:
  - validate_expected_fields_present
  - validate_spatial_bounds
notes: >
  Short, factual notes about limitations and any special handling.
~~~

> [!NOTE]
> The template uses YAML for readability, but the registry may be stored as JSON/YAML/CSV. The **required fields and semantics stay the same**.

[Back to top](#sources-registry)

---

## Recommended fields

These are strongly recommended because they improve auditability and reduce rework:

| Field | Type | Why it helps |
|---|---:|---|
| `homepage` | string | Canonical landing page for human review |
| `access` | object | URLs/endpoints, query limits, portal links (no credentials) |
| `coverage` | object | Approx spatial/temporal coverage (use coarse/public-safe extents) |
| `formats` | array[string] | Typical formats (CSV, GeoJSON, COG, WMS/WFS, etc.) |
| `attribution` | string | Required attribution string (if any) |
| `license_id` | string | SPDX where applicable (e.g., `CC-BY-4.0`) |
| `generalization_plan` | string | Required when sensitivity is not fully public |
| `governance_triggers` | array[string] | Conditions that require steward review (rights unclear, sensitive locations, PII risk, etc.) |

> [!WARNING]
> For culturally restricted sites, private individuals, or sensitive infrastructure: do not publish precise locations in public outputs. Use generalized derivatives and document the plan in the registry.

[Back to top](#sources-registry)

---

## Controlled vocabularies

### `access_method`
Allowed values (baseline):
- `api`
- `bulk`
- `portal`
- `manual`
- `scrape`

If you need a subtype (e.g., `bulk_csv`, `wms`, `wfs`), prefer:
- `access_method: portal` + `access.variant: wms`
- or record details under `access` rather than creating ad-hoc new enums.

### `sensitivity` (policy label intent)
Starter policy labels:
- `public`
- `public_generalized`
- `restricted`
- `restricted_sensitive_location`
- `internal`
- `embargoed`
- `quarantine`

> [!IMPORTANT]
> Sensitivity is a *governance contract*. If unsure, choose the more restrictive label and flag for review.

### `domain`
Baseline starter domains:
- `history`
- `science`
- `basemap`
- `admin`

You may add more specific domain values only if they are adopted consistently across the registry and validated by your controlled-vocabulary process.

[Back to top](#sources-registry)

---

## Folder contents

This folder should contain:
- `README.md` (this file)
- One or more machine-readable registries (JSON/YAML/CSV), for example:
  - `sources.yaml` (recommended)
  - `sources.csv` (acceptable for spreadsheet workflows)
- Optional supporting materials:
  - `connectors/` (connector specs per source; no secrets)
  - `evidence/terms/` (license/terms snapshots and digests)
  - `schemas/` (JSON Schema for validation, if implemented)

Example (recommended) layout:
~~~
data/registry/sources/
  README.md
  sources.yaml
  connectors/
    noaa_ncei_storm_events.md
    usgs_waterdata_nwis.md
  evidence/
    terms/
      noaa_ncei_storm_events/
        2026-01-15.pdf
        2026-01-15.pdf.sha256
~~~

> [!NOTE]
> If your repo stores evidence and connector specs elsewhere, keep only stable references here (paths/URIs + digests).

[Back to top](#sources-registry)

---

## How the registry is used

~~~mermaid
flowchart TD
  A[Source Registry Entry<br/>source_id + rights + sensitivity + access + QA] --> B[Dataset Spec / Pipeline Blueprint]
  B --> C[Acquisition Connector]
  C --> D[RAW zone artifacts<br/>immutable, content-addressed]
  D --> E[WORK/QUARANTINE transforms<br/>fail-closed validation]
  E --> F[PROCESSED artifacts<br/>publishable derivatives]
  F --> G[Catalog triplet<br/>DCAT + STAC + PROV]
  G --> H[Promotion gates<br/>license + sensitivity + QA + provenance]
  H --> I[PUBLISHED runtime<br/>governed API + UI + Focus Mode]
~~~

Key behavior:
- **License-first:** unknown/unclear rights block promotion.
- **Fail closed:** missing sensitivity, missing terms snapshot, or missing QA expectations should prevent publishing.
- **Auditability:** source entries provide the policy intent that must match what is emitted in catalogs, run receipts, and API policy decisions.

[Back to top](#sources-registry)

---

## Add or update a source

1. **Create or update** the registry entry (machine-readable).
2. **Capture rights/terms**:
   - record `license_rights`
   - add/update `terms_snapshot` (doc + digest)
3. **Set sensitivity** (policy intent) and document any generalization plan if not fully public.
4. **Define acquisition approach**:
   - `access_method`
   - `connector` reference (spec)
   - `credentials_strategy` (no secrets)
5. **Write QA expectations** as short, testable `qa_checks`.
6. Open a PR that:
   - includes the registry change
   - references the dataset(s) affected
   - includes any required governance review notes

### Definition of Done (source entry)
- [ ] `source_id` is stable and unique
- [ ] rights/terms are captured (`license_rights` + `terms_snapshot`)
- [ ] sensitivity label is set
- [ ] connector reference exists (or explicitly `none`)
- [ ] QA checks are listed and actionable
- [ ] notes include known limitations and any special handling

[Back to top](#sources-registry)

---

## Validation and gates

Recommended automated validations (CI / pre-commit):
- **Schema validation**: required fields present; types correct
- **Controlled vocab validation**: `access_method`, `sensitivity`, and `domain` values allowed
- **Terms snapshot validation**: snapshot exists and digest matches
- **No secrets**: reject inline API keys/tokens/passwords in registry files
- **Reference integrity**: `connector.ref` paths resolve (or external URIs are reachable in CI)

> [!TIP]
> Keep validation rules strict and additive. If a source is incomplete, classify as `quarantine` and block promotion.

[Back to top](#sources-registry)

---

## References

This registry is aligned to the KFM vNext governance expectations for:
- Source selection rubric
- Required source registry entries
- Controlled vocabularies (policy labels)
- Promotion gates (license, sensitivity, provenance)

(See the KFM governance guide for normative definitions and the starter “Data source registry” appendix.)
