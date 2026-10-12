<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-khri-src-readme
title: connectors/khri/src/ — KHRI Greenfield Source Layout Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas/KHRI source steward · KSHS/SHPO liaison · Archaeology steward · Settlements steward · People/privacy reviewer · Rights reviewer · Sensitivity/cultural-review steward · Security reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; greenfield-source-layout; compatibility-path; canonical-family-conflict; source-admission; historic-resource-anti-collapse; rights-fail-closed; cultural-sensitivity-fail-closed; private-location-fail-closed; no-network; no-activation; no-publication
current_path: connectors/khri/src/README.md
truth_posture: CONFIRMED source layout contains one khri package scaffold with merged v0.2 package documentation, empty initializer, comment-only fetch/admit modules, nonconforming four-field descriptor, and documentation-only local test lane; named richer modules and conventional tests were not found at exact probes / CONFLICTED final package path, compatibility class, source-role mapping, SourceDescriptor authority, product decomposition, fixture/test routing, registry activation, and public sensitivity floor / PROPOSED bounded source-layout and future source-admission implementation contract / UNKNOWN buildability, imports, executable behavior, test collection, live source access, current rights and terms, endpoint/source-head state, substantive CI enforcement, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  prior_blob: 234df59446b68e0e08f4104814312e2b0f89b83e
related:
  - ../README.md
  - ../pyproject.toml
  - ../tests/README.md
  - ./khri/README.md
  - ./khri/__init__.py
  - ./khri/fetch.py
  - ./khri/admit.py
  - ./khri/descriptor.yaml
  - ../../README.md
  - ../../kansas/README.md
  - ../../../CONTRIBUTING.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/kansas/khri.md
  - ../../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../../docs/domains/archaeology/SOURCE_REGISTRY.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/README.md
  - ../../../fixtures/README.md
  - ../../../tests/README.md
  - ../../../tests/fixtures/README.md
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../.github/workflows/connector-gate.yml
  - ../../../.github/workflows/source-descriptor-validate.yml
  - ../../../release/
tags: [kfm, connectors, khri, kshs, shpo, kansas, historic-resources, archaeology, settlements, cultural-resources, src, source-layout, python, package, greenfield, compatibility, source-admission, source-role, rights, sensitivity, privacy, geometry, no-network, raw, quarantine, governance]
notes:
  - "The v0.1 source-layout README said only this file and the child README were confirmed. Direct repository evidence now establishes the package scaffold and makes that inventory stale."
  - "The child package README is v0.2 and records an empty __init__.py, comment-only fetch.py and admit.py, a nonconforming four-field descriptor.yaml, exact absent helper-module probes, and no established conventional local tests."
  - "The KHRI source dossier states connectors/kansas/khri/ is the correct connector path, but exact current probes did not establish that child path. Documentation intent and implemented package location remain conflicted."
  - "The source dossier and archaeology guide use the narrative role administrative, while the current populated SourceDescriptor machine enum does not. This layout selects no convenience mapping."
  - "The connector-gate and source-descriptor-validate workflows execute TODO echo steps; green completion cannot prove KHRI package imports, test collection, descriptor conformance, rights review, cultural-sensitivity enforcement, or release readiness."
  - "Only this Markdown file is changed. No code, package metadata, descriptor, registry entry, fixture, test, workflow, contract, schema, policy, source payload, credential, activation decision, lifecycle artifact, evidence object, release object, path move, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KHRI Greenfield Source Layout Boundary

> Repository-grounded boundary for `connectors/khri/src/`. The layout contains a real `khri` Python package scaffold, but no supported connector behavior. This README defines how implementation code may be organized without turning the source layout into a parallel authority, lifecycle store, release engine, or cultural-resource publication surface.

**Document lifecycle:** `draft v0.2`  
**Current layout maturity:** `CONFIRMED` greenfield source layout with a non-operational `0.0.0` package scaffold  
**Owner:** `OWNER_TBD`  
**Path posture:** repository-present; compatibility intent documented; final package home and migration state `CONFLICTED / NEEDS VERIFICATION`  
**Boundary:** no live network · no activation · no package-local authority · no direct lifecycle persistence · no evidence closure · no release · no publication

> [!IMPORTANT]
> The child package contains an empty `__init__.py`, comment-only `fetch.py` and `admit.py`, and a four-field `descriptor.yaml` placeholder. These files prove package presence only. They do not implement transport, parsing, normalization, source admission, quarantine, handoff, tests, or runtime behavior.

