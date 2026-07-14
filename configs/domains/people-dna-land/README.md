<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-people-dna-land-readme
title: configs/domains/people-dna-land/ — People, DNA, and Land Configuration Boundary
type: readme
version: v0.3
status: draft
owners: OWNER_TBD — Config steward · People/DNA/Land steward · Privacy/consent reviewer · Rights-holder/cultural-authority reviewer · Identity/land-evidence reviewer · Consumer owner · Policy-runtime owner · Validation steward
created: 2026-07-13
updated: 2026-07-14
policy_label: "public; config-sublane; people-dna-land; T4-default; living-person-aware; dna-restricted; consent-revocable; cultural-rights-aware; title-anti-collapse; policy-interface-aware; finite-outcomes; non-secret; non-authoritative; no-live-binding"
current_path: configs/domains/people-dna-land/README.md
truth_posture: CONFIRMED repository-present config lane, parent config contract v0.4, People/Genealogy/DNA/Land doctrine, restricted-domain consent README, PolicyInputBundle and PolicyDecision semantic contracts, paired policy schemas, canonical ANSWER-ABSTAIN-DENY-ERROR outcomes, policy-runtime 0.0.0 placeholder, TODO-only policy workflow, assertion-first identity, living-person T4 default, raw-DNA T4 no-public-transform rule, private person-parcel T4 default, assessor-not-title rule, parcel-not-boundary-proof rule, and README-only target maturity / CONFLICTED people versus people-dna-land segment naming, top-level versus domain-nested consent placement, and engine-native versus canonical decision vocabulary / PROPOSED future named-consumer templates and accepted profile selectors / UNKNOWN executable config consumers, loader precedence, evaluator binding, runtime enforcement, deployment integration, and publication behavior / NEEDS VERIFICATION accepted owners, substantive validators and CI, consent credential and revocation services, obligation interpreter, identity methods, aggregation parameters, cultural-authority requirements, title-chain methods, and public-safe geometry parameters
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 14b59b6b84ee2b9fa46e002b60e922c97cab2761
  prior_blob: 5211ca305ed153df618060f118932a4dca548ea0
  bounded_review: target README; parent domain-config README; People-DNA-Land doctrine; restricted-domain consent README; policy input and decision contracts/schemas; policy-runtime placeholder; policy-test workflow; Directory Rules; domain, drift, and verification registers
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../policy/consent/people-dna-land/README.md
  - ../../../contracts/policy/policy_input_bundle.md
  - ../../../contracts/policy/policy_decision.md
  - ../../../schemas/contracts/v1/policy/policy_input_bundle.schema.json
  - ../../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../../packages/policy-runtime/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
  - ../../../.github/workflows/policy-test.yml
notes:
  - "This lane contains README documentation only in the bounded target-path review. No executable People/DNA/Land config payload, consumer, loader, identity resolver, person linker, DNA processor, consent evaluator, title resolver, source activation, network fetch, or publication binding is established."
  - "v0.3 preserves the v0.2 sensitivity, identity, genealogy, DNA, consent, cultural-rights, title, privacy, validation, correction, and rollback boundaries while grounding the policy interface in repository-present contracts and schemas."
  - "A bounded review cannot prove that no differently named or unindexed consumer exists."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People, DNA, and Land Domain Configuration

`configs/domains/people-dna-land/`

