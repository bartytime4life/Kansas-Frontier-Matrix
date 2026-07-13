<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kdwp-readme
title: connectors/kdwp/ — KDWP Greenfield Compatibility Connector Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas/KDWP source steward · Fauna steward · Flora steward · Habitat steward · Rights reviewer · Sensitivity/privacy reviewer · Security reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; connector-root; greenfield-scaffold; compatibility-path; canonical-family-migration; product-and-role-conflict; source-admission; rights-fail-closed; sensitivity-fail-closed; no-network; no-activation; no-publication
current_path: connectors/kdwp/README.md
truth_posture: CONFIRMED repository-present 0.0.0 compatibility scaffold, exact placeholder package bytes, README-only local test lane, Kansas-family KDWP coordination lane, incomplete registry placeholders, empty source-authority register, SourceDescriptor schema conflict, and TODO-only connector workflows / CONFLICTED package migration, final product layout, SourceDescriptor machine authority, narrative-to-machine role mapping, fixture routing, and test ownership / PROPOSED fail-closed parent connector boundary / UNKNOWN buildability, executable tests, live source access, current rights, source activation, sensitive-location transforms, substantive CI, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 84f46a1625d218ae5ceb52ff955e3179fe1458e2
  prior_blob: 7eedbe1a977174e1dd99671233d14f00fc904b36
  readme_introduction_commit: ae21a43aba405d3f86a31931e1d5fe94a2435174
related:
  - ../README.md
  - ./pyproject.toml
  - ./src/README.md
  - ./src/kdwp/README.md
  - ./src/kdwp/__init__.py
  - ./src/kdwp/fetch.py
  - ./src/kdwp/admit.py
  - ./src/kdwp/descriptor.yaml
  - ./tests/README.md
  - ../kansas/README.md
  - ../kansas/kdwp/README.md
  - ../kansas/kdwp_flora/README.md
  - ../kansas/kdwp_ert/README.md
  - ../kdwp_ert/README.md
  - ../../CONTRIBUTING.md
  - ../../.github/CODEOWNERS
  - ../../.github/workflows/connector-gate.yml
  - ../../.github/workflows/source-descriptor-validate.yml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../docs/sources/catalog/kansas/kdwp.md
  - ../../docs/standards/SENSITIVITY_RUBRIC.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../data/registry/sources/README.md
  - ../../data/registry/sources/habitat/kdwp.yaml
  - ../../data/registry/fauna/sources/kdwp_species.yaml
  - ../../control_plane/source_authority_register.yaml
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
  - ../../tests/README.md
  - ../../fixtures/README.md
  - ../../release/
tags: [kfm, connectors, kdwp, kansas, package, python, greenfield, compatibility, wildlife, sinc, listed-species, fauna, flora, habitat, ecological-review, source-admission, source-role, rights, sensitivity, no-network, raw, quarantine, no-publication]
notes:
  - "Direct repository evidence at the pinned base confirms a project named kfm-connector-kdwp at version 0.0.0, an empty __init__.py, comment-only fetch.py and admit.py files, and a four-field descriptor.yaml placeholder."
  - "The local tests lane is documentation-only at the named conventional probes; no package build, import, fetch, admission, descriptor, fixture, or lifecycle behavior is proved."
  - "The Kansas-family path connectors/kansas/kdwp/ is the current KDWP coordination lane, but named package and tests paths below it were absent; migration of the top-level distribution, import package, source IDs, product adapters, fixtures, and tests remains unresolved."
  - "KDWP listed-status, SINC-rank, range, observation, habitat, stewardship, and ecological-review products require separate source identity, role, rights, sensitivity, time, geometry, citation, and activation decisions."
  - "The connector-local descriptor is nonconforming and permissive-looking; sensitivity_floor: public is not sensitivity clearance, source activation, or release permission."
  - "The machine source-authority register contains entries: []; the populated singular SourceDescriptor schema declares the plural path canonical while the plural schema is an empty PROPOSED scaffold; narrative and machine role vocabularies are not ratified."
  - "The connector-gate and source-descriptor-validate workflows execute TODO echo steps; green completion does not prove connector or descriptor behavior."
  - "Only this Markdown file is in scope. No code, package metadata, descriptor, registry entry, fixture, test, schema, contract, policy, workflow, source payload, activation decision, lifecycle artifact, path move, release object, or public artifact is created or changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KDWP Greenfield Compatibility Connector Boundary

> Repository-grounded parent boundary for the top-level `connectors/kdwp/` scaffold. The directory contains a real Python package shape, but no supported connector behavior. It remains a compatibility implementation lane while the current Kansas-family KDWP coordination path and the final package, product, fixture, and test topology are resolved.

**Document lifecycle:** `draft v0.2`  
**Component maturity:** repository-present `0.0.0` greenfield scaffold; no supported fetch, parsing, admission, lifecycle, or public behavior  
**Owner:** `OWNER_TBD`  
**Authority:** source-specific package and compatibility documentation only; no source, schema, policy, evidence, lifecycle, release, or publication authority  
**Default posture:** no network · no activation · fail closed · caller-owned candidates only · no publication

