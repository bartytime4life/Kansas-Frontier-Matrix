<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-publish-fauna-readme
title: Fauna Publish Adapter README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <publish-steward>
  - <fauna-domain-steward>
  - <release-steward>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/publish/fauna/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/release-discipline.md
  - docs/standards/RELEASE_MANIFEST.md
  - pipelines/README.md
  - pipelines/publish/README.md
  - pipelines/domains/fauna/README.md
  - docs/domains/fauna/ARCHITECTURE.md
  - pipeline_specs/publish/fauna.yaml
  - data/catalog/domain/fauna/
  - data/triplets/
  - data/published/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/
  - release/manifests/
tags: [kfm, pipelines, publish, fauna, adapter, release-manifest, evidence-bundle, review-record, rollback, correction, governance]
notes:
  - "This README fills the blank pipelines/publish/fauna path as a Fauna adapter/profile under the shared publish-readiness lane."
  - "This path is readiness support only. It is not release authority and does not own Fauna truth, ReleaseManifests, EvidenceBundles, catalog records, or public serving behavior."
  - "Long-term placement remains NEEDS VERIFICATION / ADR if this adapter hardens beyond profile support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Publish Adapter

> Shared publish-readiness adapter/profile for Fauna releases. It checks release-candidate refs, public-safe artifact refs, EvidenceBundle closure, review state, ReleaseManifest inputs, rollback targets, correction paths, and release-steward handoffs without approving release or changing public surfaces directly.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-fauna%20publish%20adapter-2e7d32)
![authority](https://img.shields.io/badge/authority-readiness%20support%20only-0a7ea4)
![release](https://img.shields.io/badge/release%20authority-separate-d62728)

**Status:** Draft  
**Path:** `pipelines/publish/fauna/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Sublane:** Shared publish / Fauna adapter-profile support  
**Placement posture:** `PROPOSED / NEEDS VERIFICATION`; use this only as a shared adapter/profile lane. Domain-owned Fauna publish support remains under `pipelines/domains/fauna/` unless an ADR or migration note says otherwise.  
**Public posture:** no release decision here; outputs are readiness checks, blocker reports, manifest-input packages, receipt fragments, and release-steward handoffs only.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Anti-collapse rules](#3-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Adapter scope](#6-adapter-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal adapter readiness receipt](#11-minimal-adapter-readiness-receipt)
- [12. Definition of done](#12-definition-of-done)
- [13. Open questions](#13-open-questions)

---

## 1. Purpose

`pipelines/publish/fauna/` is a Fauna-specific adapter/profile under the shared publish-readiness lane.

It may support reusable readiness checks for:

- Fauna release-candidate packets;
- catalog and triplet refs for Fauna release products;
- EvidenceBundle refs supporting release-facing Fauna claims;
- ReviewRecord refs and separation-of-duties posture;
- ReleaseManifest input packages for Fauna artifacts;
- artifact digests and manifest inputs;
- representation-control receipts required by the Fauna domain lane;
- rollback target and correction path refs;
- trust-membrane checks for Fauna public surfaces.

This directory implements **adapter support** only. It does not replace `pipelines/domains/fauna/`, does not own Fauna object meaning, does not approve release state, does not author final ReleaseManifests, does not create EvidenceBundles, does not decide review state, and does not change public-serving behavior directly.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable readiness-check logic: the **how**. | CONFIRMED root responsibility |
| Why `publish/`? | Parent lane holds shared publish-readiness helpers and adapter profiles. | CONFIRMED parent-lane posture |
| Why `fauna/` under shared publish? | It can hold Fauna-specific adapter glue for shared helpers, but should not become primary domain authority. | PROPOSED / NEEDS VERIFICATION |
| Does this replace `pipelines/domains/fauna/`? | No. Fauna domain behavior remains under the domain pipeline lane. | CONFIRMED boundary posture |
| Is this release authority? | No. Release decisions, manifests, approvals, and release records remain in release responsibility roots. | CONFIRMED authority separation |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> This folder is an adapter/profile lane, not a canonical Fauna release or publish authority. If it starts owning full domain publish behavior, it should move to `pipelines/domains/fauna/publish/` or be governed by an ADR.

[⬆ Back to top](#top)

---

## 3. Anti-collapse rules

Disallowed collapses:

```text
adapter pass -> release approval
release candidate -> PUBLISHED
adapter output -> final ReleaseManifest
representation candidate -> release artifact
catalog/triplet projection -> public truth
EvidenceRef -> EvidenceBundle
generated publish summary -> evidence
pipeline run -> release authority
```

Required distinctions:

- release candidate, catalog record, triplet projection, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, CorrectionNotice, release artifact, and publish receipt remain separate;
- Fauna object-family ownership remains in the Fauna domain lane;
- representation boundaries remain labeled through publish checks;
- publish support can emit blockers and readiness reports but cannot decide release state;
- every release-facing claim resolves evidence or abstains.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include:

- fixture-only Fauna publish-readiness entrypoints;
- Fauna release-candidate validators;
- Fauna catalog/triplet closure checkers;
- EvidenceBundle and ReviewRecord readiness helpers;
- release artifact digest checkers;
- representation receipt validators;
- ReleaseManifest input validators for Fauna artifacts;
- rollback target and correction path validators;
- trust-membrane checks for Fauna public surfaces;
- publish readiness blocker builders;
- handoff helpers that return control to release stewards or Fauna domain lanes.

A good placement test:

> If the code adapts shared publish-readiness helpers for Fauna while returning control to release authority, it may belong here. If it approves release, authors final release records, owns Fauna truth, or changes public serving behavior directly, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Primary Fauna domain workflow | `pipelines/domains/fauna/` or accepted Fauna sublane |
| Full domain-specific publish workflow | `pipelines/domains/fauna/publish/` if/when accepted |
| Release decisions, manifests, approvals | `release/` |
| Correction or rollback decision records | `release/` or accepted correction/rollback homes |
| Fauna doctrine and object meaning | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| JSON Schemas | `schemas/contracts/v1/domains/fauna/` or accepted schema home |
| Review and decision policy | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, review roots |
| Fixtures | `fixtures/publish/fauna/` or `fixtures/domains/fauna/` |
| Tests | `tests/pipelines/publish/fauna/` or domain test homes |
| Lifecycle data | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, `data/processed/fauna/`, `data/catalog/domain/fauna/`, `data/published/layers/fauna/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Adapter scope

| Scope area | Adapter responsibility | Failure behavior |
|---|---|---|
| Caller authority | Require release steward, Fauna publish lane, or approved publish drill scope. | Hold if ownerless. |
| Release candidate | Resolve Fauna release-candidate refs, artifact refs, digests, and release-state refs. | Fail readiness. |
| Fauna release class | Preserve object-family labels and representation boundaries. | Fail on collapse. |
| Evidence/review | Resolve EvidenceBundle and ReviewRecord refs required for release-facing claims. | Hold or abstain. |
| Representation refs | Verify release artifacts carry required representation-control refs. | Emit blockers. |
| Manifest inputs | Verify ReleaseManifest input package is complete and hashable. | Emit blockers. |
| Rollback/correction | Verify rollback target, correction path, and invalidation posture. | Emit blockers. |
| Handoff | Return readiness report and blockers to release authority. | No release mutation side effects. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Fauna publish support must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** fixture, Fauna release candidate, catalog, triplet, EvidenceBundle, ReviewRecord, representation-control receipt, artifact, and receipt refs provided by an authorized caller.
2. **Verify** candidate closure, artifact digests, evidence refs, review refs, representation refs, ReleaseManifest inputs, rollback target, correction path, and trust-membrane posture.
3. **Emit** Fauna publish-readiness reports, receipts, blockers, and manifest-input handoffs.
4. **Return** to release authority for approval and state transition.
5. **Never approve release, create EvidenceBundles, author final ReleaseManifests, or change public surfaces directly.**

[⬆ Back to top](#top)

---

## 8. Required gates

Every Fauna publish adapter run must check or fail closed on:

1. **Caller authority gate** — release steward, Fauna publish lane, or approved drill scope must be present.
2. **Candidate lifecycle gate** — input is CATALOG/TRIPLET, release candidate, or approved publish fixture.
3. **Fauna object-family gate** — Fauna domain object-family boundaries are preserved.
4. **Representation boundary gate** — release-safe and non-release representations remain distinct.
5. **Representation receipt gate** — transform and representation receipt refs are checked where required.
6. **Evidence gate** — required EvidenceRefs resolve to EvidenceBundles.
7. **Review gate** — ReviewRecord state and steward handoff are present where required.
8. **Manifest-input gate** — ReleaseManifest inputs are complete, hashable, and content-addressed.
9. **Rollback gate** — rollback target is explicit and resolvable.
10. **Correction gate** — correction path and invalidation posture are explicit.
11. **Trust-membrane gate** — public clients would read only governed APIs and released artifacts.
12. **No-direct-release gate** — adapter support does not author or approve final ReleaseManifests.
13. **No-direct-public-serving gate** — adapter support does not change public serving state as a side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/publish/fauna/
├── README.md
├── FAUNA_PUBLISH_ADAPTER_CONTRACT.md  # PROPOSED
├── run_dry_fixture.py                 # PROPOSED
├── validate_release_candidate.py      # PROPOSED
├── validate_evidence_closure.py       # PROPOSED
├── validate_review_state.py           # PROPOSED
├── validate_representation_refs.py    # PROPOSED
├── validate_manifest_inputs.py        # PROPOSED
├── validate_rollback_target.py        # PROPOSED
├── validate_correction_path.py        # PROPOSED
├── check_trust_membrane.py            # PROPOSED
├── emit_adapter_receipt_fragment.py   # PROPOSED
└── adapters/                          # PROPOSED caller adapters only
```

Declarative specs should live outside this directory:

```text
pipeline_specs/publish/fauna.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use the owning Fauna domain/release homes under `release/`, `data/receipts/pipeline/`, and approved release-candidate homes.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Adapter fixture | `fixtures/publish/fauna/` or accepted fixture home | Synthetic/public-safe by default. |
| Caller scope | release steward, `pipelines/domains/fauna/`, or approved drill | Required; this adapter does not run ownerless. |
| Release candidate | `release/candidates/` | Read-only input unless release authority updates. |
| Fauna catalog/triplet refs | `data/catalog/domain/fauna/`, `data/triplets/` | Must resolve by stable ref/digest. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced and resolved; not created here. |
| Manifest input package | `release/candidates/` or accepted readiness home | Handoff only. |
| Receipt fragment | `data/receipts/pipeline/fauna/publish/` or accepted receipt home | Inputs, checks, blockers, output refs. |
| Final ReleaseManifest | `release/manifests/` | Release authority owns approval and write. |
| Published artifact | `data/published/` or accepted release output home | Written only by approved release workflow. |

[⬆ Back to top](#top)

---

## 11. Minimal adapter readiness receipt

```yaml
schema_version: kfm.publish.fauna_adapter_receipt.v1
adapter_run_id: fauna_publish_adapter_run_YYYYMMDDThhmmssZ
pipeline_id: publish.fauna
status: HELD
caller:
  owner: release-steward-or-fauna-publish-lane
  profile_ref: pipeline_specs/publish/fauna.yaml
candidate:
  release_candidate_ref: release/candidates/fauna/<candidate>.json
  catalog_refs: []
  triplet_refs: []
  artifact_refs: []
fauna:
  release_classes: []
  representation_receipt_refs: []
checks:
  candidate_resolved: false
  fauna_boundaries_preserved: false
  representation_boundaries_preserved: false
  evidence_bundle_refs_resolved: false
  review_ready: false
  manifest_inputs_ready: false
  rollback_target_ready: false
  correction_path_ready: false
  trust_membrane_preserved: false
anti_collapse:
  adapter_pass_is_release_approval: false
  release_candidate_is_published: false
  adapter_output_is_final_manifest: false
  representation_candidate_is_release: false
outputs:
  readiness_report_ref: null
  manifest_input_ref: null
  blocker_refs: []
  receipt_fragment_ref: data/receipts/pipeline/fauna/publish/run_YYYYMMDDThhmmssZ.yml
```

[⬆ Back to top](#top)

---

## 12. Definition of done

This README is done when it:

- fills the blank `pipelines/publish/fauna/README.md` file;
- identifies this directory as a Fauna adapter/profile under the shared publish-readiness lane;
- prevents primary Fauna domain logic, release-decision authority, schemas, contracts, policy, lifecycle data, EvidenceBundles, public API, UI, catalog, triplet, and publication authority from being placed here;
- preserves caller authority, release candidate, Fauna object-family, representation boundaries, EvidenceBundle, ReviewRecord, ReleaseManifest, rollback target, correction path, receipt, and trust-membrane boundaries;
- blocks adapter-pass-as-release-approval, release-candidate-as-PUBLISHED, adapter-output-as-final-ReleaseManifest, representation-candidate-as-release, generated-summary-as-evidence, and direct public-serving changes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this adapter lane is done only when it has public-safe publish fixtures, no-network tests, candidate/evidence/review/manifest/rollback/correction/trust-membrane tests, Fauna object-family and representation-boundary tests, representation receipt tests, deterministic receipts, CI coverage, release-steward handoff, and post-release verification documentation.

[⬆ Back to top](#top)

---

## 13. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-PUBLISH-FAUNA-001` | Should this adapter remain under `pipelines/publish/fauna/`, or should it move to `pipelines/domains/fauna/publish/` once domain publish scaffolding is accepted? | NEEDS VERIFICATION / ADR |
| `PIPE-PUBLISH-FAUNA-002` | Which schema owns Fauna publish readiness receipts, manifest-input packages, and blocker reason codes? | NEEDS VERIFICATION |
| `PIPE-PUBLISH-FAUNA-003` | Which Fauna release fixture set should be first-wave for no-network publish drills? | NEEDS VERIFICATION |
| `PIPE-PUBLISH-FAUNA-004` | Which CI job owns shared Fauna publish adapter invariant tests? | UNKNOWN |
| `PIPE-PUBLISH-FAUNA-005` | Should this adapter emit receipt fragments only, or full Fauna publish readiness reports? | NEEDS VERIFICATION |
| `PIPE-PUBLISH-FAUNA-006` | Which representation receipt vocabulary is canonical for Fauna publish checks? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Start with synthetic/public-safe publish fixtures and negative tests. Do not add release-decision authority, Fauna truth ownership, schema authority, policy authority, public API code, UI code, release-manifest writes, published-layer writes, or generated summaries until caller authority, release-candidate refs, Fauna object-family checks, representation boundaries, representation receipt refs, EvidenceBundle refs, review state, rollback targets, correction paths, trust-membrane checks, deterministic receipts, and post-release verification are proven.
