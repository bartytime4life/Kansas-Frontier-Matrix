<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kgs-las-readme
title: connectors/kgs_las/ — KGS LAS Documentation-Only Compatibility Lane
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · KGS source steward · Geology steward · Hydrology steward · Rights reviewer · Privacy/sensitivity reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; compatibility-pointer; documentation-only; noncanonical-implementation-path; path-and-slug-conflict; digital-well-log-source; product-specific-roles; rights-fail-closed; sensitive-subsurface-locations; no-code; no-descriptor; no-activation; no-publication
current_path: connectors/kgs_las/README.md
truth_posture: CONFIRMED README-only top-level product compatibility lane, exact absent package and test probes, proposed Kansas child absent, live non-operational KSGS scaffold, KGS source catalog, Geology well-log pipeline documentation, empty source-authority register, schema conflict, and TODO-only connector workflows / CONFLICTED final KGS connector path, kgs-versus-ksgs identity, LAS product placement, SourceDescriptor authority, narrative-to-machine source-role mapping, registry and test homes / PROPOSED redirect, migration, and future source-admission boundary / UNKNOWN source access, rights, activation, runtime, fixtures, executable tests, substantive CI, deployment, and release readiness
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
  - ../ksgs/src/ksgs/README.md
  - ../geology/kgs/README.md
  - ../kansas/README.md
  - ../../CONTRIBUTING.md
  - ../../.github/CODEOWNERS
  - ../../.github/workflows/connector-gate.yml
  - ../../.github/workflows/source-descriptor-validate.yml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../docs/sources/catalog/kansas/ksgs.md
  - ../../docs/domains/geology/sublanes/boreholes-wells.md
  - ../../pipelines/domains/geology/well_logs/README.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../data/registry/sources/geology/README.md
  - ../../control_plane/source_authority_register.yaml
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
  - ../../release/
tags: [kfm, connectors, kgs, ksgs, las, well-logs, well-tops, boreholes, subsurface, geology, hydrology, compatibility, path-conflict, source-admission, source-role, rights, sensitivity, no-network, raw, quarantine, no-publication]
notes:
  - "Direct reads at base commit a05b61a289cf5c87fb9d9173103c6d597a0c459d confirm connectors/kgs_las/README.md and no named pyproject.toml, src/README.md, or tests/README.md below this path."
  - "The KGS catalog proposes connectors/kansas/kgs/, but an exact read at the pinned base returned Not Found. The live connectors/ksgs/ path is a non-operational 0.0.0 scaffold, and connectors/geology/kgs/ is a documentation-only compatibility pointer."
  - "LAS curves, well-top interpretations, modeled structural surfaces, WWC5 completion records, KCC regulatory records, production aggregates, and generated summaries remain distinct source/product/role classes."
  - "Exact well, borehole, core, sample, private-well, proprietary-log, and infrastructure-adjacent locations fail closed. Source access or upstream public availability is not KFM rights, sensitivity, evidence, or release clearance."
  - "The machine source-authority register contains entries: []; the populated singular SourceDescriptor schema labels the plural path canonical while the plural schema is an empty PROPOSED scaffold; narrative and machine role vocabularies remain unratified."
  - "Only this Markdown file is in scope. No connector code, package metadata, descriptor, registry record, fixture, test, workflow, policy, schema, source payload, activation decision, lifecycle artifact, release object, path move, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KGS LAS Documentation-Only Compatibility Lane

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Component maturity:** README-only compatibility surface; no package, source client, parser, descriptor, fixture, executable test, or lifecycle handoff is established here  
> **Path posture:** `connectors/kgs_las/` exists, but final KGS connector, package, product, registry, fixture, and test placement remain `CONFLICTED`  
> **Authority:** documentation and migration context only; no source, schema, policy, evidence, lifecycle, release, or publication authority.

> [!WARNING]
> A product name, directory, source catalog statement, public well-log page, LAS file, interpreted top, placeholder registry, or green TODO-only workflow is not implementation or publication evidence. KGS LAS access and activation remain denied until placement, product identity, rights, sensitivity, source role, source head, fixtures, tests, policy, and release gates are actually closed.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#current-repository-state) · [Placement conflict](#placement-package-and-product-conflict) · [Product boundaries](#las-well-log-and-well-top-boundaries) · [Descriptor conflict](#descriptor-registry-and-policy-boundary) · [Sensitivity](#sensitivity-rights-and-public-use-boundary) · [Inputs and outputs](#inputs-and-outputs) · [Compatibility contract](#compatibility-and-future-implementation-boundary) · [Failure contract](#failure-contract) · [Validation](#validation) · [Evidence](#evidence-basis) · [Rollback](#review-migration-and-rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/kgs_las/` is a repository-present, top-level KGS product compatibility path. Its safe current role is to prevent historical or generated LAS references from becoming a second connector implementation or a publisher-wide authority surface.

