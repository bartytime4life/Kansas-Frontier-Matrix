<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/atmosphere/sources/readme
name: Atmosphere Source Registry Compatibility README
path: data/registry/atmosphere/sources/README.md
type: data-registry-domain-source-compatibility-readme
version: v0.4.0
status: draft; compatibility-boundary; no-independent-writes
owners:
  - "NEEDS VERIFICATION: registry and source stewards"
  - "NEEDS VERIFICATION: Atmosphere domain steward"
  - "NEEDS VERIFICATION: rights, sensitivity, and public-safety reviewers"
  - "NEEDS VERIFICATION: policy, validation, proof, and release stewards"
created: 2026-06-28
updated: 2026-07-28
policy_label: internal-governance
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: atmosphere-source-navigation-view
domain: atmosphere
path_posture: domain-first compatibility view; subtype-first registry authority; descriptor writes denied here
safety_posture: no-direct-public-path; no-source-activation; no-advisory-health-regulatory-or-operational-authority; fail-closed
related:
  - ../../README.md
  - ../README.md
  - ../../sources/README.md
  - ../../sources/atmosphere/README.md
  - ../../sources/atmosphere/aqs.source.json
  - ../../sources/atmosphere/knowledge_character.json
  - ../../../raw/atmosphere/README.md
  - ../../../work/atmosphere/README.md
  - ../../../quarantine/atmosphere/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../receipts/atmosphere/README.md
  - ../../../proofs/atmosphere/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../published/atmosphere/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../contracts/source/source_descriptor.md
  - ../../../../schemas/contracts/v1/source/README.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/registry/README.md
  - ../../../../policy/domains/atmosphere/README.md
  - ../../../../fixtures/domains/atmosphere/sources/README.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../.github/workflows/domain-atmosphere.yml
  - ../../../../.github/workflows/link-check.yml
  - ../../../../release/candidates/atmosphere/README.md
tags:
  - kfm
  - data
  - registry
  - atmosphere
  - sources
  - compatibility
  - generated-view
  - source-role
  - provider-lineage
  - rights
  - sensitivity
  - freshness
  - units
  - temporal-integrity
  - spatial-support
  - correction
  - rollback
  - cite-or-abstain
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 8775d3865016d39171918a2580179b369be85da8
  prior_blob: 6ac6a74530599be6fc74a64645e886cf7d0c0edd
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: cd044a38047cc9b3725d2e083eb201eb86109308
  parent_blob: eb99029511d8c2e80a7c94542050af083c12ca5b
  canonical_source_lane_blob: 6a50dd496225cd9e4c3165dead10cde3d0f23959
  registry_parent_blob: b327d22956f5454482a35dbf265f45b901c1f2a3
  source_registry_parent_blob: 2821e9681273bff6b430920d0a45312c5643ba33
  source_descriptor_standard_blob: 4327c603f76e5b5a76fa058fe24ac2af91e496d8
  source_descriptor_contract_blob: b57ae5ccc042c1423b75c168438800384c9b6713
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  aqs_placeholder_blob: 2899950cd366d9afe7c468baa45cacc65da139e9
  knowledge_character_placeholder_blob: 4b2067e4f1ba70d4689d56ad36b952ead131864c
  atmosphere_registry_schema_index_blob: 4c22c541d86d79765784bfa612e44731af74e43c
  atmosphere_source_fixtures_blob: 83a40d45d7fb5a60c4f7f40ba2efb9b031ce70e6
  domain_atmosphere_workflow_blob: 3bd0183481a73c1aaad011e4ef1e361a3ee6b5f2
  link_check_workflow_blob: c91477f6a6da84203e61b3151076eb46b3a65941
  inspection_date: 2026-07-28
notes:
  - "This README preserves the stable identity of the existing domain-first Atmosphere source-registry path."
  - "Adopted Directory Rules v2 makes the subtype-first source registry authoritative and denies independent descriptor writes here."
  - "Bounded repository search returned only this README at the domain-first path and the README plus two PROPOSED placeholder JSON files at the subtype-first Atmosphere lane; this is not a full recursive inventory."
  - "The source-authority register is PROPOSED and empty, so no active Atmosphere source admission is established."
  - "The domain-atmosphere and link-check workflows are explicit readiness holds and do not validate registry records, admit sources, prove Atmosphere claims, approve release, or publish."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Source Registry Compatibility View

