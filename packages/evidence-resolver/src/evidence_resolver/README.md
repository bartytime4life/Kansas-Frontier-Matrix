<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-evidence-resolver-src-evidence-resolver-readme
title: packages/evidence-resolver/src/evidence_resolver/ — Governed Evidence Resolution Helper Module
type: readme
version: v0.2
status: draft; repository-grounded; python-source-module; implementation-placeholder; non-authoritative
owners:
  - OWNER_TBD — Evidence resolver package owner
  - OWNER_TBD — Evidence and proof steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Policy, rights, and sensitivity steward
  - OWNER_TBD — Runtime and governed API steward
  - OWNER_TBD — Release, correction, validator, security, and docs steward
created: NEEDS VERIFICATION — target file existed before this revision
updated: 2026-07-15
supersedes: v1 planning-oriented import-namespace guide (2026-06-14)
policy_label: public; packages; evidence-resolver; python; evidenceref; evidencebundle; closure-validation; no-network-by-default; cite-or-abstain; fail-closed; non-authoritative
path: packages/evidence-resolver/src/evidence_resolver/README.md
truth_posture: CONFIRMED target and prior blob, kfm-evidence-resolver 0.0.0 project metadata, Python src layout, empty package initializer, bounded absence of selected resolver modules and package.json, parent package/source READMEs, sibling packages/evidence boundary, fielded closed EvidenceRef and EvidenceBundle schemas, paired draft contracts, minimal fixture families, generic schema harness, existing EvidenceBundle validator, missing schema-declared EvidenceRef validator, echo-only evidence-resolver workflow, Directory Rules v1.4, and current common SpecHash contract/schema / PROPOSED future pure resolver candidate helpers, lookup-snapshot adapters, local schema checks, closure issue carriers, explicit profile adapters, and package tests / CONFLICTED architecture EvidenceRef and EvidenceBundle shapes versus current paired schemas, JCS-prefixed architecture hash notation versus current SpecHash shape, resolver-local outcomes versus runtime outcomes and NEEDS_REVIEW, strong claim-scope checks versus current free-form claim_scope, and evidence-resolver versus packages/evidence responsibility overlap / UNKNOWN build backend, Python requirement, dependencies, package discovery, public exports, import consumers, resolver input/result contracts, registry adapter, package-specific tests, runtime/API wiring, package publication, release integration, and production behavior / NEEDS VERIFICATION accepted owners, canonical resolver profiles and outcomes, registry and supersession contracts, canonicalization profile, reason-code vocabulary, policy handoff, correction invalidation, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 9db5069e920614511e828510352a23ed29d14706
  prior_blob: f46f102805512cd293e96fe30e4fa9b2f57d31a8
  bounded_module_search: README.md and empty __init__.py confirmed; selected helper files were absent
related:
  - ./__init__.py
  - ../README.md
  - ../../README.md
  - ../../pyproject.toml
  - ../../../evidence/README.md
  - ../../../../contracts/evidence/evidence_ref.md
  - ../../../../contracts/evidence/evidence_bundle.md
  - ../../../../contracts/common/spec_hash.md
  - ../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json
  - ../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../../../fixtures/contracts/v1/evidence/evidence_ref/README.md
  - ../../../../fixtures/contracts/v1/evidence/evidence_bundle/README.md
  - ../../../../tools/validators/validate_evidence_bundle.py
  - ../../../../tests/schemas/test_common_contracts.py
  - ../../../../docs/architecture/evidence-identity.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../.github/workflows/evidence-resolver.yml
tags: [kfm, packages, evidence-resolver, python, source-module, EvidenceRef, EvidenceBundle, closure, resolver-profile, claim-scope, spec-hash, deterministic, no-network, fail-closed, cite-or-abstain, rollback]
notes:
  - "v0.2 replaces stale planning language with a commit-pinned description of the current kfm-evidence-resolver 0.0.0 Python scaffold."
  - "The package initializer is empty and selected resolver modules are absent; no supported resolver API, consumer, registry adapter, or production behavior is claimed."
  - "EvidenceRef and EvidenceBundle have current fielded closed PROPOSED schemas and paired draft contracts, but no resolver input/result contract or schema was found at the exact tested paths."
  - "Architecture prose, paired schemas, hash notation, scope semantics, and resolver outcome vocabularies conflict; this README records those conflicts and forbids silent normalization."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Evidence Resolution Helper Module

`packages/evidence-resolver/src/evidence_resolver/`

