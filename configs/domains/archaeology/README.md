<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-archaeology-readme
title: configs/domains/archaeology/ — Governed Archaeology and Cultural Heritage Configuration Boundary
type: readme
version: v0.3
status: draft
owners: OWNER_TBD — Config steward · Archaeology steward · Cultural/Tribal/sovereignty reviewer · Rights-holder representative · Human-remains and burial reviewer · Collection-security steward · Source steward · Consumer owner · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-07-13
updated: 2026-07-14
policy_label: "public; config-sublane; archaeology; cultural-heritage; sovereignty-aware; consent-and-revocation-aware; exact-location-deny; burial-and-sacred-site-deny; collection-security-aware; source-role-aware; candidate-not-site; non-secret; non-authoritative; no-live-binding; no-site-confirmation; no-cultural-authority; no-release-authority"
current_path: configs/domains/archaeology/README.md
truth_posture: CONFIRMED canonical Archaeology config lane, parent configuration contract, repository-present Archaeology doctrine and implementation-shaped surfaces, README-only bounded config inventory, exact-location denial doctrine, current contract-home reconciliation, object-family and short-name compatibility conflicts, placeholder/scaffold status of inspected package metadata and code, pipeline entrypoints, pipeline specs, policy files, schemas, validators, source records, published-layer registry, UI files, and domain workflow, and prior README lineage / PROPOSED future consumer-bound templates and accepted profile references / CONFLICTED Site versus ArchaeologicalSite, collapsed versus decomposed object-family names, publication-transform terminology, policy-home layering, and source-registry topology / UNKNOWN direct consumers, loader behavior, precedence, deployment binding, exhaustive recursive inventory, runtime behavior, and publication use / NEEDS VERIFICATION accepted owners and named authorities, cultural and Tribal review, rights-holder representation, consent and revocation records, source roles and rights, exact-location transform floors, collection-security controls, object identity, chronology methods, schema completeness, executable validation, policy-runtime binding, scanners, CI enforcement, correction propagation, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 5049e03434f9b6880464605a5eb31c843bb7e450
  prior_blob: e429009d4877428c46f4a77c48857ec26c13f0e2
  bounded_path_search: configs/domains/archaeology/README.md only
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/archaeology/README.md
  - ../../../docs/domains/archaeology/ARCHITECTURE.md
  - ../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../docs/domains/archaeology/DATA_LIFECYCLE.md
  - ../../../docs/domains/archaeology/API_CONTRACTS.md
  - ../../../docs/domains/archaeology/CROSS_DOMAIN.md
  - ../../../docs/domains/archaeology/CONTINUITY_INVENTORY.md
  - ../../../docs/domains/archaeology/ubiquitous-language.md
  - ../../../docs/domains/archaeology/source-families.md
  - ../../../docs/domains/archaeology/sensitivity-and-publication-posture.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
  - ../../../contracts/domains/archaeology/
  - ../../../schemas/contracts/v1/domains/archaeology/
  - ../../../policy/domains/archaeology/
  - ../../../policy/sensitivity/archaeology/
  - ../../../data/registry/sources/archaeology/
  - ../../../data/registry/archaeology/sources/
  - ../../../packages/domains/archaeology/
  - ../../../pipelines/domains/archaeology/
  - ../../../pipeline_specs/archaeology/
  - ../../../tools/validators/domains/archaeology/
  - ../../../tests/domains/archaeology/
  - ../../../fixtures/domains/archaeology/
  - ../../../apps/explorer-web/src/features/domains/archaeology/
  - ../../../data/raw/archaeology/
  - ../../../data/work/archaeology/
  - ../../../data/quarantine/archaeology/
  - ../../../data/processed/archaeology/
  - ../../../data/catalog/domain/archaeology/
  - ../../../data/triplets/archaeology/
  - ../../../data/published/layers/archaeology/
  - ../../../data/receipts/archaeology/
  - ../../../data/proofs/archaeology/
  - ../../../release/candidates/archaeology/
  - ../../../release/manifests/archaeology/
  - ../../../docs/adr/ADR-archaeology-source-roles.md
  - ../../../docs/adr/ADR-archaeology-exact-location-policy.md
  - ../../../.github/workflows/domain-archaeology.yml
tags: [kfm, configs, archaeology, cultural-heritage, sites, surveys, artifacts, contexts, lidar, remote-sensing, geophysics, collections, chronology, cultural-review, sovereignty, consent, exact-location, looting-risk, source-role, no-secrets, governance]
notes:
  - "The bounded repository search for configs/domains/archaeology returned this README only. No executable Archaeology configuration payload or indexed direct consumer was found."
  - "The prior v0.2 README already carried strong exact-location, cultural-authority, sovereignty, burial, sacred-site, collection-security, candidate-vs-confirmed, reconstruction-risk, validation, correction, and rollback controls. v0.3 preserves them and adds current repository evidence, implementation maturity, object/path conflicts, source-registry topology, and stricter first-payload gates."
  - "The repository contains many Archaeology implementation-shaped files, but inspected package code, pipeline files, declarative specs, schemas, validators, source records, public-layer registry, UI files, and workflow jobs are greenfield placeholders, empty-stage specs, empty-permissive schemas, NotImplemented entrypoints, PROPOSED records, placeholder exports, or TODO-only jobs."
  - "Opened policy files are scaffolds rather than verified enforcement. Several default to allow=false, while precise-coordinate redaction stubs explicitly say no real rules yet and default deny=false. Configuration must not activate or rely on those stubs as a safety control."
  - "Repository evidence preserves Site versus ArchaeologicalSite and other object-family naming conflicts, segmented versus lineage contract/schema paths, policy-home layering, and subtype-first versus domain-first source-registry paths. This lane does not resolve, alias, or duplicate those conflicts."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Archaeology and Cultural Heritage Domain Configuration

`configs/domains/archaeology/`

