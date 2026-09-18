<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0039
title: Exact Catalog Redirect Metadata Corrections
type: architecture-decision-record
version: v1.0-draft
status: proposed
effective_decision_status: proposed-owner-review
owners: ["@bartytime4life"]
created: 2026-09-18
updated: 2026-09-18
policy_label: public; governance; fail-closed
truth_posture: "PROPOSED exact target-content acceptance / Stage 1B HOLD / Stage 2 unauthorized"
owning_root: docs/
responsibility_root: docs/
current_path: docs/adr/
responsibility: "Record the owner disposition for seven exact catalog redirect-document corrections without binding the correction register, consuming a transition, changing the topology baseline, or authorizing integration."
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  pull_request: 4627
  pull_request_head: a7469a14267764fa2dbf279bba3951a38d0b7dda
  pull_request_base: eaff4f86e1f6b4398bbfc95c06df66e4a2f7364a
  proposed_register_blob: 7fb41985cd8eb167803774b24702ed28bd3835df
  main_register_blob: b48e8df74a2b9d8c2599ce256ef5156687b98dbf
  topology_baseline_blob: b01cb6ec58d5ae306e8afd7858c5fcc70a03d9ec
  baseline_catalog_fingerprint: sha256:521388927153c91a67ca8cead55af9d688a6064517d109aa556cffca91505006
  accepted_agriculture_target_fingerprint: sha256:0ad45247555960029c34d1222365cbe17a5cabec278bf9f6b8f3e9572ea33e8f
  proposed_final_catalog_fingerprint: sha256:71a120ae8ca2b69896266c9ddd52f6d03577ea91fa2de4390b7d57b9ceeb912f
  catalog_member_count: 43
  pr_changed_paths: 16
  pr_commits_ahead: 7
  exact_head_validator_status: "FAIL_INVARIANT at KFM-TOPO-004; inherited and intentionally unresolved"
related:
  - ADR-0029-adopt-directory-governance-standard-v2.md
  - ADR-0038-trusted-base-topology-correction-transitions.md
  - ../../control_plane/repository_topology_correction_register.yaml
  - ../../contracts/governance/repository_topology_correction_register.md
  - ../../schemas/contracts/v1/governance/repository_topology_correction_register.schema.json
  - ../../tools/validators/directory_governance/validate_repository_topology_correction_register.py
  - ../../tools/validators/directory_governance/validate_repository_topology.py
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4228
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4512
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4514
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4627
tags: [kfm, governance, topology, catalog, redirect, correction, fail-closed]
notes:
  - "This draft records the smallest evidence-backed owner decision surface for the seven exact target blobs."
  - "Until the owner explicitly accepts this record through the repository authority process, its effective status remains proposed."
  - "Even after acceptance, all seven machine-register entries remain proposed and unbound; this record does not perform Stage 1B."
  - "The current v1 register contract does not define an atomic multi-entry batch or validate cross-entry chain continuity."
  - "PR #4627 is not accepted as the integration vehicle because its live scope is broader than the register-only proposal and its lifecycle state conflicts with its draft-only description."
[/KFM_META_BLOCK_V2] -->

ADR-0039 — Exact Catalog Redirect Metadata Corrections

Status

Proposed for explicit owner decision.

Recommended disposition:

* exact target content: ACCEPT;
* current seven register entries: HOLD as proposed and unbound;
* Stage 1B exact machine binding: HOLD;
* Stage 2 trusted-base consumption and topology-baseline replacement: UNAUTHORIZED;
* PR #4627 readiness, approval, and merge: NOT AUTHORIZED;
* automatic restoration of the seven prior blobs: REJECT.

This record becomes an accepted owner decision only through an explicit owner action recorded in the repository authority process. Drafting, committing, reviewing, or merging this text must not be treated as implicit acceptance.

Decision summary

KFM should retain the seven current catalog redirect-document blobs as the intended corrected content. They strengthen the frozen-root and redirect-only boundary and avoid restoring older guidance that permitted or suggested additional files beneath catalog/.

The seven proposed machine-register entries must nevertheless remain inert. They must keep:

status: proposed
decision_ref:
  blob: null
  accepted_commit: null

Acceptance of the target content does not accept the current entries as seven independently consumable transitions. The present v1 contract binds one exact path per entry and requires the live or trusted source state to equal that entry’s from state. Entries 02 through 07 rely on calculated intermediate fingerprints that have not been established as independent live or trusted repository states. The current shape validator checks entry-local structure but does not recompute the catalog evidence, validate cross-entry continuity, or define atomic batch consumption.

The named hold is:

CATALOG_MULTI_ENTRY_BINDING_HOLD

Context

Accepted ADR-0029 classifies catalog/ as deprecated, immutable, frozen_no_writes, and redirect_only. KFM-TOPO-004 fingerprints frozen-root evidence as path@Git-blob-ID; a documentation replacement therefore changes topology identity even when the path set and member count remain unchanged.

