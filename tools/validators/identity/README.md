<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-identity-readme
title: tools/validators/identity README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-identity-steward-plus-contract-steward-plus-schema-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; identity-validator-routing-index; deterministic-identity; identity-token; spec-hash; canonicalization; provenance-aware; release-gated; non-authoritative
owning_root: tools/
responsibility: broad Identity validator routing index for checking governed identity carriers, identity_token references, spec_hash references, canonicalization posture, deterministic id posture, cross-record identity references, evidence/proof/release linkage, source-role and object-family identity boundaries, correction and rollback identity continuity, and public-surface identity leakage while deferring identity meaning, schemas, policy decisions, evidence records, receipts, lifecycle data, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../freshness/README.md
  - ../fauna/README.md
  - ../genealogy/README.md
  - ../../../docs/standards/canonicalization.md
  - ../../../docs/standards/SCHEMA-ORG.md
  - ../../../docs/architecture/contract-schema-policy-split.md
  - ../../../contracts/common/identity_token.md
  - ../../../contracts/common/spec_hash.md
  - ../../../contracts/data/validation_report.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../schemas/contracts/v1/common/identity_token.schema.json
  - ../../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../../schemas/contracts/v1/data/validation_report.schema.json
  - ../../../fixtures/contracts/v1/common/identity_token/
  - ../../../fixtures/contracts/v1/common/spec_hash/
  - ../../../policy/common/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file at tools/validators/identity/README.md. It does not confirm executable validator code."
  - "IdentityToken is a reference/identity carrier, not an authorization credential, security token, secret, login token, consent token, or proof of identity by itself."
  - "SpecHash is an integrity/reference carrier, not proof of correctness, admissibility, release, policy approval, or evidence closure."
  - "Canonicalization is about bytes, not semantics; validators must not use hash equality as a substitute for contract meaning, policy, evidence, review, or release state."
  - "ValidationReport records validation outcomes and is not proof closure, policy approval, release approval, catalog truth, or a process receipt by itself."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/identity

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-identity--validator--routing-informational)
![authority](https://img.shields.io/badge/authority-routing--index-lightgrey)
![security](https://img.shields.io/badge/identity-not--credential-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/identity/` is the broad Identity validator routing index for governed identity references, `identity_token`, `spec_hash`, canonicalization posture, deterministic identity checks, and cross-record identity continuity without becoming identity doctrine, schema authority, policy authority, proof authority, release authority, or authentication infrastructure.

---

## Purpose

`tools/validators/identity/` exists to organize Identity validation concerns under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do governed identity carriers preserve typed identity, deterministic reference posture, canonicalization/hash reproducibility, object-family boundaries, source-role boundaries, EvidenceRef/EvidenceBundle linkage, ValidationReport linkage, policy/review/release linkage, correction lineage, rollback continuity, and public-surface safety before they are used by catalog, proof, release, map, API, graph, Focus Mode, export, search, tile, screenshot, embedding, or AI surfaces?

The answer should be a deterministic validation result or routing decision. This folder should not create identity truth, credentials, security tokens, authentication tokens, consent tokens, EvidenceBundles, PolicyDecisions, ReleaseManifests, public IDs, proof packs, receipt authority, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/identity/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| `contracts/common/identity_token.md` | **CONFIRMED contract / validator NEEDS VERIFICATION** | Defines `identity_token` as a compact typed reference for governed KFM entities and explicitly not a credential or proof of identity by itself. |
| `contracts/common/spec_hash.md` | **CONFIRMED contract / validator placeholder behavior NEEDS VERIFICATION** | Defines `spec_hash` as an integrity/reference carrier and not proof of correctness, admissibility, policy approval, evidence closure, or release. |
| `docs/standards/canonicalization.md` | **CONFIRMED standard / implementation NEEDS VERIFICATION** | Defines canonicalization for artifacts whose identity is a `spec_hash` and warns canonicalization is about bytes, not semantics. |
| `contracts/data/validation_report.md` | **CONFIRMED contract / validator path NEEDS VERIFICATION** | Defines `ValidationReport` as a validation result and review-support object, not proof closure or release approval by itself. |
| Executables, registry wiring, schema bindings, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a runnable validator, test suite, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby roots and lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| Identity validator routing | `tools/validators/identity/` | This README and possible future validator adapters. |
| Shared validator plumbing | `tools/validators/_common/` | Common runner/helper code if accepted. |
| Identity meaning | `contracts/common/identity_token.md`, domain contracts, source/evidence/release contracts | Validator checks conformance; contracts define meaning. |
| Identity machine shape | `schemas/contracts/v1/common/identity_token.schema.json`, `schemas/contracts/v1/common/spec_hash.schema.json`, accepted schemas | Validator reads schemas; schemas define machine shape. |
| Canonicalization/hash standard | `docs/standards/canonicalization.md`, `contracts/common/spec_hash.md` | Validator checks reproducibility; standard/contract define posture. |
| Validation result meaning | `contracts/data/validation_report.md` | Validator may emit or reference reports only through accepted report/proof/receipt lanes. |
| Policy | `policy/common/`, domain policy roots, release policy roots | Validator reports policy gaps; does not decide policy. |
| Evidence/proofs | `contracts/evidence/`, `data/proofs/` | Validator checks references; does not create evidence truth. |
| Receipts | `data/receipts/` | Receipts remain separate from validation code. |
| Release decisions/corrections/rollback | `release/` | Validator pass is not release approval. |
| Fixtures and tests | `fixtures/`, `tests/` | Fixture/test authority stays outside this README. |
| Domain-specific identity | domain `IDENTITY_MODEL.md`, `domain_feature_identity.md`, domain validators | Domain identity remains domain-scoped unless promoted to common contract. |

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and field-level schemas are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Typed identity reference | Does the identity carrier declare what is referenced and what kind of thing it is? | Proof of personhood, source truth, or domain truth. |
| Issuer and issued time | Are issuer and issue time present where required by contract or policy? | Authorization or consent. |
| Canonicalization posture | Is the candidate canonicalized with the declared algorithm before hashing? | Semantic equivalence. |
| `spec_hash` integrity reference | Does the hash identify the same canonical bytes? | Correctness, admissibility, evidence closure, or release approval. |
| Object-family boundary | Does identity preserve entity type instead of collapsing run/source/evidence/release/domain feature/actor identities? | A universal identity mega-object. |
| Source-role boundary | Does identity preserve source, role, and authority context? | Interchangeable IDs across sources. |
| Evidence linkage | Can EvidenceRef or EvidenceBundle references resolve where required? | Generated language or summary proof. |
| Validation report linkage | Are validation outcomes linked without becoming proof or release approval? | Publication approval. |
| Correction and rollback continuity | Does identity remain traceable across correction, withdrawal, supersession, and rollback? | Immutable truth after correction. |
| Public-surface safety | Are public IDs safe, non-secret, non-credential, and non-sensitive? | Login token, API key, consent token, or sensitive identifier. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Identity validator routing index | `tools/validators/identity/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Common identity meaning | `contracts/common/identity_token.md`, `contracts/common/spec_hash.md` |
| Validation report meaning | `contracts/data/validation_report.md` |
| EvidenceBundle meaning | `contracts/evidence/evidence_bundle.md` |
| Machine shape | `schemas/contracts/v1/common/`, `schemas/contracts/v1/data/`, accepted schema homes |
| Policy and release gates | `policy/`, `release/` |
| Source descriptors and registries | `data/registry/` or accepted source registry homes |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/identity/`, `tests/common/`, `fixtures/contracts/v1/common/`, or accepted conventions |
| Domain-specific identity models | domain `docs/`, `contracts/`, `schemas/`, and validator lanes |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared identity-token, spec-hash, canonicalization, identity-continuity, evidence, policy, release, correction, rollback, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, validator registry entries, fixture shape, policy bundles, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as identity doctrine, schema home, policy home, source registry, evidence store, lifecycle data store, proof store, receipt store, release record store, credential store, auth/token service, consent authority, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/identity/` include checks that:

- verify `identity_token` instances remain small, typed, stable references rather than credentials or full records;
- verify `spec_hash` values use accepted canonicalization, algorithm tags, and digest formats;
- verify canonicalization inputs exclude non-meaning-bearing fields only when the governing standard allows it;
- verify IDs do not collapse object families, domains, source roles, actors, runs, evidence bundles, release records, or review records;
- verify public-facing identifiers are non-secret, non-credential, non-sensitive, and policy-safe;
- verify identity references resolve to expected contract/schema/policy/evidence/release homes when required;
- verify correction, supersession, rollback, and withdrawal keep identity lineage inspectable;
- emit deterministic validation findings for review without storing proof artifacts or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/identity/` | Correct home |
|---|---|
| Identity semantic contracts | `contracts/common/`, domain `contracts/` |
| Identity schemas, enums, DTOs, or machine shape | `schemas/contracts/v1/...` |
| Authentication credentials, login tokens, API keys, secrets, consent tokens, private identifiers | nowhere in repository-facing validator docs; use secure runtime/secret systems where appropriate |
| Policy rules, release gates, steward decisions, or sensitivity thresholds | `policy/`, `release/` |
| Source descriptors or registries | `data/registry/` or accepted registry homes |
| EvidenceBundles, proof packs, receipts, validation reports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, rollback cards, correction notices, withdrawal notices | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Tests and fixtures | `tests/`, `fixtures/` |
| Public API, UI, map, tile, search, graph, Focus Mode, export, screenshot, embedding, or AI runtime output | governed application/runtime roots |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `IDENTITY_VALIDATOR_PASS` | Configured Identity checks passed. |
| `IDENTITY_VALIDATOR_FAIL` | One or more configured Identity checks failed. |
| `IDENTITY_TOKEN_SCHEMA_MISSING` | Required identity-token schema binding is absent or unresolved. |
| `IDENTITY_TOKEN_NOT_CREDENTIAL` | Identity token correctly remains a reference, not a credential. |
| `IDENTITY_TOKEN_CREDENTIAL_MISUSE_DENIED` | Candidate uses identity token as credential, login token, secret, consent token, or proof of identity. |
| `SPEC_HASH_BINDING_MISSING` | Required spec-hash binding is absent or unresolved. |
| `SPEC_HASH_CANONICALIZATION_MISMATCH` | Hash does not match the declared canonical bytes/algorithm. |
| `SPEC_HASH_AUTHORITY_OVERCLAIM` | Hash is used as proof of correctness, evidence closure, policy approval, or release. |
| `OBJECT_FAMILY_IDENTITY_COLLAPSE` | Candidate collapses distinct object families or domain identities. |
| `SOURCE_ROLE_IDENTITY_COLLAPSE` | Candidate collapses source role, issuer, provenance, or authority context. |
| `EVIDENCE_REF_UNRESOLVED` | Required evidence identity cannot resolve to accepted evidence support. |
| `VALIDATION_REPORT_AUTHORITY_OVERCLAIM` | Validation report is treated as proof closure, policy approval, or release approval. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, rollback, or withdrawal reference is absent. |
| `PUBLIC_IDENTITY_LEAKAGE_DENIED` | Public surface exposes a secret, credential, sensitive identifier, or unsafe identity linkage. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future implementation sketch

Future implementation should remain small and reversible:

```text
tools/validators/identity/
├── README.md
├── validate_identity.py                 # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

If `validate_identity.py` is added, it should delegate to accepted common-contract, schema, canonicalization, evidence, policy, fixture, and release validators. It should not redefine identity meaning, copy schemas, copy policy, store fixtures, write lifecycle data, approve release, or publish public outputs.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at `tools/validators/identity/README.md`.
- [x] It marks this path as an Identity validator routing index, not identity doctrine, schema authority, policy authority, credential infrastructure, or release authority.
- [x] It links `identity_token`, `spec_hash`, canonicalization, and `ValidationReport` responsibilities to their owning roots.
- [x] It preserves deterministic identity, cite-or-abstain, evidence, policy, release, correction, rollback, and public-surface safety boundaries.
- [x] It marks executable behavior, registry wiring, schema bindings, policy bundles, fixtures, receipts, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to Identity validators are searched and classified.
- [ ] Accepted schema homes, policy homes, fixture homes, test paths, and report destinations are verified.
- [ ] Tests exercise valid and invalid identity-token, spec-hash, canonicalization, object-family, source-role, evidence-ref, release-ref, and public-surface cases.
- [ ] CI invokes the relevant Identity validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with Identity validator routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
