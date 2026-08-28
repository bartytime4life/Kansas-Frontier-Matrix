<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/program-outcome-chain/v1
title: ProgramOutcomeChain Contract
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED_INACTIVE; fixture-only
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; funding; outcomes; no-public-authority
owning_root: contracts/
responsibility: Define an evidence-linked program-to-outcome chain without collapsing eligibility, application, review, award, payment, completion, observation, or evaluation into one mutable project state.
truth_posture: "CONFIRMED source/repository gap; PROPOSED candidate semantics; NEEDS VERIFICATION governance, program, evidence, policy, and release steward review"
related:
  - ../../schemas/contracts/v1/governance/program_outcome_chain.schema.json
  - ../../fixtures/contracts/v1/governance/program_outcome_chain/
  - ../../tools/validators/governance/validate_program_outcome_chain.py
  - ../../tests/validators/governance/test_program_outcome_chain.py
  - ./governance_event.md
  - ../common/temporal_authority_envelope.md
  - ../../docs/architecture/briefing-integration.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, funding, program, award, project, payment, completion, outcome, evaluation, fixture-only, no-network]
notes:
  - "Implements the program-to-outcome object spine named by the briefing-to-system funding lane."
  - "A passing candidate proves only anti-collapse, ordering, identity, and authority non-effects."
[/KFM_META_BLOCK_V2] -->

# ProgramOutcomeChain

## Purpose

`ProgramOutcomeChain` is a proposed, release-neutral carrier for one evidence-linked
progression from a pinned program version toward measured outcomes. It prevents a
single generic “project” status from making stronger claims than its evidence supports.

The source architecture names this spine:

```text
ProgramVersion -> EligibilityArea -> ApplicationWindow -> Application
-> AdministrativeReview -> TechnicalReview -> Recommendation -> Award
-> Agreement -> Project -> ProjectFootprint -> Payment -> Milestone
-> Completion -> OutcomeObservation -> Evaluation
```

This first slice admits partial chains, but every later stage must cite its required
predecessors. It is fixture-only, deterministic, and no-network.

## Anti-collapse semantics

| Stage | Bounded public meaning | Must not imply |
|---|---|---|
| `PROGRAM_VERSION` | Rules exist for the pinned version. | Eligibility, application, funding, or outcome. |
| `ELIGIBILITY_AREA` | The named area is eligible. | A project or applicant is funded. |
| `APPLICATION_WINDOW` | Applications may be submitted in the window. | Submission or approval. |
| `APPLICATION` | An application record exists. | Administrative acceptance, recommendation, or award. |
| `ADMINISTRATIVE_REVIEW` | Administrative review state exists. | Technical merit or award. |
| `TECHNICAL_REVIEW` | Technical review state exists. | Recommendation or binding decision. |
| `RECOMMENDATION` | An authorized recommendation exists. | Award or implementation. |
| `AWARD` | A formal award scope and amount exist. | Agreement, payment, construction, or completion. |
| `AGREEMENT` | An executed agreement and obligations exist. | Project completion or outcome. |
| `PROJECT` | A project is planned or active according to its declared state. | Payment, completion, or measured result. |
| `PROJECT_FOOTPRINT` | A versioned project extent is declared. | Work completed throughout the extent. |
| `PAYMENT` | A disbursement or reimbursement is recorded. | Physical completion or effectiveness. |
| `MILESTONE` | A declared milestone is complete. | Whole-project completion. |
| `COMPLETION` | Completion was accepted for the agreed scope. | A beneficial or causal outcome. |
| `OUTCOME_OBSERVATION` | A method-bound outcome was observed. | Causation. |
| `EVALUATION` | A bounded evaluative conclusion is recorded. | Universal causation or transfer beyond stated limits. |

Each stage carries a fixed `public_claim_code`. The code is a bounded vocabulary,
not permission to expose the record publicly.

## Predecessor rules

The validator preserves the declared object spine:

- an application requires both an application window and eligibility-area context;
- administrative review requires an application;
- technical review requires administrative review;
- recommendation requires technical review;
- award requires recommendation;
- agreement requires award;
- project requires agreement;
- footprint, payment, milestone, and completion require a project;
- an outcome observation requires completion;
- evaluation requires an outcome observation.

Repeated `PAYMENT`, `MILESTONE`, and `OUTCOME_OBSERVATION` stages are allowed.
Other stage types are singular in this proposed profile. Every `depends_on` reference
must identify an earlier stage and include the most recent required predecessor.

## Amount, geometry, method, and uncertainty

- `AWARD` and `PAYMENT` require a non-negative amount and ISO-style currency code.
- Other stages cannot carry an amount.
- `ELIGIBILITY_AREA` and `PROJECT_FOOTPRINT` require a governed geometry reference.
- `OUTCOME_OBSERVATION` and `EVALUATION` require a method reference.
- `EVALUATION` also requires an uncertainty reference.
- These references are identities only. The validator does not resolve geometry,
  evidence, methods, uncertainty, rights, policy, review, or release state.

## Identity and finite outcomes

`spec_hash` uses the repository RFC 8785 JCS plus SHA-256 helper.
`program_outcome_chain_id` is derived from that hash. Stage IDs are included in the
hashed subject, must be unique, and are not interpreted as independent authority.

Finite outcomes are:

- `PASS` — the candidate satisfies the bounded profile;
- `DENY` — a stage, predecessor, claim, or authority invariant is violated;
- `ERROR` — input, schema, hashing, fixture, or identity processing failed.

## Authority boundary

The profile is fixed to `PROPOSED_INACTIVE`, `UNRELEASED`, and
`public_use_allowed: false`. Source activation, evidence resolution, policy evaluation,
review approval, promotion, release, publication, and causal inference effects are all
false.

A passing result does not prove that a program exists, an area is eligible, an
application was submitted, an award was made, money was paid, work was completed,
or an outcome occurred.

## Directory Rules basis

ADR-0029 accepts Directory Governance Standard v2. Semantic meaning belongs under
`contracts/governance/`; machine shape under
`schemas/contracts/v1/governance/`; reusable synthetic cases under
`fixtures/contracts/v1/governance/`; deterministic execution under
`tools/validators/governance/`; focused behavior under
`tests/validators/governance/`; read-only orchestration under
`.github/workflows/`; exploratory source mapping under `docs/intake/exploratory/`;
and authoring accountability under `data/receipts/generated/`.

No new root, funding source connector, program registry, policy authority, evidence
authority, release home, public route, map layer, or publication surface is created.

## Validation

```bash
python -m unittest \
  tests.validators.governance.test_program_outcome_chain \
  --verbose

python tools/validators/governance/validate_program_outcome_chain.py \
  --fixtures
```

## Rollback

Close the draft pull request or abandon the branch before merge. After an authorized
merge, revert the additive packet. No live program, application, award, payment,
project, public API, release, or published artifact requires restoration.
