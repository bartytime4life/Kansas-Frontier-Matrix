<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nrcs-ssurgo-readme
title: connectors/nrcs-ssurgo/ — NRCS SSURGO Sibling Compatibility and Source-Admission Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Source steward · Connector steward · NRCS steward · Soil steward · Agriculture steward · Hydrology steward · Ecology liaison · Rights reviewer · Sensitivity reviewer · Security steward · Validation steward · Migration steward · CI steward · Docs steward
created: 2026-06-19
updated: 2026-07-15
policy_label: "public-doctrine; connector-boundary; compatibility-lane; nrcs; ssurgo; static-vector; lineage-preserving; placement-conflicted; source-inactive; no-network-by-default; raw-quarantine-only; descriptor-gated; scale-aware; fixture-first; not-field-verification; no-publication; rollback-aware; no-secrets"
current_path: connectors/nrcs-ssurgo/README.md
truth_posture: CONFIRMED flat and nested README boundaries, NRCS family/source/package/test READMEs, kfm-connector-nrcs 0.0.0 metadata, empty package initializer, duplicate PROPOSED registry records, empty source-authority register, draft SSURGO source and pipeline docs, draft Soil lineage contracts, permissive empty SSURGO source-descriptor schema, TODO-only connector workflow, and bounded absence of named connector/parser/test/pipeline files / PROPOSED compatibility, parser, admission-candidate, outcome, fixture, migration, correction, and rollback contracts / CONFLICTED sibling versus nested placement, source ID and registry homes, source-authority vocabulary, and descriptor/schema placement / UNKNOWN active source, approved acquisition surface, current package profile, executable behavior, fixtures, tests, CI enforcement, schedules, receipts, deployment, consumers, and runtime health / NEEDS VERIFICATION owners, ADR or migration decision, source identity, rights, package profile, schema realization, validation, correction, deprecation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 6a6abd1cfadf181c093f21d0eb36a38f7ca3ed8b
  prior_blob: f48db39946243df233d1e68a0d4abcec77ffa34d
  nested_ssurgo_blob: 601b919cf0627b69b21be317cd5e8086502be0bd
  nrcs_family_blob: 888236f218fc0892c54c947c0c2651b34ca5137b
  nrcs_source_root_blob: 3b26759548ddaf52eb5b6de0e25dfa354e1d62ec
  nrcs_package_readme_blob: 3e022257cc553e8661b988e9e01c61cccc1fddc8
  nrcs_tests_blob: 7c65ba6ef85a8369e17c40d5e3fbc388b04a306b
  package_metadata_blob: c6bb1565db7df490bee52a597d04d694e2b9f8a4
  package_initializer_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  product_page_blob: 02955e076e2b2b621cf1229cd430b7094081b3a1
  source_catalog_blob: c6985eb052191092daaeae6303e84538b423ce7c
  soil_registry_placeholder_blob: 85fab71af52928888bc8bafb937063952a853552
  alternate_soil_registry_blob: 89da23fe70be089214de48f89ff3e56e8c6985b9
  agriculture_registry_placeholder_blob: e44bf499dd53588dd0d192a590ca97a98f7fe6e7
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  source_descriptor_schema_blob: 84ef1784e756c7b40874764e17fe6ae96fee98ac
  soil_map_unit_contract_blob: 9c062ace827754e328200080ad99f8dd2857dcac
  soil_component_contract_blob: abadd4efc4a68315bd3b32a035352d6ce23d1220
  horizon_contract_blob: b2af44430ed809d277d822865bc7c51e48881e40
  component_horizon_join_contract_blob: 0a7dd6ee4e11e1a8abe9adb84eebaa954e1880d9
  downstream_pipeline_readme_blob: eb457f55d6546219e0bc898dab85c4b76739a825
  connector_gate_workflow_blob: fc36ecced55bb0b4002d551cb28addfff0be918a
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  bounded_path_checks:
    - connectors/nrcs-ssurgo/README.md existed at v0.1
    - connectors/nrcs-ssurgo/__init__.py, client.py, and parser.py were not found
    - connectors/nrcs/ssurgo/README.md exists at v0.1
    - connectors/nrcs/src/nrcs/__init__.py is empty
    - connectors/nrcs/src/nrcs/products/ssurgo.py was not found
    - connectors/nrcs/tests/test_ssurgo.py and test_ssurgo_manifest.py were not found
    - connectors/nrcs/pyproject.toml contains only project name and version 0.0.0
    - three SSURGO registry-shaped records are PROPOSED placeholders or TBD templates
    - control_plane/source_authority_register.yaml has entries: []
    - the SSURGO source-descriptor schema has properties: {} and additionalProperties: true
    - its referenced contracts/domains/soil/ssurgo_source_descriptor.md was not found
    - pipeline_specs/soil/ssurgo_ingest.yaml and named pipeline entrypoints were not found
    - .github/workflows/connector-gate.yml contains TODO echo steps
