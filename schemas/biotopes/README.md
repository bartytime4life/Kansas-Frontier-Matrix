<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-biotopes-readme
title: schemas/biotopes/ — Biotopes Compatibility, Vocabulary, and Object-Split Migration Index
type: readme; directory-readme; compatibility-index; vocabulary-guardrail; schema-migration-index
version: v1.1
status: draft; index-only; frozen-for-new-schemas; vocabulary-alias-unaccepted; split-migration-required; NEEDS VERIFICATION
policy_label: public
owners: OWNER_TBD — Schema steward · Habitat domain steward · Flora domain steward · Contract steward · Registry steward · Validation steward · Fixture steward · Migration steward · Docs steward
created: NEEDS VERIFICATION — blank file was replaced by v1 on 2026-07-03
updated: 2026-07-15
current_path: schemas/biotopes/README.md
proposed_machine_shape_root: schemas/contracts/v1/domains/habitat/
truth_posture: CONFIRMED target README and prior blob, schemas root responsibility, Directory Rules compatibility-class requirements, proposed ADR-0001 schema-home direction, Habitat domain and object-family doctrine, docs-only Biotopes sublane, Biotope-not-ubiquitous-language rule, Habitat land-cover and ecoregions schema indexes, LandCoverObservation semantic contract and permissive schema scaffold, Habitat fixture/test indexes, Habitat validator index, non-recursive shared schema harness, bounded shared validator runner, empty object-family register, and TODO-only Habitat workflow at the pinned snapshot / CONFLICTED target path existence versus docs prohibition on parallel schemas/biotopes authority, proposed-versus-accepted ADR language in adjacent Habitat docs, and the umbrella term Biotope versus separately owned HabitatPatch, LandCoverObservation, EcologicalSystem, Ecoregion context, and Flora Vegetation Community / UNKNOWN exhaustive recursive inventory, inbound links, hidden or generated files below schemas/biotopes, active consumers, schema registry authority, accepted object identities, accepted filenames and $id conventions, validator execution, fixture payload validity, policy enforcement, release integration, and production use / NEEDS VERIFICATION owner decision on vocabulary, drift entry, object-by-object migration manifest, contract-schema pairing, schema hardening, registry records, negative tests, CI enforcement, deprecation window, correction propagation, inbound-link retirement, and rollback proof
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: f0121b65661a4e3acbf00e0326b86744c6975ea6
  prior_blob: 3206e6ffce1cb0054e3542318e4485c5accc19a0
  prepared_under_prompt: KFM GitHub Repository Documentation Implementation Agent v3.1.0
related:
  - ../README.md
  - ../contracts/v1/domains/habitat/README.md
  - ../contracts/v1/domains/habitat/land_cover/README.md
  - ../contracts/v1/domains/habitat/ecoregions/README.md
  - ../../contracts/domains/habitat/README.md
  - ../../contracts/domains/habitat/land_cover/observation.md
  - ../../docs/domains/habitat/README.md
  - ../../docs/domains/habitat/sublanes/biotopes.md
  - ../../docs/domains/habitat/sublanes/ecological_systems.md
  - ../../docs/domains/habitat/sublanes/ecoregions.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../control_plane/object_family_register.yaml
  - ../../fixtures/domains/habitat/README.md
  - ../../tests/domains/habitat/README.md
  - ../../tools/validators/domains/habitat/README.md
  - ../../tools/validators/_common/run_all.py
  - ../../tests/schemas/test_common_contracts.py
  - ../../.github/workflows/domain-habitat.yml
tags: [kfm, schemas, biotopes, habitat, flora, compatibility-index, vocabulary-alias, object-split, schema-home, adr-0001, drift, migration, no-parallel-authority]
notes:
  - "v1.1 replaces a generic path-pointer README with a repository-grounded compatibility, vocabulary, and object-split migration guardrail."
  - "Biotope is not KFM ubiquitous language and must not become a new object family merely because the top-level compatibility path exists."
  - "No versioned Biotopes schema lane was found at the checked candidate paths; the valid destination depends on the object family being represented."
  - "This revision changes documentation only and selects, moves, renames, deletes, activates, or publishes no schema."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `schemas/biotopes/` — Biotopes Compatibility, Vocabulary, and Object-Split Migration Index

> **Purpose.** Keep the top-level Biotopes schema path frozen and inspectable while preventing an informal umbrella term from becoming a parallel object family, schema authority, or bulk migration target.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility index" src="https://img.shields.io/badge/path-compatibility__index-orange">
  <img alt="New schemas: frozen" src="https://img.shields.io/badge/new__schemas-frozen-critical">
  <img alt="Vocabulary: alias only" src="https://img.shields.io/badge/vocabulary-alias__only-blueviolet">
  <img alt="Migration: object by object" src="https://img.shields.io/badge/migration-object__by__object-success">
</p>

> [!IMPORTANT]
> `schemas/biotopes/` is **index-only and deprecated for new machine-schema definitions**. The repository's Habitat Biotopes document says `Biotope` is not KFM ubiquitous language and must not introduce a parallel schema, contract, policy, data, or object-family authority. The term is only a documentation-layer umbrella over existing, separately governed object families.

