<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/2e4c5d7d-6e91-4a4c-bf3e-bf6f5fa5a8d6
title: Data Registry
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related:
  - data/registry/README.md
tags:
  - kfm
  - data
  - registry
notes:
  - Defines the contract for dataset/source registry entries and how they relate to catalogs, provenance, and promotion gates.
[/KFM_META_BLOCK_V2] -->

# Data Registry
Purpose: **Machine-readable “source registry” entries that drive governed dataset onboarding** (identity → pipelines → catalogs/provenance → governed runtime access).

![status](https://img.shields.io/badge/status-draft-yellow)
![policy](https://img.shields.io/badge/policy-public-blue)
![contract](https://img.shields.io/badge/contract-registry%20surface-informational)

---

## Quick navigation
- [What lives here](#what-lives-here)
- [How it fits the KFM truth path](#how-it-fits-the-kfm-truth-path)
- [Directory layout](#directory-layout)
- [Registry entry contract](#registry-entry-contract)
- [Controlled vocabularies](#controlled-vocabularies)
- [Identity, spec hashing, and DatasetVersion](#identity-spec-hashing-and-datasetversion)
- [Promotion gates checklist](#promotion-gates-checklist)
- [PR workflow for adding a dataset](#pr-workflow-for-adding-a-dataset)
- [Definition of Done](#definition-of-done)
- [Security and governance notes](#security-and-governance-notes)

---

## What lives here

This directory is the **registry of datasets/sources** that KFM knows about.

It is **not**:
- a data lake
- a place to store raw downloads
- a runtime database

It **is**:
- a **reviewable contract surface** for onboarding datasets (licensing + policy label + provenance requirements)
- the **anchor** that connects:
  - dataset identity (`kfm://dataset/...`)
  - pipeline specification (the thing that gets hashed into a DatasetVersion)
  - catalog/provenance links (DCAT/STAC/PROV)
  - human stewardship (who reviewed/approved, what obligations apply)

> Guiding principle: if it can’t be reviewed in a PR and validated in CI, it shouldn’t be considered “promoted.”

---

## How it fits the KFM truth path

Registry entries sit “above” the lifecycle zones. They describe **what** we are integrating and **under what governance**, while the pipeline run produces the actual artifacts.

```mermaid
flowchart LR
  R[data/registry<br/>source registry entry] --> S[Pipeline spec<br/>(canonical JSON)]
  S --> H[spec_hash<br/>DatasetVersion ID]
  S -->|run| A[Artifacts<br/>raw/work/processed]
  A --> C[Catalog triplet<br/>DCAT + STAC + PROV]
  C --> E[Evidence resolver<br/>EvidenceRef → EvidenceBundle]
  E --> UI[Map/Story UI<br/>+ Focus Mode]

  UI -. trust membrane .-> E
```

**Key invariants**
- **Catalogs + provenance are the canonical interface between pipeline outputs and runtime.**
- Runtime access should be mediated by governed APIs and policy enforcement, not direct storage access.

---

## Directory layout

> NOTE: This README defines the **intended** structure. If some folders don’t exist yet, create them as you implement onboarding.

```text
data/registry/
├─ README.md                 # (this file) registry contract + workflow
├─ datasets/                 # one file per dataset/source ("source registry entry")
│  ├─ <dataset_slug>.yml
│  └─ ...
├─ vocab/                    # controlled vocabularies used by registry + catalogs
│  ├─ policy_label.yml
│  ├─ theme.yml
│  └─ citation_kind.yml
├─ schemas/                  # JSON Schema (or equivalent) to validate registry entries
│  ├─ dataset_entry.schema.json
│  └─ ...
└─ fixtures/                 # tiny samples used for CI policy/tests (optional but recommended)
   ├─ <dataset_slug>/
   └─ ...
```

### Why “one file per dataset”?
- Small diffs, reviewable history, easy ownership.
- Enables deterministic spec hashing and “fail closed” review gates.

---

## Registry entry contract

### File naming
- `datasets/<dataset_slug>.yml`
- `dataset_slug` should be **stable**, lowercase, underscore-separated.
- Do **not** embed dates in `dataset_slug` (dates belong to versions / runs).

### Minimum fields (registry entry)
Below is a pragmatic **minimum** registry contract. Treat these as **required for onboarding PRs**.

| Field | Required | Meaning |
|---|---:|---|
| `dataset_slug` | ✅ | Stable short name used in paths |
| `dataset_id` | ✅ | Stable ID (recommended: `kfm://dataset/<slug>`) |
| `title` | ✅ | Human-friendly name |
| `description` | ✅ | What it is, what it’s used for |
| `publisher` | ✅ | Organization publishing the dataset |
| `license` or `rights` | ✅ | Explicit license or rights statement |
| `rights_holder` | ✅ | Who owns/controls rights |
| `attribution` | ✅ | Required attribution text (if any) |
| `policy_label` | ✅ | Access + sensitivity classification |
| `upstream` | ✅ | Where it comes from (URLs, APIs, archives) |
| `expected_cadence` | ✅ | How often updates are expected |
| `spatial_coverage` | ✅ | Narrative + optional bbox or admin unit list |
| `temporal_coverage` | ✅ | Narrative + optional time bounds |
| `contacts` | ✅ | Steward / maintainer contact(s) |
| `pipeline_spec` | ✅ | Path to the canonical pipeline spec that will be hashed |
| `catalog_links` | ⛳ | Where the DCAT/STAC/PROV records will be written after promotion |
| `notes` | ⛳ | Anything reviewers should know |
| `governance` | ⛳ | Partner agreements, special handling, redaction obligations |

⛳ = recommended but may start as optional while the system is being built

---

## Controlled vocabularies

Registry entries should refer only to **controlled vocab values** so that governance is testable.

### Required vocab sets
- `policy_label` (access + sensitivity)
- `artifact.zone` (data lifecycle)
- `citation.kind` (evidence types)
- optionally: `theme` (DCAT theme / category)

Keep these in `data/registry/vocab/` so changes are code-reviewed and versioned.

---

## Identity, spec hashing, and DatasetVersion

KFM relies on **deterministic identity** so artifacts can be cited, cached, audited, and rebuilt.

### Identifier families (recommended)
Use explicit URI-like IDs, e.g.:
- `kfm://dataset/<dataset_slug>`
- `kfm://dataset/@<dataset_version_id>`
- `kfm://artifact/sha256:<digest>`
- `kfm://run/<run_id>`
- `kfm://evidence/<bundle_digest>`

**Avoid embedding environment-specific hostnames** in canonical IDs (hostnames belong in distribution URLs).

### DatasetVersion identity via `spec_hash`
A DatasetVersion should be derived from a **canonical specification document**, then:

- `spec_hash = sha256( RFC8785_canonical_json(spec) )`
- `dataset_version_id` is derived from / incorporates `spec_hash` (implementation-specific)

**Hash drift prevention (non-negotiable)**
- Store the canonical spec used for hashing next to the computed `spec_hash`.
- Unit test that recomputing `spec_hash` yields the same value.
- Never hash “pretty printed” JSON or non-deterministic structures.

---

## Promotion gates checklist

A dataset should not be “promoted” (servable to runtime) until it passes minimum gates.

| Gate | Name | What it blocks |
|---|---|---|
| A | Identity & versioning | prevents unstable dataset/version identity |
| B | Licensing & rights | prevents use when rights are unclear |
| C | Sensitivity & redaction plan | prevents accidental exposure of sensitive data |
| D | Catalog triplet validation | prevents unverifiable runtime use |
| E | Run receipt & checksums | prevents non-reproducible builds |
| F | Policy + contract tests | prevents bypassing governance/evidence resolution |
| G | Optional production posture | strengthens supply chain, perf, a11y, etc. |

---

## PR workflow for adding a dataset

A practical PR-based workflow (high level):

1. Contributor opens PR adding:
   - **source registry entry** (this directory)
   - pipeline spec (hashed into DatasetVersion)
   - fixture sample + expected outputs (small)
2. CI runs:
   - schema validation
   - policy tests
   - `spec_hash` stability test
   - catalog cross-link check (when catalogs exist)
3. Steward review:
   - licensing and sensitivity
   - approve `policy_label`
4. Operator runs pipeline in controlled environment.
5. Outputs are written to processed + catalogs.
6. Release manifest is created and tagged.

---

## Definition of Done

### DoD for a registry entry PR
- [ ] `datasets/<slug>.yml` validates against schema
- [ ] License/rights are explicit (no “unknown” for anything other than quarantine)
- [ ] `policy_label` is set and consistent with handling plan
- [ ] `pipeline_spec` exists and is hashable (canonical)
- [ ] Fixture sample exists (if required by CI policy)
- [ ] Steward approval recorded (method TBD)

### DoD for a dataset integration (end-to-end)
- [ ] Raw acquisition is reproducible and documented
- [ ] Work transforms are deterministic
- [ ] Processed artifacts exist in approved formats and are digest-addressed
- [ ] Catalog triplet validates and is cross-linked
- [ ] EvidenceRefs resolve and render in the evidence UI
- [ ] `policy_label` assigned with documented review
- [ ] Changelog entry explains what changed and why

---

## Security and governance notes

- If rights are unclear, **fail closed**: keep dataset in `quarantine`.
- For sensitive-location or restricted datasets:
  - require a redaction/generalization plan
  - ensure geometry and extents are consistent with policy label
- Registry and catalogs are part of the trust surface; treat changes as governed changes.

---

### Sources of truth
- *Kansas Frontier Matrix (KFM) — Definitive Design & Governance Guide (vNext)* (catalog triplet, evidence resolver, promotion gates, spec hashing)
- *Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint* (FAIR/CARE framing, governance posture)

---

<p align="right"><a href="#data-registry">Back to top ↑</a></p>
