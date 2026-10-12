# SensitiveLocationParityAssessmentCandidate

Status: **PROPOSED / INACTIVE / FIXTURE-ONLY**
Profile: `kfm.governance.sensitive-location-parity-assessment.v1`

## Purpose

This additive assessment carrier records whether a synthetic public request for
a protected location family has the required cross-domain posture:

- exact precision is declared `EXACT_DENIED`; or
- generalized precision is declared
  `GENERALIZED_WITH_RECEIPT_CANDIDATE` and references a separate transform
  receipt and method profile.

The v1 matrix covers ecological nests, dens, and roosts, archaeological sites,
and critical infrastructure. It stores no coordinates, geometry, source
payload, address, or actual sensitive-location value.

A valid assessment proves declaration consistency only. It does not evaluate a
policy, authenticate a sensitivity label, resolve evidence, execute a spatial
transform, complete steward review, grant access, create a public artifact, or
authorize lifecycle, promotion, release, or publication state.

## Responsibility boundary

This is a governance assessment rather than a new cross-domain truth object or
policy bundle. Atomic facts remain owned by their domain contracts:

| Protected subject family | Declared atomic-fact owner in v1 |
|---|---|
| `ECOLOGICAL_NEST` | `fauna` |
| `ECOLOGICAL_DEN` | `fauna` |
| `ECOLOGICAL_ROOST` | `fauna` |
| `ARCHAEOLOGICAL_SITE` | `archaeology` |
| `CRITICAL_INFRASTRUCTURE` | `settlements-infrastructure` |

The assessment references domain, registry, policy, source-snapshot, and
evidence candidates but neither resolves nor replaces them. The most
restrictive applicable sensitivity posture remains upstream of this object.

## Precision and disposition rules

### Exact public request

An `EXACT` request is consistent only when:

- the disposition is `EXACT_DENIED`;
- `EXACT_LOCATION_PUBLIC_DENY` is present in the reason codes;
- the transform receipt and method references are `null`;
- the target precision is `NONE`;
- no generalized output candidate is declared; and
- exception review remains required.

### Generalized public request

A `GENERALIZED` request is consistent only when:

- the disposition is `GENERALIZED_WITH_RECEIPT_CANDIDATE`;
- `GENERALIZED_OUTPUT_REQUIRES_RECEIPT` is present in the reason codes;
- separate transform receipt and method-profile references are present;
- target precision is `GENERALIZED`;
- a generalized output candidate is declared; and
- the assessment still records that no transform was executed and no public
  output was created.

`GENERALIZED_WITH_RECEIPT_CANDIDATE` is not a policy `ALLOW`, access grant, or
release decision. It means only that a synthetic declaration carries the
minimum references needed for later independent review.

## Deterministic identity

The validator removes `assessment_id` and `spec_hash`, canonicalizes the
remaining object with the repository hashing package, computes SHA-256, and
sets:

```text
spec_hash     = sha256:<64 lowercase hexadecimal characters>
assessment_id = sensitive-location-parity-assessment:<first 24 hex>
```

Array order is semantic and must already be sorted and unique. Identity proves
only stable fixture bytes and declarations.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Closed schema shape, deterministic identity, owner mapping, precision/disposition polarity, receipt-reference posture, and fixed-false effects are internally consistent. |
| `DENY` | A bounded schema or semantic contradiction exists. |
| `ERROR` | The input could not be read safely or deterministic identity does not match. |

The validator emits finding codes and JSON pointers only. It does not echo
subject references, timestamps, or any source value.

## Activation posture

The proposal has no accepted sensitivity registry binding, policy engine,
domain-policy adapter, evidence resolver, transform executor, access-control
system, catalog writer, API, UI, release path, or publication path. Any future
activation requires separately accepted owners, policies, registry identities,
domain adapters, review and access controls, correction and rollback paths, and
human approval.

## Directory Rules basis

Governance assessment meaning belongs under `contracts/governance/`; machine
shape under `schemas/contracts/v1/governance/`; reusable public-safe synthetic
cases under `fixtures/contracts/v1/governance/`; deterministic validation under
`tools/validators/`; enforcement proof under `tests/validators/`; hosted
read-only orchestration under `.github/workflows/`; source adaptation reasoning
under `docs/intake/exploratory/`; and generated authoring accountability under
`data/receipts/generated/`.

No new root, policy bundle, domain lane, cross-domain seam authority, catalog
record, release object, or public carrier is created.

## Rollback

Revert the additive contract packet. No source, evidence, registry, policy,
transform, access grant, lifecycle object, release, deployment, or public
artifact requires cleanup.
