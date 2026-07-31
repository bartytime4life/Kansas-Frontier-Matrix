<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hydrology-readme
title: Hydrology Contracts — README
type: boundary-compact-readme; semantic-contract-index
version: v0.3
status: draft; PLACE; PROPOSED semantic contracts; mixed schema coverage; bounded validation only; no publication authority
owners:
  - "@bartytime4life — CODEOWNERS review route"
  - "Hydrology semantic steward assignment — NEEDS VERIFICATION"
created: 2026-06-22
updated: 2026-07-30
policy_label: public; contract-root; hydrology; evidence-bound; source-role-aware; not-for-life-safety; release-gated; rollback-aware
related:
  - ../README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/OBJECT_FAMILIES.md
  - ../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../schemas/contracts/v1/domains/hydrology/README.md
  - ../../../fixtures/domains/hydrology/README.md
  - ../../../tests/domains/hydrology/README.md
  - ../../../tools/validators/domains/hydrology/README.md
  - ../../../policy/domains/hydrology/README.md
  - ../../../data/registry/sources/hydrology/README.md
  - ../../../release/candidates/hydrology/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-hydrology.yml
  - ../../../.github/workflows/hydrology-proof-slice.yml
  - ../../../.github/CODEOWNERS
tags: [kfm, contracts, hydrology, DOM-HYD, watershed, huc, gauge, observation, nfhl, source-role, evidence-bundle, release-gated, rollback]
notes:
  - "Same-path modernization grounded in main@0fd7b2ed59e22f60491b267c244c04e55e965e96."
  - "Accepted Directory Rules v2 returns PLACE for contracts/domains/hydrology/; older flat-path proposals are historical drift, not a competing current authority."
  - "The directory contains 23 semantic contract documents plus this README. Every object contract remains v0.2 draft / PROPOSED."
  - "Eighteen contract-declared schema paths resolve; five are missing. Existing schemas are mixed shared-profile aliases, minimal identity envelopes, and permissive empty-object scaffolds."
  - "Executable Hydrology coverage is bounded to local EvidenceBundle alias shape, fixture polarity, and process-level network denial. Evidence closure, policy, proof, catalog closure, release, and publication remain held."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Contracts

