<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-archaeology-readme
title: configs/domains/archaeology/ — Archaeology Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Archaeology steward · Cultural/sovereignty reviewer · Consumer owner
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; archaeology; sovereignty-aware; sensitive-location-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/archaeology/README.md
truth_posture: CONFIRMED canonical archaeology slug, repository-present parent config contract, repository-present Archaeology and Cultural Heritage doctrine, exact-location denial default, and documentation-only lane / PROPOSED future consumer-bound templates / UNKNOWN consumers, precedence, loader behavior, and enforcement / NEEDS VERIFICATION owners, executable validation, cultural authority, rights review, sensitivity transforms, and runtime binding
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/archaeology/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
notes:
  - "This lane contains documentation only. It does not create, load, activate, expose, or publish an Archaeology configuration payload."
  - "v0.2 expands the Archaeology-specific scope, cultural-authority, sovereignty, exact-location, looting-risk, validation, correction, and rollback contract without creating a new policy, schema, registry, consent, or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Domain Configuration

`configs/domains/archaeology/`

> Safe-to-commit, Archaeology-specific configuration documentation and future consumer-bound templates. This lane does not own archaeological truth, cultural authority, consent, sensitivity, source admission, evidence, release, or publication.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Scope](#scope) · [Inputs](#inputs) · [Outputs](#outputs) · [Configuration contract](#minimum-configuration-contract) · [Cultural and location safety](#cultural-authority-sovereignty-and-location-safety) · [Validation](#validation) · [Failure behavior](#failure-behavior) · [Maintenance](#maintenance) · [Related](#related-folders) · [ADRs](#adrs) · [Rollback](#rollback-and-correction)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`  
> **Component maturity:** documentation boundary only  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for truth and governance  
> **Runtime posture:** no Archaeology payload, loader, consumer binding, activation, or public exposure is established by this README

> [!CAUTION]
> Exact or reconstructable archaeological locations, burial or human-remains information, sacred places, restricted cultural knowledge, collection-security details, private-land context, and looting-risk clues fail closed. Directory presence, a future configuration file, or a parsed value must never lower sensitivity, bypass cultural or steward review, grant consent, activate a source, promote lifecycle state, authorize release, or create KFM publication.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Archaeology and Cultural Heritage lane.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should behave, but they cannot decide whether a site is confirmed, who holds cultural authority, whether consent exists, whether sensitive detail may be exposed, or whether an artifact may be released.

This README is intended for:

- Archaeology domain stewards;
- cultural, Tribal, sovereignty, and steward reviewers;
- configuration and developer-experience maintainers;
- privacy, rights, sensitivity, policy, security, and release reviewers;
- package, pipeline, app, runtime, test, and tooling owners that may consume Archaeology configuration;
- reviewers checking Directory Rules placement and trust-membrane integrity.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Archaeology domain meaning | **None.** Domain doctrine remains in [`docs/domains/archaeology/`](../../../docs/domains/archaeology/README.md). |
| Cultural authority, sovereignty, or consent | **None.** Configuration cannot identify the rightful authority, record consent, or replace cultural and steward review. |
| Site confirmation or interpretation | **None.** A setting cannot convert a candidate, anomaly, model output, oral account, or contextual clue into a confirmed archaeological site. |
| Source identity, role, rights, and activation | **None.** These require the applicable source registry, connector, policy, rights, and review surfaces. |
| Schema or contract shape | **None.** Configuration may reference a verified schema or contract but must not duplicate or redefine it. |
| Policy, sensitivity, or exact-location decision | **None.** A value may select an already-governed profile; it cannot create or weaken policy, tiering, denial, or generalization rules. |
| Evidence or claim truth | **None.** Configuration cannot create an `EvidenceBundle`, validate a claim, or make generated interpretation sovereign truth. |
| Release or publication | **None.** Configuration cannot authorize promotion, release, public display, or KFM publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file under an explicit binding and precedence rule. |

A configuration value may point to an authority surface. It does not become authority by repetition, proximity, successful parsing, or operational convenience.

[Back to top](#top)

---

## Status

| Item | State | Safe conclusion |
|---|---:|---|
| Canonical domain slug | **CONFIRMED** | `archaeology` is a repository-present canonical domain lane. |
| Parent configuration contract | **CONFIRMED** | [`configs/domains/README.md`](../README.md) defines this path as a non-secret, non-authoritative configuration sublane. |
| Archaeology doctrine | **CONFIRMED repository-present** | The domain README establishes candidate-vs-confirmed separation and exact-location denial by default. |
| Current lane content | **CONFIRMED** | This README is the only verified content in this directory at the inspected base. |
| Executable payloads | **NOT ESTABLISHED** | No defaults, templates, examples, or live bindings are established here. |
| Consumer and loader | **UNKNOWN** | No consumer, parser, discovery mechanism, merge order, or unknown-key behavior is established by this README. |
| Cultural and steward review mechanism | **NEEDS VERIFICATION** | Required in principle; current owners, records, and enforcement are not proven here. |
| Sensitivity transform and release gates | **NEEDS VERIFICATION** | Must be governed elsewhere and cannot be inferred from configuration presence. |
| CI and validation enforcement | **NEEDS VERIFICATION** | Expectations are documented; executable enforcement requires repository evidence. |

Directory presence must not trigger discovery, source activation, network access, geometry exposure, indexing, map-layer creation, AI interpretation, lifecycle promotion, or publication.

[Back to top](#top)

---

## Scope

### What belongs here

Only safe, non-secret, Archaeology-specific configuration material for a named or explicitly proposed consumer belongs here.

- this configuration-boundary README;
- small `*.template.*` files using synthetic placeholders only;
- small `*.example.*` files with impossible or obviously fictional identifiers and geometry;
- conservative deny, hold, abstain, generalize, redact, or review-routing defaults;
- display profile names that refer to already-governed sensitivity and release rules;
- migration notes tied to a verified consumer, key, version, and rollback path;
- validation notes grounded in repository-supported tooling.

### What does not belong here

- exact or reconstructable archaeological-site geometry;
- burial, human-remains, funerary, sacred-place, ceremonial, or restricted cultural information;
- looting-risk indicators, collection-security detail, storage locations, access-control detail, or vulnerable-site clues;
- real site identifiers, survey records, private landowner context, oral histories, cultural identifiers, or source payloads;
- credentials, tokens, private endpoints, workstation paths, internal deployment bindings, or environment-specific secrets;
- settings that assert cultural authority, consent, affiliation, custody, repatriation status, eligibility, legal status, or access rights;
- settings that convert remote-sensing anomalies, LiDAR candidates, model outputs, historical routes, parcels, or contextual correlations into confirmed sites;
- policy, registry, schema, contract, receipt, proof, review, consent, release, correction, or publication authority;
- lifecycle data from RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED stores.

### Explicit non-ownership

This lane may reference verified outputs from other responsibility roots, but it must not redefine them. In particular, it does not own:

- archaeological object meaning or ubiquitous language;
- source descriptors, rights decisions, or source activation;
- sensitivity tiers or cultural-policy rules;
- EvidenceBundles, receipts, proofs, manifests, or release decisions;
- site, survey, artifact, feature, context, chronology, or collection records;
- people, land, title, geology, hazards, routes, or other cross-domain truth.

[Back to top](#top)

---

## Inputs

Any future configuration payload requires all of the following before it may be treated as implementation-supporting:

1. a named consumer and owning path;
2. a declared format and version;
3. a verified load or binding point;
4. an explicit precedence and override rule;
5. a canonical schema or contract reference when one exists;
6. synthetic placeholders rather than real sites, people, collections, or restricted knowledge;
7. documented source-role handling that preserves candidate, observation, interpretation, and confirmation distinctions;
8. cultural, Tribal, sovereignty, rights, sensitivity, privacy, security, and release review as applicable;
9. no-network fixtures and deterministic validation;
10. finite failure behavior and a rollback target.

A proposed payload remains inert until these conditions are verified. File presence alone is not activation.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future file may support a verified consumer by selecting conservative behavior such as:

- deny or hold exact geometry;
- choose a previously approved generalization or redaction profile;
- route unresolved cultural or sensitivity cases to review;
- preserve candidate-vs-confirmed distinctions;
- require evidence, review, and release references before public rendering;
- disable network access or public output when required references are missing.

It cannot itself:

- expose or confirm a site;
- identify cultural authority or grant consent;
- lower a sensitivity tier;
- activate a source or connector;
- create evidence, receipts, proofs, manifests, or release state;
- authorize public display or KFM publication.

[Back to top](#top)

---

## Minimum configuration contract

Every future file in this lane should document, adjacent to the file or in its owning consumer documentation:

| Contract field | Required meaning |
|---|---|
| Consumer | Exact package, service, pipeline, app, test, or tool that reads the file. |
| Purpose | The narrow behavior the file configures. |
| Format and version | YAML, JSON, TOML, or other verified format plus version or schema binding. |
| Activation | Explicit load path; no directory auto-discovery by assumption. |
| Precedence | Merge order, override rules, and environment interaction. |
| Unknown-key behavior | Reject, warn, or ignore behavior; fail closed where risk matters. |
| Defaults | Conservative behavior when keys or references are absent. |
| Authority references | Canonical policy, schema, contract, source, review, or release surfaces referenced—not copied. |
| Source-role handling | How candidates, observations, interpretations, and confirmations remain distinct. |
| Cultural review behavior | Required hold, deny, or review outcome when cultural authority, consent, or restriction is unresolved. |
| Location safety | Exact and reconstructable geometry denial, generalization, redaction, and side-channel controls. |
| Rights and privacy | Terms, attribution, private-land, living-person, collection, and restricted-knowledge handling. |
| Validation | Parser, schema, semantic, no-network, negative, and sensitivity checks. |
| Failure outcomes | Finite outcomes such as `ANSWER`, `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` where repository contracts define them. |
| Rollback | Prior known-good version, responsible owner, and validation after revert. |

Do not create a payload whose consumer, authority references, sensitivity behavior, or rollback cannot be verified.

[Back to top](#top)

---

## Cultural authority, sovereignty, and location safety

Archaeology configuration must preserve the doctrine that exact-location denial is the default.

### Permanent safety boundaries

Configuration must not provide a switch that disables or bypasses:

- protection of burial sites, human remains, funerary objects, or associated records;
- protection of sacred, ceremonial, culturally restricted, or sovereignty-sensitive places and knowledge;
- cultural, Tribal, steward, rights, and sensitivity review requirements;
- candidate-vs-confirmed distinctions;
- exact-location denial, generalization, redaction, or staged-access controls;
- collection and repository security controls;
- cite-or-abstain behavior and EvidenceBundle resolution;
- release, correction, and rollback requirements.

### Side-channel and reconstruction safety

Validation must consider whether apparently harmless values can reconstruct protected information through:

- bounding boxes, centroids, tile IDs, grid cells, zoom thresholds, or query windows;
- deterministic hashes, stable identifiers, filenames, or cache keys;
- combined public layers, route proximity, parcel context, terrain features, or imagery references;
- counts, timing, rarity, collection references, or descriptive text;
- logs, error messages, debug output, fixtures, screenshots, or generated examples.

When reconstruction risk cannot be ruled out, the safe outcome is `DENY`, `HOLD`, or `ABSTAIN` according to the governing contract—not best-effort exposure.

### Governed AI posture

No configuration may allow generated language, classification, reconstruction, anomaly scoring, image interpretation, or spatial inference to become site confirmation or sovereign truth. AI output remains interpretive and evidence-subordinate.

[Back to top](#top)

---

## Validation

### Documentation-only validation

For this README:

- one H1 and logical heading order are preserved;
- repository-relative links and anchors resolve;
- the file ends with a newline;
- no secret, private endpoint, real site, cultural identifier, protected geometry, collection-security detail, or reconstructable clue is present;
- archaeology doctrine and the parent config boundary are not contradicted;
- no new schema, policy, registry, consent, review, release, receipt, proof, or publication authority is created.

### Future payload validation

Before any non-README file is accepted, verify:

- deterministic parsing and schema validation;
- explicit consumer binding and precedence;
- rejection or safe handling of unknown keys;
- synthetic no-network fixtures;
- valid, invalid, denied, held, abstained, quarantined, and error cases;
- candidate-vs-confirmed separation;
- exact and reconstructable location denial;
- burial, human-remains, sacred-site, restricted-knowledge, and looting-risk controls;
- cultural, Tribal, sovereignty, steward, rights, privacy, security, and release gates;
- source-role, evidence, lifecycle, review, and release references;
- correction and rollback behavior;
- absence of secrets and real sensitive data.

Executable configuration validation is `NOT APPLICABLE` while this lane contains documentation only.

A passing parser or schema test does not prove cultural authority, consent, site confirmation, rights clearance, policy approval, release readiness, or public safety.

[Back to top](#top)

---

## Failure behavior

Future consumers must use finite, reviewable outcomes. Where repository contracts define these outcomes, use them consistently:

| Condition | Minimum safe behavior |
|---|---|
| Missing or invalid configuration | `ERROR` or conservative built-in denial; never permissive fallback. |
| Unknown key affecting risk | Reject or `HOLD`; do not ignore silently. |
| Cultural authority or consent unresolved | `HOLD`, `DENY`, or `ABSTAIN`. |
| Exact-location or reconstruction risk unresolved | `DENY` or approved generalization only. |
| Burial, human-remains, sacred-site, or restricted-knowledge involvement | `DENY` or `HOLD` pending the required authority and review. |
| Candidate presented as confirmed | Reject, relabel, or `ABSTAIN`; do not publish as fact. |
| Rights, attribution, or redistribution unclear | `HOLD`, `DENY`, or `ABSTAIN`. |
| Missing evidence, review, release, or rollback reference | Do not promote or render as authoritative. |
| Source or consumer unavailable | Fail closed without stale-state overclaiming. |

Configuration errors must not reveal sensitive values, site clues, cultural identifiers, private paths, or protected source details in logs or user-facing messages.

[Back to top](#top)

---

## Maintenance

README changes require configuration/docs, Archaeology, and cultural/sovereignty review.

Any future payload change additionally requires the relevant:

- consumer owner;
- schema or contract owner;
- source and rights reviewer;
- cultural, Tribal, sovereignty, and steward reviewer;
- sensitivity, privacy, security, and geoprivacy reviewer;
- validation and fixture owner;
- policy and release reviewer;
- correction and rollback owner.

Before changing or adding a payload:

- confirm the exact consumer and current branch state;
- inspect Directory Rules, accepted ADRs, the drift register, and adjacent conventions;
- search for an existing canonical or semantically equivalent config;
- preserve stable keys unless a migration and rollback are defined;
- update examples and fixtures atomically when repository convention requires it;
- record behavior-changing or authority-significant changes through the required ADR, version, correction, or supersession process;
- verify the remote diff contains no unrelated paths.

### Definition of done for the first payload

- [ ] Consumer and owner are verified.
- [ ] Format, version, schema, and precedence are documented.
- [ ] Unknown-key and missing-file behavior fail closed.
- [ ] Cultural authority, consent, rights, and sensitivity gates are identified.
- [ ] Candidate-vs-confirmed separation is tested.
- [ ] Exact-location and reconstruction-risk denial is tested.
- [ ] Burial, human-remains, sacred-site, restricted-knowledge, and looting-risk cases are tested.
- [ ] No-network valid, invalid, denied, held, abstained, and error fixtures exist.
- [ ] No secrets or real sensitive data are committed.
- [ ] Rollback and correction behavior are verified.
- [ ] Presence of the file does not create activation, release, or publication.

[Back to top](#top)

---

## Related folders

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/archaeology/README.md`](../../../docs/domains/archaeology/README.md) — Archaeology and Cultural Heritage doctrine.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — lane and sensitivity register.
- [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) — unresolved repository/doctrine drift.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

These links identify related authority or review surfaces. Their presence does not prove that every proposed Archaeology schema, policy, validator, fixture, consumer, or release artifact exists or is active.

[Back to top](#top)

---

## ADRs

No ADR is introduced by this README.

An ADR or equivalent governance decision is required before configuration is used to change:

- the canonical domain set or responsibility-root placement;
- cultural authority, consent, sovereignty, or permanent denial boundaries;
- exact-location, burial, human-remains, sacred-site, restricted-knowledge, or looting-risk protections;
- schema or contract authority;
- universal config discovery, precedence, or activation behavior;
- release, publication, correction, or rollback authority.

Configuration must not be used as a shortcut around those decisions.

[Back to top](#top)

---

## Rollback and correction

Before merge, rollback normally means closing or abandoning the unmerged review branch after preserving review evidence. After merge, create a transparent revert commit or revert pull request and rerun the applicable validation. Do not rewrite shared history.

For a behavior-changing configuration correction:

1. identify the affected consumer, version, and exposure window;
2. disable or hold unsafe behavior without revealing protected details;
3. preserve evidence, review, and operation records in their canonical homes;
4. restore the last verified safe configuration or conservative built-in denial;
5. rerun parser, schema, sensitivity, cultural-review, no-network, and negative tests;
6. issue any required correction, withdrawal, supersession, or rollback record;
7. verify that derived maps, indexes, caches, exports, and generated language no longer expose or imply the unsafe state.

A Git revert alone may not correct already released or externally relied-on information. Follow the governing correction and publication process.

[Back to top](#top)

---

## Last reviewed

**2026-07-13**, against `main@a5015c9047f6211a575748485a7485cc7271a6d1`. Review again before the first non-README payload, consumer binding, cultural-review integration, or runtime activation.
