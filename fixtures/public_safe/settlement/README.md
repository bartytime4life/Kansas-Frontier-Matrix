<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-public-safe-settlement-readme
title: fixtures/public_safe/settlement/README.md — Public-safe Settlement Fixtures
version: v0.2.0
type: readme; fixture-sublane; public-safe; synthetic; settlements-infrastructure-context
status: draft; CONFIRMED path; public-safe fixture guidance; implementation NEEDS VERIFICATION
owners: OWNER_TBD — Fixture steward · Settlements/Infrastructure steward · Evidence steward · Policy steward · Sensitivity reviewer · UI steward · Docs steward
created: NEEDS VERIFICATION — placeholder lineage predates this revision
updated: 2026-07-22
policy_label: public-doc; fixtures; public-safe; synthetic; settlement; release-gated
tags: [kfm, fixtures, public-safe, synthetic, settlement, municipality, CensusPlace, Townsite, GhostTown, Fort, Mission, ReservationCommunity, evidence, sensitivity, rollback]
related:
  - ../README.md
  - ../../README.md
  - ../../domains/settlements-infrastructure/README.md
  - ../../../tests/fixtures/README.md
  - ../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/settlements.md
  - ../../../docs/domains/settlements-infrastructure/DENY_BY_DEFAULT.md
  - ../../../contracts/domains/settlements-infrastructure/place-identity.md
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md
  - ../../../schemas/contracts/v1/domains/settlement/README.md
notes:
  - "Evidence snapshot: repository main at commit 459b41d7ec91240742d8b2d3e5d9eb4dbd248df7 (2026-07-22)."
  - "The singular directory name `settlement` is a CONFIRMED shared public-safe fixture child, not a declaration of the canonical domain slug."
  - "The working domain slug is `settlements-infrastructure`; the singular schema lane is explicitly a draft compatibility index."
  - "This revision documents fixture posture only; it creates no payloads, schemas, validators, consumers, policy decisions, releases, or public routes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Public-safe settlement fixtures

> Small, deterministic, synthetic settlement examples that are safe to review and display. Fixtures exercise behavior; they never establish place truth, public eligibility, or release authority.

**Path:** `fixtures/public_safe/settlement/`  
**Role:** shared public-safe fixture sublane  
**Owning parent:** `fixtures/public_safe/`  
**Domain context:** Settlements/Infrastructure; the working domain slug is `settlements-infrastructure`  
**Exposure posture:** synthetic and public-safe by construction; never a public-data or release lane  
**Implementation posture:** README paths are CONFIRMED; payload inventory, consumers, validators, and CI coverage are NEEDS VERIFICATION  
**Evidence snapshot:** `main@459b41d7ec91240742d8b2d3e5d9eb4dbd248df7`

