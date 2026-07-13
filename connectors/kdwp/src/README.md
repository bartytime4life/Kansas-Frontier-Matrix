<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kdwp-src-readme
title: connectors/kdwp/src/ — KDWP Greenfield Source Layout Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas/KDWP source steward · Fauna steward · Flora steward · Habitat steward · Rights reviewer · Sensitivity/privacy reviewer · Security reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; greenfield-source-layout; compatibility-path; canonical-family-migration; source-admission; product-and-role-conflict; rights-fail-closed; sensitivity-fail-closed; no-network; no-activation; no-publication
current_path: connectors/kdwp/src/README.md
truth_posture: CONFIRMED source layout contains a kdwp package with a 0.0.0 project scaffold, empty initializer, comment-only fetch/admit files, nonconforming four-field descriptor, and documentation-only local test lane / CONFLICTED package migration, product dispatch, SourceDescriptor authority, source-role vocabulary, fixture home, and test routing / PROPOSED future package-layout and admission boundary / UNKNOWN buildability, executable tests, runtime, live source access, current rights, activation, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  prior_blob: fca8430c0f0f78f89c933d997847ae7b54b0b49d
related:
  - ../README.md
  - ../pyproject.toml
  - ../tests/README.md
  - ./kdwp/README.md
  - ./kdwp/__init__.py
  - ./kdwp/fetch.py
  - ./kdwp/admit.py
  - ./kdwp/descriptor.yaml
  - ../../README.md
  - ../../kansas/README.md
  - ../../kansas/kdwp/README.md
  - ../../kansas/kdwp_flora/README.md
  - ../../kansas/kdwp_ert/README.md
  - ../../../CONTRIBUTING.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../docs/standards/SENSITIVITY_RUBRIC.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../data/registry/sources/README.md
  - ../../../data/registry/sources/habitat/kdwp.yaml
  - ../../../data/registry/fauna/sources/kdwp_species.yaml
  - ../../../control_plane/source_authority_register.yaml
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../release/
tags: [kfm, connectors, kdwp, src, source-layout, package, python, greenfield, compatibility, kansas, wildlife, sinc, listed-species, fauna, flora, habitat, source-admission, source-role, rights, sensitivity, no-network, raw, quarantine, governance]
notes:
  - "The v0.1 README said only this file and the child package README were confirmed. Direct repository reads now confirm the package scaffold and make that inventory stale."
  - "The current package is version 0.0.0; __init__.py is empty; fetch.py and admit.py are comment-only; descriptor.yaml is a nonconforming placeholder."
  - "The Kansas-family coordination lane connectors/kansas/kdwp/ exists, but migration of this distribution, import package, source IDs, products, fixtures, and tests is not accepted or implemented by this edit."
  - "KDWP product classes and source roles must remain distinct. A package directory, local placeholder, catalog page, or green workflow cannot create source authority, sensitivity clearance, activation, or release permission."
  - "Only this Markdown file is changed. No package code, descriptor, registry entry, fixture, test, workflow, policy, schema, source payload, activation decision, lifecycle artifact, release object, path move, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KDWP Greenfield Source Layout Boundary

> Repository-grounded boundary for `connectors/kdwp/src/`. The layout contains a real Python package scaffold, but no supported connector behavior. It remains inside a top-level KDWP compatibility lane while package migration and product topology are unresolved.

**Document lifecycle:** `draft v0.2`  
**Current maturity:** `CONFIRMED` greenfield source layout with a non-operational `0.0.0` package scaffold  
**Owner:** `OWNER_TBD`  
**Authority:** package-layout documentation only; no SourceDescriptor, policy, lifecycle, evidence, release, or publication authority  
**Boundary:** no live network, no activation, no direct lifecycle persistence, no release, no publication

> [!IMPORTANT]
> The child package contains an empty `__init__.py`, comment-only `fetch.py` and `admit.py`, and a four-field `descriptor.yaml` placeholder. Those files establish package presence—not fetch, parsing, admission, handoff, test, or runtime behavior.

> [!CAUTION]
> The local placeholder's `sensitivity_floor: public` is not a public-release determination. KDWP listed-status, SINC-rank, range, monitoring, habitat, stewardship, review, and observation products carry different source-role and sensitivity burdens and must fail closed until governed decisions exist.

