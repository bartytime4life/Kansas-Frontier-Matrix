<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/cairnwake-precommitted-evaluation-source-map
title: Cairnwake Precommitted Evaluation Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; read-only-source-adaptation
owners: OWNER_TBD — Intake steward · Validation steward
created: 2026-08-25
updated: 2026-08-25
policy_label: internal; exploratory; no-authority
tags: [kfm, cairnwake, preregistration, commitment, scoring, source-map]
[/KFM_META_BLOCK_V2] -->

# Cairnwake Precommitted Evaluation Source Map

## Read-only sources

- Cairn, Commission an experiment — sealed predictions, scored in public, retrieved 2026-08-25: https://cairnwake.com/experiments.html
- Cairn, Answers, retrieved 2026-08-25: https://cairnwake.com/answers.html

The sources describe SHA-256 commit and reveal, predictions and confidence fixed before observations, explicit falsifiers, intervention disclosure, and public scoring that retains misses. These are external reports and product claims, not KFM facts.

## KFM adaptation

The candidate profile keeps the bounded validation mechanism: hash the revealed sealed payload, require publication before the observation window, prevent early reveal, require exact outcome coverage, disclose ordered interventions, and reproduce Brier scoring as an integer fraction.

It does not implement payment, a public page, a live experiment, observation collection, signing, or a scoreboard. The sources are idea inputs; KFM contracts, schemas, validation semantics, authority boundaries, and future integration remain governed by repository doctrine and steward review.
