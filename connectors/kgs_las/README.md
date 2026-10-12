<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kgs-las-readme
title: connectors/kgs_las/ — KGS LAS Compatibility and Migration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · KGS source steward · Package/migration maintainer · Geology steward · Hydrology steward · Rights reviewer · Privacy/sensitivity reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; compatibility-pointer; documentation-only; noncanonical-implementation-path; path-and-slug-conflict; digital-well-log-source; interpretation-anti-collapse; sensitive-well-locations; rights-fail-closed; no-code; no-descriptor; no-activation; no-publication
current_path: connectors/kgs_las/README.md
truth_posture: CONFIRMED README-only compatibility path, KGS product-family doctrine, absent proposed Kansas child, inert 0.0.0 KSGS scaffold, schema conflict, empty authority register, and exact target history / CONFLICTED final KGS connector path, kgs-versus-ksgs identity, LAS package placement, SourceDescriptor authority, and narrative-to-machine role mapping / PROPOSED redirect and migration contract / UNKNOWN live source access, current terms, executable parsing, fixtures, tests, CI enforcement, activation, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: a05b61a289cf5c87fb9d9173103c6d597a0c459d
  prior_blob: c78311310f49b2695e244d7d3ba3ffab78285b69
  readme_introduction_commit: 3a5acc266375392d2a03603a3d381cc673ed6466
related:
  - ../README.md
  - ../kgs/README.md
  - ../ksgs/README.md
  - ../ksgs/pyproject.toml
  - ../ksgs/src/README.md
  - ../ksgs/src/ksgs/README.md
  - ../ksgs/tests/README.md
  - ../geology/kgs/README.md
  - ../kansas/README.md
  - ../kgs_surficial/README.md
  - ../kgs_bedrock/README.md
  - ../kgs_oil_gas_wells/README.md
  - ../kgs_kdhe_wwc5/README.md
  - ../../CONTRIBUTING.md
  - ../../.github/CODEOWNERS
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../docs/sources/catalog/kansas/ksgs.md
  - ../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../docs/domains/geology/SOURCES.md
  - ../../docs/domains/hydrology/README.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../data/registry/sources/README.md
  - ../../control_plane/source_authority_register.yaml
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
  - ../../release/
tags: [kfm, connectors, kgs, ksgs, las, well-logs, well-tops, curves, subsurface, geology, hydrology, compatibility, migration, source-role, rights, sensitivity, raw, quarantine, no-publication]
notes:
  - "Direct repository inspection confirms connectors/kgs_las/ is README-only at the pinned base; exact pyproject.toml, src/README.md, and tests/README.md probes returned Not Found."
  - "The KGS source catalog treats LAS curves and picked well tops as distinct evidence types and requires independent SourceDescriptor, role, rights, sensitivity, vintage, and interpretation lineage."
  - "The proposed connectors/kansas/kgs/README.md path is absent, while connectors/ksgs/ is only a non-operational 0.0.0 scaffold and connectors/geology/kgs/ is a documentation-only compatibility pointer."
  - "The connector path and slug are therefore conflicted; this README does not select a canonical implementation home."
  - "Exact well, borehole, sample, log, and private-land locations fail closed; public upstream access is not KFM rights, sensitivity, or release clearance."
  - "Only this Markdown file is in scope. No code, descriptor, registry entry, fixture, test, policy, schema, workflow, source access, lifecycle artifact, path move, release object, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KGS LAS Compatibility and Migration Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft`  
> **Component maturity:** documentation-only compatibility pointer; executable LAS connector `ABSENT or UNKNOWN`  
> **Owner:** `OWNER_TBD`  
> **Truth posture:** `CONFIRMED` current README-only path and cited repository evidence · `CONFLICTED` final KGS/LAS path, package slug, descriptor authority, and machine role mapping · `PROPOSED` migration contract  
> **Boundary:** no live fetch, no package-local descriptor authority, no direct lifecycle persistence, no operational interpretation, no release, and no publication.

