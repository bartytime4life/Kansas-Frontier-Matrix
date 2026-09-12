<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0009-hydrology-first-proof-bearing-lane
title: "ADR-0009 — Hydrology Is the First Proof-Bearing Lane"
type: adr
adr_id: ADR-0009
version: v1.5
status: draft
effective_decision_status: proposed
owners:
  - "OWNER_TBD — architecture decision owner"
  - "OWNER_TBD — Hydrology lane steward"
  - "OWNER_TBD — governance and release steward"
owner_status: "CODEOWNERS routes docs/adr/ and the affected trust-bearing roots to @bartytime4life; accepted stewardship assignments, decision quorum, independent review, and proof-graduation authority remain unverified"
reviewers_required:
  - Architecture steward
  - Docs steward
  - Hydrology lane steward
  - Source and evidence steward
  - Contract and schema steward
  - Policy reviewer
  - Governed API and Explorer Web maintainers
  - Release and rollback steward
  - "at least one affected downstream domain-lane owner"
created: 2026-05-09
updated: 2026-09-12
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: "Records the proposed cross-domain sequencing rule and conjunctive graduation criteria for Hydrology as KFM's first proof-bearing lane without granting acceptance, source admission, release, deployment, publication, or public-use authority."
current_path: docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: fee1c49c6b890d0f5e7dc630af7d0fe1c91a6feb
  target_prior_blob: cd3f47df4f35890ffc1958f461df425ebd5dd0cb
  adr_index_blob: 0c143676dfd3c1bda16cb44398c5ad5d4a49cf67
  adr_0017_blob: b5c0ac83be6f00897ee626c46df2bf64f15d82f5
  adr_0018_blob: 51cedfdf98b92f1a9af492ce3a1cde231eed9308
  adr_0026_blob: 3dc39c422ddfe18dd1c25008f77c265df6bb9831
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  living_waters_fixture_schema_blob: 2c46c56aa3f122c1baddec1b8e5671377c37f91f
  living_waters_fixture_blob: aa007944825680962f3ed69de5fb51bbf76da4c2
  living_waters_invalid_ambiguous_fixture_blob: cfe57dd95cdc968b98e0e09b0b3e711acc706cd7
  living_waters_projection_blob: d11152109e3d8aed3565bfc79ccce56f475a0845
  living_waters_projection_test_blob: 8e6b84e1b2567e4e7f0b6b48bbaf9346f9b643d4
  living_waters_validator_blob: 343b489b53a6f105fe0fe3423fc290d709337229
  living_waters_validator_test_blob: f069e701bba33bd860fedfc632ae36dc8a6489ac
  usgs_nwis_descriptor_blob: 456f64974526ae55107f507878f85cf73292dd51
  usgs_wbd_descriptor_blob: 898eecf387c9722fdf456f904ce759bfb57e429e
  hydrology_pipeline_spec_blob: e9d8751cf81c70cefa4a48f29dc180a82c7f85c4
  hydrology_policy_readme_blob: 1e39301650009a8e2a01c0b9dc3bb344e934a92b
  hydrology_proof_readme_blob: 015c9039de2ba3496b823d6b7fa203b3cd2da81e
  hydrology_release_candidate_readme_blob: 7b93fc2bc3b3363235374f0ee8b9b2c51921ffd2
  domain_hydrology_workflow_blob: 91a934b35769fd78144e6dea58c81aa3a59e3b6a
  hydrology_proof_workflow_blob: 1cef10372c72a5ed3cedf4446117cae8ea9f5fd4
