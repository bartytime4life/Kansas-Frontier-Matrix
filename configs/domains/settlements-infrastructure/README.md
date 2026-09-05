<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-settlements-infrastructure-readme
title: configs/domains/settlements-infrastructure/ — Governed Settlements and Infrastructure Configuration Boundary
type: readme
version: v0.3
status: draft; repository-grounded; README-only configuration lane; non-authoritative
owners:
  - "@bartytime4life — verified /configs/ CODEOWNERS review route only"
  - "NEEDS VERIFICATION — accountable configuration, domain, place-identity, legal-status, infrastructure-sensitivity, source/rights, cultural/sovereignty, consumer, validation, policy, and release stewardship"
created: 2026-07-13
updated: 2026-09-04
policy_label: "public; config-sublane; settlements-infrastructure; place-identity-aware; legal-status-aware; critical-asset-aware; cultural-context-aware; source-role-aware; time-aware; non-secret; non-authoritative; no-live-binding; no-service-guarantee; not-emergency-operations; no-release-authority"
current_path: configs/domains/settlements-infrastructure/README.md
owning_root: configs/
readme_profile: BOUNDARY_COMPACT
responsibility: "Document safe, non-secret Settlements/Infrastructure configuration authoring and future explicit consumer binding without acquiring place, municipal, infrastructure, source, evidence, policy, emergency, or release authority."
truth_posture: "CONFIRMED pinned tracked configuration path, parent configuration contract, accepted Directory Rules adoption, current Settlements/Infrastructure workflow source, current test-index posture, and review routing; PROPOSED future inactive configuration classes and consumer-bound profiles; UNKNOWN runtime consumption, loader precedence, live source integration, and public use; NEEDS VERIFICATION accountable stewardship, exact-head validation, rights, legal-status authority, sensitivity enforcement, and release integration."
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  base_ref: main
  base_commit: 9e152476cda7bd9b80a2afac8031619a1898eceb
  prior_blob: 55104307922fca18285b2db2e546739332a3e207
  parent_readme_blob: c497e41466f3aaf934aeca4b9976a2fa8516ff21
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  domain_workflow_blob: a47d89c40efd58ac31bc44dbc56bdfb1ccc3a325
  domain_test_readme_blob: 08cd09f1700ca02fae7a35c55a1c22684c996448
related:
  - ../README.md
  - ../../README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../docs/domains/settlements-infrastructure/IDENTITY_MODEL.md
  - ../../../docs/domains/settlements-infrastructure/SENSITIVITY.md
  - ../../../contracts/domains/settlements-infrastructure/README.md
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md
  - ../../../policy/domains/settlements-infrastructure/README.md
  - ../../../fixtures/domains/settlements-infrastructure/README.md
  - ../../../tests/domains/settlements-infrastructure/README.md
  - ../../../tools/validators/domains/settlements-infrastructure/README.md
  - ../../../data/registry/sources/settlements-infrastructure/README.md
  - ../../../data/proofs/settlements-infrastructure/README.md
  - ../../../release/candidates/settlements-infrastructure/README.md
  - ../../../.github/workflows/domain-settlements-infrastructure.yml
tags: [kfm, configs, settlements, infrastructure, municipalities, places, facilities, service-areas, dependencies, critical-assets, source-role, time, sensitivity, no-secrets, no-live-binding, governance]
notes:
  - "v0.3 supersedes v0.2 documentation at this same path; no executable configuration payload, consumer, schema, contract, policy, source record, workflow, runtime, release object, or public artifact is changed."
  - "README-only describes this tracked configuration lane, not the whole Settlements/Infrastructure domain. Current workflow source performs bounded static/readiness checks and explicit proof/release holds; it does not establish semantic validation, source admission, or publication readiness."
  - "The earlier July blanket scaffold inventory is revision history, not current implementation proof. This revision narrows claims to current repository evidence inspected for this update."
  - "Configuration may reference an accepted place-identity, source, temporal, sensitivity, public-safe geometry, service-area, dependency, review, or release profile; it cannot create or weaken those authorities."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Settlements and Infrastructure Domain Configuration

`configs/domains/settlements-infrastructure/` is the safe configuration boundary for settlement, community, municipal, facility, network, service-area, and infrastructure presentation or processing **only after a named consumer and governing profiles are explicit**.

**Status:** draft v0.3 · **Tracked configuration payload:** README only · **Owning root:** `configs/` · **Consumer binding:** UNKNOWN

