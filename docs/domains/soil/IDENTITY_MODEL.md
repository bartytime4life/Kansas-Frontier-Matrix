<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/identity-model
title: Soil Identity Model
type: domain-identity-guide
version: v1.0.0
status: draft; repository-grounded; bounded-candidate-implementation
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Identity steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Documentation steward
created: 2026-08-24
updated: 2026-08-24
policy_label: public
owning_root: docs/
responsibility: Human-readable guidance for implemented Soil candidate identities, hash roles, and authority limits
truth_posture: CONFIRMED bounded local candidate profiles and tests; PROPOSED planning lineage; NEEDS VERIFICATION canonical adoption, source admission, runtime integration, release, and publication
related:
  - docs/domains/soil/README.md
  - docs/domains/soil/ARCHITECTURE.md
  - docs/domains/soil/DATA_LIFECYCLE.md
  - contracts/domains/soil/domain_feature_identity.md
  - contracts/domains/soil/promotion_materiality_profile.md
  - schemas/contracts/v1/domains/soil/domain_feature_identity.schema.json
  - tools/validators/domains/soil/validate_domain_feature_identity.py
  - fixtures/domains/soil/domain_feature_identity/cases.json
  - tests/validators/domains/soil/test_domain_feature_identity.py
  - tools/ingest/ssurgo_watch/ssurgo_watch.py
  - tests/ingest/ssurgo_watch/test_ssurgo_watch.py
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, soil, identity, deterministic-hash, support-type, evidence, fail-closed]
notes:
  - "Repository evidence snapshot: main@362d6590b9516596ad1c34a64781c13bf85d52c8."
  - "Planning lineage: KFM Soil Architecture Extended Pro PDF-Only Planning Report, section 12, printed/PDF page 15, SHA-256 7c2d498212b9ad56f3ba37bf91f841e9f328794e8aa4940f8f665a4116c5aaea."
  - "The planning report had no mounted repository; this guide reports only identity behavior proved by current repository bytes and tests."
  - "A deterministic candidate identifier or passing validator does not create canonical identity, resolve evidence, approve review, release, or publish."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil identity model

Human-readable guide to the Soil lane's implemented identity candidates and
hash roles. The current executable surfaces are bounded, deterministic,
no-network or fixture-first controls. They do not establish a canonical Soil
identity service or a public identity contract.

> [!IMPORTANT]
> **Current determination at
> `main@362d6590b9516596ad1c34a64781c13bf85d52c8`:** the Soil
> `DomainFeatureIdentity` candidate has a closed `PROPOSED_INACTIVE` schema, a
> deterministic validator, five synthetic cases, and five focused tests. The
> valid fixture still sets every authority effect to `false` and denies public
> use. Separate Soil controls implement promotion-materiality hashes and
> fixture-only SSURGO watcher hashes. None of these surfaces activates a source,
> resolves evidence, creates canonical identity, approves review, releases, or
> publishes.

| Question | Current result |
|---|---|
| Is a Soil identity candidate executable? | `CONFIRMED` - one bounded profile is schema-, fixture-, validator-, and test-backed. |
| Is it canonical identity? | No - the schema and validator explicitly deny that effect. |
| Is it active or public? | No - status is `PROPOSED_INACTIVE` and `public_use_allowed` is `false`. |
| Are all Soil object/support families fixture-proved? | No - the positive fixture covers one `SoilMapUnit` survey-feature case. |
| Does a matching hash prove a Soil claim? | No - hashes bind selected bytes or semantics; evidence and lifecycle gates remain separate. |
| Is a repository-wide identity decision settled here? | No - cross-domain adoption and compatibility remain outside this guide. |

## 1. Authority and planning lineage

The placement and current-state claims in this guide follow
[accepted ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md),
the adopted [Directory Rules](../../doctrine/directory-rules.md), and inspected
repository implementation at the pinned SHA.

The proposal source is **KFM Soil Architecture Extended Pro PDF-Only Planning
Report**, section 12, printed/PDF page 15, created 2026-04-21, SHA-256
`7c2d498212b9ad56f3ba37bf91f841e9f328794e8aa4940f8f665a4116c5aaea`.
It recommends separating stable specifications, content, geometry, queries, and
runs rather than treating retrieval time as identity. Because the report had no
mounted repository, those recommendations are discovery input only. The
repository paths, algorithms, fields, and maturity below come from current code
and tests, not from the proposal's confidence or terminology.

