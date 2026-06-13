<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-ingest-wbd-huc-readme
title: Hydrology WBD HUC Ingest Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <usgs-source-steward>
  - <spatial-foundation-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hydrology/ingest_wbd_huc/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - pipelines/domains/hydrology/ingest/README.md
  - pipelines/domains/hydrology/catalog/README.md
  - pipelines/domains/hydrology/catalog_close/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/sources/catalog/usgs/watershed-boundary-dataset.md
  - docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md
  - pipeline_specs/hydrology/ingest_wbd_huc.yaml
  - contracts/domains/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - data/raw/hydrology/
  - data/work/hydrology/
  - data/quarantine/hydrology/
  - data/processed/hydrology/
  - data/catalog/domain/hydrology/
  - data/triplets/hydrology/
  - data/registry/sources/hydrology/
  - data/registry/sources/usgs/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/hydrology/
  - release/manifests/hydrology/
tags:
  - kfm
  - pipelines
  - domains
  - hydrology
  - ingest
  - wbd
  - huc
  - huc12
  - watershed-boundary-dataset
  - usgs
  - watershed
  - administrative-hydrography
  - accounting-unit
  - boundary-lineage
  - source-role
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/ingest_wbd_huc path as a nested executable WBD/HUC ingest sublane."
  - "WBD/HUC ingest logic is executable implementation support only; it does not own USGS source descriptors, source catalog profiles, connector/fetch logic, schemas, policy, lifecycle data, catalog truth, hydrologic truth, boundary determinations, or release decisions."
  - "The subdirectory name uses the requested underscore form ingest_wbd_huc; if repo slug rules prefer hyphenated names, record the path decision with ADR/path-map/rollback notes before moving."
  - "WBD/HUC records provide administrative hydrography framework and identity backbone for Watershed and HUCUnit object families; they are not observed streamflow, flood context, or watershed condition by themselves."
  - "HUC code hierarchy, level, name, source vintage, geometry lineage, CRS, topology/context links, and receipt lineage must be preserved."
  - "HUC12 first-slice and fixture use must remain evidence-bound and release-gated."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and map/API behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USGS WBD / HUC Hydrology Ingest Pipeline

