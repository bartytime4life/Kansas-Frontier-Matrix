<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/briefing-program-outcome-source-map
title: Briefing Program-to-Outcome Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; PROPOSED; non-authoritative
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; no-source-activation
owning_root: docs/
responsibility: Record the source-to-repository adaptation boundary for the fixture-only ProgramOutcomeChain profile.
truth_posture: "CONFIRMED supplied-source idea and current indexed gap; PROPOSED implementation mapping; UNKNOWN operational program adoption"
related:
  - ../../../contracts/governance/program_outcome_chain.md
  - ../../../docs/architecture/briefing-integration.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [briefing, funding, program, project, outcome, source-map, fixture-only]
[/KFM_META_BLOCK_V2] -->

# Briefing program-to-outcome source map

## Source requirement

The supplied *KFM Briefing-to-System Integration Architecture* says one generic
project object is insufficient because it collapses distinct authority-bearing stages.
It proposes a progression from `ProgramVersion` through eligibility, application,
review, recommendation, award, agreement, project execution, payment, completion,
outcome observation, and evaluation.

The same source distinguishes the claims each stage may support. In particular:

- eligibility is not funding;
- application is not approval;
- recommendation is not a decision;
- award is not payment or construction;
- payment is not physical completion;
- completion is not a beneficial outcome;
- observation is not causation; and
- evaluation remains bounded by method, uncertainty, evidence, and limitations.

## Current repository reconciliation

Current repository evidence already contains the shared briefing foundation,
`TemporalAuthorityEnvelope`, source-adapter work, and an inactive `GovernanceEvent`
profile. A current indexed search did not find the named program-to-outcome stage
family. This packet therefore adds the smallest closed, fixture-only semantic slice
rather than a connector, database, API, map, issue writer, or public product.

## Adaptation decision

The packet:

1. defines one inactive `ProgramOutcomeChain` carrier;
2. makes the stage vocabulary and anti-collapse claim codes finite;
3. enforces predecessor ordering and explicit references;
4. binds deterministic identity to the full candidate;
5. adds exact-polarity fixtures and tests; and
6. fixes every source, evidence, policy, review, release, publication, and causal
   effect to false.

## Deliberate holds

The following remain outside this slice:

- live funding or grant source activation;
- applicant, application, review, award, payment, or monitoring ingestion;
- rights and public-disclosure decisions;
- PostGIS or graph storage;
- issue/project mutation;
- `/v1/programs` or `/v1/outcomes` routes;
- MapLibre investment or outcome layers;
- EvidenceBundle resolution;
- policy, review, promotion, release, correction, or rollback execution; and
- AI-generated conclusions.

## Directory Rules basis

This document explains a source adaptation and therefore belongs under
`docs/intake/exploratory/`. Meaning, shape, fixtures, execution, tests, workflow, and
receipt remain in their distinct responsibility roots. No new topic root or parallel
program, source, evidence, policy, release, or publication authority is introduced.
