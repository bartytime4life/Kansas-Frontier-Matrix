<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-atmosphere-hazards-readme
title: tools/validators/atmosphere_hazards/ — Atmosphere × Hazards Compatibility Bridge and One-Authority Boundary
type: readme; directory-readme; compatibility-bridge; cross-domain-validator-alias; atmosphere; hazards; non-authoritative
version: v0.2
status: draft; repository-grounded; README-only-bridge; canonical-seam-air-hazards; duplicate-implementation-denied; executable-absent; cross-schema-index-only; index-drift-confirmed; policy-greenfield; dedicated-tests-unestablished; ci-todo-only; not-for-life-safety
owners: OWNER_TBD — Atmosphere steward · Hazards steward · Validator steward · Repository architecture steward · Migration steward · Source-role steward · Freshness steward · Evidence steward · Policy steward · Security steward · Release steward · Docs steward
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1 short compatibility-bridge README
policy_label: "repository-facing; tools; validators; compatibility; alias; atmosphere; air; hazards; canonical-air-hazards; one-active-implementation; duplicate-authority-deny; migration-aware; deprecation-aware; source-role; knowledge-character; freshness; expiry; official-source; not-for-life-safety; evidence-aware; policy-aware; release-gated; correction-aware; rollback-aware; no-network-by-default; no-truth-authority; no-alert-authority; no-release-authority"
owning_root: tools/
current_path: tools/validators/atmosphere_hazards/README.md
responsibility: >
  Repository-grounded compatibility, routing, and migration boundary for the underscore spelling of the Atmosphere/Air ×
  Hazards validator seam. This directory points maintainers and consumers to tools/validators/air-hazards/, prevents a
  second executable, profile, report schema, policy surface, or release gate from forming here, records naming and index
  drift, and defines safe compatibility and rollback requirements without validating domain claims, issuing alerts, making
  policy decisions, approving release, or publishing public outputs.
truth_posture: >
  CONFIRMED target README v0.1 and prior blob; bounded search surfaced only README.md under
  tools/validators/atmosphere_hazards/; no validate_atmosphere_hazards executable or ATMOSPHERE_HAZARDS_VALIDATION /
  ATM_HAZARDS_VALIDATION producer surfaced; tools/validators/air-hazards/README.md is current v0.2 repository-grounded
  canonical-seam documentation and explicitly classifies this path as compatibility-only; the canonical lane is itself
  README-only and executable enforcement is unestablished; tools/validators/hazards/README.md and
  tools/validators/domains/hazards/README.md still describe this path as a peer overlap/context lane, creating documented
  index drift against the canonical seam and target bridge; tools/validators/domains/atmosphere/README.md lists both
  air-hazards and atmosphere_hazards depending scope; schemas/contracts/v1/cross/atmosphere_hazards/ is a placement/index
  placeholder and not schema authority; Atmosphere and Hazards policy READMEs are greenfield scaffolds; Atmosphere and
  Hazards workflows execute TODO-only echo jobs / PROPOSED one-active-implementation contract, compatibility-resolution
  record, path-consumer inventory, migration gates, no-duplicate tests, CI admission, deprecation, correction, and rollback /
  CONFLICTED canonical seam versus older peer-lane index descriptions and air/atmosphere naming across docs, contracts,
  schemas, tests, and tooling / NEEDS VERIFICATION formal ADR or steward acceptance, CODEOWNERS, consumer inventory,
  compatibility window, canonical CLI/profile/report identities, import aliases, test ownership, CI significance, and
  deprecation plan / UNKNOWN runtime imports, external consumers, operational metrics, deployments, released products, and
  current validator pass results
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: "0d0f8109486763c7b4099a7a7b8b4c9fbed7219d"
  prior_blob: 5b7ef603ccf1d330c7647a32c63e5e49a23fd672
  canonical_air_hazards_blob: 1e026e9c404a27041bd227b320932c6e6736b174
  hazards_routing_index_blob: c3b68e4750978fa3bc08f6617f3699a93f5663ad
  hazards_domain_index_blob: 20b1f0851475cfc14aacdd3248f9ff1133595296
  atmosphere_domain_index_blob: 0bdf0d021a093b61cdeca0686a936cd91c1af318
  atmosphere_smoke_lane_blob: 5b9ba27e27b9ccad77d495af6b310b4b8c02366a
  freshness_validator_blob: b2ff3fb3341f4f619b3a93fdd3a54922c5d22410
  cross_schema_placeholder_blob: ad510dad9057cbc696921dc65095b911581b6725
  atmosphere_policy_blob: d897f4f67458f9d12e0ef2b2e7146eeba935df4b
  hazards_policy_blob: 6118f23a6cd480494f92e8355cbfe61b19a0c25c
  atmosphere_workflow_blob: a3c6a21db798b02202c87f76bfba5f45c5f08c9b
  hazards_workflow_blob: ada4e42302667488316fd0ca96137c76e1d6d4f5
  validators_root_blob: e35742288404a1eeb214f8269fbacb1429c0f86a
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
  bounded_path_checks:
    - tools/validators/atmosphere_hazards/ surfaced only README.md
    - validate_atmosphere_hazards search returned no implementation
    - ATMOSPHERE_HAZARDS_VALIDATION and ATM_HAZARDS_VALIDATION searches returned no implementation
    - tools/validators/air-hazards/ is documented as the canonical seam and remains README-only
    - schemas/contracts/v1/cross/atmosphere_hazards/ is index/placement-only and non-canonical
    - policy/domains/atmosphere/ and policy/domains/hazards/ are PROPOSED greenfield scaffolds
    - domain-atmosphere and domain-hazards workflows execute TODO echo commands
