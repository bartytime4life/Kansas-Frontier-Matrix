<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-people-dna-land-readme
title: configs/domains/people-dna-land/ — Governed People, DNA, and Land Configuration Boundary
type: readme
version: v0.4
status: draft; repository-grounded; README-only config lane; sensitive-domain; non-release; non-publication
owners: OWNER_TBD — Config steward · People/DNA/Land steward · Privacy/consent reviewer · Rights-holder/cultural-authority reviewer · Identity/land-evidence reviewer · Consumer owner · Policy-runtime owner · Validation steward
created: 2026-07-13
updated: 2026-09-04
policy_label: "public; config-sublane; people-dna-land; T4-default; living-person-aware; dna-restricted; consent-revocable; cultural-rights-aware; title-anti-collapse; finite-outcomes; non-secret; non-authoritative; no-live-binding"
current_path: configs/domains/people-dna-land/README.md
contract_version: "3.0.0"
owning_root: configs/
responsibility: Safe, non-secret, domain-scoped configuration documentation and future consumer-bound templates for People, Genealogy, DNA, and Land without owning identity, evidence, consent, policy, rights, sensitivity, title, release, or publication authority.
truth_posture: "CONFIRMED existing README-only config lane, parent domain-config contract v0.6, accepted Directory Rules v2 through ADR-0029, repository-present People/DNA/Land contracts-schemas-policy-fixtures-tests-validators-runbooks, two bounded synthetic consent profiles, and people-dna-land machine lane projection / PARTIAL bounded synthetic validation only / UNKNOWN executable config consumer, loader precedence, production policy binding, live consent/revocation service, source admission, release, deployment, promotion, and publication / NEEDS VERIFICATION compatibility topology for people versus people-dna-land and all positive operational claims"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 9e152476cda7bd9b80a2afac8031619a1898eceb
  prior_blob: 6b2d5c01278603a1686093d0b3ecddf933d60fd5
  bounded_review: target README; configs/domains parent; People-DNA-Land domain landing; accepted Directory Rules pointer; machine domain projection; People-DNA-Land validation and promotion runbooks; policy and consent surfaces
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/runbooks/people-dna-land/README.md
  - ../../../docs/runbooks/people-dna-land/VALIDATION_RUNBOOK.md
  - ../../../docs/runbooks/people-dna-land/PROMOTION_RUNBOOK.md
  - ../../../policy/domains/people-dna-land/README.md
  - ../../../policy/consent/people-dna-land/README.md
  - ../../../contracts/domains/people-dna-land/README.md
  - ../../../schemas/contracts/v1/domains/people-dna-land/README.md
  - ../../../fixtures/domains/people-dna-land/README.md
  - ../../../tests/domains/people-dna-land/README.md
  - ../../../tools/validators/domains/people-dna-land/README.md
  - ../../../control_plane/domain_lane_register.yaml
  - ../../../docs/security/SECRETS.md
notes:
  - "v0.4 replaces the July currentness snapshot with repository evidence available on 2026-09-04 while preserving deny-by-default sensitivity and no-authority boundaries."
  - "The directory remains README-only in the tracked tree. This change does not add a config payload or consumer binding."
  - "Two synthetic consent profiles and related hold-gate validation exist elsewhere in the repository; they do not prove production policy, consent, release, or publication behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed People, DNA, and Land Configuration Boundary

`configs/domains/people-dna-land/`

