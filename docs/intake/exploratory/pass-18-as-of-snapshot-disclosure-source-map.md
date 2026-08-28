<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-as-of-snapshot-disclosure-source-map
title: Pass 18 As-Of Snapshot Disclosure Source Map
type: source-map; exploratory-intake; implementation-evidence
version: 1.0.0
status: confirmed-source-map; proposed-implementation; NEEDS STEWARD REVIEW
owners: OWNER_TBD — Intake steward · Evidence steward · Temporal steward
created: 2026-08-11
updated: 2026-08-11
policy_label: public; exploratory; source-mapped; non-authoritative
tags: [kfm, pass-18, source-map, as-of, snapshot, temporal, reports]
related:
  - ../../../contracts/evidence/as_of_snapshot_disclosure.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "Separates exact attached-PDF evidence from thematic connected-Drive corroboration."
[/KFM_META_BLOCK_V2] -->

# Pass 18 As-Of Snapshot Disclosure Source Map

## Selection record

| Item | Evidence | Truth label |
|---|---|---|
| Source idea | `KFM-P18-INV-348 — As-of report snapshots for temporally changing claims` | `CONFIRMED` |
| Exact source | Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical PDF pages 148–149 / printed pages 145–146 | `CONFIRMED` |
| Connected-Drive corroboration | `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`), time-aware spatial-semantics carrier | `CONFIRMED` thematic corroboration; byte identity not claimed |
| Repository overlap | Current-main searches for the exact card ID and proposed object name returned no matching PR, branch, or code symbol before authoring | `CONFIRMED` at review time |
| Implementation | Inactive `AsOfSnapshotDisclosureCandidate` fixture profile | `PROPOSED` |

## Source-to-contract mapping

| Source concern | Bounded implementation |
|---|---|
| Underlying records can change after publication | Immutable output, snapshot, and source-head digests |
| Same claim period can yield different outputs | Separate `claim_valid_time` and `snapshot.as_of` axes |
| Reports need a reconstructable cutoff | Release/transaction snapshot references and tracking-log reference |
| Corrections can change later results | Included-through timestamp, correction references, and later-correction behavior |
| Public outputs need visible temporal context | Distinct valid-time and as-of labels plus external review/release references |

## Repository fit

The profile remains an evidence disclosure, not an execution mechanism. It complements existing verification-history and temporal-integrity surfaces without replacing them. Directory Rules and ADR-0029 place semantic meaning in `contracts/evidence/`, shape in `schemas/contracts/v1/evidence/`, synthetic examples in `fixtures/`, executable checks in `tools/` and `tests/`, and the authoring receipt in `data/receipts/generated/`.

## Non-claims

This source map does not claim that the connected Drive document is byte-identical to the attached dossier, that any source snapshot exists or was resolved, that the new declaration can reproduce a real report, or that truth, correction, policy, review, release, deployment, publication, or public use has been authorized.
