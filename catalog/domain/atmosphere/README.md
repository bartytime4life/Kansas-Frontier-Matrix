<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-domain-atmosphere-readme
title: catalog/domain/atmosphere/ — Atmosphere Domain Catalog Compatibility Redirect
type: readme; compatibility-redirect; domain-lane; drift-containment; non-authoritative
version: v0.3.0
status: repository-grounded draft; compatibility-only; deny-new-trust-writes; migration-unresolved
owners: NEEDS VERIFICATION — Atmosphere, air-quality, catalog/data, registry, evidence, receipt, proof, policy, release, correction, rollback, and docs stewards
created: 2026-06-16
updated: 2026-07-24
policy_label: public-review; compatibility-only; fail-closed; no-direct-public-path; non-life-safety
current_path: catalog/domain/atmosphere/README.md
canonical_counterpart: data/catalog/domain/atmosphere/README.md
prepared_under_prompt: KFM Markdown Modernization & GitHub Documentation Implementation Agent v4.0.0
review_packet_id: kfm-md-catalog-domain-atmosphere-redirect-20260724
truth_posture: >
  CONFIRMED exact path, parent compatibility contracts, canonical counterpart,
  Directory Rules placement doctrine, Atmosphere source-role doctrine, relevant
  proposed ADRs, bounded workflow evidence, and repository-relative link targets /
  PROPOSED normalized containment, validation, migration, correction, and rollback
  contract / UNKNOWN recursive non-README inventory, historical producers,
  consumers, runtime reads, hosting, caches, public effects, and source-rights
  closure / NEEDS VERIFICATION accepted disposition ADR, executable enforcement,
  stewardship, release closure, correction handling, and rollback drill
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d2e2e8c8002c4623a0e15f50b734512a4661ea41
  prior_blob: 34fd75fad7efb0e42477841e81995829dd93bef0
  method: complete target and governing-neighbor reads plus bounded repository, workflow, and pull-request search; no recursive clone, runtime, deployment, host-render, or external-store inspection
related:
  - ../README.md
  - ../../README.md
  - ../../../data/catalog/domain/README.md
  - ../../../data/catalog/domain/atmosphere/README.md
  - ../../../data/catalog/domain/atmosphere/pm25_2026/README.md
  - ../../../data/registry/README.md
  - ../../../data/registry/sources/atmosphere/README.md
  - ../../../data/receipts/README.md
  - ../../../data/proofs/README.md
  - ../../../data/published/README.md
  - ../../../release/README.md
  - ../../../release/candidates/atmosphere/README.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/atmosphere/SOURCES.md
  - ../../../docs/domains/atmosphere/SENSITIVITY.md
  - ../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../contracts/domains/atmosphere/README.md
  - ../../../schemas/contracts/v1/domains/atmosphere/README.md
  - ../../../policy/domains/atmosphere/README.md
  - ../../../tests/domains/atmosphere/README.md
  - ../../../tools/validators/domains/atmosphere/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/workflows/domain-atmosphere.yml
  - ../../../.github/CODEOWNERS
tags: [kfm, catalog, domain, atmosphere, air-quality, weather, climate, smoke, aod, pm25, compatibility-redirect, drift-containment, non-authoritative, non-life-safety, cite-or-abstain]
notes:
  - "The first twelve H2 sections follow the Directory Rules folder-README contract."
  - "All numbered v0.2 section fragments remain available through explicit legacy anchors."
  - "This Markdown-only change does not migrate, validate, release, publish, alert, or authorize any Atmosphere object."
  - "Static badges project verified documentation posture only; they do not assert CI, security, release, publication, or emergency authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `catalog/domain/atmosphere/` — Atmosphere Domain Catalog Compatibility Redirect

> **One-line purpose.** Preserve a visible redirect from the legacy root-level Atmosphere catalog path to `data/catalog/domain/atmosphere/` while denying new trust-bearing writes, direct public use, and emergency or life-safety authority.

