<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kgs-oil-gas-wells-readme
title: connectors/kgs_oil_gas_wells/ — KGS Oil and Gas Wells Connector Compatibility Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · KGS source steward · Kansas source steward · Geology steward · Natural resources steward · Rights reviewer · Privacy/sensitivity reviewer · Security reviewer · Contract/schema reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; compatibility-path; readme-only; path-and-slug-conflict; oil-gas-wells; production-aggregates; source-admission; source-role-anti-collapse; rights-fail-closed; sensitivity-fail-closed; no-network; no-activation; no-publication
current_path: connectors/kgs_oil_gas_wells/README.md
truth_posture: CONFIRMED README-only product lane, absent conventional package/test/fixture paths, proposed KGS oil-and-gas registry template, empty machine authority register, 0.0.0 KSGS scaffold, and absent proposed Kansas KGS child / CONFLICTED final KGS connector path, slug and package identity, product decomposition, SourceDescriptor authority, role vocabulary, registry topology, fixture routing, and migration disposition / PROPOSED future bounded source-admission contract / UNKNOWN differently named files, executable runtime, live source access, current terms, activation, substantive CI coverage, deployment, evidence closure, and release state
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: a05b61a289cf5c87fb9d9173103c6d597a0c459d
  prior_blob: 252a9246b96185bcad213ea2537d8e27dc9c84dd
related:
  - ../README.md
  - ../geology/README.md
  - ../geology/kgs/README.md
  - ../kgs/README.md
  - ../ksgs/README.md
  - ../ksgs/pyproject.toml
  - ../ksgs/src/README.md
  - ../ksgs/src/ksgs/README.md
  - ../ksgs/src/ksgs/descriptor.yaml
  - ../ksgs/tests/README.md
  - ../kcc_oil_gas_reg/README.md
  - ../kansas/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/README.md
  - ../../docs/sources/catalog/kansas/ksgs.md
  - ../../docs/sources/catalog/kansas/kcc-oil-gas-reg.md
  - ../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../docs/domains/geology/SOURCES.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../data/registry/geology/sources/ksgs_oil_and_gas.yaml
  - ../../control_plane/source_authority_register.yaml
  - ../../tests/README.md
  - ../../tests/fixtures/README.md
  - ../../fixtures/README.md
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
  - ../../.github/workflows/connector-gate.yml
  - ../../.github/workflows/source-descriptor-validate.yml
tags: [kfm, connectors, kgs, ksgs, oil-gas, wells, production, leases, fields, geology, natural-resources, kansas, compatibility, source-admission, source-role, rights, sensitivity, geometry, time, no-network, fail-closed, raw, quarantine, governance]
notes:
  - 'The inspected product lane contains this README only; exact probes did not find package metadata, source-layout documentation, a local test README, an import package initializer, a root connector test README, or a domain fixture README.'
  - 'KGS placement is materially conflicted among connectors/kgs/, the live connectors/ksgs/ 0.0.0 scaffold, proposed-but-absent connectors/kansas/kgs/, the documentation-only connectors/geology/kgs/ pointer, and top-level KGS product READMEs.'
  - 'The proposed data/registry/geology/sources/ksgs_oil_and_gas.yaml template leaves role, authority, rights, sensitivity, cadence, and access posture unresolved; it is not a conforming activation record or public-release authority.'
  - 'The machine source-authority register is PROPOSED with entries: []; the KSGS package-local descriptor is a four-field placeholder and sensitivity_floor: public must not be treated as a permissive release decision.'
  - 'KGS well observations, production aggregates, lease or field summaries, KCC regulatory records, interpreted subsurface products, and generated analyses must remain separate source-role and record classes.'
  - 'Only this Markdown file is in scope. No code, package metadata, descriptor, registry entry, contract, schema, policy, fixture, test, workflow, source payload, credential, activation decision, lifecycle object, release object, or public artifact is created or changed.'
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KGS Oil and Gas Wells Connector Compatibility Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Current maturity:** `CONFIRMED` README-only product lane at the inspected paths; no executable connector behavior is established  
> **Placement posture:** final KGS connector path, slug, package identity, product routing, registry authority, fixture home, and test routing are `CONFLICTED / NEEDS VERIFICATION`  
> **Authority:** source-admission compatibility documentation only; no source, schema, policy, lifecycle, evidence, release, operational, regulatory, or publication authority.

