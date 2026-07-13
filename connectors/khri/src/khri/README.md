<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-khri-src-package-readme
title: connectors/khri/src/khri/ — KHRI Greenfield Compatibility Package Scaffold
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas/KHRI source steward · KSHS/SHPO liaison · Archaeology steward · Settlements steward · People/privacy reviewer · Rights reviewer · Sensitivity/cultural-review steward · Security reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; greenfield-package; compatibility-path; canonical-family-conflict; source-admission; historic-resource-anti-collapse; rights-fail-closed; cultural-sensitivity-fail-closed; private-location-fail-closed; no-network; no-activation; no-publication
current_path: connectors/khri/src/khri/README.md
truth_posture: CONFIRMED repository-present 0.0.0 package scaffold with empty initializer, comment-only fetch/admit modules, nonconforming four-field descriptor, and documentation-only local test lane; named richer modules and conventional tests were not found at exact probes / CONFLICTED final package path, compatibility class, source-role mapping, SourceDescriptor authority, product decomposition, fixture/test routing, registry activation, and public sensitivity floor / PROPOSED bounded compatibility and future source-admission package contract / UNKNOWN buildability, imports, executable behavior, test collection, live source access, current rights and terms, endpoint/source-head state, substantive CI enforcement, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  prior_blob: 5741fedb6269d272585413d0f947b2137333e4ab
related:
  - ../../README.md
  - ../../pyproject.toml
  - ../README.md
  - ./__init__.py
  - ./fetch.py
  - ./admit.py
  - ./descriptor.yaml
  - ../../tests/README.md
  - ../../../README.md
  - ../../../kansas/README.md
  - ../../../../CONTRIBUTING.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/sources/catalog/kansas/khri.md
  - ../../../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../../../docs/domains/archaeology/SOURCE_REGISTRY.md
  - ../../../../contracts/source/source_descriptor.md
  - ../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../data/registry/sources/README.md
  - ../../../../fixtures/README.md
  - ../../../../tests/README.md
  - ../../../../tests/fixtures/README.md
  - ../../../../policy/rights/README.md
  - ../../../../policy/sensitivity/README.md
  - ../../../../.github/workflows/connector-gate.yml
  - ../../../../.github/workflows/source-descriptor-validate.yml
  - ../../../../release/
tags: [kfm, connectors, khri, kshs, shpo, kansas, historic-resources, archaeology, settlements, cultural-resources, python, package, greenfield, compatibility, source-admission, source-role, rights, sensitivity, privacy, geometry, no-network, raw, quarantine, governance]
notes:
  - "The v0.1 package README described a speculative helper-module map. Direct reads now confirm only an empty __init__.py, comment-only fetch.py and admit.py, and a four-field descriptor.yaml placeholder beside this README."
  - "Exact probes did not find descriptors.py, parse.py, normalize.py, roles.py, identity.py, sensitivity.py, geometry.py, handoff.py, or errors.py, nor conventional local tests named test_fetch.py, test_admit.py, test_descriptor.py, or conftest.py."
  - "The KHRI source dossier states connectors/kansas/khri/ is the correct connector path, but exact current probes did not establish that README or placeholder path. Documentation intent and implemented package location therefore remain conflicted."
  - "The source dossier and archaeology guide use the narrative role administrative, while the current populated SourceDescriptor machine enum does not. No convenience mapping is selected here."
  - "The package-local descriptor is not SourceDescriptor authority, a source registry entry, an activation decision, a rights decision, a cultural/sensitivity review, or release evidence."
  - "The connector-gate and source-descriptor-validate workflows execute TODO echo steps; green completion cannot prove KHRI package behavior, descriptor conformance, rights review, test collection, or release readiness."
  - "Only this Markdown file is changed. No code, package metadata, descriptor, registry entry, fixture, test, workflow, contract, schema, policy, source payload, credential, activation decision, lifecycle artifact, evidence object, release object, path move, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KHRI Greenfield Compatibility Package Scaffold

> Repository-grounded boundary for the `khri` Python namespace under `connectors/khri/src/khri/`. The package exists, but its named implementation files are placeholders. This README defines what a future KHRI source-admission package may do and what it must never be mistaken for.

**Document lifecycle:** `draft v0.2`  
**Current package maturity:** `CONFIRMED` non-operational `0.0.0` greenfield scaffold  
**Owner:** `OWNER_TBD`  
**Path posture:** repository-present package; compatibility intent documented; final package home and migration state `CONFLICTED / NEEDS VERIFICATION`  
**Boundary:** no live network, no source activation, no package-local policy or registry authority, no lifecycle persistence, no evidence closure, no release, no publication

> [!IMPORTANT]
> The package currently contains an empty `__init__.py`, comment-only `fetch.py` and `admit.py`, and a four-field `descriptor.yaml` placeholder. These files prove package presence only. They do not implement transport, parsing, normalization, admission, quarantine, handoff, tests, or runtime behavior.

