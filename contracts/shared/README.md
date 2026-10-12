<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-shared-readme
title: contracts/shared — Shared Contract Semantics README
type: readme
version: v0.1
status: draft; proposed-lane; shared-semantics; no-dumping-ground; needs-steward-review
owners: OWNER_TBD — Contracts steward · Schema steward · Policy steward · Domain stewards · Evidence steward · Docs steward · Directory Rules reviewer
created: 2026-06-24
updated: 2026-06-24
policy_label: public; contracts; shared; semantic-contracts; cross-domain; no-parallel-authority; no-schema; no-policy; no-data; no-runtime
tags: [kfm, contracts, shared, README, semantic-contracts, cross-domain, common-objects, no-dumping-ground, schemas, policy, fixtures, tests, evidence-first]
related:
  - ../README.md
  - ../domains/README.md
  - ../../schemas/contracts/v1/
  - ../../policy/
  - ../../fixtures/
  - ../../tests/
  - ../../tools/validators/
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "This file replaces a blank placeholder at `contracts/shared/README.md`."
  - "No existing shared contract lane content was found by repo search in this session; this README therefore defines a PROPOSED guarded lane, not mature implementation."
  - "Contracts root documentation says `contracts/` owns semantic meaning and does not contain executable validation, JSON Schema, policy code, or source data."
  - "Shared contracts must be cross-domain semantic primitives only; domain-owned object meaning belongs under `contracts/domains/<domain>/` or an established contract family root."
  - "This lane must not become a dumping ground for helpers, schemas, code, policy, data, release artifacts, fixtures, tests, or generated AI text."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/shared

> Proposed shared semantic-contract lane for cross-domain KFM object meanings that are genuinely reused by multiple contract families and do not belong to one domain. This is **not** a generic utilities folder and must not become a parallel schema, policy, data, runtime, release, fixture, or test root.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lane: proposed" src="https://img.shields.io/badge/lane-proposed-orange">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Purpose: shared semantic meaning" src="https://img.shields.io/badge/purpose-shared__semantic__meaning-blueviolet">
  <img alt="Posture: no dumping ground" src="https://img.shields.io/badge/posture-no__dumping__ground-critical">
</p>

**Status:** draft / proposed shared semantic-contract lane  
**Path:** `contracts/shared/README.md`  
**Owning root:** `contracts/` — semantic meaning only  
**Schema home:** `schemas/contracts/v1/` or accepted schema family roots  
**Policy home:** `policy/` and policy-family roots  
**Truth posture:** CONFIRMED placeholder was blank · CONFIRMED no existing shared contract-lane content found by repo search in this session · CONFIRMED `contracts/` owns semantic meaning and excludes JSON Schema/executable validation/policy/source data · PROPOSED guarded lane until steward review defines accepted shared contract inventory

## Quick jumps

