<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/evidence-resolution-source-map
title: Evidence resolution - governed source map
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; repository-grounded
owners: OWNER_TBD - evidence/proof steward; package steward; validation steward
created: 2026-08-02
updated: 2026-08-02
policy_label: public; exploratory; evidence-resolution; no-network; non-authoritative
owning_root: docs/
repository_snapshot: 658bd477e769646cd70131ca824af0780b6812b4
related: [./README.md, ../../doctrine/directory-rules.md, ../../../packages/evidence-resolver/README.md, ../../../fixtures/packages/evidence_resolver/v1alpha1/README.md, ../../../tools/validators/evidence_resolver/README.md, ../../../tests/packages/evidence_resolver/README.md, ../../../.github/workflows/evidence-resolver.yml]
tags: [kfm, intake, evidence, EvidenceRef, EvidenceBundle, candidate-resolution, cite-or-abstain, no-network]
notes:
  - The supplied documents are design evidence, not contract, schema, source, policy, review, release, or publication authority.
  - Only a bounded internal candidate check is implemented; broader closure and public outcome proposals remain held.
[/KFM_META_BLOCK_V2] -->

# Evidence resolution — governed source map

> **Outcome:** multiple supplied KFM documents converge on an
> EvidenceRef → EvidenceBundle closure step before trust-bearing maps, AI
> answers, exports, or releases. This batch adapts that pressure into one pure,
> versioned, synthetic candidate check. It does not claim full evidence closure.

## Source identity

| Source | Identity | Relevant design pressure |
|---|---|---|
| Unified Implementation Architecture Build Manual.md | SHA-256 e92500f9b40007e8b69d183ecaa6247c542ffec25857875ecd2dbd00709785b1 | Evidence plane ownership (§4.1), Gate E closure (§6.2), resolver flow (§15.3), and evidence tests (§17.1). |
| Repository Structure Guiding Document.md | SHA-256 afe08af316d1f89779bab0d39888cdc65ee989907806a4126c331c50e4a0aa3a | Runtime consumes resolver outputs; public/UI/AI surfaces remain downstream of governed evidence. |
| Kansas_Frontier_Matrix_Pipeline_Living_Implementation_Manual_v0.3.pdf | 30 pages; SHA-256 43d0c6fea4cc64edb87238a13ac49b639934a82dcef0fab2ef49217add0ba8cf | Pages 13–17 require pointer-to-bundle closure and abstention when support is missing. |
| Kansas Frontier Matrix Implementation Reference.pdf | 20 pages; SHA-256 d948332b6c5bfcdd956cf6264f7bcb88d6881ac00ca8afc2534a02d288d4b3c2 | Pages 9–10 make closure necessary for consequential public claims. |
| KFM MapLibre Operating Architecture ... Manual REVISED.pdf | 22 pages; SHA-256 77f56ec1ab632b76c7728cfb250330271b7dc8948db95c8c0594c92ad9ca6b36 | Page 5 places the map downstream of evidence; page 22 keeps evidence closure in the trust checklist. |
| [kfm_full_atlas_seed_cards.md](../../kfm_full_atlas_seed_cards.md) | SHA-256 07c7765576df1997e0be88141bd3cd213930e7281d490a8ae62afd78abe8f445 | KFM-CAND-0007 requires resolution before authoritative use; KFM-CAND-0009 proposes finite resolution reporting. |
| [KFM-encyclopedia.md](../../KFM-encyclopedia.md) | SHA-256 327edfe2ed42cd8a43cb811386fbb3a08361ac1621590184ec1d08acd7834557 | Defines Evidence Drawer/evidence closure as an EvidenceRef-to-EvidenceBundle concern. |

The attached sources are not committed by this change. Filenames, page counts,
and hashes preserve reviewable identity without copying their content into an
authority root.

## Repository reconciliation

At the inspected base, KFM already had proposed closed EvidenceRef and
EvidenceBundle schemas, paired semantic contracts, a dedicated package
scaffold, and a two-job readiness workflow. The executable package core was a
literal placeholder; no resolver command, package tests, package fixtures, or
consumer import existed.

The documents describe a larger system than the current repository can safely
admit. In particular, claim-scope meaning, authoritative registry lookup,
supersession/correction records, stable public outcomes, rights/sensitivity
semantics, governed consumers, and release integration remain unresolved.

## Adapted slice and rejected overreach

| Idea | Disposition |
|---|---|
| Explicit EvidenceRef-to-bundle identity and membership checks | **ADAPT** into the internal v1alpha1 candidate profile. |
| Deterministic finite result and fail-closed negatives | **ADAPT**, but use package-local RESOLVED, UNRESOLVED, DENIED, and ERROR; do not claim public ANSWER mapping. |
| Missing/stale/superseded/withdrawn context must not resolve | **ADAPT** through explicit caller-supplied lookup and correction context. |
| Policy handoff | **ADAPT** only as a caller-supplied outcome/reference projection using the current proposed ANSWER/ABSTAIN/DENY/ERROR vocabulary; no policy evaluation. |
| Renderer/UI/AI remains downstream of evidence | **RETAIN** as an authority prohibition; no consumer is wired. |
| Live registry fetch, source activation, or evidence-store access | **DENY** in this slice. |
| Inferring claim scope, rights, sensitivity, policy, or evidence truth | **DENY** in this slice. |
| Creating an EvidenceResolutionReport, public API, Evidence Drawer integration, release gate, or publication action | **DEFER / NEEDS VERIFICATION**. |

## Directory placement record

| Responsibility signature | Selected path | Outcome and basis |
|---|---|---|
| Reusable non-deployable pure logic | packages/evidence-resolver/ | PLACE; existing package owns the scaffold. |
| Repository-facing executable check | tools/validators/evidence_resolver/ | PLACE; validators orchestrate checks without owning evidence. |
| Reusable synthetic inputs | fixtures/packages/evidence_resolver/ | PLACE; mirrors the owning package inside the canonical fixture root. |
| Executable conformance proof | tests/packages/evidence_resolver/ | PLACE; mirrors the owning package inside the canonical test root. |
| CI orchestration | .github/workflows/evidence-resolver.yml | PLACE; preserves the existing workflow name, triggers, permissions, and job IDs. |
| Source identity and disposition | docs/intake/exploratory/ | PLACE; non-canonical human-readable intake evidence. |

No new root, contract, schema, policy, registry, data, proof, receipt, release,
runtime, or publication authority is created.

## Proof boundary

A passing fixture proves only that the internal profile produced the exact
expected local status and issue codes for synthetic inputs. It does not prove:

- that a bundle exists in an authoritative store;
- semantic equivalence between a claim and claim_scope;
- citation validity, integrity of referenced bytes, rights, or sensitivity;
- policy evaluation, accountable review, current release state, or public
  safety; or
- that any map, AI response, API response, export, or publication may proceed.

Named ownership, accepted input/result contracts, authoritative lookup and
correction profiles, stable consumer semantics, and human review remain
**PROPOSED / NEEDS VERIFICATION**.

## Rollback

Rollback is a normal revert of the bounded feature commit. It removes the
candidate logic, fixtures, tests, validator, Make targets, CI wiring, source
map, and generated receipt without migrating or changing evidence, source,
policy, review, release, runtime, or published state.
