<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-soil-readme
title: configs/domains/soil/ — Governed Soil Configuration Boundary
type: readme
version: v0.3
status: draft
owners:
  - "@bartytime4life — CODEOWNERS review route only"
  - "NEEDS VERIFICATION — config, Soil, source, survey-lineage, moisture, rights/privacy, validation, policy, release, and independent review assignments"
created: 2026-07-13
updated: 2026-09-04
owning_root: configs/
responsibility: Shared non-secret Soil configuration guidance; reference authority without duplicating it
current_path: configs/domains/soil/README.md
policy_label: "public; config-sublane; soil; support-type-aware; source-role-aware; source-vintage-aware; depth-unit-method-aware; private-land-aware; non-secret; non-authoritative; no-live-binding; no-agronomic-advice; no-engineering-advice; no-conservation-compliance-authority; no-hazard-authority; no-release-authority"
truth_posture: >
  CONFIRMED current README-only config directory, accepted Directory Rules adoption,
  parent configuration boundary, canonical subtype-first Soil source-registry writer,
  retained domain-first compatibility view, Soil architecture/source-registry documentation,
  and no executable config payload in this directory / PROPOSED future consumer-bound
  templates and accepted profile references / UNKNOWN loader, precedence, runtime use,
  deployment binding, source activation, and publication / NEEDS VERIFICATION accepted
  owners, executable config validation, exact consumer binding, current schema/contract
  authority closure, source-role vocabulary closure, support-type enforcement, rights,
  freshness, interpretation fitness, correction propagation, and rollback integration.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 9e152476cda7bd9b80a2afac8031619a1898eceb
  target_blob: ae2e04c9629a8913c78b8ac4e789d0ac10c0e5af
  inventory_scope: Exact GitHub contents listing for configs/domains/soil; README.md only
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
related:
  - ../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/soil/README.md
  - ../../../docs/domains/soil/ARCHITECTURE.md
  - ../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../data/registry/sources/soil/README.md
  - ../../../data/registry/soil/README.md
  - ../../../data/registry/soil/sources/README.md
  - ../../../contracts/domains/soil/
  - ../../../schemas/contracts/v1/domains/soil/
  - ../../../schemas/contracts/v1/soil/
  - ../../../policy/domains/soil/
  - ../../../.github/CODEOWNERS
tags: [kfm, configs, soil, ssurgo, sda, gssurgo, gnatsgo, mesonet, scan, uscrn, smap, support-type, source-role, lineage, units, depth, time, sensitivity, no-secrets, governance]
notes:
  - "Same-path README revision only; no config payload, source descriptor, source activation record, contract, schema, policy, pipeline, workflow, release object, or public artifact changes."
  - "v0.3 corrects the stale claim that Soil source-registry topology is unresolved: accepted Directory Rules make data/registry/sources/ the canonical writer, while domain-first Soil registry surfaces remain compatibility views pending migration closure."
  - "Segmented-versus-flat Soil contract/schema paths remain unresolved because the relevant schema-home decision remains separate from this config README."
  - "Configuration may reference accepted profiles but cannot create Soil truth, source authority, field verification, advice, policy, evidence, release, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Soil Domain Configuration

`configs/domains/soil/` is the shared, non-secret configuration boundary for Soil consumers. It may eventually hold small defaults, templates, examples, and references to accepted profiles, but it does not own Soil truth, source admission, schema, policy, evidence, review, release, or publication.

**Status:** draft `v0.3` · **Inventory:** README-only at the pinned main commit · **Owning root:** `configs/` · **Runtime binding:** not established.

> [!IMPORTANT]
> Presence in this directory is inert. A file is not active until a named consumer, parser, binding path, validation behavior, precedence rule, and safe failure posture are verified.

> [!CAUTION]
> Soil support types must not collapse. Static survey, gridded derivative, station/depth observation, satellite grid, pedon/profile evidence, interpretation, and released public-safe derivative are materially different supports. Configuration cannot turn one into another or elevate a derivative into source authority.

## Purpose

Use this lane for consumer-facing configuration choices that are genuinely shared within the Soil domain and safe to commit. Configuration follows its consumer unless the setting is genuinely shared; app-only settings stay with the app, pipeline specifications stay in `pipeline_specs/`, source admission stays in the source registry, policy stays in `policy/`, and secrets stay outside Git.

A useful Soil config identifies the consumer, configurable behavior, authority references, validation, failure handling, and rollback. Directory completeness alone is not a reason to add a payload.

## Authority level

**Implementation-supporting and non-authoritative.** Placement follows the accepted Directory Rules v2 decision recorded by ADR-0029. The accepted rule set makes a path an authority claim and assigns each artifact to the responsibility that owns it; this README therefore references Soil authority surfaces rather than duplicating them.