[Purpose](#purpose) · [When to use shared](#when-to-use-shared) · [Authority split](#authority-split) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Authoring rules](#authoring-rules) · [Validation checklist](#validation-checklist) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`contracts/shared/` is a proposed home for cross-domain semantic contracts that are not owned by a single domain lane and are not already covered by an established contract family such as `evidence`, `policy`, `runtime`, `release`, `source`, `governance`, `data`, or `review`.

Use this lane only when the object meaning is:

1. reused across multiple domains or contract families;
2. stable enough to justify a shared contract surface;
3. semantic Markdown, not machine schema or code;
4. not already better owned by an existing responsibility root;
5. reviewed for no-parallel-authority risk.

---

## When to use shared

Use `contracts/shared/` only for common semantic primitives such as:

| Candidate shared contract | Why it might belong here | Status |
|---|---|---|
| `identity_ref.md` | Cross-domain reference semantics for stable object identities. | PROPOSED |
| `time_interval.md` | Cross-domain meaning for valid/observed/effective time windows. | PROPOSED |
| `provenance_ref.md` | Shared reference semantics where not specific to EvidenceBundle or SourceDescriptor. | PROPOSED |
| `geometry_ref.md` | Shared geometry reference semantics where not owned by map/data schemas. | PROPOSED |
| `sensitivity_ref.md` | Shared pointer semantics to sensitivity posture, not the policy decision itself. | PROPOSED |

Do not add these files until their ownership, schema pairing, policy behavior, fixtures, tests, and migration risk are reviewed.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| Shared semantic meaning | `contracts/shared/` | Proposed lane for cross-domain Markdown contracts only. |
| Domain-specific meaning | `contracts/domains/<domain>/` | Domain-owned objects stay with their bounded context. |
| Established family meaning | `contracts/<family>/` | Evidence, policy, runtime, release, source, governance, data, review, etc. stay in their family roots. |
| Machine shape | `schemas/contracts/v1/` | JSON Schema and JSON-LD context belong under `schemas/`. |
| Policy/admissibility | `policy/` and policy-family roots | Policy owns allow/deny/restrict/abstain behavior. |
| Fixtures/examples | `fixtures/` and accepted fixture roots | Examples/proof data stay outside contracts. |
| Tests/enforcement | `tests/` and accepted test roots | Proof belongs in tests. |
| Validators/code | `tools/validators/`, packages, apps, pipelines, or accepted implementation roots | Executable behavior stays outside contracts. |
| Release/correction/rollback | `release/` and release contract/release roots | Publication is a governed state transition. |

---

## Accepted contents

| Accepted content | Purpose | Required guardrail |
|---|---|---|
| `README.md` | Lane boundary and maintainer rules. | Must preserve no-dumping-ground posture. |
| Shared semantic contract Markdown | Defines meaning for a truly cross-domain primitive. | Must include owner, schema/policy/test/fixture links or mark them NEEDS VERIFICATION. |
| `INDEX.md` | Optional inventory of accepted shared contracts. | Must not include proposed files as implemented facts. |
| `MIGRATION.md` | Optional migration/ADR notes for moved shared primitives. | Must identify rollback/backlink handling. |
| `BACKLINKS.md` | Optional stale-reference audit. | Must be factual and reviewable. |

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| Domain-owned contracts | `contracts/domains/<domain>/` | Avoids weakening domain boundaries. |
| EvidenceBundle / EvidenceRef semantics | `contracts/evidence/` or accepted evidence root | Evidence has its own authority lane. |
| PolicyDecision / PolicyInputBundle semantics | `contracts/policy/` | Policy object meaning has its own family root. |
| DecisionEnvelope / runtime response semantics | `contracts/runtime/` | Runtime objects have their own family root. |
| ReleaseManifest / rollback / withdrawal semantics | `contracts/release/` | Release objects have their own family root. |
| JSON Schema | `schemas/contracts/v1/` | Schemas own shape. |
| Policy rules | `policy/` | Policy owns admissibility. |
| Source data or registry records | data/source registry roots | Contracts do not admit or store sources. |
| Fixtures/tests/validators | `fixtures/`, `tests/`, `tools/validators/` | Enforceability and execution stay separate. |
| Helper code, generated SDKs, utility functions | packages/tools/apps/pipelines | `shared` here is semantic, not code. |
| Generated AI summaries as authority | governed AI/runtime/evidence flows | EvidenceBundle outranks generated text. |

---

## Authoring rules

Before creating a shared contract file:

1. Search for an existing family or domain owner.
2. Check whether the object is truly cross-domain rather than merely convenient.
3. Identify the paired schema home or mark schema status NEEDS VERIFICATION.
4. Identify policy implications or explicitly state none are known.
5. Identify fixtures/tests or mark enforceability NEEDS VERIFICATION.
6. State source/evidence/release/rollback boundaries.
7. Include rollback path and migration/backlink notes if the object moved from another lane.

Shared contracts should reduce duplication, not create ambient authority.

---

## Validation checklist

- [ ] Verify no JSON Schema files are added under `contracts/shared/`.
- [ ] Verify no executable code, policy rules, fixtures, tests, generated SDKs, or lifecycle data are added here.
- [ ] Verify each future shared contract has no clearer owner under `contracts/<family>/` or `contracts/domains/<domain>/`.
- [ ] Verify each future shared contract has a schema/policy/fixture/test posture or explicit NEEDS VERIFICATION labels.
- [ ] Verify no public API/UI/map/AI behavior treats shared contracts as runtime permission or evidence truth.
- [ ] Review shared-lane additions for ADR need when they alter existing object ownership.

---

## Open questions

- Should `contracts/shared/` remain as a proposed lane, or should all shared primitives live under established family roots?
- Which shared primitives are already implied by schemas but lack semantic contracts?
- Should new shared contracts require ADR review by default?
- Should `contracts/shared/INDEX.md` be created only after the first accepted shared contract exists?

---

## Rollback

Rollback is required if this folder is used as a dumping ground, schema root, policy root, data root, release root, runtime/API root, code root, fixture/test root, validator root, or a way to bypass domain/family ownership.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
