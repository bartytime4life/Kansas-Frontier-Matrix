<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-atmosphere-readme
title: schemas/atmosphere/ — Atmosphere Schema Compatibility, Drift, and Migration Index
type: readme; directory-readme; compatibility-index; schema-drift-guardrail; migration-index
version: v1.1
status: draft; index-only; deprecated-for-new-schemas; target-conflicted; mixed-scaffold; NEEDS VERIFICATION
policy_label: public
owners: OWNER_TBD — Schema steward · Atmosphere domain steward · Contract steward · Registry steward · Validation steward · Fixture steward · Migration steward · Docs steward
created: NEEDS VERIFICATION — blank file was replaced by v1 on 2026-07-03
updated: 2026-07-15
current_path: schemas/atmosphere/README.md
proposed_canonical_target: schemas/contracts/v1/domains/atmosphere/
truth_posture: CONFIRMED target README and prior blob, schemas root responsibility, proposed ADR-0001 schema-home rule, Atmosphere domain placement doctrine, current Atmosphere/Air compatibility paths, actual AirStation schema scaffold under schemas/contracts/v1/air, extensive filename/casing/slug duplication in schemas/contracts/v1/domains/atmosphere, representative permissive schema scaffolds, Atmosphere semantic-contract lane, placeholder Atmosphere validator, absent checked validators named by schema metadata, README-oriented fixture and test lanes, non-recursive common schema harness, bounded shared validator runner, and TODO-only Atmosphere workflow at the pinned snapshot / CONFLICTED path and object identity across schemas/atmosphere, schemas/contracts/v1/atmosphere, schemas/contracts/v1/air, schemas/contracts/v1/domains/air, and schemas/contracts/v1/domains/atmosphere; PascalCase, snake_case, and kebab-case filenames; schema $id namespaces; contract_doc paths; and Atmosphere versus Air ownership / UNKNOWN exhaustive recursive inventory, semantic equivalence, consumers, authoritative registry, accepted filename and $id conventions, validator coverage, fixture payload coverage, CI enforcement, release integration, and production use / NEEDS VERIFICATION owners, ADR acceptance, drift record, migration manifest, de-duplication, contract-schema pairing, schema hardening, registry state, tests, deprecation window, correction propagation, and rollback plan
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 6c71c48e88b34d76d00b43ab39d0a3a1b99328c7
  prior_blob: 6203c2f9ea1fc7209d794527ffb98b3cea1fec6f
  prepared_under_prompt: KFM GitHub Repository Documentation Implementation Agent v3.1.0
related:
  - ../README.md
  - ../contracts/v1/atmosphere/README.md
  - ../contracts/v1/air/README.md
  - ../contracts/v1/domains/air/README.md
  - ../contracts/v1/domains/atmosphere/README.md
  - ../../contracts/domains/atmosphere/README.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../fixtures/domains/atmosphere/README.md
  - ../../tests/domains/atmosphere/README.md
  - ../../tools/validators/domains/atmosphere/validate_atmosphere_decision_envelope.py
  - ../../tools/validators/_common/run_all.py
  - ../../.github/workflows/domain-atmosphere.yml
  - ../../.github/workflows/schema-validation.yml
tags: [kfm, schemas, atmosphere, air, compatibility-index, schema-home, adr-0001, drift, migration, duplicate-schema, filename-collision, id-namespace, no-parallel-authority]
notes:
  - "v1.1 replaces a path-pointer README with a repository-grounded compatibility and migration guardrail."
  - "Bounded search surfaced only this README directly under schemas/atmosphere; new machine schemas are frozen here."
  - "The proposed canonical target exists but is not a clean single authority: duplicate object families, alternate filename forms, alternate Air/Atmosphere lanes, and mixed $id and contract_doc conventions are present."
  - "This revision changes documentation only and selects, moves, renames, deletes, activates, or publishes no schema."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `schemas/atmosphere/` — Atmosphere Schema Compatibility, Drift, and Migration Index

> **Purpose.** Keep the top-level Atmosphere schema path frozen and inspectable while routing machine-checkable shape toward `schemas/contracts/v1/domains/atmosphere/` and exposing the path, filename, `$id`, contract-pairing, fixture, validator, and CI conflicts that must be resolved before migration.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility index" src="https://img.shields.io/badge/path-compatibility__index-orange">
  <img alt="New schemas: frozen" src="https://img.shields.io/badge/new__schemas-frozen-critical">
  <img alt="Target: domains atmosphere" src="https://img.shields.io/badge/target-domains%2Fatmosphere-blueviolet">
  <img alt="Target maturity: conflicted" src="https://img.shields.io/badge/target-conflicted-red">