**Quick jumps:** [Purpose](#purpose) · [Fixture lane posture](#fixture-lane-posture) · [Placement basis](#placement-basis) · [Relationship to Settlements/Infrastructure governance](#relationship-to-settlementsinfrastructure-governance) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Shared fixture design rules](#shared-fixture-design-rules) · [Expected public-safe settlement fixture families](#expected-public-safe-settlement-fixture-families) · [Packaging pattern](#packaging-pattern) · [Maintenance notes](#maintenance-notes) · [Verification status](#verification-status) · [Rollback](#rollback)

---

## Purpose

Use this lane for reviewable examples of settlement-side behavior in documentation, renderer smoke checks, governed-API dry-runs, Evidence Drawer and Focus Mode examples, source-role and evidence-resolution checks, correction exercises, rollback exercises, and deterministic expected-output comparisons.

Candidate object families are `Settlement`, `Municipality`, `CensusPlace`, `Townsite`, `GhostTown`, `Fort`, `Mission`, and `ReservationCommunity`. These names come from draft Settlements/Infrastructure doctrine and the proposed place-identity contract. A fixture using a name does not prove that its schema, validator, route, policy bundle, renderer, or UI consumer exists.

## Fixture lane posture

This is a shared `public_safe` sublane. It is **not** the canonical fixture root for the Settlements/Infrastructure domain. The singular child name is retained because the parent fixture index confirms it as a public-safe lane; it must not be copied into contracts, schemas, data roots, or code as proof that `settlement` is the canonical domain slug.

Use `fixtures/domains/settlements-infrastructure/` when a fixture is clearly domain-owned and that lane's contract and consumers are established. At the evidence snapshot, that domain fixture README is only a greenfield stub. Migration is therefore a review decision, not an automatic move.

A file here is an example carrier only. It is never:

- municipal, census, historical, cultural, land, infrastructure, emergency, or jurisdictional truth;
- a `SourceDescriptor`, admitted source, `EvidenceBundle`, proof, policy decision, review approval, run receipt, or `ReleaseManifest`;
- a real public API response, map layer, tile, or published artifact;
- evidence that a validator, UI surface, policy engine, release gate, or CI workflow is implemented; or
- permission to expose real places, sensitive geometry, restricted joins, or community information.

## Placement basis

| Responsibility | Correct home | Boundary |
|---|---|---|
| Shared synthetic public-safe settlement examples | `fixtures/public_safe/settlement/` | This lane. |
| Parent public-safe fixture rules | `fixtures/public_safe/` | CONFIRMED parent index; it explicitly lists this child. |
| Cross-cutting runtime/synthetic fixtures | `fixtures/` | Root fixture conventions and inventory. |
| Domain-owned Settlements/Infrastructure fixtures | `fixtures/domains/settlements-infrastructure/` | CONFIRMED path, but greenfield stub at the snapshot. |
| Test-local fixtures | `tests/fixtures/` | Fixtures scoped to test implementations; do not duplicate shared authority here. |
| Semantic contracts | `contracts/domains/settlements-infrastructure/` | Proposed place identity and behavior. Fixtures do not define contracts. |
| Machine schemas | `schemas/contracts/v1/domains/settlements-infrastructure/` | Working broader schema lane. The singular `settlement/` path is a compatibility index, not confirmed canonical. |
| Policy and sensitivity decisions | `policy/` and governing domain registers | Fixtures illustrate outcomes; they do not decide disclosure. |
| Lifecycle data, evidence, receipts, proofs, and releases | Their governed roots | Never store those artifacts in this lane. |
| Golden expected outputs | `fixtures/golden/` or an accepted domain-owned golden lane | Pair by stable identifier; golden output is still not a release. |

`fixtures/` is for reusable operational examples. `tests/fixtures/` is for test-local material. Neither is a lifecycle `data/` stage, and neither becomes authoritative because a test passes.

## Relationship to Settlements/Infrastructure governance

| Lane or document | Status at snapshot | Relationship |
|---|---|---|
| `fixtures/public_safe/README.md` | CONFIRMED parent index | Defines the public-safe fixture boundary and lists `settlement/`. This corrects the prior README's stale “not found” claim. |
| `fixtures/domains/settlements-infrastructure/README.md` | CONFIRMED greenfield stub | Prospective home for clearly domain-owned fixtures; no mature fixture contract is inferred. |
| `docs/domains/settlements-infrastructure/CANONICAL_PATHS.md` | CONFIRMED draft doctrine | Uses `settlements-infrastructure` as the working slug and records singular-path conflict. |
| `docs/domains/settlements-infrastructure/sublanes/settlements.md` | CONFIRMED draft doctrine | Object families and source-authority distinctions for the settlement sublane. |
| `contracts/domains/settlements-infrastructure/place-identity.md` | CONFIRMED proposed contract | Identity distinctions and release/evidence posture; schema is noted as missing. |
| `docs/domains/settlements-infrastructure/DENY_BY_DEFAULT.md` | CONFIRMED draft register | Sensitivity and review posture; runtime enforcement is NEEDS VERIFICATION. |
| `schemas/contracts/v1/domains/settlement/README.md` | CONFIRMED compatibility index | Explicitly says the singular schema path is not confirmed canonical. |
| `schemas/contracts/v1/domains/settlements-infrastructure/README.md` | CONFIRMED minimal index | Broader working schema lane; schema coverage is not established by the README. |

No accepted ADR was located that changes this existing fixture placement. This documentation revision creates no new root, path alias, domain slug, or authority.

## Accepted material

This lane may contain small, human-reviewable examples such as:

- synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.svg`, or `*.md` files;
- invented place identities and deliberately generalized geometries with no claimed real-world referent;
- examples that keep `Municipality` distinct from `CensusPlace`, and historical/cultural place families distinct from current civil geography;
- positive and negative cases for evidence, citations, source roles, rights, sensitivity, review, correction, rollback, and release posture;
- deterministic renderer, drawer, Focus Mode, or governed-API examples; and
- references to paired expected outputs, when the consumer and comparison rule are documented.

Every payload should identify its scenario, synthetic posture, expected consumer, expected outcome, and governing contract or draft assumption. If a consumer is not implemented, label the example `PROPOSED` or `NEEDS VERIFICATION`.

## Exclusions

Do not place any of the following here:

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle data;
- copied source exports, live upstream payloads, or real municipal/legal/census/historical/tribal/community records;
- exact sensitive geometry, restricted cultural or archaeological locations, private person-land joins, ownership/title records, critical-infrastructure detail, or emergency-authority content;
- identifiers, names, coordinates, dates, URLs, or attributes selected from a real sensitive entity merely because other fields were changed;
- actual SourceDescriptors, EvidenceBundles, proofs, policy decisions, review approvals, receipts, release manifests, public responses, tiles, or generated CI artifacts;
- schemas, contracts, implementation code, validators, or authority-bearing policy text; or
- fixtures that silently rely on unresolved rights, consent, sovereignty, provenance, or sensitivity decisions.

If real or restricted material is discovered, stop using the file, remove it from public-safe consumers, route it through the governed quarantine/correction process, and record the correction. Do not “sanitize in place” without reviewing join and re-identification risk.

## Shared fixture design rules

### Construction

- Keep examples synthetic, compact, deterministic, diff-friendly, and understandable without private context.
- Use invented names, IDs, citations, digests, timestamps, source references, evidence references, reviewer references, policy references, and release references. Prefix or annotate toy values so they cannot be mistaken for repository artifacts.
- Use geometry created for the test scenario, not sampled from a real sensitive feature. Generalize it to the minimum precision the behavior needs.
- Pin ordering, serialization, coordinate precision, and timestamps when byte-for-byte comparison matters.
- State whether a fixture is valid, invalid, negative, expected, or golden. Never make the consumer infer intent from the filename alone.

### Semantic separation

- Preserve `Settlement`, `Municipality`, and `CensusPlace` as distinct object families even when a toy example shares a label.
- Preserve source role, evidence support, citation status, rights, sensitivity, review, release, correction, and rollback as separate fields or assertions.
- Keep historic uncertainty visible for `Townsite` and `GhostTown`; do not convert narrative ambiguity into a precise location or date.
- Treat `Fort` and `Mission` examples as potentially archaeological or culturally sensitive even when synthetic; negative cases should demonstrate withholding or generalization.
- Use only fictional `ReservationCommunity` examples. Never imitate a real tribal identifier, boundary, name, governance statement, or restricted community record. Include sovereignty and review posture in the scenario.
- Do not mix critical-infrastructure detail into settlement fixtures. Use the governed infrastructure fixture lane and stricter policy posture where appropriate.

### Trust-membrane behavior

- The fixture may test `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`; expected output must explain which missing or failed gate causes the outcome.
- “Public-safe fixture” describes the example's construction, not the eligibility of any analogous real record.
- An expected `ANSWER` remains synthetic and evidence-bound. It is not an approval for public release.
- Missing evidence, unresolved rights, sensitivity risk, invalid identity, or failed validation must remain visible. Do not fill gaps with plausible text.
- AI-generated explanatory text is interpretive output. Keep it traceable to the fixture's toy evidence and expected outcome.

## Expected public-safe settlement fixture families

These are PROPOSED scenario families, not a claim that matching payloads or consumers exist.

| Scenario family | Minimum fixture content | Expected posture |
|---|---|---|
| Synthetic `Settlement` | Toy identity, generalized geometry, toy source/evidence refs, explicit non-authority note | Reviewable `ANSWER` only when all toy gates pass. |
| `Municipality` vs `CensusPlace` | Two distinct identities, source roles, temporal scopes, and expected non-merge assertion | Preserve both families; invalid collapse produces `ERROR` or `ABSTAIN`. |
| `Townsite` or `GhostTown` | Toy historic citations, uncertainty, temporal scope, generalized location | `ANSWER` with visible uncertainty, or `ABSTAIN` when support is missing. |
| `Fort` or `Mission` sensitivity case | Synthetic site, cultural/archaeological review flag, public representation | Generalize or withhold; unresolved case produces `DENY` or `ABSTAIN`. |
| Fictional `ReservationCommunity` | Clearly fictional identity, sovereignty/review marker, no real boundary or identifier | Review-required; unresolved authority or consent produces `DENY`. |
| Missing evidence or invalid citation | Broken toy reference and explicit expected diagnostic | `ABSTAIN` or validation `ERROR`; never fabricated support. |
| Unresolved rights or sensitivity | Explicit unresolved gate and non-public expected result | `DENY` or governed review hold where an accepted policy defines it. |
| Correction or rollback | Prior toy digest, corrected digest, reason, reviewer, expected active version | Preserve lineage; restore last approved synthetic output. |
| Drawer or Focus Mode explanation | Toy evidence list, caveats, confidence/uncertainty, governed outcome | Cite-or-abstain; no new factual claims beyond toy inputs. |

## Packaging pattern

Use a small scenario bundle when more than one file is necessary. The following names are PROPOSED conventions, not confirmed current inventory:

```text
<scenario-id>/
├── README.md          # intent, synthetic posture, consumer, governing references
├── input.json         # toy input
├── expected.json      # deterministic expected result
└── negative.json      # optional fail-closed variant
```

The scenario README should include:

| Field | Requirement |
|---|---|
| Scenario ID | Stable, synthetic identifier. |
| Object family | One or more explicitly distinguished families. |
| Public-safe rationale | Why the example has no real sensitive referent and what generalization was applied. |
| Consumer | Test, renderer, UI surface, dry-run, or documentation page; `NEEDS VERIFICATION` if not implemented. |
| Governing references | Contract, schema, policy, or draft doctrine and its status. |
| Expected outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation result, or deterministic visual/output assertion. |
| Non-authority statement | Explicitly says the fixture is not source, evidence, policy, release, or real-world truth. |
| Correction path | How to withdraw, replace, or roll back the scenario. |

A generation note or generated-work receipt may document how a fixture was authored. It is not an EvidenceBundle, RunReceipt, policy decision, review approval, or release manifest.

## Maintenance notes

- Update this index when payloads, scenario directories, consumers, validators, helper scripts, expected-output rules, or the domain fixture lane become concrete.
- Link each stable fixture to its exact consumer and assertion. Orphaned examples should remain `NEEDS VERIFICATION`, not be described as tested.
- Prefer a domain-owned lane once ownership and contracts are established; preserve redirects or consumer updates when moving files.
- Change the input, expected output, scenario note, and consumer assertion together when behavior intentionally changes.
- Keep payloads small enough for ordinary code review unless a governed large-corpus storage decision exists.
- Review public safety again when combining fixtures: two harmless examples can create a sensitive join.
- Record corrections and supersession; do not silently rewrite a fixture that is used as a stable expected result.

## Verification status

Evidence was read at `main@459b41d7ec91240742d8b2d3e5d9eb4dbd248df7`.

| Check | Result | Evidence / limit |
|---|---|---|
| Target README | CONFIRMED | Existing blob `a6fcbb4f3cdde30ff2d6ba0d1fe6b3c1b7713765` was read before this revision. |
| Parent public-safe index | CONFIRMED | `fixtures/public_safe/README.md` exists and lists the settlement child. |
| Root fixture index | CONFIRMED | `fixtures/README.md` separates reusable fixtures, lifecycle data, artifacts, and test-local material. |
| Domain fixture lane | CONFIRMED greenfield stub | `fixtures/domains/settlements-infrastructure/README.md` exists but does not establish mature consumers or contracts. |
| Test-local fixture lane | CONFIRMED | `tests/fixtures/README.md` exists as a separate responsibility lane. |
| Working domain slug and singular-path conflict | CONFIRMED draft doctrine | Canonical-path and schema indexes prefer `settlements-infrastructure`; the singular schema path is a compatibility index. |
| Place-identity semantics | CONFIRMED proposed contract | Object families and release/evidence posture are documented; schema remains missing. |
| Payload inventory | NOT ESTABLISHED | A bounded repository review did not establish child payload files. This is not proof that none exist. |
| Consumers, validators, renderer checks, API checks, UI checks, and CI coverage | NEEDS VERIFICATION | No implementation claim is made by this README update. |
| Runtime policy and sensitivity enforcement | NEEDS VERIFICATION | Draft registers describe posture; enforcement was not established. |

For this README revision:

- [x] Corrected the stale claim that the parent public-safe README was missing.
- [x] Distinguished the shared singular fixture child from the working `settlements-infrastructure` domain slug.
- [x] Preserved source, evidence, policy, proof, release, and publication boundaries.
- [x] Added no fixture payload, schema, validator, contract, policy decision, runtime behavior, or public route.

Before adding or promoting payloads:

- [ ] Inventory current children and duplicate scenarios.
- [ ] Identify the exact consumer, schema/contract status, assertion, and CI path.
- [ ] Run deterministic valid, invalid, negative, correction, and rollback cases.
- [ ] Review synthetic identity, geometry, joins, rights, sensitivity, sovereignty, and cultural/archaeological posture.
- [ ] Confirm expected `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` behavior at the governed surface.
- [ ] Verify that no fixture is treated as real source data or release authority.

## Rollback

Before merge, abandon or delete the feature branch to restore the base state. After merge, revert the README commit; do not rewrite shared history. The immediately preceding target blob at the evidence snapshot is `a6fcbb4f3cdde30ff2d6ba0d1fe6b3c1b7713765`.

Rollback is mandatory if this lane acquires real or restricted data, authority-bearing artifacts, public API or tile outputs, canonical schema/contract ownership, or any shortcut around evidence, policy, review, and release gates.

<p align="right"><a href="#top">Back to top</a></p>