> [!WARNING]
> A bulk migration from `schemas/biotopes/` to a single `.../biotopes/` destination would preserve the wrong abstraction. A typed habitat area, a land-cover observation, an ecological-system classification, an ecoregion context polygon, and a vegetation community have different meanings, owners, schemas, evidence duties, source roles, sensitivity postures, and release controls. Migration must classify and route each artifact **object by object**.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Placement](#placement-and-authority) · [Vocabulary](#terminology-and-object-family-crosswalk) · [Routing](#responsibility-and-object-routing) · [Anti-collapse](#authority-and-anti-collapse-rules) · [Maturity](#current-schema-maturity-boundary) · [Proof](#fixtures-tests-validators-and-ci) · [Migration](#governed-object-split-migration-sequence) · [Status model](#finite-status-model) · [Template](#minimal-compatibility-note) · [Done](#definition-of-done) · [Validation](#validation) · [Rollback](#correction-deprecation-and-rollback) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis)

---

## Status and evidence boundary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| `schemas/biotopes/README.md` | **CONFIRMED** | Target exists; prior blob is pinned in metadata. |
| Other direct files under `schemas/biotopes/` | **NOT SURFACED in bounded search** | Treat the path as README-only until recursive inventory proves otherwise. |
| `schemas/` | **CONFIRMED responsibility root** | Owns machine-checkable shape, not semantic meaning, policy, fixtures, validator code, lifecycle data, or release state. |
| Directory Rules | **CONFIRMED doctrine** | `schemas/` is canonical for shape; compatibility paths must declare class and must not evolve as parallel authority. |
| ADR-0001 | **CONFIRMED document / status PROPOSED** | Proposes `schemas/contracts/v1/` and `schemas/contracts/v1/domains/<domain>/` as machine-schema homes. It is not accepted merely because adjacent docs call it accepted. |
| Habitat domain | **CONFIRMED domain segment / implementation mixed** | Habitat owns landscape objects such as patches, land cover, ecological systems, suitability, and connectivity; it does not own Fauna or Flora occurrence truth. |
| `docs/domains/habitat/sublanes/biotopes.md` | **CONFIRMED draft docs grouping** | Explicitly says `Biotope` is not KFM ubiquitous language and must not introduce a new object family or parallel schema path. |
| `schemas/contracts/v1/domains/habitat/` | **CONFIRMED present / status PROPOSED** | Proposed Habitat machine-shape lane; current inventory is partial. |
| Habitat land-cover schema lane | **CONFIRMED present / mixed scaffold** | Contains `observation.schema.json`, paired to `LandCoverObservation`; current schema is empty and permissive. |
| Habitat ecoregions schema lane | **CONFIRMED README index / no concrete schema confirmed in inspected evidence** | Candidate ecoregion schemas remain NEEDS VERIFICATION. |
| Versioned `biotopes` candidates | **ABSENT at checked paths** | `schemas/contracts/v1/biotopes/`, `schemas/contracts/v1/domains/biotopes/`, and `schemas/contracts/v1/domains/habitat/biotopes/` were not found at checked README paths. |
| Habitat fixtures | **CONFIRMED README-oriented lanes** | Ecoregions and land-cover fixture lanes are documented; payload validity and consumer coverage remain incomplete. |
| Habitat tests | **CONFIRMED README-oriented lanes** | Separate tests exist as indexes for `EcologicalSystem`, `HabitatPatch`, land cover, ecoregions, and related concerns; executable pass state remains unverified. |
| Habitat validators | **CONFIRMED parent index / child executables unverified** | Validator README says no child lanes or executable inventory were confirmed during its authoring. |
| Shared schema harness | **CONFIRMED non-recursive for domain schemas** | Enumerates selected top-level families and does not discover nested `domains/habitat/` schemas. |
| Shared validator runner | **CONFIRMED bounded list** | Runs shared source/evidence/runtime validators and no Habitat validator. |
| Habitat workflow | **CONFIRMED TODO-only** | Green workflow status would not prove Habitat or Biotopes schema enforcement. |
| Object-family register | **CONFIRMED empty scaffold** | No machine register entry currently authorizes a `Biotope` object family or its schema home. |
| Active schema registry, consumers, releases, production use | **UNKNOWN** | Documentation and path presence are not activation evidence. |

**Authority of this document:** compatibility guidance, vocabulary control, drift disclosure, and migration guardrails only. Accepted ADRs, semantic contracts, schema files, registries, validators, fixtures, tests, consumer evidence, release records, correction records, and steward decisions outrank this README.

---

## Placement and authority

### Directory Rules basis

KFM places artifacts by responsibility:

```text
contracts/                         semantic meaning
schemas/contracts/v1/              machine-checkable shape
policy/                            admissibility and obligations
fixtures/                          deterministic examples
tests/                             executable proof
tools/validators/                  validator implementation
data/                              lifecycle records, receipts, proofs, catalogs, published artifacts
release/                           release, correction, withdrawal, rollback decisions
```

Directory Rules also require a compatibility path to declare its class and prohibit two homes from evolving independently.

Current safe classification:

```text
schemas/biotopes/                  compatibility index; frozen
schemas/contracts/v1/domains/habitat/
                                   proposed Habitat machine-shape family
```

The proposed schema-home rule does **not** authorize a `biotopes/` child. The correct destination depends on the object:

```text
LandCoverObservation               schemas/contracts/v1/domains/habitat/land_cover/
EcologicalSystem                   schemas/contracts/v1/domains/habitat/ or an accepted Habitat sublane
Ecoregion* context                 schemas/contracts/v1/domains/habitat/ecoregions/
HabitatPatch                       schemas/contracts/v1/domains/habitat/
Vegetation Community              Flora-owned schema lane, not Habitat
```

### Current path class

This path is best treated as:

| Field | Value |
|---|---|
| Compatibility class | `deprecated` for new schema definitions; `index-only` while references remain |
| Write posture | README, drift notes, and migration pointers only |
| Schema posture | No new `*.schema.json` files |
| Consumer posture | No new imports, `$ref` targets, registry activations, or API bindings |
| Removal posture | Not removal-ready until recursive inventory and inbound-link checks pass |
| Migration posture | Object-by-object split; no folder-level rename |
| Review posture | Habitat, Flora where relevant, schema, contract, migration, validation, and docs review |

### Adjacent documentation conflict

Repository documentation currently carries a material status inconsistency:

- ADR-0001 itself is marked `proposed`.
- Some Habitat prose describes ADR-0001 as accepted.
- This README follows the artifact's own status and labels the schema-home direction **PROPOSED** until the ADR or an accepted successor says otherwise.

Documentation disagreement must not be resolved by silently changing schema authority.

---

## Terminology and object-family crosswalk

`Biotope` is a bounded umbrella term, not a canonical KFM object.

| External or informal use of “biotope” | KFM canonical object or concept | Owning domain | Schema routing posture |
|---|---|---|---|
| Typed habitat area or mapped habitat unit | `HabitatPatch` | Habitat | Habitat parent schema family; exact schema NEEDS VERIFICATION. |
| Land-cover class assigned to space and time | `LandCoverObservation` | Habitat | `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json`; scaffold only. |
| NatureServe, GAP, or LANDFIRE ecological classification | `EcologicalSystem` | Habitat | Habitat schema family; exact schema NEEDS VERIFICATION. |
| EPA or alternate regionalization polygon | `Ecoregion`, `EcoregionSnapshot`, or context-join concept | Habitat context / Spatial Foundation review | Proposed Habitat ecoregions sublane; concrete schema inventory NEEDS VERIFICATION. |
| Plant-community classification | `Vegetation Community` | **Flora** | Flora-owned schema/contract home; never copied into Habitat merely for convenience. |
| Regulatory critical-habitat designation | Regulatory critical-habitat object/context | Habitat with regulatory source role | Separate regulatory family; not a biotope type. |
| Habitat suitability surface | `SuitabilityModel`, `HabitatQualityScore`, `UncertaintySurface` | Habitat | Separate modeled families; not a classification alias. |
| Classifier-to-classifier mapping | Crosswalk object appropriate to the classifier family | Habitat or owning domain | Directional, lossy, versioned, and non-authoritative. |
| Public-safe generalized habitat layer | Released derivative and layer/release records | Habitat plus release/publication roots | Downstream carrier; never schema truth or source truth. |

### Vocabulary rule

Use `biotope` only when all of the following are true:

- the term is explicitly identified as an external or documentation-layer umbrella;
- the actual KFM object family is named;
- the owning domain is named;
- source role and model/observation/regulatory posture remain visible;
- the term does not appear as `object_type`, canonical schema title, registry family, graph node type, API discriminator, or release family without an accepted vocabulary decision.

Do not create:

```text
object_type: Biotope
schemas/contracts/v1/domains/habitat/biotope.schema.json
contracts/domains/habitat/Biotope.md
policy/domains/habitat/biotope.rego
data/processed/habitat/biotopes/
```

unless a reviewed decision explicitly changes KFM ubiquitous language and includes migration, compatibility, consumer, correction, and rollback plans.

---

## Responsibility and object routing

### Machine-shape routing

| Candidate material | Correct destination basis | Required proof before move |
|---|---|---|
| Land-cover observation schema | Habitat `land_cover/` schema lane | Paired contract, fielded schema, valid/invalid fixtures, validator, tests, registry record. |
| Land-cover class scheme | Habitat `land_cover/` or accepted shared vocabulary profile | Meaning and directionality separate from observations. |
| Land-cover crosswalk | Habitat `land_cover/` | Lossiness, direction, source/target versions, unmapped classes, provenance. |
| Habitat-patch schema | Habitat parent or accepted patch sublane | Patch identity, geometry, source role, sensitivity, evidence, correction. |
| Ecological-system schema | Habitat parent or accepted ecological-system sublane | Classifier identity, model-vs-observation label, native class preservation, vintage. |
| Ecoregion schema | Habitat ecoregions sublane | Framework, hierarchy level, snapshot/version, geometry, source authority, context-only role. |
| Vegetation-community schema | Flora schema lane | Flora ownership, taxonomy/community semantics, sensitivity and evidence support. |
| Cross-domain context join | `schemas/contracts/v1/cross/` or lowest common responsibility family | Ownership-preserving refs; no domain truth absorption. |
| Shared geometry/time/source profile | Accepted common/spatial/source schema family | Reuse by `$ref` or accepted profile, not copy-paste. |
| Public derivative or layer shape | Accepted map/layer/release schema family | Release, redaction/generalization, evidence, correction, rollback refs. |

### Responsibility-root routing

| Concern | Owning home | Role of `schemas/biotopes/` |
|---|---|---|
| Semantic meaning | `contracts/domains/habitat/`, Flora contract lane where applicable | Link only. |
| Machine shape | Proposed `schemas/contracts/v1/domains/habitat/` and object-appropriate children | Index selected destination after approval. |
| Habitat policy | `policy/domains/habitat/`, sensitivity policy roots | Link only; no policy prose or executable rules here. |
| Flora ownership | Flora docs/contracts/schemas/policy | Preserve ownership for Vegetation Community. |
| Fixtures | `fixtures/domains/habitat/` and Flora fixture roots where applicable | Link verified examples. |
| Tests | `tests/domains/habitat/` and Flora test roots where applicable | Link executable proof. |
| Validators | `tools/validators/domains/habitat/`, shared validators, Flora validators | Link implementation and version. |
| Schema registry | Accepted schema registry/control-plane surface | Link immutable identity, owner, state, and supersession. |
| Lifecycle data | `data/<phase>/<domain>/` | Never stored here. |
| Receipts and proofs | governed `data/receipts/` and `data/proofs/` roots | Link only. |
| Release and rollback | `release/` | Link release/correction/rollback records; never approve. |
| Migration | accepted `migrations/schema/` plus drift/register records | Link object-by-object migration and rollback. |

---

## Authority and anti-collapse rules

1. **An umbrella term is not an object family.** `Biotope` must not become schema identity by repetition.
2. **HabitatPatch is not LandCoverObservation.** Patch geometry and quality are not a classifier's observation record.
3. **LandCoverObservation is not EcologicalSystem.** Land-cover classifications and ecological-system classifications preserve native schemes and roles.
4. **Ecoregion context is not habitat occurrence truth.** Regionalization classifies places; it does not prove habitat patches, species presence, or plant communities.
5. **Vegetation Community is Flora-owned.** Habitat may cite it through governed relations but does not own or duplicate it.
6. **Modeled is not observed.** Ecological-system classifications, suitability surfaces, and derived mappings keep model labels visible.
7. **Regulatory is not ecological classification.** Critical-habitat designation remains separately labeled and reviewed.
8. **Crosswalk is not canonicalization.** Mappings between schemes are directional, lossy, versioned, and advisory unless an authority says otherwise.
9. **Schema validity is not truth.** Shape validation does not prove evidence, rights, policy, review, release, or public safety.
10. **Fixture success is not implementation proof.** Synthetic examples cannot activate sources or authorize publication.
11. **Validator success is not release approval.** Promotion remains a governed state transition.
12. **A path is not authority by existence.** The top-level compatibility path cannot override Directory Rules or object ownership.
13. **A filename is not identity.** Migration must compare `$id`, contract pairing, fields, consumers, and unique semantics.
14. **Deletion is not de-duplication.** No candidate is removed until unique content and inbound consumers are resolved.
15. **AI language is not schema evidence.** Generated prose cannot select an object family or invent a field mapping.

### Habitat-specific semantic gates

Any candidate formerly called a biotope must disclose:

| Gate | Required posture |
|---|---|
| Object family | Exactly one accepted KFM family or an explicit composite/profile decision. |
| Owning domain | Habitat, Flora, or another owner; no silent shared ownership. |
| Source role | Observed, modeled, regulatory, aggregate, administrative, candidate, synthetic, or accepted registry value. |
| Classification authority | Native source/classifier and version preserved. |
| Spatial meaning | Polygon, raster, cell, patch, regionalization, or ref explicitly distinguished. |
| Temporal meaning | Source, observed/acquisition, valid, retrieval, release, and correction times separated where material. |
| Evidence | EvidenceRef resolves to admissible support before claim-bearing use. |
| Sensitivity | Sensitive joins fail closed; public geometry is generalized/redacted/aggregated as required. |
| Rights | License, terms, attribution, redistribution, and export posture explicit. |
| Correction | Supersession and correction lineage visible. |
| Release | ReleaseManifest and governed public interface required for public use. |
| Rollback | Prior safe state and downstream invalidation path identified. |

---

## Current schema maturity boundary

### Confirmed machine-shape evidence

The inspected Habitat land-cover schema is:

- present;
- JSON Schema draft 2020-12;
- marked `PROPOSED`;
- paired to the LandCoverObservation contract;
- empty under `properties`;
- permissive under `additionalProperties: true`.

It is a placement and pairing scaffold, not a field-complete active schema.

### Ecoregions posture

The Habitat ecoregions schema lane currently documents candidate names such as:

```text
ecoregion.schema.json
ecoregion_snapshot.schema.json
ecoregion_framework.schema.json
ecoregion_level.schema.json
ecoregion_context_join.schema.json
ecoregion_crosswalk.schema.json
ecoregion_public_derivative.schema.json
```

The inspected README does not confirm concrete schema files. These names are candidates, not implementation proof.

### Biotopes posture

No accepted or versioned Biotopes schema family was confirmed at the checked paths.

Consequences:

- do not create a `Biotope` schema to fill an apparent gap;
- do not rename a Habitat object schema to `biotope`;
- do not use `schemas/biotopes/` as a staging directory for new machine shape;
- do not register the umbrella term as an active object family;
- route each requirement to the object family that actually owns its meaning.

### Schema activation packet

A Habitat or Flora schema replacing an informal biotope concept should not become active until it has:

- stable schema identity and version;
- accepted semantic contract;
- explicit owner and reviewer roles;
- finite maturity/release state;
- object-family discriminator consistent with KFM vocabulary;
- source-role requirements;
- evidence-reference rules where claims depend on evidence;
- rights and sensitivity fields or profile references where material;
- temporal semantics;
- geometry/raster and CRS semantics;
- valid and invalid fixtures;
- negative anti-collapse fixtures;
- validator implementation;
- executable tests;
- schema registry entry;
- consumer inventory;
- compatibility/deprecation policy;
- correction and rollback plan;
- release/public-interface constraints.

---

## Contract–schema pairing rules

Every migrated or newly admitted schema must answer:

1. Which semantic contract defines its meaning?
2. Is the contract name the same object family as the schema title and discriminator?
3. Does the schema encode the contract's required invariants?
4. Which fields are machine-enforced and which remain semantic obligations?
5. Does a common/shared schema already own reusable shape?
6. Does a profile preserve source-role and domain ownership?
7. Are crosswalks modeled as separate objects rather than hidden recoding?
8. Are model, observation, regulatory, and context roles distinguishable?
9. Are EvidenceRefs resolvable through governed interfaces?
10. Are rights, sensitivity, correction, release, and rollback references represented where material?
11. Are aliases explicit and time-bounded?
12. Are deprecated identifiers retained long enough for consumer migration?

### Naming and identity posture

Until accepted schema naming and `$id` rules are verified:

- prefer object-family-specific names over the umbrella `biotope`;
- do not rename solely for cosmetic consistency;
- preserve old `$id` values through explicit aliases or migrations when consumers exist;
- record canonical path, legacy path, schema digest, version, contract ref, owner, and supersession in the registry;
- make a breaking change explicit rather than silently changing the shape behind an existing `$id`.

---

## Fixtures, tests, validators, and CI

### Confirmed fixture posture

The Habitat fixture root documents separate lanes for:

- `ecoregions/`;
- land-cover observation, scheme, crosswalk, change, uncertainty, layer, model-run, and watcher examples;
- invalid and golden examples;
- Habitat × Fauna thin-slice support.

These are documentation and synthetic-example lanes. Payload completeness and validity remain NEEDS VERIFICATION.

### Confirmed test posture

The Habitat test root documents separate test lanes for:

- `EcologicalSystem`;
- `HabitatPatch`;
- land cover;
- ecoregions;
- suitability, quality, connectivity, corridors, restoration, and uncertainty;
- source descriptors and cross-domain joins.

The split itself is evidence against a single Biotope object family. Each test lane protects a different meaning and authority boundary.

### Validator posture

The Habitat validator README is an index. It states:

- no child Habitat validator README lanes were confirmed during its authoring;
- exact executables, schema homes, fixtures, policy bundles, report destinations, receipts, and CI wiring remain NEEDS VERIFICATION;
- candidate validators should preserve object-family, source-role, geoprivacy, evidence, policy, release, correction, and rollback boundaries.

### Shared schema harness limitation

The shared contract-fixture test enumerates only:

```text
evidence
runtime
common
policy
source
governance
release
```

It does not recurse through:

```text
schemas/contracts/v1/domains/habitat/
```

Therefore a passing shared schema test does not establish Habitat or Biotopes schema coverage.

### Shared validator-runner limitation

The shared `run_all.py` invokes a bounded list of shared validators and does not invoke Habitat validators. Its success cannot activate a Habitat schema.

### Habitat workflow limitation

The Habitat workflow currently echoes TODO for:

- validation;
- proof building;
- publish dry-run.

A green run proves workflow execution only, not schema validity, proof closure, or release readiness.

### Required negative cases

A mature object-family migration must include negative tests for:

| Negative case | Required result |
|---|---|
| `Biotope` used as unapproved `object_type` | Reject or route to explicit compatibility adapter. |
| Typed area routed to land-cover observation without classifier/time | Reject. |
| Land-cover observation treated as HabitatPatch | Reject. |
| EcologicalSystem treated as observed ground truth | Reject or require explicit observed evidence. |
| Ecoregion polygon treated as habitat occurrence | Reject. |
| Vegetation Community assigned to Habitat ownership | Reject. |
| Regulatory critical habitat flattened into ecological classification | Reject. |
| Crosswalk silently replaces native classification | Reject. |
| Missing source role | Reject or fail closed. |
| Missing classifier/source vintage | Reject or hold. |
| Missing EvidenceRef for claim-bearing output | `ABSTAIN` or validation failure. |
| Sensitive occurrence join without geoprivacy transform | `DENY`. |
| Missing rights posture | Hold/quarantine. |
| Schema-valid but unreleased object served publicly | `DENY`. |
| Deprecated alias used after compatibility window | Reject with stable migration reason. |
| Rollback target missing for breaking migration | Block promotion. |

### Definition of proof

A schema-family claim becomes **CONFIRMED** only when the relevant evidence is verified in the same review:

- file path and blob;
- semantic contract;
- schema fields and `$id`;
- registry record;
- valid and invalid fixtures;
- validator implementation;
- executable tests;
- current CI result;
- consumer bindings;
- policy and EvidenceRef behavior where material;
- release/correction/rollback posture;
- generated-file provenance when applicable.

README prose alone is never proof.

---

## Governed object-split migration sequence

### Phase 0 — Freeze

- Keep `schemas/biotopes/` README-only.
- Add no new schemas, aliases, imports, `$ref` targets, registry activations, or generated outputs here.
- Do not delete or rename existing material before inventory.

### Phase 1 — Recursive inventory

Inventory:

- every file under `schemas/biotopes/`;
- every occurrence of `biotope` and `biotopes` in schemas, contracts, docs, policy, fixtures, tests, validators, packages, pipelines, data, release, control-plane files, and generated artifacts;
- every `$id`, `$ref`, schema digest, registry entry, consumer, and release binding;
- every generated-file provenance record.

Classify each result as:

```text
README_ONLY
DOCS_UMBRELLA
HABITAT_PATCH
LAND_COVER_OBSERVATION
ECOLOGICAL_SYSTEM
ECOREGION_CONTEXT
FLORA_VEGETATION_COMMUNITY
REGULATORY_CONTEXT
SUITABILITY_OR_QUALITY
CROSSWALK
SHARED_PROFILE
UNKNOWN
```

### Phase 2 — Vocabulary decision

The Habitat and Flora stewards decide whether:

- `biotope` remains a docs-only umbrella;
- it is renamed to `habitat-types`;
- it is deprecated entirely;
- an external-source alias is retained in a crosswalk;
- an actual new object family is justified.

A new object family is the highest-burden option and requires explicit meaning, ownership, incompatibility analysis, migration, policy, tests, registry, release, and rollback support.

### Phase 3 — Object-family routing

For each machine artifact:

- identify one owning object family;
- identify the owning domain;
- identify the canonical contract;
- identify the proposed machine-schema path;
- identify shared profiles referenced by `$ref`;
- preserve source-native terms as aliases or source fields rather than changing KFM object identity.

### Phase 4 — Compare and preserve

Before selecting a destination:

- compare fields, required lists, enums, defaults, `$defs`, references, and additional-property posture;
- compare `$id`, title, description, contract refs, source docs, generator metadata, and versions;
- inventory unique content and comments;
- find consumers, release refs, fixtures, tests, generated artifacts, and docs links;
- record whether migration is compatible, breaking, or blocked.

No file is a safe duplicate merely because its filename looks equivalent.

### Phase 5 — Repair the trust set

For each selected object family:

- create or repair the semantic contract;
- create or harden the machine schema;
- add registry identity and owner;
- create valid, invalid, edge, and anti-collapse fixtures;
- implement validators;
- add deterministic no-network tests;
- add policy/evidence checks where material;
- define correction, supersession, and rollback behavior.

### Phase 6 — Consumer migration

Migrate consumers through explicit adapters or versioned changes:

- schemas and `$ref` targets;
- package and pipeline imports;
- API DTOs;
- validators and tests;
- fixture paths;
- schema registry entries;
- generated docs;
- release manifests and correction records;
- public-client bindings.

Do not silently redirect a `$id` to a semantically different object.

### Phase 7 — Deprecation window

Publish:

- old path and identifier;
- replacement path and identifier;
- compatibility adapter, if any;
- migration deadline;
- known behavior differences;
- correction and rollback procedures;
- removal criteria.

### Phase 8 — Retirement

Retire `schemas/biotopes/` only when:

- recursive inventory is complete;
- every artifact has disposition;
- zero active consumers require the old path;
- documentation links are migrated;
- registry state is superseded/deprecated;
- compatibility tests pass;
- release/correction references are updated;
- rollback has been exercised or credibly reviewed;
- steward approval is recorded.

Removal should be a transparent migration commit or PR, never a history rewrite.

### Stop conditions

Stop migration and preserve current state when:

- an artifact cannot be assigned to one object family;
- Habitat versus Flora ownership is unresolved;
- unique fields or semantics have no destination;
- a consumer graph is incomplete;
- a `$id` is used by unknown external consumers;
- a source-native term is being mistaken for KFM identity;
- a breaking change lacks a compatibility plan;
- fixtures or validators are absent;
- sensitive joins or rights posture are unresolved;
- correction or rollback cannot be performed.

---

## Finite status model

Use these statuses for compatibility and migration records:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | Path contains navigation and guardrails only. |
| `FROZEN` | No new schemas, consumers, or registry activations may be added. |
| `VOCABULARY_ALIAS` | Term is external/docs-only and maps to accepted KFM objects. |
| `SPLIT_REQUIRED` | Material spans multiple object families and cannot migrate as one folder. |
| `MIGRATE_OBJECT_BY_OBJECT` | Each artifact has or needs a separate disposition. |
| `TRANSITIONAL` | A specific versioned migration is active and documented. |
| `DEPRECATED` | New consumers are forbidden; old consumers are being retired. |
| `BLOCKED` | Ownership, meaning, consumer, rights, sensitivity, or rollback gap prevents change. |
| `REMOVAL_READY` | Inventory, consumer migration, tests, registry, review, and rollback criteria are satisfied. |
| `NEEDS_VERIFICATION` | Evidence is incomplete. |

Schema maturity remains separate:

| Schema status | Meaning |
|---|---|
| `STUB` | File exists but meaningful shape is absent or permissive. |
| `DRAFT_SCHEMA` | Fielded shape exists but review/proof is incomplete. |
| `PROFILE` | Schema profiles accepted shared or domain shape without duplicate authority. |
| `ACTIVE_SCHEMA` | Accepted contract, registry, fixtures, validator, tests, consumers, and review exist. |
| `SUPERSEDED` | New version replaces it with visible lineage. |
| `WITHDRAWN` | Use is blocked through governed decision. |

Do not use compatibility status as schema maturity, or schema maturity as release state.

---

## Minimal compatibility note

```markdown
# <biotopes-compatibility-record-id>

## Status
INDEX_ONLY / FROZEN / VOCABULARY_ALIAS / SPLIT_REQUIRED / MIGRATE_OBJECT_BY_OBJECT / TRANSITIONAL / DEPRECATED / BLOCKED / REMOVAL_READY / NEEDS_VERIFICATION

## Current path
<schemas/biotopes/...>

## Current schema identity
<$id, version, digest, or N/A>

## External or legacy term
<biotope label or N/A>

## KFM object family
<HabitatPatch / LandCoverObservation / EcologicalSystem / Ecoregion context / Vegetation Community / other / UNKNOWN>

## Owning domain
<habitat / flora / other / UNKNOWN>

## Proposed destination
<schemas/contracts/v1/... or NEEDS VERIFICATION>

## Paired contract
<contracts/... or NEEDS VERIFICATION>

## Registry record
<record id/path or NEEDS VERIFICATION>

## Consumers
<known imports, refs, routes, releases, generators, or UNKNOWN>

## Fixtures and tests
<paths and current results or NEEDS VERIFICATION>

## Validator and CI
<paths and current results or NEEDS VERIFICATION>

## Compatibility effect
<compatible / breaking / alias-only / split / blocked / UNKNOWN>

## Correction and rollback
<supersession, deprecation, revert, and invalidation plan>

## Evidence
<commit, blob, paths, test run, review record>

## Follow-up
<open items>
```

Compatibility records must not contain real sensitive geometry, private source material, credentials, protected occurrence data, or internal chain-of-thought.

---

## Definition of done

`schemas/biotopes/README.md` is complete as a compatibility boundary when:

- [x] The path is classified as index-only and frozen.
- [x] The top-level schema path is not described as canonical.
- [x] ADR-0001 is labeled proposed, not silently accepted.
- [x] `Biotope` is identified as non-canonical vocabulary.
- [x] Canonical KFM object families and owners are named.
- [x] Habitat and Flora ownership boundaries are explicit.
- [x] Bulk migration is prohibited.
- [x] Object-by-object routing is documented.
- [x] Current Habitat schema maturity is bounded.
- [x] Fixture, test, validator, registry, and CI gaps are explicit.
- [x] Correction, deprecation, and rollback rules are visible.
- [ ] Recursive target-path inventory is complete.
- [ ] Inbound links and consumers are inventoried.
- [ ] Vocabulary decision is reviewed by Habitat and Flora stewards.
- [ ] A drift entry or migration record is approved.
- [ ] Every artifact has an object-family disposition.
- [ ] Selected destination schemas are field-complete.
- [ ] Contracts, fixtures, validators, tests, and registries are accepted.
- [ ] Consumer migration and compatibility tests pass.
- [ ] Deprecation window is complete.
- [ ] Removal or retention decision is recorded.

This README does not satisfy the unchecked implementation items by itself.

---

## Validation

The following commands are grounded review commands. They were **not run** during this API-only Markdown update.

```bash
# Inspect the compatibility path.
find schemas/biotopes -maxdepth 8 -type f -print | sort

# Find vocabulary, path, identifier, and consumer references.
git grep -nEi '(^|[/_.:-])biotopes?([/_.:-]|$)|object_type.*biotope|\$id.*biotope' -- \
  schemas contracts docs policy fixtures tests tools packages pipelines pipeline_specs \
  control_plane data release .github 2>/dev/null

# Inspect Habitat and Flora candidate schema homes.
find schemas/contracts/v1/domains/habitat -maxdepth 8 -type f -print | sort
find schemas/contracts/v1/domains/flora -maxdepth 8 -type f -print | sort 2>/dev/null

# Validate JSON syntax only; this is not semantic or release validation.
find schemas/contracts/v1/domains/habitat -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Inspect paired contracts and proof lanes.
find contracts/domains/habitat fixtures/domains/habitat tests/domains/habitat \
  tools/validators/domains/habitat -maxdepth 8 -type f -print 2>/dev/null | sort

# Candidate no-network test commands; verify actual executable inventory first.
pytest -q tests/domains/habitat
pytest -q tests/schemas
```

Interpretation:

- `find` proves path presence only.
- `git grep` is an inventory aid, not proof of semantic equivalence.
- JSON parsing proves syntax only.
- schema validation proves shape only.
- tests prove only their asserted behavior.
- no command approves source admission, policy, release, public display, correction, or rollback by itself.

---

## Correction, deprecation, and rollback

### Documentation correction

When evidence changes:

1. update the status table;
2. cite the new commit, blob, registry, test, or release evidence;
3. preserve prior conclusions in change history or a supersession note;
4. distinguish correction from implementation;
5. do not rewrite old schema identities silently.

### Before merge

Rollback for this documentation change is:

- leave the draft pull request unmerged; or
- restore prior blob `3206e6ffce1cb0054e3542318e4485c5accc19a0` in a transparent follow-up commit.

### After merge

Use a revert commit or revert pull request for the implementation commit. Do not reset or rewrite shared history.

### Migration rollback

Every object-family migration must define:

- prior schema path and `$id`;
- prior registry state;
- prior consumer bindings;
- prior release refs;
- alias/cache/index invalidation;
- restoration steps;
- correction notice requirements;
- test proving the prior safe state can be restored;
- conditions that make rollback unsafe and require a forward correction instead.

Rollback must not recombine separately owned object families into a single Biotope authority.

### Removal rollback

If the compatibility path is removed and a missed consumer is discovered:

- restore only the minimal compatibility pointer needed;
- do not restore parallel schema authority;
- record the missed consumer;
- extend the deprecation window;
- fix inventory and tests;
- issue correction/supersession records when public or released artifacts were affected.

---

## Open verification backlog

### Placement and vocabulary

- [ ] Confirm CODEOWNERS for `schemas/biotopes/`.
- [ ] Confirm whether the path should remain index-only, become a short-lived transitional pointer, or be removed after migration.
- [ ] Confirm whether `biotope` remains docs-only, is renamed to `habitat-types`, or is fully deprecated.
- [ ] Reconcile adjacent documentation that calls ADR-0001 accepted with the ADR's current proposed status.
- [ ] Record the path and vocabulary decision in the drift register or accepted migration record.

### Inventory and identity

- [ ] Run recursive inventory below `schemas/biotopes/`.
- [ ] Find every repository reference to `biotope` and `biotopes`.
- [ ] Inventory every `$id`, `$ref`, registry record, digest, version, generator, and consumer.
- [ ] Confirm whether external consumers use any old identifier.
- [ ] Confirm whether any generated artifact can recreate the path.

### Object-family routing

- [ ] Classify every artifact as HabitatPatch, LandCoverObservation, EcologicalSystem, Ecoregion context, Flora Vegetation Community, regulatory context, suitability/quality, crosswalk, shared profile, or unknown.
- [ ] Confirm exact schema home for HabitatPatch.
- [ ] Confirm exact schema home for EcologicalSystem.
- [ ] Confirm whether ecoregion schemas belong under the existing ecoregions sublane.
- [ ] Confirm Flora-owned Vegetation Community schema and contract paths.
- [ ] Confirm whether any true composite/profile object is needed.

### Contracts and schemas

- [ ] Harden the LandCoverObservation schema beyond empty permissive shape.
- [ ] Confirm object discriminator and naming conventions.
- [ ] Confirm schema `$id` convention.
- [ ] Confirm contract-schema one-to-one pairing.
- [ ] Confirm shared profiles for identity, spatial, temporal, evidence, source, rights, sensitivity, correction, and release.
- [ ] Confirm crosswalk semantics and directionality.

### Fixtures, validators, tests, and CI

- [ ] Inventory fixture payloads, not only README lanes.
- [ ] Inventory executable Habitat test modules and current pass state.
- [ ] Implement or verify Habitat object-family validators.
- [ ] Add negative cases listed in this README.
- [ ] Add recursive domain-schema discovery or explicit Habitat schema validation.
- [ ] Replace TODO-only Habitat workflow jobs with meaningful fail-closed checks.
- [ ] Confirm CI required-check and branch-protection posture.

### Registry, consumers, and release

- [ ] Populate the object-family/schema registry with accepted identities.
- [ ] Inventory package, pipeline, API, UI, map, export, search, graph, and AI consumers.
- [ ] Inventory release manifests, correction notices, rollback cards, and published artifacts referring to old terms or paths.
- [ ] Define compatibility adapters and deprecation window.
- [ ] Define downstream cache/index/alias invalidation.
- [ ] Exercise rollback or document why only forward correction is safe.

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `schemas/biotopes/README.md` prior blob | **CONFIRMED** | Existing compatibility-path intent. | Understates current vocabulary and object-split implications. |
| Directory Rules | **CONFIRMED doctrine** | `schemas/` shape authority; compatibility class and no-parallel-authority rules. | Does not decide the Biotope vocabulary. |
| ADR-0001 | **CONFIRMED document / PROPOSED decision** | Versioned schema-home direction and domain nesting. | Not accepted at inspected snapshot. |
| Habitat domain README | **CONFIRMED draft doctrine** | Habitat ownership and object-family scope. | Contains adjacent status wording that needs reconciliation. |
| Habitat Biotopes sublane | **CONFIRMED draft docs grouping** | Biotope is not KFM ubiquitous language; no new object family or parallel schema path. | Docs-layer proposal, not machine authority. |
| Habitat Ecological Systems sublane | **CONFIRMED draft** | EcologicalSystem semantics, modeled-vs-observed rule, advisory crosswalks. | Implementation remains proposed. |
| Habitat Ecoregions sublane | **CONFIRMED draft** | Ecoregions are regionalization context, not occurrence or patch truth. | Concrete schema implementation incomplete. |
| Habitat schema root README | **CONFIRMED draft index** | Proposed Habitat machine-shape root and child lanes. | Inventory partial. |
| Habitat land-cover schema README and schema | **CONFIRMED scaffold** | Current LandCoverObservation placement and permissive schema maturity. | Does not enforce fields. |
| LandCoverObservation contract | **CONFIRMED draft semantic contract** | Meaning and anti-collapse boundary. | Paired schema remains scaffold. |
| Habitat ecoregions schema README | **CONFIRMED index** | Candidate schema names and proposed sublane. | No concrete schemas confirmed in inspected evidence. |
| Habitat fixtures README | **CONFIRMED index** | Separate fixture families for ecoregions and land-cover objects. | Payload validity not established. |
| Habitat tests README | **CONFIRMED index** | Separate object-family and ecoregion test lanes. | Executable pass state unverified. |
| Habitat validator README | **CONFIRMED index** | Fail-closed validator responsibilities. | Child executables and wiring unverified. |
| Shared schema harness | **CONFIRMED code** | Selected top-level family validation. | Does not recurse into Habitat domain schemas. |
| Shared validator runner | **CONFIRMED code** | Bounded shared validators. | No Habitat validator. |
| Habitat workflow | **CONFIRMED TODO scaffold** | Workflow presence. | Does not prove validation or release readiness. |
| Object-family register | **CONFIRMED empty scaffold** | No machine authorization of Biotope family. | Register maturity itself is incomplete. |
| Checked absent candidate paths | **CONFIRMED bounded 404 checks** | No README found at common versioned Biotopes destinations. | Does not replace recursive repository inventory. |

[Back to top](#top)
