<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-cross-domain-readme
title: contracts/cross_domain/ — Cross-Domain Semantic Contract Boundary
type: readme; directory-readme; cross-domain-contract-index; semantic-boundary
version: v0.2.0
status: draft; repository-grounded; existing-cross-domain-namespace; mixed-maturity; non-authoritative; non-publisher
owner: NEEDS VERIFICATION — CODEOWNERS routes /contracts/ to @bartytime4life; accountable cross-domain, contract, domain, policy, sensitivity, validation, and release stewards are not established here
created: 2026-06-20
updated: 2026-09-08
current_path: contracts/cross_domain/README.md
owning_root: contracts/
responsibility: index and bound semantic meaning that genuinely spans independently governed domains without absorbing endpoint authority or becoming schema, policy, evidence, lifecycle, release, or publication authority
truth_posture: cite-or-abstain; repository presence, fixture validation, a passing check, merge, or an ALLOW candidate never establishes relationship truth, public-use permission, release, or publication
evidence_snapshot: bartytime4life/Kansas-Frontier-Matrix@5c563bd07e12689eece7b5cf105b1e2f0545f03a
prior_blob: 58c2f1bfaa4f9b49676c339b2977a1c46ffcf88a
directory_governance: ADR-0029 accepted Directory Rules v2; same-path documentation update only
related:
  - ../README.md
  - ./knowledge_character.md
  - ./fauna_habitat/public_safe_assignment_profile.md
  - ./soil_agriculture/public_safe_context_profile.md
  - ./soil_hydrology/public_safe_context_profile.md
  - ../joins/cross_lane_join_assessment.md
  - ../../control_plane/cross_domain_seam_register.yaml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/architecture/cross-domain/README.md
  - ../../schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json
  - ../../fixtures/contracts/v1/joins/
  - ../../tools/validators/cross_domain/
  - ../../tests/cross_domain/README.md
notes:
  - "v0.2.0 replaces the stale README-only inventory with the verified direct-child tree and four current semantic artifacts."
  - "The three pair profiles are proposed, fixture-first, no-network candidate profiles backed by existing validators, fixtures, and tests; none authorizes a public join."
  - "The proposed seam register is partial and navigational only. All five projected seams are HOLD_UNRESOLVED, public_join_allowed is false, and seam_contract_path is null."
  - "Current underscore child names are existing repository identities, not accepted canonical seam IDs; no rename or compatibility migration occurs here."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `contracts/cross_domain/` — Cross-Domain Semantic Contract Boundary

This directory owns human-readable semantic meaning for relationships or
cross-cutting concepts that genuinely span independently governed KFM domains.
It preserves the authority of every participating domain; it is not a domain,
Shared Kernel, schema home, policy engine, evidence store, release lane, or
publication surface.

The safe interpretation is:

```text
DOCUMENTED != IMPLEMENTED
ALLOW != ANSWER
SCHEMA_VALID != AUTHORIZED
MERGED != RELEASED
```

## Status and evidence boundary

| Surface | Verified state at the evidence snapshot | Safe interpretation |
|---|---|---|
| Directory contents | This README, `knowledge_character.md`, and three pair-profile directories | The prior README-only inventory is superseded. |
| Placement authority | [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) accepts [Directory Rules v2](../../docs/doctrine/directory-rules.md) | Same-path `PLACE`; no new root, move, rename, or authority change. |
| Pair profiles | Fauna–Habitat, Soil–Agriculture, and Soil–Hydrology have proposed fixture-first semantic profiles plus validators, fixtures, and tests | Bounded candidate conformance exists; public relationship authority does not. |
| Cross-cutting contract | `knowledge_character.md` is a draft semantic anti-collapse pattern | No accepted global enum, paired cross-domain schema, or cross-domain validator is established by this file. |
| Seam projection | `cross_domain_seam_register.yaml` is `PROPOSED`, partial, and navigation/review only | Every projected seam remains held; registration is not activation. |
| Review route | CODEOWNERS routes `/contracts/` to `@bartytime4life` | Routing is not accountable multi-steward approval or release authority. |

Repository bytes and exact-head evidence control implementation claims. Google
Drive research and Notion coordination may inform review, but neither can place
repository files, accept a seam, activate a source, approve policy, or publish a
relationship.

## Purpose and scope

Use this lane when the semantic responsibility itself spans two or more bounded
contexts and choosing one arbitrary lead domain would misstate ownership.

A contract belongs here only when it:

- names every participating domain and preserves the owner of each atomic fact;
- defines the meaning, invariants, exclusions, and finite outcomes of the
  cross-domain concept or relation;
- retains source role, EvidenceRef, temporal basis, geography or precision,
  sensitivity, rights, and limitations needed by later gates;
- fails closed when identity, evidence, compatibility, sensitivity, policy, or
  review is unresolved;
- creates no lifecycle, review, release, promotion, publication, or public-use
  effect merely by existing or validating.

A file does not belong here merely because multiple domains consume it. A
single-owner artifact remains with that owner and references its dependencies.

