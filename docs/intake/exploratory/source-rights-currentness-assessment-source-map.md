# SourceRightsCurrentnessAssessment source and adaptation map

## Status

**PROPOSED_INACTIVE.** This note records the source basis and adaptation boundary for a fixture-only assessment object. It is not a source review, rights decision, activation decision, or publication decision.

## Source basis

- `KFM_Comprehensive_Research_and_Verification_Agenda.docx`, especially P0 source-rights/currentness work and workstream W05.
- `KFM_Briefing_to_System_Integration_Architecture.docx`, source admission, official-source verification, correction, and rollback sections.
- the existing repository `SourceDescriptor`, `SourceActivationDecision`, and `SourcePollingCheckpoint` families.
- accepted Directory Rules v2 through `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`.

## Adaptation decision

The assessment is intentionally separate from:

- `SourceDescriptor`, which records the source's governed posture;
- `SourceActivationDecision`, which decides whether a connector/source may be activated;
- `SourcePollingCheckpoint`, which compares conditional validator state;
- evidence objects, which support claims; and
- release objects, which govern public state.

It adds dated review evidence without modifying any of those authorities. A known restriction can be current; `CURRENT` does not mean publicly reusable.

## Follow-on queue

1. Bind a real steward-authored assessment to a reviewed `SourceDescriptor` only after rights review policy is ratified.
2. Add source-specific adapters only in separately reviewed, network-capable work.
3. Connect activation policy to assessment references without letting the assessment self-authorize.
4. Add expiry/watch behavior only after operational cadence and reviewer ownership are verified.

## Non-effects

No official endpoint is contacted; no terms are accepted; no rights are asserted; no source is activated; no data enters RAW; and no release or publication authority is created.
