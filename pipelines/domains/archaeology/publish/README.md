<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-archaeology-publish-readme
title: Archaeology Publish Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <archaeology-pipeline-owner>
  - <archaeology-domain-steward>
  - <publish-artifact-steward>
  - <release-steward>
  - <review-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-archaeology-publication-review-evidence-and-rollback-gates
path: pipelines/domains/archaeology/publish/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/archaeology/README.md
  - pipelines/domains/archaeology/validate/README.md
  - pipelines/domains/archaeology/rollback/README.md
  - docs/domains/archaeology/DATA_LIFECYCLE.md
  - docs/domains/archaeology/VALIDATORS.md
  - docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - docs/domains/archaeology/RELEASE_INDEX.md
  - docs/runbooks/archaeology/ROLLBACK_RUNBOOK.md
  - pipeline_specs/archaeology/publish.yaml
  - contracts/domains/archaeology/
  - schemas/contracts/v1/domains/archaeology/
  - policy/domains/archaeology/
  - policy/sensitivity/archaeology/
  - data/catalog/domain/archaeology/
  - data/triplets/archaeology/
  - data/published/layers/archaeology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/archaeology/
  - release/manifests/archaeology/
tags: [kfm, pipelines, domains, archaeology, publish, release-manifest, layer-manifest, evidence-bundle, policy, rollback-card, correction-notice, governance]
notes:
  - "This README fills the blank pipelines/domains/archaeology/publish path as a nested executable Archaeology publication-artifact sublane."
  - "Publish logic is executable artifact assembly only; it does not own release decisions, ReleaseManifests, RollbackCards, CorrectionNotices, policy, review decisions, EvidenceBundle truth, catalog truth, schemas, source descriptors, or public API authority."
  - "Publication is a governed state transition, not a file move, not a successful pipeline run, and not a UI action."
  - "Public archaeology artifacts require evidence closure, policy allow, review state, public-safe representation, correction path, rollback target, content digests, and receipts."
  - "Concrete executable behavior, CI coverage, release wiring, public API/map behavior, and artifact schemas remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Publish Pipeline