## Placement and authority

Accepted Directory Rules keep responsibility roots distinct:

| Responsibility | Owning surface |
|---|---|
| Human-readable semantic meaning | `contracts/` |
| Machine-checkable shape | `schemas/` |
| Allowed, denied, held, restricted, or abstained conditions | `policy/` |
| Reusable synthetic inputs | `fixtures/` |
| Executable conformance | `tests/` |
| Shared repository validation | `tools/validators/` |
| Machine navigation and review projections | `control_plane/` |
| Lifecycle, evidence, receipt, proof, and released carriers | Applicable `data/` and `release/` families |

Directory Rules section 12.5 illustrates a cross-domain semantic contract at
`contracts/cross_domain/<seam_id>/`, with corresponding tests and validators in
their own responsibility roots. Never select an arbitrary lead domain merely to
obtain a path.

The current child names use established underscore identities. The proposed
seam register uses different registered-style IDs and does not map any entry to
a contract path. Do not silently rename, alias, or duplicate a child. Any
identity change requires accepted authority, a consumer map, compatibility and
migration analysis, negative checks, and rollback.

## Current direct-child map

Verified at `main@5c563bd07e12689eece7b5cf105b1e2f0545f03a`:

```text
contracts/cross_domain/
├── README.md               # boundary and inventory — this file
├── fauna_habitat/          # proposed assignment-candidate semantics
├── knowledge_character.md  # draft cross-domain anti-collapse semantics
├── soil_agriculture/       # proposed context-candidate semantics
└── soil_hydrology/         # proposed context-candidate semantics
```

This is a current direct-child map, not an illustrative future tree. Child
artifacts retain their own version, status, evidence limits, and rollback.

## Current semantic inventory

| Semantic artifact | Current posture | Verified backing | Authority limit |
|---|---|---|---|
| [`knowledge_character.md`](./knowledge_character.md) | Draft cross-domain anti-collapse pattern; exact version and evidence limits belong to the child contract | Atmosphere-specific contract, schema, registry, and tests are adjacent evidence | Does not establish an accepted global vocabulary, paired cross-domain schema, cross-domain validator, or domain-independent authority. |
| [Fauna–Habitat assignment profile](./fauna_habitat/public_safe_assignment_profile.md) | `v0.2.0`; proposed; repository-grounded; fixture-first; no-network; non-authoritative | [Pair validator](../../tools/validators/cross_domain/fauna_habitat/validate_public_safe_assignment.py), [fixtures](../../fixtures/contracts/v1/joins/fauna_habitat_public_safe_assignment/cases.json), [tests](../../tests/cross_domain/fauna_habitat/test_public_safe_assignment.py), and shared join schema | `ALLOW` is a non-publishing candidate report, not an accepted fauna occurrence, habitat assignment, or public claim. |
| [Soil–Agriculture context profile](./soil_agriculture/public_safe_context_profile.md) | `v0.2.0`; proposed; fixture-first; no-network; non-authoritative | [Pair validator](../../tools/validators/cross_domain/soil_agriculture/validate_public_safe_context.py), [fixtures](../../fixtures/contracts/v1/joins/soil_agriculture_public_safe_context/cases.json), [tests](../../tests/cross_domain/soil_agriculture/test_public_safe_context.py), and shared join schema | Does not establish crop suitability, yield causation, farm or operator identity, public-join permission, or a canonical seam. |
| [Soil–Hydrology context profile](./soil_hydrology/public_safe_context_profile.md) | `v0.2.0`; proposed; fixture-first; no-network; non-authoritative | [Pair validator](../../tools/validators/cross_domain/soil_hydrology/validate_public_safe_context.py), [fixtures](../../fixtures/contracts/v1/joins/soil_hydrology_public_safe_context/cases.json), [tests](../../tests/cross_domain/soil_hydrology/test_public_safe_context.py), and shared join schema | Does not establish hydrologic causation, operational advice, public-join permission, or a canonical seam. |

The three pair profiles reuse the generic
[`CrossLaneJoinAssessment`](../joins/cross_lane_join_assessment.md) and its
[closed schema](../../schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json).
They do not create three replacement schemas or a second join authority.

## Seam-register reconciliation

The current [seam register](../../control_plane/cross_domain_seam_register.yaml)
is a proposed, partial navigation and review projection. Its five entries are:

| Projected seam ID | Status | Public join | Contract path |
|---|---|---:|---|
| `agriculture--soil--suitability-context` | `HOLD_UNRESOLVED` | `false` | `null` |
| `archaeology--roads-rail-trade--historic-corridor-context` | `HOLD_UNRESOLVED` | `false` | `null` |
| `atmosphere--hazards--condition-advisory-context` | `HOLD_UNRESOLVED` | `false` | `null` |
| `fauna--hydrology--aquatic-occurrence-context` | `HOLD_UNRESOLVED` | `false` | `null` |
| `hazards--settlements-infrastructure--exposure-context` | `HOLD_UNRESOLVED` | `false` | `null` |