</p>

> [!IMPORTANT]
> `schemas/atmosphere/` is **index-only and deprecated for new schema definitions**. ADR-0001 is still `proposed`, but it states the current schema-home direction: machine schemas belong under `schemas/contracts/v1/`, with domain schemas under `schemas/contracts/v1/domains/<domain>/`. This README does not accept that ADR or execute a migration; it applies the safest no-parallel-authority posture while the decision and repository drift remain unresolved.

> [!WARNING]
> The proposed target is **not yet a clean canonical family**. Repository evidence shows schemas in both Atmosphere and Air paths, duplicate object families under PascalCase, snake_case, and kebab-case filenames, inconsistent `$id` forms, mixed `contract_doc` paths, permissive scaffolds, missing or placeholder validators, documentation-led fixtures/tests, and TODO-only Atmosphere CI. Do not select a winner by filename, delete “duplicates,” or add consumers until an inventory-backed migration preserves unique content and proves compatibility.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Placement](#placement-and-authority) · [Routing](#responsibility-routing) · [Drift](#confirmed-path-and-identity-drift) · [Collisions](#confirmed-filename-and-object-family-collisions) · [Maturity](#schema-maturity-boundary) · [Pairing](#contract-schema-pairing) · [Identity](#schema-identity-and-registry-posture) · [Proof](#fixtures-tests-validators-and-ci) · [Migration](#governed-migration-sequence) · [Status model](#finite-status-model) · [Template](#minimal-compatibility-note) · [Done](#definition-of-done) · [Validation](#validation) · [Rollback](#correction-and-rollback) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis)

---

## Status and evidence boundary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| `schemas/atmosphere/README.md` | **CONFIRMED** | Target exists; prior blob is pinned in metadata. |
| Other direct files under `schemas/atmosphere/` | **NOT SURFACED in bounded search** | Treat this path as README-only until recursive inventory proves otherwise. |
| `schemas/` | **CONFIRMED responsibility root** | Owns machine-checkable shape, not meaning, policy, fixtures, validator code, data, or release state. |
| ADR-0001 | **CONFIRMED document / PROPOSED decision** | Proposes the versioned schema home and prohibits permanent topic subtrees such as `schemas/<topic>/`. |
| `schemas/contracts/v1/domains/atmosphere/` | **CONFIRMED present / CONFLICTED / mixed scaffold** | Proposed target exists, but naming, identity, pairing, and maturity drift prevent clean authority claims. |
| `schemas/contracts/v1/atmosphere/README.md` | **CONFIRMED compatibility index** | Short Atmosphere alias exists; bounded search did not establish schemas there. |
| `schemas/contracts/v1/air/` | **CONFIRMED conflicting alias lane** | Its README says compatibility, but `AirStation.schema.json` exists there as a PROPOSED scaffold. |
| `schemas/contracts/v1/domains/air/README.md` | **CONFIRMED compatibility/domain-candidate index** | Air-versus-Atmosphere ownership remains unresolved. |
| Canonical-target README | **CONFIRMED stale/underinclusive** | It describes a much smaller inventory than current repository search surfaces. |
| Filename conventions | **CONFIRMED conflicted** | PascalCase, snake_case, and kebab-case variants coexist. |
| `$id` convention | **CONFIRMED conflicted** | `https://schemas.kfm.local/schemas/...`, `https://schemas.kfm.local/contracts/...`, and `kfm://schemas/...` forms are present. |
| Principal object schemas | **CONFIRMED mostly permissive scaffolds in inspected examples** | Empty `properties` plus `additionalProperties: true` do not enforce domain meaning. |
| Atmosphere validator | **CONFIRMED placeholder** | `validate_atmosphere_decision_envelope.py` contains only a placeholder docstring. |
| Validators named by selected schema metadata | **ABSENT at checked paths** | Metadata pointers are not implementation proof. |
| Atmosphere fixtures/tests | **CONFIRMED documentation lanes / payload and execution proof incomplete** | README coverage does not establish schema validity or behavior. |
| Shared schema harness and `make schemas` | **CONFIRMED non-recursive for this domain lane** | Current shared runners do not establish recursive Atmosphere validation. |
| Domain workflow | **CONFIRMED TODO-only** | Green workflow state would not prove Atmosphere validation, proof closure, or release readiness. |
| Active consumers, registry, production schemas | **UNKNOWN** | No package/API/runtime/release consumer graph or activation record was verified. |

**Authority of this document:** compatibility guidance, drift disclosure, and migration guardrails only. Accepted ADRs, schema files, semantic contracts, registry records, validators, fixtures, tests, consumer evidence, release records, correction records, and steward decisions outrank this README.

---

## Placement and authority

### Directory Rules basis

KFM separates responsibilities:

```text
contracts/                         semantic meaning
schemas/contracts/v1/              machine-checkable shape
policy/                            admissibility and obligations
fixtures/                          deterministic examples
tests/                             executable proof
tools/validators/                  validation implementation
data/                              lifecycle records, receipts, proofs, catalogs, published artifacts
release/                           release, correction, withdrawal, rollback decisions
```

ADR-0001 proposes these schema paths:

```text
schemas/contracts/v1/<cross-cutting-family>/
schemas/contracts/v1/domains/<domain>/
```

It also says a top-level `schemas/<topic>/` subtree must not become permanent schema authority. Accordingly:

- `schemas/atmosphere/` is **compatibility/index only**;
- `schemas/contracts/v1/domains/atmosphere/` is the **proposed target**, not yet a clean accepted family;
- `schemas/contracts/v1/atmosphere/`, `schemas/contracts/v1/air/`, and `schemas/contracts/v1/domains/air/` require explicit disposition;
- no new Atmosphere schema should be added to a compatibility path;
- no duplicate should be deleted until consumers, unique content, ids, contracts, and migration needs are verified.

### Lifecycle and publication boundary

Schema validation never proves truth, evidence closure, rights clearance, policy approval, release approval, or public safety.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A schema may constrain shape at a governed step. It cannot promote a record, issue a health or life-safety advisory, publish a layer, or authorize a public API response.

---

## Responsibility routing

| Concern | Owning home | Compatibility-path role |
|---|---|---|
| Atmosphere semantic meaning | `contracts/domains/atmosphere/` | Link only. |
| Atmosphere machine shape | proposed `schemas/contracts/v1/domains/atmosphere/` | Point to selected schema after migration approval. |
| Shared schema families | `schemas/contracts/v1/<family>/` | Avoid Atmosphere copies when a shared profile is correct. |
| Policy | `policy/domains/atmosphere/` and accepted shared policy roots | Link only; never encode allow/deny rules here. |
| Fixtures | `fixtures/domains/atmosphere/` | Link verified valid/invalid examples. |
| Tests | `tests/domains/atmosphere/` | Link executable proof. |
| Validators | `tools/validators/domains/atmosphere/` or accepted shared validator roots | Link implementation and version. |
| Schema registry | accepted schema registry/control-plane surface | Link immutable identity, version, owner, state, and supersession. |
| Runtime/API/UI | governed packages and applications | Consumers must use accepted schemas and governed interfaces. |
| Lifecycle data | `data/<phase>/atmosphere/` | Never stored here. |
| Receipts and proofs | governed `data/receipts/` and `data/proofs/` roots | Link only. |
| Release and rollback | `release/` | Link release/correction/rollback records; never approve them. |
| Migration | accepted `migrations/schema/` plus drift/register records | Link the inventory-backed migration. |

### Anti-collapse rules

1. A filename is not object identity.
2. A `$id` is not canonical merely because it resolves.
3. A schema-valid object is not a true or released object.
4. A schema is not a semantic contract.
5. A fixture is not production data or proof of runtime behavior.
6. A validator pass is not policy or release approval.
7. `Air` is not a second Atmosphere authority without an accepted decision.
8. An empty permissive scaffold is not an active schema.
9. A generated file needs provenance and regeneration rules before it can be trusted.
10. A migration must preserve consumers, lineage, correction, and rollback.

---

## Confirmed path and identity drift

| Path | Repository evidence | Required posture |
|---|---|---|
| `schemas/atmosphere/` | README-only in bounded search | Freeze; index and migration pointers only. |
| `schemas/contracts/v1/atmosphere/` | Compatibility README | Freeze unless migration explicitly uses it. |
| `schemas/contracts/v1/air/` | Compatibility README plus real `AirStation.schema.json` scaffold | CONFLICTED; inventory consumers and migrate or formally profile. |
| `schemas/contracts/v1/domains/air/` | Compatibility/domain-candidate README | Do not add canonical schemas until Air ownership is decided. |
| `schemas/contracts/v1/domains/atmosphere/` | Large schema set with duplicate naming forms | Proposed target; freeze duplicate growth and inventory recursively. |

### Atmosphere versus Air

Directory Rules and Atmosphere placement doctrine use `atmosphere`. Other lineage material uses `air`. Creating both as evolving schema authorities is an ADR-class parallel-home risk.

Until resolved:

- use `atmosphere` for new planned placement;
- treat `air` paths as compatibility/drift candidates;
- do not create matching files in both paths;
- do not redirect consumers without a versioned migration and fallback plan.

---

## Confirmed filename and object-family collisions

Bounded search surfaced multiple naming forms for several families, including:

| Object-family key | Representative filename forms |
|---|---|
| AOD raster | `AODRaster.schema.json`, `aod_raster.schema.json`, `aod-raster.schema.json` |
| Advisory context | `AdvisoryContext.schema.json`, `advisory_context.schema.json`, `advisory-context.schema.json` |
| Forecast context | `ForecastContext.schema.json`, `forecast_context.schema.json`, `forecast-context.schema.json` |
| PM2.5 observation | `PM25Observation.schema.json`, `pm25_observation.schema.json`, `pm25-observation.schema.json` |
| Ozone observation | `OzoneObservation.schema.json`, `ozone_observation.schema.json`, `ozone-observation.schema.json` |
| Weather observation | `WeatherObservation.schema.json`, `weather_observation.schema.json`, `weather-observation.schema.json` |
| Temperature observation | `TemperatureObservation.schema.json`, `temperature_observation.schema.json`, `temperature-observation.schema.json` |
| Climate anomaly | `ClimateAnomaly.schema.json`, `climate_anomaly.schema.json`, `climate-anomaly.schema.json` |
| Air station | canonical-target candidate plus `schemas/contracts/v1/air/AirStation.schema.json` |

This table is illustrative, not exhaustive.

### Representative direct comparison: AOD raster

All three inspected AOD files are PROPOSED permissive scaffolds, but they are not byte mirrors:

| File | `$id` / identity | `source_doc` | `contract_doc` |
|---|---|---|---|
| `AODRaster.schema.json` | PascalCase path | `CANONICAL_PATHS.md` | `AODRaster.md` |
| `aod_raster.schema.json` | snake_case path | `MISSING_OR_PLANNED_FILES.md` | `aod_raster.md` |
| `aod-raster.schema.json` | kebab-case path | `FILE_SYSTEM_PLAN.md` | `aod-raster.md` |

Therefore a deletion based only on empty `properties` would lose lineage and may break unknown consumers. A migration must compare fields, metadata, refs, commits, consumers, and regeneration provenance.

### Collision key

A first-pass collision detector may normalize a filename by removing hyphens, underscores, spaces, and case. It may group candidates; it must not choose winners.

```python
from collections import defaultdict
from pathlib import Path
import re

root = Path("schemas/contracts/v1/domains/atmosphere")
groups: dict[str, list[Path]] = defaultdict(list)

for path in root.rglob("*.schema.json"):
    stem = path.name.removesuffix(".schema.json")
    key = re.sub(r"[-_\s]+", "", stem).lower()
    groups[key].append(path)

for key, paths in sorted(groups.items()):
    if len(paths) > 1:
        print(key)
        for path in sorted(paths):
            print(f"  {path}")
```

---

## Schema maturity boundary

### Observed classes

| Class | Example | Safe interpretation |
|---|---|---|
| Empty permissive scaffold | AOD and AtmosphereAirDecisionEnvelope examples | Shape is not defined; schema presence is planning evidence only. |
| Minimal `id` scaffold | `domain_observation`, `run_receipt`, `evidence_drawer_payload`, `layer_manifest` | Only a minimal field is enforced; domain invariants remain unproved. |
| Alias-lane scaffold | `schemas/contracts/v1/air/AirStation.schema.json` | Path and object identity are conflicted; no consumer should treat it as canonical. |
| README index | compatibility and child-lane READMEs | Navigation only; no machine validation. |
| Active schema | **NOT ESTABLISHED in this review** | Requires accepted identity, contract, fixtures, validator, tests, registry, consumers, and review. |

### Promotion requirements

A schema must not be called `ACTIVE_SCHEMA` until all material requirements are verified:

- stable object-family identity and canonical filename;
- stable `$id`, version, dialect, and supersession rules;
- one paired semantic contract;
- meaningful required fields and constraints;
- valid, invalid, edge, and negative fixtures;
- executable validator and tests;
- schema registry record and owner;
- policy/evidence/release boundaries where relevant;
- consumer compatibility evidence;
- correction, deprecation, migration, and rollback posture;
- steward review and release state.

---

## Contract-schema pairing

`contracts/domains/atmosphere/` is the semantic home. It documents principal object families such as stations, observations, pollutant-specific records, smoke/AOD context, weather fields, climate context, advisory context, and the Atmosphere/Air decision envelope.

Current risks include:

- duplicate contract filenames in PascalCase and kebab-case forms;
- schema metadata pointing to different contract filename forms;
- schema filenames that do not clearly identify one contract;
- support objects that may belong in shared runtime, release, receipt, layer, evidence, or registry families rather than Atmosphere-specific copies;
- empty schemas that cannot enforce the contract’s source-role, knowledge-character, unit, time, evidence, or safety rules.

Before selecting a schema-contract pair, record:

```text
object_family_id
canonical_schema_path
canonical_schema_id
schema_version
canonical_contract_path
contract_version
superseded_schema_paths
superseded_contract_paths
compatibility_window
consumer_list
fixture_set
validator
registry_record
migration_record
rollback_target
review_decision
```

### Domain anti-collapse requirements

Atmosphere schemas must preserve these distinctions where applicable:

- AQI/reporting context is not concentration;
- AOD is not PM2.5;
- smoke context is not measured exposure or impact proof;
- modeled or forecast data is not observed data;
- station/site context is not observation truth;
- climate normal is not an observation or anomaly;
- advisory context is referral context, not emergency or life-safety authority;
- source time, observed time, valid time, issue time, retrieval time, and processing time are not one timestamp;
- source role and knowledge character must not be inferred from a convenient filename.

---

## Schema identity and registry posture

### Confirmed identity drift

Observed schema IDs use multiple roots:

```text
https://schemas.kfm.local/schemas/contracts/v1/...
https://schemas.kfm.local/contracts/v1/...
kfm://schemas/contracts/v1/...
```

ADR-0001 explicitly defers final `$id`, canonicalization, and `spec_hash` conventions. This README therefore does not choose a namespace.

### Minimum registry record

An authoritative registry, once identified, should carry at least:

| Field | Purpose |
|---|---|
| `schema_id` | Stable logical identity. |
| `canonical_path` | Selected repository path. |
| `json_schema_id` | Exact `$id`. |
| `version` | Machine-shape version. |
| `object_family_id` | Stable semantic family. |
| `contract_ref` | Paired semantic contract. |
| `status` | Finite activation state. |
| `owner` and reviewers | Accountability. |
| `content_digest` | Exact bytes or canonical digest. |
| `supersedes` / `superseded_by` | Lineage. |
| `aliases` | Compatibility ids and paths. |
| `fixture_refs` / `validator_ref` | Enforceability proof. |
| `consumer_refs` | Migration impact. |
| `migration_ref` / `rollback_ref` | Reversibility. |
| `reviewed_at` | Decision time. |

A file becomes active through governed registry/review state, not merely by existing under a proposed canonical directory.

---

## Fixtures, tests, validators, and CI

### Current proof boundary

| Surface | Current evidence | Limit |
|---|---|---|
| `fixtures/domains/atmosphere/README.md` | Rich object-lane index | Payload inventory and schema binding remain unverified. |
| `tests/domains/atmosphere/README.md` | Rich expected-test plan | Executable test inventory remains unverified. |
| `validate_atmosphere_decision_envelope.py` | File exists | Placeholder docstring only. |
| Validators named by selected schema metadata | Direct 404 at checked paths | Metadata is stale or implementation is missing there. |
| `tests/schemas/test_common_contracts.py` | Executable harness | Enumerates selected top-level families; it does not recurse into `domains/atmosphere`. |
| `make schemas` | Runs `_common/run_all.py` | Runner lists selected shared validators only; no Atmosphere validator is included. |
| `.github/workflows/schema-validation.yml` | Runs `make schemas` | Does not prove Atmosphere domain schema coverage. |
| `.github/workflows/domain-atmosphere.yml` | Workflow exists | Jobs only echo TODO. |

### Minimum negative cases

Atmosphere schema proof should include failures for:

- missing required identity, source role, knowledge character, unit, or time context;
- invalid `$id`, version, enum, format, or additional property;
- AQI/report value used as concentration;
- AOD used as PM2.5;
- modeled/forecast field labeled as observed;
- smoke context used as exposure or impact proof;
- low-cost sensor caveat omitted where required;
- unit or averaging-period ambiguity;
- climate anomaly without baseline/reference period;
- advisory context used as emergency instruction;
- evidence-dependent answer without resolvable evidence support;
- stale, corrected, superseded, withdrawn, or unreleased public response;
- duplicate schema alias accepted without explicit profile selection;
- schema metadata pointing to a missing contract, fixture, validator, or registry record.

Tests should remain deterministic, public-safe, and no-network by default.

---

## Governed migration sequence

### Phase 0 — Freeze

- Freeze new schema files under all compatibility and duplicate paths.
- Permit only documentation, inventory, correction, and migration changes.
- Record emergency exceptions explicitly.

### Phase 1 — Recursive inventory

For every Atmosphere/Air schema file, capture:

```text
path
blob_sha
byte_size
content_digest
schema dialect
$id
title
type
required fields
additional/unevaluated property posture
x-kfm status
source_doc
contract_doc
fixtures_root
validator
policy ref
generator/provenance
consumers
last modifying commit
```

### Phase 2 — Collision groups

Group candidates by normalized filename, contract reference, title, logical object family, and consumer use. Compare bytes and semantics. Preserve unique metadata and lineage.

### Phase 3 — Canonical selection proposal

For each family, propose one canonical schema path and contract pair. Record why it was selected, what it supersedes, aliases, compatibility window, consumers, and rollback target. Approval must be reviewable; filename aesthetics are insufficient.

### Phase 4 — Harden selected schemas

Define meaningful fields and constraints while preserving Atmosphere source-role, knowledge-character, units, time, evidence, sensitivity, release, and correction boundaries.

### Phase 5 — Proof

Add valid/invalid/edge fixtures, executable validators, domain tests, collision checks, metadata-reference checks, and CI coverage. Capture validation receipts where required.

### Phase 6 — Consumer migration

Migrate packages, pipelines, APIs, UI, generators, validators, registries, and release tooling to canonical ids and paths. Use explicit adapters only when reviewed and temporary.

### Phase 7 — Deprecation and retirement

Mark superseded schemas and aliases, preserve history, block new consumers, validate no active imports remain, and retire only after the compatibility window and rollback checks pass.

### Phase 8 — Compatibility-path decision

Retain `schemas/atmosphere/README.md` as a tombstone/index if inbound links require it, or remove the directory through a documented migration once all links and consumers are updated. This README alone authorizes neither outcome.

---

## Finite status model

### Compatibility path

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | Navigation and drift guidance only. |
| `FROZEN` | No new schema definitions. |
| `TRANSITIONAL` | Governed migration is active. |
| `DEPRECATED` | No new consumers; retirement planned. |
| `TOMBSTONE` | Historical pointer after migration. |
| `RETIRED` | Removed after verified migration and link cleanup. |

Current proposed status for `schemas/atmosphere/`: `INDEX_ONLY` + `FROZEN`.

### Schema candidate

| Status | Meaning |
|---|---|
| `DISCOVERED` | File exists; identity not resolved. |
| `COLLISION_CANDIDATE` | Normalized family has multiple files. |
| `STUB` | Shape is empty or materially incomplete. |
| `DRAFT_SCHEMA` | Meaningful fields exist; review/proof incomplete. |
| `READY_FOR_REVIEW` | Pairing, fixtures, validator, registry packet, and migration impact are prepared. |
| `ACTIVE_SCHEMA` | Accepted and registry-backed with enforceability proof. |
| `HELD` | Conflict, evidence, ownership, consumer, or safety blocker exists. |
| `SUPERSEDED` | New accepted schema replaces it. |
| `DEPRECATED` | Supported only during a compatibility window. |
| `RETIRED` | No active consumers and migration closure verified. |

Path presence must never be treated as `ACTIVE_SCHEMA`.

---

## Minimal compatibility note

```markdown
# <atmosphere-schema-note-id>

## Status
INDEX_ONLY / FROZEN / DISCOVERED / COLLISION_CANDIDATE / STUB / DRAFT_SCHEMA / READY_FOR_REVIEW / ACTIVE_SCHEMA / HELD / SUPERSEDED / DEPRECATED / RETIRED

## Scope
<object family or compatibility path>

## Current path
<repository path>

## Proposed canonical path
<path or NEEDS VERIFICATION>

## Schema identity
- Logical schema ID: <id or UNKNOWN>
- JSON Schema `$id`: <value or UNKNOWN>
- Version: <value or UNKNOWN>
- Digest: <value or UNKNOWN>

## Paired contract
<path or NEEDS VERIFICATION>

## Collision and alias set
<paths or none>

## Unique content to preserve
<metadata, fields, lineage, consumer requirements, or none>

## Proof
- Fixtures: <refs or NEEDS VERIFICATION>
- Validator: <ref or NEEDS VERIFICATION>
- Tests/CI: <refs or NEEDS VERIFICATION>

## Consumers and registry
<refs or UNKNOWN>

## Decision and rollback
<decision, migration ref, rollback target, reviewers, date>
```

---

## Definition of done

### This compatibility README

- [x] Declares `schemas/atmosphere/` index-only and frozen.
- [x] Identifies the proposed target without claiming it is clean or accepted.
- [x] Records Air/Atmosphere path conflicts.
- [x] Records representative filename and `$id` drift.
- [x] Separates schemas from contracts, policy, fixtures, validators, data, and release authority.
- [x] States current validation and CI limitations.
- [x] Provides migration, correction, and rollback guidance.
- [x] Changes no schema bytes.

### Atmosphere schema family

Not done until:

- [ ] recursive inventory is complete;
- [ ] collision families and unique content are reviewed;
- [ ] Atmosphere/Air ownership is resolved;
- [ ] canonical filenames, `$id`s, versions, and contracts are accepted;
- [ ] selected schemas are field-complete;
- [ ] fixtures, validators, tests, and CI prove positive and negative behavior;
- [ ] registry and consumer migration are complete;
- [ ] deprecation, correction, release, and rollback paths are verified;
- [ ] stewards approve activation.

---

## Validation

### README checks performed

- one rendered H1;
- no heading-level jumps outside fenced examples;
- balanced code fences;
- no duplicate rendered headings;
- all quick-navigation fragments resolve;
- no trailing whitespace;
- no common credential or private-key patterns;
- no Mermaid block;
- exact remote blob comparison after commit;
- one-file base-to-head scope comparison.

### Grounded repository checks

```bash
# Confirm this compatibility path remains README-only.
find schemas/atmosphere -maxdepth 4 -type f | sort

# Inventory Atmosphere and Air schema paths.
find schemas/contracts/v1 \
  \( -path '*/atmosphere/*' -o -path '*/air/*' \) \
  -type f | sort

# JSON syntax only; not semantic or governance validation.
find schemas/contracts/v1/domains/atmosphere -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Inspect paired proof surfaces.
find contracts/domains/atmosphere fixtures/domains/atmosphere \
  tests/domains/atmosphere tools/validators/domains/atmosphere \
  -maxdepth 6 -type f 2>/dev/null | sort
```

### Known limitations

```text
make schemas
  -> selected shared validators only
  -> no recursive Atmosphere proof

tests/schemas/test_common_contracts.py
  -> selected top-level schema families
  -> no domains/atmosphere recursion

domain-atmosphere workflow
  -> TODO echo jobs
  -> no Atmosphere validation or release proof
```

Repository tests, schema validation, fixture execution, consumer analysis, and workflow completion were **not run** for this Markdown-only API change.

---

## Correction and rollback

### Correction rule

When a path, status, pairing, consumer, registry, or proof claim changes:

1. issue a transparent correction;
2. identify the evidence snapshot and affected claim;
3. update canonical and compatibility indexes together;
4. preserve prior schema and documentation history;
5. propagate the correction to consumers, registry records, migration records, and release/correction surfaces where material;
6. verify public clients remain behind governed interfaces.

### Before merge

- leave the draft PR unmerged; or
- restore prior blob `6203c2f9ea1fc7209d794527ffb98b3cea1fec6f` in a transparent follow-up commit.

### After merge

- revert the implementation commit or PR;
- do not reset or rewrite shared history;
- keep independently verified schema drift in the backlog even if this prose is reverted.

This change modifies no schema, contract, registry, consumer, or published artifact, so no schema-data rollback is required.

---

## Open verification backlog

### Placement and ownership

- [ ] Confirm ADR-0001 governing status.
- [ ] Resolve `atmosphere` versus `air` segment ownership.
- [ ] Decide the disposition of all Atmosphere/Air compatibility paths.
- [ ] Confirm CODEOWNERS and required reviewers.
- [ ] Record the conflict in the drift register.

### Inventory and identity

- [ ] Export a recursive inventory with blobs, digests, metadata, `$id`, contract refs, and consumers.
- [ ] Build collision groups and semantic comparisons.
- [ ] Identify generated versus hand-authored provenance.
- [ ] Select object-family identities, filenames, `$id`s, and versions.
- [ ] Preserve unique lineage and metadata.

### Pairing and proof

- [ ] Resolve duplicate contract filenames and slugs.
- [ ] Pair each selected schema with one semantic contract.
- [ ] Decide which support objects belong in shared schema families.
- [ ] Harden schemas beyond empty/permissive scaffolds.
- [ ] Implement or correct validators named by metadata.
- [ ] Add fixture payloads, executable tests, collision checks, and recursive CI.

### Registry and consumers

- [ ] Identify and populate the authoritative schema registry.
- [ ] Inventory package, pipeline, API, UI, validator, generator, and release consumers.
- [ ] Define compatibility adapters and windows where required.
- [ ] Add migration receipts and proof.

### Migration and release

- [ ] Create a migration manifest under the accepted migration root.
- [ ] Define deprecation, correction, supersession, and rollback behavior.
- [ ] Validate release and public-client bindings.
- [ ] Obtain schema, contract, domain, validation, registry, consumer, and release review.

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior target README | **CONFIRMED** | Existing compatibility intent and rollback blob. | Understated current drift. |
| `schemas/README.md` | **CONFIRMED** | Machine-shape responsibility and no-parallel-authority rule. | Not a recursive Atmosphere inventory. |
| ADR-0001 | **CONFIRMED document / PROPOSED** | Proposed schema home and migration discipline. | Not accepted; naming and `$id` remain partly deferred. |
| Atmosphere canonical-path doctrine | **CONFIRMED draft** | `atmosphere` target and Air/Atmosphere conflict. | Older planning document originally lacked repo proof. |
| Atmosphere target README | **CONFIRMED** | Proposed target and child indexes. | Inventory is stale/underinclusive. |
| Atmosphere/Air compatibility READMEs | **CONFIRMED** | Parallel-path conflict and unresolved ownership. | Do not select authority. |
| `schemas/contracts/v1/air/AirStation.schema.json` | **CONFIRMED** | A real schema exists under a lane described as compatibility. | No consumer or activation proof. |
| Three AOD variants | **CONFIRMED direct reads** | Filename, `$id`, source-doc, and contract-doc drift. | One fully opened collision family only. |
| Atmosphere support schemas | **CONFIRMED direct reads** | Minimal permissive maturity and metadata-declared validators. | Not exhaustive. |
| Atmosphere contracts README | **CONFIRMED** | Semantic home and object roster; naming drift acknowledged. | No enforceability proof. |
| Atmosphere validator placeholder and 404 checks | **CONFIRMED at checked paths** | Validator metadata does not equal implementation. | Equivalent validators elsewhere remain possible. |
| Atmosphere fixtures/tests READMEs | **CONFIRMED** | Intended proof lanes and no-network posture. | Payload and execution coverage unverified. |
| Shared harness, runner, and workflows | **CONFIRMED direct reads** | Current automated paths do not establish recursive Atmosphere validation. | Hidden/external automation remains UNKNOWN. |
| Bounded repository search | **CONFIRMED search evidence** | Duplicate names and paths surfaced. | Not a complete tree or consumer graph. |

[Back to top](#top)
