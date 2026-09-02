<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/sensitive-overlay-gatehouse-preflight
title: Sensitive Overlay Gatehouse Preflight Contract
type: semantic-contract; deterministic preflight profile; fixture-only
version: v0.1.0
status: proposed; inactive; fixture-only; restricted; non-authoritative
owners: OWNER_TBD — Governance steward · Consent steward · Privacy steward · Security steward · People/DNA/Land steward · Policy steward · Release steward
created: 2026-08-09
updated: 2026-08-09
policy_label: restricted; governance; consent; ga4gh-passport; duo; tile-only-egress; fail-closed
related:
  - ./README.md
  - ../domains/people-dna-land/consented_genealogy_overlay.md
  - ../../schemas/contracts/v1/governance/sensitive_overlay_gatehouse_preflight.schema.json
  - ../../fixtures/contracts/v1/governance/sensitive_overlay_gatehouse_preflight/cases.json
  - ../../tools/validators/governance/validate_sensitive_overlay_gatehouse_preflight.py
  - ../../tests/validators/governance/test_sensitive_overlay_gatehouse_preflight.py
  - ../../docs/intake/exploratory/pass-32-sensitive-overlay-gatehouse-source-map.md
tags: [kfm, governance, sensitive-overlay, gatehouse, consent, ga4gh, passport, visa, duo, tre, egress, fixture-only]
notes:
  - "Implements the bounded no-network preflight portion of Pass 32 card KFM-P32-PROG-0018."
  - "Consumes synthetic verification summaries only; raw credentials, JWTs, Passports, Visas, genomic data, and row-level data are denied."
  - "A clean result is HOLD, never ALLOW, because cryptographic verification, trust configuration, DUO policy evaluation, signed receipts, TRE execution, and release remain unwired."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Sensitive Overlay Gatehouse Preflight

> A closed, fixture-only fail-closed preflight over synthetic consent,
> GA4GH Passport/Visa verification summaries, declared DUO-match evidence, and
> tile-only egress posture.

## Status and authority boundary

| Field | Value |
|---|---|
| Source card | `KFM-P32-PROG-0018` |
| Contract state | `PROPOSED` / inactive / fixture-only / no-network |
| Object | `SensitiveOverlayGatehousePreflight` |
| Machine profile | `schemas/contracts/v1/governance/sensitive_overlay_gatehouse_preflight.schema.json` |
| Positive validator outcome | `HOLD` |
| Uncertain, failed, expired, revoked, mismatched, unsafe, or overreaching outcome | `DENY` |
| Raw token parsing or cryptographic verification | Not performed |
| Policy, job execution, artifact emission, signed receipt, release, publication | Not performed |

Pass 32 proposes a gatehouse that validates consent and identity tokens,
returns `DENY` on uncertainty, confines sensitive work to an enclave/TRE,
allows only tile egress, and emits signed receipts. This change implements only
the smallest dependency-closed deterministic preflight over synthetic upstream
verification summaries. It does not implement a credential parser,
Passport Clearinghouse, policy engine, enclave, job runner, signer, or release
path.

## Why this is a preflight over summaries

The repository's common `IdentityToken` contract explicitly is not an
authentication or consent credential. The People/DNA/Land consent-overlay
profile is synthetic, revocation-aware, restricted, non-identifying, and
not-released. This contract preserves those boundaries instead of placing raw
security credentials or genomic material in a repository-facing fixture lane.

The input contains hashes, finite verification states, synthetic `.invalid`
identifier URLs, time bounds, and governed references. It must not contain:

- JWT, JWS, Passport, Visa, access-token, refresh-token, or ID-token strings;
- secrets, keys, authorization headers, cookies, or session identifiers;
- names, emails, subject identifiers, kit/vendor identifiers, or direct
  identifiers;
- VCF, FASTA, sequence, genotype, DNA segment, row-level, or reconstruction-
  capable payloads; or
- live issuer, source, key, revocation, ontology, or dataset endpoints.

## Standards-alignment boundary

The frozen fixture profile names GA4GH Passport `1.2.1` to make its evidence
basis explicit. The profile reflects these current specification pressures:

- Passports and Visas used for access require validation before reliance;
- a clearinghouse needs trust relationships for the Broker, Visa Issuer, and
  Visa Assertion Source;
- expiry, audience, Visa identity linkage, conditions, and revocation posture
  cannot remain unknown;
- controlled access requires a matching `ControlledAccessGrants` or separately
  governed custom controlled-access Visa; and
- Visa URL claims are opaque case-sensitive identifiers during policy
  evaluation and must not be fetched.

This repository validator does not perform those standards operations. It
checks only that an upstream synthetic summary declares them `VERIFIED` and
remains internally coherent. A later implementation must use vetted security
libraries and governed trust configuration; this fixture profile is not GA4GH
conformance certification.

DUO terms are declaration-only identifiers in this slice. The validator does
not download an ontology, infer term hierarchies, or decide whether a research
purpose is legally or ethically compatible with dataset conditions. It requires
a separately governed evaluator reference, ontology digest, bound evaluation
time, and `VERIFIED` match summary, then retains a policy-evaluation hold.

## Required summary groups

