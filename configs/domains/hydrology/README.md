<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-hydrology-readme
title: configs/domains/hydrology/ — Governed Hydrology Configuration Boundary
type: readme
version: v0.4
status: draft
owners: "NEEDS VERIFICATION — accountable Config, Hydrology, measurement/identity, public-safety, source/rights, consumer, validation, policy, release, and documentation stewards"
created: 2026-07-13
updated: 2026-09-04
policy_label: "public; config-sublane; hydrology; non-secret; non-authoritative; consumer-bound; source-role-aware; measurement-aware; freshness-aware; private-property-aware; not-for-life-safety; no-live-binding; no-source-activation; no-release-authority"
current_path: configs/domains/hydrology/README.md
owning_root: configs/
readme_profile: BOUNDARY_COMPACT
scope_id: hydrology
review_route: "@bartytime4life via /configs/ CODEOWNERS; routing is not accepted stewardship or independent approval"
truth_posture: "CONFIRMED tracked README-only configuration lane, adopted placement law, thirteen-entry machine domain projection, and executable bounded Hydrology fixture/schema/semantic validation wiring in the inspected workflow source / PROPOSED future named-consumer configuration and accepted profile selectors / UNKNOWN config loading, precedence, production behavior, live-source admission, runtime policy enforcement, evidence closure, release, deployment, and publication / NEEDS VERIFICATION exact-head workflow execution, accountable stewardship, consumer dependencies, source rights, public-safe geometry transforms, and official-source redirect profiles"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 9e152476cda7bd9b80a2afac8031619a1898eceb
  prior_blob: ae9976c523e0623e681bd7d9c8c20109f8e9fd57
  parent_readme_blob: c497e41466f3aaf934aeca4b9976a2fa8516ff21
  hydrology_workflow_blob: 960da1c8da3d0f4d93327465b64a56f4a1b9806a
  hydrology_domain_readme_blob: 72d7d2608dfa7b40e4515aacb213bed0b46cbfee
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
related:
  - ../README.md
  - ../../README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../contracts/domains/hydrology/README.md
  - ../../../schemas/contracts/v1/domains/hydrology/README.md
  - ../../../policy/domains/hydrology/README.md
  - ../../../tests/domains/hydrology/README.md
  - ../../../fixtures/domains/hydrology/README.md
  - ../../../data/registry/sources/hydrology/README.md
  - ../../../control_plane/domain_lane_register.yaml
  - ../../../release/candidates/hydrology/README.md
  - ../../../.github/workflows/domain-hydrology.yml
tags: [kfm, configs, hydrology, watershed, huc, flow, water-level, aquifer, nhdplus, nfhl, freshness, source-role, measurement, identity, sensitivity, governance]
notes:
  - "Same-path documentation revision. No executable configuration payload, consumer, contract, schema, policy, registry, test, fixture, workflow, source, release, or public artifact changes."
  - "Corrects v0.3 currentness drift: the machine domain register is no longer empty and the Hydrology workflow is no longer TODO-only; bounded executable validation surfaces now exist."
  - "Preserves the non-alert, NFHL anti-collapse, measurement, datum, identity, freshness, sensitivity, correction, and rollback boundaries while reducing repeated prose."
  - "Workflow source proves wiring, not a passing exact-head run, live-source correctness, production readiness, or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Hydrology Configuration Boundary

`configs/domains/hydrology/`

> Make Hydrology configuration inspectable without turning it into hydrologic truth, source admission, identity resolution, warning authority, policy, evidence, or release state.

**Status:** draft v0.4 · **Owning root:** `configs/` · **Local maturity:** README-only · **Consumer binding:** not established

