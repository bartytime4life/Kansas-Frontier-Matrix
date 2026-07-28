<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/atmosphere/sources/readme
name: Atmosphere Source Registry Compatibility README
path: data/registry/atmosphere/sources/README.md
type: data-registry-domain-source-compatibility-readme
version: v0.3.0
status: draft; compatibility-boundary; no-independent-writes
owners: NEEDS_VERIFICATION
created: 2026-06-28
updated: 2026-07-27
policy_label: internal-governance
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: atmosphere-source-navigation-view
path_posture: domain-first compatibility view; subtype-first registry authority; descriptor writes denied here
safety_posture: no-direct-public-path; no-source-activation; no-advisory-or-operational-use; fail-closed
related:
  - ../../README.md
  - ../README.md
  - ../../sources/atmosphere/README.md
  - ../../sources/atmosphere/aqs.source.json
  - ../../sources/atmosphere/knowledge_character.json
  - ../../../raw/atmosphere/README.md
  - ../../../work/atmosphere/README.md
  - ../../../quarantine/atmosphere/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../fixtures/domains/atmosphere/sources/README.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/registry/README.md
tags:
  - kfm
  - data
  - registry
  - atmosphere
  - sources
  - compatibility
  - generated-view
  - source-role
  - rights
  - sensitivity
  - freshness
  - cite-or-abstain
notes:
  - "ADR-0029 adopted Directory Rules v2 at docs/doctrine/directory-rules.md."
  - "Directory Rules DIR-SOURCE-003 and DIR-SOURCE-004 make the subtype-first source registry authoritative and prohibit this domain-first path from acting as an independent writer."
  - "No generator, parity check, active writer, active consumer, or accepted source-activation record was verified for this path."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Source Registry Compatibility View

