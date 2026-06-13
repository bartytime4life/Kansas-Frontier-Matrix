<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-people-readme
title: People Pipeline Alias README
type: readme
version: v0.1
status: draft
owners:
  - <people-dna-land-pipeline-owner>
  - <people-dna-land-domain-steward>
  - <privacy-steward>
  - <consent-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: restricted-doctrine
path: pipelines/domains/people/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/people-dna-land/README.md
  - docs/domains/people-dna-land/ARCHITECTURE.md
  - docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md
  - docs/domains/people-dna-land/SENSITIVITY.md
  - docs/domains/people-dna-land/PEOPLE_DOMAIN_MODEL.md
  - docs/domains/people-dna-land/sublanes/people.md
  - docs/domains/people-dna-land/sublanes/dna.md
  - docs/domains/people-dna-land/sublanes/land.md
  - pipeline_specs/people-dna-land/
  - pipeline_specs/people/
  - contracts/domains/people-dna-land/
  - contracts/people/
  - schemas/contracts/v1/domains/people-dna-land/
  - schemas/contracts/v1/people/
  - policy/domains/people-dna-land/
  - policy/sensitivity/people-dna-land/
  - policy/consent/people-dna-land/
  - data/raw/people-dna-land/
  - data/work/people-dna-land/
  - data/quarantine/people-dna-land/
  - data/processed/people-dna-land/
  - data/catalog/domain/people-dna-land/
  - data/triplets/people-dna-land/
  - release/candidates/people-dna-land/
  - release/manifests/people-dna-land/
tags:
  - kfm
  - pipelines
  - domains
  - people
  - people-dna-land
  - compatibility-alias
  - genealogy
  - dna
  - land-ownership
  - consent
  - privacy
  - assertion-first
  - evidence
  - policy
  - governance
notes:
  - "This README fills the previously blank pipelines/domains/people/ path as a compatibility/alias lane, not as a new canonical authority root."
  - "The governing bounded context remains People / Genealogy / DNA / Land Ownership unless an ADR resolves the segment naming conflict differently."
  - "Do not create parallel schemas, contracts, source registries, policies, lifecycle data, catalog truth, or release decisions under both people and people-dna-land without ADR/path-map/migration/rollback notes."
  - "Living-person data, DNA/genomic data, raw kit/vendor identifiers, exact burial coordinates, and private person-parcel joins are deny-by-default."
  - "Assessor/tax records are not title truth, and parcel geometry is not title-boundary proof."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, consent wiring, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🧍 People Pipeline Alias

