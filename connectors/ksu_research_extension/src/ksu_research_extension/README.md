<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksu-research-extension-src-package-readme
title: connectors/ksu_research_extension/src/ksu_research_extension/ — KSU Research and Extension Greenfield Compatibility Package Scaffold
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas/KSU source steward · Agriculture steward · Atmosphere steward · Soil steward · Flora steward · Hazards steward · Rights reviewer · Sensitivity/privacy reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; greenfield-scaffold; compatibility-path; canonical-family-migration; umbrella-and-product-conflict; source-admission; rights-fail-closed; sensitivity-fail-closed; no-network; no-activation; no-life-safety; no-publication
current_path: connectors/ksu_research_extension/src/ksu_research_extension/README.md
truth_posture: CONFIRMED 0.0.0 scaffold, empty initializer, comment-only fetch/admit files, four-field local descriptor, absent proposed helper modules, absent named conventional tests, and README-only local test lane / CONFLICTED package migration, product dispatch, SourceDescriptor machine authority, narrative-to-machine role mapping, umbrella-versus-product identity, and local sensitivity floor / PROPOSED future compatibility and admission contract / UNKNOWN buildability, executable tests, runtime, source activation, current access and rights, substantive CI enforcement, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 84f46a1625d218ae5ceb52ff955e3179fe1458e2
  prior_blob: 1d7a7b99f1e0c48b7588c33746b1dfbb0ea829e6
  readme_introduction_commit: bf73f98e749a2687538f44f716b87ccc87c2f12b
related:
  - ../README.md
  - ../../README.md
  - ../../pyproject.toml
  - ../../tests/README.md
  - ../../../README.md
  - ../../../kansas/README.md
  - ../../../kansas/mesonet/README.md
  - ../../../../CONTRIBUTING.md
  - ../../../../.github/CODEOWNERS
  - ../../../../.github/workflows/connector-gate.yml
  - ../../../../.github/workflows/source-descriptor-validate.yml
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../../../docs/sources/catalog/kansas/ksu-research-extension.md
  - ../../../../docs/sources/catalog/ksu_research_extension.md
  - ../../../../docs/sources/catalog/kansas/kansas-mesonet.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/domains/agriculture/README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../docs/domains/soil/README.md
  - ../../../../contracts/source/source_descriptor.md
  - ../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../../data/registry/sources/README.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../policy/rights/README.md
  - ../../../../policy/sensitivity/README.md
  - ../../../../release/
tags: [kfm, connectors, ksu, k-state, research-extension, extension, package, python, greenfield, compatibility, agriculture, atmosphere, soil, flora, hazards, source-admission, source-role, rights, sensitivity, freshness, raw, quarantine, no-network, no-publication]
notes:
  - "Direct reads at the pinned base confirm project version 0.0.0, an empty __init__.py, comment-only fetch.py and admit.py files, and a four-field descriptor.yaml placeholder."
  - "The exact proposed helper modules descriptors.py, parse.py, normalize.py, roles.py, identity.py, freshness.py, handoff.py, and errors.py were absent at the inspected base."
  - "The exact source-profile-proposed connectors/kansas/ksu-research-extension/README.md path was absent; connectors/kansas/ is canonical family placement, but its current direct-child inventory does not include KSU R&E."
  - "Kansas Mesonet has a separate repository-present product-admission lane at connectors/kansas/mesonet/; this umbrella package must not absorb Mesonet access, consent, station, cadence, or quality rules."
  - "The connector-local descriptor uses deprecated minimal aliases, leaves role and rights unresolved, and asserts sensitivity_floor: public; it is not a conforming SourceDescriptor, registry record, activation decision, sensitivity clearance, or release authorization."
  - "Only this Markdown file is in scope. No code, package metadata, descriptor, registry entry, fixture, test, workflow, policy, schema, source payload, activation decision, lifecycle artifact, release object, path move, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSU Research and Extension Greenfield Compatibility Package Scaffold

> Repository-grounded boundary for the Python namespace at `connectors/ksu_research_extension/src/ksu_research_extension/`. The package exists, but it is a non-operational `0.0.0` scaffold inside a top-level snake_case compatibility lane. The proposed Kansas-family child is not present at the exact documented path, and package migration, import identity, and product layout have not been accepted.

**Document lifecycle:** `draft`  
**Component maturity:** `CONFIRMED` greenfield scaffold · no supported fetch, admission, lifecycle, or public behavior  
**Owner:** `OWNER_TBD`  
**Authority level:** package inside a noncanonical compatibility lane; Kansas family placement is confirmed, but the final KSU R&E child path and package migration are `CONFLICTED / NEEDS VERIFICATION`  
**Boundary:** no live network, no activation, no package-local authority, no direct lifecycle persistence, no emergency or regulatory authority, no release, no publication

