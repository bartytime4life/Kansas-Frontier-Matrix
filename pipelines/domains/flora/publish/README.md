<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-flora-publish-readme
title: Flora Publish Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <flora-pipeline-owner>
  - <flora-domain-steward>
  - <release-steward>
  - <sensitivity-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-flora-publication-and-rollback-gates
path: pipelines/domains/flora/publish/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/flora/README.md
  - pipelines/domains/flora/catalog/README.md
  - docs/domains/flora/README.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - docs/domains/flora/RELEASE_INDEX.md
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - pipeline_specs/flora/publish.yaml
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - data/catalog/domain/flora/
  - data/triplets/flora/
  - data/published/layers/flora/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/flora/
  - release/manifests/flora/
tags:
  - kfm
  - pipelines
  - domains
  - flora
  - publish
  - release-manifest
  - rollback-card
  - correction-notice
  - redaction-receipt
  - public-safe
  - evidence-bundle
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/flora/publish path as a nested executable Flora publication-artifact sublane."
  - "Flora publish logic is executable artifact assembly only; it does not own release decisions, ReleaseManifests, RollbackCards, CorrectionNotices, policy, sensitivity decisions, EvidenceBundle truth, catalog truth, schemas, source descriptors, or public API authority."
  - "Publication is a governed state transition, not a file move, not a UI action, and not a successful pipeline run."
  - "Controlled Flora records require approved public representation, transform receipts, review, policy, ReleaseManifest, correction path, and rollback target before artifact assembly."
  - "Concrete executable behavior, CI coverage, release wiring, public API/map behavior, and artifact schemas remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Publish Pipeline