> Python source-module boundary for reusable, deterministic, side-effect-minimal helpers that may evaluate an `EvidenceRef` and a caller-supplied governed bundle lookup snapshot against an explicit resolution profile. The current repository surface is a **greenfield `0.0.0` scaffold**, not an implemented resolver: `__init__.py` is empty, selected resolver modules are absent, no supported result contract exists, and material architecture/schema conflicts must be resolved before a stable API is declared.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![distribution](https://img.shields.io/badge/distribution-kfm--evidence--resolver-3776ab)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![boundary](https://img.shields.io/badge/boundary-pointer%E2%86%92closure-6f42c1)
![network](https://img.shields.io/badge/network-none%20by%20default-455a64)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose-and-audience) · [Authority](#authority-level) · [Status](#current-repository-state) · [Context](#bounded-context-and-ubiquitous-language) · [Sibling](#relationship-to-packagesevidence) · [Profiles](#contract-schema-and-architecture-profile-conflicts) · [EvidenceRef](#evidenceref-boundary) · [EvidenceBundle](#evidencebundle-boundary) · [Scope](#claim-scope-and-closure-boundary) · [Outcomes](#resolver-outcome-boundary) · [Inputs](#accepted-inputs) · [Outputs](#permitted-outputs) · [Interface](#proposed-module-interface) · [Dependencies](#dependency-and-import-direction) · [Identity](#identity-hashing-time-and-supersession) · [Trust](#lifecycle-policy-release-and-public-safety) · [Failures](#failure-and-error-semantics) · [Security](#security-privacy-and-data-minimization) · [Tests](#tests-fixtures-validators-and-ci) · [Admission](#implementation-admission-sequence) · [Compatibility](#compatibility-correction-and-rollback) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Repository snapshot:** `main@9db5069e920614511e828510352a23ed29d14706`<br>
> **Distribution:** `kfm-evidence-resolver` version `0.0.0`<br>
> **Verified import package:** `src/evidence_resolver/`<br>
> **Verified implementation:** empty `__init__.py`; selected resolver modules absent<br>
> **Machine-shape posture:** EvidenceRef and EvidenceBundle schemas are fielded, closed, and marked `PROPOSED`<br>
> **Resolver-result posture:** no contract/schema found at the exact tested `evidence_resolution` paths<br>
> **Public posture:** public clients receive governed runtime/API results; they do not import this module or read registries, proofs, lifecycle stores, or canonical evidence directly

> [!CAUTION]
> Resolution is not truth. Schema validity is not closure. `bundle_ref` is not a verified bundle. A matched digest is not policy clearance. `RESOLVED` is not release approval. A package helper is not the registry, proof store, policy engine, release gate, or public trust membrane.

---

## Purpose and audience

`packages/evidence-resolver/src/evidence_resolver/` is the proposed implementation module inside the `kfm-evidence-resolver` shared package.

A mature implementation may provide pure or side-effect-minimal support for:

- validating current-profile `EvidenceRef` shape;
- accepting an explicit caller-supplied EvidenceBundle candidate or governed lookup snapshot;
- validating current-profile EvidenceBundle shape through the authoritative schema;
- comparing reference and bundle identity fields that are actually present in an accepted profile;
- checking whether required bundle collections are non-empty and whether declared checksums/spec hashes have valid shape;
- returning deterministic issues for missing, malformed, inconsistent, unsupported, stale, or blocked resolution context;
- preserving rights, sensitivity, release, correction, supersession, and policy references supplied by governed callers;
- preparing a **candidate** resolution result for downstream policy, citation, release, and runtime-envelope handling;
- supporting synthetic, public-safe, no-network tests.

This module must remain subordinate to evidence contracts, schemas, registry/proof systems, policy, review, release, correction, runtime, and governed API serialization.

### Audience

This README is for:

- evidence resolver package maintainers;
- evidence, proof, contract, schema, policy, release, and correction stewards;
- governed runtime and API maintainers;
- validator and fixture maintainers;
- security, privacy, and rights reviewers;
- application, pipeline, domain-package, and tool authors considering this module as a dependency;
- reviewers deciding whether proposed behavior belongs here, in `packages/evidence/`, in a registry/proof service, in policy, in a validator, or in an application.

[Back to top](#top)

---

## Authority level

**Implementation-support module, currently scaffolded; non-authoritative for evidence meaning, closure records, policy, release, storage, or public answers.**

| Concern | Authority in this module |
|---|---|
| EvidenceRef semantic meaning | **None.** Meaning belongs to `contracts/evidence/evidence_ref.md`. |
| EvidenceRef machine shape | **None.** Shape belongs to `schemas/contracts/v1/evidence/evidence_ref.schema.json`. |
| EvidenceBundle semantic meaning | **None.** Meaning belongs to `contracts/evidence/evidence_bundle.md`. |
| EvidenceBundle machine shape | **None.** Shape belongs to `schemas/contracts/v1/evidence/evidence_bundle.schema.json`. |
| Registry lookup and bundle existence | **None.** Registry/proof systems own materialized records and lookup authority. |
| Evidence closure | **None.** A stored, validated EvidenceBundle plus governed checks owns closure state. |
| Source authority and rights | **None.** Source descriptors, rights review, and policy systems own those decisions. |
| Policy and sensitivity | **None.** Policy systems decide allowance, restriction, hold, abstention, and denial. |
| Release and correction | **None.** Release records and workflows own publication, correction, withdrawal, supersession, and rollback. |
| Public runtime outcome | **None.** Governed runtime/API envelopes own `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`. |
| Local helper behavior | **Supporting only.** Code may validate explicit inputs, compare profile-defined values, and return candidate issues/results. |

Importing a schema model, validating JSON, comparing hashes, or returning a resolver status does not transfer authority into this package.

[Back to top](#top)

---

## Current repository state

### Evidence snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Repository ID | `1059091169` |
| Visibility | public |
| Base ref | `main` |
| Base commit | `9db5069e920614511e828510352a23ed29d14706` |
| Prior target blob | `f46f102805512cd293e96fe30e4fa9b2f57d31a8` |
| Current revision | documentation-only v0.2 proposal |

### Verified module and contract surface

| Surface | Evidence at snapshot | Status | Consequence |
|---|---|---:|---|
| This README | Existing v1 planning-oriented namespace guide. | **CONFIRMED** | Revised in place; useful anti-authority rules are retained. |
| Parent package README | `packages/evidence-resolver/README.md` exists. | **CONFIRMED README / planning-oriented** | Package-level responsibility remains relevant but is not implementation proof. |
| Source-root README | `packages/evidence-resolver/src/README.md` exists. | **CONFIRMED README / planning-oriented** | This file refines the import-module boundary. |
| Python project metadata | `pyproject.toml` declares `kfm-evidence-resolver` version `0.0.0`. | **CONFIRMED greenfield placeholder** | Distribution identity is known; build/install behavior is not. |
| Build backend | No `[build-system]` block appears in the inspected project file. | **NOT OBSERVED** | Do not claim wheel/editable-install behavior. |
| Python requirement | No `requires-python` field appears. | **NOT OBSERVED** | Supported interpreter versions are unknown. |
| Dependencies | No dependency list appears. | **NOT OBSERVED** | Do not claim `jsonschema`, registry, API, or crypto dependencies. |
| Package discovery | No discovery configuration appears. | **NOT OBSERVED** | Import/install behavior remains unknown. |
| JavaScript manifest | `package.json` was absent at the exact package path. | **CONFIRMED bounded absence** | Do not claim a JavaScript/TypeScript package. |
| Namespace initializer | `src/evidence_resolver/__init__.py` exists and is empty. | **CONFIRMED scaffold** | No public exports or initialization behavior are established. |
| `outcomes.py` | Absent at the exact tested path. | **CONFIRMED bounded absence** | Resolver outcome implementation is not established. |
| `resolver.py` | Absent at the exact tested path. | **CONFIRMED bounded absence** | Resolution orchestration is not established. |
| `closure.py` | Absent at the exact tested path. | **CONFIRMED bounded absence** | Closure-check implementation is not established. |
| `scope.py` | Absent at the exact tested path. | **CONFIRMED bounded absence** | Claim-scope matching is not established. |
| Indexed module search | Returned README surfaces only for the package/source/module query. | **CONFIRMED search result / incomplete tree proof** | Empty or unindexed files may exist; exhaustive absence is not claimed. |
| Import consumers | Indexed search did not establish production imports or `resolve_evidence_ref` consumers. | **NOT OBSERVED / search-limited** | Runtime/API integration remains unknown. |
| Package test README | `tests/packages/evidence-resolver/README.md` was absent at the exact path. | **CONFIRMED bounded absence** | No package-test lane is documented there. |
| Package fixture README | `fixtures/packages/evidence-resolver/README.md` was absent at the exact path. | **CONFIRMED bounded absence** | No package-specific fixture lane is documented there. |
| EvidenceRef schema | Closed schema requires `ref` and `kind`; optional `bundle_ref`; four evidence kinds. | **CONFIRMED schema / `PROPOSED`** | Local shape checks can bind to an explicit profile. |
| EvidenceBundle schema | Closed schema requires ten top-level closure fields. | **CONFIRMED schema / `PROPOSED`** | Bundle checks must use this exact field surface or a versioned successor. |
| Paired contracts | EvidenceRef and EvidenceBundle v0.2 contracts exist. | **CONFIRMED draft contracts / `PROPOSED`** | Meaning is documented but not accepted as implementation maturity. |
| Resolver input/result schema | `schemas/contracts/v1/evidence/evidence_resolution.schema.json` returned no file. | **CONFIRMED absent at tested path** | No canonical resolver result shape is established there. |
| Resolver semantic contract | `contracts/evidence/evidence_resolution.md` returned no file. | **CONFIRMED absent at tested path** | Resolver outcome meaning is not canonically defined there. |
| EvidenceRef fixtures | One valid and one invalid missing-`ref` case. | **CONFIRMED minimal coverage** | Coverage does not test resolution. |
| EvidenceBundle fixtures | One valid and one invalid missing-`bundle_id` case. | **CONFIRMED minimal coverage** | Coverage does not test cross-record closure. |
| EvidenceBundle validator | Thin executable wrapper loads the bundle schema and fixture root. | **CONFIRMED file / not run in this authoring step** | Presence does not prove package behavior. |
| EvidenceRef validator | Schema declares `tools/validators/validate_evidence_ref.py`; exact file was absent. | **CONFIRMED contract mismatch** | Dedicated validator parity is incomplete. |
| Generic schema harness | `tests/schemas/test_common_contracts.py` includes the evidence family. | **CONFIRMED test code** | It validates fixture shape, not resolver semantics. |
| Resolver workflow | `.github/workflows/evidence-resolver.yml` contains two `echo TODO` jobs. | **CONFIRMED CI scaffold** | A green run would not prove resolution behavior. |
| Runtime/release evidence | No runtime log, registry trace, resolution receipt, release record, or public response was inspected. | **UNKNOWN** | This README is not production proof. |

### Current module tree

```text
packages/evidence-resolver/
├── README.md
├── pyproject.toml                 # kfm-evidence-resolver 0.0.0 only
└── src/
    ├── README.md
    └── evidence_resolver/
        ├── README.md              # this file
        └── __init__.py            # empty
```

This is a bounded verified surface, not an exhaustive recursive-tree claim.

[Back to top](#top)

---

## Bounded context and ubiquitous language

The bounded context is:

> Deterministic evaluation of explicit evidence pointer, bundle candidate, and governed lookup context against a named resolution profile, producing a non-authoritative candidate result for downstream gates.

Use these terms consistently:

| Term | Meaning here | Not equivalent to |
|---|---|---|
| EvidenceRef | Current-profile pointer with `ref`, `kind`, and optional `bundle_ref`. | EvidenceBundle, citation completeness, or proof. |
| EvidenceBundle | Current-profile claim-scope closure object with required refs, records, citations, rights, sensitivity, transforms, checksums, and spec hash. | PolicyDecision, ReleaseManifest, or public response. |
| Bundle candidate | Explicit object supplied to this module for checking. | Admitted/materialized proof record. |
| Lookup snapshot | Explicit registry/proof metadata supplied by a governed caller or adapter. | Registry authority or live store access. |
| Resolution profile | Version/hash identifying the exact contracts, schemas, and cross-record rules used. | “Latest” ambient behavior. |
| Local validity | The object passes local/profile checks. | Evidence closure, policy allowance, or release eligibility. |
| Closure issue | Deterministic reason a ref and candidate bundle cannot yet support the next gate. | Public denial explanation or hidden exception. |
| Resolver result candidate | Package-local output for downstream policy/runtime processing. | `RuntimeResponseEnvelope` or public truth. |
| Supersession | Governed lineage state supplied by a registry/correction system. | A field currently present in the paired EvidenceBundle schema. |
| Cite-or-abstain | Do not answer from unresolved required evidence. | Permission to expose sensitive evidence. |

The word **resolve** means “evaluate explicit supplied resolution context.” It does not mean “search arbitrary stores, retrieve secret material, prove truth, approve release, or publish.”

[Back to top](#top)

---

## Relationship to `packages/evidence`

Two sibling package lanes are documented:

```text
packages/evidence/            # general ref, identity, digest, carrier, fixture helpers
packages/evidence-resolver/   # narrower pointer-to-closure evaluation lane
```

Boundary rules:

- general EvidenceRef value-object and digest helpers belong in `packages/evidence/` unless resolver-specific behavior is required;
- this module may consume shared evidence value types but must not duplicate them;
- `packages/evidence/` must not become a second resolver implementation;
- this module must not become a dumping ground for all evidence helpers;
- shared normalization/canonicalization code needs one owning package and tests;
- consolidation, rename, or import migration is ADR-class because it affects responsibilities, compatibility, consumers, tests, release evidence, and rollback.

**Status:** both package paths and READMEs are `CONFIRMED`; the final implementation split is `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Contract, schema, and architecture profile conflicts

The repository contains materially different descriptions of EvidenceRef, EvidenceBundle identity, and resolver outcomes. These conflicts block a stable implementation API.

### EvidenceRef shape conflict

The current paired schema permits only:

```text
ref
kind = measurement | record | dataset | artifact
bundle_ref?
```

and sets:

```text
additionalProperties: false
```

The older architecture note proposes fields such as:

```text
ref_id
target_spec_hash
expected_bundle_digest
resolution
policy_metadata
```

Those architecture-only fields cannot be added to the current closed schema. The architecture note explicitly labels its field list `PROPOSED`; the paired v0.2 contract/schema are newer repository evidence for the current profile.

### EvidenceBundle shape conflict

The current paired schema requires:

```text
bundle_id
claim_scope
evidence_refs
source_records
citations
rights
sensitivity
transforms
checksums
spec_hash
```

The older architecture note discusses different families such as `inputs`, `parameters`, `artifacts`, `checks`, `integrity`, and `signatures/attestations`.

The module must not merge those profiles into one object. A migration requires a versioned contract/schema change, fixtures, validator updates, compatibility tests, and consumer migration.

### SpecHash notation and canonicalization conflict

The architecture note describes:

```text
jcs:sha256:<hex>
```

The current common SpecHash schema instead requires an object:

```json
{
  "value": "sha256:<64 lowercase hex>"
}
```

The current SpecHash contract also states that the canonicalization procedure is not represented by the schema and remains to be pinned by producers/surrounding records.

Therefore this module may validate current shape and preserve supplied values, but it must not generate authoritative `spec_hash` values until the canonical byte surface and canonicalization profile are accepted.

### Resolver-outcome conflict

The existing resolver READMEs propose local outcomes:

```text
RESOLVED · UNRESOLVED · DENIED · ERROR
```

The architecture note describes runtime/public outcomes:

```text
ANSWER · ABSTAIN · DENY · ERROR · NEEDS_REVIEW
```

Current runtime envelope work elsewhere uses:

```text
ANSWER · ABSTAIN · DENY · ERROR
```

No resolver input/result contract or schema was found at the exact tested `evidence_resolution` paths. `NEEDS_REVIEW` is not part of the confirmed finite RuntimeResponseEnvelope enum inspected in the Envelopes work.

Required posture:

1. do not expose a stable resolver enum until its semantic contract and machine shape are accepted;
2. keep package-local resolver status distinct from public runtime outcome;
3. treat any `DENIED` local state as a transport of caller-supplied policy state, never local policy evaluation;
4. map local issues to `ABSTAIN`, `DENY`, or `ERROR` only in the governed runtime/API layer;
5. route review-required context through an accepted review/policy mechanism rather than inventing a fifth public outcome;
6. reject mixed profile fields and unknown status vocabularies.

[Back to top](#top)

---

## EvidenceRef boundary

For the current paired profile, an EvidenceRef has:

| Field | Required | Package-helper posture |
|---|---:|---|
| `ref` | yes | Preserve exactly; do not silently retarget or dereference through hidden I/O. |
| `kind` | yes | Require one of `measurement`, `record`, `dataset`, `artifact`. |
| `bundle_ref` | no | Treat as a claimed pointer to closure, not verified closure. |

Allowed local checks:

- required fields are present;
- `kind` is in the current enum;
- no unknown fields appear under the closed profile;
- the value passes the authoritative schema;
- a supplied lookup snapshot addresses the same explicit `bundle_ref` when one is present;
- profile/version metadata is explicit outside the object if needed.

Not allowed:

- inventing `bundle_ref`;
- resolving a ref by scanning RAW, WORK, QUARANTINE, catalogs, proofs, or network services directly;
- treating `bundle_ref` as proof that the bundle exists, is current, is the lineage head, or supports the requested claim;
- inferring rights, sensitivity, policy, or release from `kind`;
- widening a dataset-level ref into item-level claim support.

[Back to top](#top)

---

## EvidenceBundle boundary

The current paired EvidenceBundle schema is closed and requires ten top-level fields.

| Field | Current schema posture | Resolver-helper rule |
|---|---|---|
| `bundle_id` | required patterned string | Compare with explicit reference/lookup values; do not mint authoritative identity locally. |
| `claim_scope` | required string | Preserve; strong machine scope matching is not possible from this free-form field alone. |
| `evidence_refs` | required, minimum one | Validate each current-profile EvidenceRef; do not assume every ref is itself resolved. |
| `source_records` | required, minimum one | Preserve identifiers; do not fetch source contents. |
| `citations` | required, minimum one | Preserve strings; citation presence is not citation validation. |
| `rights` | required object with `license` | Preserve; do not decide whether the license permits the requested use. |
| `sensitivity` | required policy schema reference | Preserve; policy systems decide exposure. |
| `transforms` | required array | Preserve order; do not claim transform verification without receipts/specs. |
| `checksums` | required object, minimum one, SHA-256 string values | Validate syntax and compare explicit expected values; do not guess canonical inputs. |
| `spec_hash` | required common SpecHash object | Validate current shape; authoritative generation requires an accepted canonicalization profile. |

A schema-valid bundle candidate is not necessarily:

- present in the governed proof registry;
- the current supersession head;
- supported by admissible source records;
- rights-cleared for the requested audience;
- safe at the requested spatial/temporal precision;
- citation-complete;
- reviewed;
- released;
- eligible for a public `ANSWER`.

[Back to top](#top)

---

## Claim-scope and closure boundary

The current EvidenceBundle schema represents `claim_scope` as a string. The current EvidenceRef schema does not include field path, temporal scope, spatial scope, domain, object id, expected digest, or supersession fields.

Therefore the older README claims about machine-checking all of those dimensions are not implementable from the current paired objects alone.

A strong resolver would need a separate, accepted input contract containing structured context such as:

```text
requested_claim_id
requested_field_path
requested_domain
requested_object_id
requested_valid_time
requested_spatial_scope
expected_bundle_id
expected_bundle_digest
registry_head_ref
policy_decision_ref
release_ref
correction_state
```

No canonical resolver-input schema was verified in this task.

Until one exists, this module may:

- validate the current EvidenceRef and EvidenceBundle profiles;
- perform exact comparisons over explicit fields that are present;
- preserve additional governed context in a separate caller-owned object;
- return `UNSUPPORTED`/issue context when a requested closure test cannot be proven from the selected profile;
- avoid parsing free-form `claim_scope` as if it were a stable machine language.

It must not use substring matching, generated interpretation, or heuristic similarity to upgrade scope sufficiency.

[Back to top](#top)

---

## Resolver outcome boundary

A resolver result should be finite, explicit, and non-authoritative. Its canonical shape and final status enum remain **UNRESOLVED GOVERNANCE**.

The existing four proposed local meanings may be retained as discussion vocabulary:

| Proposed local status | Meaning | Downstream posture |
|---|---|---|
| `RESOLVED` | The selected profile and supplied lookup context passed all resolver checks implemented by this package. | Eligible for later policy, citation, review, release, and runtime checks; not automatically `ANSWER`. |
| `UNRESOLVED` | Required evidence, bundle, identity, scope, freshness, lineage, or correction support is absent or inconsistent. | Normally an abstain-ready issue. |
| `DENIED` | Caller supplied a policy/rights/sensitivity decision that blocks the requested resolution/use. | Deny-ready context; this package does not compute the decision. |
| `ERROR` | Input/profile/schema/adapter execution failed safely. | Error-ready context; no fallback content. |

Rules:

- `RESOLVED` must name the resolution profile used;
- unresolved required refs must not be dropped from composed claims;
- local status must not be serialized directly as the public runtime outcome;
- `NEEDS_REVIEW` must be handled through accepted review/policy workflow, not silently added to a closed runtime enum;
- a resolver error must not cause the caller to use the original claim without evidence;
- reason codes must be stable, safe, and separately governed before public exposure.

[Back to top](#top)

---

## Accepted inputs

Inputs must be explicit and supplied by governed callers or deterministic tests.

| Input family | Accepted posture | Rejected behavior |
|---|---|---|
| Resolution profile | Explicit contract/schema version or content hash. | Ambient “latest” selection. |
| EvidenceRef | Current-profile mapping/object. | Free-form URL or guessed ref upgrade. |
| Bundle candidate | Current-profile mapping/object supplied by a registry/proof adapter. | Hidden store/network lookup inside pure helpers. |
| Lookup snapshot | Explicit found/not-found, registry id, current-head, lineage, and expected-digest values under an accepted adapter contract. | Reading canonical stores directly. |
| Claim context | Structured caller-owned context under an accepted resolver-input profile. | Heuristic parsing of free-form `claim_scope`. |
| Policy context | PolicyDecision/ref, audience, rights/sensitivity posture, obligations. | Local policy evaluation. |
| Release/correction context | Release ref/state, correction, withdrawal, supersession, rollback refs. | Local publication/correction mutation. |
| Time context | Explicit observation/evaluation/request times and freshness posture. | Hidden wall-clock dependence. |
| Integrity context | Expected checksum/spec-hash values and canonicalization profile. | Hashing unknown bytes and calling the result authoritative. |
| Fixture context | Synthetic/public-safe objects and expected issues. | Production evidence or sensitive records in source fixtures. |

[Back to top](#top)

---

## Permitted outputs

A future module may return:

- a current-profile validated EvidenceRef value;
- a current-profile validated EvidenceBundle candidate;
- deterministic local issue objects;
- a candidate resolver result naming the profile and checks performed;
- preserved evidence, registry, policy, release, and correction refs;
- a receipt-ready summary for an owning runtime/tool to persist;
- synthetic fixture builders.

It must not return:

- a stored/admitted EvidenceBundle;
- a new proof pack;
- a PolicyDecision;
- a ReleaseManifest or PromotionDecision;
- a public RuntimeResponseEnvelope;
- a citation validation report unless delegated to its authoritative validator;
- a generated claim, answer, or summary;
- a hidden-registry handle that bypasses governed access;
- a success boolean that hides unresolved required evidence.

### Proposed result carrier

The following is illustrative and **not implemented or canonical**:

```python
from dataclasses import dataclass
from typing import Mapping

@dataclass(frozen=True)
class ResolutionIssue:
    code: str
    field: str | None = None
    detail: str | None = None  # safe, bounded context only

@dataclass(frozen=True)
class EvidenceResolutionCandidate:
    profile: str
    status: str  # enum pending accepted resolver-result contract
    evidence_ref: Mapping[str, object]
    bundle_id: str | None
    checks_performed: tuple[str, ...]
    issues: tuple[ResolutionIssue, ...]
    policy_decision_ref: str | None = None
    release_ref: str | None = None
    correction_ref: str | None = None
```

This carrier does not persist a receipt or authorize a runtime answer.

[Back to top](#top)

---

## Proposed module interface

No proposed file below is currently verified as implemented.

```text
packages/evidence-resolver/src/evidence_resolver/
├── README.md
├── __init__.py              # deliberate supported exports only
├── issues.py                # local issue/result carriers
├── profiles.py              # accepted resolution profile identifiers
├── evidence_ref.py          # current-profile shape adapter
├── evidence_bundle.py       # current-profile shape adapter
├── resolver.py              # pure evaluation over explicit inputs
├── integrity.py             # explicit checksum/spec-hash comparisons
└── compatibility.py         # add only after migration rules exist
```

Smallest useful callable surface after governance resolution:

```python
validate_evidence_ref_candidate(...)
validate_evidence_bundle_candidate(...)
evaluate_resolution_candidate(...)
compare_declared_integrity(...)
```

Admission rules:

- no export until a real consumer and tests exist;
- no wildcard exports;
- no import-time I/O, registry connection, or plugin registration;
- no generic `resolve(anything)` API;
- no hidden fallback from unsupported profile to permissive behavior;
- no authority verbs such as `publish`, `approve`, `admit_bundle`, `decide_policy`, `force_resolved`, `resolve_truth`, or `call_model`.

[Back to top](#top)

---

## Import and export posture

The current empty `__init__.py` establishes no supported API.

A future reviewed import may look like:

```python
from evidence_resolver.resolver import evaluate_resolution_candidate
from evidence_resolver.profiles import ResolutionProfile
```

Avoid:

```python
from evidence_resolver import *
from evidence_resolver._unsafe import force_resolved
from packages.evidence import resolve_bundle  # parallel responsibility risk
```

`__init__.py` should export only stable reviewed symbols. Registry adapters, compatibility shims, and migration internals should remain private until their burden is accepted.

[Back to top](#top)

---

## Dependency and import direction

Preferred direction:

```text
contracts + schemas + governed lookup/policy/release context
                         |
                         v
               registry/runtime adapter
                         |
                         v
        evidence_resolver pure candidate checks
                         |
                         v
 authoritative schema + policy + citation + release gates
                         |
                         v
              governed runtime/API envelope
                         |
                         v
                    public client
```

This module may eventually depend on:

- Python standard library;
- narrowly accepted shared evidence value types;
- an approved JSON Schema validation library;
- generated schema models with pinned generation provenance;
- immutable caller-owned lookup/result types.

This module must not import:

- source connectors;
- lifecycle/canonical stores;
- proof or receipt writers;
- policy engines;
- release writers;
- model providers;
- API routers/service containers;
- UI/map components;
- deployment credentials/configuration.

A runtime adapter may call a registry and then invoke this package with the result. The package itself should remain no-network by default.

[Back to top](#top)

---

## Identity, hashing, time, and supersession

### Identity

Preserve distinct identifiers:

- EvidenceRef `ref`;
- optional EvidenceRef `bundle_ref`;
- EvidenceBundle `bundle_id`;
- source record identifiers;
- policy/release/correction refs;
- resolution-profile identity.

Do not encode secrets, raw evidence, sensitive coordinates, personal data, or credentials in ids.

### Hashing

The current schemas confirm:

- EvidenceBundle `checksums` values use `sha256:<64 lowercase hex>`;
- EvidenceBundle `spec_hash` uses the common SpecHash object;
- the common SpecHash profile uses `{ "value": "sha256:<64 lowercase hex>" }`.

The architecture note's JCS-prefixed notation and canonicalization claim are not represented by the current schema. Until canonicalization is accepted:

- validate shape;
- preserve supplied values;
- compare values only when producers used the same known profile;
- do not generate authoritative hashes from developer-formatted JSON;
- record the canonicalization profile in surrounding governed context if available.

### Time and freshness

The current EvidenceRef/EvidenceBundle schemas do not contain structured observation, valid, transaction, review, release, or freshness times. A resolver must not infer freshness from file timestamps, lookup time, or publication metadata.

Freshness checks require an accepted external resolver-input/registry profile.

### Supersession and correction

The current paired schemas do not encode lineage head or supersession fields. The architecture note proposes append-only lineage/supersession behavior, but implementation contracts remain unverified.

This module may compare caller-supplied supersession metadata under an accepted profile. It must not:

- walk a registry directly in pure helpers;
- treat the first bundle found as current;
- rewrite old bundles;
- discard correction history;
- silently repoint refs.

[Back to top](#top)

---

## Lifecycle, policy, release, and public safety

The lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This module owns no lifecycle phase.

Allowed flow:

```text
governed request/context
  -> registry/proof adapter supplies explicit lookup snapshot
  -> resolver package validates selected profiles and comparisons
  -> policy + rights + sensitivity
  -> citation validation + review + release/correction checks
  -> RuntimeResponseEnvelope
  -> governed public client
```

Blocked flow:

```text
resolver package
  -> scan RAW / WORK / QUARANTINE / proof store
  -> choose evidence heuristically
  -> decide policy
  -> generate claim text
  -> publish or return public answer directly
```

### Policy and rights

The module may preserve caller-supplied policy/rights/sensitivity values. It must not:

- interpret a license as legal permission;
- decide audience access;
- reduce sensitivity;
- waive obligations;
- convert unknown rights into allow;
- disclose protected evidence in issue messages.

### Release and correction

The module may preserve release/correction refs. It must not:

- approve release;
- mark evidence published;
- create a ReleaseManifest;
- correct, withdraw, supersede, or roll back records;
- hide stale/corrected state from downstream callers.

### Public and AI posture

Public clients and AI runtimes must not consume this package directly as truth authority. AI remains interpretive and may answer only after evidence, policy, citation, release, and runtime gates permit it.

[Back to top](#top)

---

## Failure and error semantics

Failures should be finite, deterministic where practical, and safe.

### Proposed issue families

```text
profile/unsupported
profile/mixed-fields
schema/evidence-ref-invalid
schema/evidence-bundle-invalid
lookup/not-found
lookup/inconsistent-id
lookup/not-current-head
closure/bundle-ref-missing
closure/evidence-ref-not-member
closure/required-evidence-unresolved
scope/unsupported-profile
scope/mismatch
integrity/checksum-mismatch
integrity/spec-hash-mismatch
integrity/canonicalization-unknown
policy/blocked-context
release/not-eligible
correction/superseded
internal/unexpected
```

Rules:

- package issues do not decide the public runtime outcome;
- `UNRESOLVED`, `DENIED`, and `ERROR` must remain distinct;
- unknown/unsupported checks fail closed;
- no partial result should be represented as resolved after a fatal issue;
- raw exceptions may be chained internally but must not leak sensitive details;
- no error path may fall back to ungoverned claim content;
- issue details must exclude credentials, private evidence, raw prompts, chain-of-thought, protected locations, and unrestricted source content.

[Back to top](#top)

---

## Security, privacy, and data minimization

Future code should be no-network, no-secret, and low-retention by default.

Required controls:

- no environment credential reads;
- no direct registry/store/network clients in pure helpers;
- no production filesystem writes;
- no logging full EvidenceBundles by default;
- no raw evidence, source payload, model output, prompt, or hidden reasoning retention;
- no sensitive values in reprs, exceptions, ids, or issue details;
- bounded input sizes and collection lengths;
- rejection of unknown fields under closed profiles;
- synthetic/public-safe fixtures only;
- dependency review before adding schema, crypto, or serialization libraries;
- constant-time digest comparison where threat analysis justifies it;
- explicit redaction policy for any diagnostic context;
- denial-of-service tests for deeply nested or oversized supplied objects.

Schema validation should occur before expensive cross-record comparisons.

[Back to top](#top)

---

## Tests, fixtures, validators, and CI

### Confirmed validation surfaces

| Surface | Current evidence | What it proves | What it does not prove |
|---|---|---|---|
| EvidenceRef schema | Fielded, closed, `PROPOSED`. | Current pointer machine shape. | Ref existence, closure, policy, or release. |
| EvidenceBundle schema | Fielded, closed, `PROPOSED`. | Current bundle candidate machine shape. | Registry admission, current head, source admissibility, or public safety. |
| EvidenceRef fixtures | One valid, one invalid missing-`ref` case. | Minimal shape examples. | Resolver behavior or broad negative coverage. |
| EvidenceBundle fixtures | One valid, one invalid missing-`bundle_id` case. | Minimal shape examples. | Cross-record closure or integrity behavior. |
| Generic schema harness | Discovers evidence-family fixture directories. | Repository test code exists. | Package-specific resolver behavior. |
| EvidenceBundle validator | Thin wrapper targets bundle schema/fixtures. | Dedicated file and paths exist. | It was run here or validates resolution. |
| EvidenceRef validator | Declared by schema but exact file absent. | Validator gap is visible. | No dedicated validator behavior exists at that path. |
| Evidence-resolver workflow | Two `echo TODO` jobs. | CI scaffold exists. | Any resolver code, denial, or fail-closed behavior. |

### Required package tests before first export

```text
tests/packages/evidence_resolver/
├── test_import_safety.py
├── test_public_exports.py
├── test_profiles.py
├── test_evidence_ref_candidate.py
├── test_evidence_bundle_candidate.py
├── test_resolution_candidate.py
├── test_scope_unsupported.py
├── test_integrity_comparison.py
├── test_policy_passthrough.py
├── test_correction_and_supersession.py
├── test_no_hidden_io.py
├── test_no_authority_imports.py
└── test_sensitive_diagnostics.py
```

This tree is **PROPOSED**. Confirm repository naming and placement before creating it.

### Required cases

- each missing required EvidenceRef/EvidenceBundle field;
- unknown fields under closed schemas;
- invalid EvidenceRef `kind`;
- absent and inconsistent `bundle_ref`;
- bundle id mismatch;
- bundle member mismatch;
- malformed and mismatched checksums/spec hashes;
- unknown canonicalization profile;
- free-form claim scope that cannot support requested machine checks;
- missing registry/current-head metadata;
- corrected, withdrawn, superseded, and stale context;
- caller-supplied policy block;
- unresolved required refs in composed claims;
- oversized/deep input;
- deterministic repeatability;
- no-network/no-filesystem behavior;
- no sensitive diagnostic leakage;
- import graph checks against connectors, stores, policy engines, release writers, model clients, API routes, and UI packages.

### Validation commands

Confirmed repository paths:

```bash
python tools/validators/validate_evidence_bundle.py
pytest -q tests/schemas/test_common_contracts.py
```

The following are **blocked/proposed**:

```bash
python tools/validators/validate_evidence_ref.py   # declared path currently absent
pytest -q tests/packages/evidence_resolver         # package test lane not established
```

A green `evidence-resolver` workflow is not meaningful until its `echo TODO` steps are replaced with executable checks.

[Back to top](#top)

---

## Implementation admission sequence

Use the smallest reversible sequence:

1. **Resolve responsibility:** confirm the split between `packages/evidence/` and `packages/evidence-resolver/`.
2. **Pin current object profiles:** accept or version the EvidenceRef, EvidenceBundle, and SpecHash contracts/schemas.
3. **Define resolver contracts:** add accepted resolver input and result meaning/shape in canonical roots.
4. **Resolve outcome vocabulary:** distinguish local resolver state, review state, policy decision, and public runtime outcome.
5. **Resolve scope representation:** replace or supplement free-form `claim_scope` if machine scope checks are required.
6. **Resolve registry/supersession adapter:** define the governed lookup snapshot and current-head semantics.
7. **Pin canonicalization:** define the bytes and canonicalization used for authoritative hash generation/comparison.
8. **Complete package metadata:** build backend, Python range, dependencies, discovery, license, and security posture.
9. **Repair validator parity:** add or deliberately remove the missing EvidenceRef validator declaration.
10. **Add package tests:** use repository conventions and synthetic fixtures.
11. **Implement one pure path:** validate one EvidenceRef plus one supplied EvidenceBundle candidate; no live registry.
12. **Wire one governed consumer:** runtime/app adapter performs I/O and validates again at the trust boundary.
13. **Replace workflow stubs:** execute real schema/package/negative-path checks.
14. **Record review evidence:** versions, hashes, fixtures, tests, known gaps, correction, and rollback target.
15. **Expand only from observed need:** add lineage, scope, compatibility, or performance features after consumers prove need.

Do not combine contract resolution, implementation, self-approval, and release in one unreviewed change.

[Back to top](#top)

---

## Compatibility, correction, and rollback

### Compatibility

Before a stable API exists:

- require explicit profiles;
- reject mixed or unknown fields;
- do not silently translate architecture fields to current schema fields;
- do not normalize `jcs:sha256:` to `sha256:` without an accepted migration;
- do not map `NEEDS_REVIEW` into a closed runtime outcome by convenience;
- treat all proposed exports as unstable.

After a stable release:

- use an accepted versioning policy;
- document deprecations and removal dates;
- provide source/target profile adapters only when losslessness is proven;
- add migration fixtures and consumer tests;
- retain old resolution receipts and correction lineage.

### Correction

A corrected schema, contract, registry head, source record, citation, rights decision, or release state may invalidate prior resolver results.

A mature result should let callers identify:

- resolver version/profile;
- EvidenceRef identity;
- EvidenceBundle id;
- expected/observed integrity values;
- registry snapshot/current-head identity;
- policy/release/correction refs;
- checks performed;
- issues and unsupported checks;
- input/output digests where governed.

Do not mutate historical resolution evidence in place.

### Rollback triggers

Rollback or disable implementation if it:

- becomes a parallel contract/schema/policy/proof/release authority;
- performs hidden store/network/model access;
- silently accepts mixed profiles;
- treats `bundle_ref` as verified closure;
- parses free-form scope heuristically as authoritative;
- generates hashes without an accepted canonicalization profile;
- hides unresolved required evidence;
- fabricates policy/release/correction state;
- leaks sensitive evidence;
- bypasses governed runtime/API validation;
- duplicates `packages/evidence/` responsibilities without migration authority;
- claims a stub workflow proves resolver behavior.

### Documentation-only rollback

Restore prior blob:

```text
f46f102805512cd293e96fe30e4fa9b2f57d31a8
```

No code, schema, contract, policy, fixture, test, proof, receipt, release, deployment, or package-registry rollback is required for this README-only revision.

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Grounds the actual `kfm-evidence-resolver` `0.0.0` Python scaffold.
- [x] Records the empty initializer and bounded absence of selected modules.
- [x] Preserves helper-only, no-network, cite-or-abstain, fail-closed boundaries.
- [x] Distinguishes EvidenceRef, EvidenceBundle, registry lookup, policy, release, and runtime outcomes.
- [x] Records current paired schema fields rather than architecture-only fields.
- [x] Surfaces EvidenceRef validator asymmetry and echo-only CI.
- [x] Surfaces shape, hash, scope, outcome, and sibling-package conflicts.
- [x] Defines a smallest reversible implementation path.
- [x] Changes no code, schema, contract, policy, fixture, test, workflow, data, proof, receipt, release, or deployment artifact.

### First supported resolver release

- [ ] Owners and CODEOWNERS review are accepted.
- [ ] Resolver versus general evidence-package ownership is settled.
- [ ] EvidenceRef, EvidenceBundle, SpecHash, resolver-input, and resolver-result profiles are accepted.
- [ ] Resolver-local and public runtime outcome vocabularies are accepted.
- [ ] Scope, registry, lineage, supersession, freshness, and correction semantics are machine-defined.
- [ ] Build backend, Python range, dependencies, discovery, and license are defined.
- [ ] Public exports and compatibility policy are accepted.
- [ ] Dedicated validators and package tests pass.
- [ ] Workflow stubs are replaced with executable checks.
- [ ] One governed I/O adapter and one real consumer exist.
- [ ] No authority-root or trust-membrane bypass is proven.
- [ ] Security, privacy, rights, correction, and rollback review is complete.
- [ ] Package artifact provenance is verified if distributed.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `EVRES-001` | Who owns the package/module and which CODEOWNERS rule is enforceable? | **UNKNOWN** |
| `EVRES-002` | Which responsibilities belong in `packages/evidence/` versus `packages/evidence-resolver/`? | **CONFLICTED / ADR** |
| `EVRES-003` | Are the current EvidenceRef and EvidenceBundle v0.2 contracts/schemas accepted profiles? | **NEEDS VERIFICATION** |
| `EVRES-004` | Which EvidenceRef shape is canonical: current paired schema or architecture proposal? | **CONFLICTED** |
| `EVRES-005` | Which EvidenceBundle shape is canonical across architecture and paired schema? | **CONFLICTED** |
| `EVRES-006` | What is the canonical resolver input contract and schema? | **UNKNOWN** |
| `EVRES-007` | What is the canonical resolver result contract and schema? | **UNKNOWN** |
| `EVRES-008` | Which local resolver status enum is accepted? | **UNKNOWN** |
| `EVRES-009` | How is review-required state represented without adding an unaccepted public outcome? | **UNKNOWN** |
| `EVRES-010` | What structured claim-scope model supports field/time/space matching? | **UNKNOWN** |
| `EVRES-011` | What registry lookup snapshot and current-head contract are accepted? | **UNKNOWN** |
| `EVRES-012` | How are lineage and supersession represented and validated? | **UNKNOWN** |
| `EVRES-013` | Which canonicalization profile produces authoritative SpecHash values? | **CONFLICTED / UNKNOWN** |
| `EVRES-014` | Should hash syntax be `sha256:` or `jcs:sha256:` in each profile? | **CONFLICTED** |
| `EVRES-015` | Should the missing EvidenceRef validator be implemented or the schema metadata changed? | **NEEDS VERIFICATION** |
| `EVRES-016` | Where should package-specific tests and fixtures live? | **NEEDS VERIFICATION** |
| `EVRES-017` | Which policy reason codes and obligations may the resolver carry? | **UNKNOWN** |
| `EVRES-018` | Which runtime/app owns registry/proof I/O? | **UNKNOWN** |
| `EVRES-019` | Which consumer is the first supported adopter? | **UNKNOWN** |
| `EVRES-020` | What correction/withdrawal invalidation flow applies to cached resolver results? | **UNKNOWN** |
| `EVRES-021` | Which CI checks block hidden I/O, unresolved evidence, and authority bypass? | **UNKNOWN** |
| `EVRES-022` | Is package-registry publication planned, and how is it separated from evidence publication? | **UNKNOWN** |
| `EVRES-023` | Can public clients be proven unable to bypass governed resolution and runtime envelopes? | **NEEDS VERIFICATION** |
| `EVRES-024` | What performance/cache behavior preserves correction and policy freshness? | **UNKNOWN** |

[Back to top](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Current request | **CONFIRMED task authority** | Update this exact README through a scoped documentation change. | Not implementation proof. |
| Prior target README | **CONFIRMED** | Existing resolver intent, local outcome vocabulary, no-network and anti-authority posture. | Planning-oriented and overstates unverified scope checks/API. |
| `packages/evidence-resolver/pyproject.toml` | **CONFIRMED** | Distribution `kfm-evidence-resolver`, version `0.0.0`. | No build backend, dependencies, discovery, Python range, or publication behavior. |
| Empty `__init__.py` | **CONFIRMED** | Python package marker exists. | No exports or runtime behavior. |
| Exact helper-file checks | **CONFIRMED bounded absence** | Selected proposed modules were not found. | Not exhaustive proof of every file. |
| Parent package/source READMEs | **CONFIRMED repository docs** | Resolver package and source-root intent. | Do not prove implementation. |
| `packages/evidence/README.md` | **CONFIRMED sibling doc** | General evidence-helper lane and anti-duplication intent. | Responsibility split remains unaccepted. |
| EvidenceRef contract/schema | **CONFIRMED paired draft surfaces** | Current fields, kind enum, optional `bundle_ref`, closed shape. | Status `PROPOSED`; no resolution behavior. |
| EvidenceBundle contract/schema | **CONFIRMED paired draft surfaces** | Current ten-field closure candidate and closed shape. | Status `PROPOSED`; no registry/current-head proof. |
| Common SpecHash contract/schema | **CONFIRMED paired draft surfaces** | Current object shape and `sha256:` value pattern; canonicalization gap. | Conflicts with architecture notation; validator behavior not relied upon here. |
| EvidenceRef fixtures | **CONFIRMED minimal family** | One valid and one invalid missing-field case. | No dedicated validator wrapper; no resolution coverage. |
| EvidenceBundle fixtures | **CONFIRMED minimal family** | One valid and one invalid missing-id case. | No cross-record resolution coverage. |
| EvidenceBundle validator | **CONFIRMED file** | Dedicated schema/fixture wrapper exists. | Not resolver implementation; not executed in this authoring step. |
| EvidenceRef validator exact path | **CONFIRMED absent** | Schema/fixture documentation mismatch is real. | Does not rule out another validator elsewhere. |
| Common schema harness | **CONFIRMED test code** | Evidence fixtures are discoverable by generic tests. | Not package-specific resolver tests. |
| Evidence resolver workflow | **CONFIRMED echo-only scaffold** | Workflow name/jobs exist. | A green run is not behavioral proof. |
| Architecture evidence-identity note | **CONFIRMED draft doc / PROPOSED implementation** | Cite-or-abstain intent, resolver trust-membrane concept, proposed identity/lineage/outcome ideas. | Predates current paired schemas and conflicts with them. |
| Directory Rules v1.4 | **CONFIRMED placement doctrine** | `packages/` is shared implementation; contracts, schemas, policy, data, runtime, tests, and release remain distinct. | Does not decide unresolved object existence or API design. |
| Indexed search | **CONFIRMED bounded search** | Did not establish resolver code or consumers. | Search is not runtime/exhaustive tree proof. |

[Back to top](#top)

---

## Status summary

`packages/evidence-resolver/src/evidence_resolver/` is a verified empty Python namespace scaffold inside distribution `kfm-evidence-resolver` version `0.0.0`. Current repository evidence provides draft EvidenceRef/EvidenceBundle contracts and closed schemas, minimal schema fixtures, a generic harness, an EvidenceBundle validator, a missing declared EvidenceRef validator, and an echo-only resolver workflow. No stable resolver API, result contract, registry adapter, package tests, consumer, runtime wiring, or production behavior is established. The next sound change is governance reconciliation plus one pure, profile-pinned candidate check—not a broad live-store resolver.

<p align="right"><a href="#top">Back to top</a></p>
