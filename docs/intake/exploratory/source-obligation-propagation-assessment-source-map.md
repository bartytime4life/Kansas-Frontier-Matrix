<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/source-obligation-propagation-assessment-source-map
title: SourceObligationPropagationAssessment Source Adaptation Map
type: exploratory source map
version: v0.1.0
status: draft; source-grounded; implementation-companion
owners: OWNER_TBD — Source steward · Rights reviewer · Documentation steward
created: 2026-08-11
updated: 2026-08-11
policy_label: public; exploratory; source; rights; attribution
related:
  - ../../../contracts/source/source_obligation_propagation_assessment.md
  - ../../../contracts/source/source_rights_currentness_assessment.md
  - ../../../schemas/contracts/v1/source/source_obligation_propagation_assessment.schema.json
  - ../../../tools/validators/source/validate_source_obligation_propagation_assessment.py
tags: [kfm, source-map, attribution, rights, obligations, derivative, export]
[/KFM_META_BLOCK_V2] -->

# SourceObligationPropagationAssessment source adaptation map

## Goal

Record why KFM needs a bounded, fixture-only check that source attribution and
use obligations survive downstream derivation, catalog, and export-candidate
carriers.

## Evidence boundary

| Evidence | Status | What it supports | What it cannot prove |
|---|---|---|---|
| `KFM_Comprehensive_Research_and_Verification_Report.docx` from Google Drive | CONFIRMED supplied research source | Publication tests should demonstrate that attribution and use restrictions survive into every derived and exported artifact; source rights, terms, redistribution, and derivative-use posture must remain explicit and fail closed. | Current repository implementation, legal permission, or release readiness. |
| `KFM_Briefing_to_System_Integration_Architecture.docx` from Google Drive | CONFIRMED supplied design source | Official-source snapshots, evidence, policy, review, and release objects remain distinct; generated narrative cannot authorize public products. | Rights interpretation or a current runtime carrier chain. |
| `contracts/source/source_rights_currentness_assessment.md` at base `01b3f70bb0514c0557e777294b36992317e992c8` | CONFIRMED repository evidence | KFM already has a dated fixture-only assessment for source identity, terms, rights, attribution, redistribution, derivative use, access, and cadence. It explicitly says currentness is not permission and restrictions must be enforced downstream. | Whether downstream artifacts actually preserve those declarations. |
| `contracts/source/source_artifact.md`, release contracts, and carrier-oriented repository docs at the same base | CONFIRMED repository evidence | KFM has distinct source-artifact, catalog, release, and export-oriented object families that can be linked by opaque references. | A complete source-to-export obligation-propagation proof. |
| Exact repository search for `SourceObligationPropagationAssessment` and `AttributionPropagationAssessment` at the same base | CONFIRMED bounded search result | No exact object family with either name was found before authoring. | Absence of every conceptually similar check or external/private implementation. |
| ADR-0029 and adopted Directory Rules v2 | ACCEPTED placement authority | Semantic meaning belongs in `contracts/source/`; shape, fixtures, validators, tests, workflow, source map, and generated receipt remain in their owning roots. | Rights approval, policy decision, release, or publication. |

## Adaptation decision

**PROPOSED:** add one source-agnostic assessment candidate that references an
existing rights/currentness assessment and checks a declared carrier chain for
obligation loss.

The candidate preserves these distinctions:

- a current rights review versus permission;
- source obligations versus downstream carrier declarations;
- internal derivative, catalog candidate, and export candidate;
- attribution/terms/notice propagation versus artifact-byte integrity;
- a complete fixture declaration versus policy or release approval; and
- public-candidate intent versus public-use authority.

## Scope admitted in this packet

- one semantic contract;
- one closed Draft 2020-12 schema;
- synthetic complete, review-due, blocked, and error cases;
- one deterministic no-network validator;
- focused unit, CLI, non-echoing, identity, ordering, chain-closure, and
  fail-closed tests;
- one read-only workflow; and
- one generated authoring receipt bound to the final bytes.

## Explicit non-goals

- interpreting source terms, copyright, license, consent, or public-domain law;
- resolving referenced source, artifact, catalog, receipt, or release objects;
- adding a rights registry, policy rule, export implementation, or release
  pipeline;
- creating or modifying public artifacts;
- weakening a more restrictive upstream obligation; or
- authorizing source use, export, release, or publication.

## Follow-up boundary

A later operational adoption would require object-resolution checks against
actual source, artifact, transform-receipt, catalog, and release records, plus
policy and steward review. This packet does not pre-authorize that work.

## Rollback

Revert the additive packet. No existing object family is superseded and no
source, artifact, lifecycle, release, export, or public state is changed.
