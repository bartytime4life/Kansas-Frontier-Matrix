<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-hazards-readme
title: configs/domains/hazards/ — Governed Hazards Configuration Boundary
type: readme
version: v0.4
status: draft; repository-grounded; README-only configuration lane; non-authoritative
owners:
  - "@bartytime4life — verified /configs/ CODEOWNERS review route only"
  - "NEEDS VERIFICATION — accountable configuration, Hazards, source/rights, public-safety boundary, freshness, sensitivity, consumer, validation, policy, and release stewardship"
created: 2026-07-13
updated: 2026-09-04
policy_label: "public; config-sublane; hazards; contextual-only; not-for-life-safety; alert-authority-denied; source-role-aware; freshness-aware; infrastructure-sensitive; non-secret; non-authoritative; no-live-binding; no-source-activation; no-notification-activation; no-release-authority"
current_path: configs/domains/hazards/README.md
owning_root: configs/
readme_profile: BOUNDARY_COMPACT
responsibility: "Document safe, non-secret Hazards configuration authoring and future explicit consumer binding without acquiring source, evidence, policy, alerting, or release authority."
truth_posture: "CONFIRMED pinned tracked configuration inventory, parent contracts, accepted Directory Rules adoption, review routing, and workflow source; PROPOSED future configuration classes and payload/binding profiles; UNKNOWN runtime consumption, live enforcement, source admission, and public use; NEEDS VERIFICATION accountable stewardship and exact-head behavioral validation."
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  base_ref: main
  base_commit: 700570cbcf191038aa20a030174c2dd08cf93675
  main_tree: f98d5965812e9a29f55d820f9942549719930408
  prior_blob: 9ea59b80a1e73fb0cd4f3dc23b30b39c9c8cea10
  tracked_config_files: [README.md]
  parent_readme_blob: c497e41466f3aaf934aeca4b9976a2fa8516ff21
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  domain_workflow_blob: a13416bda7deed696aadccb81f0009bd4fc22c18
related:
  - ../README.md
  - ../../README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../contracts/domains/hazards/README.md
  - ../../../schemas/contracts/v1/domains/hazards/README.md
  - ../../../policy/domains/hazards/README.md
  - ../../../fixtures/domains/hazards/README.md
  - ../../../tests/domains/hazards/README.md
  - ../../../release/candidates/hazards/README.md
  - ../../../.github/workflows/domain-hazards.yml
tags: [kfm, configs, hazards, contextual-only, not-for-life-safety, source-role, freshness, sensitivity, no-secrets, governance]
notes:
  - "v0.4 supersedes v0.3 documentation at this same path; no executable payload, consumer, schema, policy, source record, workflow, or release object changes."
  - "README-only describes this tracked configuration directory, not the whole Hazards domain. The workflow now invokes bounded synthetic validation and retains explicit proof/release holds."
  - "The earlier July inventory and alias observations remain revision history, not current implementation proof. Main and linked source files must be re-pinned before a subsequent change."
  - "Existing section anchors are retained. Configuration field/class examples below are proposals, not an adopted schema or implemented loader."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Hazards Domain Configuration

`configs/domains/hazards/` provides the configuration boundary for **hazard history, analysis, and contextual presentation—not emergency alerting**.

**Status:** draft v0.4 · **Tracked contents:** README only · **Owning root:** `configs/` · **Consumer binding:** UNKNOWN