[![Status: compatibility boundary](https://img.shields.io/badge/status-compatibility%20boundary-f59e0b?style=flat-square)](#status)
[![Authority: noncanonical view](https://img.shields.io/badge/authority-noncanonical%20view-8250df?style=flat-square)](#authority-and-path-decision)
[![Writes: denied](https://img.shields.io/badge/writes-denied-b91c1c?style=flat-square)](#write-contract)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md)

> **One-line purpose.** Preserve a safe, human-readable Atmosphere source navigation path while all source-descriptor identity and writes remain under the subtype-first registry authority.

> [!CAUTION]
> Do not add or edit source descriptors, activation decisions, payloads, credentials, or public-facing data here. This path does not activate a source, prove a claim, grant rights, clear sensitivity, authorize operational or health guidance, release data, or publish KFM content.

**Navigation:** [Purpose](#purpose) · [Status](#status) · [Authority](#authority-and-path-decision) · [Write contract](#write-contract) · [View contract](#view-contract) · [Source controls](#source-control-minimums) · [Validation](#validation) · [Related authority](#related-authority) · [Open verification](#open-verification)

## Purpose

This README governs the existing domain-first path:

```text
data/registry/atmosphere/sources/
```

Its bounded role is navigation and migration compatibility for readers approaching source governance from the Atmosphere domain lane. It may identify or link to Atmosphere-related source records, but it must not become a second registry writer.

The authoritative responsibility remains **registry identity and routing**, not Atmosphere observations, forecasts, advisories, model output, evidence, policy, catalog closure, release, or public delivery.

## Status

| Surface | Evidence-backed state |
|---|---|
| This README path | **CONFIRMED** at the pinned repository base |
| Governing Directory Rules | **CONFIRMED adopted** through [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) |
| Domain-first source path | **Compatibility/generated-view posture** under `DIR-SOURCE-004` |
| Subtype-first registry parent | **Canonical placement rule** under `DIR-SOURCE-003` |
| Atmosphere source-first scaffold | **CONFIRMED present** at [`data/registry/sources/atmosphere/`](../../sources/atmosphere/README.md) |
| Records verified in that scaffold | Two **PROPOSED placeholder** JSON files; no active source admission established |
| Generator and parity validation for this view | **NEEDS VERIFICATION** |
| Active writers and consumers of this exact path | **UNKNOWN** |
| Public or operational readiness | **DENY BY DEFAULT** |

> [!IMPORTANT]
> Repository presence is not activation. The current source-authority register is `PROPOSED` and contains no entries; this README must not infer an active source, accepted descriptor schema, current feed, or public-safe output.

## Authority and path decision

The accepted Directory Rules separate the two path shapes:

| Concern | Governing home | This path's relation |
|---|---|---|
| Machine source identities and descriptors | `data/registry/sources/` | May point to them; must not duplicate or mutate them |
| Human source guidance | `docs/sources/` and Atmosphere domain documentation | May summarize boundaries and link outward |
| Connector implementation | `connectors/` | No executable or activation authority here |
| Source payloads | `data/raw/`, `data/work/`, or `data/quarantine/` as governed | Payloads are prohibited here |
| Validation evidence and process memory | `data/proofs/` and `data/receipts/` | References only |
| Release decisions and public-safe carriers | `release/` and `data/published/` | No release or publication authority here |

**Placement result for source-descriptor records:** `DENY` independent writes here. A one-way generated navigation view may be `MIRROR` only after its canonical inputs, generator, owner, digest/parity check, consumers, rollback, and exit criteria are verified.

This README remains at the requested path to preserve navigation and make the no-write boundary explicit. It does not resolve every deeper source-ID or domain-index migration question.

## Write contract

### Allowed

- this compatibility README;
- a verified, generated, read-only index whose entries resolve to canonical subtype-first records;
- migration or tombstone metadata required by an accepted migration;
- parity, source digest, and generation metadata that cannot be mistaken for source admission;
- links to canonical contracts, schemas, policies, fixtures, tests, receipts, proofs, catalogs, correction records, rollback targets, and release decisions.

### Prohibited

| Do not place or maintain here | Required handling |
|---|---|
| `SourceDescriptor` or source-activation records | Write only through the accepted subtype-first registry topology |
| Atmosphere observations, station series, grids, rasters, model runs, satellite scenes, advisories, or downloaded files | Route through RAW, WORK, or QUARANTINE according to admission state |
| Manually copied source indexes | Generate from canonical records with parity validation or do not create |
| Rights, sensitivity, stale-state, access, or release policy | Keep normative rules under `policy/` |
| Contracts or machine schemas | Keep meaning under `contracts/` and shape under `schemas/` |
| Receipts, proofs, catalog records, release records, or published carriers | Use each owning object-family lane |
| Credentials, tokens, signed URLs, private endpoints, or restricted operational details | Use approved secret or restricted storage; never commit here |
| Public API, map, dashboard, alert, health, exposure, compliance, or AI output | Use governed released interfaces; cite or abstain |

## View contract

If a generated Atmosphere view is later implemented, every row must be derived from a canonical source record and remain strictly less authoritative than that record.

| Required view property | Minimum behavior |
|---|---|
| Stable identity | Carry the canonical `source_id`; do not mint a domain-local ID |
| Source location | Link to the canonical record or governed resolver |
| Role preservation | Carry the exact role from the canonical record; do not mint or upgrade a domain-local role. Keep contextual use and access restriction separate unless accepted authority defines them as roles |
| Rights and sensitivity | Surface unresolved or restrictive posture without upgrading it |
| Time and freshness | Preserve source, observation, issue, valid, retrieval, model-run, revision, expiration, and stale-state distinctions when applicable |
| Scope | Preserve station, network, grid, raster, aggregation, geography, precision, and uncertainty boundaries |
| Change lineage | Carry correction, supersession, withdrawal, deactivation, and rollback references |
| Generation evidence | Record canonical input digest, generator version, output digest, generated time, parity result, and rollback target |

The view must fail closed when a canonical record is missing, ambiguous, stale beyond its declared use, rights- or sensitivity-unresolved, or inconsistent with the generated projection.

## Source-control minimums

Atmosphere source families are especially vulnerable to role and time collapse. The following controls apply whether a reader arrives through this compatibility path or the canonical registry.

| Source family | Preserve | Never imply |
|---|---|---|
| Regulatory monitoring and archives | parameter, units, method, averaging interval, QA, revision, station/network, and time scope | that regulatory context is identical to an observation or release permission |
| Public AQI, smoke, and agency reporting | issuing authority, valid/effective time, stale state, caveats, and official-source routing | health advice, emergency direction, or timeless current conditions |
| Weather stations and mesonets | sensor/station identity, siting, units, QA, observation time, and missing/stale markers | that every station record is quality-assured or public-safe |
| Climate normals and anomalies | baseline period, method, scale, uncertainty, and revision state | that a normal or anomaly is a real-time observation |
| Satellite aerosol, smoke, fire, and cloud-adjacent products | algorithm/product identity, resolution, QA, limitations, footprint, and acquisition time | that AOD or smoke context is direct PM2.5 measurement |
| Forecast, reanalysis, and smoke-model fields | model/version, run time, forecast hour, inputs, uncertainty, validation, and valid time | that modeled fields are observations |
| Low-cost, community, research, or local networks | calibration, correction, confidence, ownership, terms, privacy, method, and review posture | regulatory equivalence or unrestricted reuse |
| Historical records | source vintage, station/instrument changes, digitization uncertainty, calendar/time-zone treatment, and correction lineage | current conditions or unchanged comparability |

Promotion must never silently upgrade source role. Aggregation must never create point truth. AI-generated language must never replace a canonical descriptor, EvidenceBundle, policy decision, review record, or release state.

## Inputs and outputs

| Direction | Accepted surface | Boundary |
|---|---|---|
| Input | Canonical source identities, role, rights, sensitivity, cadence, scope, and correction metadata | Must be resolved from an accepted source record or marked unavailable |
| Input | Registry, contract, schema, policy, fixture, validator, receipt, proof, catalog, and release references | A reference does not prove the target is accepted or executed |
| Output | Human navigation to canonical source governance | Read-only and non-authoritative |
| Output | Optional generated domain view | Requires one-way generation and parity evidence |
| Output | Structured hold or verification item | Must not activate, ingest, promote, release, or publish |

Public clients and ordinary AI/UI surfaces must not read this compatibility path as a data service.

## Validation

Before changing this README or materializing a view:

- [ ] Re-pin the repository base and re-read the accepted Directory Rules and ADR-0029.
- [ ] Inventory direct children, writers, readers, references, aliases, and any generated-file markers.
- [ ] Confirm all source-descriptor writes remain under the accepted subtype-first topology.
- [ ] Verify every view entry resolves to exactly one canonical source identity and matching digest.
- [ ] Verify role, rights, sensitivity, time/freshness, spatial scope, citation, correction, and supersession fields are not upgraded or dropped.
- [ ] Verify no source payload, secret, restricted identifier, unsafe precision, operational detail, or public-serving path is introduced.
- [ ] Verify links, anchors, badges, tables, alerts, code fences, HTML comments, and the final newline.
- [ ] Record generator, parity, and rollback evidence—or retain the view as README-only.

The repository's [`link-check`](../../../../.github/workflows/link-check.yml) workflow is currently an explicit readiness hold; it does not validate repository or external links. Manual or future repository-native link checks remain documentation QA only.

## Correction, supersession, and rollback

1. Correct the canonical source record or its governing authority first.
2. Emit the required correction, supersession, withdrawal, deactivation, or review record through its owning process.
3. Regenerate any admitted view from the corrected canonical inputs.
4. Invalidate stale view bytes and confirm parity before consumers resume.
5. If the view cannot be regenerated safely, remove the derived view while retaining this no-write README or an approved tombstone.

Before merge, rollback is the prior README blob on the scoped branch. After merge, use a transparent revert or follow-up pull request; do not restore independent descriptor writes at this path.

## Related authority

| Reference | Role |
|---|---|
| [Directory Rules v2](../../../../docs/doctrine/directory-rules.md) | Adopted placement doctrine; see `DIR-SOURCE-003`, `DIR-SOURCE-004`, and README inheritance |
| [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption and single-authority decision |
| [`data/registry/`](../../README.md) | Parent registry responsibility boundary |
| [Subtype-first Atmosphere scaffold](../../sources/atmosphere/README.md) | Current source-first Atmosphere registry surface |
| [`aqs.source.json`](../../sources/atmosphere/aqs.source.json) | Confirmed `PROPOSED` placeholder; not active admission evidence |
| [`knowledge_character.json`](../../sources/atmosphere/knowledge_character.json) | Confirmed `PROPOSED` placeholder; not accepted vocabulary authority |
| [Source Descriptor Standard](../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) | Draft semantic and admission guidance |
| [Atmosphere Source Registry documentation](../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md) | Human domain guidance |
| [Source authority register](../../../../control_plane/source_authority_register.yaml) | Proposed machine projection; currently empty |
| [Atmosphere source fixtures](../../../../fixtures/domains/atmosphere/sources/README.md) | Synthetic test examples; not source authority |
| [Atmosphere registry schema index](../../../../schemas/contracts/v1/domains/atmosphere/registry/README.md) | Draft schema-placement index; implementation remains unverified |

## Open verification

| Item | Status | Evidence required |
|---|---|---|
| Direct-child inventory at this path | `NEEDS VERIFICATION` | Pinned recursive tree and file classifications |
| Active writers and consumers | `UNKNOWN` | Connector, pipeline, tool, workflow, API/UI, and external-consumer inventory |
| View generator and parity check | `NOT VERIFIED` | Repository-owned generator, deterministic fixtures, tests, and output digest |
| Canonical source-ID topology below `data/registry/sources/` | `NEEDS VERIFICATION` | Populated source register, accepted identity grammar, migration mapping, and validator |
| SourceDescriptor contract and schema authority | `NEEDS VERIFICATION` | Accepted contract/schema pairing plus fixtures and validation |
| Atmosphere activation state | `UNKNOWN` | Populated source-authority entry and reviewed activation decision |
| Rights, sensitivity, stale-state, correction, and rollback enforcement | `UNKNOWN` | Policy, negative fixtures, validator outputs, receipts, and drills |
| CODEOWNERS and accountable steward | `NEEDS VERIFICATION` | Current path-specific routing and named accountable owner |

Unknowns narrow behavior and block higher-authority claims; they do not authorize plausible defaults.

## Change history

### v0.3.0 — 2026-07-27

- aligned the existing path with adopted Directory Rules v2 and ADR-0029;
- changed the path posture from unresolved descriptor lane to no-independent-write compatibility view;
- removed proposed descriptor filenames and local activation vocabulary that could create parallel authority;
- preserved source-role, rights, sensitivity, freshness, correction, rollback, and public-boundary controls;
- added evidence-backed badges, compact navigation, validation, and explicit open verification.

### v0.2.0 — 2026-06-28

- replaced the original placeholder with a detailed Atmosphere source-registry boundary;
- recorded the then-unresolved domain-first versus subtype-first path conflict.

[Back to top](#top)