The Soil–Agriculture profile is related to, but does not resolve or adopt, the
first projected seam. Fauna–Habitat and Soil–Hydrology are not represented by
the five current entries. `knowledge_character` is a cross-cutting semantic
pattern rather than a registered seam entry. These mismatches remain visible
holds; this README does not repair them by assertion.

## Inputs, outputs, and consumers

| Direction | Permitted boundary |
|---|---|
| Inputs | Versioned domain-owned contracts, stable object references, source-role and sensitivity declarations, EvidenceRefs, accepted doctrine and ADRs, and repository-grounded implementation evidence. |
| Outputs | Versioned semantic definitions, finite candidate meanings, explicit exclusions, compatibility notes, and links to separately owned enforcement. |
| Writers | Repository contributors through review; CODEOWNERS provides routing only. Authority-changing decisions require the accountable owners and accepted decision path. |
| Machine consumers | Schemas, policy, validators, tests, pipelines, and governed services may implement or check these semantics without moving their authority here. |
| Public consumers | Ordinary clients must use governed interfaces and released carriers. Raw contracts, fixtures, validator output, PRs, and merges are not public evidence or release records. |

No contract in this directory may activate or retrieve a source, ingest or emit
geometry or data, resolve EvidenceRefs, create an EvidenceBundle, write lifecycle
state, decide policy, assign review, create a release, or publish a result.

## Exposure, sensitivity, mutation, and retention

- This is public repository documentation; precise sensitive, private,
  controlled, licensed, or living-person payloads are prohibited here.
- A derived or generalized relation inherits the most restrictive applicable
  source, sensitivity, rights, and release posture until an owning policy and
  accountable review establish otherwise.
- Files are durable, versioned source artifacts changed through reviewed commits.
  They are not generated runtime state and have no direct production writer.
- A semantic edit must identify affected schemas, policy, fixtures, validators,
  tests, consumers, compatibility, correction, and rollback. Documentation-only
  edits must not claim those dependent artifacts changed.

## Validation and negative checks

For this directory README, review must verify:

1. one H1, unique headings, closed fences, normalized whitespace, and a final
   newline;
2. every relative link and every direct-child inventory entry at the pinned
   commit;
3. consistency with accepted Directory Rules, ADR-0029, the current seam
   register, the generic join contract and schema, and each child contract;
4. that no prose promotes a proposed seam, fixture result, schema-valid object,
   PR, merge, or passing check into truth, authorization, release, or
   publication;
5. exact-head diff, hosted checks, review state, and open-PR overlap before
   relying on the update.

For a semantic or executable change, also run the affected pair validator,
fixture matrix, focused tests, generic join regressions, and applicable hosted
workflow. A skipped, uncollected, stale-head, or unrelated check is not passing
evidence. The [cross-domain test index](../../tests/cross_domain/README.md)
records current test coverage and its limits.

Required negative checks include arbitrary-lead-domain placement, endpoint
ownership collapse, source-role coercion, sensitivity downgrade, missing
evidence, unsafe precision, living-person or private-entity exposure, implied
causation, non-false publication effects, unregistered identity, and absent
dependency behavior.

## Review, escalation, and open holds

Escalate when a change alters a domain owner, seam identity, canonical path,
Shared Kernel relationship, machine vocabulary, public exposure, lifecycle or
release responsibility, or compatibility promise. A README cannot accept those
decisions.

Open holds include:

- accountable contract, domain, policy, sensitivity, validation, and release
  stewardship;
- accepted seam-registration and activation authority, coverage, and mapping to
  current underscore paths;
- accepted source-role crosswalks and global `knowledge_character` vocabulary;
- per-seam policy, evidence closure, rights, authenticated review, release,
  correction, withdrawal, and rollback;
- verified public-client consumer closure through governed interfaces only;
- a governed end-to-end cross-domain `ANSWER` with no trust-membrane bypass.

Until those are closed, every proposed public join remains held.

## Related references

- [Parent contract root](../README.md)
- [Cross-domain architecture index](../../docs/architecture/cross-domain/README.md)
- [Cross-domain seam register](../../control_plane/cross_domain_seam_register.yaml)
- [Generic join contract](../joins/cross_lane_join_assessment.md)
- [Generic join schema](../../schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json)
- [Cross-domain validators](../../tools/validators/cross_domain/)
- [Join fixtures](../../fixtures/contracts/v1/joins/)
- [Cross-domain test index](../../tests/cross_domain/README.md)
- [Directory Rules](../../docs/doctrine/directory-rules.md)
- [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)

## Rollback and review trigger

Rollback is a focused revert of this README to prior blob
`58c2f1bfaa4f9b49676c339b2977a1c46ffcf88a`. It changes no child contract,
schema, policy, fixture, validator, test, pipeline, lifecycle object, evidence,
release record, or public surface.

Re-review this index when a direct child changes, a seam is registered or
activated, an ADR changes placement or authority, an enforcement or consumer
binding changes, a public exposure path is proposed, or correction, withdrawal,
rollback, or material drift is observed.

[Back to top](#top)
