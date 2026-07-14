<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-people-dna-land-readme
title: configs/domains/people-dna-land/ — People, DNA, and Land Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · People/DNA/Land steward · Privacy/consent reviewer · Rights-holder/cultural-authority reviewer · Identity/land-evidence reviewer · Consumer owner · Validation steward
created: 2026-07-13
updated: 2026-07-14
policy_label: public; config-sublane; people-dna-land; T4-default; living-person-aware; dna-restricted; consent-revocable; cultural-rights-aware; title-anti-collapse; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/people-dna-land/README.md
truth_posture: CONFIRMED canonical people-dna-land config lane, repository-present parent config contract, repository-present People/Genealogy/DNA/Land doctrine, person-assertion-not-fact rule, living-person T4 default, raw-DNA T4 no-public-transform rule, private person-parcel T4 default, assessor-not-title rule, parcel-geometry-not-boundary-proof rule, relationship-hypothesis-not-fact rule, revocable-consent cleanup rule, watcher-as-non-publisher rule, and documentation-only lane / CONFLICTED people versus people-dna-land segment naming and canonical source-role mapping versus older authority-observation-context-model wording / PROPOSED future consumer-bound templates and governed privacy, consent, aggregation, and public-safe profile selectors / UNKNOWN consumers, loader behavior, precedence, deployment binding, and enforcement / NEEDS VERIFICATION owners, executable validation, source rights, living/deceased determination rules, consent-token verification, revocation propagation, identity-resolution methods, k-anonymity and aggregation parameters, cultural-authority requirements, title-chain methods, public-safe geometry parameters, and runtime binding
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 5b8b9e52d7e1a78d2cfa87f74934a984eed2bba0
  prior_blob: 3dc25454206435e6c22ab8a27da50502c8248008
  bounded_search_result: configs/domains/people-dna-land/README.md only
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
notes:
  - "This lane contains documentation only in the bounded path search. No executable People/DNA/Land configuration payload, consumer, loader, identity resolver, person linker, DNA processor, consent authority, title resolver, source activation, network fetch, or publication binding is established."
  - "A bounded repository search for configs/domains/people-dna-land returned this README and no indexed executable consumer. This is bounded evidence, not proof that no differently named or unindexed consumer exists."
  - "v0.2 expands the identity, genealogy, DNA, consent, revocation, cultural-rights, land-record, title-anti-collapse, privacy, validation, correction, and rollback contract without creating policy, schema, identity, kinship, consent, title, source, release, or public-surface authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People, DNA, and Land Domain Configuration

`configs/domains/people-dna-land/`

