<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/policy/policy-obligation
title: PolicyObligation Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Policy steward · Contracts steward · Schema steward · Validation steward · Runtime steward · Release steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; fixture-only; non-authoritative
authority_root: contracts/
current_path: contracts/policy/policy_obligation.md
related:
  - ./policy_decision.md
  - ./policy_decision_vocabulary.md
  - ./policy_obligation_reduction.md
  - ../../schemas/contracts/v1/policy/policy_obligation.schema.json
  - ../../policy/decision/vocabulary.v1.json
  - ../../fixtures/contracts/v1/policy/policy_obligation/
  - ../../tools/validators/policy/validate_policy_obligation.py
  - ../../tests/validators/test_validate_policy_obligation.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, policy, obligation, duties, enforcement, evidence, rights, sensitivity, release, fixture-first]
notes:
  - "This contract gives PolicyDecision obligation codes a parameterized, separately addressable carrier."
  - "The profile is inactive and fixture-only; it does not evaluate policy or prove enforcement."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# PolicyObligation Contract

> A `PolicyObligation` is a structured duty attached to an already-issued policy decision. It records what must happen, for which operation and audience, with which parameters, during which interval, and whether enforcement is pending or evidenced. It does not author policy, apply a transform, grant access, or authorize release or publication.

## Status and authority boundary

| Field | Value |
|---|---|
| Profile status | `PROPOSED_INACTIVE` |
| Execution mode | fixture-only, no network |
| Vocabulary authority | `policy/decision/vocabulary.v1.json` |
| Machine shape | `schemas/contracts/v1/policy/policy_obligation.schema.json` |
| Validator | `tools/validators/policy/validate_policy_obligation.py` |
| Policy evaluation | none |
| Enforcement execution | none |
| Promotion, release, publication, or public-use effect | none |

A conforming record proves only that one synthetic obligation carrier is well-shaped, references a registered code, is coherent for that code, has canonical arrays and time ordering, reproduces its `spec_hash`, and does not claim governance effects.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. This slice uses existing responsibility roots:

| Responsibility | Path family |
|---|---|
| Object meaning | `contracts/policy/` |
| Machine shape | `schemas/contracts/v1/policy/` |
| Vocabulary and policy-owned registry | `policy/decision/` |
| Synthetic fixtures | `fixtures/contracts/v1/policy/` |
| Validation implementation | `tools/validators/policy/` |
| Tests | `tests/validators/` |
| Read-only CI | `.github/workflows/` |
| Authoring accountability | `data/receipts/generated/` |

No root, executable-policy authority, source registry, release home, proof home, or public route is added.

## Relationship to existing policy objects

| Object | Relationship |
|---|---|
| `PolicyDecision` | Continues to carry compact string obligation codes. Each structured obligation points back through `policy_decision_ref`; adding forward `obligation_refs` remains future work. |
| `PolicyDecisionVocabulary` | Defines the admitted code and policy-family combination. This contract does not duplicate the registry. |
| `PolicyObligationReduction` | Reduces a specialized geoprivacy/date/embargo projection of already-issued obligations. It remains separate and non-authoritative. |
| Policy runtime | May later resolve and enforce obligations, but that implementation is outside this slice. |
| Release gates | Must verify required obligations before release; this object is not release approval. |

## Required field families

| Family | Meaning |
|---|---|
| Identity | `obligation_id`, schema version, and RFC 8785 JCS + SHA-256 `spec_hash`. |
| Source decision | `policy_decision_ref`, `policy_family`, registered `code`. |
| Scope | Operation, object scope, and admitted audiences. |
| Parameters | Explicit typed values for citations, rights notices, geometry, embargo, retention, aggregation, review, share-alike, export, and rollback checks. Unused parameters remain `null` or an empty array. |
| Valid time | Effective start and optional end; end cannot precede start. |
| Enforcement | `PENDING`, `SATISFIED`, `UNSATISFIED`, `CONFLICTED`, or `WAIVED`, with evidence/ref requirements appropriate to the state. |
| Explanation | Public-safe explanation plus an optional internal reason reference; sensitive facts are not embedded. |
| Non-effects | All governance flags remain false. |

## Code-specific parameter rules

| Code | Required parameter |
|---|---|
| `ATTACH_CITATIONS` | nonempty `required_evidence_refs` |
| `ATTACH_RIGHTS_NOTICE` | `required_notice_ref` |
| `DELAY_PUBLICATION` | `embargo_until` |
| `GENERALIZE_GEOMETRY` | positive `generalize_distance_m` |
| `REDACT_EXACT_LOCATION` | `suppress_geometry: true` |
| `REQUIRE_STEWARD_REVIEW` | `review_role` |
| `VERIFY_ROLLBACK_TARGET` | `rollback_target_ref` |
| `WITHHOLD_EXPORT` | `export_allowed: false` |
| `AGGREGATE_ONLY` | `minimum_group_size >= 2` or `aggregation_unit_ref` |
| `RETAIN_UNTIL` | `retain_until` |
| `SHARE_ALIKE` | `share_alike_license_ref` |

The validator checks code membership and the code's admitted policy families against the policy-owned vocabulary. It does not decide whether the code should have been issued.

## Enforcement-state invariants

- `PENDING` has no evaluator, evaluation time, or waiver reference.
- `SATISFIED`, `UNSATISFIED`, and `CONFLICTED` require an evaluator, evaluation time, and at least one evidence reference; they cannot carry a waiver reference.
- `WAIVED` requires an evaluator, evaluation time, and waiver reference.
- An enforcement state is a recorded claim that still requires authoritative evidence and release-gate verification; schema validity alone does not prove it.

## Deterministic identity

`spec_hash` is computed over the full record except the `spec_hash` field using the repository hashing profile, RFC 8785 JCS plus SHA-256. Arrays that express sets must be sorted and unique before hashing.

## Failure posture

The validator emits only `PASS`, `FAIL`, or `ERROR`, with stable field pointers and finding codes. It does not echo untrusted values. Unknown codes, missing code-specific parameters, family mismatch, time reversal, incoherent enforcement state, hash drift, and governance overclaim fail closed.

## Compatibility

- Existing `PolicyDecision.obligations` string arrays remain valid.
- The current `PolicyDecision` schema is unchanged; structured records bind back to it through `policy_decision_ref`.
- Existing policy-obligation reduction and transform simulation profiles remain unchanged.
- No consumer, policy bundle, runtime route, lifecycle data, release, or public surface is activated.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_policy_obligation.py' \
  --verbose

python tools/validators/policy/validate_policy_obligation.py --fixtures
python tools/validators/policy/validate_policy_decision_vocabulary.py --registry
```

## Rollback

Before merge, close the draft pull request and delete its feature branch. After an authorized merge, revert the implementation commit or merge commit. The profile is inactive and fixture-only, so rollback requires no source deactivation, data migration, cache invalidation, release withdrawal, or public correction.

## Open verification

- Which accepted policy runtime will resolve `obligation_refs` and prove fulfillment?
- Which receipt type binds enforcement evidence to exact output bytes or response payloads?
- Which reviewer classes may authorize a waiver?
- When should a `PolicyObligation` graduate from inactive fixture profile to a required release-gate input?

<p align="right"><a href="#top">Back to top</a></p>