> [!CAUTION]
> KHRI material may include archaeological or culturally restricted locations, historic-resource geometry, private-property details, historical or living-person associations, eligibility and designation evaluations, photographs, survey attachments, and collection-security information. Unknown rights, product identity, source role, cultural review, sensitivity, geometry precision, or public-release posture fails closed.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Current layout](#current-layout) · [Repository fit](#repository-fit) · [Path conflict](#path-and-migration-conflict) · [Allowed contents](#allowed-contents) · [Forbidden contents](#forbidden-contents) · [Package boundary](#package-boundary) · [Inputs and outputs](#inputs-and-outputs) · [Descriptor boundary](#descriptor-registry-and-activation-boundary) · [Surface identity](#khri-and-kshs-surface-identity) · [Record meanings](#khri-record-and-claim-boundaries) · [Rights and sensitivity](#rights-cultural-sensitivity-privacy-and-geometry) · [Time and identity](#identity-time-and-correction) · [Lifecycle](#lifecycle-boundary) · [Failure contract](#failure-contract) · [Validation](#validation) · [Fixtures and tests](#fixtures-and-tests) · [Review](#review-burden) · [Evidence](#evidence-basis) · [ADRs](#adrs-and-migration) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/khri/src/` is the implementation-layout container for the repository-present KHRI connector scaffold.

Its current purpose is to:

- expose the exact package files that exist;
- prevent documentation and placeholder modules from being mistaken for an operational connector;
- define what belongs in the package namespace versus contracts, schemas, registries, policy, fixtures, tests, evidence, lifecycle, and release roots;
- preserve the unresolved relationship between the present package and the documented Kansas-family KHRI placement;
- prevent KHRI, Kansas Memory, KSHS State Archives proper, NRHP, GNIS, assessor/parcel records, archaeology records, and generated derivatives from collapsing into one source surface;
- require fail-closed rights, cultural-sensitivity, privacy, location, geometry, temporal, and review behavior;
- keep future package output limited to caller-owned bytes or admission candidates;
- make implementation, validation, migration, and rollback obligations inspectable before code is added.

This source layout does not declare either the present top-level package or the documented Kansas-family path to be the accepted final implementation home. That requires an accepted migration or architecture decision supported by repository evidence.

[Back to top](#top)

---

## Authority level

**Implementation layout only.** The `src/` directory organizes package code. It has no independent authority over source identity, contract meaning, schema shape, rights, cultural sensitivity, privacy, lifecycle state, evidence, catalog closure, release, correction, rollback, or public delivery.

| Concern | Owning surface | Source-layout boundary |
|---|---|---|
| Source-specific fetch, probe, preservation, parsing, packaging, and admission mechanics | `connectors/` | Code may live below this layout after governance and migration decisions exist. |
| Object meaning | `contracts/` | Package code consumes accepted contracts; it does not redefine them. |
| Machine-checkable shape | `schemas/` | Package code validates against accepted schemas; local classes do not become schema authority. |
| Source identity, role, rights, sensitivity, cadence, access, and activation | registry and control-plane surfaces | A local YAML or module cannot mint source authority or activation. |
| Allow, deny, restrict, redact, abstain, or hold policy | `policy/` | Package code applies returned policy decisions; it does not invent policy. |
| Fixtures and enforceability proof | accepted `fixtures/` and `tests/` lanes | Test support may import the package, but fixture truth and test authority do not move into `src/`. |
| Lifecycle persistence | `data/` under governed orchestration | Package code returns candidates; it does not write lifecycle phases directly. |
| Evidence and process records | proof and receipt lanes | Parsed candidates and logs are not EvidenceBundles or release proofs. |
| Release, correction, withdrawal, and rollback | `release/` and governed lifecycle surfaces | A package, commit, pull request, or successful fetch cannot publish. |

[Back to top](#top)

---

## Current layout

Direct repository reads and the merged child package README establish this bounded layout:

```text
connectors/khri/
├── pyproject.toml                  # project kfm-connector-khri, version 0.0.0
├── src/
│   ├── README.md                   # this source-layout boundary
│   └── khri/
│       ├── README.md               # v0.2 package scaffold boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only greenfield placeholder
│       ├── admit.py                # comment-only greenfield placeholder
│       └── descriptor.yaml         # four-field greenfield placeholder
└── tests/
    └── README.md                   # documentation-only test boundary, currently v0.1
```

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| [`../pyproject.toml`](../pyproject.toml) | Project `kfm-connector-khri`, version `0.0.0`. | No build backend, dependencies, Python constraint, package discovery, entry point, or command is established. |
| [`./khri/README.md`](./khri/README.md) | v0.2 package boundary. | Reliable documentation of the bounded package scaffold; not executable proof. |
| [`./khri/__init__.py`](./khri/__init__.py) | Empty. | No import API or import-time registration. |
| [`./khri/fetch.py`](./khri/fetch.py) | One placeholder comment. | No transport, endpoint, authentication, pagination, rate limiting, retry, caching, source-head, or correction behavior. |
| [`./khri/admit.py`](./khri/admit.py) | One placeholder comment. | No parsing, validation, finite disposition, quarantine, candidate envelope, or sink behavior. |
| [`./khri/descriptor.yaml`](./khri/descriptor.yaml) | Four legacy-style fields with unresolved role and rights. | Nonconforming placeholder; no authority, activation, or release effect. |
| [`../tests/README.md`](../tests/README.md) | Documentation-only compatibility test contract. | Does not prove test discovery, execution, coverage, fixture safety, or substantive CI. |

The richer helper modules named in v0.1 were not found at exact probes:

```text
descriptors.py
parse.py
normalize.py
roles.py
identity.py
sensitivity.py
geometry.py
handoff.py
errors.py
```

Likewise, conventional local files named `conftest.py`, `test_fetch.py`, `test_admit.py`, and `test_descriptor.py` were not found at the tested paths. These are bounded absence statements; differently named, generated, unindexed, or later-added files remain `UNKNOWN`.

[Back to top](#top)

---

## Repository fit

Directory Rules make responsibility, not subject matter, the placement test.

`connectors/khri/src/` is valid as an implementation layout because it sits under the `connectors/` responsibility root. KHRI's archaeology, historic-resource, settlement, and person associations do not make `src/` a domain truth root. Domain ownership, policy, evidence, and release remain elsewhere.

The current layout must stay boring:

- one package namespace unless an accepted product-adapter design requires more;
- no duplicate schema, contract, descriptor, registry, policy, fixture, proof, receipt, or release homes;
- no direct public client coupling;
- no lifecycle persistence;
- no secret discovery;
- no hidden activation;
- no model-generated authority;
- no parallel implementation created merely to satisfy documentation wording.

[Back to top](#top)

---

## Path and migration conflict

Current evidence shows a divergence between documentation intent and implemented package location.

| Surface | Observed posture | Current implication |
|---|---|---|
| `connectors/khri/src/khri/` | Repository-present `0.0.0` package scaffold. | Actual package placeholder exists here today; presence does not establish final canonicality. |
| `connectors/khri/` | Parent README calls the lane compatibility/noncanonical. | Compatibility intent exists, but its exact class is not backed by an accepted migration record reviewed here. |
| `connectors/kansas/khri/` | Named by the KHRI source dossier as the correct connector path. | Exact probes did not establish a README or placeholder there during the package evidence pass; executable migration is not proven. |
| `connectors/kansas/` | Kansas source-family coordination lane. | Valid family context; does not by itself prove child-package presence or migration completion. |

Directory Rules require a compatibility surface to declare whether it is legacy, mirror, deprecated, external-export, or transitional. The current top-level KHRI documentation uses compatibility language but does not point to an accepted migration decision that fully settles this classification.

A safe path decision must resolve together:

- winning package location and losing-path disposition;
- distribution and import names;
- KHRI product-adapter topology;
- stable source and product identifiers;
- descriptor, registry, and activation references;
- fixture and test routing;
- workflow and source-head state;
- receipt, evidence, correction, withdrawal, and supersession lineage;
- consumer imports and documentation backlinks;
- deprecation schedule and rollback.

Until then, do not create a second evolving package under `connectors/kansas/khri/`, and do not promote this path to canonical authority by convention.

[Back to top](#top)

---

## Allowed contents

After accepted package and migration decisions exist, this layout may contain:

- one or more explicitly approved Python package namespaces;
- package-level README files;
- dependency-injected source client interfaces;
- deterministic parsers for identified KHRI product shapes;
- source-native metadata preservation;
- KHRI/KSHS surface and product dispatch;
- source-role enforcement using accepted vocabulary;
- resource, survey, evaluation, designation, location, and attachment identity preservation;
- temporal, geometry, precision, uncertainty, withholding, and transform metadata preservation;
- finite hold, quarantine, deny, abstain, error, no-op, retry, stale, and drift outcomes using accepted shared contracts;
- caller-owned immutable bytes, source-native records, or admission candidates;
- migration shims, warnings, and compatibility adapters approved by an ADR or migration record;
- lightweight package-internal test helpers that contain no authority-bearing fixtures or sensitive payloads.

Every module must remain subordinate to accepted contracts, schemas, descriptors, policy, validation, and release state.

[Back to top](#top)

---

## Forbidden contents

Do not place or infer the following under this source layout:

- canonical contracts or JSON Schemas;
- source registry, authority, activation, rights, sensitivity, or release records;
- policy-as-code or discretionary cultural-review decisions;
- production credentials, tokens, cookies, sessions, signed URLs, or secret-manager material;
- bulk source harvests, archives, media dumps, survey packages, or fixture corpora;
- exact archaeological, sacred, burial-associated, human-remains, private-property, or security-sensitive geometry;
- authoritative archaeology, legal designation, title, ownership, occupancy, current condition, current existence, or access-permission truth outside declared source scope;
- evidence bundles, proof packs, promotion decisions, release manifests, corrections, withdrawals, or rollback cards;
- direct writes to RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, registry, proof, receipt, or release roots;
- public maps, tiles, APIs, reports, alerts, exports, summaries, citations, or AI answers;
- a second independently evolving KHRI implementation at a competing path;
- generated text, crosswalks, joins, or models presented as source authority.

[Back to top](#top)

---

## Package boundary

The child package README owns package-specific detail. This layout README owns only the broader placement boundary.

The source layout must ensure that:

- package modules do not escape the `connectors/` responsibility boundary;
- helper modules remain source-specific rather than becoming shared contract, schema, policy, or evidence libraries;
- product-specific adapters are created only after product identity and source-role design are accepted;
- imports are side-effect-free;
- network access is explicit, injected, reviewed, and disabled by default;
- package outputs remain caller-owned;
- test helpers do not carry real sensitive KHRI content;
- migration compatibility is explicit and time-bounded;
- the package cannot upgrade a descriptor, policy, review, evidence, or release state.

A package directory is not a source activation decision. An importable class is not a SourceDescriptor. A parser result is not a KFM claim.

[Back to top](#top)

---

## Inputs and outputs

### Allowed future inputs

Executable code below this layout may accept only explicit caller-supplied inputs such as:

- a reviewed product-specific descriptor or stable reference to one;
- an activation decision appropriate to the requested operation;
- a declared KHRI source surface, product family, source type, role, and authority rank;
- immutable response bytes, a local file reference, or injected transport result;
- retrieval context containing source URI, source head, retrieval time, request identity, and safe response metadata;
- caller-supplied timeout, retry, rate-limit, pagination, cache, clock, UUID, and temporary-directory policy;
- accepted resource, status, designation, place, person, parcel, and crosswalk references;
- rights, cultural-sensitivity, privacy, geometry, and review references;
- an explicit external sink or callback interface.

The package must not discover production credentials, infer activation, guess a source role, or silently contact a source during import, tests, documentation builds, or ordinary validation.

### Allowed future outputs

A future package may return bounded, caller-owned values such as:

- immutable fetched bytes plus safe retrieval metadata;
- a parsed source-native record retaining original fields and qualifiers;
- a normalized admission candidate with explicit product, role, identity, time, geometry, rights, sensitivity, review, and provenance references;
- a finite hold, quarantine, deny, abstain, error, accepted-for-external-handoff, retry, stale, drift, or no-op result;
- stable reason codes and non-sensitive explanations;
- a receipt candidate or evidence reference for an external orchestrator to validate and persist.

The package must not persist lifecycle state. An accepted external orchestrator decides whether a candidate may enter governed RAW or QUARANTINE handling.

[Back to top](#top)

---

## Descriptor, registry, and activation boundary

The package-local `descriptor.yaml` is not a conforming `SourceDescriptor`.

| Local field | Current value | Fail-closed interpretation |
|---|---|---|
| `name` | `khri` | Package or agency-surface shorthand, not necessarily a stable product-specific `source_id`. |
| `role` | `TBD` | Unresolved legacy alias; not an accepted machine role. |
| `rights` | `TBD` | No permission, attribution, redistribution, media, retention, or derivative-use decision. |
| `sensitivity_floor` | `public` | Deprecated permissive alias; not reviewed cultural, location, privacy, attachment, or join clearance. |

The current SourceDescriptor contract requires a much richer surface, including stable identity and version, source type and role, authority rank, publisher/steward, structured rights, sensitivity, cadence, access, citation, source-head evidence, admissibility limits, public-release posture, review state, release state, and lifecycle state.

Before implementation or source contact, governance must provide:

1. one accepted SourceDescriptor contract and schema authority;
2. stable KHRI product-level source IDs and descriptor versions;
3. explicit source surface, product scope, source type, role, and authority rank;
4. accepted mapping for narrative role language such as `administrative` where needed;
5. reviewed rights, attribution, redistribution, retention, disclaimer, media, and derivative posture;
6. cultural sensitivity, sovereignty, privacy, exact-location, geometry, and public-transform posture;
7. cadence, access method, rate and size limits, citation, and source-head evidence;
8. admissibility limits, review state, activation state, lifecycle class, and public-release posture;
9. reviewed authority/control-plane entries where required;
10. safe fixtures, executable negative tests, and substantive CI.

Unknown, placeholder, contradictory, draft, denied, retired, fixture-only, or unreviewed state prevents live access and public output.

[Back to top](#top)

---

## KHRI and KSHS surface identity

KHRI is a KSHS-operated source surface, but institutional relationship does not collapse product identity.

| Surface | Permitted relationship | Prohibited collapse |
|---|---|---|
| KHRI | Historic-resource inventory, survey, evaluation, status, place, and supporting material within declared product scope. | Not the whole KSHS institutional corpus and not every archaeology or property record. |
| Kansas Memory | Separate digital-collection surface with its own items, rights, metadata, and access posture. | A Kansas Memory item is not automatically a KHRI inventory record or designation source. |
| KSHS State Archives proper | Separate archival holdings and finding-aid surface. | An archival record is not automatically KHRI inventory, designation, ownership, or location truth. |
| NRHP or other designation authorities | Parallel or corroborating legal/designation sources according to accepted role and time. | Crosswalk match is not identity or legal equivalence without evidence. |
| GNIS and other place authorities | Parallel place anchors. | Name similarity is not resource identity, designation, parcel, or exact-location proof. |
| Assessor, parcel, title, address, and property sources | Separate current or historical property context. | KHRI owner, occupant, address, or parcel references are not current title, residence, tax, or access truth. |
| Archaeology registries and steward-controlled records | Separate protected site, survey, or cultural-resource authority. | KHRI references do not authorize disclosure or replace cultural/steward review. |
| Generated joins, maps, summaries, and AI text | Rebuildable derivative carriers. | Cannot mint source authority, resolve ambiguity by fluency, or reveal withheld information. |

[Back to top](#top)

---

## KHRI record and claim boundaries

| Record element | What it may support | What it does not prove by itself |
|---|---|---|
| Inventory presence | The source included a resource or record at a stated time and scope. | Current existence, condition, legal designation, ownership, access, or public safety. |
| Survey form or evaluation | A survey/evaluation occurred using a stated method, date, and criteria. | Final legal determination, designation, eligibility today, or complete site knowledge. |
| Eligibility or recommendation | A time-scoped evaluation or recommendation. | Final listing, current designation, permit approval, or legal effect outside stated authority. |
| Designation/listing field | Source-reported status within a declared jurisdiction, effective time, and citation. | Title, occupancy, current condition, public access, or every related property's status. |
| Historic district boundary | A source-defined district extent at a stated vintage. | That every parcel or resource is contributing, publicly accessible, or culturally non-sensitive. |
| Address, coordinates, or mapped point | Source-native location reference with stated method and uncertainty. | Parcel boundary, current residence, access permission, safe public precision, or archaeological absence. |
| Owner or occupant field | Historical or source-reported association at a stated time. | Current ownership, living-person identity, residence, title, consent, or contact permission. |
| Resource type or use | Source-native classification at a stated time. | Current use, condition, structural safety, or legal zoning. |
| Photograph, plan, attachment, or narrative | Supporting source material with independent rights and sensitivity posture. | Permission to redistribute, expose faces/names, reveal secure locations, or infer missing facts. |
| Crosswalk or external identifier | Candidate or reviewed relationship to another authority. | Identity without matching evidence, versioned mapping, and conflict handling. |
| Generated normalization or summary | Rebuildable representation of admitted inputs. | Sovereign truth, cultural clearance, designation authority, or release approval. |

Unknown or mixed meanings must be retained, split, held, quarantined, or abstained from rather than flattened into a convenient record.

[Back to top](#top)

---

## Rights, cultural sensitivity, privacy, and geometry

### Rights

No live access, persistence, fixture reuse, redistribution, attachment handling, derivative generation, or public output is permitted until current terms and review establish:

- automated and manual access permissions;
- attribution and citation requirements;
- redistribution and derivative permissions;
- retention, caching, and screenshot/media limits;
- treatment of photographs, plans, PDFs, GIS packages, and attachments;
- disclaimer and compelled-link language;
- correction, withdrawal, and stale-state expectations.

Unknown, no-assertion, denied, expired, or contradictory rights fail closed.

### Cultural sensitivity and sovereignty

Default-deny or steward-review material includes:

- archaeological locations and site indicators;
- sacred, ceremonial, burial-associated, cemetery, funerary, or human-remains contexts;
- tribal, sovereign, community-controlled, or culturally restricted knowledge;
- collection-security details, vulnerable structures, access routes, and looting risk;
- attachments or narratives whose restriction is not visible from top-level metadata;
- joins that reconstruct a protected location from generalized inputs.

Public exposure requires the appropriate cultural or steward review, approved transform/generalization, and traceable redaction evidence. Package code cannot make that decision.

### Privacy and private property

Fail closed for:

- living-person names, contact details, residences, submissions, and private correspondence;
- private parcel, owner, occupant, access, security, or interior-location details;
- historical person fields that may refer to a living person or current household;
- joins to parcel, assessor, voter, business, directory, or social data that increase identifiability;
- images or attachments containing faces, signatures, license plates, personal papers, or private interiors.

Historical association is not permission to expose current personal data.

### Geometry

Every candidate must preserve or explicitly account for:

- native geometry type;
- source CRS and datum;
- coordinate method and derivation;
- observed, inferred, generalized, centroided, buffered, withheld, or null state;
- precision and uncertainty;
- geometry vintage and source feature identity;
- transform/generalization identity and reviewer state;
- public versus steward-only geometry separation.

False precision, coordinate swaps, undocumented centroiding, invalid ranges, missing datum where material, and reconstruction of withheld locations fail or quarantine.

[Back to top](#top)

---

## Identity, time, and correction

A future package must preserve, when available:

- KHRI/KSHS source surface;
- product family and record type;
- source-native inventory/resource/survey identifiers;
- stable upstream URL or reference;
- source version, revision, amendment, and supersession links;
- retrieved bytes or safe content identity;
- survey, construction, alteration, evaluation, recommendation, designation, effective, retrieval, review, release, correction, and withdrawal times as distinct fields;
- source-native resource type, status, contributing/noncontributing, and designation vocabulary;
- unresolved mapping and crosswalk version;
- geometry source, vintage, method, precision, and uncertainty;
- attachment identity, rights, sensitivity, and withheld state.

Retrieval time must not replace survey, evaluation, designation, effective, or correction time. A later source version must not silently overwrite prior meaning. Corrections and withdrawals must remain auditable and link to superseded candidates and released derivatives.

[Back to top](#top)

---

## Lifecycle boundary

```text
source edge / pre-RAW
        ↓
package returns caller-owned bytes or admission candidate
        ↓
external governed orchestrator
        ├── DENY / ABSTAIN / ERROR / HOLD
        ├── QUARANTINE candidate
        └── RAW candidate after descriptor, activation, rights, and sensitivity gates
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

The source layout and child package own only the bounded source edge. They cannot persist, skip, merge, or authorize later lifecycle stages.

Promotion is a governed state transition, not:

- a successful HTTP request;
- a parsed record;
- a file write;
- a commit or pull request;
- a merge;
- a connector receipt;
- a map preview;
- a generated summary.

[Back to top](#top)

---

## Failure contract

| Semantic outcome | Use |
|---|---|
| `HOLD` | Structurally parseable material lacks required governance, mapping, or review state. |
| `QUARANTINE` | Candidate may be useful but cannot safely advance; reasons are recorded. |
| `DENY` | Requested access, transform, persistence, disclosure, or use is prohibited. |
| `ABSTAIN` | Identity, evidence, mapping, temporal, spatial, or authority support is insufficient. |
| `ERROR` | Deterministic contract, transport, parse, or operational failure; no permissive fallback. |

The exact enum and envelope remain `NEEDS VERIFICATION`. Package modules must consume the accepted shared contract rather than create incompatible local semantics.

Every failure should carry:

- stable reason code;
- non-sensitive explanation;
- affected field or gate;
- safe source/product/descriptor reference when permitted;
- retryability or remediation class;
- no partial public result;
- no side effect outside caller-owned temporary state.

[Back to top](#top)

---

## Validation

Future implementation below this layout must prove at least:

- imports are side-effect-free and no-network;
- zero executable tests and unexpected skipped negative cases fail readiness review;
- descriptor shape and activation state resolve from accepted authority surfaces;
- the current four-field placeholder is rejected;
- KHRI source surface, product family, source role, and authority rank are explicit;
- narrative `administrative` language is not silently mapped to a machine enum;
- KHRI, Kansas Memory, State Archives, NRHP, GNIS, parcel, archaeology, and generated surfaces remain distinct;
- inventory, survey, evaluation, eligibility, recommendation, designation, location, ownership, condition, and current existence meanings do not collapse;
- upstream identity, source URI, version, amendment, and supersession links are preserved;
- survey, decision, effective, retrieval, review, release, correction, and withdrawal times remain distinct;
- source-native resource, status, and designation values survive unresolved mappings;
- rights, attribution, redistribution, media, retention, and disclaimer posture fail closed;
- cultural sensitivity, sovereignty, privacy, exact location, attachments, and join-induced risk fail closed;
- geometry type, CRS/datum, derivation, precision, uncertainty, withholding, and transform metadata are preserved;
- parsing and normalization are deterministic and preserve unknown source values;
- network, credentials, production filesystems, lifecycle roots, registry, proof, receipt, catalog, and release writes are denied by default;
- no public map, tile, API payload, report, summary, alert, citation, evidence claim, export, or AI answer is emitted;
- migration cannot create duplicate active packages, descriptors, fixtures, tests, source-head state, or lineage;
- substantive CI runs real package and test commands instead of TODO-only echo steps.

### Negative decision matrix

| Condition | Required result |
|---|---|
| Missing or invalid descriptor | No source access; hold, quarantine, or deny. |
| Missing, draft, denied, retired, or fixture-only activation | No live source access. |
| Unknown rights or terms | No persistence or public output. |
| Unknown cultural/sensitivity review | No public output; hold or deny. |
| Unknown source surface, product, or role | Hold/quarantine; no umbrella fallback. |
| Narrative `administrative` role mapped by convenience | Fail pending accepted role crosswalk. |
| Inventory record treated as final legal designation | Fail. |
| Eligibility or recommendation treated as listed status | Fail. |
| Historical owner/occupant treated as current person or title truth | Fail. |
| Address treated as parcel, residence, or access permission | Fail. |
| Historic district boundary treated as every feature's contributing status | Fail. |
| Cultural or archaeological indicator exposed without review | Deny public output. |
| Attachment or log leaks restricted text, image, identity, or geometry | Fail. |
| Retrieval time substituted for survey, decision, or effective time | Fail. |
| Sensitive join becomes less restrictive than an input | Fail. |
| Direct lifecycle, evidence, catalog, proof, registry, or release write | Fail. |
| Current or proposed Kansas-family path declares canonical implementation without migration evidence | Fail migration review. |
| Same controlled inputs produce different candidates or reason codes | Fail determinism. |
| Green connector workflow only echoes TODO | Do not count as implementation proof. |

[Back to top](#top)

---

## Fixtures and tests

Fixtures and executable tests remain outside the source-layout authority.

### Fixture posture

Use only:

- invented shape fixtures containing no real resource, person, property, location, attachment, endpoint, credential, or source payload;
- minimized public samples after source, rights, cultural-sensitivity, privacy, and fixture review;
- redacted or generalized samples with documented transforms and no committed original;
- invalid fixtures designed to prove deterministic rejection;
- golden candidates derived only from approved fixtures.

Never commit exact protected locations, private-property details, living-person information, restricted attachments, collection-security details, credentials, private exports, or unclear-rights media.

### Test posture

The default test suite must:

- block network access rather than merely avoid using it;
- use caller-owned temporary directories;
- fail on zero discovery after tests are introduced;
- fail when mandatory negative tests are skipped;
- reject the placeholder descriptor;
- prove no lifecycle, registry, proof, receipt, catalog, release, or public side effects;
- prove role, surface, record-meaning, rights, cultural-sensitivity, privacy, geometry, time, and migration negatives;
- keep logs and snapshots safe for CI retention.

The current local test README is documentation, not executable coverage.

[Back to top](#top)

---

## Review burden

| Reviewer role | Required focus |
|---|---|
| Connector/package maintainer | Package API, imports, transport, parsing, side effects, determinism, dependencies, and migration compatibility. |
| Kansas/KHRI source steward | Product inventory, source identity, current access surfaces, cadence, corrections, and source-native fields. |
| KSHS/SHPO liaison | Institutional and surface boundaries, survey/designation semantics, stewardship, and official-source context. |
| Archaeology/cultural-review steward | Exact locations, sacred/burial/human-remains contexts, sovereignty, consultation, collection security, and redaction. |
| Settlements/historic-resources steward | Resource types, districts, surveys, built-environment semantics, and place/time interpretation. |
| People/privacy reviewer | Historical versus living-person fields, current residences, private contacts, ownership/occupancy ambiguity, and joins. |
| Rights reviewer | Terms, attribution, redistribution, retention, media, attachments, fixtures, and public derivatives. |
| Sensitivity reviewer | Public geometry, private property, cultural places, sensitive facilities, joins, logs, and fixture safety. |
| Security reviewer | Network and credential posture, retries, request logging, parsers, archives/media, dependencies, and CI artifacts. |
| Contract/schema reviewer | Accepted SourceDescriptor, candidate, receipt, and failure shapes plus role/path migration. |
| Test/validation steward | Discovery, negative cases, reason codes, no-side-effect assertions, safe fixtures, and substantive CI. |
| Migration/architecture reviewer | Winning path, imports, source IDs, consumers, deprecation, history, backlinks, and rollback. |

Exact individual owners and GitHub teams remain `UNKNOWN`; do not invent assignments.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| Prior `connectors/khri/src/README.md` blob | **CONFIRMED** | Previous layout posture and exact rollback target. | Current implementation or accepted migration. |
| `connectors/khri/pyproject.toml` | **CONFIRMED** | Distribution name and version `0.0.0`. | Buildability, dependencies, Python support, or runtime. |
| Merged `src/khri/README.md` v0.2 | **CONFIRMED DOCUMENTATION** | Bounded package files, absent probes, path/role conflicts, cultural controls, validation, and rollback. | Executable implementation, coverage, activation, or release. |
| `__init__.py`, `fetch.py`, `admit.py`, `descriptor.yaml` | **CONFIRMED** | Empty initializer, comment-only modules, and nonconforming four-field placeholder. | Fetching, parsing, admission, handoff, or authority. |
| Exact absent module/test probes | **CONFIRMED AT NAMED PATHS** | Speculative helper map and conventional tests were not present at those names. | Absence of differently named, generated, or unindexed code. |
| Parent and test READMEs | **CONFIRMED v0.1 DOCUMENTATION** | Compatibility intent and proposed boundaries. | Runtime, test coverage, or accepted migration. |
| Exact `connectors/kansas/khri/` probes | **NOT FOUND AT NAMED PATHS** | The dossier's path claim is not proven as an implemented child package lane. | Total absence of differently represented work. |
| KHRI source dossier | **CONFIRMED DRAFT DOCUMENTATION** | KSHS-operated per-surface framing, Kansas-first authority posture, product/claim context, and placement intent. | Machine descriptor, current endpoint/terms, package migration, activation, or release. |
| KSHS umbrella dossier | **CONFIRMED DOCUMENTATION** | Institutional anti-collapse and surface-specific descriptor requirement. | KHRI runtime behavior. |
| Archaeology source-registry guide | **CONFIRMED DRAFT DOCTRINE/DOCUMENTATION** | Deny-by-default exact cultural locations, cultural/steward review, role separation, and admission posture. | Implemented KHRI policy or registry instances. |
| SourceDescriptor contract/schema | **CONFIRMED REPOSITORY SURFACES; STATUS PROPOSED** | Required field surface, deprecated aliases, machine role vocabulary, rights/sensitivity gates, and activation states. | Conforming KHRI descriptor or one accepted canonical schema path. |
| Source-authority register | **CONFIRMED EMPTY** | No established machine authority entry at the inspected register. | Absence of all authority evidence elsewhere. |
| Connector/descriptor workflows | **CONFIRMED TODO-ONLY** | Workflow scaffolding. | Package import, test collection, descriptor conformance, policy enforcement, or rights review. |
| Directory Rules | **CONFIRMED PLACEMENT DOCTRINE** | Responsibility roots, lifecycle invariant, compatibility discipline, test/fixture separation, migration, and no-parallel-authority rules. | Resolution of current package and role conflicts. |

No live KHRI or KSHS endpoint, payload, current terms page, credential, runtime log, deployed service, EvidenceBundle, release manifest, or public client was inspected for this documentation update.

[Back to top](#top)

---

## ADRs and migration

This README creates no ADR and resolves no migration.

An accepted ADR or governed migration record is required before any change that:

- moves or duplicates the package;
- classifies `connectors/khri/` as legacy, mirror, deprecated, external-export, transitional, redirect-only, or retained implementation;
- changes distribution, import, source, or product IDs;
- chooses one versus multiple KHRI product adapters;
- maps narrative `administrative` source-role language to a machine enum;
- changes fixture or test routing;
- creates parallel descriptor, registry, policy, schema, receipt, proof, release, or publication homes;
- establishes a public cultural-sensitivity, privacy, or geometry default;
- retires this path or promotes it from compatibility posture.

A README may expose these conflicts. It cannot settle them by wording alone.

[Back to top](#top)

---

## Definition of done

### This documentation revision

- [x] Current source-layout and package maturity are explicit.
- [x] The stale two-README inventory is replaced by verified package files and bounded absent probes.
- [x] The merged child package v0.2 boundary is integrated without copying authority into this layout.
- [x] The dossier's Kansas-family placement intent is separated from actual package location.
- [x] Directory Rules responsibility roots and lifecycle law are preserved.
- [x] KHRI/KSHS surface and record-meaning anti-collapse controls are explicit.
- [x] Rights, cultural sensitivity, sovereignty, privacy, exact location, geometry, time, attachments, fixtures, and joins fail closed.
- [x] Inputs, outputs, failure semantics, validation, review, migration, rollback, and backlog are explicit.
- [x] No implementation, activation, or release maturity is overclaimed.

### Source-layout readiness remains open

- [ ] Accepted package path, import identity, product topology, source IDs, compatibility class, losing-path disposition, and migration plan.
- [ ] Accepted SourceDescriptor contract/schema/validator authority and conforming KHRI product descriptors.
- [ ] Reviewed authority/control-plane entries, activation decisions, and source-head evidence.
- [ ] Current access surfaces, endpoint shapes, terms, attribution, redistribution, retention, cadence, rate/size limits, correction, and withdrawal posture.
- [ ] Accepted resource, survey, evaluation, designation, place, person, parcel, attachment, and crosswalk contracts.
- [ ] Implemented cultural-sensitivity, sovereignty, privacy, geometry, attachment, and public-transform policy.
- [ ] Implemented package configuration, transport/parser/admission interfaces, finite candidate envelope, and deterministic reason codes.
- [ ] Safe reviewed fixtures and executable no-network negative tests.
- [ ] Substantive CI with non-zero collection, zero-discovery failure, and demonstrated boundary failures.
- [ ] Evidence, catalog, policy, review, release, correction, withdrawal, and rollback closure outside the package.

Documentation completeness does not imply package readiness, source admission, activation, rights clearance, cultural/sensitivity clearance, evidence closure, or publication.

[Back to top](#top)

---

## Rollback

Rollback is required if this README is used to claim accepted canonicality, completed migration, executable package behavior, live source access, activation, rights clearance, cultural/sensitivity clearance, safe exact-location exposure, lifecycle authority, evidence closure, or release readiness.

Before merge, close the draft pull request and abandon the scoped branch if the revision is rejected.

After merge, restore prior README blob:

```text
234df59446b68e0e08f4104814312e2b0f89b83e
```

through a transparent revert commit or revert pull request, then rerun applicable documentation, link, connector-boundary, policy, sensitivity, and rollback checks. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Complete recursive source-layout and consumer inventory | **UNKNOWN** | Mounted checkout or non-truncated tree/import receipt at the reviewed commit. |
| Final connector and package home | **CONFLICTED** | Accepted ADR/migration, consumer inventory, import/source-ID plan, deprecation, and rollback. |
| Compatibility class of `connectors/khri/` | **CONFLICTED / NEEDS VERIFICATION** | Accepted legacy/mirror/deprecated/external-export/transitional/retained decision. |
| Existence and role of `connectors/kansas/khri/` | **NOT ESTABLISHED AT NAMED PROBES** | Current tree evidence and accepted placement/migration record. |
| KHRI product-family topology | **NEEDS VERIFICATION** | Accepted inventory of portal/search, survey, evaluation, designation, attachment, geometry, and restricted products. |
| SourceDescriptor schema and validator authority | **CONFLICTED / PROPOSED** | One accepted contract/schema, migration, fixtures, validator, and CI command. |
| Narrative `administrative` to machine-role mapping | **CONFLICTED** | Accepted vocabulary/crosswalk and negative tests. |
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

Keep this source layout small, deterministic, no-network by default, and subordinate to evidence and policy.

The smallest safe implementation sequence is:

1. settle package path, compatibility class, product/source IDs, descriptor authority, role vocabulary, fixture home, and test routing;
2. replace the local descriptor placeholder with an accepted external reference or governed migration shim;
3. add one invented invalid KHRI-shaped fixture containing no real resource, person, property, coordinate, attachment, endpoint, credential, or source payload;
4. prove import and network denial;
5. prove one deterministic fail-closed candidate with no side effects;
6. add surface, record-meaning, rights, cultural-sensitivity, privacy, identity, time, geometry, attachment, join, and migration negatives;
7. only then consider a reviewed, opt-in source probe.

[Back to top](#top)