> Executable Flora sublane for assembling public-safe Flora publication artifacts from approved release inputs while preserving ReleaseManifest authority, EvidenceBundle bindings, transform receipts, correction paths, rollback targets, policy outcomes, catalog/triplet refs, and the public trust membrane.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-flora%20publish-2e7d32)
![authority](https://img.shields.io/badge/authority-artifact%20assembly%20only-0a7ea4)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![rollback](https://img.shields.io/badge/rollback-required-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/flora/publish/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Flora  
**Sublane:** Publish / release-artifact assembly  
**Placement posture:** nested executable sublane under `pipelines/domains/flora/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no independent release authority; this lane may assemble only release-approved public artifacts with ReleaseManifest, EvidenceBundle, policy, correction, and rollback closure.

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
- [11. Minimal publish artifact receipt](#11-minimal-publish-artifact-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Correction, stale state, and rollback](#13-correction-stale-state-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/flora/publish/` is the executable sublane for Flora publication-artifact assembly.

It supports artifact preparation for:

- release-approved Flora layers, tiles, indexes, extracts, cards, manifests, and metadata bundles;
- released derivatives of `PlantTaxon`, `FloraOccurrence`, `Specimen`, `VegetationCommunity`, `InvasivePlantRecord`, `PhenologyObservation`, `RangePolygon`, and related Flora records;
- transform-receipted public representations for controlled Flora material;
- ReleaseManifest-bound dataset, layer, tile, EvidenceBundle, policy, review, CorrectionNotice, and RollbackCard refs;
- public attribute include-lists, caveat text, negative-state badges, source freshness badges, and Evidence Drawer refs;
- artifact receipts that record digests, input refs, release refs, transform refs, and rollback target refs;
- hold records for missing release decision, missing rollback target, unresolved evidence, unresolved policy, stale state, or artifact-integrity failure.

This directory implements or will implement the **how** of Flora publication artifact assembly. It does not decide release, define ReleaseManifest shape, define policy, decide sensitivity handling, own EvidenceBundle truth, own catalog truth, own source descriptors, mutate canonical stores, serve public API responses, or create public UI state by itself.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/flora/`? | Flora is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `publish/`? | This is a narrow executable sublane for assembling release-approved Flora artifacts. | PROPOSED / NEEDS VERIFICATION |
| Does this publish by itself? | No. It consumes release-approved inputs and emits artifacts/receipts; release authority lives under `release/`. | CONFIRMED governance posture |
| Does this own sensitivity decisions? | No. It requires receipt, review, and policy refs and fails closed when missing. | CONFIRMED sensitivity posture |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust membrane posture |

> [!IMPORTANT]
> A successful publish-artifact run is not a release decision. Flora is public only when a ReleaseManifest with resolvable EvidenceBundle refs, policy outcomes, correction path, and rollback target has already authorized the artifact set.

[⬆ Back to top](#top)

---

## 3. Publish anti-collapse rules

Publish-artifact assembly must preserve release authority, evidence bindings, transform state, correction state, and rollback state.

Disallowed collapses:

```text
pipeline run -> release approval
copy to published path -> publication
published layer -> canonical Flora truth
catalog record -> public artifact
EvidenceRef -> EvidenceBundle
transform receipt -> policy approval
public representation -> source representation
ReleaseManifest -> mutable latest pointer
RollbackCard -> optional cleanup note
CorrectionNotice -> silent edit
generated public summary -> evidence
public UI payload -> canonical store
```

Required distinctions:

- ReleaseManifest, MapReleaseManifest, LayerManifest, EvidenceBundle, transform receipt, ReviewRecord, PolicyDecision, CorrectionNotice, RollbackCard, catalog record, graph projection, and public artifact remain separate;
- controlled Flora records use approved public representation before release-facing artifacts are assembled;
- public artifacts bind to content hashes and release refs, not floating latest pointers;
- stale, superseded, corrected, withdrawn, denied, and held states remain visible;
- public clients never read RAW, WORK, QUARANTINE, canonical/internal stores, source APIs, graph internals, vector indexes, or direct model outputs.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Flora publication-artifact assembly.

Appropriate contents include:

- fixture-only release-artifact dry-run entrypoints;
- ReleaseManifest input validators;
- EvidenceBundle, policy, review, transform receipt, CorrectionNotice, and RollbackCard presence checks;
- public layer/PMTiles/extract/card/index builders;
- artifact digest and manifest writers;
- public attribute include-list and caveat injectors;
- stale/corrected/superseded/withdrawn badge builders;
- artifact-integrity and rollback-target validators;
- release receipt emitters, if not shared;
- hold/quarantine routing helpers for missing release preconditions.

A good placement test:

> If the code assembles artifacts from an already-approved Flora release candidate and writes content-addressed artifact outputs plus receipts, it may belong here. If it decides release, edits policy, decides sensitivity handling, validates raw source material, owns catalog truth, serves the API, or writes UI state, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers, API clients, watchers | `connectors/` or watcher roots |
| Source descriptors / source registry entries | `data/registry/sources/flora/` or approved registry home |
| Ingest, normalize, validate, or catalog logic | sibling Flora pipeline sublanes |
| Flora doctrine and object meaning | `docs/domains/flora/`, `contracts/domains/flora/` |
| JSON Schemas | `schemas/contracts/v1/domains/flora/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Release decisions, ReleaseManifest authorship, RollbackCards | `release/...` responsibility roots |
| Fixtures | `fixtures/domains/flora/publish/` or accepted fixture home |
| Tests | `tests/pipelines/domains/flora/publish/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet lifecycle records | `data/...` lifecycle homes |
| Public API or map viewer code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Direct model summaries or generated answer text | Governed AI/released artifact paths only after review |

[⬆ Back to top](#top)

---

## 6. Publication-artifact scope

| Scope area | Publish-lane responsibility | Failure behavior |
|---|---|---|
| Release input | Confirm release candidate and ReleaseManifest refs are present and resolvable. | Hold; no artifact change. |
| Evidence binding | Confirm EvidenceBundle refs resolve and digests match. | Hold or quarantine. |
| Sensitivity | Confirm controlled material uses approved public representation and receipts. | Hold release-facing output. |
| Artifact integrity | Write content-addressed artifacts, manifests, checksums, and receipts. | Fail closed on digest mismatch. |
| Correction path | Carry CorrectionNotice and invalidation expectations. | Hold if missing for corrected releases. |
| Rollback | Confirm rollback target or RollbackCard precondition is present. | Hold release-facing output. |
| Public interface | Produce artifacts for governed API/UI consumption only. | No direct UI/API side effects. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Flora publish run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** release-approved inputs only: ReleaseManifest refs, release candidates, catalog/triplet refs, EvidenceBundle refs, policy decisions, review records, transform receipts, CorrectionNotices, rollback targets, and artifact specs.
2. **Verify** every required reference resolves and every digest matches expected inputs.
3. **Assemble** public artifacts such as layers, tiles, extracts, cards, caveats, indexes, and manifest sidecars.
4. **Emit** artifact receipts, digests, and rollback/correction/invalidation links.
5. **Hold or quarantine** missing release, evidence, policy, transform, correction, rollback, freshness, or integrity preconditions.
6. **Never mutate canonical stores, source captures, catalog truth, release decisions, public UI state, or direct API behavior.**

Publish here means artifact assembly after a governed release decision. It is not an approval gate and not a shortcut from catalog to public exposure.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Flora publish run must check or explicitly fail closed on:

1. **ReleaseManifest gate** — release identity, contents, digests, evidence refs, rollback target, time, and correction path are present.
2. **EvidenceBundle gate** — all public claims resolve evidence and digest closure passes.
3. **Policy/review gate** — release policy outcome and review state are present; no silent allow.
4. **Sensitivity gate** — controlled material has approved public handling with receipt support.
5. **Rights gate** — unresolved rights or source-role uncertainty blocks public promotion.
6. **Freshness/stale gate** — stale source, schema drift, geography drift, review age, or rights change is surfaced and handled.
7. **Artifact digest gate** — artifact content hashes, manifests, tiles, extracts, and indexes match release refs.
8. **Correction gate** — corrected outputs carry CorrectionNotice and invalidation list where required.
9. **Rollback gate** — rollback target is resolvable before controlled Flora artifact publication.
10. **Trust membrane gate** — outputs are suitable for governed APIs; no public client reads internal stores.
11. **No-direct-decision gate** — this lane does not create release decisions or policy decisions.
12. **No-direct-UI/API gate** — no side effects in public UI, public API routes, or direct model responses.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/flora/publish/
├── README.md                         # this file
├── PUBLISH_CONTRACT.md               # PROPOSED: Flora publish artifact execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized/redacted fixture only
├── validate_release_manifest.py      # PROPOSED
├── validate_evidence_bundle_refs.py  # PROPOSED
├── validate_transform_receipts.py    # PROPOSED
├── validate_policy_review.py         # PROPOSED
├── validate_rollback_target.py       # PROPOSED
├── build_public_layer_manifest.py    # PROPOSED
├── build_public_artifacts.py         # PROPOSED
├── emit_publish_receipt.py           # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/flora/publish.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted release/public artifact homes under `data/published/layers/flora/`, `data/receipts/`, `release/candidates/flora/`, and `release/manifests/flora/`, with decisions remaining in `release/` and public serving remaining behind governed API/UI roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/flora/publish/` or accepted fixture home | Synthetic or redacted release fixture. |
| Release candidate | `release/candidates/flora/` | Reviewable input only. |
| ReleaseManifest | `release/manifests/flora/` | Decision authority, not owned here. |
| Evidence proof | `data/proofs/evidence_bundle/` | Required and resolved before artifact assembly. |
| Catalog/triplet refs | `data/catalog/domain/flora/`, `data/triplets/flora/` | Inputs by stable refs/digests. |
| Published artifact | `data/published/layers/flora/` or accepted public artifact home | Content-addressed output only. |
| Receipt | `data/receipts/pipeline/flora/publish/<run_id>.yml` or accepted receipt home | Records release refs, digests, checks, outputs. |
| Correction / rollback refs | `release/...` | Required refs for controlled releases. |

[⬆ Back to top](#top)

---

## 11. Minimal publish artifact receipt

The final schema is not defined here. This example shows the minimum information a Flora publish run should preserve.

```yaml
schema_version: kfm.flora_publish_receipt.v1
publish_run_id: flora_publish_run_YYYYMMDDThhmmssZ
pipeline_id: domains.flora.publish
status: HELD
release:
  release_manifest_ref: release/manifests/flora/<release_id>.json
  release_manifest_hash: sha256:<hash>
  release_candidate_ref: release/candidates/flora/<candidate_id>.json
inputs:
  catalog_refs: []
  triplet_refs: []
  evidence_bundle_refs: []
  policy_decision_refs: []
  review_record_refs: []
  transform_receipt_refs: []
  correction_notice_refs: []
  rollback_target_ref: null
sensitivity:
  controlled_material_present: false
  public_representation_state: <withheld|generalized|aggregated|staged|denied|public>
  sensitive_lane_release_ready: false
artifacts:
  layer_manifest_ref: null
  pmtiles_ref: null
  extract_refs: []
  artifact_digests: {}
checks:
  evidence_resolved: false
  policy_resolved: false
  rollback_resolved: false
  digests_match: false
anti_collapse:
  publish_run_is_release_decision: false
  copied_file_is_publication: false
  public_layer_is_canonical_truth: false
  public_representation_is_source_material: false
outputs:
  receipt_ref: data/receipts/pipeline/flora/publish/run_YYYYMMDDThhmmssZ.yml
  published_artifact_refs: []
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/redacted, and no-network** until publish specs, release fixtures, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/flora/publish/
├── test_no_network_dry_run.py              # PROPOSED
├── test_release_manifest_required.py       # PROPOSED
├── test_evidence_bundle_required.py        # PROPOSED
├── test_policy_review_required.py          # PROPOSED
├── test_transform_receipt_required.py      # PROPOSED
├── test_controlled_material_has_public_state.py # PROPOSED
├── test_rollback_target_required.py        # PROPOSED
├── test_artifact_digests_match_manifest.py # PROPOSED
├── test_stale_state_surfaces.py            # PROPOSED
├── test_correction_notice_invalidates.py   # PROPOSED
├── test_publish_run_not_release_decision.py # PROPOSED
├── test_no_internal_store_exposure.py      # PROPOSED
└── test_no_direct_ui_api_side_effect.py    # PROPOSED
```

A dry run should prove fixtures load without network access, ReleaseManifest and rollback target are required, EvidenceBundle and policy refs resolve, controlled Flora source material is not emitted as a raw public artifact, artifacts are content-addressed, receipts are deterministic, stale/correction states are surfaced, and no run mutates release decisions, canonical stores, public UI, or public API routes.

[⬆ Back to top](#top)

---

## 13. Correction, stale state, and rollback

Flora publish pipelines may materialize correction and rollback-aware artifacts. They do not approve corrections or rollbacks.

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
- rollback is authenticated and receipt-backed, not ad-hoc deletion;
- `CorrectionNotice`, `RollbackCard`, invalidation lists, and prior release refs must stay attached to public artifacts;
- controlled Flora artifact publication requires rollback proof before artifact assembly;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/flora/publish/README.md` file;
- identifies this directory as a nested executable Flora publish-artifact sublane;
- prevents source, ingest, normalize, validate, catalog, schema, contract, policy, sensitivity-decision, release-decision, public API, UI, and canonical-store authority from being placed here;
- preserves ReleaseManifest, EvidenceBundle, policy, review, transform receipts, CorrectionNotice, RollbackCard, catalog/triplet, artifact digest, release, correction, and rollback boundaries;
- blocks pipeline-run-as-release, copy-as-publication, catalog-as-public-artifact, public-representation-as-source-material, generated-summary-as-evidence, direct UI/API side effects, and internal-store exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has release-fixture coverage, schema-backed artifact receipts, ReleaseManifest/EvidenceBundle/policy/transform/rollback/digest tests, deterministic receipts, CI coverage, steward-review handoff, and rollback/correction documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `FLORA-PUB-001` | Should Flora publish remain one sublane, or split into layer, tile, extract, Evidence Drawer, and Focus Mode artifact builders? | NEEDS VERIFICATION / ADR |
| `FLORA-PUB-002` | Which object owns the binding between `ReleaseManifest`, `MapReleaseManifest`, `LayerManifest`, and PMTiles digests? | NEEDS VERIFICATION |
| `FLORA-PUB-003` | Which schema owns Flora publish receipts and public artifact manifests? | NEEDS VERIFICATION |
| `FLORA-PUB-004` | Which CI job owns Flora publish invariant tests? | UNKNOWN |
| `FLORA-PUB-005` | Which transform receipt format is required for controlled Flora public artifacts? | NEEDS VERIFICATION / ADR |
| `FLORA-PUB-006` | What artifact homes are approved for Flora public layers, extracts, cards, and indexes? | NEEDS VERIFICATION |
| `FLORA-PUB-007` | Which rollback proof must be present before controlled Flora artifacts are materialized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/redacted release fixtures and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, sensitivity-decision authority, release-decision authority, direct catalog writes, public UI code, public API code, release-manifest authorship, or generated botanical summaries until ReleaseManifest refs, EvidenceBundle refs, transform receipts, policy decisions, review state, artifact digests, correction paths, and rollback targets are proven.
