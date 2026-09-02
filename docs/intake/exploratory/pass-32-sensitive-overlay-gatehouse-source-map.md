<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-sensitive-overlay-gatehouse-source-map
title: Pass 32 Sensitive Overlay Gatehouse Source Map
type: exploratory-source-map
version: v0.1
status: draft; triaged; bounded-slice-implemented-in-pr
owners: OWNER_TBD — Intake steward · Governance steward · Consent steward · Privacy steward · Security steward · People/DNA/Land steward
created: 2026-08-09
updated: 2026-08-09
policy_label: restricted; exploratory; source-adaptation; no-authority
related:
  - ../new-ideas-register.md
  - ../../../contracts/governance/sensitive_overlay_gatehouse_preflight.md
  - ../../../contracts/domains/people-dna-land/consented_genealogy_overlay.md
  - ../../../schemas/contracts/v1/governance/sensitive_overlay_gatehouse_preflight.schema.json
  - ../../../tools/validators/governance/validate_sensitive_overlay_gatehouse_preflight.py
tags: [kfm, pass-32, sensitive-overlay, gatehouse, consent, ga4gh, passport, visa, duo, tre, egress, intake]
notes:
  - "Records a bounded repository adaptation of KFM-P32-PROG-0018."
  - "The source documents and external standards remain evidence; they do not create repository policy, trust configuration, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pass 32 Sensitive Overlay Gatehouse Source Map

## Source candidate

| Field | Value |
|---|---|
| Atlas | `KFM_Pass_32_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` |
| Stable card | `KFM-P32-PROG-0018` |
| Card title | GA4GH token gatehouse stub |
| Pass 32 status | `NEW` / active / `PROPOSED` |
| Source IDs | `SRC-P32-002` (`New Ideas 5-17-26`) |
| Atlas `spec_hash` | `sha256:360ec29489c3ec11ff4e48f10f2fbc0e194765bd7349c2f6d221e34a0cfe542f` |
| Normalized statement | A gatehouse stub should validate consent and identity tokens, return `DENY` on uncertainty, and emit signed receipts for any sensitive overlay job. |
| Retrieved evidence | Google Drive source document and Pass 32 atlas, inspected 2026-08-09 |

The source proposal further calls for short-lived consent, GA4GH Passport/Visa
and revocation checks, DUO-aware policy, enclave/TRE-only work, tile-only egress,
no VCF/FASTA/raw/row-level egress, deny-by-default OPA/Conftest checks, and a
receipt/attestation trail.

## Repository reconciliation

**CONFIRMED at base `main@6947a2cbae6e02ce0bacedc74353f8dc3b430774`:**

- `contracts/domains/people-dna-land/consented_genealogy_overlay.md` already
  defines a synthetic, revocation-aware, non-identifying, restricted,
  not-released overlay candidate and explicitly denies raw genomic material;
- its validator and fixtures exercise active/expired/revoked consent, privacy,
  coarse precision, deterministic hashes, non-release, and no-network behavior;
- `contracts/common/identity_token.md` explicitly says KFM `IdentityToken` is a
  reference carrier, not an authentication credential, JWT, bearer token,
  consent token, or proof of identity;
- governance already has finite gate outcomes and sensitive release-review
  closure, but no GA4GH Passport/Visa summary preflight or tile-only sensitive
  overlay gatehouse;
- repository and PR search found no existing `GA4GH gatehouse`, `GA4GH
  Passport`, or `sensitive overlay gatehouse` implementation; and
- ADR-0029 is accepted and routes cross-family governance meaning, canonical
  schema, fixtures, validators, tests, workflows, source maps, and generated
  receipts to their established responsibility roots.

## External standard check

Primary sources inspected 2026-08-09:

- [GA4GH Passport specification 1.2.1](https://ga4gh.github.io/data-security/ga4gh-passport)
- [GA4GH AAI OIDC Profile](https://ga4gh.github.io/data-security/aai-openid-connect-profile)
- [GA4GH Data Security version history](https://ga4gh.github.io/data-security/versions)
- [GA4GH Data Use Ontology repository](https://github.com/EBISPOT/DUO)

The sources support a fail-closed trust posture: Passports and Visas require
validation before reliance; relevant Broker, issuer, and assertion-source trust
must be established; controlled access needs a controlled-access grant or
governed custom equivalent; expiry and relevant Visa conditions matter; and
identifier URLs used in policy are opaque values rather than fetch targets.

This PR does not claim GA4GH conformance. The profile consumes declarations
that upstream checks were performed and retains holds for the missing real
credential, cryptographic, trust, policy, and execution surfaces.

## Bounded adaptation

The selected slice adds a fixture-only
`SensitiveOverlayGatehousePreflight` contract, schema, deterministic validator,
41-case matrix, focused tests, read-only workflow, source map, and generated
receipt.

It accepts only synthetic verification summaries:

- active consent with hashed token reference, receipt reference, exact scope
  and audience, current revocation snapshot, and at most 24-hour lifetime;
- GA4GH Passport 1.2.1 summary with verified signature, Broker trust, audience,
  expiry, Visa-identity linkage, and matching controlled-access grant;
- used-Visa summaries with verified signature/issuer/source trust, current
  revocation, satisfied conditions, target binding, and expiry;
- declaration-only DUO terms plus an external evaluator reference, ontology
  digest, bound time, and verified match summary; and
- synthetic TRE plus PMTiles/MVT-only, non-public, not-released egress with no
  raw genomic, row-level, identifying, or outbound-network posture.

Every uncertainty or unsafe declaration returns `DENY`. The all-verified
synthetic case returns `HOLD`, not `ALLOW`, because operational dependencies
remain absent.

## Idea treatment

| Source pressure | Treatment | Reason |
|---|---|---|
| Validate consent and identity tokens | **SUMMARY PREFLIGHT IMPLEMENTED** | Raw token parsing and cryptographic verification remain outside repository-facing fixtures and are explicit holds. |
| Consent lifetime no greater than 24 hours | **IMPLEMENTED** | Validator checks interval length and requested-job TTL coverage. |
| GA4GH Passport/Visa, trust, conditions, expiry, revocation | **SUMMARY CHECKS IMPLEMENTED** | Exact finite denials cover unknown/failed states; no live Clearinghouse or trust registry is claimed. |
| DUO-aware policy | **DECLARATION CHECK ONLY** | Evaluator ref, ontology digest, evaluation time, and verified result are required; ontology reasoning and policy authorship are deferred. |
| Enclave/TRE job execution | **DECLARATION CHECK ONLY** | Synthetic TRE posture is required; attestation and execution remain unwired. |
| Tile-only egress; no VCF/FASTA/raw/row-level output | **IMPLEMENTED AS PREFLIGHT DENIALS** | Map-tile class/media types are required and unsafe egress flags deny. No artifact is emitted. |
| OPA/Conftest deny-by-default policy pack | **DEFERRED** | No accepted policy semantics or runtime input contract was found; inventing one would create authority rather than a bounded precursor. |
| Signed receipt for every sensitive job | **DEFERRED / HELD** | The source requirement is preserved as `SIGNED_RECEIPT_EMISSION_UNWIRED`; no unsigned substitute is emitted. |

## Directory Rules basis

| Responsibility | Repository home |
|---|---|
| Cross-family gatehouse semantics | `contracts/governance/sensitive_overlay_gatehouse_preflight.md` |
| Machine shape | `schemas/contracts/v1/governance/sensitive_overlay_gatehouse_preflight.schema.json` |
| Synthetic case matrix | `fixtures/contracts/v1/governance/sensitive_overlay_gatehouse_preflight/cases.json` |
| Durable validation | `tools/validators/governance/validate_sensitive_overlay_gatehouse_preflight.py` |
| Enforceability proof | `tests/validators/governance/test_sensitive_overlay_gatehouse_preflight.py` |
| Hosted read-only orchestration | `.github/workflows/sensitive-overlay-gatehouse-preflight.yml` |
| Source adaptation record | this file |
| AI authoring provenance | `data/receipts/generated/genrec-pass32-sensitive-overlay-gatehouse-20260809.json` |

No new root or parallel identity, consent, token, trust, key, policy, ontology,
proof, receipt, enclave, release, or publication authority is created.

## Validation and non-effects

The case matrix includes one positive `HOLD` and 40 exact `DENY` paths covering
consent verification/state/revocation/expiry/scope/receipt, the 24-hour cap,
Passport/Visa signature/trust/audience/linkage/target/conditions/revocation/
expiry, controlled-access grant presence, DUO binding, TRE and tile-only egress,
sensitive egress, network/public/release posture, authority overreach,
deterministic identity, and raw-token-field denial.

The change reads no live token or endpoint, performs no network request or key
fetch, stores no credential or genomic payload, evaluates no policy, starts no
job, emits no tile or signed receipt, and creates no release, deployment,
publication, or public-use authority.

## Deferred dependencies

See the contract's deferred-work list. Highest-priority dependencies are an
accepted raw-credential boundary, vetted security libraries, trust/key/
revocation configuration, consent authority, pinned DUO evaluator contract,
OPA policy semantics, attested TRE runtime, signed-receipt authority, and
release/correction/rollback/withdrawal integration.

## Rollback

Before merge, close the draft pull request and remove its review branch. After
an authorized merge, revert the additive commit and rerun the dedicated
workflow. No credential, consent record, policy decision, job, artifact,
enclave, receipt, release, deployment, or public surface requires restoration.

<p align="right"><a href="#top">Back to top</a></p>
