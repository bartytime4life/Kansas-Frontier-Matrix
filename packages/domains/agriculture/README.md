<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-agriculture-readme
title: Governed Agriculture Domain Helper Package
type: readme
version: v0.2
status: draft; repository-grounded; python-package-scaffold
owners:
  - OWNER_TBD — Agriculture package and domain steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Policy, rights, and sensitivity steward
  - OWNER_TBD — Evidence and release steward
  - OWNER_TBD — Validation, security, and docs steward
created: 2026-06-13
updated: 2026-07-14
supersedes: v0.1 (2026-06-13)
policy_label: public; packages; agriculture; python; source-role-aware; no-network; field-level-deny-by-default; non-authoritative
path: packages/domains/agriculture/README.md
truth_posture: CONFIRMED target and prior blob, package name/version, Python src layout, source-root and child-module v0.2 contracts, empty agriculture initializer, domain contract/schema/policy/test/fixture indexes, Directory Rules v1.4, proposed ADR-0001, and echo-only domain workflow / PROPOSED future reusable mapping, normalization, candidate-DTO, identity, temporal, aggregation-support, validation-adapter, and generated-type APIs / CONFLICTED contract/schema compatibility paths, AggregationReceipt pairing and naming, policy-versus-runtime outcome vocabulary, and package-specific versus domain test/fixture path assumptions / UNKNOWN build backend, Python requirement, dependencies, public exports, consumers, executable helpers, package validators, meaningful CI enforcement, runtime wiring, receipts, evidence closure, release integration, and production behavior
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 266dfb53f4a144940fc3c094b852605dcc2e9356
  prior_blob: dd2fc20db17e18478d9135cd5105b8695fbbfee1
related:
  - ./pyproject.toml
  - ./src/README.md
  - ./src/agriculture/README.md
  - ./src/agriculture/__init__.py
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/agriculture/README.md
  - ../../../contracts/domains/agriculture/README.md
  - ../../../schemas/contracts/v1/domains/agriculture/README.md
  - ../../../policy/domains/agriculture/README.md
  - ../../../tests/domains/agriculture/README.md
  - ../../../fixtures/domains/agriculture/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../.github/workflows/domain-agriculture.yml
tags: [kfm, packages, domains, agriculture, python, package-boundary, bounded-context, candidate-dto, source-role, identity, time-kinds, aggregation, public-safety, evidence, rollback]
notes:
  - "v0.2 replaces planning-oriented package language with a commit-pinned description of the current kfm-domain-agriculture 0.0.0 Python scaffold."
  - "The detailed source-root and import-module boundaries live in src/README.md and src/agriculture/README.md."
  - "The package may support candidate preparation and pure helpers; it cannot admit sources, decide truth or policy, write lifecycle state, close evidence, approve release, or serve public clients."
  - "Field-, operator-, private-parcel-, and rights-limited detail remains deny-by-default for public use."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Agriculture Domain Helper Package

`packages/domains/agriculture/`

