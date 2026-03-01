<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/2a083922-112e-47f1-85a3-b2cdaad90e7c
title: Naming Schema
type: standard
version: v1
status: draft
owners: TODO
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - TODO: docs/data/_schemas/index.md
  - TODO: docs/data/_schemas/prov.schema.md
  - TODO: docs/data/_schemas/stac.profile.md
  - TODO: docs/data/_schemas/dcat.profile.md
tags: [kfm, data, schema, naming, identity]
notes:
  - Canonical identifier + path conventions for KFM datasets, versions, runs, and artifacts.
  - Items marked PROPOSED or UNKNOWN must be verified before enforcing as hard CI gates.
[/KFM_META_BLOCK_V2] -->

# Naming Schema
Canonical ID and path rules for **datasets**, **dataset versions**, **runs**, and **artifacts** across the KFM trust membrane.

![status](https://img.shields.io/badge/status-draft-yellow)
![schema](https://img.shields.io/badge/schema-v1-blue)
![policy](https://img.shields.io/badge/policy_label-public-brightgreen)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Where this fits:** `docs/data/_schemas/` — governs naming/identity used by:
- pipeline specs (`spec_hash` → `dataset_version_id`)
- promotion gates (Identity & versioning)
- object-store layout (`data/raw|work|processed|catalog/...`)
- catalog triplet (DCAT/STAC/PROV cross-links)
- evidence resolver + Evidence Drawer

---

## Quick navigation
- [Design intent](#design-intent)
- [Normative language](#normative-language)
- [Identifier families](#identifier-families)
- [Dataset slug](#dataset-slug)
- [DatasetVersion identity](#datasetversion-identity)
- [Run identity](#run-identity)
- [Artifact identity](#artifact-identity)
- [Canonical storage layout](#canonical-storage-layout)
- [Filename and component rules](#filename-and-component-rules)
- [Validation rules](#validation-rules)
- [Appendix: Regex library](#appendix-regex-library)

---

## Design intent
KFM must make identity predictable. The system cannot reliably **cache**, **cite**, or **reproduce** without stable identifiers.

This schema exists to:
1. Make IDs and paths **deterministic** from governed inputs (specs + hashes).
2. Keep the “truth path” navigable **without a database** (manifests/receipts live next to artifacts).
3. Prevent “identity drift” (same spec producing different IDs across machines).

---

## Normative language
This document uses:
- **MUST / MUST NOT** = required for promotion into runtime surfaces
- **SHOULD / SHOULD NOT** = recommended; may become MUST later
- **MAY** = optional

Each rule is labeled:
- **CONFIRMED**: directly supported by current KFM design references
- **PROPOSED**: present as a proposal in KFM references; treat as soft until gated
- **UNKNOWN**: not specified; do not enforce until decided

---

## Identifier families
**Status: CONFIRMED (recommended families)**

KFM uses **URI-like identifiers with stable prefixes**. Canonical IDs **MUST NOT** embed environment-specific hostnames; hostnames belong in distribution URLs.

| Kind | Canonical prefix | Example | Notes |
|---|---|---|---|
| Dataset | `kfm://dataset/` | `kfm://dataset/noaa_ncei_storm_events` | Dataset identity (slug-based) |
| Dataset version reference | `kfm://dataset/<slug>@<dataset_version_id>` | `kfm://dataset/noaa_ncei_storm_events@2026-02.abcd1234` | Used by stories/citations/catalog links |
| Artifact (content-addressed) | `kfm://artifact/sha256:` | `kfm://artifact/sha256:...` | Digest-addressed entity |
| Run | `kfm://run/` | `kfm://run/2026-02-20T12:34:56Z.noaa_ncei_storm_events.abcd1234` | Activity identity |
| Evidence | `kfm://evidence/` | `kfm://evidence/...` | **UNKNOWN** format; see below |
| Story | `kfm://story/` | `kfm://story/<uuid>@v1` | Story Node IDs |

### Evidence IDs
**Status: UNKNOWN**

This doc does **not** define the EvidenceRef/EvidenceBundle URI format (only the prefix family).
- **Fail closed**: if an EvidenceRef cannot be resolved, publishing/promotion should be blocked by policy gates.

---

## Dataset slug
**Status: PROPOSED (slug conventions)**

### Rules
A `dataset_slug`:
- MUST be **lowercase**
- MUST separate words with **underscore (`_`)**
- SHOULD include upstream authority when helpful
- MUST NOT include a date (dates belong in `dataset_version_id`)

### Examples
- `usgs_nwis_kansas`
- `noaa_ncei_storm_events`
- `fema_disaster_declarations`
- `ipums_nhgis_county_time_series`

### Schema (v1)
- **Recommended regex (PROPOSED v1):**
  - `^[a-z][a-z0-9_]{2,62}$`
- **Additional constraints (PROPOSED):**
  - no double underscores (`__`)
  - no trailing underscore
  - keep under 64 chars unless a governance exception exists

---

## DatasetVersion identity
**Status: MIXED**
- spec hashing rule: **CONFIRMED pattern**
- exact `dataset_version_id` *string format*: **PROPOSED** (inferred from examples)

### spec_hash
A `DatasetVersion` is derived from a **canonical specification** (endpoints, normalization, validation, output plan, policy intent, cadence).

Compute:
- `spec_hash = sha256( RFC8785_canonical_json(spec) )`

**Hash drift prevention** (operational rules):
- Store the canonical spec used for hashing next to the computed `spec_hash`.
- Unit-test that recomputing `spec_hash` yields the same value.
- Never compute hashes from pretty-printed JSON; always canonicalize.

### dataset_version_id
The references show examples such as:
- `2026-02.abcd1234`

**PROPOSED v1 format (matches current examples):**
- `dataset_version_id = <YYYY-MM>.<sha8(spec_hash)>`

Rationale:
- `<YYYY-MM>` is aligned to cadence/release window.
- `sha8(spec_hash)` provides human-usable short identity while the full `spec_hash` remains the cryptographic anchor.

**Risk/tradeoff:** `sha8` is shorter than a full hash; collision risk is low but non-zero. The system MUST still store and validate the **full** `spec_hash` wherever identity matters (promotion manifest, receipts, PROV).

---

## Run identity
**Status: CONFIRMED (run receipt exists); run_id format: PROPOSED (pattern from examples)**

A run receipt is emitted for **every pipeline run and Focus Mode query**.

### run_id
Examples show:
- `kfm://run/2026-02-20T12:34:56Z.noaa_ncei_storm_events.abcd1234`

**PROPOSED v1 format:**
- `run_id = kfm://run/<RFC3339_UTC>.<dataset_slug>.<sha8(spec_hash)>`

Rules:
- timestamp MUST be UTC and end with `Z`
- separators MUST be `.` between components
- no spaces; ASCII only

---

## Artifact identity
**Status: CONFIRMED (family) + PROPOSED (policy details)**

### artifact_id
Artifacts are digest-addressed:
- `artifact_id = kfm://artifact/sha256:<hex_digest>`

**PROPOSED policy:**
- sha256 is mandatory for artifacts and bundles
- keep algorithm in the ID (`sha256:`) to support future migration

### artifact paths
An artifact’s **path** is not its canonical identity; the canonical identity is its digest-based `artifact_id`.
However, KFM storage paths MUST be predictable and must correspond to a promoted dataset version.

---

## Canonical storage layout
**Status: PROPOSED (canonical layout) + CONFIRMED (runtime eligibility rules)**

**Canonical path convention (PROPOSED):**
```text
data/
  raw/
    <dataset_slug>/
      <acquisition_id>/
        manifest.json
        artifacts/
          ...
  work/
    <dataset_slug>/
      <work_run_id>/
        ...
  processed/
    <dataset_slug>/
      <dataset_version_id>/
        artifacts/
          <artifact_name>.<ext>
        checksums.json
        qa/
          validation_report.json
  catalog/
    <dataset_slug>/
      <dataset_version_id>/
        dcat.jsonld
        stac/
          collection.json
          items/
            <item_id>.json
        prov/
          bundle.jsonld
        receipts/
          run_receipt.json
```

**Rules (CONFIRMED from references):**
- Only **processed** and **catalog** artifacts are eligible for serving to runtime.
- Every artifact has a digest and appears in `checksums.json`.
- Keep manifests and receipts close to artifacts so the truth path is navigable without a database.

> NOTE: Some example receipts show `data/processed/<slug>/<dataset_version_id>/<artifact>` without the `artifacts/` subfolder. Treat `artifacts/` as the canonical layout and align templates/validators before enforcing.

---

## Filename and component rules
**Status: PROPOSED (v1 hardening)**

### Allowed characters for “path components”
For any component used in a filesystem/object-store path (`dataset_slug`, `dataset_version_id`, `artifact_name`, etc):
- MUST be ASCII
- MUST NOT include spaces
- SHOULD restrict to: `a-z`, `0-9`, `_`, `-`, `.`
- MUST NOT include `/` or `\`
- SHOULD NOT include secrets, credentials, or sensitive-location specifics

### artifact_name
**PROPOSED v1:**
- snake_case or lower-kebab-case
- Examples:
  - `events.parquet`
  - `events.pmtiles`
  - `dcat.jsonld`
  - `bundle.jsonld`
  - `run_receipt.json`

### acquisition_id and work_run_id
**Status: UNKNOWN**

The canonical layout references these IDs but does not specify format.
Until decided:
- treat as opaque strings that MUST pass the path component rules above
- do not enforce structure beyond safe characters + length limits

**PROPOSED candidates (choose one via ADR):**
1) `acquisition_id = <RFC3339_UTC>.<sha8(source_fingerprint)>`
2) `acquisition_id = <YYYY-MM-DD>.<source_release_tag>`
3) `work_run_id = <run_id without scheme>` (URL-safe)

---

## Validation rules
This schema is intended to be enforced by CI gates and validators.

### Gate alignment
**Status: CONFIRMED (gate intent)**  
Promotion must fail-closed unless identity & versioning rules are satisfied.

Minimum checks:
- [ ] Dataset ID is stable and follows naming convention.
- [ ] DatasetVersion ID is immutable and derived from stable `spec_hash`.
- [ ] Run receipt exists for producing runs and includes dataset_slug + dataset_version_id + digests.
- [ ] Processed artifacts exist at predictable paths and are digested.
- [ ] Catalog triplet (DCAT/STAC/PROV) references resolvable IDs and cross-links.

### Suggested enforcement tiers
**Tier 0 (lint-only):**
- validate regex for dataset_slug
- validate canonical prefixes for IDs

**Tier 1 (promotion blocking):**
- enforce `spec_hash` deterministic recomputation (hash drift test)
- enforce `dataset_version_id` pattern
- enforce `artifact_id` digest format
- enforce canonical layout paths for processed + catalog outputs

**Tier 2 (runtime hardening):**
- enforce `checksums.json` completeness
- enforce “no hostnames in canonical IDs”
- enforce EvidenceRef resolvability gates for publish workflows

---

## Appendix: Regex library
> These are **PROPOSED v1** regexes unless marked otherwise.

```text
dataset_slug:
  ^[a-z][a-z0-9_]{2,62}$

spec_hash (sha256):
  ^sha256:[a-f0-9]{64}$

dataset_version_id (example-aligned):
  ^\d{4}-\d{2}\.[a-f0-9]{8}$

dataset_id:
  ^kfm://dataset/[a-z][a-z0-9_]{2,62}$

dataset_ref (dataset version reference):
  ^kfm://dataset/[a-z][a-z0-9_]{2,62}@\d{4}-\d{2}\.[a-f0-9]{8}$

artifact_id:
  ^kfm://artifact/sha256:[a-f0-9]{64}$

run_id (example-aligned):
  ^kfm://run/\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\.[a-z][a-z0-9_]{2,62}\.[a-f0-9]{8}$
```

---

## Open items
- [ ] Define EvidenceRef/EvidenceBundle canonical URI patterns (currently UNKNOWN).
- [ ] Decide `acquisition_id` and `work_run_id` formats (currently UNKNOWN).
- [ ] Confirm the authoritative `dataset_version_id` formula text from design references (examples strongly imply `YYYY-MM.sha8(spec_hash)`).
- [ ] Implement validators + CI gates (Conftest/OPA or equivalent) that enforce Tier 1 before promotion.