> [!WARNING]
> A directory, catalog page, placeholder descriptor, proposed registry template, well record, production table, pull request, merge, or green TODO-only workflow is not connector implementation, source activation, current operational status, reserve truth, regulatory authority, or public-release evidence.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#current-status) · [Placement](#placement-and-naming-conflict) · [Product boundaries](#product-and-source-role-boundaries) · [Identity and time](#identity-time-geometry-and-units) · [Rights](#rights-sensitivity-and-access) · [Lifecycle](#lifecycle-and-publication-boundary) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Evidence](#evidence-basis) · [ADRs](#adrs-and-migration) · [Rollback](#rollback) · [Definition of done](#definition-of-done) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/kgs_oil_gas_wells/` is the repository-present documentation lane for an unresolved KGS oil-and-gas wells and production connector product path.

Its present responsibility is to:

- record the exact README-only surface that exists;
- prevent a product-named directory from being mistaken for a working or canonical connector;
- expose the unresolved relationship among KGS publisher-level, package-level, domain-pointer, Kansas-family, and product-specific paths;
- preserve the distinction among well observations, headers, lease and field records, production aggregates, interpreted subsurface products, and KCC regulatory records;
- define fail-closed boundaries for source role, identity, time, geometry, coordinate precision, units, rights, privacy, sensitivity, and cross-source joins;
- describe the minimum contract for any future product adapter without creating source or release authority here;
- preserve a reversible migration target while the repository selects one accepted KGS connector topology.

This directory does not prove that the snake_case slug is final, that a KGS implementation package exists here, that `connectors/kansas/kgs/` exists, that the live `connectors/ksgs/` scaffold owns this product, that a KGS source may be contacted, or that any KGS-derived record is safe to publish.

Directory Rules place source-specific fetch, probe, preservation, and admission mechanics under `connectors/`. Source catalogs, machine authority records, contracts, schemas, policies, tests, fixtures, lifecycle storage, evidence closure, release decisions, public APIs, maps, and generated explanations remain in their owning responsibility roots.

