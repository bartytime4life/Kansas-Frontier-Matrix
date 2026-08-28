<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/object-identity-kind-assessment
title: ObjectIdentityKindAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Governance steward · Contract steward · Identity steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; governance; identity; entity; value-object; derived-artifact
responsibility: Define a fixture-only identity-kind declaration for one object family without creating identifiers, changing schemas or registers, or granting evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED attached Pass 18 card, attached DDD reference, visual review, and bounded repository gap; PROPOSED inactive assessment; UNKNOWN family adoption; NEEDS VERIFICATION governance, contract, identity, and validation review plus hosted exact-head CI"
related:
  - ./object_family_domain_reference_profile.md
  - ../../control_plane/object_family_register.yaml
  - ../../schemas/contracts/v1/governance/object_identity_kind_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/object_identity_kind_assessment/cases.json
  - ../../tools/validators/governance/validate_object_identity_kind_assessment.py
  - ../../tests/validators/governance/test_validate_object_identity_kind_assessment.py
  - ../../docs/intake/exploratory/pass-18-object-identity-kind-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# ObjectIdentityKindAssessment Candidate

`ObjectIdentityKindAssessmentCandidate` is an additive, fixture-only
declaration of how identity is intended to work for one object family. It
implements the smallest reviewable portion of supplied Pass 18 card
`KFM-P18-INV-464`: distinguish entities that need lifecycle-continuous
identity from immutable value objects that are equivalent by attributes.

The candidate also admits `DERIVED_ARTIFACT` as a KFM-specific adaptation for
content-addressed outputs whose equivalence follows bytes rather than a durable
real-world or governance identity. This third kind is a proposal derived from
current repository practice, not a claim made by the attached DDD reference.

## Identity kinds

| Kind | Identity basis | Required declaration |
|---|---|---|
| `ENTITY` | `DURABLE_IDENTITY` | Durable identity and lifecycle continuity are required; attribute or byte equality alone does not establish sameness. |
| `VALUE_OBJECT` | `STRUCTURAL_VALUE` | Attributes define equivalence; durable identity and lifecycle continuity are not required. |
| `DERIVED_ARTIFACT` | `CONTENT_ADDRESS` | A content digest defines artifact-version equivalence; durable identity and lifecycle continuity are not required. |
| `UNRESOLVED` | `UNRESOLVED` | No identity behavior is inferred; validation abstains. |

These categories classify the declaration only. They do not manufacture an
identifier, decide whether an existing ID is correct, or rewrite an object
family.

## Register and review posture

The candidate binds a semantic contract by opaque reference and digest. An
optional object-family register binding may be `RESOLVED`, `UNRESOLVED`, or
`NOT_REGISTERED`. Non-resolved register posture yields `ABSTAIN`; it never
silently adds a family to the partial register.

A complete declaration requires a canonical review-record reference set and a
plain-language rationale. The validator checks local coherence only and does
not authenticate those references or substitute for steward review.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Kind, basis, equivalence flags, semantic-contract binding, register posture, review declaration, timestamp, and content hash are locally coherent. |
| `ABSTAIN` | Identity kind, register posture, or review posture remains unresolved. |
| `DENY` | Identity semantics, register binding, review evidence, ordering, timestamp, or content hash is contradictory. |
| `ERROR` | The candidate cannot be safely parsed or evaluated under the closed schema. |

## Boundary

A validator result does not:

- create, assign, rotate, canonicalize, or retire an identifier;
- edit a semantic contract, schema, object-family register, or domain lane;
- infer entity status from the mere presence of an ID;
- migrate stored objects or change equality, persistence, or correction code;
- resolve evidence, decide policy, approve review, or authorize promotion,
  release, deployment, publication, or public use.

The candidate carries no object payload, source row, geometry, credential,
query, policy rule, or public record.

## Directory Rules basis

Cross-family identity classification is governance meaning, so the semantic
contract belongs under `contracts/governance/`. Shape, synthetic replay,
validation, tests, read-only CI, source reconciliation, and authoring provenance
remain under their established responsibility roots. The partial
`control_plane/object_family_register.yaml` remains unchanged and authoritative
only for its declared navigational scope.

## Validation and rollback

```bash
python -m unittest tests.validators.governance.test_validate_object_identity_kind_assessment -v
python tools/validators/governance/validate_object_identity_kind_assessment.py --fixtures
```

Rollback is one additive commit revert. The inactive profile has no register,
schema-migration, persistence, lifecycle, release, deployment, publication, or
public-state side effect.