> Safe-to-commit, People/Genealogy/DNA/Land-specific configuration documentation and future consumer-bound templates. This lane does not own identity, kinship, DNA interpretation, consent, cultural authority, title, ownership, privacy policy, evidence, release, or publication.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Scope](#scope) · [Repository fit](#repository-fit) · [Inputs](#inputs) · [Outputs](#outputs) · [File contract](#minimum-configuration-contract) · [Consumer binding](#consumer-binding-precedence-and-discovery) · [Identity](#identity-assertion-and-kinship-guardrails) · [DNA](#dna-consent-and-revocation-contract) · [Land](#land-record-title-and-boundary-guardrails) · [Cultural rights](#cultural-rights-sovereignty-and-community-authority) · [Sensitivity](#sensitivity-privacy-and-public-safe-derivatives) · [Logging](#logging-telemetry-and-observability) · [Validation](#validation) · [Failure behavior](#failure-behavior) · [AI](#governed-ai-and-generated-language) · [Review](#review-burden) · [Maintenance](#maintenance-and-safe-change-pattern) · [Migration](#migration-and-anti-bypass-posture) · [Done](#definition-of-done-for-the-first-payload) · [Related](#related-folders) · [ADRs](#adrs-and-drift-triggers) · [Rollback](#rollback-correction-and-revocation) · [Language](#safe-language-rules)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`  
> **Observed lane maturity:** README-only in the bounded path search; no executable People/DNA/Land configuration payload is established  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for identity, rights, consent, title, truth, or governance  
> **Runtime posture:** no loader, consumer binding, source activation, person linking, DNA processing, title reasoning, consent grant, public layer, release, or publication is established by this README

> [!CAUTION]
> **Living-person fields, raw DNA segment data, and private person–parcel joins default to T4 denial.** Person identity is an evidence-bound view over assertions, relationship hypotheses remain hypotheses, assessor and tax records are not title, parcel geometry is not boundary proof, and consent is scoped and revocable. Configuration must fail closed whenever identity, living status, consent, rights, cultural authority, title support, or sensitivity is unresolved.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical People, Genealogy, DNA, and Land Ownership lane.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should parse, render, validate, or select already-governed material, but they cannot decide:

- whether two records represent the same person;
- whether a person is living or deceased;
- whether a name, life event, residence, migration event, or relationship assertion is true;
- whether a DNA match establishes kinship;
- whether a relationship hypothesis may be promoted as fact;
- whether consent exists, is valid, covers a purpose, or remains unrevoked;
- whether a rights holder, tribal nation, cultural authority, family, or community authorizes use;
- whether an assessor or tax record establishes ownership or title;
- whether a parcel geometry proves a legal boundary;
- whether a deed, patent, probate record, survey, lease, lien, easement, or title instrument controls;
- whether a chain-of-title gap may be filled;
- whether a person–parcel, person–place, family, DNA, or cultural join may be exposed;
- whether evidence supports a claim; or
- whether an artifact may be promoted, released, or published.

This README is intended for:

- People/DNA/Land domain stewards;
- configuration and developer-experience maintainers;
- privacy, consent, identity, genealogy, DNA, land-record, title, cultural-rights, sovereignty, security, policy, legal/rights, and release reviewers;
- package, pipeline, app, runtime, test, watcher, connector, and tooling owners that may consume configuration; and
- reviewers checking Directory Rules placement and trust-membrane integrity.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Domain meaning | **None.** Doctrine remains in [`docs/domains/people-dna-land/`](../../../docs/domains/people-dna-land/README.md). |
| Person identity | **None.** Configuration cannot create a canonical identity, merge persons, resolve conflicts, or choose a “best” record by convenience. |
| Living/deceased status | **None.** Configuration cannot infer or override living status for exposure purposes. Uncertainty fails closed. |
| Names, dates, life events, residences, and migration | **None.** These remain source-attributed assertions with time, evidence, and confidence. |
| Kinship and genealogy | **None.** Configuration cannot turn a relationship assertion, tree import, or hypothesis into verified kinship. |
| DNA interpretation | **None.** Configuration cannot infer relationships, ethnicity, health, identity, parentage, or ancestry from DNA. |
| Consent | **None.** A value may reference an accepted consent profile; it cannot grant, broaden, renew, waive, or prove consent. |
| Revocation | **None.** Configuration cannot ignore, defer, reverse, or narrow a valid revocation. |
| Cultural authority and sovereignty | **None.** Configuration cannot grant permission, represent a community, or substitute for rights-holder review. |
| Land ownership or title | **None.** Configuration cannot turn assessor, tax, parcel, or occupancy context into title truth. |
| Legal boundary | **None.** Configuration cannot convert parcel geometry, a map, or a derived polygon into surveyed or adjudicated boundary proof. |
| Source identity, role, rights, cadence, and activation | **None.** These require registry, connector, rights, policy, and review surfaces. |
| Schema or contract shape | **None.** Configuration may reference verified schemas and contracts but must not duplicate or redefine them. |
| Privacy, sensitivity, redaction, aggregation, or public-safe geometry | **None.** A value may select an accepted profile; it cannot create, weaken, or approve a rule. |
| Evidence or claim truth | **None.** Configuration cannot create an `EvidenceBundle`, validate a claim, or make generated interpretation sovereign truth. |
| Release or publication | **None.** Configuration cannot authorize promotion, release, public display, or KFM publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file under an explicit binding and precedence rule. |

A configuration value may point to an authority surface. It does not become authority through repetition, proximity, successful parsing, operational convenience, apparent confidence, or use by a map, family tree, graph, search index, Evidence Drawer, Focus Mode, export, or AI surface.

[Back to top](#top)

---

## Status

### Evidence snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Repository ID | `1059091169` |
| Visibility | public |
| Base ref | `main` |
| Base commit | `5b8b9e52d7e1a78d2cfa87f74934a984eed2bba0` |
| Prior README blob | `3dc25454206435e6c22ab8a27da50502c8248008` |
| Bounded path-search result | `configs/domains/people-dna-land/README.md` only |

### Maturity matrix

| Item | State | Safe conclusion |
|---|---:|---|
| Canonical config slug | **CONFIRMED** | `people-dna-land` is a repository-present domain configuration lane. |
| Parent configuration contract | **CONFIRMED** | [`configs/domains/README.md`](../README.md) defines this path as a non-secret, non-authoritative configuration sublane. |
| Domain doctrine | **CONFIRMED repository-present** | The domain README establishes assertion-first identity, T4 defaults, consent revocation, title anti-collapse, cultural-rights review, and fail-closed publication. |
| Living-person fields | **CONFIRMED — T4 DEFAULT** | Public exposure is denied unless a separately governed transform, consent/review path, and release state permit a derivative. |
| Raw DNA segments and vendor identifiers | **CONFIRMED — T4 / NO PUBLIC TRANSFORM** | Raw segments and correlatable vendor IDs may not be released publicly or logged through this lane. |
| Private person–parcel joins | **CONFIRMED — T4 DEFAULT** | Any public-safe derivative requires separately governed de-identification/generalization and review. |
| Person identity | **CONFIRMED ASSERTION-FIRST** | Identity is an evidence-bound projection over assertions, not a configuration-selected fact. |
| Relationship hypothesis | **CONFIRMED NOT FACT** | DNA, GEDCOM, graph, and model outputs remain hypotheses unless governed evidence and review support a different assertion class. |
| Assessor/tax role | **CONFIRMED — NOT TITLE** | Administrative records cannot be configured as ownership or title authority. |
| Parcel geometry | **CONFIRMED — NOT BOUNDARY PROOF** | A parcel polygon cannot become legal boundary truth through configuration. |
| Consent revocation | **CONFIRMED REVERSIBLE** | Valid revocation requires tombstoning, downstream cleanup, embargo/cache invalidation, and correction handling. |
| Current lane content | **README ONLY IN BOUNDED SEARCH** | No executable payload, consumer, or activation path was found by the path-scoped search. Exhaustive inventory remains `NEEDS VERIFICATION`. |
| Indexed executable consumer | **NOT FOUND IN BOUNDED SEARCH** | Differently named or unindexed consumers remain `UNKNOWN`. |
| Consumer and loader | **UNKNOWN** | No parser, auto-discovery mechanism, merge order, precedence, or unknown-key behavior is established here. |
| Segment name | **CONFLICTED** | Directory Rules uses `people-dna-land` for domain-segment roots; the Atlas crosswalk uses `people` for several schema/contract/policy roots. Configuration must not create aliases or settle the conflict. |
| Source-role vocabulary mapping | **CONFLICTED / NEEDS VERIFICATION** | Canonical role classes and older `authority / observation / context / model` wording require governance, not local aliases. |
| Source rights and terms | **NEEDS VERIFICATION** | Source-specific rights, attribution, redistribution, retention, access, and reuse limits require verified records. |
| Living/deceased determination | **NEEDS VERIFICATION** | Rules, evidence thresholds, age cutoffs, uncertainty handling, and review obligations require accepted policy. |
| Consent verification and purpose binding | **NEEDS VERIFICATION** | Token format, scope, purpose, subject, controller, expiry, and revocation checks require accepted contracts and policy. |
| Identity and kinship methods | **NEEDS VERIFICATION** | Match thresholds, conflict resolution, false-positive controls, and human review must be governed and tested. |
| Aggregation and k-anonymity profiles | **NEEDS VERIFICATION** | Thresholds, cells, suppression, differencing defenses, and residual-risk tests require accepted policy. |
| Cultural-authority requirements | **NEEDS VERIFICATION** | Rights-holder, tribal, family, institutional, and community approvals require explicit governance. |
| Title-chain methods | **NEEDS VERIFICATION** | Instrument precedence, gaps, overlaps, supersession, jurisdiction, and legal-review requirements must be explicit. |
| Validation and CI enforcement | **NEEDS VERIFICATION** | Expectations are documented; substantive executable enforcement is not proven by this README. |
| Runtime, release, and publication | **NOT ESTABLISHED** | Nothing in this lane authorizes operational use, linking, DNA processing, consent action, title determination, release, or publication. |

Directory presence must not trigger config discovery, source activation, network access, record linkage, person canonicalization, family-tree import, DNA matching, relationship inference, consent creation, title resolution, parcel joining, graph projection, map-layer creation, lifecycle promotion, or publication.

[Back to top](#top)

---

## Scope

### What belongs here

Only safe, non-secret, People/DNA/Land-specific configuration material for a named or explicitly proposed consumer belongs here.

| Material | Permitted purpose | Minimum posture |
|---|---|---|
| `README.md` | Define this configuration boundary. | Preserve non-authority, privacy, consent, rights, evidence, and release controls. |
| `*.template.yaml` or `*.template.yml` | Placeholder-based template for a verified consumer. | Parseable, versioned, consumer-bound, no secrets, no live binding, no identity or consent action. |
| `*.example.yaml`, `*.example.json`, or `*.example.toml` | Tiny illustrative configuration. | Unmistakably synthetic people, families, DNA handles, instruments, parcels, dates, and places; impossible real-world correlation. |
| Conservative deny/hold/review defaults | Select an existing deny, abstain, restrict, review, tombstone, or disabled profile. | Cannot waive privacy, consent, rights, cultural authority, evidence, or release burden. |
| Privacy-profile selectors | Select an already-governed privacy or redaction profile. | Cannot define new exposure rules or permit living-person fields. |
| Consent-profile selectors | Select an accepted purpose-bound verification profile. | Cannot grant, broaden, renew, infer, or waive consent. |
| Revocation-handling selectors | Select an accepted cleanup/tombstone workflow profile for a verified consumer. | Cannot delay, suppress, or narrow valid revocation obligations. |
| Aggregation-profile selectors | Select an accepted aggregate or k-anonymized public-safe profile. | Cannot invent thresholds or expose small-cell/differencing risk. |
| Identity-review profile selectors | Select an accepted review/abstention profile. | Cannot auto-merge, choose a person, or promote a hypothesis. |
| Land-record display selectors | Configure labels, instrument classes, gap markers, or “not title” warnings. | Must not establish ownership, title, boundary, or legal effect. |
| Presentation hints | Configure source badges, assertion state, time, confidence, caveats, consent status, stale state, or correction display. | Must not change truth, authority, sensitivity, or release state. |
| Migration notes | Document a real key, version, consumer, or path transition. | Time-bounded, owner-linked, reversible, and not a parallel authority. |
| Validation notes | Describe verified checks and finite outcomes. | Commands and workflows must resolve or remain labeled `PROPOSED` / `NEEDS VERIFICATION`. |

Synthetic examples must not resemble real people, minors, relatives, adoptees, donors, DNA kits, haplotypes, segments, family trees, parcels, legal descriptions, instruments, owners, cultural affiliations, tribal membership, contact details, addresses, sealed records, or sensitive places closely enough to support identification or reconstruction.

### What does not belong here

- living-person names, dates of birth, addresses, contact details, identifiers, relationships, residences, employment, education, migration, or other personal data;
- data about minors, adoptees, sealed records, protected witnesses, victims, medical or reproductive history, or other heightened-risk contexts;
- raw or derived DNA segments, chromosome coordinates, centimorgan values, haplotypes, genotype files, kit IDs, vendor account IDs, match lists, triangulation tables, or genetic-health/ancestry inferences;
- real GEDCOM, GEDZip, family-tree, genealogy, obituary, cemetery, census, vital, court, probate, military, church, school, directory, or vendor exports;
- consent grants, consent tokens, passports, OAuth artifacts, revocation records, identity documents, access approvals, or rights-holder decisions;
- real assessor, tax, deed, patent, title, mortgage, lien, easement, lease, probate, survey, plat, legal-description, parcel, ownership, water-right, mineral-right, or access records;
- exact or reconstructable private person–parcel, person–place, family, DNA, cultural, tribal, land, or title joins;
- credentials, tokens, private keys, cookies, signed URLs, private endpoints, workstation paths, internal deployment bindings, or environment-specific secrets;
- settings that treat a person canonicalization candidate as identity fact;
- settings that treat a relationship hypothesis or DNA match as verified kinship;
- settings that infer living/deceased status without accepted evidence and review;
- settings that treat assessor or tax records as title;
- settings that treat parcel geometry as a surveyed, adjudicated, or insured boundary;
- settings that silently fill chain-of-title gaps or choose among conflicting instruments;
- settings that suppress consent scope, expiry, revocation, cultural authority, rights, uncertainty, or evidence;
- source admission, activation, rights, retention, redistribution, or source-role decisions;
- schemas, contracts, policy, registries, consent records, receipts, proofs, EvidenceBundles, release records, correction notices, or publication decisions;
- package code, pipeline logic, connector code, watcher code, identity-resolution code, DNA-processing code, legal reasoning code, runtime adapters, infrastructure definitions, generated artifacts, caches, exports, screenshots, or reports.

[Back to top](#top)

---

## Repository fit

```text
configs/
└── domains/
    └── people-dna-land/
        └── README.md
```

This lane is one responsibility segment. It may eventually support verified consumers in packages, pipelines, applications, runtime components, tests, tools, or review systems, but it does not replace those roots.

### Placement rules

- Configuration stays under `configs/`.
- Domain meaning stays under `docs/` and verified contracts.
- Machine shape stays under the canonical schema root after the segment-name conflict is resolved.
- Privacy, consent, cultural-rights, sensitivity, admissibility, and release rules stay under policy/governance roots.
- Source identity, rights, role, retention, and activation stay in verified source registry and connector surfaces.
- People, genealogy, DNA, land, title, and consent data stay in governed lifecycle roots.
- Receipts, proofs, evidence, review, release, correction, and rollback artifacts stay in their canonical homes.
- Implementation stays in packages, pipelines, connectors, apps, runtime, tools, and infrastructure.
- Public clients use released artifacts through governed APIs, never this directory.

### Segment-name conflict

The domain doctrine records a blocking conflict:

- Directory Rules uses `people-dna-land` for domain-segment roots.
- The Atlas crosswalk uses `people` for several schema, contract, sensitivity-policy, and consent-policy roots.

This README uses its confirmed current path, `configs/domains/people-dna-land/`, and does not create aliases, duplicate files, cross-root symlinks, fallback searches, or implicit precedence for `people`.

[Back to top](#top)

---

## Inputs

This README currently consumes documentation evidence only.

A future configuration payload must identify:

| Input | Required handling |
|---|---|
| Exact consumer | Repository path, component, owner, and bounded purpose. |
| File format and version | YAML, JSON, TOML, or another explicit parser contract. |
| Load mechanism | Explicit path or argument; directory presence alone must not activate loading. |
| Precedence | Built-in defaults, committed template, local ignored override, environment input, and command-line order. |
| Unknown-key behavior | Consequential unknown keys reject or hold; silent ignore is not acceptable. |
| Contract and schema references | Canonical and versioned; unresolved segment naming blocks authority claims. |
| Policy references | Privacy, consent, sensitivity, cultural rights, identity, land/title, retention, and release profiles. |
| Source references | Source IDs only; no credentials, live URLs, private endpoints, vendor IDs, or payloads. |
| Source role | Explicit and preserved; unresolved role mapping remains visible. |
| Person state | Assertion/candidate/canonical projection state, living/deceased/unknown status, and review posture. |
| Identity method reference | Accepted method/profile only; no local thresholds or convenience matching. |
| Relationship state | Assertion or hypothesis, evidence basis, confidence, and review state. |
| Consent context | Purpose, subject, controller, scope, expiry, revocation-check requirement, and verifier reference. |
| Cultural authority context | Required rights-holder/community/tribal/institutional review profile. |
| DNA handling class | Synthetic, aggregate, research-restricted, or denied; raw identifiers and segments forbidden. |
| Land-record class | Instrument, assessor, tax, parcel version, legal description, title assertion, ownership interval, or context. |
| Jurisdiction and temporal scope | Recorder/court/agency jurisdiction, effective/recorded dates, source vintage, and supersession state. |
| Spatial semantics | CRS, scale, precision, source geometry, derived geometry, uncertainty, and public-safe profile. |
| Privacy/sensitivity context | Tiers, living/minor status, private joins, small cells, repeated-query risk, and residual risk. |
| Rights and retention | Attribution, redistribution, retention, deletion, embargo, purpose, and revocation obligations. |
| Validation reference | Deterministic parse, shape, semantic, privacy, consent, rights, negative, and no-network checks. |
| Failure behavior | Finite outcomes, fail-closed defaults, and visible reason codes. |
| Migration and rollback | Previous version, deactivation path, cleanup duties, and rollback target. |
| Local override posture | Ignored/local-only path with no secrets or sensitive data committed. |

Placeholder IDs must be obviously synthetic, such as:

- `<SYNTHETIC_PERSON_ASSERTION_ID>`;
- `<SYNTHETIC_DNA_TOKEN>`;
- `<ACCEPTED_CONSENT_PROFILE_ID>`;
- `<ACCEPTED_PRIVACY_PROFILE_ID>`;
- `<SYNTHETIC_INSTRUMENT_ID>`;
- `<SYNTHETIC_PARCEL_ID>`;
- `<LOCAL_IGNORED_OVERRIDE_PATH>`.

Do not use realistic names, birth dates, kit numbers, chromosome segments, addresses, parcel numbers, legal descriptions, recorder references, tribal affiliations, or instrument numbers as examples.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future file may provide a validated consumer with:

- safe presentation defaults;
- assertion-state and evidence-display selectors;
- deny, abstain, hold, restricted, reviewer-only, tombstone, or disabled defaults;
- accepted privacy, consent-verification, aggregation, redaction, or public-safe profile selectors;
- “not identity fact,” “hypothesis,” “not title,” and “not boundary proof” labels;
- time, source, confidence, living-status uncertainty, consent, rights, stale-state, correction, and supersession display hints;
- synthetic test values; and
- migration or compatibility metadata.

A future file must not output or cause:

- a person identity;
- a person merge;
- a kinship conclusion;
- a DNA inference;
- a living/deceased determination;
- a consent grant or waiver;
- a rights-holder or cultural-authority approval;
- an ownership, title, or boundary determination;
- a source activation or network request;
- a lifecycle transition;
- a public layer or API route;
- a release, correction, or publication decision.

[Back to top](#top)

---

## Minimum configuration contract

Every future non-README file must document or encode, directly or through a resolvable adjacent specification:

1. configuration ID and version;
2. intended consumer path and owner;
3. bounded purpose and prohibited purposes;
4. parser and format version;
5. explicit load/discovery mechanism;
6. precedence and merge behavior;
7. missing-file, duplicate-key, and unknown-key behavior;
8. canonical contract, schema, policy, registry, and doctrine references;
9. source IDs, source roles, rights, retention, and activation assumptions;
10. assertion/candidate/canonical projection distinctions;
11. living, deceased, minor, unknown, and protected-person handling;
12. identity-resolution and conflict behavior;
13. relationship assertion versus hypothesis behavior;
14. DNA handling class and raw-ID/segment prohibition;
15. consent purpose, scope, expiry, verifier, and revocation checks;
16. cultural-rights, sovereignty, and rights-holder review requirements;
17. land-record class, jurisdiction, instrument role, and title/boundary disclaimers;
18. source, event, valid, recorded, effective, retrieval, processing, release, correction, revocation, and supersession time semantics;
19. privacy tier and accepted public-safe profile references;
20. small-cell, k-anonymity, differencing, repeated-query, graph, and reconstruction controls;
21. logging, telemetry, cache, index, and export restrictions;
22. deterministic validation and negative cases;
23. finite failure outcomes and reason codes;
24. no-network and no-side-effect behavior;
25. deactivation, tombstoning, cleanup, migration, correction, and rollback; and
26. proof that directory presence alone activates nothing.

A future file that cannot satisfy this contract remains `PROPOSED`, disabled, or held for review.

### Required file header

Each payload should begin with a machine-readable documentation header or adjacent metadata that identifies:

```text
config_id
config_version
status
intended_consumer
consumer_owner
purpose
prohibited_purposes
format_version
contract_ref
schema_ref
policy_refs
privacy_profile_ref
consent_profile_ref
source_role_profile_ref
validation_ref
effective_from
supersedes
rollback_target
```

Exact field names remain `NEEDS VERIFICATION` until a canonical configuration schema exists.

[Back to top](#top)

---

## Consumer binding, precedence, and discovery

No consumer binding is established by this README.

A future consumer must:

1. name the exact file explicitly;
2. validate before use;
3. reject unsupported versions;
4. define precedence deterministically;
5. reject duplicate consequential keys unless the parser contract explicitly governs them;
6. reject or hold unknown consequential keys;
7. remain disabled when required policy, consent, rights, identity, or review dependencies are unresolved;
8. avoid network, person-linking, DNA, consent, title, and publication side effects during validation;
9. expose the effective configuration and source provenance for review without exposing protected values; and
10. support deactivation, tombstoning, correction, cleanup, and rollback.

### Directory presence is not discovery

The existence of:

```text
configs/domains/people-dna-land/
```

must not cause:

- recursive scanning;
- source activation;
- family-tree import;
- record linkage;
- person canonicalization;
- DNA upload or processing;
- consent verification or issuance;
- land-record joining;
- title-chain execution;
- graph construction;
- indexing;
- public exposure;
- release or publication.

### Precedence must be explicit

A future consumer must state the order among:

- built-in safe defaults;
- committed templates;
- local ignored overrides;
- deployment inputs;
- environment values;
- command-line options; and
- policy-enforced constraints.

Policy, consent, rights, sensitivity, evidence, cultural authority, and release gates always outrank configuration convenience.

[Back to top](#top)

---

## Identity, assertion, and kinship guardrails

### Person assertions are evidence, not facts

Configuration must preserve:

- source attribution;
- assertion type;
- subject and object references;
- source-native identifiers;
- temporal scope;
- confidence and uncertainty;
- evidence references;
- conflicting assertions;
- review state;
- correction and supersession lineage.

A `PersonCanonical` view is derived. It must not become a separate source of truth or erase the assertions and decisions that produced it.

### Identity resolution

Configuration may select an already-governed identity-review profile for a verified consumer. It must not:

- invent match thresholds;
- treat name similarity as identity;
- treat shared address, household, parcel, school, employer, cemetery, or event as proof;
- prefer a source merely because it is convenient or recent;
- merge records across living/deceased uncertainty;
- choose the first candidate;
- collapse aliases, married names, transliterations, or spelling variants without evidence;
- infer protected characteristics;
- suppress conflicting identity evidence;
- overwrite source-native identities.

Ambiguous identity produces `ABSTAIN`, `DENY`, or a review hold, never silent merging.

### Life events and time

Birth, death, marriage, burial, residence, migration, probate, ownership, and other events must keep distinct:

- asserted event time;
- valid/effective time;
- source publication or recording time;
- retrieval time;
- processing time;
- release time;
- correction time;
- revocation time;
- supersession time.

Unknown, approximate, bounded, conflicting, and inferred dates remain visibly qualified.

### Relationship assertions and hypotheses

Configuration must preserve the difference among:

- source-documented relationship assertion;
- user-contributed tree relationship;
- DNA-supported hypothesis;
- model- or graph-generated candidate;
- reviewer-confirmed assertion;
- unresolved or disputed relationship.

A relationship hypothesis must never be labeled or queried as fact merely because multiple weak signals agree.

### Living/deceased and protected-person status

Living, deceased, minor, protected, unknown, and disputed status are consequential.

- Unknown living status fails closed.
- A missing death record does not prove a person is living.
- Age heuristics do not establish death.
- A tree flag does not waive review.
- Deceased status does not automatically make every associated field public.
- Living relatives may be reconstructable from deceased-person releases.
- Minors and protected persons require the strictest applicable handling.
- Adoption, donor conception, guardianship, sealed records, victim status, and similar contexts require specialized policy and review.

Configuration may select accepted handling profiles but cannot define these rules.

[Back to top](#top)

---

## DNA, consent, and revocation contract

### Raw DNA and vendor identifiers

The following are forbidden in committed configuration, examples, logs, telemetry, caches, indexes, and public artifacts:

- genotype files;
- raw DNA segments;
- chromosome/start/end coordinates;
- centimorgan values;
- haplotypes;
- vendor kit IDs;
- vendor account IDs;
- match lists;
- triangulation outputs;
- download URLs;
- authentication tokens;
- research participant identifiers;
- correlatable pseudonyms.

An opaque synthetic `DNAKitToken` example must be non-correlatable and impossible to confuse with a real vendor identifier.

### DNA anti-collapse

Configuration must not turn:

- a DNA match into verified kinship;
- shared DNA into parentage;
- a segment into identity;
- an ethnicity estimate into ancestry fact;
- a relationship probability into a legal or genealogical conclusion;
- a vendor label into source authority;
- aggregate DNA research into person-level inference.

Raw DNA segment data has no public-transform path. Configuration cannot create one.

### Consent requirements

A future consumer that handles restricted material must verify, through accepted policy and contracts:

- subject or authorized representative;
- controller and processor;
- specific purpose;
- data class;
- operations allowed;
- recipients and environment;
- geographic or jurisdictional scope;
- start and expiry;
- retention and deletion;
- onward-transfer restrictions;
- research agreement where applicable;
- revocation mechanism;
- audit and receipt requirements.

Configuration may reference an accepted consent-verification profile. It cannot:

- manufacture consent;
- assume consent from upload or account creation;
- infer broad consent from narrow consent;
- treat public availability as consent;
- treat family consent as consent for another person;
- extend expired consent;
- ignore changed purpose;
- bypass rights-holder or cultural review.

### Revocation

A valid revocation must trigger the separately governed actions applicable to the consumer, which may include:

- stop processing;
- deny new access;
- tombstone restricted objects;
- invalidate derived indexes and caches;
- withdraw or supersede releases;
- identify downstream derivatives;
- notify governed consumers;
- preserve legally required audit evidence without retaining prohibited content;
- issue correction or withdrawal records;
- verify cleanup completion.

Configuration cannot delay, suppress, narrow, reinterpret, or reverse revocation.

[Back to top](#top)

---

## Land-record, title, and boundary guardrails

### Administrative records are not title

Assessor and tax records may provide administrative, valuation, mailing, or cadastral context. They do not establish:

- legal ownership;
- marketable title;
- beneficial ownership;
- current possession;
- boundary;
- mineral, water, access, or other rights;
- legal capacity;
- absence of unrecorded interests.

Configuration must retain an explicit **not title** posture.

### Parcel geometry is not boundary proof

A parcel polygon, map tile, geocoder result, centroid, derived geometry, or GIS overlay is not:

- a survey;
- a legal description;
- a monument;
- an adjudicated boundary;
- a title-insurance determination;
- a substitute for recorder, court, surveyor, attorney, or other authoritative review.

Configuration may select a presentation profile that displays parcel context with caveats. It cannot elevate geometry to legal truth.

### Instruments and chain of title

Configuration must preserve distinctions among:

- patent;
- deed;
- title instrument;
- mortgage;
- lien;
- easement;
- lease;
- probate instrument;
- court order;
- tax record;
- assessor record;
- plat or survey;
- legal description;
- water, mineral, access, or other rights instrument.

A chain-of-title view must surface:

- gaps;
- overlaps;
- conflicting instruments;
- jurisdiction;
- recording and effective dates;
- supersession;
- unresolved legal descriptions;
- uncertain party identity;
- missing evidence;
- limitations of the source set.

Configuration must not silently fill gaps, select a controlling instrument, infer ownership continuity, or state a legal conclusion.

### Private person–parcel joins

Private person–parcel joins default to T4 denial.

A public-safe derivative, when separately permitted, must use accepted de-identification, aggregation, generalization, review, receipt, and release profiles. Configuration cannot define the transform or claim that residual re-identification risk is acceptable.

[Back to top](#top)

---

## Cultural rights, sovereignty, and community authority

People, genealogy, DNA, burial, land, kinship, migration, historic-person, tribal, Indigenous, descendant-community, cemetery, archaeological, and cultural-place material may carry rights beyond ordinary public-record status.

Configuration must not:

- infer tribal citizenship, enrollment, descent, clan, family, or community membership;
- publish culturally restricted names, relationships, places, ceremonies, burial context, or knowledge;
- treat archival availability as community authorization;
- use a government record to override sovereignty or cultural authority;
- collapse Indigenous land relationships into fee-simple ownership;
- expose descendant-community or family links;
- treat a generic privacy setting as cultural-rights approval;
- bypass rights-holder, tribal, family, institutional, or community review.

A future file may select an accepted cultural-rights review profile. It cannot create authority or substitute for consultation.

[Back to top](#top)

---

## Cross-lane ownership and join rules

Every cross-lane relation must preserve ownership, source role, sensitivity, consent, cultural authority, evidence, and release state.

| Related lane | Permitted context | Boundary |
|---|---|---|
| Settlements / Infrastructure | historical residence, cemetery, school, court, jurisdiction, and place context | Living-person and private-address details fail closed. |
| Roads / Rail / Trade | historical migration, access, and movement context | Paths carry uncertainty; no current-person tracking or inferred itinerary. |
| Archaeology / Cultural Heritage | historic person, documentary, land, burial, and cultural-place context | Sovereignty, cultural authority, sensitive-site, and descendant-community controls remain with that lane and rights holders. |
| Agriculture | historical farm, producer-adjacent, land-use, and parcel context | Private person–parcel and current-producer joins default to denial. |
| Hydrology | historical water-right, irrigation, access, and land-instrument context | Hydrology remains owner of water-system truth; person/land records do not establish hydrologic fact. |
| Geology | mineral, extraction, lease, parcel, and instrument context | Geology remains owner of resource claims; instruments do not prove resource occurrence or reserve. |
| Roads / Infrastructure / Hazards | exposure or resilience summaries | Exact private-person and critical-infrastructure joins are restricted or denied. |
| Frontier Matrix / analytics | aggregate population or ownership context | Cells and aggregates are derivative releases with their own privacy, evidence, and rollback. |

A join may increase sensitivity even when every input is individually public. The resulting product must be evaluated independently.

[Back to top](#top)

---

## Sensitivity, privacy, and public-safe derivatives

### Default tiers

The domain doctrine establishes:

| Class | Default posture |
|---|---|
| Living-person fields | **T4 denied** |
| Raw DNA segment data | **T4 denied; no public-transform path** |
| Private person–parcel joins | **T4 denied** |
| DNA-derived relationship hypotheses involving living people | **T4 denied** |
| Deceased-person assertions | Context-dependent; evidence, living-relative, cultural-rights, and release review still apply |
| Public land instruments | Context-dependent; not-title and boundary caveats remain mandatory |
| Aggregates | Public only after accepted aggregation, suppression, differencing, and residual-risk review |

Configuration may select only already-governed profiles. It must not define:

- k-anonymity thresholds;
- cell sizes;
- geographic aggregation levels;
- suppression thresholds;
- jitter distances;
- date shifting;
- hashing or tokenization methods;
- de-identification methods;
- residual-risk acceptance;
- consent exceptions;
- research-agreement exceptions;
- cultural-rights exceptions.

### Reconstruction risk

Validation and review must consider:

- low counts;
- sparse geography;
- exact or narrow dates;
- rare names;
- family clusters;
- repeated queries;
- differencing across releases;
- time-series changes;
- map zoom and tile inspection;
- graph traversal;
- cross-domain joins;
- public-record enrichment;
- vendor pseudonym correlation;
- parcel and address linkage;
- deceased-to-living relative inference;
- cached, indexed, or exported copies.

Hidden fields, opacity, client-side filters, access-obscure URLs, coarse default zoom, or undocumented conventions are not privacy controls.

### Public-safe derivatives

A derivative is not public-safe merely because:

- direct identifiers were removed;
- a name was hashed;
- geometry was generalized;
- a small count was rounded;
- a person was marked deceased;
- a DNA token was pseudonymous;
- the source was public;
- a consumer displays a disclaimer.

Public-safe status requires accepted policy, receipts, review, evidence, release, and residual-risk evaluation.

[Back to top](#top)

---

## Logging, telemetry, and observability

A future consumer must define safe observability before activation.

Logs, traces, metrics, exceptions, caches, indexes, screenshots, test artifacts, and support bundles must not contain:

- real names or personal identifiers;
- contact details or addresses;
- birth, death, marriage, adoption, or other sensitive events;
- family or relationship graphs;
- raw or correlatable DNA identifiers;
- segment coordinates or match values;
- consent tokens or identity documents;
- person–parcel joins;
- recorder instrument numbers where sensitivity or reconstruction risk applies;
- exact cultural, burial, tribal, or descendant-community context;
- private endpoints, credentials, or signed URLs.

Safe diagnostics should prefer:

- bounded reason codes;
- synthetic fixture IDs;
- non-correlatable run IDs;
- counts above accepted disclosure thresholds;
- schema and config versions;
- validator names;
- digests that cannot be used as stable person or DNA identifiers;
- redacted stack traces;
- explicit `DENY`, `ABSTAIN`, `ERROR`, `STALE`, `REVOKED`, or `HELD` states.

Debug mode must not disable privacy, consent, or rights controls.

[Back to top](#top)

---

## Validation

Validation must be deterministic, side-effect-free, no-network, and fail closed.

### Documentation-only checks

For the current README:

- KFM meta block is parseable and internally consistent.
- Headings, anchors, tables, links, and final newline are valid.
- Authority and T4 default boundaries remain explicit.
- Segment and role-vocabulary conflicts remain visible.
- No real person, family, DNA, consent, parcel, title, cultural, or protected data is included.
- No credentials, private endpoints, personal paths, or live bindings are included.
- No executable behavior is claimed.

### Future payload checks

A future payload should validate:

1. syntax and parser compatibility;
2. configuration version;
3. named consumer and owner;
4. explicit load path and precedence;
5. missing, duplicate, and unknown-key behavior;
6. contract, schema, policy, registry, and doctrine references;
7. source role and source-rights state;
8. assertion/candidate/canonical projection distinctions;
9. living/deceased/minor/protected/unknown status handling;
10. identity conflict and ambiguity behavior;
11. relationship assertion versus hypothesis;
12. raw DNA and correlatable ID prohibition;
13. consent purpose, scope, expiry, verifier, and revocation checks;
14. cultural-rights and sovereignty review requirements;
15. land-record class and assessor-not-title behavior;
16. parcel-geometry-not-boundary behavior;
17. chain-of-title gaps, overlaps, conflicts, jurisdiction, and supersession;
18. source, event, effective, recorded, valid, retrieval, release, correction, revocation, and supersession times;
19. privacy tier and accepted public-safe profile references;
20. small-cell, repeated-query, differencing, graph, and reconstruction risk;
21. logging, telemetry, caching, indexing, export, and screenshot restrictions;
22. no-network and no-side-effect behavior;
23. deactivation, tombstoning, cleanup, migration, correction, withdrawal, and rollback; and
24. proof that directory presence alone activates nothing.

### Essential negative cases

- living-person data accepted under a public profile;
- unknown living status treated as deceased;
- a minor exposed;
- person records merged from weak similarity;
- conflicting assertions silently discarded;
- a relationship hypothesis labeled as fact;
- GEDCOM import bypassing living-person or rights screening;
- raw vendor kit ID written to logs;
- DNA segment or match list accepted;
- DNA match treated as verified kinship;
- consent inferred from upload or account ownership;
- consent scope broadened;
- expired consent treated as valid;
- revocation ignored or cleanup skipped;
- cultural or tribal authority bypassed;
- public-record availability treated as permission;
- assessor or tax record treated as title;
- parcel geometry treated as legal boundary;
- chain-of-title gap silently filled;
- private person–parcel join released;
- small aggregate enabling re-identification;
- repeated queries enabling differencing;
- graph projection leaking living-person or DNA relations;
- unknown consequential key ignored;
- invalid config falling back to permissive behavior;
- network access during validation;
- consumer side effect during validation; and
- connector, watcher, or consumer writing directly to catalog, published, or release state.

Repository workflows that only echo TODO messages are scaffolds, not proof of substantive People/DNA/Land validation.

[Back to top](#top)

---

## Failure behavior

Failures must be finite, visible, deterministic, and non-permissive. Exact machine enums and exit codes remain `NEEDS VERIFICATION`.

| Condition | Required behavior |
|---|---|
| Missing optional file | Keep the proposed feature disabled or use a separately verified safe built-in default. |
| Missing required file | Recorded error or hold; do not continue with partial assumptions. |
| Unreadable or malformed file | Recorded error; no best-effort parsing. |
| Unsupported version | Hold or error with migration guidance. |
| Unknown consequential key | Reject or hold. |
| Duplicate key | Reject unless explicitly governed by the parser contract. |
| Missing consumer or owner | Hold; no activation. |
| Unresolved schema, contract, policy, registry, or doctrine reference | Hold or error. |
| Unresolved source role or rights | Deny or hold. |
| Unknown living/deceased status | Deny public exposure or hold for review. |
| Ambiguous person identity | Abstain or hold; no merge. |
| Conflicting relationship evidence | Abstain or hold; preserve conflict. |
| Relationship hypothesis requested as fact | Deny or abstain. |
| Raw DNA or correlatable vendor ID present | Deny, quarantine, and assess exposure. |
| Missing, expired, out-of-scope, or unverifiable consent | Deny processing or access. |
| Valid revocation present | Stop use, trigger accepted cleanup/tombstone path, and deny further access. |
| Missing cultural/rights-holder approval | Deny or hold when the accepted policy requires it. |
| Assessor or tax record used as title | Deny. |
| Parcel geometry used as boundary proof | Deny. |
| Chain-of-title gap or conflict | Abstain or hold; surface gap/conflict. |
| Unresolved private person–parcel sensitivity | Deny or restrict. |
| Aggregate fails disclosure-risk profile | Deny or hold. |
| Source outage or stale source | Preserve last-known lineage with visible stale state or return unavailable; do not infer absence. |
| Network request attempted during no-network validation | Error. |
| Consumer side effect during validation | Error and rollback test state. |
| Rollback or cleanup target unavailable | Hold activation or release-dependent use. |

No failure path may silently:

- widen exposure;
- lower review burden;
- relabel an assertion;
- merge a person;
- resolve kinship;
- infer living/deceased status;
- convert a hypothesis into fact;
- extend or broaden consent;
- ignore revocation;
- override cultural authority;
- convert administrative land context into title;
- fill a title gap;
- treat geometry as legal boundary;
- reduce an aggregation threshold;
- erase stale, correction, or supersession state;
- activate a source or network request;
- publish an artifact; or
- generate an authoritative legal, genetic, genealogical, or identity conclusion.

[Back to top](#top)

---

## Governed AI and generated language

Configuration may support presentation preferences for an already-governed AI or Focus Mode consumer. It cannot authorize AI to become identity, kinship, DNA, title, consent, cultural, or legal authority.

Generated language must:

- use released, resolvable evidence only;
- preserve person assertions and conflicting evidence;
- distinguish canonical projections from source truth;
- distinguish relationship assertions from hypotheses;
- distinguish DNA evidence from genealogical or legal conclusions;
- distinguish assessor/tax/parcel context from title and boundary;
- disclose source, time, confidence, uncertainty, consent, rights, stale state, correction, and supersession where material;
- abstain when identity, relationship, evidence, living status, consent, rights, cultural authority, title support, or temporal scope is insufficient;
- deny living-person, raw-DNA, private person–parcel, protected cultural, and other restricted exposure;
- deny legal, genetic-health, parentage, tribal-membership, citizenship, title-insurance, or similar authoritative conclusions; and
- remain subordinate to policy, evidence, review, consent, rights, and release state.

Configuration must not contain prompts or text that instruct a model to:

- identify or merge people from weak signals;
- infer a living person’s identity, relatives, address, ancestry, health, parentage, or DNA traits;
- promote a relationship hypothesis as fact;
- infer consent;
- ignore revocation;
- infer tribal, cultural, ethnic, clan, family, or community membership;
- state that an assessor record proves ownership;
- state that parcel geometry proves a legal boundary;
- fill a chain-of-title gap;
- expose sealed, protected, minor, adoption, donor, victim, burial, or culturally restricted context;
- suppress uncertainty, privacy, consent, rights, cultural, title, or boundary caveats.

Any AI output is interpretive and requires the applicable runtime receipt and finite outcome. This README does not establish those runtime surfaces.

[Back to top](#top)

---

## Review burden

README changes require:

- configuration or documentation review;
- People/DNA/Land domain review;
- privacy and consent boundary review; and
- cultural-rights/rights-holder boundary review.

A future payload also requires the applicable:

- named consumer owner;
- identity and record-linkage reviewer;
- genealogy and relationship-evidence reviewer;
- DNA/genomics privacy reviewer;
- consent and revocation reviewer;
- rights-holder or authorized-representative reviewer;
- cultural, tribal, sovereignty, and community-authority reviewer;
- land-record, title, legal-description, and jurisdiction reviewer;
- source-role and evidence reviewer;
- source-rights, retention, and attribution reviewer;
- aggregation, de-identification, and residual-risk reviewer;
- schema or contract reviewer;
- validation and test reviewer;
- security and privacy reviewer;
- accessibility and caveat-presentation reviewer;
- correction/cleanup reviewer; and
- policy and release reviewer.

A sensitive-lane release may require author, sensitivity reviewer, release authority, and rights-holder representative as distinct roles under the applicable maturity and materiality rules.

No reviewer may approve raw DNA for public release, infer consent, ignore revocation, treat an assessor record as title, treat parcel geometry as boundary proof, or turn configuration into identity authority.

Do not infer acceptance from a missing reviewer rule or placeholder `CODEOWNERS` entry. Owners remain `OWNER_TBD` until verified.

[Back to top](#top)

---

## Maintenance and safe change pattern

When a People/DNA/Land configuration file is added or changed:

1. identify the exact consumer, owner, purpose, and prohibited purposes;
2. re-read the parent config contract and domain doctrine;
3. verify canonical contract, schema, policy, registry, source, consent, rights, and cultural-authority references;
4. preserve assertion, candidate, canonical projection, and source-truth distinctions;
5. verify living/deceased/minor/protected/unknown handling;
6. verify identity ambiguity, conflict, false-positive, and review behavior;
7. preserve relationship assertion versus hypothesis;
8. verify raw-DNA, vendor-ID, logging, telemetry, cache, and index prohibitions;
9. verify consent purpose, scope, expiry, verifier, revocation, cleanup, and tombstone behavior;
10. verify cultural-rights, sovereignty, rights-holder, tribal, family, and community review obligations;
11. preserve assessor/tax/parcel context versus title and boundary;
12. verify instrument class, jurisdiction, legal description, gaps, overlaps, conflicts, effective dates, and supersession;
13. verify source, event, valid, recorded, effective, retrieval, release, correction, revocation, and supersession times;
14. review rights, retention, private joins, low counts, aggregation, differencing, repeated-query, graph, and reconstruction risk;
15. run deterministic parse, shape, semantic, privacy, consent, rights, negative, and no-network checks;
16. document precedence, unknown-key behavior, deactivation, tombstoning, migration, correction, withdrawal, cleanup, and rollback;
17. inspect the complete diff for secrets, live bindings, real people, DNA, consent artifacts, parcels, title assertions, cultural details, and reconstructable clues;
18. verify remote read-back and changed paths; and
19. keep configuration, source admission, identity, consent, cultural authority, evidence, policy, release, and publication as separate governed concerns.

### Change-budget discipline

A configuration PR should not silently add or alter:

- person-matching or canonicalization logic;
- genealogy or relationship inference;
- living/deceased determination;
- DNA processing, interpretation, tokenization, or de-identification;
- consent creation, verification logic, scope, or revocation policy;
- cultural-rights or sovereignty policy;
- source activation or network behavior;
- contracts or schemas;
- source-role vocabulary or mapping;
- privacy tiers, aggregation thresholds, or k-anonymity parameters;
- land-record precedence, title, legal-boundary, or chain-of-title algorithms;
- connectors, watchers, pipelines, models, or package logic;
- lifecycle data;
- receipts, proofs, consent records, or review records;
- release decisions; or
- public routes, maps, graphs, search indexes, family trees, reports, or exports.

Those changes require separate scoped implementation and review surfaces.

[Back to top](#top)

---

## Migration and anti-bypass posture

If misplaced material is found here:

1. do not treat it as authoritative merely because it is committed;
2. classify it as safe config, personal data, DNA data, consent artifact, cultural-rights material, secret/live binding, contract, schema, policy, registry, source payload, identity decision, relationship inference, land/title decision, package code, pipeline/connector/watcher code, runtime/infra, lifecycle object, trust artifact, release record, public artifact, generated output, or sensitive detail;
3. remove or quarantine credentials, live bindings, living-person data, DNA data, consent artifacts, private person–parcel joins, exact private locations, and culturally restricted context immediately;
4. rotate or revoke exposed credentials and vendor tokens as required;
5. suspend affected processing, indexing, graph projection, and public access;
6. move machine shape to `schemas/`;
7. move semantic meaning to `contracts/`;
8. move privacy, consent, cultural-rights, identity, title, sensitivity, and release rules to `policy/`;
9. move source identity, role, rights, retention, and activation state to registry/connector governance;
10. move implementation to packages, pipelines, connectors, runtime, apps, tools, or infrastructure as appropriate;
11. move lifecycle, catalog, receipt, proof, and published material to canonical `data/` lanes;
12. move consent, review, release, correction, withdrawal, supersession, cleanup, and rollback decisions to their canonical governance homes;
13. preserve provenance, source-native values, consumer impact, migration reason, exposure assessment, consent/revocation state, and rollback instructions; and
14. create a drift, correction, privacy incident, or security incident record when misplaced material was consumed or exposed.

### Anti-bypass matrix

| Bypass risk | Required response |
|---|---|
| Config treated as identity truth | Reject; identity remains evidence-bound and review-governed. |
| Config auto-merges persons | Reject; ambiguous identity abstains or holds. |
| Config promotes relationship hypothesis as fact | Reject. |
| Config exposes living-person or minor data | Deny and assess incident/correction obligations. |
| Config contains raw DNA or vendor ID | Deny, quarantine, and assess exposure. |
| Config infers or broadens consent | Reject. |
| Config ignores revocation | Stop use and invoke accepted cleanup/correction path. |
| Config substitutes for cultural or tribal authority | Reject. |
| Config treats public availability as permission | Reject. |
| Config treats assessor/tax as title | Deny. |
| Config treats parcel geometry as boundary proof | Deny. |
| Config fills chain-of-title gap | Abstain or hold. |
| Config reduces aggregation threshold | Reject; policy remains authoritative. |
| Config enables repeated-query reconstruction | Deny or hold. |
| Config hides fields only in the client | Reject; transform, restrict, or deny before public artifact generation. |
| Config duplicates contract or schema | Move meaning/shape to the canonical root and keep only references here. |
| Directory presence activates a source, linker, or DNA processor | Reject; require explicit verified binding. |
| Config writes catalog, receipt, proof, consent, review, or release records | Reject and move to canonical governance homes. |
| Public client reads this directory | Reject; public access must cross the governed API and released artifacts. |
| Watcher publishes from config | Reject; watchers and connectors may propose candidates and receipts only. |

[Back to top](#top)

---

## Definition of done for the first payload

- [ ] A named consumer, bounded purpose, prohibited purposes, and accepted owners are verified.
- [ ] The file format, version, parser, and explicit load path are verified.
- [ ] Canonical schema, contract, policy, registry, doctrine, source, consent, rights, and cultural-authority references resolve.
- [ ] The `people` versus `people-dna-land` segment conflict is resolved or the payload avoids unresolved canonical claims.
- [ ] Source-role mapping is governed and does not create aliases by configuration.
- [ ] Precedence, duplicate-key, missing-file, and unknown-key behavior are documented and tested.
- [ ] Network, source activation, person linking, DNA processing, consent action, title resolution, and publication remain disabled by file presence.
- [ ] Assertions, candidates, canonical projections, and source records remain distinct.
- [ ] Living, deceased, minor, protected, unknown, and disputed status handling is explicit and fail closed.
- [ ] Ambiguous identity produces abstention or review hold.
- [ ] Relationship assertions and hypotheses remain distinct.
- [ ] Raw DNA, vendor IDs, segment data, and correlatable pseudonyms are prohibited from config, logs, telemetry, caches, indexes, and public outputs.
- [ ] Consent purpose, scope, subject, controller, processor, expiry, verifier, and revocation behavior are explicit.
- [ ] Revocation cleanup, tombstoning, cache/index invalidation, correction, and withdrawal are tested.
- [ ] Cultural-rights, sovereignty, rights-holder, tribal, family, and community review obligations are explicit.
- [ ] Assessor and tax records cannot be labeled or queried as title.
- [ ] Parcel geometry cannot be labeled or queried as legal boundary proof.
- [ ] Land-instrument classes, jurisdiction, legal descriptions, gaps, overlaps, conflicts, effective dates, and supersession are explicit.
- [ ] Source, event, valid, recorded, effective, retrieval, release, correction, revocation, and supersession times remain distinct.
- [ ] Privacy tier and public-safe profile references come from accepted policy, not ad hoc values.
- [ ] Small-cell, aggregation, differencing, repeated-query, graph, join, and reconstruction risks are tested.
- [ ] Logging, telemetry, debugging, screenshots, caches, indexes, and exports are privacy-safe.
- [ ] Synthetic fixtures cover valid, invalid, held, denied, abstained, revoked, stale, ambiguous, conflicting, corrected, superseded, and error cases.
- [ ] No-network tests pass.
- [ ] Secret, private-endpoint, personal-path, living-person, DNA, consent, parcel, title, cultural, and protected-context scans pass.
- [ ] Migration, deactivation, tombstoning, cleanup, correction, withdrawal, and rollback behavior are tested.
- [ ] No identity, relationship, DNA, consent, title, public layer, API route, release, or publication is activated by file presence.
- [ ] Repository-native checks are substantive or their scaffold limitations are stated explicitly.

[Back to top](#top)

---

## Related folders

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/people-dna-land/README.md`](../../../docs/domains/people-dna-land/README.md) — People/Genealogy/DNA/Land doctrine, object families, T4 defaults, consent, title, validation, and lifecycle posture.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — canonical lane and sensitivity register.
- [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) — unresolved path and authority drift.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement and responsibility law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — credential and sensitive-value handling.

Future files should link to verified People/DNA/Land contracts, schemas, privacy/consent/cultural policy, source descriptors, consent verifiers, identity methods, title methods, tests, fixtures, receipts, proofs, review records, cleanup records, and release records only after those exact paths and authority relationships are confirmed.

[Back to top](#top)

---

## ADRs and drift triggers

No ADR is introduced by this README.

Separate governance is required for changes that would:

- add, rename, merge, or retire a canonical domain slug;
- resolve `people` versus `people-dna-land` segment naming;
- change source-role vocabulary or mapping;
- define person identity or canonicalization methods;
- define living/deceased/minor/protected-person rules;
- define genealogy or relationship-evidence thresholds;
- define DNA processing, tokenization, inference, research, or de-identification rules;
- define consent formats, scope, purpose, expiry, delegation, revocation, or cleanup;
- define cultural-rights, sovereignty, rights-holder, tribal, family, or community authority;
- define privacy tiers, aggregation, k-anonymity, suppression, differencing, or residual-risk acceptance;
- define land-record precedence, title, legal-boundary, chain-of-title, or legal-review rules;
- decide source rights, retention, redistribution, or live-source activation;
- establish universal config discovery, precedence, or unknown-key behavior;
- create a parallel contract, schema, policy, registry, consent, review, receipt, proof, or release authority;
- authorize direct public access to internal or canonical stores;
- change lifecycle, evidence, correction, revocation, withdrawal, promotion, or release separation; or
- introduce a direct public route to configuration material.

Configuration must not be used to settle these decisions indirectly.

[Back to top](#top)

---

## Rollback, correction, and revocation

Before merge, rollback means closing the unmerged pull request and abandoning the scoped branch when separately authorized.

After merge, create a transparent revert commit or revert pull request that restores the prior known-good README or configuration version. Do not force-push or rewrite shared history.

For a future payload correction or revocation:

1. disable or stop selecting the affected configuration through the verified consumer mechanism;
2. stop affected source ingestion, identity linking, DNA processing, graph projection, indexing, map generation, search, export, and AI workflows;
3. preserve the faulty configuration and non-sensitive evidence needed for review;
4. identify affected people, assertions, relationships, DNA derivatives, consent scopes, person–parcel joins, title views, caches, indexes, graphs, tiles, exports, screenshots, and narratives without reproducing protected content;
5. assess whether living-person, minor, DNA, consent, cultural-rights, private-land, title, or boundary information was exposed or misclassified;
6. honor valid revocation and applicable deletion/tombstone/withdrawal duties;
7. invalidate affected caches, indexes, graph projections, embeddings, exports, and downstream derivatives;
8. restore the prior known-good version or safe disabled state;
9. re-run validation and negative cases;
10. create required privacy/security incidents, `RevocationReceipt`, correction, withdrawal, redaction, review, release, or rollback records in their canonical homes; and
11. verify that no public or restricted surface continues to serve unauthorized, revoked, stale, misidentified, misrelated, mistitled, or reconstructable material.

A Git revert does not itself:

- withdraw exposed data;
- revoke access;
- complete deletion or tombstoning;
- invalidate a cache, search index, graph, embedding, tile, or export;
- correct identity, kinship, DNA, title, boundary, consent, or cultural-rights claims;
- notify downstream consumers; or
- establish KFM publication lineage.

[Back to top](#top)

---

## Safe language rules

Use language such as:

- “source-attributed person assertion”;
- “derived identity candidate — review required”;
- “evidence-bound canonical projection, not a sovereign source”;
- “relationship hypothesis, not verified kinship”;
- “living status unknown — public exposure denied”;
- “raw DNA denied; no public-transform path”;
- “purpose-bound consent profile reference”;
- “revocation requires governed cleanup”;
- “administrative assessor context — not title”;
- “parcel geometry — not legal boundary proof”;
- “chain-of-title gap remains unresolved”;
- “public-safe aggregate subject to accepted privacy policy and release review”;
- “bounded search found no indexed executable consumer”;
- “configuration aid, not authority.”

Avoid unsupported claims such as:

- “these records are the same person”;
- “this is the person’s family”;
- “DNA proves the relationship”;
- “this kit belongs to this person”;
- “this person is deceased” without accepted evidence and review;
- “upload means consent”;
- “consent covers future uses”;
- “revocation can wait until the next release”;
- “public record means unrestricted”;
- “this person is a tribal member”;
- “the assessor says they own it”;
- “the parcel line is the legal boundary”;
- “the title chain is complete” when gaps or conflicts exist;
- “the aggregate is anonymous” without accepted disclosure-risk proof;
- “this config is validated by CI” when workflows are scaffolding;
- “this setting authorizes public display”;
- “this folder contains the operational People/DNA/Land configuration.”

[Back to top](#top)

---

## Last reviewed

**2026-07-14**, against `main@5b8b9e52d7e1a78d2cfa87f74934a984eed2bba0`.

Review again before the first non-README payload, consumer binding, loader or precedence decision, identity-review profile, living-status profile, DNA profile, consent or revocation profile, cultural-rights profile, privacy/aggregation profile, land/title profile, source activation, graph/search integration, or public-output integration.

<details>
<summary>Appendix A — no-loss preservation note</summary>

The v0.1 README established the correct core boundary: no identity, kinship, DNA, consent, title, cultural-rights, evidence, or release authority; no real living-person, DNA, genealogy, parcel, title, or reconstructable data; and fail-closed review. v0.2 preserves those controls while grounding the lane in the current bounded repository snapshot and adding explicit consumer binding, assertion-first identity, living/deceased uncertainty, relationship-hypothesis separation, raw-DNA and logging prohibitions, purpose-bound consent and revocation cleanup, cultural-rights and sovereignty review, assessor/title and parcel/boundary anti-collapse, chain-of-title gap handling, temporal semantics, reconstruction-risk controls, finite failure behavior, governed AI restrictions, and a concrete first-payload definition of done.

</details>
