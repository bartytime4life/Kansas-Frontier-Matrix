<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-people-dna-land-readme
title: People-DNA-Land Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - People-DNA-Land domain steward
  - OWNER_TBD - Privacy steward
  - OWNER_TBD - Consent steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
created: 2026-07-06
updated: 2026-07-06
policy_label: restricted-doc; tests; fixtures; people-dna-land; synthetic-only; no-network; deny-by-default; consent-aware; revocation-aware; land-link-aware; renderer-not-truth
tags: [kfm, tests, fixtures, people-dna-land, people, dna, land, consent, revocation, privacy, land-link, synthetic, no-network, DENY, ABSTAIN, HOLD, ERROR]
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../policy/consent/people-dna-land/README.md
  - ../../../docs/domains/people-dna-land/RELEASE_INDEX.md
  - ../../../contracts/domains/people-dna-land/
  - ../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../policy/sensitivity/
  - ../../../policy/consent/
  - ../../../release/
notes:
  - "This README replaces placeholder content at tests/fixtures/people-dna-land/README.md."
  - "This lane is for unit-test-scoped, synthetic, public-safe People-DNA-Land fixtures only. It is not a source-data home, consent register, evidence store, release store, title authority, genealogy authority, DNA authority, policy home, or public map root."
  - "Fixtures in this lane must fail closed for living-person, consent, revocation, relationship, DNA/genomic, and private person-land join uncertainty."
  - "Executable tests, payload inventory, schema bindings, consent runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People-DNA-Land test fixtures

> Unit-test-scoped fixture lane for synthetic People-DNA-Land examples. This README keeps privacy, consent, revocation, DNA/genomic, relationship, and land-link test cases reviewable without making fixtures into identity truth, title truth, source authority, consent authority, policy authority, evidence closure, release approval, or public map artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: people-dna-land" src="https://img.shields.io/badge/lane-people--dna--land-purple">
  <img alt="Default: deny closed" src="https://img.shields.io/badge/default-deny__closed-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/people-dna-land/README.md`  
**Status:** draft / placeholder replaced / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/people-dna-land`  
**Default posture:** synthetic, minimized, no-network, public-safe transformed, deny-by-default fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED `tests/fixtures/` is unit-test-scoped by repo doctrine; CONFIRMED People-DNA-Land sensitivity doctrine is deny-by-default for living-person, DNA/genomic, and private person-land surfaces; NEEDS VERIFICATION for fixture payload inventory, executable tests, schemas, consent runtime wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/fixtures/people-dna-land/` for small synthetic fixtures that exercise People-DNA-Land test expectations.

In scope:

- consent, revocation, expiration, dispute, and purpose-scope examples;
- minimized person, relationship, derivative, and land-link examples;
- privacy-preserving denial, abstention, hold, correction, and rollback canaries;
- synthetic source-role, evidence-state, release-state, and policy-state examples;
- test-local manifests that explain expected outcomes without carrying real protected material.

Out of scope:

- real person records;
- real DNA/genomic material;
- real private family, household, relationship, or land-link detail;
- title records or source exports;
- public map payloads;
- production consent records, receipts, proofs, releases, or policy rules.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Unit-test-scoped People-DNA-Land fixtures | `tests/fixtures/people-dna-land/` | This lane. |
| Domain tests | `tests/domains/people-dna-land/` | Expected consumers; not fixture authority. |
| Reusable cross-test fixtures | `fixtures/domains/people-dna-land/` if accepted | Cross-cutting fixture home; NEEDS VERIFICATION. |
| Consent policy | `policy/consent/people-dna-land/` and parent consent roots | Policy authority; not owned here. |
| Sensitivity policy/profile | `docs/domains/people-dna-land/SENSITIVITY_PROFILE.md`, policy roots | Governs default-deny posture. |
| Object meaning | `contracts/domains/people-dna-land/` | Defines semantics; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/people-dna-land/` or accepted schema home | Shape authority; NEEDS VERIFICATION. |
| Release decisions | `release/` | Publication, correction, withdrawal, and rollback authority. |

> [!IMPORTANT]
> This fixture lane must not become a second consent register, identity graph, genealogy store, land-title store, DNA store, evidence store, release store, policy home, schema home, or public map artifact root.

---

## Fixture rule

People-DNA-Land fixtures are downstream test carriers. They should prove fail-closed behavior without exposing real protected values.

Core expectations:

| Expectation | Required posture |
|---|---|
| Synthetic only | Use toy IDs, toy refs, toy dates, toy relations, and toy land-link placeholders. |
| No-network default | No live source, identity, genealogy, parcel, title, vendor, API, model, tile, or public-service calls. |
| Minimized identifiers | Use pseudonymous or placeholder refs only. |
| Consent-aware | Missing, expired, disputed, revoked, ambiguous, or out-of-scope consent blocks materialization. |
| Revocation-aware | Revoked or disputed examples must expect denial, hold, correction, or cache/derivative invalidation posture. |
| Land-link-aware | Person-land joins require evidence, consent, sensitivity, rights, review, and release checks; fixtures cannot imply title truth. |
| Finite outcomes | Expected outcomes should be explicit where useful: `ALLOW`, `DENY`, `ABSTAIN`, `HOLD`, `ERROR`, or validation failure. |

---

## Accepted inputs

Accepted material is limited to compact, synthetic, reviewable examples, such as:

- small `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` fixture notes;
- toy consent grant refs and toy revocation refs;
- toy person refs, relationship refs, and land-link refs;
- toy EvidenceRef, PolicyDecision, ReviewRecord, CorrectionNotice, RollbackCard, and ReleaseManifest refs;
- expected outcome and reason-code examples for `DENY`, `ABSTAIN`, `HOLD`, `ERROR`, and public-safe `ALLOW` cases;
- links to consumer tests once those tests are verified.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| real person, family, relationship, DNA/genomic, private land-link, source export, or title material | governed lifecycle roots, consent/policy gates, or quarantine as appropriate |
| consent records, consent receipts, revocation infrastructure, or consent registry entries | consent policy/register/receipt roots after verification |
| evidence bundles, proofs, receipts, release manifests, rollback cards, or correction notices | their governed responsibility roots |
| policy rules or schemas | `policy/` and `schemas/` |
| domain implementation code | accepted package or app roots |
| public map payloads, tiles, screenshots, or exports | governed publication/artifact roots only after release |
| secrets, private endpoints, production logs, or external identifiers | not allowed in repository fixtures |

---

## Suggested layout

```text
tests/fixtures/people-dna-land/
|-- README.md
|-- consent_missing.deny.json
|-- consent_revoked.deny.json
|-- consent_expired.deny.json
|-- consent_out_of_scope.deny.json
|-- relationship_disputed.hold.json
|-- derivative_unsupported.abstain.json
|-- land_link_private_join.deny.json
|-- release_state_missing.abstain.json
|-- correction_visible.valid.json
`-- rollback_required.valid.json
```

The layout is PROPOSED until payload files and consumers exist.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/domains/people-dna-land tests/fixtures/people-dna-land
```

Default runs should be deterministic, local, no-network, minimized, and finite-outcome only.

---

## Maintenance checklist

- [ ] Keep examples synthetic, minimized, compact, and reviewable.
- [ ] Make consent, purpose, audience, revocation, evidence, sensitivity, review, release, correction, and rollback posture explicit where material.
- [ ] Use `DENY`, `ABSTAIN`, or `HOLD` for missing, revoked, disputed, unsupported, or out-of-scope cases.
- [ ] Do not store real protected material, source exports, production consent records, evidence records, policy rules, schemas, public artifacts, or secrets here.
- [ ] Link to consumer tests only after verification.
- [ ] Update this README when fixture payloads, schemas, tests, or consent runtime wiring are verified.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; placeholder replaced. |
| Consent policy lane | CONFIRMED as draft doctrine; runtime enforcement NEEDS VERIFICATION. |
| Sensitivity profile | CONFIRMED as draft doctrine for deny-by-default posture. |
| Fixture payload inventory | NEEDS VERIFICATION. |
| Consumer tests | NEEDS VERIFICATION. |
| Schema bindings | NEEDS VERIFICATION. |
| Consent runtime wiring | NEEDS VERIFICATION. |
| Runner and CI wiring | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