> Shared Python package boundary for reusable Agriculture helpers. The current repository surface is a **greenfield `0.0.0` scaffold**, not an implemented library: project metadata is minimal, the import-package initializer is empty, and no public exports, dependencies, consumers, build backend, or executable helper modules are established by the inspected evidence.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-1f6feb)
![distribution](https://img.shields.io/badge/distribution-kfm--domain--agriculture-3776ab)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![sensitivity](https://img.shields.io/badge/field%20%2F%20operator-deny%20by%20default-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose-and-audience) · [Status](#current-repository-state) · [Context](#bounded-context-and-ubiquitous-language) · [Ownership](#owned-responsibilities) · [Non-ownership](#explicit-non-ownership) · [Interfaces](#internal-and-public-interface-boundary) · [Objects](#agriculture-object-family-boundary) · [Dependencies](#dependency-direction) · [Identity](#identity-and-temporal-handling) · [Trust](#trust-membrane-lifecycle-and-public-safety) · [Validation](#validation-tests-fixtures-and-ci) · [Evolution](#implementation-admission-and-package-evolution) · [Rollback](#compatibility-correction-and-rollback) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Repository snapshot:** `main@266dfb53f4a144940fc3c094b852605dcc2e9356`<br>
> **Distribution:** `kfm-domain-agriculture`<br>
> **Declared version:** `0.0.0`<br>
> **Verified implementation container:** `src/`<br>
> **Verified import package:** `src/agriculture/`<br>
> **Verified executable state:** empty `src/agriculture/__init__.py`; no supported public API established<br>
> **Domain CI:** three echo-only jobs; workflow success is not implementation or publication proof

> [!CAUTION]
> A parsed crop code is not a `CropObservation`. A geometry-derived key is not a confirmed field. A yield adapter is not yield truth. A suitability score is not a land-use decision. An aggregation helper is not an `AggregationReceipt`, redaction approval, EvidenceBundle, PolicyDecision, PromotionDecision, or ReleaseManifest.

---

## Purpose and audience

`packages/domains/agriculture/` is the package-level boundary for reusable, source-agnostic Agriculture implementation support.

A mature package may provide deterministic or side-effect-minimal helpers for:

- preserving source-native crop codes, labels, identifiers, units, geometry references, and timestamps;
- mapping governed input records into **candidate** Agriculture DTOs;
- normalizing yield, crop rotation, irrigation, conservation, suitability, stress, and economic context;
- preserving source role, rights posture, sensitivity labels, uncertainty, limitations, and distinct time kinds;
- preparing deterministic local candidate keys under an accepted identity profile;
- preparing aggregation, generalization, redaction, or suppression candidates from caller-authorized policy inputs;
- adapting candidate objects to accepted contracts and schemas;
- returning explicit issue and finite-result structures;
- supporting deterministic, synthetic, no-network tests.

The package is for:

- Agriculture package and domain maintainers;
- governed application, pipeline, worker, tool, and validator authors;
- contract, schema, policy, evidence, release, and source-registry stewards;
- privacy, rights, sensitivity, and security reviewers;
- maintainers deciding whether proposed logic belongs in a shared package, source connector, pipeline, validator, policy lane, or application.

The package must not fetch live sources, admit data, write lifecycle state, decide source authority, make Agriculture claims true, resolve evidence closure, approve release, or serve as the public trust membrane.

[Back to top](#top)

---

## Current repository state

### Verified package surface

The following surface is verified at the evidence snapshot. It is a bounded inventory, not a claim that no unindexed or empty file can exist elsewhere.

```text
packages/domains/agriculture/
├── README.md
├── pyproject.toml
└── src/
    ├── README.md
    └── agriculture/
        ├── README.md
        └── __init__.py
```

| Surface | Evidence | Status | Consequence |
|---|---|---|---|
| This README | Existing planning-oriented v0.1 at blob `dd2fc20d...`. | **CONFIRMED** | Revised in place; prior content remains recoverable in Git history. |
| [`pyproject.toml`](./pyproject.toml) | Contains only `[project]`, name `kfm-domain-agriculture`, and version `0.0.0`. | **CONFIRMED minimal placeholder** | Distribution identity is known; build/install behavior is not. |
| [`src/README.md`](./src/README.md) | Repository-grounded v0.2 source-root contract. | **CONFIRMED** | Owns source layout, imports, dependency direction, generated code, and test-placement boundaries. |
| [`src/agriculture/README.md`](./src/agriculture/README.md) | Repository-grounded v0.2 import-module contract. | **CONFIRMED** | Owns detailed helper semantics, finite results, object adapters, identity/time, and public-safety guidance. |
| `src/agriculture/__init__.py` | Exists and is empty. | **CONFIRMED** | Import-package marker only; no public exports are established. |
| Build backend | No `[build-system]` section is present in the inspected project file. | **NOT OBSERVED** | Wheel/sdist construction and editable-install behavior remain unknown. |
| Dependencies | No project dependency list is present in the inspected project file. | **NOT OBSERVED** | Runtime and compatibility claims are unsupported. |
| Supported Python | No `requires-python` field is present. | **NOT OBSERVED** | Supported interpreter range is unknown. |
| Executable helpers | Exact checks documented by the child-module review did not find `core.py`, `crop.py`, `field_identity.py`, or `aggregation.py`. | **CONFIRMED bounded absence** | Do not claim helper implementation. |
| Consumers | Indexed searches did not establish imports or runtime consumers. | **NOT OBSERVED / search-limited** | Production integration remains unknown. |
| Domain contracts | Agriculture semantic-contract index exists; object-level coverage is incomplete and a compatibility path also exists. | **CONFIRMED index / CONFLICTED placement** | Code generation and stable DTO promises are blocked pending authority resolution. |
| Domain schemas | Agriculture schema index exists; current known schema coverage is scaffold-level and a shorter alias lane exists. | **CONFIRMED index / incomplete** | Do not treat generated shapes as canonical. |
| Domain policy | Agriculture policy README exists; executable policy files and enforcement remain unverified. | **CONFIRMED index / UNKNOWN enforcement** | Package code cannot make policy decisions. |
| Domain tests | README-backed Agriculture test lanes exist under `tests/domains/agriculture/`. | **CONFIRMED documentation / execution unknown** | Use the established domain test root unless an accepted package-test convention says otherwise. |
| Domain fixtures | README-backed Agriculture fixture lanes exist under `fixtures/domains/agriculture/`. | **CONFIRMED documentation / partial inventory** | Reuse synthetic governed fixtures; do not create an ungoverned parallel fixture home. |
| Domain workflow | `.github/workflows/domain-agriculture.yml` runs three `echo TODO` jobs. | **CONFIRMED scaffold** | A green check does not prove validation, proof construction, or publication readiness. |
| Runtime and release | No build artifact, package publication, emitted receipt, resolved EvidenceBundle, deployed consumer, runtime log, or release record was inspected. | **UNKNOWN** | This README is not implementation or release proof. |

```text
distribution identity        = CONFIRMED
source layout                = CONFIRMED
import package               = CONFIRMED
empty initializer            = CONFIRMED
public exports               = NOT ESTABLISHED
implemented helpers          = NOT OBSERVED
build backend                = UNKNOWN
dependencies                 = UNKNOWN
supported Python versions    = UNKNOWN
consumers                    = NOT OBSERVED
test/fixture documentation   = CONFIRMED
test execution               = UNKNOWN
policy enforcement           = UNKNOWN
runtime/release integration  = UNKNOWN
```

[Back to top](#top)

---

## Bounded context and ubiquitous language

### Bounded context

The package bounded context is:

> Reusable Agriculture helper implementation that preserves governed input meaning and prepares typed candidates without acquiring source, truth, policy, evidence, lifecycle, review, or release authority.

The package boundary includes:

- distribution and source-layout organization;
- package exports and compatibility promises;
- pure mapping, normalization, crosswalk, temporal, identity, and aggregation-support helpers;
- candidate DTO and local result structures;
- package-level dependency and import discipline;
- generated-adapter admission;
- no-network package validation.

It excludes:

- external source retrieval and admission;
- canonical Agriculture object meaning or machine shape;
- source rights and authority decisions;
- crop, field, yield, operator, parcel, irrigation-right, or suitability truth;
- lifecycle orchestration and persistence;
- policy evaluation and sensitivity approval;
- EvidenceRef-to-EvidenceBundle closure;
- authoritative receipt emission;
- release, correction, withdrawal, and rollback decisions;
- governed API, map, UI, or AI delivery.

### Ubiquitous language

| Term | Meaning at this package boundary | Must not be confused with |
|---|---|---|
| Distribution | The installable project identity `kfm-domain-agriculture`. | Import package, domain doctrine, or released artifact. |
| Import package | Python module namespace `agriculture` under `src/`. | Agriculture domain authority. |
| Helper | Reusable pure or side-effect-minimal function supporting a governed caller. | Connector, pipeline, policy evaluator, or release service. |
| Candidate DTO | Locally prepared object awaiting canonical validation, evidence, policy, lifecycle, and review gates. | Confirmed record, published claim, or released API payload. |
| Native value | Source-provided code, label, unit, identifier, geometry reference, or timestamp. | Normalized value or canonical identity. |
| Crosswalk | Versioned mapping from native classification to a target classification with confidence and unresolved states. | Evidence that the target classification is true. |
| Field candidate | Potential field or management-unit identity with provenance and ambiguity. | Parcel, ownership, operator identity, or confirmed field. |
| Local key | Deterministic implementation key used inside an accepted profile. | Canonical identifier unless the owning contract explicitly says so. |
| Aggregation candidate | Proposed grouping or suppression result plus transform metadata. | Approved public-safe release or `AggregationReceipt`. |
| Issue | Structured missing, malformed, ambiguous, conflicted, stale, restricted, or unsupported condition. | PolicyDecision unless a governed policy layer maps it. |
| Evidence reference | Pointer preserved from governed input. | Evidence closure or permission to disclose the referenced content. |

The package must use Agriculture terms consistently with domain doctrine and semantic contracts. It must not silently invent alternate meanings in code.

[Back to top](#top)

---

## Owned responsibilities

The package may own reusable implementation support for these responsibilities.

| Responsibility | Package obligation |
|---|---|
| Native-value preservation | Keep source-provided and normalized fields distinct and retain source identity and role. |
| Mapping and normalization | Normalize approved codes, enums, dates, units, and optional fields without deleting caveats or uncertainty. |
| Candidate DTO preparation | Produce schema-ready candidates for a governed caller without claiming schema or truth authority. |
| Candidate identity support | Compute deterministic local keys only under an accepted identity profile and version. |
| Temporal sequencing | Order observations and crop rotations while preserving gaps, conflicts, and distinct time kinds. |
| Unit conversion | Record input unit, output unit, conversion profile/version, precision, and assumptions. |
| Crosswalk support | Return mapped, unresolved, ambiguous, deprecated, or conflicted states explicitly. |
| Aggregation support | Prepare grouping, threshold, suppression, and transform metadata without deciding admissibility. |
| Redaction/generalization support | Apply an already authorized transform profile supplied by a governed caller; never select policy implicitly. |
| Validation adapters | Invoke accepted schema/validator tooling and return structured results without redefining canonical rules. |
| Receipt-ready metadata | Return method/version, input/output digest candidates, issue codes, and transform summaries for caller-owned receipts. |
| Test support | Provide deterministic synthetic builders or utilities when the accepted fixture convention permits them. |
| Compatibility | Preserve explicit migration adapters and deprecation windows when public package APIs eventually exist. |

A package helper may make governed work reproducible. It does not make the resulting claim authoritative.

[Back to top](#top)

---

## Explicit non-ownership

| Responsibility | Owning surface | Package posture |
|---|---|---|
| Agriculture doctrine, scope, and public framing | [`docs/domains/agriculture/`](../../../docs/domains/agriculture/README.md) | Consume; do not redefine. |
| Agriculture object meaning | [`contracts/domains/agriculture/`](../../../contracts/domains/agriculture/README.md) or accepted contract home | Consume; do not invent fields as canonical. |
| Machine-checkable Agriculture shape | [`schemas/contracts/v1/domains/agriculture/`](../../../schemas/contracts/v1/domains/agriculture/README.md) under proposed ADR-0001 | Consume accepted versions; do not create parallel schemas. |
| Agriculture admissibility and sensitivity policy | [`policy/domains/agriculture/`](../../../policy/domains/agriculture/README.md) and shared policy roots | Supply context; do not decide. |
| Source identity, role, rights, cadence, and activation | Source descriptors and registries | Preserve refs; do not admit sources. |
| Source acquisition | `connectors/` | No hidden network or direct source fetching. |
| Executable transformations and lifecycle movement | `pipelines/domains/agriculture/`, `pipeline_specs/agriculture/`, and authorized workers/tools | Return candidates; do not persist or promote. |
| Lifecycle records | `data/raw/`, `work/`, `quarantine/`, `processed/`, `catalog/`, `triplets/`, and `published/` | No hidden writes. |
| Receipts and proofs | Governed receipt/proof homes | Return receipt-ready metadata only. |
| Evidence closure | EvidenceRef/EvidenceBundle systems | Preserve references; never fabricate closure. |
| Release, correction, withdrawal, and rollback | `release/` and accepted records | Reference state; never authorize. |
| Public API, map, UI, or AI behavior | Governed apps and runtime packages | No independent public interface. |
| Secrets, credentials, source caches, or private payloads | Deployment secret stores and governed lifecycle paths | Forbidden in this package. |

### Package anti-collapse rules

```text
package presence                 != implemented Agriculture capability
empty import package             != supported public API
candidate DTO                    != canonical record
normalized crop code             != CropObservation truth
field candidate                  != parcel / ownership / operator truth
yield adapter                    != YieldObservation truth
irrigation relation              != water right or permit
suitability candidate            != land-use decision authority
aggregation candidate            != public-safe approval
schema pass                      != evidence closure
test pass                        != lifecycle promotion
workflow success                 != publication readiness
merge                            != KFM PUBLISHED
```

[Back to top](#top)

---

## Internal and public interface boundary

### Internal interface

A future package API should remain small, typed, deterministic, and reviewable.

```python
from dataclasses import dataclass
from enum import Enum
from typing import Generic, Mapping, Sequence, TypeVar

T = TypeVar("T")

class IssueKind(str, Enum):
    MISSING = "missing"
    MALFORMED = "malformed"
    AMBIGUOUS = "ambiguous"
    CONFLICTED = "conflicted"
    STALE = "stale"
    RESTRICTED = "restricted"
    UNSUPPORTED = "unsupported"

@dataclass(frozen=True)
class AgricultureIssue:
    kind: IssueKind
    code: str
    message: str
    source_ref: str | None = None
    field: str | None = None

@dataclass(frozen=True)
class AgricultureResult(Generic[T]):
    value: T | None
    issues: Sequence[AgricultureIssue]
    source_refs: Sequence[str]
    evidence_refs: Sequence[str]
    metadata: Mapping[str, object]
```

**Status:** `PROPOSED`. No implementation, export, or accepted contract for these names is verified.

Expected properties:

- no import-time I/O;
- no network by default;
- no filesystem, database, graph, catalog, receipt, proof, or release writes;
- immutable or clearly copy-on-write result values;
- explicit issue states rather than silent coercion;
- source, evidence, policy, review, release, and correction references preserved when supplied;
- no hidden global state;
- deterministic behavior for identical pinned inputs and profiles;
- no sensitive value in exception text, logs, representation methods, or metrics.

### Public interface

This package has no independent public interface.

```text
public client
  -> governed API or released artifact
  -> policy-filtered, evidence-resolved response
  -> optional package-produced candidate metadata already admitted by the caller
```

The browser, MapLibre shell, Focus Mode, public API client, or export consumer must not import package internals or treat a package result as display permission.

[Back to top](#top)

---

## Package architecture and source layout

### Verified layout

```text
packages/domains/agriculture/
├── pyproject.toml
└── src/
    └── agriculture/
        └── __init__.py
```

The READMEs at each level form a documentation hierarchy:

| README | Responsibility |
|---|---|
| `packages/domains/agriculture/README.md` | Distribution/package boundary, ownership, interfaces, dependencies, validation, compatibility, and admission. |
| `packages/domains/agriculture/src/README.md` | Source-root, import-layout, generated-code, dependency-direction, and test-placement boundary. |
| `packages/domains/agriculture/src/agriculture/README.md` | Import-module helper semantics, object adapters, identity/time handling, finite results, and detailed safety rules. |

### Proposed future layout

```text
packages/domains/agriculture/
├── pyproject.toml
├── src/
│   └── agriculture/
│       ├── __init__.py
│       ├── result.py
│       ├── crop.py
│       ├── field_candidate.py
│       ├── rotation.py
│       ├── yield_observation.py
│       ├── irrigation.py
│       ├── conservation.py
│       ├── suitability.py
│       ├── economy.py
│       ├── stress.py
│       ├── aggregation.py
│       ├── validation.py
│       └── generated/
└── CHANGELOG.md
```

Every future path above is **PROPOSED**. Add a file only when a concrete consumer, accepted contract/schema or explicitly local-only interface, fixture/test family, and review owner justify it.

Do not add:

- parallel language implementations without an ADR or migration note;
- generated modules without generator provenance and drift checks;
- package-local source caches;
- embedded policy modules;
- emitted receipt/proof/release instances;
- examples containing field/operator/private-parcel detail;
- one-off workflow logic that belongs in `tools/` or `pipelines/`.

[Back to top](#top)

---

## Agriculture object-family boundary

The package may eventually adapt or prepare candidates for Agriculture's documented object families. It must preserve each family's authority and uncertainty.

| Object family | Safe helper role | Forbidden collapse |
|---|---|---|
| `CropObservation` | Preserve native and normalized crop classifications, source role, time, support, and confidence. | Mapping success becomes confirmed observation. |
| `FieldCandidate` | Canonicalize geometry input under an accepted precision profile and preserve candidate lineage and ambiguity. | Candidate becomes parcel, owner, operator, or confirmed field. |
| `CropRotation` | Order source-backed observations, preserve gaps and conflicts, and report sequence quality. | Missing years are imputed as fact. |
| `YieldObservation` | Normalize units and spatial/temporal support with conversion metadata. | Modeled or aggregate yield becomes direct observation. |
| `IrrigationLink` | Preserve governed links to Hydrology or source context. | Relation implies permit, water right, ownership, or lawful use. |
| `ConservationPractice` | Normalize practice codes and effective dates while preserving program/source authority. | Candidate becomes verified implementation or compliance record. |
| `SoilCropSuitability` | Prepare derived candidates with input refs, method version, scale, and uncertainty. | Score becomes recommendation or land-use authority. |
| `AgriculturalEconomyObservation` | Normalize aggregate geography, period, currency/unit, and source limitations. | Aggregate statistics reveal or infer private business performance. |
| `SupplyChainNode` | Prepare contextual identifiers and relation candidates. | Node becomes infrastructure, facility, or company authority. |
| `DroughtStressIndicator` | Prepare derived indicator candidates with method and cross-lane refs. | Indicator becomes emergency warning or direct crop observation. |
| `PestStressIndicator` | Preserve method, taxonomy/source refs, and confidence. | Indicator becomes confirmed infestation or treatment advice. |
| `AggregationReceipt` | Prepare transform metadata, digests, thresholds, suppressed fields, and reason candidates. | Package authorizes or emits the authoritative receipt or release. |

### Cross-lane ownership

- Soil owns soil map-unit, component, horizon, hydrologic-group, and soil-property truth.
- Hydrology owns streamflow, water level, groundwater, flood, and water-measurement truth.
- Atmosphere owns weather, climate, smoke, and atmospheric-observation truth.
- Hazards owns hazard-event, warning-context, declaration, and emergency-context truth.
- People/DNA/Land owns people, parcel, ownership, consent, and private-join truth.
- Flora and Fauna own taxonomic and occurrence truth.
- Agriculture may cite or transform bounded references; it must not absorb another lane's canonical meaning.

[Back to top](#top)

---

## Inputs and outputs

### Accepted input classes

A package function may accept already admitted, caller-supplied values such as:

| Input class | Required context |
|---|---|
| Source-native record fragment | Source ID, role, native identifiers, retrieval/source time, rights/sensitivity labels when applicable. |
| Candidate Agriculture DTO | Object family, schema/contract version or explicit local-only status, source/evidence refs, lifecycle status supplied by caller. |
| Crosswalk profile | Profile ID/version, native/target vocabularies, mapping status, deprecation state, confidence rules. |
| Identity profile | Profile ID/version, normalization and hashing recipe, collision behavior, scope. |
| Temporal profile | Named time kinds, timezone/calendar rules, interval semantics, missing/conflict behavior. |
| Aggregation/redaction profile | Caller-authorized policy/profile ID, threshold/suppression rules, audience, spatial and temporal support. |
| Validation context | Accepted schema/validator ref, mode, strictness, expected issue vocabulary. |

The package must not fetch missing context from the network, canonical stores, private databases, or hidden configuration.

### Permitted output classes

- candidate DTO;
- normalized value with native value preserved;
- crosswalk result with mapped/unresolved/ambiguous/conflicted status;
- deterministic local key candidate;
- validation finding;
- aggregation/redaction candidate;
- issue list;
- receipt-ready transform metadata;
- deprecation or migration warning.

### Forbidden output claims

The package must not return an object labeled or treated as:

- confirmed truth solely because mapping succeeded;
- source-admitted solely because it has a source ID;
- evidence-closed solely because it has an EvidenceRef;
- policy-approved solely because a value was suppressed;
- released solely because a manifest reference is present;
- public-safe solely because a field is omitted from one representation;
- published solely because a commit, pull request, or package version exists.

[Back to top](#top)

---

## Dependency direction

### Allowed direction

```text
accepted contracts / schemas / profiles
  -> generated or handwritten package adapters
  -> candidate results + issues + preserved references
  -> governed caller
  -> validation + evidence + policy + lifecycle + review + release
```

### Forbidden direction

```text
package
  -> connector or live-source fetch
  -> direct RAW / WORK / QUARANTINE / PROCESSED / CATALOG / PUBLISHED write
  -> direct policy or release decision
  -> EvidenceBundle fabrication
  -> browser or public API serving
```

### Dependency classes

| Dependency class | Rule |
|---|---|
| Python standard library | Preferred for first pure helpers when sufficient. |
| Shared KFM package | Must have a clear boundary, version/compatibility posture, and no circular authority dependency. |
| Third-party runtime dependency | Requires package metadata, license/security review, pinned compatibility policy, tests, and rollback. |
| Contract/schema-generated code | Requires accepted source path, generator identity/version, deterministic output, drift test, and no hand edits. |
| Policy runtime | Package may prepare inputs but must not embed or silently invoke policy as ordinary normalization. |
| Database/network client | Forbidden in the default helper package unless an accepted architecture decision explicitly changes the boundary. |
| Application/UI dependency | Forbidden. Shared package code must not depend on deployable application internals. |

No dependency is established merely because this README describes it.

[Back to top](#top)

---

## Identity and temporal handling

### Identity

A helper may compute a local candidate key only when the recipe is explicit.

```text
candidate_key = hash(
  identity_profile_version
  + source_id
  + source_native_id
  + object_family
  + normalized_spatial_support
  + normalized_temporal_support
)
```

This formula is illustrative and **PROPOSED**, not a canonical identity contract.

Required behavior:

- preserve native IDs separately from local keys;
- include identity-profile version;
- expose collisions, missing inputs, and unstable geometry;
- do not use names, operator identity, or approximate geometry as silent canonical identity;
- do not merge candidates merely because normalized keys match;
- never imply parcel, ownership, or operator identity;
- make recomputation and deprecation possible.

### Time kinds

Keep distinct where material:

| Time kind | Meaning |
|---|---|
| `source_time` | Time expressed by the source. |
| `observed_time` | Time the phenomenon was observed or measured. |
| `valid_time` | Time interval the assertion or candidate applies to. |
| `retrieval_time` | Time the source payload was obtained. |
| `processing_time` | Time a helper or pipeline transformed the value. |
| `release_time` | Time an authorized release became effective. |
| `correction_time` | Time a correction, supersession, or withdrawal was recorded. |

A package helper may normalize a supplied time. It must not invent missing observation dates, silently substitute retrieval time for observed time, or infer release state from filesystem location.

[Back to top](#top)

---

## Trust membrane, lifecycle, and public safety

### Lifecycle boundary

```text
PRE-RAW / source admission
  -> RAW
  -> WORK or QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> PUBLISHED
```

This package is not a lifecycle stage. It may be invoked by an authorized caller inside a stage, but it must not decide or persist stage transitions.

| Lifecycle concern | Package rule |
|---|---|
| Admission | Require caller-supplied admitted context; do not activate or fetch sources. |
| RAW preservation | Never overwrite or reinterpret source-native values without retaining lineage. |
| Work/quarantine | Return issues and candidate outputs; caller decides storage and quarantine reason. |
| Processed | Schema or helper success does not establish processed status. |
| Catalog/triplet | Package may prepare reference candidates; it cannot close catalog or graph authority. |
| Published | No package call authorizes publication or public display. |
| Receipts/proofs | Return metadata candidates; authoritative records remain caller-owned. |
| Correction/rollback | Preserve versions and inputs needed for replay; do not execute release rollback. |

### Field, operator, parcel, and rights safety

Public exact exposure is denied by default for:

- field polygons and precise management units;
- operator identity and owner/operator joins;
- private parcel-adjacent records;
- source-rights-limited values;
- small-cell or low-count aggregates vulnerable to re-identification;
- quarantine, candidate, or unreleased data;
- raw model output and unsupported inferred attributes.

A helper may apply an **already authorized** aggregation, suppression, redaction, or generalization profile. It must return:

- profile ID and version;
- input spatial and temporal support;
- output spatial and temporal support;
- threshold and suppression summary;
- removed or generalized field names;
- reason/obligation candidates;
- input/output digest candidates;
- residual-risk notes;
- source, evidence, policy, and review refs supplied by the caller.

It must not choose a public threshold by convenience, infer consent, convert omission into policy approval, or log restricted values.

### Public path

```text
package candidate
  -> authorized pipeline / service
  -> contract and schema validation
  -> EvidenceRef -> EvidenceBundle resolution
  -> rights and sensitivity policy
  -> review and release state
  -> released artifact / governed API
  -> map, UI, export, or bounded AI interpretation
```

Any shortcut from package internals to public clients violates the trust membrane.

[Back to top](#top)

---

## Contracts, schemas, policy, fixtures, and validators

| Surface | Current package relationship | Required future gate |
|---|---|---|
| Semantic contracts | Consume accepted Agriculture contracts; do not define object meaning in code alone. | Contract path, version, owner, review state, compatibility policy. |
| Machine schemas | Adapt to accepted field-complete schemas; ADR-0001 is currently proposed. | Canonical path, `$id`, dialect, fixtures, registry entry, validator. |
| Policy | Preserve policy input/output references and obligations; never decide locally. | Accepted input contract, evaluator binding, finite outcome normalization, negative tests. |
| Fixtures | Reuse `fixtures/domains/agriculture/` or add a documented reviewed sublane. | Synthetic/public-safe provenance, consumer mapping, valid/invalid/restricted cases. |
| Tests | Use `tests/domains/agriculture/` unless a package-specific lane is accepted. | Pure unit tests, boundary tests, import tests, property tests, integration contract tests. |
| Validators | Package may wrap pure validator functions but orchestration remains under validator tooling. | Exact validator path, version, deterministic result, fail-closed integration. |
| Evidence | Preserve EvidenceRefs; no closure. | Resolver and EvidenceBundle coverage. |
| Receipts | Return receipt-ready metadata only. | Authoritative emitter, schema, digest, storage, review. |
| Release | Read supplied release state where needed; no approval. | ReleaseManifest, correction path, rollback target, public-boundary test. |

### Known conflicts that code must not settle implicitly

- `contracts/domains/agriculture/` versus compatibility material under `contracts/agriculture/`;
- `schemas/contracts/v1/domains/agriculture/` versus the shorter `schemas/contracts/v1/agriculture/` index lane;
- `aggregation-receipt` versus `aggregation_receipt` naming and pairing;
- policy-lane outcomes such as `ALLOW`, `RESTRICT`, and `HOLD` versus canonical runtime response outcomes;
- package-specific test/fixture paths named by older planning docs versus current README-backed domain roots.

Resolve these through stewards, ADRs, drift/migration records, and cross-root validation—not through convenient imports or duplicate types.

[Back to top](#top)

---

## Finite failure outcomes

Package functions should return explicit local outcomes rather than silently guessing.

| Local outcome | Meaning | Required caller behavior |
|---|---|---|
| `VALUE` | Candidate value produced with preserved context. | Continue to canonical validation, evidence, policy, lifecycle, and review gates. |
| `MISSING` | Required input absent. | Supply context or abstain; do not invent. |
| `MALFORMED` | Input cannot satisfy the local adapter contract. | Reject or quarantine through the authorized caller. |
| `AMBIGUOUS` | More than one mapping or identity candidate remains. | Preserve candidates and route for resolution. |
| `CONFLICTED` | Sources, profiles, contracts, or versions disagree. | Stop the affected transform and surface the conflict. |
| `STALE` | Input/profile freshness requirement is not met. | Revalidate, narrow, or abstain. |
| `RESTRICTED` | Caller-supplied sensitivity/rights context blocks the requested local output. | Do not expose detail; route to policy/review. |
| `UNSUPPORTED` | Requested object, schema, profile, or operation is not implemented. | Return a bounded error; no fallback guess. |
| `ERROR` | Unexpected implementation or dependency failure. | Fail closed, record sanitized diagnostics, and avoid partial authority claims. |

These are package-local result states, not canonical runtime `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` envelopes and not policy decisions.

[Back to top](#top)

---

## Validation, tests, fixtures, and CI

### Minimum package validation

| Validation class | Required cases |
|---|---|
| Import safety | Import performs no network, filesystem write, database connection, environment mutation, or registration side effect. |
| Native-value preservation | Native and normalized values remain separately recoverable. |
| Crosswalk behavior | Mapped, missing, ambiguous, deprecated, conflicted, and unknown codes. |
| Identity | Stable recomputation, missing components, profile-version change, collision, and unstable geometry. |
| Temporal | Missing time, invalid interval, timezone/calendar edge, conflicting time kinds, sequence gaps. |
| Units | Valid conversion, unknown unit, precision loss, impossible value, versioned conversion profile. |
| Source role | Observation, model, estimate, aggregate, administrative, candidate, and synthetic roles remain distinct. |
| Object boundary | Candidate adapters cannot claim confirmed object status. |
| Sensitivity | Field/operator/private-parcel detail does not appear in output, logs, exceptions, or snapshots without authorized context. |
| Aggregation | Threshold boundary, low-count suppression, residual-risk metadata, and no release-approval flag. |
| Evidence | EvidenceRefs preserved; no fabricated EvidenceBundle or citation. |
| Lifecycle | Monkeypatched storage/network clients prove no hidden writes or fetches. |
| Determinism | Repeated pinned input/profile yields stable value, issues, and digest candidates. |
| Compatibility | Export changes, deprecations, and migration adapters are explicit once public API exists. |
| Security | Secret, path-traversal, oversized input, malicious label, and exception-redaction cases. |

### Fixture posture

Default package tests must be no-network and use synthetic, minimized, deterministic, public-safe fixtures.

Do not place in fixtures:

- credentials or source tokens;
- full live source responses;
- restricted field or operator records;
- private parcel joins;
- source caches;
- canonical production data;
- release candidates or published artifacts.

### Current CI truth

The current domain workflow runs:

```text
echo TODO validate-agriculture
echo TODO build-proof-agriculture
echo TODO publish-dry-run-agriculture
```

A successful run proves only that the echo steps executed. It does not prove package importability, test coverage, contract/schema alignment, sensitivity enforcement, evidence closure, proof construction, release readiness, or publication safety.

### Suggested local commands

These commands are **PROPOSED** until package metadata and test entry points are accepted.

```bash
python -m compileall packages/domains/agriculture/src

PYTHONPATH=packages/domains/agriculture/src \
python -c "import agriculture"

pytest -q tests/domains/agriculture

python tools/validate_all.py
```

Do not claim success unless the commands are actually run against the relevant commit and their outputs are recorded.

[Back to top](#top)

---

## Implementation admission and package evolution

### First helper admission sequence

1. Name the consuming app, pipeline, worker, tool, validator, or test.
2. Confirm the logic is reusable package behavior rather than source-specific acquisition or workflow orchestration.
3. Pin the source role, object family, contract/schema or explicit local-only interface, identity profile, time profile, and sensitivity expectations.
4. Add synthetic positive, negative, ambiguous, conflicted, stale, restricted, unsupported, and no-network cases.
5. Implement one pure helper with no hidden I/O or authority.
6. Export deliberately only when compatibility support is intended.
7. Run import, unit, boundary, determinism, sensitivity, and contract/schema tests.
8. Add meaningful CI wiring; do not count echo-only jobs.
9. Review security, rights, sensitivity, dependency, consumer, correction, and rollback impact.
10. Record the package version and changelog effect.

### Package versioning

The current `0.0.0` value is a placeholder and must not imply a release.

Before the first supported release, define:

- build backend;
- package discovery;
- supported Python versions;
- dependencies and optional dependency groups;
- license and security posture;
- public export policy;
- semantic-versioning or accepted alternative;
- deprecation window;
- changelog format;
- wheel/sdist reproducibility;
- provenance and integrity metadata;
- package registry/release relationship, if any.

A package release is still not KFM data publication.

### Change impact

Any change to mapping, identity, time, aggregation, suppression, or public exports requires:

- changed contract/profile reference;
- before/after fixtures;
- downstream consumer inventory;
- migration or recompile plan;
- correction/invalidation analysis;
- version and changelog decision;
- rollback target.

[Back to top](#top)

---

## Compatibility, correction, and rollback

### Compatibility

No supported public package API is currently established. Future compatibility promises begin only when exports and version policy are explicitly accepted.

Do not treat an internal module path as stable merely because another file imports it.

### Correction and invalidation

When a mapping, identity, temporal, unit, aggregation, or suppression defect is found:

1. identify the affected package version, helper, profile, and input range;
2. stop or narrow affected callers where material;
3. add a failing regression fixture;
4. correct the helper or governing profile in its owning root;
5. recompute candidate outputs through authorized pipelines;
6. invalidate affected caches, candidate artifacts, receipts, proofs, catalog projections, or releases through their owning systems;
7. preserve correction and supersession lineage;
8. verify public-safe state and rollback support before re-release.

The package must never mutate previously released records in place.

### README rollback

Before merge, abandon or close the review branch if the revision is rejected. After merge, create a transparent revert restoring prior blob:

```text
dd2fc20db17e18478d9135cd5105b8695fbbfee1
```

Then rerun applicable documentation and repository checks. Do not rewrite shared history.

No data, schema, policy, source, deployment, or release rollback is required for this documentation-only revision.

[Back to top](#top)

---

## Definition of done

### README v0.2

- [x] Pins repository, base commit, target, and prior blob.
- [x] Reconciles the parent package README with the current source-root and child-module v0.2 contracts.
- [x] Records the verified `kfm-domain-agriculture` `0.0.0` scaffold and empty initializer.
- [x] Preserves strong v0.1 helper, anti-collapse, sensitivity, test, and authority content.
- [x] Adds bounded context, ubiquitous language, owned/non-owned responsibilities, interfaces, object invariants, dependencies, identity/time, finite outcomes, public safety, evidence/release expectations, validation, correction, and rollback.
- [x] Surfaces known contract/schema/outcome/test-path conflicts rather than resolving them by prose.
- [x] Avoids claims of implementation, test execution, CI enforcement, runtime use, evidence closure, or release.
- [x] Changes no code, schema, policy, workflow, data, source, registry, receipt, proof, or release artifact.

### First supported package release

- [ ] Owners and review mapping are accepted.
- [ ] Build backend, discovery, Python range, dependencies, and license/security posture are defined.
- [ ] Public exports and compatibility policy are accepted.
- [ ] At least one real reusable helper has a consumer and accepted contract/schema or explicit local-only scope.
- [ ] Positive, negative, ambiguous, conflicted, stale, restricted, unsupported, and no-network tests pass.
- [ ] Native values, source roles, identity, time, uncertainty, and limitations are preserved.
- [ ] No hidden I/O, policy, lifecycle, evidence, release, or public-path authority is proven.
- [ ] Meaningful CI checks replace echo-only scaffolds.
- [ ] Correction, deprecation, migration, and rollback are documented.
- [ ] Release provenance and artifact integrity are verified.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-AG-001` | Who owns the package and which CODEOWNERS rule is enforceable? | **UNKNOWN** |
| `PKG-DOM-AG-002` | Which build backend, Python versions, package-discovery rules, dependencies, and license metadata apply? | **UNKNOWN** |
| `PKG-DOM-AG-003` | Is the verified surface the complete package tree, and which consumers import it? | **NEEDS VERIFICATION** |
| `PKG-DOM-AG-004` | Which symbols will form the first supported public API? | **UNKNOWN** |
| `PKG-DOM-AG-005` | Which Agriculture contracts and schemas are accepted and field-complete? | **NEEDS VERIFICATION** |
| `PKG-DOM-AG-006` | How will compatibility paths and `AggregationReceipt` naming be resolved? | **CONFLICTED** |
| `PKG-DOM-AG-007` | What is the accepted mapping from policy outcomes to package issues and runtime envelopes? | **CONFLICTED** |
| `PKG-DOM-AG-008` | Should package tests remain in `tests/domains/agriculture/` or gain a reviewed package sublane? | **NEEDS VERIFICATION** |
| `PKG-DOM-AG-009` | Which fixture lanes and validator paths bind to the first helper? | **UNKNOWN** |
| `PKG-DOM-AG-010` | Which identity, geometry normalization, canonicalization, and time profiles are accepted? | **UNKNOWN** |
| `PKG-DOM-AG-011` | Which aggregation, suppression, and generalization thresholds are approved for each audience? | **UNKNOWN** |
| `PKG-DOM-AG-012` | Which rights and sensitivity profiles govern remote-sensing, NASS, field, operator, and parcel-adjacent inputs? | **NEEDS VERIFICATION** |
| `PKG-DOM-AG-013` | Which meaningful CI jobs block incompatible or unsafe package changes? | **UNKNOWN** |
| `PKG-DOM-AG-014` | How are package-produced candidate outputs invalidated and replayed after corrections? | **UNKNOWN** |
| `PKG-DOM-AG-015` | Can public apps be proven unable to import package internals or bypass governed APIs? | **NEEDS VERIFICATION** |
| `PKG-DOM-AG-016` | Is a package registry publication planned, and how is it separated from KFM data publication? | **UNKNOWN** |

[Back to top](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Current request and KFM GitHub documentation operating prompt | **CONFIRMED task authority** | One-file IMPLEMENT scope, package/domain README profile, validation, remote readback, draft PR, rollback. | Not repository implementation proof. |
| Prior target README | **CONFIRMED** | Existing helper boundaries, sensitivity posture, anti-collapse rules, proposed tests, rollback blob. | Planning-oriented and stale relative to current source-root evidence. |
| `pyproject.toml` | **CONFIRMED** | Distribution name and placeholder version. | No build, dependency, Python, or publishing behavior. |
| `src/README.md` v0.2 | **CONFIRMED repository document** | Source layout, empty initializer, bounded helper absence, test/fixture roots, workflow truth. | Documentation and inspected-path evidence, not executable proof. |
| `src/agriculture/README.md` v0.2 | **CONFIRMED repository document** | Detailed helper semantics, object-family boundaries, identity/time, finite results, public safety. | Does not establish helper code or consumers. |
| Agriculture domain README | **CONFIRMED repository document** | Domain object families, aggregate/permissioned posture, cross-lane ownership. | Earlier authoring evidence limits remain inside that document. |
| Agriculture contract/schema/policy indexes | **CONFIRMED documentation/indexes** | Authority split, known scaffolds, compatibility and naming conflicts. | Incomplete object-level and executable closure. |
| Agriculture test/fixture READMEs | **CONFIRMED documentation** | Existing domain lanes and fixture/test rules. | Test modules, payload coverage, and results remain unverified. |
| Directory Rules v1.4 | **CONFIRMED doctrine** | `packages/` responsibility, Domain Placement Law, trust/lifecycle split, anti-drift rules. | Some path and ADR decisions remain proposed. |
| ADR-0001 | **CONFIRMED file / proposed decision** | Proposed canonical schema home and four-layer split. | Not accepted and not field-level schema proof. |
| `domain-agriculture.yml` | **CONFIRMED workflow scaffold** | Exact echo-only current behavior. | No meaningful enforcement. |
| Domain-Driven Design reference | **REFERENCE** | Bounded context and shared language concepts. | Does not override KFM doctrine or repo evidence. |

[Back to top](#top)

---

## Status summary

`packages/domains/agriculture/` is a verified Python package path with distribution metadata `kfm-domain-agriculture` version `0.0.0`, a `src` layout, and an empty `agriculture` initializer. It is not yet a verified helper library, stable public API, connector, pipeline, source registry, schema authority, policy engine, EvidenceBundle resolver, lifecycle writer, receipt/proof emitter, release authority, public API, UI package, map renderer, or governed-AI surface.

<p align="right"><a href="#top">Back to top</a></p>
