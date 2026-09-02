<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/encyclopedia-changelog
title: KFM Encyclopedia Scaffold and Edition Changelog
type: changelog
version: v1.0
status: active; repository-grounded; non-authoritative; no-publication
owners:
  - "@bartytime4life via the current CODEOWNERS review route"
created: 2026-05-15
updated: 2026-08-14
policy_label: public; planning-reference
owning_root: docs/
responsibility: >-
  Preserve append-only history for the encyclopedia scaffold, carrier decisions,
  chapter-source migrations, generated assemblies, corrections, and future planning
  editions without creating doctrine, implementation, release, or publication authority.
related:
  - README.md
  - INDEX.md
  - encyclopedia.md
  - ../KFM-encyclopedia.md
  - ../doctrine/encyclopedia.md
  - ../adr/ADR-0036-planning-encyclopedia-carrier-single-writer-and-scaffold-disposition.md
tags: [kfm, encyclopedia, changelog, lineage, scaffold, migration]
notes:
  - "This changelog records repository documentation history. It is not a ReleaseManifest, CorrectionNotice, proof, or publication ledger."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Encyclopedia Scaffold and Edition Changelog

> **Authority limit.** This file records documentation history only. It does not accept an ADR, establish manuscript authority, certify source accuracy, release an edition, or publish KFM content.

## Unreleased

### Proposed — ADR-0036 decision packet

- Proposes `docs/encyclopedia/` as the planning-reference lane.
- Proposes the ordered chapter set as the only writable manuscript source.
- Proposes `encyclopedia.md` as a deterministic generated assembly.
- Proposes `docs/KFM-encyclopedia.md` as a temporary compatibility index.
- Keeps `docs/doctrine/encyclopedia.md` separate.
- Performs no chapter population, generation, migration, release, or publication.

Status: **PROPOSED** until explicit reviewed acceptance.

## 2026-08-14 — Repository-grounded scaffold boundary

Merged PR #2841 updated `README.md` in place.

Material results:

- confirmed seven direct children and seventeen chapter files;
- classified sixteen structural files as generic placeholders;
- identified one extra settlements/infrastructure scaffold and the duplicate `11-` ordinal;
- separated the planning index, doctrine encyclopedia, and scaffold roles;
- recorded finite placement outcome `HOLD`;
- preserved legacy anchors;
- defined review, validation, migration, correction, and rollback boundaries.

Merge commit: `d9bb2653860430f4929039f1af557415bf7e81db`.

No chapter, source PDF, generated assembly, release, or publication was created.

## 2026-08-01 — Planning index modernization

Merged PR #1895 modernized `docs/KFM-encyclopedia.md` as a repository-grounded planning index and source-manuscript crosswalk.

It recorded the source manuscript as:

- title: *Kansas Frontier Matrix Domain and Capability Encyclopedia*;
- edition: v0.1;
- date: 2026-05-05;
- pages: 82;
- SHA-256: `cc899a7a57cbadb5870709be07d9b0dbfd01712cd794d63dc4d640485970419a`;
- exact repository carrier: `UNKNOWN`.

The change did not create or admit `docs/encyclopedia/`.

## 2026-05-15 — Scaffold creation

Merged PR #896 added:

- `encyclopedia.md`, `INDEX.md`, and `CHANGELOG.md` placeholders;
- sixteen structural chapter placeholders;
- `assets/.gitkeep` and `lineage/.gitkeep`.

The scaffold was created to avoid later path churn. Its creation did not establish a canonical lane or manuscript writer.

Merge commit: `f05a14be7f5b7e8d89c3113927b8096ec1285329`.

## 2026-05-09 — Initial lane README

Commit `a7bc537699a18724e8d67e929b8988f142c6fa18` created the initial `docs/encyclopedia/README.md`.

Later repository evidence corrected its no-repository and proposed-tree assumptions.

## Changelog rules

Record:

- accepted carrier or writer decisions;
- chapter-source population and material corrections;
- generated-assembly producer changes;
- compatibility migrations and retirement checkpoints;
- source-manuscript identity changes;
- edition supersession and rollback.

Do not use this file to record:

- software releases;
- data publication;
- source activation;
- policy approval;
- EvidenceBundle closure;
- receipts, proofs, or release manifests.

[Back to top](#top)