> [!CAUTION]
> A raw LAS curve, a picked formation top, an interpreted structural surface, and a regulatory record are not interchangeable. This lane must preserve the distinction between measured or recorded log content, human or algorithmic interpretation, modeled derivatives, administrative context, and downstream public-safe products.

**Quick links:** [Purpose](#purpose) · [Authority level](#authority-level) · [Current repository state](#current-repository-state) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [LAS boundaries](#las-log-curve-and-well-top-boundaries) · [Descriptor conflict](#sourcedescriptor-and-activation-conflict) · [Inputs and outputs](#inputs-and-outputs) · [Lifecycle](#lifecycle-and-handoff-boundary) · [Validation](#validation) · [Evidence](#evidence-basis) · [Review and rollback](#review-migration-and-rollback) · [Definition of done](#definition-of-done) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/kgs_las/` is an existing top-level compatibility path for historical or generated references to KGS LAS digital well logs and well tops.

Its purpose is deliberately narrow:

1. prevent this product-specific path from becoming an independent connector authority;
2. preserve the LAS-specific evidence, interpretation, depth, geometry, rights, and sensitivity boundaries that a future accepted connector must implement;
3. record the unresolved relationship among `connectors/kgs/`, `connectors/ksgs/`, proposed `connectors/kansas/kgs/`, `connectors/geology/kgs/`, and the top-level KGS product paths;
4. provide an auditable redirect, deprecation, or migration surface after a path decision is accepted.

This README does not prove that the current path should survive, that `kgs_las` is a valid final package or source ID, that the proposed Kansas child exists, that the KSGS scaffold is canonical, or that any LAS source is approved for access or admission.

[Back to top](#top)

---

## Authority level

**Documentation-only compatibility path; no source, schema, policy, evidence, lifecycle, or publication authority.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Responsibility root | **CONFIRMED** | Source-specific retrieval and admission implementation belongs under `connectors/`; contracts, schemas, registry, policy, evidence closure, release, and public delivery remain in their owning roots. |
| This path | **CONFIRMED / NONCANONICAL** | `connectors/kgs_las/README.md` exists; no executable package or test lane was found at named conventional paths. |
| Source-family meaning | **CONFIRMED draft doctrine** | The KGS source catalog recognizes LAS digital well logs and well tops as a distinct KGS sub-product requiring independent admission treatment. |
| Proposed Kansas child | **ABSENT AT PINNED BASE** | Exact read of `connectors/kansas/kgs/README.md` returned `Not Found`. |
| Live KSGS scaffold | **CONFIRMED / NON-OPERATIONAL** | `connectors/ksgs/` has project version `0.0.0`; its package files and tests are documented as placeholders or absent. |
| Domain-scoped KGS path | **CONFIRMED / DOCUMENTATION-ONLY** | `connectors/geology/kgs/` explicitly rejects domain-scoped connector implementation and records the canonical path as conflicted. |
| Final KGS connector path and slug | **CONFLICTED** | Repository evidence names or retains `kgs`, `ksgs`, proposed `kansas/kgs`, domain-scoped compatibility, and product-specific paths. No accepted decision in scope chooses one. |
| LAS implementation placement | **UNKNOWN / NEEDS VERIFICATION** | No accepted package, parser, product dispatcher, fixture suite, test suite, or activation record was verified. |
| Publication authority | **NONE** | This README emits no source material and authorizes no lifecycle transition or public output. |

Path presence is not authority. Product specificity is not permission to create another implementation island.

[Back to top](#top)

---

## Current repository state

The bounded snapshot below is pinned to repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `a05b61a289cf5c87fb9d9173103c6d597a0c459d`.

```text
connectors/
├── kgs_las/
│   ├── README.md                         # CONFIRMED; this compatibility boundary
│   ├── pyproject.toml                    # ABSENT by exact probe
│   ├── src/README.md                     # ABSENT by exact probe
│   └── tests/README.md                   # ABSENT by exact probe
├── kgs/
│   └── README.md                         # compatibility path
├── ksgs/
│   ├── pyproject.toml                    # project kfm-connector-ksgs, version 0.0.0
│   ├── src/ksgs/                         # inert greenfield scaffold
│   └── tests/README.md                   # documentation boundary
├── geology/kgs/
│   └── README.md                         # documentation-only compatibility pointer
└── kansas/
    ├── README.md                         # Kansas family coordination
    └── kgs/README.md                     # ABSENT by exact probe
```

| Surface | What current evidence proves | What it does not prove |
|---|---|---|
| [`connectors/kgs_las/`](./README.md) | README-only product compatibility lane at the pinned base. | Runtime, package, parser, source access, fixture, tests, activation, or release. |
| [`connectors/kgs/`](../kgs/README.md) | Top-level KGS compatibility documentation exists. | Canonical path or executable behavior. |
| [`connectors/ksgs/`](../ksgs/README.md) | A `0.0.0` implementation-shaped scaffold exists. | Accepted slug, working client/parser, valid descriptors, tests, activation, or maturity. |
| [`connectors/geology/kgs/`](../geology/kgs/README.md) | Domain-scoped compatibility pointer exists and rejects implementation there. | Final source-first path. |
| `connectors/kansas/kgs/README.md` | Exact path was checked. | File was not found; absence does not select another path. |

Absence claims are limited to the exact paths at the pinned commit. Differently named, generated, unindexed, or later-added files remain `UNKNOWN`.

[Back to top](#top)

---

## What belongs here

Until migration is accepted, content in this path should remain limited to:

- this README;
- an approved redirect, deprecation notice, or compatibility-import note;
- references to the accepted KGS connector, product descriptor, source registry, tests, and migration record;
- bounded LAS-specific warnings needed to prevent evidence, interpretation, depth, geometry, rights, sensitivity, and public-use collapse;
- a migration receipt, supersession reference, or rollback pointer after governed path resolution.

A future accepted migration may reduce this folder to a short redirect or remove it through a transparent, history-preserving change.

---

## What does not belong here

Do not add the following without an accepted ADR or migration that explicitly retains this path:

- live KGS clients, downloaders, crawlers, sessions, credentials, or scheduled watchers;
- LAS, DLIS, image-log, well-top, curve, raster, tabular, or archive parsers;
- package metadata, import namespaces, product dispatchers, caches, staging files, or source payloads;
- authoritative `SourceDescriptor` instances, source-authority entries, activation decisions, or source-role vocabularies;
- canonical contracts, JSON Schemas, policy bundles, redaction rules, or release rules;
- real well, borehole, log, sample, owner, lease, parcel, or exact-location fixtures;
- direct writers to RAW, QUARANTINE, WORK, PROCESSED, CATALOG, TRIPLET, receipts, proofs, release, rollback, or PUBLISHED roots;
- reservoir, drilling, completion, production, engineering, groundwater-supply, hazard, investment, regulatory, or life-safety advice;
- public maps, cross-sections, logs, APIs, dashboards, exports, search indexes, graph edges, or AI answers;
- generated summaries presented as measured log evidence, interpreted geology, hydrology truth, KCC regulatory status, or public-release approval.

Use each owning responsibility root after placement is resolved.

[Back to top](#top)

---

## LAS log, curve, and well-top boundaries

The KGS source catalog treats LAS digital logs and well tops as one publisher sub-product family, but not as one homogeneous evidence class.

| Evidence class | Typical source-document posture | Identity and context that must survive | Must not be treated as |
|---|---|---|---|
| **Well/log container** | Source package or file context | KGS source/product ID, well identity, API/UWI or source-native identifier where present, file/log identity, source URI, checksum, retrieval time, vintage, rights, disclaimer. | A curve observation, formation interpretation, current well condition, or release grant. |
| **Raw or recorded log curve** | `observed` candidate in narrative doctrine | Curve mnemonic and original name, units, null value, depth index, depth unit, depth reference/datum, sampling interval, service/company provenance where lawful, source-native values, quality flags. | A picked top, lithologic truth, stratigraphic boundary, reservoir estimate, or regulatory determination. |
| **Picked well top** | Interpretation or modeled/context candidate | Interpreter or source, method, formation/unit label, pick depth, depth reference, uncertainty, confidence, vintage, supersession, source-log references. | A measured sensor curve, universally accepted boundary, canonical stratigraphy, or observed surface. |
| **Derived structural surface or cross-section input** | `modeled` or derived context candidate | Model/run identity, input picks, interpolation method, CRS/datum, vertical datum, uncertainty, vintage, `ModelRunReceipt` or accepted equivalent. | Raw observation, exact subsurface truth, reserve/resource estimate, or drilling guidance. |
| **Well-header or administrative metadata** | Administrative/context candidate | Field/lease/well identifiers, status source, time, publisher, crosswalks, geometry source and uncertainty. | KCC permit/authorization, completion truth, production fact, or unrestricted private-location data. |

Required anti-collapse rules:

1. preserve well, file, log, curve, pick, interpretation, and model identities separately;
2. preserve measured depth, true vertical depth, depth reference, datum, units, null conventions, and uncertainty without silent conversion;
3. preserve original curve mnemonics and source-native units alongside any normalized representation;
4. do not present a picked top as a measured observation;
5. do not present an interpolated structural surface as direct subsurface observation;
6. do not relabel KGS records as KCC regulatory determinations, KDHE environmental findings, WWC5 completion truth, or operator engineering data;
7. mixed packages must split by evidence class and source role or fail closed;
8. corrections and reinterpretations create explicit supersession lineage rather than overwriting prior picks;
9. maps, sections, summaries, joins, graph projections, and AI explanations remain downstream carriers.

[Back to top](#top)

---

## SourceDescriptor and activation conflict

No connector-local descriptor exists in this README-only lane, and the current repository does not provide a settled machine authority for minting one here.

| Authority surface | Confirmed inspected posture | Consequence |
|---|---|---|
| [`docs/sources/catalog/kansas/ksgs.md`](../../docs/sources/catalog/kansas/ksgs.md) | Draft human-facing source catalog; requires separate descriptors for KGS sub-products and distinguishes raw LAS curves, picked tops, modeled surfaces, and KCC regulatory records. | Strong source-meaning guidance, not machine activation authority. |
| [`contracts/source/source_descriptor.md`](../../contracts/source/source_descriptor.md) | Draft semantic contract for a rich `SourceDescriptor`. | Defines intended meaning, but remains proposed and does not activate LAS. |
| [`schemas/contracts/v1/source/source_descriptor.schema.json`](../../schemas/contracts/v1/source/source_descriptor.schema.json) | Populated closed schema that labels the plural path canonical and itself legacy. | Provides substantive constraints but exposes unresolved schema-home migration. |
| [`schemas/contracts/v1/sources/source_descriptor.schema.json`](../../schemas/contracts/v1/sources/source_descriptor.schema.json) | Empty `PROPOSED` scaffold accepting arbitrary properties. | Cannot provide meaningful validation. |
| [`control_plane/source_authority_register.yaml`](../../control_plane/source_authority_register.yaml) | `PROPOSED` with `entries: []`. | No LAS source authority or activation entry is established. |
| Rights and sensitivity policy READMEs | Greenfield stubs. | No executable LAS rights, sensitive-location, or public-precision policy is proven. |

The source catalog uses narrative role words such as `observed`, `context`, and `modeled`; the populated machine schema uses a different controlled vocabulary. No accepted mapping was found in scope.

Therefore:

- do not create one publisher-wide KGS descriptor for every LAS/log/top product;
- do not infer a machine role from prose or filename;
- do not infer rights, redistribution, sensitivity, or public geometry from upstream availability;
- do not activate transport or parsing without a conforming product-specific descriptor and explicit activation decision;
- do not store authoritative descriptors or activation decisions in this compatibility folder;
- do not treat a descriptor as proof that a log interpretation is true or public-safe.

[Back to top](#top)

---

## Inputs and outputs

### Current inputs

None. This path declares no function, class, command, configuration, endpoint, host allowlist, credential variable, parser shape, fixture format, or sink interface.

### Current outputs

None. This path emits no source bytes, source-head observation, parse result, candidate envelope, receipt, validation report, RAW object, QUARANTINE object, EvidenceBundle, catalog record, or public artifact.

### Future admissible inputs

Only after placement and governance decisions close, an accepted LAS connector may receive:

- a conforming, reviewed, product-specific `SourceDescriptor` reference;
- an explicit activation decision for fixture-only, restricted, or approved live operation;
- an approved KGS source endpoint, archive, file, service, or steward-mediated input;
- source-native well, file, log, curve, top, and model identifiers;
- source-head evidence such as version, release date, checksum, `ETag`, `Last-Modified`, or documented manual identity;
- rights, terms, attribution, redistribution, disclaimer, sensitivity, geometry, and reviewer references;
- run identity plus retrieval, source, observed, interpreted, valid/effective, release, and correction time where applicable;
- synthetic, minimized, or rights-cleared fixtures that cannot disclose a real sensitive location;
- caller-owned candidate-output interfaces.

### Future admissible outputs

A future accepted implementation may return, without direct persistence:

- deterministic source-head/probe results;
- parse results preserving source-native values and evidence class;
- structured validation or interpretation-lineage failures;
- a `RAW` handoff candidate when identity, rights, role, sensitivity, source head, depth context, geometry, and activation are resolved;
- a `QUARANTINE` handoff candidate with a bounded reason when they are not;
- a process-memory retrieval, denial, no-op, or handoff receipt candidate when an accepted receipt contract exists.

It must not select release, persist directly to lifecycle roots, create evidence closure, expose exact sensitive geometry, or convert parse success into geological truth.

[Back to top](#top)

---

## Lifecycle and handoff boundary

The governing lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This compatibility README performs no lifecycle transition.

A future connector may only produce caller-owned `RAW` or `QUARANTINE` **candidates** after descriptor and activation checks. It must not normalize canonical domain objects, assemble EvidenceBundles, emit catalog/triplet truth, create release manifests, generalize public geometry, or publish.

Minimum quarantine conditions include:

- unresolved connector path, package/import name, source ID, or product identity;
- missing, invalid, unreviewed, superseded, or inactive descriptor;
- unknown source shape, unsupported LAS version, malformed header, or source-head mismatch;
- unresolved rights, attribution, redistribution, disclaimer, or sensitivity;
- missing well/log/curve/top identity or source-native references;
- lost or ambiguous depth index, units, datum, reference, null value, or sampling interval;
- picked top lacking interpretation provenance, method, confidence, or supersession state;
- derived surface lacking model/run lineage, inputs, method, or uncertainty;
- geometry without source, derivation, uncertainty, withholding, or public-precision state;
- attempted lifecycle persistence, public output, operational advice, or sensitive payload echo.

Unknowns receive `DENY`, `ABSTAIN`, `HOLD`, `ERROR`, or a `QUARANTINE` candidate—never a permissive default.

[Back to top](#top)

---

## Validation

No package build, install, import, parser, or test command is documented because no package or executable test lane was verified at this path.

Before implementation maturity can be claimed, evidence must cover:

1. accepted KGS connector path, product topology, package/import/source-ID convention, and losing-path migration;
2. complete package, fixture, test, workflow, and backlink inventory;
3. build backend, package discovery, supported Python versions, dependencies, commands, and clean install/import;
4. accepted `SourceDescriptor` schema authority and narrative-to-machine role mapping;
5. product-specific descriptors, review state, rights/sensitivity decisions, source heads, and activation decisions;
6. current KGS LAS/log/top access methods, formats, versions, terms, attribution, redistribution, disclaimers, cadence, and correction behavior;
7. no-network defaults plus host, credential, timeout, retry, response-size, archive, decompression, and payload-logging controls;
8. LAS header, well identity, curve mnemonic, unit, null, depth index, datum/reference, interval, encoding, and malformed-input tests;
9. picked-top interpretation, confidence, uncertainty, source-log, supersession, and raw-vs-interpreted anti-collapse tests;
10. derived-surface model lineage, interpolation, CRS/vertical-datum, input-pick, uncertainty, and observed-vs-modeled tests;
11. exact-location, private-well, owner/parcel, PLSS-derived geometry, withholding, and public-precision negative cases;
12. KGS/KCC/KDHE/WWC5 and log/top/surface role-separation tests;
13. deterministic `RAW`/`QUARANTINE` candidate, denial, no-op, idempotency, and lifecycle-boundary tests;
14. substantive package-specific CI discovery and negative coverage;
15. correction, reinterpretation, supersession, deactivation, migration, and rollback tests.

Documentation checks for this revision should include one H1, balanced fences, valid repository-relative links, no remote badge/image dependency, no credential-like values, a final newline, and an exact one-file diff.

[Back to top](#top)

---

## Evidence basis

Evidence is bounded to the pinned repository state and named exact probes.

| Evidence | Status | Supports | Does not support |
|---|---|---|---|
| Target README and history | **CONFIRMED** | Prior blob `c78311310f49b2695e244d7d3ba3ffab78285b69`; initial substantive README commit `3a5acc266375392d2a03603a3d381cc673ed6466`. | Runtime, source access, rights, tests, or activation. |
| Exact target-child probes | **CONFIRMED absent at base** | No named `pyproject.toml`, `src/README.md`, or `tests/README.md` under this lane. | Permanent nonexistence or absence of differently named files. |
| [`connectors/geology/kgs/README.md`](../geology/kgs/README.md) | **CONFIRMED v0.2** | Current path/slug conflict, source-first rule, product decomposition, and sensitive-well boundary. | Accepted canonical source path. |
| [`connectors/ksgs/`](../ksgs/README.md) | **CONFIRMED scaffold** | Current implementation-shaped placeholder and unresolved `kgs`/`ksgs` identity. | Executable LAS behavior or canonicality. |
| [`docs/sources/catalog/kansas/ksgs.md`](../../docs/sources/catalog/kansas/ksgs.md) | **CONFIRMED draft** | LAS/log/top product identity, role anti-collapse, rights, sensitivity, and source-family context. | Current endpoint, valid machine role, descriptor admission, or activation. |
| `SourceDescriptor` contract and schemas | **CONFIRMED draft/PROPOSED** | Rich descriptor requirements, fail-closed constraints, and current schema-path conflict. | Accepted migration or persisted LAS descriptor. |
| Source-authority register | **CONFIRMED empty** | `entries: []`. | Any KGS/LAS activation. |
| Rights and sensitivity policy READMEs | **CONFIRMED stubs** | Current greenfield policy state. | Executable product policy. |
| Exact `connectors/kansas/kgs/README.md` probe | **CONFIRMED absent at base** | Proposed child was not present. | Final path decision. |

Not inspected: live KGS services, current terms pages, credentials, LAS payloads, well records, exact coordinates, proprietary log data, parser runs, runtime logs, emitted receipts, EvidenceBundles, release manifests, deployments, or public clients. Treat associated claims as `UNKNOWN` or `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Review, migration, and rollback

Review changes here as connector-placement, package/import identity, source-product identity, measured-vs-interpreted evidence, depth/datum, rights, sensitivity, private-location, security, and lifecycle-boundary changes—even when the diff is documentation-only.

A later migration must preserve or explicitly supersede:

- Git and documentation history;
- package/import compatibility and deprecation behavior;
- KGS product/source IDs and descriptor references;
- source-head, retrieval, well, log, curve, pick, interpretation, and model lineage;
- fixtures, tests, workflows, and negative cases;
- receipts, candidate-envelope references, catalog/evidence backlinks, and correction state;
- rights, disclaimers, sensitivity, geometry, uncertainty, withholding, review, release, and withdrawal state;
- rollback to the last known safe documentation and package state.

Rollback this README revision if it is used to:

- treat this path or another path as canonical without an accepted decision;
- create or activate a package, descriptor, registry record, or source from documentation alone;
- infer public rights or safe precision from upstream access;
- claim working fetch, parsing, interpretation, fixtures, tests, CI, or lifecycle output without evidence;
- collapse curves, tops, structural surfaces, well headers, WWC5 records, KCC records, or generated summaries;
- expose exact well, borehole, sample, private-land, or sensitive subsurface detail;
- provide operational drilling, engineering, resource, groundwater-supply, regulatory, investment, hazard, or safety advice;
- bypass descriptor, activation, evidence, rights, sensitivity, policy, review, release, correction, or rollback gates.

Before merge, close the draft change and abandon the branch if rejected. After merge, create a transparent revert of the documentation commit, restoring prior blob `c78311310f49b2695e244d7d3ba3ffab78285b69` from base `a05b61a289cf5c87fb9d9173103c6d597a0c459d`. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Definition of done

### Documentation boundary

- [x] Current README-only state and exact named absences are explicit.
- [x] Final KGS path, slug, and package placement remain visibly conflicted.
- [x] LAS curves, well tops, derived surfaces, headers, and regulatory records are not collapsed.
- [x] SourceDescriptor/schema authority and role-vocabulary conflict are explicit.
- [x] Rights, disclaimer, depth/datum, exact-location, uncertainty, interpretation, and public-use boundaries are explicit.
- [x] Current inputs, outputs, runtime, tests, activation, lifecycle behavior, and publication are stated as absent or unknown.
- [x] Evidence limits, migration discipline, and rollback target are recorded.

### Implementation readiness

- [ ] Accepted KGS connector path, package/import/source-ID strategy, and product topology exist.
- [ ] Losing paths are redirected, deprecated, migrated, or removed with preserved history and rollback.
- [ ] Owners and required reviewers are assigned.
- [ ] Build, install, API, dependency, configuration, and command contracts are implemented.
- [ ] SourceDescriptor authority and narrative-to-machine role mapping are accepted.
- [ ] Product-specific LAS/log/top descriptors, rights/sensitivity reviews, source heads, and activation decisions exist.
- [ ] Current KGS access, formats, versions, terms, attribution, redistribution, disclaimers, cadence, corrections, and withdrawals are reviewed.
- [ ] Curve, depth, datum, top interpretation, model lineage, geometry, uncertainty, withholding, and sensitive-location policy is executable.
- [ ] Default tests are offline, deterministic, synthetic or rights-cleared, negative-first, and CI-discovered.
- [ ] Correction, reinterpretation, supersession, migration, deactivation, and rollback are tested.

Until every applicable implementation-readiness item closes, keep this path documentation-only and fail closed.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Final KGS connector path and `kgs`/`ksgs` slug. | **CONFLICTED** | Accepted ADR or migration decision plus repository implementation. |
| LAS package/import/source-ID placement. | **NEEDS VERIFICATION** | Accepted package layout, references, tests, and compatibility plan. |
| Current KGS LAS/log/top access surfaces and formats. | **NEEDS VERIFICATION** | Source-steward review, current official documentation, and source-head probes. |
| Product-specific terms, attribution, redistribution, and disclaimers. | **NEEDS VERIFICATION** | Rights review and descriptor evidence. |
| Machine role mapping for curves, tops, surfaces, and headers. | **CONFLICTED** | Accepted vocabulary/crosswalk and validator tests. |
| SourceDescriptor schema authority. | **CONFLICTED** | Accepted schema-home migration or ADR and substantive validation. |
| Sensitive well/log geometry and public precision. | **NEEDS VERIFICATION** | Executable policy, fixtures, redaction/generalization tests, and review records. |
| Parser/API/DTO/reason-code contracts. | **UNKNOWN** | Implemented code, contracts, schemas, and tests. |
| Fixtures and CI discovery. | **UNKNOWN** | Synthetic/rights-cleared fixtures, test inventory, workflow execution, and logs. |
| Release, correction, withdrawal, and rollback closure. | **UNKNOWN** | EvidenceBundle, policy/review records, release manifest, correction path, and rollback drill. |

[Back to top](#top)
