<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-cross-domain-readme
title: contracts/cross_domain/ — Cross-Domain Semantic Contracts
type: readme
version: v0.2.1
status: draft; repository-grounded; mixed-maturity; non-publisher
owners: OWNER_TBD — Contract steward · Architecture steward · Participating domain stewards
created: 2026-06-20
updated: 2026-09-07
owning_root: contracts/
responsibility: Index cross-domain semantic contracts while preserving domain ownership and the separation of candidate assessment, evidence, policy, review, and release.
truth_posture: CONFIRMED pinned inventory and adopted placement; PROPOSED or draft child contracts; execution and public readiness not established by this README.
evidence_snapshot: bartytime4life/Kansas-Frontier-Matrix@6087d07b49362540e437dc666d1cbaa6eb6b82c3
prior_blob: 58c2f1bfaa4f9b49676c339b2977a1c46ffcf88a
policy_label: repository-facing; cross-domain; semantic-contracts; cite-or-abstain; no-parallel-authority
related:
  - ../README.md
  - ./knowledge_character.md
  - ./fauna_habitat/public_safe_assignment_profile.md
  - ./soil_agriculture/public_safe_context_profile.md
  - ./soil_hydrology/public_safe_context_profile.md
  - ../joins/cross_lane_join_assessment.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../control_plane/cross_domain_seam_register.yaml
notes:
  - "Same-path README revision plus generated authoring provenance; no child contract, schema, policy, validator, fixture, test, register, or public behavior changes."
  - "The adopted cross_domain container is not an unresolved naming proposal. Mapping existing pair directories to registered seam IDs remains separate work."
  - "Presence, declared contract status, executed validation, and permission to publish are independent claims."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Cross-Domain Semantic Contracts

> `contracts/cross_domain/` indexes meaning that spans KFM domains. It does not
> transfer ownership of atomic facts, turn a fixture candidate into a relationship
> claim, or authorize a public join.

## Quick jumps