> [!IMPORTANT]
> `fetch.py` and `admit.py` contain comments only, `__init__.py` is empty, and `descriptor.yaml` is a nonconforming placeholder. Nothing in the inspected package fetches K-State Research and Extension material, makes an admission decision, emits a candidate envelope, writes to a lifecycle root, or creates a public claim.

> [!CAUTION]
> `sensitivity_floor: public` in the connector-local placeholder is **not** a public-safety determination. K-State R&E is an umbrella over products with different roles, rights, privacy, freshness, and release burdens. Unresolved product identity, rights, private-land exposure, or advisory context fails closed.

**Quick links:** [Purpose](#purpose) · [Current package](#current-package) · [Repository fit](#repository-fit) · [Descriptor and activation conflict](#descriptor-and-activation-conflict) · [Product boundaries](#ksu-research-and-extension-product-and-role-boundaries) · [Sensitivity and public use](#sensitivity-and-public-use-boundary) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Inputs and outputs](#inputs-and-outputs) · [Implementation boundary](#implementation-boundary) · [Failure contract](#failure-contract) · [Validation](#validation) · [Evidence](#evidence) · [Review and migration](#review-migration-and-rollback) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Definition of done](#definition-of-done)

---

## Purpose

This README records what the current Python namespace is, what it demonstrably does not do, and which placement, source, policy, packaging, and validation gates must close before implementation begins.

Today the package is useful only as:

- a visible marker for the live `ksu_research_extension` scaffold;
- a fail-closed boundary around placeholder code and metadata;
- a record of the unresolved migration from the top-level snake_case compatibility lane to an accepted Kansas-family child;
- a product and source-role anti-collapse contract for future maintainers;
- a review and rollback input for a later package or connector migration decision.

The intended audience is connector and package maintainers, Kansas/KSU source stewards, Agriculture, Atmosphere, Soil, Flora, and Hazards stewards, rights and sensitivity/privacy reviewers, security reviewers, validation/test stewards, and migration reviewers.

This README does not prove that the current package path should survive, that `ksu_research_extension` is the final package or source-ID slug, that one adapter should represent every K-State R&E product, or that any source is approved for access, admission, transformation, or release.

[Back to top](#top)

---

## Current package

Direct file reads at base commit `84f46a1625d218ae5ceb52ff955e3179fe1458e2` confirm this bounded surface:

```text
connectors/ksu_research_extension/
├── pyproject.toml                  # project kfm-connector-ksu_research_extension, version 0.0.0
├── src/
│   ├── README.md                   # stale compatibility source-layout outline
│   └── ksu_research_extension/
│       ├── README.md               # this package boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only greenfield placeholder
│       ├── admit.py                # comment-only greenfield placeholder
│       └── descriptor.yaml         # four-field greenfield placeholder
└── tests/
    └── README.md                   # documentation boundary; no named conventional tests found
```

| Surface | Confirmed state | Consequence |
|---|---|---|
| [`pyproject.toml`](../../pyproject.toml) | Declares `kfm-connector-ksu_research_extension` at `0.0.0`; no build system, dependencies, Python constraint, package-discovery rule, entry point, or command is declared. | Buildability, installability, supported runtime, dependency posture, and package API are `UNKNOWN`. |
| [`__init__.py`](./__init__.py) | Empty file. | No package API or import-time behavior is implemented. |
| [`fetch.py`](./fetch.py) | Comment-only placeholder. | No transport, endpoint, authentication, retry, timeout, rate-limit, pagination, caching, source-head, or freshness behavior exists. |
| [`admit.py`](./admit.py) | Comment-only placeholder. | No descriptor resolution, validation, quarantine, admission, receipt, or handoff behavior exists. |
| [`descriptor.yaml`](./descriptor.yaml) | `name: ksu_research_extension`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public`. | Incomplete and unsafe as an activation basis; not a conforming descriptor or authority record. |
| [`src/README.md`](../README.md) | States that only the source-layout README and child package README were confirmed. Direct package-file reads prove additional placeholder files exist. | Treat the parent inventory as stale documentation, not current package evidence. |
| [`tests/README.md`](../../tests/README.md) | Documentation contract at the inspected path. Exact probes for `test_fetch.py`, `test_admit.py`, `test_descriptor.py`, and `conftest.py` returned `Not Found`. | Package tests, discovery, coverage, and CI enforcement are absent or `UNKNOWN`. |

Exact probes for the v0.1 README's proposed `descriptors.py`, `parse.py`, `normalize.py`, `roles.py`, `identity.py`, `freshness.py`, `handoff.py`, and `errors.py` returned `Not Found` at the pinned base.

This is a bounded named-path inventory, not a complete recursive tree receipt. Differently named, generated, unindexed, or later-added files remain `UNKNOWN`.

[Back to top](#top)

---

## Repository fit

KFM's [`connectors/`](../../../README.md) root owns source-specific fetch, probe, packaging, and admission support. Source doctrine, registry instances, machine schemas, policy decisions, evidence closure, lifecycle promotion, release decisions, and public-client behavior live elsewhere.

| Surface | Current evidence | Package implication |
|---|---|---|
| [`connectors/ksu_research_extension/`](../../README.md) | Repository-present top-level `0.0.0` scaffold; its READMEs call the lane compatibility-only and noncanonical. | Presence does not grant canonical status or permission to implement. |
| [`connectors/kansas/`](../../../kansas/README.md) | Repository-present canonical Kansas source-family coordination lane. | Parent placement is confirmed; its current direct-child README inventory does not include KSU R&E. |
| `connectors/kansas/ksu-research-extension/` | Proposed by the nested source catalog; exact README probe returned `Not Found` at the pinned base. | Keep the child path `PROPOSED`; do not claim implementation or migration. |
| [`connectors/kansas/mesonet/`](../../../kansas/mesonet/README.md) | Repository-present Kansas Mesonet product-admission lane with its own access, consent, cadence, station, and quality boundaries. | Mesonet remains a separate product lane and must not be absorbed into this umbrella package. |
| [Nested KSU R&E source catalog](../../../../docs/sources/catalog/kansas/ksu-research-extension.md) | Draft umbrella brief that proposes product-specific identities, roles, rights, cadences, and a Kansas-family kebab-case child. | Human-facing planning evidence, not machine activation authority. |
| [Legacy flat catalog stub](../../../../docs/sources/catalog/ksu_research_extension.md) | Repository-present generated stub that still points to the top-level connector and an older descriptor path. | Stale/conflicting documentation until separately redirected, superseded, or retired. |
| [`SourceDescriptor` contract](../../../../contracts/source/source_descriptor.md) | Rich draft contract and admission semantics. | The local four-field YAML does not satisfy it. |
| Machine source-authority register | [`entries: []`](../../../../control_plane/source_authority_register.yaml). | No accepted machine authority or activation entry was verified. |
| Rights and sensitivity policy | [`policy/rights/`](../../../../policy/rights/README.md) and [`policy/sensitivity/`](../../../../policy/sensitivity/README.md) are greenfield stubs. | Unknown rights or sensitivity cannot be replaced by package-local assumptions. |

The exact compatibility disposition of the current package is unresolved. Calling it `legacy`, `transitional`, `deprecated`, `mirror`, or removable would each require migration evidence not verified here.

Choosing, renaming, consolidating, or deleting this lane may affect imports, source IDs, per-product descriptors, fixtures, receipts, backlinks, and lineage. Resolve that work through an accepted ADR or explicit migration plan with rollback; this README does not select a winner.

[Back to top](#top)

---

## Descriptor and activation conflict

[`descriptor.yaml`](./descriptor.yaml) is not a usable `SourceDescriptor`.

| Connector-local field | Current value | Current contract posture |
|---|---|---|
| `name` | `ksu_research_extension` | Not the canonical required `source_id`; the package is an institutional umbrella rather than one source product. |
| `role` | `TBD` | Deprecated alias; one role cannot represent extension publications, aggregates, observations, models, lab outputs, and advisories. |
| `rights` | `TBD` | Unresolved rights must fail closed. |
| `sensitivity_floor` | `public` | Deprecated alias and unsafe as a permissive default while product identity, rights, private-land exposure, privacy, source head, and review state are unresolved. |

The [`SourceDescriptor` contract](../../../../contracts/source/source_descriptor.md) and [paired singular-path schema](../../../../schemas/contracts/v1/source/source_descriptor.schema.json) require a much richer closed object: identity and version, source type and role, authority rank, publisher and steward, rights, sensitivity, cadence, access, citation, source-head evidence, admissibility limits, public-release posture, review state, release state, and lifecycle state.

The same schema:

- declares [`schemas/contracts/v1/sources/source_descriptor.schema.json`](../../../../schemas/contracts/v1/sources/source_descriptor.schema.json) canonical while calling its own singular path legacy;
- retains `role` and `sensitivity_floor` only as deprecated migration aliases;
- requires the richer field set before canonical validation.

The plural-path schema is currently an empty permissive `PROPOSED` scaffold. Therefore schema-home and machine-validation authority remain `CONFLICTED`.

Consequences:

- do not load the local YAML as a registry or activation authority;
- do not infer public safety from `sensitivity_floor: public`;
- do not assign one role, right, cadence, or release class to every K-State R&E surface;
- do not place authoritative descriptors or activation decisions in this package;
- do not enable transport until conforming per-product descriptors, review state, and activation decisions exist in accepted authority surfaces;
- do not treat any descriptor as proof that source claims are true or approved for release.

The machine [source-authority register](../../../../control_plane/source_authority_register.yaml) is `PROPOSED` with `entries: []`. The inspected [rights](../../../../policy/rights/README.md) and [sensitivity](../../../../policy/sensitivity/README.md) policy READMEs are greenfield stubs. Those facts reinforce default deny; they do not authorize package-local substitutes.

[Back to top](#top)

---

## KSU Research and Extension product and role boundaries

K-State Research and Extension is an institutional umbrella, not one homogeneous dataset. Admission must identify the exact product and the kind of support it provides.

| Product or record class | Meaning to preserve | Candidate role posture | Must not become |
|---|---|---|---|
| Extension publications, bulletins, fact sheets, and advisory documents | Published research or outreach material with edition, topic, authorship, date, and caveats. | `administrative` as a publication record; `aggregate` when the document carries summarized statistics. | A direct observation, regulatory instrument, emergency order, or universally current recommendation. |
| Variety trials and crop-performance reports | Trial design, cultivar, plot or aggregate unit, season, site, methods, and results. | `aggregate` for published summaries; `observed` only for reviewed plot-level records with method and location controls. | A statewide yield guarantee, a private-field fact, or a regulatory seed determination. |
| Soil-testing laboratory outputs | Sample result tied to method, units, collection context, and laboratory process. | `observed` at sample level; often restricted when linked to a landowner, parcel, address, or private field. | Public parcel truth, complete soil-map truth, or unrestricted landowner record. |
| Agricultural Experiment Station weather, agronomy, and research-station outputs | Station or trial observations and any separately identified derived indices. | `observed` for direct measurements; `modeled` for derived products. | Kansas Mesonet data, area-wide current conditions, or observation/model collapse. |
| Drought, pest, disease, and crop-management advisories | Time-bounded advisory context, assumptions, geographic applicability, and update state. | `administrative` or `modeled`, depending on the product. | Regulatory authority, emergency alert, medical/veterinary directive, or life-safety decision. |
| Kansas Mesonet observations and metadata | Product-specific station, variable, depth/height, cadence, quality, preliminary-data, and consent posture. | Governed in the separate [`connectors/kansas/mesonet/`](../../../kansas/mesonet/README.md) lane. | An umbrella KSU R&E sub-feed implemented here or an inherited automated-ingest permission. |
| Mixed institutional packages | Multiple products or meanings combined in one archive, portal, or publication bundle. | Split into product-specific mappings or quarantine until identity and role can be represented safely. | One untyped all-purpose “KSU R&E” feed. |

Additional anti-collapse rules:

1. K-State R&E is **not** a `C7-10` Kansas-First Domain Authority in the current source catalog.
2. Research and extension advice is not regulatory authority.
3. An aggregate county or regional summary is not a per-place observation.
4. A modeled suitability, drought, pest, or stress product is not a direct measurement.
5. A publication record is not the substantive evidence inside every publication.
6. Kansas Mesonet product identity, access consent, cadence, quality, and correction rules remain in its own lane.
7. Institutional affiliation does not erase per-product rights, privacy, sensitivity, or freshness requirements.

[Back to top](#top)

---

## Sensitivity and public-use boundary

KSU R&E material is not uniformly public-safe merely because an upstream page or publication is public.

Fail closed or require explicit review for:

- soil-test records linked to a person, address, parcel, farm, field, or landowner;
- plot- or field-level variety-trial records whose geometry or ownership is not approved for repository use;
- unpublished or partner-restricted research-station data;
- producer, client, subscriber, contact, or service-account information;
- private-land management, input, disease, pest, or yield records;
- exact infrastructure, sensor, laboratory, or operational details that create security or misuse risk;
- preliminary or corrected measurements whose revision status is not preserved;
- advisories that may be stale, geographically inapplicable, or misused as regulatory, emergency, medical, veterinary, or life-safety direction;
- rights, attribution, redistribution, automation, or derivative-use terms that have not been verified.

Public or publicized upstream access does not by itself establish:

- automated-ingest permission;
- redistribution permission;
- permission to join the record to private land or living persons;
- permission to publish precise geometry;
- currentness or fitness for a specific decision;
- EvidenceBundle closure;
- KFM release approval.

No source record or generated summary from this package may be presented as current public advice without product identity, source date, freshness state, method, caveats, rights, policy, review, evidence, and release support.

[Back to top](#top)

---

## What belongs here

Only after placement and source-governance decisions are accepted, this package may contain or expose:

- compatibility imports or transparent redirects whose removal date and rollback are documented;
- product-dispatch helpers that require an explicit product identifier;
- opt-in transport clients whose endpoints, authentication, consent, terms, timeout, retry, rate-limit, and source-head rules are approved per product;
- source-native parsers that preserve original fields, identifiers, units, dates, geometry, and caveats;
- deterministic product and source-role preservation helpers;
- freshness and supersession preservation helpers;
- validation that prepares `RAW` or `QUARANTINE` candidates without upgrading source material to evidence;
- safe, minimal, synthetic or rights-cleared fixture helpers referenced from the accepted fixture root;
- deterministic operational result objects whose machine contract is accepted elsewhere;
- migration shims that prevent the top-level package from becoming a second canonical implementation.

A future package may share low-level helpers across products only when each operation receives a reviewed product identity and descriptor reference. Institutional common ownership is not a substitute for product dispatch.

[Back to top](#top)

---

## What does not belong here

This package must not own or imply authority over:

- one all-purpose descriptor for “KSU Research and Extension” as an institution;
- source activation or product-admission decisions;
- canonical `SourceDescriptor` instances, source-authority entries, role vocabularies, contracts, or schemas;
- rights, sensitivity, privacy, consent, access, redaction, public-precision, or release policy;
- Kansas Mesonet transport, station identity, variable, cadence, quality, or consent behavior;
- private client, producer, landowner, parcel, field, or soil-test identity as public data;
- advisory, emergency, regulatory, medical, veterinary, or life-safety authority;
- canonical Agriculture, Atmosphere, Soil, Flora, or Hazards objects;
- transformation that silently turns source fields into canonical fields;
- cross-product joins, aggregates, models, or inference without downstream governed pipelines;
- direct writes to `WORK`, `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`, proof, receipt-authority, or release stores;
- `EvidenceBundle`, catalog, graph, proof-pack, release-manifest, correction, withdrawal, or rollback authority;
- public APIs, maps, dashboards, alerts, recommendations, or AI answers;
- credentials, tokens, cookies, private URLs, private exports, or unreviewed payloads;
- independent evolution of this top-level package as a second canonical Kansas KSU R&E implementation;
- generated language presented as observation, research conclusion, advisory, regulatory, or release truth.

A fetched file is not an admitted source. An admitted source is not validated evidence. Validated evidence is not a released public claim.

[Back to top](#top)

---

## Inputs and outputs

### Current inputs

None. The package declares no supported function, class, command, configuration contract, endpoint, credential variable, descriptor resolver, product dispatcher, or fixture format.

### Current outputs

None. The placeholders emit no payload, candidate envelope, receipt, validation report, `RAW` record, `QUARANTINE` record, or public artifact.

### Future admissible inputs

Only after placement and activation gates are accepted, a narrow package contract may accept:

- a conforming, reviewed, product-specific `SourceDescriptor` reference;
- an explicit activation decision and approved access configuration;
- an exact product identifier, source version, edition, or release identifier;
- caller-supplied bytes, files, or approved transport results;
- synthetic or rights-cleared no-network fixtures;
- explicit run identity, retrieval time, source-head evidence, and destination intent;
- caller-owned `RAW`-candidate, `QUARANTINE`-candidate, and receipt-candidate sinks;
- product-specific freshness, correction, and supersession expectations.

### Future admissible outputs

A future package may return deterministic fetch results, parse results, validation failures, or `RAW`/`QUARANTINE` candidate envelopes to governed orchestration.

It must not:

- choose public release;
- persist directly into later lifecycle roots;
- convert connector success into evidence or truth;
- treat a process-memory receipt candidate as proof closure;
- return a public advisory or recommendation.

The exact DTOs, finite outcome vocabulary, reason codes, sink protocol, idempotency contract, and receipt type remain `PROPOSED / NEEDS VERIFICATION`.

[Back to top](#top)

---

## Implementation boundary

No operational code should be added merely because this import namespace exists.

Before implementation, maintainers must resolve:

1. **Package placement** — retain this compatibility namespace, move it, replace it with a redirect, or retire it.
2. **Import and source identity** — define package name, product IDs, source IDs, and migration aliases.
3. **Product dispatch** — identify which KSU R&E products are in scope and keep Kansas Mesonet separate.
4. **Descriptor authority** — settle schema path, machine role vocabulary, registry home, and activation authority.
5. **Access and rights** — verify endpoints or files, terms, attribution, redistribution, automation permission, credentials, rate limits, and cadence for each product.
6. **Sensitivity and privacy** — define private-land, producer/client, soil-test, plot-level, unpublished-research, infrastructure, and advisory controls.
7. **Candidate-envelope contract** — define immutable source preservation, source-head evidence, checksums, failure outcomes, and caller-owned sinks.
8. **Fixtures and tests** — provide no-network positive and negative coverage without carrying private or unsafe records.
9. **Migration and rollback** — preserve history, imports, descriptors, receipts, backlinks, corrections, and revert targets.

A future implementation should prefer narrow product adapters or a dispatcher over one institution-wide parser.

[Back to top](#top)

---

## Failure contract

The package must fail closed. Exact machine reason codes remain `PROPOSED`; the behavioral contract is:

| Condition | Required package outcome | Forbidden fallback |
|---|---|---|
| Missing or nonconforming product descriptor | `DENY_NO_ACTIVATION` or deterministic hold | Guess product role or use local YAML as authority. |
| Missing activation decision | `DENY_NO_ACTIVATION` | Fetch because the source is public or institutional. |
| Unknown rights, attribution, redistribution, or automation permission | `QUARANTINE_CANDIDATE` or hold | Assume public-web access authorizes ingest and reuse. |
| Missing product identity | `QUARANTINE_CANDIDATE` | Route all material through one KSU umbrella identity. |
| Source-role ambiguity | `QUARANTINE_CANDIDATE` | Infer role from filename, folder, institution, or user convenience. |
| Kansas Mesonet material presented to this umbrella package | `DENY_WRONG_PRODUCT_LANE` or explicit redirect after migration approval | Parse it here or inherit Mesonet consent. |
| Private-land, client, parcel, field, plot, or soil-test identity unresolved | `QUARANTINE_CANDIDATE` or `DENY_SENSITIVE` | Emit public detail or precise geometry. |
| Missing source date, edition, cadence, source head, or freshness state | `QUARANTINE_CANDIDATE` | Present stale material as current advice. |
| Advisory requested as regulatory, emergency, medical, veterinary, or life-safety authority | `DENY_OUT_OF_SCOPE` | Produce an authoritative public directive. |
| Source shape, unit, identifier, or integrity drift | `QUARANTINE_CANDIDATE` | Silently coerce or normalize into canonical truth. |
| Unapproved live network in default/test mode | `ERROR_NETWORK_DISABLED` | Contact the source. |
| Output sink is not a governed caller-owned candidate interface | `ERROR_INVALID_SINK` | Write directly to a lifecycle or release root. |
| Same source head and run identity already handled | Deterministic `NO_OP` when the accepted contract allows | Duplicate writes or mutate prior material. |

Failures must preserve enough non-sensitive context for audit: product identifier if known, descriptor reference, run identity, source-head evidence, failure class, retrieval time, and safe diagnostic details. Do not log credentials, private payloads, personal information, precise private geometry, or restricted research data.

[Back to top](#top)

---

## Validation

### Current validation state

No executable package validation is established by the named files inspected for this revision.

- `pyproject.toml` declares no build or test system.
- Named conventional tests were not found.
- [`connector-gate.yml`](../../../../.github/workflows/connector-gate.yml) executes TODO `echo` steps.
- [`source-descriptor-validate.yml`](../../../../.github/workflows/source-descriptor-validate.yml) executes TODO `echo` steps.

A green run of those workflow names does not prove package, descriptor, rights, sensitivity, or lifecycle correctness.

### Required future package tests

At minimum:

| Test family | Required proof |
|---|---|
| Import and side-effect | Package imports without network, filesystem writes, credential reads, or activation. |
| Placeholder rejection | Local four-field YAML cannot activate a source or authorize public treatment. |
| Product dispatch | Every operation requires an accepted product identity; umbrella-only input fails closed. |
| Mesonet separation | Kansas Mesonet input is rejected or routed only through an accepted migration adapter. |
| Source-role anti-collapse | Administrative, aggregate, observed, and modeled products remain distinguishable. |
| Rights and automation | Unknown rights or automated-ingest permission blocks fetch. |
| Freshness and source head | Date, edition, source head, correction, and staleness are preserved. |
| Privacy and sensitivity | Private-land, person, client, parcel, field, plot, soil-test, and unpublished-research cases fail closed. |
| Advisory boundary | Advisory outputs cannot be represented as regulatory, emergency, medical, veterinary, or life-safety authority. |
| Fixture safety | No real private record, credential, restricted payload, or unsafe coordinate enters the repository. |
| Candidate boundary | Package can return only accepted `RAW`, `QUARANTINE`, receipt, no-op, denial, or operational-error candidates. |
| Lifecycle denial | No code path writes directly to later lifecycle, proof, catalog, release, API, map, or AI surfaces. |
| Migration compatibility | Accepted aliases are explicit, tested, deprecated, and removable without silent source-ID drift. |

### Documentation checks for this file

Review should verify:

- one H1 and coherent heading hierarchy;
- balanced metadata, code fences, tables, callouts, and links;
- preserved `doc_id`, creation date, prior blob, and introduction commit;
- no remote badge or tracking image;
- no credential, private endpoint, personal record, soil-test result, plot location, or restricted payload;
- current-state claims remain bounded to the pinned repository evidence;
- the diff contains only `connectors/ksu_research_extension/src/ksu_research_extension/README.md`.

[Back to top](#top)

---

## Evidence

| Evidence | What it supports | What it does not prove |
|---|---|---|
| Target blob `1d7a7b99f1e0c48b7588c33746b1dfbb0ea829e6` at the pinned base | Exact editing baseline and stale proposal-heavy v0.1 language. | Runtime, activation, or product readiness. |
| Introduction commit `bf73f98e749a2687538f44f716b87ccc87c2f12b` | The v0.1 README replaced a blank placeholder. | That restoring a blank file is the preferred current rollback. |
| Current package files | `0.0.0` project metadata, empty initializer, comment-only fetch/admit placeholders, and four-field local descriptor exist. | Any executable behavior or supported API. |
| Exact absent helper probes | The eight helper names proposed in v0.1 were not present at the pinned base. | Absence of all differently named implementation. |
| Exact absent named test probes | Common local test files were not present at the pinned base. | Absence of every differently named or external test. |
| [`connectors/ksu_research_extension/README.md`](../../README.md) and [`src/README.md`](../README.md) | Existing top-level lane declares compatibility intent and points toward Kansas-family migration. | A completed migration or correct current inventory. |
| [`connectors/kansas/README.md`](../../../kansas/README.md) | Kansas is the canonical family coordination lane; current direct child topology is provisional. | Presence of the proposed KSU child. |
| Exact `connectors/kansas/ksu-research-extension/README.md` probe | The source-profile-proposed child README was not found at the pinned base. | Absence of every differently named KSU implementation. |
| [Nested KSU R&E catalog](../../../../docs/sources/catalog/kansas/ksu-research-extension.md) | Umbrella-versus-product model, candidate product classes, role distinctions, rights/freshness gaps, and proposed kebab-case child. | Accepted machine descriptors, current endpoints, or activation. |
| [Legacy flat catalog stub](../../../../docs/sources/catalog/ksu_research_extension.md) | A stale generated source-family stub remains and points to the top-level lane. | Current canonical catalog or descriptor authority. |
| [Kansas Mesonet product lane](../../../kansas/mesonet/README.md) | Mesonet is independently governed and carries product-specific access/consent/cadence/quality boundaries. | Permission for this package to fetch or parse Mesonet. |
| [`SourceDescriptor` contract](../../../../contracts/source/source_descriptor.md) and both schema paths | Rich descriptor semantics exist, while schema path and enforceable authority conflict. | A valid KSU descriptor or activation decision. |
| Empty [source-authority register](../../../../control_plane/source_authority_register.yaml) | No machine authority entry was verified in that register. | Absence from every differently named registry artifact. |
| Rights/sensitivity READMEs and TODO-only workflows | Enforcement is not established by those inspected files. | Absence of all policy or CI behavior elsewhere. |

Absence claims are bounded to the exact paths, indexed searches, and pinned commit. This README does not assert a complete recursive repository inventory.

[Back to top](#top)

---

## Review, migration, and rollback

### Review burden

Substantive package, source, descriptor, or migration work should involve:

- connector steward;
- package maintainer;
- Kansas/KSU source steward;
- Agriculture steward;
- Atmosphere steward for weather, climate, and station material;
- Soil steward for laboratory and soil-measurement material;
- Flora steward for cultivar and plant-context material;
- Hazards steward for drought, pest, disease, and advisory context;
- rights reviewer;
- sensitivity/privacy reviewer;
- security reviewer where credentials, private endpoints, or infrastructure detail are involved;
- validation/test steward;
- docs steward.

The current `.github/CODEOWNERS` provides a repository-wide fallback but no KSU R&E package-specific owner. Team existence, assignment, and reviewer availability remain `NEEDS VERIFICATION`; this README does not invent usernames.

### Migration requirements

Any move, redirect, alias, or retirement must preserve:

- Git history and review trail;
- Python import compatibility or an explicit breaking-change notice;
- source and product IDs;
- descriptor, activation, and source-head lineage;
- fixtures, tests, and CI discovery;
- receipts and candidate-envelope references;
- documentation backlinks and catalog references;
- correction, supersession, withdrawal, and rollback paths;
- a time-bounded deprecation plan for the top-level snake_case package.

Do not copy the package into a second path and let both evolve.

### Rollback

Before merge, close the review branch if the revision is rejected.

After merge, create a transparent revert that restores prior README blob `1d7a7b99f1e0c48b7588c33746b1dfbb0ea829e6`. Do not reset, force-push, or rewrite shared history.

The blank placeholder predates v0.1, but the safe current rollback target is the exact prior blob—not an invented reconstruction of the blank file.

[Back to top](#top)

---

## ADRs

- [Directory Rules](../../../../docs/doctrine/directory-rules.md) govern the `connectors/` responsibility root, family placement, compatibility roots, README contracts, and migration discipline.
- [ADR-0012](../../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) is present as a draft/proposed numbered connector-boundary decision. Directory Rules remain the governing authority while the ADR is not accepted.
- No accepted path-specific ADR was verified that resolves:
  - migration or retirement of `connectors/ksu_research_extension/`;
  - the final Kansas-family child slug;
  - package/import/source-ID compatibility;
  - umbrella versus product adapter topology;
  - `SourceDescriptor` schema and role-vocabulary authority.
- This README update does not itself trigger a new ADR: it edits one existing Markdown file, moves no path, creates no authority home, and changes no lifecycle boundary.
- Future path, source-ID, import, descriptor-authority, or product-topology decisions require the applicable accepted ADR or explicit migration record.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Review date | `2026-07-13` |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Base ref | `main` |
| Pinned base commit | `84f46a1625d218ae5ceb52ff955e3179fe1458e2` |
| Prior README blob | `1d7a7b99f1e0c48b7588c33746b1dfbb0ea829e6` |
| README introduction commit | `bf73f98e749a2687538f44f716b87ccc87c2f12b` |
| Review scope | Target README/history; project/package placeholder files; proposed helper names; named conventional test files; parent compatibility READMEs; Kansas family and Mesonet lanes; nested and flat source catalog pages; Directory Rules; connector-output ADR; SourceDescriptor contract and both schema paths; source-authority register; rights/sensitivity stubs; connector and descriptor workflow stubs; branch/PR overlap search |
| Reviewer identity | `OWNER_TBD` — no semantic owner assignment made by this document |

[Back to top](#top)

---

## Definition of done

This package is not implementation-ready until all applicable items are complete:

- [ ] An accepted migration or ADR resolves the final package path, import name, source-ID aliases, and disposition of the top-level snake_case lane.
- [ ] In-scope KSU R&E products are enumerated and each has a stable product identity.
- [ ] Kansas Mesonet remains in its separately governed product lane.
- [ ] Product-specific conforming `SourceDescriptor`s exist in an accepted registry home.
- [ ] Source-role machine vocabulary and schema authority are settled.
- [ ] Explicit activation decisions exist for each permitted operation.
- [ ] Current access methods, endpoints or files, authentication, terms, attribution, redistribution, automation permission, rate limits, cadence, source heads, corrections, and withdrawal behavior are reviewed per product.
- [ ] Rights, privacy, private-land, soil-test, plot-level, unpublished-research, infrastructure, and public-precision controls are implemented and tested.
- [ ] Advisory products are explicitly prevented from becoming regulatory, emergency, medical, veterinary, or life-safety authority.
- [ ] The connector-local placeholder descriptor is removed, replaced with a non-authoritative fixture, or made an explicit invalid test case.
- [ ] A build backend, supported Python versions, dependency policy, package discovery, and public API are declared.
- [ ] No-network valid and invalid fixtures exist in the accepted fixture home.
- [ ] Executable tests cover import safety, descriptor/activation denial, product dispatch, Mesonet separation, role anti-collapse, rights, sensitivity, freshness, advisory misuse, fixture safety, candidate outputs, lifecycle denial, and migration aliases.
- [ ] CI executes substantive checks rather than TODO-only echoes.
- [ ] Candidate-envelope, reason-code, sink, checksum, idempotency, and receipt contracts are accepted.
- [ ] Migration, deprecation, correction, withdrawal, and rollback are documented and tested.
- [ ] Owners and required reviewers are assigned.
- [ ] No implementation claim is upgraded without code, tests, workflow evidence, or emitted governed artifacts.

Until then, the safe state is: **no network, no activation, no public output, no direct lifecycle persistence, and no authority inference from package presence.**

[Back to top](#top)
