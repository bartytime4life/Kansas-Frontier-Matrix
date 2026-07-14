<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-agriculture-src-readme
title: Agriculture Domain Package Source Root README
type: readme
version: v0.2
status: draft; repository-grounded; python-source-root; implementation-placeholder; PROPOSED source-root contract
owners:
  - OWNER_TBD — Agriculture package/domain steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Policy, rights, and sensitivity steward
  - OWNER_TBD — Evidence and release steward
  - OWNER_TBD — Validation, security, and docs steward
created: 2026-06-13
updated: 2026-07-14
supersedes: v0.1 (2026-06-13)
policy_label: public; packages; agriculture; python; no-network; field-level-deny-by-default; non-authoritative
path: packages/domains/agriculture/src/README.md
repository_snapshot: main@14b59b6b84ee2b9fa46e002b60e922c97cab2761
initial_evidence_snapshot: main@98b39c7171129b90ca858e2e3849ed121c0d7769
truth_posture: CONFIRMED target and prior blob, Python project name/version, src layout, agriculture import package, empty initializer, merged child-module v0.2 contract, domain doctrine, contract/schema/policy indexes, domain tests/fixtures, Directory Rules, and echo-only domain workflow / PROPOSED future package discovery, exports, pure adapters, generated code, and test sublanes / CONFLICTED contract/schema compatibility paths, AggregationReceipt pairing/naming, policy outcome vocabulary, and stale parent package documentation / UNKNOWN build backend, dependencies, Python requirement, consumers, executable helpers, validators, passing tests, release artifacts, and runtime behavior
related:
  - ./agriculture/README.md
  - ../README.md
  - ../pyproject.toml
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/agriculture/README.md
  - ../../../../contracts/domains/agriculture/README.md
  - ../../../../schemas/contracts/v1/domains/agriculture/README.md
  - ../../../../policy/domains/agriculture/README.md
  - ../../../../tests/domains/agriculture/README.md
  - ../../../../fixtures/domains/agriculture/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../.github/workflows/domain-agriculture.yml
tags: [kfm, packages, domains, agriculture, python, src-layout, source-root, import-boundary, candidate-dto, source-role, time-kinds, aggregation, privacy, no-network, fail-closed, compatibility, rollback]
notes:
  - "v0.2 replaces runtime and manifest uncertainty with a commit-pinned description of the current Python src-layout scaffold."
  - "The project declares kfm-domain-agriculture 0.0.0; src/agriculture/__init__.py is empty; no implemented helper modules or exports are claimed."
  - "The merged src/agriculture/README.md v0.2 owns detailed helper semantics; this file owns source-root, import, dependency, generated-code, packaging, and test-placement boundaries."
  - "The existing Agriculture domain test and fixture roots are tests/domains/agriculture/ and fixtures/domains/agriculture/; package-specific parallel roots are not established."
  - "The domain-agriculture workflow contains echo-TODO jobs and does not prove validation, proof construction, or publication readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Domain Package Source Root

`packages/domains/agriculture/src/`

