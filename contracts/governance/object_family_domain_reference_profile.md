<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/object-family-domain-reference-profile
title: Object Family Domain Reference Profile Candidate
type: semantic-contract
version: v0.1.0
status: proposed; inactive; review-pending; non-authoritative
owners: OWNER_TBD — Governance steward · Contracts steward · Domain stewards · Sensitivity steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; governance; object-family; domain-reference; fixture-only
owning_root: contracts/
responsibility: Define the semantic meaning and fail-closed validation boundary of a fixture-only object-family/domain reference candidate.
truth_posture: PROPOSED source-grounded adaptation / CONFIRMED deterministic fixture validation / no ownership, sensitivity-policy, register-write, release, or publication authority
related:
  - ../../docs/registers/OBJECT_FAMILY.md
  - ../../control_plane/domain_lane_register.yaml
  - ../../control_plane/object_family_register.yaml
  - ../../schemas/contracts/v1/governance/object_family_domain_reference_profile.schema.json
  - ../../fixtures/contracts/v1/governance/object_family_domain_reference_profile/cases.json
  - ../../tools/validators/governance/validate_object_family_domain_reference_profile.py
  - ../../tests/validators/governance/test_object_family_domain_reference_profile.py
  - ../../docs/intake/exploratory/object-family-domain-reference-profile-source-map.md
tags: [kfm, governance, object-family, domain, ownership, citation, sensitivity, fixture-only]
notes:
  - "Implements a bounded contract-first slice of the Full Atlas Object Family x Domain Reference Matrix proposal."
  - "The profile records source-reported ownership and proposed sensitivity defaults; it does not assign authority or write the existing object-family register."
[/KFM_META_BLOCK_V2] -->

# Object Family Domain Reference Profile Candidate

> A deterministic, fixture-only profile for keeping object-family ownership,
> cross-domain citation, and proposed sensitivity defaults distinct and
> inspectable.

## Status and purpose

| Field | Value |
|---|---|
| Profile | `kfm.object-family-domain-reference-candidate.v1` |
| State | `PROPOSED` / inactive / review-pending |
| Source proposal | Full Atlas "Object Family x Domain Reference Matrix" and Atlas v1.1 section 24.14 |
| Positive result | `PASS` with `profile_state: REVIEW_REQUIRED` |
| Runtime, policy, release, or publication effect | None |

The source proposal calls for one matrix that names the owner of each
cross-cutting object family, the domains that cite it, and its sensitivity
default. KFM already has a human-facing `OBJECT_FAMILY.md` register and a
partial machine-readable object-family register. This profile does not replace,
extend, or write either register. It supplies a closed candidate shape and
validator that a separately reviewed register extension can later reuse.

## Preserved axes

Each candidate row keeps these concerns separate:

- one source-reported authority owner: a registered domain lane or a named
  cross-cutting steward role;
- zero or more registered domain lanes that may cite but not mutate the family;
- one semantic contract reference that remains the meaning authority;
- a source-reported ownership basis that is not silently upgraded to an
  accepted repository decision;
- a sensitivity default explicitly labeled `PROPOSED_SOURCE_DEFAULT`, not a
  policy decision for any instance; and
- fixed-false authority and side-effect fields.

## Deterministic validation

The validator requires canonical lexical ordering, unique family IDs, known
domain-lane references, existing semantic-contract paths, internally consistent
summary counts, and JCS plus SHA-256 identity. It rejects:

- multiple or unknown owners;
- an owner appearing in its own citing-domain set;
- unknown or duplicate citing domains;
- unsorted rows or citing-domain arrays;
- missing or non-contract references;
- RAW, WORK, QUARANTINE, direct-store, URL, or query material;
- sensitivity, policy, release, publication, registry-write, or owner-change
  authority claims; and
- stale summary, digest, or identifier fields.

## Finite outcomes

| Outcome | Meaning | Non-effect |
|---|---|---|
| `PASS` | The synthetic candidate is internally consistent. | Still `REVIEW_REQUIRED`; no owner or tier is adopted. |
| `DENY` | Shape, identity, reference, ordering, or authority invariants fail. | No register mutation or fallback inference. |
| `ERROR` | The input cannot be boundedly read or parsed. | No partial result is trusted. |

## Directory Rules basis

| Responsibility | Home |
|---|---|
| Candidate semantic meaning | `contracts/governance/` |
| Machine shape | `schemas/contracts/v1/governance/` |
| Synthetic cases | `fixtures/contracts/v1/governance/` |
| Deterministic validation | `tools/validators/governance/` |
| Executable conformance evidence | `tests/validators/governance/` |
| Hosted read-only orchestration | `.github/workflows/` |
| Source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root, domain lane, object-family authority, sensitivity authority, or
parallel register is created.

## Non-effects

A green result does not:

- add, rename, retire, or reassign an object family;
- establish that a source assertion is correct or current;
- amend the Domain Lane Register or Object Family Register;
- adopt the T0-T4 scheme or set instance-level sensitivity;
- authorize a cross-domain join or mutation;
- resolve evidence, evaluate policy, approve review, release data, deploy code,
  publish a surface, or authorize public use.

## Rollback

Before merge, close the draft pull request and remove its branch. After an
authorized merge, revert the additive packet and rerun its dedicated workflow.
No registry, domain, object-family, policy, data, release, deployment, or public
state requires restoration.
