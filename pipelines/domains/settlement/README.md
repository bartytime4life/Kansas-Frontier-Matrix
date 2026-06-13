<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-settlement-readme
title: Settlement Pipeline Alias README
type: readme
version: v0.1
status: draft
owners:
  - <settlements-infrastructure-pipeline-owner>
  - <settlements-infrastructure-domain-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/settlement/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/settlements-infrastructure/README.md
  - docs/domains/settlements-infrastructure/README.md
  - docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md
  - docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - contracts/domains/settlements-infrastructure/
  - schemas/contracts/v1/domains/settlements-infrastructure/
  - policy/domains/settlements-infrastructure/
  - pipeline_specs/settlements-infrastructure/
  - data/raw/settlements-infrastructure/
  - data/work/settlements-infrastructure/
  - data/quarantine/settlements-infrastructure/
  - data/processed/settlements-infrastructure/
  - data/catalog/domain/settlements-infrastructure/
  - data/triplets/settlements-infrastructure/
  - data/published/layers/settlements-infrastructure/
  - data/registry/sources/settlements-infrastructure/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/settlements-infrastructure/
  - release/manifests/settlements-infrastructure/
tags:
  - kfm
  - pipelines
  - domains
  - settlement
  - settlements-infrastructure
  - compatibility-alias
  - municipality
  - census-place
  - townsite
  - facility
  - service-area
  - evidence
  - policy
  - governance
notes:
  - "This README fills the previously blank pipelines/domains/settlement path as a compatibility/alias lane, not as a new canonical authority root."
  - "The governing bounded context remains Settlements and Infrastructure unless an ADR resolves the segment naming differently."
  - "Do not create parallel schemas, contracts, source registries, policies, lifecycle data, catalog truth, or release decisions under both settlement and settlements-infrastructure without ADR/path-map/migration/rollback notes."
  - "Restricted facility, operator, condition, dependency, private-property, and culturally sensitive context fail closed by default."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🏘️ Settlement Pipeline Alias

