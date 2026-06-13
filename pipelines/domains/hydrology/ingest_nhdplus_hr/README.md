<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-ingest-nhdplus-hr-readme
title: Hydrology NHDPlus HR Ingest Pipeline README
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
path: pipelines/domains/hydrology/ingest_nhdplus_hr/README.md
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
  - docs/sources/catalog/usgs/nhdplus-hr.md
  - docs/sources/catalog/usgs/3dep-elevation.md
  - docs/sources/catalog/usgs/README.md
  - pipeline_specs/hydrology/ingest_nhdplus_hr.yaml
  - contracts/domains/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - policy/sensitivity/hydrology/
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
  - nhdplus-hr
  - usgs
  - hydrography
  - comid
  - network-topology
  - vaa
  - modeled-attribute
  - observed-geometry
  - reach
  - wbd
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/ingest_nhdplus_hr path as a nested executable NHDPlus HR ingest sublane."
  - "NHDPlus HR ingest logic is executable implementation support only; it does not own USGS source descriptors, source catalog profiles, connector/fetch logic, schemas, policy, lifecycle data, catalog truth, hydrologic truth, engineering determinations, or release decisions."
  - "The subdirectory name uses the requested underscore form ingest_nhdplus_hr; if repo slug rules prefer hyphenated names, record the path decision with ADR/path-map/rollback notes before moving."
  - "NHDPlus HR source-role split must be preserved: digitized hydrography geometry is observed/digitized geometry, while VAAs and network topology attributes are modeled."
  - "COMID identity, WBD packaging scope, release vintage, upstream/downstream topology, VAA method lineage, geometry lineage, and receipt lineage must be preserved."
  - "NHDPlus HR is informational hydrography context, not NFHL, not observed streamflow, not a regulatory flood determination, not engineering certification, and not current safety guidance."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USGS NHDPlus HR Hydrology Ingest Pipeline