| Concern | This lane may | This lane must not |
|---|---|---|
| Source selection | Reference an admitted source/profile by stable ID | Admit, activate, suspend, or supersede a source |
| Source role | Reference accepted role vocabulary | Upcast observation/model/context into authority |
| Support type | Reference accepted support profiles | Merge survey, grid, station, satellite, pedon, or interpretation support |
| Survey lineage | Require MUKEY/COKEY/CHKEY and source-vintage fields | Invent joins or rewrite source identity |
| Units/depth/QC | Select accepted normalization profiles | Assume units, depth, method, or quality state |
| Time/freshness | Select accepted stale-state behavior | Treat retrieval time as observation time or stale data as current |
| Spatial support | Select accepted scale/generalization profiles | Treat point, grid, polygon, or profile supports as interchangeable |
| Interpretation | Reference accepted suitability/erosion methodology | Issue agronomic, engineering, compliance, lending, legal, or hazard advice |
| Sensitive context | Select accepted redaction/generalization profile | Expose private land, producer, owner, or private-sensor context |
| Public behavior | Configure a released consumer | Authorize release or bypass governed APIs/artifacts |

## Current repository status

At `main@9e152476cda7bd9b80a2afac8031619a1898eceb`, the exact GitHub contents listing for this directory contains only `README.md`. No executable Soil configuration payload is therefore established by this lane.

The strongest relevant current repository findings are:

- `configs/domains/README.md` defines child domain config lanes as non-secret, non-authoritative, and inactive unless consumer binding is verified;
- ADR-0029 is accepted and adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md`;
- `data/registry/sources/soil/README.md` records `data/registry/sources/soil/` as the canonical subtype-first Soil source-registry writer under the accepted Directory Rules;
- domain-first Soil registry paths remain compatibility surfaces and must not become independent writers;
- Soil architecture and canonical-path docs preserve source-role and support-type separation, lineage, time, rights, sensitivity, public-safe, correction, and rollback concerns;
- contract/schema path convergence is still separate and must not be resolved locally by this config lane.

This README does not prove working Soil ingestion, a config loader, a live source, passing CI, source rights, policy enforcement, release readiness, or public operation.

## What belongs here

Small, reviewable, non-secret files for a **named and verified consumer** may belong here, including:

- `*.template.yaml` or `*.template.yml` with placeholders only;
- synthetic `*.example.yaml`, `*.example.json`, or `*.example.toml` files;
- deterministic development or test defaults;
- review defaults that prefer hold, deny, quarantine, caveat, or abstention;
- references to accepted source, support-type, units, depth, QC, freshness, interpretation, sensitivity, or public-safe profiles;
- bounded compatibility mappings for a verified key migration with an exit plan.

Do not place source payloads, credentials, private endpoints, SourceDescriptors, activation decisions, JSON Schemas, semantic contracts, policy rules, EvidenceBundles, receipts, proofs, catalog records, PMTiles/COGs/GeoParquet, release manifests, or publication state here.

## Soil support model

A configuration consumer must preserve the support carried by the data. At minimum, do not conflate:

| Support class | Typical examples | Critical boundary |
|---|---|---|
| Static survey | SSURGO / SDA map-unit and tabular survey material | Survey vintage is not current field observation |
| Gridded derivative | gSSURGO, gNATSGO, other modeled/gridded soil products | Grid is not source-survey authority |
| Station/depth observation | Kansas Mesonet, SCAN, USCRN-style observations | Point/depth does not imply area truth |
| Satellite grid | SMAP-style soil-moisture products | Remote-sensing support is not in-situ support |
| Pedon/profile evidence | Site/profile measurements and descriptions | Specific profile is not map-unit-wide truth |
| Interpretation | Hydrologic group, erosion, suitability, fitness-for-use products | Interpretation is not measurement or advice |
| Public-safe derivative | Released generalized/aggregated/redacted product | Derivative is not canonical internal evidence |

Cross-support aggregation requires an explicit derivation method, compatible units/time/scale, retained lineage, uncertainty/limitations, validation, policy/review, and release closure before public use.

## Minimum configuration contract

A non-trivial payload should identify or reference at least:

```yaml
domain_slug: soil
config_class: <template|example|dev-default|test-default|review-default|profile-reference|compatibility>
intended_consumer: <verified path or NEEDS_VERIFICATION>
consumer_version: <version or NEEDS_VERIFICATION>
format: <yaml|json|toml|other>
binding: <explicit file-selection mechanism>
precedence: <explicit order or UNRESOLVED>
missing_file_behavior: <inactive|hold|error>
unknown_key_behavior: <fail|hold|explicit-safe-policy>
source_profile_refs: []
source_role_vocabulary: <accepted ref or NEEDS_VERIFICATION>
support_type_refs: []
lineage_profile: <accepted ref or NEEDS_VERIFICATION>
units_profile: <accepted ref or NEEDS_VERIFICATION>
depth_profile: <accepted ref or NEEDS_VERIFICATION>
quality_profile: <accepted ref or NEEDS_VERIFICATION>
temporal_profile: <accepted ref or NEEDS_VERIFICATION>
spatial_support_profile: <accepted ref or NEEDS_VERIFICATION>
sensitivity_profile: <accepted ref or NEEDS_VERIFICATION>
validation_ref: <executable validator or NEEDS_VERIFICATION>
network_behavior: none
side_effects: none
rollback: <prior file/profile/version and deactivation procedure>
```

This example is documentation, not a schema and not an accepted universal field contract.

## Consumer binding, precedence, and failure

Binding must be explicit. Do not recursively auto-load files because they appear under `configs/domains/soil/`, and do not infer precedence from filename or directory order.

A verified consumer should record the exact path/version/digest it reads, parser/version, merge or replace semantics, environment handling, unknown-key behavior, and missing/invalid-file behavior. Missing, stale, ambiguous, or invalid config should produce an explicit inactive, hold, abstain, deny, or error state rather than silently choosing a newer source, assuming a unit/depth, accepting missing QC, revealing private context, or falling back to production.

## Validation

For the first executable payload, require proportionate changed-area validation rather than claiming broad Soil readiness. At minimum verify:

1. syntax parses with the named parser/version;
2. unknown keys fail or resolve to an explicit safe state;
3. the exact named consumer reads the exact config path/version;
4. referenced source/profile IDs resolve without creating source activation;
5. source role and support type remain distinct;
6. MUKEY/COKEY/CHKEY and source-vintage lineage are preserved where applicable;
7. units, depth, method, QC, time, freshness, scale, and uncertainty are explicit where material;
8. no secret, private endpoint, private land, producer, owner, or private-sensor value is present;
9. parse/validation has no network or lifecycle side effect where practical;
10. rollback/deactivation works and does not imply release rollback automatically.

Finite review outcomes should be explicit: `PASS`, `HOLD`, `DENY`, `ABSTAIN`, or `ERROR`. A config `PASS` proves only the scoped configuration behavior.

## Source-registry boundary

The source-registry path question that was unresolved in v0.2 is now narrower. Accepted Directory Rules establish the source-first writer under `data/registry/sources/`; for Soil, `data/registry/sources/soil/` is the current canonical source-registry writer described by repository documentation.

Retained domain-first registry surfaces are compatibility views or migration surfaces. Do not create or maintain divergent source descriptors in both locations. Configuration may reference a stable admitted source ID; it must not write registry authority or activate a connector.

## Sensitive and cross-domain boundaries

Soil configuration may contribute context to Agriculture, Hydrology, Geology, Habitat, Flora, Fauna, Hazards, and People/Land consumers, but each domain retains its own truth and release authority.

Private land, parcel, producer, owner, field-specific, conservation-practice, or private-sensor context requires explicit rights/privacy/sensitivity review. Configuration cannot make these public merely by omitting a field from the UI.

## AI and generated language

AI may explain already-governed Soil material through a governed consumer. It cannot create source role, support type, measurement context, evidence, policy, release state, or advice authority. EvidenceBundle and policy remain upstream of generated language.

## Definition of done for the first payload

The first non-README Soil config payload is complete only when all of the following are true:

- a real consumer is identified and current;
- placement under this shared config lane is justified rather than consumer-local placement;
- the file contains no secret or private operational binding;
- parser, binding, precedence, missing-file, and unknown-key behavior are documented;
- authoritative source/profile references are stable and reviewable;
- support-type separation and survey/source lineage are preserved;
- units/depth/method/QC/time/scale constraints are explicit where material;
- sensitivity/public-safe behavior fails closed;
- focused tests exercise positive and negative cases with synthetic or fixture data;
- changed-area validation is run and recorded;
- rollback/deactivation is documented;
- no source activation, lifecycle promotion, release, deployment, or publication is implied.

## Rollback and correction

This README can be reverted as a normal Git change. A future payload must additionally define how a consumer stops reading it and returns to the previous valid configuration. Config rollback does not silently roll back source, data, catalog, evidence, release, or published artifacts; those remain owned by their own correction and rollback processes.

## Open verification

The highest-value unresolved checks are the first real consumer and binding model, executable config validation, current contract/schema authority convergence, accepted source-role vocabulary mapping, machine-enforced support-type separation, source rights and freshness profiles, interpretation fitness-for-use rules, private-land handling, CI enforcement, correction propagation, and release/rollback integration.

Until those are verified, keep this lane small, explicit, inactive by presence, and fail closed.