> [!IMPORTANT]
> The current package has an empty initializer, comment-only fetch and admission modules, a nonconforming local descriptor, and no established executable test suite at the named conventional paths. Repository presence is not implementation maturity.

> [!CAUTION]
> `sensitivity_floor: public` in the connector-local placeholder is **not** a public-safety decision. KDWP products include listed status, SINC ranks, range context, monitoring observations, habitat or stewardship material, and ecological-review outputs with different source roles and sensitivity burdens. Unknown product identity, role, rights, sensitivity, geometry, review state, or public precision fails closed.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Current state](#current-repository-state) · [Repository fit](#repository-fit) · [Migration](#placement-package-and-migration-boundary) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Products](#kdwp-product-and-source-role-boundaries) · [Descriptor conflict](#descriptor-registry-and-policy-boundary) · [Sensitivity](#sensitivity-rights-and-public-use-boundary) · [Inputs](#inputs) · [Outputs](#outputs) · [Failure contract](#failure-contract) · [Lifecycle](#lifecycle-and-publication-boundary) · [Validation](#validation) · [Evidence](#evidence-basis) · [Review and rollback](#review-migration-and-rollback) · [Definition of done](#definition-of-done) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/kdwp/` is the repository-present parent for a non-operational Python scaffold using the `kdwp` distribution and import name.

Its current responsibility is to:

- record the exact scaffold that exists;
- keep placeholder code, metadata, and tests fail closed;
- preserve KDWP product identity, source role, rights, sensitivity, geometry, time, attribution, disclaimer, and provenance boundaries;
- expose the unresolved relationship between this top-level compatibility package and the Kansas-family KDWP coordination lane;
- prevent listed-status, SINC-rank, range, occurrence, habitat, stewardship, ecological-review, and generated products from collapsing into one source role;
- define what must be proved before implementation, source access, activation, or migration;
- preserve a reversible path for redirect, compatibility import, deprecation, or removal.

This directory does **not** prove that:

- `connectors/kdwp/` is the final implementation home;
- `kdwp` is the final distribution, import package, source ID, or product slug;
- one package should represent every KDWP product;
- the Kansas-family coordination lane already contains executable code;
- any KDWP source is approved for contact, retrieval, admission, transformation, evidence use, or release.

Directory Rules place source-specific fetch, probe, packaging, parsing, and admission mechanics under `connectors/`. Source doctrine, registry entries, contracts, schemas, policy, lifecycle state, evidence closure, cross-system tests, release decisions, public APIs, maps, and AI answers remain in their owning responsibility roots.

[Back to top](#top)

---

## Authority level

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Owning responsibility root | **CONFIRMED** | `connectors/` owns source-specific fetch, probe, preservation, packaging, parsing, and admission mechanics. |
| Current parent path | **CONFIRMED** | `connectors/kdwp/` contains the README, project metadata, source layout, package scaffold, and local test documentation described below. |
| Distribution/import identity | **CONFIRMED scaffold / UNRESOLVED final** | Metadata and package folder use `kdwp`; no accepted migration proves the final distribution, import, source ID, or product scheme. |
| Current implementation | **GREENFIELD PLACEHOLDER** | Empty initializer, comment-only fetch/admit files, minimal metadata, and a placeholder descriptor establish no runtime behavior. |
| Local descriptor | **NONCONFORMING / DENY FOR AUTHORITY USE** | The four-field YAML does not satisfy the richer SourceDescriptor contract and cannot authorize access, admission, sensitivity, or release. |
| Local tests | **README-ONLY AT NAMED PROBES / OTHERWISE UNKNOWN** | No conventional import, fetch, admission, descriptor, conftest, or local-fixture README was established in the inspected evidence. |
| Kansas-family coordination | **CONFIRMED PATH / IMPLEMENTATION DEPTH UNKNOWN** | `connectors/kansas/kdwp/README.md` exists; named package and test paths below it were absent at the inspected base. |
| Product layout | **CONFLICTED / NEEDS VERIFICATION** | KDWP, KDWP Flora, KDWP ERT, top-level ERT compatibility, and this package exist without an accepted final child/sibling/package topology. |
| Machine source authority | **NOT ESTABLISHED** | The source-authority register is `PROPOSED` with `entries: []`; inspected KDWP registry files are placeholders. |
| SourceDescriptor schema authority | **CONFLICTED** | The populated singular-path schema labels the plural path canonical; the plural schema is an empty permissive scaffold. |
| Connector CI | **TODO-ONLY AT NAMED WORKFLOWS** | Current connector and descriptor workflows execute `echo TODO ...`; success cannot establish behavior or governance. |
| Source access and activation | **DENIED / NOT VERIFIED** | No approved product descriptor, source head, rights review, sensitivity review, activation decision, or executable gate was verified. |
| Public output | **NONE** | This scaffold emits no evidence object, lifecycle object, map, API response, proof, release, or public claim. |

Editing this README does not ratify the top-level path, package name, product topology, local descriptor, registry placeholders, workflow stubs, or public-use posture.

[Back to top](#top)

---

## Current repository state

The following bounded snapshot is pinned to repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `84f46a1625d218ae5ceb52ff955e3179fe1458e2`:

```text
connectors/
├── kdwp/
│   ├── README.md                         # this parent boundary
│   ├── pyproject.toml                    # kfm-connector-kdwp, version 0.0.0
│   ├── src/
│   │   ├── README.md                     # greenfield source-layout boundary
│   │   └── kdwp/
│   │       ├── README.md                 # greenfield package boundary
│   │       ├── __init__.py               # empty
│   │       ├── fetch.py                  # comment-only placeholder
│   │       ├── admit.py                  # comment-only placeholder
│   │       └── descriptor.yaml           # four-field nonconforming placeholder
│   └── tests/
│       └── README.md                     # documentation-only test boundary
└── kansas/
    ├── README.md                         # Kansas source-family coordination
    ├── kdwp/
    │   ├── README.md                     # current KDWP coordination lane
    │   └── .gitkeep                      # path marker
    ├── kdwp_flora/README.md              # Flora/listed-species documentation lane
    └── kdwp_ert/README.md                # Ecological Review Tool documentation lane
```

Named exact probes below `connectors/kansas/kdwp/` found no `pyproject.toml`, `src/README.md`, or `tests/README.md` at the inspected evidence boundary. Named exact probes below `connectors/kdwp/tests/` found no conventional `conftest.py`, `test_fetch.py`, `test_admit.py`, `test_descriptor.py`, or `tests/fixtures/README.md`.

These absence statements are bounded to the named paths and pinned evidence. Differently named, generated, unindexed, or later-added files remain `UNKNOWN`.

### Current maturity

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| [`pyproject.toml`](./pyproject.toml) | Declares `kfm-connector-kdwp` at `0.0.0`; no build backend, dependencies, supported Python, package discovery, entry point, command, or test runner. | Buildability, installability, dependency posture, and package API are `UNKNOWN`. |
| [`src/kdwp/__init__.py`](./src/kdwp/__init__.py) | Empty. | No package API or import-time behavior is implemented. |
| [`src/kdwp/fetch.py`](./src/kdwp/fetch.py) | Comment-only placeholder. | No endpoint, authentication, timeout, retry, rate-limit, pagination, cache, source-head, or payload behavior exists. |
| [`src/kdwp/admit.py`](./src/kdwp/admit.py) | Comment-only placeholder. | No descriptor resolution, validation, quarantine, admission, finite outcome, receipt, or candidate-handoff behavior exists. |
| [`src/kdwp/descriptor.yaml`](./src/kdwp/descriptor.yaml) | `name: kdwp`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public`. | Invalid as a governed descriptor, authority record, activation decision, sensitivity clearance, or release authorization. |
| [`src/README.md`](./src/README.md) | v0.2 repository-grounded source-layout boundary. | Documents the scaffold; implements nothing. |
| [`src/kdwp/README.md`](./src/kdwp/README.md) | v0.2 package boundary. | Documents product, descriptor, sensitivity, failure, and migration constraints; implements nothing. |
| [`tests/README.md`](./tests/README.md) | v0.2 test-boundary documentation. | No discovered count, pass/fail result, coverage, fixture inventory, or substantive CI follows from README presence. |
| Connector workflows | TODO-only echo steps. | Green workflow status proves only that placeholder steps executed. |

[Back to top](#top)

---

## Repository fit

| Surface | Responsibility | Current posture |
|---|---|---:|
| `connectors/kdwp/` | Top-level compatibility package scaffold. | **CONFIRMED / NONCANONICAL IMPLEMENTATION POSTURE** |
| `connectors/kansas/kdwp/` | KDWP coordination lane under the Kansas source family. | **CONFIRMED PATH / PACKAGE DEPTH UNKNOWN** |
| `connectors/kansas/kdwp_flora/` | Flora/listed-species documentation lane. | **CONFIRMED / FINAL TOPOLOGY NEEDS VERIFICATION** |
| `connectors/kansas/kdwp_ert/` | Ecological Review Tool documentation lane. | **CONFIRMED / FINAL TOPOLOGY NEEDS VERIFICATION** |
| `connectors/kdwp_ert/` | Top-level ERT compatibility lane. | **CONFIRMED / NONCANONICAL** |
| `docs/sources/catalog/kansas/kdwp.md` | Human-facing source-family catalog. | **DRAFT DOCTRINE / NOT MACHINE AUTHORITY** |
| `data/registry/...` and `control_plane/...` | Source identity, product descriptors, authority, activation, rights, and sensitivity records. | **PLACEHOLDER OR EMPTY IN INSPECTED EVIDENCE** |
| `contracts/` and `schemas/` | Object meaning and machine shape. | **OUTSIDE CONNECTOR / SCHEMA AUTHORITY CONFLICTED** |
| `policy/rights/` and `policy/sensitivity/` | Rights and sensitivity decisions. | **OUTSIDE CONNECTOR / CURRENT READMES GREENFIELD** |
| root `tests/` and `fixtures/` | Canonical cross-system enforceability and approved samples. | **OUTSIDE CONNECTOR-LOCAL OWNERSHIP** |
| `data/raw/` and `data/quarantine/` | Governed lifecycle entry targets. | **CALLER-OWNED HANDOFF ONLY** |
| `release/` | Promotion, release, correction, withdrawal, and rollback authority. | **OUTSIDE CONNECTOR** |

The parent responsibility root is clear: source-specific implementation belongs under `connectors/`. The unresolved question is how this compatibility package, the Kansas-family coordination path, product adapters, source IDs, fixtures, tests, and import compatibility converge without creating duplicate authorities.

[Back to top](#top)

---

## Placement, package, and migration boundary

The current evidence supports three bounded conclusions:

1. `connectors/kansas/kdwp/` is the current KDWP coordination path under the Kansas source family.
2. `connectors/kdwp/` contains the only repository-present implementation-shaped Python scaffold inspected here.
3. No accepted migration or implementation evidence proves that the package has moved, that this top-level path is final, or that the Kansas-family path already owns a working distribution.

A later migration must settle, together:

- canonical connector and package path;
- distribution and import names;
- product adapter and sublane topology;
- stable source and product IDs;
- descriptor and registry references;
- fixtures and test routing;
- source-head and retrieval lineage;
- compatibility imports or redirects;
- documentation and code backlinks;
- deprecation, correction, and supersession notices;
- receipts, review records, and rollback target.

Do not copy the package into the Kansas-family path while leaving the original active. Do not select a winner from directory names or catalog prose alone. Use an accepted ADR or explicit migration plan, preserve history, and keep the change reversible.

[Back to top](#top)

---

## What belongs here

Only after placement, product, descriptor, and activation gates are accepted, a retained parent package may contain:

- one distribution boundary and one import package;
- explicit opt-in source clients whose import and default-test posture is no-network;
- source fetch, probe, source-head, checksum, preservation, and candidate-envelope helpers;
- source-native parsers for reviewed formats and products;
- product dispatch that preserves listed-status, SINC-rank, range, observation, habitat/stewardship, and review-tool distinctions;
- identity-preservation and field-normalization helpers that do not upgrade source meaning;
- accepted source-role mapping helpers after the machine vocabulary is ratified;
- geometry, precision, uncertainty, withholding-state, and public-transform metadata preservation;
- source, observed, valid/effective, retrieval, and correction time preservation where material;
- finite outcomes with stable reason codes;
- caller-owned RAW or QUARANTINE candidate builders that do not choose lifecycle sinks;
- narrow connector-local tests for retained package behavior;
- compatibility adapters only when an accepted migration defines ownership, warnings, sunset criteria, tests, and rollback.

Every executable module requires offline tests, safe fixtures, an observable CI command, and explicit failure behavior before implementation maturity is claimed.

---

## What does not belong here

This directory must not contain or imply authority over:

- source catalog doctrine, `SourceDescriptor` authority, source activation, or product admission decisions;
- canonical contracts, schemas, role vocabularies, rights rules, sensitivity rules, taxonomy-backbone decisions, or release rules;
- bulk source downloads, unreviewed upstream payload corpora, caches, production snapshots, or proprietary exports;
- credentials, cookies, authorization headers, signed URLs, account details, private endpoints, or secrets;
- real exact sensitive taxa, nests, dens, roosts, hibernacula, spawning sites, rare plants, natural-community locations, private-land joins, owner-linked records, or sensitive facilities in examples, fixtures, logs, snapshots, exceptions, or generated output;
- network access on import, installation, documentation rendering, or default tests;
- direct persistence to lifecycle, catalog, triplet, proof, release, rollback, or published roots;
- EvidenceBundle closure, proof generation, promotion, correction, withdrawal, supersession, rollback, or public release;
- public APIs, maps, tiles, dashboards, exports, ecological-review decisions, legal advice, operational notices, hunting or fishing instructions, emergency guidance, or life-safety authority;
- AI narratives or summaries presented as listed-status, occurrence, range, habitat, sensitivity, ecological-review, or release truth;
- a second canonical KDWP implementation evolving independently from the accepted Kansas-family topology.

Public upstream availability is not KFM rights clearance, sensitivity clearance, evidence closure, or release approval.

[Back to top](#top)

---

## KDWP product and source-role boundaries

KDWP is a source family, not one homogeneous dataset. Product-level identity and role must be explicit before parsing or admission.

| Product or record family | Typical evidence posture | Required preservation | Must not be collapsed into |
|---|---|---|---|
| **Listed or legal status** | Authority or regulatory-context candidate, subject to accepted machine mapping | Issuing authority, jurisdiction, status vocabulary, effective time, citation, version, correction/supersession state. | Occurrence, range, habitat observation, field measurement, or KFM-created legal determination. |
| **SINC rank / sensitive natural community status** | Stewardship/sensitivity authority candidate | Rank vocabulary, taxon or community identity, rank scope, effective time, review state, sensitivity implications, citation. | Public exact-location permission, occurrence observation, or general legal status. |
| **Range or distribution product** | Context, interpreted, or modeled candidate depending on source product | Product identity, geometry scale, season/time, method, uncertainty, source role, vintage, public precision. | Point occurrence, guaranteed presence, habitat suitability, or unrestricted exact geometry. |
| **Monitoring, survey, mortality, or disease record** | Observation candidate | Event/record identity, method, observed time, taxon identity, geometry/uncertainty, qualifiers, source program, correction state. | Listed-status decision, complete distribution, causal conclusion, or current public-safe release. |
| **Habitat, natural-community, or stewardship layer** | Context, observation, or modeled candidate depending on product | Layer/product identity, method, geometry scale, time, uncertainty, source role, citation, sensitivity. | Occurrence, legal status, ownership, restoration approval, or unrestricted exact ecological location. |
| **Ecological Review Tool output** | Review/context candidate with bounded legal and operational effect | Request or review identity, product version, scope, date, caveats, source references, reviewer state, public/restricted posture. | Permit, legal clearance, absence proof, comprehensive survey, emergency instruction, or public exact-location dataset. |
| **Park, access, regulation, or operational publication** | Administrative or regulatory-context candidate where admitted | Issuing unit, effective period, supersession, jurisdiction, citation, currentness, disclaimer. | Biodiversity observation, permanent legal truth, KFM alert authority, or life-safety guarantee. |
| **Generated summary, map, tile, graph, or AI answer** | Downstream carrier only | Input evidence refs, method, policy/release state, citations, limitations, correction lineage. | Source record, authority decision, EvidenceBundle, or release approval. |

Narrative role names in the current catalog and machine values in the populated schema are not an accepted crosswalk. Until the mapping is ratified, preserve source-native meaning and route ambiguous cases to hold, quarantine, deny, or abstain.

### Required anti-collapse assertions

```text
listed status != occurrence
SINC rank != public precision
range polygon != confirmed presence
observation != complete distribution
habitat layer != occurrence
modeled suitability != observed habitat
ERT review != permit or legal clearance
administrative notice != biodiversity observation
source retrieval != source activation
valid parse != evidence closure
passing test != release approval
AI summary != source truth
```

[Back to top](#top)

---

## Descriptor, registry, and policy boundary

The local [`descriptor.yaml`](./src/kdwp/descriptor.yaml) is not a usable `SourceDescriptor`.

```yaml
name: kdwp
role: TBD
rights: TBD
sensitivity_floor: public
```

| Local field | Current issue | Required safe treatment |
|---|---|---|
| `name: kdwp` | Agency/package umbrella, not a stable governed product source ID. | Reject as authority; require product-specific identity. |
| `role: TBD` | Unresolved deprecated-style alias; no accepted product role. | Hold or deny activation until the machine role mapping is accepted. |
| `rights: TBD` | Scalar placeholder instead of reviewed rights structure. | Fail closed; no live or public operation. |
| `sensitivity_floor: public` | Unsafe permissive-looking default while product and record sensitivity are unresolved. | Treat as invalid negative input, not clearance. |

The inspected evidence also contains:

- a populated singular-path SourceDescriptor schema that declares the plural schema path canonical and itself legacy;
- an empty permissive plural-path SourceDescriptor scaffold;
- a machine source-authority register with `entries: []`;
- incomplete KDWP registry placeholders;
- greenfield rights and sensitivity README surfaces;
- narrative role terms that do not directly match the populated machine enum.

This parent README does not resolve those conflicts. Product access remains denied until the accepted contract, schema, registry, role mapping, rights review, sensitivity review, source head, activation state, and policy checks are explicit.

[Back to top](#top)

---

## Sensitivity, rights, and public-use boundary

KDWP material may contain or enable harmful ecological disclosure even when a source page is publicly reachable.

Fail-closed classes include:

- exact or reconstructable locations for listed or sensitive taxa;
- nests, dens, roosts, hibernacula, spawning sites, colonies, and breeding sites;
- rare plants and sensitive natural communities;
- private-land, owner, parcel, access-route, contact, or living-person joins;
- sensitive facilities or infrastructure-adjacent ecological records;
- restricted review-tool inputs and outputs;
- source-rights-limited files, images, attachments, exports, or media;
- proprietary or agreement-limited material;
- joins, logs, errors, caches, fixtures, snapshots, coordinates, identifiers, or model output that reconstruct withheld precision.

Required posture:

1. Unknown rights deny live access and public use.
2. Unknown or record-dependent sensitivity routes to hold or quarantine.
3. Original geometry and intended public geometry remain distinct.
4. Public geometry requires an accepted transform, rule version, review, and receipt in the owning downstream lane.
5. Tests and examples use invented, minimized, generalized, withheld-location, or explicitly rights-cleared material.
6. Logs and errors must not reveal source payloads, credentials, private identifiers, or coordinates.
7. A public source URL is not permission to republish, aggregate, infer, or expose.
8. ERT or stewardship output is not a substitute for consultation, permit review, survey, or legal advice.
9. KFM is not an emergency, closure, hunting/fishing, or life-safety authority.

[Back to top](#top)

---

## Inputs

### Current

The scaffold declares no supported function, class, command, endpoint, configuration contract, credential variable, descriptor contract, fixture format, runner, or input DTO.

### Future admissible inputs

After placement and product activation gates are accepted, a retained connector may consume:

- a conforming, reviewed, product-specific `SourceDescriptor` reference;
- an explicit activation decision for the requested fixture-only, restricted, or live operation;
- an approved access configuration supplied through governed secret handling when needed;
- caller-supplied bytes, files, metadata, or reviewed transport results;
- source, product, record, taxon/community, observation/review, and geometry identity;
- source-head evidence such as a reviewed version, checksum, date, `ETag`, `Last-Modified`, or manual release identifier;
- rights, attribution, disclaimer, redistribution, sensitivity, precision, uncertainty, time, and review context;
- caller-owned destination intent for RAW or QUARANTINE candidates;
- synthetic or explicitly rights-cleared test fixtures.

No source contact may occur merely because a path or catalog page exists.

[Back to top](#top)

---

## Outputs

### Current

The scaffold emits no response bytes, parsed record, validation result, finite decision, candidate envelope, receipt, lifecycle write, map artifact, API payload, or public claim.

### Future allowed outputs

A retained package may return only in-memory, caller-owned results such as:

- a preserved transport or parse result;
- a deterministic validation finding;
- an `admit-candidate` for RAW handoff;
- a `hold` or `quarantine-candidate` with machine-readable reasons;
- `deny`, `abstain`, `no-op`, `rate-limit`, or `error`;
- a process-memory retrieval, probe, denial, or handoff receipt **candidate** when an accepted receipt contract exists.

Orchestration—not this package—chooses persistence and lifecycle sinks.

A connector result is not:

- an EvidenceBundle;
- a catalog or graph claim;
- a public-safe geometry decision;
- a policy decision;
- a release manifest;
- a published layer, API answer, or AI response;
- a permit, consultation, legal, ecological-review, or operational conclusion.

[Back to top](#top)

---

## Failure contract

Unsafe or unresolved conditions must produce explicit finite outcomes rather than permissive fallback.

| Condition | Required outcome |
|---|---|
| Product identity absent or ambiguous | `hold` or `deny` |
| Descriptor absent, nonconforming, or unresolved | `deny` or `quarantine-candidate` |
| Activation absent or does not cover requested operation | `deny` |
| Rights, attribution, or redistribution unresolved | `hold` or `deny` |
| Sensitivity or public precision unresolved | `hold` or `quarantine-candidate` |
| Source role or machine mapping unresolved | `hold` or `abstain` |
| Taxon/community/status vocabulary unresolved | `hold` or `quarantine-candidate` |
| Exact or reconstructable sensitive geometry detected | `deny` or restricted quarantine path |
| Source head, vintage, or temporal scope missing where material | `hold`, `no-op`, or `abstain` |
| Unsupported or malformed payload | `error` or `quarantine-candidate` |
| Authentication or authorization failure | `error`; no secret or payload logging |
| Rate limit or retry exhaustion | `rate-limit` or `error` with bounded metadata |
| Response exceeds approved limits | `deny` or `error` |
| Destination would exceed RAW/QUARANTINE candidate boundary | `deny` |
| Network access attempted during import or default tests | fail the operation or test |
| Public artifact, map, API response, or release requested from connector | `deny` |

Stable reason codes, redacted logging, bounded retry behavior, timeouts, response-size limits, content-type checks, and source-head comparison are **PROPOSED** until executable contracts and tests exist.

[Back to top](#top)

---

## Lifecycle and publication boundary

The connector participates only at the source edge and lifecycle admission boundary.

```text
reviewed source/product descriptor + activation
                  |
                  v
       fixture or explicit source operation
                  |
                  v
      fetch / probe / parse / preserve candidate
                  |
                  v
      +-------------------------------+
      | finite connector outcome      |
      | RAW candidate                 |
      | QUARANTINE candidate          |
      | hold / deny / abstain / error |
      +-------------------------------+
                  |
                  v
 caller-owned orchestration and lifecycle gates
                  |
                  v
 WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The package must not:

- select a live lifecycle path implicitly;
- write to repository `data/` or `release/` roots directly;
- create EvidenceBundles, proofs, catalog records, graph truth, release manifests, corrections, or rollback cards;
- publish a public-safe geometry or claim;
- infer that successful retrieval, parsing, validation, commit, workflow, or merge equals promotion.

Promotion remains a governed state transition outside this connector.

[Back to top](#top)

---

## Validation

### Current verified limitations

- no declared build backend or test runner;
- no supported package API or command;
- no fetch or admission implementation;
- no conforming local descriptor;
- no verified product activation;
- no established executable local tests at named conventional paths;
- no local fixture contract or fixture inventory;
- TODO-only connector and descriptor workflows;
- unresolved schema and source-role authority;
- incomplete or empty registry/control-plane state;
- no release or public-output evidence.

### Required future validation families

| Validation family | Minimum proof |
|---|---|
| Import safety | Import performs no network, credential, filesystem, lifecycle, evidence, release, or publication side effect. |
| Package metadata | Supported Python, build backend, dependency policy, package discovery, entry points, commands, and test runner are explicit. |
| Descriptor/activation | Nonconforming placeholders fail; only reviewed product descriptors and matching activation state are accepted. |
| Product dispatch | Listed status, SINC rank, range, observation, habitat/stewardship, ERT, administrative, and generated classes remain distinct. |
| Identity preservation | Source, product, record, taxon/community, status/rank, observation/review, citation, geometry, time, and source-head identity survive. |
| Role anti-collapse | Ambiguous or mismapped roles produce hold, quarantine, deny, or abstain. |
| Rights and sensitivity | Unknown terms, harmful precision, private joins, and restricted material fail closed. |
| Transport safety | Host allowlist, TLS, timeouts, retries, rate limits, content type, response size, checksum, and source-head behavior are bounded. |
| Parser safety | Unsupported, malformed, oversized, mixed-role, or schema-drifted payloads produce deterministic findings without data leakage. |
| Candidate outcomes | RAW/QUARANTINE candidates and failure outcomes are deterministic, caller-owned, and side-effect-free. |
| Lifecycle boundary | No direct WORK, PROCESSED, CATALOG, TRIPLET, proof, release, rollback, or PUBLISHED write occurs. |
| Fixture safety | Fixtures are synthetic, minimized, rights-cleared, geoprivacy-safe, and provenance-documented. |
| Migration | Compatibility imports, warnings, backlinks, losing-path disposition, sunset criteria, correction, and rollback are tested. |
| CI observability | Zero test discovery, unexpected skips, network attempts, fixture leaks, and missing negative cases fail substantive CI. |

A green workflow proves only the behavior it actually executes. The current TODO-only jobs are weak evidence and must not be cited as connector maturity.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| `connectors/kdwp/README.md` prior blob `7eedbe1a977174e1dd99671233d14f00fc904b36` | **CONFIRMED** | Existing v0.1 compatibility document and rollback target. | Current implementation maturity. |
| `connectors/kdwp/pyproject.toml` | **CONFIRMED** | Project name and version `0.0.0`. | Buildability, dependencies, runtime, commands, or tests. |
| `connectors/kdwp/src/kdwp/` exact files | **CONFIRMED** | Empty initializer, comment-only fetch/admit modules, four-field descriptor, updated package README. | Working client, parser, admission, handoff, or activation. |
| `connectors/kdwp/src/README.md` | **CONFIRMED** | Updated repository-grounded source-layout boundary. | Executable behavior. |
| `connectors/kdwp/tests/README.md` | **CONFIRMED** | Updated connector-local test contract and named absence evidence. | Test discovery, coverage, pass rate, or substantive CI. |
| `connectors/kansas/kdwp/README.md` | **CONFIRMED** | Current Kansas-family KDWP coordination path and product/migration conflicts. | Package migration or source activation. |
| KDWP source catalog | **CONFIRMED draft doctrine** | KDWP product families, authority/observation distinction, SINC sensitivity burden, and Kansas-family placement. | Machine descriptor, current endpoint, rights, activation, or release. |
| SourceDescriptor contract and schemas | **CONFIRMED files / CONFLICTED authority** | Rich descriptor burden and singular/plural-path conflict. | Accepted final schema, role crosswalk, or KDWP conformance. |
| KDWP registry placeholders | **CONFIRMED placeholders** | Migration and negative-test inputs. | Source authority or activation. |
| Source-authority register | **CONFIRMED empty** | `entries: []` at inspected evidence. | KDWP activation. |
| Rights and sensitivity READMEs | **CONFIRMED greenfield surfaces** | Required ownership boundary. | Product-specific executable decisions. |
| Connector workflows | **CONFIRMED TODO-only** | Workflow names and placeholder execution. | Connector, descriptor, rights, sensitivity, or lifecycle enforcement. |
| Directory Rules and connector-output ADR | **CONFIRMED doctrine** | Responsibility root and RAW/QUARANTINE candidate boundary. | Implementation completion. |

Absence claims are limited to exact named probes and the pinned evidence boundary. Memory, directory names, catalog prose, generated summaries, and README repetition are not implementation proof.

[Back to top](#top)

---

## Review, migration, and rollback

### Required reviewers

Reviewer assignments remain `UNKNOWN`. Material implementation or migration should include, as applicable:

- connector and package maintainer;
- Kansas/KDWP source steward;
- Fauna, Flora, and Habitat stewards;
- rights and sensitivity/privacy reviewers;
- security reviewer;
- validation/test steward;
- architecture or Directory Rules reviewer;
- release steward when promotion or public behavior is affected.

### Migration requirements

Any move, rename, package consolidation, import alias, redirect, or deprecation must preserve:

- Git history and original path lineage;
- source and product IDs;
- descriptor and registry references;
- source-head and retrieval history;
- fixtures, tests, and CI routing;
- receipts and provenance references;
- backlinks from docs, policies, schemas, pipelines, and releases;
- correction, supersession, and deactivation state;
- compatibility warnings and sunset criteria;
- exact rollback target.

### Rollback

This documentation change is reversible.

```text
authoring base: 84f46a1625d218ae5ceb52ff955e3179fe1458e2
restore prior blob: 7eedbe1a977174e1dd99671233d14f00fc904b36
introduction commit: ae21a43aba405d3f86a31931e1d5fe94a2435174
```

Before merge, close the draft PR and abandon the branch if rejected. After merge, use a transparent revert commit or revert PR. Do not reset, force-push, or rewrite shared history.

Rollback or correction is required if this README is used to justify:

- source access or activation;
- canonical path or package status;
- one all-purpose KDWP descriptor;
- permissive public sensitivity;
- source-role collapse;
- real sensitive fixtures or payload logging;
- direct lifecycle writes;
- public ecological-review, legal, operational, or life-safety claims;
- EvidenceBundle, release, or publication authority.

[Back to top](#top)

---

## Definition of done

### Documentation boundary

- [x] Current parent, source layout, package scaffold, local descriptor, and test-lane maturity are explicit.
- [x] Kansas-family coordination and top-level compatibility implementation are not collapsed.
- [x] Package, product, descriptor, role, registry, fixture, and test migration conflicts are explicit.
- [x] Listed status, SINC rank, range, observation, habitat/stewardship, ERT, administrative, and generated-product distinctions are explicit.
- [x] Rights, sensitivity, exact-location, private-join, fixture, log, and public-use boundaries fail closed.
- [x] Current inputs, outputs, commands, tests, activation, lifecycle behavior, and publication are stated as absent or unknown.
- [x] Finite failure, lifecycle, evidence, review, migration, and rollback boundaries are recorded.

### Implementation readiness

- [ ] Canonical package path and migration plan are accepted.
- [ ] Losing and compatibility paths are dispositioned with warnings and sunset criteria.
- [ ] Owners and required reviewers are assigned.
- [ ] Build, install, supported-runtime, dependency, command, and package API contracts exist.
- [ ] Product inventory, stable source IDs, and adapter topology are accepted.
- [ ] SourceDescriptor machine authority and narrative-to-machine role mapping are accepted.
- [ ] Product-specific descriptors, source heads, rights, sensitivity, citation, cadence, review, and activation are approved.
- [ ] Current access surfaces, formats, terms, attribution, redistribution, rate limits, correction, and withdrawal are verified.
- [ ] Product dispatch, parsing, identity, time, geometry, uncertainty, taxonomy/status, and ERT boundaries are implemented.
- [ ] Default tests are offline, deterministic, negative-first, synthetic or rights-cleared, and CI-discovered.
- [ ] Connector and descriptor workflows execute substantive checks instead of TODO steps.
- [ ] Candidate-envelope, no-op, denial, quarantine, receipt, lifecycle, deactivation, correction, migration, and rollback behavior is tested.
- [ ] Public release, if ever approved, resolves evidence, policy, review, manifest, correction, and rollback state outside the connector.

Until every applicable implementation-readiness item closes, keep the package inactive, fail closed, and non-publishing.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Final canonical package and import home | **NEEDS VERIFICATION** | Accepted ADR or migration plan plus repository implementation. |
| Product adapter and sublane topology | **NEEDS VERIFICATION** | Approved product inventory, package design, and steward review. |
| Stable source and product IDs | **NEEDS VERIFICATION** | Accepted registry conventions and product descriptors. |
| SourceDescriptor schema authority | **CONFLICTED** | Accepted schema decision and substantive validator. |
| Narrative-to-machine role crosswalk | **CONFLICTED** | Accepted vocabulary mapping with negative tests. |
| Registry and source-authority state | **NEEDS VERIFICATION** | Reviewed product entries and activation decisions. |
| Current source access and formats | **UNKNOWN** | Source-steward inspection of current products, files, services, or request workflows. |
| Rights, attribution, redistribution, and disclaimers | **NEEDS VERIFICATION** | Product-specific legal/rights review. |
| Sensitivity, public precision, and transform rules | **NEEDS VERIFICATION** | Policy references, steward review, transform tests, and receipts. |
| Taxonomy, status, rank, range, observation, habitat, and ERT semantics | **NEEDS VERIFICATION** | Product schemas/contracts, fixtures, and domain review. |
| Build/install/runtime contract | **UNKNOWN** | Package metadata, build, import, command, and runtime evidence. |
| Fixture home and safety receipts | **CONFLICTED / NEEDS VERIFICATION** | Accepted fixture decision and inspected synthetic or rights-cleared samples. |
| Executable local and root tests | **UNKNOWN** | Test files, collection results, negative cases, and observed runs. |
| Substantive connector CI | **NOT IMPLEMENTED AT NAMED WORKFLOWS** | Workflows that execute real package, descriptor, fixture, policy, and boundary checks. |
| Owners and reviewer routing | **UNKNOWN** | Accepted CODEOWNERS or steward register entries. |
| Correction, withdrawal, deactivation, migration, and rollback | **NEEDS VERIFICATION** | Tested operational records and runbooks. |
| Public API/map/AI behavior | **DENIED UNTIL GOVERNED** | EvidenceBundle, policy, review, release manifest, correction, and rollback closure. |

[Back to top](#top)