related:
  - docs/adr/INDEX.md
  - docs/adr/ADR-0017-source-descriptor-admission-process.md
  - docs/adr/ADR-0018-promotion-gate-sequence.md
  - docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/THIN_SLICE.md
  - contracts/domains/hydrology/flow_observation.md
  - contracts/domains/hydrology/gauge_site.md
  - contracts/domains/hydrology/hydrograph.md
  - contracts/domains/hydrology/evidence_bundle.md
  - contracts/domains/hydrology/nwis_county_capture.md
  - contracts/domains/hydrology/usgs_water_api_cutover.md
  - schemas/contracts/v1/domains/hydrology/living_waters_fixture_packet.schema.json
  - fixtures/contracts/v1/domains/hydrology/living_waters_fixture_packet/valid/first_proof.json
  - apps/explorer-web/src/features/living_atlas/living-waters-fixture.ts
  - apps/explorer-web/tests/living-waters-fixture.test.ts
  - data/registry/sources/hydrology/usgs_nwis.yaml
  - data/registry/sources/hydrology/usgs_wbd.yaml
  - pipeline_specs/hydrology/usgs_water_observations.yaml
  - policy/domains/hydrology/README.md
  - .github/workflows/domain-hydrology.yml
  - .github/workflows/hydrology-proof-slice.yml
  - data/proofs/hydrology/README.md
  - release/candidates/hydrology/README.md
tags: [kfm, adr, hydrology, proof-bearing-lane, living-waters, synthetic-fixture, evidence-closure, finite-outcomes, fail-closed, source-admission, release-gate]
notes:
  - "v1.5 is a documentation-only reconciliation at main@fee1c49c6b890d0f5e7dc630af7d0fe1c91a6feb. It preserves source metadata draft and effective decision status proposed."
  - "The Living Waters packet, validator, workflow wiring, and Explorer projection establish bounded synthetic behavior only. They do not admit a source, establish a real gauge or product, close evidence or policy, produce a proof, or release or publish data."
  - "Both listed Hydrology source descriptors remain PROPOSED placeholders. The USGS observations pipeline specification remains PROPOSED_INACTIVE, NOT_IMPLEMENTED, disabled, and non-writing."
  - "Notion and Google Drive materials were consulted for design lineage on 2026-09-12. They are non-authoritative planning context; the pinned GitHub tree is the sole current-state authority for this ADR."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0009 — Hydrology Is the First Proof-Bearing Lane

