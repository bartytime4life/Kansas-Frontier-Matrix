<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/briefing-evidence-binding-chain-source-map
title: Briefing Evidence Binding Chain Source Map
type: exploratory-source-map
version: v0.1.0
status: confirmed-source-map; proposed-implementation; NEEDS STEWARD REVIEW
owners: OWNER_TBD — Intake steward · Source steward · Evidence steward · Contracts steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; exploratory; evidence; reference-closure; no-authority
owning_root: docs/
responsibility: Record source identity, repository overlap, placement, and non-effects for the bounded SourceArtifact-to-ClaimFieldBinding chain assessment.
truth_posture: confirmed source and repository evidence; proposed implementation; cite-or-abstain
related:
  - ./briefing-claim-field-binding-source-map.md
  - ../../../contracts/source/source_artifact.md
  - ../../../contracts/source/source_adapter.md
  - ../../../contracts/evidence/evidence_ref.md
  - ../../../contracts/evidence/claim_field_binding.md
  - ../../../contracts/evidence/evidence_binding_chain_assessment.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, exploratory, briefing, source-artifact, parse-result, evidence-ref, field-binding]
[/KFM_META_BLOCK_V2] -->

# Briefing evidence-binding chain source map

## Selected source requirement

| Item | Evidence reference | Truth label |
|---|---|---|
| Connected Drive briefing | `gdrive://1UnJ3dl9ZFvWHM01pYnqdoh0OOWinSFUg`; `KFM_Briefing_to_System_Integration_Architecture.docx` | `CONFIRMED` source carrier for the separate SourceArtifact, ParseResult, EvidenceRef, ClaimFieldBinding, EvidenceBundle, and ReleaseEvidenceIndex responsibilities. |
| Existing briefing adaptation | `docs/intake/exploratory/briefing-claim-field-binding-source-map.md`; SHA-256 `9ab71fb30e988caeab41b10bef21caa7578316a850b1e16e1d46c499c61c1ea4` | `CONFIRMED` first next sourced idea: prove `SourceArtifact -> ParseResult -> EvidenceRef -> ClaimFieldBinding` reference closure without creating EvidenceBundle. |
| Directory authority | `docs/doctrine/directory-rules.md`; SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`; accepted by ADR-0029 | `CONFIRMED` responsibility-root placement. |

The connected briefing says a SourceArtifact binds exact captured bytes and parser identity; a ParseResult binds parser output and diagnostics to that artifact; an EvidenceRef identifies the cited support and its limits; and a ClaimFieldBinding associates one object field with the source-native statement/value, normalized value, EvidenceRef, transform, and confidence. It separately requires EvidenceBundle and release indexing for later closure and public use.

## Current-main overlap check

Reviewed base: `main@c4cb046829f72afd07e39d167c781fb7435a9ac4`. Connected GitHub inspection found no overlapping open pull request for the evidence-binding chain. Draft PR #2572 concerns purpose-specific hash-subject assessment and does not alter source/evidence chain objects.

Current main already contains the four independent building blocks:

| Building block | Current evidence | Remaining seam |
|---|---|---|
| SourceArtifact | `contracts/source/source_artifact.md`; SHA-256 `b4ad11e42dd2e6993247947c38ab49103fa19783536beee21bae6d2d7c2e531c` | No cross-object chain test. |
| ParseResult | `contracts/source/source_adapter.md`; SHA-256 `ab6ea49281d2585e4f5055638a9521bc064d4570194a4e8ae23dd00015117fd6`; executable value object in `packages/connectors-core/` | No serialized chain assessment. |
| EvidenceRef | `contracts/evidence/evidence_ref.md`; SHA-256 `5131d5cfb889567dd3f4f4485348925d42fb11c0b6f4b093e78142fba8ad193a` | Existing schema is a pre-closure pointer and intentionally does not prove resolution. |
| ClaimFieldBinding | `contracts/evidence/claim_field_binding.md`; SHA-256 `9c2540beff2fb66d95c71341ef67ef0a51eda64425fba8f40bdd25af7581a4f3` | Its validator deliberately does not dereference EvidenceRef or ParseResult. |

## Gap decision

Status: `REPO_GAP`, accepted only as a synthetic, inactive cross-object assessment.

The slice embeds the existing SourceArtifact, EvidenceRef, and ClaimFieldBinding shapes, exercises the executable ParseResult model, and adds assessment-local `EvidenceResolution` linkage so exact refs, parser tuples, record digests, native locators, and value digests can be checked together.

It intentionally does not change the four existing object families, define a general resolver, admit a source, store raw source content, resolve an EvidenceBundle, decide rights or policy, write lifecycle data, create a ReleaseEvidenceIndex, release, or publish.

## Placement and non-effects

Directory Rules place evidence-chain meaning, shape, synthetic input, deterministic validation, tests, CI, source mapping, and authoring receipt in their existing responsibility roots. The ParseResult implementation remains in the existing source-agnostic `packages/connectors-core/` package and is consumed read-only.

No new root, source authority, registry record, EvidenceBundle, proof record, policy decision, review record, release object, API response, AI answer, map layer, export, or public route is created.

## Rollback

Revert the bounded feature commit. No live source, captured bytes, evidence record, resolver state, lifecycle state, policy result, release, cache, map, API, or publication requires operational rollback.