> Compatibility README for the requested `pipelines/domains/people/` path. This path must not become a parallel authority beside `pipelines/domains/people-dna-land/`. Until an ADR resolves segment naming, use this path only for carefully bounded People-sublane executable work or compatibility documentation that preserves People / Genealogy / DNA / Land controls.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-people%20alias%20lane-2e7d32)
![authority](https://img.shields.io/badge/authority-compatibility%20not%20canonical-d62728)
![sensitivity](https://img.shields.io/badge/T4%20deny--by--default-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/people/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain posture:** `people` is a compatibility/alias segment for the People / Genealogy / DNA / Land bounded context  
**Placement posture:** `CONFLICTED / NEEDS VERIFICATION` until the `people` vs `people-dna-land` segment naming conflict is resolved by ADR, path map, migration note, and rollback note  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, rights, consent where applicable, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Alias and authority posture](#2-alias-and-authority-posture)
- [3. Sensitivity and consent boundary](#3-sensitivity-and-consent-boundary)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Relationship to people-dna-land](#6-relationship-to-people-dna-land)
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

`pipelines/domains/people/` is a requested compatibility lane for People-sublane executable pipeline work.

This README does **not** establish `people` as a new canonical domain root. It exists to prevent ambiguity while the repo carries both segment forms:

- `people-dna-land` — visible KFM bounded-context name used by the People / Genealogy / DNA / Land documentation set;
- `people` — a shorter segment referenced in some schema/contract/policy crosswalks and now represented by this pipeline path.

Use this README to keep the alias safe. The governing semantics, privacy posture, consent posture, title-boundary posture, and release posture are inherited from People / Genealogy / DNA / Land.

This path may support narrow People-sublane transformations such as:

- person assertions;
- name assertions;
- person identity candidates;
- life events;
- residence events;
- migration events;
- relationship assertions;
- family groups;
- public-safe, release-reviewed person-context derivatives.

It must not become the home for DNA pipeline logic, land-title/parcel pipeline logic, whole-domain source registries, schemas, policy, lifecycle data, catalog truth, or release decisions unless a future ADR explicitly changes the boundary.

[⬆ Back to top](#top)

---

## 2. Alias and authority posture

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/people/`? | User requested this path, and People appears as a short segment in the People/DNA/Land naming conflict. | PROPOSED / NEEDS VERIFICATION |
| Is `people` canonical? | Not proven. The visible domain docs identify `people-dna-land` as the bounded context and record `people` vs `people-dna-land` as an open conflict. | CONFLICTED / NEEDS ADR |
| What is canonical today? | Treat `people-dna-land` as the governing bounded-context lane for docs and controls until ADR resolution. | CONFIRMED documentation posture; implementation NEEDS VERIFICATION |
| Can this path create parallel authority? | No. It must not create duplicate schemas, contracts, policies, registries, data lanes, or release lanes. | CONFIRMED governance posture |
| Where do declarative specs live? | Prefer `pipeline_specs/people-dna-land/`; `pipeline_specs/people/` is alias-candidate only until ADR. | NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/people-dna-land/` unless ADR resolves otherwise. | PROPOSED / NEEDS VERIFICATION |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> The alias must not weaken the controls of the parent bounded context. A short path is not permission to publish living-person, DNA, relationship, title, parcel, or person-parcel claims.

[⬆ Back to top](#top)

---

## 3. Sensitivity and consent boundary

People-sublane work inherits the strict People/DNA/Land boundary:

- living-person fields are deny-by-default;
- DNA-derived relationship hypotheses are restricted even if a People-sublane pipeline references them;
- raw DNA kit IDs, vendor identifiers, match lists, and segment details must not appear here;
- consent scope, purpose, retention, and revocation must be enforced where applicable;
- exact burial coordinates and culturally sensitive family/place context fail closed;
- generated summaries cannot convert assertions or hypotheses into confirmed truth;
- graph projections cannot replace canonical review state;
- public derivatives require release review, rollback, correction path, and public-safe transform receipts.

Disallowed collapses:

```text
Person assertion -> public person truth
Relationship hypothesis -> confirmed relationship
DNA hint -> public kinship claim
Living-person record -> public profile
Generated summary -> evidence
People alias path -> canonical domain authority
```

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here only if an ADR, path map, or maintainer decision intentionally uses `people` as a compatibility or People-sublane pipeline segment.

Appropriate contents may include:

- this README documenting alias limits;
- fixture-only dry-run entrypoints using synthetic/redacted people data;
- person-assertion and name-assertion normalizers;
- life-event, residence-event, and migration-event normalizers;
- relationship-assertion candidate builders that do not touch DNA evidence directly;
- living-person boundary validators;
- assertion-first validators;
- public-safe person-context transform helpers, if not centralized elsewhere;
- quarantine routing helpers for living-person, relationship, identity, rights, or sensitivity failures;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code narrowly transforms People-sublane lifecycle inputs into assertion candidates, processed restricted records, restricted catalog/triplet handoffs, receipts, or review handoffs, and does not create a parallel People/DNA/Land authority, it may belong here. Otherwise use `pipelines/domains/people-dna-land/` or the correct responsibility root.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/people-dna-land/` or approved registry home |
| People/DNA/Land architecture / doctrine | `docs/domains/people-dna-land/...` |
| Whole-domain pipeline logic | `pipelines/domains/people-dna-land/` unless ADR resolves otherwise |
| DNA tokenization, raw DNA evidence handling, DNA segment processing | `pipelines/domains/people-dna-land/` or restricted DNA sublane after ADR/review |
| Land instruments, assessor records, parcel versions, title-boundary checks | `pipelines/domains/people-dna-land/` or land sublane after ADR/review |
| Object meaning contracts | `contracts/domains/people-dna-land/`, `contracts/people/`, or accepted ADR home |
| JSON Schemas | `schemas/contracts/v1/domains/people-dna-land/`, `schemas/contracts/v1/people/`, or accepted ADR home |
| Policy, consent, sensitivity, retention, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/people-dna-land/` or accepted spec home |
| Fixtures | `fixtures/domains/people-dna-land/` or accepted fixture home |
| Tests | `tests/pipelines/domains/people/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/people-dna-land/`, `release/manifests/people-dna-land/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Legal, genealogical, biological, living-person, or title determinations | Outside this executable pipeline lane |

> [!WARNING]
> Do not use this path as a workaround for the heavier controls in `people-dna-land`. The alias exists to reduce confusion, not to reduce governance.

[⬆ Back to top](#top)

---

## 6. Relationship to people-dna-land

`pipelines/domains/people-dna-land/README.md` is the broader pipeline contract for the full People / Genealogy / DNA / Land Ownership lane.

This alias README must stay subordinate to it until an ADR says otherwise:

```text
pipelines/domains/people-dna-land/   # governing whole-domain executable lane
pipelines/domains/people/            # compatibility / People-sublane alias candidate
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

Every People alias pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal alias-lane stance:

1. **Read** approved synthetic/redacted fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, temporal scope, spatial/place scope, assertion status, living-person posture, consent state where applicable, evidence references, and public-safe transform posture.
3. **Quarantine** unresolved rights, living-person exposure, identity-resolution risk, relationship-hypothesis exposure, missing consent where applicable, schema drift, sensitivity risk, or validation failure.
4. **Promote to processed** only after validation, policy, consent where applicable, evidence, sensitivity/public-safe transform, review, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with sensitivity-safe payloads.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a move from one lifecycle folder to another as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 8. Required gates

Every People alias pipeline run must check or explicitly fail closed on:

1. **Alias gate** — the run must declare whether `people` is alias, compatibility, or ADR-approved canonical segment.
2. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
3. **Source-role gate** — assertion, administrative, aggregate, candidate, synthetic, and context records are not silently collapsed.
4. **Living-person gate** — living-person fields and joins are denied from public release unless explicit policy approval and lawful/public-safe basis close.
5. **Consent gate** — consent scope, purpose, retention, revocation, and dereference-time enforcement close where applicable.
6. **Relationship hypothesis gate** — relationship hypotheses remain hypotheses unless evidence and review close; generated language cannot promote them.
7. **Rights gate** — unknown or restrictive license, permission, attribution, privacy, or redistribution terms block public release.
8. **Sensitivity gate** — exact burial coordinates, cultural/family sensitivity, living-person, private land-interest, and identity-resolution risks fail closed.
9. **Public-safe transform gate** — public products require approved redaction, aggregation, pseudonymization, delay, restriction, or denial decisions with receipts.
10. **Temporal gate** — source time, event time, valid time, assertion time, consent time, revocation time, processing time, catalog time, and release time remain distinct.
11. **Spatial/place gate** — place, residence, parcel references, geometry, legal-description, and public-safe spatial transforms remain distinct.
12. **Schema gate** — candidate and processed records match approved schemas.
13. **Contract gate** — object meanings match People/DNA/Land contracts and do not invent new semantics silently.
14. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
15. **Policy gate** — policy decisions are finite and recorded; no silent allow.
16. **Validation gate** — validators exercise pass, fail, restrict, abstain, deny, and error paths, not only success.
17. **Receipt gate** — every run records input refs, versions, parameters, transforms, consent refs, hashes, output refs, and outcomes.
18. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.
19. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical records or review state.
20. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended alias-safe shape:

```text
pipelines/domains/people/
├── README.md                         # this file; alias / compatibility contract
├── PIPELINE_CONTRACT.md              # PROPOSED only after ADR/path decision
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixtures only
├── normalize_person_assertion.py     # PROPOSED
├── normalize_name_assertion.py       # PROPOSED
├── normalize_life_event.py           # PROPOSED
├── normalize_residence_event.py      # PROPOSED
├── normalize_relationship_assertion.py # PROPOSED; no raw DNA evidence handling here
├── validate_living_person_boundary.py # PROPOSED
├── validate_assertion_first.py       # PROPOSED
├── apply_public_safe_transform.py    # PROPOSED; may belong in shared tools if reused
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_people_candidate.py      # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Do not create these parallel authority homes without ADR:

```text
schemas/contracts/v1/domains/people/
contracts/domains/people/
policy/domains/people/
data/raw/people/
data/processed/people/
release/manifests/people/
```

Generated outputs must not be written beside the code that generated them. Use accepted lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Minimal alias-lane candidate record

The final schema is not defined here. This example shows the minimum information a People alias-lane candidate should preserve.

```yaml
schema_version: kfm.people_alias_pipeline_candidate.v1
candidate_id: people_<object_family>_<run_id>_<hash>
pipeline_id: domains.people
alias_status: NEEDS_VERIFICATION
canonical_context: people-dna-land
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <person_assertion|name_assertion|life_event|residence_event|migration_event|relationship_assertion|identity_candidate>
source_inputs:
  - source_id: src_people_example
    source_role: <assertion|administrative|context|aggregate|candidate|synthetic|restricted>
    lifecycle_ref: data/raw/people-dna-land/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
anti_collapse:
  person_assertion_is_canonical_person: false
  relationship_hypothesis_is_confirmed: false
  dna_hint_is_public_relationship_truth: false
  generated_summary_is_evidence: false
consent:
  required: unknown
  consent_grant_ref: null
  revocation_receipt_ref: null
  dereference_allowed: false
temporal_scope:
  source_time: null
  event_time: null
  valid_start: null
  valid_end: null
  consent_time: null
  revocation_time: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
sensitivity:
  living_person_risk: needs_review
  identity_resolution_risk: needs_review
  family_context_risk: needs_review
  public_release_default: DENY
policy:
  outcome: ABSTAIN
  reason_code: ALIAS_CONSENT_SENSITIVITY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/people-dna-land/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/people/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 11. Tests and validation

Default execution is **fixture-only, synthetic/redacted, consent-scoped, and no-network** until source activation, rights review, consent review, sensitivity review, alias-path review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/people/
├── test_no_network_dry_run.py                 # PROPOSED
├── test_alias_status_declared.py              # PROPOSED
├── test_no_parallel_authority_paths.py        # PROPOSED
├── test_no_real_living_person_fixture.py      # PROPOSED
├── test_source_role_required.py               # PROPOSED
├── test_rights_unknown_denied.py              # PROPOSED
├── test_living_person_public_denied.py        # PROPOSED
├── test_revoked_consent_blocks_dereference.py # PROPOSED
├── test_relationship_hypothesis_not_confirmed.py # PROPOSED
├── test_missing_evidence_abstains.py          # PROPOSED
├── test_receipt_hashes.py                     # PROPOSED
└── test_no_direct_publish.py                  # PROPOSED
```

A dry run should prove:

- fixtures load without network access;
- fixtures are synthetic/redacted and contain no real living-person examples;
- alias status is declared and does not create parallel authority;
- every input has source identity and source role;
- unknown rights produce `ABSTAIN`, `DENY`, or quarantine;
- missing, expired, out-of-scope, or revoked consent blocks downstream use where applicable;
- relationship hypotheses remain hypotheses;
- missing EvidenceBundle support produces `ABSTAIN`;
- invalid records fail validation;
- receipts include input hashes, method hashes, consent refs, revocation refs, transform refs, output refs, and outcomes;
- no outputs are written to public UI, public API, `data/published/`, or release manifests by default.

[⬆ Back to top](#top)

---

## 12. Promotion, publication, correction, and rollback

People alias pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
people source/work input
  -> people assertion candidate
  -> validation report
  -> policy decision
  -> consent / revocation check where required
  -> public-safe transform receipt where required
  -> EvidenceBundle closure
  -> processed restricted dataset version under accepted People/DNA/Land lane
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, revoked, restricted, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- consent revocation invalidates downstream dereference/release where applicable;
- alias-path migration must preserve receipts, evidence, review state, and rollback targets;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 13. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/people/README.md` file;
- explicitly marks `people` as an alias/compatibility segment, not a parallel authority root;
- points maintainers to `pipelines/domains/people-dna-land/` for the governing whole-domain pipeline contract;
- preserves living-person, consent, revocation, assertion-first, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks direct publication and sensitive personal exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this alias lane is done only when it has:

- ADR or path-map justification;
- owners and review burden;
- source-descriptor coverage;
- synthetic/redacted no-network fixtures;
- schema-backed candidates through the accepted People/DNA/Land schema home;
- contract conformance;
- rights, sensitivity, consent, revocation, temporal, place/spatial, and evidence tests;
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
| `PEOPLE-PIPE-001` | Should `pipelines/domains/people/` remain as compatibility alias, become a People-only sublane, or be removed after ADR resolution? | NEEDS VERIFICATION / ADR |
| `PEOPLE-PIPE-002` | Which segment is canonical for contracts, schemas, specs, policy, and data lanes: `people-dna-land` or `people`? | CONFLICTED / NEEDS ADR |
| `PEOPLE-PIPE-003` | Should People-only processing live here or under `pipelines/domains/people-dna-land/people/`? | NEEDS VERIFICATION |
| `PEOPLE-PIPE-004` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `PEOPLE-PIPE-005` | Which CI job owns People alias-lane invariant tests? | UNKNOWN |
| `PEOPLE-PIPE-006` | How should this alias path be linted so it cannot create duplicate schemas, contracts, policies, registries, data lanes, or release lanes? | NEEDS VERIFICATION |
| `PEOPLE-PIPE-007` | Which public-safe map/API products are allowed after review and release, and at what redaction/generalization level? | NEEDS VERIFICATION |

---

## Maintainer note

Start with this README as a guardrail. Do not add live source fetching, raw DNA identifiers, real living-person fixture examples, private relationship disclosure, person-parcel joins, legal-title assertions, public map layers, release handoff automation, or direct API payload generation until source roles, rights, consent/revocation enforcement, public-safe transforms, evidence closure, alias-path governance, and rollback are proven.
