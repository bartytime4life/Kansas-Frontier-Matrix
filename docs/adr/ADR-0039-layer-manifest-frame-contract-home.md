<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0039
adr_id: ADR-0039
title: "ADR-0039 — Keep LayerManifest and LayerFrame in the Existing Data Contract/Schema Family"
type: adr
version: v1.1
status: proposed
owners:
  - "@bartytime4life"
owner_status: "CODEOWNERS routing is present; independent contract/schema stewardship remains NEEDS VERIFICATION."
reviewers_required:
  - "Contract/Schema steward"
  - "Data/Layer steward"
  - "Evidence/Receipt steward"
  - "Validation steward"
  - "Architecture steward"
  - "Affected UI/Map steward"
created: 2026-09-12
updated: 2026-09-14
policy_label: "public; non-release; fixture-only; no-source-activation"
truth_posture: "cite-or-abstain"
responsibility_root: "docs/"
responsibility: "Record the proposed LayerManifest and LayerFrame contract/schema home and sequencing boundary without authorizing dependent implementation."
owning_root: "docs/"
current_path: "docs/adr/ADR-0039-layer-manifest-frame-contract-home.md"
supersedes: []
superseded_by: null
evidence_snapshot:
  repository: "bartytime4life/Kansas-Frontier-Matrix"
  base_ref: "main"
  base_commit: "d3f9db88d0d48291ac3810f684eeeb5b9aeca72d"
  base_tree: "a518e85b584b4718a09135dd4708a245f7ec0c93"
  refresh_2026_09_14:
    base_ref: "main"
    base_commit: "40c2bf1ab5f197185b62ce4d0729560f90bcd0f5"
    base_tree: "52c90c5d88b46e78dc5359b11991be927b11b09e"
    prior_adr_blob: "0e81520829ab275d6028dd8dc4702062831b6c4c"
    adr_index_blob: "0c143676dfd3c1bda16cb44398c5ad5d4a49cf67"
    adr_0029_blob: "4c1ef5f7f812d58fbdde9898acc96bb4c9280b2c"
    layer_manifest_contract_blob: "234dca70e768ee744f7d78109afc6e0dc745af1b"
    layer_descriptor_contract_blob: "8822340fbf55b518da45c40ba12eb1073919c7b7"
    layer_manifest_data_schema_blob: "abca306cb271ed75127a83dd05b73830ba20773b"
    data_layer_manifest_validator_blob: "577d31795caaf6712132e73189af18d318ac0e8a"
    layers_schema_index_blob: "a37a1426a1c13a50c2ee854b9935136c96564ab1"
    layers_manifest_scaffold_blob: "81b6872fa7f9c843adb8432f28aa306ab8d272f6"
    map_manifest_scaffold_blob: "a28a6b194ce61dfc25667ebe9f095680b099893a"
    runtime_manifest_pointer_blob: "799c52f6a7938de96598e6ac1cdebf1bb7c20fbe"
    runtime_manifest_scaffold_blob: "297756e311aee0a351068b553403fe275c2db18e"
    release_manifest_bridge_blob: "adfad2688b84fac945de610f1afa84139fd42b8f"
    temporal_frame_model_blob: "21d7d6429d33e619e2df4482bcbbb59aec3cb19e"
    representation_receipt_contract_blob: "4e4a7e4d1d98c8592a76d0d3127eb90233906614"
    representation_receipt_schema_blob: "6ed7c07ad22d31b983e2339a101b69d2a1b1adff"
    maplibre_readme_blob: "3f459b0b0617ee26b0793c5dfc4b2de5412aa612"
    policy_split_blob: "e420dce959b493c295af735357ab528c18ff9771"
