<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/stale-state-supersession-assessment
title: StaleStateSupersessionAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD - Data steward · Evidence steward · Correction steward · Release steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; common; stale-state; supersession; lineage; review-required
responsibility: Define a fixture-only assessment of stale-state and supersession declarations without changing an object, rewriting history, resolving evidence or policy, issuing a correction, or granting lifecycle, release, or publication authority.
truth_posture: "CONFIRMED connected Full Atlas proposal, current repository stale-state reference, accepted Directory Rules, adjacent correction/release contracts, and bounded implementation gap; PROPOSED inactive assessment; UNKNOWN cross-lane propagation policy and steward ownership; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../docs/atlases/stale-state-reference.md
  - ../../docs/doctrine/directory-rules.md
  - ../../schemas/contracts/v1/common/stale_state_supersession_assessment.schema.json
  - ../../fixtures/contracts/v1/common/stale_state_supersession_assessment/cases.json
  - ../../tools/validators/governance/validate_stale_state_supersession_assessment.py
  - ../../tests/validators/governance/test_validate_stale_state_supersession_assessment.py
  - ../../docs/intake/exploratory/full-atlas-stale-state-supersession-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# StaleStateSupersessionAssessment Candidate

`StaleStateSupersessionAssessmentCandidate` is an additive, fixture-only
declaration that makes one object's stale-state signal, lineage relation,
proposed response, affected surfaces, review posture, and non-authority boundary
inspectable. It adapts the Full Atlas "Stale-State and Supersession Lineage"
proposal without resolving the repository's open cross-lane propagation
decision.

The candidate distinguishes **stale** from **incorrect**. A stale object has
aged beyond a declared support condition; that alone does not prove its
substance wrong. An object known to be incorrect requires explicit correction
or withdrawal linkage. Neither conclusion is inferred merely from file age,
schema validity, a newer version, or a passing workflow.

## Declared assessment

| Concern | Required declaration | Local check |
|---|---|---|
| Subject | Stable object ref, family, version, declared state, and exposure. | The assessment never edits or resolves the referenced object. |
| Stale signal | One bounded marker, detection time, basis refs, and substance posture. | Unknown or unsupported signals abstain; contradictions deny. |
| Lineage | Relation, predecessor/successor refs, effective time, retention, and lineage refs. | Silent rebinds, self-links, missing successors, and discarded prior versions deny. |
| Proposed response | Review-only action plus correction, withdrawal, rollback, decision, and affected-surface refs where applicable. | No action is executed; public or incorrect cases must retain the appropriate closure refs. |
| Review | Pending, unknown, or complete-for-declared-scope with record refs. | A locally coherent candidate remains `REVIEW_REQUIRED`; it never becomes approved. |

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `REVIEW_REQUIRED` | The fixture-only declaration is locally coherent and still requires human review plus resolution of every referenced authority object. |
| `ABSTAIN` | The marker, lineage, support basis, next action, or review posture remains unresolved. |
| `DENY` | The declaration would erase lineage, silently rebind state, mutate an AI receipt retroactively, omit required correction/rollback support, contradict its own state, or cross the trust membrane. |
| `ERROR` | The candidate cannot be safely parsed or evaluated under the closed schema. |

## Invariants

- Prior versions remain retained for audit; supersession is a link, not deletion.
- A successor cannot be the same object as the subject or predecessor.
- `AI_RECEIPT` history is immutable: a corrected answer is a new receipt with a
  cross-reference, never an in-place supersession.
- `SCHEMA` and `POLICY` supersession proposals carry an ADR reference; the
  validator does not claim the ADR is accepted.
- `PUBLISHED` subjects proposed for supersession or withdrawal carry a rollback
  ref and affected-surface refs.
- `INCORRECT` substance carries a correction or withdrawal ref.
- No candidate may reference RAW, WORK, QUARANTINE, direct stores, or embedded
  query text as a public lineage shortcut.

## Authority boundary

A validator result does not:

- mark an object stale, current, superseded, corrected, withdrawn, or released;
- resolve a SourceDescriptor, EvidenceBundle, ReviewRecord, PolicyDecision,
  CorrectionNotice, WithdrawalNotice, ReleaseManifest, or RollbackCard;
- rewrite an AI receipt or any prior artifact;
- decide cross-lane propagation, invalidate caches, or update public surfaces;
- approve review or authorize lifecycle mutation, promotion, release,
  deployment, publication, or public use.

## Directory Rules basis

The object is a cross-family semantic assessment, so its meaning belongs under
`contracts/common/`. Machine shape, synthetic fixtures, executable validation,
tests, read-only CI, source lineage, and authoring provenance remain in their
established responsibility roots. No new correction, supersession, registry,
receipt, proof, policy, release, or publication home is created.

## Validation and rollback

```bash
python -m unittest tests.validators.governance.test_validate_stale_state_supersession_assessment -v
python tools/validators/governance/validate_stale_state_supersession_assessment.py --fixtures
```

Rollback is one additive commit revert. The inactive packet creates no object,
lineage, correction, cache, release, deployment, publication, or public state
that requires restoration.
