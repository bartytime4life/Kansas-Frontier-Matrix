<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-interface-evolution-assessment
title: SourceInterfaceEvolutionAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Source steward · Contract steward · Migration steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; source; interface-observation; compatibility; migration
owning_root: contracts/
responsibility: fixture-only separation of declared source identity, observed interface behavior, compatibility classification, consumer readiness, and proposed migration posture without changing any source or lifecycle state
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ./source_descriptor.md
  - ./source_health_assessment.md
  - ./web_delta_profile.md
  - ./source_activation_decision.md
  - ../../schemas/contracts/v1/source/source_interface_evolution_assessment.schema.json
  - ../../fixtures/contracts/v1/source/source_interface_evolution_assessment/cases.json
  - ../../tools/validators/source/validate_source_interface_evolution_assessment.py
  - ../../tests/validators/test_validate_source_interface_evolution_assessment.py
  - ../../docs/intake/exploratory/source-interface-evolution-source-map.md
tags: [kfm, source, interface, observation, compatibility, dual-read, migration, retirement, fixture]
notes:
  - "Adapts Full Atlas KFM-TRIAD-070 / KFM-CAND-0208..0210 as one bounded assessment profile."
  - "Observed deprecation, retirement, reactivation, or redirect signals remain assertions and cannot mutate declared source identity or lifecycle state."
[/KFM_META_BLOCK_V2] -->

# SourceInterfaceEvolutionAssessment Candidate Contract

SourceInterfaceEvolutionAssessmentCandidate records how a declared source interface compares with bounded synthetic observations. It separates declaration, observation, compatibility, consumer readiness, and migration proposal so that a transport or capability change cannot silently become a new canonical source identity.

## Source-derived gap

Full Atlas triad KFM-TRIAD-070 proposes explicit interface observations, compatibility windows, redirects, migration decisions, rollback posture, and retirement records. New Ideas 4-14-26 contains source-interface, deprecation, and redirect examples. Current KFM contracts cover source identity, health, web deltas, source activation, aliases, and graph migration, but the reviewed base has no source-lane family that composes these concerns into one reproducible compatibility assessment.

## Authority boundary

This profile assesses fixture declarations only. It does not contact a source, resolve evidence, accept an external lifecycle assertion, alter a SourceDescriptor, change an interface or connector, follow a redirect, change canonical identity, activate or retire a source, execute dual-read, migrate a consumer, perform rollback, authorize release, or permit public use.

The object always distinguishes:

- source_interface — the declared identity, profile, version, and capability set;
- observations — time-ordered evidence references and externally asserted behavior;
- compatibility — a reproduced comparison, never an authoritative source claim;
- consumers — explicit readiness, debt, and profile bindings;
- migration — a proposed disposition whose decision_has_effect is false;
- summary — a reproduced review posture whose trusted_surface_allowed is false.

## Finite compatibility grammar

The latest observation is classified into exactly one state:

| Classification | Reproduced condition | Default posture |
|---|---|---|
| UNCHANGED | Full observation matches profile, version, capabilities, and identity | NO_CHANGE |
| ADDITIVE | Full observation adds capability without removal | PROPOSE_MIGRATION only with rollback reference |
| BREAKING | Full observation removes a declared capability | Bound dual-read required |
| REDIRECTED | A redirect target is observed | HOLD |
| UNDOCUMENTED | Capabilities match while declared profile or version drifts | HOLD |
| PARTIAL_SAMPLE | Observation scope is not the full contract | HOLD |
| INCOMPARABLE | Canonical identity differs | DENY; use a separate identity decision |

Redirect classification takes precedence over partial scope. Partial scope takes precedence over capability comparison because a sample cannot prove the complete interface.

## Observation and identity rules

Observations are sorted by observed_at and observation_id, bind one evidence reference, declare observation scope, and carry response-shape and transport hashes. Hashes cannot use all-zero placeholders. Capabilities are sorted and unique.

An observed canonical identity is comparison input only. It is never authoritative. A mismatch fails closed rather than rewriting source_id, source_descriptor_ref, interface_id, or canonical_identity_ref.

DEPRECATED, SUNSET_SIGNALLED, RETIRED_ASSERTED, and REACTIVATED_ASSERTED are explicitly assertions. They hold migration unless the reproduced retirement posture is eligible only for a separate gate.

## Consumer and migration rules

Every consumer binds its current and observed target profile, readiness state, evidence references, and debt references. BLOCKED or UNKNOWN consumers hold migration. For a retirement assertion they become explicit retirement blockers.

A breaking active interface requires a bound dual-read declaration:

- old_profile_ref equals the declared profile;
- new_profile_ref equals the latest observed profile;
- evidence_refs is nonempty;
- NOT_RUN proposes dual-read only;
- MATCH plus rollback evidence may propose migration;
- MISMATCH plus rollback evidence may propose rollback;
- all other combinations hold.

PROPOSE_MIGRATION and PROPOSE_ROLLBACK require rollback_ref. A retirement assertion with no blocked or unknown consumers can produce PROPOSE_RETIREMENT_REVIEW, but the separate decision requirement remains true and the proposal has no effect.

## Deterministic invariants

- Declared capabilities, observed capabilities, references, observations, and consumers are canonicalized by explicit sort rules.
- Observation and consumer identifiers are unique.
- assessed_at is not earlier than the latest observation.
- Compatibility, added and removed capabilities, reason code, and identity posture are reproduced.
- Consumer target profiles bind to the latest observed profile.
- Dual-read profiles and evidence are reproduced against the declaration and latest observation.
- Migration disposition and retirement blockers are reproduced.
- Summary counts, affected consumers, blocked consumers, readiness, and assessment state are reproduced.
- spec_hash is RFC 8785 JCS plus SHA-256 over the object excluding only assessment_id and spec_hash.
- assessment_id derives from the first 24 digest characters.
- Every operational, lifecycle, release, publication, and public-use flag is false.

## Validator outcomes

PASS means the fixture declaration, ordering, compatibility, consumer bindings, migration proposal, summary, identity, and non-effect boundary agree. DENY identifies a schema, semantic, identity, or deterministic-reproduction defect. ERROR identifies unsafe JSON input. PASS does not mean the observed behavior is real, current, complete, approved, or safe to act on.

## Directory Rules basis

Source-interface meaning belongs in contracts/source/ under DIR-SCOPELANE-004. Machine shape belongs in schemas/contracts/v1/source/ under DIR-AUTHROOT-001. Synthetic cases, deterministic validation, tests, source mapping, platform CI, and authoring accountability remain in their existing fixture, tool, test, docs, platform, and receipt roots.

This packet does not modify the SourceDescriptor, SourceHealthAssessment, WebDeltaProfile, SourceActivationDecision, PathAliasRegister, or GraphMigrationDeclaration authorities.

## Validation

~~~bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_source_interface_evolution_assessment.py' \
  --verbose

python tools/validators/source/validate_source_interface_evolution_assessment.py \
  --fixtures
~~~

## Rollback

Before merge, close the draft PR and retire its branch. After an authorized merge, revert the additive packet. It has no source connector, runtime consumer, lifecycle writer, or released artifact, so rollback requires no source deactivation, migration reversal, release withdrawal, or public notice.