refresh_2026_09_14_limit: "This documentation refresh re-read repository entry points, direct filename/code-search results, and planning lineage only; it did not execute a validator, test suite, hosted workflow, runtime, deployment, release, or publication check."
refresh_2026_09_14_filename_observation: "A direct filename search returning no layer_frame result is a bounded source observation, not proof of zero consumers or authorization to create, migrate, or activate a LayerFrame path."
  adr_index_blob: "b911db30622c31867ccc835a4014c8e8fcd13a09"
  adr_0001_blob: "ed6f258f8d9ea152996570768a31666953e4a809"
  adr_0002_blob: "e626d82970932c319a690fc6044727ed114ada6a"
  adr_0029_blob: "a4de0d7a96b78da59cfc499d1025e1508afd8dd9"
  layer_manifest_contract_blob: "234dca70e768ee744f7d78109afc6e0dc745af1b"
  layer_descriptor_contract_blob: "8822340fbf55b518da45c40ba12eb1073919c7b7"
  layer_manifest_data_schema_blob: "abca306cb271ed75127a83dd05b73830ba20773b"
  layer_schema_index_blob: "a37a1426a1c13a50c2ee854b9935136c96564ab1"
  layer_manifest_scaffold_schema_blob: "81b6872fa7f9c843adb8432f28aa306ab8d272f6"
  representation_receipt_contract_blob: "4e4a7e4d1d98c8592a76d0d3127eb90233906614"
  representation_receipt_schema_blob: "6ed7c07ad22d31b983e2339a101b69d2a1b1adff"
  maplibre_performance_readme_blob: "3f459b0b0617ee26b0793c5dfc4b2de5412aa612"
  data_receipts_readme_blob: "041f205dd5e618185fc7c75e95c85872fc9bbf69"
  data_proofs_readme_blob: "0d8b6e92d3b4b9ff3961d29c53ead497922a31cf"
related:
  - "docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md"
  - "docs/adr/ADR-0002-contracts-vs-schemas-split.md"
  - "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
  - "docs/doctrine/directory-rules.md"
  - "docs/architecture/contract-schema-policy-split.md"
  - "contracts/data/layer_manifest.md"
  - "contracts/data/layer_descriptor.md"
  - "contracts/layers/README.md"
  - "schemas/contracts/v1/data/layer_manifest.schema.json"
  - "schemas/contracts/v1/layers/README.md"
  - "contracts/receipts/representation_receipt.md"
  - "schemas/contracts/v1/receipts/representation_receipt.schema.json"
  - "schemas/maplibre/README.md"
  - "data/receipts/README.md"
  - "data/proofs/README.md"
tags: [kfm, adr, explorer, layer-manifest, layer-frame, contracts, schemas, receipts, evidence, performance, no-parallel-authority, fixture-only]
notes:
  - "This is a proposed placement and sequencing decision. It does not accept ADR-0001 or ADR-0002."
  - "The proposal records the smallest reviewable home for Phase 0 and the dependency boundary for fixture-only Phase 1."
  - "No source, transport, runtime loader, renderer admission, release, deployment, or publication path is changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0039 — Keep LayerManifest and LayerFrame in the Existing Data Contract/Schema Family

> **Proposed decision.** Keep the semantic meaning of LayerManifest and LayerFrame in the existing contracts/data family, and keep their machine-checkable shapes in the existing schemas/contracts/v1/data family. Do not add new consumers to the competing layers schema scaffolds until a separately reviewed migration decision exists.