> **Proposed decision.** If accepted, Hydrology will be KFM's first candidate lane for proof-bearing graduation. It is not proof-bearing today. The currently committed Living Waters work is a closed synthetic fixture packet and a UI projection; it is useful evidence of finite-state behavior, but it is not a real-source proof, source admission, policy decision, release, or publication.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![Living Waters: synthetic](https://img.shields.io/badge/living%20waters-synthetic%20fixture-6e7781?style=flat-square)](#current-repository-evidence)
[![Proof workflow: hold](https://img.shields.io/badge/proof%20workflow-governed%20hold-b42318?style=flat-square)](#current-gate-status)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#consequences)

> [!IMPORTANT]
> **Decision status and implementation maturity are separate facts.** The canonical ADR index records this source as draft and its effective decision status as proposed. A future acceptance would choose the lane; a later, separate graduation review would determine whether an actual proof-bearing slice exists.

> [!CAUTION]
> **Do not inflate a fixture into operational truth.** The committed packet identifies its snapshot as fixture://hydrology/snapshot/watershed-reaches, its profile as living-waters-fixture-v1, and its source roles as synthetic. It neither names nor admits a real source snapshot or gauge observation.

> [!WARNING]
> **No hard-coded approval is a governance decision.** The proof workflow retains an explicit hold because there is no accepted Hydrology proof producer, EvidenceBundle closure command, or CatalogMatrix implementation. Readiness checks, receipts, filenames, or a synthetic approval record cannot satisfy the graduation burden.

**Quick navigation:** [Status](#status) · [Evidence boundary](#evidence-boundary) · [Repository evidence](#current-repository-evidence) · [Decision](#decision) · [Current gates](#current-gate-status) · [Acceptance gates](#acceptance-gates) · [Consequences](#consequences) · [Verification](#verification-checklist) · [References](#references)

---

## Status

| Field | Current value |
|---|---|
| ADR identity | ADR-0009, uniquely indexed at [docs/adr/INDEX.md](./INDEX.md) |
| Source metadata | draft |
| Effective decision status | proposed; this ADR is not binding |
| Proposed sequence | Hydrology first, then any other lane only after a reviewed outcome |
| Current implementation evidence | A bounded synthetic Living Waters packet, validator, workflow wiring, and app-local projection |
| Current proof status | No proof-bearing graduation; the dedicated proof workflow is an explicit governed hold |
| Authority granted by this update | Documentation reconciliation only |
| Authority not granted | ADR acceptance, source admission, source activation, capture, policy application, promotion, release, deployment, publication, or public use |

ADR-0029 separately accepts the directory-placement standard. It confirms the correct human-record location for this ADR; it does not accept ADR-0009 or graduate Hydrology.

---

## Evidence Boundary

| Evidence class | Authority in this ADR | Permitted use | Explicitly not inferred |
|---|---|---|---|
| Pinned GitHub tree at main@fee1c49c6b890d0f5e7dc630af7d0fe1c91a6feb | Current-state authority | File contents, declared workflow behavior, committed fixtures, tests, and statuses | A live run, a source admission, or an external operational fact not committed in the tree |
| Notion: KFM Hourly Hydrology Domain Builder v1.0 and KFM Explorer — Kansas-First Layers, Animation, Live Updates, 3D & Performance Roadmap | Supporting planning lineage | The intended first real-slice shape and historical coordination context | Current repository state, accepted decision, source activation, or proof |
| Google Drive: KFM Explorer — Kansas-First Layers, Animation, Live Updates, 3D & Performance Roadmap and KFM Explorer — Living Atlas Interface, Default Views and Animation Design — v0.1 | Supporting design lineage | Kansas-first design rationale and intended user-facing evidence behavior | Admitted data, deployed experience, release state, or source truth |
| Older Hydrology docs and contracts | Mixed-maturity repository lineage | Intended boundaries and vocabulary | Completeness, current execution, or acceptance unless their current status says so |

Notion and Google Drive were read on 2026-09-12. Their materials consistently describe a proposed, Kansas-first proof slice with a versioned HUC or reach, one gauge, precise measurement semantics, an evidence bundle, and visible negative outcomes. The GitHub tree is controlling for the present tense, and it does not yet show a real-source proof.

---

## Context

KFM needs one deliberately small lane in which source identity, spatial and temporal semantics, evidence, policy, runtime outcomes, cataloging, release, correction, replay, and rollback can be tested together. Hydrology is a good proposed candidate because it naturally exposes:

- a bounded spatial identity such as a HUC or reach;
- a named observation site and time series;
- parameter, statistic, unit, qualifier, and freshness semantics;
- meaningful joins whose ambiguity must be surfaced rather than guessed; and
- clear user-facing states for current, stale, empty, unavailable, and ambiguous results.

This is a selection rationale, not evidence that those properties already close across an admitted source. ADR-0026 separately proposes a WBD HUC12-first source spine; it does not accept that source ordering or admit WBD data. ADR-0017 and ADR-0018 remain the relevant proposed admission and promotion sequencing records rather than operational authorizations.

---

## Decision

This ADR proposes that **Hydrology be the first lane eligible to pursue proof-bearing graduation**. Until it is accepted and the separate graduation gates below are met, Hydrology remains a proposed lane with bounded synthetic progress.

The first real proof slice, if it proceeds after source admission, must be deliberately narrow:

1. one versioned Kansas HUC or reach snapshot with immutable identity and digest;
2. one explicitly identified real gauge or observation site;
3. one explicitly identified data product and parameter, statistic, unit, qualifier, datum where applicable, observation window, and freshness rule;
4. an auditable mapping among HUC or reach, gauge, observation, and user-visible feature;
5. a finite response for current, stale, no-results, unavailable, and ambiguous mapping conditions;
6. evidence resolution, policy evaluation, citation or abstention, catalog agreement, release review, correction, replay, and rollback evidence; and
7. one reviewed proof packet that can be rerun without network dependence from an authorized captured artifact.

No real station, gauge identifier, product endpoint, or source snapshot is selected by this ADR update. A future selection must be recorded through the applicable source-admission process rather than inferred from a fixture, planning document, identifier-like test value, or UI copy.

### What proof-bearing means here

Proof-bearing does not mean “the map can draw a line,” “a schema validates,” or “a test passes.” It means a reviewer can trace one released-safe claim from a permitted source artifact through declared semantics and governed policy to a finite response, evidence bundle, catalog record, release decision, and correction or rollback path.

Each link must fail closed. A missing artifact, expired result, forbidden policy outcome, broken join, or conflicting catalog field must result in the documented non-claim rather than a substituted claim.

---

## Current Repository Evidence

| Surface | Confirmed current fact | What it establishes | What it does not establish |
|---|---|---|---|
| [Living Waters fixture schema](../../schemas/contracts/v1/domains/hydrology/living_waters_fixture_packet.schema.json) and [valid packet](../../fixtures/contracts/v1/domains/hydrology/living_waters_fixture_packet/valid/first_proof.json) | A closed synthetic-only packet exists. It uses profile living-waters-fixture-v1, fixture snapshot identity, synthetic reference roles, a fixture gauge, and a small 00060 discharge series. | The repository can represent a finite hydrology-shaped packet with declared provenance fields and negative scenarios. | A real snapshot, real gauge, source access, source rights, capture, admission, or publishable observation. |
| [Invalid ambiguous packet](../../fixtures/contracts/v1/domains/hydrology/living_waters_fixture_packet/invalid/ambiguous_join_answered.json), [validator](../../tools/validators/domains/hydrology/validate_living_waters_fixture_packet.py), and [validator test](../../tests/domains/hydrology/test_living_waters_fixture_packet.py) | The validator checks a bounded synthetic packet and rejects a packet that answers an ambiguous reach mapping. The harness states it proves workflow block wiring and failure propagation, not all Hydrology suites or runner-wide network isolation. | The intended refusal of an answered ambiguous join in this fixture profile. | A real join-resolution service, evidence closure, policy decision, proof producer, or complete isolation proof. |
| [Explorer projection](../../apps/explorer-web/src/features/living_atlas/living-waters-fixture.ts) and [test](../../apps/explorer-web/tests/living-waters-fixture.test.ts) | An app-local projection accepts an already bounded packet and exposes current, stale, no-results, unavailable, and ambiguous-reach frame states. Its boundary states that it does not fetch, resolve a source, evaluate policy, release data, or bind a renderer. | A UI-facing projection of bounded fixture outcomes without source authority. | A governed API path, live map rendering, a real observation, a policy result, or publication. |
| [Domain workflow](../../.github/workflows/domain-hydrology.yml) | Executable bounded shape and polarity checks cover selected proposed profiles, including Living Waters fixture work. The workflow comments exclude live source requests, real Hydrology truth, source admission, policy application, promotion, release, and publish. | Repository-level bounded validation intent for selected synthetic profiles. | End-to-end evidence, catalog, release, or publication closure. |
| [Proof-slice workflow](../../.github/workflows/hydrology-proof-slice.yml) | The workflow explicitly records a governed hold: no accepted Hydrology proof producer, EvidenceBundle closure command, or CatalogMatrix implementation exists to run truthfully. It neither promotes nor publishes. | The missing proof-bearing surfaces are named and intentionally held. | That a hold is a proof, approval, or release. |
| [USGS NWIS descriptor](../../data/registry/sources/hydrology/usgs_nwis.yaml) and [USGS WBD descriptor](../../data/registry/sources/hydrology/usgs_wbd.yaml) | Both files contain status PROPOSED and state that they are placeholders created from documentation inventory. | A declared planning location for future descriptors. | Admission, rights review, source availability, captured bytes, or authorized use. |
| [USGS observations pipeline specification](../../pipeline_specs/hydrology/usgs_water_observations.yaml) | Its status is PROPOSED_INACTIVE, implementation status is NOT_IMPLEMENTED, execution is disabled, and writes are false. | A non-operational proposal that denies activation and writes. | A runnable connector, capture pipeline, or release pathway. |
| [NWIS county capture contract](../../contracts/domains/hydrology/nwis_county_capture.md) and [USGS Water API cutover contract](../../contracts/domains/hydrology/usgs_water_api_cutover.md) | They are proposed captured-input or fixture-only profiles with no transport or source activation authority. | A possible offline normalization and assessment boundary. | Real transport, source admission, evidence closure, or public data delivery. |
| [Hydrology policy README](../../policy/domains/hydrology/README.md) | The policy boundary is draft, mixed-maturity, evaluator-unbound, proof-held, non-release, and non-publication. | That policy work is recognized and constrained. | An evaluated decision applied to a real proof packet. |
| [Proof directory README](../../data/proofs/hydrology/README.md) and [release candidate README](../../release/candidates/hydrology/README.md) | They describe controlled lanes; the proof workflow separately verifies there is no proof payload, and the release document says a candidate is not a release or publication. | Vocabulary and intended storage boundaries. | A proof payload, candidate approval, release, or publication. |

The central current fact is therefore mixed but clear: the repository has stronger synthetic semantics and presentation boundaries than the prior ADR snapshot, while the real-source, evidence, policy, catalog, release, and public-use chain remains intentionally unclosed.

---

## Current Gate Status

| Gate family | Current status | Reason |
|---|---|---|
| ADR decision acceptance | HOLD | This record is draft with effective status proposed. |
| Lane selection rationale | PROPOSED | Hydrology remains a plausible first candidate; no acceptance is recorded. |
| Synthetic packet shape and finite UI states | BOUNDED PROGRESS | The committed fixture, validator, and app projection cover specified synthetic scenarios. |
| Source descriptor admission | HOLD | USGS NWIS and WBD descriptors are explicit PROPOSED placeholders. |
| Real-source artifact and replay | HOLD | No admitted real snapshot, capture manifest, or authorized immutable replay artifact is evidenced here. |
| Contract and schema semantic closure | HOLD | Several relevant contracts and schemas remain draft, proposed, or schema-stub surfaces. |
| Evidence and policy closure | HOLD | No accepted proof producer or EvidenceBundle closure command exists; policy is evaluator-unbound. |
| Catalog agreement | HOLD | The proof workflow explicitly lacks a CatalogMatrix implementation. |
| Promotion, release, and correction | HOLD | Pipeline and proof workflow deny activation or promotion; release material is candidate guidance only. |
| Public presentation | HOLD | The Explorer projection is fixture-only and expressly excludes fetch, policy, release, and renderer binding. |

A green validation of the synthetic fixture, if or when it occurs, changes none of the HOLD rows. It proves only the checked bounded behavior.

---

## Acceptance Gates

Hydrology may be described as proof-bearing only when all of the following are reviewed and recorded. These gates are conjunctive; a passing lower-level test cannot bypass a later gate.

| # | Gate | Required evidence |
|---:|---|---|
| 1 | Decision acceptance | ADR-0009 and its index status are reviewed and made consistent as accepted; scope and stewards are assigned. |
| 2 | Source admission | A concrete source descriptor identifies authority, license or terms, permitted use, retention, attribution, refresh, revocation, and rollback expectations; it passes the applicable admission review. |
| 3 | Bounded capture | One authorized, immutable, versioned source artifact is captured with identity, digest, scope, time, and deterministic replay inputs. |
| 4 | Spatial and temporal semantics | HUC or reach, site, geometry or spatial support, observation window, timezone, datum where applicable, parameter, statistic, unit, qualifier, and freshness policy are contractually precise. |
| 5 | Mapping and ambiguity | The HUC or reach to gauge or observation mapping is reproducible. Zero, multiple, stale, unavailable, and unsupported cases are explicitly represented and cannot silently select an answer. |
| 6 | Contract and schema enforcement | Reviewed contracts and schemas validate both shape and semantics for the actual slice; negative fixtures exercise prohibited substitutions and ambiguous claims. |
| 7 | Evidence closure | Every displayed or API claim resolves to a reviewer-readable EvidenceBundle or a finite abstention with enough provenance to explain the outcome. |
| 8 | Policy closure | A policy evaluator consumes declared inputs, records the decision and reason, and fails closed if its inputs or evaluation are unavailable. |
| 9 | Governed API and Explorer boundary | The browser receives an allowed finite response from the governed boundary; it never creates source, policy, release, or renderer authority from app-local data. |
| 10 | Catalog agreement | Required catalog representations agree on identity, lineage, access, and status, with a documented treatment for disagreement. |
| 11 | Release review | Promotion, release, citation, visibility, correction, and rollback checks are independently reviewable and cannot be satisfied by a hard-coded approval. |
| 12 | Reproducible proof | A no-network proof command reruns the admitted captured artifact through the reviewed path, produces an immutable proof record, and demonstrates correction, replay, and rollback. |

The current Living Waters fixture contributes mainly to gates 4 through 6 as a synthetic design exercise and to gate 9 as a constrained UI projection. It does not independently satisfy any real-source, evidence, policy, catalog, or release gate.

---

## Consequences

If accepted, this ADR gives the program a narrow sequence for proving governance across one domain without asserting that a real Hydrology product already exists.

- Future Hydrology work must preserve the distinction between a fixture, captured source artifact, source descriptor, evidence bundle, proof, release candidate, and publication.
- A source name, gauge-like identifier, source URL, or dashboard mockup must not be treated as an admitted source or real observation.
- The Explorer may continue to render bounded synthetic states, but those states must retain their fixture identity and must not acquire new authority by presentation.
- Any unavailable, stale, empty, or ambiguous condition must remain visible as a finite non-claim rather than be coerced into “current,” “exact,” or “available.”
- Admission and proof work may proceed only through the relevant source, evidence, policy, catalog, and release reviews. This ADR does not authorize live network access, external data retrieval, or data publication.

### Out of scope

This update does not:

- select or activate a particular USGS, WBD, NWIS, or other source;
- establish a real gauge, reach, HUC, observation, or data product;
- change contracts, schemas, validators, workflows, source descriptors, pipelines, policy, the governed API, or Explorer Web;
- execute or approve capture, promotion, release, deployment, publication, or external communications; or
- decide the second proof-bearing lane.

---

## Verification Checklist

Before moving this ADR from proposed to accepted, reviewers should verify:

- [ ] the ADR index and this file agree on identity, path, source metadata, and effective decision status;
- [ ] the assigned decision, Hydrology, source, policy, catalog, API, UI, and release stewards are recorded;
- [ ] the repository still distinguishes the synthetic Living Waters packet from admitted source material;
- [ ] a particular real first slice is selected only through the source-admission process;
- [ ] the first slice includes all specified negative outcomes, including abstention on an ambiguous mapping;
- [ ] the proof producer, EvidenceBundle closure command, policy evaluator, CatalogMatrix, release and correction controls exist and are reviewable; and
- [ ] the final proof command is deterministic, no-network, based on authorized captured bytes, and produces a reviewable record rather than a readiness receipt.

---

## References

### Current repository evidence

| Reference | Status in this ADR | Supports | Does not prove |
|---|---|---|---|
| [ADR index](./INDEX.md) | Confirmed repository file | ADR identity, tracked path, and current draft or proposed placement | Acceptance or lane graduation |
| [ADR-0017](./ADR-0017-source-descriptor-admission-process.md), [ADR-0018](./ADR-0018-promotion-gate-sequence.md), and [ADR-0026](./ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md) | Proposed related decisions | Intended admission, promotion, and Hydrology source-spine sequencing | An admitted source, approved release, or active pipeline |
| [Living Waters schema and valid packet](../../schemas/contracts/v1/domains/hydrology/living_waters_fixture_packet.schema.json) | Confirmed synthetic fixture surface | Bounded packet vocabulary and finite fixture cases | Real observations or source authority |
| [Living Waters validator](../../tools/validators/domains/hydrology/validate_living_waters_fixture_packet.py) and [test](../../tests/domains/hydrology/test_living_waters_fixture_packet.py) | Confirmed bounded validation surface | Selected synthetic validation and failure propagation | Whole-lane proof, network isolation, or evidence closure |
| [Explorer projection](../../apps/explorer-web/src/features/living_atlas/living-waters-fixture.ts) | Confirmed app-local boundary | Fixture-to-frame projection without source authority | Governed live data or map rendering |
| [Hydrology workflows](../../.github/workflows/domain-hydrology.yml) and [proof hold](../../.github/workflows/hydrology-proof-slice.yml) | Confirmed workflow definitions | Bounded validation and explicit proof, catalog, and release holds | A proof or release |
| [USGS source descriptors](../../data/registry/sources/hydrology/usgs_nwis.yaml) and [pipeline specification](../../pipeline_specs/hydrology/usgs_water_observations.yaml) | Confirmed proposed, inactive surfaces | Planned source and pipeline locations | Source admission, capture, or execution |
| [Policy README](../../policy/domains/hydrology/README.md), [proof README](../../data/proofs/hydrology/README.md), and [release candidate README](../../release/candidates/hydrology/README.md) | Confirmed controlled-boundary documents | Current held policy, proof, and release posture | Evaluated policy, proof payload, or publication |

### Supporting external lineage

| Source | Role | Boundary |
|---|---|---|
| Notion: KFM Hourly Hydrology Domain Builder v1.0 | Historical planning and coordination for a Kansas-first hydrology slice | Non-authoritative; no source, release, deployment, or proof fact is taken from it |
| Notion: KFM Explorer — Kansas-First Layers, Animation, Live Updates, 3D & Performance Roadmap | Proposed first real-slice experience and visibility of negative outcomes | Non-authoritative; repository facts override it |
| Google Drive: KFM Explorer — Kansas-First Layers, Animation, Live Updates, 3D & Performance Roadmap | Supporting roadmap lineage | Proposed documentation only; not an admission or publication record |
| Google Drive: KFM Explorer — Living Atlas Interface, Default Views and Animation Design — v0.1 | Supporting UI and evidence-drawer design lineage | Proposed design only; not a deployed interface or data authority |

---

## Change Log

| Version | Date | Change |
|---|---|---|
| v1.5 | 2026-09-12 | Reconciled to main@fee1c49c6b890d0f5e7dc630af7d0fe1c91a6feb. Recorded the current closed synthetic Living Waters packet, validator, test, constrained Explorer projection, and explicit proof-workflow hold. Clarified that USGS descriptors and pipeline work remain proposed or inactive and that no real source, gauge, policy evaluation, evidence closure, catalog closure, release, or publication is established. Added non-authoritative Notion and Google Drive planning lineage. Preserved draft and proposed status. |
| v1.4 | 2026-08-14 | Same-path repository reconciliation that preserved the proposed decision, recognized bounded Hydrology validation, and retained proof and release holds. |
| v1.3 | 2026-07-23 | Repository-grounded modernization that separated ADR acceptance from proof graduation and recorded then-known placeholder, workflow, and release boundaries. |
| v1.2 | 2026-05-15 | Tightened acceptance semantics, source-role separation, risk handling, and rollback. |
| v1 | 2026-05-09 | Initial proposal selecting Hydrology as the first candidate proof-bearing domain lane. |

---

**Last updated:** 2026-09-12 · **Source metadata:** draft · **Effective decision status:** proposed · **Synthetic packet:** committed · **Real-source proof:** not established · **Proof workflow:** governed hold · **Release and publication:** none · **Path:** docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md · [Back to top](#top)