[![Status: draft](https://img.shields.io/badge/status-draft-d29922?style=flat-square)](#status-and-authority)
[![Placement: PLACE](https://img.shields.io/badge/placement-PLACE-1f6feb?style=flat-square)](#placement-and-inheritance)
[![Validation: shape only](https://img.shields.io/badge/validation-shape__only-f59e0b?style=flat-square)](#validation-and-current-holds)
[![Publication: none](https://img.shields.io/badge/publication-none-b42318?style=flat-square)](#exposure-mutation-and-retention)

Semantic contracts for Hydrology identities, observations, regulatory context,
derived relationships, and trust-support envelopes.

> [!IMPORTANT]
> This directory defines human-readable meaning. It does not prove a Hydrology
> claim, admit a source, validate real-world evidence, make policy, approve a
> release, publish data, or provide emergency flood guidance.

## Quick navigation

- [Status and authority](#status-and-authority)
- [Placement and inheritance](#placement-and-inheritance)
- [Non-negotiable boundaries](#non-negotiable-boundaries)
- [Belongs, prohibited, inputs, and outputs](#belongs-prohibited-inputs-and-outputs)
- [Exposure, mutation, and retention](#exposure-mutation-and-retention)
- [Verified direct-child map](#verified-direct-child-map)
- [Contract inventory](#contract-inventory)
- [Schema posture and drift](#schema-posture-and-drift)
- [Source-role and anti-collapse rules](#source-role-and-anti-collapse-rules)
- [Validation and current holds](#validation-and-current-holds)
- [Promotion, correction, and rollback](#promotion-correction-and-rollback)
- [Evidence ledger](#evidence-ledger)
- [Open verification register](#open-verification-register)

## Status and authority

| Surface | Current posture at the pinned snapshot | Authority boundary |
|---|---|---|
| This README | v0.3; `draft`; `PLACE`; `BOUNDARY_COMPACT` | Indexes this directory and records verified limits. It does not upgrade any child contract. |
| Direct semantic contracts | 23 files; each v0.2 and `draft` / `PROPOSED` | Define candidate object/interface meaning only. |
| Contract-declared schemas | 18 paths resolve; 5 are missing | Existing shape does not establish semantic truth, evidence, policy, or release. |
| Hydrology tests | One executable smoke module with three tests; seven named modules remain documentation-only placeholders | Proves only the bounded behavior actually asserted. |
| Hydrology policy | Four five-line `PROPOSED` scaffolds with `default allow := false` | Deny-by-default scaffolding is not accepted policy semantics or a release decision. |
| Proof-bearing designation | ADR-0009 is `proposed`; configured lane maturity is partial | The lane is not semantically closed or proof-bearing in operation. |
| Release and publication | No authority created by this directory or README | Publication requires separate evidence, policy, review, release, correction, and rollback closure. |

**Repository review route:** [`@bartytime4life`](../../../.github/CODEOWNERS) is
the verified CODEOWNERS route for `contracts/`. Hydrology, evidence, policy,
sensitivity, and release stewardship assignments remain `NEEDS VERIFICATION`;
CODEOWNERS routing is not independent review, policy approval, or release
authority.

[Back to top](#top)

## Placement and inheritance

This directory inherits the semantic-contract boundary from
[`contracts/domains/`](../README.md). Accepted
[Directory Rules v2](../../../docs/doctrine/directory-rules.md) makes the
three-way split mandatory:

| Responsibility | Owning root | Hydrology surface |
|---|---|---|
| Semantic meaning | `contracts/` | `contracts/domains/hydrology/` |
| Machine-checkable shape | `schemas/` | `schemas/contracts/v1/domains/hydrology/` |
| Allowed, denied, held, restricted, or abstained outcomes | `policy/` | `policy/domains/hydrology/` |

The accepted standard explicitly uses Hydrology as its domain-lane example.
[ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts those exact rules and makes them effective repository authority.

**Path decision:** `PLACE`.

- Authority owner: semantic meaning.
- Responsibility root: `contracts/`.
- Scope kind: domain.
- Scope ID: `hydrology`.
- Rules: `DIR-AUTHROOT-002`, `DIR-SCOPELANE-001` through
  `DIR-SCOPELANE-004`, and `DIR-README-001` through `DIR-README-005`.
- Evidence: accepted Directory Rules v2, ADR-0029, the current repository tree,
  and the parent contract README.

Older prose that proposed flat `contracts/hydrology/` or
`schemas/contracts/v1/hydrology/` paths is historical drift. No competing flat
contract or schema file was found at the pinned snapshot. Do not recreate one.

[Back to top](#top)

## Non-negotiable boundaries

> [!CAUTION]
> **KFM Hydrology is not an emergency flood-warning or life-safety system.**
> It must not replace official alerts, evacuation instructions, navigation,
> engineering judgment, insurance determinations, or emergency-response
> authority.

<!-- Separate safety callouts so Markdown renderers do not merge them. -->

> [!WARNING]
> **NFHL is regulatory context, not observed flooding.** A flood-zone
> designation must not be presented as observed inundation, a forecast extent,
> a hydraulic-model result, or current flood status.

<!-- Separate safety callouts so Markdown renderers do not merge them. -->

> [!IMPORTANT]
> **Source role does not change during transformation.** An observation does
> not become a forecast, a modeled result does not become an observation, an
> aggregate does not become per-place truth, and a candidate does not become
> public because it crossed a directory boundary.

Additional invariants:

- Evidence-dependent claims resolve an `EvidenceRef` to an admissible
  `EvidenceBundle` or return a bounded non-answer.
- Public and ordinary UI clients use governed interfaces and release-approved
  public-safe carriers, never RAW, WORK, QUARANTINE, canonical/internal, or
  unreleased candidate stores.
- Schema validity is not source truth, source admission, evidence closure,
  public safety, policy approval, review, promotion, release, or publication.
- Private-well, owner, infrastructure, exact-location, and other sensitive
  implications require explicit policy and public-safe treatment.
- Generated text, maps, graphs, tiles, summaries, and model output remain
  subordinate to evidence and release state.

[Back to top](#top)

## Belongs, prohibited, inputs, and outputs

### Belongs here

- Human-readable semantic definitions for Hydrology-owned object and interface
  families.
- Explicit exclusions, source-role rules, temporal meaning, identity
  boundaries, evidence expectations, sensitivity posture, public-use limits,
  correction semantics, and rollback expectations.
- Links to paired schemas, fixtures, tests, validators, policy, source
  registry, lifecycle, proof, release, and governed-delivery surfaces.
- A verified direct-child index and an honest maturity ledger.

### Prohibited here

| Prohibited material | Owning responsibility root |
|---|---|
| JSON Schema or generated type authority | `schemas/` |
| Rego or other executable admissibility rules | `policy/` |
| Test inputs and expected outputs | `fixtures/` |
| Tests and validator implementation | `tests/`, `tools/validators/` |
| Source descriptors or activation records | `data/registry/sources/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED records | `data/` lifecycle and accountability lanes |
| Receipts and proof objects | `data/receipts/`, `data/proofs/` |
| Release, correction, withdrawal, or rollback decisions | `release/` |
| Connector, pipeline, package, application, or renderer code | Its executable responsibility root |
| Real source payloads, sensitive locations, credentials, or personal data | Governed external storage or the appropriate restricted lifecycle lane |

### Inputs

This index is maintained from:

- accepted directory and authority doctrine;
- Hydrology domain doctrine and accepted/proposed ADR state;
- current direct-child contract bytes;
- paired schema bytes and `$ref` targets;
- synthetic fixture and test inventory;
- validator and workflow definitions;
- policy scaffold state;
- source-registry, evidence, release, correction, and rollback references.

### Outputs and consumers

The output is reviewable semantic guidance for contract authors, schema authors,
validator and test authors, policy reviewers, source and evidence stewards,
pipeline and API implementers, map/UI authors, governed-AI authors, and release
reviewers.

It is not a runtime DTO, data record, source registry, policy decision,
validation report, proof, release manifest, public API payload, map layer, or
AI answer.

[Back to top](#top)

## Exposure, mutation, and retention

| Property | Required posture |
|---|---|
| Exposure | Public repository documentation only. Do not embed nonpublic source payloads, sensitive exact locations, credentials, personal data, or operational secrets. |
| Permitted writers | Reviewed repository changes by authorized contributors. CODEOWNERS routes review; pipelines, connectors, watchers, public clients, and AI runtime must not rewrite this semantic authority. |
| Mutability | Versioned and reviewable. Semantic changes require coordinated contract/schema/test/consumer review where applicable. |
| Retention | Git history preserves prior bytes. Supersession uses explicit lineage; correction does not silently erase relied-on meaning. |
| Generation | Hand-authored authority document. Generated indexes may assist review but must not overwrite this file as an independent authority. |
| Physical storage | Git repository. This path carries no authority over external Hydrology data storage. |
| Public-delivery effect | None. A commit, pull request, merge, test pass, badge, or rendered README is not promotion or publication. |

The lifecycle for Hydrology records remains:

`RAW -> WORK or QUARANTINE -> PROCESSED -> CATALOG and optional TRIPLETS -> PUBLISHED`

Promotion is a governed state transition supported by receipts, evidence,
policy, review, release, correction, and rollback. It is never inferred from a
file move or successful documentation check.

[Back to top](#top)

## Verified direct-child map

The following map is verified from repository search at
`main@0fd7b2ed59e22f60491b267c244c04e55e965e96`. It shows direct children only,
as required by Directory Rules v2.

```text
contracts/domains/hydrology/
├── README.md                       # boundary contract and verified index
├── aquifer_observation.md           # aquifer-state observation meaning
├── decision_envelope.md             # finite runtime outcome semantics
├── domain_feature_identity.md       # shared Hydrology feature identity
├── domain_layer_descriptor.md       # layer meaning; not release authority
├── domain_observation.md            # shared Hydrology observation semantics
├── domain_validation_report.md      # validation-result meaning
├── drought_link.md                  # Hydrology-to-drought relationship
├── evidence_bundle.md               # Hydrology evidence-support profile
├── flow_observation.md              # discharge observation meaning
├── gauge_site.md                    # monitoring-site identity
├── groundwater_well.md              # well identity and sensitivity boundary
├── huc_unit.md                      # HUC identity and vintage semantics
├── hydro_feature.md                 # stream and waterbody feature meaning
├── hydrograph.md                    # observed or modeled time-series meaning
├── irrigation_link.md               # Hydrology-to-irrigation relationship
├── nfhl_zone.md                     # regulatory flood context only
├── reach_identity.md                # reach identity and ambiguity boundary
├── run_receipt.md                   # process-memory semantics
├── upstream_trace.md                # derived network traversal meaning
├── water_level_observation.md       # water-level observation meaning
├── water_quality_observation.md     # water-quality observation meaning
├── water_use_link.md                # Hydrology-to-water-use relationship
└── watershed.md                     # watershed meaning and scope
```

All 23 child contract documents are v0.2 `draft` / `PROPOSED` at the pinned
snapshot. File presence and prose depth do not make them validated, released,
or published.

[Back to top](#top)

## Contract inventory

### Identity and feature contracts

| Contract | Semantic role | Contract-declared schema posture |
|---|---|---|
| [`domain_feature_identity.md`](./domain_feature_identity.md) | Shared domain feature identity and deterministic-reference boundary. | [Minimal `id` envelope](../../../schemas/contracts/v1/domains/hydrology/domain_feature_identity.schema.json); permissive beyond three generic properties. |
| [`huc_unit.md`](./huc_unit.md) | HUC identity, level, source-vintage, and boundary meaning. | [Permissive empty-object scaffold](../../../schemas/contracts/v1/domains/hydrology/huc_unit.schema.json). |
| [`watershed.md`](./watershed.md) | Watershed identity and drainage-area context. | [Permissive empty-object scaffold](../../../schemas/contracts/v1/domains/hydrology/watershed.schema.json). |
| [`hydro_feature.md`](./hydro_feature.md) | Stream, river, waterbody, and hydrographic-feature meaning. | [Permissive empty-object scaffold](../../../schemas/contracts/v1/domains/hydrology/hydro_feature.schema.json). |
| [`reach_identity.md`](./reach_identity.md) | Reach identity, source-version, crosswalk, and ambiguity boundary. | [Permissive empty-object scaffold](../../../schemas/contracts/v1/domains/hydrology/reach_identity.schema.json). |
| [`gauge_site.md`](./gauge_site.md) | Monitoring-location identity, separate from observations. | [Permissive empty-object scaffold](../../../schemas/contracts/v1/domains/hydrology/gauge_site.schema.json). |
| [`groundwater_well.md`](./groundwater_well.md) | Well identity, access, location, and sensitivity meaning. | [Permissive empty-object scaffold](../../../schemas/contracts/v1/domains/hydrology/groundwater_well.schema.json). |

### Observation and time-series contracts

| Contract | Semantic role | Contract-declared schema posture |
|---|---|---|
| [`domain_observation.md`](./domain_observation.md) | Shared observation meaning and source/time/evidence boundary. | [Minimal `id` envelope](../../../schemas/contracts/v1/domains/hydrology/domain_observation.schema.json); permissive beyond three generic properties. |
| [`flow_observation.md`](./flow_observation.md) | Observed discharge/flow meaning with unit and qualifier expectations. | [Permissive empty-object scaffold](../../../schemas/contracts/v1/domains/hydrology/flow_observation.schema.json). |
| [`water_level_observation.md`](./water_level_observation.md) | Observed level/stage meaning. | [Permissive empty-object scaffold](../../../schemas/contracts/v1/domains/hydrology/water_level_observation.schema.json). |
| [`water_quality_observation.md`](./water_quality_observation.md) | Water-quality measurement meaning. | [Permissive empty-object scaffold](../../../schemas/contracts/v1/domains/hydrology/water_quality_observation.schema.json). |
| [`aquifer_observation.md`](./aquifer_observation.md) | Aquifer-state observation and well-reference boundary. | `MISSING`: declared `aquifer_observation.schema.json` does not resolve. |
| [`hydrograph.md`](./hydrograph.md) | Time series whose observed/modeled role must remain explicit. | [Permissive empty-object scaffold](../../../schemas/contracts/v1/domains/hydrology/hydrograph.schema.json). |

### Regulatory, derived, and cross-domain contracts

| Contract | Semantic role | Contract-declared schema posture |
|---|---|---|
| [`nfhl_zone.md`](./nfhl_zone.md) | FEMA regulatory flood-hazard context; never observed flooding. | [Permissive empty-object scaffold](../../../schemas/contracts/v1/domains/hydrology/nfhl_zone.schema.json). |
| [`upstream_trace.md`](./upstream_trace.md) | Derived network traversal with source/version/ambiguity lineage. | `MISSING`: declared `upstream_trace.schema.json` does not resolve. |
| [`water_use_link.md`](./water_use_link.md) | Evidence-bearing relationship to water-use authority. | `MISSING`: declared `water_use_link.schema.json` does not resolve. |
| [`drought_link.md`](./drought_link.md) | Relationship to drought status or indicators without ownership collapse. | `MISSING`: declared `drought_link.schema.json` does not resolve. |
| [`irrigation_link.md`](./irrigation_link.md) | Relationship to irrigation/agriculture authority without ownership collapse. | `MISSING`: declared `irrigation_link.schema.json` does not resolve. |

### Trust-support and delivery-boundary contracts

| Contract | Semantic role | Contract-declared schema posture |
|---|---|---|
| [`decision_envelope.md`](./decision_envelope.md) | Finite `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` response meaning. | [Alias to the shared runtime schema](../../../schemas/contracts/v1/domains/hydrology/decision_envelope.schema.json). |
| [`evidence_bundle.md`](./evidence_bundle.md) | Hydrology profile for evidence support and citation scope. | [Alias to the shared evidence schema](../../../schemas/contracts/v1/domains/hydrology/evidence_bundle.schema.json). |
| [`run_receipt.md`](./run_receipt.md) | Process-memory semantics; a receipt is not proof or approval. | [Alias to the shared runtime receipt schema](../../../schemas/contracts/v1/domains/hydrology/run_receipt.schema.json). |
| [`domain_validation_report.md`](./domain_validation_report.md) | Validation-result meaning and bounded outcome reporting. | [Minimal `id` envelope](../../../schemas/contracts/v1/domains/hydrology/domain_validation_report.schema.json); permissive beyond three generic properties. |
| [`domain_layer_descriptor.md`](./domain_layer_descriptor.md) | Layer meaning, source/evidence pointers, and public-boundary expectations. | [Minimal `id` envelope](../../../schemas/contracts/v1/domains/hydrology/domain_layer_descriptor.schema.json); permissive beyond three generic properties. |

[Back to top](#top)

## Schema posture and drift

The 23 contract-declared schema paths resolve as follows:

| Schema class | Count | Current consequence |
|---|---:|---|
| Shared-profile aliases | 3 | `decision_envelope`, `evidence_bundle`, and `run_receipt` delegate through `$ref`; the domain aliases do not add Hydrology semantics. |
| Minimal identity envelopes | 4 | `domain_feature_identity`, `domain_layer_descriptor`, `domain_observation`, and `domain_validation_report` require only `id` and permit additional properties. |
| Empty-object scaffolds | 11 | Stable `$id` and title exist, but no properties or required fields are defined and arbitrary properties are accepted. |
| Missing contract-declared schemas | 5 | Aquifer observation, drought link, irrigation link, upstream trace, and water-use link lack their declared machine-shape file. |

Additional drift found in the schema lane:

- [`catalog_matrix.schema.json`](../../../schemas/contracts/v1/domains/hydrology/catalog_matrix.schema.json)
  is a permissive minimal scaffold whose declared domain contract and fixture
  lane are absent; the proof workflow explicitly holds CatalogMatrix closure.
- [`hydro-crosswalk-manifest.schema.json`](../../../schemas/contracts/v1/domains/hydrology/hydro-crosswalk-manifest.schema.json)
  is a permissive empty-object scaffold whose declared contract path is absent.
- The [Hydrology schema README](../../../schemas/contracts/v1/domains/hydrology/README.md)
  still says no concrete schemas were confirmed, despite the current files.
  That README is stale documentation debt and requires a separate,
  schema-owned update.

Do not describe any Hydrology object family as `schema-aligned`,
`validated`, or `active` from these files alone.

[Back to top](#top)

## Source-role and anti-collapse rules

| Source role | Example | Required interpretation |
|---|---|---|
| `observed` | Gauge reading or sampled water-quality measurement | May support an observation only when identity, time, unit, qualifier, and evidence resolve. |
| `regulatory` | FEMA NFHL zone | Regulatory context only; never observed or forecast inundation. |
| `modeled` | Reconstructed hydrograph or terrain-derived surface | Requires model/run/uncertainty lineage; never an observation. |
| `aggregate` | HUC summary or drought/irrigation rollup | Retains aggregation unit and window; never per-place truth. |
| `administrative` | Well, allocation, or water-right registry context | Administrative status only unless separate evidence supports another claim. |
| `candidate` | Watcher output or quarantined record | No public edge before validation, policy, review, and promotion. |
| `synthetic` | Fixture, reconstruction, or generated summary | Test or interpretive material only; never observed reality. |

Anti-collapse boundaries:

- `GaugeSite` is not a `FlowObservation`, `WaterLevelObservation`, or
  `WaterQualityObservation`.
- `GroundwaterWell` identity is not an `AquiferObservation`.
- `NFHLZone` is not `ObservedFloodEvent`, forecast inundation, current flood
  status, or emergency instruction.
- `Hydrograph` must preserve whether its points are observed, modeled, or
  mixed; rendering a line does not settle the role.
- `HUCUnit`, `Watershed`, `HydroFeature`, and `ReachIdentity` are distinct
  identity and geometry concepts.
- `UpstreamTrace` is a derived traversal, not source truth.
- Water-use, drought, and irrigation links do not transfer canonical ownership
  into Hydrology.
- A `RunReceipt`, `DomainValidationReport`, or schema pass is not an
  `EvidenceBundle`, `PolicyDecision`, `ReleaseManifest`, or publication event.
- A valid `DecisionEnvelope` shape does not justify `ANSWER`; unresolved
  evidence, policy, sensitivity, or release state requires `ABSTAIN`, `DENY`,
  or `ERROR` as appropriate.

[Back to top](#top)

## Validation and current holds

### Confirmed bounded command

The repository-defined no-network smoke slice is:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
python -m pytest -q -p no:cacheprovider \
  tests/domains/hydrology/test_hydrology_smoke.py
```

The module contains three executable tests:

1. accept one synthetic EvidenceBundle alias fixture;
2. reject one fixture missing the reviewed required field; and
3. fail closed for process-level socket, DNS, and URL calls.

The [`domain-hydrology` workflow](../../../.github/workflows/domain-hydrology.yml)
runs that module and the EvidenceBundle wrapper. It also guards the broader
test, validator, source, schema, and policy inventories so placeholder changes
must be reviewed deliberately.

### Explicit holds

| Surface | Current state | Not established |
|---|---|---|
| Seven named domain test modules | One-line `PROPOSED` placeholders | HUC fingerprinting, NFHL role separation, NHDPlus ambiguity, reach ambiguity, USGS normalization, no-network proof, and EvidenceBundle semantic closure |
| Decision-envelope and run-receipt wrappers | Present and inventoried | Accepted domain semantics or executed Hydrology coverage |
| Broader Hydrology schemas | Permissive, minimal, alias-only, or missing | Contract/schema parity and meaningful negative rejection |
| Hydrology policy | Four deny-default scaffolds | Source-role, freshness, sensitivity, groundwater, rights, evidence, or release decisions |
| [`hydrology-proof-slice` workflow](../../../.github/workflows/hydrology-proof-slice.yml) | Readiness inspection with explicit holds | Proof production, semantic EvidenceRef-to-EvidenceBundle closure, and CatalogMatrix closure |
| Pipeline and E2E proof path | Placeholder/TODO surfaces | Governed proof, promotion, correction, rollback, release, or publication |

A green smoke or workflow result is evidence only for the tested revision and
boundary. It must not be cited as evidence that a Hydrology source is admitted,
a claim is true, an EvidenceBundle is semantically closed, policy allowed a
record, or a public release exists.

[Back to top](#top)

## Promotion, correction, and rollback

Before any contract-backed Hydrology carrier can become public, the owning
workflow must close, as applicable:

- deterministic identity and source-version lineage;
- admitted source role, rights, cadence, and permitted claims;
- meaningful machine shape and negative fixtures;
- evidence resolution and citation scope;
- temporal and freshness posture;
- sensitivity and public-safe transformation;
- policy outcome and required review;
- catalog/proof agreement;
- release manifest and immutable public carrier;
- correction, withdrawal, invalidation, and rollback target.

Rollback this documentation change if it:

- recreates a flat or parallel contract/schema authority;
- treats permissive scaffolds as meaningful validation;
- hides the five missing contract-declared schemas or the two unpaired schema
  scaffolds;
- upgrades placeholder tests, policy, pipelines, or workflows to implemented
  status;
- collapses NFHL, modeled, aggregate, administrative, candidate, or synthetic
  roles into observations;
- weakens the governed public-client boundary;
- implies that documentation, CI, a commit, or a merge releases Hydrology data.

Before merge, rollback is to close the draft pull request and abandon its
scoped branch. After merge, use a focused revert or corrective pull request
against the actual merge commit. The current baseline blob is
`4a511d3f4d052cf6af8d92c60fe71bc9d73a5c37`. Reverting this README does not
revert any external source, Hydrology observation, policy decision, release
state, or publication.

[Back to top](#top)

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| [`docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) at blob `fd49a0b…` | CONFIRMED / adopted through ADR-0029 | `contracts/` owns meaning; domain Hydrology uses this path; BOUNDARY_COMPACT fields and direct-child map law apply. | Does not implement contract semantics. |
| [`ADR-0029`](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | ACCEPTED | Makes the exact Directory Rules v2 bytes effective repository authority. | Does not implement later topology or maturity work. |
| Current `contracts/domains/hydrology/` search at `main@0fd7b2e…` | CONFIRMED | 24 direct Markdown files: this README plus 23 v0.2 draft contracts. | Search and file presence do not prove semantics or runtime use. |
| Contract-by-contract schema-reference resolution | CONFIRMED | 18 resolved paths and five missing paths; resolved shapes fall into alias, minimal, or empty-stub classes. | Does not prove validators, consumers, or field-level parity. |
| [`test_hydrology_smoke.py`](../../../tests/domains/hydrology/test_hydrology_smoke.py) and its workflow | CONFIRMED executable boundary | Three bounded local tests for alias shape, fixture polarity, and process-level network denial. | Not evidence closure, source admission, policy, proof, release, or publication. |
| Seven other `tests/domains/hydrology/test_*.py` modules | CONFIRMED placeholders | Records intended coverage names. | No executable assertions. |
| Four `policy/domains/hydrology/*.rego` files | CONFIRMED scaffolds | Deny-by-default placeholder posture. | No accepted Hydrology policy behavior. |
| [`ADR-0009`](../../../docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md) | CONFIRMED proposed decision and current gate ledger | Hydrology is the configured candidate for first proof-bearing graduation; current proof, evidence, and catalog gates are held. | Does not accept the ADR or graduate the lane. |
| [`CODEOWNERS`](../../../.github/CODEOWNERS) | CONFIRMED review route | `@bartytime4life` is the verified GitHub review identity for `contracts/`. | Not stewardship assignment, independent approval, policy, or release authority. |

[Back to top](#top)

## Open verification register

| ID | Status | Required work |
|---|---|---|
| `HYD-CONTRACT-01` | `NEEDS VERIFICATION` | Assign verified Hydrology, contract, evidence, policy, sensitivity, and release stewards without treating CODEOWNERS as role assignment. |
| `HYD-CONTRACT-02` | `NEEDS VERIFICATION` | Reconcile each v0.2 contract with a meaningful closed schema, positive and negative fixtures, validator, tests, and known consumers. |
| `HYD-CONTRACT-03` | `NEEDS VERIFICATION` | Add or deliberately defer schemas for aquifer observation, drought link, irrigation link, upstream trace, and water-use link. |
| `HYD-CONTRACT-04` | `NEEDS VERIFICATION` | Resolve the unpaired CatalogMatrix and hydro-crosswalk-manifest schema scaffolds without creating parallel authority. |
| `HYD-CONTRACT-05` | `NEEDS VERIFICATION` | Update the schema-lane README whose concrete inventory is stale; keep that work schema-owned and path-scoped. |
| `HYD-CONTRACT-06` | `NEEDS VERIFICATION` | Replace the seven placeholder test modules with deterministic, fixture-backed negative and positive coverage in bounded slices. |
| `HYD-CONTRACT-07` | `NEEDS VERIFICATION` | Implement and test source-role, freshness, sensitivity, groundwater, rights, evidence, and release policy with finite fail-closed outcomes. |
| `HYD-CONTRACT-08` | `NEEDS VERIFICATION` | Prove EvidenceRef-to-EvidenceBundle semantic closure, citation behavior, and cite-or-abstain response handling. |
| `HYD-CONTRACT-09` | `NEEDS VERIFICATION` | Close CatalogMatrix, proof, promotion, correction, rollback, governed API, map/UI, and publication gates without executing placeholder approval logic. |
| `HYD-CONTRACT-10` | `NEEDS VERIFICATION` | Audit remaining Hydrology docs for stale flat-path and “repo not mounted” claims now contradicted by accepted Directory Rules and current repository evidence. |

Re-review this README when direct children, schema posture, test or validator
coverage, policy, CODEOWNERS, source admission, exposure, sensitivity, ADR
status, proof/release posture, correction, withdrawal, rollback, or public
consumers change.

[Back to top](#top)