related:
  - ../README.md
  - ../nrcs/README.md
  - ../nrcs/src/README.md
  - ../nrcs/src/nrcs/README.md
  - ../nrcs/ssurgo/README.md
  - ../nrcs/tests/README.md
  - ../nrcs/pyproject.toml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../docs/sources/catalog/nrcs.md
  - ../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../docs/sources/catalog/nrcs/soil-data-access.md
  - ../../docs/sources/catalog/nrcs/gssurgo.md
  - ../../control_plane/source_authority_register.yaml
  - ../../data/registry/sources/soil/nrcs-ssurgo.yaml
  - ../../data/registry/soil/sources/nrcs_ssurgo.yaml
  - ../../data/registry/sources/agriculture/ssurgo.yaml
  - ../../schemas/contracts/v1/domains/soil/ssurgo_source_descriptor.schema.json
  - ../../contracts/domains/soil/soil_map_unit.md
  - ../../contracts/domains/soil/soil_component.md
  - ../../contracts/domains/soil/horizon.md
  - ../../contracts/domains/soil/component_horizon_join.md
  - ../../pipelines/domains/soil/ssurgo_ingest/README.md
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../release/
  - ../../.github/workflows/connector-gate.yml
tags: [kfm, connectors, nrcs, ssurgo, soil-survey, static-vector, survey-area, package, spatial, tabular, MUKEY, COKEY, CHKEY, source-vintage, scale-aware, lineage-preserving, raw, quarantine, no-network, fixture-first, anti-collapse, migration, rollback]
notes:
  - "This revision changes only connectors/nrcs-ssurgo/README.md."
  - "Both flat and nested SSURGO paths are README boundaries; this file does not ratify, migrate, deprecate, delete, supersede, or redirect either path."
  - "No active source, executable product module, product test, pipeline spec, or real connector gate is established."
  - "A SSURGO package remains survey-area-, package-, geometry-, table-, lineage-, scale-, vintage-, and source-scoped."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NRCS SSURGO Sibling Compatibility and Source-Admission Boundary

`connectors/nrcs-ssurgo/`

