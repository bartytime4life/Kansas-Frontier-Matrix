# Source adaptation — VerificationBacklogItem

## Goal

Convert the strongest repository-appropriate idea from the supplied **KFM Comprehensive Research and Verification Agenda** into a dependency-closed, fixture-only KFM governance record: one bounded uncertainty with explicit resolution modes, evidence, constraints, impact, acceptance, residual unknowns, and rollback/correction implications.

## Source-derived ideas incorporated

The Agenda requires every research item to record:

1. item ID and question;
2. resolution status using `CONFIRMED`, `PROPOSED`, `UNKNOWN`, or `NEEDS_VERIFICATION`;
3. answer and bounded scope;
4. primary evidence and direct locator;
5. version/date/access date and currentness risk;
6. rights, sensitivity, sovereignty, security, and public-use constraints;
7. conflicts and alternative interpretations;
8. affected KFM contract, schema, policy, source, test, runtime, release, and documentation surfaces;
9. recommended decision and owner role;
10. acceptance evidence, validation, rollback, and correction implications;
11. residual unknowns and the next check.

The Agenda also distinguishes five resolution modes—`EXT`, `REPO`, `DEC`, `STW`, and `TST`—and defines `P0` through `P3` priorities. Those distinctions are preserved as closed vocabularies rather than flattened into free-form prose.

## KFM adaptations

| Source idea | Adaptation |
|---|---|
| Required answer record | Closed `VerificationBacklogItem` schema with all required evidence, constraint, impact, acceptance, and residue surfaces. |
| Separate research modes | Exact mode vocabulary and validation that primary evidence uses only declared modes. |
| Fail closed on sensitive uncertainty | Rights, sensitivity, sovereignty, security, and public-use `UNKNOWN` or `REVIEW_REQUIRED` states keep the item on `HOLD`. |
| Current evidence over plausible inference | A resolved item requires confirmed status, primary evidence, acceptance evidence, validation tests, and no residual unknowns. |
| Explicit residue list | `resolution.residual_unknowns` and `recommendation.next_check` remain first-class. |
| Reversibility | Every item carries a closure condition and rollback/correction implication. |
| Prioritized decision packet | `P0`–`P3` is retained for ordering without granting authority. |

## Directory and authority decision

Directory Rules v2 says:

- `contracts/` owns object meaning;
- `schemas/` owns machine shape;
- `policy/` owns allow/deny/hold/restrict/abstain rules;
- `docs/registers/` contains human-readable verification views;
- `control_plane/` contains machine projections of **accepted** governance and cannot self-authorize a new rule.

Therefore this slice adds the semantic contract, schema, fixture suite, validator, tests, CI, and authoring receipt, but it does **not** create or modify a `control_plane/` verification register. A live register class remains separate governance work.

## Existing repository fit

Current repository evidence already includes:

- `docs/registers/VERIFICATION_BACKLOG.md`;
- domain-specific verification backlog documents;
- `contracts/governance/README.md`, which names `VerificationBacklogItem` as a proposed object family;
- accepted ADR-0029 and the adopted Directory Rules v2 path authority;
- shared RFC 8785 JCS plus SHA-256 support under `packages/hashing/`;
- established fixture-first governance validator patterns; and
- small private validator modules that separate bounded JSON/schema/identity, semantic outcomes, compact fixture expansion, and CLI orchestration.

The new object makes the proposed family executable without replacing the existing human registers.

## Ideas deliberately excluded

- live web research or repository inspection;
- automated source activation;
- automatic ADR, policy, review, or steward decisions;
- automatic mutation of docs or control-plane registers;
- storing private reasoning, protected source payloads, credentials, or sensitive exact locations;
- treating a green validator as evidence, proof, review approval, release, or publication authority.

## Evidence boundary

The supplied Agenda is a **PROPOSED research brief**, not proof of current implementation. Current repository presence and placement were verified separately before this change. The object family itself remains `PROPOSED_INACTIVE` and fixture-only.

## Rollback

Close the draft pull request before merge, or revert the additive feature commit after an authorized merge. No source, lifecycle state, release, deployment, or public product is affected.