> Executable Hydrology sublane for normalizing admitted USGS NHDPlus High Resolution hydrography inputs into governed work candidates, quarantine records, validation handoffs, receipts, and downstream catalog/release-review packages — without collapsing observed digitized geometry, modeled Value-Added Attributes, network topology, regulatory flood context, measured streamflow, or public release state.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-NHDPlus%20HR%20hydrology%20ingest-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![identity](https://img.shields.io/badge/identity-COMID%20network%20aware-d62728)
![source-role](https://img.shields.io/badge/observed%20geometry%20%E2%89%A0%20modeled%20VAA-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/ingest_nhdplus_hr/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** USGS NHDPlus HR ingest / hydrography-network normalization  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; NHDPlus HR-derived output is work/quarantine/validation input only and requires downstream evidence, policy, catalog, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. NHDPlus HR anti-collapse rules](#3-nhdplus-hr-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ingest scope](#6-ingest-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal NHDPlus HR ingest candidate record](#11-minimal-nhdplus-hr-ingest-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/ingest_nhdplus_hr/` is the executable sublane for USGS NHDPlus HR hydrography-network normalization inside the Hydrology domain.

It supports candidate processing for:

- NHDPlus HR packaged geodatabase captures and source-vintage metadata;
- NHDFlowline, NHDArea, NHDWaterbody, and related hydrographic geometry candidates;
- COMID-keyed reach identity records;
- WBD/HU packaging and accounting-unit scope refs;
- upstream/downstream network topology and level-path references;
- Value-Added Attributes (VAAs) such as cumulative drainage area, mean annual flow, mean annual velocity, stream order, and flow-direction context as modeled attributes;
- geometry lineage and VAA/model lineage receipts;
- quarantine records for missing COMID, missing topology refs, geometry/VAA role collapse, WBD packaging ambiguity, release-vintage ambiguity, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of NHDPlus HR ingest normalization. It does not fetch USGS data directly, define USGS source identity, define Hydrology object meaning, define schemas, encode policy, store lifecycle data, decide release, issue current safety guidance, decide NFHL meaning, or certify engineering use.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and the Hydrology pipeline README. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `ingest_nhdplus_hr/`? | This is a narrow executable sublane for USGS NHDPlus HR hydrography-network input normalization. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/usgs/` or an accepted source-edge home. This sublane reads admitted lifecycle inputs or fixtures. | CONFIRMED separation |
| Does this own the NHDPlus HR source profile? | No. Source profile content lives under `docs/sources/catalog/usgs/nhdplus-hr.md` and source descriptors live in registry homes. | CONFIRMED source-doc separation |
| Where do declarative run specs live? | `pipeline_specs/hydrology/ingest_nhdplus_hr.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may emit work candidates, quarantine records, validation handoffs, and receipts only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> NHDPlus HR ingest is not publication, not NFHL, not observed streamflow, not an engineering determination, not current safety guidance, and not release approval. It prepares evidence-bound hydrography-network candidates for downstream validation and review.

[⬆ Back to top](#top)

---

## 3. NHDPlus HR anti-collapse rules

NHDPlus HR ingest must preserve source-role separation, COMID identity, topology lineage, and release vintage.

Disallowed collapses:

```text
NHDPlus HR geometry -> observed streamflow
NHDFlowline geometry -> legal water boundary
COMID -> stable eternal feature identity without release vintage
VAA modeled attribute -> measured value
network topology -> field-observed flow direction
WBD packaging unit -> hydrologic truth by itself
NHDPlus HR -> FEMA NFHL
NHDPlus HR -> 3DHP successor without migration receipt
mean annual flow VAA -> current flow condition
generated summary -> evidence
ingest receipt -> release approval
```

Required distinctions:

- observed/digitized geometry, modeled VAAs, and modeled network topology are separate truth/support classes;
- COMID identifiers are preserved with release vintage and source package context;
- WBD/HU package scope is recorded but does not become independent hydrologic truth;
- VAA fields carry modeled-method lineage and are not cited as measured observations;
- topology and reach graph refs preserve upstream/downstream linkage without replacing canonical review state;
- NHDPlus HR remains distinct from NFHL regulatory context, measured gauge observations, 3DEP terrain derivatives, and future 3DHP remapping.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable NHDPlus HR hydrography-network ingest normalization.

Appropriate contents include:

- fixture-only NHDPlus HR ingest entrypoints;
- package metadata and release-vintage normalizers;
- COMID and reach identity normalizers;
- NHDFlowline, NHDArea, and NHDWaterbody geometry normalizers;
- WBD/HU packaging scope normalizers;
- VAA table and modeled-attribute normalizers;
- upstream/downstream network topology normalizers;
- geometry-vs-VAA source-role anti-collapse validators;
- COMID/release-vintage/topology validators;
- method receipt builders for VAA/network-derived attributes, if not shared;
- quarantine routing helpers for COMID, topology, source-role, geometry, VAA, release-vintage, evidence, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for Hydrology validation, catalog, and triplet stages;
- thin adapters that read governed lifecycle inputs, not live USGS endpoints.

A good placement test:

> If the code transforms admitted NHDPlus HR lifecycle inputs into Hydrology hydrography-network candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, defines schemas, stores lifecycle data, writes catalog records, issues public guidance, decides regulatory status, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| USGS source fetchers / connectors | `connectors/usgs/` or accepted connector home |
| NHDPlus HR source catalog profile | `docs/sources/catalog/usgs/nhdplus-hr.md` |
| Source descriptors / source registry entries | `data/registry/sources/usgs/`, `data/registry/sources/hydrology/`, or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Spatial Foundation hydrography doctrine | `docs/domains/spatial-foundation/...` or accepted spatial docs home |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/ingest_nhdplus_hr/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/ingest_nhdplus_hr/` or accepted test home |
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
| Source package | Preserve source id, release vintage, WBD/HU package scope, and retrieval refs. | Quarantine if missing. |
| COMID identity | Preserve COMID keys and reach identity context. | Quarantine if missing or duplicated without resolution. |
| Geometry | Normalize flowlines, areas, and waterbodies as observed/digitized geometry. | Quarantine on geometry/source-role ambiguity. |
| VAAs | Normalize value-added attributes as modeled context. | Deny if cited as measured observations. |
| Network topology | Preserve upstream/downstream, level-path, and graph linkage refs. | Quarantine on topology gaps. |
| WBD packaging | Preserve package scope and accounting-unit context. | Deny if treated as independent truth. |
| 3DHP successor | Preserve as migration/remapping context only. | Require ADR/receipt before replacement. |
| Hydrology handoff | Prepare candidates with source-role and method caveats. | No direct current-flow or regulatory claims. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every NHDPlus HR ingest run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work inputs, quarantine inputs in remediation mode, or prior processed NHDPlus baselines.
2. **Normalize** into Hydrology work candidates with source role, release vintage, COMID, WBD package refs, geometry refs, topology refs, VAA/method refs, evidence refs, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, missing COMID, missing release vintage, unsupported source role, geometry/VAA collapse, topology gap, method-lineage gap, rights failure, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, COMID refs, topology refs, VAA/method refs, validation refs, output refs, and outcomes.
5. **Support promotion** only by feeding downstream Hydrology validation and review workflows.
6. **Never publish directly.**

NHDPlus HR ingest is an early lifecycle transformation. It is not processed-state promotion, catalog closure, release approval, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every NHDPlus HR ingest run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — USGS NHDPlus HR source identity, role, release vintage, rights, and sensitivity posture are known.
3. **Source-role gate** — digitized hydrography geometry, modeled VAAs, and modeled network topology remain distinct.
4. **COMID gate** — COMID identity is present, release-vintaged, and not treated as eternal truth.
5. **Package-scope gate** — WBD/HU packaging scope is recorded and not treated as canonical hydrologic truth by itself.
6. **Geometry gate** — NHDFlowline, NHDArea, NHDWaterbody, CRS, geometry lineage, and source vintage are explicit where applicable.
7. **VAA gate** — VAA fields are labeled modeled and carry method/model lineage or abstain.
8. **Topology gate** — upstream/downstream and level-path lineage is preserved or quarantined.
9. **3DHP migration gate** — 3DHP replacement/remapping requires an explicit migration receipt/ADR.
10. **Evidence gate** — claim-bearing downstream candidates can resolve evidence refs or abstain.
11. **Rights and sensitivity gate** — unresolved rights or restricted context cannot proceed to public-safe handoff.
12. **Schema/contract gate** — candidates match accepted schema and Hydrology semantics.
13. **No-direct-publish gate** — no writes to public UI, public API, catalog store, published layers, or release manifests as an ingest side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/ingest_nhdplus_hr/
├── README.md                         # this file
├── INGEST_CONTRACT.md                # PROPOSED: NHDPlus HR ingest execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_package_metadata.py     # PROPOSED
├── normalize_comid_identity.py       # PROPOSED
├── normalize_hydrography_geometry.py # PROPOSED
├── normalize_vaa_table.py            # PROPOSED
├── normalize_network_topology.py     # PROPOSED
├── validate_source_role_split.py     # PROPOSED
├── validate_comid_release_vintage.py # PROPOSED
├── validate_topology_lineage.py      # PROPOSED
├── validate_vaa_method_lineage.py    # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/ingest_nhdplus_hr.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the ingest code. Use accepted lifecycle homes under `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/ingest_nhdplus_hr/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw NHDPlus HR capture | `data/raw/hydrology/<source_id>/<run_id>/` or accepted USGS raw home | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/hydrology/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed hydrography handoff | `data/processed/hydrology/<dataset_id>/<version>/` | Only after downstream validation and promotion gates. |
| Receipt | `data/receipts/pipeline/hydrology/ingest_nhdplus_hr/<run_id>.yml` or accepted receipt home | Records input refs, COMIDs, topology, VAA lineage, and outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing downstream records. |
| Catalog handoff | `pipelines/domains/hydrology/catalog/` via lifecycle data homes | No direct catalog writes from ingest unless approved by spec. |

[⬆ Back to top](#top)

---

## 11. Minimal NHDPlus HR ingest candidate record

The final schema is not defined here. This example shows the minimum information a NHDPlus HR ingest candidate should preserve.

```yaml
schema_version: kfm.hydrology_nhdplus_hr_ingest_candidate.v1
candidate_id: hydrology_nhdplus_hr_<comid_or_package>_<run_id>_<hash>
pipeline_id: domains.hydrology.ingest_nhdplus_hr
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <flowline|waterbody|area|reach_identity|vaa_record|network_topology|package_metadata>
source:
  source_id: usgs_nhdplus_hr
  source_role: <observed_digitized_geometry|modeled_vaa|modeled_network_topology|synthetic>
  lifecycle_ref: data/raw/hydrology/usgs_nhdplus_hr/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
release:
  release_vintage: null
  package_scope: <wbd_hu4|wbd_hu8|other>
identity:
  comid: null
  reach_code: null
  permanent_identifier: null
geometry:
  geometry_ref: null
  crs: null
topology:
  upstream_refs: []
  downstream_refs: []
  level_path: null
vaa:
  vaa_fields: []
  modeled_attribute: true
  method_receipt_ref: null
anti_collapse:
  vaa_is_measured_observation: false
  geometry_is_streamflow_observation: false
  comid_is_eternal_identity: false
  nhdplus_is_nfhl: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_COMID_TOPOLOGY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/hydrology/run_YYYYMMDDThhmmssZ/nhdplus_hr_candidate.yml
  receipt: data/receipts/pipeline/hydrology/ingest_nhdplus_hr/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, NHDPlus HR ingest spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/ingest_nhdplus_hr/
├── test_no_network_dry_run.py             # PROPOSED
├── test_source_descriptor_required.py     # PROPOSED
├── test_source_role_split_required.py     # PROPOSED
├── test_comid_required.py                 # PROPOSED
├── test_release_vintage_required.py       # PROPOSED
├── test_geometry_not_streamflow.py        # PROPOSED
├── test_vaa_not_measured_value.py         # PROPOSED
├── test_topology_refs_required.py         # PROPOSED
├── test_nhdplus_not_nfhl.py               # PROPOSED
├── test_3dhp_replacement_requires_receipt.py # PROPOSED
├── test_evidence_gap_abstains.py          # PROPOSED
├── test_quarantine_on_schema_failure.py   # PROPOSED
├── test_receipt_hashes.py                 # PROPOSED
└── test_no_direct_publish.py              # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors and source roles are required, COMID and release vintage are preserved, geometry and VAAs remain distinct, topology lineage is present, NHDPlus HR is not NFHL, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

NHDPlus HR ingest may prepare work candidates and quarantine records. It does not publish.

Required chain:

```text
admitted NHDPlus HR source capture
  -> hydrography-network ingest candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed Hydrology network record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined NHDPlus HR ingest runs remain auditable;
- ingest receipts preserve source refs, release-vintage refs, COMID refs, topology refs, VAA/method refs, rule ids, and outcomes;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, COMID refs, topology refs, VAA refs, release-vintage refs, evidence refs, source-role refs, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/ingest_nhdplus_hr/README.md` file;
- identifies this directory as a nested executable Hydrology NHDPlus HR ingest sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, and release authority from being placed here;
- preserves NHDPlus HR source-role split, COMID identity, WBD package scope, release vintage, geometry lineage, VAA method lineage, topology lineage, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks geometry-as-streamflow, VAA-as-measurement, COMID-as-eternal-identity, NHDPlus-as-NFHL, generated-summary-as-evidence, and direct catalog/release writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, source-role/COMID/topology/VAA/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-NHDPLUS-HR-001` | Should this sublane remain Hydrology-specific or move to Spatial Foundation with Hydrology adapters? | NEEDS VERIFICATION / ADR |
| `HYDRO-NHDPLUS-HR-002` | Which source-edge job owns USGS NHDPlus HR retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `HYDRO-NHDPLUS-HR-003` | Which first-wave feature classes are approved for fixture-only dry runs: NHDFlowline, NHDArea, NHDWaterbody, VAAs, network topology, or package metadata? | NEEDS VERIFICATION |
| `HYDRO-NHDPLUS-HR-004` | Which schema owns COMID reach candidates, VAA candidates, topology candidates, and quarantine reasons? | NEEDS VERIFICATION |
| `HYDRO-NHDPLUS-HR-005` | Which CI job owns NHDPlus HR ingest invariant tests? | UNKNOWN |
| `HYDRO-NHDPLUS-HR-006` | Should catalog handoff be forbidden as an ingest side effect, or allowed only through an explicit chained spec? | NEEDS VERIFICATION |
| `HYDRO-NHDPLUS-HR-007` | Which receipt type owns VAA method lineage, network topology lineage, and future 3DHP migration/remapping? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live USGS fetching, direct catalog writes, public layer writes, release-manifest writes, current safety guidance, engineering-use language, or direct API payload generation until source roles, COMID identity, VAA/topology lineage, evidence closure, public-safe transforms, release review, and rollback are proven.
