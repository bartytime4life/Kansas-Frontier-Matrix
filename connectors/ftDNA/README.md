<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ftdna-readme
title: connectors/ftDNA/ — FamilyTreeDNA Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · People/DNA/Land steward · Consent steward · Sensitivity reviewer · Rights-holder representative · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: restricted-doctrine; consent-required; default-deny
proposed_path: connectors/ftDNA/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-lane contract / UNKNOWN implementation depth
related:
  - ../README.md
  - ../../docs/domains/people-dna-land/README.md
  - ../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../docs/domains/people-dna-land/SOURCE_FAMILIES.md
  - ../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../docs/domains/people-dna-land/sublanes/genealogy.md
  - ../../docs/sources/catalog/README.md
  - ../../data/registry/sources/people-dna-land/
  - ../../data/raw/people-dna-land/
  - ../../data/quarantine/people-dna-land/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../schemas/contracts/v1/source/
  - ../../schemas/contracts/v1/consent/
  - ../../policy/consent/people/
  - ../../policy/sensitivity/people/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, ftdna, familytreedna, people-dna-land, genealogy, dna, consent, source-admission, raw, quarantine, governance]
notes:
  - "This README replaces a greenfield stub with a governed connector-lane contract for ftDNA / FamilyTreeDNA source admission."
  - "No ftDNA-specific source catalog page was found in repo search during this update; connector details remain NEEDS VERIFICATION until a SourceDescriptor and source profile exist."
  - "People/DNA/Land docs define this as a highest-sensitivity lane where living-person and DNA-derived material is denied or restricted by default."
  - "Source listing, connector activation, and consent are not publication grants. Public release requires downstream policy, review, evidence, release, correction, and rollback support."
  - "Connector output may enter RAW or QUARANTINE only; validation, transformation, graph projection, publication, and release remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FamilyTreeDNA Connector

> Proposed source-admission connector lane for ftDNA / FamilyTreeDNA material inside the KFM People / Genealogy / DNA / Land domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Consent: required" src="https://img.shields.io/badge/consent-required-critical">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/ftDNA/`

## Quick jumps

[Scope](#scope) · [Evidence basis](#evidence-basis) · [Authority boundary](#authority-boundary) · [Admission posture](#admission-posture) · [Consent and review posture](#consent-and-review-posture) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/ftDNA/` is a proposed connector lane for admitting source-shaped material from ftDNA / FamilyTreeDNA into KFM governance.

It may contain connector-local documentation, configuration examples, source-admission code, consent-aware import helpers, parser helpers, bounded client helpers, and tests.

It must not become person truth, kinship truth, DNA truth, land-title truth, consent authority, source descriptor authority, policy authority, schema authority, graph authority, proof authority, release authority, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/ftDNA/`  
> **Truth posture:** README path is CONFIRMED. Implementation files, source profile, SourceDescriptor, consent-sidecar behavior, rights review, test fixtures, CI wiring, and activation state remain `NEEDS VERIFICATION`.

---

## Evidence basis

Repo evidence checked for this update:

- `connectors/ftDNA/README.md` existed as a greenfield stub.
- Search did not find an ftDNA-specific source catalog page.
- People/DNA/Land domain docs define living-person and DNA-derived material as denied or restricted by default.
- The People/DNA/Land source registry states that listing a source is admission control, not a publication grant and not a substitute for consent.

This README therefore stays at connector-lane level and does not invent endpoints, auth flows, export formats, kit fields, rate limits, or source terms.

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/people-dna-land/
  data/quarantine/people-dna-land/

NOT HERE:
  person identity truth
  kinship truth
  DNA interpretation truth
  title or ownership truth
  consent authority
  source descriptor authority
  policy authority
  schema authority
  processed records
  graph/triplet records
  published records
  release decisions
```

This connector may help stage source material for governed admission. It does not decide whether a person assertion, kinship assertion, match assertion, land relationship, or derived claim is true, consent-valid, rights-cleared, review-complete, or publishable.

---

## Admission posture

Expected behavior:

- no live access unless explicitly enabled and reviewed;
- no source fetch without a SourceDescriptor and activation decision;
- no import without scoped consent and review state where required;
- no implicit publication from retrieved or imported material;
- no generated claims treated as evidence;
- no conversion of private or vendor-scoped records into public truth;
- no loss of source identity, retrieval metadata, consent reference, rights reference, source role, review state, or revocation state;
- unclear consent, rights, source role, identity mapping, or review status routes to quarantine or abstention.

Recommended finite outcomes:

| Situation | Outcome |
|---|---|
| SourceDescriptor missing | `ABSTAIN` or connector error. |
| Consent sidecar missing where required | Quarantine or deny. |
| Live access not enabled | `ABSTAIN`; fixture-based tests still pass. |
| Rights or terms unclear | `NEEDS_VERIFICATION`; no live activation. |
| Identity mapping unclear | Quarantine or review-required result. |
| Revocation state unclear | Quarantine or review-required result. |
| Source response malformed | `ERROR` with safe metadata. |

---

## Consent and review posture

Consent does not publish data. It constrains whether the connector may stage, transform, render, or retain material under a governed rule.

Minimum posture:

1. Consent must be scoped, recorded, reviewable, and revocable where required.
2. Revocation must block future use and trigger downstream cleanup according to policy.
3. Vendor exports and private identifiers must not be exposed through public outputs.
4. Derived outputs remain restricted unless downstream policy, evidence, review, release, correction, and rollback support exists.
5. Public surfaces must use governed APIs and released artifacts only, never RAW, QUARANTINE, internal connector state, or direct model output.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- SourceDescriptor references are required for activation;
- consent and rights references are present where required;
- records carry source role, review state, and lifecycle target;
- malformed or incomplete responses fail closed;
- uncertain identity or consent state routes to quarantine or denial;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or explicitly approved.

Root-level validation, policy-as-code, release gates, consent review, EvidenceBundle closure, and rollback remain outside this connector.

---

## Definition of done

This connector lane is ready for first review when:

- [ ] An ftDNA / FamilyTreeDNA source catalog profile exists or this README links to an approved alternative source profile.
- [ ] SourceDescriptor location and source ID are verified.
- [ ] Live access is disabled by default.
- [ ] Source terms, permitted use, and retention rules are reviewed.
- [ ] Consent sidecar requirements are documented and tested.
- [ ] Revocation handling is documented and tested.
- [ ] Connector outputs are limited to RAW or QUARANTINE handoff.
- [ ] No public claims are created by connector code.
- [ ] Tests cover no-network, missing descriptor, missing consent, revoked consent, malformed response, identity-unclear, rights-unclear, and review-required cases.
- [ ] Reviewers have a rollback and cleanup path for connector activation and cached material.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm exact source name, source profile, and source_id. | **NEEDS VERIFICATION** | Source catalog profile and SourceDescriptor. |
| Confirm actual implementation files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm allowed access method and terms. | **NEEDS VERIFICATION** | Source steward and rights review. |
| Confirm consent-sidecar schema and storage path. | **NEEDS VERIFICATION** | `schemas/contracts/v1/consent/` and policy docs. |
| Confirm revocation and cleanup behavior. | **NEEDS VERIFICATION** | Consent policy and runbook. |
| Confirm fixture strategy. | **NEEDS VERIFICATION** | Fixture registry and validation review. |
| Confirm CI wiring for connector-local tests. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

Keep this connector narrow and consent-first. It should help stage source material for governed review without becoming a parallel source registry, identity resolver, consent engine, interpretation engine, release path, or public truth surface.