[Evidence](#status-and-evidence) · [Placement](#repository-fit-and-directory-rules-basis) · [Future binding](#minimum-configuration-contract) · [Safety](#not-for-life-safety-and-official-source-referral) · [Validation](#validation-and-test-matrix) · [First payload](#definition-of-done-for-the-first-payload) · [Rollback](#rollback-correction-supersession-and-invalidation)

> [!CAUTION]
> **KFM is not an emergency alert system. KFM-as-alert-authority is T4 forever.** Configuration cannot issue, synthesize, rank, suppress, extend, cancel, replace, or operationalize warnings, watches, advisories, evacuation instructions, shelter directions, road-safety instructions, medical guidance, or incident-command actions. Official operational products remain attributed context with visible validity/expiry, a not-for-life-safety disclaimer, and referral to appropriate official authorities. These are governing requirements, not a claim that runtime enforcement has been proved.

## Purpose

Inherit the [domain configuration contract](../README.md) and [configuration root contract](../../README.md). This page adds the Hazards-specific constraints that a maintainer needs before drafting a template or binding it to a consumer.

A future configuration may help a named consumer label, qualify, generalize, cache, or present already-governed context. It cannot decide whether an event is true, a source is active, a warning is actionable, an area is safe, or an artifact is released. The audience is configuration maintainers, consumer owners, Hazards reviewers, and source, rights, freshness, sensitivity, policy, and release reviewers.

**Inputs:** parent configuration contracts, accepted decisions, source/profile references, and explicitly synthetic authoring inputs. **Outputs:** reviewable configuration documentation and inactive candidate templates, not lifecycle records, approvals, or public artifacts.

## Authority level

**Implementation-supporting, contextual-only, and non-authoritative.** Configuration may reference an accepted decision; it may not manufacture or override it.

Preserve `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`. Promotion is a governed transition, not a file move; configuration cannot skip a lifecycle gate.

| Concern | Owning authority or required evidence | Configuration limit |
|---|---|---|
| Domain meaning and object semantics | [Hazards doctrine](../../../docs/domains/hazards/README.md) and [semantic contracts](../../../contracts/domains/hazards/README.md) | No conversion of a detection, model, declaration, or aggregate into an observation. |
| Machine shape | [Hazards schema lane](../../../schemas/contracts/v1/domains/hazards/README.md) | Refer to an appropriate versioned profile; do not define a second schema home. |
| Admissibility, rights, and sensitivity | [Hazards policy boundary](../../../policy/domains/hazards/README.md) and applicable source governance | No policy weakening, rights clearance, source-role upgrade, or exact-location permission. |
| Evidence and review | Resolvable EvidenceRef -> EvidenceBundle and applicable review records | No invented evidence closure, approval, or accepted stewardship. |
| Release and correction | [Release-candidate boundary](../../../release/candidates/hazards/README.md) and governed release records | A candidate, config value, successful check, or file move is not a release. |
| Consumer operation | Exact loader, binding, validation, and runtime evidence | No implicit discovery, precedence, network access, notification, or deployment. |
| Emergency authority | [Permanent life-safety boundary](../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md) | None; not unlockable by configuration, an AI prompt, a UI mode, or a release. |

## Status and evidence

### Evidence snapshot

This revision inspected GitHub at `main@700570cbcf191038aa20a030174c2dd08cf93675`, tree `f98d5965812e9a29f55d820f9942549719930408`. The previous target blob is `9ea59b80a1e73fb0cd4f3dc23b30b39c9c8cea10`.

The exact tracked contents of this directory are:

```text
configs/domains/hazards/
└── README.md
```

### Current maturity matrix

| Surface | Confirmed at the snapshot | What remains unproved |
|---|---|---|
| This configuration directory | One tracked README and no child directory or executable configuration payload. | Ignored, untracked, externally stored configuration, loaders, and runtime use. |
| Parent configuration guidance | The domain parent is v0.6; the root is v0.5. Both separate configuration from governance authority. | General discovery, merge order, or universal consumer binding. |
| Hazards domain | The domain README describes mixed maturity; fixture and test indexes document bounded synthetic families alongside incomplete lanes. | Whole-domain completeness or production readiness. README-only is not a domain-wide maturity label. |
| Domain workflow | Source invokes drought smoke tests, `make hazards-validate`, and workflow-binding tests. | Exact-head execution and results in this authoring session. The workflow is no longer TODO-only. |
| Proof and release jobs | Workflow source explicitly retains proof-producer and release-dry-run holds. | Accepted proof production, release assembly, promotion, deployment, or publication. A successful hold check proves none of these. |
| Review routing | `/configs/` routes to `@bartytime4life` in CODEOWNERS. | Accountable specialist stewardship, required-review enforcement, and independent approval. |
| Source and public integration | No such capability is established by this README. | Live admission, rights, freshness, evidence closure, policy execution, warning-feed operation, cache invalidation, and public-use safety. |

### Evidence boundary

The July v0.3 blanket descriptions of placeholder tests and an echo-only workflow are superseded by this bounded current-state account. Its wider connector, registry, schema-alias, and manifest inventory is **historical**, not automatically reverified here. This revision does not settle those seams or claim an exhaustive consumer audit.

[Workflow source](../../../.github/workflows/domain-hazards.yml), [fixture index](../../../fixtures/domains/hazards/README.md), and [test index](../../../tests/domains/hazards/README.md) remain separate evidence surfaces. Their prior test receipts are not this revision's test results.

**Source lineage:** the Drive *Directory Rules* document and *KFM Hazards Architecture — Extended Pro PDF-Only Implementation Blueprint* (2026-04-21; Drive ID `1nTzBV_-7_-DzzXxCQPsrQRGffoO2zZSv`, pp. 1–3) support responsibility separation and the contextual-only boundary. The blueprint explicitly lacked a mounted repository; its proposed paths and source checks are not current repository or live-source proof. The Notion Hazards builder's August 31 monitoring entry is coordination history; GitHub records its PR #4001 as merged, not an open blocker for this file.

## What belongs here

Safe, non-secret configuration documentation and, when separately scoped, small **inactive** templates or synthetic examples. Future payloads may select reviewed presentation, freshness, official-referral, public-safe transformation, review-routing, or compatibility profiles for a named contextual consumer.

Unmistakably synthetic authoring may proceed with a **PROPOSED** consumer/profile and explicit non-effects. Missing production approval does not prohibit drafting; it prohibits treating that draft as an active or approved binding. No such payload is added in this revision.

## What does not belong here

Real warnings or source records; credentials, tokens, cookies, signed URLs, private endpoints or workstation bindings; emergency contacts or notification destinations; protected coordinates or reconstructable infrastructure/person details; source admission or role decisions; policy parameters that create or weaken protection; schemas, semantic contracts, receipts, proofs, release decisions, lifecycle data, runtime code, caches, or public artifacts.

Also prohibited are hidden current-condition claims, reassuring fallbacks for missing data, expired-as-current display, KFM-authored protective actions, arbitrary public-user profile selection, and parallel files created to bypass an unresolved canonical-home decision.

## Repository fit and Directory Rules basis

[Accepted ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [Directory Rules v2](../../../docs/doctrine/directory-rules.md) bytes, including their retained `PROPOSED_FOR_ADOPTION` source label. The accepted decision—not that frozen label in isolation—establishes adoption.

### Directory Rules decisions preserved

The owning root stays `configs/`: this file documents safe configuration, not Hazards truth. The `hazards` segment refines that responsibility; it does not create a root-level domain. Directory Rules §16.3 supplies the `BOUNDARY_COMPACT` profile, and `DIR-README-003` limits the directory map to this directory and its direct children. Parent contracts carry shared configuration obligations.

Meaning remains in `contracts/`, shape in `schemas/`, admissibility in `policy/`, examples in `fixtures/`, validation in `tests/` and tooling, lifecycle instances in `data/`, and release/correction decisions in `release/`. The verified links above navigate those responsibilities; they do not establish that every object or implementation within them is accepted. No new home, move, rename, or ADR is introduced.

## Configuration classes

These are **PROPOSED authoring classes**, retained from v0.3, not an implemented enumeration or accepted configuration schema.

| Class | Bounded purpose |
|---|---|
| `context_presentation` | Labels, attribution, source-role badges, uncertainty, historical/stale state. |
| `freshness_profile_ref` | Reference a governed, source/product-specific validity profile; never extend official validity. |
| `official_referral_profile_ref` | Reference reviewed authority links and neutral referral wording, without completeness guarantees. |
| `public_safe_profile_ref` | Reference policy-owned aggregation, redaction, suppression, or delay; never authorize exposure. |
| `review_routing` | Select a governance-review route; never approve or contact emergency responders. |
| `feature_toggle` | Non-consequential, non-alerting presentation only; never source, network, or release activation. |
| `synthetic_test_profile` | Deterministic synthetic, non-operational test inputs. |
| `migration_compatibility` | Explicit, time-bounded mapping with one writer, consumer impact, and rollback. |

Prefer one class per payload; document the atomic dependency when more than one is necessary.

## Minimum configuration contract

### Identity and ownership

A future binding must establish `config_id`, immutable `config_version`, proposed/accepted class, exact `consumer_id`, accountable owner, bounded purpose, authority/profile references, supersession relationship, and rollback target. These field names describe design requirements, not an adopted schema. An inactive draft must visibly retain unresolved ownership and profile status rather than invent accepted values.

### Parsing and loading

Before execution, document the exact allowlisted filename, encoding, parser, supported version, restrictive shape, required/optional-file behavior, duplicate/unknown-key rejection, atomic failure behavior, permitted substitutions/includes, external-reference policy, reload semantics, and disabled fallback. No remote include or environment substitution may silently introduce secrets, policy overrides, or executable behavior.

### Hazards-specific context

Bind the object family, originating source/product identity, source role, material times, validity/expiry profile, disclaimer, referral, audience, output surface, public-safe profile, cross-lane references, review requirements, release constraints, and correction/invalidation behavior. Live source identity, rights, and activation must be verified at the transition that uses them; synthetic drafting is not source admission.

### Safety controls

Validation defaults to no-network fixtures. No file-presence activation, notification/contact field, real operational identifier, exact protected geometry, permissive fallback, partial application, or concealed production binding is allowed. A valid config does not waive evidence, rights, sensitivity, policy, review, or release requirements.

## Consumer binding, precedence, and discovery

### Required binding record

**No Hazards config loader is established here.** A future consumer must intentionally select a named file and version/digest, validate its exact profile, record safe selection evidence where consequential, and provide atomic disable/revert behavior. Directory scanning is not source or feature activation authority.

### Safe precedence principles

Defaults, test, local, deployment, and runtime overrides need an explicit order. They must not override policy, rights, source role, evidence, release, sensitivity, official validity, disclaimer, or referral. Unknown keys/versions, duplicate keys, ambiguous aliases, malformed inputs, missing required configuration, and failed reloads must not yield a partially applied or permissive configuration. Public callers cannot select arbitrary paths or policy profiles.

## Hazards object family boundaries

The [domain README](../../../docs/domains/hazards/README.md) identifies these families. Their presence in this table does not prove a corresponding accepted config schema or runtime.

| Family | Preserve | Never infer from it alone |
|---|---|---|
| `HazardEvent` / `HazardObservation` | Sourced event versus measured/observed datum. | Current danger, complete event confirmation, forecast, or action. |
| `WarningContext` / `AdvisoryContext` | Attributed official-source product/reference and its validity. | KFM issuance, endorsement, extension, cancellation, or priority. |
| `DisasterDeclaration` | Administrative declaration and effective scope. | Observed damage, current conditions, or individual eligibility. |
| `FloodContext` | Explicit regulatory, modeled, historical, or observed support. | Current inundation, an evacuation zone, or route safety. |
| `WildfireDetection` | Detection/candidate status and source limitations. | Confirmed perimeter, incident status, or evacuation need. |
| `SmokeContext` | Polygon, model, observation, or advisory character. | Ground-level PM2.5, local visibility, or health instructions. |
| `DroughtIndicator` | Classification/index, geography, and period. | Current water supply, crop outcome, or emergency status. |
| `EarthquakeEvent` / `HeatColdEvent` | Sourced phenomenon and its uncertainty. | Damage, building safety, individual medical risk, or official emergency status. |
| `ExposureSummary` / `ResilienceSummary` | Derived join, method, scale, and uncertainty. | Observed impact, loss, casualties, readiness, or safety guarantees. |
| `HazardTimeline` / `ImpactArea` | Sourced chronology or area with role and limits. | Complete incident history or an official/verified operational footprint. |

### Load-bearing anti-collapse rules

```text
official warning context != KFM-issued alert
administrative declaration != observed hazard event
regulatory flood zone != observed inundation
sensor detection != confirmed event
smoke polygon != ground-level PM2.5 measurement
forecast or model != observation
historical event != current operational condition
exposure model != observed impact
resilience score != safety guarantee
source fetch success != current, complete, or releasable truth
```

## Source role and evidence character

Preserve the domain's seven source-role classes: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic`. Configuration references a governed role; it cannot assign, infer, upgrade, alias away, or silently substitute that role. Aggregate support is not site-level truth; a scenario is not current conditions.

### Required source evidence

Before real-source binding, verify canonical source/product ID, origin versus distributor, authority scope, role, rights/attribution, access/admission state, cadence, time semantics, spatial support, quality flags, and correction/supersession behavior. An aggregator, public URL, successful fetch, or copied source name does not establish authority or redistribution rights.

## Time, freshness, expiry, and correction

### Time kinds

Keep source, observation, valid, retrieval, issue, effective, update, expiry, cancellation, supersession, release, and correction times distinct when material. Retrieval, file modification, or release time cannot refresh the underlying observation or extend a warning.

### Presentation states

Future profiles must distinguish contextual-current, stale, expired, cancelled, superseded, withdrawn, partial, delayed, unavailable, and intentionally historical material. These are presentation requirements, not a newly adopted machine enum. Expired/cancelled material cannot look active; historical use still requires rights and release support. Withdrawal and supersession must remain visible and enforceable.

### Freshness profile rules

Thresholds and clock-skew tolerance come from reviewed source/product governance, not convenience defaults. Preserve official expiry/cancellation and uncertainty. Do not infer freshness from cache age alone, discard supersession links, substitute products silently, or turn unavailable/partial data into an all-clear state.

### Clock and cache safety

Use UTC or an explicit timezone, validate applicable time relationships, and preserve original timestamps. Expiry, cancellation, correction, and withdrawal must stop affected current presentation and invalidate controlled caches and derivatives. See [rollback](#rollback-correction-supersession-and-invalidation) for already-distributed copies.

## Not-for-life-safety and official-source referral

### Required public-surface elements

Every authorized Hazards map, drawer, API representation, Focus answer, report, or export must retain source attribution, source role, material issue/effective/update/expiry state, stale/historical/partial/unavailable labels, uncertainty, a visible not-for-life-safety disclaimer, and appropriate official referral. It must not contain KFM-authored protective-action guidance.

### Referral profile requirements

A reviewed profile identifies jurisdiction/audience, official authority family, a verified public destination, neutral wording, unavailable-link behavior, review owner, version, and rollback. It cannot imply completeness, exclusivity, or that KFM evaluated what emergency action to take. Unverified links block an active referral binding, not drafting a clearly inactive example.

Neutral wording: **KFM provides contextual information only. Consult appropriate official authorities for current warnings and instructions.** No profile may disable this boundary or convert official text into KFM advice.

## Cross-lane ownership and context rules

Hydrology retains water/gauge/flood-system authority; Atmosphere retains weather, air-quality, and smoke-source authority; Geology retains geological support; Roads/Rail retains transport records; Settlements/Infrastructure retains asset and service context. Agriculture, Soil, Habitat, Fauna, Flora, Archaeology, and People/DNA/Land retain their own records, rights, and sensitive-context controls. Hazards consumes governed references rather than duplicating capture or redefining those facts.

### Join-induced sensitivity

A hazard polygon joined to a private residence, responder location, critical facility, protected site, or small vulnerable population can become more sensitive than either input. Carry the strongest applicable restrictions and review the joined output independently. Exposure is a derived relation, not proof of damage, ownership, operational availability, or individual risk.

## Sensitivity, infrastructure, and reconstruction risk

### Fail-closed classes

Protect precise critical infrastructure/dependencies, hazardous-material sites, emergency operations and staging, responder deployment, shelters and protected populations, healthcare capacity, utility/control/communications detail, private people/addresses/parcels/contacts, low-count exposure results, and rare-species or archaeological/cultural locations. Unreleased operational or investigative details do not belong in commit-safe examples.

### Public-safe transforms

Configuration may select an accepted policy profile, not create its thresholds or approve its output. Permitted governed outcomes include omission, suppression, aggregation, generalization, delay, restricted access, derived summary, export denial, or denial of the object. Record transform lineage and reasons without leaking protected facts.

### Reconstruction tests

Test combined zooms, layers, time slices, query filters, repeated exports, temporal differencing, tooltips, source identifiers/URLs, cache keys, imagery/parcels, graph neighbors, screenshots, and AI clues. A rounded coordinate alone is not proof against reconstruction.

## Connector, source-registry, and watcher boundaries

### Connector placement

Source implementation remains source/authority-family-first. The historical `connectors/hazards/` compatibility index is not permission to create a parallel source hierarchy. Before binding, inspect the current accepted connector path, source ID, descriptor, rights, activation, fixtures, consumers, and correction/rollback behavior.

### Source-registry topology

The July revision reported both `data/registry/sources/hazards/` and `data/registry/hazards/sources/`, plus contract/schema and singular/plural manifest variants. **These are retained historical seam warnings, not a fresh inventory or a canonicality decision.** Resolve the actual home from current rules, accepted decisions, and the owning source/alias records before a new binding. Do not write two records, choose a path by filename preference, or accept proposed vocabulary by repetition.

### Watcher rule

Watchers may detect changes and propose governed work; they do not publish, issue alerts, change source roles, extend validity, bypass policy/release, create public layers, or ask AI for emergency instructions. Watcher, source, and configuration activation are separate operations.

## Network, notification, and automation boundary

### Network access

Default configuration validation uses synthetic no-network inputs. Real retrieval requires independent source/connector admission and authorized execution; this lane grants neither. Dependency installation in CI is not evidence that the entire hosted job is network-isolated.

### Notification and messaging

No SMS/email/push/call destinations, siren integration, dispatch, pagers, geofencing, escalation, responder mobilization, or public warning delivery belong in these configs. Non-emergency maintainer/build notifications may be governed elsewhere, but cannot masquerade as hazard warnings.

### Automation safety

Missing authority, stale/invalid official times, failed disclaimer/referral obligations, sensitive joins, unresolved release, ambiguous config identity, or a protective-action request must produce a bounded failure—not an automatic source substitution, permissive retry, or reassuring output. No route, renderer, notification, source, watcher, or release is enabled by file presence.

## Map, UI, export, and governed-AI boundaries

### Map and UI

Public clients use governed APIs and released artifacts, never RAW, WORK, QUARANTINE, candidates, or canonical/internal stores directly. A restricted review preview is not a public release. Rendering, visual urgency, animation, styling, or a layer toggle cannot change source role, warning authority, release state, or sensitivity.

### Evidence Drawer

Retain object/source identity, role, time, freshness, EvidenceRef resolution state, rights, caveats, uncertainty, disclaimer, referral, and correction/supersession lineage. An unresolved EvidenceRef must not appear as a resolved EvidenceBundle, and restricted evidence must not leak through an error or tooltip.

### Export and screenshots

Reports, tiles, PMTiles, screenshots, graph/index projections, cached narratives, and offline bundles are downstream carriers, not truth. Preserve applicable labels, release checks, sensitivity controls, attribution, and correction references. A screenshot cannot bypass a restriction merely because it is an image.

### Governed AI

Scope -> evidence -> EvidenceBundle -> policy, rights, sensitivity, review, and release checks -> cited interpretation or bounded abstention/denial/error. AI cannot author emergency instructions, make safety guarantees, infer observed impact from exposure, or expose protected facts. No model endpoint or internal-store access becomes a normal public path.

## Logging, telemetry, caches, and derived indexes

### Logging rules

Use safe reason codes, identifiers, and hashes rather than restricted payloads, exact locations, emergency contacts, secrets, signed URLs, private-person details, or policy explanations that disclose protected facts. Respect source redistribution limits in logs too.

### Cache identity

Where material, bind source/product and version, object, config/version, policy/version, release, audience, public-safe profile, validity/expiry, and correction/supersession identity. A cached result must not silently survive a change to those obligations.

### Invalidation triggers

Source correction/withdrawal, expiry/cancellation, governed role/rights/sensitivity changes, config/profile changes, release changes, referral changes, evidence-resolution changes, newly discovered protected joins, and rollback require impact assessment and invalidation of controlled affected carriers. Preserve an auditable lineage; do not rewrite history to conceal the error.

## Failure behavior

Keep validation results, work states, and runtime outcomes distinct. `PASS` is not approval; `HOLD` is a work-state restriction; `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` are outward outcomes where the governing runtime contract uses them. This README does not introduce a combined enum.

| Condition | Required boundary |
|---|---|
| Malformed/duplicate/unknown keys, unsupported version, ambiguous alias, failed reload | Reject atomically; no partial application or permissive fallback. |
| Missing owner/consumer/profile for active use | Keep inactive or HOLD; a labeled synthetic draft may still be reviewed. |
| Missing evidence, rights, policy, sensitivity, review, release, or rollback support | Abstain, deny, hold, or error at the responsible gate; never implicit allow. |
| Role collapse, expired-as-current, hidden disclaimer, invalid active referral | Deny affected public use and correct the representation. |
| Emergency advice, notification/dispatch, exact protected detail, arbitrary user profile | Deny the requested KFM behavior; referral remains neutral and governed. |
| Source outage, partial retrieval, stale cache, cross-lane conflict | Preserve the actual failure/uncertainty; stop affected presentation until resolved. |
| Runtime cannot enforce an obligation | Deny or error; documentation is not a compensating implementation. |

## Validation and test matrix

### Documentation validation

Check balanced metadata and fences, one H1, retained section anchors, resolving local navigation, source-backed relative links, accurate truth/maturity labels, safe examples, whitespace, and final newline. Compare the exact remote blob with the validated candidate; confirm that the diff changes only this README. Do not label a custom Markdown check as the repository's native validator.

### Future payload validation

#### Syntax and shape

Require supported encoding/parser/version, required fields, duplicate/unknown-key rejection, restrictive schema/profile resolution, secret/private-endpoint/contact-field rejection, and atomic failure.

#### Semantic checks

Verify consumer binding, role/object/time distinctions, source/product-scoped profiles, disclaimer/referral behavior, rights, sensitivity, cross-lane ownership, deterministic discovery, safe precedence, and no activation by presence. Synthetic profile validation proves no real-source admission.

#### Required negative cases

Cover expired/cancelled-as-current; forecast/detection/declaration/regulatory/aggregate-as-observed; smoke-as-PM2.5; emergency Focus/notification requests; unresolved EvidenceRef; direct internal-store access; missing disclaimer/referral; precise infrastructure and low-count joins; arbitrary user config; duplicate/unknown keys; partial application; network access; stale cache after correction; and missing rollback.

#### Structural behavior

Prove deterministic finite failures, no-network fixture execution, safe logs, no caching of rejected config, atomic reload/disable, and correction/withdrawal invalidation. Tests must assert outcomes, not merely collect successfully or echo a message.

### Current repository reality

The current [domain workflow](../../../.github/workflows/domain-hazards.yml) names these commands:

```bash
# From a matching complete checkout with its declared dependencies installed.
python -m unittest -v tests.domains.hazards.test_hazards_smoke
make hazards-validate
python -m unittest tests.domains.hazards.test_domain_hazards_workflow_binding -v
```

**Verified here: workflow source, not execution.** These commands exercise bounded synthetic Hazards behavior, not a config loader or the complete future-payload matrix. Their exact-head results are **NOT RUN in this authoring environment**. The workflow triggers on pull requests, pushes to `main`, and manual dispatch; a feature-branch push alone does not establish a domain-workflow result.

The proof job retains `WORKFLOW_HOLD: no accepted Hazards proof producer or deterministic proof command`. The release job retains `WORKFLOW_HOLD: no accepted Hazards release dry-run command or candidate manifest contract`. Neither is an executed proof build or release dry run. Hosted CI, policy evaluation, live freshness, browser behavior, and operational rollback remain separate verification.

## Review burden

[CODEOWNERS](../../../.github/CODEOWNERS) routes `/configs/` to `@bartytime4life`; that is not specialist stewardship or independent approval. README changes need configuration/domain review, with public-safety boundary review when wording affects perceived authority. Active bindings additionally need applicable consumer, source/rights, freshness/referral, contract/schema, policy, sensitivity/security, cross-lane, validation, and release/rollback review.

Do not infer approval from a placeholder owner, absent review rule, passing hold job, or an old receipt.

## Maintenance and safe change pattern

Pin current main and target bytes; inspect parent contracts, accepted Directory Rules, relevant seams and overlapping work; define the smallest complete change; author on an isolated branch; validate changed-area behavior and links; attribute failures to exact refs; verify remote content; preserve rollback and review limitations.

**Mutation and retention:** use reviewed, versioned branch changes rather than in-place runtime edits. Preserve superseded config identity and correction history under the owning retention rules; no operational-data retention or deletion policy is created here.

Only this README changes in v0.4. No dependency, executable configuration, source payload, fixture, test, schema, contract, policy, workflow, runtime binding, lifecycle record, or public artifact is created or modified. A later source or release hold does not prohibit this reversible documentation work.

## Migration and anti-bypass posture

A real configuration migration needs old/new path/key/version, one accountable consumer, explicit precedence, compatibility period, deprecation/removal conditions, affected caches/derivatives, repaired backlinks, validation, and rollback. Dual-read, where justified, is not permission for two authoritative writers.

### Forbidden migration shortcuts

Do not silently merge old/new files, duplicate descriptors or schemas, choose unresolved manifest aliases, move policy thresholds into configuration, weaken expiry/disclaimer/referral controls, or introduce temporary notification keys that become public alerting. Preserve semantic identity or version an intentional change through the owning contract.

## ADRs and drift triggers

This revision creates or accepts no ADR. New canonical homes, source-role/object mappings, shared discovery rules, alias migrations, live bindings, or public-output changes require their own applicable governance and evidence. The permanent life-safety and public trust boundaries are not ordinary configuration options or exceptions this README can authorize.

Record confirmed drift at the owning surface: alias-as-authority, divergent source records, hidden referral/disclaimer, expired-as-current, fixture-as-production proof, protected joins, arbitrary profile selection, or missing correction/invalidation. Historical seam reports need fresh verification before being described as current conflicts.

## Definition of done for the first payload

Separate the transition being checked; later release prerequisites must not become a ban on safe drafting.

| Transition | Minimum completion | Must remain unavailable without further authority |
|---|---|---|
| Inactive authoring | Bounded purpose, proposed consumer/profile identity, unmistakably synthetic/non-secret values, clear status, no live binding, documented validation and rollback. | Production consumption, live source access, notifications, sensitive disclosure, promotion, and publication. |
| Consumer binding | Verified owner/consumer, allowlisted path, immutable version/digest, appropriate schema/profile, strict parser, explicit precedence, atomic disable/reload, meaningful positive/negative/no-network tests, reviewed obligations. | Unadmitted sources, unreviewed policy changes, unapproved audiences or output surfaces. |
| Real-source or public integration | Applicable source identity/admission, rights, role, freshness/expiry, EvidenceRef -> EvidenceBundle closure, sensitivity/transform lineage, policy, review, validation receipts/proofs, release identity, correction/withdrawal, and rollback. | Alert authority, protective-action guidance, direct public internal-store access, or permission inferred from config presence. |

No checklist item is marked complete merely because this document exists. A new payload must update this inventory and state exactly which stage and acceptance tests it satisfies.

## Rollback, correction, supersession, and invalidation

### README rollback

Before integration, preserve or abandon the task branch under the contribution workflow; there is no runtime configuration to deactivate in this change. After separately authorized integration, restore the prior README through a reviewed revert/forward correction. Do not rewrite shared history or automatically revert unrelated work.

### Future payload rollback

Disable affected selection through the verified consumer; stop dependent refresh/watch/cache paths where authorized; preserve faulty identity and evidence; assess misleading freshness/role/referral and sensitive disclosure; restore a verified prior or disabled state; invalidate controlled derivatives; rerun negative/no-network checks; and record correction, withdrawal, review, and rollback in their owning homes.

A Git revert does not stop a running consumer, revoke admission, invalidate caches, or withdraw distributed artifacts. Already-downloaded screenshots, exports, and offline copies may not be remotely erasable: stop serving affected controlled versions, publish the authorized correction/withdrawal references, and document residual distribution rather than promise complete erasure.

## Safe language rules

### Preferred language

Use “contextual,” “historical,” “official-source warning context,” “modeled,” “candidate,” “regulatory,” “administrative,” “stale,” “expired,” “partial,” “unavailable,” “evidence unresolved,” and “consult official sources” when they accurately describe the source and governed state.

### Prohibited or high-risk language

Do not author “safe,” “all clear,” “no risk,” “evacuate,” “shelter now,” “return home,” “road is safe,” “official KFM warning,” or comparable protective-action assurances. “Confirmed,” “current,” “complete,” and “real-time” require evidence for the exact claim and cannot erase the contextual-only boundary. Any permitted source quotation must stay attributed and must not become KFM-authored instruction.

## Last reviewed

**2026-09-04**, against `main@700570cbcf191038aa20a030174c2dd08cf93675`. This is a documentation/currentness review, not specialist approval, operational certification, or proof of runtime enforcement.

Re-review before the first non-README payload, consumer binding, profile/source-role change, official-referral update, alias migration, source/watch activation, notification-adjacent behavior, exposure change, or public integration. Re-pin main, target bytes, controlling decisions, and relevant checks each time.

[Back to top](#top)