> Safe-to-commit configuration documentation and future consumer-bound templates for archaeological surveys, site and feature candidates, artifact and provenience records, excavation and stratigraphic context, remote sensing and LiDAR anomalies, geophysics, 3D documentation, chronology, collections, cultural review, sensitivity transforms, and public-safe derivatives. This lane is not archaeological truth, cultural authority, consent, site confirmation, collection custody, exact-location clearance, evidence, policy, or release authority.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.3-informational)
![authority](https://img.shields.io/badge/authority-config__sublane-green)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![location](https://img.shields.io/badge/exact__location-deny__by__default-red)
![cultural](https://img.shields.io/badge/cultural__authority-defer__to__named__authority-purple)
![secrets](https://img.shields.io/badge/secrets-forbidden-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs-and-drift-triggers) · [Last reviewed](#last-reviewed) · [Scope](#scope-and-bounded-context) · [Classes](#configuration-classes) · [Contract](#minimum-configuration-contract) · [Binding](#consumer-binding-precedence-and-discovery) · [Objects](#archaeology-object-family-boundaries) · [Identity](#identity-alias-and-candidate-promotion) · [Roles](#source-role-and-knowledge-character) · [Cultural authority](#cultural-authority-sovereignty-consent-and-revocation) · [Location](#exact-location-reconstruction-and-looting-risk) · [Burial](#burial-human-remains-sacred-and-funerary-material) · [Collections](#collections-custody-repatriation-and-security) · [Time](#chronology-time-and-uncertainty) · [Remote sensing](#remote-sensing-lidar-geophysics-and-three-dimensional-documentation) · [Joins](#cross-domain-context-and-anti-confirmation) · [Logging](#logging-telemetry-caches-and-derived-indexes) · [Failure](#failure-behavior) · [AI](#governed-ai-and-generated-language) · [Migration](#migration-and-anti-bypass-posture) · [Rollback](#rollback-correction-withdrawal-and-invalidation) · [Done](#definition-of-done-for-the-first-payload)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.3`  
> **Observed lane maturity:** README-only in the bounded config-path search; no executable Archaeology configuration payload or direct consumer binding is established  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for archaeological meaning, cultural authority, consent, site identity, sensitivity, policy, evidence, review, or release  
> **Runtime posture:** no loader, precedence rule, source activation, network fetch, anomaly analysis, site confirmation, map layer, public lookup, AI interpretation, release, or publication is established by this README

> [!CAUTION]
> Exact or reconstructable archaeological locations, burial and human-remains information, sacred or ceremonial places, culturally restricted knowledge, collection-security details, private-land context, and looting-risk clues fail closed. A configuration value cannot convert a candidate into a site, identify the rightful cultural authority, establish consent or waiver, lower sensitivity, make a permissive scaffold safe, or authorize public exposure.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical `archaeology` domain segment under `configs/domains/`.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should parse, validate, route, label, generalize, redact, render, or package already-governed Archaeology material, but they cannot decide:

- whether an archaeological site, component, artifact, feature, context, excavation unit, stratigraphic unit, chronology, collection, anomaly, or candidate is true;
- whether `Site` and `ArchaeologicalSite`, `LiDARCandidate` and `CandidateFeature`, or other overlapping names are equivalent;
- whether a remote-sensing anomaly, LiDAR return, geophysics observation, historic source, oral history, route correlation, terrain pattern, or model score confirms a site;
- who holds cultural authority, sovereignty, custodial authority, consent authority, or rights-holder standing;
- whether consent exists, remains current, was revoked, was limited, or applies to a new use;
- whether a place, narrative, object, collection, image, recording, or category is sacred, restricted, community-controlled, or appropriate for KFM representation;
- whether exact, buffered, generalized, delayed, or fully denied geometry is appropriate;
- whether burial, human remains, funerary objects, associated records, or sacred-place context may be processed or exposed;
- whether collection ownership, lawful custody, repository status, repatriation status, access permission, or legal disposition is established;
- whether a source is admitted, active, rights-cleared, current, redistributable, or authoritative for a requested claim;
- whether evidence supports a claim;
- whether an artifact may be promoted, released, rendered, indexed, searched, exported, summarized, or published.

This README is intended for configuration maintainers, Archaeology stewards, cultural and Tribal reviewers, rights-holder representatives, human-remains and burial reviewers, collection-security stewards, source and evidence stewards, consumer owners, validation owners, policy and release reviewers, security reviewers, and contributors checking Directory Rules placement.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Archaeology domain meaning | **None.** Human doctrine remains under `docs/domains/archaeology/`; semantic meaning remains in accepted contract homes. |
| Cultural knowledge substance | **None.** KFM defers to the named authority; config cannot translate, normalize, reinterpret, or claim ownership of community-controlled meaning. |
| Cultural authority and sovereignty | **None.** Config cannot choose the authority, reviewer, rights-holder, or community representative by convenience. |
| Consent and revocation | **None.** Config may reference an accepted live consent/revocation record; it cannot create consent, infer consent, waive review, or ignore revocation. |
| Site and object identity | **None.** Config cannot merge aliases, promote candidates, or resolve object-family conflicts. |
| Source identity, role, rights, and activation | **None.** Config may reference reviewed source/profile IDs; it cannot admit, activate, suspend, retire, or supersede a source. |
| Exact-location or sensitivity disposition | **None.** Config may select an accepted transform profile; it cannot define the public floor, lower a tier, or authorize exact exposure. |
| Burial, human remains, sacred sites, funerary objects | **None.** Config cannot grant processing, access, display, or release permission. |
| Collection custody, ownership, repatriation, access | **None.** Config cannot determine legal, cultural, ethical, or custodial status. |
| Chronology and interpretation | **None.** Config may reference an accepted method; it cannot make a date, period, affiliation, or interpretation certain. |
| Evidence and claim truth | **None.** Config cannot create an `EvidenceBundle`, close proof, validate a claim, or convert a candidate into truth. |
| Policy and review | **None.** Config cannot substitute for executable policy, CulturalReview, StewardReview, ReviewRecord, or named-authority decision. |
| Release and publication | **None.** Config cannot authorize lifecycle promotion, public map/API/UI use, export, Focus Mode, AI response, or publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file through explicit binding and deterministic precedence. |

A configuration value may point to authority. It cannot acquire that authority through naming, file placement, parsing, repetition, successful validation, or operational convenience.

[Back to top](#top)

---

## Status

### Repository snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Repository ID | `1059091169` |
| Visibility | public |
| Base ref | `main` |
| Base commit | `5049e03434f9b6880464605a5eb31c843bb7e450` |
| Prior target blob | `e429009d4877428c46f4a77c48857ec26c13f0e2` |
| Bounded config search | `configs/domains/archaeology/README.md` only |

The bounded search result is not a complete recursive filesystem receipt. Differently named, generated, unindexed, branch-only, or future files remain `UNKNOWN` until directly inspected.

### Current evidence matrix

| Surface | Inspected evidence | Status | Safe conclusion |
|---|---|---:|---|
| Config lane | This README only in bounded search | **README-ONLY** | No payload or consumer is established. |
| Parent config contract | `configs/domains/README.md` v0.4 | **CONFIRMED** | No secrets, no authority, no automatic activation. |
| Archaeology doctrine | README, canonical paths, cultural review, sensitivity/publication docs | **CONFIRMED DOCUMENTS / DRAFT** | Strong fail-closed doctrine; runtime enforcement remains separate. |
| Contract lane | Rich README and object contracts | **CONFIRMED DRAFTS** | Meaning surfaces exist; naming and coverage remain incomplete/conflicted. |
| `Site` naming | `site.md` is compatibility; object map expects `ArchaeologicalSite` | **CONFLICTED** | Config must not choose an alias or canonical family. |
| Package metadata | `pyproject.toml` version `0.0.0` | **GREENFIELD** | Package maturity is not established. |
| Package code | `layers.py` contains only a placeholder comment | **PLACEHOLDER** | No working layer helper is proven. |
| Pipeline code | Inspected ingest, validate, catalog, triplets, rollback files are placeholders | **PLACEHOLDER** | No executable pipeline behavior is proven. |
| Pipeline specs | Inspected specs contain `stages: []` | **EMPTY STAGE LISTS** | No declarative execution is wired. |
| Policy modules | Generated files are `PROPOSED`; precise-coordinate stubs say no real rules yet | **SCAFFOLD / MIXED DEFAULTS** | Presence is not policy enforcement. |
| Schema files | Opened schemas have empty `properties` and `additionalProperties: true` | **PROPOSED PERMISSIVE SCAFFOLDS** | They do not meaningfully validate Archaeology objects. |
| Validator files | Opened validators raise `NotImplementedError` | **NOT IMPLEMENTED** | No executable domain validation is proven. |
| Source-role and source files | Opened YAML files are `PROPOSED` placeholders/TBD templates | **PLACEHOLDER** | No source is admitted or active. |
| Registry topology | Both subtype-first and domain-first paths exist | **CONFLICTED / NEEDS VERIFICATION** | Do not maintain divergent records. |
| Published-layer registry | File exists but says `status: PROPOSED` and placeholder | **NOT A RELEASE** | Path presence does not prove a published layer. |
| Explorer Web files | Opened TypeScript/TSX files export placeholder flags | **PLACEHOLDER** | No UI display or Evidence Drawer behavior is proven. |
| Domain workflow | Three jobs execute TODO echo commands | **TODO SCAFFOLD** | CI does not prove Archaeology validation, proof, or publication. |
| Archaeology ADRs | Source-role and exact-location ADR files are `PROPOSED` scaffolds | **NOT ACCEPTED** | They are planning handles, not current decisions. |
| Direct consumer/loader | No indexed direct consumer from config search | **UNKNOWN / NOT ESTABLISHED** | No file here is active by presence. |

### Critical scaffold warning

Some inspected policy scaffolds use `default allow := false`. Two precise-coordinate redaction stubs explicitly state that no real rules exist and use `default deny := false`.

Therefore:

- no scaffold may be treated as an accepted protection;
- no config may select a scaffold as though it were a production policy profile;
- absence of a deny result from a stub is **not** permission;
- consumers must enter a safe inactive, `DENY`, `HOLD`, `ABSTAIN`, or `ERROR` state until accepted policy and tests exist.

### Current conflict register

| Conflict | Status | Required posture |
|---|---:|---|
| `Site` versus `ArchaeologicalSite` | `CONFLICTED` | Treat `site.*` as compatibility/lineage until accepted reconciliation. |
| Collapsed versus decomposed object-family names | `CONFLICTED / NEEDS VERIFICATION` | Preserve source terms and map through reviewed contracts. |
| `SensitivityTransform` versus `PublicationTransformReceipt` and cross-cutting receipt names | `CONFLICTED / NEEDS VERIFICATION` | Do not invent equivalence or receipt authority in config. |
| `contracts/domains/archaeology/` versus `contracts/archaeology/` | `RESOLVED IN CURRENT PATH DOC / LINEAGE REMAINS` | Follow segmented path; preserve migration history. |
| `schemas/contracts/v1/domains/archaeology/` versus flat shorthand | `RESOLVED IN CURRENT PATH DOC / LINEAGE REMAINS` | Follow segmented path; do not duplicate schemas. |
| Domain policy versus sensitivity-policy placement | `LAYERED / NEEDS VERIFICATION` | Reference accepted policy IDs; do not copy rules or assume runtime binding. |
| `data/registry/sources/archaeology/` versus `data/registry/archaeology/sources/` | `CONFLICTED` | Do not create divergent descriptor sets; require ADR/migration. |
| Cultural-review schemas under domain versus governance homes | `NEEDS VERIFICATION` | Do not choose a machine authority from config. |
| Exact-location public floor and lane-local refinements | `NEEDS STEWARD RATIFICATION` | Most restrictive applicable rule controls. |

[Back to top](#top)

---

## What belongs here

Only safe, non-secret Archaeology configuration support for a named and verified consumer belongs here.

| Material | Permitted purpose | Minimum posture |
|---|---|---|
| `README.md` | Define the configuration boundary. | Preserve exact-location, cultural-authority, consent, source-role, evidence, policy, and release controls. |
| `*.template.yaml` / `*.template.yml` | Placeholder-based template for a verified consumer. | Parseable, versioned, synthetic, inert by presence, explicit consumer and schema/profile refs. |
| `*.example.yaml` / `*.example.json` / `*.example.toml` | Tiny fictional example. | Impossible IDs and geometry; no real cultural terms, sites, collections, communities, people, or routes. |
| Conservative review defaults | Select accepted deny, hold, abstain, review, redaction, generalization, or restricted-access profiles. | Cannot lower protection or replace a review record. |
| Public-safe display selectors | Reference an accepted transform/release profile. | No coordinates, tile identifiers, query windows, exact counts, or reconstruction clues. |
| Candidate-labeling selectors | Preserve candidate, anomaly, interpretation, and confirmed distinctions. | Cannot promote or relabel an object. |
| Migration notes | Document a real key/path/version transition. | Time-bounded, owner-linked, reversible, and does not create a second authority. |
| Validation notes | Explain required deterministic and sensitivity checks. | Executable commands must be verified or labeled `PROPOSED` / `NEEDS VERIFICATION`. |

Examples must remain unmistakably synthetic. A plausible-looking fictitious location, cultural identifier, accession, oral-history excerpt, Tribal name, parcel, route, coordinate, or object description can still cause harm and is not acceptable merely because it is labeled “example.”

[Back to top](#top)

---

## What does not belong here

| Prohibited material | Why prohibited | Correct home or action |
|---|---|---|
| Exact or reconstructable site geometry | Looting, damage, trespass, cultural harm, and irreversible exposure risk. | Restricted lifecycle/policy/release lanes; deny, quarantine, generalize, or withhold. |
| Burial, human-remains, funerary, sacred, ceremonial, or restricted-knowledge detail | High cultural, ethical, legal, and sovereignty significance. | Named-authority and governed review process; no ordinary public config. |
| Cultural authority, consent, waiver, revocation, affiliation, or rights-holder determinations | Config cannot make or replace human/community authority decisions. | Accepted governance/review/consent records. |
| Oral-history substance or community-controlled categories | KFM must not translate or appropriate the substance. | Named authority controls; store only governed references where permitted. |
| Looting-risk, access, vulnerability, storage, security, or collection-location clues | Can enable theft or site harm. | Restricted operational/security controls; not public repository config. |
| Real site, survey, artifact, collection, accession, private-land, or person records | These are lifecycle/evidence objects, often sensitive. | Correct `data/`, proof, registry, or restricted store. |
| Source descriptors, source-role definitions, activation decisions, rights rows | Config cannot admit or activate sources. | Accepted source registry. |
| Schemas, contracts, policy modules, review records, receipts, proofs, release records | These are authority/trust object families. | Their canonical responsibility roots. |
| Pipeline, package, validator, app, UI, or runtime code | Config is not implementation. | `packages/`, `pipelines/`, `tools/`, `apps/`, or runtime roots. |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads | Config is not a lifecycle store. | Correct lifecycle phase under `data/`. |
| Credentials, private endpoints, access tokens, local paths, signed URLs | Secret and topology exposure. | External secret/config manager or ignored local deployment settings. |
| Settings that turn candidates, anomalies, models, histories, routes, or context into confirmed sites | Violates source-role and candidate/site boundaries. | Contracts, evidence, review, and governed lifecycle. |
| Settings that mark a `PROPOSED` schema/policy/source/layer as active | Presence and labels are not acceptance. | Accepted registry/policy/release state. |
| Automatic publication, indexing, vectorization, map-layer creation, or AI answering | Bypasses review and the trust membrane. | Explicit governed consumer/release workflow. |

No file in this lane may act as a hidden shortcut around cultural review, consent/revocation, sensitivity transforms, source rights, evidence closure, review records, or release governance.

[Back to top](#top)

---

## Inputs

A future payload requires all of the following:

1. **Named consumer** — exact package, pipeline, service, app, runtime, test, or tool.
2. **Declared format and version** — including parser and canonical schema/profile references.
3. **Explicit binding** — exact path or identifier; no recursive discovery or filename activation.
4. **Deterministic precedence** — base, domain, environment, deployment, command-line, and runtime order.
5. **Unknown-key behavior** — reject by default where safety or authority could change.
6. **Accepted authority references** — contracts, schemas, policy, source registry, cultural review, consent/revocation, and release profiles.
7. **Synthetic values only** — no real locations, names, identifiers, access details, cultural content, or collection records.
8. **Object and source-role preservation** — candidate, observation, context, interpretation, authority, restricted, and confirmed states remain distinct.
9. **Named-authority posture** — unresolved `authority_to_control` or equivalent produces hold/deny/abstain.
10. **Consent and revocation posture** — revocation is a live fail-closed input, not cached permission.
11. **Location and reconstruction review** — coordinates, grids, tiles, hashes, logs, joins, counts, and timing are assessed.
12. **Burial/sacred/human-remains review** — most restrictive applicable rule applies.
13. **Rights and collection-security review** — including private land, access, storage, custody, and redistribution.
14. **No-network fixtures** — valid, invalid, denied, held, abstained, quarantined, and error examples.
15. **Correction and rollback** — deactivation, cache/index invalidation, downstream withdrawal, and prior known-good state.

A file missing any required item remains `PROPOSED` and inert.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future validated payload may support a verified consumer by selecting already-governed behavior such as:

- candidate labels and non-confirmation warnings;
- accepted deny/hold/abstain/review routing;
- an accepted county/region or more restrictive public-safe geometry profile;
- an accepted redaction/generalization profile;
- required cultural, Tribal, rights-holder, human-remains, burial, collection, or security review routes;
- stale, revoked, superseded, restricted, withdrawn, or correction state display;
- source-role, uncertainty, chronology, and evidence-citation presentation;
- network-disabled or public-output-disabled behavior when dependencies are missing.

It may not:

- confirm or expose a site;
- identify or choose cultural authority;
- create consent or ignore revocation;
- determine burial, sacred, affiliation, custody, ownership, repatriation, or access status;
- activate a source, policy, schema, validator, layer, route, or model;
- close evidence, review, receipts, catalog, or release;
- advance lifecycle state;
- create a public map/API/UI/search/vector/AI surface.

[Back to top](#top)

---

## Validation

No executable validator for this config lane was verified. Opened Archaeology validator files raise `NotImplementedError`; opened schemas are empty and permissive; the domain workflow runs TODO echo commands.

The following matrix is the **required target**, not a claim of implementation.

| Check | Required result | Current evidence |
|---|---|---|
| Parse and format | Deterministic parse under declared version. | `NEEDS VERIFICATION` per future payload. |
| Non-empty accepted schema | Schema has meaningful required fields, closed/controlled extras, fixtures, validator, and review. | Opened schemas fail this target. |
| Known-key behavior | Unknown risk-bearing keys fail. | `UNKNOWN`. |
| Explicit consumer binding | Exact consumer and selection path are tested. | No consumer established. |
| Precedence and fallback | Deterministic and fail-closed. | `UNKNOWN`. |
| Secret and private-path scan | No credentials, endpoints, local paths, or operational details. | Required; enforcement unverified. |
| Sensitive-content scan | No site, burial, sacred, cultural, private-land, collection, or access clues. | Required; enforcement unverified. |
| Candidate-not-site | Candidate/anomaly/context/model cannot be emitted as confirmed. | Required; policy scaffold is not proof. |
| Named-authority check | Missing/unverified cultural authority blocks consequential use. | Required; mechanism unverified. |
| Consent/revocation check | Missing, expired, limited, or revoked consent blocks use. | Required; mechanism unverified. |
| Exact-location denial | Coordinates and reconstruction channels fail closed. | Required; policy stubs are not proof. |
| Burial/sacred/human-remains cases | Denied/held and routed to required authority/review. | Required. |
| Collection-security case | Storage/access/custody clues are suppressed and reviewed. | Required. |
| Source-role preservation | Observation, candidate, context, model, authority, restricted, synthetic remain distinct. | Source-role YAML is placeholder. |
| Identity and alias checks | `Site`/`ArchaeologicalSite` and other conflicts do not silently merge. | Required; contracts document conflict. |
| Chronology and uncertainty | Method, range, confidence, source time, valid time, review/release/correction time remain explicit. | Required. |
| Cross-domain anti-confirmation | Routes, geology, land, hazards, genealogy, imagery, terrain cannot confirm a site. | Required. |
| No-network validation | Fixtures and checks avoid live source systems. | Required where practical. |
| No side effect | Parse/validation does not fetch, publish, index, map, vectorize, or call models. | Required. |
| Logging and error safety | No sensitive values, hashes, identifiers, joins, or side-channel clues. | Required. |
| Release support | Public-bound behavior requires accepted evidence, policy, review, transform, release, correction, rollback. | Required; runtime wiring unverified. |
| Invalidation | Revocation/correction/withdrawal removes derived caches, indexes, layers, exports, and generated text. | `NEEDS VERIFICATION`. |

### Configuration-review outcomes

These outcomes apply to config review only, not public release:

| Outcome | Meaning | Action |
|---|---|---|
| `PASS` | Config support checks pass and all referenced authorities are accepted/current. | May merge as implementation support; no release authority. |
| `HOLD` | Reviewable uncertainty remains. | Keep inactive; resolve authority, rights, consent, policy, or validation. |
| `DENY` | Sensitive content, authority bypass, permissive fallback, real location, or unsafe binding exists. | Remove/quarantine and follow incident/correction process. |
| `ERROR` | Parser, validator, or review machinery failed. | Repair the process; failure is not permission. |

Where runtime contracts use `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`, a configuration consumer must map safely without converting `HOLD` or unresolved review into `ANSWER`.

[Back to top](#top)

---

## Review burden

### Minimum review posture

| Change | Required review |
|---|---|
| README clarification | Config/docs + Archaeology steward + cultural/sensitivity reviewer. |
| New template/example | Config + consumer + Archaeology + sensitivity/security. |
| Candidate/site, object-family, identity, chronology, source-role setting | Add contract/schema/source/evidence reviewers. |
| Exact-location, generalization, redaction, map, search, export, tile, cache, index, or AI setting | Cultural/Tribal reviewer + rights-holder representative + policy + security + release. |
| Oral history, community-controlled knowledge, consent, revocation, sovereignty | Named authority + cultural/Tribal reviewer + consent/governance + legal/rights as applicable. |
| Burial, human remains, funerary, sacred, ceremonial | Most restrictive review; no ordinary config-only approval. |
| Collections, custody, repatriation, repository access/security | Collection steward + cultural/rights-holder + security + legal/rights as applicable. |
| Source or rights setting | Source steward + rights + sensitivity + policy. |
| Runtime/public behavior | Consumer/app/runtime + evidence + policy + review + release + rollback owners. |
| Path, schema, policy, registry, or object-family authority change | ADR/migration-class review. |

`OWNER_TBD` is not accepted ownership. Automatic reviewer enforcement remains `NEEDS VERIFICATION`.

### Separation of duties

Configuration authors must not unilaterally:

- choose the named cultural authority;
- approve their own consent/review record;
- define and approve a public geometry transform;
- treat a validator pass as release approval;
- approve public exposure of sensitive or exact material;
- collapse generation, review, policy, and release into one step.

[Back to top](#top)

---

## Related folders

| Responsibility | Home | Relationship |
|---|---|---|
| Parent config boundary | `configs/domains/README.md` | Common no-secret/no-authority rules. |
| Domain doctrine | `docs/domains/archaeology/` | Scope, language, cultural review, sensitivity, lifecycle. |
| Semantic meaning | `contracts/domains/archaeology/` | Current segmented contract home; naming conflicts remain. |
| Machine shape | `schemas/contracts/v1/domains/archaeology/` | Draft scaffold schemas; field completeness unverified. |
| Domain policy | `policy/domains/archaeology/` | Domain policy modules; inspected files are scaffolds. |
| Sensitivity policy | `policy/sensitivity/archaeology/` and related paths | Sensitive geometry/sovereignty controls; runtime binding unverified. |
| Source registry | `data/registry/sources/archaeology/` or accepted topology | Source roles, rights, cadence, activation. |
| Domain-first source registry | `data/registry/archaeology/sources/` | Existing competing topology; do not diverge. |
| Package helpers | `packages/domains/archaeology/` | Current inspected metadata/code is greenfield. |
| Pipeline logic | `pipelines/domains/archaeology/` | Current inspected core files are placeholders. |
| Pipeline specs | `pipeline_specs/archaeology/` | Current inspected specs have no stages. |
| Validators | `tools/validators/domains/archaeology/` | Current inspected entrypoints raise `NotImplementedError`. |
| Tests/fixtures | `tests/domains/archaeology/`, `fixtures/domains/archaeology/` | Enforceability and synthetic examples. |
| Lifecycle | `data/<phase>/archaeology/` | Source/candidate/processed/catalog/published state. |
| Receipts/proofs | `data/receipts/`, `data/proofs/` | Process memory and EvidenceBundle/proof support. |
| Release | `release/` | Promotion, review linkage, correction, withdrawal, rollback. |
| Explorer UI | `apps/explorer-web/src/features/domains/archaeology/` | Current inspected files are placeholders. |
| Domain CI | `.github/workflows/domain-archaeology.yml` | Current jobs are TODO scaffolds. |

Public clients must use governed interfaces and released, policy-safe derivatives. They must not read this config lane, source registries, canonical/internal lifecycle stores, sensitive proof records, or unpublished layer registries directly.

[Back to top](#top)

---

## ADRs and drift triggers

### Repository-present Archaeology ADRs

| ADR | Current status | Effect |
|---|---:|---|
| `ADR-archaeology-source-roles.md` | `PROPOSED scaffold` | Does not establish an accepted source-role vocabulary. |
| `ADR-archaeology-exact-location-policy.md` | `PROPOSED scaffold` | Does not establish accepted exact-location runtime enforcement. |

### Decisions not enacted here

This README does not decide:

- `Site` versus `ArchaeologicalSite`;
- collapsed versus decomposed object-family names;
- receipt and transform terminology;
- consent/revocation schema and record homes;
- domain versus governance cultural-review schema placement;
- policy domain/sensitivity layering;
- source-registry topology;
- public geometry floors or transform profiles;
- accepted cultural/Tribal/rights-holder roles;
- configuration discovery or precedence;
- runtime, API, UI, map, search, index, AI, or release behavior.

### ADR or migration triggers

Create or update a governed decision before:

- changing a canonical object-family name or alias;
- creating a second schema, contract, policy, review, consent, source, or receipt authority;
- changing exact-location, burial, sacred-site, human-remains, or cultural-control defaults;
- changing consent or revocation semantics;
- changing source-registry order;
- treating a scaffold policy/schema/validator as active;
- making directory presence a loader/activation mechanism;
- enabling public location, map, search, vector, export, or AI behavior;
- retiring compatibility paths or moving trust-bearing records.

[Back to top](#top)

---

## Last reviewed

**2026-07-14**, against `main@5049e03434f9b6880464605a5eb31c843bb7e450`.

Review again when:

- a non-README payload is proposed;
- a direct consumer or loader appears;
- `Site`/`ArchaeologicalSite` or another object conflict is resolved;
- an Archaeology ADR changes status;
- a schema gains meaningful fields;
- a validator becomes executable;
- a policy module gains reviewed rules and runtime binding;
- source descriptors are admitted;
- cultural review/consent/revocation integration is implemented;
- a map, layer, API, UI, search, index, export, or AI surface becomes real;
- six months pass.

[Back to top](#top)

---

## Scope and bounded context

This configuration lane may support already-governed Archaeology object families without owning their meaning.

| Family | Config may support | Config must not decide |
|---|---|---|
| Site and site component | Display label/profile selection after accepted identity/review. | Site existence, confirmation, boundaries, public coordinates. |
| Survey project/transect | Parser/display/validation profile selection. | Survey adequacy, authority, site confirmation. |
| Artifact/artifact record | Safe presentation profile selection. | Ownership, provenance truth, affiliation, custody, public access. |
| Provenience/context | Accepted context-display profile. | Context reconstruction, exact provenience exposure. |
| Excavation/stratigraphy | Unit/method presentation profile. | Archaeological interpretation or chronology truth. |
| Remote sensing/LiDAR/candidate feature | Candidate label, method, uncertainty, review routing. | Site confirmation or public precise geometry. |
| Geophysics observation | Method/QC display profile. | Feature/site truth. |
| 3D documentation | Public-safe derivative profile after release. | Exact reconstruction, access, ownership, or site clearance. |
| Cultural/Steward review | Reference accepted review status. | Who has authority or whether a review is sufficient. |
| Collection/repository record | Safe repository-display profile. | Ownership, custody, repatriation, access permission, storage location. |
| Chronology assertion/period | Method/range/uncertainty display. | Final date, affiliation, or period certainty. |
| Sensitivity/publication transform | Reference accepted profile and receipt. | Policy definition, transform approval, release. |

---

## Configuration classes

| Class | Use | Posture |
|---|---|---|
| `template` | Demonstrate supported keys with placeholders. | Never active by presence. |
| `example` | Fictional, non-operational illustration. | No plausible real site/cultural/collection detail. |
| `dev-default` | Conservative setting for verified development consumer. | Synthetic/no-network; public exposure disabled. |
| `test-default` | Deterministic test configuration. | Fixture-bound and no real sensitive values. |
| `review-default` | Hold/deny/review routing for a verified review tool. | Cannot approve review or release. |
| `public-safe-template` | Reference an accepted transform/release profile. | No geometry or transform logic embedded. |
| `compatibility` | Temporary key/path/profile alias. | Time-bounded, documented, reversible. |
| `production-binding` | Real source, endpoint, credential, reviewer roster, or release binding. | **Forbidden here.** |

---

## Minimum configuration contract

A future non-README file must document:

| Field | Requirement |
|---|---|
| `domain_slug` | `archaeology`. |
| `config_class` | One class from the taxonomy above. |
| `intended_consumer` | Exact code/app/pipeline/tool path. |
| `consumer_version` | Verified version/range or `NEEDS VERIFICATION`. |
| `format` | Parser and format version. |
| `authority_refs` | Accepted contract/schema/policy/source/review/release handles only. |
| `object_families` | Explicit set; no implicit all-Archaeology scope. |
| `source_roles` | Accepted roles and anti-upcast behavior. |
| `candidate_behavior` | Candidate/anomaly/context/model never silently confirmed. |
| `cultural_authority_ref` | Named-authority handle where required; not a free-text assertion. |
| `consent_revocation_ref` | Live governed reference where applicable. |
| `sensitivity_floor` | Reference to accepted policy; most restrictive applies. |
| `geometry_behavior` | Deny/generalize/redact profile reference; no embedded coordinates. |
| `burial_sacred_behavior` | Mandatory deny/hold/review routing. |
| `collection_security_behavior` | Redaction and access limits. |
| `chronology_behavior` | Methods, uncertainty, ranges, and temporal facets. |
| `network_behavior` | `none` for parse/validation by default. |
| `side_effects` | `none` for parse/validation. |
| `unknown_key_behavior` | Reject for safety/authority keys. |
| `missing_ref_behavior` | Safe inactive/deny/hold/abstain/error. |
| `logging_posture` | Redacted; no sensitive identifiers, joins, or values. |
| `validation_ref` | Executable accepted validator/test or `NEEDS VERIFICATION`. |
| `rollback` | Deactivation, prior version, invalidation, and correction path. |
| `owner` | Accepted owner or `OWNER_TBD`; never invented. |
| `reviewed_at` | ISO date. |

A payload referencing an empty schema, placeholder validator, scaffold policy, TBD source descriptor, or PROPOSED layer registry is not ready for active use.

---

## Consumer binding, precedence, and discovery

### Explicit binding

Consumers must name the exact file or stable config identifier. Do not recursively discover `configs/domains/archaeology/`.

### No implicit precedence

This README does not establish an overlay order. The verified consumer must define:

- files considered;
- merge versus replace;
- environment/deployment overrides;
- unknown-key behavior;
- type coercion;
- missing-file behavior;
- stale config behavior;
- safe fallback;
- logging and telemetry redaction;
- cache and invalidation behavior.

### Fail-safe behavior

A loader failure must not:

- expose exact or generalized geometry by guessing;
- fall back to a permissive policy stub;
- ignore a revoked consent record;
- promote a candidate;
- select a “latest” release without review;
- retain stale map/search/vector/AI caches;
- query source systems automatically;
- emit a public answer.

---

## Archaeology object-family boundaries

The repository carries overlapping collapsed and decomposed object-family vocabularies.

Configuration must:

- preserve the original object family;
- use reviewed crosswalks rather than string similarity;
- record aliases without choosing canonical authority;
- avoid mapping broad `Site`, `Survey`, `Artifact`, `Feature`, or `Context` labels to narrower objects by convenience;
- avoid treating review, transform, receipt, proof, and release objects as interchangeable.

Configuration must not collapse:

```text
Site -> ArchaeologicalSite
CandidateFeature -> ArchaeologicalSite
LiDARCandidate -> ArchaeologicalSite
RemoteSensingAnomaly -> ArchaeologicalSite
SurveyProject -> confirmed site
ArtifactRecord -> collection ownership
CulturalReview -> consent
StewardReview -> release approval
SensitivityTransform -> PublicationTransformReceipt
PublicationTransformReceipt -> RedactionReceipt
validation pass -> policy approval
policy allow -> release
published-path placeholder -> released artifact
```

---

## Identity, alias, and candidate promotion

### `Site` versus `ArchaeologicalSite`

Current repository evidence treats:

- `archaeological_site.md` as the object-map expected contract;
- `site.md` as a compatibility/lineage contract;
- `site.schema.json` as an empty permissive scaffold.

A config must not:

- select `site` as canonical;
- merge both identities;
- direct consumers to the scaffold as complete validation;
- use an alias to bypass candidate-to-site review;
- treat an old path as release authority.

### Candidate promotion

Promotion from anomaly/candidate/context to reviewed site identity requires evidence and governance outside this lane. Configuration may only preserve labels and route to review.

### Stable identity

Where accepted contracts exist, preserve:

- source-native identifiers;
- survey/project/transect identifiers;
- provenience and context identifiers;
- collection/accession/repository identifiers;
- candidate/model/run identifiers;
- geometry/provenance digests where safe and non-reconstructive;
- correction/supersession lineage.

Do not merge by proximity, geometry overlap, similar names, historic labels, route association, parcel intersection, imagery resemblance, or generated embedding similarity.

---

## Source role and knowledge character

Use only an accepted vocabulary. Until source-role ADR/schema acceptance is verified, map roles explicitly and conservatively.

| Knowledge character | Boundary |
|---|---|
| `observed` | Direct documented observation under stated method; not automatically public. |
| `authority` / `regulatory` | Official designation or authority record; not site condition or public permission. |
| `candidate` | Unreviewed possibility; never site confirmation. |
| `context` | Background, historical, environmental, route, land, or geology context; insufficient for confirmation. |
| `modeled` / `inferred` | Remote sensing, classification, prediction, reconstruction, or statistical inference. |
| `oral_history` / community-controlled | Governed by named authority, consent, restrictions, attribution, retention, and revocation. |
| `restricted` | Cannot be exposed through ordinary public config. |
| `synthetic` | Demo/test material with explicit reality boundary. |
| `legacy` | Historical record or prior terminology; preserve vintage and uncertainty. |

No config value may upcast a role. A source role belongs to the use and evidence context, not merely to a publisher name.

---

## Cultural authority, sovereignty, consent, and revocation

Configuration must defer the substance of cultural knowledge to the named authority.

It may reference:

- accepted authority identifiers;
- accepted review workflow/profile identifiers;
- governed consent and revocation handles;
- obligations, restrictions, attribution, retention, benefit, and access profile IDs;
- safe public notice/chip profile IDs after review.

It must not:

- create `authority_to_control`;
- infer authority from geography, organization name, dataset ownership, or government records;
- flatten multiple communities or authorities;
- treat silence or missing metadata as consent;
- convert one-time consent into perpetual or secondary-use permission;
- ignore partial, scoped, expired, superseded, or revoked consent;
- expose internal reviewer identity where not appropriate;
- encode cultural categories or sacred meaning without authority control;
- allow generated text to translate or reinterpret restricted knowledge.

Revocation must invalidate active views, caches, indexes, exports, prompts, embeddings, vector entries, generated summaries, and release derivatives as required by the governing process.

---

## Exact location, reconstruction, and looting risk

Exact-location denial includes more than latitude/longitude.

### Direct geometry channels

- coordinates, UTM, survey grids, bearings, distances;
- polygons, points, centroids, bounding boxes;
- buffers small enough to reveal the site;
- elevations or terrain profiles when identifying;
- collection/find-spot references.

### Indirect reconstruction channels

- tile, quad, H3, geohash, grid, raster cell, or zoom identifiers;
- stable hashes or cache keys derived from geometry;
- filenames, IDs, directory names, or URLs encoding location;
- query windows, map extents, viewport state, API pagination, or error messages;
- route, river, land parcel, ownership, geology, landform, trail, fort, mission, settlement, or infrastructure proximity;
- public layer intersections and cross-layer differencing;
- rarity, count, date, survey description, accession, collection, photograph, or narrative clues;
- model saliency maps, embeddings, nearest-neighbor results, or AI chain outputs;
- screenshot metadata, debug traces, logs, metrics labels, telemetry dimensions, or test snapshots.

### Required behavior

When reconstruction risk is unresolved:

- do not degrade to “best effort” geometry;
- do not expose an intermediate tile or centroid;
- do not use a client-side-only blur as protection;
- do not return a count or narrative that uniquely identifies the location;
- use `DENY`, `HOLD`, or `ABSTAIN`, or an accepted more restrictive transform.

County/region generalization described in project doctrine is a public floor proposal, not a promise that every record may be generalized and released. Burial, sacred, cultural, rights, looting, and named-authority rules can require full denial.

---

## Burial, human remains, sacred, and funerary material

No ordinary configuration switch may allow:

- exact or generalized burial location;
- human-remains inventory or disposition details;
- funerary object or associated object locations;
- sacred/ceremonial place identification;
- culturally sensitive affiliation or community-controlled classification;
- excavation, storage, access, handling, imaging, analysis, or transfer details;
- legal, ethical, repatriation, or eligibility conclusions.

The most restrictive applicable policy and named-authority decision controls. Missing context is not clearance.

Tests for this area must use deliberately non-real synthetic fixtures with no resemblance to known locations or communities.

---

## Collections, custody, repatriation, and security

Configuration may reference a public-safe released repository profile. It cannot determine:

- ownership or title;
- lawful custody;
- accession legitimacy;
- repository authority;
- repatriation or consultation status;
- NAGPRA or other legal eligibility/status;
- access permission;
- storage location;
- security arrangements;
- insurance or valuation;
- movement, transport, handling, or vulnerability.

Collection identifiers, accession numbers, repository names, images, and descriptions can create reconstruction or theft risk and require review.

---

## Chronology, time, and uncertainty

Keep distinct where material:

- source creation/vintage;
- observation or excavation time;
- collection/acquisition time;
- valid/effective time;
- interpretation/model time;
- retrieval time;
- cultural review time;
- consent/revocation time;
- policy decision time;
- release time;
- correction/supersession/withdrawal time.

Chronology configuration may select an accepted display or method profile. It cannot:

- make a date range exact;
- select a cultural period as certain;
- infer affiliation;
- suppress calibration/method uncertainty;
- equate terminology across communities or scholarship;
- present a legacy interpretation as current;
- erase revised or contested chronology.

---

## Remote sensing, LiDAR, geophysics, and three-dimensional documentation

These surfaces are evidence-bearing methods, not site-confirmation shortcuts.

A config may reference accepted method, QA, uncertainty, visualization, and review profiles. It must preserve:

- sensor/product/source identity;
- acquisition date and geometry;
- resolution and processing chain;
- model/run/version and parameters where accepted;
- confidence/uncertainty and false-positive limits;
- candidate status;
- cultural, sensitivity, rights, and access restrictions;
- EvidenceRef and review linkage.

It must not:

- convert an anomaly score to site truth;
- publish raw or derived exact candidate geometry;
- expose saliency or feature layers that reconstruct the candidate;
- treat 3D documentation as permission to reproduce or distribute;
- let AI vision or spatial models confirm a site;
- use public imagery availability as rights or sensitivity clearance.

---

## Cross-domain context and anti-confirmation

| Related lane | Allowed relation | Forbidden collapse |
|---|---|---|
| Roads/Rail/Trade | Historic-route context. | Route proximity confirms a site. |
| People/DNA/Land | Genealogy, deeds, parcels, land history under governance. | Ownership/title/identity confirms site or grants access. |
| Geology | Landform, materials, stratigraphy context. | Geological suitability confirms archaeology. |
| Hazards | Erosion, fire, flood, exposure context. | Hazard layer authorizes disclosure or intervention. |
| Settlements/Infrastructure | Historic settlement/facility context. | Settlement/facility identity confirms site or safe access. |
| Hydrology | Water/river context. | Water proximity confirms a site. |
| Habitat/Flora/Fauna | Environmental context. | Ecological association confirms site or exposes rare/sensitive joins. |
| Atmosphere | Weather/climate context. | Environmental condition confirms chronology/site. |
| Agriculture | Land-use disturbance/context. | Field/crop classification confirms site or grants field access. |

Cross-domain relations do not transfer authority. The strongest sensitivity and named-authority obligations survive every join and projection.

---

## Logging, telemetry, caches, and derived indexes

Do not log or index:

- coordinates, grids, tiles, extents, or geometry-derived hashes;
- site/candidate/cultural/collection identifiers;
- authority, consent, review, or restriction details beyond safe audit references;
- oral-history text or restricted cultural categories;
- private-land, owner, access, storage, security, or collection details;
- raw prompts, model explanations, embeddings, nearest-neighbor outputs, or full denial context;
- sensitive source endpoints, paths, query parameters, or filenames.

Safe observability should use bounded reason codes, non-sensitive counts, reviewed coarse categories, and protected audit references.

A correction, revocation, withdrawal, or sensitivity increase must invalidate:

- application caches;
- CDN/tile caches;
- search indexes;
- vector indexes and embeddings;
- graph/triplet projections;
- exported files and reports;
- screenshots/previews where controlled;
- AI retrieval indexes and generated summaries;
- downstream layer manifests and bookmarks as governed.

---

## Failure behavior

| Condition | Minimum safe behavior |
|---|---|
| Missing/invalid config | `ERROR` or conservative inactive denial. |
| Unknown risk-bearing key | Reject or `HOLD`. |
| Empty/permissive schema | Do not activate payload. |
| Placeholder validator | Do not claim validation; `HOLD`/`ERROR`. |
| Scaffold policy or mixed permissive default | Do not rely on it; safe denial/inactive state. |
| Cultural authority unresolved | `HOLD`, `DENY`, or `ABSTAIN`. |
| Consent missing/expired/revoked/out-of-scope | `DENY`/`HOLD`; invalidate prior derivatives. |
| Candidate presented as site | Reject/relabel and route to review. |
| Exact/reconstruction risk unresolved | `DENY` or accepted more restrictive transform. |
| Burial/sacred/human-remains involvement | `DENY`/`HOLD` under most restrictive rule. |
| Collection security/custody unresolved | `DENY`/`HOLD`. |
| Source role/rights unclear | `HOLD`, `DENY`, or `ABSTAIN`. |
| Evidence/review/receipt/release/rollback missing | Do not render or promote publicly. |
| Source/consumer unavailable | Fail closed; do not overstate stale state. |
| Correction/revocation invalidation incomplete | Keep withdrawn/restricted; do not restore public response. |

Errors must not reveal the protected value or enough context to infer it.

---

## Governed AI and generated language

AI is interpretive, not root truth.

Configuration must not permit AI to:

- confirm archaeological sites;
- infer sacredness, affiliation, authority, consent, ownership, custody, repatriation, or legal status;
- reconstruct exact locations from public clues;
- rank looting targets or vulnerable sites;
- generate access directions;
- reveal restricted oral-history or cultural knowledge;
- turn anomaly/model output into fact;
- produce public answers from RAW, WORK, QUARANTINE, candidates, private registries, or unreleased records;
- treat citations as permission to expose sensitive content.

Preferred order:

1. define bounded question and audience;
2. resolve released EvidenceRef to EvidenceBundle;
3. apply named-authority, consent/revocation, sensitivity, rights, policy, review, and release checks;
4. use public-safe released projections only;
5. answer with citations, limitations, and bounded confidence—or `ABSTAIN`/`DENY`.

AI receipts, retrieval indexes, prompt logs, and generated summaries must follow the same correction, revocation, and invalidation rules.

---

## Migration and anti-bypass posture

When misplaced or unsafe material is found here:

1. freeze activation and public use;
2. identify consumers, caches, indexes, exports, generated outputs, and exposure window;
3. remove/quarantine secrets and sensitive details immediately;
4. preserve incident/correction evidence without copying protected content into public notes;
5. identify the true responsibility root;
6. move meaning to contracts, shape to schemas, policy to policy, source records to registry, data to lifecycle, reviews/consent to governance homes, receipts/proofs to their roots, release decisions to release;
7. preserve aliases/migration notes without parallel authority;
8. update consumers through explicit binding;
9. run candidate/site, cultural authority, consent/revocation, reconstruction, burial/sacred, collection-security, rights, source-role, no-network, and negative tests;
10. invalidate derived maps, caches, indexes, embeddings, graph projections, exports, and generated language;
11. record correction/withdrawal/rollback;
12. remove compatibility material when closure is verified.

### Anti-bypass matrix

| Bypass | Required response |
|---|---|
| Config selects scaffold policy as active | Reject; require accepted policy and tests. |
| Config treats empty schema as validation | Reject; require meaningful schema/fixtures/validator. |
| Config treats validator README/path as executable proof | Reject; verify runnable code and results. |
| Config treats source placeholder as admitted source | Reject; require accepted descriptor/rights/activation. |
| Config treats `data/published/...` path as released | Reject; require release state/manifests and public-safe artifact. |
| Config enables direct UI/source-store reads | Reject; route through governed API/released artifact. |
| Config promotes candidate based on score/threshold | Reject; preserve candidate and review. |
| Config lowers geometry/sensitivity for convenience | Reject; most restrictive accepted rule applies. |
| Config caches permission or consent indefinitely | Reject; resolve current live state. |
| Config suppresses a denial reason by exposing sensitive detail | Return safe reason code only. |

---

## Rollback, correction, withdrawal, and invalidation

### Rollback triggers

- sensitive or exact detail appears;
- cultural authority or consent was misrepresented;
- revocation was ignored;
- candidate was presented as confirmed;
- scaffold policy/schema/validator/source/layer was treated as active;
- public/client path bypassed release governance;
- collection security or looting risk increased;
- cross-domain joins enabled reconstruction;
- correction did not propagate to caches/indexes/AI outputs.

### Required response

1. enter a safer state immediately;
2. stop public/API/UI/search/export/AI delivery;
3. preserve a protected audit trail;
4. identify affected releases and derivatives;
5. restore prior safe config or built-in denial;
6. issue correction, restriction, withdrawal, supersession, or rollback records;
7. invalidate caches, tiles, indexes, vectors, graphs, exports, prompts, and summaries;
8. re-run tests and review;
9. verify no downstream surface still exposes or implies the unsafe state.

For this README, the mechanical rollback target is prior blob `e429009d4877428c46f4a77c48857ec26c13f0e2`.

Deleting or reverting a file does not erase already disclosed information.

---

## Definition of done for the first payload

Before the first non-README file is accepted:

- [ ] exact consumer, owner, and code binding verified;
- [ ] config class, format, version, parser, precedence, missing-file, unknown-key, and fallback behavior defined;
- [ ] accepted non-empty schema with required fields and controlled additional properties;
- [ ] executable validator and valid/invalid fixtures;
- [ ] accepted policy modules with tests and runtime binding; no scaffold reliance;
- [ ] canonical contract/object-family names resolved or explicit compatibility mapping approved;
- [ ] source IDs, roles, rights, cadence, sensitivity, and activation verified;
- [ ] named cultural authority and reviewer requirements verified;
- [ ] consent scope, retention, secondary use, expiration, and revocation flow verified;
- [ ] candidate/anomaly/context/model-to-site promotion tests pass;
- [ ] exact-location and reconstruction-channel denial tests pass;
- [ ] burial, human-remains, sacred, funerary, and restricted-knowledge tests pass;
- [ ] oral-history and community-controlled-content tests pass;
- [ ] collection custody/repatriation/access/security tests pass;
- [ ] identity/alias/provenience/collection/chronology tests pass;
- [ ] cross-domain anti-confirmation tests pass;
- [ ] no real locations, names, cultural content, access details, or restricted records in fixtures;
- [ ] no-network parse/validation tests pass;
- [ ] logging/telemetry/cache/index redaction tests pass;
- [ ] public-bound flow requires EvidenceBundle, policy, review, transform receipt, release, correction, and rollback;
- [ ] revocation/correction/withdrawal invalidation tests cover caches, maps, search, vector, graph, exports, and AI;
- [ ] reviewers approve under separation-of-duties posture;
- [ ] documentation and evidence ledger updated.

---

## Verification backlog

| Item | Status |
|---|---:|
| Exhaustive recursive config inventory | `NEEDS VERIFICATION` |
| Direct config consumer/loader | `UNKNOWN` |
| Discovery/precedence/fallback | `UNKNOWN` |
| Accepted owners and named authorities | `OWNER_TBD / NEEDS VERIFICATION` |
| `Site` versus `ArchaeologicalSite` | `CONFLICTED` |
| Collapsed versus decomposed object-family vocabulary | `CONFLICTED` |
| Transform/receipt vocabulary and homes | `CONFLICTED / NEEDS VERIFICATION` |
| Contract/schema lineage migration | `NEEDS VERIFICATION` |
| Domain/sensitivity policy layering | `NEEDS VERIFICATION` |
| Source-registry topology | `CONFLICTED` |
| Source-role vocabulary and accepted descriptors | `NEEDS VERIFICATION` |
| Cultural/Tribal/rights-holder reviewer roster | `NEEDS VERIFICATION` |
| Consent/revocation record authority and live lookup | `NEEDS VERIFICATION` |
| Public geometry floor and transform profiles | `NEEDS STEWARD RATIFICATION` |
| Package implementation | `GREENFIELD 0.0.0 / PLACEHOLDER` |
| Pipeline implementation | `PLACEHOLDER` |
| Pipeline specs | `EMPTY STAGE LISTS` |
| Policy implementation | `PROPOSED SCAFFOLDS / MIXED DEFAULTS` |
| Schema completeness | `EMPTY-PROPERTIES PERMISSIVE SCAFFOLDS` |
| Validator implementation | `NOT IMPLEMENTED IN OPENED FILES` |
| Source records | `PROPOSED/TBD PLACEHOLDERS` |
| Published-layer registry | `PROPOSED PLACEHOLDER — NOT RELEASE` |
| Explorer UI | `PLACEHOLDER EXPORTS` |
| Workflow enforcement | `TODO SCAFFOLD` |
| Tests/pass rates | `NEEDS VERIFICATION` |
| Burial/human-remains/sacred handling | `NEEDS VERIFICATION` |
| Collection custody/repatriation/security | `NEEDS VERIFICATION` |
| Chronology methods and uncertainty profiles | `NEEDS VERIFICATION` |
| Logging/telemetry/cache/index scanners | `NEEDS VERIFICATION` |
| Governed API/runtime/publication | `UNKNOWN` |
| Correction/revocation invalidation | `NEEDS VERIFICATION` |
| CODEOWNERS/branch protection | `NEEDS VERIFICATION` |

---

## Safe language rules

| Avoid | Prefer |
|---|---|
| “The config is active.” | “The README defines a boundary; direct consumer binding is not established.” |
| “The policy denies exact coordinates.” | “Exact-location denial is doctrine; opened policy files are scaffolds and runtime enforcement is unverified.” |
| “The schema validates sites.” | “Opened schemas are PROPOSED empty-permissive scaffolds.” |
| “The validator passed.” | “Opened validator entrypoints raise `NotImplementedError`; no result is claimed.” |
| “The source is registered.” | “A PROPOSED placeholder/TBD source record exists; admission and activation are unverified.” |
| “The layer is published.” | “A `status: PROPOSED` placeholder exists under a published-path lane; no release is proven.” |
| “This is an archaeological site.” | “This is a candidate/anomaly/context record unless reviewed evidence supports a governed site identity.” |
| “Exact location hidden.” | “No direct or indirect reconstruction channel is exposed under the accepted transform and review.” |
| “County generalization makes it public-safe.” | “Generalization is only one requirement; named authority, rights, sensitivity, review, evidence, policy, release, and looting risk still control.” |
| “The Tribe approved it.” | “A current governed review/authority record supports the specified use; do not generalize beyond its scope.” |
| “Consent was obtained.” | “A current scoped consent record exists and revocation has been checked.” |
| “No consent means public.” | “Missing or unclear consent/authority fails closed.” |
| “This artifact belongs to…” | “The cited record reports a custody/provenance assertion; ownership and cultural/legal status are not inferred.” |
| “LiDAR found a site.” | “LiDAR produced a candidate/anomaly under a stated method and uncertainty.” |
| “Historical route confirms the site.” | “The route is contextual evidence and does not confirm the site.” |
| “The UI hides it.” | “Protection is enforced upstream by accepted policy/release controls; client rendering is not the security boundary.” |
| “CI validates Archaeology.” | “The inspected domain workflow currently runs TODO echo jobs.” |

---

## Evidence ledger

| Evidence | State | Supports | Does not prove |
|---|---|---|---|
| Target README | prior blob `e429009d…`, v0.2 | Existing exact-location/cultural/reconstruction/failure/rollback safeguards. | Payloads or consumers. |
| Parent config README | blob `2c5e8b70…`, v0.4 | No-secret/no-authority child contract. | Archaeology runtime behavior. |
| Bounded config search | README only | No indexed payload/direct consumer. | Exhaustive absence. |
| Archaeology README | blob `e44040a1…` | Scope, objects, T4/CARE/exact-location doctrine. | Current implementation. |
| Canonical paths | blob `e2443077…` | Segmented path resolution, lineage paths, sensitive disposition guidance. | Accepted runtime policy or every path’s contents. |
| Cultural review | blob `2097297f…` | Named-authority, consent/revocation, CARE, review governance. | Implemented records or runtime checks. |
| Sensitivity/publication doc | blob `3522cfc1…` | Fail-closed categories and required release-support concepts. | Accepted reason codes or enforcement. |
| Contract README | blob `d857c0eb…` | Semantic boundary and object-family conflicts. | Complete contract/schema coverage. |
| `site.md` | blob `841ef554…` | Site/ArchaeologicalSite compatibility conflict. | Canonical resolution or site confirmation. |
| Package metadata/code | blobs `484e115e…`, `3578be96…` | Version 0.0.0 and placeholder layer file. | Working package. |
| Pipeline files | placeholder comments | Core paths exist as greenfield placeholders. | Executable processing. |
| Pipeline specs | `stages: []` | Spec paths exist. | Stage wiring. |
| Candidate/sacred/oral-history/AI policy files | `PROPOSED`, `default allow := false` | Fail-closed intent. | Complete rules, tests, runtime binding. |
| Precise-coordinate policy stubs | “No real rules yet”, `default deny := false` | Path/stub presence. | Safe enforcement. |
| Opened schemas | empty properties, additional properties allowed | Proposed paths and paired contract refs. | Meaningful validation. |
| Opened validators | `raise NotImplementedError` | Intended entrypoint paths. | Executable validation. |
| Source-role/source YAML | `PROPOSED` placeholders/TBD template | Candidate registry paths and topology conflict. | Accepted source roles, rights, or activation. |
| Published layer registry | `status: PROPOSED` placeholder | Path presence. | Released layer or public safety. |
| Explorer UI files | placeholder exports | Intended UI paths. | Real layers/Evidence Drawer/privacy enforcement. |
| Domain workflow | TODO echo jobs | Trigger/job scaffolding. | Substantive CI/proof/release. |
| Archaeology ADR files | `PROPOSED` scaffolds | Open decision handles. | Accepted decisions. |

---

<details>
<summary><strong>Appendix A — no-loss preservation note</strong></summary>

v0.2 established:

- the Archaeology config lane and documentation-only maturity;
- no archaeology truth, cultural authority, consent, source, evidence, policy, or release authority;
- exact/reconstructable location denial;
- burial, human-remains, sacred-site, restricted-knowledge, private-land, collection-security, and looting-risk safeguards;
- candidate-vs-confirmed separation;
- direct and indirect reconstruction controls;
- AI as interpretive and evidence-subordinate;
- minimum configuration contract;
- future validation, failure behavior, review, correction, and rollback.

v0.3 preserves those safeguards and adds:

- current repository and prior-blob evidence;
- bounded config inventory;
- actual scaffold/placeholder maturity across implementation-shaped surfaces;
- mixed policy-default warning;
- object-family, alias, path, policy-layer, receipt, and registry conflicts;
- named-authority, consent, revocation, sovereignty, and oral-history rules;
- collection custody/repatriation/security boundaries;
- chronology and uncertainty rules;
- remote sensing/LiDAR/geophysics/3D controls;
- cross-domain anti-confirmation;
- logging, telemetry, cache, search, vector, graph, export, and AI invalidation;
- stricter validation matrix and first-payload gate;
- safe-language and evidence ledgers.

No v0.2 safeguard is intentionally weakened.

</details>

<details>
<summary><strong>Appendix B — documentation-only boundary</strong></summary>

This revision changes no:

- executable config payload;
- consumer, loader, discovery, or precedence behavior;
- source descriptor, activation decision, connector, or watcher;
- schema, contract, policy, package, pipeline, validator, test, fixture, or workflow code;
- cultural authority, consent, revocation, review, or rights record;
- site, candidate, survey, artifact, collection, chronology, geometry, source payload, or interpretation;
- lifecycle, registry, receipt, proof, catalog, triplet, graph, or published artifact;
- release, correction, withdrawal, supersession, or rollback object;
- API, map, UI, search, vector, export, Focus Mode, AI, or deployment behavior.

Any future behavior change must be implemented and validated in its owning responsibility roots.

</details>

## Status summary

`configs/domains/archaeology/` is a README-only, non-secret, non-authoritative configuration-support lane. The surrounding repository contains rich Archaeology doctrine, contracts, and many implementation-shaped paths, but the inspected package, pipeline, specification, policy, schema, validator, source, published-layer, UI, workflow, and ADR surfaces remain draft, scaffolded, placeholder, conflicted, or unverified. No direct config consumer is established. Future payloads require explicit binding, accepted non-empty schemas and executable validators, accepted policy/runtime enforcement, named cultural authority, current consent/revocation, source rights, candidate/site and identity controls, exact-location and reconstruction denial, burial/sacred/human-remains and collection-security safeguards, evidence, review, transform receipts, release, correction, withdrawal, invalidation, and rollback.

<p align="right"><a href="#top">Back to top</a></p>