This README may:

- record the current README-only state;
- redirect future implementation toward one accepted source-first KGS connector topology;
- preserve LAS, well-log, curve, well-top, well, borehole, source-role, rights, depth, datum, unit, geometry, uncertainty, vintage, and disclaimer distinctions;
- document the relationship among this path, `connectors/kgs/`, `connectors/ksgs/`, `connectors/geology/kgs/`, and proposed `connectors/kansas/kgs/`;
- define migration, review, validation, deprecation, and rollback requirements;
- keep exact subsurface and private-location material fail closed;
- prevent a retrieved LAS file or picked top from becoming public geology, hydrology, resource, regulatory, engineering, or safety truth.

This README does not:

- select the canonical KGS connector path, distribution, import name, source ID, or LAS product slug;
- prove any executable connector, source endpoint, account, credential mode, parser, fixture, test, workflow enforcement, or deployment;
- activate KGS LAS, KGS well tops, or any related KGS product;
- define a canonical `SourceDescriptor`, schema, source-role mapping, rights decision, sensitivity policy, or release decision;
- permit direct lifecycle persistence, EvidenceBundle creation, catalog/triplet emission, public API delivery, map publication, or AI authority.

Directory Rules assign source-specific fetch and admission mechanics to `connectors/`, while source doctrine, registry entries, schemas, policy, evidence closure, pipelines, release, and public delivery remain in their owning responsibility roots.

