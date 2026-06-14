<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-publish-readme
title: Publish Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <publish-steward>
  - <release-steward>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/publish/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/release-discipline.md
  - docs/standards/RELEASE_MANIFEST.md
  - pipelines/README.md
  - pipelines/validate/README.md
  - pipelines/catalog/README.md
  - pipelines/triplets/README.md
  - pipelines/rollback/README.md
  - pipeline_specs/publish/
  - pipelines/domains/
  - tests/pipelines/publish/
  - fixtures/publish/
  - data/catalog/
  - data/triplets/
  - data/published/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/
  - release/manifests/
tags: [kfm, pipelines, publish, release, release-manifest, trust-membrane, evidence-bundle, review-record, rollback, correction, governance]
notes:
  - "This README replaces the greenfield stub at pipelines/publish/README.md with a governed implementation-lane contract."
  - "pipelines/ is executable pipeline logic; pipeline_specs/ is declarative configuration."
  - "This lane checks publish readiness. It is not release authority and does not own ReleaseManifests, policy decisions, EvidenceBundles, catalog truth, or public serving behavior."
  - "Domain-specific publish support remains under domain lanes unless an ADR says otherwise."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Publish Pipelines

> Shared executable publish-readiness lane for checking release candidates, EvidenceBundle closure, review state, manifest inputs, rollback targets, correction paths, and release-steward handoffs.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-shared%20publish%20readiness-2e7d32)
![authority](https://img.shields.io/badge/authority-readiness%20support%20only-0a7ea4)
![release](https://img.shields.io/badge/release%20authority-separate-d62728)

**Status:** Draft  
**Path:** `pipelines/publish/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Sublane:** Shared publish-readiness support  
**Placement posture:** implementation sublane under `pipelines/`; long-term framework authority remains `NEEDS VERIFICATION / ADR`.  
**Public posture:** no release decision here; outputs are readiness checks, blocker reports, manifest-input packages, receipt fragments, and release-steward handoffs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Anti-collapse rules](#3-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Readiness scope](#6-readiness-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal readiness receipt](#11-minimal-readiness-receipt)
- [12. Tests and fixtures](#12-tests-and-fixtures)
- [13. Definition of done](#13-definition-of-done)
- [14. Open questions](#14-open-questions)

---

## 1. Purpose

`pipelines/publish/` is the shared executable lane for publish-readiness support that can be reused by domain publish lanes and release-steward workflows.

It may support:

- release-candidate input checks;
- catalog and triplet closure checks;
- EvidenceBundle resolution checks;
- ReviewRecord readiness checks;
- rights, sensitivity, redaction, aggregation, and public-representation checks;
- ReleaseManifest input checks;
- artifact digest and manifest preflight checks;
- rollback target and correction path checks;
- trust-membrane checks;
- publish-readiness receipt and blocker builders;
- domain publish adapter helpers.

This directory implements the **how** of publish-readiness checking and handoff. It does not approve release, author final ReleaseManifests, own catalog truth, create EvidenceBundles, decide policy or review state, or serve public clients.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | Publish helpers are executable logic: the **how**. | CONFIRMED root responsibility |
| Why a shared `publish/` lane? | It can hold reusable readiness helpers for domain and release lanes. | PROPOSED / NEEDS VERIFICATION |
| Does this replace domain publish lanes? | No. Domain-owned publish support stays under domain lanes unless an ADR says otherwise. | CONFIRMED boundary posture |
| Is this release authority? | No. Release decisions, manifests, and approval records remain in release responsibility roots. | CONFIRMED authority separation |
| Is this public-client authority? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> Publish readiness is not publication. Publication is a governed transition to PUBLISHED with required artifacts, resolved references, policy decision, review state, ReleaseManifest, correction path, and rollback target.

[⬆ Back to top](#top)

---

## 3. Anti-collapse rules

Disallowed collapses:

```text
helper pass -> release approval
release candidate -> PUBLISHED
manifest input -> final ReleaseManifest
catalog/triplet projection -> public truth
EvidenceRef -> EvidenceBundle
ValidationReport pass -> public release
artifact digest match -> policy approval
generated publish summary -> evidence
pipeline run -> release authority
```

Required distinctions:

- release candidate, catalog record, triplet projection, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, CorrectionNotice, public artifact, and publish receipt remain separate;
- publish support can check readiness and emit blockers but cannot decide release state;
- every public-facing claim must resolve EvidenceBundle support or abstain;
- public clients read only governed APIs or released artifacts.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include:

- fixture-only publish-readiness entrypoints;
- release-candidate validators;
- catalog/triplet closure checkers;
- EvidenceBundle resolution helpers;
- review/readiness checkers;
- artifact digest and manifest input checkers;
- rollback target and correction path validators;
- trust-membrane checkers;
- publish-readiness blocker builders;
- publish receipt builders;
- shared adapters used by domain publish lanes.

A good placement test:

> If the code helps multiple domain or release lanes prove publish readiness without owning the release decision, it may belong here. If it approves release, authors final release records, owns catalog truth, changes public serving behavior directly, or creates evidence, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Domain-specific publish workflows | `pipelines/domains/<domain>/publish/` |
| Release decisions, approvals, manifests | `release/` |
| Correction or rollback decision records | `release/` or accepted correction/rollback homes |
| Public API or UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Domain doctrine | `docs/domains/<domain>/` |
| Schemas | `schemas/contracts/v1/...` accepted schema home |
| Contracts/object meaning | `contracts/...` accepted contract home |
| Policy | `policy/...` responsibility roots |
| Declarative publish specs | `pipeline_specs/publish/` or domain-specific spec homes |
| Fixtures | `fixtures/publish/` or domain fixture homes |
| Tests | `tests/pipelines/publish/` or domain test homes |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Catalog/triplet materialization | `data/catalog/`, `data/triplets/` |
| Published artifacts | `data/published/` or accepted release output homes |

[⬆ Back to top](#top)

---

## 6. Readiness scope

| Scope area | Shared publish responsibility | Failure behavior |
|---|---|---|
| Caller authority | Require release steward, domain publish lane, or approved publish drill scope. | Hold if ownerless. |
| Candidate input | Resolve release candidate, catalog refs, triplet refs, artifact refs, and digests. | Fail readiness. |
| Evidence | Resolve EvidenceRef to EvidenceBundle where claims depend on evidence. | Hold or abstain. |
| Review | Verify ReviewRecord and separation-of-duties posture where required. | Hold. |
| Artifact integrity | Verify digests, manifests, and public-safe representation refs. | Emit blockers. |
| Rollback/correction | Verify rollback target and correction path before handoff. | Emit blockers. |
| Receipts | Emit deterministic publish-readiness receipts. | Fail closed on missing hashes. |
| Handoff | Return readiness report and blockers to release authority. | No public-serving side effects. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Publish support must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** release-candidate refs, catalog refs, triplet refs, EvidenceBundle refs, review refs, artifact refs, and receipt refs provided by an authorized caller.
2. **Verify** required artifacts exist and resolve: EvidenceBundle, SourceDescriptor, ValidationReport, PolicyDecision, ReviewRecord where required, ReleaseManifest inputs, rollback target, and correction path.
3. **Emit** publish-readiness reports, receipts, blockers, and manifest-input handoffs.
4. **Return** to release authority for approval and the final PUBLISHED transition.
5. **Never bypass release authority, alter public-facing outputs directly, or treat copying/deploying as publication.**

[⬆ Back to top](#top)

---

## 8. Required gates

Every shared publish component must check or fail closed on:

1. **Caller authority gate** — release steward, domain publish lane, or approved drill scope must be present.
2. **Candidate lifecycle gate** — input is CATALOG/TRIPLET, release candidate, or approved publish fixture.
3. **Evidence gate** — every required EvidenceRef resolves to an EvidenceBundle.
4. **Source/receipt gate** — required source, model, run, transform, validation, and catalog refs resolve.
5. **Review gate** — review state is present where required.
6. **Rights/sensitivity gate** — rights, sensitivity, redaction, aggregation, or public-safe representation refs are closed.
7. **Manifest-input gate** — ReleaseManifest inputs are complete, hashable, and content-addressed.
8. **Rollback gate** — rollback target is explicit and resolvable.
9. **Correction gate** — correction path and invalidation posture are explicit.
10. **Trust-membrane gate** — public clients would read only governed APIs and released artifacts.
11. **Receipt gate** — readiness invocation emits deterministic receipt/report metadata.
12. **No-direct-release gate** — publish support does not author or approve final ReleaseManifests.
13. **No-direct-public-serving gate** — publish support does not change public serving state as a side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/publish/
├── README.md
├── PUBLISH_SHARED_CONTRACT.md         # PROPOSED
├── run_dry_fixture.py                 # PROPOSED
├── validate_release_candidate.py      # PROPOSED
├── validate_evidence_closure.py       # PROPOSED
├── validate_review_state.py           # PROPOSED
├── validate_manifest_inputs.py        # PROPOSED
├── validate_rollback_target.py        # PROPOSED
├── validate_correction_path.py        # PROPOSED
├── check_trust_membrane.py            # PROPOSED
├── build_readiness_report.py          # PROPOSED
├── emit_publish_receipt.py            # PROPOSED only if not shared
└── adapters/                          # PROPOSED domain/release adapters only
```

Declarative specs should live outside this directory:

```text
pipeline_specs/publish/<profile>.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted homes under `data/receipts/pipeline/`, `release/candidates/`, `release/manifests/`, and domain release/publish homes as governed by release stewards.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Publish fixture | `fixtures/publish/` or domain fixture home | Synthetic/public-safe by default. |
| Declarative spec | `pipeline_specs/publish/` or domain spec home | The what, not executable logic. |
| Release candidate | `release/candidates/` | Read-only input unless release authority updates. |
| Catalog/triplet refs | `data/catalog/`, `data/triplets/` | Must resolve by stable ref/digest. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced and resolved; not created here. |
| Manifest input package | `release/candidates/` or accepted readiness home | Handoff only. |
| Receipt | `data/receipts/pipeline/<domain-or-release>/publish/` or accepted receipt home | Records inputs, checks, blockers, and output refs. |
| Final ReleaseManifest | `release/manifests/` | Release authority owns approval and write. |
| Published artifact | `data/published/` or accepted release output home | Written only by approved release workflow. |

[⬆ Back to top](#top)

---

## 11. Minimal readiness receipt

```yaml
schema_version: kfm.shared_publish_readiness_receipt.v1
publish_readiness_run_id: publish_readiness_run_YYYYMMDDThhmmssZ
pipeline_id: publish.<profile_id>
status: HELD
caller:
  owner: release-steward-or-domain-publish-lane
  profile_ref: pipeline_specs/publish/<profile_id>.yaml
candidate:
  release_candidate_ref: release/candidates/<candidate>.json
  catalog_refs: []
  triplet_refs: []
  artifact_refs: []
checks:
  candidate_resolved: false
  evidence_bundle_refs_resolved: false
  source_and_receipt_refs_resolved: false
  review_ready: false
  rights_sensitivity_ready: false
  manifest_inputs_ready: false
  rollback_target_ready: false
  correction_path_ready: false
  trust_membrane_preserved: false
anti_collapse:
  helper_pass_is_release_approval: false
  release_candidate_is_published: false
  manifest_input_is_final_manifest: false
  validation_pass_is_public_release: false
outputs:
  readiness_report_ref: null
  blocker_refs: []
  manifest_input_ref: null
  receipt_ref: data/receipts/pipeline/publish/run_YYYYMMDDThhmmssZ.yml
```

[⬆ Back to top](#top)

---

## 12. Tests and fixtures

Recommended tests:

```text
tests/pipelines/publish/
├── test_no_network_dry_run.py              # PROPOSED
├── test_caller_authority_required.py       # PROPOSED
├── test_release_candidate_required.py      # PROPOSED
├── test_evidence_bundle_refs_required.py   # PROPOSED
├── test_review_required.py                 # PROPOSED
├── test_rights_sensitivity_required.py     # PROPOSED
├── test_manifest_inputs_required.py        # PROPOSED
├── test_rollback_target_required.py        # PROPOSED
├── test_correction_path_required.py        # PROPOSED
├── test_trust_membrane_preserved.py        # PROPOSED
├── test_no_release_manifest_side_effect.py # PROPOSED
└── test_no_direct_public_serving.py        # PROPOSED
```

A dry run should prove fixtures load without network access, caller authority is required, candidate refs resolve, evidence/review/rights/sensitivity refs are checked, manifest inputs are complete, rollback/correction support exists, receipts are deterministic, and no run writes final ReleaseManifests or changes public-serving state as a side effect.

[⬆ Back to top](#top)

---

## 13. Definition of done

This README is done when it:

- replaces the greenfield stub at `pipelines/publish/README.md`;
- identifies this directory as a shared executable publish-readiness support lane under `pipelines/`;
- prevents release-decision authority, domain truth, schemas, contracts, policy, lifecycle data, EvidenceBundles, public API, UI, catalog, triplet, and publication authority from being placed here;
- preserves release candidate, catalog, triplet, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, rollback target, correction path, receipt, and trust-membrane boundaries;
- blocks helper-pass-as-release-approval, release-candidate-as-PUBLISHED, manifest-input-as-final-ReleaseManifest, validation-pass-as-public-release, generated-summary-as-evidence, and direct public-serving changes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this lane is done only when it has public-safe publish fixtures, no-network tests, candidate/evidence/review/rights/sensitivity/manifest/rollback/correction/trust-membrane tests, deterministic receipts, CI coverage, release-steward handoff, and post-release verification documentation.

[⬆ Back to top](#top)

---

## 14. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-PUBLISH-001` | Is `pipelines/publish/` the final accepted home for shared publish-readiness helpers, or should this move under `packages/`, `tools/release/`, or domain lanes by ADR? | NEEDS VERIFICATION / ADR |
| `PIPE-PUBLISH-002` | Which schema owns shared publish-readiness receipts, blocker lists, and manifest-input packages? | NEEDS VERIFICATION |
| `PIPE-PUBLISH-003` | Should every domain publish sublane call shared helpers, or only use them for release-candidate and trust-membrane checks? | NEEDS VERIFICATION |
| `PIPE-PUBLISH-004` | Which CI job owns shared publish invariant tests? | UNKNOWN |
| `PIPE-PUBLISH-005` | Which publish profiles belong in `pipeline_specs/publish/` versus domain-specific specs? | NEEDS VERIFICATION |
| `PIPE-PUBLISH-006` | Should shared publish helpers emit full readiness reports or only receipt fragments for release stewards to adopt? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe publish fixtures and negative tests. Do not add release-decision authority, schema authority, policy authority, domain truth ownership, public API code, UI code, release-manifest writes, published-layer writes, or generated summaries until caller authority, release-candidate refs, EvidenceBundle refs, review state, rights/sensitivity posture, rollback targets, correction paths, trust-membrane checks, deterministic receipts, and post-release verification are proven.
