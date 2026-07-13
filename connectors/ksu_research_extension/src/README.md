<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksu-research-extension-src-readme
title: connectors/ksu_research_extension/src/ — KSU Research and Extension Greenfield Compatibility Source Layout
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas/KSU source steward · Agriculture steward · Atmosphere steward · Soil steward · Flora steward · Hazards steward · Rights reviewer · Sensitivity/privacy reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; src-layout-boundary; greenfield-scaffold; compatibility-path; canonical-family-migration; umbrella-and-product-conflict; source-admission; rights-fail-closed; sensitivity-fail-closed; no-network; no-activation; no-life-safety; no-publication
current_path: connectors/ksu_research_extension/src/README.md
truth_posture: CONFIRMED source-layout path, one child package directory, merged v0.2 package README, empty initializer, comment-only fetch/admit files, four-field local descriptor, and absent named conventional package tests / CONFLICTED final package path, import/source-ID migration, KSU umbrella-versus-product topology, SourceDescriptor machine authority, narrative-to-machine role mapping, and local sensitivity floor / PROPOSED future compatibility layout and package migration contract / UNKNOWN buildability, executable tests, runtime, source activation, current access and rights, substantive CI enforcement, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: b047eef221136e0efe59a9983f1aae1340c23b70
  prior_blob: 382bec1d8442f228296f8a1824446b9c7458fb71
  readme_introduction_commit: eb3319ac6ca2634132771a9ca561a75346e21c05
related:
  - ../README.md
  - ../pyproject.toml
  - ../tests/README.md
  - ./ksu_research_extension/README.md
  - ./ksu_research_extension/__init__.py
  - ./ksu_research_extension/fetch.py
  - ./ksu_research_extension/admit.py
  - ./ksu_research_extension/descriptor.yaml
  - ../../README.md
  - ../../kansas/README.md
  - ../../kansas/mesonet/README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/connector-gate.yml
  - ../../../.github/workflows/source-descriptor-validate.yml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../../docs/sources/catalog/kansas/ksu-research-extension.md
  - ../../../docs/sources/catalog/ksu_research_extension.md
  - ../../../docs/sources/catalog/kansas/kansas-mesonet.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/domains/agriculture/README.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/soil/README.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../data/registry/sources/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../release/
tags: [kfm, connectors, ksu, k-state, research-extension, source-layout, src, python, greenfield, compatibility, agriculture, atmosphere, soil, flora, hazards, source-admission, source-role, rights, sensitivity, freshness, raw, quarantine, no-network, no-publication]
notes:
  - "Direct reads at the pinned base confirm this src layout contains one package directory with README.md, empty __init__.py, comment-only fetch.py and admit.py, and a four-field descriptor.yaml placeholder."
  - "The child package README is now v0.2 and records the package as a non-operational 0.0.0 compatibility scaffold; this parent README defines the broader src layout boundary."
  - "The exact source-profile-proposed connectors/kansas/ksu-research-extension/README.md path remains absent; connectors/kansas/ is canonical family placement, but its current direct-child inventory does not include KSU R&E."
  - "Kansas Mesonet has a separate repository-present product-admission lane at connectors/kansas/mesonet/; this source layout must not absorb Mesonet package, consent, station, cadence, or quality behavior."
  - "The connector-local descriptor is not a conforming SourceDescriptor, registry record, activation decision, sensitivity clearance, or release authorization."
  - "Only this Markdown file is in scope. No code, package metadata, descriptor, registry entry, fixture, test, workflow, policy, schema, source payload, activation decision, lifecycle artifact, release object, path move, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSU Research and Extension Greenfield Compatibility Source Layout

> Repository-grounded layout boundary for `connectors/ksu_research_extension/src/`. This directory contains the Python package namespace for a non-operational `0.0.0` compatibility scaffold. It organizes package code; it does not activate a source, decide source role, own a descriptor, persist lifecycle data, or authorize publication.

**Document lifecycle:** `draft`  
**Component maturity:** `CONFIRMED` greenfield source layout · no supported fetch, admission, lifecycle, or public behavior  
**Owner:** `OWNER_TBD`  
**Authority level:** source-layout container inside a noncanonical compatibility connector; final Kansas-family child and package migration are `CONFLICTED / NEEDS VERIFICATION`  
**Boundary:** package organization only; no live network, no activation, no package-local authority, no direct lifecycle persistence, no emergency or regulatory authority, no release, no publication

