<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/corroboration-role-assessment-source-map
title: Corroboration Role Assessment Source Map
type: exploratory-source-map; implementation-record
version: v0.1.0
status: proposed adaptation; fixture-only; production wiring held
owners: OWNER_TBD — Evidence steward · Source steward · Policy steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-adaptation; no-authority
related:
  - ../../../contracts/evidence/corroboration_role_assessment.md
  - ../../../schemas/contracts/v1/evidence/corroboration_role_assessment.schema.json
  - ../../../fixtures/contracts/v1/evidence/corroboration_role_assessment/cases.json
  - ../../../docs/kfm_full_atlas_seed_cards.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, full-atlas, corroboration, source-role, freshness, independence, overlap]
notes:
  - "Records a bounded repository adaptation of KFM-TRIAD-037 / KFM-CAND-0109..0111."
  - "The source candidates do not create evidence, confidence, claim, policy, review, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# Corroboration Role Assessment Source Map

## Source candidates

| Field | Value |
|---|---|
| Repository atlas | `docs/kfm_full_atlas_seed_cards.md` |
| Triad | `KFM-TRIAD-037` — Cross-source corroboration graph |
| Idea | `KFM-CAND-0109` — qualified relationships rather than raw source count |
| Feature | `KFM-CAND-0110` — support, contradiction, qualification, duplicate, inability to evaluate, independence, freshness, overlap, and role limitations |
| Programming card | `KFM-CAND-0111` — fail closed on role collapse, unresolved contradiction, missing freshness, and prohibited role combinations |
| Supporting source | Google Drive `New Ideas 4-16-26` (`1IqoqVHWERGK8VtLSUX69VBBmFNXqS62xBC2HE380Jrc`) |
| Retrieved evidence | Repository atlas and connected Google Drive source inspected 2026-08-10 |

The connected source supplies a concrete air-quality example in which runtime
observation, historical baseline, smoke context, and model context have
different evidence roles. It calls the relationship “Cross-Source
Corroboration” and separately proposes domain thresholds. This adaptation uses
the role and relationship pressure, but does **not** adopt any source-specific
threshold.

## Repository reconciliation

**CONFIRMED at `main@457e4fba09ef641efbddc0639bd8127e4c464b5a`:**

- `SourceDescriptor` already owns the finite source-role vocabulary;
- `EvidenceRef` already owns evidence identity rather than source payloads;
- `SourceConflictInfluenceAssessmentCandidate` preserves pairwise conflicts and
  declared influence, but does not model qualified corroboration independence,
  freshness, or spatiotemporal overlap;
- repository and open-PR searches found no implementation of
  `KFM-TRIAD-037`, `CorroborationRoleAssessment`, or
  `SourceIndependenceAssessment`; and
- accepted ADR-0029 routes this semantic object, schema, synthetic fixtures,
  validator, tests, workflow, exploratory record, and generated receipt to
  existing responsibility roots.

## Bounded adaptation

The implementation creates one composite fixture-only candidate rather than
two competing authorities. It copies the current source-role vocabulary,
requires a complete unordered pair matrix, and derives only a finite assessment
outcome from declared freshness, independence, overlap, compatibility, and
source relationship.

Two supporting sources yield `INSUFFICIENT` when their pair is shared upstream
or derived. A current independent pair with compatible roles and overlapping
support can yield `SUPPORTED`; qualification or partial overlap yields
`SUPPORTED_WITH_QUALIFICATION`. Contradiction is preserved, while missing
freshness, role collapse, prohibited roles, or unknown compatibility produce
`CANNOT_EVALUATE`.

## Source-pressure treatment

| Source pressure | Treatment | Boundary |
|---|---|---|
| Qualified source roles | **IMPLEMENTED AS DECLARATION** | Reuses `SourceDescriptor` roles; never upgrades authority. |
| Independence and dependency | **IMPLEMENTED AS CLOSED ENUMS** | Does not discover lineage or inspect source payloads. |
| Freshness | **IMPLEMENTED AS REPRODUCIBLE STATE** | Compares declared timestamps only; does not poll providers. |
| Spatial and temporal overlap | **IMPLEMENTED AS DECLARATION** | Does not perform geometry or temporal joins. |
| Support, qualification, contradiction, duplicate | **IMPLEMENTED AS DECLARATION** | Does not select truth or authorize a claim. |
| Raw source count as confidence | **REJECTED** | Schema has no score or confidence field; flag is fixed false. |
| Source-specific thresholds | **EXCLUDED** | Thresholds remain domain policy proposals outside this slice. |
| Runtime evidence resolution and production wiring | **HELD** | Requires accepted producers and separate evidence/policy/review/release gates. |

## Non-effects and rollback

The slice performs no source read, network request, evidence resolution, value
comparison, confidence calculation, claim decision, policy evaluation, review,
promotion, release, deployment, publication, or public-use authorization.

Before merge, close the draft and abandon its branch. After an authorized
merge, revert the bounded files together. No external or public state requires
restoration.