> Executable Archaeology sublane for assembling release-approved public artifacts, layer manifests, tile/extract outputs, Evidence Drawer payload fragments, public-safe labels, correction hooks, rollback refs, and artifact receipts from governed catalog/triplet inputs — without deciding release, bypassing review, exposing internal lifecycle stores, or treating generated text as evidence.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-archaeology%20publish-8a6d3b)
![authority](https://img.shields.io/badge/authority-artifact%20assembly%20only-0a7ea4)
![policy](https://img.shields.io/badge/policy-default%20deny-d62728)
![rollback](https://img.shields.io/badge/rollback-required-d62728)

**Status:** Draft  
**Path:** `pipelines/domains/archaeology/publish/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Archaeology  
**Sublane:** Publish / release-artifact assembly  
**Placement posture:** nested executable sublane under `pipelines/domains/archaeology/`; concrete behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no independent release authority; this lane may assemble only release-approved artifacts with ReleaseManifest, EvidenceBundle, policy, review, correction, and rollback closure.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Publish anti-collapse rules](#3-publish-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Publication-artifact scope](#6-publication-artifact-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal publish receipt](#11-minimal-publish-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Correction, stale state, and rollback](#13-correction-stale-state-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/archaeology/publish/` is the executable sublane for Archaeology publication-artifact assembly.

It supports artifact preparation for:

- release-approved public-safe layer manifests, tile artifacts, extracts, Evidence Drawer fragments, Focus Mode context packets, cards, indexes, and metadata bundles;
- tiered public derivatives of cataloged archaeology records, survey coverage, generalized activity zones, documentation surfaces, chronology summaries, and released candidate-context surfaces;
- ReleaseManifest-bound dataset, layer, tile, EvidenceBundle, PolicyDecision, ReviewRecord, CorrectionNotice, RollbackCard, and artifact-digest refs;
- public attribute include-lists, source-role labels, uncertainty labels, generalization/explanation labels, reality-boundary notes, and Evidence Drawer refs;
- artifact receipts that record digests, input refs, release refs, public representation refs, correction refs, and rollback target refs;
- hold records for missing release decision, missing rollback target, unresolved evidence, unresolved policy, missing review state, unsupported tier, missing transform receipt, or artifact-integrity failure.

This directory implements or will implement the **how** of Archaeology publication artifact assembly. It does not decide release, define ReleaseManifest shape, define policy, decide review outcomes, own EvidenceBundle truth, own catalog truth, own source descriptors, mutate canonical stores, serve public API responses, or create UI state by itself.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/archaeology/`? | Archaeology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path pattern; behavior NEEDS VERIFICATION |
| Why `publish/`? | This sublane assembles release-approved public artifacts and receipts. | PROPOSED / NEEDS VERIFICATION |
| Does this publish by itself? | No. It consumes release-approved inputs and emits artifacts/receipts; release authority lives under `release/`. | CONFIRMED governance posture |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust membrane posture |

> [!IMPORTANT]
> A successful artifact assembly run is not a release decision. Archaeology output is public only when a ReleaseManifest with resolvable EvidenceBundle refs, policy outcomes, ReviewRecords, correction path, and rollback target has authorized the artifact set.

[⬆ Back to top](#top)

---

## 3. Publish anti-collapse rules

Publish-artifact assembly must preserve release authority, evidence bindings, review state, correction state, rollback state, and public-safe representation as separate objects.

Disallowed collapses:

```text
pipeline run -> release approval
copy to published path -> publication
published layer -> canonical archaeology truth
catalog record -> public artifact
candidate feature -> confirmed record
EvidenceRef -> EvidenceBundle
ReleaseManifest -> mutable latest pointer
CorrectionNotice -> silent edit
RollbackCard -> optional metadata
generated public summary -> evidence
public UI payload -> canonical store
style-only hiding -> public-safe transform
```

Required distinctions:

- ReleaseManifest, LayerManifest, EvidenceBundle, ReviewRecord, PolicyDecision, ValidationReport, CorrectionNotice, RollbackCard, catalog record, graph projection, and public artifact remain separate;
- public representation must be transformed or generalized before artifact assembly when policy requires it;
- generated summaries, 3D representations, reconstructions, and AI carriers require representation/reality-boundary receipts before release-facing use;
- public artifacts bind to content hashes and release refs, not floating latest pointers;
- stale, superseded, corrected, withdrawn, denied, and held states remain visible;
- public clients never read RAW, WORK, QUARANTINE, canonical/internal stores, source APIs, graph internals, vector indexes, or direct model outputs.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Archaeology publication-artifact assembly.

Appropriate contents include:

- fixture-only release-artifact dry-run entrypoints;
- ReleaseManifest input validators;
- EvidenceBundle, policy, ReviewRecord, ValidationReport, CorrectionNotice, and RollbackCard presence checks;
- public layer/PMTiles/extract/card/index builders;
- artifact digest and manifest writers;
- public attribute include-list, tier-label, source-role-label, uncertainty-label, and generalization-note injectors;
- reality-boundary, representation, transform, correction, stale, superseded, and withdrawn badge builders;
- artifact-integrity and rollback-target validators;
- publish receipt emitters, if not shared;
- hold routing helpers for missing release preconditions.

A good placement test:

> If the code assembles artifacts from an already-approved Archaeology release candidate and writes content-addressed artifact outputs plus receipts, it may belong here. If it decides release, edits policy, validates source material, owns catalog truth, serves the API, writes UI state, or hides restricted bytes by style alone, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers, API clients, watchers | `connectors/` or watcher roots |
| Source descriptors / source registry entries | `data/registry/sources/archaeology/` or approved registry home |
| Ingest, normalize, validate, catalog, or rollback logic | sibling Archaeology pipeline sublanes |
| Domain doctrine and object meaning | `docs/domains/archaeology/`, `contracts/domains/archaeology/` |
| JSON Schemas | `schemas/contracts/v1/domains/archaeology/` or accepted schema home |
| Policy, rights, review, release rules | `policy/...` and review responsibility roots |
| Release decisions, ReleaseManifest authorship, RollbackCards | `release/...` responsibility roots |
| Fixtures | `fixtures/domains/archaeology/publish/` or accepted fixture home |
| Tests | `tests/pipelines/domains/archaeology/publish/` or accepted test home |
| Lifecycle records | `data/...` lifecycle homes |
| Public API or map viewer code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Direct model summaries or generated answer text | Governed AI/released artifact paths only after review |

[⬆ Back to top](#top)

---

## 6. Publication-artifact scope

| Scope area | Publish-lane responsibility | Failure behavior |
|---|---|---|
| Release input | Confirm release candidate and ReleaseManifest refs are present and resolvable. | Hold; no artifact change. |
| Evidence binding | Confirm EvidenceBundle refs resolve and digests match. | Hold. |
| Validation | Confirm ValidationReport pass and role-boundary denials are honored. | Hold on missing/failed validation. |
| Review/policy | Confirm required ReviewRecords and PolicyDecisions exist. | Hold on missing review/policy. |
| Representation | Confirm tier, transform, representation, and reality-boundary receipts exist where required. | Hold release-facing output. |
| Artifact integrity | Write content-addressed artifacts, manifests, checksums, and receipts. | Fail closed on digest mismatch. |
| Correction/rollback | Carry CorrectionNotice, invalidation expectations, and rollback target. | Hold if missing. |
| Public interface | Produce artifacts for governed API/UI consumption only. | No direct UI/API side effects. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Archaeology publish run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** release-approved inputs only: ReleaseManifest refs, release candidates, catalog/triplet refs, EvidenceBundle refs, ValidationReports, PolicyDecisions, ReviewRecords, CorrectionNotices, rollback targets, and artifact specs.
2. **Verify** every required reference resolves and every digest matches expected inputs.
3. **Assemble** public-safe artifacts such as layers, tiles, extracts, cards, Evidence Drawer fragments, indexes, and manifest sidecars.
4. **Emit** artifact receipts, digests, public-representation refs, correction refs, and rollback refs.
5. **Hold** missing release, evidence, validation, policy, review, transform, correction, rollback, or integrity preconditions.
6. **Never mutate canonical stores, source captures, catalog truth, release decisions, public UI state, or direct API behavior.**

Publish here means artifact assembly after a governed release decision. It is not release approval and not a shortcut from catalog to exposure.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Archaeology publish run must check or explicitly fail closed on:

1. **ReleaseManifest gate** — release identity, contents, digests, evidence refs, rollback target, time, and correction path are present.
2. **EvidenceBundle gate** — all public claims resolve evidence and digest closure passes.
3. **ValidationReport gate** — validation pass exists and role-boundary denials are preserved.
4. **Policy/review gate** — policy outcome and required review state are present; no silent allow.
5. **Representation gate** — tier, generalization, redaction/withholding, representation, and reality-boundary receipts exist where required.
6. **Rights gate** — unresolved rights or source-role uncertainty blocks public promotion.
7. **Artifact digest gate** — artifact content hashes, manifests, tiles, extracts, and indexes match release refs.
8. **Correction gate** — corrected outputs carry CorrectionNotice and invalidation list where required.
9. **Rollback gate** — rollback target is resolvable before artifact assembly.
10. **Trust membrane gate** — outputs are suitable for governed APIs; no client reads internal stores.
11. **No-direct-decision gate** — this lane does not create release decisions or policy decisions.
12. **No-direct-UI/API gate** — no side effects in public UI, public API routes, or direct model responses.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/archaeology/publish/
├── README.md                         # this file
├── PUBLISH_CONTRACT.md               # PROPOSED: Archaeology publish artifact execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/public-safe release fixture only
├── validate_release_manifest.py      # PROPOSED
├── validate_evidence_bundle_refs.py  # PROPOSED
├── validate_validation_report.py     # PROPOSED
├── validate_policy_review.py         # PROPOSED
├── validate_public_representation.py # PROPOSED
├── validate_rollback_target.py       # PROPOSED
├── build_public_layer_manifest.py    # PROPOSED
├── build_public_artifacts.py         # PROPOSED
├── emit_publish_receipt.py           # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/archaeology/publish.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted release/public artifact homes under `data/published/layers/archaeology/`, `data/receipts/`, `release/candidates/archaeology/`, and `release/manifests/archaeology/`, with decisions remaining in `release/` and public serving remaining behind governed API/UI roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/archaeology/publish/` or accepted fixture home | Synthetic/public-safe release fixture. |
| Release candidate | `release/candidates/archaeology/` | Reviewable input only. |
| ReleaseManifest | `release/manifests/archaeology/` | Decision authority, not owned here. |
| Evidence proof | `data/proofs/evidence_bundle/` | Required and resolved before artifact assembly. |
| ValidationReport | `data/processed/archaeology/` or accepted validation-report home | Input by stable ref/digest. |
| Catalog/triplet refs | `data/catalog/domain/archaeology/`, `data/triplets/archaeology/` | Inputs by stable refs/digests. |
| Published artifact | `data/published/layers/archaeology/` or accepted public artifact home | Content-addressed output only. |
| Receipt | `data/receipts/pipeline/archaeology/publish/<run_id>.yml` or accepted receipt home | Records release refs, digests, checks, outputs. |
| Correction / rollback refs | `release/...` | Required refs for release-capable artifacts. |

[⬆ Back to top](#top)

---

## 11. Minimal publish receipt

The final schema is not defined here. This example shows the minimum information an Archaeology publish run should preserve.

```yaml
schema_version: kfm.archaeology_publish_receipt.v1
publish_run_id: archaeology_publish_run_YYYYMMDDThhmmssZ
pipeline_id: domains.archaeology.publish
status: HELD
release:
  release_manifest_ref: release/manifests/archaeology/<release_id>.json
  release_manifest_hash: sha256:<hash>
  release_candidate_ref: release/candidates/archaeology/<candidate_id>.json
inputs:
  catalog_refs: []
  triplet_refs: []
  validation_report_refs: []
  evidence_bundle_refs: []
  policy_decision_refs: []
  review_record_refs: []
  correction_notice_refs: []
  rollback_target_ref: null
publication_controls:
  public_representation_ready: false
  transform_receipts_ready: false
  reality_boundary_notes_ready: false
  rights_review_ready: false
artifacts:
  layer_manifest_ref: null
  tile_artifact_refs: []
  extract_refs: []
  artifact_digests: {}
checks:
  evidence_resolved: false
  validation_resolved: false
  policy_resolved: false
  review_resolved: false
  rollback_resolved: false
  digests_match: false
anti_collapse:
  publish_run_is_release_decision: false
  copied_file_is_publication: false
  public_layer_is_canonical_truth: false
  candidate_feature_is_confirmed_record: false
outputs:
  receipt_ref: data/receipts/pipeline/archaeology/publish/run_YYYYMMDDThhmmssZ.yml
  published_artifact_refs: []
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/public-safe, and no-network** until publish specs, release fixtures, evidence, policy, review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/archaeology/publish/
├── test_no_network_dry_run.py              # PROPOSED
├── test_release_manifest_required.py       # PROPOSED
├── test_evidence_bundle_required.py        # PROPOSED
├── test_validation_report_required.py      # PROPOSED
├── test_policy_review_required.py          # PROPOSED
├── test_public_representation_required.py  # PROPOSED
├── test_rollback_target_required.py        # PROPOSED
├── test_artifact_digests_match_manifest.py # PROPOSED
├── test_no_style_only_hiding.py            # PROPOSED
├── test_no_candidate_as_confirmed_record.py # PROPOSED
├── test_publish_run_not_release_decision.py # PROPOSED
├── test_no_internal_store_exposure.py      # PROPOSED
└── test_no_direct_ui_api_side_effect.py    # PROPOSED
```

A dry run should prove fixtures load without network access, ReleaseManifest and rollback target are required, EvidenceBundle and policy refs resolve, review refs are present, public representation refs are safe, artifacts are content-addressed, receipts are deterministic, correction states are surfaced, and no run mutates release decisions, canonical stores, public UI, or public API routes.

[⬆ Back to top](#top)

---

## 13. Correction, stale state, and rollback

Archaeology publish pipelines may materialize correction and rollback-aware artifacts. They do not approve corrections or rollbacks.

Required chain:

```text
catalog / triplet + EvidenceBundle + policy + review
  -> release candidate
  -> ReleaseManifest + rollback target
  -> publish artifact assembly
  -> artifact receipt + public layer/extract/index
  -> governed API/UI consumption
```

Correction and rollback posture:

- stale is visible and not silently refreshed;
- correction is a governed forward transition, not a silent edit;
- rollback is authenticated and receipt-backed, not ad-hoc cleanup;
- CorrectionNotice, RollbackCard, invalidation lists, and prior release refs stay attached to public artifacts;
- released artifacts are invalidated when source rights, evidence, validation, policy, review, representation, correction, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/archaeology/publish/README.md` file;
- identifies this directory as a nested executable Archaeology publish-artifact sublane;
- prevents source, ingest, normalize, validate, catalog, schema, contract, policy, release-decision, public API, UI, and canonical-store authority from being placed here;
- preserves ReleaseManifest, EvidenceBundle, ValidationReport, PolicyDecision, ReviewRecord, CorrectionNotice, RollbackCard, public representation, catalog/triplet, artifact digest, release, correction, and rollback boundaries;
- blocks pipeline-run-as-release, copy-as-publication, catalog-as-public-artifact, candidate-as-confirmed-record, style-only-hiding-as-transform, generated-summary-as-evidence, direct UI/API side effects, and internal-store exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has release-fixture coverage, schema-backed artifact receipts, ReleaseManifest/EvidenceBundle/ValidationReport/policy/review/representation/rollback/digest tests, deterministic receipts, CI coverage, steward-review handoff, and rollback/correction documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `ARCH-PUB-001` | Should Archaeology publish remain one sublane, or split into layer, tile, extract, Evidence Drawer, Focus Mode, and card artifact builders? | NEEDS VERIFICATION / ADR |
| `ARCH-PUB-002` | Which object owns binding between ReleaseManifest, LayerManifest, tile digests, and governed API payload digests? | NEEDS VERIFICATION |
| `ARCH-PUB-003` | Which schema owns Archaeology publish receipts and public artifact manifests? | NEEDS VERIFICATION |
| `ARCH-PUB-004` | Which CI job owns Archaeology publish invariant tests? | UNKNOWN |
| `ARCH-PUB-005` | Which public representation receipt vocabulary is canonical for archaeology artifacts? | NEEDS VERIFICATION / ADR |
| `ARCH-PUB-006` | What artifact homes are approved for Archaeology public layers, extracts, cards, and indexes? | NEEDS VERIFICATION |
| `ARCH-PUB-007` | Which rollback proof must be present before Archaeology artifacts are materialized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe release fixtures and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, release-decision authority, direct catalog writes, public UI code, public API code, release-manifest authorship, style-only suppression, or generated archaeology summaries until ReleaseManifest refs, EvidenceBundle refs, ValidationReport refs, policy decisions, review state, public representation refs, artifact digests, correction paths, and rollback targets are proven.