## 2. Responsibility-root map

| Responsibility | Current home |
|---|---|
| Human explanation and routing | `docs/domains/soil/IDENTITY_MODEL.md` |
| Semantic meaning | `contracts/domains/soil/domain_feature_identity.md` |
| Machine shape | `schemas/contracts/v1/domains/soil/domain_feature_identity.schema.json` |
| Candidate evaluator | `tools/validators/domains/soil/validate_domain_feature_identity.py` |
| Synthetic cases | `fixtures/domains/soil/domain_feature_identity/cases.json` |
| Focused proof | `tests/validators/domains/soil/test_domain_feature_identity.py` |
| SSURGO watcher implementation | `tools/ingest/ssurgo_watch/` |
| Promotion materiality meaning | `contracts/domains/soil/promotion_materiality_profile.md` |

The guide does not duplicate a schema or contract and adds no identity registry,
service, public API, evidence, receipt, release, or publication home.

## 3. DomainFeatureIdentity candidate

### 3.1 Closed machine shape

The current schema is a closed object (`additionalProperties: false`) with:

- profile `kfm.domains.soil.domain-feature-identity.v1`;
- status `PROPOSED_INACTIVE` and version `1.0.0`;
- an identifier shaped as `soil-identity:<24 lowercase hex characters>`;
- a full SHA-256 `spec_hash`;
- Soil object family, object role, support type, source identity, temporal scope,
  evidence references, match status, and limitations;
- `public_use_allowed: false`; and
- six effects fixed to `false`: canonical identity creation, evidence resolution,
  policy evaluation, review approval, release, and publication.

The enumerated object and support families define the candidate profile's
allowed vocabulary. They do not prove that every combination is implemented or
accepted.

### 3.2 Deterministic candidate algorithm

The validator copies the candidate, removes `id` and `spec_hash`, serializes the
remaining object as sorted compact ASCII JSON, and computes SHA-256. It then
requires:

```text
spec_hash = "sha256:" + full_digest
id        = "soil-identity:" + first_24_hex_characters(full_digest)
```

The algorithm is deterministic for the candidate profile. The function name
`canonical_hash` describes canonical byte construction; it does not confer
canonical repository identity. The candidate's explicit
`canonical_identity_created: false` effect remains controlling.

### 3.3 Finite outcomes and fail-closed checks

| Condition | Outcome |
|---|---|
| Candidate matches the bounded profile and deterministic identity | `PASS` |
| Support type/object role collapses or public/effect authority is overclaimed | `DENY` |
| Profile, source identity, temporal scope, canonical arrays, hash, or ID is invalid | `ERROR` unless a deny-class finding is also present |

The validator also requires non-empty source identity fields, sorted unique
`evidence_refs` and `limitations`, a bounded temporal-scope form, and the
support-type/object-role matrix implemented in the validator.

### 3.4 Current proof boundary

The five synthetic cases prove:

1. one valid `SoilMapUnit` / `SURVEY_FEATURE` /
   `authoritative_static_soil` candidate;
2. denial of support-role collapse;
3. denial of public-use overclaim;
4. denial of authority-effect overclaim; and
5. error on a mismatched specification hash.

The five focused tests additionally verify schema closure and inactivity,
fixture/result parity, deterministic digest and ID construction, support-role
separation, and denial of release/public authority. This is strong proof of the
bounded candidate behavior, not coverage of every object family, source family,
support type, correction path, or runtime consumer.

## 4. Other implemented Soil hash roles

Hash names are local contract terms. They must not be collapsed merely because
they all use SHA-256.

### 4.1 Promotion-materiality dimensions

The inactive Soil promotion-materiality profile compares five substantive
identities:

- `content_spec_hash`
- `source_descriptor_hash`
- `schema_hash`
- `validator_hash`
- `policy_hash`

`retrieved_at` is retained for audit but excluded from semantic materiality. An
unchanged or retrieval-time-only change is a `NON_EVENT`; a substantive change
with complete evidence is a `PROMOTION_CANDIDATE`; missing baseline/evidence is
`HOLD`; evaluation failure is `ERROR`. A promotion candidate is not approval or
promotion.

### 4.2 Fixture-only SSURGO watcher hashes

The SSURGO watcher currently distinguishes:

| Hash | Current input role |
|---|---|
| `spec_hash` | Binds the watcher profile, fixture-only posture, source descriptor reference, extraction/geometry profiles, and materiality profile. |
| `content_hash` | Binds the candidate content except the `content_hash` field itself. |
| geometry-set hash | Binds geometry profile, analysis geometry/area, and per-map-unit geometry hashes. |
| spatial-diff `content_hash` | Binds the spatial-difference artifact except its own content hash. |

A focused test changes `observed_at` and proves that the watcher `spec_hash`
stays stable while `content_hash` changes. The watcher remains fixture-only and
no-network; its hashes do not prove a live source, canonical Soil geometry, or
publication.

## 5. Identity, evidence, and lifecycle

```text
source identity + role + rights
  -> RAW
  -> WORK / QUARANTINE
  -> validated identity candidate + evidence references
  -> PROCESSED
  -> CATALOG / TRIPLET with EvidenceBundle support
  -> policy + accountable review
  -> governed release and publication controls
  -> PUBLISHED
```

A candidate identifier supports joins and audit. It does not replace the owning
Soil object, source descriptor, `EvidenceBundle`, `EvidenceRef`, policy decision,
review record, release manifest, correction record, revocation, or rollback
target. Evidence-dependent claims cite resolved evidence or abstain. Public
clients use governed interfaces, never the candidate or internal store directly.

## 6. Sensitivity and publication boundary

Identity can become sensitive when combined with precise locations, private-land
or parcel-adjacent detail, infrastructure, living-person data, culturally
controlled material, archaeology, rare species, or operational sensors. Stable
identifiers and hashes do not neutralize those risks.

Required outcomes remain minimization, generalization, redaction, staged access,
quarantine, delayed access, or denial until rights, consent, sovereignty,
sensitivity, evidence, policy, review, release, and rollback requirements close.
No candidate or hash authorizes public use by itself.

## 7. Current limitations and next gates

- The positive DomainFeatureIdentity fixture covers only one object/support
  combination; broader enumerations are shape allowance, not fixture proof.
- Cross-domain identity inheritance, canonical source-native key families, and
  compatibility/migration behavior remain unresolved.
- The candidate profile does not prove source admission, runtime API/UI use,
  evidence resolution, policy execution, review approval, release, publication,
  correction propagation, or rollback invalidation.
- Other proposed hash roles from planning material are not treated as implemented
  without a cited repository contract, executable path, and test.
- Any activation or public projection requires an accepted decision and
  dependency-closed implementation outside this documentation slice.

## 8. Validation commands

```bash
python tools/validators/domains/soil/validate_domain_feature_identity.py --fixtures
python -m unittest tests.validators.domains.soil.test_domain_feature_identity
python -m unittest tests.ingest.ssurgo_watch.test_ssurgo_watch
```

These commands prove local fixture behavior only. They do not contact a source
or establish lifecycle, release, or publication authority.

## 9. Related repository surfaces

- [Soil domain index](README.md)
- [Soil architecture](ARCHITECTURE.md)
- [Soil lifecycle guide](DATA_LIFECYCLE.md)
- [DomainFeatureIdentity semantic contract](../../../contracts/domains/soil/domain_feature_identity.md)
- [Promotion materiality profile](../../../contracts/domains/soil/promotion_materiality_profile.md)
- [DomainFeatureIdentity schema](../../../schemas/contracts/v1/domains/soil/domain_feature_identity.schema.json)
- [Candidate validator](../../../tools/validators/domains/soil/validate_domain_feature_identity.py)
- [Synthetic cases](../../../fixtures/domains/soil/domain_feature_identity/cases.json)
- [Focused candidate tests](../../../tests/validators/domains/soil/test_domain_feature_identity.py)
- [SSURGO watcher](../../../tools/ingest/ssurgo_watch/ssurgo_watch.py)
- [SSURGO watcher tests](../../../tests/ingest/ssurgo_watch/test_ssurgo_watch.py)

## 10. Maintenance rule

Update this guide from exact repository evidence. Pin behavior claims to the
schema, validator, fixtures, tests, and tested SHA. If an accepted decision
changes canonical identity, public compatibility, or lifecycle authority, record
the decision, migration, validation, correction, revocation, and rollback
boundaries rather than silently upgrading this candidate's status.
