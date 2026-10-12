<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/drift-register-triage-assessment
title: DriftRegisterTriageAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Governance steward · Architecture steward · Repository steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; governance; drift-register; triage; directory-rules
responsibility: Define a fixture-only assessment of declared drift-triage coherence without reading or changing the canonical drift register, assigning an owner, executing a correction, resolving drift, or granting lifecycle authority.
truth_posture: "CONFIRMED supplied Full Atlas concept, connected Drive source, accepted Directory Rules, and current repository drift register; PROPOSED inactive assessment; UNKNOWN triage vocabulary adoption and steward ownership; NEEDS VERIFICATION governance, architecture, repository, contract, validation, and hosted exact-head CI review"
related:
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/doctrine/directory-rules.md
  - ../../schemas/contracts/v1/governance/drift_register_triage_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/drift_register_triage_assessment/cases.json
  - ../../tools/validators/governance/validate_drift_register_triage_assessment.py
  - ../../tests/validators/governance/test_validate_drift_register_triage_assessment.py
  - ../../docs/intake/exploratory/full-atlas-drift-register-triage-source-map.md
[/KFM_META_BLOCK_V2] -->

# DriftRegisterTriageAssessment Candidate

`DriftRegisterTriageAssessmentCandidate` is an additive declaration for checking
the local coherence of a synthetic drift-triage snapshot. It makes stable drift
IDs, category, severity, state, affected paths, ownership uncertainty, evidence,
ADR blockers, correction and resolution refs, review cadence, and content
identity testable without parsing or replacing the human drift register.

## Assessment declaration

| Concern | Required declaration | Local check |
|---|---|---|
| Stable identity | Ordered, unique `DRIFT-YYYY-MM-DD-NNN` identifiers. | Duplicate or non-canonical entry order is denied. |
| Affected paths | Ordered, unique repository-relative paths with no traversal. | Absolute, backslash, dot-segment, or non-canonical paths are denied. |
| Active triage | `OPEN`, `ACKNOWLEDGED`, `BLOCKED_ADR`, or `CORRECTION_IN_PROGRESS` plus state-specific bindings. | Unknown owner, evidence, or next review abstains; missing ADR/correction bindings are denied. |
| Terminal triage | `RESOLVED` or `WITHDRAWN` plus evidence and resolution posture. | Missing or contradictory terminal bindings are denied. |
| Review | `COMPLETE`, `PENDING`, or `UNKNOWN` with canonical opaque record refs. | Pending or unknown review abstains; complete review without a record is denied. |
| Identity | SHA-256 over canonical JSON excluding `assessment_id`. | Identity drift is an error. |

References are opaque strings. The validator does not dereference an ADR,
correction, resolution, review, or evidence record and does not inspect whether
an affected path exists.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The synthetic triage snapshot is locally coherent under this candidate profile. |
| `ABSTAIN` | Required ownership, evidence, review, or review-cadence knowledge is unresolved. |
| `DENY` | Entry order, path safety, state bindings, correction, resolution, review, or authority boundaries contradict the profile. |
| `ERROR` | The input cannot be safely parsed, fails the closed schema, or has a mismatched content identity. |

`PASS` is fixture coherence only. It is not proof that drift exists, a correction
worked, a resolution is accepted, or any repository change is approved.

## Authority boundary

A validator result does not:

- create, edit, renumber, triage, resolve, withdraw, or delete a drift entry;
- inspect or mutate any declared affected path;
- create or accept an ADR, correction, resolution, review, or evidence record;
- assign an owner, steward, severity, due date, or review cadence;
- execute remediation, rollback, policy, data, runtime, or repository work;
- authorize promotion, release, deployment, publication, or public use.

## Directory Rules basis

Governance meaning belongs under `contracts/governance/`; machine shape under
`schemas/contracts/v1/governance/`; synthetic replay under
`fixtures/contracts/v1/governance/`; executable validation and proof under
`tools/validators/governance/` and `tests/validators/governance/`; read-only CI
under `.github/workflows/`; and source lineage under
`docs/intake/exploratory/`. `docs/registers/DRIFT_REGISTER.md` remains the human
register, and this packet does not establish a parallel machine authority.

## Validation and rollback

```bash
python -m unittest tests.validators.governance.test_validate_drift_register_triage_assessment -v
python tools/validators/governance/validate_drift_register_triage_assessment.py --fixtures
```

Rollback is one additive commit revert. The inactive packet creates no register,
triage, correction, resolution, policy, runtime, release, deployment,
publication, or public state that requires restoration.