> [!CAUTION]
> KHRI material may include historic-resource locations, archaeological or culturally sensitive places, private-property details, historical or living-person associations, eligibility or designation evaluations, photographs, survey attachments, and security-relevant collection information. Unknown rights, product identity, source role, review state, cultural sensitivity, geometry precision, or public-release posture fails closed.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Current scaffold](#current-scaffold) · [Path conflict](#path-and-migration-conflict) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Descriptor boundary](#descriptor-registry-and-activation-boundary) · [Surface identity](#khri-and-kshs-surface-identity) · [Record meanings](#khri-record-and-claim-boundaries) · [Rights and sensitivity](#rights-cultural-sensitivity-privacy-and-geometry) · [Time and identity](#identity-time-and-correction) · [Lifecycle](#lifecycle-boundary) · [Failure contract](#failure-contract) · [Validation](#validation) · [Review](#review-burden) · [Evidence](#evidence-basis) · [ADRs](#adrs-and-migration) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/khri/src/khri/` is the repository-present Python package namespace for a future KHRI source-specific connector implementation.

Its present purpose is to:

- expose the exact incompleteness of the current package scaffold;
- prevent placeholder files from being interpreted as a live KHRI harvester or admitted source;
- preserve the unresolved relationship between this package and the documented Kansas-family KHRI path;
- keep KHRI, Kansas Memory, KSHS State Archives proper, NRHP, GNIS, assessor/parcel data, archaeology records, and generated derivatives from collapsing into one source surface;
- preserve resource, inventory, survey, evaluation, designation, location, person, parcel, rights, and review distinctions;
- define fail-closed requirements for cultural sensitivity, private-location exposure, living-person data, geometry, rights, and source-role uncertainty;
- limit future package output to caller-owned source-edge bytes or admission candidates;
- identify the contracts, schemas, registries, policies, fixtures, tests, and reviews required before implementation or activation.

This README does not declare the current path canonical, deprecated, legacy, redirect-only, or permanent. It also does not establish that `connectors/kansas/khri/` currently contains an executable replacement package. Those are migration and architecture decisions, not documentation shortcuts.

[Back to top](#top)

---

## Authority level

**Source-specific package scaffold only.** This directory has no independent authority over source identity, object meaning, schema shape, rights, cultural sensitivity, privacy, lifecycle state, evidence, catalog closure, release, correction, rollback, or public delivery.

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Responsibility root | **CONFIRMED** | Source-specific fetch, probe, preservation, parsing, packaging, and admission mechanics belong under `connectors/`. |
| Current package path | **CONFIRMED** | `connectors/khri/src/khri/` exists. |
| Distribution | **CONFIRMED PLACEHOLDER** | `kfm-connector-khri`, version `0.0.0`; no build backend, dependencies, Python constraint, package discovery, entry point, or command was established in `pyproject.toml`. |
| Import surface | **EMPTY** | `__init__.py` contains no API or import-time behavior. |
| Fetch behavior | **NOT IMPLEMENTED** | `fetch.py` contains one placeholder comment. |
| Admission behavior | **NOT IMPLEMENTED** | `admit.py` contains one placeholder comment. |
| Local descriptor | **NONCONFORMING PLACEHOLDER** | Four legacy-style fields do not satisfy the current SourceDescriptor contract or schema. |
| Local tests | **DOCUMENTATION-ONLY AT NAMED LANE** | `tests/README.md` exists; conventional test files were not found at exact probes. Differently named tests remain `UNKNOWN`. |
| Compatibility class | **CONFLICTED** | Existing docs call this path compatibility/noncanonical, but no accepted migration record reviewed here classifies it as legacy, deprecated, mirror, redirect, transitional, or retained implementation. |
| Final package home | **CONFLICTED** | The source dossier names `connectors/kansas/khri/`; the actual package scaffold is here, and exact probes did not establish the named Kansas-family child path. |
| Source activation | **DENIED / NOT ESTABLISHED** | No conforming KHRI product descriptor, authority-register entry, source-head evidence, rights review, sensitivity/cultural review, or activation decision was verified. |
| Public release | **NONE** | Package presence, successful retrieval, a commit, a pull request, or a connector receipt cannot create a public KHRI claim or artifact. |

[Back to top](#top)

---

## Current scaffold

Direct repository reads confirm this bounded package surface:

```text
connectors/khri/
├── pyproject.toml                  # project kfm-connector-khri, version 0.0.0
├── src/
│   ├── README.md                   # source-layout documentation, currently v0.1
│   └── khri/
│       ├── README.md               # this package boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only greenfield placeholder
│       ├── admit.py                # comment-only greenfield placeholder
│       └── descriptor.yaml         # four-field greenfield placeholder
└── tests/
    └── README.md                   # documentation-only test boundary, currently v0.1
```

### Exact absent probes

The richer v0.1 module map was not established at these exact paths:

```text
connectors/khri/src/khri/descriptors.py
connectors/khri/src/khri/parse.py
connectors/khri/src/khri/normalize.py
connectors/khri/src/khri/roles.py
connectors/khri/src/khri/identity.py
connectors/khri/src/khri/sensitivity.py
connectors/khri/src/khri/geometry.py
connectors/khri/src/khri/handoff.py
connectors/khri/src/khri/errors.py
```

Conventional local tests were not established at these exact paths:

```text
connectors/khri/tests/conftest.py
connectors/khri/tests/test_fetch.py
connectors/khri/tests/test_admit.py
connectors/khri/tests/test_descriptor.py
```

These are bounded absence statements, not a complete recursive tree receipt. Differently named, generated, unindexed, or concurrently added files remain `UNKNOWN` until read directly at the reviewed commit.

[Back to top](#top)

---

## Path and migration conflict

The repository and documentation currently disagree about KHRI package placement.

| Surface | Observed posture | Current implication |
|---|---|---|
| `connectors/khri/src/khri/` | Repository-present `0.0.0` package scaffold. | Actual package placeholder exists here; presence does not establish final canonicality. |
| `connectors/khri/` | Parent README calls the lane compatibility/noncanonical. | Documents migration intent but does not classify the path through an accepted ADR or migration record. |
| `connectors/kansas/khri/` | Named by the KHRI source dossier as the correct connector path. | Exact probes did not establish the child README or `.gitkeep`; implementation presence is not confirmed. |
| `connectors/kansas/` | Repository-present Kansas source-family coordination root. | Strong responsibility-family intent; not proof that KHRI package migration occurred. |
| `docs/sources/catalog/kansas/khri.md` | Human-facing KHRI source dossier. | Source and placement doctrine; not an executable package, registry entry, or migration receipt. |

A safe migration must settle together:

- winning package path and losing-path disposition;
- compatibility class and deprecation schedule;
- distribution and import names;
- stable KHRI source and product identifiers;
- descriptor, activation, rights, sensitivity, and source-head references;
- fixtures and test routing;
- workflows and package consumers;
- retrieval, correction, withdrawal, and supersession history;
- receipts, evidence references, catalog links, and release backlinks;
- rollback and restoration procedure.

Until that decision exists, do not create a second independently evolving KHRI package under the Kansas-family path, and do not upgrade this package to canonical authority by convenience.

[Back to top](#top)

---

## What belongs here

After accepted contract, policy, source, and migration decisions, this package may contain narrowly scoped source mechanics such as:

- an import-safe package API;
- dependency-injected, explicitly enabled KHRI transport interfaces;
- deterministic parsing of approved KHRI product shapes;
- preservation of source-native fields and qualifiers;
- KHRI/KSHS surface-identity preservation;
- product and source-role dispatch;
- resource, inventory, survey, evaluation, designation, and attachment identity preservation;
- source-native date, status, and amendment preservation;
- geometry, CRS/datum, precision, uncertainty, withholding, and transform metadata preservation;
- rights and review-state references without package-local policy decisions;
- finite hold, quarantine, deny, abstain, and error outcomes using an accepted shared contract;
- caller-owned candidate envelopes or immutable response-byte/reference values;
- compatibility warnings or migration shims authorized by an accepted migration plan;
- no-network test support that follows the accepted fixture and test architecture.

Implementation must remain source-specific. It must not absorb domain truth, cultural-review authority, policy, evidence closure, release, or public-delivery responsibilities.

[Back to top](#top)

---

## What does not belong here

Do not place or infer the following under this package:

- canonical contracts or schemas;
- source registry or authority records;
- policy-as-code, cultural-review decisions, or discretionary redaction decisions;
- rights, redistribution, sensitivity, privacy, or public-geometry approvals;
- production credentials, tokens, cookies, browser sessions, API keys, signed URLs, or private endpoints;
- bulk KHRI exports, survey archives, photo collections, GIS packages, fixture corpora, or sensitive payload dumps;
- authoritative parcel, title, ownership, occupancy, person, archaeology, designation, eligibility, demolition, or current-condition truth outside the declared KHRI record role;
- EvidenceBundles, claims, proof packs, promotion decisions, release manifests, corrections, withdrawals, or rollback cards;
- direct writes to RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, registry, receipt, proof, or release roots;
- public maps, tiles, APIs, reports, alerts, summaries, exports, or AI answers;
- permit, legal-clearance, preservation-compliance, consultation-completion, eligibility, or absence determinations;
- a second independently evolving package at a competing path;
- generated language, models, or joins presented as sovereign truth.

[Back to top](#top)

---

## Inputs

Future executable code may accept only explicit caller-supplied inputs, such as:

- a reviewed product-specific SourceDescriptor or stable reference to one;
- an explicit activation decision appropriate to the requested operation;
- a declared KHRI product/record family and source role;
- immutable response bytes, a local file reference, or an injected transport result;
- retrieval context containing source URI, source head, retrieval time, request identity, and safe response metadata;
- caller-supplied clock, timeout, retry, rate-limit, cache, pagination, and size policy;
- a caller-owned temporary directory;
- reviewed resource-type, status, designation, eligibility, place, and authority crosswalk references;
- rights, cultural sensitivity, privacy, geometry, and public-transform policy references;
- an explicit sink or callback interface owned by an external orchestrator.

The package must not discover production credentials, infer activation, guess a record role, assume a public sensitivity floor, or contact a source during import, default tests, documentation builds, or ordinary validation.

[Back to top](#top)

---

## Outputs

A future KHRI connector package may return only bounded caller-owned values, for example:

- immutable fetched bytes plus safe retrieval metadata;
- a parsed source-native record preserving original fields, labels, codes, and qualifiers;
- a normalized admission candidate with explicit product, role, identity, time, geometry, rights, sensitivity, and review references;
- a finite disposition such as hold, quarantine, deny, abstain, error, or accepted-for-external-handoff;
- deterministic reason codes and non-sensitive explanations;
- stale, drift, no-op, retry, amendment, correction, withdrawal, or supersession signals;
- a receipt candidate or EvidenceRef candidate for an external orchestrator to validate and persist.

The package does not persist lifecycle state. An accepted external orchestrator may choose a governed RAW or QUARANTINE handoff after validating the candidate. Anything beyond that remains downstream.

[Back to top](#top)

---

## Descriptor, registry, and activation boundary

The current package-local YAML is not a conforming `SourceDescriptor`:

```yaml
name: khri
role: TBD
rights: TBD
sensitivity_floor: public
```

| Local field | Current value | Fail-closed interpretation |
|---|---|---|
| `name` | `khri` | Package/agency shorthand, not a stable product-specific `source_id`. |
| `role` | `TBD` | Deprecated legacy alias and unresolved role. |
| `rights` | `TBD` | Wrong shape for the current closed rights object and no permission decision. |
| `sensitivity_floor` | `public` | Deprecated permissive alias, not reviewed source-, product-, record-, or geometry-level public clearance. |

The current SourceDescriptor contract requires a substantially richer record: stable source identity and version, source type and role, authority rank, publisher/steward, structured rights, sensitivity default, cadence, access, citation, source head, admissibility limits, public-release posture, review state, release state, and lifecycle state.

Before any live KHRI access or admission behavior exists, governance must provide:

1. one accepted SourceDescriptor contract/schema/validator authority;
2. stable KHRI product-level source IDs and descriptor versions;
3. explicit product scope, source type, source role, authority rank, publisher, and steward;
4. reviewed rights, attribution, redistribution, retention, disclaimer, and permitted-use posture;
5. cultural sensitivity, privacy, exact-location, geometry, public-transform, and join policy;
6. cadence, access method, rate/size limits, citation, and observed source-head evidence;
7. admissibility limits, review state, activation state, lifecycle handoff class, and public-release posture;
8. an accepted registry/control-plane entry where required;
9. safe fixtures, executable tests, and substantive CI.

The control-plane source-authority register currently contains no entries. Package-local files cannot fill that authority gap.

Unknown, missing, placeholder, contradictory, draft, denied, retired, fixture-only, or unreviewed state must prevent live source access and public output.

[Back to top](#top)

---

## KHRI and KSHS surface identity

KHRI is documented as a KSHS-operated per-surface product under a broader KSHS institutional umbrella. The package must preserve, not blur, that structure.

| Surface or authority | Meaning boundary | Prohibited collapse |
|---|---|---|
| KHRI | Historic-resource inventory and related survey/evaluation material within its stated product scope. | Not every KSHS archive, publication, museum, archaeology, parcel, or planning record. |
| Kansas Memory | Digitized cultural heritage and archival carrier surface. | A Kansas Memory image or document is not automatically a KHRI inventory record or designation decision. |
| KSHS State Archives proper | Archival recordkeeping and collection authority within its scope. | Archival custody does not create KHRI resource status, current ownership, or legal designation. |
| NRHP or other designation authority | Separate designation/listing authority within its jurisdiction and time. | KHRI presence, recommendation, or eligibility field is not automatically a final listing decision. |
| GNIS/place authorities | Place-name or feature identity within declared scope. | Place identity does not create KHRI resource identity, parcel boundaries, or historic significance. |
| Assessor, parcel, title, deed, or tax sources | Property and ownership context according to source role and time. | KHRI address or associated owner fields are not current title, tax, occupancy, or parcel truth. |
| Archaeology and cultural-resource registries | Sensitive site/survey/stewardship authority within their governed scope. | KHRI built-resource inventory must not expose restricted archaeology or cultural locations through joins. |
| Generated summaries, maps, or AI text | Downstream carriers derived from governed inputs. | Cannot become original evidence, policy, review, or release authority. |

Each record must retain its source surface, upstream identifier, product family, source role, retrieval context, and source URI. An umbrella institution does not authorize a single descriptor or adapter to cover every surface.

[Back to top](#top)

---

## KHRI record and claim boundaries

KHRI is a source family of records and assessments, not one undifferentiated truth feed.

| Record or field family | Candidate meaning | Prohibited inference |
|---|---|---|
| Inventory resource record | KHRI identifies and describes a resource within a stated inventory scope and vintage. | Presence in inventory is not final legal protection, current existence, public accessibility, ownership, or condition. |
| Building, structure, site, object, or district type | Source-native resource classification at the record's time and method. | Not a parcel boundary, zoning class, archaeological site classification, or current land use without corroboration. |
| Survey or nomination material | A survey, evaluation, nomination, or supporting record with author, method, scope, and date. | Not a final designation or legal decision unless the issuing authority and decision state are explicit. |
| Eligibility, recommendation, or significance assessment | Time-scoped professional or administrative assessment. | Not final listed status, legal protection, compliance clearance, or timeless significance. |
| Designation or listing reference | Reference to a separate designation authority or decision. | Do not upgrade a cross-reference, candidate, recommendation, or stale field into current designation truth. |
| Location or geometry | Source-reported or derived location with method, precision, uncertainty, and sensitivity state. | Not guaranteed parcel, entrance, ownership, public-access, or safe public precision. |
| Address | Source-reported address or location label at a stated time. | Not current residence, mailing address, occupancy, parcel, or title truth. |
| Owner, occupant, architect, builder, or associated person | Historical/source-reported association within stated role and period. | Not current ownership, living-person identity, contact information, or relationship truth. |
| Construction, alteration, demolition, condition, or use | Time-scoped source assertion or observation. | Not current condition, current existence, code compliance, hazard status, or permitted use. |
| Photograph, scan, report, map, attachment, or document | Linked or embedded carrier with its own identity, rights, and sensitivity. | Metadata availability does not imply redistribution rights or public-safe contents. |
| Archaeological or culturally sensitive indicator | Review signal requiring steward and sensitivity controls. | Never infer public exact location, absence, access permission, consultation completion, or release approval. |
| Crosswalk to NRHP, local register, GNIS, parcel, Wikidata, or other source | Relationship candidate with mapping method and confidence. | A join does not merge authorities or let one source overwrite another's role and time. |

When a record mixes multiple meanings, the package must preserve field-level provenance and either split candidates or require an accepted multi-role contract. Convenience is not a source-role rule.

[Back to top](#top)

---

## Rights, cultural sensitivity, privacy, and geometry

### Rights

No live source access, persistence, fixture reuse, redistribution, screenshot/media handling, or public output is permitted until current terms and source-steward review establish:

- automated-access permission and access conditions;
- attribution and citation requirements;
- redistribution and derivative permissions;
- commercial-use posture;
- disclaimer and compelled-link language;
- caching, retention, and archive limits;
- treatment of photographs, scans, maps, attachments, reports, downloads, and GIS files;
- correction, withdrawal, and stale-state expectations.

Unknown, no-assertion, denied, expired, or contradictory rights fail closed.

### Cultural sensitivity and sovereignty

The archaeology source-registry guide states that exact archaeological geometry, sacred or burial-associated locations, human-remains contexts, private-landowner geometry, and collection-security details are deny-by-default for public surfaces unless required cultural/steward review, sensitivity transform, and redaction receipt exist.

The package must therefore hold, quarantine, deny, or generalize when a KHRI record or join may reveal:

- archaeological sites or candidate features;
- sacred, ceremonial, burial, funerary, human-remains, or culturally restricted places;
- tribal, sovereign, steward-controlled, or consultation-sensitive information;
- vulnerable collections, access points, security details, or looting risk;
- exact geometry that can reconstruct a withheld location;
- attachments or narratives whose text reveals restricted context even when geometry is removed.

A public-facing source page or apparently public address does not override record-level cultural review.

### Privacy and private property

Default-deny or review-required material includes:

- living-person names, contact details, submitter/reviewer identities, signatures, phone numbers, emails, or private notes;
- current residences, private-property access routes, owner/occupant joins, and nonpublic parcel details;
- records where historical person fields can be confused with current identity or ownership;
- ecological, infrastructure, cultural, or security sensitivity created through cross-source joins;
- public derivatives lacking an approved transform and receipt.

### Geometry

Every candidate must preserve or explicitly account for:

- native geometry type and source CRS/datum;
- coordinate, address, parcel, centroid, boundary, or narrative derivation method;
- observed, reported, inferred, geocoded, generalized, buffered, centroided, withheld, or null status;
- precision and uncertainty;
- geometry vintage and source-feature identity;
- public versus steward-only geometry;
- transform/generalization identity and review state.

False precision, undocumented geocoding, coordinate swaps, invalid ranges, silent centroiding, unreviewed parcel joins, or reconstruction of withheld locations must fail or quarantine.

[Back to top](#top)

---

## Identity, time, and correction

A KHRI candidate must preserve identity and time without overwriting history.

### Identity

Preserve, when available:

- stable KHRI record/inventory identifier;
- source surface and product identifier;
- upstream record version or revision identity;
- resource, survey, nomination, designation-reference, attachment, and geometry identities;
- source URI and retrieval/request identity;
- related/superseded/corrected record references;
- crosswalk target, mapping method, confidence, and reviewer state.

Missing or colliding identity must hold or quarantine. Do not use a mutable title, address, owner name, or geometry as the sole durable identity.

### Time

Keep distinct where material:

- resource construction or historical-period dates;
- survey, nomination, evaluation, decision, designation, alteration, demolition, or observation dates;
- record effective/valid interval;
- upstream revision/update time;
- retrieval time;
- KFM review time;
- release time;
- correction, withdrawal, or supersession time.

Retrieval time must not substitute for historical, survey, decision, or validity time. A later retrieval must not silently replace an earlier meaning.

### Corrections and withdrawals

The package may signal correction, supersession, withdrawal, deletion, or source drift. It must not erase prior lineage, decide public correction text, or mutate released artifacts directly. External governed systems own correction notices, release aliases, and rollback.

[Back to top](#top)

---

## Lifecycle boundary

```text
KHRI source edge / pre-RAW
        ↓
package returns caller-owned bytes or admission candidate
        ↓
external governed orchestrator
        ├── DENY / ABSTAIN / ERROR / HOLD
        ├── QUARANTINE candidate
        └── RAW candidate after descriptor, activation, rights,
            cultural-sensitivity, privacy, and geometry gates
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

The package owns only the bounded source edge. It cannot skip, merge, or authorize later phases. Promotion is a governed state transition, not a fetch, parse, file copy, directory move, commit, pull request, merge, or receipt.

[Back to top](#top)

---

## Failure contract

Unsafe or incomplete input must produce one finite, inspectable outcome.

| Semantic outcome | Use |
|---|---|
| `HOLD` | Structurally parseable record lacks required governance, mapping, identity, or review state. |
| `QUARANTINE` | Record may be useful but cannot safely advance; reasons and safe references are preserved. |
| `DENY` | Requested access, transform, exposure, join, or use is prohibited. |
| `ABSTAIN` | Evidence, identity, mapping, temporal support, or spatial support is insufficient for the requested interpretation. |
| `ERROR` | Deterministic contract, transport, parse, or operational failure; no permissive fallback. |

The exact enum and candidate-envelope contract remain `NEEDS VERIFICATION`. Code must use the accepted shared contract rather than create an incompatible package-local vocabulary.

A safe failure includes:

- stable reason code;
- non-sensitive human-readable explanation;
- affected field or governance gate;
- safe source/product/descriptor reference when allowed;
- retryability or remediation class;
- no partial public result;
- no side effect outside caller-owned temporary state.

[Back to top](#top)

---

## Validation

Future implementation must prove at least:

- package import is side-effect-free and no-network;
- zero executable tests and unexpected skipped negative tests fail readiness review;
- descriptor shape and activation state resolve from accepted authority surfaces;
- the current four-field placeholder is rejected;
- KHRI product family, source surface, source role, and authority rank are explicit;
- narrative `administrative` role language is not silently mapped to a machine enum;
- KHRI, Kansas Memory, State Archives, NRHP, GNIS, parcel, archaeology, and generated surfaces remain distinct;
- inventory presence, eligibility, recommendation, designation, location, ownership, condition, and current existence do not collapse;
- upstream identity, source URI, product ID, version, amendment, and supersession links are preserved;
- historical, survey, decision, effective, retrieval, review, release, and correction times remain distinct;
- source-native resource/status/designation values survive unresolved crosswalks;
- rights, attribution, redistribution, retention, disclaimer, and media posture fail closed;
- cultural sensitivity, privacy, exact location, geometry, attachment contents, and join-induced risk fail closed;
- geometry type, CRS/datum, derivation, precision, uncertainty, withholding, and transform metadata are preserved;
- parsing and normalization are deterministic and retain unknown source values;
- network, credentials, production filesystem, lifecycle roots, registry, proof, receipt, catalog, and release writes are denied by default;
- no public map, tile, API payload, report, summary, alert, citation, evidence claim, or AI answer is emitted;
- path migration cannot create duplicate packages, descriptors, fixtures, tests, source-head state, or lineage;
- substantive CI executes real package and test commands rather than TODO-only echo steps.

### Negative decision matrix

| Condition | Required result |
|---|---|
| Missing or invalid descriptor | No source access; hold, quarantine, or deny. |
| Missing, draft, denied, retired, or fixture-only activation | No live source access. |
| Unknown rights or terms | No persistence/public output; fail closed. |
| Unknown sensitivity/cultural review | No public output; hold or deny. |
| Unknown product family or source role | Hold/quarantine; no umbrella fallback. |
| `administrative` narrative role mapped by convenience | Fail pending accepted role crosswalk. |
| Inventory record treated as final legal designation | Fail. |
| Eligibility/recommendation treated as listed status | Fail. |
| Historical owner/occupant treated as current person or title truth | Fail. |
| Address treated as parcel, residence, or access permission | Fail. |
| Range/location geometry treated as safe exact public location | Fail or quarantine. |
| Archaeological/cultural indicator exposed without review | Deny public output. |
| Retrieval time substituted for survey/decision/effective time | Fail. |
| Sensitive join becomes less restrictive than an input | Fail. |
| Attachment or log leaks restricted text, image, identity, or geometry | Fail. |
| Direct lifecycle, evidence, catalog, proof, registry, or release write | Fail. |
| Current or proposed Kansas-family path declares canonical implementation without migration evidence | Fail migration review. |
| Same controlled inputs yield different candidate or reason codes | Fail determinism. |
| Green workflow runs only TODO echo steps | Do not count as implementation proof. |

[Back to top](#top)

---

## Review burden

| Reviewer role | Required focus |
|---|---|
| Connector/package maintainer | Package API, transport, parsing, side effects, determinism, dependencies, and migration compatibility. |
| Kansas/KHRI source steward | Product inventory, source identity, current access surfaces, cadence, corrections, and source-native fields. |
| KSHS/SHPO liaison | Institutional/surface boundaries, survey/designation semantics, stewardship, and official-source context. |
| Archaeology/cultural-review steward | Exact locations, sacred/burial/human-remains contexts, sovereignty, consultation, collection security, and redaction. |
| Settlements/historic-resources steward | Resource types, districts, surveys, built-environment semantics, and place/time interpretation. |
| People/privacy reviewer | Historical versus living-person fields, current residences, private contacts, ownership/occupancy ambiguity, and joins. |
| Rights reviewer | Terms, attribution, redistribution, retention, media, attachments, fixtures, and public derivatives. |
| Sensitivity reviewer | Public geometry, private property, cultural places, sensitive facilities, joins, logs, and fixture safety. |
| Security reviewer | Network/credential posture, retries, request logging, parsers, archives/media, dependencies, and CI artifacts. |
| Contract/schema reviewer | Accepted SourceDescriptor, candidate, receipt, and failure shapes plus role migration. |
| Test/validation steward | Discovery, negative cases, reason codes, no-side-effect assertions, safe fixtures, and substantive CI. |
| Migration/architecture reviewer | Winning path, imports, source IDs, consumers, deprecation, history, backlinks, and rollback. |

Exact individual owners and GitHub teams remain `UNKNOWN`; do not invent assignments.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| Prior `connectors/khri/src/khri/README.md` blob | **CONFIRMED** | Previous speculative boundary and exact rollback target. | Implementation or accepted path placement. |
| `connectors/khri/pyproject.toml` | **CONFIRMED** | Distribution name and version `0.0.0`. | Buildability, dependencies, Python support, or runtime. |
| `__init__.py`, `fetch.py`, `admit.py`, `descriptor.yaml` | **CONFIRMED** | Empty initializer, comment-only behavior modules, and four-field placeholder. | Fetching, parsing, admission, handoff, or source authority. |
| Exact absent module/test probes | **CONFIRMED AT NAMED PATHS** | Richer v0.1 module map and conventional tests were not present at those names. | Absence of differently named or generated implementation. |
| Parent, source-layout, and test READMEs | **CONFIRMED v0.1 DOCUMENTATION** | Compatibility intent, proposed boundaries, and local documentation topology. | Executable behavior, test coverage, or accepted migration. |
| Exact `connectors/kansas/khri/` probes | **NOT FOUND AT NAMED PATHS** | The dossier's path claim is not currently proven as an implemented child lane. | Total absence of differently represented work. |
| KHRI source dossier | **CONFIRMED DRAFT DOCUMENTATION** | KSHS-operated per-surface framing, Kansas-first authority posture, product/claim context, and placement intent. | Machine descriptor, current endpoint/terms, package migration, activation, or release. |
| KSHS umbrella dossier | **CONFIRMED DOCUMENTATION** | Institutional anti-collapse and need for surface-specific descriptors. | KHRI-specific runtime behavior. |
| Archaeology source-registry guide | **CONFIRMED DRAFT DOCTRINE/DOCPATH** | Deny-by-default exact cultural locations, role separation, cultural/steward review, and source-admission posture. | Implemented KHRI policy or machine registry records. |
| SourceDescriptor contract/schema | **CONFIRMED REPOSITORY SURFACES; STATUS PROPOSED** | Required field surface, deprecated aliases, machine role vocabulary, rights/sensitivity gates, and activation states. | A conforming KHRI descriptor or one accepted canonical schema path. |
| Source-authority register | **CONFIRMED EMPTY** | No established machine authority entry at the inspected register. | That no authority evidence exists elsewhere. |
| Connector/descriptor workflows | **CONFIRMED TODO-ONLY** | Workflow scaffolding. | Package import, test collection, descriptor conformance, rights review, or enforcement. |
| Directory Rules | **CONFIRMED PLACEMENT DOCTRINE** | Responsibility roots, lifecycle invariant, compatibility discipline, fixtures/tests separation, migration, and no-parallel-authority rules. | Resolution of current package and role conflicts. |

No live KHRI endpoint, payload, current terms page, credential, runtime log, deployed service, EvidenceBundle, release manifest, or public client was inspected for this documentation update.

[Back to top](#top)

---

## ADRs and migration

This README creates no ADR and resolves no migration.

An accepted ADR or explicit governed migration record is required before any change that:

- moves or duplicates the package;
- classifies this path as legacy, mirror, deprecated, transitional, redirect, or retained implementation;
- changes distribution, import, source, or product IDs;
- chooses one versus multiple KHRI product adapters;
- maps narrative `administrative` role language to the current machine source-role enum;
- changes fixture or test routing;
- creates parallel descriptor, registry, policy, schema, receipt, proof, release, or publication homes;
- establishes a public sensitivity or geometry default;
- retires this path or promotes it from compatibility posture.

A README may expose these conflicts. It cannot settle them by wording alone.

[Back to top](#top)

---

## Definition of done

### This documentation revision

- [x] Current package maturity and exact files are explicit.
- [x] The speculative v0.1 module map is replaced by verified presence and bounded absence evidence.
- [x] The source-dossier path claim is separated from actual package placement.
- [x] Directory Rules responsibility roots and lifecycle law are preserved.
- [x] KHRI/KSHS surface identity and product/claim anti-collapse controls are explicit.
- [x] Rights, cultural sensitivity, sovereignty, privacy, exact location, geometry, time, attachments, and joins fail closed.
- [x] Inputs, outputs, failure semantics, validation, review, migration, rollback, and backlog are explicit.
- [x] No implementation, activation, or release maturity is overclaimed.

### Package readiness remains open

- [ ] Accepted package path, import identity, product topology, source IDs, compatibility class, losing-path disposition, and migration plan.
- [ ] Accepted SourceDescriptor contract/schema/validator authority and conforming KHRI product descriptors.
- [ ] Reviewed authority/control-plane entries, activation decisions, and source-head evidence.
- [ ] Current access surfaces, endpoint shapes, terms, attribution, redistribution, retention, cadence, rate/size limits, correction, and withdrawal posture.
- [ ] Accepted resource, survey, evaluation, designation, place, person, parcel, and crosswalk contracts.
- [ ] Implemented cultural-sensitivity, privacy, geometry, attachment, and public-transform policies.
- [ ] Implemented package configuration, transport/parser/admission interfaces, finite candidate envelope, and deterministic reason codes.
- [ ] Safe reviewed fixtures and executable no-network negative tests.
- [ ] Substantive CI with non-zero collection, zero-discovery failure, and demonstrated boundary failures.
- [ ] Evidence, catalog, policy, review, release, correction, and rollback closure outside the package.

Documentation completeness does not imply package readiness, source admission, activation, rights clearance, cultural/sensitivity clearance, evidence closure, or publication.

[Back to top](#top)

---

## Rollback

Rollback is required if this README is used to claim accepted canonicality, completed migration, executable package behavior, live source access, activation, rights clearance, cultural/sensitivity clearance, safe exact-location exposure, lifecycle authority, evidence closure, or release readiness.

Before merge, close the draft pull request and abandon the scoped branch if the revision is rejected.

After merge, restore prior README blob:

```text
5741fedb6269d272585413d0f947b2137333e4ab
```

through a transparent revert commit or revert pull request, then rerun applicable documentation, link, connector-boundary, policy, sensitivity, and rollback checks. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Complete recursive package and consumer inventory | **UNKNOWN** | Mounted checkout or non-truncated tree/import receipt at reviewed commit. |
| Final connector/package home | **CONFLICTED** | Accepted ADR/migration, consumer inventory, import/source-ID plan, deprecation, and rollback. |
| Compatibility class of `connectors/khri/` | **CONFLICTED / NEEDS VERIFICATION** | Accepted legacy/mirror/redirect/transitional/retained decision. |
| Existence and role of `connectors/kansas/khri/` | **NOT ESTABLISHED AT NAMED PROBES** | Current tree evidence and accepted placement/migration record. |
| KHRI product-family topology | **NEEDS VERIFICATION** | Accepted inventory of portal/search, survey, designation, attachment, geometry, and restricted products. |
| SourceDescriptor schema and validator authority | **CONFLICTED / PROPOSED** | One accepted contract/schema, migration, fixtures, validator, and CI command. |
| `administrative` narrative-to-machine role mapping | **CONFLICTED** | Accepted role vocabulary/crosswalk and negative tests. |
| Product descriptors and authority entries | **NOT ESTABLISHED** | Conforming records and reviewed registry/control-plane entries. |
| Activation decisions and source-head evidence | **NOT ESTABLISHED** | Reviewed activation records and approved source-head observations. |
| Current access surfaces, endpoints, product schemas, and cadence | **NEEDS VERIFICATION** | Current authoritative KSHS/KHRI documentation and source-steward review. |
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

Keep this package small, deterministic, no-network by default, and subordinate to evidence and policy.

The smallest safe implementation sequence is:

1. settle package path, compatibility class, product/source IDs, descriptor authority, role vocabulary, fixture home, and test routing;
2. replace the local descriptor placeholder with an accepted external reference or governed migration shim;
3. add one invented invalid KHRI-shaped descriptor fixture with no real person, property, coordinate, attachment, endpoint, credential, or source payload;
4. prove import and network denial;
5. prove one deterministic fail-closed candidate with no side effects;
6. add surface, inventory/designation, rights, cultural sensitivity, privacy, identity, time, geometry, attachment, join, and migration negatives;
7. only then consider a reviewed, opt-in source probe.

Do not build new authority here. Let SourceDescriptor, policy, EvidenceBundle, review, release, correction, and rollback surfaces carry their own responsibilities.

[Back to top](#top)
