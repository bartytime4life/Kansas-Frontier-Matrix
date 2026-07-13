<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-memory-src-readme
title: connectors/kansas_memory/src/ — Kansas Memory Compatibility Source Layout Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Archives steward · Package maintainer · Test steward · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-12
policy_label: public-doctrine; src-layout-boundary; noncanonical-compatibility-lane; placeholder-runtime; no-network-default; rights-fail-closed; sensitivity-fail-closed; no-activation; no-publication
current_path: connectors/kansas_memory/src/README.md
truth_posture: CONFIRMED current source-layout and package scaffold / CONFLICTED final package placement and SourceDescriptor authority / PROPOSED source-layout contract / UNKNOWN runtime, tests, activation, and CI depth
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 8df2275382850b805c9ebc83a3dc7f4a2dd2169a
  prior_blob: 560f32827da03a8b052e47d10d7e694788574ee3
related:
  - ../../README.md
  - ../README.md
  - kansas_memory/README.md
  - ../tests/README.md
  - ../pyproject.toml
  - ../../kansas/README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/kansas/kansas-memory.md
  - ../../../docs/sources/catalog/kansas_memory.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../data/registry/sources/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../data/raw/archives/
  - ../../../data/quarantine/archives/
  - ../../../data/receipts/
  - ../../../release/
tags: [kfm, connectors, kansas-memory, src, python, package-layout, compatibility, placeholder, source-admission, rights, sensitivity, raw, quarantine, receipts, governance]
notes:
  - "The inspected src layout contains this README and one kansas_memory package directory."
  - "The package directory contains README.md, an empty __init__.py, one-line admit.py and fetch.py placeholders, and a four-field descriptor.yaml placeholder."
  - "The parent pyproject.toml declares project name kfm-connector-kansas_memory and version 0.0.0 only; it does not prove a buildable or runnable package."
  - "The package-local descriptor is not a governed SourceDescriptor, registry record, activation decision, rights decision, sensitivity decision, or release authority."
  - "Only this Markdown file is in scope. No code, package metadata, descriptor, registry record, fixture, test, policy, schema, workflow, receipt, source activation, path move, release object, or public artifact is created or changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas Memory Compatibility Source Layout Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft`  
> **Component maturity:** repository-present source-layout scaffold; executable behavior `UNKNOWN`  
> **Owner:** `OWNER_TBD`  
> **Truth posture:** `CONFIRMED` current layout and placeholder bytes · `CONFLICTED` final package placement and descriptor authority · `PROPOSED` source-layout contract  
> **Boundary:** implementation-package organization only. This layout does not activate Kansas Memory, decide source role or rights, classify material as public, establish historical truth, publish archive content, serve public clients, or authorize release.

> [!WARNING]
> The package-local `kansas_memory/descriptor.yaml` is an unsafe placeholder, not authority. It contains unresolved `role` and `rights` values and a `public` sensitivity floor. Code and operators must fail closed rather than use it as a descriptor, activation, rights, sensitivity, or release decision.