> [!IMPORTANT]
> The current source layout is not README-only. It contains an empty package initializer, comment-only `fetch.py` and `admit.py`, and a four-field `descriptor.yaml` placeholder. These files establish a scaffold, not implementation maturity.

> [!CAUTION]
> The child descriptor's `sensitivity_floor: public` value is not a sensitivity decision. K-State Research and Extension spans products with different source roles, rights, privacy, freshness, private-land, and advisory burdens. Unknown product identity, rights, automation permission, sensitivity, or freshness must fail closed.

**Quick links:** [Purpose](#purpose) · [Current layout](#current-layout) · [Authority and repository fit](#authority-and-repository-fit) · [Child package boundary](#child-package-boundary) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Product separation](#product-and-source-role-separation) · [Runtime posture](#runtime-posture) · [Validation](#validation) · [Evidence](#evidence) · [Review and migration](#review-migration-and-rollback) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Definition of done](#definition-of-done)

---

## Purpose

`connectors/ksu_research_extension/src/` is the source-layout container for the current top-level KSU Research and Extension compatibility connector.

Its responsibilities are narrow:

- organize the Python package namespace that already exists;
- make package boundaries visible to maintainers and reviewers;
- prevent placeholder files from being mistaken for working connector behavior;
- preserve the separation between KSU R&E umbrella products and independently governed product lanes such as Kansas Mesonet;
- record the unresolved package-path and import migration;
- route future implementation toward governed product-specific admission without creating authority inside `src/`.

This README is for connector and package maintainers, Kansas/KSU source stewards, Agriculture, Atmosphere, Soil, Flora, and Hazards stewards, rights and sensitivity/privacy reviewers, security reviewers, test/validation stewards, and migration reviewers.

It does not prove that this package path should survive, that the snake_case import name is final, that one package should cover every K-State R&E product, or that any source is approved for access, ingest, transformation, or release.

[Back to top](#top)

---

## Current layout

Direct reads at base commit `b047eef221136e0efe59a9983f1aae1340c23b70` confirm this bounded tree:

```text
connectors/ksu_research_extension/
├── README.md                          # top-level compatibility connector README; currently v0.1
├── pyproject.toml                     # project kfm-connector-ksu_research_extension, version 0.0.0
├── src/
│   ├── README.md                      # this source-layout boundary
│   └── ksu_research_extension/
│       ├── README.md                  # merged v0.2 package scaffold boundary
│       ├── __init__.py                # empty
│       ├── fetch.py                   # comment-only greenfield placeholder
│       ├── admit.py                   # comment-only greenfield placeholder
│       └── descriptor.yaml            # four-field greenfield placeholder
└── tests/
    └── README.md                      # documentation boundary; named conventional tests not found
```

| Surface | Confirmed state | Layout consequence |
|---|---|---|
| [`../pyproject.toml`](../pyproject.toml) | Declares `kfm-connector-ksu_research_extension` at `0.0.0`; no build backend, dependency set, Python constraint, package-discovery rule, entry point, or command is declared. | This layout does not yet define an installable or supported package. |
| [`./ksu_research_extension/README.md`](./ksu_research_extension/README.md) | v0.2 package boundary documents the package as a greenfield compatibility scaffold. | Package-level implementation and product rules live there; this README governs the enclosing layout. |
| [`./ksu_research_extension/__init__.py`](./ksu_research_extension/__init__.py) | Empty. | No package API or import-time behavior exists. |
| [`./ksu_research_extension/fetch.py`](./ksu_research_extension/fetch.py) | Comment-only placeholder. | No transport, endpoint, authentication, retry, timeout, rate-limit, source-head, or freshness behavior exists. |
| [`./ksu_research_extension/admit.py`](./ksu_research_extension/admit.py) | Comment-only placeholder. | No validation, quarantine, admission, candidate-envelope, receipt, or sink behavior exists. |
| [`./ksu_research_extension/descriptor.yaml`](./ksu_research_extension/descriptor.yaml) | `name: ksu_research_extension`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public`. | Not a conforming descriptor, authority record, activation decision, policy result, or release authorization. |
| [`../tests/README.md`](../tests/README.md) | Compatibility-test documentation exists. Exact probes for `test_fetch.py`, `test_admit.py`, `test_descriptor.py`, and `conftest.py` returned `Not Found` at the pinned base. | Executable test coverage, discovery, and CI enforcement are absent or `UNKNOWN`. |

The v0.1 source-layout README stated that only the layout README and child package README were confirmed. Direct file reads disprove that inventory. This revision replaces that stale claim with the bounded tree above.

This is not a complete recursive repository receipt. Differently named, generated, unindexed, or later-added files remain `UNKNOWN`.

[Back to top](#top)

---

## Authority and repository fit

KFM's [`connectors/`](../../README.md) root owns source-specific fetch, probe, preservation, packaging, and admission support. A `src/` directory only organizes implementation files inside that responsibility root.

| Surface | Responsibility | Current posture |
|---|---|---:|
| [`connectors/`](../../README.md) | Canonical root for source-specific connector implementation and admission support. | **CONFIRMED** |
| [`connectors/ksu_research_extension/`](../README.md) | Existing top-level snake_case compatibility connector and package scaffold. | **CONFIRMED path / NONCANONICAL per its README / root README still v0.1** |
| `connectors/ksu_research_extension/src/` | This source-layout container. | **CONFIRMED path / GREENFIELD SCAFFOLD** |
| [`connectors/kansas/`](../../kansas/README.md) | Canonical Kansas source-family coordination lane. | **CONFIRMED parent / provisional child topology** |
| `connectors/kansas/ksu-research-extension/` | Child path proposed by the nested source catalog. | **Exact README probe returned Not Found at the pinned base** |
| [`connectors/kansas/mesonet/`](../../kansas/mesonet/README.md) | Repository-present Kansas Mesonet product-admission lane. | **CONFIRMED separate product lane / final child slug still conflicted** |
| [Nested KSU R&E source catalog](../../../docs/sources/catalog/kansas/ksu-research-extension.md) | Human-facing umbrella brief with proposed per-product identities and roles. | **CONFIRMED draft documentation / not machine activation authority** |
| [Legacy flat source stub](../../../docs/sources/catalog/ksu_research_extension.md) | Generated older umbrella page pointing to the top-level connector. | **CONFIRMED stale/conflicting documentation** |
| [`SourceDescriptor` contract](../../../contracts/source/source_descriptor.md) | Semantic admission contract. | **CONFIRMED draft contract / no valid local descriptor** |
| [`data/registry/sources/`](../../../data/registry/sources/README.md) | Governed source identity and admission-record responsibility. | **Outside this layout** |
| Rights and sensitivity policy | [`policy/rights/`](../../../policy/rights/README.md) and [`policy/sensitivity/`](../../../policy/sensitivity/README.md). | **Outside this layout / inspected READMEs are greenfield stubs** |
| `release/` | Release, correction, withdrawal, and rollback authority. | **Outside this layout** |

The final package disposition is unresolved. Calling this layout `legacy`, `transitional`, `deprecated`, `mirror`, or removable would require evidence and an accepted migration decision not verified here.

The source-profile-proposed Kansas child is a proposal, not current implementation fact. Do not create a second package tree merely to make the prose true. Any destination must be accepted through migration or ADR review first.

[Back to top](#top)

---

## Child package boundary

The child [`ksu_research_extension/`](./ksu_research_extension/README.md) package README is the implementation boundary for the Python namespace. This parent layout README does not duplicate the full package contract.

The child package currently establishes:

- package maturity is a non-operational `0.0.0` scaffold;
- current inputs and outputs are none;
- the local descriptor is invalid as activation or policy authority;
- KSU R&E is an institutional umbrella that requires product-specific identity and source-role separation;
- Kansas Mesonet remains in its own product lane;
- private-land, soil-test, client, field/plot, unpublished-research, advisory, and infrastructure concerns fail closed;
- future outputs must remain caller-owned candidate envelopes and may not become evidence, release, or public truth;
- package movement requires import, source-ID, descriptor, fixture, receipt, backlink, correction, and rollback preservation.

This layout must keep those package invariants visible and must not weaken them through a broader `src/` convention.

### Local descriptor warning

The child [`descriptor.yaml`](./ksu_research_extension/descriptor.yaml) is a greenfield placeholder, not a machine authority.

The inspected [`SourceDescriptor` contract](../../../contracts/source/source_descriptor.md) and [populated singular-path schema](../../../schemas/contracts/v1/source/source_descriptor.schema.json) require a richer field set covering identity, version, source type and role, authority, publisher and steward, rights, sensitivity, cadence, access, citation, source head, admissibility, public-release posture, review state, release state, and lifecycle state.

The schema declares [`schemas/contracts/v1/sources/source_descriptor.schema.json`](../../../schemas/contracts/v1/sources/source_descriptor.schema.json) canonical while that plural-path file remains an empty permissive `PROPOSED` scaffold. Schema-home and validation authority therefore remain `CONFLICTED`.

Consequences for this layout:

- never treat package-local YAML as the canonical descriptor home;
- never infer public safety from `sensitivity_floor: public`;
- never place activation decisions, source-authority entries, policy results, or release decisions under `src/`;
- never use a package directory as evidence that a source is admitted or active;
- keep descriptor, policy, registry, test, and release authority outside the package tree.

[Back to top](#top)

---

## What belongs here

After placement and governance are accepted, this `src/` layout may contain:

- one or more Python package directories approved by the package/migration decision;
- package-level README files and compatibility notices;
- source-native transport and probe modules with no-network defaults;
- product-dispatch modules requiring explicit product identity;
- parsers that preserve source fields, identifiers, units, dates, geometry, caveats, and source-head metadata;
- deterministic source-role, rights-state, sensitivity-state, and freshness preservation helpers;
- package-local validation helpers that do not replace canonical validators or policy;
- deterministic candidate-envelope and operational-result helpers whose contracts are accepted elsewhere;
- transparent compatibility imports or redirects with documented removal and rollback;
- small test-support utilities only when they contain no source payloads or fixtures better placed in governed fixture/test roots.

A future layout should stay small. If different KSU R&E products require materially different access, rights, cadence, privacy, or parser behavior, prefer separate product adapters or a strict dispatcher over one institution-wide module.

[Back to top](#top)

---

## What does not belong here

Do not place or imply authority for any of the following under `src/`:

- canonical `SourceDescriptor` instances or source-authority registry records;
- machine schemas, semantic contracts, or source-role vocabulary decisions;
- source activation or product-admission decisions;
- rights, sensitivity, privacy, consent, access, redaction, precision, or release policy;
- source payload archives, bulk harvests, or fixture corpora;
- credentials, tokens, cookies, private URLs, account state, or secrets;
- private client, producer, landowner, parcel, field, plot, or soil-test records as package resources;
- Kansas Mesonet transport, station, variable, consent, cadence, quality, or correction logic unless an accepted architecture explicitly delegates a shared low-level helper;
- canonical Agriculture, Atmosphere, Soil, Flora, or Hazards domain objects;
- normalization that silently upgrades source fields into canonical KFM truth;
- cross-product joins, aggregates, models, or inferences that belong in governed pipelines;
- direct lifecycle writes to `WORK`, `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`, proof, receipt-authority, or release stores;
- `EvidenceBundle`, proof-pack, catalog, release-manifest, correction, withdrawal, or rollback authority;
- public APIs, maps, dashboards, alerts, recommendations, or AI answers;
- emergency, regulatory, medical, veterinary, or life-safety authority;
- generated summaries presented as observation, research conclusion, advisory, regulatory, or release truth;
- parallel packages at both compatibility and proposed canonical paths that evolve independently.

A package can fetch or parse source material without making it evidence. A successful import or connector operation is not source admission, validation, or release.

[Back to top](#top)

---

## Product and source-role separation

K-State Research and Extension is an umbrella source family. The layout must support product-specific boundaries rather than institutional collapse.

| Product class | Layout implication | Denied collapse |
|---|---|---|
| Extension publications and fact sheets | Package code must preserve publication identity, edition, authorship, date, topic, and caveats. | Publication registry treated as direct observation or regulatory instrument. |
| Variety trials and crop-performance reports | Preserve trial, site or aggregation unit, season, cultivar, method, and result context. | Aggregate result treated as private-field or statewide guaranteed truth. |
| Soil-testing outputs | Keep sample method, units, collection context, privacy, landowner/parcel links, and release limits explicit. | Private sample result treated as public parcel truth or complete soil-map truth. |
| Agricultural Experiment Station observations and models | Keep direct measurements and derived products in separate source roles. | Model treated as observation or station result treated as area-wide current conditions. |
| Drought, pest, disease, and management advisories | Preserve issue time, geographic applicability, assumptions, expiry, and caveats. | Advisory treated as regulation, emergency order, medical/veterinary directive, or life-safety instruction. |
| Kansas Mesonet | Use the separate [`connectors/kansas/mesonet/`](../../kansas/mesonet/README.md) product lane and its product-specific access/consent/quality rules. | Mesonet absorbed into the KSU umbrella package or automated-ingest permission inherited by affiliation. |
| Mixed archives or portals | Require dispatch by product identity or quarantine. | One untyped all-purpose KSU R&E feed. |

KSU R&E is not a `C7-10` Kansas-First Domain Authority in the current nested source catalog. Connector placement or package presence must not elevate institutional material into regulatory or authority-of-last-resort status.

[Back to top](#top)

---

## Runtime posture

### Current runtime

There is no supported runtime contract in the inspected source layout.

- no declared build backend or package-discovery rule;
- no supported Python version;
- no dependency or command declaration;
- no package API;
- no transport or source access;
- no admission logic;
- no candidate-envelope or sink contract;
- no executable local tests verified at the named paths;
- no activation or source-authority entry verified.

### Required default posture for future code

Any future code under this layout must default to:

- no network;
- no source activation;
- no credential or secret reads during import or default tests;
- no public output;
- no package-local descriptor, policy, or registry authority;
- no direct lifecycle or release persistence;
- product-specific identity and descriptor requirements;
- deterministic failure for unresolved rights, sensitivity, privacy, role, product identity, source head, freshness, integrity, or sink;
- caller-owned `RAW`/`QUARANTINE`/receipt-candidate interfaces only;
- no emergency, regulatory, medical, veterinary, or life-safety behavior;
- audit-safe logging without credentials, private payloads, personal information, private geometry, or restricted research data.

A live-source path, if later approved, must be opt-in, product-specific, terms-reviewed, automation-permission-reviewed, credential-safe, rate-limited, source-head-aware, auditable, and excluded from default tests.

[Back to top](#top)

---

## Validation

### Current validation evidence

No executable source-layout or package validation is established by the named files inspected for this revision.

- `pyproject.toml` declares no build or test system.
- Named conventional local tests were not found.
- [`connector-gate.yml`](../../../.github/workflows/connector-gate.yml) executes TODO `echo` steps.
- [`source-descriptor-validate.yml`](../../../.github/workflows/source-descriptor-validate.yml) executes TODO `echo` steps.
- The machine [source-authority register](../../../control_plane/source_authority_register.yaml) is `PROPOSED` with `entries: []`.
- [Rights](../../../policy/rights/README.md) and [sensitivity](../../../policy/sensitivity/README.md) policy READMEs are greenfield stubs.

A green workflow run proves only the steps the workflow actually executes. These inspected workflow definitions do not establish package, descriptor, rights, sensitivity, or lifecycle correctness.

### Required future checks

| Check family | Required proof |
|---|---|
| Layout inventory | Every package, compatibility module, and generated file is known and classified. |
| Package import | Imports produce no network, filesystem write, activation, credential read, or public side effect. |
| Placeholder rejection | Package-local descriptor cannot activate a source or authorize public treatment. |
| Product dispatch | Every operation requires accepted product identity; umbrella-only requests fail closed. |
| Mesonet separation | Mesonet inputs are rejected or delegated only through an accepted interface and migration decision. |
| Source-role preservation | Administrative, aggregate, observed, and modeled material remains distinguishable. |
| Rights and automation | Unknown rights, redistribution, attribution, or automation permission blocks fetch. |
| Privacy and sensitivity | Private-land, client, parcel, field, plot, soil-test, unpublished-research, and infrastructure cases fail closed. |
| Freshness and correction | Source date, edition, source head, revision, supersession, and stale state are preserved. |
| Advisory boundary | Advisory material cannot become regulatory, emergency, medical, veterinary, or life-safety authority. |
| Fixture safety | No private record, credential, restricted payload, or unsafe coordinate enters package resources or tests. |
| Candidate outputs | Package outputs are limited to accepted candidate/result types and caller-owned sinks. |
| Lifecycle denial | No package path writes directly to later lifecycle, proof, catalog, release, API, map, or AI surfaces. |
| Migration compatibility | Aliases are explicit, tested, time-bounded, and removable without silent import or source-ID drift. |
| Documentation integrity | README links, metadata, truth labels, evidence snapshot, and rollback target remain current. |

### Documentation checks for this file

Review should verify:

- one H1 and coherent heading hierarchy;
- balanced metadata, code fences, tables, callouts, and links;
- preserved `doc_id`, creation date, prior blob, and introduction commit;
- no remote badge or tracking image;
- no credential, private endpoint, personal record, soil-test result, plot location, or restricted payload;
- current-state claims remain bounded to the pinned repository evidence;
- the diff contains only `connectors/ksu_research_extension/src/README.md`.

[Back to top](#top)

---

## Evidence

| Evidence | What it supports | What it does not prove |
|---|---|---|
| Target blob `382bec1d8442f228296f8a1824446b9c7458fb71` at the pinned base | Exact v0.1 editing baseline and stale two-file inventory. | Runtime, activation, or package readiness. |
| Introduction commit `eb3319ac6ca2634132771a9ca561a75346e21c05` | The v0.1 layout README replaced a blank placeholder. | That a blank file is the preferred current rollback. |
| Current source tree | One package directory containing v0.2 README, empty initializer, comment-only fetch/admit placeholders, and four-field descriptor. | Executable behavior or complete recursive inventory. |
| [`../pyproject.toml`](../pyproject.toml) | Package project name and version `0.0.0`. | Buildability, supported Python, dependencies, or install behavior. |
| [`./ksu_research_extension/README.md`](./ksu_research_extension/README.md) | Current package boundary, product anti-collapse, sensitivity, migration, failure, and definition-of-done contract. | Runtime implementation. |
| [`../README.md`](../README.md) | Top-level path declares compatibility intent. | Accurate current target-path implementation or complete package evidence; the file remains v0.1. |
| [`../../kansas/README.md`](../../kansas/README.md) | Kansas is the canonical family coordination lane and current child topology is provisional. | Presence of the proposed KSU child. |
| Exact proposed child README probe | `connectors/kansas/ksu-research-extension/README.md` was not found at the pinned base. | Absence of every differently named KSU implementation. |
| [Nested source catalog](../../../docs/sources/catalog/kansas/ksu-research-extension.md) | Umbrella/product model, candidate product classes, role distinctions, rights/freshness gaps, and proposed child path. | Accepted descriptors, current endpoints, or activation. |
| [Legacy flat source stub](../../../docs/sources/catalog/ksu_research_extension.md) | Stale generated source-family documentation remains. | Current canonical catalog or descriptor authority. |
| [Kansas Mesonet product lane](../../kansas/mesonet/README.md) | Mesonet is independently governed with product-specific access, consent, cadence, and quality boundaries. | Permission for this layout to own Mesonet behavior. |
| [`SourceDescriptor` contract](../../../contracts/source/source_descriptor.md) and both schema paths | Rich descriptor semantics exist while schema path and enforceable authority conflict. | A valid KSU descriptor or activation decision. |
| Empty [source-authority register](../../../control_plane/source_authority_register.yaml) | No machine authority entry is present in that register. | Absence from every differently named registry artifact. |
| Rights/sensitivity READMEs and TODO-only workflows | Enforcement is not established by those inspected files. | Absence of all policy or CI behavior elsewhere. |

Absence claims are bounded to exact paths, indexed searches, and the pinned commit. This README does not assert a complete recursive repository inventory.

[Back to top](#top)

---

## Review, migration, and rollback

### Review burden

Material changes to this source layout or child package should involve:

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
- security reviewer where credentials, private endpoints, or infrastructure details are involved;
- validation/test steward;
- docs steward.

The current `.github/CODEOWNERS` provides a repository-wide fallback but no KSU R&E layout-specific owner. Team existence, assignment, and reviewer availability remain `NEEDS VERIFICATION`; this README does not invent usernames.

### Migration requirements

Any move, alias, redirect, package split, consolidation, or retirement must preserve:

- Git history and review lineage;
- Python import compatibility or an explicit breaking-change notice;
- source and product IDs;
- descriptor, activation, and source-head lineage;
- fixtures, tests, and CI discovery;
- candidate-envelope and receipt references;
- documentation backlinks and catalog references;
- corrections, supersession, withdrawal, and rollback paths;
- a time-bounded deprecation plan for the top-level snake_case source layout.

Do not duplicate the source tree into a proposed Kansas child and allow both to evolve. A migration must select ownership, preserve traceability, and provide a reversible cutover.

### Rollback

Before merge, close the review branch if this revision is rejected.

After merge, create a transparent revert that restores prior README blob `382bec1d8442f228296f8a1824446b9c7458fb71`. Do not reset, force-push, or rewrite shared history.

The blank placeholder predates v0.1, but the safe current rollback target is the exact prior blob, not an invented reconstruction.

[Back to top](#top)

---

## ADRs

- [Directory Rules](../../../docs/doctrine/directory-rules.md) govern the `connectors/` responsibility root, compatibility posture, README contracts, authority boundaries, and migration discipline.
- [ADR-0012](../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) is present as a draft/proposed numbered connector-output decision. Directory Rules remain the governing authority while the ADR is not accepted.
- No accepted path-specific ADR was verified that resolves:
  - migration or retirement of `connectors/ksu_research_extension/src/`;
  - the final Kansas-family KSU R&E child slug;
  - package/import/source-ID compatibility;
  - umbrella versus product adapter topology;
  - `SourceDescriptor` schema and role-vocabulary authority.
- This README update does not trigger a new ADR by itself: it edits one existing Markdown file, moves no path, creates no authority home, and changes no lifecycle boundary.
- Future path, package split, import/source-ID, descriptor-authority, or product-topology decisions require the applicable accepted ADR or explicit migration record.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Review date | `2026-07-13` |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Base ref | `main` |
| Pinned base commit | `b047eef221136e0efe59a9983f1aae1340c23b70` |
| Prior README blob | `382bec1d8442f228296f8a1824446b9c7458fb71` |
| README introduction commit | `eb3319ac6ca2634132771a9ca561a75346e21c05` |
| Review scope | Target README/history; current src and package files; merged child package README; parent connector and tests READMEs; Kansas family and Mesonet lanes; nested and flat source catalogs; Directory Rules; connector-output ADR; SourceDescriptor contract and both schema paths; source-authority register; rights/sensitivity stubs; connector and descriptor workflow stubs; branch/PR overlap search |
| Reviewer identity | `OWNER_TBD` — no semantic owner assignment made by this document |

[Back to top](#top)

---

## Definition of done

This source layout is not implementation-ready until all applicable items are complete:

- [ ] An accepted migration or ADR resolves the final source-layout and package path, import name, source-ID aliases, and disposition of the top-level snake_case lane.
- [ ] In-scope KSU R&E products are enumerated and each has a stable product identity.
- [ ] Kansas Mesonet remains in its separately governed product lane.
- [ ] Product-specific conforming `SourceDescriptor`s exist in an accepted registry home.
- [ ] Source-role machine vocabulary and schema authority are settled.
- [ ] Explicit activation decisions exist for each permitted operation.
- [ ] Current access methods, endpoints or files, authentication, terms, attribution, redistribution, automation permission, rate limits, cadence, source heads, corrections, and withdrawal behavior are reviewed per product.
- [ ] Rights, privacy, private-land, soil-test, plot-level, unpublished-research, infrastructure, and public-precision controls are implemented and tested.
- [ ] Advisory products are prevented from becoming regulatory, emergency, medical, veterinary, or life-safety authority.
- [ ] The package-local placeholder descriptor is removed, replaced with a non-authoritative fixture, or made an explicit invalid test case.
- [ ] A build backend, supported Python versions, dependency policy, package discovery, and public package API are declared.
- [ ] No-network valid and invalid fixtures exist in the accepted fixture home.
- [ ] Executable tests cover import safety, descriptor/activation denial, product dispatch, Mesonet separation, role anti-collapse, rights, privacy, sensitivity, freshness, advisory misuse, fixture safety, candidate outputs, lifecycle denial, and migration aliases.
- [ ] CI executes substantive checks rather than TODO-only echoes.
- [ ] Candidate-envelope, reason-code, sink, checksum, idempotency, and receipt contracts are accepted.
- [ ] Migration, deprecation, correction, withdrawal, and rollback are documented and tested.
- [ ] Parent connector, source-layout, package, and tests READMEs agree on current inventory and migration state.
- [ ] Owners and required reviewers are assigned.
- [ ] No implementation claim is upgraded without code, tests, workflow evidence, or emitted governed artifacts.

Until then, the safe state is: **no network, no activation, no public output, no direct lifecycle persistence, and no authority inference from source-layout or package presence.**

[Back to top](#top)