[Back to top](#top)

---

## Authority level

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Owning responsibility root | **CONFIRMED** | `connectors/` owns source-specific fetch, probe, preservation, and admission mechanics. |
| Current path | **CONFIRMED / NONCANONICAL** | `connectors/kgs_las/README.md` exists as a product compatibility surface. Path presence does not grant implementation authority. |
| Content below this path | **README-ONLY AT NAMED PROBES** | Exact reads found no `pyproject.toml`, `src/README.md`, or `tests/README.md`. Differently named or unindexed files remain `UNKNOWN`. |
| Final KGS connector path | **CONFLICTED** | Repository surfaces include `connectors/kgs/`, `connectors/ksgs/`, `connectors/geology/kgs/`, proposed-but-absent `connectors/kansas/kgs/`, and several top-level KGS product paths. |
| KGS package runtime | **NON-OPERATIONAL SCAFFOLD ELSEWHERE** | `connectors/ksgs/` contains a `0.0.0` placeholder package documented as noncanonical; it does not establish LAS behavior or canonical placement. |
| LAS product implementation | **NOT ESTABLISHED** | No client, parser, product dispatcher, fixture, executable test, activation record, or source head is proved by this lane. |
| Geology well-log processing | **DOCUMENTED DOWNSTREAM LANE** | `pipelines/domains/geology/well_logs/README.md` defines a downstream processing boundary. Its existence does not prove executable code or authorize this connector. |
| Machine source authority | **NOT ESTABLISHED** | The inspected source-authority register is `PROPOSED` with `entries: []`. |
| SourceDescriptor authority | **CONFLICTED** | The populated singular-path schema declares the plural path canonical; the plural path is an empty permissive scaffold. |
| Rights and sensitivity policy | **NEEDS VERIFICATION / FAIL CLOSED** | Current terms, redistribution, attribution, exact-location handling, proprietary-log posture, and public precision require product-specific review. |
| Connector CI | **TODO-ONLY FOR NAMED WORKFLOWS** | `connector-gate` and `source-descriptor-validate` currently execute `echo TODO ...`; green status cannot prove behavior or governance. |
| Publication authority | **NONE** | This compatibility folder emits no source record, evidence object, lifecycle object, release, map, API response, or public claim. |

No new authority may be built in this path merely because it is present. A future retained implementation requires an accepted placement and migration decision plus product-specific governance.

[Back to top](#top)

---

## Current repository state

This bounded snapshot is pinned to repository `bartytime4life/Kansas-Frontier-Matrix` at commit `a05b61a289cf5c87fb9d9173103c6d597a0c459d`.

```text
connectors/
├── kgs_las/
│   └── README.md                         # CONFIRMED; this compatibility boundary
├── kgs/
│   └── README.md                         # top-level compatibility README
├── ksgs/
│   ├── README.md                         # noncanonical 0.0.0 scaffold boundary
│   ├── pyproject.toml                    # kfm-connector-ksgs, version 0.0.0
│   ├── src/ksgs/                         # placeholder package scaffold
│   └── tests/README.md                   # test documentation boundary
├── geology/kgs/
│   └── README.md                         # documentation-only compatibility pointer
└── kansas/
    ├── README.md                         # Kansas source-family coordination
    └── kgs/README.md                     # ABSENT by exact probe
```

Exact reads under `connectors/kgs_las/` returned `Not Found` for:

```text
connectors/kgs_las/pyproject.toml
connectors/kgs_las/src/README.md
connectors/kgs_las/tests/README.md
```

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| This README | Prior v0.1 compatibility document; prior blob `c78311310f49b2695e244d7d3ba3ffab78285b69`. | Documentation can be corrected without implying runtime change. |
| `connectors/kgs/README.md` | Older compatibility document still states more canonical-path certainty than current repository evidence supports. | Useful lineage, not final path authority. |
| `connectors/geology/kgs/README.md` | Newer v0.2 compatibility pointer explicitly records the KGS path conflict and rejects domain-scoped implementation. | Strong current path-conflict evidence. |
| `connectors/ksgs/` | Repository-present `0.0.0` scaffold with placeholder code and metadata, documented as noncanonical. | Does not establish LAS implementation, activation, or final naming. |
| Proposed `connectors/kansas/kgs/` | Exact README read returned `Not Found`. | Keep the path `PROPOSED`; absence does not select a different winner. |
| `pipelines/domains/geology/well_logs/README.md` | Downstream well-log processing contract exists. | Does not prove executable pipeline behavior or connector placement. |
| KGS source catalog | Draft catalog identifies LAS digital well logs and well tops as a distinct KGS sub-product. | Human-facing doctrine; not machine activation or rights clearance. |
| Source authority register | `PROPOSED`, `entries: []`. | No KGS LAS activation or authority entry. |
| Connector workflows | TODO-only echo steps. | No substantive connector, descriptor, rights, sensitivity, or lifecycle enforcement. |

This snapshot is not a recursive tree receipt. Any broader presence or absence claim must be regenerated at the commit under review.

[Back to top](#top)

---

## Placement, package, and product conflict

The responsibility root is clear: source-specific access belongs under `connectors/`. The exact KGS source-first path and packaging are not.

| Candidate surface | Current posture | Decision this README makes |
|---|---|---|
| `connectors/kgs_las/` | README-only top-level product compatibility lane. | Retain as documentation only; do not add runtime behavior without an accepted migration. |
| `connectors/kgs/` | README-only top-level source compatibility lane. | Does not automatically become canonical. |
| `connectors/ksgs/` | Only implementation-shaped `0.0.0` scaffold; explicitly noncanonical and non-operational. | Does not automatically absorb LAS or settle `kgs` versus `ksgs`. |
| `connectors/geology/kgs/` | Documentation-only domain-scoped compatibility pointer. | Not an implementation home. |
| `connectors/kansas/kgs/` | Proposed by the source catalog; exact child README absent. | Keep `PROPOSED`; do not claim current implementation. |
| `pipelines/domains/geology/well_logs/` | Downstream transformation responsibility. | Must not fetch source data or decide connector placement. |

A future migration must settle, in one reviewable plan:

1. canonical connector path;
2. distribution and import names;
3. product/source-ID convention;
4. whether LAS is a dispatcher under one KGS package or a separately named product module;
5. losing-path redirect/deprecation behavior;
6. descriptor, activation, fixture, test, workflow, and credential ownership;
7. source-head, receipt, correction, supersession, and rollback continuity;
8. documentation and backlink updates.

This README does not select a winner and does not create an ADR by implication.

[Back to top](#top)

---

## LAS, well-log, and well-top boundaries

KGS LAS and well-top material is not one interchangeable data surface. Product and record identity must survive admission and every downstream transform.

| Material class | Source-document role posture | Required preservation | Denied collapse |
|---|---|---|---|
| **LAS file and source headers** | Source-native digital-log payload and metadata | Publisher/product identity, well/borehole identity, file/source ID, source URI, retrieval time, source head, LAS/header metadata, rights, checksum, and vintage | File availability treated as public-release permission or proof of log validity |
| **Raw or submitted curves** | `observed`-like measurement record in current source docs | Curve mnemonic and description, units, sampling interval, null value, depth index, source-native values, tool/run context where available, and quality flags | Curve treated as interpreted formation top, continuous stratigraphy, reserve, production, or regulatory status |
| **Well-top or formation pick** | Interpretation/context in current source docs | Pick identity, interpreter/source, formation/unit identity, depth, depth reference, datum, uncertainty, method, source curves/log refs, and revision lineage | Pick treated as direct measurement or unquestioned canonical geology |
| **Modeled structural or stratigraphic surface** | `modeled` derivative | Model/run identity, algorithm/method, input picks, interpolation/support, uncertainty, spatial resolution, validation, and model receipt | Modeled surface labeled observed or used as operational drilling truth |
| **Scanned log or image surrogate** | Historical/source surrogate | Original item identity, image/OCR relation, scan quality, page/frame identity, rights, and transcription/OCR uncertainty | OCR or image extraction presented as verified curve data without review |
| **WWC5 completion record** | Per-well completion observation/context | Joint-program identity, completion fields, PLSS derivation, coordinate uncertainty, dates, disclaimer, and source role | Water-well record treated as oil/gas log, production evidence, current water quality, or safe-supply conclusion |
| **KCC filing or permit record** | Regulatory/legal context owned by KCC | KCC source identity, instrument/filing identity, status/effective time, and citation | KCC regulatory posture relabeled KGS geologic observation, or KGS observation relabeled permit approval |
| **Oil/gas production aggregate** | Aggregate/reporting record | Reporting scope, lease/field/county identity, time period, units, source role, and aggregation receipt | Aggregate attached to one well as per-well production truth |
| **Generated summary or AI explanation** | Downstream interpretation only | Resolved evidence refs, policy decision, release state, citations, uncertainty, and finite outcome | Generated language treated as source record, EvidenceBundle, or operational advice |

Required anti-collapse rules:

1. preserve one stable identity for each source file, well/borehole, log, curve, pick, model, and release;
2. distinguish measured depth, true vertical depth, elevation, datum, and unknown depth reference rather than converting silently;
3. preserve source units and explicit conversion receipts; do not infer units from a mnemonic alone;
4. preserve source-native null/sentinel values and transform them only through documented normalization;
5. do not turn one top pick into a continuous surface without a model/run artifact and uncertainty;
6. do not turn a public KGS page into rights or redistribution clearance;
7. do not conflate KGS observation/context with KCC regulatory or legal authority;
8. do not conflate WWC5, LAS, production, bedrock maps, surficial maps, or Geoportal resources under one role or descriptor;
9. keep maps, tiles, cross-sections, graphs, summaries, and AI answers downstream of evidence, policy, review, and release.

[Back to top](#top)

---

## Descriptor, registry, and policy boundary

No authoritative descriptor belongs in this compatibility folder.

The inspected `SourceDescriptor` contract and populated singular-path schema require a rich, closed object covering source identity and version, source type and role, authority rank, publisher and steward, rights, sensitivity, cadence, access, citation, source-head evidence, admissibility limits, public-release posture, review state, release state, and lifecycle state.

Current machine authority remains conflicted:

- the populated singular schema labels `schemas/contracts/v1/sources/source_descriptor.schema.json` canonical and itself legacy;
- the plural schema is an empty `PROPOSED` scaffold with no meaningful field validation;
- source documents use role terms such as `observed`, `context`, `modeled`, `aggregate`, `administrative`, and `candidate`;
- the populated schema uses a different controlled vocabulary such as `observation`, `regulatory_context`, `model_context`, and `candidate_signal`;
- no accepted narrative-to-machine role mapping was verified;
- the source-authority register contains no entries;
- current rights and sensitivity README surfaces are greenfield stubs or otherwise do not prove LAS-specific decisions;
- the named connector and descriptor workflows run TODO-only echo steps.

Therefore:

- do not create one agency-wide KGS descriptor for all products;
- do not load a README, LAS file header, product page, or generated template as activation authority;
- do not assign a machine source role by copying narrative text;
- do not infer rights, redistribution, public precision, or release from upstream accessibility;
- do not place authoritative descriptor records, activation decisions, or policy rules in this path;
- do not enable network transport until the exact product descriptor, source head, terms review, sensitivity review, and activation decision are accepted;
- do not treat any descriptor as proof that a curve, top, model, or summary is true or released.

[Back to top](#top)

---

## Sensitivity, rights, and public-use boundary

KGS well-log and well-top material can expose or help reconstruct:

- exact wells, boreholes, cores, samples, and subsurface resource locations;
- private-water-well or landholder-linked information;
- proprietary, licensed, restricted, or account-gated logs;
- infrastructure-adjacent and active extraction locations;
- detailed depth, formation, interval, and resource signals;
- harmful cross-source joins among wells, parcels, owners, production, infrastructure, or environmental records.

Default rules:

- unknown or unverified rights deny public release;
- a publicly reachable source does not establish redistribution permission;
- exact or withheld geometry must not be reconstructed from PLSS fields, logs, exceptions, caches, fixtures, screenshots, indexes, model output, or cross-source joins;
- PLSS-derived coordinates retain derivation level and uncertainty and must not be presented as surveyed precision;
- source-native geometry, precision, uncertainty, withholding state, and private/public geometry intent must remain explicit;
- fixtures must be synthetic, minimized, rights-cleared, non-operational, and incapable of identifying a real sensitive location;
- errors, logs, test snapshots, and documentation examples must not echo source payloads, credentials, owner information, exact coordinates, or proprietary curve content;
- generalized maps, cross-sections, or structural surfaces require downstream policy, validation, evidence, review, release, correction, and rollback support;
- no output from this lane is drilling, engineering, reservoir, resource, investment, legal, water-supply, environmental, or life-safety advice.

[Back to top](#top)

---

## Inputs and outputs

### Current inputs

None. This README-only lane declares no supported function, class, command, endpoint, configuration contract, credential variable, host allowlist, fixture format, LAS parser profile, source-head protocol, or sink interface.

### Current outputs

None. It emits no payload, header record, curve record, top interpretation, model, candidate envelope, receipt, validation report, lifecycle object, EvidenceBundle, map artifact, API response, or public claim.

### Future admissible inputs

Only after an accepted placement, package, descriptor, activation, rights, sensitivity, and product decision, a retained connector may accept:

- a conforming, reviewed, product-specific `SourceDescriptor` reference;
- an explicit activation decision for fixture-only, restricted, or approved live operation;
- approved caller-supplied files, bytes, archives, metadata, or transport results;
- exact KGS product/surface identity and source-native identifiers;
- well/borehole, log, file, curve, top, and model identifiers as applicable;
- source-head evidence such as version, release date, checksum, revision, `ETag`, `Last-Modified`, or documented manual identity;
- source, observed, valid/effective, retrieval, and correction time where material;
- depth index, depth reference, datum, units, sampling interval, null values, geometry, uncertainty, and withholding state;
- rights, attribution, redistribution, disclaimer, sensitivity, and reviewer references;
- explicit run identity and caller-owned candidate-output interfaces;
- synthetic or explicitly rights-cleared offline fixtures.

### Future admissible outputs

A future accepted implementation may return, without selecting release or direct persistence:

- deterministic source-head or probe results;
- preserved source metadata and parse results;
- explicit unsupported-format or unsupported-curve findings;
- a `RAW` handoff candidate when identity, role, rights, sensitivity, source head, and activation are sufficiently resolved;
- a `QUARANTINE` handoff candidate with structured reasons when they are not;
- a deterministic denial, abstention, no-op, rate-limit, or error outcome;
- an in-memory operational receipt candidate when an accepted receipt contract exists.

The connector must not create processed geology, interpreted canonical truth, EvidenceBundles, catalog/triplet records, released cross-sections, public geometry, regulatory decisions, or public answers.

[Back to top](#top)

---

## Compatibility and future implementation boundary

### Allowed now

Because this is README-only and noncanonical, accepted content is deliberately narrow:

- this documentation boundary;
- links to current competing paths and governing source/domain documents;
- an approved redirect, deprecation notice, supersession reference, or migration receipt;
- warnings that prevent duplicate connector, product, descriptor, registry, fixture, test, policy, or release authority;
- a bounded inventory that is regenerated from pinned repository evidence.

### Allowed only after an accepted migration

- a transparent compatibility import or redirect with an owner, warning, sunset criterion, tests, and rollback;
- narrow product dispatch that preserves exact KGS/LAS product identity;
- explicit opt-in transport behind reviewed host, credential, timeout, retry, rate-limit, content-type, response-size, and source-head controls;
- source-native LAS/header/curve metadata parsing whose supported versions and constraints are explicitly tested;
- deterministic normalization that preserves raw values, units, depth semantics, nulls, uncertainty, and source lineage;
- structured finite outcomes and reason codes;
- side-effect-free candidate-envelope construction for governed orchestration;
- offline, synthetic, minimized, negative-first fixtures and tests.

### Forbidden

- network calls on import, installation, documentation rendering, or default test execution;
- credentials, cookies, authorization headers, account data, private endpoints, signed URLs, or source payloads in source, docs, fixtures, logs, errors, or snapshots;
- publisher-wide default roles, rights, sensitivity, cadence, source-head, or release assumptions;
- authoritative descriptors, authority entries, activation decisions, policies, or releases inside this folder;
- direct writes to RAW, QUARANTINE, receipts, WORK, PROCESSED, CATALOG, TRIPLET, proofs, release, rollback, or PUBLISHED roots;
- parsing that silently changes units, depth reference, datum, curve meaning, null values, geometry precision, or interpretation status;
- automatic conversion from curve to formation top, top to model, model to fact, or upstream availability to public release;
- reconstruction or exposure of withheld locations;
- public maps, cross-sections, APIs, downloads, dashboards, exports, engineering tools, or AI answers;
- claims of implementation, coverage, validation, activation, or CI maturity without current evidence.

There is intentionally no quickstart. A runnable example would imply a supported API, source, format, rights posture, and safety boundary that do not exist.

[Back to top](#top)

---

## Failure contract

A future accepted implementation must fail deterministically without echoing sensitive or proprietary source content. Minimum reason families include:

- unresolved connector path, package/import identity, source ID, or LAS product topology;
- missing, nonconforming, unreviewed, superseded, or inactive product descriptor;
- missing activation decision or operation not allowed by activation mode;
- unknown source product, unsupported LAS/source shape, unsafe archive, source-head mismatch, or stale source;
- unresolved rights, attribution, redistribution, disclaimer, access, cadence, or sensitivity;
- missing well/borehole/log/file/curve/top/model identity;
- missing or ambiguous depth index, depth reference, datum, units, sampling interval, null value, or curve meaning;
- unresolved geometry, precision, PLSS derivation, uncertainty, withholding, private-land, or infrastructure-adjacent risk;
- observed curve, interpreted top, modeled surface, completion record, regulatory filing, or aggregate mixed without a governed split;
- denied network posture, unapproved host, unsafe credential handling, response-size violation, or payload logging;
- attempted direct lifecycle persistence, evidence creation, release, public output, or operational advice.

Unknowns route to `DENY`, `ABSTAIN`, `HOLD`, `ERROR`, or a `QUARANTINE` candidate. They never receive permissive defaults.

[Back to top](#top)

---

## Validation

No build, install, import, parser, or test command is documented because this path contains no verified package metadata or executable implementation.

Before any LAS connector maturity can be claimed, evidence must cover:

1. accepted KGS connector path, package/import identity, source-ID convention, product topology, and losing-path migration;
2. complete recursive inventory of package, fixtures, tests, workflows, descriptors, registry entries, and backlinks;
3. supported LAS/source formats, parser profile, safe archive handling, build backend, Python support, dependency policy, and clean install/import;
4. accepted `SourceDescriptor` schema authority and narrative-to-machine role mapping;
5. product-specific descriptor, source-authority/registry state, review state, activation decision, and source head;
6. current source access, terms, attribution, redistribution, disclaimers, cadence, rate limits, corrections, and withdrawal behavior;
7. no-network default plus host, credential, timeout, retry, content-type, response-size, archive, and payload-logging controls;
8. synthetic or rights-cleared fixtures covering headers, curves, tops, depth, datum, units, nulls, malformed files, unsupported shapes, and safe failures;
9. source-role and anti-collapse tests for raw curves, interpreted tops, modeled surfaces, WWC5, KCC records, and production aggregates;
10. sensitive-location, PLSS, private-land, proprietary-log, infrastructure, geometry, uncertainty, and withholding negative tests;
11. deterministic candidate-envelope, no-op, denial, idempotency, receipt, and lifecycle-boundary tests;
12. proof that the connector cannot create policy, EvidenceBundle, catalog, release, public map/API/UI, or AI authority;
13. substantive package-specific CI discovery with positive and negative failure evidence;
14. correction, deactivation, supersession, migration, invalidation, and rollback tests.

The current named connector and source-descriptor workflows are TODO-only. Their green completion must not be cited as proof of LAS package behavior, descriptor validity, rights presence, sensitivity enforcement, or source activation.

Documentation validation for this revision should include one H1, balanced fenced blocks, working repository-relative links, no remote badge/image dependencies, no credential-like strings, a final newline, and an exact one-file diff.

[Back to top](#top)

---

## Evidence basis

Evidence is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `a05b61a289cf5c87fb9d9173103c6d597a0c459d`.

| Evidence | Status | Supports | Does not support |
|---|---|---|---|
| Target README and history | **CONFIRMED** | Prior blob `c78311310f49b2695e244d7d3ba3ffab78285b69`; substantive README introduced by commit `3a5acc266375392d2a03603a3d381cc673ed6466`. | Runtime, source access, rights, tests, activation, or release. |
| Exact target-child probes | **CONFIRMED absent at base** | No named `pyproject.toml`, `src/README.md`, or `tests/README.md` under this lane. | Permanent nonexistence or absence of differently named/unindexed files. |
| `connectors/geology/kgs/README.md` | **CONFIRMED v0.2 documentation** | Current path conflict, source-first placement rule, README-only product lanes, and sensitive-well posture. | Accepted canonical path, product activation, or runtime. |
| `connectors/ksgs/README.md` and package docs | **CONFIRMED scaffold** | Separate non-operational `0.0.0` KSGS package exists. | LAS implementation, canonical identity, source activation, or release. |
| Exact `connectors/kansas/kgs/README.md` probe | **CONFIRMED absent at base** | Proposed child is not present at the pinned commit. | Permanent nonexistence or final path decision. |
| KGS source catalog | **CONFIRMED draft** | LAS logs and well tops are distinct products; raw curves, interpretations, models, WWC5, KCC, and aggregates require role separation; rights and exact-location handling fail closed. | Current source service, terms, machine role, descriptor, or activation. |
| Geology well-log pipeline README | **CONFIRMED documentation** | Downstream processing and anti-collapse boundary. | Executable pipeline behavior, connector ownership, passing tests, or release. |
| SourceDescriptor contract and populated singular schema | **CONFIRMED draft / PROPOSED schema** | Rich descriptor surface and fail-closed constraints. | Accepted plural-path migration or LAS descriptor enforcement. |
| Plural SourceDescriptor schema | **CONFIRMED empty PROPOSED scaffold** | Current schema-home conflict. | Meaningful validation or canonical migration completion. |
| Source-authority register | **CONFIRMED** | `status: PROPOSED`, `entries: []`. | Any KGS LAS authority or activation decision. |
| Connector and descriptor workflows | **CONFIRMED TODO-only** | Workflow names and triggers exist. | Substantive connector, descriptor, rights, sensitivity, or lifecycle validation. |
| Directory Rules and connector-output doctrine | **CONFIRMED doctrine** | Responsibility-root placement, source-edge boundary, no parallel authority, governed lifecycle, and reversible migration. | Current runtime implementation by themselves. |

Not inspected: live KGS source services, current terms pages, credentials, source payloads, proprietary logs, real well coordinates, account-gated records, executable LAS parsers, runtime logs, deployed configuration, emitted receipts, EvidenceBundles, release manifests, or public clients. Treat associated claims as `UNKNOWN` or `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Review, migration, and rollback

Review changes here as connector-placement, package/import identity, KGS product identity, source-role, rights, subsurface sensitivity, privacy, exact-location, security, dependency, and lifecycle-boundary changes—even when the diff is documentation-only.

A future migration must preserve or deliberately supersede:

- Git and document history;
- package/import compatibility and deprecation behavior;
- product/source/file/well/log/curve/top/model identities;
- descriptor references and source-authority records;
- source-head and retrieval lineage;
- depth, datum, unit, geometry, uncertainty, withholding, and disclaimer semantics;
- fixtures, tests, workflow discovery, and negative cases;
- receipts, candidate-envelope references, and downstream backlinks;
- rights, sensitivity, correction, withdrawal, review, and release state;
- rollback to the last known safe connector and documentation state.

Rollback this README revision if it is used to:

- treat this or another path as canonical without an accepted decision;
- activate a missing or unresolved descriptor, registry placeholder, or source;
- claim working access, parsing, fixtures, tests, CI, policy, lifecycle handoff, or release;
- collapse raw curves, well tops, models, WWC5, KCC records, production, or generated summaries;
- expose proprietary content, private-well data, exact sensitive locations, or harmful joins;
- present a log, top, or model as engineering, drilling, reserve, water-supply, legal, environmental, or safety advice;
- bypass descriptor, activation, rights, sensitivity, evidence, policy, review, release, correction, or rollback gates.

Before merge, close the draft change and abandon its scoped branch if rejected. After merge, create a transparent revert of the documentation commit; do not reset, force-push, or rewrite shared history. The baseline target blob is `c78311310f49b2695e244d7d3ba3ffab78285b69` at base commit `a05b61a289cf5c87fb9d9173103c6d597a0c459d`.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Final KGS connector path and `kgs` versus `ksgs` package/import/source-ID convention | **CONFLICTED** | Accepted ADR or migration plan with inventory, compatibility, deprecation, and rollback. |
| Disposition of `connectors/kgs_las/` | **NEEDS VERIFICATION** | Retain-as-pointer, redirect, deprecate, migrate, or remove decision. |
| LAS product identity and relation to KGS dispatcher/product modules | **NEEDS VERIFICATION** | Accepted source/product architecture and stable identifiers. |
| SourceDescriptor schema authority and narrative-to-machine role mapping | **CONFLICTED** | Accepted schema/validator migration and role crosswalk. |
| Product-specific descriptor, registry/authority entry, review state, and activation | **NOT ESTABLISHED** | Conforming records and governed review evidence. |
| Current access methods, supported formats, source heads, endpoints, terms, attribution, redistribution, cadence, and rate limits | **NEEDS VERIFICATION** | Source-steward and rights review against current source surfaces. |
| LAS parser profile, safe archive behavior, headers, curves, depth, datum, units, nulls, and unsupported-shape outcomes | **UNKNOWN** | Implemented parser contract, fixtures, tests, and logs. |
| Well-top interpretation and modeled-surface lineage | **NEEDS VERIFICATION** | Interpretation/model contracts, receipts, evidence refs, uncertainty, tests, and correction behavior. |
| Exact-location, PLSS, private-land, proprietary-log, infrastructure, geometry, uncertainty, redaction, and public-precision policy | **NEEDS VERIFICATION** | Executable policy, negative fixtures, transform receipts, review, and release tests. |
| Safe fixtures and executable package tests | **UNKNOWN** | Synthetic/rights-cleared fixture inventory, runner, discovered tests, and negative coverage. |
| Substantive connector and descriptor CI | **NOT IMPLEMENTED IN NAMED WORKFLOWS** | Workflow steps executing real validation and preserving failure evidence. |
| Downstream pipeline, EvidenceBundle, catalog, release, correction, and rollback closure | **UNKNOWN** | Current implementation, receipts, proofs, manifests, tests, and drills. |
| Owners and required reviewers | **UNKNOWN** | Accepted CODEOWNERS or steward register entries. |

[Back to top](#top)

---

## Definition of done

### Documentation boundary

- [x] Current README-only state and exact named absence probes are explicit.
- [x] Proposed Kansas child, live KSGS scaffold, domain-scoped pointer, and product path are not collapsed.
- [x] LAS file, curve, top, model, WWC5, KCC, production, and generated-summary distinctions are explicit.
- [x] Descriptor/schema/registry/policy/workflow conflicts and default-deny result are explicit.
- [x] Current inputs, outputs, commands, parser, tests, activation, lifecycle behavior, and publication are stated as absent or unknown.
- [x] Rights, proprietary content, exact location, private land, PLSS, depth, datum, units, uncertainty, and public-use boundaries are explicit.
- [x] Evidence limits, migration discipline, review burden, and rollback target are recorded.

### Implementation readiness

- [ ] Connector/package/product migration is accepted and losing paths are dispositioned.
- [ ] Owners and required reviewers are assigned.
- [ ] Build, install, supported-runtime, dependency, command, and package API contracts exist.
- [ ] SourceDescriptor machine authority and role mapping are accepted.
- [ ] Product-specific descriptor, source-authority/registry state, source head, review, rights, sensitivity, and activation are approved.
- [ ] Current access, formats, terms, attribution, redistribution, cadence, rate limits, correction, and withdrawal are reviewed.
- [ ] LAS/header/curve, well-top interpretation, depth/datum/unit, model, identity, geometry, and uncertainty contracts are implemented.
- [ ] Default tests are offline, deterministic, synthetic or rights-cleared, negative-first, and CI-discovered.
- [ ] Connector and descriptor workflows execute substantive checks instead of TODO steps.
- [ ] Candidate-envelope, no-op, denial, receipt, lifecycle, correction, deactivation, migration, and rollback behavior is tested.
- [ ] Public release, if ever approved, resolves EvidenceBundle, policy, review, manifest, correction, and rollback state.

Until every applicable implementation-readiness item closes, keep this lane documentation-only and fail closed.

<p align="right"><a href="#top">Back to top</a></p>