[![decision](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#1-status-and-scope)
[![semantic home](https://img.shields.io/badge/semantic%20home-contracts%2Fdata-1f6feb?style=flat-square)](#3-decision)
[![schema home](https://img.shields.io/badge/schema%20home-schemas%2Fcontracts%2Fv1%2Fdata-1f6feb?style=flat-square)](#3-decision)
[![runtime](https://img.shields.io/badge/runtime-no%20change-6e7781?style=flat-square)](#7-implementation-migration-and-compatibility)

> [!IMPORTANT]
> This record is proposed and reviewable, not accepted. A file, index row, branch, pull request, merge, or passing check does not accept this decision or authorize dependent implementation.

## 1. Status and scope

| Field | Current value |
|---|---|
| ADR status | proposed |
| Decision owner | @bartytime4life; independent stewardship remains NEEDS VERIFICATION |
| Evidence baseline | Initial main at d3f9db88d0d48291ac3810f684eeeb5b9aeca72d; current refresh at 40c2bf1ab5f197185b62ce4d0729560f90bcd0f5 |
| Decision class | Object-family contract/schema placement and Phase 0/Phase 1 sequencing |
| In scope | LayerManifest, LayerFrame, frame status, evidence references, render receipts, performance artifacts, compatibility boundaries |
| Out of scope | Source admission, live transport, runtime loading, MapLibre dependency admission, release, deployment, publication, thresholds, and telemetry |
| Implementation effect of this proposal | None; this change records a proposal only |

This ADR narrows the unresolved LayerManifest/LayerFrame home question identified by the September 11 Explorer roadmap. It does not accept the broader proposed schema-home or contracts-versus-schemas ADRs.

### Current repository readback — 2026-09-14

This documentation-only refresh re-pins implementation evidence at `main@40c2bf1ab5f197185b62ce4d0729560f90bcd0f5` (tree `52c90c5d88b46e78dc5359b11991be927b11b09e`). It preserves this ADR as `proposed` and does not accept, create, migrate, or activate a contract, schema, fixture, validator, consumer, source, runtime, release, deployment, or publication path.

| Surface | Current readback | Boundary |
|---|---|---|
| ADR source and canonical index | ADR blob `0e815208…` remains `proposed`; index blob `0c143676…` retains ADR-0039 as `proposed` | The record remains a reviewable placement proposal, not an effective decision |
| Canonical LayerManifest candidate | `contracts/data/layer_manifest.md` blob `234dca70…` is v0.3, `draft; proposed-inactive; dual-profile; fixture-only-strict-profile` | The paired data contract remains a bounded, inactive candidate rather than an implementation activation |
| Paired data schema and validator | `schemas/contracts/v1/data/layer_manifest.schema.json` blob `abca306c…` documents a legacy permissive and closed fixture-only profile; `tools/validators/data/validate_layer_manifest.py` blob `577d3179…` says PASS creates no policy, review, release, publication, signature, registry, or public-use authority | No validation was executed by this refresh; the inspected source is not a release or runtime result |
| Other LayerManifest lanes | The `layers`, `map`, and `runtime` schema copies inspected are permissive `PROPOSED` scaffolds with empty properties; the runtime contract is a compatibility pointer and the release contract calls itself a compatibility bridge | These observations reinforce the no-parallel-authority boundary; they do not resolve their migration or retirement |
| LayerFrame source shape | The direct `filename:layer_frame` query returned no file result at this base. The repository does contain `packages/temporal/src/temporal/core.py` blob `21d7d642…`, with renderer-independent `TemporalFrameContext` and `TemporalFrameLayer` types | The temporal model is not a standalone LayerFrame semantic contract or machine schema; the bounded query is not proof of zero consumers or a directive to create one |
| Receipt, performance, and policy seams | Existing RepresentationReceipt and MapLibre compatibility sources remain under their separate families | This refresh creates no receipt, proof, performance threshold, policy, renderer, or source authority |

The September 11 Explorer roadmap remains planning lineage: it recommends one governed LayerFrame contract and says to resolve the existing LayerManifest handoff before selecting a schema home. It is proposed/documentation-only; GitHub remains implementation authority.


## 2. Context and current evidence

The roadmap identifies Phase 0 plus fixture-only Phase 1 as the next actionable work, while leaving the LayerManifest/LayerFrame authority and release/performance authorities for human review.

The current repository presents two layer-schema signals:

1. The existing semantic LayerManifest and LayerDescriptor contracts live in contracts/data/.
2. The existing LayerManifest machine schema is paired at schemas/contracts/v1/data/layer_manifest.schema.json.
3. schemas/contracts/v1/layers/ contains shared layer schema files, but its own README describes them as proposed scaffolds, with empty properties and additionalProperties enabled.
4. contracts/layers/README.md explicitly records the data-versus-layers placement conflict and warns that the directory is an orientation/compatibility path rather than resolved canonical authority.

The repository already has distinct responsibility families for receipts, evidence/proofs, release decisions, runtime code, and generated QA output. The placement question can therefore be resolved without creating a new root or moving any existing payload.

## 3. Decision

### 3.1 Semantic contract home

The semantic home is contracts/data/.

- The existing contracts/data/layer_manifest.md remains the LayerManifest semantic contract.
- A future LayerFrame contract, if accepted for implementation, belongs beside it as contracts/data/layer_frame.md.
- LayerFrame is the temporal/renderable companion to LayerManifest. It identifies one frame of a governed layer representation and carries frame-specific temporal, spatial, quality, trust, evidence, and lineage information.
- The existing `TemporalFrameContext` and `TemporalFrameLayer` implementation types remain a bounded temporal model; they are not, by name or by this ADR, a standalone LayerFrame semantic contract.
- LayerDescriptor remains a separate renderer-facing semantic contract in contracts/data/layer_descriptor.md.
- contracts/layers/ remains a pointer/orientation path. It does not become an independently writable semantic home.

This decision preserves the already-paired contract family and avoids a semantic move merely because the object is displayed by a map.

### 3.2 Machine-schema home

The machine-schema home is schemas/contracts/v1/data/.

- The existing schemas/contracts/v1/data/layer_manifest.schema.json remains the paired LayerManifest schema.
- A future LayerFrame schema, if accepted for implementation, belongs beside it as schemas/contracts/v1/data/layer_frame.schema.json.
- LayerFrame schemas must reference or profile shared schemas rather than copy the same meaning into domain-specific or layer-specific duplicates.
- schemas/contracts/v1/layers/ is not a new implementation target. Its existing files remain visible as proposed, unverified scaffolds with no new consumers.
- No schema file is moved, deleted, renamed, or made active by this ADR.

The broader ADR-0001 remains the proposed record for repository-wide schema-family routing and migration. This ADR chooses only the smallest LayerManifest/LayerFrame path needed for review of the Explorer roadmap.

### 3.3 Frame status

Frame status belongs on LayerFrame as a finite frame-availability/trust field, not as a new status registry and not as a replacement for lifecycle or release records.

The proposed finite values are:

| Status | Meaning |
|---|---|
| AVAILABLE | The frame is available within its declared candidate or released context |
| STALE | The frame exists but exceeds its declared freshness expectation |
| UNAVAILABLE | No usable frame is available for the requested context |
| ERROR | The bounded frame evaluation failed |
| ABSTAINED | KFM cannot responsibly assert or expose the frame |
| DENIED | Policy, rights, sensitivity, or access rules prohibit the frame |
| CONFLICT | Relevant inputs or lineage disagree and are unresolved |
| DEGRADED | A bounded fallback or reduced-fidelity frame is being represented |
| WITHDRAWN | The frame was withdrawn by a governed correction or source action |
| ROLLED_BACK | The frame was replaced by a governed rollback |

These values describe frame state only. Manifest lifecycle, policy decisions, review status, promotion decisions, release state, source status, and rollback authority remain in their existing families.

### 3.4 Evidence and proof

LayerManifest and LayerFrame may carry references to evidence, but they do not own EvidenceBundle meaning or proof authority.

- EvidenceBundle and proof instances belong under data/proofs/.
- The contract/schema may require stable evidence references and preserve uncertainty, coverage, limitations, and correction lineage.
- A reference does not prove that the referenced bundle resolves.
- A schema-valid frame does not prove source truth, policy approval, review, release, or public safety.
- The browser and renderer remain downstream of governed evidence and released carriers.

### 3.5 Render receipts

Render receipts belong to the existing receipt family, not to the layer schema family and not to the performance-schema compatibility lane.

- Semantic receipt meaning belongs under contracts/receipts/.
- The smallest Phase 1 shape is a RenderReceipt-compatible profile of the existing RepresentationReceipt family.
- Machine shape belongs under schemas/contracts/v1/receipts/.
- Emitted receipt instances belong under data/receipts/.
- A render receipt records what the client or adapter attempted to render: frame identifiers, evidence references, renderer/adapter identity, projection/camera parameters, active fallback, capability profile, warnings, and disposal/context-loss outcome.
- It does not establish evidence truth, policy permission, release, publication, or scientific validity.
- A distinct RenderReceipt contract should be added only if later field review shows that a profile of RepresentationReceipt cannot preserve the semantic distinction.

### 3.6 Performance artifacts

Performance configuration, measurement, and proof remain separate.

- Existing schemas/maplibre/ is a transitional compatibility lane for MapLibre performance-related schemas. It is not performance authority and does not establish runtime readiness.
- The existing PerfEnvelope shape remains configuration/budget input, not measured performance evidence.
- Performance measurements, proof packs, and reproducibility metadata belong as evidence/proof instances under data/proofs/.
- CI-generated copies may remain under artifacts/qa/ as non-authoritative generated output.
- RenderReceipt may record render-attempt facts, but it is not a performance proof.
- Device profiles, thresholds, browser/toolchain identity, fixture identity, long-session evidence, and release-authoritative performance review remain NEEDS VERIFICATION and human decision.
- No performance threshold is ratified by this ADR.

## 4. Placement outcomes

| Artifact or path | Proposed outcome | Reason |
|---|---|---|
| contracts/data/layer_manifest.md | PLACE | Existing semantic contract and current paired family |
| contracts/data/layer_frame.md | PLACE after acceptance | Same semantic data family; not created by this proposal |
| schemas/contracts/v1/data/layer_manifest.schema.json | PLACE | Existing paired machine shape |
| schemas/contracts/v1/data/layer_frame.schema.json | PLACE after acceptance | Same versioned machine-schema family |
| contracts/layers/ | HOLD / compatibility pointer | Existing README records unresolved placement conflict |
| schemas/contracts/v1/layers/ | HOLD / scaffold-only | Proposed permissive duplicates; no new consumers |
| contracts/receipts/ | PLACE | Existing receipt semantic authority |
| schemas/contracts/v1/receipts/ | PLACE | Existing versioned receipt-schema family |
| data/receipts/ | PLACE | Emitted process-memory records |
| data/proofs/ | PLACE | Evidence and performance proof instances |
| schemas/maplibre/ | HOLD / transitional compatibility | Existing performance schema migration is unresolved |
| artifacts/qa/ | MIRROR / generated output only | QA copies cannot become contract, proof, release, or publication authority |

## 5. Alternatives considered

### 5.1 Use contracts/layers and schemas/contracts/v1/layers

Rejected for the first implementation slice. These paths contain explicit placement conflict and proposed permissive scaffolds. Choosing them now would promote an unresolved duplicate lane by convention.

### 5.2 Create a new explorer or renderer contract/schema root

Rejected. The new root would add no responsibility boundary and would violate the no-parallel-authority and no-speculative-root rules.

### 5.3 Move the existing data contracts and schemas immediately

Rejected for Phase 0. A move would require accepted migration authority, inbound-reference repair, identity analysis, consumer audit, compatibility handling, and rollback evidence. None is required to record the smallest home decision.

### 5.4 Leave the conflict entirely unresolved

Retained only as the pre-decision state. It prevents a truthful Phase 1 contract seam and allows future contributors to choose between duplicate paths by convenience.

## 6. Consequences and risks

### Benefits

- Reuses the existing LayerManifest semantic/schema pairing.
- Avoids a new root and avoids widening the duplicate layers schema lane.
- Keeps frame status, evidence, receipts, performance proof, release, and runtime authority distinct.
- Allows Phase 1 to remain fixture-only and deterministic after the decision is accepted.
- Preserves existing paths and minimizes migration risk.

### Costs and residual risks

- LayerFrame does not yet have a standalone semantic contract, machine schema, or fixture validator. The inspected temporal package has bounded `TemporalFrameContext`/`TemporalFrameLayer` implementation types, but this ADR does not equate them with the proposed contract or infer a governed consumer.
- The existing layers schemas remain visible and may continue to confuse contributors until a later migration/retirement decision.
- ADR-0001 and ADR-0002 remain broader proposed decisions.
- Performance authority, thresholds, browser profiles, and artifact retention remain unresolved.
- Owner and independent reviewer assignments remain NEEDS VERIFICATION.

## 7. Implementation, migration, and compatibility

Decision and dependent implementation are separate transitions.

| Order | Change | State |
|---:|---|---|
| 1 | Review this proposed ADR and its synchronized index row | Current proposal |
| 2 | Explicitly accept or reject the ADR through the repository review process | Human decision required |
| 3 | Repin current main after acceptance | Required before implementation |
| 4 | Add the LayerFrame semantic/schema/fixture/test slice under the selected existing families | Separate implementation PR |
| 5 | Add or profile RenderReceipt only after receipt-family review | Separate bounded follow-up if needed |
| 6 | Reassess the layers schema scaffolds and any domain profiles | Separate migration/retirement decision |
| 7 | Establish performance profiles and thresholds | Separate human performance-authority decision |

This proposal changes no existing contract, schema, fixture, validator, runtime, source, release, or data instance. No destructive cleanup is authorized.

This refresh changes this ADR's documentation only. It does not create a `LayerFrame` contract/schema/fixture, modify any existing contract/schema/validator, add a consumer, resolve the scaffold migration question, or change a source, runtime, release, deployment, or publication state.

## 8. Validation and acceptance

### 8.1 Proposal checks

| Check | Scope | State |
|---|---|---|
| Initial main ref readback | Initial baseline identity | CONFIRMED: d3f9db88d0d48291ac3810f684eeeb5b9aeca72d |
| Current repository re-read | Refresh identity, source placement, and bounded filename/code-search observation | CONFIRMED: 40c2bf1ab5f197185b62ce4d0729560f90bcd0f5; no validator or test executed |
| ADR index inspection | Number availability and status | CONFIRMED: ADR-0038 is highest numbered record at baseline |
| Layer contract/schema inventory | Existing pairing and duplicate-path evidence | CONFIRMED |
| Receipt and proof family inventory | Placement boundary | CONFIRMED |
| Local ADR validator | This proposal branch | PENDING |
| Hosted checks | Exact pull-request head | PENDING |
| Human contract/schema review | Decision acceptance | NOT RUN / REQUIRED |

For this documentation refresh, only the source-entry-point readback and exact text-replacement preflight are recorded. Repository-native, hosted, runtime, deployment, release, and publication validation remain unrun and must not be inferred.

### 8.2 Acceptance criteria

- The ADR source and canonical index row identify ADR-0039 consistently.
- Required reviewers assess the selected contract and schema homes.
- The accepted decision does not create a second writable layer schema authority.
- Frame status is kept separate from lifecycle, policy, review, release, and source status.
- EvidenceBundle, receipt, performance proof, runtime, and release paths remain separately owned.
- Dependent implementation remains blocked until the accepted decision is effective and current main is repinned.
- No source, runtime, release, deployment, or publication effect is inferred from this proposal.

## 9. Rollback, correction, and supersession

- **Documentation rollback target:** the exact pre-change main tree at d3f9db88d0d48291ac3810f684eeeb5b9aeca72d.
- **Revert:** remove the proposed ADR and synchronized index row through a reviewed revert if the proposal is withdrawn before acceptance.
- **Correction:** append a reviewed correction or successor ADR if the selected home changes.
- **Implementation rollback:** any later LayerFrame implementation must preserve the existing compatibility profile, fixtures, references, and no-source/no-runtime boundary.
- **Cleanup:** do not delete or rename the layers scaffolds until zero-consumer, inbound-reference, identity, and migration evidence exists.
- **Supersession:** none. This ADR does not supersede ADR-0001, ADR-0002, or ADR-0029.

## 10. Security, rights, sensitivity, and sovereignty

| Concern | Applies? | Boundary |
|---|---:|---|
| Source rights and redistribution | Yes | No source is admitted or activated |
| Sensitive geometry or harmful precision | Yes | No payload or geometry is added |
| Living-person, DNA, archaeology, rare-species, and infrastructure data | Yes | Existing deny-by-default rules remain unchanged |
| Runtime/network behavior | Yes | No endpoint, transport, loader, telemetry, or renderer path changes |
| Performance evidence privacy | Yes | Profiles and artifacts must avoid sensitive coordinates, tokens, raw URLs, and unsafe logs |

Unknown high-risk conditions remain HOLD or DENY.

## 11. Open verification

| Item | Status | Next evidence |
|---|---|---|
| Contract/schema steward identity | NEEDS VERIFICATION | Named review and ownership record |
| Whether LayerFrame needs a separate file or a section in LayerManifest | NEEDS VERIFICATION | Contract-family review; this ADR recommends a companion file |
| Exact RenderReceipt field profile | NEEDS VERIFICATION | Receipt-family review against RepresentationReceipt |
| Migration/retirement status of layers scaffolds | NEEDS VERIFICATION | Consumer and inbound-reference inventory |
| Performance artifact authority and thresholds | NEEDS VERIFICATION | Human performance decision, profiles, fixtures, and reproducibility plan |
| Validator and fixture coverage for LayerFrame | NOT YET IMPLEMENTED | Separate post-acceptance Phase 1 PR |

## 12. Evidence and references

### 12.1 Initial repository evidence — 2026-09-12

- [Current main ref](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/d3f9db88d0d48291ac3810f684eeeb5b9aeca72d)
- [LayerManifest semantic contract](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d3f9db88d0d48291ac3810f684eeeb5b9aeca72d/contracts/data/layer_manifest.md)
- [LayerManifest data schema](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d3f9db88d0d48291ac3810f684eeeb5b9aeca72d/schemas/contracts/v1/data/layer_manifest.schema.json)
- [Layer compatibility path](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d3f9db88d0d48291ac3810f684eeeb5b9aeca72d/contracts/layers/README.md)
- [Layer schema scaffold index](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d3f9db88d0d48291ac3810f684eeeb5b9aeca72d/schemas/contracts/v1/layers/README.md)
- [RepresentationReceipt contract](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d3f9db88d0d48291ac3810f684eeeb5b9aeca72d/contracts/receipts/representation_receipt.md)
- [MapLibre performance boundary](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d3f9db88d0d48291ac3810f684eeeb5b9aeca72d/schemas/maplibre/README.md)
- [Receipt process-memory boundary](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d3f9db88d0d48291ac3810f684eeeb5b9aeca72d/data/receipts/README.md)
- [Proof and evidence boundary](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d3f9db88d0d48291ac3810f684eeeb5b9aeca72d/data/proofs/README.md)

### 12.2 Current refresh evidence — 2026-09-14

- [Current main ref](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/40c2bf1ab5f197185b62ce4d0729560f90bcd0f5)
- [Current LayerManifest contract](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/40c2bf1ab5f197185b62ce4d0729560f90bcd0f5/contracts/data/layer_manifest.md)
- [Current data LayerManifest schema](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/40c2bf1ab5f197185b62ce4d0729560f90bcd0f5/schemas/contracts/v1/data/layer_manifest.schema.json)
- [Current fixture-only validator](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/40c2bf1ab5f197185b62ce4d0729560f90bcd0f5/tools/validators/data/validate_layer_manifest.py)
- [Current temporal frame model](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/40c2bf1ab5f197185b62ce4d0729560f90bcd0f5/packages/temporal/src/temporal/core.py)
- [Current runtime compatibility pointer](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/40c2bf1ab5f197185b62ce4d0729560f90bcd0f5/contracts/runtime/layer_manifest.md)
- [Current release compatibility bridge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/40c2bf1ab5f197185b62ce4d0729560f90bcd0f5/contracts/release/layer_manifest.md)

### 12.3 Governing decisions

- [ADR-0001 — Schema Home](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d3f9db88d0d48291ac3810f684eeeb5b9aeca72d/docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) — proposed
- [ADR-0002 — Contracts vs Schemas Split](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d3f9db88d0d48291ac3810f684eeeb5b9aeca72d/docs/adr/ADR-0002-contracts-vs-schemas-split.md) — proposed
- [ADR-0029 — Directory Governance Standard v2](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d3f9db88d0d48291ac3810f684eeeb5b9aeca72d/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) — accepted

### 12.4 Planning lineage

- [KFM Explorer roadmap in Google Drive](https://docs.google.com/document/d/1L8zsQgam1bdP7uUbX2zxOkTA01enXXu_tlHLKZRPvzQ/edit)
- [KFM Explorer roadmap in Notion](https://app.notion.com/p/3d8a92021bf68190a68ef071b378162e?pvs=204)

The roadmap is planning lineage and coordination context. GitHub remains the implementation authority; the roadmap does not accept this ADR or activate dependent paths.

## 13. Change history

| Date | Record status | Change | Evidence |
|---|---|---|---|
| 2026-09-14 | proposed | Re-pinned repository evidence; distinguished the temporal implementation model from a standalone LayerFrame contract/schema; preserved all non-effects | main at 40c2bf1ab5f197185b62ce4d0729560f90bcd0f5 |
| 2026-09-12 | proposed | Initial repository-grounded contract/schema-home proposal | Branch from main at d3f9db88d0d48291ac3810f684eeeb5b9aeca72d |

[Back to top](#top)
