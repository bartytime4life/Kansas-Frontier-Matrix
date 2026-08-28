<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-people-compat-readme
title: contracts/people — People Contract Compatibility README
type: readme
version: v0.1
status: draft; compatibility; restricted-review; no-parallel-authority
owners: OWNER_TBD — People/DNA/Land steward · People contract steward · Living-person privacy steward · Consent steward · Evidence steward · Policy steward · Docs steward · Directory Rules reviewer
created: 2026-06-24
updated: 2026-06-24
policy_label: restricted-review; contracts; people; people-dna-land; compatibility; living-person-aware; consent-aware; evidence-bound; release-gated; no-parallel-authority
related:
  - ../README.md
  - ../domains/people-dna-land/README.md
  - ../domains/people-dna-land/people/README.md
  - ../domains/people-dna-land/genealogy/README.md
  - ../domains/people-dna-land/land-ownership/README.md
  - ../../docs/domains/people-dna-land/README.md
  - ../../docs/domains/people-dna-land/people.md
  - ../../docs/domains/people-dna-land/PEOPLE_DOMAIN_MODEL.md
  - ../../docs/domains/people-dna-land/IDENTITY_MODEL.md
  - ../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../docs/domains/people-dna-land/CONSENT_MODEL.md
  - ../../docs/domains/people-dna-land/CANONICAL_PATHS.md
  - ../../schemas/contracts/v1/domains/people-dna-land/
  - ../../policy/domains/people-dna-land/
  - ../../fixtures/domains/people-dna-land/
  - ../../tests/domains/people-dna-land/
  - ../../release/candidates/people-dna-land/
tags: [kfm, contracts, people, people-dna-land, compatibility, living-person, privacy, consent, evidence-bundle, policy-decision, release-gated, rollback, no-parallel-authority]
notes:
  - "Compatibility pointer for the requested `contracts/people/` path."
  - "The inspected canonical People / DNA / Land contract lane is `contracts/domains/people-dna-land/`; the inspected people subfolder is `contracts/domains/people-dna-land/people/`."
  - "This README does not create a person store, identity authority, schema home, policy home, source registry, consent store, lifecycle-data store, release gate, public API, map layer, or AI truth surface."
  - "Previous file content was a placeholder; rollback target is blob SHA `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/people

> Compatibility guard for the legacy/requested `contracts/people/` path. Use [`contracts/domains/people-dna-land/`](../domains/people-dna-land/) and its [`people/`](../domains/people-dna-land/people/) subfolder for inspected People / DNA / Land semantic contracts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility" src="https://img.shields.io/badge/path-compatibility-lightgrey">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-6f42c1">
  <img alt="Living person: fail closed" src="https://img.shields.io/badge/living__person-fail__closed-critical">
  <img alt="Authority: pointer only" src="https://img.shields.io/badge/authority-pointer__only-lightgrey">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release__gated-critical">
</p>