[![Status: compatibility only](https://img.shields.io/badge/status-compatibility%20only-d4a72c?style=flat-square)](#status)
[![Authority: non-authoritative](https://img.shields.io/badge/authority-non--authoritative-b42318?style=flat-square)](#authority-level)
[![Trust-bearing writes: denied](https://img.shields.io/badge/trust%20writes-denied-b42318?style=flat-square)](#what-does-not-belong-here)
[![Emergency authority: denied](https://img.shields.io/badge/emergency%20authority-denied-b42318?style=flat-square)](#atmosphere-source-role-guardrails)
[![Canonical home: data/catalog/domain/atmosphere](https://img.shields.io/badge/canonical-data%2Fcatalog%2Fdomain%2Fatmosphere-1f6feb?style=flat-square)](#related-folders)

> [!IMPORTANT]
> This path is a child redirect inside the non-canonical top-level `catalog/` drift root. It may document routing, migration, correction, and rollback, but it cannot own Atmosphere catalog records, observations, station or sensor data, source registries, receipts, proofs, policy, release decisions, published artifacts, contracts, schemas, code, or public truth.

> [!CAUTION]
> KFM Atmosphere is not an emergency alert or life-safety system. AQI is not raw concentration; AOD is not surface PM2.5; forecasts, reanalysis, interpolation, and model fields are not observations. Low-cost sensor data, preliminary reports, advisory context, and public exposure require their proper source roles, evidence, caveats, rights, policy, review, and release state.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Evidence](#evidence-basis) · [Guardrails](#atmosphere-source-role-guardrails) · [Boundary](#lifecycle-and-authority-boundary) · [Migration](#migration-correction-and-rollback) · [Verification](#open-verification-register) · [Done](#definition-of-done) · [Language](#safe-language-rules) · [No-loss](#no-loss-ledger)

<a id="1-purpose"></a>

## Purpose

`catalog/domain/atmosphere/` keeps a legacy or accidental root-level Atmosphere catalog location visible as a **compatibility redirect and drift-control fence** while catalog work is routed to the governed lifecycle lane at `data/catalog/domain/atmosphere/`.

This README preserves path identity and link continuity. It does not grant this path an ongoing catalog responsibility, authorize a mirror of the canonical lane, or prove that every producer and consumer has migrated.

<a id="3-authority-boundary"></a>

## Authority level

**CONFIRMED path presence / CONFLICTED placement inherited from top-level `catalog/` / PROPOSED temporary redirect / non-authoritative.**

Atmosphere meaning and source-role doctrine live under `docs/domains/atmosphere/`; semantic contracts under `contracts/domains/atmosphere/`; machine shape under `schemas/contracts/v1/domains/atmosphere/`; admissibility under `policy/domains/atmosphere/`; lifecycle catalog records under `data/catalog/domain/atmosphere/`; source, rights, and sensitivity records under `data/registry/`; process memory under `data/receipts/`; proof support under `data/proofs/`; release decisions under `release/`; public clients use governed interfaces and released public-safe artifacts.

<a id="4-default-posture"></a>

## Status

| Field | Bounded result |
|---|---|
| Path | `catalog/domain/atmosphere/README.md` |
| Version | `v0.3.0` |
| Base evidence | `main@d2e2e8c8002c4623a0e15f50b734512a4661ea41` |
| Prior blob | `34fd75fad7efb0e42477841e81995829dd93bef0` |
| Parent posture | Compatibility redirect inside severe top-level catalog drift |
| Canonical counterpart | `data/catalog/domain/atmosphere/README.md` |
| Canonical child observed | `data/catalog/domain/atmosphere/pm25_2026/README.md` |
| Recursive non-README inventory | `UNKNOWN` |
| Historical producers, consumers, runtime reads, hosts, caches, or public effects | `UNKNOWN` |
| Migration or retirement | `NOT PERFORMED` |
| Emergency or life-safety authority | `DENIED` |
| Public or release readiness | `DENY BY PLACEMENT` |
| Human review | `PENDING` |

<a id="5-allowed-contents"></a>

## What belongs here

Only bounded compatibility material:

- this redirect README;
- reviewed migration, deprecation, drift, correction, or rollback notes;
- temporary marker metadata required by an accepted migration;
- no independent catalog, observation, evidence, policy, release, runtime, alerting, or publication payload.

Any future non-README file requires verified inventory, an accepted disposition, named review, explicit sunset or retention criteria, and validation that it cannot become parallel authority.

<a id="6-forbidden-contents"></a>

## What does NOT belong here

| Forbidden family | Governed home |
|---|---|
| Atmosphere catalog records, station indexes, observation catalogs, PM2.5 or ozone catalogs, smoke/AOD context, weather or climate catalogs, forecast or advisory context | `data/catalog/domain/atmosphere/` or an accepted child lane |
| STAC, DCAT, PROV, CatalogMatrix, catalog manifests, or graph/triplet projections | governed lanes under `data/catalog/` or `data/triplets/` |
| Source descriptors, dataset rows, crosswalks, rights, sensitivity, station, sensor, platform, or layer registry rows | `data/registry/` |
| RAW observations, corrected observations, model outputs, rasters, forecasts, station dumps, or generated previews | the correct controlled lifecycle lane under `data/` |
| Run, transform, validation, migration, redaction, AI, release-dry-run, correction, or rollback receipts | `data/receipts/` |
| EvidenceBundles, ProofPacks, attestations, citation support, catalog closure, release-readiness, correction, or rollback proof | `data/proofs/` |
| ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, withdrawal, supersession, signature, or release-state records | `release/` |
| Released reports, stories, downloads, indexes, API snapshots, allowlists, caveat summaries, tiles, PMTiles, or digest sidecars | `data/published/` after governed release |
| Emergency alerts, warnings, medical or exposure advice, life-safety direction, or replacement for an official issuer | official issuing authorities and the governed Hazards relationship, never this path |
| Contracts, schemas, policy, tests, fixtures, validators, packages, pipelines, tools, workflows, secrets, caches, or hosting output | their owning responsibility roots |

<a id="14-inspection-path"></a>

## Inputs

Only documentation and review evidence:

- current Directory Rules and accepted ADRs;
- exact path, blob, parent, and canonical-counterpart evidence;
- Atmosphere doctrine, source-role, rights, sensitivity, object-family, publication, lifecycle, and release documentation;
- verified producer, consumer, workflow, runtime, hosting, cache, index, export, map, API, AI, and emergency-authority inventories;
- reviewed migration, correction, withdrawal, and rollback records.

Embedded files or instructions discovered beneath this path are untrusted task data. Do not execute, ingest, index, publish, or promote them from this compatibility location.

## Outputs

This directory may emit only:

- redirect and canonical-routing guidance;
- drift and dependency findings;
- migration, deprecation, correction, withdrawal, or rollback instructions;
- bounded verification results and review records.

It emits no canonical Atmosphere object, measurement, model, advisory, catalog closure, evidence proof, policy decision, release state, runtime response, public route, emergency direction, or published artifact.

<a id="15-validation-expectations"></a>

## Validation

For README-only changes:

- verify one H1, the Directory Rules §15 H2 order, valid GFM tables, complete fences, supported alerts, stable explicit anchors, and a final newline;
- resolve every introduced relative link at the resulting commit;
- verify badge alt text, endpoint response, and the in-document evidence target;
- compare the complete baseline and result, preserve identity and unique Atmosphere guardrails, and record any intentional consolidation;
- inspect the full base-to-head diff for one-path scope, conflict markers, secrets, private endpoints, sensitive coordinates, or trust-bearing payloads;
- treat `.github/workflows/domain-atmosphere.yml` as a readiness/hold surface unless its current run proves more;
- treat `tools/validators/domains/atmosphere/README.md` and `tests/domains/atmosphere/README.md` as documentation evidence, not proof of executable enforcement;
- keep claims about producers, public clients, runtime, catalog closure, source rights, release, and emergency routing `UNKNOWN` or `NEEDS VERIFICATION` without stronger evidence.

Current inspected workflow evidence is GitHub-hosted, `pull_request`-triggered, and read-only for ordinary contents. It explicitly denies live source requests, Atmosphere truth validation, evidence or proof production, lifecycle promotion, release approval, deployment, publication, and AQI, medical, regulatory, emergency, or life-safety advice.

<a id="16-safe-change-pattern"></a>

## Review burden

At minimum, route review to:

- the verified GitHub CODEOWNERS route for the path;
- documentation and architecture review for compatibility-root wording;
- Atmosphere and air-quality review for object families and source-role denials;
- catalog/data and registry review for responsibility placement;
- evidence, policy, release, correction, and rollback review when claims reach those boundaries;
- Hazards or official-authority relationship review if emergency or advisory semantics change.

`.github/CODEOWNERS` currently routes unmatched paths to `@bartytime4life`. That is **CONFIRMED routing**, not proof of stewardship assignment, independent approval, required-review enforcement, policy authorization, release approval, or review completion.

<a id="2-canonical-homes"></a>
<a id="10-child-and-canonical-lane-posture"></a>

## Related folders

| Responsibility | Verified repository path |
|---|---|
| Parent compatibility roots | [`catalog/domain/`](../README.md) · [`catalog/`](../../README.md) |
| Canonical domain catalog parent | [`data/catalog/domain/`](../../../data/catalog/domain/README.md) |
| Canonical Atmosphere catalog lane | [`data/catalog/domain/atmosphere/`](../../../data/catalog/domain/atmosphere/README.md) |
| Observed PM2.5 child lane | [`data/catalog/domain/atmosphere/pm25_2026/`](../../../data/catalog/domain/atmosphere/pm25_2026/README.md) |
| Source, rights, and sensitivity registry | [`data/registry/`](../../../data/registry/README.md) · [`data/registry/sources/atmosphere/`](../../../data/registry/sources/atmosphere/README.md) |
| Process memory and proof support | [`data/receipts/`](../../../data/receipts/README.md) · [`data/proofs/`](../../../data/proofs/README.md) |
| Release and public-safe artifacts | [`release/`](../../../release/README.md) · [`release/candidates/atmosphere/`](../../../release/candidates/atmosphere/README.md) · [`data/published/`](../../../data/published/README.md) |
| Atmosphere doctrine | [`README`](../../../docs/domains/atmosphere/README.md) · [`SOURCES`](../../../docs/domains/atmosphere/SOURCES.md) · [`SENSITIVITY`](../../../docs/domains/atmosphere/SENSITIVITY.md) · [`PUBLICATION_POSTURE`](../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md) · [`OBJECT_FAMILY_MAP`](../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md) |
| Meaning, shape, and admissibility | [`contracts/domains/atmosphere/`](../../../contracts/domains/atmosphere/README.md) · [`schemas/contracts/v1/domains/atmosphere/`](../../../schemas/contracts/v1/domains/atmosphere/README.md) · [`policy/domains/atmosphere/`](../../../policy/domains/atmosphere/README.md) |
| Tests and documented validator lane | [`tests/domains/atmosphere/`](../../../tests/domains/atmosphere/README.md) · [`tools/validators/domains/atmosphere/`](../../../tools/validators/domains/atmosphere/README.md) |
| Readiness workflow and review routing | [`domain-atmosphere.yml`](../../../.github/workflows/domain-atmosphere.yml) · [`CODEOWNERS`](../../../.github/CODEOWNERS) |

These links prove that the named paths and documents existed at the evidence snapshot. They do not prove complete inventories, accepted schemas, source rights, deterministic validators, release closure, live routes, or public safety.

## ADRs

| Decision record | Observed state | Relevance |
|---|---:|---|
| [`ADR-0011 — Receipts vs Proofs vs Manifests vs Catalog Separation`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | `PROPOSED` | Supports the separation `receipt ≠ proof ≠ catalog ≠ publication`; it is not accepted-rule or enforcement proof. |
| [`ADR-0022 — Catalog Matrix · STAC + DCAT + PROV Must Agree`](../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) | `PROPOSED` | Supports cross-projection closure requirements; it does not prove an implemented or released Atmosphere CatalogMatrix. |

[`Directory Rules`](../../../docs/doctrine/directory-rules.md) §12 places Atmosphere as a lane inside responsibility roots; §13 treats parallel authority as drift; §14 governs reversible migration; §15 defines this folder-README contract. No accepted ADR authorizing root-level `catalog/domain/atmosphere/` as a canonical catalog was identified in the bounded review.

## Last reviewed

**2026-07-24** against `main@d2e2e8c8002c4623a0e15f50b734512a4661ea41`.

Review again after six months, or sooner if the parent compatibility contract, canonical Atmosphere catalog lane, source-role doctrine, Directory Rules, relevant ADR status, workflow posture, producer paths, public clients, advisory handling, or release process changes.

<a id="0-evidence-basis-for-this-revision"></a>

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| Exact target and prior blob | `CONFIRMED` | In-place upgrade of an existing README | Recursive inventory, producer history, or migration closure |
| Parent `catalog/` and `catalog/domain/` READMEs | `CONFIRMED` | Compatibility-only, deny-new-trust-writes posture | All legacy dependencies are removed |
| `data/catalog/domain/atmosphere/README.md` | `CONFIRMED path and draft posture` | Canonical Atmosphere catalog placement | Concrete valid records, complete schema/profile, or release state |
| `docs/domains/atmosphere/README.md` and supporting docs | `CONFIRMED document presence` | Non-life-safety and source-role doctrine | Runtime, source rights, or public behavior |
| Registry, receipt, proof, release, and published roots | `CONFIRMED document presence` | Object-family separation | Complete emitted inventories or cross-family closure |
| Directory Rules §§12–15 | `CONFIRMED doctrine` | Domain-lane placement, drift prevention, migration, README order | Full repository compliance |
| ADR-0011 and ADR-0022 | `CONFIRMED documents; PROPOSED decisions` | Bounded design intent | Acceptance or executable enforcement |
| `.github/workflows/domain-atmosphere.yml` | `CONFIRMED readiness surface` | Explicit holds and non-publisher boundaries | Atmosphere truth, proof, release, or public safety |
| `.github/CODEOWNERS` | `CONFIRMED route` | GitHub review request routing | Stewardship, independent approval, or branch protection |
| Open-PR search | `CONFIRMED bounded search` | No overlapping open Atmosphere catalog README PR was found | Historical, draft, renamed, or externally hosted work outside the search |

EvidenceBundle outranks generated prose. This README must narrow or abstain when evidence, source role, rights, sensitivity, review, policy, release, correction, or rollback state is not resolved.

<a id="8-atmosphere-source-role-guardrails"></a>

## Atmosphere source-role guardrails

Atmosphere catalog drift is risky because observations, public reports, proxies, models, forecasts, advisories, and emergency context can look interchangeable in an index. They are not.

| Guardrail | Required posture |
|---|---|
| Atmosphere is not emergency authority | Do not issue or restate life-safety direction as KFM authority. Preserve the official issuer, jurisdiction, issue and expiry time, and redirect users to that authority; route governed hazard relationships through the Hazards lane. |
| AQI is not raw concentration | Keep categorical AQI/report context separate from measured concentration, units, averaging windows, and proof support. Do not infer µg/m³ or ppb from an AQI label without an admissible governed transform. |
| AOD is not PM2.5 | Aerosol optical depth is a column proxy, not a surface mass observation. Any relationship requires an identified model, inputs, uncertainty, validation, evidence, and caveats. |
| Model fields are not observations | Forecast, reanalysis, interpolation, assimilation, and derived fusion retain model or forecast roles, run and valid times, versions, uncertainty, and limitations. |
| Preliminary reports are not regulatory archives | Preserve preliminary, corrected, certified, regulatory, and archival state; do not silently replace one with another. |
| Low-cost sensors remain caveated | Require device and site identity, calibration or correction method, QA state, confidence, limitations, source rights, policy posture, and release review before public use. |
| Station and parameter identity are explicit | Preserve station, sensor/platform, parameter, unit, method, vertical context, timestamp, time zone, duration, and quality flags. |
| Advisory context is passthrough context | Preserve official source, jurisdiction, timestamp, expiry, caveat, and link; never turn placement or summary into authority. |
| Public exposure is release-gated | Catalog presence does not make an object public. Require evidence, policy, review, release, public-safe representation, correction, and rollback support. |
| AI is interpretive only | AI summaries are candidates or carriers, never root truth; resolve EvidenceRef to EvidenceBundle and apply source-role, rights, sensitivity, policy, and release checks first. |

Common object families include `AirStation`, `AirObservation`, `PM25Observation`, `OzoneObservation`, `SmokeContext`, `AODRaster`, `WeatherStation`, `WeatherObservation`, `WindField`, `PrecipitationObservation`, `TemperatureObservation`, `ClimateNormal`, `ClimateAnomaly`, `ForecastContext`, and `AdvisoryContext`. Listing a family here does not prove its contract, schema, validator, record inventory, or release maturity.

<a id="9-minimum-safe-redirect-slice"></a>

## Minimum safe redirect slice

| Slice item | Minimum requirement | Why it matters |
|---|---|---|
| Redirect README | Points to the canonical Atmosphere catalog lane and owning support roots | Prevents parallel authority |
| No catalog or payload records | No station, observation, PM2.5, ozone, smoke, AOD, weather, climate, forecast, advisory, model, or manifest payload | Preserves lifecycle ownership |
| No registry, receipt, proof, release, or public object | No cross-family trust-bearing records | Preserves family separation |
| No emergency authority | No alerts, warnings, medical or exposure instructions, or replacement for an official issuer | Prevents dangerous authority confusion |
| Producer guard | Producers and workflows do not write durable Atmosphere material here | Prevents recurring drift |
| Consumer guard | APIs, maps, search, exports, tiles, stories, AI retrieval, static hosts, and caches do not read here as canonical | Preserves the trust membrane |
| Drift and correction procedure | Misplaced or consumed material has an auditable disposition and rollback target | Keeps remediation reversible |
| Verification backlog | Unknowns and missing enforcement remain visible | Prevents documentation from implying maturity |

<a id="7-directory-shape"></a>
<a id="13-diagram"></a>

## Lifecycle and authority boundary

```mermaid
flowchart LR
    LEGACY["catalog/domain/atmosphere/<br/>compatibility redirect"] -. "classify and redirect" .-> REVIEW["object-family and source-role review"]
    REVIEW --> CATALOG["data/catalog/domain/atmosphere/<br/>catalog records"]
    REVIEW --> REGISTRY["data/registry/<br/>source, rights, sensitivity"]
    REVIEW --> RECEIPTS["data/receipts/<br/>process memory"]
    REVIEW --> PROOFS["data/proofs/<br/>evidence and proof support"]
    CATALOG --> RELEASE["release/<br/>decision, correction, rollback"]
    REGISTRY --> RELEASE
    RECEIPTS --> RELEASE
    PROOFS --> RELEASE
    RELEASE --> PUBLISHED["data/published/<br/>released public-safe carriers"]
    OFFICIAL["official issuing authority"] --> HAZARDS["governed Hazards relationship"]
    LEGACY -. "must not bypass release" .-> PUBLISHED
    LEGACY -. "must not claim emergency authority" .-> OFFICIAL
```

The diagram is an ownership and governance map, not proof that a complete catalog pipeline, source registry, validator suite, release resolver, public route, emergency integration, correction flow, or rollback drill is implemented. The compatibility path participates only through classification and redirect.

The only assumed directory shape is the verified README itself. `MIGRATION.md`, `DRIFT.md`, `OPEN-QUESTIONS.md`, or marker files remain **PROPOSED** until an accepted, reviewed need exists. Do not treat an illustrative tree as inventory.

<a id="12-runtime-and-producer-anti-bypass-matrix"></a>

## Runtime and producer anti-bypass matrix

| Bypass risk | Required behavior | Evidence needed to close |
|---|---|---|
| Producer writes Atmosphere catalog material here | Deny; write to `data/catalog/domain/atmosphere/` | Producer config, negative test, and run evidence |
| Registry, receipt, proof, release, or public object lands here | Deny; route to its responsibility root | Classifier, validator, fixtures, and review |
| Public client, map, search, export, tile job, static host, or cache reads this path | Deny as canonical; use governed API and released public-safe carrier | Code/config inventory and runtime evidence |
| AQI is re-served as concentration | Hold or deny until identity, units, method, averaging window, transform, evidence, and caveats resolve | Source-role validator and evidence bundle |
| AOD is re-served as PM2.5 | Hold or deny; keep proxy role and model uncertainty explicit | Model, validation, uncertainty, and policy evidence |
| Forecast, reanalysis, or interpolation is labeled observed | Correct or deny; preserve knowledge character and time semantics | Contract/schema validation and review |
| Preliminary or low-cost sensor data loses caveats | Quarantine, correct, restrict, or deny | Calibration, QA, rights, caveat, policy, and release record |
| Advisory context becomes KFM authority | Remove or reroute to official issuer and governed Hazards relationship | Official-source and emergency-authority review |
| Claim-bearing entry lacks EvidenceBundle support | Cite-or-abstain; do not publish the unsupported claim | Resolvable EvidenceRef, EvidenceBundle, policy and release closure |
| Sensitive health, infrastructure, station, person, or relationship join appears | Deny, quarantine, redact, generalize, aggregate, or restrict | Sensitivity review and transform receipt |
| AI-generated summary appears here | Treat as candidate only; move to governed work/review flow | Evidence resolution, policy, review, and receipt |
| Documentation claims enforcement without run evidence | Mark `NEEDS VERIFICATION` | Current validator and required-check evidence |
| Drift was already consumed | Correct downstream indexes, caches, maps, API payloads, citations, and AI surfaces | Correction record, consumer parity, and rollback target |

<a id="11-migration-posture"></a>
<a id="17-rollback-and-correction-posture"></a>

## Migration, correction, and rollback

1. Freeze the governing doctrine, accepted decisions, exact tree, blobs, producers, consumers, and canonical counterpart.
2. Inventory every tracked, generated, hosted, cached, indexed, exported, mapped, API-served, and externally referenced object.
3. Classify object family and Atmosphere source role: catalog, observation, station, sensor, public report, proxy, model, forecast, advisory, registry, receipt, proof, release, public carrier, code, schema, policy, or temporary output.
4. Record rights, sensitivity, evidence, review, lifecycle, release, correction, and rollback state; unresolved material fails closed.
5. Accept a disposition before moving, mirroring, deprecating, or deleting anything.
6. Stop new writers and public readers with executable negative validation.
7. Move or regenerate trust-bearing material through the governed canonical process; preserve deterministic identity, digest, provenance, source role, units, time semantics, station/platform identity, and lineage.
8. Validate catalog, STAC/DCAT/PROV alignment when applicable, EvidenceRef resolution, policy, sensitivity transforms, source rights, release, and public-safe representation.
9. Correct downstream indexes, caches, exports, maps, tiles, stories, API payloads, citations, alerts/advisory links, and AI retrieval surfaces.
10. Rehearse rollback without recreating parallel authority or reintroducing misleading or sensitive content.
11. Retire the redirect only after zero-producer, zero-consumer, link, host, cache, correction, and rollback checks pass.

Before merge, rollback of this README update means closing the draft pull request and abandoning its branch. After merge, use a transparent revert commit or revert pull request; do not rewrite shared history. This documentation change performs no data, authority, release, publication, or emergency-routing migration.

<a id="19-open-verification-items"></a>

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive tracked and non-tracked inventory | `UNKNOWN` | Trusted checkout plus generated, LFS, hosted, cached, indexed, and external-reference classification |
| Producers, consumers, runtime reads, hosts, maps, exports, APIs, AI use, and caches | `UNKNOWN` | Code, configuration, workflow, runtime, hosting, and observability search |
| Accepted top-level `catalog/` and redirect disposition | `NEEDS VERIFICATION` | Accepted ADR, governing register, migration records, and deprecation controls |
| Canonical Atmosphere inventory, schema/profile, and catalog validators | `NEEDS VERIFICATION` | Current records, contracts, schemas, validators, fixtures, tests, and steward review |
| STAC/DCAT/PROV and CatalogMatrix closure | `NEEDS VERIFICATION` | Projection records, crosswalks, consistency validation, and accepted ADR status |
| Source descriptors, rights, sensitivity, station identity, and source-role validation | `NEEDS VERIFICATION` | Per-source registry and policy evidence plus executable validation |
| Redirect allowlist and negative-path enforcement | `NEEDS VERIFICATION` | Validator implementation, fixtures, tests, and required workflow |
| Emergency-authority and Hazards relationship behavior | `UNKNOWN` | Contracts, policy, implementation, official-source handling, tests, and runtime evidence |
| Public-client exclusion and release-safe delivery | `UNKNOWN` | Governed API, route, map, search, export, hosting, and release evidence |
| Migration, correction, retirement, and rollback closure | `NOT PERFORMED` | Reviewed manifest, consumer cutover, correction handling, and rollback drill |
| GitHub-rendered Mermaid and badge behavior | `PENDING` | Host render observation on the draft pull request |

<a id="18-definition-of-done"></a>

## Definition of done

This redirect is complete only while all of the following remain true:

- the path exists solely for compatibility, migration, drift, correction, or rollback documentation;
- it points readers and tools to `data/catalog/domain/atmosphere/` and the correct support roots;
- no trust-bearing writer, public client, map, search, export, tile job, API, host, cache, or AI surface depends on it;
- no catalog, observation, source, registry, receipt, proof, release, published, schema, policy, code, workflow, test, or application authority is duplicated here;
- Atmosphere source roles remain distinct: AQI/concentration, AOD/PM2.5, model/observation, forecast/observation, preliminary/regulatory, advisory/official authority, and low-cost sensor/corrected observation;
- KFM Atmosphere issues no emergency or life-safety direction;
- unknown rights, sensitivity, evidence, review, policy, release, correction, and rollback state fails closed;
- any future migration or retirement is accepted, validated, corrected, rollback-tested, and dependency-free.

A polished README alone does not satisfy implementation, enforcement, migration, release, publication, emergency-routing, or retirement closure.

<a id="20-safe-language-rules"></a>

## Safe language rules

| Avoid saying | Safer wording |
|---|---|
| “This folder contains Atmosphere catalog records.” | “This is a compatibility redirect; canonical Atmosphere catalog records belong under `data/catalog/domain/atmosphere/`.” |
| “Records here are valid or public.” | “Any material here is drift until reviewed; public exposure requires governed release and public-safe delivery.” |
| “AQI is PM2.5 concentration.” | “AQI is report/index context; concentration requires its own parameter, unit, method, averaging window, and evidence.” |
| “AOD is PM2.5.” | “AOD is a column optical proxy; a surface PM2.5 relationship requires an explicit validated model and uncertainty.” |
| “Forecast or model fields are observations.” | “Forecast, reanalysis, interpolation, and modeled fields retain model roles and time semantics.” |
| “This folder publishes advisories.” | “Advisory context preserves and redirects to the official issuer; KFM Atmosphere is not emergency authority.” |
| “CI blocks this.” | “Enforcement is `NEEDS VERIFICATION` unless a current required validator run proves it.” |
| “The README proves migration.” | “The README defines a proposed containment contract; migration needs inventory, disposition, validation, correction, and rollback evidence.” |

## No-loss ledger

| v0.2 material | v0.3.0 disposition |
|---|---|
| Stable path, `doc_id`, title role, creation date, and final newline | Preserved |
| Compatibility redirect and drift-control boundary | Preserved and strengthened |
| Evidence basis and canonical-home routing | Preserved, refreshed to a pinned base, linked, and expanded |
| Allowed and forbidden content rules | Preserved and normalized into the Directory Rules folder contract |
| Atmosphere object-family inventory | Preserved as bounded examples without implying implementation |
| AQI, AOD, model, forecast, preliminary, low-cost sensor, advisory, and emergency-authority guardrails | Preserved and strengthened |
| Directory shape and no-mirror rule | Preserved with an explicit inventory limitation |
| Minimum safe slice and anti-bypass matrix | Preserved and consolidated |
| Inspection, validation, and safe-change guidance | Preserved without unsafe executable shell snippets or unsupported pass claims |
| Migration, correction, rollback, and open verification items | Preserved and expanded |
| Definition-of-done and safe-language intent | Preserved and evidence-bounded |
| Numbered fragments `0` through `20` | Preserved through explicit legacy anchors |
| Payload, schema, policy, code, workflow, release, publication, or emergency behavior | Unchanged |

### Change history

#### v0.3.0 — 2026-07-24

- aligned the first twelve H2 sections with the Directory Rules §15 folder-README contract;
- preserved document identity, all numbered legacy anchors, and Atmosphere-specific content coverage;
- refreshed the evidence boundary to a pinned repository base and verified link targets;
- replaced decorative status claims with evidence-linked badges;
- strengthened source-role, non-life-safety, public-path, correction, and rollback boundaries;
- changed one Markdown file and no runtime, data, schema, policy, release, publication, or emergency-routing state.

<p align="right"><a href="#top">Back to top</a></p>
