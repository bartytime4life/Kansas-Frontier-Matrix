<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-khri-readme
title: connectors/khri/ — KHRI Greenfield Compatibility Connector Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas/KHRI source steward · KSHS/SHPO liaison · Archaeology steward · Settlements steward · People/privacy reviewer · Rights reviewer · Sensitivity/cultural-review steward · Security reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; greenfield-scaffold; compatibility-path; canonical-family-conflict; source-admission; historic-resource-anti-collapse; rights-fail-closed; cultural-sensitivity-fail-closed; private-location-fail-closed; no-network; no-activation; no-publication
current_path: connectors/khri/README.md
truth_posture: CONFIRMED repository-present 0.0.0 Python scaffold with merged v0.2 source-layout, package-boundary, and test-boundary READMEs, empty initializer, comment-only fetch/admit modules, nonconforming four-field descriptor, and documentation-only local test lane / CONFLICTED final connector path, compatibility class, package migration, SourceDescriptor authority, narrative-to-machine source-role mapping, KHRI product topology, fixture/test routing, registry activation, and public sensitivity floor / PROPOSED bounded compatibility and future source-admission contract / UNKNOWN buildability, imports, executable connector behavior, test collection, live source access, current rights and terms, endpoint/source-head state, substantive CI enforcement, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  prior_blob: 1eab43f40ce2b86e80321e6f49aafe5d697c8de4
related:
  - ../README.md
  - ./pyproject.toml
  - ./src/README.md
  - ./src/khri/README.md
  - ./src/khri/__init__.py
  - ./src/khri/fetch.py
  - ./src/khri/admit.py
  - ./src/khri/descriptor.yaml
  - ./tests/README.md
  - ../kansas/README.md
  - ../kansas_state_archives/README.md
  - ../../CONTRIBUTING.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/sources/catalog/kansas/khri.md
  - ../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../docs/sources/catalog/kansas/kansas-memory.md
  - ../../docs/domains/archaeology/SOURCE_REGISTRY.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../control_plane/source_authority_register.yaml
  - ../../data/registry/sources/README.md
  - ../../fixtures/README.md
  - ../../tests/README.md
  - ../../tests/fixtures/README.md
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
  - ../../.github/workflows/connector-gate.yml
  - ../../.github/workflows/source-descriptor-validate.yml
  - ../../release/
tags: [kfm, connectors, khri, kshs, shpo, kansas, historic-resources, archaeology, settlements, cultural-resources, python, greenfield, compatibility, source-admission, source-role, rights, sensitivity, privacy, geometry, no-network, raw, quarantine, governance]
notes:
  - "The top-level lane contains a confirmed 0.0.0 package scaffold; the prior README's pointer-only and canonicality assertions were stale and overconfident."
  - "The source-layout, package, and test-boundary READMEs are merged at v0.2 and describe the same non-operational scaffold, invalid local descriptor, migration conflict, role-vocabulary conflict, and cultural-resource fail-closed posture."
  - "The KHRI source dossier names connectors/kansas/khri/ as the intended connector path, but named current probes recorded by the merged child evidence did not establish an executable child lane there. Documentation intent and implemented package location remain conflicted."
  - "The source dossier and archaeology guide use narrative role administrative, while the current populated SourceDescriptor machine enum does not. No convenience mapping is selected here."
  - "A dossier, directory name, local YAML, package import, commit, pull request, merge, or green TODO-only workflow cannot create SourceDescriptor authority, rights clearance, cultural/sensitivity clearance, activation, evidence closure, or release permission."
  - "Only this Markdown file is changed. No code, package metadata, descriptor, registry entry, fixture, executable test, workflow, contract, schema, policy, source payload, credential, activation decision, lifecycle artifact, evidence object, release object, path move, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KHRI Greenfield Compatibility Connector Boundary

> Repository-grounded boundary for the source-specific lane at `connectors/khri/`. This path contains a real Python package scaffold, but no supported connector behavior. Existing documentation expresses Kansas-family placement intent; the actual package remains here, so final canonicality, compatibility class, and migration remain unresolved.

**Document lifecycle:** `draft v0.2`  
**Current package maturity:** `CONFIRMED` non-operational `0.0.0` greenfield scaffold  
**Owner:** `OWNER_TBD`  
**Path posture:** repository-present; compatibility intent documented; final implementation home `CONFLICTED / NEEDS VERIFICATION`  
**Boundary:** no live network · no source activation · no package-local authority · no direct lifecycle persistence · no evidence closure · no release · no publication

> [!IMPORTANT]
> The lane contains an empty `__init__.py`, comment-only `fetch.py` and `admit.py`, a nonconforming four-field `descriptor.yaml`, and a README-only local test lane. These establish repository presence—not a harvester, parser, admission gate, quarantine implementation, lifecycle handoff, test suite, or runtime.