> Repository-present but placement-conflicted sibling boundary for USDA NRCS Soil Survey Geographic Database source admission. Current evidence establishes a documentation lane—not a runnable connector, active source, approved acquisition surface, tested package parser, or release-ready soil-survey workflow.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![placement](https://img.shields.io/badge/placement-CONFLICTED-orange)
![source](https://img.shields.io/badge/source-NRCS__SSURGO-2e7d32)
![network](https://img.shields.io/badge/network-off__by__default-critical)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE-blue)
![field verification](https://img.shields.io/badge/field__verification-DENIED-red)

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-boundary) · [Placement](#directory-rules-and-topology) · [Invariants](#keystone-invariants) · [Input](#explicit-input-and-transport-contract) · [Identity](#package-and-source-identity) · [Lineage](#mukey-cokey-chkey-lineage) · [Scale](#scale-geometry-time-and-correction) · [Boundaries](#interpretation-and-product-boundaries) · [Admission](#source-admission-handoff) · [Tests](#testing-and-fixtures) · [Implementation](#implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Rollback](#rollback-correction-and-migration)

> [!IMPORTANT]
> **This README is not an activation or placement decision.** Path presence does not establish a canonical implementation, active SourceDescriptor, approved source surface, parser, fixtures, tests, receipts, schedules, CI enforcement, deployment, or publication readiness.

> [!CAUTION]
> **SSURGO is survey evidence, not parcel or current field truth.** A connector may preserve official source packages and lineage. It may not turn map units into parcels, components into horizons, survey interpretations into regulatory determinations, or connector success into public release.

---

<a id="purpose"></a>

## Purpose

This README defines the allowed boundary for the flat sibling lane while both of these paths exist:

```text
connectors/nrcs-ssurgo/
connectors/nrcs/ssurgo/
```

A future implementation associated with this path may exist only after governance selects it as canonical, classifies it as a compatibility adapter, or explicitly keeps it documentation-only.

Any implementation must remain:

- subordinate to the NRCS family boundary;
- descriptor-gated and source-activation-aware;
- no-network by default;
- fixture-first and deterministic;
- bounded in redirects, timeouts, retries, pagination, payload, archive members, and decompression;
- lossless about survey area, package, file, geometry, table, relationship, source-native keys, scale, vintage, and correction context;
- limited to RAW or QUARANTINE candidates;
- separate from normalization, aggregation, interpretation, evidence closure, release, public API, UI, map, and AI behavior.

It must not become a second independent NRCS implementation, a SourceDescriptor registry, a Soil pipeline, a policy engine, a release service, or a public surface.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| Flat SSURGO README | **CONFIRMED v0.1 before revision** | A sibling documentation boundary exists. |
| Flat `__init__.py`, `client.py`, `parser.py` | **NOT FOUND in bounded checks** | No local implementation is established. |
| Nested `connectors/nrcs/ssurgo/README.md` | **CONFIRMED v0.1** | A second README boundary exists. |
| Central NRCS package | **CONFIRMED `0.0.0` shell** | Package presence does not prove SSURGO support. |
| Central `products/ssurgo.py` | **NOT FOUND** | No product module is established. |
| Product-specific connector tests | **NOT FOUND** | No tested connector behavior is established. |
| Soil registry pointer | **PROPOSED placeholder** | Not an operational SourceDescriptor. |
| Alternate soil registry template | **PROPOSED/TBD** | ID exists, but role, authority, rights, cadence, and access are unresolved. |
| Agriculture registry pointer | **PROPOSED placeholder** | Domain inventory, not source authority. |
| Source-authority register | **PROPOSED and empty** | Activation is not established. |
| SSURGO source-descriptor schema | **PROPOSED permissive stub** | No declared properties; cannot enforce an operational profile. |
| Referenced source-descriptor contract | **NOT FOUND** | Semantic profile gap remains. |
| Soil object contracts | **CONFIRMED detailed drafts** | Meaning is documented; machine enforcement remains incomplete. |
| SSURGO pipeline README | **CONFIRMED draft documentation** | Downstream intent, not executable proof. |
| Pipeline spec and named entrypoints | **NOT FOUND** | Executable pipeline is not established. |
| Connector workflow | **TODO-only** | A green run cannot prove connector or receipt behavior. |

This README does not claim current endpoints, survey-area inventory, package structure, parser correctness, installation, test coverage, receipts, schedules, deployment, downstream closure, or public behavior.

[Back to top](#top)

---

<a id="authority-boundary"></a>

## Authority boundary

After placement is ratified, this lane may support source-specific discovery, bounded retrieval, package inspection, integrity checks, native-key preservation, and RAW/QUARANTINE candidate construction.

It must not own:

| Excluded responsibility | Governing home or decision |
|---|---|
| Canonical path and source ID | Accepted ADR or migration note. |
| NRCS or SSURGO doctrine | `docs/sources/catalog/nrcs.md` and `docs/sources/catalog/nrcs/ssurgo.md`. |
| Source identity, rights, cadence, and activation | Accepted SourceDescriptor and authority controls. |
| Soil object meaning | `contracts/domains/soil/`. |
| Machine shape | `schemas/contracts/v1/`. |
| Normalization, joins, or rollups | `pipelines/domains/soil/ssurgo_ingest/`. |
| Rights and sensitivity decisions | `policy/rights/`, `policy/sensitivity/`, and review. |
| Evidence closure | Governed evidence/proof processes. |
| Promotion and release | `release/` plus validation, policy, review, and receipts. |
| Public map/API/UI/AI | Released artifacts through governed interfaces. |

```text
PERMITTED
approved source -> bounded retrieval or supplied package -> integrity/identity checks -> RAW | QUARANTINE candidate

DENIED
connector -> WORK -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

<a id="directory-rules-and-topology"></a>

## Directory Rules and topology

Directory Rules place source-specific fetch and admission under `connectors/`, name `connectors/nrcs/` in the family spine, and restrict connector outputs to RAW or QUARANTINE.

Confirmed topology:

```text
connectors/
├── nrcs/
│   ├── README.md
│   ├── pyproject.toml          # 0.0.0
│   ├── src/nrcs/__init__.py    # empty
│   ├── tests/README.md
│   └── ssurgo/README.md        # nested boundary
└── nrcs-ssurgo/README.md       # this sibling boundary
```

### Freeze-by-default

Until a decision is accepted, do not create duplicate clients, parsers, descriptors, endpoint configurations, fixtures, tests, import aliases, schedules, correction state, or downstream consumers in both lanes.

An approved compatibility adapter may re-export a canonical implementation or translate a documented legacy configuration. It must not retrieve independently, use a different descriptor, transform packages differently, or emit separate lifecycle writes.

A path decision must identify the canonical path, compatibility classification, source ID, registry home, package mapping, test/fixture ownership, schedule owner, reference updates, deprecation window, validation, and rollback.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

1. A connector admits source material; it does not publish.
2. Source activation requires accepted machine-readable authority, not path presence.
3. Survey area, package, file, spatial layer, table, row, and native-key identity remain distinct.
4. MUKEY, COKEY, and CHKEY are lineage anchors, not interchangeable object identities.
5. A map unit is not a parcel, farm, ownership boundary, or current point condition.
6. A component is not a map unit; a horizon is not a component.
7. Scale, CRS, geometry scope, source vintage, and package vintage remain visible.
8. SSURGO, SDA, gSSURGO, gNATSGO, and STATSGO2 do not collapse into one product.
9. Interpretations are not regulatory, engineering, compliance, crop/yield, or hydrology determinations.
10. Corrections and replacements create lineage; they do not silently overwrite history.
11. Rights or sensitivity uncertainty routes to QUARANTINE or denial.
12. Public clients use governed interfaces and released artifacts only.

[Back to top](#top)

---

<a id="explicit-input-and-transport-contract"></a>

## Explicit input and transport contract

A future invocation must receive explicit configuration, including:

- SourceDescriptor reference and revision;
- product and acquisition profile;
- approved locator or supplied package reference;
- expected survey-area and package identity;
- allowed scheme and host;
- redirect, timeout, retry, rate, and pagination limits;
- maximum response, archive, member, file-count, and decompressed-size limits;
- integrity expectations;
- accepted package-profile version;
- RAW/QUARANTINE routing context;
- rights and sensitivity references;
- dry-run/live mode.

Importing the package must not perform network access, DNS, secret reads, filesystem writes, environment mutation, logging configuration, thread/process creation, scheduling, endpoint selection, or lifecycle writes.

Transport must reject private-network targets unless specifically approved, re-check redirects, bound every operation, validate observed content type and archive structure, avoid unsafe deserialization, redact credentials and signed URLs, and clean partial files after failure.

[Back to top](#top)

---

<a id="package-and-source-identity"></a>

## Package and source identity

Preserve, where exposed:

- source family and product;
- SourceDescriptor revision;
- acquisition profile;
- survey area symbol and name;
- state or territory context;
- package locator and publisher filename;
- package date, source vintage, retrieval time, and digest;
- file/member names, sizes, compression, and digests;
- spatial layer names, geometry types, CRS evidence, and extents;
- tabular table names, encodings, row counts, relationship metadata, and field inventories;
- source documentation references;
- correction or replacement lineage.

A deterministic candidate identity should be based on an accepted canonicalization profile over stable identity inputs, such as descriptor revision, product, survey area, package vintage, package/file digest, and parser profile. Retrieval time is provenance and normally must not create a different content identity by itself.

Do not fabricate missing identifiers, infer one survey area from another, silently substitute a WSS session or SDA query for a package, or treat identical locators with changed bytes as the same uncorrected object.

[Back to top](#top)

---

<a id="mukey-cokey-chkey-lineage"></a>

## MUKEY, COKEY, and CHKEY lineage

The connector preserves source relationships; it does not perform domain rollups.

```text
survey area
  -> package
    -> map-unit geometry/table row (MUKEY)
      -> component row (COKEY)
        -> horizon row (CHKEY)
```

Required safeguards:

- keep map-unit, component, and horizon identity separate;
- preserve source table and row context;
- retain component percentages and minor components;
- preserve relationship metadata and orphan findings;
- quarantine duplicate keys with conflicting content;
- quarantine broken parent-child relationships;
- do not turn a horizon property into a map-unit property without a downstream derivation receipt;
- do not select a dominant component as the whole map unit without an explicit reviewed method;
- do not treat ETL success as evidence or release approval.

The current SoilMapUnit contract is detailed but paired machine shape remains permissive; SoilComponent, Horizon, and ComponentHorizonJoin machine shapes are not established strongly enough to claim enforcement.

[Back to top](#top)

---

<a id="scale-geometry-time-and-correction"></a>

## Scale, geometry, time, and correction

Preserve source CRS evidence, layer extent, geometry type, geometry validity findings, source scale or intended-use metadata, and any transformations as downstream candidates—not silently altered source truth.

Do not imply parcel precision, point-level certainty, exact current field conditions, or suitability outside the source's intended scale and vintage.

Keep distinct:

- survey/source vintage;
- package date;
- retrieval time;
- processing time;
- correction time;
- valid/release time where applicable.

Changed bytes, changed package members, changed geometry, changed relationships, or changed table content at a stable locator require reviewable correction or replacement lineage. Preserve prior digests and affected survey-area scope.

[Back to top](#top)

---

<a id="interpretation-and-product-boundaries"></a>

## Interpretation and product boundaries

| Do not collapse | Required treatment |
|---|---|
| Map unit → parcel | Keep survey geometry separate from cadastral and ownership authority. |
| Survey polygon → current field condition | Require observation or field evidence. |
| Map unit → one component | Preserve component distribution and minor components. |
| Component → horizon | Preserve hierarchy and depth context. |
| Soil rating → regulatory determination | Carry source meaning and downstream policy/review. |
| Hydrologic soil group → flood truth | Hydrology and hazards require separate evidence. |
| Suitability → crop/yield or management advice | Agriculture claims require separate methods and evidence. |
| Soil property → geology/lithology truth | Keep domain authority separate. |
| SSURGO → SDA query response | Preserve query scope and receipt separately. |
| SSURGO → gSSURGO/gNATSGO raster | Preserve derivative identity and transformation lineage. |
| WSS session → canonical package | Require accepted acquisition posture and package identity. |
| Missing record → absence of soil condition | Missingness is not an all-clear or negative fact. |

NRCS source use may be primary for official SSURGO records within NRCS authority, contextual or corroborating for broader claims, and restricted when private, compliance, cultural, ecological, or insufficiently precise information is implicated. Those are authority-use classes; `authoritative_static_soil` is a support-type label. Do not merge them into one field without an accepted contract.

[Back to top](#top)

---

<a id="source-admission-handoff"></a>

## Source-admission handoff

A connector should return a candidate to a governed runner rather than directly writing later lifecycle stores.

| Candidate | Meaning |
|---|---|
| `READY_FOR_RAW` | Identity, integrity, package structure, rights references, and routing prerequisites pass. |
| `READY_FOR_QUARANTINE` | Material is preserved but ambiguity, conflict, restriction, or validation failure requires review. |
| `NO_CHANGE` | A deterministic comparison found no material package change. |
| `NO_DATA` | The approved source surface returned no usable package under expected semantics. |
| `RETRY_LATER` | A bounded transient failure may be retried. |
| `ERROR` | Deterministic connector failure requiring operator review. |

These are **PROPOSED connector-local outcomes**, not canonical policy outcomes and not release decisions.

A candidate should carry source/descriptor refs, request fingerprint, package/file inventory, digests, survey-area/vintage identity, spatial/tabular inventory, lineage findings, validation findings, rights/sensitivity refs, route, reason codes, and sanitized diagnostics.

Quarantine examples include unresolved source activation, topology or source-ID conflict, unexpected package profile, missing required member, unsafe archive, digest mismatch, unknown CRS, broken MUKEY/COKEY/CHKEY relations, ambiguous vintage, unresolved rights, sensitive private context, and any attempt to write beyond RAW/QUARANTINE.

[Back to top](#top)

---

<a id="testing-and-fixtures"></a>

## Testing and fixtures

Default tests must be no-network, no-secret, deterministic, and isolated to temporary directories.

Minimum test groups:

- import safety;
- package/build discovery;
- descriptor and activation gates;
- explicit configuration and endpoint allowlists;
- timeout, retry, redirect, rate, pagination, payload, archive, decompression, and SSRF limits;
- package/member inventory and digest checks;
- spatial-layer, CRS, geometry, and extent preservation;
- tabular table, encoding, row-count, and relationship preservation;
- MUKEY/COKEY/CHKEY uniqueness and parent-child integrity;
- component percentage, minor-component, horizon-depth, and missing-value cases;
- source vintage, replacement, correction, and replay;
- SSURGO/WSS/SDA/gSSURGO/gNATSGO product separation;
- parcel, current-condition, regulatory, engineering, crop/yield, hydrology, and public-release denial paths;
- RAW/QUARANTINE-only output enforcement;
- secret and sensitive-data redaction;
- deterministic candidate identity and outcomes.

Fixture metadata must include purpose, source or synthetic origin, retrieval/creation date, digest, rights posture, sensitivity review, minimization/redaction, expected behavior, and safety rationale.

Do not commit credentials, private landowner or producer records, access-controlled packages, sensitive cultural/ecology locations, uncontrolled full-size datasets, or unreviewed session material.

The repository currently documents expected SSURGO tests but does not establish product-specific test files. The connector workflow contains TODO echo steps, so a green run is not implementation proof.

[Back to top](#top)

---

<a id="implementation-sequence"></a>

## Implementation sequence

1. **Resolve topology and identity.** Accept the canonical path, compatibility posture, source ID, registry home, and ownership. Stop if unresolved.
2. **Repair source authority.** Replace placeholders with an accepted SourceDescriptor, semantic contract, closed schema, rights/sensitivity posture, and activation decision. Stop if not accepted.
3. **Create import-safe package shell.** Add build metadata, discovery, no-network imports, explicit config, finite errors, and tests. Stop if imports have side effects.
4. **Implement fixture-first package inventory.** Parse approved synthetic/minimized fixtures and preserve native package structure and lineage. Stop on unsupported structure.
5. **Implement admission candidates.** Add deterministic RAW/QUARANTINE candidates, reason codes, and temporary-runner tests. Stop if later lifecycle writes are possible.
6. **Add bounded live retrieval.** Allow only descriptor-approved sources with strict resource and security controls. Stop on unapproved redirect, host, format, or size.
7. **Integrate downstream carefully.** Hand admitted packages to the separate Soil pipeline without moving normalization into the connector. Stop if lineage or receipts are incomplete.
8. **Add real CI and operations.** Enforce tests, fixture metadata, security, receipts, correction, rollback, and owner escalation. Do not treat TODO-only workflows as gates.
9. **Migrate or deprecate the losing path.** Inventory consumers, test compatibility, update references, record deprecation, and prove rollback before removal.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

- [ ] Owners and review responsibilities are accepted.
- [ ] Flat versus nested placement and compatibility are decided.
- [ ] One canonical source ID and registry home are accepted.
- [ ] SourceDescriptor, semantic contract, closed schema, rights, sensitivity, cadence, and activation are accepted.
- [ ] Current acquisition and package profiles are versioned and verified.
- [ ] Build/install/import behavior is tested and side-effect-free.
- [ ] Survey-area, package, file, spatial, tabular, key, scale, vintage, and correction identity is preserved.
- [ ] MUKEY/COKEY/CHKEY lineage and orphan/conflict handling is tested.
- [ ] WSS, SDA, gSSURGO, gNATSGO, and STATSGO2 remain distinct.
- [ ] Security and resource bounds fail closed.
- [ ] Rights, private context, cultural/ecology sensitivity, and precision uncertainty fail closed.
- [ ] Only RAW or QUARANTINE candidates can be produced.
- [ ] Receipts and correction/rollback targets are durable and auditable.
- [ ] Product-specific tests and reviewed fixtures exist.
- [ ] CI runs substantive checks rather than echo-only placeholders.
- [ ] Downstream normalization remains in the Soil pipeline.
- [ ] No connector path becomes evidence, release, public API/UI, or AI authority.

[Back to top](#top)

---

<a id="verification-register"></a>

## Verification register

| ID | Question | Status |
|---|---|---|
| SSURGO-V-01 | Accepted owner set | NEEDS VERIFICATION |
| SSURGO-V-02 | Canonical flat or nested path | CONFLICTED |
| SSURGO-V-03 | Compatibility/deprecation classification | NEEDS VERIFICATION |
| SSURGO-V-04 | Canonical source ID and registry home | CONFLICTED |
| SSURGO-V-05 | Active source authority | NOT ESTABLISHED |
| SSURGO-V-06 | Rights and attribution | NEEDS VERIFICATION |
| SSURGO-V-07 | Approved acquisition profile | NEEDS VERIFICATION |
| SSURGO-V-08 | Current survey-area inventory | UNKNOWN |
| SSURGO-V-09 | Current package/member profile | UNKNOWN |
| SSURGO-V-10 | CRS, geometry, scale, and vintage semantics | NEEDS VERIFICATION |
| SSURGO-V-11 | MUKEY/COKEY/CHKEY relationship profile | NEEDS VERIFICATION |
| SSURGO-V-12 | Closed SSURGO SourceDescriptor schema | PROPOSED STUB |
| SSURGO-V-13 | Paired semantic source contract | NOT FOUND |
| SSURGO-V-14 | Canonical Python product module | NOT FOUND |
| SSURGO-V-15 | Product-specific connector tests | NOT FOUND |
| SSURGO-V-16 | Reviewed fixture inventory | UNKNOWN |
| SSURGO-V-17 | Connector candidate/outcome contract | PROPOSED |
| SSURGO-V-18 | Ingest-receipt profile | NEEDS VERIFICATION |
| SSURGO-V-19 | Pipeline declarative spec | NOT FOUND |
| SSURGO-V-20 | Pipeline executable entrypoint | NOT FOUND |
| SSURGO-V-21 | Correction invalidation and reprocessing | UNKNOWN |
| SSURGO-V-22 | Real connector CI enforcement | NOT ESTABLISHED |
| SSURGO-V-23 | Rollback automation/drill evidence | UNKNOWN |
| SSURGO-V-24 | Production schedule and runtime health | UNKNOWN |

[Back to top](#top)

---

<a id="rollback-correction-and-migration"></a>

## Rollback, correction, and migration

### Documentation rollback

Restore prior blob:

```text
connectors/nrcs-ssurgo/README.md
f48db39946243df233d1e68a0d4abcec77ffa34d
```

### Future implementation rollback

Record the code commit, package version, parser/acquisition profile, SourceDescriptor revision, run IDs, admitted digests, RAW/QUARANTINE candidates, downstream runs, receipts/proofs, correction notice, rollback decision, and reprocessing plan.

### Source correction

Do not erase the prior package. Create replacement lineage with old/new digests, survey-area and vintage scope, package/member delta, relationship impact, downstream impact, review decision, invalidation/reprocessing action, release correction if needed, and rollback target.

### Path migration

A migration must preserve prior and replacement paths, import/source-ID mapping, compatibility window, references, fixtures/tests, schedules, deprecation owner/date, removal criteria, and a tested rollback operation.

Do not deprecate either lane until canonical implementation, registry, imports, consumers, schedules, fixtures, tests, docs, correction handling, and rollback have been verified.

[Back to top](#top)

---

## Evidence ledger

| Evidence surface | Finding | Interpretation |
|---|---|---|
| Flat and nested READMEs | Both exist | Placement remains conflicted. |
| NRCS package initializer | Empty | Package shell only. |
| SSURGO module and tests | Not found | Runtime and coverage not established. |
| Three registry-shaped records | PROPOSED/TBD | No singular active source authority. |
| Source-authority register | `entries: []` | Activation not established. |
| Source-descriptor schema | Empty permissive object | Operational profile cannot be enforced. |
| Paired source contract | Not found | Semantic source-profile gap. |
| Soil lineage contracts | Detailed drafts | Meaning exists; machine enforcement is incomplete. |
| SSURGO pipeline README | Draft | Downstream boundary, not executable proof. |
| Pipeline spec/entrypoints | Not found | Pipeline implementation not established. |
| Connector workflow | TODO echo steps | No meaningful connector gate. |
| Directory Rules | NRCS family spine; RAW/QUARANTINE only | Governing placement and lifecycle boundary. |

---

## Status summary

`connectors/nrcs-ssurgo/` is currently a **README-only, placement-conflicted, source-inactive sibling boundary**.

Its permitted future role is narrow: preserve approved SSURGO packages and provenance, perform bounded source-admission checks, and prepare governed RAW or QUARANTINE candidates without collapsing survey area, package, geometry, tables, native-key lineage, scale, vintage, rights, or correction context.

It is not a runnable connector, path decision, active source descriptor, Soil pipeline, field-verification system, parcel or ownership truth, crop/yield or hydrology truth, engineering/regulatory authority, evidence closure, release approval, public map/API/UI behavior, or AI truth source.

<p align="right"><a href="#top">Back to top</a></p>