> Executable Hydrology sublane for normalizing admitted USGS Watershed Boundary Dataset / Hydrologic Unit Code inputs into governed work candidates, quarantine records, validation handoffs, receipts, and downstream catalog/release-review packages — without collapsing administrative hydrography boundaries into observed hydrology, modeled network topology, or release approval.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-WBD%20HUC%20hydrology%20ingest-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![identity](https://img.shields.io/badge/identity-HUC%20hierarchy%20aware-d62728)
![anti-collapse](https://img.shields.io/badge/WBD%20%E2%89%A0%20observed%20hydrology-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/ingest_wbd_huc/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** USGS WBD / HUC ingest and administrative-hydrography normalization  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Publication posture:** no direct publication; WBD/HUC-derived output is work/quarantine/validation input only and requires downstream evidence, policy, catalog, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. WBD / HUC anti-collapse rules](#3-wbd--huc-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ingest scope](#6-ingest-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal WBD / HUC ingest candidate record](#11-minimal-wbd--huc-ingest-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/ingest_wbd_huc/` is the executable sublane for USGS WBD / HUC normalization inside the Hydrology domain.

It supports candidate processing for:

- WBD source-package metadata and source-vintage records;
- hydrologic unit records across HUC2, HUC4, HUC6, HUC8, HUC10, HUC12, and any admitted WBD level;
- HUC code, HUC name, level, parent/child hierarchy, and accounting-unit context;
- Watershed and HUCUnit identity candidates;
- HUC12 proof-slice candidates and fixture records;
- WBD geometry references, CRS, topology, adjacency, and hierarchy lineage;
- context-link handoffs across KFM domain lanes with owning-domain refs;
- quarantine records for missing HUC code, invalid hierarchy, geometry ambiguity, CRS/source-vintage ambiguity, context-link policy gaps, source-role collapse, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of WBD/HUC ingest normalization. It does not fetch USGS data directly, define USGS source identity, define Hydrology object meaning, define schemas, encode policy, store lifecycle data, decide release, issue guidance, or certify hydrologic conclusions.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and the Hydrology pipeline README. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `ingest_wbd_huc/`? | This is a narrow executable sublane for USGS WBD/HUC administrative-hydrography input normalization. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/usgs/` or an accepted source-edge home. This sublane reads admitted lifecycle inputs or fixtures. | CONFIRMED separation |
| Does this own the WBD/HUC source profile? | No. Source profile content lives under `docs/sources/catalog/usgs/watershed-boundary-dataset.md` and source descriptors live in registry homes. | CONFIRMED source-doc separation |
| Where do declarative run specs live? | `pipeline_specs/hydrology/ingest_wbd_huc.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may emit work candidates, quarantine records, validation handoffs, and receipts only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> WBD/HUC ingest is not publication, not observed hydrology, not modeled network truth, not guidance, and not release approval. It prepares evidence-bound administrative hydrography candidates for downstream validation and review.

[⬆ Back to top](#top)

---

## 3. WBD / HUC anti-collapse rules

WBD/HUC ingest must preserve administrative hydrography semantics, HUC hierarchy, geometry lineage, and source vintage.

Disallowed collapses:

```text
WBD polygon -> observed watershed condition
HUC boundary -> jurisdictional boundary proof
HUC12 fixture -> published layer without release
HUC code -> stable feature identity without source vintage
parent HUC -> child HUC without hierarchy receipt
context link -> cross-domain truth
WBD -> NHDPlus HR network topology
WBD -> NFHL regulatory context
watershed label -> hydrologic measurement
generated summary -> evidence
ingest receipt -> release approval
```

Required distinctions:

- HUC code, level, name, parent, child, geometry, and source vintage are explicit;
- administrative hydrography framework, observed hydrology, modeled topology, terrain derivatives, and regulatory context remain distinct;
- WBD/HUC can anchor identity and context links, but it does not by itself prove conditions in another domain;
- HUC12 fixtures remain dry-run/release-gated assets until EvidenceBundle, policy, catalog closure, release, correction, and rollback close;
- cross-domain links carry owning-domain refs and policy outcomes.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable WBD/HUC ingest normalization.

Appropriate contents include:

- fixture-only WBD/HUC ingest entrypoints;
- source-package and source-vintage normalizers;
- HUC code, level, name, and hierarchy normalizers;
- Watershed and HUCUnit candidate builders;
- HUC12 proof-slice candidate builders;
- geometry, CRS, adjacency, and topology-context validators;
- parent/child hierarchy validators;
- context-link and policy-preflight helpers;
- source-role anti-collapse validators;
- quarantine routing helpers for missing HUC code, invalid hierarchy, geometry/CRS drift, source-vintage ambiguity, context-link policy gaps, evidence gaps, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for Hydrology validation, catalog, and triplet stages;
- thin adapters that read governed lifecycle inputs, not live USGS endpoints.

A good placement test:

> If the code transforms admitted WBD/HUC lifecycle inputs into Hydrology watershed/HUC candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, defines schemas, stores lifecycle data, writes catalog records, issues guidance, decides boundaries, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| USGS source fetchers / connectors | `connectors/usgs/` or accepted connector home |
| WBD/HUC source catalog profile | `docs/sources/catalog/usgs/watershed-boundary-dataset.md` |
| Source descriptors / source registry entries | `data/registry/sources/usgs/`, `data/registry/sources/hydrology/`, or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy and release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/ingest_wbd_huc/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/ingest_wbd_huc/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Catalog/triplet builders | `pipelines/domains/hydrology/catalog/`, `pipelines/catalog/`, or accepted graph/catalog adapter home |
| Catalog close / release preflight | `pipelines/domains/hydrology/catalog_close/` or release workflow homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions and manifests | `release/...` responsibility roots |
| Public API, map code, or public layers | `apps/governed-api/`, `apps/explorer-web/`, `data/published/...`, or release-controlled artifact homes |

[⬆ Back to top](#top)

---

## 6. Ingest scope

| Scope area | Ingest responsibility | Failure behavior |
|---|---|---|
| Source package | Preserve source id, source vintage, package scope, and retrieval refs. | Quarantine if missing. |
| HUC identity | Preserve HUC code, level, name, parent/child refs, and source vintage. | Quarantine if missing or invalid. |
| HUC hierarchy | Preserve HUC2-to-HUC12 nesting and hierarchy proofs. | Quarantine on mismatch. |
| Geometry | Normalize boundary geometry refs, CRS, and source lineage. | Quarantine on geometry/CRS ambiguity. |
| HUC12 fixture | Prepare dry-run proof-slice candidate with evidence refs. | No direct release. |
| Context links | Prepare joins only as evidence-bound context. | Restrict or quarantine if policy unresolved. |
| Cross-source relation | Preserve separation from NHDPlus HR, 3DEP, NWIS, and NFHL. | Deny if silently merged. |
| Hydrology handoff | Prepare candidates with source-role and source-vintage caveats. | No direct condition or regulatory claim. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every WBD/HUC ingest run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work inputs, quarantine inputs in remediation mode, or prior processed WBD/HUC baselines.
2. **Normalize** into Hydrology work candidates with source role, HUC code, HUC level, parent/child refs, source vintage, geometry refs, CRS, context-link refs, evidence refs, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, missing HUC code, invalid hierarchy, unsupported source role, geometry drift, CRS ambiguity, context-link policy gap, rights failure, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, HUC hierarchy refs, geometry refs, validation refs, output refs, and outcomes.
5. **Support promotion** only by feeding downstream Hydrology validation and review workflows.
6. **Never publish directly.**

WBD/HUC ingest is an early lifecycle transformation. It is not processed-state promotion, catalog closure, release approval, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every WBD/HUC ingest run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — USGS WBD/HUC source identity, role, source vintage, rights, and policy posture are known.
3. **Source-role gate** — WBD/HUC remains administrative hydrography framework and never observed hydrology or regulatory context.
4. **HUC code gate** — HUC code exists, level is explicit, and code length matches level semantics.
5. **Hierarchy gate** — parent/child nesting and HUC2-to-HUC12 hierarchy are validated or quarantined.
6. **Source-vintage gate** — HUC identity and geometry are tied to source vintage/release refs.
7. **Geometry/CRS gate** — geometry refs, CRS, validity, and source lineage are explicit.
8. **Context-link gate** — cross-domain links carry owning-domain, policy, and evidence refs.
9. **Cross-source boundary gate** — WBD/HUC is not silently merged with NHDPlus HR, 3DEP, NWIS, NFHL, or generated summaries.
10. **Evidence gate** — claim-bearing downstream candidates can resolve evidence refs or abstain.
11. **Rights gate** — unresolved rights cannot proceed to release handoff.
12. **Schema/contract gate** — candidates match accepted schema and Hydrology semantics.
13. **No-direct-publish gate** — no writes to public UI, public API, catalog store, published layers, or release manifests as an ingest side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/ingest_wbd_huc/
├── README.md                         # this file
├── INGEST_CONTRACT.md                # PROPOSED: WBD/HUC ingest execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_source_package.py       # PROPOSED
├── normalize_huc_identity.py         # PROPOSED
├── normalize_huc_hierarchy.py        # PROPOSED
├── normalize_watershed_geometry.py   # PROPOSED
├── build_huc12_fixture_candidate.py  # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_huc_code_level.py        # PROPOSED
├── validate_hierarchy_lineage.py     # PROPOSED
├── validate_context_links.py         # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/ingest_wbd_huc.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the ingest code. Use accepted lifecycle homes under `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/ingest_wbd_huc/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw WBD/HUC capture | `data/raw/hydrology/<source_id>/<run_id>/` or accepted USGS raw home | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/hydrology/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed watershed handoff | `data/processed/hydrology/<dataset_id>/<version>/` | Only after downstream validation and promotion gates. |
| Receipt | `data/receipts/pipeline/hydrology/ingest_wbd_huc/<run_id>.yml` or accepted receipt home | Records input refs, HUC hierarchy, geometry lineage, checks, and outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing downstream records. |
| Catalog handoff | `pipelines/domains/hydrology/catalog/` via lifecycle data homes | No direct catalog writes from ingest unless approved by spec. |

[⬆ Back to top](#top)

---

## 11. Minimal WBD / HUC ingest candidate record

The final schema is not defined here. This example shows the minimum information a WBD/HUC ingest candidate should preserve.

```yaml
schema_version: kfm.hydrology_wbd_huc_ingest_candidate.v1
candidate_id: hydrology_wbd_huc_<huc_code_or_package>_<run_id>_<hash>
pipeline_id: domains.hydrology.ingest_wbd_huc
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <watershed|huc_unit|huc_hierarchy|huc12_fixture|context_link>
source:
  source_id: usgs_wbd_huc
  source_role: administrative_hydrography_framework
  lifecycle_ref: data/raw/hydrology/usgs_wbd_huc/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
release:
  source_vintage: null
  package_scope: <national|state|huc_region|huc_subregion|fixture>
identity:
  huc_code: null
  huc_level: null
  huc_name: null
  parent_huc: null
  child_hucs: []
geometry:
  geometry_ref: null
  crs: null
  geometry_lineage_ref: null
context:
  linked_domains: []
  policy_review: needs_review
anti_collapse:
  wbd_is_observed_hydrology: false
  huc_boundary_is_jurisdictional_boundary: false
  wbd_is_nfhl: false
  context_link_is_cross_domain_truth: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_HUC_HIERARCHY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/hydrology/run_YYYYMMDDThhmmssZ/wbd_huc_candidate.yml
  receipt: data/receipts/pipeline/hydrology/ingest_wbd_huc/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, WBD/HUC ingest spec, evidence, policy, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/ingest_wbd_huc/
├── test_no_network_dry_run.py             # PROPOSED
├── test_source_descriptor_required.py     # PROPOSED
├── test_huc_code_required.py              # PROPOSED
├── test_huc_level_matches_code_length.py  # PROPOSED
├── test_huc_hierarchy_valid.py            # PROPOSED
├── test_source_vintage_required.py        # PROPOSED
├── test_geometry_crs_required.py          # PROPOSED
├── test_wbd_not_observed_hydrology.py     # PROPOSED
├── test_wbd_not_nfhl.py                   # PROPOSED
├── test_context_link_requires_policy.py   # PROPOSED
├── test_evidence_gap_abstains.py          # PROPOSED
├── test_quarantine_on_schema_failure.py   # PROPOSED
├── test_receipt_hashes.py                 # PROPOSED
└── test_no_direct_publish.py              # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors and source roles are required, HUC code/level/hierarchy/source-vintage are preserved, WBD stays administrative hydrography context, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

WBD/HUC ingest may prepare work candidates and quarantine records. It does not publish.

Required chain:

```text
admitted WBD/HUC source capture
  -> watershed / HUC ingest candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed Hydrology watershed/HUC record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> released artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined WBD/HUC ingest runs remain auditable;
- ingest receipts preserve source refs, source-vintage refs, HUC hierarchy refs, geometry refs, context-link refs, rule ids, and outcomes;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, HUC refs, hierarchy refs, geometry refs, evidence refs, source-role refs, policy refs, or context-link refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/ingest_wbd_huc/README.md` file;
- identifies this directory as a nested executable Hydrology WBD/HUC ingest sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, and release authority from being placed here;
- preserves WBD/HUC source role, HUC code and hierarchy, source vintage, geometry lineage, context-link policy, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks WBD-as-observed-hydrology, HUC-boundary-as-jurisdictional-boundary, WBD-as-NFHL, context-link-as-truth, generated-summary-as-evidence, and direct catalog/release writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, HUC/hierarchy/geometry/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-WBD-HUC-001` | Should this sublane remain Hydrology-specific or move to Spatial Foundation with Hydrology adapters? | NEEDS VERIFICATION / ADR |
| `HYDRO-WBD-HUC-002` | Which source-edge job owns USGS WBD/HUC retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `HYDRO-WBD-HUC-003` | Which first-wave levels are approved for fixture-only dry runs: HUC2, HUC4, HUC6, HUC8, HUC10, HUC12, or HUC12 only? | NEEDS VERIFICATION |
| `HYDRO-WBD-HUC-004` | Which schema owns Watershed/HUCUnit candidates, hierarchy records, and quarantine reasons? | NEEDS VERIFICATION |
| `HYDRO-WBD-HUC-005` | Which CI job owns WBD/HUC ingest invariant tests? | UNKNOWN |
| `HYDRO-WBD-HUC-006` | Should HUC12 proof-slice logic live here or in a release-candidate fixture lane? | NEEDS VERIFICATION |
| `HYDRO-WBD-HUC-007` | Which receipt type owns context-link validation for cross-domain joins? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized HUC12 fixture-only dry runs and negative tests. Do not add live USGS fetching, direct catalog writes, public layer writes, release-manifest writes, boundary-determination language, condition claims, or direct API payload generation until source roles, HUC hierarchy, geometry lineage, evidence closure, release review, and rollback are proven.