> [!CAUTION]
> KHRI material may include archaeological or culturally restricted locations, historic-resource geometry, private-property details, historical or living-person associations, eligibility and designation evaluations, photographs, survey attachments, and collection-security information. Unknown rights, product identity, source role, cultural review, sensitivity, geometry precision, or public-release posture fails closed.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Current status](#current-status) · [Path conflict](#path-and-migration-conflict) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Descriptor boundary](#descriptor-registry-and-activation-boundary) · [Surface identity](#khri-and-kshs-surface-identity) · [Record meanings](#khri-record-and-claim-boundaries) · [Rights and sensitivity](#rights-cultural-sensitivity-privacy-and-geometry) · [Identity and time](#identity-time-and-correction) · [Lifecycle](#lifecycle-boundary) · [Failure contract](#failure-contract) · [Validation](#validation) · [CI limits](#ci-and-observability) · [Review](#review-burden) · [Evidence](#evidence-basis) · [ADRs](#adrs-and-migration) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/khri/` is a repository-present source-specific implementation lane under the `connectors/` responsibility root.

Its current purpose is to:

- expose the exact incompleteness of the KHRI package scaffold;
- prevent placeholder files and documentation from being mistaken for an active connector;
- preserve the unresolved relationship between the current package and the documented Kansas-family KHRI placement;
- keep KHRI, Kansas Memory, KSHS State Archives proper, NRHP, GNIS, parcel sources, archaeology registries, and generated derivatives from collapsing into one source surface;
- preserve inventory, survey, evaluation, eligibility, designation, location, person, property, rights, geometry, time, and review distinctions;
- define fail-closed cultural-sensitivity, sovereignty, privacy, private-location, media, and attachment requirements;
- limit future package output to caller-owned bytes or source-admission candidates;
- identify the contracts, schemas, registries, policies, fixtures, tests, and reviews required before implementation or activation.

This README does not declare the current path canonical, deprecated, legacy, redirect-only, or permanent. It also does not establish that `connectors/kansas/khri/` currently contains an executable replacement package. Those are governed migration and architecture decisions.

[Back to top](#top)

---

## Authority level

**Source-specific connector scaffold only.** This folder has no independent authority over source identity, object meaning, schema shape, rights, cultural sensitivity, privacy, lifecycle state, evidence, catalog closure, release, correction, withdrawal, rollback, or public delivery.

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Responsibility root | **CONFIRMED** | Source-specific fetch, probe, preservation, parsing, packaging, and admission mechanics belong under `connectors/`. |
| Current path | **CONFIRMED** | `connectors/khri/` exists and contains a Python scaffold. |
| Distribution | **CONFIRMED PLACEHOLDER** | `kfm-connector-khri`, version `0.0.0`; buildability and supported runtime remain unknown. |
| Package behavior | **NOT IMPLEMENTED IN NAMED MODULES** | Initializer is empty; fetch and admit modules contain comments only. |
| Local descriptor | **NONCONFORMING PLACEHOLDER** | It is not SourceDescriptor authority, a rights decision, cultural/sensitivity review, activation decision, or release authorization. |
| Local tests | **DOCUMENTATION BOUNDARY** | The test README exists; conventional executable tests were not established at the named probes. |
| Compatibility class | **CONFLICTED** | Older docs say compatibility/noncanonical, but no accepted migration record reviewed here classifies the path as legacy, mirror, deprecated, external-export, transitional, redirect, or retained implementation. |
| Final package home | **CONFLICTED** | Kansas-family placement is documented, while the actual package scaffold currently remains here. |
| Source activation | **DENIED / NOT ESTABLISHED** | No conforming product descriptor, reviewed authority entry, source-head evidence, rights review, cultural/sensitivity review, or activation decision was verified. |
| Public release | **NONE** | Connector presence, retrieval, a commit, PR, merge, or receipt cannot create a public KHRI claim or artifact. |

[Back to top](#top)

---

## Current status

### Repository snapshot

Direct reads and the merged v0.2 child documentation establish this bounded tree:

```text
connectors/khri/
├── README.md                       # this parent connector boundary
├── pyproject.toml                  # project kfm-connector-khri, version 0.0.0
├── src/
│   ├── README.md                   # v0.2 source-layout boundary
│   └── khri/
│       ├── README.md               # v0.2 package scaffold boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only placeholder
│       ├── admit.py                # comment-only placeholder
│       └── descriptor.yaml         # name: khri; role/rights TBD; sensitivity_floor: public
└── tests/
    └── README.md                   # v0.2 negative-first test boundary
```

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| [`pyproject.toml`](./pyproject.toml) | Project name and `0.0.0` version. | No build backend, dependencies, Python constraint, discovery, entry point, or command is established. |
| [`src/README.md`](./src/README.md) | v0.2 source-layout boundary. | Documentation only; no implementation maturity follows. |
| [`src/khri/README.md`](./src/khri/README.md) | v0.2 package boundary. | Current package inventory and governance contract; not executable proof. |
| [`src/khri/__init__.py`](./src/khri/__init__.py) | Empty. | No import API or import-time registration. |
| [`src/khri/fetch.py`](./src/khri/fetch.py) | Comment-only. | No transport, endpoint, authentication, pagination, rate-limit, retry, cache, source-head, or correction behavior. |
| [`src/khri/admit.py`](./src/khri/admit.py) | Comment-only. | No parsing, validation, finite disposition, quarantine, candidate envelope, or sink behavior. |
| [`src/khri/descriptor.yaml`](./src/khri/descriptor.yaml) | Four legacy-style fields. | Invalid as source, rights, sensitivity, activation, or release authority. |
| [`tests/README.md`](./tests/README.md) | v0.2 negative-first future test contract. | Does not prove collection, passing tests, coverage, fixtures, or substantive CI. |

This is not a complete recursive tree receipt. Differently named, generated, ignored, unindexed, or later-added files remain `UNKNOWN` until directly inspected at the commit under review.

[Back to top](#top)

---

## Path and migration conflict

Current evidence shows documentation intent and implemented package location do not yet match.

| Surface | Observed posture | Current implication |
|---|---|---|
| `connectors/khri/` | Repository-present `0.0.0` package scaffold. | Actual placeholder package exists here; presence does not establish final canonicality. |
| `connectors/kansas/khri/` | Named by the KHRI source dossier as the intended connector path. | Named probes in the merged child evidence did not establish an executable child lane; migration is not proven. |
| `connectors/kansas/` | Kansas source-family coordination lane. | Valid family context; does not by itself create a child package or complete migration. |
| `connectors/kansas_state_archives/` | Separate KSHS State Archives connector surface. | Institutional relationship does not justify collapsing KHRI and archival products. |

A safe migration must resolve together:

- winning package path and losing-path disposition;
- compatibility class and deprecation schedule;
- distribution and import names;
- product adapter topology;
- stable source and product identifiers;
- descriptor, registry, and activation references;
- fixtures and test routing;
- workflows and source-head state;
- receipts, evidence links, corrections, withdrawals, and supersession lineage;
- consumer imports and documentation backlinks;
- rollback.

Until then, do not create a second independently evolving package under the Kansas-family path and do not upgrade this path to canonical authority by convention.

[Back to top](#top)

---

## What belongs here

After accepted implementation and migration decisions exist, this connector lane may contain:

- source-specific client interfaces with explicit dependency injection;
- deterministic parsers for reviewed KHRI product shapes;
- KHRI/KSHS surface and product dispatch;
- preservation of source-native fields and qualifiers;
- source, inventory, resource, survey, decision, attachment, and revision identity helpers;
- time-kind preservation without truth upgrades;
- geometry, CRS, uncertainty, precision, withholding, and transform metadata preservation;
- finite hold, quarantine, deny, abstain, and error outcomes using accepted shared contracts;
- caller-owned bytes, parsed source-native records, or admission candidates;
- compatibility warnings and migration shims authorized by an accepted decision;
- no-network synthetic test support under the accepted test and fixture architecture.

Implementation must remain limited to source-specific fetch and admission mechanics. It must not absorb domain truth, policy, evidence, release, or public-delivery responsibilities.

[Back to top](#top)

---

## What does not belong here

Do not place or infer the following under this connector lane:

- canonical contracts or schemas;
- source registry or authority records;
- policy-as-code or discretionary policy decisions;
- rights, cultural, sovereignty, sensitivity, privacy, or public-geometry approvals;
- production credentials, browser sessions, API keys, signed URLs, cookies, or tokens;
- bulk harvests, archives, fixture corpora, media dumps, or restricted cultural-resource payloads;
- authoritative archaeology, designation, parcel, ownership, occupancy, title, current-condition, or access truth outside declared source/product scope;
- EvidenceBundles, proof packs, release manifests, promotion decisions, corrections, withdrawals, or rollback cards;
- direct writes to RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, registry, proof, receipt, or release roots;
- public maps, tiles, APIs, reports, alerts, citations, summaries, exports, or AI answers;
- a second independently evolving implementation at a competing path;
- generated language or models presented as source truth.

[Back to top](#top)

---

## Inputs

Future executable code may accept only explicit caller-supplied inputs such as:

- a reviewed product-specific descriptor or stable reference to one;
- an explicit activation decision appropriate to the requested operation;
- a declared KSHS surface, KHRI product family, source type, and source role;
- immutable response bytes, local file reference, or injected transport result;
- retrieval context containing source URI, source head, retrieval time, request identity, and safe status metadata;
- caller-supplied clock, retry, timeout, rate-limit, cache, and pagination policy;
- a caller-controlled temporary directory;
- reviewed resource/status/place/person crosswalk references;
- rights, cultural-sensitivity, privacy, geometry, and review policy references;
- an explicit sink or callback owned by an external orchestrator.

The package must not discover production credentials, infer activation, guess a product or role, or contact a source during import, tests, documentation builds, or ordinary validation.

[Back to top](#top)

---

## Outputs

A future connector may return only bounded caller-owned values, for example:

- immutable fetched bytes plus safe retrieval metadata;
- a parsed source-native record preserving original fields and qualifiers;
- a normalized admission candidate with explicit surface, product, role, identity, time, geometry, rights, sensitivity, and review references;
- a finite disposition such as hold, quarantine, deny, abstain, error, or accepted-for-external-handoff;
- deterministic reason codes and safe explanations;
- no-op, retry, stale, drift, correction, withdrawal, and supersession signals;
- a receipt candidate or EvidenceRef for an external orchestrator to validate and persist.

The connector does not persist lifecycle state. An accepted external orchestrator may choose a governed RAW or QUARANTINE handoff after validating the candidate. Anything beyond that remains downstream.

[Back to top](#top)

---

## Descriptor, registry, and activation boundary

The current package-local YAML is not a conforming `SourceDescriptor`.

| Local field | Current value | Fail-closed interpretation |
|---|---|---|
| `name` | `khri` | Agency/surface umbrella, not necessarily a stable product-specific source ID. |
| `role` | `TBD` | Unresolved legacy field; not an accepted machine role. |
| `rights` | `TBD` | No permission, attribution, redistribution, media, or retention decision. |
| `sensitivity_floor` | `public` | Deprecated permissive placeholder; not cultural, record-level, geometry, join, or public-release clearance. |

Before live source access or admission behavior exists, governance must provide:

1. one accepted SourceDescriptor contract, schema, validator, and migration authority;
2. stable KHRI surface/product source IDs and descriptor versions;
3. explicit source type, source role, authority rank, publisher, and steward;
4. reviewed rights, terms, attribution, redistribution, retention, disclaimer, and media posture;
5. cultural-sensitivity, sovereignty, privacy, exact-location, geometry, and public-transform posture;
6. cadence, access method, source-head evidence, citation, and operational limits;
7. admissibility limits, review state, activation state, lifecycle class, and public-release posture;
8. registry/control-plane entries where required;
9. safe fixtures and substantive CI.

### Source-role conflict

The source dossier and archaeology documentation use narrative `administrative` role language. The current populated SourceDescriptor machine enum does not contain that token. This README does not translate it by convenience.

An accepted crosswalk must specify whether each KHRI product is authoritative for a claim, historical context, steward-review source, citation source, candidate signal, or another permitted role. Unknown mapping blocks activation and public use.

[Back to top](#top)

---

## KHRI and KSHS surface identity

Institutional relationship does not erase source-surface identity.

| Surface | Required preservation | Prohibited collapse |
|---|---|---|
| KHRI | Inventory/resource IDs, survey/evaluation context, record version, source URI, and source-native fields. | KSHS umbrella is not a substitute descriptor for KHRI. |
| Kansas Memory | Collection/item/presentation, rights, media, and source identity. | A digitized item is not automatically a KHRI inventory or designation record. |
| KSHS State Archives proper | Collection, series, folder, item, creator, access, and restriction context. | Archival description is not KHRI survey or designation authority. |
| NRHP or other designation authority | Program, jurisdiction, nomination, status, decision, effective time, and record identity. | Designation cannot be inferred from KHRI presence or map overlap. |
| GNIS and place authorities | Place-name and feature identity within role. | A place anchor is not historic-resource status, parcel identity, or exact resource geometry. |
| Assessor, parcel, deed, or title sources | Independent property identity and time. | KHRI cannot establish current ownership, title, occupancy, parcel match, access, or residence. |
| Archaeology/cultural registries | Steward, sensitivity, sovereignty, site, survey, and review authority. | Generic KHRI presence cannot expose or create archaeology status. |
| Generated joins, maps, summaries, models, or AI text | Input references, transform identity, uncertainty, policy labels, and reality boundary. | Generated carriers cannot mint authority, designation, title truth, or public-location clearance. |

[Back to top](#top)

---

## KHRI record and claim boundaries

| Record meaning | Bounded interpretation | Prohibited upgrade |
|---|---|---|
| Inventory presence | A source record exists for a stated resource and version. | Current existence, legal designation, eligibility, ownership, condition, or public access. |
| Survey or evaluation | Work occurred under a stated method, scope, author, and date. | Survey opinion equals final agency decision or current condition. |
| Eligibility or recommendation | Source records a bounded recommendation/evaluation at a stated time. | Recommendation equals listing, designation, protection, permit approval, or perpetual status. |
| Designation/legal status | A named authority issued a decision within stated jurisdiction and effective time. | KHRI text alone creates legal status without decision evidence. |
| Address or place description | Historical or descriptive location supplied by source. | Current parcel, residence, access route, exact resource geometry, or permission. |
| Geometry | Observed, digitized, inferred, generalized, buffered, withheld, or null geometry with method and uncertainty. | Exact, current, complete, parcel-aligned, or public-safe geometry without proof and review. |
| Owner or occupant | Historical association at a stated time and evidence basis. | Current owner, resident, titleholder, contact, or living-person identity. |
| Condition or use | Condition/use observed or reported at a stated time. | Current condition, safety, vacancy, demolition, or occupancy. |
| Attachment, image, form, or report | Distinct media/document object with identity, rights, and sensitivity metadata. | Safe to download, OCR, quote, embed, commit, redistribute, or publish by default. |
| Correction, withdrawal, or supersession | Later record changes the interpretation of an earlier record. | Latest retrieval silently overwrites history or deletes prior provenance. |

[Back to top](#top)

---

## Rights, cultural sensitivity, privacy, and geometry

### Rights

No live access, persistence, fixture reuse, media handling, redistribution, or public output is allowed until current terms and source-steward review establish access permission, attribution, redistribution, derivative use, retention, automated-access rules, disclaimers, attachment/media posture, and correction/withdrawal obligations.

Unknown or contradictory rights fail closed.

### Cultural sensitivity and sovereignty

Default-deny or steward-review material includes archaeological locations, sacred or burial-associated places, human-remains contexts, culturally restricted knowledge, consultation-sensitive records, tribal or sovereign interests, collection-security details, and any derivative that could reconstruct withheld information.

Connector code cannot replace cultural, sovereignty, rights-holder, or steward review.

### Privacy and private property

Historical names and associations must remain distinct from living-person data. Private property, current owner/contact information, residences, access routes, project locations, reviewer identities, and restricted communications require minimization and policy review.

### Geometry

Every candidate must preserve native geometry type, CRS/datum, derivation method, observed/inferred/generalized/withheld state, precision, uncertainty, vintage, source feature identity, transform identity, and public-versus-steward geometry separation.

False precision, undocumented centroiding, coordinate swaps, invalid ranges, and reconstruction of withheld locations must fail or quarantine.

### Join-induced sensitivity

A public place, district, parcel, address, road, building footprint, aerial image, historic owner, archaeology indicator, review result, or institutional record may become more sensitive when joined. The joined candidate inherits the most restrictive applicable posture until policy and review explicitly permit otherwise.

[Back to top](#top)

---

## Identity, time, and correction

A candidate must preserve KHRI/KSHS surface identity, source/product IDs, inventory/resource IDs, survey/evaluation/nomination/decision IDs, attachment/media IDs, source URI, version/revision, and amendment/correction/withdrawal/supersession relationships.

Keep distinct where material:

- resource construction or historical period;
- survey/fieldwork time;
- evaluation/recommendation time;
- nomination/decision time;
- effective/expiration time;
- source publication/update time;
- retrieval time;
- review and release time;
- correction, withdrawal, and supersession time.

Retrieval time never substitutes for the historical, survey, legal, or administrative event time. Unresolved crosswalks preserve source-native values and yield hold or abstention rather than guessed canonical identities.

[Back to top](#top)

---

## Lifecycle boundary

```text
source edge / pre-RAW
        ↓
connector returns caller-owned bytes or admission candidate
        ↓
external governed orchestrator
        ├── DENY / ABSTAIN / ERROR / HOLD
        ├── QUARANTINE candidate
        └── RAW candidate after descriptor, activation, rights, and cultural/sensitivity gates
                ↓
WORK / QUARANTINE
                ↓
PROCESSED
                ↓
CATALOG / TRIPLET + EvidenceBundle / proof closure
                ↓
reviewed release transition
                ↓
PUBLISHED governed API / artifact / map surface
```

The connector owns only the bounded source edge. It cannot skip, merge, or authorize later stages. Promotion is a governed state transition, not a file copy, path move, commit, PR, merge, successful fetch, or connector receipt.

[Back to top](#top)

---

## Failure contract

Unsafe or incomplete input must produce one finite, inspectable semantic outcome:

| Outcome | Meaning |
|---|---|
| `HOLD` | Structurally parseable candidate lacks required governance, mapping, or review state. |
| `QUARANTINE` | Candidate may be useful but cannot safely advance; reasons are recorded. |
| `DENY` | Requested access, transform, exposure, or use is prohibited. |
| `ABSTAIN` | Evidence, identity, mapping, temporal/spatial support, or authority is insufficient. |
| `ERROR` | Deterministic contract, transport, parse, or operational failure; no permissive fallback. |

The exact enum and envelope contract remain `NEEDS VERIFICATION`. Package code must use the accepted shared contract rather than creating an incompatible local vocabulary.

A safe failure includes stable reason codes, a non-sensitive explanation, affected gates, retry/remediation class, no partial public result, and no side effect outside caller-owned temporary state.

[Back to top](#top)

---

## Validation

Future implementation must prove at least:

- package import is side-effect-free and no-network;
- zero test discovery and unexpected skipped negative tests fail readiness review;
- descriptor shape and activation resolve from accepted authority surfaces;
- the current four-field placeholder is rejected;
- KSHS surface, KHRI product, source type, role, and authority rank are explicit;
- narrative `administrative` is not mapped silently to a machine role;
- KHRI, Kansas Memory, State Archives, NRHP, GNIS, parcel, archaeology, and generated surfaces remain distinct;
- inventory, survey, evaluation, recommendation, designation, ownership, condition, and current existence do not collapse;
- source identity, amendments, corrections, withdrawals, and supersession are preserved;
- historical, survey, decision, effective, retrieval, review, release, and correction times remain distinct;
- rights, attribution, redistribution, retention, disclaimer, and media posture fail closed;
- cultural sensitivity, sovereignty, privacy, exact location, attachments, geometry, and join-induced risk fail closed;
- parsing and normalization retain source-native unknown values and are deterministic;
- network, credentials, lifecycle roots, registry, proof, receipt, catalog, and release writes are denied by default;
- no public map, tile, API response, report, citation, evidence claim, export, or AI answer is emitted;
- migration cannot create duplicate active packages, descriptors, fixtures, tests, source-head state, or lineage;
- substantive CI executes package and test commands rather than TODO-only echo steps.

### Negative decision matrix

| Condition | Required result |
|---|---|
| Missing or invalid descriptor | No source access; hold, quarantine, or deny. |
| Missing/draft/denied/retired/fixture-only activation | No live source access. |
| Unknown rights or terms | No persistence or public output. |
| Unknown cultural sensitivity, sovereignty, privacy, or review | No public output; hold or deny. |
| Unknown surface, product, or source role | Hold/quarantine; no umbrella fallback. |
| Narrative `administrative` mapped by convenience | Fail pending accepted crosswalk. |
| Inventory record treated as final legal designation | Fail. |
| Eligibility/recommendation treated as listed status | Fail. |
| Historical owner/occupant treated as current person or title truth | Fail. |
| Address treated as parcel, residence, exact geometry, or access permission | Fail. |
| Historical condition/use treated as current condition | Fail or abstain. |
| Retrieval time substituted for survey/decision/effective time | Fail. |
| False-precision or reconstructable sensitive geometry | Fail or quarantine. |
| Sensitive join becomes less restrictive than an input | Fail. |
| Attachment, fixture, log, snapshot, or artifact leaks restricted material | Fail. |
| Direct lifecycle, evidence, catalog, proof, registry, or release write | Fail. |
| Either path declares canonical implementation without migration evidence | Fail migration review. |
| Same controlled inputs yield different candidate or reasons | Fail determinism. |
| Green workflow runs only TODO echo steps | Do not count as implementation proof. |

[Back to top](#top)

---

## CI and observability

The inspected `connector-gate` and `source-descriptor-validate` workflows contain TODO echo steps. Successful execution cannot prove package installation, imports, test collection, parser behavior, descriptor conformance, role crosswalks, network denial, rights/cultural/privacy enforcement, lifecycle safety, migration safety, activation, or release readiness.

Future substantive CI should report the exact environment and lock identity, exact test command, collected/passed/failed/skipped/xfailed counts, zero-discovery failure, executed negative cases, network-denial configuration, safe fixture inventory and hashes, deterministic reason codes, leak-safe logs/artifacts, and commit/package identity.

Coverage percentage alone is not readiness.

[Back to top](#top)

---

## Review burden

| Reviewer role | Required focus |
|---|---|
| Connector/package maintainer | Package API, transport, parsing, side effects, determinism, dependencies, and migration compatibility. |
| Kansas/KHRI source steward | Product inventory, source identity, current access surfaces, cadence, corrections, and source-native fields. |
| KSHS/SHPO liaison | Institutional boundaries, survey/evaluation/designation semantics, stewardship, and official-source context. |
| Archaeology/cultural-review steward | Exact locations, sacred/burial/human-remains contexts, sovereignty, consultation, collection security, and redaction. |
| Settlements/historic-resources steward | Resource types, districts, built-environment semantics, place/time interpretation, and current-condition limits. |
| People/privacy reviewer | Historical versus living-person fields, residences, contacts, ownership/occupancy ambiguity, and joins. |
| Rights reviewer | Terms, attribution, redistribution, retention, attachments, media, fixtures, and public derivatives. |
| Sensitivity reviewer | Public geometry, private property, cultural places, sensitive facilities, joins, logs, and fixture safety. |
| Security reviewer | Network/credential posture, request logging, parsers, archives/media, dependencies, and CI artifacts. |
| Contract/schema reviewer | Accepted SourceDescriptor, candidate, receipt, failure, and role-crosswalk shapes. |
| Test/validation steward | Collection, negative cases, reason codes, side-effect assertions, safe fixtures, and substantive CI. |
| Migration/architecture reviewer | Winning path, imports, source IDs, tests/fixtures, consumers, deprecation, history, and rollback. |

Exact individuals and GitHub teams remain `UNKNOWN`; do not invent assignments.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| Prior `connectors/khri/README.md` blob | **CONFIRMED** | Previous compatibility wording and exact rollback target. | Current implementation, accepted path, or activation. |
| `pyproject.toml` | **CONFIRMED** | Distribution name and version `0.0.0`. | Buildability, dependencies, imports, or runtime. |
| Package files | **CONFIRMED** | Empty initializer, comment-only fetch/admit modules, four-field descriptor. | Fetching, parsing, admission, or handoff behavior. |
| Merged source/package/test v0.2 READMEs | **CONFIRMED DOCUMENTATION** | Current tree, named absent probes, conflicts, record meanings, fail-closed boundaries, and proposed validation. | Executable implementation, test coverage, activation, or release. |
| KHRI source dossier | **CONFIRMED DRAFT DOCUMENTATION** | KSHS-operated per-surface framing, Kansas-first authority posture, product context, and placement intent. | Current endpoint/terms, machine descriptor, package migration, activation, or release. |
| KSHS umbrella dossier | **CONFIRMED DOCUMENTATION** | Institutional anti-collapse and need for per-surface descriptors. | KHRI-specific runtime behavior. |
| Archaeology source-registry guide | **CONFIRMED DRAFT DOCUMENTATION** | Deny-by-default exact cultural locations, role separation, cultural/steward review, and source-admission posture. | Implemented KHRI policy or machine registry records. |
| SourceDescriptor contract/schema | **CONFIRMED REPOSITORY SURFACES; STATUS PROPOSED** | Required field surface, deprecated aliases, machine role vocabulary, rights/sensitivity gates, and activation states. | A conforming KHRI descriptor or one accepted canonical schema path. |
| Source-authority register | **CONFIRMED EMPTY IN REVIEWED EVIDENCE** | No established machine authority entry in the inspected register. | That no authority evidence exists elsewhere. |
| Connector/descriptor workflows | **CONFIRMED TODO-ONLY** | Workflow scaffolding. | Imports, tests, descriptor conformance, rights review, cultural enforcement, or substantive CI. |
| Directory Rules | **CONFIRMED PLACEMENT DOCTRINE** | Responsibility roots, lifecycle law, compatibility discipline, fixture/test separation, migration, and no-parallel-authority rules. | Resolution of current path, role, product, and fixture conflicts. |

No live KHRI endpoint, source payload, terms page, credential, runtime log, deployed service, EvidenceBundle, release manifest, or public client was inspected for this documentation update.

[Back to top](#top)

---

## ADRs and migration

This README creates no ADR and resolves no migration.

An accepted ADR or explicit governed migration record is required before any change that:

- moves or duplicates the package;
- classifies this path as legacy, mirror, deprecated, external-export, transitional, redirect, retained, or removed;
- changes distribution, import, source, or product identifiers;
- chooses one versus multiple KHRI product adapters;
- maps narrative `administrative` to a machine source-role token;
- changes fixture or test routing;
- creates parallel descriptor, registry, policy, schema, receipt, proof, release, or publication homes;
- establishes a public sensitivity or geometry default;
- retires this path or promotes it from compatibility posture.

A README may expose these conflicts; it cannot settle them by wording alone.

[Back to top](#top)

---

## Definition of done

### This documentation revision

- [x] Current package and path maturity is explicit.
- [x] Pointer-only inventory and overconfident canonicality wording are corrected.
- [x] Merged source-layout, package, and test v0.2 boundaries are integrated.
- [x] Directory Rules responsibility roots and lifecycle law are preserved.
- [x] KHRI/KSHS surface and record-meaning anti-collapse controls are explicit.
- [x] Rights, cultural sensitivity, sovereignty, privacy, geometry, time, attachments, media, fixtures, and joins fail closed.
- [x] Inputs, outputs, failure semantics, validation, CI limits, review, migration, rollback, and backlog are explicit.
- [x] No implementation, activation, evidence, or release maturity is overclaimed.

### Connector readiness remains open

- [ ] Accepted connector/package path, import identity, product topology, source IDs, compatibility class, losing-path disposition, and migration plan.
- [ ] Accepted SourceDescriptor contract/schema/validator authority, machine role crosswalk, and conforming KHRI product descriptors.
- [ ] Reviewed authority/control-plane entries, activation decisions, and source-head evidence.
- [ ] Current source access, endpoint shapes, terms, attribution, redistribution, retention, cadence, rate/size limits, correction, and withdrawal posture.
- [ ] Accepted resource, survey, evaluation, eligibility, designation, place, person, property, and crosswalk contracts.
- [ ] Implemented cultural-sensitivity, sovereignty, privacy, geometry, attachment, media, and public-transform policies.
- [ ] Implemented package configuration, transport/parser/admission interfaces, finite candidate envelope, and deterministic reason codes.
- [ ] Safe reviewed fixtures and executable no-network negative tests.
- [ ] Substantive CI with non-zero collection, zero-discovery failure, and demonstrated boundary failures.
- [ ] Evidence, catalog, policy, review, release, correction, withdrawal, and rollback closure outside the connector.

Documentation completeness does not imply connector readiness, source admission, activation, rights clearance, cultural/sensitivity clearance, evidence closure, or publication.

[Back to top](#top)

---

## Rollback

Rollback is required if this README is used to claim source authority, accepted canonicality, completed migration, executable connector behavior, source access, activation, rights clearance, cultural/sensitivity clearance, safe exact-location exposure, lifecycle authority, evidence closure, or release readiness.

Before merge, close the draft pull request and abandon the scoped branch if the revision is rejected.

After merge, restore prior README blob:

```text
1eab43f40ce2b86e80321e6f49aafe5d697c8de4
```

through a transparent revert commit or revert pull request, then rerun applicable documentation, link, connector-boundary, policy, sensitivity, test-discovery, and rollback checks. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Complete recursive connector and consumer inventory | **UNKNOWN** | Mounted checkout or non-truncated tree/import receipt at reviewed commit. |
| Final connector/package home | **CONFLICTED** | Accepted ADR/migration, consumer inventory, import/source-ID plan, deprecation, and rollback. |
| Compatibility class of `connectors/khri/` | **CONFLICTED / NEEDS VERIFICATION** | Accepted legacy/mirror/deprecated/export/transitional/redirect/retained decision. |
| Existence and role of `connectors/kansas/khri/` | **NOT ESTABLISHED AT NAMED PROBES** | Current tree evidence and accepted placement/migration record. |
| KHRI product-family topology | **NEEDS VERIFICATION** | Accepted inventory of portal/search, survey, evaluation, designation, attachment, geometry, and restricted products. |
| SourceDescriptor schema and validator authority | **CONFLICTED / PROPOSED** | One accepted contract/schema, migration, fixtures, validator, and CI command. |
| Narrative-to-machine role mapping | **CONFLICTED** | Accepted vocabulary/crosswalk and negative tests. |
| Product descriptors and authority entries | **NOT ESTABLISHED** | Conforming records and reviewed registry/control-plane entries. |
| Activation decisions and source-head evidence | **NOT ESTABLISHED** | Reviewed activation records and approved source-head observations. |
| Current access surfaces, endpoints, schemas, and cadence | **NEEDS VERIFICATION** | Current authoritative KSHS/KHRI documentation and source-steward review. |
| Current rights, attribution, redistribution, media, retention, and disclaimers | **NEEDS VERIFICATION** | Current terms and signed rights review. |
| Cultural sensitivity, sovereignty, privacy, public geometry, redaction, and joins | **NEEDS VERIFICATION** | Policy, transform profiles, fixtures, receipts, tests, and reviewer decisions. |
| Resource, survey, eligibility, designation, status, and crosswalk semantics | **NEEDS VERIFICATION** | Product contracts, source examples, mappings, and source/domain review. |
| Executable package behavior | **NOT IMPLEMENTED IN NAMED MODULES** | Code, packaging, imports, tests, and logs. |
| Test collection and safe fixture strategy | **NOT ESTABLISHED** | Accepted fixture home, reviewed samples, test command, collection output, and negative cases. |
| Substantive connector CI | **NOT ESTABLISHED** | Real workflow commands, logs, and demonstrated negative failure. |
| Owners and review routing | **UNKNOWN** | Accepted CODEOWNERS or ownership register. |
| Repository-wide promotion prerequisites | **NEEDS VERIFICATION** | Trusted workflow results and required doctrine/release artifacts. |

[Back to top](#top)

---

## Maintainer note

Keep this connector small, deterministic, no-network by default, and subordinate to evidence, policy, cultural review, and release state.

The smallest safe implementation sequence is:

1. settle package path, compatibility class, product/source IDs, descriptor authority, role vocabulary, fixture home, and test routing;
2. replace the local descriptor placeholder with an accepted external reference or governed migration shim;
3. add one invented invalid KHRI-shaped descriptor fixture with no real person, property, resource, coordinate, attachment, endpoint, credential, or source payload;
4. prove import and network denial;
5. prove one deterministic fail-closed candidate with no side effects;
6. add surface, role, identity, record-meaning, rights, cultural-sensitivity, privacy, time, geometry, attachment, and migration negative tests;
7. only then consider a reviewed opt-in source probe.

Do not build new authority here. Governed evidence, policy, review, validation, and release artifacts must carry the system’s truth.

[Back to top](#top)