> Safe-to-commit, named-consumer configuration documentation and future templates for the People / Genealogy / DNA / Land lane. Configuration may select an already-governed profile; it cannot create identity, kinship, DNA interpretation, consent, cultural authority, title, privacy policy, evidence, release, or publication authority.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.3-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![sensitivity](https://img.shields.io/badge/sensitivity-T4__default-critical)
![policy interface](https://img.shields.io/badge/policy__interface-explicit-0a7ea4)
![outcomes](https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-0b7285)
![secrets](https://img.shields.io/badge/secrets-forbidden-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status-and-evidence) · [Scope](#scope) · [Repository fit](#repository-fit) · [Policy interface](#policy-interface-and-outcome-normalization) · [Domain guardrails](#domain-guardrails) · [File contract](#minimum-configuration-contract) · [Validation](#validation) · [Failures](#failure-behavior) · [AI](#governed-ai-and-generated-language) · [Maintenance](#maintenance-and-change-budget) · [Done](#definition-of-done-for-the-first-payload) · [Related](#related-authority-surfaces) · [ADRs](#adrs-and-drift-triggers) · [Rollback](#rollback-correction-and-revocation)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.3`
> **Observed maturity:** README-only in the bounded target-path review
> **Authority:** implementation-supporting configuration sublane; non-authoritative for truth and governance
> **Runtime posture:** directory presence activates nothing

> [!CAUTION]
> **Living-person fields, raw DNA data, DNA-derived relationship hypotheses involving living people, and private person–parcel joins default to T4 denial.** Consent is necessary where policy requires it but never sufficient. Configuration cannot create a consent credential, `PolicyInputBundle`, `PolicyDecision`, evidence closure, rights clearance, sensitivity clearance, review approval, release approval, or publication state.

---

## Purpose

This directory is the safe-to-commit configuration boundary for the canonical People, Genealogy, DNA, and Land Ownership lane.

A future file may describe how a **named, verified consumer** parses, validates, renders, or selects already-governed material. It cannot decide:

- whether two records identify the same person;
- whether a person is living, deceased, a minor, protected, or safe to expose;
- whether an event, residence, migration, relationship, occupancy, ownership, or title assertion is true;
- whether DNA establishes identity, kinship, ancestry, parentage, health, citizenship, or cultural membership;
- whether consent exists, covers the requested purpose, remains current, or survives revocation;
- whether a rights holder, tribal nation, family, descendant community, institution, or cultural authority authorizes use;
- whether a source is admissible, authoritative, redistributable, or active;
- whether assessor/tax records establish ownership or title;
- whether parcel geometry proves a legal boundary;
- which deed, patent, probate record, survey, lease, lien, easement, title instrument, or court order controls;
- whether evidence supports a claim; or
- whether an artifact may be promoted, released, or published.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Domain meaning | None. Human doctrine remains under `docs/domains/people-dna-land/`. |
| Identity, living status, events, kinship, DNA | None. Configuration may reference accepted profiles only. |
| Consent and revocation | None. Policy and governed evaluator surfaces decide a scoped consent gate. |
| Cultural authority and sovereignty | None. Configuration cannot grant permission or replace consultation. |
| Ownership, title, legal boundary | None. Administrative records and GIS geometry remain context, not legal proof. |
| Source identity, role, rights, activation | None. Registry, connector, rights, and policy surfaces retain authority. |
| Contract meaning / machine shape | None. `contracts/` owns meaning; `schemas/` owns shape. |
| Policy admissibility | None. `policy/` owns rules; config cannot forge policy inputs or decisions. |
| Evidence, review, release, publication | None. Independent trust and release surfaces retain authority. |
| Consumer behavior | Supporting only after explicit binding, validation, precedence, and fail-closed behavior are verified. |

A config value may point to authority. Parsing, repetition, proximity, operational convenience, or use by a map, graph, family tree, search index, export, Evidence Drawer, Focus Mode, or AI surface does not make it authoritative.

[Back to top](#top)

---

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| Target README | **CONFIRMED** | This configuration lane exists. |
| Parent config contract | **CONFIRMED** | `configs/domains/README.md` defines domain config as non-secret, non-authoritative, and inactive by default. |
| Domain doctrine | **CONFIRMED repository-present** | Assertion-first identity, T4 defaults, revocable consent, cultural-rights review, and title anti-collapse are documented. |
| Restricted-domain consent README | **CONFIRMED DRAFT DOCS** | Consent is one scoped gate; placement and executable enforcement remain unresolved. |
| `PolicyInputBundle` contract/schema | **CONFIRMED / PLACEHOLDER SHAPE** | Semantic contract exists; paired schema requires only `id` and permits additional properties. |
| `PolicyDecision` contract/schema | **CONFIRMED / PROPOSED SHAPE** | Canonical outcome enum is `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`; `policy_family` includes `consent`. |
| Policy runtime package | **CONFIRMED PLACEHOLDER** | Package metadata is version `0.0.0`; behavior is unproved. |
| Policy workflow | **CONFIRMED TODO-ONLY** | Jobs echo TODO and do not prove policy behavior or fixture coverage. |
| Target-lane payload/consumer | **NOT ESTABLISHED IN BOUNDED REVIEW** | No executable payload, loader, evaluator, or binding is established by this README. |
| Segment naming | **CONFLICTED** | `people` versus `people-dna-land` remains unresolved for some authority roots. |
| Consent-policy placement | **CONFLICTED** | Top-level and domain-nested placement remains an ADR question. |
| Runtime/release/publication | **UNKNOWN / NOT AUTHORIZED** | Nothing here proves operational use or public safety. |

The repository evidence supports a **documented interface**, not operational enforcement.

[Back to top](#top)

---

## Scope

### What belongs here

Only safe, non-secret configuration for a named or explicitly proposed consumer:

- this boundary `README.md`;
- placeholder-only `*.template.yaml` / `*.template.yml`;
- tiny unmistakably synthetic `*.example.yaml`, `*.example.json`, or `*.example.toml`;
- conservative deny, abstain, hold, review, tombstone, disabled, stale, or unavailable defaults;
- selectors for already-governed privacy, consent-verification, redaction, aggregation, identity-review, cultural-review, land-display, or public-safe profiles;
- presentation hints for source role, assertion state, evidence, time, confidence, uncertainty, consent status, policy state, correction, and supersession;
- time-bounded migration and compatibility notes;
- validation documentation whose commands and enforcement are verified or explicitly labeled.

### What does not belong here

- real people, minors, protected persons, contact data, addresses, dates, relationships, residences, or private identifiers;
- real genealogy, GEDCOM/GEDZip, obituary, vital, court, probate, church, cemetery, directory, school, military, or vendor exports;
- genotype files, segments, chromosome coordinates, centimorgan values, haplotypes, kit/account IDs, match lists, triangulation outputs, genetic-health or ancestry inference;
- consent credentials/tokens, revocation records, identity documents, private keys, access approvals, or rights-holder decisions;
- real deeds, patents, titles, mortgages, liens, easements, leases, probate instruments, surveys, plats, legal descriptions, parcels, ownership, water/mineral/access rights;
- exact or reconstructable person–parcel, person–place, family, DNA, cultural, tribal, burial, or title joins;
- credentials, cookies, signed URLs, private endpoints, workstation paths, or deployment secrets;
- source activation, schemas, contracts, policy rules, registries, lifecycle data, receipts, proofs, EvidenceBundles, review records, release records, corrections, or publication decisions;
- package, pipeline, connector, watcher, identity-resolution, DNA-processing, policy-evaluation, title-reasoning, runtime, application, infrastructure, cache, index, export, screenshot, or report implementation.

Synthetic examples must be impossible to confuse with real records.

[Back to top](#top)

---

## Repository fit

```text
configs/
└── domains/
    └── people-dna-land/
        └── README.md
```

Directory Rules basis: the primary responsibility is safe, non-secret configuration, so `configs/` owns this file. Domain meaning stays in `docs/` and contracts; shape in `schemas/`; admissibility in `policy/`; source identity/rights/activation in registry and connector governance; implementation in implementation roots; lifecycle and trust artifacts in canonical `data/`/`release/` homes.

This README uses the confirmed current slug `people-dna-land`. It does not create `people` aliases, fallback searches, duplicate files, symlinks, or implicit precedence.

Public clients must not read this directory. They consume released artifacts through governed interfaces.

[Back to top](#top)

---

## Policy interface and outcome normalization

A future consumer that performs a consequential render, answer, export, join, derivative, restricted query, or release-adjacent operation must not treat configuration as a policy decision.

```text
validated config selector
        |
        v
explicit PolicyInputBundle
        |
        v
accepted policy bundle + governed evaluator
        |
        v
engine-native result
        |
        v
accepted normalization
        |
        v
PolicyDecision
  outcome: ANSWER | ABSTAIN | DENY | ERROR
  reasons: [...]
  obligations: [...]
        |
        v
caller enforces every obligation
        |
        v
independent evidence + rights + sensitivity + review + release gates
```

### Required boundaries

- Config may reference a verified policy/evaluator/profile identifier; it cannot embed policy rules, consent credentials, `PolicyInputBundle`, or `PolicyDecision` instances.
- Policy input must explicitly identify operation, audience, object/release refs, evidence state, source role, rights, sensitivity, living/protected state, consent context, review state, release state, evaluator identity/version/hash, and unresolved fields.
- Missing context must be represented as unresolved and fail closed; policy evaluation must not perform hidden fetches.
- Engine-native `ALLOW`, `RESTRICT`, `HOLD`, or equivalent values are **not** public/runtime outcomes.
- Normalization to `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` requires accepted, versioned mapping.
- Reasons and obligations must be preserved.
- A caller that cannot understand or enforce every obligation must return `DENY` or `ERROR`.
- `ANSWER` means only that the evaluated policy gate permits the requested operation subject to obligations. It is not evidence closure, consent proof, release approval, or publication.
- Consent is one independent policy family. Rights, sensitivity, source role, evidence, review, release, correction, and rollback gates still run.

### Current limitations

The policy-input schema is permissive; the runtime package is `0.0.0`; the policy workflow is TODO-only; target-lane executable config, evaluator binding, reason-code registry, obligation interpreter, receipt emission, and cache invalidation are unproved.

[Back to top](#top)

---

## Domain guardrails

### Identity, assertions, and relationships

- Person assertions are evidence-bearing records, not facts.
- A `PersonCanonical` projection is derived and must retain contributing assertions, conflicts, decisions, review, and correction lineage.
- Name similarity, shared address/parcel/household/event, first-match selection, or model confidence cannot silently merge people.
- Ambiguous identity or relationship returns `ABSTAIN`, `DENY`, or review hold.
- Source-documented relationships, user-contributed trees, DNA-supported hypotheses, model/graph candidates, reviewer-confirmed assertions, and disputed relationships remain distinct.
- Unknown living status fails closed; deceased status does not automatically make associated data public.
- Minors, protected persons, adoption, donor conception, guardianship, sealed records, victims, and similar contexts require specialized policy/review.

### DNA, consent, and revocation

Raw genotype, segments, coordinates, centimorgan values, haplotypes, vendor IDs, match lists, triangulation data, research participant IDs, download URLs, authentication material, and correlatable pseudonyms are forbidden in config, examples, logs, telemetry, caches, indexes, screenshots, and public artifacts.

A DNA match is not verified kinship; shared DNA is not parentage; ethnicity estimates are not ancestry facts; raw DNA has no public-transform path.

Consent must be purpose-, subject/holder-, controller/processor-, operation-, audience-, field/relation-, precision-, recipient-, environment-, jurisdiction-, start/expiry-, retention-, onward-transfer-, research-, revocation-, dispute-, and audit-bound. Upload, account creation, public availability, family relationship, or prior narrow consent does not imply broader consent.

Valid revocation/suspension requires accepted stop-use, access denial, tombstone, derivative discovery, cache/index invalidation, withdrawal/supersession, notification, correction, and verification steps. Configuration cannot delay or reinterpret it.

### Land, title, boundary, and cultural rights

Assessor and tax records are administrative context, not ownership or title. Parcel geometry, centroids, maps, tiles, and overlays are not surveys, legal descriptions, monuments, adjudicated boundaries, or title-insurance conclusions.

Instrument classes, jurisdiction, recording/effective time, gaps, overlaps, conflicts, supersession, unresolved descriptions, uncertain party identity, and source limitations must remain visible. Config cannot choose a controlling instrument or fill a chain-of-title gap.

Private person–parcel joins default to T4 denial.

Archival/public-record availability does not waive cultural, Indigenous, tribal, family, descendant-community, cemetery, burial, sovereignty, or rights-holder authority. Config cannot infer tribal citizenship, descent, clan, membership, or culturally restricted relationships/places.

### Time, joins, and reconstruction risk

Keep asserted/event, valid/effective, recorded/source, retrieval, processing, policy-evaluation, release, correction, revocation, and supersession times distinct where material.

Every cross-lane join may increase sensitivity. Review low counts, sparse geography, narrow dates, rare names, family clusters, repeated queries, differencing across releases, map zoom, graph traversal, cross-domain joins, public-record enrichment, parcel/address linkage, deceased-to-living inference, and cached/exported copies.

Client-side hiding, opacity, coarse default zoom, obscure URLs, hashing alone, pseudonyms, disclaimers, or removal of direct identifiers are not sufficient privacy controls.

[Back to top](#top)

---

## Minimum configuration contract

Every future non-README payload must document or encode:

1. stable config ID, version, status, supersession, and rollback target;
2. exact consumer path, owner, bounded purpose, and prohibited purposes;
3. format/parser version, explicit load mechanism, and no auto-discovery;
4. deterministic precedence, missing-file, duplicate-key, unknown-key, and unsupported-version behavior;
5. canonical contract, schema, policy, registry, doctrine, and validation references;
6. source IDs/roles/rights/retention/activation assumptions;
7. assertion/candidate/canonical/source distinctions;
8. living/deceased/minor/protected/unknown/disputed handling;
9. identity ambiguity and relationship hypothesis behavior;
10. DNA class and raw-ID/segment prohibition;
11. consent purpose, scope, audience, operation, expiry, verifier, revocation, dispute, and third-party effects;
12. cultural/tribal/rights-holder review profile;
13. land-record class, jurisdiction, instrument role, title/boundary disclaimers, gaps/conflicts, and temporal scope;
14. accepted privacy, aggregation, generalization, redaction, and public-safe profile refs;
15. explicit policy-input assembly and accepted evaluator/bundle refs;
16. canonical outcome normalization, reason handling, and obligation enforcement;
17. privacy-safe logging, telemetry, cache, index, screenshot, support, and export behavior;
18. deterministic no-network/no-side-effect validation and negative cases;
19. deactivation, tombstone, cleanup, correction, withdrawal, and rollback.

Exact machine field names remain `NEEDS VERIFICATION` until a canonical config schema exists.

Directory presence must not activate recursive scanning, source fetch, family-tree import, person linking, DNA processing, consent verification/issuance, policy evaluation, title-chain execution, graph/index/map construction, public exposure, release, or publication.

[Back to top](#top)

---

## Validation

Validation must be deterministic, side-effect-free, no-network, and fail closed.

### README checks

- parseable, internally consistent KFM meta block;
- valid headings, anchors, tables, links, and final newline;
- explicit authority/T4/policy-interface boundaries;
- visible segment, consent-placement, and outcome-vocabulary conflicts;
- no real personal, DNA, consent, land/title, cultural, secret, private-endpoint, or live-binding material;
- no executable/runtime/CI enforcement overclaim.

### Future payload checks

Validate syntax/parser/version, consumer/owner, explicit load and precedence, unknown/duplicate keys, authority refs, source role/rights, assertion state, living/protected state, identity/relationship ambiguity, DNA prohibition, consent scope/expiry/revocation, cultural review, land/title/boundary distinctions, temporal semantics, privacy/public-safe profiles, policy-input completeness, evaluator identity/freshness, outcome normalization, reason/obligation handling, observability, reconstruction risk, no-network/no-side-effects, cleanup, and rollback.

### Essential negative cases

- living-person data accepted under a public profile;
- unknown living status treated as deceased;
- weak-signal person merge or hypothesis promoted to fact;
- raw DNA/vendor ID reaches config or logs;
- DNA match becomes verified kinship;
- consent inferred, broadened, stale, expired, disputed, or revoked;
- one person’s consent authorizes another’s disclosure;
- config embeds/forges policy input or decision;
- engine `ALLOW` maps directly to publication;
- `RESTRICT`/`HOLD` becomes `ANSWER`;
- evaluator timeout/missing bundle falls back permissively;
- unknown or unenforceable obligation is ignored;
- cultural authority bypassed;
- public-record availability treated as permission;
- assessor/tax becomes title or geometry becomes boundary;
- title gap silently filled;
- private person–parcel join released;
- low-count/repeated-query/graph/map reconstruction succeeds;
- invalid config falls back permissively;
- validation performs network or side effects;
- watcher/consumer writes directly to catalog, published, or release state.

TODO-only workflows are scaffolds, not proof.

[Back to top](#top)

---

## Failure behavior

| Condition | Required behavior |
|---|---|
| Missing/malformed/unsupported required config | `ERROR` or disabled/hold; no best-effort continuation. |
| Unknown/duplicate consequential key | Reject or hold. |
| Missing consumer/owner/authority ref | Disabled/hold or `ERROR`. |
| Missing policy context | `ABSTAIN`, `DENY`, or `ERROR`; never `ANSWER`. |
| Missing/stale evaluator or bundle | `ERROR` or hold. |
| Unnormalized engine result | `ERROR`. |
| Unknown/unenforceable obligation | `DENY` or `ERROR`. |
| Unknown living status / ambiguous identity | Deny exposure or abstain/hold; no merge. |
| Raw DNA/correlatable ID | `DENY`, quarantine, exposure assessment. |
| Missing/expired/out-of-scope/unverifiable consent | `DENY`. |
| Valid revocation/suspension | Stop use, deny access, invoke cleanup. |
| Missing cultural/rights-holder approval | `DENY` or hold when required. |
| Assessor as title / geometry as boundary | `DENY`. |
| Title gap/conflict | `ABSTAIN` or hold; surface conflict. |
| Disclosure-risk failure | `DENY` or hold. |
| Source outage/staleness | Preserve lineage and visible stale state; do not infer absence. |
| Rollback/cleanup target unavailable | Hold activation and release-dependent use. |

No failure path may widen exposure, lower review, merge identity, promote hypotheses, infer living status, broaden consent, ignore revocation, override cultural authority, convert administrative context into title, fill a title gap, lower privacy thresholds, erase stale/correction state, activate a source, or publish.

[Back to top](#top)

---

## Governed AI and generated language

Configuration may support presentation preferences for an already-governed AI or Focus Mode consumer. It cannot authorize AI as identity, kinship, DNA, consent, cultural, title, legal, policy, evidence, or release authority.

Generated language must use released resolvable evidence; preserve assertions and conflicts; distinguish projections from sources, hypotheses from verified assertions, DNA evidence from conclusions, and parcel context from title; disclose time, confidence, uncertainty, policy, consent, rights, stale/correction state; and use canonical finite outcomes.

Prompts/config must not instruct a model to identify or merge people from weak signals, infer living-person relatives/address/health/parentage/DNA traits, infer consent, ignore revocation, infer tribal/cultural membership, fill title gaps, expose protected contexts, or suppress caveats.

[Back to top](#top)

---

## Maintenance and change budget

For each change:

1. identify consumer, owner, purpose, prohibited purposes, and exact path;
2. re-read parent config, domain doctrine, consent policy, and Directory Rules;
3. verify canonical refs and unresolved conflicts;
4. preserve identity/assertion/relationship/DNA/title distinctions;
5. verify living/protected state, consent, revocation, cultural authority, privacy, and reconstruction risk;
6. verify explicit policy input, evaluator identity/freshness, normalization, reasons, and obligations;
7. run parse, semantic, policy-interface, privacy, consent, rights, negative, no-network, and no-side-effect checks;
8. document precedence, migration, deactivation, cleanup, correction, withdrawal, and rollback;
9. inspect the complete diff for secrets, live bindings, real/sensitive/reconstructable content;
10. verify remote read-back and changed paths.

A config PR must not silently add person matching, DNA processing, consent or policy rules, outcome normalization, obligation interpretation, privacy thresholds, title algorithms, source activation, contracts/schemas, implementation code, lifecycle/trust/release data, or public surfaces.

[Back to top](#top)

---

## Definition of done for the first payload

- [ ] Named consumer, owner, purpose, format, parser, and explicit load path are verified.
- [ ] Canonical refs resolve; segment and consent-placement conflicts are resolved or avoided.
- [ ] Precedence and unknown/duplicate-key behavior are tested.
- [ ] Directory presence activates nothing.
- [ ] Explicit policy input is complete for operation, audience, object, evidence, rights, sensitivity, consent, review, and release context.
- [ ] Evaluator/bundle identity, version/hash, timeout, and fail-closed behavior are verified.
- [ ] Engine results normalize to `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.
- [ ] Reasons and obligations are preserved; unknown/unenforceable obligations fail closed.
- [ ] Consent remains one independent gate and never publication approval.
- [ ] Identity, relationship, living/protected state, DNA, cultural-rights, land/title, temporal, and privacy boundaries are explicit and tested.
- [ ] Synthetic fixtures cover valid, invalid, abstain, deny, error, stale, revoked, disputed, ambiguous, conflicting, corrected, superseded, and obligation-failure cases.
- [ ] No-network/no-side-effect and sensitive-value scans pass.
- [ ] Deactivation, tombstone, cleanup, correction, withdrawal, and rollback are tested.
- [ ] Repository checks are substantive or scaffold limitations are stated.
- [ ] No identity, DNA, consent decision, title, route, layer, release, or publication activates from file presence.

[Back to top](#top)

---

## Related authority surfaces

- [`../README.md`](../README.md) — parent domain-config contract.
- [`../../README.md`](../../README.md) — root config boundary.
- [`../../../docs/domains/people-dna-land/README.md`](../../../docs/domains/people-dna-land/README.md) — domain doctrine and T4 posture.
- [`../../../policy/consent/people-dna-land/README.md`](../../../policy/consent/people-dna-land/README.md) — restricted-domain consent gate; placement and enforcement remain unresolved.
- [`../../../contracts/policy/policy_input_bundle.md`](../../../contracts/policy/policy_input_bundle.md) and paired [schema](../../../schemas/contracts/v1/policy/policy_input_bundle.schema.json) — explicit input semantics and current placeholder shape.
- [`../../../contracts/policy/policy_decision.md`](../../../contracts/policy/policy_decision.md) and paired [schema](../../../schemas/contracts/v1/policy/policy_decision.schema.json) — canonical finite decision semantics.
- [`../../../packages/policy-runtime/README.md`](../../../packages/policy-runtime/README.md) and [`pyproject.toml`](../../../packages/policy-runtime/pyproject.toml) — runtime boundary and current `0.0.0` placeholder.
- [`../../../.github/workflows/policy-test.yml`](../../../.github/workflows/policy-test.yml) — TODO-only policy workflow.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md), [`DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md), and [`VERIFICATION_BACKLOG.md`](../../../docs/registers/VERIFICATION_BACKLOG.md) — lane state, drift, and open verification.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret and sensitive-value handling.

[Back to top](#top)

---

## ADRs and drift triggers

This README introduces no ADR and resolves no conflict.

Separate governance is required to resolve or define:

- domain segment and consent-policy placement;
- source-role vocabulary;
- identity/canonicalization, living-status, genealogy/DNA thresholds;
- consent credential, delegation, multi-party consent, dispute, revocation, or cleanup;
- canonical policy outcomes, engine normalization, reason codes, or obligation interpreters;
- cultural/tribal/rights-holder authority;
- privacy tiers, aggregation, k-anonymity, suppression, differencing, residual-risk acceptance;
- land/title/boundary/legal-review methods;
- source rights/activation;
- universal config discovery/precedence;
- any parallel authority home, direct public access, or lifecycle/release change.

Configuration must not settle these decisions indirectly.

[Back to top](#top)

---

## Rollback, correction, and revocation

Before merge, close the draft PR and abandon the scoped branch. After merge, use a transparent revert commit or PR restoring the prior known-good file; do not rewrite shared history.

For a future payload correction/revocation:

1. disable selection through the verified consumer;
2. stop affected ingestion, linking, DNA, policy-dependent action, graph/index/map/export/AI workflows;
3. preserve non-sensitive review evidence;
4. identify affected derivatives without reproducing protected content;
5. assess exposure/misclassification;
6. honor deletion, tombstone, withdrawal, revocation, and notification obligations;
7. invalidate caches, indexes, graphs, embeddings, tiles, exports, and derivatives;
8. restore prior safe version or disabled state;
9. rerun validation and negative cases;
10. emit required incident, revocation, correction, withdrawal, review, release, or rollback records in canonical homes;
11. verify no surface continues serving unauthorized, revoked, stale, misidentified, misrelated, mistitled, or reconstructable material.

A Git revert does not itself withdraw data, revoke access, delete derivatives, invalidate caches, correct claims, notify consumers, or establish publication lineage.

[Back to top](#top)

---

## Last reviewed

**2026-07-14**, against `main@14b59b6b84ee2b9fa46e002b60e922c97cab2761`.

Review again before the first non-README payload, consumer binding, loader/precedence decision, policy bundle activation, evaluator integration, obligation interpreter, identity/living-status/DNA/consent/cultural-rights/privacy/aggregation/land/title profile, source activation, graph/search/map integration, or public-output integration.

<details>
<summary>Appendix A — preservation and v0.3 delta</summary>

v0.3 preserves the v0.2 no-authority boundary, assertion-first identity model, living-person and raw-DNA T4 defaults, private person–parcel denial, relationship-hypothesis separation, purpose-bound revocable consent, cultural-rights and sovereignty review, assessor-not-title and parcel-not-boundary-proof rules, title-gap handling, temporal distinctions, reconstruction-risk controls, no-network validation, governed-AI limits, migration discipline, correction, and rollback.

The material delta is policy-interface grounding: repository evidence distinguishes `PolicyInputBundle` input from `PolicyDecision` output, records canonical `ANSWER / ABSTAIN / DENY / ERROR` outcomes, requires engine-result normalization and obligation enforcement, and states current limitations of the permissive input schema, `0.0.0` runtime package, TODO-only workflow, unresolved consent placement, and absent target-lane executable payload.

</details>