related:
  - ../README.md
  - ../_common/README.md
  - ../air-hazards/README.md
  - ../hazards/README.md
  - ../freshness/README.md
  - ../evidence/README.md
  - ../citation/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../domains/atmosphere/README.md
  - ../domains/atmosphere/smoke/README.md
  - ../domains/hazards/README.md
  - ../../../docs/architecture/smoke-atmosphere-hazards.md
  - ../../../docs/domains/atmosphere/CROSS_LANE_RELATIONS.md
  - ../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../schemas/contracts/v1/cross/atmosphere_hazards/README.md
  - ../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../schemas/contracts/v1/domains/hazards/
  - ../../../contracts/domains/atmosphere/
  - ../../../contracts/domains/hazards/
  - ../../../policy/domains/atmosphere/README.md
  - ../../../policy/domains/hazards/README.md
  - ../../../data/registry/sources/atmosphere/
  - ../../../data/registry/sources/hazards/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../tests/domains/atmosphere/
  - ../../../tests/domains/hazards/
  - ../../../.github/workflows/domain-atmosphere.yml
  - ../../../.github/workflows/domain-hazards.yml
  - ../../../docs/doctrine/directory-rules.md
tags: [kfm, tools, validators, atmosphere-hazards, compatibility-bridge, air-hazards, naming, migration, deprecation, one-authority, not-for-life-safety, official-source, correction, rollback]
notes:
  - "This revision changes only tools/validators/atmosphere_hazards/README.md; a generated provenance receipt is paired separately."
  - "No validator executable, semantic contract, schema, policy rule, source descriptor, fixture, test, workflow, lifecycle object, EvidenceBundle, release record, alert, model call, or public artifact is created or modified."
  - "The bridge accepts no domain payload and contains no emergency, health, evacuation, shelter, or life-safety guidance."
  - "A future canonical-path change requires reviewed migration or ADR discipline and must preserve one active implementation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere × Hazards Compatibility Bridge and One-Authority Boundary

`tools/validators/atmosphere_hazards/`

> **One-line purpose.** Preserve the underscore spelling as a documentation-only compatibility bridge to [`tools/validators/air-hazards/`](../air-hazards/README.md), prevent duplicate validator authority, and make any future rename, alias, migration, deprecation, correction, or rollback explicit and testable.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tools" src="https://img.shields.io/badge/root-tools%2F-blue">
  <img alt="Role: compatibility bridge" src="https://img.shields.io/badge/role-compatibility__bridge-blueviolet">
  <img alt="Canonical: air hazards" src="https://img.shields.io/badge/canonical-air--hazards-success">
  <img alt="Implementation: prohibited here" src="https://img.shields.io/badge/implementation-prohibited__here-critical">
  <img alt="Life safety: never" src="https://img.shields.io/badge/life__safety-never-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-informational">
</p>

> [!IMPORTANT]
> **This directory is a bridge, not a second seam.** Current repository evidence identifies `tools/validators/air-hazards/` as the documented canonical Atmosphere/Air × Hazards validator seam. This directory must not acquire an independent executable, profile, report schema, reason-code registry, policy adapter, fixture family, CI gate, release integration, or public entrypoint while that topology remains in force.

> [!CAUTION]
> **The canonical seam is not operationally proven merely because it is canonical in documentation.** Its current v0.2 README classifies the lane as README-only with executable enforcement unestablished. This bridge cannot elevate that maturity, simulate a validator, or return `PASS` for domain claims.

> [!WARNING]
> **KFM is never an emergency-alert or life-safety authority.** This bridge accepts no smoke, AQI, PM2.5, weather, warning, advisory, watch, fire-weather, evacuation, shelter, health, or operational payload. Domain validation and official-source referral belong to the canonical seam and its owning governance surfaces after implementation is verified.