> Compatibility README for the requested `pipelines/domains/settlement/` path. This path must not become a parallel authority beside `pipelines/domains/settlements-infrastructure/`. Until an ADR resolves segment naming, use this path only for carefully bounded Settlement-sublane executable work or compatibility documentation that preserves Settlements / Infrastructure governance.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-settlement%20alias%20lane-2e7d32)
![authority](https://img.shields.io/badge/authority-compatibility%20not%20canonical-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/settlement/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain posture:** `settlement` is a compatibility/alias segment for the Settlements / Infrastructure bounded context  
**Placement posture:** `CONFLICTED / NEEDS VERIFICATION` until the `settlement` vs `settlements-infrastructure` segment naming decision is resolved by ADR, path map, migration note, and rollback note  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, rights, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Alias and authority posture](#2-alias-and-authority-posture)
- [3. Sensitivity boundary](#3-sensitivity-boundary)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Relationship to settlements-infrastructure](#6-relationship-to-settlements-infrastructure)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Minimal alias-lane candidate record](#10-minimal-alias-lane-candidate-record)
- [11. Tests and validation](#11-tests-and-validation)
- [12. Promotion, publication, correction, and rollback](#12-promotion-publication-correction-and-rollback)
- [13. Definition of done](#13-definition-of-done)
- [14. Open questions](#14-open-questions)

---

## 1. Purpose

`pipelines/domains/settlement/` is a requested compatibility lane for Settlement-sublane executable pipeline work.

This README does **not** establish `settlement` as a new canonical domain root. It exists to prevent ambiguity while the repo uses the broader canonical domain segment:

- `settlements-infrastructure` — visible KFM bounded-context name used by the Settlements and Infrastructure documentation set;
- `settlement` — a shorter requested path represented here as an alias candidate only.

Use this README to keep the alias safe. The governing semantics, sensitivity posture, source-role posture, lifecycle posture, and release posture are inherited from Settlements / Infrastructure.

This path may support narrow Settlement-sublane transformations such as:

- settlement candidates;
- municipality candidates;
- census-place candidates;
- townsite and ghost-town candidates;
- fort, mission, and community context;
- public-safe, release-reviewed settlement-context derivatives.

It must not become the home for whole-domain infrastructure pipeline logic, source registries, schemas, policy, lifecycle data, catalog truth, or release decisions unless a future ADR explicitly changes the boundary.

[⬆ Back to top](#top)

---

## 2. Alias and authority posture

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/settlement/`? | User requested this path; it is treated as a Settlement-sublane alias candidate. | PROPOSED / NEEDS VERIFICATION |
| Is `settlement` canonical? | Not proven. The visible domain docs identify `settlements-infrastructure` as the broader domain lane and list `pipelines/domains/settlements-infrastructure/` as the pipeline logic home. | NEEDS VERIFICATION / likely alias |
| What is canonical today? | Treat `settlements-infrastructure` as the governing bounded-context lane for docs and controls until ADR resolution. | CONFIRMED documentation posture; implementation NEEDS VERIFICATION |
| Can this path create parallel authority? | No. It must not create duplicate schemas, contracts, policies, registries, data lanes, or release lanes. | CONFIRMED governance posture |
| Where do declarative specs live? | Prefer `pipeline_specs/settlements-infrastructure/`; `pipeline_specs/settlement/` is alias-candidate only until ADR. | NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/*/settlements-infrastructure/` unless ADR resolves otherwise. | PROPOSED / NEEDS VERIFICATION |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> The alias must not weaken the controls of the parent bounded context. A shorter path is not permission to publish restricted facility, operator, private-land, living-person, condition, dependency, or exact-location details.

[⬆ Back to top](#top)

---

## 3. Sensitivity boundary

Settlement-sublane work inherits the Settlements / Infrastructure sensitivity posture.

A pipeline must fail closed when it cannot prove safe handling for:

- restricted facility or operator-sensitive details;
- condition observations and dependencies;
- exact facility geometry where public exposure is not release-approved;
- service-area or network-dependency context that requires review;
- private-property or living-person joins;
- historic settlement, mission, fort, community, burial-adjacent, or culturally sensitive context that requires review;
- generated summaries that could be mistaken for source evidence, legal status, or operational status.

Disallowed collapses:

```text
Settlement candidate -> official municipal status
Census place -> municipality truth
Facility context -> public restricted detail
Condition observation -> current operational status
Service area -> guaranteed service truth
Generated summary -> evidence
Settlement alias path -> canonical domain authority
```

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here only if an ADR, path map, or maintainer decision intentionally uses `settlement` as a compatibility or Settlement-sublane pipeline segment.

Appropriate contents may include:

- this README documenting alias limits;
- fixture-only dry-run entrypoints using synthetic/generalized/redacted settlement data;
- settlement, municipality, census-place, townsite, ghost-town, fort, mission, and community candidate builders;
- settlement name and temporal-status normalizers;
- source-role validators distinguishing settlement candidates, municipalities, census places, and administrative records;
- public-safe settlement-context transform helpers, if not centralized elsewhere;
- quarantine routing helpers for rights, sensitivity, source-role, identity, temporal, or geometry failures;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code narrowly transforms Settlement-sublane lifecycle inputs into candidates, processed restricted records, restricted catalog/triplet handoffs, receipts, or review handoffs, and does not create a parallel Settlements/Infrastructure authority, it may belong here. Otherwise use `pipelines/domains/settlements-infrastructure/` or the correct responsibility root.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/settlements-infrastructure/` or approved registry home |
| Settlements/Infrastructure architecture / doctrine | `docs/domains/settlements-infrastructure/...` |
| Whole-domain pipeline logic | `pipelines/domains/settlements-infrastructure/` unless ADR resolves otherwise |
| Infrastructure asset, network, service-area, condition, operator, dependency pipeline logic | `pipelines/domains/settlements-infrastructure/` or sublane after ADR/review |
| Object meaning contracts | `contracts/domains/settlements-infrastructure/` or accepted ADR home |
| JSON Schemas | `schemas/contracts/v1/domains/settlements-infrastructure/` or accepted ADR home |
| Policy, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/settlements-infrastructure/` or accepted spec home |
| Fixtures | `fixtures/domains/settlements-infrastructure/` or accepted fixture home |
| Tests | `tests/pipelines/domains/settlement/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/settlements-infrastructure/`, `release/manifests/settlements-infrastructure/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Legal determinations, restricted facility analysis, live operational condition, service guarantees, or emergency guidance | Outside this executable pipeline lane |

> [!WARNING]
> Do not use this path as a workaround for the broader controls in `settlements-infrastructure`. The alias exists to reduce confusion, not to reduce governance.

[⬆ Back to top](#top)

---

## 6. Relationship to settlements-infrastructure

`pipelines/domains/settlements-infrastructure/` is the broader executable lane for the full Settlements / Infrastructure bounded context.

This alias README must stay subordinate to it until an ADR says otherwise:

```text
pipelines/domains/settlements-infrastructure/   # governing whole-domain executable lane
pipelines/domains/settlement/                   # compatibility / Settlement-sublane alias candidate
```

If future work keeps both paths, the repo needs:

- an ADR naming canonical and compatibility segments;
- a path map that says which objects belong in each path;
- tests proving no duplicate authority;
- lint/checks preventing parallel schemas, contracts, policies, registries, lifecycle data, and release lanes;
- a rollback note for any migration.

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Settlement alias pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal alias-lane stance:

1. **Read** approved synthetic/generalized/redacted fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, temporal scope, spatial/place scope, assertion status, sensitivity posture, evidence references, and public-safe transform posture.
3. **Quarantine** unresolved rights, source-role mismatch, identity ambiguity, temporal ambiguity, restricted detail, cultural sensitivity, private-property joins, geometry risk, schema drift, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, sensitivity/public-safe transform, review, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with sensitivity-safe payloads.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a move from one lifecycle folder to another as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Settlement alias pipeline run must check or explicitly fail closed on:

1. **Alias gate** — the run must declare whether `settlement` is alias, compatibility, or ADR-approved canonical segment.
2. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
3. **Source-role gate** — settlement candidate, municipality, census place, historic townsite, administrative record, aggregate, synthetic, and context records are not silently collapsed.
4. **Identity gate** — name reuse, relocation, abandonment, incorporation, disincorporation, annexation, and boundary changes remain temporally scoped.
5. **Sensitivity gate** — restricted facility, operator, condition, dependency, private-property, living-person, and cultural contexts fail closed unless public-safe handling is proven.
6. **Rights gate** — unknown or restrictive license, permission, attribution, privacy, or redistribution terms block public release.
7. **Public-safe transform gate** — public products require approved redaction, aggregation, generalization, delay, restriction, or denial decisions with receipts.
8. **Temporal gate** — source time, event time, valid time, observed time, retrieval time, processing time, catalog time, and release time remain distinct.
9. **Spatial/place gate** — place point, boundary, facility geometry, service area, network node/segment, and public-safe spatial transforms remain distinct.
10. **Schema gate** — candidate and processed records match approved schemas.
11. **Contract gate** — object meanings match Settlements/Infrastructure contracts and do not invent new semantics silently.
12. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
13. **Policy gate** — policy decisions are finite and recorded; no silent allow.
14. **Validation gate** — validators exercise pass, fail, restrict, abstain, deny, and error paths, not only success.
15. **Receipt gate** — every run records input refs, versions, parameters, transforms, hashes, output refs, and outcomes.
16. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.
17. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical records or review state.
18. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended alias-safe shape:

```text
pipelines/domains/settlement/
├── README.md                         # this file; alias / compatibility contract
├── PIPELINE_CONTRACT.md              # PROPOSED only after ADR/path decision
├── run_dry_fixture.py                # PROPOSED synthetic/generalized/redacted fixtures only
├── normalize_settlement_candidate.py # PROPOSED
├── normalize_municipality.py         # PROPOSED
├── normalize_census_place.py         # PROPOSED
├── normalize_townsite.py             # PROPOSED
├── normalize_ghost_town.py           # PROPOSED
├── validate_settlement_identity.py   # PROPOSED
├── validate_alias_boundary.py        # PROPOSED
├── apply_public_safe_transform.py    # PROPOSED; may belong in shared tools if reused
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_settlement_candidate.py  # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Do not create these parallel authority homes without ADR:

```text
schemas/contracts/v1/domains/settlement/
contracts/domains/settlement/
policy/domains/settlement/
data/raw/settlement/
data/processed/settlement/
release/manifests/settlement/
```

Generated outputs must not be written beside the code that generated them. Use accepted lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Minimal alias-lane candidate record

The final schema is not defined here. This example shows the minimum information a Settlement alias-lane candidate should preserve.

```yaml
schema_version: kfm.settlement_alias_pipeline_candidate.v1
candidate_id: settlement_<object_family>_<run_id>_<hash>
pipeline_id: domains.settlement
alias_status: NEEDS_VERIFICATION
canonical_context: settlements-infrastructure
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <settlement|municipality|census_place|townsite|ghost_town|fort|mission|community>
source_inputs:
  - source_id: src_settlement_example
    source_role: <authority|observation|administrative|historical|context|aggregate|candidate|synthetic|restricted>
    lifecycle_ref: data/raw/settlements-infrastructure/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
anti_collapse:
  settlement_candidate_is_municipal_authority: false
  census_place_is_municipality: false
  generated_summary_is_evidence: false
spatial_scope:
  place_ref: restricted_or_public_safe_ref
  geometry_ref: restricted_or_public_safe_ref
  public_precision: denied_until_public_safe_transform
temporal_scope:
  source_time: null
  event_time: null
  valid_start: null
  valid_end: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
method:
  transform_family: settlement_alias_candidate_normalization
  algorithm_version: <version>
  parameter_hash: sha256:<hash>
sensitivity:
  restricted_detail_risk: needs_review
  private_property_join_risk: needs_review
  cultural_or_historic_sensitivity: needs_review
  public_release_default: DENY_UNTIL_REVIEW
policy:
  outcome: ABSTAIN
  reason_code: ALIAS_RIGHTS_SENSITIVITY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/settlements-infrastructure/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/settlement/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 11. Tests and validation

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, rights review, sensitivity review, alias-path review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/settlement/
├── test_no_network_dry_run.py                 # PROPOSED
├── test_alias_status_declared.py              # PROPOSED
├── test_no_parallel_authority_paths.py        # PROPOSED
├── test_source_role_required.py               # PROPOSED
├── test_rights_unknown_denied.py              # PROPOSED
├── test_census_place_not_municipality.py      # PROPOSED
├── test_settlement_candidate_not_authority.py # PROPOSED
├── test_restricted_detail_denied.py           # PROPOSED
├── test_sensitive_join_quarantines.py         # PROPOSED
├── test_missing_evidence_abstains.py          # PROPOSED
├── test_receipt_hashes.py                     # PROPOSED
└── test_no_direct_publish.py                  # PROPOSED
```

A dry run should prove:

- fixtures load without network access;
- fixtures are synthetic, generalized, or redacted;
- alias status is declared and does not create parallel authority;
- every input has source identity and source role;
- unknown rights produce `ABSTAIN`, `DENY`, or quarantine;
- settlement candidates, municipalities, census places, historic townsites, and facilities remain distinct;
- restricted details fail closed;
- missing EvidenceBundle support produces `ABSTAIN`;
- invalid records fail validation;
- receipts include input hashes, method hashes, transform refs, output refs, and outcomes;
- no outputs are written to public UI, public API, `data/published/`, or release manifests by default.

[⬆ Back to top](#top)

---

## 12. Promotion, publication, correction, and rollback

Settlement alias pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
settlement source/work input
  -> settlement assertion/candidate
  -> validation report
  -> policy decision
  -> public-safe transform receipt where required
  -> EvidenceBundle closure
  -> processed restricted dataset version under accepted Settlements/Infrastructure lane
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- alias-path migration must preserve receipts, evidence, review state, and rollback targets;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 13. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/settlement/README.md` file;
- explicitly marks `settlement` as an alias/compatibility segment, not a parallel authority root;
- points maintainers to `pipelines/domains/settlements-infrastructure/` for the governing whole-domain pipeline lane;
- preserves source-role, settlement identity, sensitivity, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks direct publication and restricted detail exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this alias lane is done only when it has:

- ADR or path-map justification;
- owners and review burden;
- source-descriptor coverage;
- synthetic/generalized/redacted no-network fixtures;
- schema-backed candidates through the accepted Settlements/Infrastructure schema home;
- contract conformance;
- rights, sensitivity, source-role, temporal, place/spatial, and evidence tests;
- deterministic receipts;
- no-parallel-authority tests;
- no-direct-publish tests;
- CI coverage;
- steward-review handoff;
- release, correction, and rollback documentation.

[⬆ Back to top](#top)

---

## 14. Open questions

| ID | Question | Status |
|---|---|---|
| `SETTLEMENT-PIPE-001` | Should `pipelines/domains/settlement/` remain as compatibility alias, become a Settlement-only sublane, or be removed after ADR resolution? | NEEDS VERIFICATION / ADR |
| `SETTLEMENT-PIPE-002` | Which segment is canonical for pipeline implementation: `settlement` or `settlements-infrastructure`? | NEEDS VERIFICATION / ADR |
| `SETTLEMENT-PIPE-003` | Should Settlement-only processing live here or under `pipelines/domains/settlements-infrastructure/settlement/`? | NEEDS VERIFICATION |
| `SETTLEMENT-PIPE-004` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `SETTLEMENT-PIPE-005` | Which CI job owns Settlement alias-lane invariant tests? | UNKNOWN |
| `SETTLEMENT-PIPE-006` | How should this alias path be linted so it cannot create duplicate schemas, contracts, policies, registries, data lanes, or release lanes? | NEEDS VERIFICATION |
| `SETTLEMENT-PIPE-007` | Which public-safe map/API products are allowed after review and release, and at what redaction/generalization level? | NEEDS VERIFICATION |
| `SETTLEMENT-PIPE-008` | How should cross-lane joins with Roads/Rail, Hydrology, Hazards, People/Land, Archaeology, Agriculture, or Spatial Foundation be denied, restricted, or generalized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with this README as a guardrail. Do not add live source fetching, restricted facility examples, private-property joins, public operational-condition claims, public map layers, release handoff automation, or direct API payload generation until source roles, rights, sensitivity review, public-safe transforms, evidence closure, alias-path governance, and rollback are proven.