[Back to top](#top)

---

## Authority level

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Owning responsibility root | **CONFIRMED** | `connectors/` owns source-specific fetch, probe, preservation, parsing, and admission mechanics. |
| Current product path | **CONFIRMED** | `connectors/kgs_oil_gas_wells/README.md` exists at the pinned base. |
| Current implementation here | **NOT FOUND AT NAMED CONVENTIONAL PROBES / OTHERWISE UNKNOWN** | No package metadata, source layout, import package, connector-local tests, root connector tests, or domain fixture README was found at the inspected paths. |
| Final KGS connector path | **CONFLICTED** | Current evidence includes `connectors/kgs/`, the `connectors/ksgs/` scaffold, proposed-but-absent `connectors/kansas/kgs/`, the non-implementation `connectors/geology/kgs/` pointer, and several top-level KGS product README paths. |
| Product adapter strategy | **CONFLICTED** | The repository has product-specific compatibility paths, while the KGS catalog expects separate product descriptors under a publisher adapter. No accepted dispatcher or package split was verified. |
| Package and import identity | **CONFLICTED** | The only implementation-shaped scaffold uses `ksgs`; the publisher abbreviation and several docs use `kgs`; this product path uses `kgs_oil_gas_wells`. No accepted migration reconciles them. |
| Product registry template | **PROPOSED / INCOMPLETE** | `data/registry/geology/sources/ksgs_oil_and_gas.yaml` leaves role, authority, license, redistribution, sensitivity, cadence, access posture, and citation unresolved. |
| Package-local descriptor | **NONCONFORMING PLACEHOLDER** | `connectors/ksgs/src/ksgs/descriptor.yaml` contains four minimal fields and cannot authorize this product, activation, rights, sensitivity, or release. |
| Machine authority | **NOT ESTABLISHED** | `control_plane/source_authority_register.yaml` is `PROPOSED` with `entries: []`. |
| Source activation | **DENIED / NOT VERIFIED** | No accepted product descriptor, source head, access method, rights review, sensitivity review, fixture plan, tests, or activation decision was verified. |
| Public output | **NONE FROM THIS LANE** | This README emits no source payload, lifecycle record, evidence object, map, API response, release, or publication artifact. |

Editing this README does not ratify the current path, any proposed child, the `kgs` or `ksgs` slug, product scope, source role, rights posture, sensitivity posture, access method, activation state, or release class.

[Back to top](#top)

---

## Current status

### Bounded repository snapshot

The directly inspected product surface is:

```text
connectors/kgs_oil_gas_wells/
└── README.md                           # this compatibility boundary
```

Exact probes returned `Not Found` for:

```text
connectors/kgs_oil_gas_wells/pyproject.toml
connectors/kgs_oil_gas_wells/src/README.md
connectors/kgs_oil_gas_wells/tests/README.md
connectors/kgs_oil_gas_wells/src/kgs_oil_gas_wells/__init__.py
connectors/kansas/kgs/README.md

tests/connectors/kgs_oil_gas_wells/README.md
fixtures/domains/geology/kgs_oil_gas_wells/README.md
```

These absence statements are bounded to the pinned commit, indexed search, and named exact paths. Differently named, generated, ignored, unindexed, or concurrent files remain `UNKNOWN`.

### Related live and proposed surfaces

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| [`connectors/geology/kgs/`](../geology/kgs/README.md) | README-only compatibility pointer that explicitly rejects domain-scoped KGS implementation. | Not an implementation home. |
| [`connectors/kgs/`](../kgs/README.md) | README-only top-level compatibility lane. | Presence does not settle canonicality. |
| [`connectors/ksgs/`](../ksgs/README.md) | `0.0.0` greenfield scaffold with package/test documentation and placeholder files. | Implementation-shaped but non-operational and not ratified as canonical. |
| `connectors/kansas/kgs/` | Proposed by the human-facing KGS catalog; exact README absent. | Proposal and migration input, not path-presence proof. |
| This product path | README only. | Documentation boundary, not product implementation. |
| [KGS source catalog](../../docs/sources/catalog/kansas/ksgs.md) | Draft human-facing publisher and product orientation. | Does not activate a source or prove implementation paths. |
| [KGS oil-and-gas registry template](../../data/registry/geology/sources/ksgs_oil_and_gas.yaml) | Proposed template with unresolved trust-bearing fields. | Negative or migration input, not source authority. |
| [KCC regulatory connector](../kcc_oil_gas_reg/README.md) | Separate regulatory compatibility boundary. | KCC records must not be collapsed into KGS observations or aggregates. |

[Back to top](#top)

---

## Placement and naming conflict

The repository contains enough conflicting evidence that no final KGS connector path can be declared by convenience.

| Candidate | Current posture | Constraint |
|---|---:|---|
| `connectors/kgs/` | **REPOSITORY-PRESENT / README-ONLY / CONFLICTED** | Geology path doctrine names it, but its own README calls it compatibility-only. |
| `connectors/ksgs/` | **REPOSITORY-PRESENT / 0.0.0 SCAFFOLD / NON-OPERATIONAL** | Package slug differs from publisher abbreviation; placeholder files do not ratify ownership. |
| `connectors/kansas/kgs/` | **PROPOSED / ABSENT AT EXACT README PROBE** | The source catalog asserts this path, but the same catalog states it cannot prove path existence. |
| `connectors/geology/kgs/` | **REPOSITORY-PRESENT / DOCUMENTATION-ONLY / FORBIDDEN FOR IMPLEMENTATION** | Source-first connector doctrine rejects a consumer-domain implementation path. |
| `connectors/kgs_oil_gas_wells/` | **REPOSITORY-PRESENT / README-ONLY PRODUCT PATH** | Product naming does not authorize an independent package, descriptor, credential, or activation lane. |

The smallest safe posture is:

1. keep this path documentation-only;
2. do not create product code, descriptors, credentials, fixtures, or tests here until placement is accepted;
3. preserve all existing KGS product and path evidence as migration inputs;
4. require one accepted source-first connector topology with explicit product routing, compatibility behavior, tests, and rollback;
5. migrate or retire losing paths transparently rather than silently declaring them canonical.

[Back to top](#top)

---

## What belongs here

### Current allowed content

Until an accepted KGS path and migration decision exists, this directory should contain only:

- this compatibility and evidence-boundary README;
- bounded repository-state notes about the current product path;
- links to KGS catalog, KCC peer, contracts, schemas, registry, policy, tests, fixtures, and release authority;
- explicit path, slug, package, product, role, identity, rights, sensitivity, geometry, fixture, and test conflicts;
- deprecation, redirect, delegation, or losing-path instructions after they are accepted;
- rollback instructions that preserve history.

### Future allowed content only after a placement decision

If an accepted ADR or migration retains this product as an implementation package or delegates it through a parent KGS adapter, narrowly scoped mechanics may include:

- explicit opt-in transport with reviewed hosts, timeouts, retries, rate limits, byte limits, cancellation, credential boundaries, and source-head capture;
- parsers for source-native well headers, lease or field identifiers, monthly or periodic production rows, and documented aggregate scopes;
- source-head, checksum, pagination, freshness, and no-change detection helpers;
- deterministic well, lease, field, production-row, and source-record identity preservation;
- pure validation and caller-owned candidate-envelope builders;
- deterministic `DENY`, `ABSTAIN`, `HOLD`, rate-limit, no-change, quarantine-candidate, and error outcomes;
- package-local tests only for behavior owned by the accepted package;
- migration shims with explicit ownership, warnings, sunset criteria, tests, and rollback.

A README, directory, source-catalog assertion, proposed registry template, or `0.0.0` scaffold is not sufficient authority to begin that implementation.

[Back to top](#top)

---

## What does not belong here

This directory must not contain or imply authority over:

- canonical KGS placement, package identity, product routing, source ID, source role, rights, sensitivity, access, or activation;
- authoritative `SourceDescriptor` records, machine authority entries, contracts, schemas, policies, evidence objects, or release decisions;
- bulk KGS downloads, production tables, well exports, map-service caches, database dumps, PDFs, images, logs, or unreviewed source samples;
- credentials, cookies, authorization headers, account details, signed URLs, private endpoints, or secrets;
- KCC regulatory determinations, legal advice, mineral-title truth, current operational status, emergency guidance, life-safety guidance, drilling guidance, reservoir conclusions, reserve estimates, forecasts, or investment guidance;
- a claim that a well header proves current operation, production, compliance, ownership, reservoir condition, reserves, or regulatory authorization;
- a claim that county, field, or lease production can be attributed to a specific well without explicit source linkage and an accepted contract;
- real private-owner, royalty-owner, residence, parcel, non-public business, or harmful infrastructure joins in fixtures, logs, examples, or generated output;
- network access on import, installation, default tests, or documentation rendering;
- direct writes to `data/raw/`, `data/quarantine/`, receipts, processed, catalog, triplets, proofs, published, or `release/`;
- public maps, tiles, APIs, dashboards, summaries, graphs, embeddings, or AI narratives generated directly from connector output;
- source records, aggregates, interpreted products, or generated analyses relabeled as one another.

[Back to top](#top)

---

## Product and source-role boundaries

KGS oil-and-gas material is not one uniform source product.

| Record or product class | Safe source-role posture | Denied collapse |
|---|---|---|
| Well header or well-record observation | Observation or administrative record, subject to accepted vocabulary and descriptor | Does not prove current operation, production, compliance, reserves, or KCC authorization. |
| Lease or field record | Administrative or aggregation context, as defined by the source | Must not be silently treated as a well identity or mineral-title assertion. |
| Production total | Aggregate with explicit period and aggregation unit | Must not be attributed to a well, parcel, formation, owner, or reserve estimate beyond source support. |
| KCC permit, order, inspection, UIC, or enforcement record | Regulatory context owned by KCC source lanes | Must not be synthesized from KGS observations or aggregates. |
| Well top, structural surface, or interpreted subsurface product | Modeled or interpreted derivative with lineage | Must not be labeled as raw observation or direct measurement. |
| KFM summary, map, join, score, forecast, or AI explanation | Derived carrier requiring evidence, policy, review, and release | Never becomes sovereign truth or source authority. |

The current catalog uses `observed`, `aggregate`, `administrative`, `modeled`, `context`, `candidate`, and `synthetic` language, while the proposed local registry template documents a different abbreviated role vocabulary and leaves `role: TBD`. This README records that conflict; it does not translate or select an enum by convenience.

### KGS and KCC anti-collapse rule

KGS may publish well or production information. KCC publishes regulatory records. Shared well identifiers, places, dates, or names may support a governed crosswalk, but they do not merge source roles or authority.

Any future join must preserve:

- publisher and source-product identity;
- source-native identifiers and source URI;
- source role and record class;
- valid, reported, retrieval, and release times;
- join method, confidence, ambiguity, and unmatched state;
- rights, sensitivity, geometry, and release posture for each side;
- independent EvidenceRefs and correction lineage.

[Back to top](#top)

---

## Identity, time, geometry, and units

### Identity

Future accepted code must preserve source-native identity rather than inventing one undifferentiated hydrocarbon record.

At minimum, retain where supplied:

- publisher and product ID;
- source URI and retrieval identity;
- KGS well identifier and API number, with scheme/version when available;
- lease, field, county, operator, completion, and production-row identifiers as separate fields;
- source table, layer, service, or publication identity;
- original versus corrected, superseded, duplicate, or withdrawn status;
- crosswalk references and ambiguity state.

A deterministic KFM candidate ID may be proposed only after the owning contract defines its namespace, normalization, version, and collision behavior.

### Time

Keep material time kinds separate:

- source publication or update time;
- source-reported well event date;
- completion, plugging, or other event time where present;
- production period start and end;
- source reporting or revision period;
- retrieval time;
- KFM validation, release, correction, and withdrawal times.

A current source refresh does not make every historical record current. A recent production table does not establish present well status. Missing or ambiguous time must remain visible and may require `ABSTAIN` or quarantine.

### Geometry and precision

Preserve:

- source-native coordinates;
- CRS and datum when supplied;
- coordinate method and source;
- PLSS components and derivation when applicable;
- positional uncertainty and precision class;
- generalized or withheld public geometry plus transform rule version;
- geometry correction or supersession lineage.

Do not present PLSS-derived or approximate coordinates as surveyed precision. Exact well, borehole, private-land, and infrastructure-adjacent locations fail closed when public exposure could increase harm or violate terms.

### Units and aggregation

Production values require explicit:

- commodity or measure name;
- unit and unit vocabulary;
- reporting interval;
- aggregation unit such as county, field, lease, or explicitly linked well;
- missing, zero, withheld, estimated, corrected, or not-applicable state;
- source revision and completeness caveat.

Never convert an aggregate to a finer spatial or record-level claim without explicit source support and a governed transformation record.

[Back to top](#top)

---

## Rights, sensitivity, and access

Current product rights, attribution, redistribution, access mechanics, and source-specific terms remain `NEEDS VERIFICATION`.

Default behavior:

- unknown rights or redistribution posture → `DENY` public release;
- missing attribution or disclaimer requirements → hold or quarantine;
- unresolved exact-location sensitivity → withhold or generalize;
- private-person, owner, royalty, residence, parcel, or harmful business joins → deny unless explicitly governed;
- unclear credential or access method → no network access;
- stale or missing source head → no claim of current completeness;
- source public availability → not equivalent to KFM publication permission.

Sensitive classes may include exact wells or boreholes, active or infrastructure-adjacent locations, private-land context, owner-linked attributes, and joins that reveal non-public operational or personal information.

Any public geometry transform requires a deterministic rule, reason, reviewer, before/after scope, and auditable redaction or generalization receipt in the accepted responsibility root. This connector must not perform silent public redaction or publish transformed coordinates directly.

[Back to top](#top)

---

## Lifecycle and publication boundary

This connector is upstream of lifecycle storage and downstream of accepted source authority.

```text
accepted SourceDescriptor reference + activation state
                    |
                    v
        explicit opt-in transport or caller bytes
                    |
                    v
       parse + preserve + validate + classify
                    |
        +-----------+-----------+
        |                       |
        v                       v
caller-owned RAW candidate   caller-owned QUARANTINE candidate
        |                       |
        +-----------+-----------+
                    |
                    v
      caller-owned orchestration and governed lifecycle
                    |
                    v
WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

### Current behavior

None. This README performs no fetch, parse, admission, candidate construction, lifecycle write, evidence closure, release, or publication.

### Future connector ceiling

An accepted implementation may return in-memory, caller-owned:

- source-faithful parse results;
- source-head and no-change results;
- deterministic validation findings;
- RAW candidate envelopes containing approved source-native content or references plus provenance;
- QUARANTINE candidate envelopes with stable reason codes and bounded diagnostics;
- receipt candidates describing an attempted operation without claiming policy approval, evidence closure, or release.

It must not select a repository lifecycle sink, write directly to lifecycle roots, close an `EvidenceBundle`, create authoritative receipts or proofs, approve promotion, or publish a public artifact.

[Back to top](#top)

---

## Inputs

### Current inputs

None. The inspected lane declares no callable interface, command, endpoint, environment variable, credential mode, fixture shape, parser contract, or supported package.

### Future permitted inputs

Only after placement, contracts, review, and activation are accepted:

- a conforming, reviewed product-specific `SourceDescriptor` reference;
- an explicit activation state and approved access configuration;
- caller-supplied source bytes, files, rows, or approved transport results;
- source URI, source head, retrieval time, checksum, run identity, and destination intent;
- well, lease, field, production-row, period, geometry, unit, and source-product identifiers;
- rights, attribution, redistribution, disclaimer, sensitivity, access-class, and review context;
- synthetic, generated-shape-only, redacted, or explicitly rights-cleared fixtures;
- correction, supersession, withdrawal, and replay context.

Missing, stale, malformed, conflicted, or unsafe trust-bearing inputs must fail closed before network access or candidate handoff.

[Back to top](#top)

---

## Outputs

### Current outputs

None.

### Future permitted outputs

Only in-memory, caller-owned candidates and deterministic finite outcomes, including:

- source-faithful parsed records;
- `DENY`, `ABSTAIN`, `HOLD`, no-change, rate-limit, cancellation, or error outcomes;
- RAW candidates with source-native identity, time, geometry, units, rights, sensitivity, and provenance;
- QUARANTINE candidates with stable reason codes and payload-safe diagnostics;
- receipt candidates that describe the operation without claiming admission, policy approval, evidence closure, or release.

Forbidden outputs include direct lifecycle writes, public maps or APIs, production forecasts, reserve statements, regulatory conclusions, owner or parcel profiles, evidence bundles, release manifests, published records, and AI-generated source truth.

[Back to top](#top)

---

## Validation

No executable test runner or product-specific suite is established for this lane. The following is a future acceptance contract, not a claim of implemented coverage.

| Validation family | Required behavior |
|---|---|
| Import and package discovery | No network, credentials, files, logs, threads, registration, activation, or global-state mutation on import or discovery. |
| Placement and migration | Fail if the product path, package, slug, descriptor, or fixture lane is treated as canonical without accepted migration evidence. |
| Descriptor and activation | Reject the proposed registry template and package-local YAML as activation authority; require a conforming reviewed product descriptor and explicit activation state. |
| Product and source role | Preserve well observations, lease or field records, production aggregates, KCC regulatory records, interpreted products, and generated derivatives as distinct classes. |
| Identity | Preserve source-native well, API, lease, field, operator, production-row, source URI, and source-product identifiers; expose ambiguity and duplicate state. |
| Time | Keep source update, well event, production period, retrieval, release, and correction times distinct. |
| Geometry | Preserve CRS, datum, method, PLSS derivation, precision, uncertainty, generalization, and correction lineage; deny unsupported precision upgrades. |
| Units and aggregation | Require explicit commodity, unit, period, aggregation scope, missingness, revision, and completeness state. |
| Rights and sensitivity | Fail closed on unknown rights, attribution, redistribution, disclaimer, exact-location, private-person, owner, parcel, or infrastructure-sensitive conditions. |
| Network boundary | Default tests and imports are offline; live transport is explicit, reviewed, bounded, credential-safe, and excluded from default CI. |
| Candidate handoff | Permit caller-owned RAW or QUARANTINE candidates only; deny direct lifecycle, receipt, proof, catalog, release, or publication writes. |
| Error hygiene | Stable reason codes; no credential, private data, restricted coordinates, or raw sensitive payloads in logs or exceptions. |
| KGS/KCC crosswalk | Preserve both sources, roles, evidence, join method, confidence, time, geometry, rights, and unmatched states; never merge authority. |
| Publication denial | A successful fetch or parse cannot create a public claim, map, tile, forecast, reserve statement, regulatory conclusion, or AI answer. |

A future live-source integration test must be opt-in, terms-reviewed, rate-limited, credential-safe, source-head-aware, and separately approved. It must not become a default CI dependency.

[Back to top](#top)

---

## Review burden

A material implementation, migration, source-access, or public-exposure change requires review appropriate to its effects:

- connector and package maintainer;
- KGS and Kansas source stewards;
- Geology / Natural Resources domain steward;
- KCC source or regulatory-context reviewer when crosswalks are affected;
- rights and attribution reviewer;
- privacy and sensitivity reviewer;
- security reviewer for transport, credentials, logs, dependencies, and endpoints;
- contract/schema reviewer;
- validation and test steward;
- migration/ADR reviewer when paths, slugs, imports, descriptors, source IDs, or package identity change;
- release steward only when a later change reaches release-candidate scope.

No one reviewer or successful connector operation may collapse source access, evidence, policy, validation, and release authority into one decision.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| This README baseline blob `252a9246b96185bcad213ea2537d8e27dc9c84dd` | **CONFIRMED** | Prior v0.1 compatibility narrative and rollback lineage. | Current runtime, tests, canonicality, or activation. |
| Exact product-path probes | **CONFIRMED at pinned base** | README-only conventional product surface and named absence list. | Exhaustive absence of differently named or unindexed files. |
| [`connectors/geology/kgs/README.md`](../geology/kgs/README.md) | **CONFIRMED v0.2** | Current path conflict, product decomposition, and source-first placement constraints. | Accepted final KGS path. |
| [`connectors/ksgs/pyproject.toml`](../ksgs/pyproject.toml) | **CONFIRMED** | Distribution `kfm-connector-ksgs`, version `0.0.0`. | Buildability, product ownership, dependencies, runner, or supported behavior. |
| [`connectors/ksgs/src/ksgs/descriptor.yaml`](../ksgs/src/ksgs/descriptor.yaml) | **CONFIRMED placeholder** | Minimal unresolved package-local metadata. | SourceDescriptor conformance, activation, rights, sensitivity, or release. |
| [KGS source catalog](../../docs/sources/catalog/kansas/ksgs.md) | **CONFIRMED document / CONFLICTED path claim** | Independent product descriptors, source-role anti-collapse, identity/time/geometry guidance, and rights/sensitivity posture. | Machine authority or presence of its proposed connector child. |
| [KGS oil-and-gas registry template](../../data/registry/geology/sources/ksgs_oil_and_gas.yaml) | **CONFIRMED file / PROPOSED template** | Existing product-ID and registry-lineage candidate. | Conforming descriptor, reviewed rights, activation, or release. |
| [Machine source-authority register](../../control_plane/source_authority_register.yaml) | **CONFIRMED** | Register status is `PROPOSED`; `entries: []`. | KGS product activation or authority. |
| [KCC regulatory connector](../kcc_oil_gas_reg/README.md) | **CONFIRMED v0.2** | Regulatory-record separation and current KCC compatibility boundary. | KGS physical or production truth. |
| Directory Rules and responsibility-root doctrine | **CONFIRMED doctrine** | Source-specific code belongs under `connectors/`; parallel authority homes and silent migrations are forbidden. | Current runtime behavior by itself. |

[Back to top](#top)

---

## ADRs and migration

This documentation-only revision does not create, move, rename, or delete a path and therefore does not select a final KGS topology.

An accepted ADR or explicit migration plan is required before materially changing:

- canonical KGS connector and product paths;
- `kgs`, `ksgs`, or product-specific package and import identities;
- publisher adapter versus independent product-package strategy;
- source-ID namespace and descriptor strategy;
- role vocabulary and mapping;
- registry topology and losing-template disposition;
- compatibility, delegation, deprecation, redirect, mirror, or sunset behavior;
- fixture and test routing where a new authority lane would be created;
- lifecycle, receipt, proof, release, correction, or publication ownership.

The migration record must identify affected imports, packages, product dispatch, descriptors, registry entries, fixtures, tests, credentials, workflows, receipts, source IDs, documentation backlinks, data lineage, correction behavior, and rollback target.

[Back to top](#top)

---

## Rollback

Before merge, close the scoped pull request and abandon its branch.

After merge, create a transparent revert that restores prior blob:

```text
252a9246b96185bcad213ea2537d8e27dc9c84dd
```

Do not rewrite shared history. Reverting this README does not resolve the KGS placement, slug, descriptor, registry, role, fixture, test, rights, sensitivity, activation, or release conflicts.

Rollback is required if this README is used to justify:

- a canonical-path or package decision not accepted by governance;
- live source access or activation;
- use of unresolved descriptor templates as authority;
- KGS/KCC or observation/aggregate/interpreted-record collapse;
- unsupported well-level attribution of lease or field production;
- permissive inference from `sensitivity_floor: public`;
- exact-location, owner, parcel, or infrastructure exposure without review;
- direct lifecycle writes, evidence closure, release, or publication from connector code.

[Back to top](#top)

---

## Definition of done

This lane remains a documentation-only compatibility boundary until all applicable items are satisfied:

- [ ] One accepted KGS source-first connector topology and package identity are recorded.
- [ ] The disposition of `connectors/kgs/`, `connectors/ksgs/`, proposed `connectors/kansas/kgs/`, `connectors/geology/kgs/`, and top-level KGS product paths is explicit and reversible.
- [ ] Product routing for oil-and-gas wells and production is defined without collapsing other KGS products.
- [ ] A conforming, reviewed product-specific `SourceDescriptor` and activation decision exist in accepted authority surfaces.
- [ ] The proposed registry template is migrated, corrected, superseded, or retired without creating parallel authority.
- [ ] Source role, well/lease/field/production identity, time, geometry, precision, unit, aggregation, rights, disclaimer, and sensitivity contracts are accepted.
- [ ] Default-offline imports and tests are implemented and observed.
- [ ] Synthetic or explicitly rights-cleared fixtures have generation, rights, sensitivity, provenance, and expected-outcome notes.
- [ ] KGS/KCC and observation/aggregate/interpreted-product anti-collapse tests pass.
- [ ] Candidate-only RAW/QUARANTINE handoff and direct-write denial are tested.
- [ ] Security review covers transport, credentials, rate limits, retries, logging, and dependencies.
- [ ] No public operational, drilling, reservoir, reserve, investment, regulatory, title, owner, parcel, hydrology, or geology claim is created by connector code.
- [ ] Correction, supersession, deactivation, migration, and rollback paths are tested.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Final KGS connector, package, and product topology | **CONFLICTED / NEEDS VERIFICATION** | Accepted ADR or migration plan plus repository implementation. |
| `kgs` versus `ksgs` naming | **CONFLICTED** | Accepted package, import, catalog, and source-ID decision. |
| Publisher adapter versus independent oil-and-gas package | **UNKNOWN** | Product-dispatch contract, ownership decision, and tests. |
| Product-specific SourceDescriptor | **NOT VERIFIED** | Conforming reviewed descriptor and validation output. |
| Registry-template disposition | **NEEDS VERIFICATION** | Migration, supersession, correction, or retirement record. |
| Source-role vocabulary | **CONFLICTED / NEEDS VERIFICATION** | Accepted contract/schema vocabulary and migration mapping. |
| Current KGS access methods and source heads | **UNKNOWN** | Source-steward review and bounded transport evidence. |
| Rights, attribution, redistribution, and disclaimers | **NEEDS VERIFICATION** | Current product terms and rights decision. |
| Well, lease, field, production-row, and API-number identity | **NEEDS VERIFICATION** | Source schema samples, contracts, fixtures, and collision tests. |
| Time and revision semantics | **NEEDS VERIFICATION** | Source documentation, fixtures, and temporal tests. |
| Geometry, datum, PLSS derivation, and precision | **NEEDS VERIFICATION** | Source fields, geometry contract, uncertainty policy, and tests. |
| Production units and aggregation scope | **NEEDS VERIFICATION** | Source schema, unit vocabulary, aggregation contract, and tests. |
| Sensitive-location and private-data posture | **NEEDS VERIFICATION** | Policy, reviewers, public-safe fixtures, and redaction/generalization tests. |
| KGS/KCC crosswalk behavior | **NEEDS VERIFICATION** | Crosswalk contract, ambiguity handling, independent evidence refs, and negative tests. |
| Fixture homes and expected outcomes | **UNKNOWN** | Accepted fixture routing, generation notes, and consuming tests. |
| Executable product tests and CI discovery | **UNKNOWN** | Test files, runner, workflow command, logs, and coverage evidence. |
| Activation, deployment, evidence closure, and release | **NOT VERIFIED / DENIED BY DEFAULT** | Accepted activation, runtime evidence, policy decisions, proofs, manifests, and rollback target. |

---

## Last reviewed

**2026-07-13** — repository-grounded v0.2 revision against base commit `a05b61a289cf5c87fb9d9173103c6d597a0c459d`.

[Back to top](#top)