[![Status: compatibility boundary](https://img.shields.io/badge/status-compatibility%20boundary-f59e0b?style=flat-square)](#status)
[![Canonical writer: subtype first](https://img.shields.io/badge/canonical%20writer-subtype--first-0969da?style=flat-square)](#authority-and-path-decision)
[![Writes: denied](https://img.shields.io/badge/writes-denied-b91c1c?style=flat-square)](#write-contract)
[![Operational use: denied](https://img.shields.io/badge/operational%20use-denied-b91c1c?style=flat-square)](#atmosphere-measurement-time-and-scope-integrity)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md)

> **One-line purpose.** Preserve a safe, human-readable Atmosphere source navigation path while source identity and descriptor writes remain under the subtype-first registry authority.

> [!CAUTION]
> Do not add or edit source descriptors, activation decisions, source payloads, credentials, operational details, or public-facing Atmosphere data here. This path does not activate a source, prove a claim, grant rights, clear sensitivity, determine compliance, issue health or emergency guidance, authorize release, or publish KFM content.

> [!WARNING]
> Atmosphere material is unusually vulnerable to source-role, unit, time, spatial-support, and stale-state collapse. AQI is not concentration; AOD or smoke context is not a direct PM2.5 measurement; a model field is not an observation; an aggregate is not point truth; and a public upstream source is not automatic release permission.

**Navigation:** [Purpose](#purpose) · [Status](#status) · [Authority](#authority-and-path-decision) · [Inventory](#current-bounded-inventory) · [Write contract](#write-contract) · [View contract](#view-contract) · [Source controls](#source-control-minimums) · [Measurement/time integrity](#atmosphere-measurement-time-and-scope-integrity) · [Inputs and outputs](#inputs-and-outputs) · [Workflow evidence](#current-workflow-evidence) · [Validation](#validation) · [Correction and rollback](#correction-supersession-and-rollback) · [Related authority](#related-authority) · [Open verification](#open-verification)

<a id="purpose"></a>

## Purpose

This README governs the existing domain-first path:

```text
data/registry/atmosphere/sources/
```

Its bounded role is navigation and migration compatibility for readers approaching source governance from the Atmosphere domain lane. It may identify or link to Atmosphere-related source records, but it must not become a second source-registry writer.

The authoritative responsibility remains **registry identity and routing**—not Atmosphere observations, forecasts, advisories, model output, health interpretation, regulatory conclusions, evidence, policy, catalog closure, release, or public delivery.

<a id="status"></a>

## Status

| Surface | Evidence-backed state |
|---|---|
| This README path | **CONFIRMED** at `main@8775d3865016d39171918a2580179b369be85da8` |
| Document lifecycle | `draft` |
| README profile | Sensitive `BOUNDARY_COMPACT` compatibility view |
| Governing Directory Rules | **CONFIRMED adopted** through [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) |
| Domain-first source path | **Compatibility/generated-view posture** under `DIR-SOURCE-004` |
| Subtype-first source registry | **Canonical placement rule** under `DIR-SOURCE-003` |
| Canonical Atmosphere source lane | [`data/registry/sources/atmosphere/`](../../sources/atmosphere/README.md) |
| Canonical-lane records found in bounded search | README plus two JSON files explicitly marked `PROPOSED`; no active admission established |
| Local domain-first descriptor payloads | None established; bounded search returned this README only |
| Source-authority register | **CONFIRMED present**, `PROPOSED`, and empty |
| Atmosphere registry schema index | Draft index; concrete registry schemas remain **NEEDS VERIFICATION** |
| Atmosphere source fixtures | Draft synthetic fixture lane; payload inventory and executable validation remain **NEEDS VERIFICATION** |
| Atmosphere workflow | Explicit validation, proof, and release-readiness holds; no source admission or publication authority |
| Active writers and consumers of this exact path | **UNKNOWN** |
| Direct public, medical, regulatory, emergency, or operational use | **DENY BY DEFAULT** |
| Accountable stewardship assignments | **NEEDS VERIFICATION** |

Repository presence is not activation. A README, proposed schema, placeholder record, empty register, connector, workflow, commit, pull request, or merge does not establish an admitted source, accepted descriptor, rights clearance, sensitivity clearance, evidence closure, release approval, current conditions, or public-safe output.

<a id="authority-and-path-decision"></a>

## Authority and path decision

Adopted Directory Rules v2 separates canonical source identity from domain-first navigation:

| Concern | Governing home | This path's relation |
|---|---|---|
| Machine source identities and descriptors | `data/registry/sources/` | May point to them; must not duplicate or mutate them |
| Human source guidance | `docs/sources/` and Atmosphere domain documentation | May summarize boundaries and link outward |
| Connector and watcher implementation | `connectors/`, `tools/`, and `pipelines/` | No executable or activation authority here |
| Source payloads | `data/raw/`, `data/work/`, or `data/quarantine/` as governed | Payloads are prohibited here |
| Contracts and schemas | `contracts/` and `schemas/` | Meaning and machine shape remain separate authorities |
| Policy and review | `policy/` and governed review records | This README cannot make allow, deny, restrict, hold, or release decisions |
| Validation evidence and process memory | `data/proofs/` and `data/receipts/` | References only |
| Catalog, release, and public-safe carriers | `data/catalog/`, `release/`, and `data/published/` | No catalog, release, or publication authority here |

**Placement result for source-descriptor records:** `DENY` independent writes here.

A one-way generated navigation view may be `MIRROR` only after its canonical inputs, generator, accountable owner, source and output digests, parity check, consumers, rollback target, expiry or exit criteria, and regeneration command are verified.

This README remains at the requested path to preserve navigation and make the no-write boundary explicit. It does not resolve source-ID grammar, `air` versus `atmosphere` slug drift in adjacent roots, schema-path drift, producer/consumer inventory, or final migration disposition.

<a id="current-bounded-inventory"></a>

## Current bounded inventory

This inventory is grounded in the pinned repository search and exact file reads used for this revision. It is not a complete recursive-tree guarantee.

| Surface | Verified content | What it does not establish |
|---|---|---|
| `data/registry/atmosphere/sources/README.md` | This compatibility README | No local descriptor, activation, payload, proof, release, or public-serving state |
| [`data/registry/sources/atmosphere/README.md`](../../sources/atmosphere/README.md) | Draft subtype-first source-lane README | Does not prove accepted schema, active admission, complete inventory, or runtime readers |
| [`aqs.source.json`](../../sources/atmosphere/aqs.source.json) | `PROPOSED` placeholder linked to an Atmosphere verification backlog | Not a conformant or active AQS SourceDescriptor |
| [`knowledge_character.json`](../../sources/atmosphere/knowledge_character.json) | `PROPOSED` placeholder created from documentation inventory | Not accepted vocabulary, source-role, or admission authority |
| [`source_authority_register.yaml`](../../../../control_plane/source_authority_register.yaml) | `PROPOSED` metadata with an empty `entries` list | No active source, steward assignment, rights clearance, or activation decision |
| [Atmosphere registry schema index](../../../../schemas/contracts/v1/domains/atmosphere/registry/README.md) | Draft documentation index | No concrete registry-schema inventory or accepted schema home |
| [Atmosphere source fixtures](../../../../fixtures/domains/atmosphere/sources/README.md) | Draft synthetic fixture guidance | No authoritative records; payload inventory and executable tests remain unverified |

Do not infer absence from bounded search alone. A complete inventory requires a pinned recursive tree, file classification, generated-file detection, LFS or external-storage review, and writer/consumer analysis.

<a id="write-contract"></a>

## Write contract

### Allowed

- this compatibility README;
- a verified, generated, read-only index whose entries resolve to canonical subtype-first records;
- migration, redirect, tombstone, or retirement metadata required by an accepted migration;
- parity, canonical-input digest, output digest, generation time, expiry, and rollback metadata that cannot be mistaken for source admission;
- public-safe links to canonical contracts, schemas, policies, fixtures, tests, receipts, proofs, catalogs, correction records, rollback targets, and release decisions.

### Prohibited

| Do not place or maintain here | Required handling |
|---|---|
| `SourceDescriptor`, source-intake, or source-activation records | Write through the accepted subtype-first registry topology and governing decision process |
| Atmosphere observations, station series, grids, rasters, model runs, satellite scenes, advisories, reports, or downloaded files | Route through RAW, WORK, or QUARANTINE according to admission and review state |
| Dataset, layer, domain-state, rights, sensitivity, or crosswalk registry records | Use the owning subtype-first registry family |
| Manually copied source indexes | Generate from canonical records with parity validation or do not create |
| Rights, sensitivity, stale-state, access, health, regulatory, or release policy | Keep normative rules under `policy/` and official authorities |
| Contracts or machine schemas | Keep meaning under `contracts/` and shape under `schemas/` |
| Receipts, proofs, catalog records, release records, or published carriers | Use each owning object-family lane |
| Credentials, tokens, signed URLs, private endpoints, facility-security detail, or restricted operational information | Use approved secret or restricted storage; never commit here |
| Public API, map, dashboard, alert, health, exposure, compliance, search, graph, vector-index, or AI output | Use governed released interfaces; cite or abstain |

<a id="view-contract"></a>

## View contract

If a generated Atmosphere view is later implemented, every row must derive from exactly one canonical source record and remain strictly less authoritative than that record.

| Required view property | Minimum behavior |
|---|---|
| Stable identity | Carry the canonical `source_id`; do not mint a domain-local identity |
| Canonical location | Link to the canonical record or governed resolver |
| Provider lineage | Preserve the original publisher, monitoring network, contributing institution, sensor owner, dataset, and aggregation path where applicable |
| Role preservation | Carry the exact canonical source role; do not infer or upgrade a role locally |
| Parameter and method | Preserve parameter identity, native units, averaging interval, method, instrument or algorithm, and QA posture |
| Rights and sensitivity | Surface unresolved or restrictive posture without upgrading it |
| Time and freshness | Preserve observation, issue, valid, effective, model-run, forecast, retrieval, revision, expiration, correction, and stale-state distinctions |
| Spatial support | Preserve station, network, point, grid, raster, plume, polygon, regional aggregate, resolution, uncertainty, and precision boundaries |
| Negative state | Preserve missing, unavailable, invalid, provisional, below-detection, stale, withdrawn, and denied states without coercion |
| Change lineage | Carry correction, supersession, withdrawal, deactivation, and rollback references |
| Generation evidence | Record canonical input digest, generator version, output digest, generated time, parity result, expiry, and rollback target |

The view must fail closed when a canonical record is missing, ambiguous, stale beyond its declared use, rights- or sensitivity-unresolved, unit- or method-incompatible, spatially mismatched, or inconsistent with the generated projection.

<a id="source-control-minimums"></a>

## Source-control minimums

Atmosphere source families are especially vulnerable to role, measurement, time, and spatial collapse. These controls apply whether a reader arrives through this compatibility path or the canonical registry.

| Source family or material class | Preserve | Never imply |
|---|---|---|
| Regulatory monitoring and archives | parameter, units, method, instrument, averaging interval, QA, revision, station/network, jurisdiction, and time scope | that regulatory context is identical to a measurement, current compliance determination, or release permission |
| Aggregators and distributors | original provider, network, station or sensor identity, licensing chain, method, QA, and source role | that the aggregation path creates regulatory, observed, or canonical authority |
| Public AQI, smoke, and agency reporting | issuing authority, category or index definition, issue/valid/expiration time, stale state, caveats, and official-source routing | raw concentration, health diagnosis, emergency direction, or timeless current conditions |
| Weather stations and mesonets | sensor/station identity, siting, units, method, QA flags, observation time, and missing/stale markers | that every station record is quality-assured, representative beyond its support, or public-safe |
| Climate normals and anomalies | baseline period, method, scale, uncertainty, revision state, and comparison basis | real-time observation, forecast, or unchanged comparability across editions |
| Satellite aerosol, smoke, fire, and cloud-adjacent products | product/algorithm identity, resolution, QA, footprint, acquisition time, cloud/surface limits, and source role | direct surface concentration, exposure, or confirmed smoke impact at a point |
| Forecast, reanalysis, interpolation, and smoke-model fields | model/version, run time, forecast hour, valid time, inputs, uncertainty, resolution, and validation scope | observation, official advisory, or measured exposure |
| Low-cost, community, research, or local networks | calibration, correction, confidence, ownership, terms, privacy, method, siting, and review posture | regulatory equivalence, unrestricted reuse, or universal representativeness |
| Historical records | source vintage, station/instrument changes, digitization uncertainty, time-zone/calendar treatment, and correction lineage | current conditions or direct comparability without documented harmonization |
| Cross-domain context and impact inputs | source role, scale, time, uncertainty, join purpose, and owning downstream domain | crop, health, habitat, hydrology, infrastructure, or hazard conclusions owned by another lane |

Promotion must never silently upgrade source role. Aggregation must never create point truth. A map, dashboard, graph, model, or AI-generated explanation must never replace a canonical descriptor, `EvidenceBundle`, policy decision, review record, official advisory, or release state.

<a id="atmosphere-measurement-time-and-scope-integrity"></a>

## Atmosphere measurement, time, and scope integrity

The registry view must preserve distinctions that are easy to lose in downstream joins and summaries. Current enforcement of these rules remains **NEEDS VERIFICATION**.

| Integrity dimension | Required preservation | Fail-closed example |
|---|---|---|
| Parameter identity | Pollutant or variable identity, method code, instrument or algorithm, and applicable standard | Do not compare or merge records when parameter identity is unresolved |
| Units and conversion | Native units, normalized units when used, conversion formula or specification, temperature/pressure basis where material, and rounding policy | Do not present unit-free or silently converted values |
| Averaging and aggregation | Instantaneous, hourly, rolling, daily, event, climatological, or other interval; aggregation support and completeness | Do not compare incompatible averaging periods as equivalent |
| Time semantics | Observation, issue, valid, effective, model-run, forecast, retrieval, revision, expiration, correction, and stale timestamps | Do not label a retrieved or model-run time as observation time |
| Missingness and quality | Missing, zero, below detection, invalid, provisional, QA-qualified, revised, withdrawn, and unavailable states | Do not coerce missing or invalid data to zero or “good” |
| Spatial support | Monitor point, station network, grid cell, raster footprint, plume, polygon, county/region aggregate, resolution, and uncertainty | Do not convert regional or gridded values into exact point truth |
| Model versus observation | Model/run identity, inputs, uncertainty, validation state, and observation references where used | Do not label modeled or interpolated values as observed |
| AQI versus concentration | Index definition, pollutant, breakpoint/version, averaging period, category, and issuing authority | Do not present AQI as a raw concentration or direct exposure dose |
| Revision and correction | Provisional/final status, source revision, corrected value, supersession, withdrawal, and consumer invalidation | Do not keep a stale compatibility view after canonical correction |

When these fields are unavailable, the safe result is a narrowed claim, visible hold, abstention, denial, or redirect to the official source—not a plausible default.

<a id="inputs-and-outputs"></a>

## Inputs and outputs

| Direction | Accepted surface | Boundary |
|---|---|---|
| Input | Canonical source identities, provider lineage, role, rights, sensitivity, cadence, parameter/method, time, spatial support, correction, and rollback metadata | Must resolve from an accepted record or remain explicitly unavailable |
| Input | Registry, contract, schema, policy, fixture, validator, receipt, proof, catalog, and release references | A reference does not prove acceptance, execution, evidence closure, or release |
| Output | Human navigation to canonical source governance | Read-only and non-authoritative |
| Output | Optional generated domain view | Requires one-way generation, parity evidence, expiry, and rollback |
| Output | Structured hold, migration, or verification item | Must not activate, ingest, promote, release, or publish |

Public clients and ordinary AI/UI surfaces must not read this compatibility path as a data service.

<a id="current-workflow-evidence"></a>

## Current workflow evidence

The current [`domain-atmosphere`](../../../../.github/workflows/domain-atmosphere.yml) workflow is an explicit readiness-hold workflow:

- it triggers on pull requests, pushes to `main`, and manual dispatch;
- it uses GitHub-hosted `ubuntu-latest`, `contents: read`, and `persist-credentials: false`;
- it performs no live source request;
- it checks required boundary files and detects whether executable Atmosphere tests, validators, proof producers, or release machinery have surfaced;
- it emits explicit holds because accepted executable Atmosphere validation, proof production, and release dry-run commands are not established.

A green held result is readiness evidence only. It is not source admission, descriptor validation, observation accuracy, AQI or concentration equivalence, health advice, regulatory determination, emergency authority, evidence closure, release approval, or publication.

The current [`link-check`](../../../../.github/workflows/link-check.yml) workflow is also an explicit governed hold. It does not check local paths, anchors, images, redirects, citations, or external URLs. Link resolution, when implemented, will remain documentation QA rather than truth, evidence, policy, or release authority.

<a id="validation"></a>

## Validation

Before changing this README or materializing a generated view:

- [ ] Re-pin the repository base and re-read adopted Directory Rules v2 and ADR-0029.
- [ ] Inventory direct children, canonical records, writers, readers, references, aliases, generated-file markers, and external consumers.
- [ ] Confirm all source-descriptor writes remain under the accepted subtype-first topology.
- [ ] Verify every view entry resolves to exactly one canonical source identity and matching source digest.
- [ ] Verify provider lineage, source role, parameter/method, units, averaging interval, rights, sensitivity, time/freshness, spatial support, citation, correction, and supersession fields are not upgraded, dropped, or coerced.
- [ ] Verify negative states such as missing, invalid, provisional, stale, withdrawn, denied, and below-detection remain distinguishable.
- [ ] Verify no source payload, secret, restricted identifier, unsafe precision, facility-security detail, operational endpoint, health guidance, or public-serving path is introduced.
- [ ] Verify metadata, links, anchors, badges, tables, alerts, code fences, HTML comments, UTF-8 encoding, and the final newline.
- [ ] Record generator, parity, expiry, and rollback evidence—or retain the view as README-only.
- [ ] Treat the Atmosphere and link-check workflows according to their declared hold scope; do not report them as registry, source, evidence, or release validation.

A passing source-level Markdown check or green readiness-hold workflow does not prove canonical registry enforcement, descriptor validity, rights clearance, source activation, measurement correctness, stale-state handling, policy correctness, evidence closure, release readiness, or public safety.

<a id="correction-supersession-and-rollback"></a>

## Correction, supersession, and rollback

1. Correct the canonical source record or governing authority first.
2. Emit the required correction, supersession, withdrawal, deactivation, review, or rollback record through its owning process.
3. Regenerate any admitted compatibility view from the corrected canonical inputs.
4. Invalidate stale view bytes and dependent caches or projections where governed consumers exist.
5. Verify identity, source and output digests, parity, negative states, and consumer refresh before use resumes.
6. If the view cannot be regenerated safely, remove the derived view while retaining this no-write README or an approved tombstone.

Before merge, rollback is closing the draft pull request and leaving the branch unmerged. After merge, use a transparent revert or follow-up pull request; do not restore independent descriptor writes at this path.

<a id="related-authority"></a>

## Related authority

| Reference | Role |
|---|---|
| [Directory Rules v2](../../../../docs/doctrine/directory-rules.md) | Adopted placement doctrine; see `DIR-SOURCE-003`, `DIR-SOURCE-004`, and README inheritance |
| [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption and single-authority decision |
| [`data/registry/`](../../README.md) | Parent registry responsibility boundary |
| [Atmosphere registry parent](../README.md) | Domain-first compatibility parent |
| [Subtype-first Atmosphere source lane](../../sources/atmosphere/README.md) | Canonical placement surface for Atmosphere source records; implementation remains draft |
| [`aqs.source.json`](../../sources/atmosphere/aqs.source.json) | Confirmed `PROPOSED` placeholder; not active admission evidence |
| [`knowledge_character.json`](../../sources/atmosphere/knowledge_character.json) | Confirmed `PROPOSED` placeholder; not accepted vocabulary or authority |
| [Source Descriptor Standard](../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) | Draft semantic and admission guidance |
| [SourceDescriptor contract](../../../../contracts/source/source_descriptor.md) | Draft semantic contract; paired schema and path migration remain proposed |
| [Atmosphere Source Registry documentation](../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md) | Human domain guidance |
| [Atmosphere registry schema index](../../../../schemas/contracts/v1/domains/atmosphere/registry/README.md) | Draft schema-placement index; concrete schemas unverified |
| [Atmosphere source fixtures](../../../../fixtures/domains/atmosphere/sources/README.md) | Synthetic fixture guidance; not source authority |
| [Source authority register](../../../../control_plane/source_authority_register.yaml) | Proposed machine projection; currently empty |
| [Atmosphere workflow](../../../../.github/workflows/domain-atmosphere.yml) | Explicit readiness holds; not source admission, proof, release, or publication authority |
| [Link-check workflow](../../../../.github/workflows/link-check.yml) | Explicit documentation-QA readiness hold; no links are currently checked |
| [Atmosphere release candidates](../../../../release/candidates/atmosphere/README.md) | Candidate boundary; a candidate is not a release |

<a id="open-verification"></a>

## Open verification

| Item | Status | Evidence required |
|---|---|---|
| Complete direct-child inventory at this path | **NEEDS VERIFICATION** | Pinned recursive tree, file classifications, generated markers, LFS/external-storage review |
| Active writers and consumers | **UNKNOWN** | Connector, watcher, pipeline, tool, workflow, API/UI, runtime, and external-consumer inventory |
| View generator, expiry, and parity check | **NOT VERIFIED** | Repository-owned generator, deterministic fixtures, tests, input/output digests, consumer refresh, rollback |
| Concrete descriptor inventory under `data/registry/sources/atmosphere/` | **UNKNOWN** beyond two placeholders in bounded search | Pinned tree, descriptors, identities, rights/sensitivity review, and validation |
| Canonical Atmosphere source README modernization | **NEEDS VERIFICATION** | Align its pre-adoption topology and slug text with accepted Directory Rules without changing descriptor state |
| `air` versus `atmosphere` path and code aliases | **NEEDS VERIFICATION** | Registered domain slug, alias map, consumers, migration plan, and accepted decision where identity changes |
| SourceDescriptor contract and schema authority | **NEEDS VERIFICATION** | Accepted contract/schema pairing, canonical path, compatibility policy, fixtures, and validator |
| Atmosphere activation state | **UNKNOWN** | Populated source-authority entry and reviewed activation decision |
| Parameter, unit, method, temporal, spatial-support, and stale-state enforcement | **UNKNOWN** | Schema fields, negative fixtures, validators, receipts, and representative runs |
| Rights, sensitivity, correction, supersession, and rollback enforcement | **UNKNOWN** | Policy, review records, negative fixtures, receipts, and drills |
| CODEOWNERS and accountable stewards | **NEEDS VERIFICATION** | Current path-specific routing and named accountable owners |
| Final migration disposition | **PROPOSED / NEEDS VERIFICATION** | Retained compatibility README, generated mirror, redirect/tombstone, or retirement decision |
| Physical deletion eligibility | **HOLD** | Zero-writer, zero-consumer, link-closure, parity/retirement, external-consumer review, and rollback evidence |

Unknowns narrow behavior and block higher-authority claims; they do not authorize plausible defaults.

## Change history

### v0.4.0 — 2026-07-28

- added a current commit- and blob-pinned evidence snapshot;
- replaced generic ownership with explicit `NEEDS VERIFICATION` steward roles;
- grounded the bounded inventory in the current canonical README, two placeholder records, empty source-authority register, schema index, fixtures, and workflow evidence;
- added provider-lineage, parameter/method, units, averaging, missingness, spatial-support, time, revision, and negative-state preservation rules;
- replaced the stale link-check-only validation note with explicit Atmosphere and link-check workflow interpretation;
- strengthened generated-view parity, expiry, correction, cache invalidation, consumer refresh, and rollback requirements;
- preserved the no-independent-write compatibility posture, stable path, `doc_id`, source-role discipline, operational-safety boundary, and cite-or-abstain rule.

### v0.3.0 — 2026-07-27

- aligned the existing path with adopted Directory Rules v2 and ADR-0029;
- changed the path posture from unresolved descriptor lane to no-independent-write compatibility view;
- removed proposed descriptor filenames and local activation vocabulary that could create parallel authority;
- preserved source-role, rights, sensitivity, freshness, correction, rollback, and public-boundary controls;
- added evidence-backed badges, compact navigation, validation, and explicit open verification.

### v0.2.0 — 2026-06-28

- replaced the original placeholder with a detailed Atmosphere source-registry boundary;
- recorded the then-unresolved domain-first versus subtype-first path conflict.

KFM rule: `data/registry/atmosphere/sources/` is a compatibility view for public-safe navigation and lineage only. It is not an independent source-registry writer, payload store, Atmosphere truth authority, policy authority, evidence authority, release authority, health or emergency authority, or public data service.

[Back to top](#top)