**Quick links:** [Purpose](#purpose) · [Current status](#current-status-and-evidence) · [Directory Rules](#directory-rules-and-authority) · [Topology](#naming-topology-and-index-drift) · [Bridge contract](#compatibility-bridge-contract) · [Resolution record](#proposed-compatibility-resolution-record) · [One authority](#one-active-implementation-invariant) · [Consumer matrix](#consumer-compatibility-matrix) · [Allowed content](#allowed-and-prohibited-content) · [Outcomes](#finite-outcomes-and-reason-codes) · [Security](#security-and-not-for-life-safety-boundary) · [Tests](#tests-and-no-duplicate-proof) · [CI](#ci-admission-contract) · [Migration](#migration-options-and-required-gates) · [Sequence](#smallest-sound-change-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#rollback-path) · [Ledger](#evidence-ledger) · [Changelog](#changelog)

---

<a id="purpose"></a>

## Purpose

This directory exists because the repository and project vocabulary use both **Air** and **Atmosphere** for the same bounded context and use both hyphenated and underscore naming conventions in different compatibility surfaces.

The durable question for this bridge is:

> Does every maintainer, document, tool, test, workflow, import, profile, registry, and consumer resolve the underscore spelling to one documented canonical seam without creating divergent behavior or implying that the bridge itself validated a Hazards claim?

The bridge may document and test:

- canonical-path resolution;
- compatibility and deprecation status;
- consumer inventory;
- migration state;
- version and profile identity mapping;
- report and reason-code compatibility;
- link and documentation routing;
- one-active-implementation assertions;
- correction and rollback of path decisions.

It must not:

- parse or validate Atmosphere or Hazards domain payloads;
- assign source roles or knowledge characters;
- evaluate smoke, aerosol, AQI, PM2.5, weather, warning, advisory, watch, fire, or model facts;
- resolve EvidenceRefs or create EvidenceBundles;
- evaluate policy, rights, sensitivity, freshness, expiry, or release permission;
- issue warnings, alerts, health guidance, evacuation or shelter instructions;
- approve release or publish map, API, export, Focus Mode, search, tile, screenshot, graph, embedding, or AI output.

All substantive seam validation remains documented at [`../air-hazards/README.md`](../air-hazards/README.md).

[Back to top](#top)

---

<a id="current-status-and-evidence"></a>

## Current status and evidence

| Surface | Inspected status | Safe conclusion |
|---|---|---|
| `tools/validators/atmosphere_hazards/` | **CONFIRMED README-only in bounded search** | Compatibility documentation exists; no executable or data-handling bridge surfaced. |
| `validate_atmosphere_hazards` | **NOT SURFACED** | No bridge or seam executable was found under that name. |
| `ATMOSPHERE_HAZARDS_VALIDATION` / `ATM_HAZARDS_VALIDATION` | **NOT SURFACED** | No result producer or stable outcome vocabulary was found under those names. |
| `tools/validators/air-hazards/README.md` | **CONFIRMED v0.2 canonical-seam documentation** | It explicitly identifies this path as compatibility-only and requires one active implementation. |
| Canonical seam executable | **NOT SURFACED / UNKNOWN** | The canonical README classifies itself as README-only and unimplemented. |
| `tools/validators/hazards/README.md` | **CONFIRMED older routing index** | Describes this path as an Atmosphere/Hazards overlap lane, which drifts from the bridge classification. |
| `tools/validators/domains/hazards/README.md` | **CONFIRMED older per-domain index** | Treats `air-hazards/` and `atmosphere_hazards/` as related contexts without resolving bridge/canonical status. |
| `tools/validators/domains/atmosphere/README.md` | **CONFIRMED older per-domain index** | Lists both spellings for overlapping Atmosphere/Hazards concerns. |
| Cross-schema underscore path | **CONFIRMED placement/index placeholder** | It defines no schema shape and remains non-canonical. |
| Atmosphere and Hazards policy lanes | **CONFIRMED greenfield scaffolds** | File presence does not establish policy syntax, bundle parity, tests, or runtime enforcement. |
| Atmosphere and Hazards workflows | **CONFIRMED TODO-only** | Checkout plus `echo TODO ...` does not prove validation, proof building, release dry run, or bridge integrity. |
| Consumer imports, runtime use, external references | **UNKNOWN** | A complete consumer inventory has not been verified. |
| Formal ADR/steward decision selecting the canonical spelling | **NEEDS VERIFICATION** | Current posture is documented and merged, but formal architecture acceptance was not surfaced. |

A README, route name, schema placeholder, import alias, green workflow badge, or matching directory name is not executable proof.

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

The existing directory is valid under `tools/` only as a compatibility and routing surface. Its responsibility is narrower than the canonical seam.

| Responsibility | Owning home | Bridge relationship |
|---|---|---|
| Canonical Atmosphere/Air × Hazards validation seam | `tools/validators/air-hazards/` | Destination for substantive validator design and any accepted implementation. |
| Underscore compatibility pointer | `tools/validators/atmosphere_hazards/` | This directory; documentation, migration, and deprecation only. |
| Broad Hazards validator routing | `tools/validators/hazards/` | Parent routing index; should eventually align its description of this bridge. |
| Per-domain Hazards routing | `tools/validators/domains/hazards/` | Hazards-local validators and routing. |
| Per-domain Atmosphere routing | `tools/validators/domains/atmosphere/` | Atmosphere-local validators and smoke specialization. |
| Smoke specialty | `tools/validators/domains/atmosphere/smoke/` | Owns smoke/AOD specialty validation when implemented. |
| Shared freshness | `tools/validators/freshness/` | Owns time, cadence, expiry, stale-state, supersession, and correction checks. |
| Shared evidence/citation | `tools/validators/evidence/`, `tools/validators/citation/` | Owns evidence and citation validation. |
| Domain meaning | `docs/domains/`, `contracts/domains/` | Defines Atmosphere and Hazards semantics. |
| Machine shape | accepted `schemas/contracts/v1/...` homes | The cross underscore path remains index-only. |
| Policy and obligations | `policy/` | The bridge cannot decide policy. |
| Source identity and role | `data/registry/sources/` and accepted contracts | The bridge cannot admit or classify sources. |
| Evidence, reports, proofs, receipts | accepted `data/`, `artifacts/`, and receipt roots | The bridge stores none of these by default. |
| Release, correction, withdrawal, rollback | `release/` | The bridge cannot authorize publication. |
| Public serving | governed application/runtime roots | No public client should call this directory. |

### Placement law

1. Keep the existing bridge under `tools/validators/` because it routes a validator name.
2. Do not create schemas, contracts, policies, source records, evidence, lifecycle data, reports, receipts, releases, or public code here.
3. Keep one canonical implementation, profile identity, report schema family, and reason-code registry.
4. Treat domain names and file-path spellings as compatibility metadata, not separate bounded contexts.
5. Use an ADR or reviewed migration note before changing the canonical path or introducing executable alias behavior.

[Back to top](#top)

---

<a id="naming-topology-and-index-drift"></a>

## Naming topology and index drift

### Current documented topology

```text
tools/validators/
├── air-hazards/
│   └── README.md                 # documented canonical seam; README-only today
└── atmosphere_hazards/
    └── README.md                 # this compatibility bridge
```

### Current drift

| Evidence | Description | Status |
|---|---|---|
| Canonical `air-hazards` v0.2 | Explicitly says `atmosphere_hazards/` is compatibility-only | **CONFIRMED current canonical documentation** |
| This target v0.1 | Says this directory is a bridge and denies duplicate implementation | **CONFIRMED aligned intent** |
| Broad Hazards index v0.1 | Describes this path as a weather/smoke/model overlap lane | **CONFLICTED wording** |
| Per-domain Hazards index v0.1 | Lists both paths as related validator contexts | **AMBIGUOUS / NEEDS UPDATE** |
| Per-domain Atmosphere index v0.1 | Routes hazards work among `air-hazards`, `atmosphere_hazards`, and smoke depending scope | **AMBIGUOUS / NEEDS UPDATE** |
| Cross-schema underscore path | Uses `atmosphere_hazards` spelling but is index-only | **Compatibility naming, not validator authority** |

This README records the conflict but does not edit or silently supersede the older indexes. A separate small documentation PR should align those references after steward review.

### Naming is not domain identity

`air`, `atmosphere`, `air-hazards`, and `atmosphere_hazards` may appear in compatibility paths, but naming variation must not create:

- a second Atmosphere domain;
- a second Hazards domain;
- a second seam contract;
- a second validator profile;
- a second report schema;
- a second release gate;
- divergent reason-code semantics.

[Back to top](#top)

---

<a id="compatibility-bridge-contract"></a>

## Compatibility bridge contract

The bridge has five responsibilities.

### 1. Resolve

Map the underscore spelling to the current canonical seam identity.

```text
tools/validators/atmosphere_hazards/
    -> tools/validators/air-hazards/
```

### 2. Describe

State the canonical path, compatibility state, supported window, and migration status without copying the full seam contract.

### 3. Detect drift

Identify duplicate executables, profiles, schemas, reason codes, reports, tests, workflows, or documentation claims that suggest two active authorities.

### 4. Preserve compatibility

When a formal alias is needed, preserve old consumer behavior through a thin, versioned, tested adapter that delegates to the canonical implementation without reinterpreting inputs or outputs.

### 5. Support reversal

Ensure a path rename or deprecation can be rolled back without restoring unsafe public output or losing audit lineage.

### Bridge input boundary

This directory should require no domain payload. A future structural bridge checker may inspect only repository metadata such as:

- path inventory;
- filenames and hashes;
- import declarations;
- profile IDs;
- report-schema IDs;
- workflow references;
- documentation links;
- registry aliases;
- migration and deprecation metadata.

It must reject or ignore Atmosphere/Hazards data payloads rather than processing them.

### Bridge output boundary

A future structural checker may emit only a bounded compatibility result. It must not emit an Air–Hazards domain validation result or imply that a claim is safe.

[Back to top](#top)

---

<a id="proposed-compatibility-resolution-record"></a>

## Proposed compatibility-resolution record

The following record is **PROPOSED**. It is not an implemented schema.

```json
{
  "bridge_id": "atmosphere_hazards",
  "bridge_version": "<version>",
  "canonical_path": "tools/validators/air-hazards/",
  "canonical_profile_id": "<profile-id-or-unknown>",
  "canonical_profile_digest": "<digest-or-null>",
  "status": "BRIDGE_OK|DRIFT|MIGRATION_REQUIRED|DEPRECATED|REMOVED|ERROR",
  "supported_until": "<date-or-null>",
  "consumer_inventory_digest": "<digest-or-null>",
  "findings": [
    {
      "code": "AH_BRIDGE_<FINITE_REASON_CODE>",
      "severity": "info|warning|error",
      "subject_ref": "<safe-repository-ref>",
      "message": "<bounded-message>",
      "required_actions": ["<finite-action>"]
    }
  ],
  "record_digest": "<digest>"
}
```

### Record limits

- It contains no smoke, weather, warning, advisory, hazard, infrastructure, person, land, or location payload.
- It contains no source credentials, private URLs, protected branch tokens, hidden policy thresholds, or raw workflow secrets.
- `BRIDGE_OK` means naming/topology checks passed. It does **not** mean Air–Hazards validation passed.
- The canonical profile may remain `unknown` while no executable is implemented.
- The record belongs in an accepted QA or receipt lane if adopted, not in this directory by convenience.

[Back to top](#top)

---

<a id="one-active-implementation-invariant"></a>

## One-active-implementation invariant

At every point in the migration lifecycle, the repository should have:

- one canonical implementation path;
- one stable CLI or package entrypoint;
- one validator profile identity;
- one report schema family;
- one finite outcome and reason-code registry;
- one policy-adapter contract;
- one set of canonical reusable fixtures;
- one substantive CI gate;
- one release-gate integration;
- one correction and rollback owner.

Compatibility paths may:

- point;
- document;
- delegate;
- translate a deprecated import to the canonical entrypoint without semantic change;
- emit bounded deprecation diagnostics.

Compatibility paths must not:

- fork validation logic;
- alter policy outcomes;
- reinterpret domain payloads;
- maintain independent thresholds or defaults;
- emit a competing report type;
- publish independently;
- remain silently active after the support window.

### Fail-closed duplicate rule

If both paths contain executable or trust-bearing behavior before an accepted migration:

```text
DUPLICATE_AUTHORITY_RISK -> FAIL / HOLD
```

The safer action is to stop adoption and route to architecture review, not to guess which implementation wins.

[Back to top](#top)

---

<a id="consumer-compatibility-matrix"></a>

## Consumer compatibility matrix

| Consumer surface | Current bridge behavior | Required migration evidence |
|---|---|---|
| Markdown links | Point to canonical README | Link inventory and link check |
| Documentation prose | Use canonical seam name and identify bridge explicitly | Search report and reviewed edits |
| Python/JS/Rust imports | **UNKNOWN; no alias claimed** | Complete import search and adapter tests |
| CLI commands | **UNKNOWN; no bridge CLI allowed today** | One accepted CLI identity and `--help` test |
| Validator registry | **UNKNOWN** | Registry entry with canonical path and alias status |
| Profile IDs | **UNKNOWN** | One profile ID plus compatibility mapping |
| Report schema IDs | **UNKNOWN** | One schema family and version compatibility tests |
| Reason codes | Bridge-only codes must remain distinct from seam codes | Registry and collision tests |
| Fixtures | No bridge domain fixtures | Canonical fixture ownership and no-duplicate inventory |
| Tests | Structural compatibility tests only | Dedicated no-duplicate and migration tests |
| Workflows | Should reference one canonical seam | Workflow search and substantive CI |
| Schemas/contracts | Cross underscore path stays index-only | ADR/registry/migration decision |
| Policy | No bridge policy package | Canonical policy entrypoints and parity digest |
| Runtime/Focus/API/UI | No bridge runtime surface | Governed consumer inventory |
| External repositories | **UNKNOWN** | Coordinated deprecation and communication plan |

A complete consumer inventory is required before deleting, renaming, or turning the bridge into an executable alias.

[Back to top](#top)

---

<a id="allowed-and-prohibited-content"></a>

## Allowed and prohibited content

### Allowed here

- this README;
- a reviewed migration note;
- an ADR pointer;
- a deprecation notice;
- a machine-readable alias manifest **only after** its schema and owner are accepted;
- structural tests or references proving no duplicate implementation, if the accepted test-placement convention permits them;
- safe compatibility metadata with no domain payload.

### Prohibited here while `air-hazards/` is canonical

- validator source code;
- domain parsers or transformations;
- CLI or package entrypoints;
- independent profiles or defaults;
- semantic contracts;
- canonical schemas;
- policy rules or policy bundles;
- source descriptors;
- domain fixtures;
- EvidenceBundles, proofs, reports, or receipts;
- release manifests or release gates;
- runtime routes;
- public map, API, export, search, tile, graph, screenshot, Focus Mode, embedding, or AI code;
- emergency, health, evacuation, shelter, or life-safety guidance;
- duplicate copies of canonical documentation disguised as compatibility help.

### Review trigger

Any proposed file other than README, migration/ADR pointer, or narrowly accepted alias metadata requires architecture and validator-owner review before creation.

[Back to top](#top)

---

<a id="finite-outcomes-and-reason-codes"></a>

## Finite outcomes and reason codes

### Bridge outcomes

| Outcome | Meaning | Downstream behavior |
|---|---|---|
| `BRIDGE_OK` | Repository references resolve to the documented canonical seam and no duplicate authority was found | Continue structural checks only |
| `BRIDGE_DRIFT` | Docs, registries, workflows, imports, or indexes disagree about canonical/bridge status | Hold migration and file a bounded drift item |
| `MIGRATION_REQUIRED` | A consumer still depends on the bridge or a canonical-path change is proposed | Require migration plan, owner, tests, and rollback |
| `DEPRECATED` | Bridge is inside an announced compatibility window | Warn safely; delegate only if an accepted adapter exists |
| `REMOVED` | Bridge support ended and references must fail explicitly | Reject stale references with migration guidance |
| `ABSTAIN` | Consumer inventory or path authority is insufficient to decide | Do not modify topology |
| `ERROR` | Structural checker failed safely | Fail closed and preserve bounded diagnostics |

### Reason-code families

| Family | Example codes |
|---|---|
| Canonical path | `AH_BRIDGE_CANONICAL_PATH_MISSING`, `AH_BRIDGE_CANONICAL_PATH_AMBIGUOUS` |
| Duplicate authority | `AH_BRIDGE_DUPLICATE_EXECUTABLE`, `AH_BRIDGE_DUPLICATE_PROFILE`, `AH_BRIDGE_DUPLICATE_REPORT_SCHEMA`, `AH_BRIDGE_DUPLICATE_POLICY_ADAPTER` |
| Documentation drift | `AH_BRIDGE_INDEX_DRIFT`, `AH_BRIDGE_LINK_DRIFT`, `AH_BRIDGE_DOC_AUTHORITY_CONFLICT` |
| Consumer migration | `AH_BRIDGE_CONSUMER_UNKNOWN`, `AH_BRIDGE_IMPORT_STILL_ACTIVE`, `AH_BRIDGE_WORKFLOW_STILL_ACTIVE`, `AH_BRIDGE_REGISTRY_STILL_ACTIVE` |
| Version compatibility | `AH_BRIDGE_PROFILE_MAPPING_MISSING`, `AH_BRIDGE_REPORT_MAPPING_MISSING`, `AH_BRIDGE_REASON_CODE_COLLISION` |
| Deprecation | `AH_BRIDGE_DEPRECATION_DATE_MISSING`, `AH_BRIDGE_SUPPORT_WINDOW_EXPIRED`, `AH_BRIDGE_REMOVAL_UNANNOUNCED` |
| Security | `AH_BRIDGE_DOMAIN_PAYLOAD_REJECTED`, `AH_BRIDGE_SECRET_REFERENCE_BLOCKED`, `AH_BRIDGE_UNTRUSTED_INSTRUCTION_IGNORED` |
| Rollback | `AH_BRIDGE_ROLLBACK_PLAN_MISSING`, `AH_BRIDGE_PREVIOUS_PATH_UNRESTORABLE` |
| Operational | `AH_BRIDGE_CONFIG_ERROR`, `AH_BRIDGE_UNEXPECTED_ERROR` |

These codes are bridge-local. They must not be confused with domain-validation outcomes from the canonical seam.

[Back to top](#top)

---

<a id="security-and-not-for-life-safety-boundary"></a>

## Security and not-for-life-safety boundary

### No domain payload

A bridge checker must reject input that contains or attempts to route:

- raw Atmosphere or Hazards records;
- current warnings, watches, advisories, or emergency instructions;
- smoke, plume, AOD, PM2.5, AQI, weather, fire, flood, heat, cold, or event payloads;
- precise sensitive locations;
- critical-infrastructure detail;
- living-person or private-land detail;
- source credentials or restricted-source fields.

### No authority amplification

The bridge cannot make a canonical README operational, turn a TODO workflow into a gate, or convert a compatibility path into policy or release authority.

### Untrusted content

Repository files, issue text, workflow logs, source metadata, generated text, and external documentation are evidence inputs. They cannot instruct the bridge to:

- expose secrets;
- disable checks;
- select themselves as canonical;
- create an executable;
- approve a release;
- issue public guidance;
- ignore the user task or governing contract.

### Default structural-check posture

- read-only;
- no secrets;
- no network;
- no production services;
- no model calls;
- bounded repository metadata only;
- stable sorting and hashing;
- safe diagnostics;
- fail closed on ambiguity.

[Back to top](#top)

---

<a id="tests-and-no-duplicate-proof"></a>

## Tests and no-duplicate proof

No dedicated bridge test lane surfaced. The following is a **PROPOSED** structural test contract.

### Required test cases

```text
tests/validators/atmosphere_hazards_bridge/
├── README.md
├── test_bridge_topology.py
├── test_consumer_inventory.py
├── test_no_duplicate_authority.py
├── test_deprecation_contract.py
├── test_migration_rollback.py
└── fixtures/
    ├── canonical_readme_present/
    ├── canonical_readme_missing/
    ├── duplicate_executable_denied/
    ├── duplicate_profile_denied/
    ├── duplicate_report_schema_denied/
    ├── stale_documentation_link/
    ├── stale_workflow_reference/
    ├── active_import_requires_migration/
    ├── reason_code_collision/
    ├── expired_compatibility_window/
    ├── unknown_consumer_abstain/
    ├── domain_payload_rejected/
    └── rollback_plan_missing/
```

### Structural assertions

- Direct bridge inventory contains only accepted compatibility files.
- Canonical path exists and its README identifies one seam.
- No executable files or package metadata exist in both paths.
- No registry marks both paths active.
- No workflow invokes both paths as separate validators.
- No report schema or profile identity is duplicated.
- Bridge reason codes do not collide with seam validation codes.
- All compatibility links resolve.
- Removal is blocked while consumers remain unknown or active.
- Tests use synthetic repository metadata and no domain payload.
- Repeated runs produce stable results.

### Proposed command pattern

```bash
pytest -q tests/validators/atmosphere_hazards_bridge
```

This command is a future interface, not proof that the path or tests currently exist.

[Back to top](#top)

---

<a id="ci-admission-contract"></a>

## CI admission contract

### Current workflow evidence

The inspected Atmosphere and Hazards workflows run checkout and TODO echo commands. They do not enforce bridge topology, detect duplicate authority, validate links, inventory consumers, or prove migration safety.

### Proposed bridge gates

1. README and internal-link validation.
2. Direct bridge inventory allowlist.
3. Canonical path presence.
4. No duplicate executable/package/CLI check.
5. One profile and report-schema identity check.
6. Registry and workflow reference scan.
7. Documentation/index drift scan.
8. Reason-code collision check.
9. Consumer inventory completeness check before deprecation/removal.
10. Migration and rollback-plan validation.
11. No-network and no-domain-payload enforcement.
12. Generated-receipt validation for AI-authored compatibility documentation.

### CI must fail or hold when

- both paths contain executable logic;
- both paths are registered as active;
- older indexes describe peer authority without an accepted exception;
- the canonical path disappears without migration metadata;
- a bridge import changes input/output semantics;
- a compatibility window expires while active consumers remain;
- domain payload or life-safety content enters bridge fixtures or diagnostics;
- TODO-only jobs are represented as substantive enforcement.

CI success proves structural consistency for the checked commit. It does not validate an Atmosphere/Hazards claim or authorize public output.

[Back to top](#top)

---

<a id="migration-options-and-required-gates"></a>

## Migration options and required gates

### Option A — retain current topology

```text
air-hazards/        = canonical seam
atmosphere_hazards/ = README-only bridge
```

Required actions:

- align parent indexes and documentation;
- inventory consumers;
- add no-duplicate structural tests;
- keep implementation, profiles, reports, policy adapters, and CI under the canonical seam;
- define whether the bridge is permanent or time-bounded.

### Option B — rename canonical seam to underscore spelling

Required actions:

1. accept an ADR or reviewed migration note;
2. identify every consumer;
3. move implementation, tests, profiles, registries, workflows, docs, and receipts atomically;
4. leave a compatibility pointer at `air-hazards/`;
5. preserve profile and report compatibility or publish a versioned breaking change;
6. run no-duplicate and rollback tests;
7. announce and monitor the support window.

### Option C — move the seam under a shared cross-domain tree

Required actions:

- justify the responsibility root and directory;
- preserve Atmosphere, Hazards, smoke-specialty, freshness, evidence, policy, and release boundaries;
- supply adapters for both existing paths;
- avoid creating a third active implementation;
- update Directory Rules or ADR evidence where required;
- provide full rollback.

### Required gates for every option

- named owner;
- CODEOWNERS;
- consumer inventory;
- compatibility matrix;
- security review;
- test plan;
- CI plan;
- deprecation schedule;
- correction path;
- rollback plan;
- human review receipt.

[Back to top](#top)

---

<a id="smallest-sound-change-sequence"></a>

## Smallest sound change sequence

1. **Merge this bridge clarification.** Preserve current behavior; create no executable.
2. **Align routing indexes.** Update broad Hazards, per-domain Hazards, and per-domain Atmosphere descriptions in a separate reviewed PR.
3. **Inventory consumers.** Search imports, CLIs, registries, workflows, docs, tests, packages, releases, and external dependencies.
4. **Choose formal topology.** Record steward approval, ADR, or migration note.
5. **Define compatibility metadata.** Canonical profile ID, alias mapping, report mapping, reason-code separation, and support window.
6. **Add structural tests.** Prove no duplicate implementation and no domain payload.
7. **Wire least-privilege CI.** Make topology drift detectable without publishing or using secrets.
8. **Implement the canonical seam only after prerequisites close.** Keep the bridge thin.
9. **Run dry migration.** Observe references and failures without deleting the bridge.
10. **Deprecate or retain explicitly.** Announce status and preserve rollback.

Each step is independently reversible and must not weaken the not-for-life-safety or trust-membrane boundaries.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This bridge may be described as mature only when all applicable items are verified.

### Authority and topology

- [ ] One canonical seam path is formally accepted.
- [ ] One active implementation path is verified.
- [ ] Owners and CODEOWNERS are assigned.
- [ ] Parent indexes consistently describe this path as bridge or canonical according to the decision.
- [ ] Cross-schema compatibility paths remain non-authoritative or are migrated through an accepted decision.

### Compatibility

- [ ] Complete consumer inventory exists.
- [ ] Canonical CLI, package, profile, report schema, and reason-code identities are documented.
- [ ] Alias behavior, if any, is a thin semantic-preserving delegation.
- [ ] Support window and deprecation state are explicit.
- [ ] External consumers have a communication and migration path.

### Proof

- [ ] Direct bridge inventory allowlist is tested.
- [ ] Duplicate executable/profile/report/policy/registry behavior is blocked.
- [ ] Documentation and workflow drift is detected.
- [ ] No-domain-payload and no-network behavior is enforced.
- [ ] CI runs substantive structural checks.
- [ ] Current structural test results are recorded with commit and profile digests.

### Governance and operations

- [ ] Migration or ADR is reviewed.
- [ ] Security and not-for-life-safety review is complete.
- [ ] Correction and rollback paths are tested.
- [ ] Bridge removal cannot occur while active consumers are unknown.
- [ ] Human review is recorded.

Until then, classify this directory as **README-only compatibility bridge / duplicate implementation denied**.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Verification item | Status | Required evidence |
|---|---|---|---|
| AH-BRIDGE-01 | Formal canonical-path decision | **NEEDS VERIFICATION** | ADR, migration note, or steward approval |
| AH-BRIDGE-02 | Named owners and CODEOWNERS | **NEEDS VERIFICATION** | CODEOWNERS and steward registry |
| AH-BRIDGE-03 | Complete direct bridge inventory | **NEEDS VERIFICATION** | Repository tree including generated/ignored paths |
| AH-BRIDGE-04 | Complete canonical seam inventory | **NEEDS VERIFICATION** | Repository tree and package/CLI registry |
| AH-BRIDGE-05 | Runtime or package imports using underscore spelling | **UNKNOWN** | Complete import and dependency search |
| AH-BRIDGE-06 | Workflow references using underscore spelling | **NEEDS VERIFICATION** | Workflow search and run evidence |
| AH-BRIDGE-07 | Validator registry aliases | **UNKNOWN** | Registry/config inventory |
| AH-BRIDGE-08 | Canonical profile identity and digest | **UNKNOWN** | Accepted implementation/profile |
| AH-BRIDGE-09 | Canonical report schema family | **UNKNOWN** | Contract/schema/registry |
| AH-BRIDGE-10 | Bridge versus seam reason-code separation | **NEEDS VERIFICATION** | Reason-code registry and tests |
| AH-BRIDGE-11 | Parent Hazards index alignment | **NEEDS VERIFICATION** | Reviewed README update |
| AH-BRIDGE-12 | Per-domain Hazards index alignment | **NEEDS VERIFICATION** | Reviewed README update |
| AH-BRIDGE-13 | Per-domain Atmosphere index alignment | **NEEDS VERIFICATION** | Reviewed README update |
| AH-BRIDGE-14 | Cross-schema underscore path disposition | **NEEDS VERIFICATION** | ADR/registry/migration note |
| AH-BRIDGE-15 | Documentation backlink inventory | **NEEDS VERIFICATION** | Link/search report |
| AH-BRIDGE-16 | Tests and fixtures for bridge topology | **NEEDS VERIFICATION** | Collected offline tests |
| AH-BRIDGE-17 | Substantive CI and required-check significance | **NEEDS VERIFICATION** | Workflow and branch-protection evidence |
| AH-BRIDGE-18 | Compatibility support window | **NEEDS VERIFICATION** | Deprecation policy |
| AH-BRIDGE-19 | External consumer inventory | **UNKNOWN** | Coordinated dependency review |
| AH-BRIDGE-20 | Migration communication owner | **NEEDS VERIFICATION** | Owner and communication plan |
| AH-BRIDGE-21 | Correction process for wrong canonical references | **NEEDS VERIFICATION** | Runbook and test |
| AH-BRIDGE-22 | Rollback from each migration option | **NEEDS VERIFICATION** | Rehearsed rollback evidence |
| AH-BRIDGE-23 | Runtime use of canonical seam | **UNKNOWN** | Code, logs, configs, dashboards |
| AH-BRIDGE-24 | Current seam pass/fail results | **UNKNOWN** | Executable implementation and pinned runs |
| AH-BRIDGE-25 | Human review and separation of duties | **NEEDS VERIFICATION** | Review records |

Open items do not grant permission to create an implementation here. Ambiguity preserves the bridge and blocks structural migration.

[Back to top](#top)

---

<a id="rollback-path"></a>

## Rollback path

### Documentation-only rollback

Before merge:

- close the draft PR;
- abandon the branch;
- leave `main` unchanged.

After merge:

- revert the README commit through a reviewed branch;
- restore prior README blob `5b7ef603ccf1d330c7647a32c63e5e49a23fd672` if full restoration is required;
- revert or supersede the paired generated receipt according to receipt-retention policy;
- preserve the revert and supersession trail.

No runtime, policy, source, evidence, lifecycle, release, deployment, or public-output rollback is required for this README-only revision.

### Future topology rollback

Every future migration must record:

- prior canonical path;
- prior CLI/package/profile/report identities;
- prior registry and workflow references;
- consumer inventory;
- compatibility support state;
- file and commit rollback targets;
- cache and artifact invalidation;
- correction notice for misleading documentation;
- proof that only one implementation is active after rollback.

Rollback must not restore unsafe public behavior or duplicate authority merely to preserve an old path.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Blob | Session conclusion |
|---|---|---|
| Target v0.1 bridge README | `5b7ef603ccf1d330c7647a32c63e5e49a23fd672` | Bridge intent and duplicate-implementation denial confirmed |
| Canonical Air–Hazards v0.2 README | `1e026e9c404a27041bd227b320932c6e6736b174` | Current canonical-seam documentation, one-active-implementation rule, README-only maturity |
| Broad Hazards routing index | `c3b68e4750978fa3bc08f6617f3699a93f5663ad` | Older peer-lane wording creates index drift |
| Per-domain Hazards index | `20b1f0851475cfc14aacdd3248f9ff1133595296` | Older ambiguous relationship and stale broad-index absence claim |
| Per-domain Atmosphere index | `0bdf0d021a093b61cdeca0686a936cd91c1af318` | Both spellings appear in routing guidance |
| Atmosphere smoke specialty | `5b9ba27e27b9ccad77d495af6b310b4b8c02366a` | Smoke specialization belongs outside the bridge |
| Shared freshness lane | `b2ff3fb3341f4f619b3a93fdd3a54922c5d22410` | Time/expiry/correction logic belongs outside the bridge |
| Cross-schema underscore placeholder | `ad510dad9057cbc696921dc65095b911581b6725` | Index/placement only; no schema authority |
| Atmosphere policy README | `d897f4f67458f9d12e0ef2b2e7146eeba935df4b` | Greenfield scaffold |
| Hazards policy README | `6118f23a6cd480494f92e8355cbfe61b19a0c25c` | Greenfield scaffold |
| Atmosphere workflow | `a3c6a21db798b02202c87f76bfba5f45c5f08c9b` | TODO-only jobs |
| Hazards workflow | `ada4e42302667488316fd0ca96137c76e1d6d4f5` | TODO-only jobs |
| Validator root README | `e35742288404a1eeb214f8269fbacb1429c0f86a` | Validators are checkers, not authority |
| Directory Rules | `2affb080e6f0043867c64c7f06c1ca52030fbd55` | Responsibility-root and parallel-home discipline |
| Generated receipt schema | `fba21ed27ebccf1362fe397fe0c3ebd85e072685` | Provenance contract for this AI-authored update |
| Runtime imports, external consumers, operational metrics | — | **UNKNOWN** |

No external research was required. This update is grounded in repository and project evidence.

[Back to top](#top)

---

<a id="changelog"></a>

## Changelog

### v0.2 — 2026-07-16

- grounded the bridge in current repository evidence;
- preserved `air-hazards/` as the documented canonical seam and this path as compatibility-only;
- recorded conflicting older index descriptions without silently resolving them;
- classified both bridge and canonical seam implementation maturity honestly;
- added Directory Rules placement, bridge input/output limits, one-active-implementation invariant, consumer matrix, finite outcomes, safe reason codes, security boundaries, structural tests, CI admission, migration options, definition of done, open verification, and rollback;
- kept the cross-schema underscore path index-only;
- added no executable behavior or domain payload.

### v0.1 — 2026-07-07

- replaced an empty file with a short compatibility bridge pointing to `air-hazards/`.

[Back to top](#top)