**Quick links:** [Purpose](#purpose) · [Current layout](#current-layout) · [Repository fit](#repository-fit) · [Placement and migration](#placement-and-migration) · [Allowed contents](#allowed-contents) · [Forbidden contents](#forbidden-contents) · [Descriptor boundary](#descriptor-and-activation-boundary) · [Product boundaries](#kdwp-product-and-source-role-boundaries) · [Inputs and outputs](#inputs-and-outputs) · [Failure contract](#failure-contract) · [Validation](#validation) · [Evidence](#evidence-basis) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

This README explains what the source layout demonstrably contains, what it does not implement, and which placement, package, source, policy, and validation gates must close before behavior is added.

The layout currently serves as:

- a container for the live `kdwp` Python namespace scaffold;
- a fail-closed boundary around placeholder code and metadata;
- a compatibility and migration record for the top-level KDWP lane;
- a product and source-role anti-collapse guide for future package work;
- a routing point to package-level, connector-level, test, registry, policy, and release authorities.

It does not prove that `connectors/kdwp/` is canonical, that `kdwp` is the final package or source-ID slug, that one package should cover every KDWP product, or that any KDWP source is approved for access, admission, transformation, or release.

Directory Rules place source-specific fetch, probe, preservation, parsing, and admission mechanics under `connectors/`. They place object meaning, machine shape, policy, tests, registry authority, lifecycle state, evidence closure, and release decisions in their own responsibility roots. This source layout must not duplicate those authorities.

[Back to top](#top)

---

## Current layout

Direct repository reads confirm this bounded surface:

```text
connectors/kdwp/
├── pyproject.toml                  # project kfm-connector-kdwp, version 0.0.0
├── src/
│   ├── README.md                   # this source-layout boundary
│   └── kdwp/
│       ├── README.md               # package boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only greenfield placeholder
│       ├── admit.py                # comment-only greenfield placeholder
│       └── descriptor.yaml         # four-field greenfield placeholder
└── tests/
    └── README.md                   # test-boundary documentation
```

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| [`../pyproject.toml`](../pyproject.toml) | Declares `kfm-connector-kdwp` at `0.0.0`; no build system, dependencies, Python constraint, package discovery, entry point, or command. | Buildability, installability, supported runtime, dependencies, and package API are `UNKNOWN`. |
| [`kdwp/__init__.py`](./kdwp/__init__.py) | Empty. | No import API or import-time behavior is implemented. |
| [`kdwp/fetch.py`](./kdwp/fetch.py) | Comment-only. | No transport, endpoint, authentication, retry, timeout, pagination, rate-limit, caching, or source-head behavior exists. |
| [`kdwp/admit.py`](./kdwp/admit.py) | Comment-only. | No validation, quarantine, admission, finite outcome, receipt, or candidate-handoff behavior exists. |
| [`kdwp/descriptor.yaml`](./kdwp/descriptor.yaml) | Minimal placeholder using `name`, `role: TBD`, `rights: TBD`, and `sensitivity_floor: public`. | Not a conforming SourceDescriptor, registry entry, activation decision, sensitivity clearance, or release authorization. |
| [`kdwp/README.md`](./kdwp/README.md) | Repository-grounded package boundary describing the same scaffold and unresolved migration. | Governs documentation posture; does not implement behavior. |
| [`../tests/README.md`](../tests/README.md) | Test contract only at the inspected path. | Executable package tests, discovery count, coverage, and substantive CI remain absent or `UNKNOWN`. |

This is a bounded inventory, not a complete recursive tree receipt. Differently named, generated, unindexed, or concurrently added files remain `UNKNOWN` until directly inspected at the commit under review.

[Back to top](#top)

---

## Repository fit

| Surface | Responsibility | Current posture |
|---|---|---:|
| `connectors/kdwp/src/` | Source layout for the live compatibility package scaffold. | **CONFIRMED / non-operational** |
| `connectors/kdwp/src/kdwp/` | Current Python namespace and package placeholder. | **CONFIRMED `0.0.0` scaffold** |
| `connectors/kdwp/` | Top-level compatibility connector lane. | **PRESENT / noncanonical documentation posture** |
| `connectors/kansas/` | Kansas source-family coordination lane. | **PRESENT** |
| `connectors/kansas/kdwp/` | KDWP Kansas-family coordination lane. | **PRESENT README lane / executable package migration unresolved** |
| `connectors/kansas/kdwp_flora/` | Flora/listed-species documentation lane. | **PRESENT / topology needs verification** |
| `connectors/kansas/kdwp_ert/` | Ecological Review Tool documentation lane. | **PRESENT / topology needs verification** |
| `connectors/kdwp/tests/` | Local compatibility test boundary. | **README-only at inspected paths** |
| `docs/sources/catalog/kansas/kdwp.md` | Human-facing KDWP source-family/product doctrine. | **Draft documentation; not machine authority** |
| Source registries | Source identity, role, rights, sensitivity, cadence, review, activation, and authority limits. | **Placeholders/conflicts remain; no package-local authority** |
| `policy/` | Rights, sensitivity, access, redaction, and public-use decisions. | **Outside this layout** |
| `release/` | Promotion, correction, withdrawal, supersession, and rollback decisions. | **Outside this layout** |

The owning responsibility root is clear: source implementation belongs under `connectors/`. The unresolved matters are the final connector and package path, distribution/import/source IDs, product decomposition, descriptor migration, fixture and test homes, compatibility behavior, deprecation, and rollback.

[Back to top](#top)

---

## Placement and migration

The top-level package scaffold and the Kansas-family KDWP coordination lane coexist. This edit does not choose a migration strategy.

A safe future decision must address at least:

- whether `connectors/kdwp/` remains a compatibility package, redirects, migrates, or retires;
- whether `connectors/kansas/kdwp/` hosts one package, several product packages, or coordination only;
- which distribution name, import namespace, connector slug, and source IDs survive;
- how KDWP authority, regulatory/listed-status, observation, modeled/context, and review products are dispatched;
- how descriptors, registries, fixtures, tests, workflows, receipts, source-head history, backlinks, corrections, and rollback move together;
- how losing paths warn, redirect, deprecate, and preserve history.

Do not copy this package beneath the Kansas-family lane and allow both copies to evolve. That would create parallel source mechanics and fragment source identity, tests, fixtures, corrections, and provenance. Any move or split requires an accepted ADR or explicit migration plan with rollback.

[Back to top](#top)

---

## Allowed contents

### Current allowed contents

Until placement and migration are accepted, this layout should remain minimal:

- package-level documentation;
- empty or inert compatibility package markers;
- migration and deprecation notes;
- no-network synthetic shape helpers only when backed by tests and an accepted package plan;
- compatibility imports only when their ownership, warnings, sunset criteria, tests, and rollback are explicit.

### Future allowed contents after placement acceptance

A retained source package may contain narrowly scoped mechanics such as:

- opt-in transport clients whose import and default-test posture is no-network;
- source-head, checksum, retrieval, pagination, retry, timeout, and rate-limit helpers;
- product-specific parsers and normalizers that preserve source-native meaning;
- deterministic identity and finite outcome helpers;
- product dispatch that preserves source role, taxonomy, status, sensitivity, geometry, uncertainty, time, rights, attribution, and disclaimers;
- caller-owned RAW or QUARANTINE candidate-envelope builders that do not choose lifecycle sinks;
- package-local pure functions and package-local tests.

Every executable module requires offline tests and an observable CI command. A package file or passing TODO workflow does not establish readiness.

[Back to top](#top)

---

## Forbidden contents

This source layout must not contain or imply authority over:

- canonical SourceDescriptor records, source-authority decisions, or activation decisions;
- contracts, canonical schemas, policy, release review, or publication decisions;
- bulk KDWP downloads, caches, unreviewed extracts, precise sensitive-species records, or restricted ecological material;
- credentials, cookies, tokens, API keys, private endpoints, or session state;
- direct writes to WORK, PROCESSED, CATALOG, TRIPLET, proof, release, or PUBLISHED roots;
- EvidenceBundle closure, proof generation, promotion, correction, withdrawal, supersession, rollback, or release;
- public range, occurrence, habitat, legal-status, SINC-rank, stewardship, or review conclusions;
- generated summaries presented as KDWP authority;
- network activity on import, package discovery, installation, default tests, or documentation rendering;
- silent canonicality claims for the top-level compatibility path.

Public availability upstream is not equivalent to KFM rights clearance, sensitivity clearance, evidence closure, or release approval.

[Back to top](#top)

---

## Descriptor and activation boundary

The connector-local `descriptor.yaml` is a negative input and migration placeholder, not authority.

| Local field | Value | Required posture |
|---|---|---|
| `name` | `kdwp` | Do not treat as an accepted stable product-level `source_id`. |
| `role` | `TBD` | Reject. Role must be resolved for the specific KDWP product or record class. |
| `rights` | `TBD` | Reject for activation and public use. |
| `sensitivity_floor` | `public` | Never treat as clearance while product identity, rights, geometry, sensitivity, redaction, review, and release remain unresolved. |

A governed SourceDescriptor must live in the accepted registry topology and conform to the accepted contract/schema. It must establish identity, publisher, product scope, source type and role, authority rank, rights, sensitivity, cadence, access, citation, source-head evidence, admissibility limits, review state, release state, lifecycle state, connector reference, and activation state.

Missing, malformed, conflicted, unresolved, unreviewed, or unactivated descriptors must yield a finite fail-closed outcome: `DENY`, `ABSTAIN`, `HOLD/QUARANTINE`, or `ERROR` as appropriate. Package code must not repair authority by inference.

[Back to top](#top)

---

## KDWP product and source-role boundaries

KDWP is an agency and source family, not one interchangeable payload.

| Product or record family | Preserve | Must not become |
|---|---|---|
| Listed-status and regulatory records | Taxon identity, jurisdiction, status vocabulary, authority, effective date, citation, version, correction state. | Species occurrence, current presence, abundance, range, habitat suitability, or legal advice outside the record's scope. |
| SINC or sensitivity-rank records | Taxon/list identity, rank system, version, effective date, review state, sensitivity and handling requirements. | Public exact-location permission or universal sensitivity truth. |
| Range or distribution products | Product identity, method, scale, vintage, geometry support, uncertainty, source role, public-use class. | Point occurrence, current occupancy, or surveyed absence. |
| Monitoring, survey, mortality, or disease observations | Event/observation identity, method, place/time, effort, qualifiers, uncertainty, source version. | Legal status, complete range, population trend, or current statewide condition without support. |
| Habitat, stewardship, or management context | Product identity, method, geography, vintage, stewardship purpose, source role, limitations. | Regulatory critical habitat, species occurrence, land title, or release approval. |
| Ecological Review Tool output | Request/input identity, assessed scope, data vintage, decision class, caveats, review authority, expiration/correction state. | Permit, legal clearance, professional consultation, or independent observation. |
| Maps, portals, downloads, and search results | Carrier identity, source URI, retrieved version, product type, attribution, disclaimer, access and terms. | A publisher-wide role, validated evidence closure, or safe public release by default. |

Mixed files must be split by record class or carry per-record role and product identity. A single agency-level role is insufficient when one publisher provides materially different evidence classes.

[Back to top](#top)

---

## Inputs and outputs

### Current

The inspected package declares no supported function, class, command, endpoint, configuration contract, credential variable, descriptor contract, fixture shape, or runner. It emits no response bytes, parsed record, decision, candidate, receipt, lifecycle write, map artifact, API payload, or public claim.

### Future admissible inputs

After placement, product, descriptor, and activation gates close, a retained package may consume:

- a conforming, reviewed, product-specific SourceDescriptor reference;
- an explicit activation decision and approved access configuration;
- caller-supplied bytes, files, metadata, or reviewed transport results;
- product, record, source-head, retrieval-time, and run identity;
- rights, attribution, disclaimer, redistribution, sensitivity, geometry, time, taxonomy, uncertainty, and review context;
- synthetic or explicitly rights-cleared fixtures.

### Future allowed outputs

A retained package may return in-memory, caller-owned parsed records, validation findings, and deterministic finite outcomes such as:

- `admit-candidate`;
- `hold/quarantine-candidate`;
- `deny`;
- `abstain`;
- `no-op`;
- `rate-limit`;
- `error`.

Orchestration chooses persistence. Package code must not select a lifecycle sink, mint authoritative receipts, close evidence, approve release, or publish.

[Back to top](#top)

---

## Failure contract

| Condition | Required outcome |
|---|---|
| Import or package discovery contacts a source | **FAIL** |
| Local placeholder accepted as SourceDescriptor authority | **FAIL / DENY** |
| `TBD` role or rights accepted | **FAIL / DENY** |
| `sensitivity_floor: public` treated as release clearance | **FAIL / DENY** |
| Product or record class missing | **HOLD / QUARANTINE** |
| Source role missing or incompatible with claim | **DENY / ABSTAIN / QUARANTINE** |
| Listed-status record treated as occurrence | **FAIL / DENY** |
| Range product treated as point occurrence or current occupancy | **FAIL / DENY** |
| Observation treated as legal status or complete range | **FAIL / DENY** |
| ERT output treated as permit or legal clearance | **FAIL / DENY** |
| Unknown rights, attribution, redistribution, or disclaimer | **HOLD / DENY PUBLIC USE** |
| Sensitive taxon or exact location lacks governed handling | **HOLD / QUARANTINE / DENY PUBLIC USE** |
| Geometry lacks method, precision, uncertainty, or redaction state | **HOLD / QUARANTINE** |
| Default test or import contacts a live endpoint | **FAIL** |
| Package writes beyond a caller-owned candidate | **FAIL** |
| Connector output treated as evidence closure or publication | **FAIL / DENY** |
| Workflow echoes TODO or discovers zero tests | **FAIL AS COVERAGE CLAIM** |

[Back to top](#top)

---

## Validation

No package build, install, import test, parser test, admission test, descriptor validation, fixture run, source probe, or package-specific CI command is established by this README.

Required future coverage includes:

1. package import and test collection cause no network, DNS, credential, filesystem, registry, lifecycle, or publication side effect;
2. `0.0.0`, empty/comment-only modules, and the local placeholder cannot be reported as a working connector;
3. package and path tests do not choose a migration destination without accepted evidence;
4. metadata declares supported Python, build backend, dependencies, package discovery, entry points, extras, and runner;
5. missing, malformed, conflicted, `TBD`, unreviewed, or unactivated descriptors deny or hold access;
6. product and source-role anti-collapse is preserved across listed-status, SINC, range, observations, habitat/stewardship, ERT, and carrier products;
7. taxonomy, status vocabulary, product identity, observation identity, geometry, uncertainty, temporal fields, rights, attribution, disclaimers, sensitivity, review, correction, and source-head fields remain explicit;
8. exact sensitive locations and identifying joins never appear in default fixtures, logs, errors, snapshots, or public candidates;
9. finite outcomes and reason codes are deterministic;
10. package helpers cannot write lifecycle, evidence, catalog, proof, release, or publication state;
11. fixtures are compact, synthetic or rights-cleared, source-labeled, sensitivity-labeled, and expected-outcome-labeled;
12. CI runs the accepted command, reports discovered tests, and fails on zero discovery, TODO-only execution, network access, sensitive-data leakage, or negative-case regression.

```text
import retained package
  -> no network or DNS
  -> no credential lookup
  -> no filesystem, registry, or lifecycle write
  -> no activation
  -> no receipt, proof, catalog, release, or public artifact
```

A green generic connector workflow is not substantive package proof unless it executes the accepted KDWP test command and reports the expected test set.

[Back to top](#top)

---

## Evidence basis

| Evidence | Supports | Does not prove |
|---|---|---|
| This prior README blob | Exact v0.1 baseline and stale two-README inventory. | Runtime, canonicality, or migration. |
| `pyproject.toml` | Distribution name and version `0.0.0`. | Installability, dependency support, entry points, or package API. |
| Exact package files | Empty initializer, comment-only fetch/admit, local placeholder descriptor. | Fetch, parse, admission, handoff, or release behavior. |
| Package README | Current package-level scaffold and governance analysis. | Executable implementation or accepted migration. |
| Test README | Intended no-network and fail-closed test posture. | Test files, discovery, coverage, or passing CI. |
| Parent and Kansas-family READMEs | Compatibility posture and current coordination lanes. | Accepted package migration or activation. |
| Source catalog and domain docs | Product distinctions, source-role boundaries, sensitivity risks, and proposed placement. | Machine authority, current source terms, or runtime behavior. |
| SourceDescriptor contract/schema and registry docs | Required descriptor surface and current authority conflicts. | A conforming, reviewed, activated KDWP product descriptor. |
| Directory Rules | Responsibility-root placement and migration discipline. | Which unresolved KDWP package topology is accepted. |

Claims are bounded to directly inspected files and named repository surfaces. Documentation and path presence do not substitute for executable tests, source review, policy decisions, or release records.

[Back to top](#top)

---

## Definition of done

### This documentation update

- [x] Replaces the stale two-README inventory with the directly confirmed package scaffold.
- [x] Records `0.0.0`, empty/comment-only modules, and the nonconforming local descriptor without runtime overclaiming.
- [x] Keeps top-level compatibility and Kansas-family migration status visible.
- [x] Preserves product, source-role, rights, sensitivity, geometry, temporal, lifecycle, evidence, and release boundaries.
- [x] Defines allowed and forbidden source-layout responsibilities.
- [x] Defines finite failure outcomes and negative-first validation expectations.
- [x] Changes only this Markdown file.

### Implementation readiness remains open

- [ ] Accepted package path, distribution/import/source IDs, product dispatch, descriptor topology, fixture home, and test routing.
- [ ] Product-specific SourceDescriptors, authority entries, reviews, source heads, and activation decisions.
- [ ] Current source surfaces, access methods, terms, attribution, redistribution, disclaimers, cadence, rate limits, and correction behavior.
- [ ] Build metadata, executable package code, compact safe fixtures, negative-first tests, substantive CI, owners, and rollback-tested migration.

Documentation readiness does not imply package readiness, source access, activation, rights approval, sensitivity clearance, evidence closure, release approval, or publication.

---

## Rollback

Rollback is required if this README is used to claim canonical status, working package behavior, test/CI behavior, source access, activation, rights/sensitivity clearance, public safety, downstream lifecycle authority, evidence closure, or release.

Before merge, leave the draft pull request unmerged and abandon the scoped branch if rejected.

After merge, restore the prior README blob:

```text
fca8430c0f0f78f89c933d997847ae7b54b0b49d
```

through a transparent revert commit or revert pull request, then rerun applicable documentation, link, connector-boundary, source-role, and policy checks. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Complete recursive source-layout inventory | **UNKNOWN** | Non-truncated tree receipt or mounted checkout. |
| Final connector/package/distribution/import/source-ID topology | **CONFLICTED** | Accepted ADR/migration, consumer inventory, backlinks, tests, and rollback plan. |
| Product dispatch and source-role mapping | **NEEDS VERIFICATION** | Product inventory, contract/schema decision, descriptors, and anti-collapse tests. |
| SourceDescriptor schema, validator, and registry authority | **CONFLICTED / NEEDS VERIFICATION** | One accepted meaningful schema, validator, fixtures, CI command, and registry topology. |
| Local descriptor disposition | **NEEDS VERIFICATION** | Migrate, validate, or retire through source-registry review. |
| Current KDWP source surfaces and access | **NEEDS VERIFICATION** | Current authoritative source documentation and source-steward review. |
| Rights, attribution, redistribution, disclaimers, and reuse | **NEEDS VERIFICATION** | Current terms and rights review. |
| Sensitivity, exact-location, geometry, uncertainty, and redaction | **NEEDS VERIFICATION** | Policies, transforms, fixtures, tests, and sensitivity review. |
| Executable package, tests, fixtures, and substantive CI | **NOT IMPLEMENTED AT INSPECTED PATHS / OTHERWISE UNKNOWN** | Code, exact test command, discovered test count, logs, and demonstrated negative failure. |
| Package migration and compatibility sunset | **NEEDS VERIFICATION** | Accepted migration sequence, deprecation warnings, consumer tests, history preservation, and rollback drill. |
| Owners and review routing | **UNKNOWN** | Accepted CODEOWNERS or ownership records. |

[Back to top](#top)

---

## Maintainer note

Keep this source layout minimal until placement, package identity, product dispatch, descriptor authority, access, rights, sensitivity, fixtures, tests, and review conflicts are resolved.

The safest first executable increment is synthetic and negative-first: import without side effects; reject the local descriptor; preserve one invented product identity, role, taxon/status context, geometry uncertainty, rights, sensitivity, attribution, and disclaimer surface; return a caller-owned hold/quarantine candidate with deterministic reasons; prove no network or lifecycle write; and fail CI on zero discovery or negative-case regression.

Only after that slice, an accepted package migration, product-specific governance, and observed CI should an opt-in source-access test be considered.

[Back to top](#top)