[Status](#status) · [Scope](#scope) · [Path posture](#path-posture) ·
[Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) ·
[Exclusions](#exclusions) · [Current directory snapshot](#current-directory-snapshot) ·
[Contract inventory](#contract-inventory) · [Placement rules](#cross-domain-placement-rules) ·
[Semantic rules](#semantic-contract-rules) · [Trust boundary](#lifecycle-and-trust-boundary) ·
[Validation](#validation) · [Evidence](#evidence-basis) · [Rollback](#rollback) ·
[Definition of done](#definition-of-done)

## Status

| Concern | Bounded status |
|---|---|
| Evidence checkpoint | `main@6087d07b49362540e437dc666d1cbaa6eb6b82c3`, rechecked 2026-09-07 CT |
| Document | `draft`; directory index and semantic-boundary guidance, not a new contract family |
| Owning responsibility | `contracts/` owns semantic meaning and interface promises |
| Container placement | **CONFIRMED adopted pattern** under Directory Rules v2 §12.5 and accepted ADR-0029 |
| Tracked inventory | **CONFIRMED:** five Markdown files recursively, including this README, in the pinned subtree |
| Child maturity | KnowledgeCharacter is `draft`; the three pair profiles remain `proposed`, fixture-first, no-network, and non-authoritative |
| Stewardship | `OWNER_TBD`; this update does not appoint stewards or establish independent review |
| Execution and public readiness | **NEEDS VERIFICATION:** this index is not evidence of passing native tests, live policy, evidence resolution, source admission, release, or runtime behavior |

The [parent contract README](../README.md) supplies the meaning/shape/policy split.
A contract's presence is confirmed independently of whether its design is adopted,
its implementation passes, or its outputs may be published.

## Scope

This directory is for shared semantic markers and pair-specific contract profiles
that legitimately cross bounded domain contexts. A cross-domain contract must
identify its participants, preserve the owner of each atomic fact, and explain
why a single-domain contract is insufficient. Reuse shared object families rather
than copying identity, time, evidence, or policy definitions into each pair.

Generic candidate-assessment meaning remains in
[CrossLaneJoinAssessment](../joins/cross_lane_join_assessment.md). This directory
adds pair-specific meaning; it is not a replacement generic join engine or a
repository-wide source-role crosswalk.

## Path posture

[Directory Rules](../../docs/doctrine/directory-rules.md), adopted by
[ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md),
explicitly place cross-domain semantic contracts under
`contracts/cross_domain/<seam_id>/`. The previous edition's uncertainty about the
`cross_domain` container is superseded by that accepted placement authority.

The following distinctions remain important:

| Surface | Current interpretation |
|---|---|
| `contracts/cross_domain/` | Adopted semantic-contract container, not a new domain or repository root |
| `fauna_habitat/`, `soil_agriculture/`, `soil_hydrology/` | Existing fixture-profile directories; their presence does not establish registered canonical seam IDs |
| `knowledge_character.md` | Existing shared semantic draft retained at its current path; not silently moved into a pair directory |
| Registered seam identifiers and aliases | Governed separately; Directory Rules §13 defaults seam slugs to kebab-case and requires explicit identity/alias decisions |
| Paired schema, policy, fixture, and implementation homes | Follow the responsible existing family; do not create matching directory trees merely for symmetry |

This revision neither renames existing paths nor adopts a directory-to-seam alias.
Any later move needs consumer/link closure, explicit placement evidence, and a
reversible migration; an authority-changing decision needs the applicable ADR.

## Repo fit

Use this index to find the pair contract, then follow its existing generic,
machine-shape, validator, fixture, and test dependencies. Those dependencies do
not acquire semantic ownership merely by importing or validating a contract.

| Responsibility | Existing navigation or governing basis |
|---|---|
| Semantic meaning | [Contract root](../README.md) and the child contracts below |
| Generic join assessment | [CrossLaneJoinAssessment](../joins/cross_lane_join_assessment.md) |
| Generic machine shape | [Join-assessment schema](../../schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json) |
| Seam coordination | [Cross-domain seam register](../../control_plane/cross_domain_seam_register.yaml), a partial proposal/review projection |
| Placement and root boundaries | [Adopted Directory Rules](../../docs/doctrine/directory-rules.md) §§7, 11–13 |
| Contributor and delivery controls | [CONTRIBUTING](../../CONTRIBUTING.md) |

## Accepted inputs

Appropriate content includes cross-domain semantic contracts, contract-family
navigation, field intent, relation meaning, input/exclusion rules, compatibility
notes, and evidence-backed validation or migration guidance. A contract for a
derived product must name its source-domain dependencies without absorbing their
facts or declaring its own output authoritative.

Evidence ledgers here are references and documentation provenance, not stored
EvidenceBundles, process receipts, proofs, source records, or release decisions.

## Exclusions

| Excluded responsibility | Owning boundary |
|---|---|
| Single-domain observations or terminology | The existing owning-domain contract; do not choose a lead domain to disguise a cross-domain seam |
| Machine-checkable shape | `schemas/`, using the established schema family rather than a parallel schema inside `contracts/` |
| Executable admissibility rules | `policy/`; contract prose does not execute policy |
| Validator implementation | `tools/` or the established implementation owner |
| Fixtures and executable tests | `fixtures/` and `tests/`, with declared reuse rather than competing copies |
| Source records, lifecycle instances, receipts, and proofs | Their governed lanes under `data/`; receipts and proofs are not interchangeable |
| Release, correction, withdrawal, and rollback decisions | `release/`; released carrier bytes remain separate under `data/published/` |
| Public API, UI, map, or AI implementation | Its governed application/package boundary; this directory is not a runtime or publication path |
| A root-level `cross_domain/` or duplicate domain doctrine | Not authorized by this README |

## Current directory snapshot

The direct children at the evidence checkpoint are shown below, following
Directory Rules `DIR-README-003`. The contract inventory links the deeper files.

```text
contracts/cross_domain/
├── README.md
├── knowledge_character.md
├── fauna_habitat/
├── soil_agriculture/
└── soil_hydrology/
```

The recursive inventory contains five Markdown files: this README and the four
contracts below. This corrects the older README-only inventory. It proves tracked
presence at the pinned commit, not complete cross-domain coverage or production
readiness.

## Contract inventory

| Contract | Declared maturity and meaning | Must not be inferred |
|---|---|---|
| [KnowledgeCharacter](knowledge_character.md) | `v0.2`, `draft`; object-level epistemic character with Atmosphere vocabulary lineage | A settled cross-domain enum/registry, a verified paired schema, evidence validity, or replacement of SourceDescriptor source role |
| [Fauna–Habitat assignment profile](fauna_habitat/public_safe_assignment_profile.md) | `v0.1.0`, `proposed`; synthetic generalized occurrence-reference and habitat-patch-reference candidate | An observed occurrence, established population, ecological assignment, or public relationship |
| [Soil–Agriculture context profile](soil_agriculture/public_safe_context_profile.md) | `v0.1.0`, `proposed`; synthetic Soil and aggregate/public-safe Agriculture context candidate | Crop suitability, observed yield, causation, farm ownership, or a private farm/operator/parcel/yield join |
| [Soil–Hydrology context profile](soil_hydrology/public_safe_context_profile.md) | `v0.1.0`, `proposed`; synthetic generalized Soil and Hydrology context candidate; non-emergency | Runoff/infiltration causation, flood risk, warnings, regulatory truth, or measured stream conditions |

All three pair validators have a code-bearing module that imports the generic
join helper. Their linked test modules and fixture directories also exist:

| Pair | Validator | Fixtures | Focused tests |
|---|---|---|---|
| Fauna–Habitat | [Assignment validator](../../tools/validators/cross_domain/fauna_habitat/validate_public_safe_assignment.py) | [Fixture directory](../../fixtures/contracts/v1/joins/fauna_habitat_public_safe_assignment/) | [Assignment tests](../../tests/cross_domain/fauna_habitat/test_public_safe_assignment.py) |
| Soil–Agriculture | [Context validator](../../tools/validators/cross_domain/soil_agriculture/validate_public_safe_context.py) | [Fixture directory](../../fixtures/contracts/v1/joins/soil_agriculture_public_safe_context/) | [Context tests](../../tests/cross_domain/soil_agriculture/test_public_safe_context.py) |
| Soil–Hydrology | [Context validator](../../tools/validators/cross_domain/soil_hydrology/validate_public_safe_context.py) | [Fixture directory](../../fixtures/contracts/v1/joins/soil_hydrology_public_safe_context/) | [Context tests](../../tests/cross_domain/soil_hydrology/test_public_safe_context.py) |

**Inspection is not execution.** These links establish existing companion
surfaces, not that every invariant is enforced or that the suites currently pass.
The pair documents retain historical introductory wording about profiles not yet
existing; that wording is not a current inventory. This README does not alter
those documents or silently promote their proposed status.

KnowledgeCharacter's paired machine schema, canonical enum, registry placement,
and consumer enforcement remain **NEEDS VERIFICATION** in this revision. The
join schema's source-role enum is not evidence that KnowledgeCharacter is settled.

## Cross-domain placement rules

Choose the responsibility root first, then the registered seam or existing
object-family lane. Keep domain-owned facts in their own contexts and cross-link
rather than copy. A pair's left/right ordering is an execution convention, not
an assignment of superior domain authority.

The [seam register](../../control_plane/cross_domain_seam_register.yaml) is
`PROPOSED`, partial, and explicitly navigational/review-only. Its five initial
entries all declare `HOLD_UNRESOLVED`, `public_join_allowed: false`, and
`seam_contract_path: null` at the checkpoint. Its defaults preserve each
participant's EvidenceBundle and release requirements, source roles, and the
most restrictive policy/sensitivity posture.

Those five entries are not a one-to-one inventory of the three fixture-profile
directories above. In particular, similarity between the agriculture/soil seam
name and `soil_agriculture/` does not resolve the missing mapping or authorize a
public join. Do not fill null paths, accept an alias, add a seam, or clear a hold
as a side effect of updating this index.

## Semantic contract rules

Each cross-domain contract must make the following reviewable:

1. **Ownership and meaning:** participants, atomic-fact owners, relation meaning,
   accepted inputs, exclusions, and why the shared boundary is necessary.
2. **Identity and scope:** input/source/dataset versions, deterministic identity
   where practical, spatial support and precision, valid/observed/retrieval or
   release times as applicable, and explicit matching/tolerance semantics.
3. **Source roles and evidence:** preserve per-input roles and object knowledge
   character; require claim-appropriate `EvidenceRef -> EvidenceBundle` closure.
   References in synthetic tests do not prove resolution or admissible evidence.
4. **Rights and sensitivity:** begin with the most restrictive input posture and
   assess the combined result. A join may reveal more than either input alone.
   Unclear rights, living-person/DNA, cultural/archaeological, rare-species,
   private-land, or infrastructure sensitivity must not become public by joining.
5. **Governance and reversibility:** distinguish validation, policy, review, proof,
   release, correction, affected consumers, withdrawal, replay, and rollback.
   Declare downstream map/API/AI limitations and how corrections propagate.

The [generic join contract](../joins/cross_lane_join_assessment.md) owns its finite
assessment vocabulary:

| Outcome | Bounded interpretation |
|---|---|
| `ALLOW` / `JOIN_CANDIDATE` | Candidate assessment only; output role remains `CANDIDATE_RELATION`; no evidence creation, policy/review/release decision, lifecycle write, publication, or public-use authorization |
| `ABSTAIN` | Evidence, role, sensitivity, matching, domain scope/alias, or temporal semantics require resolution; preserve the specific reason and obligation |
| `DENY` | The generic privacy/sensitivity boundary forbids candidate emission under the supplied fixture posture |
| `ERROR` | A required dependency is unavailable or invalid; no candidate is asserted |

Do not substitute `ANSWER` or `HOLD` for these assessment outcomes.
`HOLD_UNRESOLVED` in the seam register is a different work-state vocabulary.
A pair validator's `PASS` means its assessed report is coherent with that profile;
a correctly denied or abstaining fixture can pass validation without becoming an
allowed join.

The generic profile abstains on every unequal source-role vector; it owns no
global role-equivalence crosswalk. It also distinguishes same-domain or unresolved
alias pairs and zero-tolerance intervals that only touch at a boundary. Its
`SPATIAL_TEMPORAL` comparison uses synthetic cell references and intervals, not
real geometry; a matched fixture is not a measured spatial relationship.

## Lifecycle and trust boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This is governed lifecycle doctrine, not a claim that the pair validators execute
it. QUARANTINE is conditional, graph/triplet projection is optional, and promotion
is a governed transition rather than a file move.

Before public use, the responsible system must establish identity, rights,
sensitivity, validation, provenance, integrity, receipts/proofs, policy, review,
release, correction, and rollback support. `EvidenceRef -> EvidenceBundle`
resolution is necessary for evidence-dependent claims but is not itself release
permission. Receipts record process; proofs support closure; release records
carry decisions; `data/published/` carries released public-safe outputs.

Public clients consume governed APIs and released artifacts, never RAW, WORK,
QUARANTINE, unreleased internal stores, or direct model output. Maps, tiles,
graphs, indexes, scenes, exports, summaries, and AI are downstream carriers, not
truth authorities. A renderer toggle or fluent explanation cannot lift a join
hold, create evidence, or approve publication.

## Validation

For a documentation-only change, verify the pinned inventory, adopted placement
basis, relative links, heading anchors, truth labels, candidate/public separation,
and the README plus required authoring-receipt scope. Record actual commands,
results, unrun checks, and the exact base/head in the delivery evidence; do not
inherit a green result from an older commit or infer one from a workflow definition.

AI-authored revisions require provenance in the existing
[generated-receipt lane](../../data/receipts/generated/README.md), with final
artifact hashes and pending human review. Validate the receipt's schema and
artifact binding separately; neither is independent approval or release proof.

For changes to a pair profile or its implementation, use a provisioned repository
environment following [CONTRIBUTING](../../CONTRIBUTING.md). The existing focused
pytest modules can be selected together without colliding on duplicate basenames:

```bash
python -m pytest -q --import-mode=importlib \
  tests/cross_domain/fauna_habitat/test_public_safe_assignment.py \
  tests/cross_domain/soil_agriculture/test_public_safe_context.py \
  tests/cross_domain/soil_hydrology/test_public_safe_context.py
```

These are validation instructions, **not results from this README revision**.
Also run the generic regressions identified by
[CrossLaneJoinAssessment](../joins/cross_lane_join_assessment.md) when changing
shared behavior, and the affected schema, policy, fixture, receipt-integrity,
workflow, and consumer checks required by the actual diff.

Review negative behavior for missing evidence, unequal source roles, unavailable
dependencies, same-domain/unresolved-alias pairs, ambiguous temporal boundaries,
restricted exact or generalized context, living-person joins, forbidden private
agricultural context, and unsupported hydrologic/ecological claims. Report
whether each case is specified, implemented, or actually tested; this checklist
does not assert complete coverage.

## Evidence basis

| Source inspected | Supports | Limit |
|---|---|---|
| Pinned target and recursive child-tree reads | Five-file inventory and immediately prior README blob | Not a repository-wide capability census |
| [Directory Rules](../../docs/doctrine/directory-rules.md) and [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adopted semantic root, seam placement, identity, data/release separation | No automatic acceptance of a child profile or seam alias |
| [Parent README](../README.md), four child contracts, and [generic join contract](../joins/cross_lane_join_assessment.md) | Meaning, local statuses, ownership and candidate boundaries | Historical self-descriptions are not current implementation proof |
| Linked schema, validator headers/imports, test definitions, and fixture path/header reads | Existing machine-shape and code-bearing companion surfaces | Not a full code audit or executed schema/test/policy result |
| [Seam register](../../control_plane/cross_domain_seam_register.yaml) | Five held entries, partial projection, null contract mappings, non-effects | Not semantic adoption, complete coverage, or public-join permission |
| [Drive Directory Rules](https://docs.google.com/document/d/1uTqdIEFZE2cq3gyISetoRYM6LIlnKqTc3FobtEx7Cbs/edit) | Read-only responsibility-root and authority-separation lineage | Adopted repository doctrine controls current placement |
| [Notion Repository Workbench](https://app.notion.com/p/3c9a92021bf68195b8b1f3a8d694b447) and [CONTRIBUTING](../../CONTRIBUTING.md) | Coordination and bounded delivery context | No implementation, approval, merge, deployment, or publication authority by coordination prose |

All repository observations above use the checkpoint in [Status](#status).
Drive and Notion are references, not additional writable copies of this README.
This revision reports no native pytest run, live policy execution, hosted CI pass,
EvidenceBundle resolution, runtime validation, or independent approval.

## Rollback

The immediately preceding target is the **nonblank** README blob
`58c2f1bfaa4f9b49676c339b2977a1c46ffcf88a` at
`6087d07b49362540e437dc666d1cbaa6eb6b82c3`. The earlier task-branch revision is
retained in commit `deadb826d5f96025ce0d73622a906e9764e05fba`; it is not current
main. The older blank-file rollback reference is historical, not the target for
this revision.

Before integration, preserve or withdraw the task branch through the applicable
delivery controls. After integration, use a reviewed forward correction or revert
of the documentation changes, restoring only this README from the recorded blob
where appropriate. Preserve the generated receipt as historical provenance;
corrections to its assertions must remain traceable. Do not reset current main,
rewrite history, remove child contracts, clear registry holds, or revert unrelated
work. Any later contract migration requires its own rollback and consumer-impact
evidence.

## Definition of done

**For this README revision:** the adopted container placement is distinguished
from unresolved seam mappings; all five tracked files are indexed; verified
companions are linked; original heading anchors and document identity remain;
child statuses and non-publisher effects are preserved; and rollback targets the
immediately preceding nonblank file. The delivery record must establish the
actual README-and-receipt diff, bounded checks, and exact remote readback. The
direct-child map, linked deeper inventory, and receipt artifact hash must agree
with the delivered bytes.

**Still open beyond this README:** accountable stewardship and independent
review; registered directory-to-seam mappings; KnowledgeCharacter enum/schema/
registry and consumer closure; native exact-head validation; and any live-source,
policy, evidence, rights/sensitivity, release, correction, or public-runtime
qualification. None is completed merely by checking documentation.

## Status summary

`contracts/cross_domain/` is an adopted semantic placement boundary with four
existing draft/proposed contract documents and three code-bearing fixture-profile
companions. It is neither an empty placeholder nor a production join service.
Candidate assessment, admissible evidence, policy permission, review approval,
and public release remain separate gates.

[Back to top](#top)