[Purpose](#purpose) · [Authority](#authority-level) · [Evidence](#status-and-evidence) · [Placement](#repository-fit-and-directory-rules-basis) · [Configuration contract](#minimum-configuration-contract) · [Identity](#place-identity-legal-status-and-object-boundaries) · [Infrastructure safety](#critical-infrastructure-facilities-services-and-dependencies) · [Time](#time-freshness-and-stale-state) · [Validation](#validation-and-test-matrix) · [Rollback](#rollback-correction-supersession-and-invalidation)

> [!CAUTION]
> Configuration is not municipal or legal authority, title proof, source authority, infrastructure-status authority, service-availability authority, emergency guidance, security clearance, evidence closure, policy approval, or release authority. Missing evidence, unclear rights, stale status, uncertain legal meaning, unresolved cultural authority, or sensitive infrastructure detail must fail closed at the applicable governed boundary.

## Purpose

This page inherits the [domain configuration contract](../README.md) and the [configuration root contract](../../README.md). It records only the Settlements/Infrastructure-specific constraints a maintainer needs before drafting or binding a configuration file.

A future configuration may help a verified consumer select labels, display modes, aggregation, public-safe geometry, freshness presentation, source-role badges, relation rendering, or review routing for already-governed material. It cannot decide whether a settlement exists, whether a municipality has a particular legal status, whether a census geography is a jurisdiction, whether a facility is operating, whether a service is available, whether a dependency is complete, whether a place is safe to approach, or whether a public release is permitted.

The audience is configuration maintainers, consumer owners, Settlements/Infrastructure reviewers, place-identity and legal-status reviewers, infrastructure-security reviewers, cultural/sovereignty reviewers, and source, rights, validation, policy, and release stewards.

## Authority level

**Implementation-supporting and non-authoritative.** A configuration value may point to authority; it cannot become authority by repetition or successful parsing.

| Concern | Owning authority or evidence | Configuration limit |
|---|---|---|
| Domain meaning and object semantics | [Domain doctrine](../../../docs/domains/settlements-infrastructure/README.md) and accepted semantic contracts | No merging or redefining settlement, municipality, census place, townsite, facility, operator, service area, or dependency semantics. |
| Machine shape | [Schema lane](../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md) | Reference an accepted shape; do not create a second schema home. |
| Place identity and legal status | Accepted identity/legal sources, contracts, evidence, and review | No canonical-name selection, incorporation inference, annexation/dissolution inference, or census-place-to-municipality conversion. |
| Sources, rights, freshness | Source registry and applicable governance | No source admission, role upgrade, rights clearance, freshness extension, or network activation. |
| Sensitivity and public-safe representation | Applicable policy, review, and transform evidence | No weakening of critical-infrastructure, cultural, sovereignty, private-land, archaeology, or living-person protections. |
| Evidence and review | Resolvable EvidenceRef -> EvidenceBundle and review records | No invented evidence closure or approval. |
| Release and correction | Governed release/correction records | A config, successful check, map display, or file move is not release. |
| Consumer operation | Exact loader/binding/validation/runtime evidence | No implicit discovery, precedence, remote include, deployment, or public use. |

Preserve `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED`. Configuration cannot skip or authorize a lifecycle transition.

## Status and evidence

This revision was prepared from current GitHub evidence at `main@9e152476cda7bd9b80a2afac8031619a1898eceb`.

### Current bounded findings

| Surface | Confirmed at the snapshot | What remains unproved |
|---|---|---|
| This configuration lane | The target README exists under the canonical `configs/domains/settlements-infrastructure/` path. | Any executable config payload, loader, ignored/untracked files, or runtime consumption. |
| Parent domain configuration contract | `configs/domains/README.md` is v0.6 and explicitly keeps child lanes non-secret, non-authoritative, and inactive unless consumer binding is verified. | Generic discovery, merge order, precedence, runtime behavior, and publication behavior. |
| Directory governance | ADR-0029 is accepted and points to the exact current Directory Rules v2 bytes under `docs/doctrine/`. | No new path, alias, root, or authority change is introduced here. |
| Domain workflow | `.github/workflows/domain-settlements-infrastructure.yml` performs bounded readiness checks, parses current schemas/fixtures structurally, and records explicit semantic-validation, proof, and release holds. | Accepted semantic validation, proof production, release dry run, source admission, or publication readiness. |
| Domain tests | `tests/domains/settlements-infrastructure/README.md` is a domain-test parent index and explicitly keeps executable coverage/pass rates as NEEDS VERIFICATION. | Exact executable test inventory, exact-head pass results, policy runtime, release integration, and public-surface invalidation. |
| Review routing | `/configs/` has a CODEOWNERS review route to `@bartytime4life`. | Accountable specialist ownership, independent review, required-review enforcement, and approval. |
| Runtime/release/publication | Not established by this README. | Live source use, production binding, deployment, release, publication, or emergency operation. |

The July v0.2 maturity table described many package, pipeline, schema, policy, validator, and workflow surfaces as broad placeholders. That statement is retained only as historical lineage. This v0.3 page narrows its currentness claims to the surfaces actually re-inspected for this revision and does not imply a whole-domain audit.

## What belongs here

Safe, non-secret configuration documentation and, when separately scoped, small **inactive** templates or synthetic examples for a named or conspicuously proposed consumer.

Suitable future classes include:

| Proposed class | Bounded purpose |
|---|---|
| `place_presentation` | Labels, place-type display, source-role badges, uncertainty, historical/current distinction. |
| `temporal_profile_ref` | Reference accepted rules for source, observed, valid, retrieval, release, and correction time. |
| `public_safe_geometry_ref` | Reference policy-owned aggregation, generalization, redaction, suppression, or delay. |
| `facility_context` | Presentation-only settings for already-cleared facility or infrastructure context. |
| `service_area_presentation` | Render already-governed service-area evidence without implying entitlement or current availability. |
| `dependency_presentation` | Render already-governed dependencies without inferring completeness, criticality, vulnerability, or operational status. |
| `review_routing` | Select a governance review path; never approve or release. |
| `synthetic_test_profile` | Deterministic, fictional, no-network authoring input. |
| `migration_compatibility` | Explicit, time-bounded consumer migration with rollback and no parallel authority. |

These are authoring categories, not an adopted schema or implemented enumeration.

## What does not belong here

Do not place the following in this directory:

- credentials, tokens, cookies, private endpoints, workstation bindings, or signed URLs;
- real source records, evidence objects, proofs, receipts, policy decisions, review records, release decisions, or lifecycle data;
- municipal legal determinations, incorporation/annexation/dissolution decisions, title or ownership assertions;
- exact or reconstructable critical-infrastructure details, vulnerability data, restricted access routes, private facility internals, or sensitive dependency topology;
- cultural or sovereignty-sensitive precision without accepted review and public-safe treatment;
- schemas, semantic contracts, validators, executable tests, runtime code, pipelines, caches, or published artifacts;
- live alerting, emergency, dispatch, incident-command, or service-guarantee settings;
- files whose only purpose is to bypass an unresolved canonical-home or alias decision.

## Repository fit and Directory Rules basis

The owning responsibility root remains `configs/`. This document describes safe configuration authoring; it does not own domain doctrine, machine shape, policy, evidence, lifecycle state, or release state.

[ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) accepted the exact [Directory Rules v2](../../../docs/doctrine/directory-rules.md) bytes as the placement authority. Under those rules, domain scope refines an existing responsibility root rather than creating a root-level domain home. The `BOUNDARY_COMPACT` README posture is appropriate here because the parent contracts carry shared configuration rules.

Meaning stays in `contracts/`; shape in `schemas/`; admissibility in `policy/`; source descriptors and lifecycle records in governed `data/` homes; enforceability in tests/tooling; and release/correction decisions in `release/`. This update creates no new root, alias, schema home, policy home, source registry, proof home, or release home.

## Minimum configuration contract

A future executable binding should not be accepted until it identifies, at minimum:

- `config_id` and immutable `config_version`;
- exact `consumer_id` and owner;
- explicit configuration class and bounded purpose;
- accepted contract/schema/profile references;
- exact parser and supported version;
- required/optional-file behavior;
- unknown-key, duplicate-key, malformed-input, and unsupported-version behavior;
- remote-include and environment-substitution policy;
- source/network activation boundary;
- rights, sensitivity, cultural/sovereignty, and public-safe profile references where applicable;
- material time/freshness behavior;
- validation command and negative fixtures;
- rollback/deactivation target;
- migration/supersession relationship.

These are design requirements, not proof that such fields or a loader currently exist.

### Consumer binding and precedence

No loader is established by this README. A future consumer must select a file intentionally, validate its exact supported profile, apply configuration atomically, and fail closed on malformed or ambiguous inputs. Directory scanning must not become feature activation, network activation, source admission, or release authority.

Local, test, deployment, or runtime overrides must never override source role, rights, evidence, legal status, sensitivity, review, release state, or official validity. Public callers must not be able to choose arbitrary filesystem paths or policy profiles.

## Place identity, legal status, and object boundaries

Keep these families distinct unless an accepted contract explicitly relates them:

- `Settlement`
- `Municipality`
- `CensusPlace`
- `Townsite`
- `GhostTown`
- `Fort`
- `Mission`
- `ReservationCommunity`
- `InfrastructureAsset`
- `NetworkNode`
- `NetworkSegment`
- `Facility`
- `ServiceArea`
- `Operator`
- `ConditionObservation`
- `Dependency`

Configuration must not collapse display-name equality, coordinate proximity, geometry overlap, historic continuity, census geography, administrative rosters, or generated summaries into identity or legal status.

Historic and current places can share names while representing different objects, extents, jurisdictions, time scopes, or evidence states. Preserve source identity, object role, temporal scope, and correction lineage where material.

## Source role and knowledge character

A source may support observation, official/administrative status, contextual history, model output, classification, aggregate statistics, or another accepted role. Configuration may select a display treatment for an already-resolved role; it cannot upgrade one role into another.

Do not treat:

- census geography as legal municipal authority;
- a gazetteer as proof of current legal status;
- operator-provided coverage as independently verified service availability;
- a model or inferred graph edge as an observed dependency;
- a map label as identity proof;
- a published derivative as the source record it summarizes.

## Time, freshness, and stale state

Keep material time kinds distinct. At minimum, do not silently collapse source vintage, observation time, validity/effective time, retrieval time, release time, and correction time.

A future config may reference an accepted freshness profile and choose how stale state is displayed. It must not extend official validity, hide stale state, substitute a cached historical value as current, or convert missing data into a reassuring fallback.

## Critical infrastructure, facilities, services, and dependencies

Infrastructure detail is consequence-sensitive. Missing classification or uncertain public-safety posture must not default to precision.

Configuration may reference an accepted public-safe profile, but it cannot decide that exact geometry, operator detail, condition, access information, dependency topology, vulnerability, service availability, or private-property context is safe to expose.

Public-facing views should prefer the least precise representation that still serves the released claim. When exactness would create security, privacy, cultural, sovereignty, archaeological, or private-land risk, use accepted generalization, aggregation, suppression, delay, or denial and preserve transform provenance.

No configuration value may promise that a facility is open, a utility is available, a road/bridge is safe, a service area confers entitlement, a dependency is complete, or a site is appropriate to visit.

## Historic, cultural, community, and sovereignty context

Settlement history can intersect tribal sovereignty, missions, forts, reservation communities, archaeology, cemeteries, sacred places, and living communities. Configuration must not flatten these contexts into a neutral place-name list or expose precise sensitive locations merely because geometry is available.

When authority, rights, cultural review, or precision is unresolved, the safe outcome is redaction, generalization, restricted review, or abstention according to governing policy—not a config-local exception.

## Validation and test matrix

Default validation should be deterministic, synthetic, and no-network.

| Gate | Expected result |
|---|---|
| UTF-8 / parseability / supported version | reject malformed or unsupported input atomically |
| Unknown and duplicate keys | reject unless an accepted compatibility rule says otherwise |
| Placeholder and secret hygiene | reject secret-like values, unsafe real identifiers, or undocumented substitutions |
| Consumer binding | reject absent or ambiguous consumer identity before executable use |
| Authority/profile references | reject unresolved or incompatible binding for executable use |
| Time/freshness | preserve time kinds and expose stale/unknown state |
| Place/legal-status boundary | reject inference from labels, census geography, proximity, or config-local aliases |
| Infrastructure sensitivity | deny exact/reconstructable exposure without accepted public-safe posture |
| Source role | preserve role; reject role upcast |
| Evidence/release | config cannot satisfy evidence, approval, release, or publication gates |
| Negative fixtures | prove malformed, stale, ambiguous, unsupported, sensitive, and authority-conflicting inputs fail safely |
| Network | default tests perform no live source requests |

Current workflow evidence establishes readiness/static checks and explicit holds, not domain semantic validation or release readiness. Exact-head hosted results remain separate evidence.

## Review burden

A README-only wording correction is low runtime risk but can still affect governance interpretation. Review should confirm:

1. the path remains inside the accepted `configs/` authority boundary;
2. legal-status and place-identity language does not overclaim authority;
3. critical-infrastructure and public-safe geometry limits remain fail closed;
4. cultural/sovereignty-sensitive context is not reduced to ordinary public location data;
5. source-role and time distinctions remain explicit;
6. test/workflow language does not turn readiness checks or holds into passing semantic validation;
7. no statement implies release, deployment, publication, emergency operation, or service guarantees.

CODEOWNERS routing is not proof of specialist review or accepted ownership.

## Governed AI and generated language

AI may summarize already-released evidence through governed interfaces. It may not infer municipal status, place continuity, facility condition, access rights, service availability, infrastructure vulnerability, dependency completeness, cultural authority, or public-safety posture from this configuration.

A generated answer that lacks admissible evidence must abstain. Generated language cannot become source truth, policy, approval, or release state.

## Rollback, correction, supersession, and invalidation

Configuration changes must be reversible independently of source data and release state.

A future binding should record the prior config version/digest, current config version/digest, consumer, activation state, affected outputs, migration reason, disable/revert procedure, and whether derived caches or views require invalidation.

Rollback of configuration does not roll back source evidence, legal status, infrastructure condition, policy, review, or release state. Those families require their own governed correction/rollback procedures.

If this README is later found inaccurate, correct it forward or revert the documentation change through normal review. Do not rewrite source evidence, receipts, or release history to make the documentation appear retrospectively correct.

## Definition of done for the first executable payload

The first non-README config payload is not complete merely because it parses. Before executable binding, require:

1. named consumer and accountable owner;
2. accepted placement and profile references;
3. restrictive schema/contract binding;
4. deterministic parser/loader behavior;
5. no-network synthetic positive and negative fixtures;
6. explicit unknown-key/version/duplicate/fallback behavior;
7. secret and sensitive-value controls;
8. place-identity and legal-status anti-collapse checks;
9. critical-infrastructure/public-safe geometry checks;
10. source-role and material-time checks;
11. documented rollback/deactivation;
12. applicable review and CI evidence.

Source admission, deployment, release, publication, emergency operation, and public exposure remain separate transitions.

## Related folders

| Responsibility | Reference |
|---|---|
| Parent domain config boundary | [`../README.md`](../README.md) |
| Config root | [`../../README.md`](../../README.md) |
| Human domain doctrine | [`../../../docs/domains/settlements-infrastructure/README.md`](../../../docs/domains/settlements-infrastructure/README.md) |
| Directory governance | [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) |
| Accepted Directory Rules decision | [`../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) |
| Semantic contract lane | [`../../../contracts/domains/settlements-infrastructure/README.md`](../../../contracts/domains/settlements-infrastructure/README.md) |
| Schema lane | [`../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md`](../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md) |
| Policy lane | [`../../../policy/domains/settlements-infrastructure/README.md`](../../../policy/domains/settlements-infrastructure/README.md) |
| Fixture lane | [`../../../fixtures/domains/settlements-infrastructure/README.md`](../../../fixtures/domains/settlements-infrastructure/README.md) |
| Test lane | [`../../../tests/domains/settlements-infrastructure/README.md`](../../../tests/domains/settlements-infrastructure/README.md) |
| Validator boundary | [`../../../tools/validators/domains/settlements-infrastructure/README.md`](../../../tools/validators/domains/settlements-infrastructure/README.md) |
| Source registry | [`../../../data/registry/sources/settlements-infrastructure/README.md`](../../../data/registry/sources/settlements-infrastructure/README.md) |
| Proof lane | [`../../../data/proofs/settlements-infrastructure/README.md`](../../../data/proofs/settlements-infrastructure/README.md) |
| Release-candidate lane | [`../../../release/candidates/settlements-infrastructure/README.md`](../../../release/candidates/settlements-infrastructure/README.md) |
| Domain workflow | [`../../../.github/workflows/domain-settlements-infrastructure.yml`](../../../.github/workflows/domain-settlements-infrastructure.yml) |

## Last reviewed

**2026-09-04** — repository-currentness pass against `main@9e152476cda7bd9b80a2afac8031619a1898eceb`.

### Open verification

- accountable Settlements/Infrastructure stewardship and independent review roles;
- exact executable config consumer, loader, precedence, and reload behavior;
- accepted source-role vocabulary and source admission state;
- legal-status authority and place-identity conflict resolution;
- cultural/sovereignty review routing;
- exact critical-infrastructure sensitivity policy and public-safe profiles;
- semantic validation, negative fixtures, and exact-head hosted results;
- proof production, release integration, deployment, publication, correction propagation, and rollback drills.