ADR-0038 accepts a trusted-base exact-transition mechanism for a single bounded agriculture correction. It separates:

1. Stage 1A accepted decision authority;
2. Stage 1B exact machine binding from a later trusted base; and
3. Stage 2 trusted-base consumption and baseline transition.

ADR-0038 does not grant a blanket frozen-root exception. Its accepted scope is the exact agriculture replacement that moves the catalog fingerprint from:

sha256:521388927153c91a67ca8cead55af9d688a6064517d109aa556cffca91505006

to:

sha256:0ad45247555960029c34d1222365cbe17a5cabec278bf9f6b8f3e9572ea33e8f

Seven additional catalog redirect READMEs now have corrected live blobs. PR #4512 attempted to restore their older blobs, but review found that the older STAC text and parallel language in the other redirect documents reintroduced forbidden frozen-root write guidance. PR #4512 merged despite its recorded draft-only boundary. PR #4514 then restored the corrected redirect texts and the prior baseline bytes. Those lifecycle events do not constitute policy approval and remain governed by issue #4024.

PR #4627 proposes seven inert register entries describing the corrected direction. Its exact head is broader than that proposal: GitHub reports seven commits and sixteen changed paths, including lockfile, local-data, connector, test, and documentation work. Its body still describes a one-file draft scope, while live readback reports it open and non-draft. It therefore cannot serve as the acceptance or integration vehicle for this decision.

Evidence reviewed

Evidence	Exact observation	Decision relevance
repository_topology_baseline.json blob b01cb6ec58d5ae306e8afd7858c5fcc70a03d9ec	KFM-TOPO-004 records 43 sorted catalog/ members and fingerprint 521388…	Establishes the trusted stale source state
Main correction-register blob b48e8df74a2b9d8c2599ce256ef5156687b98dbf	Contains only the agriculture entry, still proposed with null binding	Confirms Stage 1B is not complete even for agriculture
PR #4627 register blob 7fb41985cd8eb167803774b24702ed28bd3835df	Adds seven proposed entries and leaves every decision blob and accepted commit null	Confirms the proposal remains inert
Exact head a7469a14267764fa2dbf279bba3951a38d0b7dda	Every proposed target blob matches the corresponding live file	Confirms the proposed target identities
ADR-0038 and the v1 register contract	Require accepted authority, trusted-base identity, one-use exact matching, and later consumption	Preserves the Stage 1A/1B/2 separation
Register shape validator and tests	Validate schema and entry-local invariants but do not recompute fingerprints or cross-entry chains	Establishes the multi-entry proof gap
Exact-head hosted validator run	Fails only at the repository-topology ratchet for live 71a120… versus stale 521388…; surrounding validator steps pass	Confirms fail-closed behavior remains active
Issues #4024 and #4228	#4024 remains open; #4228 remains Stage 1A accepted, Stage 1B hold, Stage 2 unauthorized	Prevents lifecycle or topology authority from being inferred

Evaluated corrections

All entries preserve a 43-member evidence set, replace exactly one existing path/blob member, add no path, delete no path, and prohibit automatic restoration of the prior blob.

Correction ID	Path	Prior blob	Accepted target blob
KFM-TOPO-004-CORR-4512-01	catalog/STAC/README.md	198a970db9e71b2dc7f5cdbf171b14c0f9a878ce	c2e327dafbabec3cd6cc185f690fbcf4f227ca11
KFM-TOPO-004-CORR-4512-02	catalog/domain/README.md	fd4826b2b5e54672796b840d2664b5947d4054ec	ad9e2406a75746d96b0f8494a2fc0696cfc583c7
KFM-TOPO-004-CORR-4512-03	catalog/index/README.md	3898725a2e3311222020c66099ae4a09f806ea5e	11cb956e56189ed1c618d577158df2b280d21d91
KFM-TOPO-004-CORR-4512-04	catalog/manifest/README.md	9fe630fe18decc275d26ad99c5c7e2ac215d18ca	b4493e247b626eab4db94ba7c030ad5dd67ce785
KFM-TOPO-004-CORR-4512-05	catalog/proof/README.md	2e602944895f26229f41db2b17a603a4be4fafc1	0d82fcc28cf149e5160b38915612dca767306a43
KFM-TOPO-004-CORR-4512-06	catalog/publication/README.md	7f37e6efab211e63eb3ae237adda8551dd640afd	d30392e9b27af050048d595077a4c71456b8be1b
KFM-TOPO-004-CORR-4512-07	catalog/triplet/README.md	270725cc2e907a4f94d928f7c71759f4b6becd0b	2bd84c5a9142d3f7a63e8ae1c2cc9296043afc4b