**Quick links:** [Purpose](#purpose) · [Authority level](#authority-level) · [Status](#status) · [Directory map](#current-repository-snapshot-and-directory-map) · [Inputs](#inputs) · [Outputs](#outputs) · [Allowed contents](#allowed-contents) · [Exclusions](#exclusions) · [Runtime boundary](#runtime-and-admission-boundary) · [Validation](#validation) · [Maintenance](#maintenance-and-definition-of-done) · [Related folders](#related-folders) · [Evidence](#evidence-basis) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

<a id="scope"></a>

## Purpose

`connectors/kansas_memory/src/` is the source-layout container for the repository-present `kansas_memory` Python package scaffold inside the noncanonical `connectors/kansas_memory/` compatibility lane.

Its permitted future responsibility is narrow: organize connector-local code that preserves admitted Kansas Memory source identity, parses explicitly approved material without upgrading its meaning, and returns auditable candidates to caller-owned `RAW`, `QUARANTINE`, or process-memory receipt handling.

This directory is not a second connector root, source catalog, governed registry, contract or schema home, policy engine, evidence-closure service, public API, search index, release workflow, or publication surface.

The current bytes prove only that a layout and package scaffold exist. They do not prove a working connector, valid descriptor, safe endpoint, installable package, parser, tests, source activation, or runtime behavior.

[Back to top](#top)

---

<a id="repo-fit"></a>

## Authority level

**Implementation source layout inside a noncanonical compatibility lane; final migration class and canonical package home remain unresolved.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Responsibility root | **CONFIRMED** | Source-specific fetch and admission implementation belongs under `connectors/`. This layout cannot own source doctrine, registry, policy, proof, or release authority. |
| Current `src/` path | **CONFIRMED** | `connectors/kansas_memory/src/` exists at the pinned base and contains the paths listed below. |
| Parent path posture | **CONFIRMED / NONCANONICAL** | The parent README describes `connectors/kansas_memory/` as a compatibility lane rather than the canonical Kansas-family implementation. |
| Canonical family | **CONFIRMED** | `connectors/kansas/` is the current Kansas source-family coordination lane. |
| Final Kansas Memory child | **CONFLICTED / NEEDS VERIFICATION** | Source documentation proposes `connectors/kansas/kansas-memory/`, but that exact README path was absent at the pinned base. No accepted path-specific migration decision was verified. |
| Package implementation | **PLACEHOLDER / NOT RUNTIME EVIDENCE** | The package initializer is empty; `admit.py` and `fetch.py` are one-line placeholders; package metadata contains only a name and version `0.0.0`. |
| Local descriptor | **PLACEHOLDER / DENY FOR AUTHORITY USE** | `descriptor.yaml` is connector-local scaffolding, not a governed registry instance or activation decision. |
| Tests and fixtures | **UNKNOWN** | A test-contract README exists, but conventional package test paths probed at the pinned base were absent. No package test run was verified. |
| Source access and activation | **UNKNOWN / DISABLED BY DEFAULT** | No approved endpoint, access method, terms review, source head, or activation record was verified. |
| Policy and publication authority | **NONE** | Rights, sensitivity, CARE/sovereignty, privacy, evidence closure, release, correction, withdrawal, and rollback remain outside this layout. |

This README records the real scaffold. It does not ratify the underscore slug, create the proposed Kansas-family child, convert the local descriptor into authority, or establish an operational archive connector.

[Back to top](#top)

---

## Status

| Item | Status | Meaning |
|---|---:|---|
| This README | **DRAFT v0.2** | Reviewable source-layout boundary; not source activation or KFM publication. |
| Source-layout directory | **CONFIRMED** | Current path exists at base `8df2275382850b805c9ebc83a3dc7f4a2dd2169a`. |
| Child package | **CONFIRMED SCAFFOLD** | The `kansas_memory/` directory and five directly inspected package files exist. |
| Package code | **GREENFIELD PLACEHOLDERS** | No executable admission or fetch behavior is established by the inspected files. |
| Package metadata | **PLACEHOLDER** | Project name and version exist; build backend, dependencies, package discovery, entry points, and supported Python version were not verified. |
| Governed `SourceDescriptor` | **NOT VERIFIED** | Proposed registry paths were absent and the inspected source-authority register had no entries. |
| Descriptor schema authority | **CONFLICTED** | The populated singular schema declares itself legacy while the nominal plural schema is an empty scaffold. |
| Rights and redistribution | **NEEDS VERIFICATION** | Public availability does not establish reuse, redistribution, AI use, or item-class licensing. |
| Sensitivity and CARE | **REVIEW REQUIRED / FAIL CLOSED** | Archive material may implicate living persons, archaeology, sacred or culturally sensitive places, private land, precise locations, or restricted source content. |
| Runtime, tests, CI, and deployment | **UNKNOWN** | No package build, import, parser test, connector run, emitted receipt, or deployment was verified. |
| Public output | **NONE** | This layout creates no public archive claim, map, timeline, search result, API response, or released artifact. |

[Back to top](#top)

---

<a id="expected-layout"></a>

## Current repository snapshot and directory map

The following map is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `8df2275382850b805c9ebc83a3dc7f4a2dd2169a` and the exact paths inspected for this update.

```text
connectors/kansas_memory/src/
├── README.md
└── kansas_memory/
    ├── README.md
    ├── __init__.py        # CONFIRMED empty
    ├── admit.py           # CONFIRMED one-line greenfield placeholder
    ├── fetch.py           # CONFIRMED one-line greenfield placeholder
    └── descriptor.yaml    # CONFIRMED four-field unsafe placeholder
```

The parent package metadata at `connectors/kansas_memory/pyproject.toml` contains only:

```toml
[project]
name = "kfm-connector-kansas_memory"
version = "0.0.0"
```

This bounded map corrects the v0.1 statement that only the two README files were confirmed. It does not claim an exhaustive recursive tree or rule out differently named or unindexed files.

| File | Current bytes | What the file does not prove |
|---|---|---|
| `README.md` | This source-layout contract. | Package implementation or activation. |
| `kansas_memory/README.md` | Draft package-boundary documentation. | Executable modules, valid configuration, tests, or CI. |
| `kansas_memory/__init__.py` | Empty file. | Import API, version export, initialization, or side-effect safety. |
| `kansas_memory/admit.py` | One comment identifying a greenfield admission gate placeholder. | Admission decisions, validation, finite outcomes, or writes. |
| `kansas_memory/fetch.py` | One comment identifying a greenfield fetcher placeholder. | Endpoint support, networking, authentication, retries, or rate limits. |
| `kansas_memory/descriptor.yaml` | `name`, unresolved `role`, unresolved `rights`, and `sensitivity_floor: public`. | Schema validity, registry authority, activation, rights approval, sensitivity approval, or public-release safety. |

[Back to top](#top)

---

## Inputs

### Current implementation

No callable package input contract is implemented by the inspected files.

### Permitted future inputs

Future code may accept only evidence-bounded, caller-supplied inputs whose exact contracts are approved, such as:

- a governed `SourceDescriptor` reference and explicit activation state;
- source-head identity, retrieval time, collection and item identifiers, and source URI;
- source bytes or metadata already obtained through an approved access path;
- rights, attribution, redistribution, sensitivity, privacy, and CARE/cultural-review context;
- bounded parser configuration and caller-owned handoff context;
- synthetic or explicitly reviewed fixtures that cannot be mistaken for released archive records.

The package must not infer missing authority from a filename, host, collection title, local YAML field, public web page, or prior successful fetch.

[Back to top](#top)

---

## Outputs

### Current implementation

The inspected placeholder modules emit no output.

### Permitted future outputs

Future code may return in-memory, caller-owned candidates for:

- `RAW` admission when descriptor, activation, identity, provenance, rights, and source-head requirements are satisfied;
- `QUARANTINE` when required evidence or policy state is missing, conflicted, stale, malformed, or unsafe;
- structured `DENY`, `ABSTAIN`, or `ERROR` outcomes with stable reason codes;
- process-memory receipt candidates that record fetch, parse, validation, and handoff decisions.

The package must not write directly to `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`, proof, release, correction, withdrawal, or public-delivery surfaces. A connector result is not an `EvidenceBundle`, verified historical claim, release approval, or publication event.

[Back to top](#top)

---

<a id="allowed-contents"></a>

## Allowed contents

Subject to accepted placement and contracts, this `src/` layout may contain:

- one Python package directory and package-local boundary documentation;
- small source-client modules with network access disabled by default;
- parsers and normalizers that preserve source-native identity and meaning;
- validation and finite-outcome helpers;
- caller-owned `RAW` or `QUARANTINE` candidate builders;
- process-memory receipt-candidate builders;
- deterministic errors and reason codes;
- compatibility shims with an explicit migration and deprecation contract.

Any implementation must remain small, deterministic, reviewable, and reversible. New modules require corresponding tests and must not create a parallel authority home.

[Back to top](#top)

---

<a id="forbidden-contents"></a>

## Exclusions

Do not place or authorize the following under this layout:

- canonical contracts, schemas, source registry records, or activation decisions;
- rights, sensitivity, privacy, consent, CARE/sovereignty, or release policy authority;
- source payload archives or bulk fixture corpora;
- credentials, tokens, cookies, session state, or private endpoints;
- live-source jobs enabled by import, installation, or default test execution;
- direct writes to downstream lifecycle, proof, receipt-authority, release, or public stores;
- public APIs, maps, tiles, search indexes, timelines, summaries, or generated narratives;
- OCR or transcription presented as the source image, metadata presented as historical truth, or generated text presented as evidence;
- code that treats `connectors/kansas_memory/` as canonical without accepted migration evidence;
- a second package, descriptor, registry, contract, schema, policy, or release authority created for convenience.

Fixtures belong in an accepted fixture or test lane and require explicit rights and sensitivity review. Bulk or sensitive archive material must not be committed as package data.

[Back to top](#top)

---

<a id="runtime-posture"></a>

## Runtime and admission boundary

The current placeholder files do not implement or enforce a runtime posture. Any future implementation must satisfy all of the following before source access:

1. Resolve the final package path and compatibility class.
2. Resolve one governed descriptor, schema, registry, and validator authority.
3. Verify source identity, access method, terms, rights, attribution, cadence, and source head.
4. Record sensitivity, privacy, living-person, archaeology, cultural/sovereignty, CARE, private-land, and precise-location posture.
5. Require an explicit activation decision.
6. Use an opt-in, bounded, credential-safe, rate-limited source client.
7. Preserve collection, item, component, page, scan, file, OCR, and transcription identities without truth upgrade.
8. Return a finite admission outcome and process-memory receipt candidate.
9. Leave evidence closure, policy enforcement, cataloging, release, correction, withdrawal, and public delivery to their owning systems.

Default outcomes:

| Condition | Required outcome |
|---|---|
| Descriptor or activation missing | `DENY` or `ABSTAIN`; no network. |
| Role, rights, or sensitivity unresolved | `QUARANTINE` or `DENY`; never accept the local placeholder as authority. |
| Source identity or item identity ambiguous | `QUARANTINE`; preserve candidate evidence. |
| Source head changed unexpectedly | `QUARANTINE` or structured no-op/drift outcome; do not overwrite lineage. |
| Parser shape drift | `QUARANTINE` or `ERROR`; retain bounded diagnostic evidence. |
| Approved unchanged source | Deterministic no-op receipt candidate. |
| Valid admitted source | Caller-owned `RAW` candidate only. |
| Public release requested | Refuse; release is outside this layout. |

[Back to top](#top)

---

## Validation

### Current documentation checks

This revision must preserve:

- the existing document ID and creation date;
- one H1 and logical heading order;
- the KFM meta block and final newline;
- relative links that resolve from `connectors/kansas_memory/src/`;
- the actual package scaffold and placeholder status;
- visible uncertainty, conflicts, ownership gaps, and rollback identifiers;
- no remote badges, tracking images, credentials, source payloads, personal data, or sensitive locations;
- a one-file Markdown diff with no code, descriptor, schema, policy, registry, workflow, or release changes.

### Required future package checks

Before any implementation maturity is claimed, tests must prove:

- imports perform no network, filesystem write, registration, logging of secrets, or source activation;
- the local placeholder descriptor is rejected as authority;
- missing or conflicted descriptor, activation, rights, sensitivity, and CARE state fail closed;
- source, collection, item, component, page, scan, file, OCR, and transcription identities are preserved;
- metadata, OCR, transcription, entity resolution, and generated summaries do not silently upgrade truth status;
- malformed inputs, schema drift, ambiguous identity, stale source heads, and unsafe content route to finite fail-closed outcomes;
- outputs remain caller-owned `RAW`, `QUARANTINE`, or receipt candidates;
- no code writes to downstream lifecycle, proof, release, correction, or public surfaces;
- network tests are opt-in, isolated, credential-safe, terms-reviewed, rate-limited, and excluded from default CI;
- migration shims, if retained, have tests, warnings, ownership, sunset criteria, and rollback coverage.

Passing repository-wide documentation or policy checks does not prove this package is implemented, activated, or safe for live source access.

[Back to top](#top)

---

## Maintenance and definition of done

This README is ready for documentation review when:

- [x] The pinned base, prior blob, current path, and review date are recorded.
- [x] The real `src/` and package scaffold replaces the stale two-README-only map.
- [x] Current placeholder code and package metadata are distinguished from runtime implementation.
- [x] The local descriptor is explicitly denied authority.
- [x] Scope, repository fit, inputs, outputs, inclusions, exclusions, runtime boundary, validation, maintenance, evidence, rollback, and backlog are present.
- [x] Rights, sensitivity, CARE, privacy, archive-meaning, and publication boundaries fail closed.
- [ ] An accepted ADR or migration record selects the final Kansas Memory package path and compatibility class.
- [ ] The package-local descriptor is removed, converted to a clearly labeled fixture, or replaced through an accepted governed migration.
- [ ] One enforceable descriptor contract, schema, registry, and validator authority is accepted.
- [ ] A product-level descriptor, source ID, source-head strategy, review state, and activation decision exist.
- [ ] Access method, terms, rights, attribution, redistribution, cadence, correction, withdrawal, and supersession are verified.
- [ ] Package build metadata, import surface, dependencies, entry points, and supported runtime are implemented.
- [ ] Safe valid and invalid fixtures plus no-network tests cover all fail-closed cases.
- [ ] Output envelopes, sinks, reason codes, receipts, idempotency, retries, replay, and drift behavior are accepted and tested.
- [ ] Connector-specific owners and required reviewers are assigned.

Documentation readiness does not imply package readiness, source activation, evidence closure, rights approval, sensitive-data approval, or public release.

[Back to top](#top)

---

## Related folders

| Surface | Relationship | Status at the pinned base |
|---|---|---:|
| [`../../README.md`](../../README.md) | Connector-root admission and lifecycle boundary. | **CONFIRMED file** |
| [`../README.md`](../README.md) | Parent Kansas Memory compatibility lane. | **CONFIRMED / noncanonical** |
| [`kansas_memory/README.md`](kansas_memory/README.md) | Child package boundary. | **CONFIRMED file / v0.1 at base** |
| [`../tests/README.md`](../tests/README.md) | Intended no-network test contract. | **CONFIRMED README / tests unverified** |
| [`../pyproject.toml`](../pyproject.toml) | Package metadata scaffold. | **CONFIRMED placeholder / version 0.0.0** |
| [`../../kansas/README.md`](../../kansas/README.md) | Kansas source-family coordination lane. | **CONFIRMED / child topology provisional** |
| `../../kansas/kansas-memory/README.md` | Source-profile-proposed child path. | **CONFIRMED exact path absent** |
| [`../../../docs/sources/catalog/kansas/kansas-memory.md`](../../../docs/sources/catalog/kansas/kansas-memory.md) | Current nested human-facing source profile. | **CONFIRMED draft / implementation claims bounded** |
| [`../../../docs/sources/catalog/kansas_memory.md`](../../../docs/sources/catalog/kansas_memory.md) | Older flat source-catalog stub. | **CONFIRMED lineage / path drift** |
| [`../../../data/registry/sources/README.md`](../../../data/registry/sources/README.md) | Governed source-registry responsibility. | **CONFIRMED README / exact product entry unverified** |
| [`../../../control_plane/source_authority_register.yaml`](../../../control_plane/source_authority_register.yaml) | Machine source-authority register. | **CONFIRMED file / no inspected Kansas Memory entry** |
| [`../../../policy/rights/`](../../../policy/rights/) | Rights and reuse decisions. | **Outside layout** |
| [`../../../policy/sensitivity/`](../../../policy/sensitivity/) | Sensitivity, privacy, redaction, and CARE-adjacent controls. | **Outside layout** |
| [`../../../data/raw/archives/`](../../../data/raw/archives/) | Potential caller-owned admitted capture surface. | **Outside layout / exact shape unverified** |
| [`../../../data/quarantine/archives/`](../../../data/quarantine/archives/) | Potential caller-owned hold surface. | **Outside layout / exact reason shape unverified** |
| [`../../../data/receipts/`](../../../data/receipts/) | Process-memory receipts. | **Outside layout** |
| [`../../../release/`](../../../release/) | Release, correction, withdrawal, and rollback controls. | **Outside layout** |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence basis

| Evidence | What it supports | What it does not prove |
|---|---|---|
| Target blob `560f32827da03a8b052e47d10d7e694788574ee3` | Exact v0.1 edit baseline, stale inventory, remote badges, and rollback placeholder. | Runtime or source readiness. |
| Direct reads of the child package files | Empty initializer, one-line code placeholders, and four-field local descriptor. | Executable behavior, complete recursive inventory, or safe configuration. |
| Parent `pyproject.toml` | Project name and version `0.0.0`. | Installability, build behavior, dependencies, or entry points. |
| Parent, package, tests, and Kansas-family READMEs | Compatibility posture, intended no-network boundary, and provisional child topology. | Accepted migration or executable behavior. |
| Current nested and older flat source-catalog pages | Source-family meaning and unresolved catalog/path lineage. | Machine descriptor, activation, endpoint, terms, or source-role approval. |
| Populated singular and empty plural descriptor schemas | Descriptor-shape and schema-home conflict. | One accepted machine authority. |
| Direct proposed-path and conventional-test probes | Named paths were absent at the pinned base. | Absence of every differently named or unindexed file. |
| Directory Rules and connector-root README | Responsibility root, compatibility discipline, README contract, and connector output boundary. | Product activation or package runtime. |
| Contribution guidance and CODEOWNERS | Smallest reversible change, truth labels, and repository-wide fallback ownership. | Actual steward assignment or approval. |

Absence claims are bounded to exact paths, indexed search, and the pinned commit. This README does not assert a complete recursive repository inventory.

[Back to top](#top)

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, canonical status, local-descriptor authority, direct downstream writes, public archive claims, rights or sensitivity bypass, or implementation maturity without verified code and tests.

Before merge, rollback is to leave the review branch unmerged and abandon the proposed change. Closing the pull request or deleting its branch requires separate authorization.

After merge, restore prior README blob `560f32827da03a8b052e47d10d7e694788574ee3` from base `8df2275382850b805c9ebc83a3dc7f4a2dd2169a` through a transparent revert commit or revert pull request, then rerun applicable documentation and connector-boundary validation. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Resolve canonical package path and compatibility class. | **CONFLICTED** | Accepted ADR or migration record, import/reference inventory, deprecation entry, tests, and rollback plan. |
| Reconcile underscore and hyphen source/package slugs. | **CONFLICTED** | Stable identity decision and compatibility map. |
| Reconcile flat and nested Kansas Memory source-catalog pages. | **CONFLICTED** | Docs-owner migration and redirect/deprecation treatment. |
| Decide disposition of package-local `descriptor.yaml`. | **NEEDS VERIFICATION** | Registry, package, contract, schema, policy, and migration review. |
| Resolve descriptor schema, registry, and validator authority. | **CONFLICTED** | Accepted ADR/contract, one enforceable schema, validator entry point, fixtures, and migration. |
| Create and validate a governed product descriptor and authority entry. | **NEEDS VERIFICATION** | Registry record, source ID, review state, activation state, validation report, and control-plane linkage. |
| Confirm current Kansas Memory access method and source head. | **NEEDS VERIFICATION** | Current authoritative source documentation and steward review. |
| Confirm rights, attribution, redistribution, AI use, and item-class restrictions. | **NEEDS VERIFICATION** | Rights review and policy tests. |
| Confirm sensitivity, privacy, living-person, cultural, sovereignty, CARE, archaeology, private-land, and precise-place rules. | **NEEDS VERIFICATION** | Policy, steward review, transforms, negative fixtures, and receipts. |
| Confirm package build, import, dependency, configuration, and network behavior. | **UNKNOWN** | Package implementation and observed tests. |
| Define outputs, sinks, outcomes, reason codes, receipts, retries, idempotency, replay, and drift handling. | **NEEDS VERIFICATION** | Accepted contracts, schemas, policy, fixtures, and runtime tests. |
| Confirm fixture home, fixture rights, and no-network coverage. | **UNKNOWN** | Fixture registry, review receipts, test files, and logs. |
| Assign package and connector owners and reviewers. | **UNKNOWN** | CODEOWNERS or accepted ownership records. |

[Back to top](#top)

---

## Maintainer note

Keep `src/` boring: one explicit package, no hidden side effects, no bundled source payloads, and no authority encoded by convenience. Until governance resolves the final package home and descriptor controls, preserve this layout as a small, visible compatibility scaffold.

When implementation begins, make the smallest proof-bearing slice offline first: a synthetic or explicitly approved fixture, deterministic identity preservation, local-placeholder rejection, fail-closed rights and sensitivity behavior, and a caller-owned quarantine outcome. Only then add a reviewed source-access path. Evidence closure, historical interpretation, cataloging, release approval, public delivery, correction, withdrawal, and rollback remain outside this layout.

[Back to top](#top)
