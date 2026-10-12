# Policy Reviewer Role Vocabulary

Status: **PROPOSED_INACTIVE** · scope: stable reviewer-role identifiers for policy and release review routing.

Pass 9 calls for stable policy reason, obligation, and reviewer-role vocabularies. Reason and obligation codes already have a repository contract; this follow-on fills the reviewer-role gap without assigning people, approvals, or authority.

## Invariants

- role identifiers are stable uppercase snake-case tokens;
- every role declares a bounded responsibility and compatible review scopes;
- a role is a class of review responsibility, not proof that a qualified reviewer exists or approved a candidate;
- duplicate codes or overlapping aliases fail validation;
- all authority flags remain false;
- no role token may create evidence, policy approval, lifecycle promotion, release, or publication authority.

## Initial roles

`POLICY_STEWARD`, `EVIDENCE_STEWARD`, `DOMAIN_STEWARD`, `RELEASE_STEWARD`, and `SECURITY_PRIVACY_REVIEWER` are proposed first-wave identifiers. Their acceptance and assignment remain separate governance actions.

## Directory Rules basis

Accepted ADR-0029 assigns semantic meaning to `contracts/policy/`, machine shape to `schemas/contracts/v1/policy/`, inactive policy vocabulary source to `policy/decision/`, fixtures to `fixtures/`, validation to `tools/validators/`, tests to `tests/`, and CI to `.github/workflows/`.