> Safe-to-commit configuration documentation for the People / Genealogy / DNA / Land lane. Configuration can select or parameterize an already-governed behavior for a verified consumer; it cannot manufacture identity, kinship, consent, cultural authority, land title, evidence, policy, review, release, or publication authority.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.4-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![sensitivity](https://img.shields.io/badge/sensitivity-T4__default-critical)
![validation](https://img.shields.io/badge/validation-bounded__synthetic-orange)
![secrets](https://img.shields.io/badge/secrets-forbidden-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Current evidence](#current-repository-evidence) · [Scope](#scope) · [Directory fit](#directory-rules-basis) · [Sensitive defaults](#sensitive-domain-defaults) · [Policy boundary](#policy-and-consent-boundary) · [Consumer contract](#future-consumer-contract) · [Validation](#validation) · [Failure behavior](#failure-behavior) · [AI](#governed-ai) · [Related](#related-surfaces) · [Rollback](#rollback-and-correction)

> [!IMPORTANT]
> **Observed lane maturity:** tracked `configs/domains/people-dna-land/` remains README-only at the pinned base. Repository-present contracts, schemas, policy, fixtures, tests, validators, and runbooks exist in their own responsibility roots, but no executable configuration payload or config consumer is established by this lane.

> [!CAUTION]
> **Living-person information, raw DNA, DNA-derived relationship hypotheses involving living people, and private person-parcel joins remain deny-by-default / T4-sensitive.** Consent can be a necessary gate, but it is never sufficient by itself. Unknown living status, rights, source role, consent state, cultural authority, sensitivity, title basis, review state, or release state fails closed.

---

## Purpose

This directory is the domain-scoped configuration sublane for People, Genealogy, DNA, and Land. Its job is deliberately narrow: make safe configuration expectations inspectable without turning configuration into a trust authority.

A future consumer-bound file here may select an accepted profile, set a conservative threshold, choose a display mode, or expose a safe default. It must not decide:

- whether two records represent the same person;
- whether a person is living, deceased, a minor, protected, or safe to expose;
- whether a kinship, genealogy, migration, residence, occupancy, ownership, or title assertion is true;
- whether DNA establishes identity, parentage, ancestry, citizenship, cultural membership, health, or legal status;
- whether consent exists, covers a purpose, remains valid, or survives revocation;
- whether a tribal nation, family, descendant community, rights holder, institution, or cultural authority permits use;
- whether a source is admissible, current, authoritative, redistributable, or active;
- whether assessor or tax records establish title;
- whether parcel geometry proves a legal boundary; or
- whether evidence, policy, review, release, promotion, or publication gates are satisfied.

[Back to top](#top)

---

## Authority level

**Implementation-supporting configuration only; non-authoritative for truth and governance.**

| Concern | This lane may do | This lane must not do |
|---|---|---|
| Domain behavior | Expose safe defaults for a named consumer | Define domain truth or object meaning |
| Identity and genealogy | Reference an accepted review/profile identifier | Merge people or declare a relationship true |
| DNA | Select an already-governed public-safe presentation profile | Store raw genotypes, segments, vendor IDs, or inferential truth |
| Consent | Reference a verified consent-policy/profile identifier | Create credentials, approvals, revocations, or consent truth |
| Cultural authority | Carry a required-review selector | Grant permission or replace consultation |
| Land | Select a public-safe display/generalization profile | Establish ownership, title, survey truth, or legal boundary |
| Policy | Identify an accepted policy profile/evaluator | Embed policy authority or forge a `PolicyDecision` |
| Evidence and release | Preserve references required by a consumer | Create EvidenceBundles, review approval, release, or publication state |

Parsing a config file never upgrades its authority.

[Back to top](#top)

---

## Current repository evidence

The July v0.3 README understated current repository maturity outside this config directory. The safe current picture is:

| Surface | Current bounded result | What it proves |
|---|---:|---|
| `configs/domains/people-dna-land/` | **CONFIRMED README-only** | The config boundary exists; no tracked executable config payload is present. |
| Parent domain config README | **CONFIRMED v0.6** | Domain config is non-secret, non-authoritative, inactive by default, and consumer-bound when implemented. |
| Accepted Directory Rules | **CONFIRMED through ADR-0029** | `configs/` owns configuration responsibility; domain files remain beneath responsibility roots rather than becoming roots themselves. |
| Domain landing docs | **CONFIRMED repository-present** | The lane documents assertion-first identity, T4 defaults, consent/revocation, cultural-rights review, title anti-collapse, and compatibility uncertainty. |
| Contracts / schemas / policy | **CONFIRMED repository-present / mixed maturity** | These roots contain People/DNA/Land surfaces; presence is not production activation. |
| Fixtures / tests / validators | **CONFIRMED bounded implementation** | Synthetic proof surfaces exist outside `configs/`. |
| Domain workflow and validation runbook | **CONFIRMED bounded hold gate** | Two synthetic consent profiles and static boundary checks are exercised; broader semantics and production behavior are not proved. |
| Promotion / rollback runbooks | **CONFIRMED HOLD boundaries** | Operational promotion and complete rollback remain unavailable or unproved. |
| Machine domain projection | **CONFIRMED present / projection only** | `people-dna-land` is projected as a registered lane; the register does not create policy or publication authority. |
| Live config consumer | **UNKNOWN** | No loader, precedence, binding, or production consumption is established here. |

### Compatibility topology remains unsettled

Current repository evidence contains both `people-dna-land` paths and narrower `people` compatibility/registry guardrails in some responsibility roots. This README uses the existing canonical config path `configs/domains/people-dna-land/` and does not create aliases, mirrors, fallback lookup rules, or migration behavior.

Any rename, alias, split, or migration needs its own accepted authority and compatibility plan.

[Back to top](#top)

---

## Scope

### What belongs here

Only safe, non-secret configuration documentation or future **named-consumer** payloads such as:

- this `README.md`;
- placeholder-only templates;
- tiny, unmistakably synthetic examples;
- deny/abstain/hold/review/stale/disabled defaults;
- selectors for accepted privacy, consent-verification, aggregation, identity-review, cultural-review, land-display, redaction, or public-safe profiles;
- presentation hints for evidence state, source role, uncertainty, review state, consent state, correction, and supersession;
- migration notes for a verified consumer; and
- documented validation commands whose behavior has actually been verified.

### What does not belong here

Do not store:

- real people, minors, protected persons, private contact information, addresses, relationships, or identifiers;
- GEDCOM/GEDZip, obituary, vital, court, probate, cemetery, church, school, military, directory, or vendor exports containing real people;
- genotype files, chromosome segments, centimorgan values, haplotypes, kit IDs, match lists, triangulation outputs, genetic-health data, or ancestry inference;
- consent credentials, revocation records, identity documents, access tokens, private keys, or rights-holder decisions;
- deeds, patents, titles, mortgages, liens, easements, leases, legal descriptions, private parcel joins, or title-chain evidence;
- exact or reconstructable protected person-place, family, DNA, cultural, tribal, burial, or private-land joins;
- source payloads, lifecycle records, EvidenceBundles, receipts, proofs, release manifests, or publication decisions;
- schemas, semantic contracts, policy rules, source registries, pipelines, runtime code, or application implementation; or
- secrets, signed URLs, private endpoints, cookies, workstation paths, or deployment credentials.

Synthetic examples must be clearly impossible to confuse with real records.

[Back to top](#top)

---

## Directory Rules basis

Accepted ADR-0029 makes the current Directory Rules the placement authority. The responsibility here is configuration, so the existing path is correct:

```text
configs/
└── domains/
    └── people-dna-land/
        └── README.md
```

Responsibility remains separated:

| Responsibility | Owning surface |
|---|---|
| Human domain explanation | `docs/domains/people-dna-land/` |
| Operational procedures | `docs/runbooks/people-dna-land/` |
| Semantic meaning | `contracts/domains/people-dna-land/` |
| Machine shape | `schemas/contracts/v1/domains/people-dna-land/` |
| Admissibility | `policy/domains/people-dna-land/` and governed consent policy surfaces |
| Synthetic proof | `fixtures/`, `tests/`, and `tools/validators/` domain lanes |
| Source identity/admission | governed registry and connector surfaces |
| Lifecycle / evidence / release | canonical data, proof, catalog, release, and publication surfaces |
| Safe consumer configuration | `configs/domains/people-dna-land/` |

Public clients do not gain authority by reading configuration. Public behavior must flow through governed APIs and released public-safe artifacts.

[Back to top](#top)

---

## Sensitive domain defaults

### Identity and genealogy

- Person assertions remain evidence-bearing assertions, not automatic facts.
- Similar names, shared addresses, shared parcels, household co-occurrence, graph proximity, or model confidence must not silently merge identities.
- Ambiguity returns review, `ABSTAIN`, `DENY`, or `ERROR` as appropriate; it does not become a permissive default.
- Deceased status does not automatically make every associated relationship, address, DNA implication, or land record public.

### DNA

- Raw DNA and vendor-derived identifiers are restricted inputs, not public configuration values.
- DNA-supported relationships remain hypotheses until evidence and review support a bounded claim.
- Public derivatives require explicit policy, rights, sensitivity, review, release, and anti-reidentification controls.
- Configuration cannot lower k-anonymity, aggregation, redaction, or disclosure thresholds below an accepted policy floor.

### Consent, revocation, and cultural authority

- Consent is scoped, purpose-bound, time-aware, and revocable where policy requires it.
- Revocation must propagate through governed correction/tombstone/cleanup behavior; a config reload is not revocation handling.
- Cultural authority and Indigenous/community governance are independent from individual consent and must not be synthesized from ancestry, DNA, surname, geography, or model output.

### Land and title

- Assessor and tax records are administrative evidence, not title truth.
- Parcel geometry is a representation, not legal boundary proof.
- Ownership and occupancy are time-bounded assertions.
- Deeds, patents, probate records, surveys, court orders, leases, liens, easements, mineral/water/access rights, and title instruments retain distinct source roles.
- Configuration cannot resolve a title conflict or select a legal winner.

[Back to top](#top)

---

## Policy and consent boundary

A future consequential consumer must keep configuration downstream of policy authority:

```text
validated config selector
        ↓
explicit policy input
        ↓
accepted policy bundle + governed evaluator
        ↓
canonical decision
ANSWER | ABSTAIN | DENY | ERROR
        ↓
caller enforces every obligation
        ↓
independent evidence + rights + sensitivity + review + release gates
```

Rules:

- Config may reference a verified profile or evaluator identifier; it may not embed consent credentials or policy decisions.
- Missing policy context must remain missing and fail closed.
- Engine-native values such as `ALLOW`, `RESTRICT`, or `HOLD` are not automatically KFM runtime outcomes.
- Reasons and obligations must survive normalization.
- A caller unable to understand every obligation must deny or error.
- `ANSWER` is not proof of evidence closure, consent validity, release approval, or publication readiness.
- Synthetic consent-profile tests are evidence of those bounded fixtures only; they do not establish a production consent service.

[Back to top](#top)

---

## Future consumer contract

No executable config payload should be added until a change identifies a concrete consumer and closes the minimum interface below.

| Required field or behavior | Minimum requirement |
|---|---|
| Consumer identity | Exact package/app/pipeline/tool path and owner |
| File path | Explicit; no implicit directory auto-discovery unless separately verified |
| Schema | Versioned machine validation before use |
| Precedence | Deterministic defaults/overrides order |
| Unknown keys | Fail or warn according to a documented compatibility rule; never silently change sensitive behavior |
| Sensitive defaults | Deny/restrict by default |
| Policy binding | Explicit accepted profile/evaluator reference; config cannot contain policy logic |
| Source role | Preserve source-role distinctions |
| Time | Preserve material temporal scope and freshness where relevant |
| Evidence | Require evidence references for consequential output; config is never evidence |
| Audit | Record effective config digest/version in the consuming operation when behavior is consequential |
| Rollback | Prior known-good config and compatibility path identified |

A generic `people.yaml` added without a verified consumer would be ambiguous and should remain **PROPOSED**, not operational.

[Back to top](#top)

---

## Validation

### Confirmed bounded validation elsewhere in the lane

Current People/DNA/Land validation documentation reports a bounded executable hold gate that runs **two synthetic consent profiles** plus static boundary checks. That is useful implementation evidence for those fixtures and checks only.

It does **not** prove:

- a live config loader;
- generic config schema validation;
- production policy evaluation;
- real consent issuance or revocation;
- identity resolution;
- DNA inference safety;
- title-chain reasoning;
- source admission;
- release, deployment, promotion, or publication.

### Validation required for a future config payload

A future payload should minimally prove:

1. exact consumer and file binding;
2. parser/schema acceptance of a valid synthetic fixture;
3. rejection of unknown or malformed sensitive settings;
4. deny-by-default behavior when values are absent;
5. deterministic precedence and config digesting;
6. no secret or real-person fixture content;
7. policy obligations cannot be disabled by config;
8. redaction/aggregation/public-safe floors cannot be weakened below accepted policy;
9. no network or external write occurs merely from parsing config; and
10. rollback to the previous valid config is deterministic.

[Back to top](#top)

---

## Failure behavior

| Failure | Required posture |
|---|---|
| Config missing | Use a verified conservative built-in default or fail closed; never silently enable sensitive behavior |
| Parse/schema error | `ERROR`; do not partially apply |
| Unknown sensitive key | `ERROR` or explicit rejection |
| Unknown living/consent/rights/sensitivity state | `DENY` or governed review hold |
| Policy evaluator unavailable | `ERROR` or `DENY` according to the accepted caller contract |
| Evidence unresolved | `ABSTAIN` or `DENY`; never infer from config |
| Required obligation unsupported | `DENY` or `ERROR` |
| Consumer/config version mismatch | Refuse activation and retain prior known-good behavior |
| Public-safe transform missing | `DENY` public exposure |

Fail-safe behavior is part of the config contract, not an optional operational convenience.

[Back to top](#top)

---

## Governed AI

AI may explain an already-governed configuration choice or summarize released evidence. It must not:

- infer identity from ambiguous records;
- turn DNA similarity into authoritative kinship;
- infer living status, consent, tribal/cultural membership, title, or legal ownership;
- reconstruct redacted person-place or DNA information;
- bypass configured or policy-required denial because a model is confident; or
- convert a map, graph, search result, family tree, parcel layer, or generated narrative into root truth.

Evidence and policy outrank generated language. If support is insufficient, the correct result is bounded abstention or denial.

[Back to top](#top)

---

## Related surfaces

| Surface | Role |
|---|---|
| [`../README.md`](../README.md) | Parent domain-config contract and inventory |
| [`../../../docs/domains/people-dna-land/README.md`](../../../docs/domains/people-dna-land/README.md) | Domain scope, current maturity, sensitivity posture, and compatibility notes |
| [`../../../docs/runbooks/people-dna-land/README.md`](../../../docs/runbooks/people-dna-land/README.md) | Operational procedures and explicit HOLD boundaries |
| [`../../../docs/runbooks/people-dna-land/VALIDATION_RUNBOOK.md`](../../../docs/runbooks/people-dna-land/VALIDATION_RUNBOOK.md) | Bounded validation evidence and limits |
| [`../../../docs/runbooks/people-dna-land/PROMOTION_RUNBOOK.md`](../../../docs/runbooks/people-dna-land/PROMOTION_RUNBOOK.md) | Promotion prerequisites and current unavailability |
| [`../../../policy/domains/people-dna-land/README.md`](../../../policy/domains/people-dna-land/README.md) | Domain policy responsibility |
| [`../../../policy/consent/people-dna-land/README.md`](../../../policy/consent/people-dna-land/README.md) | Consent-policy boundary and compatibility posture |
| [`../../../contracts/domains/people-dna-land/README.md`](../../../contracts/domains/people-dna-land/README.md) | Semantic contracts |
| [`../../../schemas/contracts/v1/domains/people-dna-land/README.md`](../../../schemas/contracts/v1/domains/people-dna-land/README.md) | Machine shape |
| [`../../../fixtures/domains/people-dna-land/README.md`](../../../fixtures/domains/people-dna-land/README.md) | Synthetic fixtures |
| [`../../../tests/domains/people-dna-land/README.md`](../../../tests/domains/people-dna-land/README.md) | Domain test boundary |
| [`../../../tools/validators/domains/people-dna-land/README.md`](../../../tools/validators/domains/people-dna-land/README.md) | Validator boundary |
| [`../../../control_plane/domain_lane_register.yaml`](../../../control_plane/domain_lane_register.yaml) | Machine lane projection only |
| [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | Adopted directory-governance bytes |
| [`../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Directory Rules adoption record |

[Back to top](#top)

---

## Rollback and correction

This README changes documentation only. It does not activate a source, consent service, policy evaluator, config loader, release path, or public artifact.

For a future config payload:

1. preserve the prior validated config and its digest;
2. reject incompatible consumer/config combinations before activation;
3. make rollback deterministic and auditable;
4. propagate corrections and revocations through the owning lifecycle systems rather than editing config as a substitute; and
5. never rewrite historical receipts or evidence to make the rollback appear cleaner than it was.

If this README is found to misstate repository reality, correct it through a focused reviewed change. Documentation may be reverted; evidence and governance history should remain inspectable.

---

## Last reviewed

`2026-09-04` against `main@9e152476cda7bd9b80a2afac8031619a1898eceb`.

**Current safe conclusion:** the configuration lane is real and README-only; the wider People/DNA/Land domain now has bounded synthetic consent validation and substantial repository structure, but operational configuration consumption, live policy/consent behavior, source admission, release, deployment, promotion, and publication remain unproved.

[Back to top](#top)