**Navigate:** [Purpose](#purpose) · [Authority](#authority-and-supersession) · [Current evidence](#current-status) · [Scope](#scope) · [Repository fit](#repository-fit) · [File contract](#minimum-file-contract) · [Consumer binding](#consumer-binding-and-precedence) · [Source roles](#source-role-and-semantic-guardrails) · [Measurements](#measurement-spatial-and-identity-integrity) · [Time](#temporal-freshness-and-stale-state) · [NFHL](#nfhl-flood-context-and-life-safety) · [Cross-lane](#cross-lane-and-sensitivity-boundaries) · [Validation](#validation-and-finite-failures) · [AI/public](#governed-ai-and-public-surfaces) · [Change](#review-change-and-migration-discipline) · [First payload](#definition-of-done-for-the-first-payload) · [Rollback](#rollback-and-correction) · [Language](#safe-language)

> [!IMPORTANT]
> **Two different maturity statements:** this configuration directory contains only this README at the pinned repository snapshot. The wider Hydrology lane has executable bounded fixture/schema/semantic validation wired in `.github/workflows/domain-hydrology.yml`. Neither statement establishes a configuration loader, consumer binding, live source, production policy evaluation, release, deployment, or publication.

> [!CAUTION]
> **KFM Hydrology is not an emergency flood-warning system.** NFHL is regulatory flood context, not observed inundation. A gauge reading is not a forecast; a modeled hydrograph is not an observation; a HUC aggregate is not site truth; a source outage is not an all-clear.

## Purpose

This lane inherits the [domain configuration contract](../README.md) and the [commit-safe configuration root](../../README.md). It exists for small, public-safe, non-secret defaults, templates, examples, and profile references consumed by a **named and verified Hydrology component**.

A useful configuration answers **how an already-governed consumer is configured**. It does not decide whether a water observation, watershed identity, regulatory flood context, model result, warning, source, or public claim is true or admissible.

## Authority and supersession

**Configuration-supporting; non-authoritative for meaning, source admission, policy, evidence, review, or release.**

| Responsibility | Owning boundary; what config may do |
|---|---|
| Placement | Accepted [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the [Directory Rules](../../../docs/doctrine/directory-rules.md). This same-path revision remains under `configs/`. |
| Hydrology meaning | [`docs/domains/hydrology/`](../../../docs/domains/hydrology/README.md) and `contracts/` own domain language and semantic meaning. Config may reference versioned decisions; it must not redefine them. |
| Machine shape | [`schemas/contracts/v1/domains/hydrology/`](../../../schemas/contracts/v1/domains/hydrology/README.md) owns machine-checkable shape. Config may bind to a verified schema; it must not embed a competing one. |
| Source admission | Source governance and [`data/registry/sources/hydrology/`](../../../data/registry/sources/hydrology/README.md) own source identity, role, rights, cadence, and activation. Config cannot admit or activate a source. |
| Policy and sensitivity | [`policy/domains/hydrology/`](../../../policy/domains/hydrology/README.md) and applicable cross-cutting policy own decisions. Config may select an accepted profile; it cannot weaken or replace it. |
| Evidence and proof | `EvidenceRef`, `EvidenceBundle`, receipts, proofs, and review records remain outside this lane. A successful parse is not evidence closure. |
| Release/publication | Governed release and publication surfaces remain separate. A config toggle, workflow pass, map display, or merge cannot authorize publication. |

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

Promotion is a governed transition, not a file move or configuration choice. Public clients use governed APIs and released public-safe artifacts, never RAW, WORK, QUARANTINE, unreleased stores, or direct model endpoints.

This `v0.4` revision supersedes `v0.3` at the same document ID and path. Git history retains the prior wording; no parallel Hydrology configuration authority is created.

## Current status

All current-repository statements below are bounded to `main@9e152476cda7bd9b80a2afac8031619a1898eceb`, inspected on **2026-09-04**.

```text
configs/domains/hydrology/
└── README.md    # boundary documentation; no executable config payload
```

| Evidence | Bounded finding | Does not establish |
|---|---|---|
| This directory | Exact tracked listing contains one README blob. | Ignored/untracked/external config, parser, loader, precedence, or consumer binding. |
| Parent config README | `configs/domains/README.md` v0.6 records thirteen canonical child lanes and non-authority rules. | Current behavior of any consumer. |
| Machine domain projection | `control_plane/domain_lane_register.yaml` is a thirteen-entry machine projection. | Accepted stewardship, source activation, policy, evidence closure, or release. |
| Directory governance | ADR-0029 is accepted and adopts Directory Rules. | Acceptance of every older path proposal or compatibility alias. |
| Hydrology doctrine | `docs/domains/hydrology/README.md` exists and preserves source-role, time, evidence, NFHL, and non-alert boundaries. | Production implementation merely because doctrine exists. |
| Hydrology workflow source | `domain-hydrology.yml` wires executable bounded checks for EvidenceBundle alias/shape, AquiferObservation/AquiferContextLink separation, frozen FlowObservation and datum-bound WaterLevelObservation profiles, NHDPlus waterbody crosswalk behavior, accepted Hydrology tests, startup no-egress protection, and additional semantic validators. | A passing exact-head run, real-source correctness, end-to-end proof, policy execution, release, or publication. |
| Source/pipeline posture in workflow | The workflow explicitly checks placeholder source descriptors and inactive no-network pipeline declarations. | Live source admission or ingestion. |
| Release candidate lane | `release/candidates/hydrology/README.md` is required by the workflow source. | A release candidate having passed promotion or publication gates. |

**Correction to v0.3:** the previous README described the machine lane register as empty and documentation workflows as TODO scaffolds. Those claims are stale. The inspected current workflow contains executable bounded validation and the machine domain projection contains thirteen entries. This update corrects the underclaim without upgrading the wider Hydrology lane to production-ready.

No live hydrologic source, public route, deployment, warning service, policy runtime, release operation, or publication surface was exercised for this README update.

## Scope

### What belongs here

| Material | Conditions |
|---|---|
| `README.md` | Explain responsibility, evidence, limits, review, correction, and rollback. |
| Future `*.template.*` | Placeholder-based, versioned, non-secret, inert until a named consumer and loader are verified. |
| Future `*.example.*` | Tiny synthetic examples with impossible/non-sensitive values; no real gauges, wells, owners, warnings, coordinates, or endpoints. |
| Profile references | Select already-governed role, freshness, measurement, identity, public-safe geometry, review, stale-state, or presentation behavior. |
| Presentation defaults | Units/labels/badges/caveat visibility/accessibility only where they cannot change meaning, evidence, sensitivity, or release state. |
| Migration notes | Describe a real consumer/key/version transition and rollback without becoming a second authority. |

A reversible inert draft may carry `PROPOSED` or `NEEDS VERIFICATION` dependencies. It must not be described as active, consumer-ready, source-admitted, or public-ready.

### What does not belong here

No real gauge, flow, water-level, water-quality, groundwater, well, hydrograph, flood-event, NFHL, owner, water-right, source, lifecycle, or release payload. No credentials, private endpoints, signed URLs, workstation paths, deployment bindings, emergency instructions, all-clear logic, exact private-well or resilience-critical infrastructure detail.

Contracts, schemas, normative policy, source registries, EvidenceBundles, receipts, proofs, review decisions, release manifests, correction notices, connectors, watchers, pipelines, apps, runtime code, tiles, reports, caches, and published artifacts remain in their owning roots.

A setting must never relabel NFHL as observed flooding, a model as an observation, an aggregate as site truth, a candidate crosswalk as resolved identity, missing data as zero, or unavailable data as safe conditions.

## Repository fit

The responsibility root is `configs/`; the domain segment is `hydrology`. This path is already established, so the smallest sound change is an in-place README revision.

| Responsibility | Home | Relationship to this lane |
|---|---|---|
| Safe repository configuration | `configs/` | Parent authority for commit-safe defaults/templates. |
| Domain-scoped configuration | `configs/domains/` | Immediate parent contract. |
| Hydrology doctrine | `docs/domains/hydrology/` | Human-readable domain scope and law. |
| Semantic contracts | `contracts/domains/hydrology/` | Meaning and object semantics. |
| Machine schemas | `schemas/contracts/v1/domains/hydrology/` | Machine shape and validation targets. |
| Policy | `policy/domains/hydrology/` | Admissibility/sensitivity/warning rules. |
| Source registry | `data/registry/sources/hydrology/` | Source metadata and activation posture. |
| Tests/fixtures | `tests/domains/hydrology/`, `fixtures/domains/hydrology/` | Bounded executable evidence and synthetic inputs. |
| Validators | `tools/validators/domains/hydrology/` and related compatibility lanes | Validation implementation; compatibility ownership must remain explicit. |
| Release | `release/candidates/hydrology/` and governed release surfaces | Release-state work; config cannot promote. |

Do not create flat aliases, parallel schemas, duplicate source registries, compatibility paths, or alternate release homes from this lane. A path conflict is resolved through the owning governance/migration process, not consumer precedence.

## Inputs and outputs

A future config may consume a named consumer ID; format/version; verified contract/schema/policy/source-profile references; accepted role/freshness/measurement/identity/public-safe-geometry/review/stale-state profile IDs; safe presentation defaults; and migration/rollback metadata.

**Current output: documentation only.** A future validated payload may produce deterministic settings for one verified consumer. It must not emit or trigger a source request, observation, warning, model run, identity decision, sensitivity transform, EvidenceBundle, lifecycle write, release record, API response, layer, tile, cache, or publication.

## Minimum file contract

Before the first non-README payload is consumer-ready, document or encode:

| Contract item | Required information |
|---|---|
| Identity | Status, owner, named consumer, config version, exact path and format. |
| Binding | Parser/loader entrypoint, load timing, selection mechanism, reload behavior, and tests. |
| Authority refs | Exact contract, schema, policy, source/profile, doctrine, and release-boundary references. |
| Source roles | Canonical role vocabulary and fail-closed behavior for missing/conflicting role. |
| Measurements | Parameter, source/display units, datum, qualifier, provisional state, precision, uncertainty, and no-data behavior. |
| Identity | HUC level/vintage, reach/site namespace, crosswalk method/version, confidence, ambiguity outcome, and supersession. |
| Spatial | CRS, axis order, geometry type, scale/resolution, accuracy, simplification/generalization, and public-safe profile. |
| Time/freshness | Observed/valid/issue/expiry/retrieval/release/correction semantics plus stale/partial/outage behavior. |
| Sensitivity | Wells, owners, rights, dams, utilities, facilities, joins, low counts, differencing, reconstruction, and export/cache implications. |
| Warning boundary | Explicit non-alert posture and verified official-source redirect profile where operational context is displayed. |
| Parser failures | Missing file, unknown/duplicate keys, unsupported version, malformed values, and consequential fallback behavior. |
| Precedence | Complete deterministic order among built-in, repository, environment, local, CLI, and deployment sources. |
| Network | No network/source activation by file presence; validation remains no-network unless separately authorized. |
| Validation | Positive and negative parsing, shape, semantic, sensitivity, no-egress, deactivation, migration, and rollback checks. |

Safe placeholders include `<HYDROLOGY_CONSUMER_ID>`, `<VERIFIED_SCHEMA_REF>`, `<VERIFIED_POLICY_PROFILE>`, `<ACCEPTED_FRESHNESS_PROFILE>`, `<ACCEPTED_MEASUREMENT_PROFILE>`, `<ACCEPTED_IDENTITY_PROFILE>`, and `<PUBLIC_SAFE_GEOMETRY_PROFILE>`.

## Consumer binding and precedence

A file is not active because it exists. Verified binding must establish the owning component, exact supported path/version, parser/loader, load timing, mandatory/optional behavior, precedence, unknown/duplicate-key handling, failure behavior, deactivation, migration, rollback, and tests proving that directory presence causes no source activation, network call, model run, warning, lifecycle write, or public output.

Until then:

- auto-discovery and recursive loading are off;
- missing/invalid consequential values hold or reject the feature rather than weaken safeguards;
- missing config leaves the proposed feature disabled; and
- environment/CLI/deployment overrides do not silently outrank repository config.

## Source-role and semantic guardrails

Preserve roles as data, not styling. If current source-registry vocabulary and older Hydrology prose disagree, reconcile through the governing source-role authority rather than inventing a local alias.

| Material | Must not become |
|---|---|
| Gauge/flow/water-level observation | Forecast, warning, regulatory zone, or model result. |
| NFHL zone | Observed inundation, current flooding, forecast, warning, or parcel-level legal/insurance determination. |
| Modeled/reconstructed hydrograph | Observed series. |
| HUC/watershed aggregate | Per-site or per-property truth. |
| Administrative well/water-right record | Observed use, ownership proof, or event timeline without its actual authority. |
| Candidate NHDPlus/reach crosswalk | Resolved identity when ambiguity remains. |
| Terrain-derived drainage/inundation | Official hydrography, observed flooding, or regulatory designation. |
| Historical flood evidence | Current operational warning. |
| Synthetic fixture | Real site, event, source, observation, or authority. |

A role mismatch is a trust-boundary failure, not a display preference.

## Measurement, spatial, and identity integrity

A consumer must preserve source-native parameter, value, unit, datum, qualifier, provisional/approved state, estimated/censored state, method, precision, uncertainty, support interval, and no-data semantics.

Do not infer unit compatibility from names, perform undocumented conversions, discard qualifiers/provisional state, turn no-data into zero, mix stage/discharge/elevation/depth/concentration/withdrawal, hide datum differences, or render precision beyond source support.

Preserve CRS, axis order, geometry type, source scale/resolution, horizontal/vertical accuracy, HUC digit level, source vintage, topology expectations, clipping, generalization, and public-safe class. Client-side hiding, zoom limits, styling, clustering, or popup omission is not a sensitivity transform.

For identity, preserve source ID/vintage, feature/site namespace, crosswalk method/version, candidate set, confidence/reason, temporal validity, topology/geometry checks, and supersession. Ambiguous mappings return `ABSTAIN` or hold for review unless a separately governed and tested rule resolves them.

## Temporal, freshness, and stale state

Do not collapse these times: source, observed, valid, issue, expiry, retrieval, processing, release, correction, and supersession.

Source-specific freshness behavior should make fresh/delayed/stale/expired/partial/unavailable/corrected/superseded states inspectable. Missing or unavailable data is not zero flow, no flooding, or safety. Cached values retain original observation and retrieval time. Corrections preserve lineage. Warning/forecast validity is never extended by configuration.

## NFHL, flood context, and life safety

NFHL remains **regulatory context**. Preserve source/map vintage, zone/designation, effective/publication date, citation, geometry/scale limits, caveats, evidence, and release state.

Regulatory, observed, modeled, historical, and operational-context material may appear together only if each constituent remains separately role-typed, time-scoped, cited, and sensitivity-filtered. Do not flatten them into one flood-truth flag.

Hydrology configuration must never issue, modify, suppress, extend, cancel, or replace an official warning; generate evacuation/shelter/rescue/travel/medical/protective-action instructions; emit an all-clear; trigger dispatch or escalation; or infer safety from missing data.

Where an authorized surface displays operational warning context, it should identify the official authority, preserve issue/expiry state, show current/stale/expired/historical posture, and fail closed when authority/freshness/link state is unresolved. Exact disclaimer and redirect profiles remain policy/product decisions.

## Cross-lane and sensitivity boundaries

Hydrology may join neighboring lanes only while preserving ownership, role, time, evidence, rights, precision, review, and release state.

- **Hazards:** Hydrology contributes water observations/context; Hazards owns warning/event/exposure claims.
- **Soil/Agriculture:** Hydrology contributes water/runoff/irrigation context; those lanes own soil/crop/production claims.
- **Geology:** geology owns geologic/hydrostratigraphic units; Hydrology owns water observations and relationships.
- **Infrastructure/Transport:** hydrologic context may relate to dams, intakes, bridges, crossings, closures, and networks, but operational status and sensitive precision remain with the owning lane.
- **Habitat/Fauna/Flora:** wetland/riparian/aquatic context does not transfer biological taxonomy, occurrence, or geoprivacy authority.
- **People/DNA/Land:** private wells, water rights, owners, and parcels require the owning privacy/title/rights controls.

Assess sensitivity on the **resulting join**, not only the inputs. Repeated queries, alternate IDs, tiles, caches, exports, low counts, temporal deltas, and metadata can reconstruct information hidden from a single field.

## Validation and finite failures

### Confirmed by this update

- Current main and the target tracked directory were read directly.
- The lane is README-only at the pinned tracked snapshot.
- The parent domain-config README is v0.6 and records thirteen child lanes.
- ADR-0029 and the adopted Directory Rules were re-read as placement authority.
- Current Hydrology workflow source was inspected and contains executable bounded checks rather than the v0.3 TODO-only description.
- Open-PR search returned no existing PR for this exact Hydrology config README before branch creation.

### Not proved by this update

No exact-head workflow execution, full test suite, live-source probe, policy-runtime check, deployment, release, publication, warning behavior, or production consumer was run or inferred.

### Required before a future payload

At minimum: parser/version checks; required/unknown/duplicate-key polarity; consumer binding; source-role/NFHL anti-collapse; ambiguous-identity rejection; measurement/unit/datum/no-data checks; time/freshness/outage/correction behavior; rights/sensitivity/join-risk checks; no-egress validation; finite errors; deactivation; migration; and rollback.

Representative negative cases include NFHL-as-observed, model-as-observation, aggregate-as-site-truth, ambiguous reach auto-selection, datum mismatch, qualifier loss, no-data-to-zero, stale-as-current, outage-as-safe, KFM-generated warning/all-clear, unresolved rights accepted, exact private/sensitive geometry exposed, unknown consequential key ignored, network access during validation, or direct write to published/release state.

## Governed AI and public surfaces

AI is interpretive and never root truth. A Hydrology answer, Evidence Drawer panel, map popup, graph edge, summary, export, tile, or Focus Mode result must remain downstream of governed evidence and release state.

Configuration may select presentation behavior for an already-governed consumer. It must not make a model authoritative, bypass citation/policy review, expose internal stores, or turn rendered geometry into evidence. Where support is inadequate, use the finite outward posture appropriate to the owning contract: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.

## Review, change, and migration discipline

For any change beyond documentation:

1. identify the named consumer and accountable owners;
2. re-pin current `main`, target bytes, Directory Rules, current ADRs, and overlapping PRs;
3. verify contract/schema/policy/source-profile dependencies;
4. add the smallest inert payload plus positive/negative tests;
5. keep source activation, production egress, release, deployment, and publication as separate governed transitions;
6. record compatibility, deactivation, migration, correction, and rollback; and
7. preserve historical evidence instead of rewriting it to make the new state look older or more certain.

## Definition of done for the first payload

The first non-README payload is not done because it parses. It is done only when it has a named consumer and owners; deterministic version/precedence; verified authority references; fail-closed source-role, measurement, identity, time, freshness, sensitivity, and warning behavior; positive and negative no-network tests; documented deactivation/migration/rollback; no secrets or real sensitive records; and no implication of source admission, release, deployment, or publication.

## Rollback and correction

Before integration, closing the draft or abandoning the feature branch restores repository state. After an authorized merge, use a reviewed forward correction or normal Git revert according to repository policy; do not force-push shared history.

If a future config leaks secrets or sensitive hydrologic/private-property detail, Git reversion alone is insufficient: invoke the applicable incident/credential/data-correction process and inspect derived caches, artifacts, logs, and public products. A correction must preserve lineage rather than silently rewriting prior public state.

## Safe language

Prefer:

- “configuration-supporting, not authoritative”;
- “bounded workflow wiring confirmed; exact-head result not yet verified”;
- “regulatory context, not observed inundation”;
- “candidate identity remains ambiguous; abstain/hold”;
- “stale/unavailable source state is visible and not interpreted as safe”;
- “consumer binding / live-source admission / release remains unverified.”

Avoid “active,” “authoritative,” “production-ready,” “official flood map,” “safe,” “no flood,” “verified owner,” “resolved reach,” “live,” “released,” or “published” unless the owning evidence actually establishes that state.

## Last reviewed

**2026-09-04** — repository-grounded v0.4 currentness pass against `main@9e152476cda7bd9b80a2afac8031619a1898eceb`.

[Back to top](#top)