Verified fingerprint chain

The validator’s canonical algorithm was applied to the baseline’s decoded 43-member evidence set. The agriculture replacement and all seven proposed replacements reproduce every declared fingerprint exactly:

Step	State or correction	Verified fingerprint
0	Baseline	sha256:521388927153c91a67ca8cead55af9d688a6064517d109aa556cffca91505006
1	Agriculture target from KFM-TOPO-004-CORR-4228-01	sha256:0ad45247555960029c34d1222365cbe17a5cabec278bf9f6b8f3e9572ea33e8f
2	KFM-TOPO-004-CORR-4512-01	sha256:5517e475f22d4f7e5b54d88d728edda389a106a903cf769ac3c98eaeb08c6c4b
3	KFM-TOPO-004-CORR-4512-02	sha256:dbac8e3f55a2810c36941d3339d2280be26db59eaf4ca05fbc56ab108eb3b254
4	KFM-TOPO-004-CORR-4512-03	sha256:29e61905ff2fe83760e03d79c6049feea9a8e774564220b6b79e88c4d460ff08
5	KFM-TOPO-004-CORR-4512-04	sha256:98b86686c2a90d6772cf6d6e23c4b7da2bdb31e2c62b4030c02cf7adf7cb0a7a
6	KFM-TOPO-004-CORR-4512-05	sha256:87f34fdc7b2a9b9e1d3e83942f213815943671fd6d736300626925aed371f9a3
7	KFM-TOPO-004-CORR-4512-06	sha256:622be3445da9747dd3f7758583cf5b2024359f95a4cb12e4c2098f5a65f3a93e
8	KFM-TOPO-004-CORR-4512-07 / final live state	sha256:71a120ae8ca2b69896266c9ddd52f6d03577ea91fa2de4390b7d57b9ceeb912f

This confirms the arithmetic and exact blob identities. It does not establish that the six intermediate states after the first proposed replacement were live or trusted repository states, and it does not supply missing batch-consumption authority.

Content assessment

The seven target documents are acceptable as bounded redirect metadata because they:

* identify catalog/ as deprecated and frozen;
* direct users toward the appropriate governed homes beneath data/ and other responsibility roots;
* deny new payload, trust-object, release, publication, policy, schema, or producer authority;
* distinguish public documentation from public data or runtime exposure;
* preserve unknowns rather than claiming producer, consumer, migration, enforcement, or release closure;
* preserve evidence, policy, review, release, correction, and rollback as separate authorities; and
* remove or supersede older language that suggested adding new notes, placeholders, migration records, or other files under the frozen root.

Acceptance of these exact target blobs does not validate every historical statement or timestamp embedded in the documents as permanently current. Later factual corrections require separately reviewed exact transitions.

Decision

Subject to explicit owner acceptance of this ADR, KFM adopts the following disposition.

1. Accept the exact target content

The seven target blobs listed above are accepted as the intended corrected redirect-document content. The decision is exact: no other path, blob, fingerprint, root, or content class is included.

2. Treat the seven corrections as one decision set

The seven corrections are reviewed together because they jointly describe the observed live catalog fingerprint. This statement is a governance grouping only. It does not invent machine batch semantics or make the existing v1 entries consumable.

3. Keep every register entry proposed and unbound

This ADR does not change status, decision_ref.blob, or decision_ref.accepted_commit. The entries remain non-consumable until a later Stage 1B decision begins from a trusted base that already contains the accepted form of this ADR.

4. Hold Stage 1B on batch semantics

Before any Stage 1B binding, a separately reviewed change must choose and prove one of these fail-closed representations:

1. Atomic batch: one accepted batch identity binds all seven paths, prior blobs, target blobs, the common 43-member path set, the source fingerprint, and the final fingerprint; or
2. Ordered chain: the contract explicitly makes order normative, binds every predecessor and successor, validates the complete chain from trusted evidence, and prevents partial or reordered consumption.

The chosen representation must not broaden permission beyond these exact seven replacements.

5. Keep Stage 2 unauthorized

No topology-validator consumption, baseline replacement, live-finding suppression, or correction retirement is authorized. Stage 2 requires a later trusted-base change after both accepted ADR authority and accepted machine binding are already present in its trusted base.

6. Hold PR #4627

PR #4627 is evidence and a proposal source only. Its broader 16-path, seven-commit exact-head scope and non-draft live state prevent it from serving as the narrow ADR or register-binding delivery path. This ADR grants no readiness, approval, merge, rebase, branch update, or lifecycle authority for that PR.

Stage 1B acceptance requirements

The named hold may be lifted only after all of the following are evidenced from a newly pinned trusted base:

* this ADR is explicitly accepted through the repository authority process;
* the accepted ADR bytes and accepted commit are immutable and already present in the later change’s trusted base;
* the selected atomic-batch or ordered-chain model is defined in the governing contract and schema;
* deterministic validation recomputes the 43-member evidence set and all applicable fingerprints rather than trusting asserted YAML values;
* the machine projection binds exactly these seven paths and fourteen blobs;
* positive proof reaches final fingerprint 71a120… from the accepted trusted source;
* negative tests reject absent, partial, reordered, duplicated, mutated, current-only, wrong-path, wrong-blob, wrong-fingerprint, cardinality-changing, path-adding, path-removing, ambiguous, reused, or network-dependent cases;
* current register bytes must equal trusted-base register bytes during later consumption;
* independent review covers the exact head proposed for Stage 1B;
* issue #4024’s required lifecycle containment and enforcement prerequisites are satisfied or a separately authorized safe delivery path is established; and
* issue #4228 is updated by an explicit owner disposition rather than inferred from CI, a merge, or coordination prose.

Rejected alternatives

Restore the seven prior blobs

Rejected. Matching a stale fingerprint is not sufficient justification for restoring guidance that conflicts with the frozen-root posture. Automatic content restoration is prohibited by the proposed entries and by ADR-0038’s rollback model.

Treat the seven YAML entries as self-authorizing

Rejected. A proposed register entry creates no authority. A same-change decision path, current-only binding, or later merge cannot authorize the entry that introduced it.

Treat calculated intermediate fingerprints as historical proof

Rejected. Correct arithmetic proves a deterministic chain, not that each intermediate state was a live or trusted repository state. Batch or chain semantics require an explicit contract decision and validation.

Refresh the topology baseline now

Rejected. Baseline replacement belongs to Stage 2 and requires a trusted base already containing accepted decision authority and accepted machine binding.

Consume only a subset of the seven entries

Rejected unless a later explicit decision proves that the subset corresponds to an exact live or trusted source-to-target transition. This ADR does not permit partial normalization.

Infer approval from PR or CI state

Rejected. Mergeability, green checks, review comments, branch contents, ready state, or merge history do not establish owner policy acceptance, independent review, Stage 1B binding, or Stage 2 authority.

Consequences

The desired corrected redirect content is no longer an open owner-preference question once this ADR is explicitly accepted. The remaining work becomes a narrower machine-representation and trusted-base proof problem.

KFM-TOPO-004 remains red for the catalog fingerprint until an authorized later Stage 2 change. That failure is expected fail-closed evidence, not a reason to weaken the validator or silently replace the baseline.

The seven prior blobs remain available in Git history for provenance, but they are not approved rollback targets. Any later content correction must receive its own exact transition decision.

Rollback and correction

Before acceptance, abandon or revise this draft without changing the register, baseline, or catalog content.

After acceptance but before Stage 1B, rollback changes this ADR back to proposed or records a superseding owner decision. The machine entries remain inert, so no register-consumer or baseline rollback is required.

After any future Stage 1B binding, control rollback revokes or removes recognition and returns enforcement to fail closed. It must not automatically restore any prior catalog blob.

After any future Stage 2 consumption, rollback must preserve the accepted decision, register, validator, baseline, and exact repository history needed to explain the forward and reverse states. A content change remains a new reviewed transition.

Non-effects

This ADR does not:

* bind or consume any correction-register entry;
* change any entry from proposed to accepted;
* populate any decision_ref.blob or decision_ref.accepted_commit;
* establish that the synthetic intermediate fingerprints were live repository states;
* change repository_topology_baseline.json;
* change KFM-TOPO-004 finding construction, severity, evidence identity, or fail-closed behavior;
* suppress the current 71a120… live finding or the stale 521388… baseline finding;
* authorize new files, payloads, placeholders, writers, or consumers under catalog/;
* reclassify catalog/ or any other responsibility root;
* authorize deletion, migration, source admission, scheduling, runtime activation, release, deployment, promotion, publication, or public exposure;
* approve, ready, merge, close, rebase, or otherwise mutate PR #4627;
* close or relax issue #4024;
* advance issue #4228 beyond STAGE 1A ACCEPTED / STAGE 1B HOLD / STAGE 2 UNAUTHORIZED; or
* treat AI generation, schema validity, CI, mergeability, comments, or repository history as owner acceptance.

Owner decision block

The owner may adopt this ADR only with an explicit decision equivalent to:

I accept ADR-0039 for the seven exact target catalog redirect-document blobs
listed in this record. Keep every correction-register entry proposed and
unbound. Keep Stage 1B under CATALOG_MULTI_ENTRY_BINDING_HOLD and Stage 2
unauthorized. This decision does not approve, ready, or merge PR #4627; change
the topology baseline; consume a transition; restore an older blob; or alter
the #4024 and #4228 boundaries.

Until that owner decision is recorded and this exact ADR is accepted through a trusted repository transition, this document remains proposed.