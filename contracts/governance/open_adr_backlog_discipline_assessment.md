<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/open-adr-backlog-discipline-assessment
title: OpenAdrBacklogDisciplineAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Architecture steward · Governance steward · Contract steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; governance; adr-backlog; decision-hygiene; directory-rules
responsibility: Define a fixture-only assessment of declared open-ADR backlog hygiene without creating an ADR, changing the canonical backlog, assigning an owner, resolving a decision, or granting lifecycle authority.
truth_posture: "CONFIRMED supplied Full Atlas concept, connected Drive source, accepted Directory Rules, and current repository backlog pointer; PROPOSED inactive assessment; UNKNOWN canonical Atlas backlog availability and steward ownership; NEEDS VERIFICATION architecture, governance, contract, validation, and hosted exact-head CI review"
related:
  - ../../docs/backlog/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../schemas/contracts/v1/governance/open_adr_backlog_discipline_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/open_adr_backlog_discipline_assessment/cases.json
  - ../../tools/validators/governance/validate_open_adr_backlog_discipline_assessment.py
  - ../../tests/validators/governance/test_validate_open_adr_backlog_discipline_assessment.py
  - ../../docs/intake/exploratory/full-atlas-open-adr-backlog-discipline-source-map.md
[/KFM_META_BLOCK_V2] -->

# OpenAdrBacklogDisciplineAssessment Candidate

`OpenAdrBacklogDisciplineAssessmentCandidate` is an additive declaration for
checking the local coherence of a synthetic Open-ADR backlog snapshot. It makes
stable IDs, decision state, ownership uncertainty, blockers, evidence, ADR
references, supersession, review, and content identity testable without copying
or replacing the canonical backlog.

## Assessment declaration

| Concern | Required declaration | Local check |
|---|---|---|
| Stable identity | Ordered, unique `ADR-S-NN` identifiers. | Duplicate or non-canonical entry order is denied. |
| Active decisions | `OPEN`, `IN_REVIEW`, or `BLOCKED` plus owner, evidence, and decision-required posture. | Unknown owner or evidence abstains; a blocked entry without a blocker is denied. |
| Terminal decisions | `RESOLVED`, `WITHDRAWN`, or `SUPERSEDED` with the state-specific ADR, evidence, and successor bindings. | Contradictory terminal fields are denied. |
| Review | `COMPLETE`, `PENDING`, or `UNKNOWN` with canonical opaque record refs. | Pending or unknown review abstains; complete review without a record is denied. |
| Identity | SHA-256 over canonical JSON excluding `assessment_id`. | Identity drift is an error. |

References are opaque strings. The validator does not dereference an Atlas,
open an ADR, inspect a review system, or infer that any referenced artifact
exists.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The synthetic snapshot is locally coherent under this candidate profile. |
| `ABSTAIN` | Required ownership, evidence, or review knowledge is unresolved. |
| `DENY` | Backlog order, state bindings, blockers, terminal posture, supersession, review, or authority boundaries contradict the profile. |
| `ERROR` | The input cannot be safely parsed, fails the closed schema, or has a mismatched content identity. |

`PASS` is fixture coherence only. It does not mean an ADR exists, a decision is
accepted, a backlog item is resolved, or any change is approved.

## Authority boundary

A validator result does not:

- create, edit, renumber, promote, resolve, withdraw, or supersede a backlog item;
- create, accept, reject, or amend an ADR;
- assign an owner, reviewer, steward, policy, or due date;
- resolve a reference or attest that referenced evidence exists;
- mutate repository, runtime, data, policy, release, deployment, or public state;
- authorize promotion, release, deployment, publication, or public use.

## Directory Rules basis

Governance meaning belongs under `contracts/governance/`; machine shape under
`schemas/contracts/v1/governance/`; synthetic replay under
`fixtures/contracts/v1/governance/`; executable validation and proof under
`tools/validators/governance/` and `tests/validators/governance/`; read-only CI
under `.github/workflows/`; and source lineage under
`docs/intake/exploratory/`. `docs/backlog/README.md` remains a pointer, and this
packet does not create a second backlog authority.

## Validation and rollback

```bash
python -m unittest tests.validators.governance.test_validate_open_adr_backlog_discipline_assessment -v
python tools/validators/governance/validate_open_adr_backlog_discipline_assessment.py --fixtures
```

Rollback is one additive commit revert. The inactive packet creates no backlog,
ADR, ownership, policy, runtime, release, deployment, publication, or public
state that requires restoration.