> Python `src`-layout container for the `kfm-domain-agriculture` shared package. This directory may organize reusable, source-agnostic Agriculture helper code, but it must not become Agriculture doctrine, object or schema authority, source admission, field/operator truth authority, hidden lifecycle writer, EvidenceBundle producer, policy engine, release authority, or public trust membrane.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-1f6feb)
![layout](https://img.shields.io/badge/layout-Python%20src--layout-3776ab)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![sensitivity](https://img.shields.io/badge/field%20%2F%20operator-deny%20by%20default-critical)
![network](https://img.shields.io/badge/import%20network-forbidden-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

> [!IMPORTANT]
> **Review-branch base:** `main` at `14b59b6b84ee2b9fa46e002b60e922c97cab2761`  
> **Detailed Agriculture evidence snapshot:** `main` at `98b39c7171129b90ca858e2e3849ed121c0d7769`; intervening changes affected only unrelated policy and Hazards configuration READMEs  
> **Distribution:** `kfm-domain-agriculture`  
> **Version:** `0.0.0`  
> **Verified source root:** `src/`  
> **Verified import package:** `src/agriculture/`  
> **Verified implementation:** empty `agriculture/__init__.py`; no helper module implementation established  
> **Verified child contract:** [`agriculture/README.md`](./agriculture/README.md) v0.2  
> **Build backend, dependencies, Python requirement, exports, and consumers:** not established  
> **Domain tests and fixtures:** README-backed lanes exist under `tests/domains/agriculture/` and `fixtures/domains/agriculture/`; execution and payload coverage remain unverified  
> **Domain CI:** echo-TODO scaffold, not enforcement proof

> [!CAUTION]
> A crop-code mapping is not a `CropObservation`. A geometry key is not a confirmed field. A yield adapter is not yield truth. A field candidate is not a parcel or operator record. An aggregation helper is not an `AggregationReceipt`, a redaction decision, an EvidenceBundle, a PolicyDecision, or release authorization.

---

## Quick jump

- [1. Purpose and audience](#1-purpose-and-audience)
- [2. Current repository state](#2-current-repository-state)
- [3. Source-root bounded context](#3-source-root-bounded-context)
- [4. Placement and authority](#4-placement-and-authority)
- [5. Current directory surface](#5-current-directory-surface)
- [6. Source root versus import package](#6-source-root-versus-import-package)
- [7. Import and export contract](#7-import-and-export-contract)
- [8. Import-time safety](#8-import-time-safety)
- [9. Dependency direction](#9-dependency-direction)
- [10. Agriculture object-family boundary](#10-agriculture-object-family-boundary)
- [11. Native values, source roles, and time kinds](#11-native-values-source-roles-and-time-kinds)
- [12. Contracts, schemas, policy, and drift](#12-contracts-schemas-policy-and-drift)
- [13. Field, operator, and aggregation safety](#13-field-operator-and-aggregation-safety)
- [14. Lifecycle, evidence, receipts, and release](#14-lifecycle-evidence-receipts-and-release)
- [15. Proposed source-tree evolution](#15-proposed-source-tree-evolution)
- [16. Generated code and schema adapters](#16-generated-code-and-schema-adapters)
- [17. Tests and fixtures](#17-tests-and-fixtures)
- [18. Packaging, installation, and CI gates](#18-packaging-installation-and-ci-gates)
- [19. Security and observability](#19-security-and-observability)
- [20. Compatibility, correction, and rollback](#20-compatibility-correction-and-rollback)
- [21. Validation commands](#21-validation-commands)
- [22. Definition of done](#22-definition-of-done)
- [23. Open verification register](#23-open-verification-register)
- [24. Evidence ledger](#24-evidence-ledger)
- [25. Maintainer checklist](#25-maintainer-checklist)

---

## 1. Purpose and audience

`packages/domains/agriculture/src/` is the implementation container for the Python project declared by [`../pyproject.toml`](../pyproject.toml).

Its durable responsibility is structural:

- contain importable source for the `agriculture` package;
- make package discovery and import boundaries explicit;
- provide a stable home for reusable Agriculture helper code;
- keep package exports deliberate, small, and reviewable;
- preserve source-native values, source roles, uncertainty, identity lineage, and time kinds;
- keep generated adapters subordinate to accepted contracts and schemas;
- keep implementation separate from source-specific connectors, pipelines, lifecycle data, policy, evidence, receipts, release, and public serving;
- support deterministic, offline-first tests without storing production payloads in the source root.

This README is for package and domain maintainers, connector/pipeline authors, contract/schema/validator/test maintainers, governance stewards, and security reviewers.

Detailed helper semantics belong in [`agriculture/README.md`](./agriculture/README.md). This source-root README governs the container, import surface, dependency direction, generated-code boundary, packaging posture, and enforceability placement.

[Back to top](#top)

---

## 2. Current repository state

| Surface | Evidence at snapshot | Status | Consequence |
|---|---|---|---|
| This README | Existing v0.1 source-root planning document. | **CONFIRMED** | Revised in place. |
| [`../pyproject.toml`](../pyproject.toml) | Declares `[project]`, name `kfm-domain-agriculture`, and version `0.0.0` only. | **CONFIRMED minimal placeholder** | Python distribution identity is known; build and dependency behavior are not. |
| [`agriculture/README.md`](./agriculture/README.md) | Repository-grounded child-module contract v0.2. | **CONFIRMED** | Detailed helper, candidate, sensitivity, and authority guidance lives there. |
| `agriculture/__init__.py` | Exists and is empty. | **CONFIRMED** | Import-package marker only; no public exports are established. |
| Selected proposed helper files | `core.py`, `crop.py`, `field_identity.py`, and `aggregation.py` were absent at exact tested paths during the child-module review. | **CONFIRMED bounded absence** | No executable Agriculture helper implementation is established. |
| Build backend | No `[build-system]` section was observed. | **NOT OBSERVED** | Build and install behavior remain unknown. |
| Dependencies | No dependency list was observed. | **NOT OBSERVED** | Do not claim compatibility or isolation. |
| Supported Python versions | No `requires-python` field was observed. | **NOT OBSERVED** | Supported interpreter range is unknown. |
| Public exports | Empty initializer. | **NOT ESTABLISHED** | No symbol is part of a supported package API. |
| Consumers | Indexed search during child-module review did not establish package consumers. | **NOT OBSERVED / search-limited** | Do not claim production integration. |
| Agriculture doctrine | Domain README documents twelve object families and aggregate/permissioned public posture. | **CONFIRMED repository document** | Helpers must preserve domain and sensitivity boundaries. |
| Semantic contracts | Contract index exists; object-level coverage remains incomplete and a compatibility path also exists. | **CONFIRMED index / CONFLICTED placement** | Do not generate models as if all contracts were accepted. |
| Schema lane | Domain schema index exists; `aggregation_receipt.schema.json` is a permissive proposed scaffold and a shorter alias lane exists. | **CONFIRMED index / incomplete** | Generated adapters are blocked pending authority and field-completeness. |
| Policy lane | Domain policy README exists; executable files and runtime enforcement remain unverified. | **CONFIRMED index / UNKNOWN enforcement** | Package helpers cannot act as policy. |
| Agriculture tests | [`tests/domains/agriculture/README.md`](../../../../tests/domains/agriculture/README.md) documents domain test lanes; modules/results remain unverified. | **CONFIRMED README-backed lanes / NOT RUN** | Use the existing domain test root. |
| Agriculture fixtures | [`fixtures/domains/agriculture/README.md`](../../../../fixtures/domains/agriculture/README.md) documents multiple fixture lanes; payload inventory and wiring remain incomplete. | **CONFIRMED README-backed lanes / partial** | Reuse governed domain fixtures or add a reviewed sublane. |
| Domain workflow | `.github/workflows/domain-agriculture.yml` contains three echo-TODO jobs. | **CONFIRMED scaffold** | A green workflow does not prove validation or publication readiness. |
| Runtime/release evidence | No build artifact, emitted receipt, deployed consumer, runtime log, or release artifact was inspected. | **UNKNOWN** | This README is not implementation proof. |

```text
Python distribution identity            = CONFIRMED
Python src-layout container              = CONFIRMED
agriculture import package               = CONFIRMED
empty initializer                        = CONFIRMED
implemented helper modules               = NOT OBSERVED
public exports                           = NOT ESTABLISHED
package consumers                        = NOT OBSERVED
build/install behavior                   = UNKNOWN
domain test/fixture READMEs              = CONFIRMED
test execution and payload coverage      = UNKNOWN
policy enforcement                       = UNKNOWN
runtime/release behavior                 = UNKNOWN
```

[Back to top](#top)

---

## 3. Source-root bounded context

The source-root bounded context is:

> The organization and admission boundary for importable, reusable Agriculture helper implementation.

It includes source-tree structure, import placement, exports, dependency direction, generated-code placement, tests/fixtures integration, and packaging.

It excludes doctrine, canonical object meaning, schema authority, source admission, crop/field/yield/operator truth, lifecycle orchestration, policy evaluation, evidence closure, authoritative receipts, release, and public serving.

| Concept | Current value | Status |
|---|---|---|
| Distribution name | `kfm-domain-agriculture` | **CONFIRMED** |
| Import package | `agriculture` | **CONFIRMED path / no exports** |
| Version | `0.0.0` | **CONFIRMED placeholder** |
| Public package API | none established | **NOT OBSERVED** |
| Build backend | none observed | **UNKNOWN** |

[Back to top](#top)

---

## 4. Placement and authority

Directory Rules classify `packages/` as the canonical root for shared reusable code.

```text
packages/domains/agriculture/src/       = package implementation container
packages/domains/agriculture/src/agriculture/
                                        = Agriculture import package
docs/domains/agriculture/               = doctrine and domain scope
contracts/domains/agriculture/          = semantic meaning
schemas/contracts/v1/domains/agriculture/
                                        = machine-checkable shape
policy/domains/agriculture/             = Agriculture admissibility policy
connectors/                             = source-specific acquisition/admission support
pipelines/domains/agriculture/          = executable transformations
pipeline_specs/agriculture/             = declarative run specifications
tests/domains/agriculture/              = enforceability proof
fixtures/domains/agriculture/           = test/example inputs
data/                                   = lifecycle data, receipts, proofs, registries
release/                                = release/correction/rollback decisions
apps/governed-api/                      = public trust membrane
```

This source root may organize reusable implementation, expose reviewed helpers, preserve governed references, and support no-network tests.

It may not create parallel contract/schema/policy/test/fixture/receipt/proof/release authority, contain source-specific clients or secrets by default, execute hidden network requests, write lifecycle state, approve exact disclosure, publish, or serve public clients.

[Back to top](#top)

---

## 5. Current directory surface

```text
packages/domains/agriculture/src/
├── README.md
└── agriculture/
    ├── README.md
    └── __init__.py    # empty
```

This is a bounded inspected shape, not a recursive tree proof.

| Path | Current role | Status |
|---|---|---|
| `src/README.md` | Source-root contract. | **CONFIRMED; this file** |
| `src/agriculture/README.md` | Detailed helper-module contract. | **CONFIRMED v0.2** |
| `src/agriculture/__init__.py` | Import-package marker. | **CONFIRMED empty** |
| Executable helper modules | No tested helper file was found. | **NOT OBSERVED** |

The old README omitted the initializer and described Python as unverified. v0.2 corrects both claims.

[Back to top](#top)

---

## 6. Source root versus import package

| Layer | Responsibility | Must not become |
|---|---|---|
| `src/` | Container, discovery boundary, generated-code placement, import/dependency rules. | A second package, test root, data store, or workflow root. |
| `src/agriculture/` | Reusable Agriculture helper implementation and deliberate exports. | Doctrine, canonical object authority, policy engine, pipeline, or public API. |
| `src/agriculture/__init__.py` | Curated export surface. | Wildcard export of unstable internals. |
| Future internal modules | Narrow pure helpers and typed results. | Source-specific connectors, lifecycle writers, or release approvers. |

Do not add sibling import packages such as `agriculture_core`, `kfm_agriculture`, or `ag_domain` without an accepted responsibility split, compatibility plan, and migration.

[Back to top](#top)

---

## 7. Import and export contract

The empty initializer is the current public truth.

A symbol may enter `agriculture.__init__` only when:

1. its responsibility belongs here;
2. its semantic source is identified;
3. any contract/schema dependency is accepted and version-pinned;
4. its side effects are absent or explicit;
5. native values, source roles, time kinds, uncertainty, and sensitivity are preserved;
6. positive and negative tests exist;
7. restricted/private-adjacent fields are not public by default;
8. compatibility is documented;
9. package/domain stewards approve the export.

New helpers remain internal until stable. Do not wildcard export, expose fixtures in production API, re-export schemas as authority, export source-specific clients, or imply API stability while version is `0.0.0`.

[Back to top](#top)

---

## 8. Import-time safety

Importing `agriculture` must not:

- access the network;
- resolve credentials, tokens, cookies, or secret files;
- read environment variables for governance decisions;
- read/write lifecycle, registry, proof, receipt, or release paths;
- create caches/directories;
- initialize telemetry;
- spawn threads, timers, processes, or background tasks;
- evaluate policy;
- load live source descriptors;
- infer field/operator identity;
- select a schema authority silently;
- download vocabularies or crosswalks.

Safe import behavior is limited to definitions, safe constants, type declarations, lazy references, lightweight version metadata, and exceptions.

[Back to top](#top)

---

## 9. Dependency direction

```text
connector / pipeline / worker / validator / tool / governed app / test
  -> agriculture package
  -> candidate DTO, normalized metadata, issue, or adapter result
  -> caller-owned lifecycle, evidence, policy, review, and release flow
```

Blocked:

```text
agriculture package
  -> apps/
  -> source-specific connectors/
  -> executable pipelines/
  -> data lifecycle stores
  -> release records
  -> policy authority
  -> public UI/map runtime
  -> hidden source-registry mutation
```

Dependencies must be explicit and declared. Circular dependencies with connectors or Agriculture pipelines are prohibited.

[Back to top](#top)

---

## 10. Agriculture object-family boundary

Agriculture doctrine names:

`CropObservation` · `FieldCandidate` · `CropRotation` · `YieldObservation` · `IrrigationLink` · `ConservationPractice` · `SoilCropSuitability` · `AgriculturalEconomyObservation` · `SupplyChainNode` · `DroughtStressIndicator` · `PestStressIndicator` · `AggregationReceipt`

This source root does not define canonical meaning or shape.

Future candidate/adaptor results must preserve source-native values, source/evidence refs, source role, time kinds, geometry lineage/precision, uncertainty, rights/sensitivity refs, validation issues, and correction/supersession links.

Disallowed upgrades:

```text
mapped crop code       -> confirmed CropObservation
geometry cluster       -> confirmed FieldCandidate
parsed yield value     -> yield truth
irrigation indicator   -> water-right truth
soil join              -> Agriculture-owned Soil truth
model output           -> observed event
aggregation output     -> AggregationReceipt
fixture object         -> canonical record
```

[Back to top](#top)

---

## 11. Native values, source roles, and time kinds

Normalizers and crosswalks must preserve original code, label, unit, ID, geometry/ref, vocabulary/version, mapping version, ambiguity, and transform notes.

Source role must be supplied by governed source metadata, never inferred from provider, filename, URL, field names, apparent official status, or model confidence.

Do not collapse source publication, observation, valid/effective, retrieval, model-run, aggregation-window, release, and correction times into a generic timestamp. Missing required time semantics must produce an explicit issue.

[Back to top](#top)

---

## 12. Contracts, schemas, policy, and drift

| Concern | Repository surface | Package posture |
|---|---|---|
| Meaning | [`contracts/domains/agriculture/README.md`](../../../../contracts/domains/agriculture/README.md) | Consume accepted contracts; do not redefine. |
| Shape | [`schemas/contracts/v1/domains/agriculture/README.md`](../../../../schemas/contracts/v1/domains/agriculture/README.md) | Generate/validate only from accepted field-complete schemas. |
| Admissibility | [`policy/domains/agriculture/README.md`](../../../../policy/domains/agriculture/README.md) | Carry inputs/results; never decide locally. |
| Test proof | [`tests/domains/agriculture/README.md`](../../../../tests/domains/agriculture/README.md) | Put reviewed behavior tests under this root. |
| Test inputs | [`fixtures/domains/agriculture/README.md`](../../../../fixtures/domains/agriculture/README.md) | Reuse/add synthetic public-safe fixtures here. |

Confirmed drift includes a compatibility contract path, a shorter schema alias lane, a permissive `AggregationReceipt` scaffold, contract filename/path mismatch, and unverified policy vocabulary/enforcement.

Until resolved:

- no generated canonical Agriculture model package;
- no convenience adapter that silently selects a compatibility schema;
- no package enum presented as policy authority;
- no canonical `AggregationReceipt` constructor;
- no automatic public-safe field transform;
- no public API promise based on scaffold schemas.

[Back to top](#top)

---

## 13. Field, operator, and aggregation safety

```text
aggregate/permissioned product = eligible for further review
exact field geometry          = deny/restrict by default
operator-resolved detail      = deny by default
private parcel-adjacent join  = deny by default
rights-unknown source detail  = abstain/hold/deny
quarantine-adjacent material  = deny public use
```

A helper handling spatial/operator-adjacent data must receive explicit caller context, preserve precision/sensitivity internally without logging it, return method/parameters and uncertainty, and state that any aggregation/generalization is unapproved.

```text
aggregation calculation
  != AggregationReceipt
  != PolicyDecision
  != EvidenceBundle
  != ReleaseManifest
  != published layer
```

[Back to top](#top)

---

## 14. Lifecycle, evidence, receipts, and release

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Package helpers may transform in-memory values under caller control. They must not secretly write anywhere under `data/` or `release/`.

| Artifact | Package may | Package may not |
|---|---|---|
| `EvidenceRef` | Preserve existing ref. | Claim resolution/sufficiency. |
| `EvidenceBundle` | Preserve ref or consume caller-supplied verified status. | Create closure or proof authority. |
| Validation result | Return local structural issues. | Claim repository-wide validation or promotion. |
| Aggregation metadata | Return method/parameters/digest candidates. | Mint `AggregationReceipt`. |
| Receipt fields | Return value components. | Emit authoritative receipt identity/persistence. |
| Release ref | Preserve supplied ref. | Approve, publish, correct, withdraw, or roll back. |

Public clients must receive only governed runtime/release outputs after evidence, policy, review, and release gates.

[Back to top](#top)

---

## 15. Proposed source-tree evolution

### Phase 0 — scaffold

```text
src/
└── agriculture/
    ├── README.md
    └── __init__.py
```

### Phase 1 — packaging/import proof

```text
src/agriculture/
├── __init__.py
├── _version.py          # PROPOSED
└── _internal/
    └── __init__.py      # PROPOSED
```

Require build backend, package discovery, Python policy, clean import, no-network/no-write proof.

### Phase 2 — pure native-value helpers

```text
src/agriculture/
├── crop_mapping.py      # PROPOSED
├── time_kinds.py        # PROPOSED
├── source_values.py     # PROPOSED
└── issues.py            # PROPOSED
```

No canonical object construction or disclosure decision.

### Phase 3 — field/aggregation candidates

```text
src/agriculture/
├── field_candidate.py       # PROPOSED
└── aggregation_support.py   # PROPOSED
```

Require accepted identity profile, uncertainty, geometry/operator safety tests, and explicit non-approval results.

### Phase 4 — schema adapters

```text
src/agriculture/adapters/
├── README.md                # PROPOSED
└── <accepted_family>.py     # PROPOSED
```

Require accepted contract/schema, one canonical path, provenance, fixtures, validator/CI, compatibility, rollback.

Implement one low-risk aggregate helper before broad object-family coverage.

[Back to top](#top)

---

## 16. Generated code and schema adapters

Generated code requires a record of generator/version, source schema path/digest, contract path, output path/digest, generation time, reviewers, and rollback ref.

It must be reproducible, tied to one accepted schema, covered by fixtures/import tests, free of policy/source secrets, and correctable.

Because Agriculture contract/schema pairing remains unresolved, generated canonical models are currently **PROPOSED / BLOCKED**.

[Back to top](#top)

---

## 17. Tests and fixtures

Use the existing domain roots rather than creating parallel `tests/packages/...` or `fixtures/packages/...` homes by symmetry.

Existing tests include README-backed lanes for aggregate-only, catalog closure, policy deny, rollback drill, schema, soil moisture, SSURGO lineage, and vegetation-index context.

Existing fixtures include valid/invalid, field-level attempts, no-network, NASS-shaped aggregates, HLS, SSURGO, soil-moisture, golden, catalog, and release-shaped lanes.

Exact package-helper sublane names remain **PROPOSED / NEEDS VERIFICATION**.

Minimum behavior tests:

- clean side-effect-free import;
- empty API baseline;
- native-value preservation;
- source-role and time-kind preservation;
- candidate-only output;
- field uncertainty and operator safety;
- aggregation non-approval;
- no hidden lifecycle writes;
- refusal of unresolved schema authority;
- other-domain ownership preservation;
- resource limits;
- correction/supersession.

Fixtures must be synthetic/minimized, deterministic, no-network, free of real restricted geometry/operator identity, explicit about source role/time, and tied to expected results.

[Back to top](#top)

---

## 18. Packaging, installation, and CI gates

Before build/install claims:

- add `[build-system]`;
- configure `src/agriculture` discovery;
- declare supported Python range and dependencies;
- define versioning, wheel/sdist, license/readme metadata;
- prove secrets/fixtures/lifecycle data are excluded.

Future clean-environment checks:

```bash
python -m build
python -m pip install --no-deps dist/*.whl
python -c "import agriculture"
pytest tests/domains/agriculture
```

These are proposed until metadata/tooling are accepted.

The current `domain-agriculture` workflow only echoes TODO messages. Replace it with real build/import/no-network/domain-test/fixture/sensitivity/drift/rollback checks before using workflow success as implementation evidence.

[Back to top](#top)

---

## 19. Security and observability

Never log or expose exact restricted geometry, operator/private business identifiers, parcel-owner joins, credentials, signed URLs, embargoed excerpts, or sensitive quarantine reasons.

Errors should be finite, structured, safe, and distinct from policy/runtime outcomes.

Proposed local issue categories:

```text
MISSING_INPUT
MALFORMED_INPUT
UNSUPPORTED_VALUE
AMBIGUOUS_MAPPING
SOURCE_ROLE_MISSING
TIME_KIND_MISSING
IDENTITY_PROFILE_MISSING
SCHEMA_AUTHORITY_CONFLICT
RIGHTS_CONTEXT_MISSING
SENSITIVITY_CONTEXT_MISSING
FIELD_EXPOSURE_BLOCKED
OPERATOR_EXPOSURE_BLOCKED
RESOURCE_LIMIT_EXCEEDED
INTERNAL_ERROR
```

Metrics must avoid field IDs, operator IDs, geometry, URLs, source record IDs, or free-text error labels.

[Back to top](#top)

---

## 20. Compatibility, correction, and rollback

`0.0.0` implies no stable API, but changes still require intentional compatibility.

- avoid silent behavior changes;
- version mappings/crosswalks;
- preserve source-native lineage;
- document breaking changes;
- do not preserve unsafe exact disclosure for compatibility.

When mapping/vocabulary/identity/schema/aggregation changes, retain prior version refs, record reason, identify affected outputs/consumers, add regression fixtures, preserve historical evidence/receipts, and re-evaluate public/release outputs.

Rollback on sensitive disclosure, silent source-role/time/native-value changes, non-deterministic identity, implicit schema selection, unexpected lifecycle writes, broken consumers, or unreproducible generated code.

Documentation rollback: close the draft PR or revert its commit.

[Back to top](#top)

---

## 21. Validation commands

```bash
find packages/domains/agriculture -maxdepth 5 -type f -print | sort

find tests/domains/agriculture fixtures/domains/agriculture \
  -maxdepth 6 -type f -print | sort

find contracts/domains/agriculture \
     schemas/contracts/v1/domains/agriculture \
     policy/domains/agriculture \
  -maxdepth 6 -type f -print | sort

git grep -nE '(^|[[:space:]])(from|import)[[:space:]]+agriculture([[:space:].]|$)'
git grep -nE 'packages/domains/agriculture|src/agriculture' -- \
  apps connectors pipelines tools tests
```

These inspect; they do not prove passing implementation. Required CI commands must fail closed without `|| true`.

[Back to top](#top)

---

## 22. Definition of done

This README revision is done when:

- [x] Python distribution and `src` layout are confirmed;
- [x] source root and import package responsibilities are separated;
- [x] empty initializer and absent helper implementation are stated;
- [x] child-module v0.2 is linked;
- [x] authority roots remain separate;
- [x] native values, source roles, time kinds, uncertainty, and cross-lane ownership are protected;
- [x] field/operator detail remains denied by default;
- [x] tests/fixtures point to existing domain roots;
- [x] schema/contract drift blocks generated canonical adapters;
- [x] TODO workflow is not enforcement proof;
- [x] compatibility, correction, and rollback are defined;
- [x] no implementation maturity is overstated.

Implementation-ready requires accepted packaging, clean build/install/import, intentional exports, one narrow helper, positive/negative domain tests and fixtures, no-network/no-write proof, resolved schema authority, consumer inventory, compatibility/rollback, and real CI.

[Back to top](#top)

---

## 23. Open verification register

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-AG-SRC-001` | Which build backend and package discovery own the `src` layout? | UNKNOWN |
| `PKG-DOM-AG-SRC-002` | Which Python versions and dependencies are supported? | UNKNOWN |
| `PKG-DOM-AG-SRC-003` | Which symbols become first public exports? | PROPOSED owner decision |
| `PKG-DOM-AG-SRC-004` | Which consumers currently import this package? | NOT OBSERVED |
| `PKG-DOM-AG-SRC-005` | Which reviewed test sublane holds package-helper tests? | NEEDS VERIFICATION |
| `PKG-DOM-AG-SRC-006` | Which fixture lanes should package tests reuse/extend? | NEEDS VERIFICATION |
| `PKG-DOM-AG-SRC-007` | Which object contracts are field-complete and accepted? | UNKNOWN |
| `PKG-DOM-AG-SRC-008` | Which schema path is canonical per family? | CONFLICTED |
| `PKG-DOM-AG-SRC-009` | When is `AggregationReceipt` ready for an adapter? | CONFLICTED |
| `PKG-DOM-AG-SRC-010` | What identity profile governs field candidates/local keys? | UNKNOWN |
| `PKG-DOM-AG-SRC-011` | Which aggregation/generalization methods may helpers calculate? | UNKNOWN |
| `PKG-DOM-AG-SRC-012` | Which policy outcomes/obligations are accepted at runtime? | CONFLICTED / UNKNOWN |
| `PKG-DOM-AG-SRC-013` | Which real CI workflow proves package boundaries? | UNKNOWN |
| `PKG-DOM-AG-SRC-014` | What is the first low-risk governed consumer? | PROPOSED |
| `PKG-DOM-AG-SRC-015` | What rollback target applies after first public export? | NEEDS VERIFICATION |

[Back to top](#top)

---

## 24. Evidence ledger

| Evidence | Blob / ref | Supports | Limitation |
|---|---|---|---|
| Previous source-root README | `f531039d607b1ce77a6e7d1a9f7c48d5462c7067` | Existing v0.1 boundaries/stale questions. | Planning-era claims. |
| [`../pyproject.toml`](../pyproject.toml) | `9ff43f0defdfe0f6fed9fc565ee44154111bf547` | Python name/version. | No build/dependency config. |
| `agriculture/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | Import package exists/empty. | Not full tree proof. |
| [`agriculture/README.md`](./agriculture/README.md) | `36a26e8ae705b60db11d4d536f36994d4ae7ed82` | Helper boundary and bounded missing paths. | No executable proof. |
| [`../README.md`](../README.md) | `dd2fc20db17e18478d9135cd5105b8695fbbfee1` | Parent helper/sensitivity posture. | Stale implementation uncertainty. |
| [`docs/domains/agriculture/README.md`](../../../../docs/domains/agriculture/README.md) | `a2cac517ad26ea9105d46b5a7472de25cb35da2b` | Domain scope/object families/public posture. | Implementation remains proposed. |
| [`contracts/domains/agriculture/README.md`](../../../../contracts/domains/agriculture/README.md) | `27e6b7648d416e0c01da63c339210f9b072a98c5` | Semantic authority/compatibility conflict. | Object coverage incomplete. |
| [`schemas/contracts/v1/domains/agriculture/README.md`](../../../../schemas/contracts/v1/domains/agriculture/README.md) | `35d28a2c767a2e932572656c0f93727ceb18a541` | Schema lane/alias/aggregation scaffold. | No complete schema/validator proof. |
| [`policy/domains/agriculture/README.md`](../../../../policy/domains/agriculture/README.md) | `ba73c387e16f70895f32444e489d6d55dd577b75` | Fail-closed policy intent. | Runtime enforcement unknown. |
| [`tests/domains/agriculture/README.md`](../../../../tests/domains/agriculture/README.md) | `35ebf2a578f2a39b4f4766cc4146aafde8124e67` | Existing test root/lanes. | Modules/results unverified. |
| [`fixtures/domains/agriculture/README.md`](../../../../fixtures/domains/agriculture/README.md) | `68660dfb8e64dc39a146964866f4ddcec36d6e1e` | Existing fixture root/public-safe posture. | Payload/wiring incomplete. |
| [`docs/doctrine/directory-rules.md`](../../../../docs/doctrine/directory-rules.md) | `2affb080e6f0043867c64c7f06c1ca52030fbd55` | Responsibility-root separation. | No implementation proof. |
| [`.github/workflows/domain-agriculture.yml`](../../../../.github/workflows/domain-agriculture.yml) | `a9f5f212ef61d72fdc209d9f8b173bbf87fb1803` | Workflow is echo-only. | No enforcement. |
| Detailed Agriculture evidence snapshot | `98b39c7171129b90ca858e2e3849ed121c0d7769` | Commit-pinned package/domain inspection context. | No runtime/release execution. |
| Review-branch base | `14b59b6b84ee2b9fa46e002b60e922c97cab2761` | Target blob rechecked unchanged; intervening changes were unrelated. | Does not add Agriculture implementation evidence. |

[Back to top](#top)

---

## 25. Maintainer checklist

- [ ] Confirm the change is reusable package implementation.
- [ ] Read parent and child READMEs.
- [ ] Preserve doctrine, contract, schema, policy, test, fixture, data, and release roots.
- [ ] Keep imports side-effect free.
- [ ] Keep network/lifecycle IO caller-owned.
- [ ] Preserve native values, source role, time kinds, uncertainty, and cross-lane ownership.
- [ ] Treat outputs as candidates unless governed contracts say otherwise.
- [ ] Deny exact field/operator exposure by default.
- [ ] Do not mint EvidenceBundles, PolicyDecisions, AggregationReceipts, ReleaseManifests, or lifecycle records.
- [ ] Reuse Agriculture domain test/fixture roots.
- [ ] Do not generate canonical models from scaffold/conflicted schemas.
- [ ] Add negative-first tests before exports.
- [ ] Declare dependencies/Python versions before third-party imports.
- [ ] Add compatibility/rollback notes for API changes.
- [ ] Keep secrets, real restricted geometry, and operator IDs out of source/fixtures.
- [ ] Mark unverified behavior honestly.
- [ ] Do not present TODO workflow success as proof.

## Status summary

`packages/domains/agriculture/src/` is a **confirmed Python source-root scaffold** with one empty import package and a repository-grounded child-module contract. It is not yet an implemented or installable Agriculture library. The next sound change is a small packaging/import-safety slice followed by one pure, native-value-preserving helper with domain-root tests and synthetic fixtures.

<p align="right"><a href="#top">Back to top</a></p>