**Status:** draft compatibility guard  
**Owners:** `OWNER_TBD` — People/DNA/Land steward · People contract steward · Living-person privacy steward · Consent steward · Evidence steward · Policy steward · Docs steward · Directory Rules reviewer  
**Path:** `contracts/people/README.md`  
**Canonical inspected domain contract lane:** [`../domains/people-dna-land/`](../domains/people-dna-land/)  
**Inspected people contract subfolder:** [`../domains/people-dna-land/people/`](../domains/people-dna-land/people/)  
**Truth posture:** CONFIRMED placeholder replaced · CONFIRMED inspected People / DNA / Land contract lane exists · CONFIRMED inspected people subfolder exists · PROPOSED cleanup until steward/ADR review resolves whether this legacy path should remain

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Compatibility flow](#compatibility-flow) · [People trust rules](#people-trust-rules) · [Migration checklist](#migration-checklist) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Scope

`contracts/people/` is **not** the inspected canonical people contract lane.

This README exists to prevent a short, convenient path from becoming a parallel authority for people/person identity contracts. In the inspected repo evidence, people/person semantic contracts are part of the broader People / DNA / Land bounded context under `contracts/domains/people-dna-land/`, with a `people/` subfolder for person-oriented contract meaning.

> [!IMPORTANT]
> **Do not add person object contracts here unless an accepted ADR or migration explicitly moves them.** Person assertions, name assertions, identity candidates, life events, residence events, migration events, and person-canonical semantics should use the inspected People / DNA / Land contract lane until placement is formally changed.

---

## Repo fit

| Responsibility | Current or expected path | Relationship to this README |
|---|---|---|
| Contracts root rule | [`../README.md`](../README.md) | Contracts define semantic meaning; schemas, policy, tests, and data remain separate. |
| People / DNA / Land contract lane | [`../domains/people-dna-land/`](../domains/people-dna-land/) | Inspected parent lane for semantic contracts. |
| People subfolder | [`../domains/people-dna-land/people/`](../domains/people-dna-land/people/) | Inspected person-oriented contract subfolder. |
| Genealogy subfolder | [`../domains/people-dna-land/genealogy/`](../domains/people-dna-land/genealogy/) | Adjacent relationship/family context, not this path. |
| Land-ownership subfolder | [`../domains/people-dna-land/land-ownership/`](../domains/people-dna-land/land-ownership/) | Adjacent land/title/person-party context, not this path. |
| People domain docs | `../../docs/domains/people-dna-land/` | Domain doctrine, identity, sensitivity, consent, and path notes. |
| Machine schemas | `../../schemas/contracts/v1/domains/people-dna-land/` | Shape authority; not this folder. |
| Policy and consent gates | `../../policy/domains/people-dna-land/` and accepted sensitivity/consent policy roots | Allow/deny/restrict/abstain authority; not this folder. |
| Fixtures and tests | `../../fixtures/domains/people-dna-land/`, `../../tests/domains/people-dna-land/` | Proof and examples; not semantic authority. |
| Source registry | `../../data/registry/sources/people-dna-land/` or accepted source-registry home | Source role, cadence, rights, caveats, activation state. |
| Lifecycle data | `../../data/raw/`, `../../data/work/`, `../../data/quarantine/`, `../../data/processed/`, `../../data/catalog/`, `../../data/published/` | Evidence-bearing artifacts by lifecycle phase; not contracts. |
| Release and rollback | `../../release/candidates/people-dna-land/` and release roots | Promotion, release, correction, withdrawal, rollback authority. |

---

## Accepted inputs

Only conservative content belongs here while `contracts/people/` remains a compatibility path:

| Accepted item | Purpose | Required posture |
|---|---|---|
| `README.md` | Compatibility pointer to the inspected People / DNA / Land contract lane. | Accepted. |
| Migration note | Temporary note if maintainers move people contracts into or out of this path. | Temporary; must include rollback. |
| Backlink audit note | Temporary note listing inbound references to `contracts/people/`. | Temporary. |

No durable object contracts, schemas, fixtures, policies, source records, lifecycle data, consent records, release records, runtime files, public payloads, or AI outputs should be added here without accepted governance.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| Person assertion or identity semantic contracts | `../domains/people-dna-land/people/` unless ADR moves them | Avoids parallel people authority. |
| Genealogy relationship contracts | `../domains/people-dna-land/genealogy/` or accepted home | Relationship semantics are adjacent but distinct. |
| Land/title/person-party contracts | `../domains/people-dna-land/land-ownership/` or accepted home | Land evidence and title-sensitive semantics are distinct. |
| JSON Schema | `../../schemas/contracts/v1/domains/people-dna-land/` | Schemas own machine-checkable shape. |
| Policy, consent, redaction, rights, or access rules | `../../policy/...` accepted homes | Policy owns allow/deny/restrict/abstain behavior. |
| Source descriptors and rights registries | `../../data/registry/sources/people-dna-land/` or accepted registry home | Source authority and rights posture must remain auditable. |
| Raw family-tree exports, source files, scans, OCR, vital/census/court/probate records, or DNA material | `../../data/<phase>/people-dna-land/` or accepted restricted lifecycle homes | Lifecycle and sensitivity controls do not live in contracts. |
| Person records, identity records, consent records, proof/receipt records | Governed lifecycle, consent, proof, receipt, or release roots | Contracts describe meaning; they do not store people or consent state. |
| Public API routes, UI components, Focus Mode answers, map layers | `../../apps/`, `../../packages/`, governed API/release roots | Public clients use governed interfaces and released artifacts. |
| AI-generated identity, biography, lineage, or residence narratives as truth | Governed AI envelopes with citations and receipts | Generated language is interpretive and evidence-subordinate. |

---

## Compatibility flow

```mermaid
flowchart LR
  legacy["contracts/people<br>compatibility guard"] -. points to .-> parent["contracts/domains/people-dna-land<br>semantic contract lane"]
  parent --> people["people/<br>person-oriented contract meaning"]
  parent --> genealogy["genealogy/<br>relationship context"]
  parent --> land["land-ownership/<br>land/title-sensitive context"]
  people --> schemas["schemas/contracts/v1/domains/people-dna-land<br>machine shape"]
  people --> policy["policy/domains/people-dna-land<br>privacy, consent, access gates"]
  people --> data["data lifecycle roots<br>RAW to PUBLISHED"]
  people --> release["release roots<br>promotion, correction, rollback"]
```

---

## People trust rules

People/person contracts are high-risk and must stay assertion-first.

Minimum posture:

- a person-shaped claim is an assertion with source role, evidence, time, uncertainty, review, and sensitivity context;
- canonical identity is not public truth by itself;
- living-person, residence, identity-link, DNA-derived, and private person-to-place/person-to-parcel details fail closed unless evidence, rights, consent where required, policy, review, release, correction, and rollback gates all pass;
- contract prose cannot create consent, release state, title authority, source authority, or identity adjudication;
- public clients must consume governed APIs and released artifacts, not RAW, WORK, QUARANTINE, canonical/internal stores, private joins, or direct model output;
- generated language may summarize evidence only when citations and policy allow it, and must abstain or deny when support is missing.

---

## Migration checklist

Before making `contracts/people/` canonical:

- [ ] Confirm why `contracts/domains/people-dna-land/people/` is insufficient.
- [ ] Add an ADR or migration note explaining the ownership change.
- [ ] Preserve People / DNA / Land cross-lane boundaries for genealogy, DNA, consent, and land/title assertions.
- [ ] Pair any moved object contract with the accepted schema home.
- [ ] Link policy, sensitivity, consent, fixtures, tests, source registry, release, correction, and rollback requirements.
- [ ] Preserve history with `git mv` where moving existing files.
- [ ] Update inbound links and remove stale compatibility notes after migration.
- [ ] Re-review living-person and DNA/privacy exposure defaults before any public release.

---

## Validation checklist

- [ ] `contracts/people/` contains no durable object contracts beyond this compatibility README unless an ADR accepts the path.
- [ ] The inspected People / DNA / Land contract lane remains discoverable.
- [ ] The inspected `people/` subfolder remains the person-oriented contract home until migration.
- [ ] No schema, policy, source registry, data, consent, proof, receipt, release, runtime code, UI, API, map, or AI output is normalized here.
- [ ] Living-person, identity, DNA-derived, residence, and private-join material remains fail-closed.

---

## Rollback

Rollback is required if this README is used to justify a parallel people authority, bypass People / DNA / Land governance, publish living-person or DNA-derived material, store people data under contracts, or treat generated identity narratives as evidence.

Rollback target for this replacement: previous placeholder blob SHA `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`.

<p align="right"><a href="#top">Back to top</a></p>