| Group | Required meaning |
|---|---|
| Job | Synthetic job reference, exact synthetic target URL, and requested TTL no greater than 24 hours |
| Consent | Verified active summary, hashed token reference, issue/expiry interval no longer than 24 hours, current revocation check, unrevoked state, consent-receipt reference, restricted scope and audience |
| Identity | GA4GH Passport 1.2.1 summary hash, verified signature/audience/Broker trust, sufficient expiry, verified Visa-identity linkage, and at least one matching controlled-access grant |
| Used Visas | Verified signature, issuer trust, source trust, current revocation, satisfied conditions, sufficient expiry, and opaque synthetic identifier URLs |
| Data use | DUO identifier declarations plus verified external match summary, evaluator reference, evaluation time, and ontology digest |
| Egress | Synthetic TRE declaration, map-tiles-only artifact class, PMTiles or MVT media type, no raw genomic, row-level, direct-identifier, outbound-network, public, or released posture |
| Governance | Every side effect fixed false; execution mode fixed `FIXTURE_ONLY` |

## Deterministic decision table

| Condition | Outcome | Meaning |
|---|---|---|
| Schema, deterministic identity, and every summary check are coherent | `HOLD` | Candidate may proceed only to separately governed implementation/review work; no job is allowed here |
| Consent absent, uncertain, inactive, expired, revoked, stale, out of scope, or longer than 24 hours | `DENY` | Fail closed |
| Passport/Visa signature, audience, identity link, trust, conditions, revocation, target, or expiry unresolved | `DENY` | Fail closed |
| Controlled-access grant absent or does not name the exact target | `DENY` | Fail closed |
| DUO evaluation unknown or unbound | `DENY` | Fail closed |
| Egress is not map-tile-only, or contains sensitive/row-level/identifying material | `DENY` | Fail closed |
| Outbound network, public exposure, released state, or governance side-effect claim | `DENY` | Fail closed |
| Raw token field, undeclared property, malformed input, hash or identity mismatch | `DENY` | Fail closed |

There is intentionally no `ALLOW`, `PASS`, `APPROVE`, `EXECUTE`, `RELEASE`, or
`PUBLISH` outcome in this profile.

## Retained holds

Even the clean synthetic case retains:

- `RAW_TOKEN_PARSING_UNWIRED`
- `CRYPTOGRAPHIC_TOKEN_VERIFICATION_UNWIRED`
- `ISSUER_AND_SOURCE_TRUST_CONFIGURATION_UNWIRED`
- `DUO_POLICY_EVALUATION_UNWIRED`
- `SIGNED_RECEIPT_EMISSION_UNWIRED`
- `TRE_ATTESTATION_AND_JOB_EXECUTION_UNWIRED`
- `RELEASE_AUTHORIZATION_NOT_EVALUATED`

These are runtime limitations, not optional warnings.

## Deterministic identity

`spec_hash` uses the repository hashing profile over the complete object after
removing `preflight_id` and `spec_hash`. `preflight_id` is
`kfm:sensitive-overlay-gatehouse-preflight:` plus the first 24 hexadecimal
characters of that hash. The identity proves fixture-byte determinism only.

## Directory Rules basis

| Responsibility | Home |
|---|---|
| Cross-family gatehouse meaning | `contracts/governance/` |
| Canonical machine shape for this proposed profile | `schemas/contracts/v1/governance/` |
| Reusable synthetic case matrix | `fixtures/contracts/v1/governance/` |
| Durable deterministic validation | `tools/validators/governance/` |
| Enforceability evidence | `tests/validators/governance/` |
| Hosted read-only orchestration | `.github/workflows/` |
| Source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root or parallel identity, consent, policy, token, key, trust, ontology,
receipt, proof, enclave, release, or publication authority is created.

## Validation

```bash
python -m unittest -v \
  tests.validators.governance.test_sensitive_overlay_gatehouse_preflight

KFM_NO_NETWORK=1 \
python tools/validators/governance/validate_sensitive_overlay_gatehouse_preflight.py \
  --fixtures
```

A green result proves only closed schema shape, deterministic fixture identity,
one clean hold, exact fail-closed denials, bounded parsing, non-echoing output,
and no-network behavior.

## Deferred operational work

A later, separately reviewed implementation would be required for:

- raw credential intake in a non-repository secret boundary;
- vetted OIDC/JWT/JWS and GA4GH Passport/Visa parsing and cryptographic checks;
- trusted Broker, issuer, source, key, rotation, revocation, and audience
  configuration;
- consent legal sufficiency, proof, revocation execution, and cache cleanup;
- pinned DUO distribution, purpose/condition matching, policy authorship, tests,
  and a real policy runtime;
- attested TRE/enclave job execution and no-egress enforcement;
- tile generation with privacy, aggregation, reconstruction, evidence, and
  sensitivity controls;
- signed receipt emission into an accepted receipt authority;
- release, correction, rollback, withdrawal, deployment, observability, and
  incident-response integration; and
- external conformance and penetration testing.

## Rollback

Before merge, close the draft pull request and remove its review branch. After
an authorized merge, revert the additive commit and rerun the dedicated
workflow. No credential, identity, consent record, policy decision, job,
artifact, enclave, receipt, release, deployment, or public surface requires
restoration.

<p align="right"><a href="#top">Back to top</a></p>
