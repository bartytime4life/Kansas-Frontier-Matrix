<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-state-archives-readme
title: connectors/kansas_state_archives/ — Kansas State Archives Greenfield Compatibility Connector Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas source steward · Archives steward · Rights reviewer · Sensitivity/privacy reviewer · CARE/cultural/sovereignty reviewer · Security reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; connector-boundary; greenfield-scaffold; compatibility-path; path-and-surface-conflict; source-admission; rights-fail-closed; sensitivity-fail-closed; care-review; no-network; no-activation; no-publication
current_path: connectors/kansas_state_archives/README.md
truth_posture: CONFIRMED repository-present 0.0.0 scaffold, one Python package, README-only local test lane, placeholder descriptor, and TODO-only connector workflows / CONFLICTED compatibility class, final connector path, package scope, KSHS umbrella-versus-surface topology, SourceDescriptor authority, registry migration, and fixture routing / PROPOSED future bounded source-admission contract / UNKNOWN executable runtime, source access, activation, substantive CI coverage, deployment, and release
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 18f18960ae35155a823053466e7fce039e716c4f
  prior_blob: af6fe630e81329eaf68fbcdeb1929c3b005b7c3b
related:
  - ../README.md
  - ./pyproject.toml
  - ./src/README.md
  - ./src/kansas_state_archives/README.md
  - ./src/kansas_state_archives/descriptor.yaml
  - ./tests/README.md
  - ../kansas/README.md
  - ../../CONTRIBUTING.md
  - ../../.github/CODEOWNERS
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/README.md
  - ../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../docs/sources/catalog/kansas_state_archives.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../data/registry/sources/README.md
  - ../../control_plane/source_authority_register.yaml
  - ../../tests/README.md
  - ../../tests/fixtures/README.md
  - ../../fixtures/README.md
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
  - ../../.github/workflows/connector-gate.yml
  - ../../.github/workflows/source-descriptor-validate.yml
tags: [kfm, connectors, kansas-state-archives, kshs, archives, python, greenfield, compatibility, source-admission, source-role, rights, privacy, sensitivity, care, fixtures, no-network, fail-closed, raw, quarantine, governance]
notes:
  - 'The repository-present lane is a 0.0.0 greenfield scaffold with one kansas_state_archives package, an empty __init__.py, comment-only fetch.py and admit.py, a four-field nonconforming descriptor.yaml, and a README-only local test lane.'
  - 'The current top-level path exists, but no accepted evidence reviewed here establishes whether its compatibility class is legacy, transitional, deprecated, mirror, redirect, or retained implementation.'
  - 'The exact connectors/kansas/kshs-state-archives/ child remains proposed in repository documentation and was not established as the implemented replacement path by this update.'
  - 'The package-local descriptor is not SourceDescriptor authority, a registry record, an activation decision, a rights decision, a sensitivity decision, or release evidence.'
  - 'The connector-gate and source-descriptor-validate workflows execute TODO echo steps; green workflow completion does not prove this connector is implemented, tested, admitted, activated, or releasable.'
  - 'Only this Markdown file is in scope. No code, package metadata, descriptor, test, fixture, schema, contract, policy, registry record, workflow, receipt, source activation, path move, release object, or public artifact is created or changed.'
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas State Archives Greenfield Compatibility Connector Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Current package maturity:** repository-present `0.0.0` greenfield scaffold; no supported connector behavior  
> **Path posture:** current top-level path exists, but its compatibility class, final connector home, package scope, and migration disposition are `CONFLICTED / NEEDS VERIFICATION`  
> **Boundary:** no live network by default, no source activation, no direct lifecycle persistence, no evidence closure, no release, and no publication.

> [!WARNING]
> Directory presence, a package name, a local descriptor, a README, a pull request, a merge, a source-catalog statement, or a green TODO-only workflow is not source authority, test coverage, activation, evidence, or publication approval.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Current status](#current-status) · [Repository snapshot](#repository-snapshot) · [Path conflict](#path-and-scope-conflict) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Descriptor boundary](#descriptor-and-registry-boundary) · [Surface boundaries](#kshs-surface-boundaries) · [Validation](#validation) · [Review](#review-burden) · [Evidence](#evidence-basis) · [ADRs](#adrs-and-migration) · [Rollback](#rollback) · [Definition of done](#definition-of-done) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/kansas_state_archives/` is a repository-present source-specific implementation lane that currently contains only a non-operational Python scaffold and its documentation boundaries.

Its present purpose is to:

- make the incomplete package state visible;
- prevent placeholder code and metadata from being mistaken for an active connector;
- preserve the unresolved relationship among the top-level lane, the Kansas connector-family lane, the KSHS umbrella source brief, and proposed per-surface adapters;
- define the gates that must close before source access, parsing, admission, lifecycle handoff, or migration can be implemented;
- keep rights, privacy, sensitivity, cultural/CARE, sovereignty, precise-location, and derivative-identity decisions outside package-local convenience logic.

This README does not ratify the current snake_case slug, choose a canonical replacement path, declare one adapter sufficient for every KSHS surface, or authorize source activation.

[Back to top](#top)

---

## Authority level

**Source-specific connector scaffold under the `connectors/` responsibility root. It has no independent schema, contract, registry, policy, lifecycle, evidence, release, or publication authority.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Responsibility root | **CONFIRMED** | Source-specific fetch and admission implementation belongs under `connectors/`; authoritative contracts, schemas, registries, policies, evidence, release, and publication controls remain elsewhere. |
| Current path | **CONFIRMED** | `connectors/kansas_state_archives/` exists at the pinned base. |
| Current package | **GREENFIELD PLACEHOLDER** | Project version is `0.0.0`; the initializer is empty; fetch and admit modules contain comments only. |
| Current tests | **README-ONLY AT NAMED LANE** | The local tests README exists; conventional executable test paths were not found in the adjacent evidence pass. Differently named or unindexed tests remain `UNKNOWN`. |
| Compatibility class | **CONFLICTED** | No accepted evidence reviewed here safely establishes `legacy`, `transitional`, `deprecated`, `mirror`, `redirect`, or retained canonical implementation. |
| Final connector home | **CONFLICTED** | The top-level lane exists, `connectors/kansas/` exists, and documentation proposes per-surface Kansas children whose final implementation status remains unresolved. |
| Package scope | **CONFLICTED** | “Kansas State Archives” is used both as a KSHS umbrella and as a possible State Archives proper surface. One package must not silently collapse independently governed surfaces. |
| Descriptor authority | **NOT ESTABLISHED** | The local YAML is a nonconforming placeholder and cannot activate a source. |
| Source activation | **DENIED / NOT VERIFIED** | No conforming per-surface descriptor, authority-register entry, rights/sensitivity review, source head, access approval, or activation decision was verified. |
| Public release | **NONE** | Connector existence or successful future retrieval would not authorize a public claim, map, API payload, index, timeline, receipt, proof, release, correction, or rollback. |

[Back to top](#top)

---

## Current status

### Repository snapshot

The following snapshot is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `18f18960ae35155a823053466e7fce039e716c4f` and the directly inspected files cited in this README:

```text
connectors/kansas_state_archives/
├── README.md                         # this connector-boundary document
├── pyproject.toml                    # project kfm-connector-kansas_state_archives, version 0.0.0
├── src/
│   ├── README.md                     # source-layout boundary
│   └── kansas_state_archives/
│       ├── README.md                 # package-scaffold boundary
│       ├── __init__.py               # empty
│       ├── fetch.py                  # comment-only placeholder
│       ├── admit.py                  # comment-only placeholder
│       └── descriptor.yaml           # four-field nonconforming placeholder
└── tests/
    └── README.md                     # README-only connector-local test boundary
```

This is not an exhaustive recursive tree receipt. Broader presence and absence claims require a new repository scan at the commit under review.

### Maturity table

| Surface | Current state | Safe conclusion |
|---|---|---|
| [`pyproject.toml`](./pyproject.toml) | Name and version only. | Build backend, dependencies, Python support, package discovery, entry points, runner, and supported commands are `UNKNOWN` or undeclared. |
| [`src/`](./src/README.md) | One package child. | The layout organizes placeholders; it does not establish runtime behavior. |
| [`src/kansas_state_archives/`](./src/kansas_state_archives/README.md) | Empty initializer, comment-only fetch/admit modules, placeholder descriptor. | No source client, parser, admission decision, candidate envelope, sink, or public API exists in the inspected files. |
| [`tests/`](./tests/README.md) | Documentation boundary only at named lane. | No package behavior, coverage, pass rate, or CI discovery is proven. |
| Connector workflows | TODO-only echo steps. | Workflow execution is not substantive connector validation. |
| Source authority register | No activating entry established in the inspected evidence. | Default deny remains required. |
| Rights and sensitivity policy | General greenfield documentation surfaces. | No KSHS-specific executable rights, privacy, sensitivity, cultural/CARE, or release decision is established. |

[Back to top](#top)

---

## Path and scope conflict

The current repository evidence does not support a simple “old path versus new path” conclusion.

| Surface | Observed posture | Consequence |
|---|---|---|
| [`connectors/kansas_state_archives/`](./README.md) | Repository-present top-level scaffold. | Presence does not prove canonicality or required retention. |
| [`connectors/kansas/`](../kansas/README.md) | Repository-present Kansas source-family coordination lane. | Family context exists, but it does not itself prove an archives child is implemented. |
| `connectors/kansas/kshs-state-archives/` | Proposed in documentation; exact implementation remains unverified here. | Keep the path `PROPOSED / NEEDS VERIFICATION`; do not redirect code or delete this lane based on prose alone. |
| [Nested Kansas State Archives source-family brief](../../docs/sources/catalog/kansas/kansas-state-archives.md) | Human-facing KSHS umbrella brief with per-surface separation pressure. | Planning and source-family evidence, not machine activation authority. |
| [Legacy flat source stub](../../docs/sources/catalog/kansas_state_archives.md) | Repository-present conflicting/older source-catalog surface. | Requires explicit supersession, redirect, or migration handling; repetition does not settle authority. |

A path decision may affect imports, distribution names, source IDs, per-surface descriptors, registry records, fixtures, tests, receipts, backlinks, and lineage. Resolve it through an accepted ADR or explicit migration plan with rollback.

[Back to top](#top)

---

## What belongs here

Until path, package, and surface decisions are accepted, this lane should remain minimal.

### Documentation that belongs now

- this repository-grounded connector boundary;
- package/source-layout/test READMEs that truthfully describe the scaffold;
- migration notes tied to an accepted ADR or migration plan;
- links to authoritative contract, schema, registry, policy, test, fixture, release, and doctrine surfaces;
- bounded evidence inventories that distinguish confirmed files from proposed behavior.

### Executable material that may belong later

Only after placement, scope, descriptor authority, access, rights, sensitivity, and tests are accepted, this lane may contain narrowly owned source-specific helpers for:

- explicit opt-in transport with reviewed hosts, authentication, timeouts, retries, rate limits, byte limits, cancellation, and credential boundaries;
- source-head capture, checksums, retrieval metadata, and deterministic errors;
- source-faithful parsing that preserves surface, collection, item, record-class, source URI, date, rights, sensitivity, provenance, and derivative identity;
- independently reviewed per-surface dispatch;
- side-effect-free construction of RAW or QUARANTINE **candidates** for caller-owned orchestration;
- a compatibility shim only when a migration defines ownership, delegation, warnings, sunset criteria, tests, and rollback.

Every executable change requires offline, negative-first tests and an accepted runner before implementation maturity is claimed.

[Back to top](#top)

---

## What does not belong here

This lane must not contain, become, or imply:

- authoritative `SourceDescriptor` instances, source-authority entries, activation decisions, rights decisions, sensitivity decisions, or policy bundles;
- a second contract, schema, registry, policy, fixture, receipt, proof, catalog, release, correction, rollback, or publication authority;
- bulk KSHS exports, manuscripts, images, audiovisual media, OCR corpora, maps, private records, or unclear-rights fixture dumps;
- credentials, tokens, cookies, account data, private endpoints, access agreements, or sensitive logs;
- network access triggered by import, installation, package discovery, or default tests;
- direct writes to `data/raw/`, `data/quarantine/`, `data/receipts/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/published/`, or `release/`;
- public APIs, map layers, tiles, archive summaries, timelines, search indexes, graph projections, embeddings, or generated narratives;
- one publisher-wide source role, rights profile, sensitivity class, activation state, or citation rule;
- silent equivalence among the KSHS umbrella, State Archives proper, Kansas Memory, KHRI, publication indexes, and adjacent discovery surfaces;
- original records, digital surrogates, OCR, transcription, annotation, indexes, entity links, or generated summaries collapsed into one record class;
- living-person data, donor-restricted content, exact archaeological or sacred locations, private-land detail, infrastructure-sensitive detail, or harmful cross-source joins;
- implementation, test, CI, deployment, activation, evidence, or release claims without current proof.

[Back to top](#top)

---

## Inputs

### Current inputs

None. The inspected package declares no supported function, class, command, endpoint, configuration contract, credential variable, or fixture shape.

### Future permitted inputs

Only after governance accepts the relevant contracts and source activation, future code may consume:

- a conforming, reviewed, per-surface `SourceDescriptor` reference;
- an explicit activation state and approved access configuration;
- approved KSHS surface, collection, item, record-class, and source identifiers;
- caller-supplied bytes, files, metadata, or approved transport results;
- source URI, source-head evidence, retrieval time, checksum, run identity, and destination intent;
- rights, attribution, redistribution, privacy, sensitivity, cultural/sovereignty, CARE, access-class, and review context;
- synthetic, generated-shape-only, redacted, or explicitly rights-cleared fixtures;
- correction, withdrawal, supersession, replay, and migration context where applicable.

Missing, stale, conflicted, malformed, inactive, or unsafe trust-bearing inputs must fail closed before network access or handoff.

---

## Outputs

### Current outputs

None. The inspected package emits no source payload, parsed record, validation report, candidate envelope, receipt candidate, lifecycle write, or public artifact.

### Future permitted outputs

Future package code may return in-memory, caller-owned:

- source-faithful parse results;
- deterministic deny, abstain, hold, no-op, rate-limit, cancellation, or error outcomes;
- RAW candidates containing approved source-native bytes or references plus identity and retrieval metadata;
- QUARANTINE candidates with stable reason codes and bounded diagnostics;
- receipt candidates describing the attempted package operation without claiming evidence closure, policy approval, or release.

The package must not select or write a lifecycle sink, close an `EvidenceBundle`, catalog a claim, issue a release decision, or turn connector success into truth.

[Back to top](#top)

---

## Descriptor and registry boundary

[`src/kansas_state_archives/descriptor.yaml`](./src/kansas_state_archives/descriptor.yaml) is not a usable source authority record.

| Local field | Current posture | Required interpretation |
|---|---|---|
| `name` | Package-local placeholder | Does not settle canonical `source_id`, product identity, or umbrella-versus-surface scope. |
| `role` | Unresolved / deprecated-style alias | Must fail closed; role requires per-surface and record-class review. |
| `rights` | Unresolved | Must fail closed; upstream accessibility does not equal KFM redistribution or release clearance. |
| `sensitivity_floor` | Permissive placeholder / deprecated-style alias | Must not be read as public-safety approval while privacy, cultural/CARE, exact-location, surface identity, and review state are unresolved. |

The authoritative [SourceDescriptor contract](../../contracts/source/source_descriptor.md), [machine schema](../../schemas/contracts/v1/source/source_descriptor.schema.json), [source registry guidance](../../data/registry/sources/README.md), and [source-authority register](../../control_plane/source_authority_register.yaml) remain outside this package.

Therefore:

- do not load the package-local YAML as registry or activation authority;
- do not infer public safety from a local sensitivity alias;
- do not assign one role, rights posture, or activation state to every KSHS surface;
- do not enable transport until conforming per-surface descriptors and activation decisions exist in accepted authority surfaces;
- do not treat a descriptor as evidence that retrieved claims are true or releasable.

[Back to top](#top)

---

## KSHS surface boundaries

| Surface or derivative | Required distinction | Denied collapse |
|---|---|---|
| Kansas State Archives proper | Archival holdings and record classes require collection/item-level provenance and rights context. | One institution-wide rights or sensitivity rule. |
| Kansas Memory | Digital portal and surrogate/discovery layer. | Digitization treated as a new observation or as removal of underlying rights and provenance. |
| Kansas Historic Resources Inventory | Inventory/discovery surface with location and regulatory-context risks. | Inventory record presented as current condition, legal designation, unrestricted exact-location truth, or field verification. |
| Publication and bibliographic indexes | Discovery aids and citations. | Index entry presented as the primary source for a substantive historical claim. |
| Original record | Source object or source-faithful representation. | Collapsed with OCR, transcription, annotation, summary, or entity-resolution output. |
| OCR / transcription | Derived text with method and uncertainty. | Presented as exact source text without derivative identity and quality limits. |
| Annotation / entity link / generated summary | Interpretive derivative. | Presented as archive authority, evidence closure, or release approval. |

Institutional common ownership does not make surfaces, record classes, rights, identifiers, access mechanics, cadence, or source roles interchangeable.

[Back to top](#top)

---

## Validation

### Current validation posture

No executable package validation is established by the inspected files. The repository-wide `connector-gate` and `source-descriptor-validate` workflows currently contain TODO-only commands, so successful execution does not prove connector behavior.

### Required future checks

Before implementation maturity or activation is claimed, validation must cover:

- import and installation safety with no network or side effects;
- explicit transport injection and default-deny egress;
- descriptor rejection, activation preconditions, and source-head requirements;
- surface, collection, item, record-class, source-URI, and derivative identity preservation;
- title, creator, date, description, retrieval time, checksum, provenance, rights, and citation preservation where present;
- rights, attribution, redistribution, privacy, sensitivity, cultural, sovereignty, CARE, archaeological, private-land, and infrastructure fail-closed behavior;
- deterministic parsing and normalization without upgrading authority, confidence, or release state;
- bounded RAW/QUARANTINE candidate construction for caller-owned orchestration;
- no direct lifecycle, receipt, proof, catalog, release, or publication writes;
- error hygiene that does not echo restricted payloads, tokens, locations, or private metadata;
- compatibility/delegation behavior only after an accepted migration;
- denial of public artifacts, uncited claims, and publisher-wide surface collapse.

Package-local tests prove only package-local behavior. Canonical cross-system enforceability belongs under the root [`tests/`](../../tests/README.md) responsibility root. Test-only fixtures belong under [`tests/fixtures/`](../../tests/fixtures/README.md); shared runtime/documentation fixtures belong under [`fixtures/`](../../fixtures/README.md) according to their governing split.

[Back to top](#top)

---

## Review burden

Material implementation or activation work requires review appropriate to the affected risk:

- connector/package maintainer;
- Kansas source and archives steward;
- rights and attribution reviewer;
- privacy and sensitivity reviewer;
- cultural, sovereignty, and CARE reviewer;
- security reviewer for transport, credentials, logging, and dependency changes;
- validation/test steward;
- migration/ADR reviewer when paths, imports, source IDs, or package identity change;
- release steward only when a later change reaches release-candidate scope.

No one reviewer or successful connector operation may collapse source access, evidence, policy, and release authority into one decision.

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| This README baseline blob `af6fe630e81329eaf68fbcdeb1929c3b005b7c3b` | **CONFIRMED** | Prior v0.1 compatibility narrative and rollback lineage. | Current runtime, tests, or canonicality. |
| [`pyproject.toml`](./pyproject.toml) | **CONFIRMED** | Distribution name and `0.0.0` placeholder version. | Buildability, dependencies, runner, supported Python, or command. |
| [`src/README.md`](./src/README.md) and [package README](./src/kansas_state_archives/README.md) | **CONFIRMED** | One-package source layout and non-operational package evidence. | Source access, activation, or deployment. |
| [`tests/README.md`](./tests/README.md) | **CONFIRMED** | README-only connector-local test boundary and named absence probes from its evidence snapshot. | Exhaustive test absence or pass status. |
| [Kansas connector-family README](../kansas/README.md) | **CONFIRMED** | Repository-present Kansas coordination lane. | Implemented KSHS child or accepted migration. |
| [Nested KSHS source-family brief](../../docs/sources/catalog/kansas/kansas-state-archives.md) | **CONFIRMED document** | Per-surface separation pressure and source-family planning. | Machine activation authority or path existence. |
| [Legacy flat source stub](../../docs/sources/catalog/kansas_state_archives.md) | **CONFIRMED document** | Conflicting lineage that must be migrated explicitly. | Current canonicality. |
| SourceDescriptor contract/schema and authority surfaces | **CONFIRMED documents/files** | Required authority separation and richer source metadata. | A conforming KSHS descriptor or active entry. |
| Connector workflow files | **CONFIRMED** | TODO-only workflow content. | Substantive test coverage or policy enforcement. |
| Uploaded KFM doctrine, including Directory Rules | **CONFIRMED doctrine** | Responsibility-root placement, lifecycle law, default-deny posture, and reversible migration requirements. | Current repository behavior by itself. |

Directory Rules place source-specific implementation under `connectors/` while preserving contracts, schemas, policy, registries, tests, fixtures, lifecycle data, and release decisions in their owning responsibility roots.

[Back to top](#top)

---

## ADRs and migration

This documentation-only revision does not itself trigger a new ADR because it creates, moves, renames, or deletes no path and changes no authority boundary.

A future ADR or explicit migration plan is required before work that materially changes:

- canonical connector or package path;
- import or distribution identity;
- source-ID namespace or per-surface descriptor strategy;
- compatibility class or sunset behavior;
- losing-path redirect, mirror, deletion, or retained shim;
- fixture/test routing where a new authority home would be created;
- lifecycle, registry, schema, contract, policy, receipt, proof, release, or publication ownership.

The migration record must name affected imports, descriptors, registry entries, fixtures, tests, receipts, documentation backlinks, source IDs, rollback target, and correction strategy.

---

## Rollback

Rollback is required if this README is used to justify source activation, canonicality, direct network access, package-local authority, public release, rights/sensitivity/CARE bypass, surface collapse, derivative collapse, or direct lifecycle writes.

Rollback target for this revision:

```text
base commit: 18f18960ae35155a823053466e7fce039e716c4f
prior blob:  af6fe630e81329eaf68fbcdeb1929c3b005b7c3b
```

Before merge, close the draft PR and abandon its branch. After merge, create a transparent revert; do not rewrite shared history.

---

## Definition of done

### Documentation boundary — this revision

- [x] Current package and test maturity are bounded to directly inspected evidence.
- [x] Path and surface conflicts are recorded without selecting an unverified winner.
- [x] Package-local descriptor authority is denied.
- [x] Inputs, outputs, exclusions, validation, review, migration, and rollback boundaries are explicit.
- [x] Remote badge dependencies and unresolved rollback placeholders are removed.
- [x] Only this README is changed.

### Connector implementation — not complete

- [ ] Accepted connector/package/surface topology and migration disposition.
- [ ] Conforming per-surface descriptors and source-authority entries.
- [ ] Reviewed access method, terms, attribution, redistribution, cadence, and source-head behavior.
- [ ] Executable rights, privacy, sensitivity, cultural/CARE, sovereignty, and precise-location policy.
- [ ] Accepted build/install/runtime/test contracts and dependency review.
- [ ] Offline synthetic or rights-cleared fixtures with generation and expected-outcome records.
- [ ] Negative-first import, network, descriptor, activation, surface, derivative, metadata, rights, sensitivity, error, migration, and publication-denial tests.
- [ ] Caller-owned RAW/QUARANTINE candidate and receipt-candidate contracts.
- [ ] Substantive CI discovery and observed passing results.
- [ ] Activation review, evidence closure, release review, correction path, and rollback target where later applicable.

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Final connector, package, import, source-ID, and test path | **NEEDS VERIFICATION** | Accepted ADR or migration record plus current repository tree. |
| Exact compatibility class and losing-path disposition | **UNKNOWN** | Explicit decision, owners, sunset conditions, tests, and rollback. |
| KSHS umbrella versus per-surface adapter strategy | **NEEDS VERIFICATION** | Source steward review and conforming per-surface descriptors. |
| Complete recursive package inventory | **NEEDS VERIFICATION** | Commit-pinned recursive tree. |
| Build, install, dependency, runtime, and runner contracts | **UNKNOWN** | Complete package metadata and executable commands. |
| Current KSHS access methods, schemas, terms, cadence, and source heads | **NEEDS VERIFICATION** | Current official source review and activation record. |
| Rights, privacy, sensitivity, cultural, sovereignty, CARE, derivative, and exact-location posture | **NEEDS VERIFICATION** | Policy decisions, fixtures, tests, and reviewer records. |
| Fixture homes, generation notes, payloads, and expected outcomes | **UNKNOWN** | Fixture registry and consuming tests. |
| RAW/QUARANTINE candidate and receipt-candidate contracts | **PROPOSED** | Accepted contracts, schemas, tests, and caller-owned orchestration. |
| Substantive CI coverage | **UNKNOWN** | Non-placeholder workflows, logs, and observed results. |
| Legacy flat catalog-stub supersession | **NEEDS VERIFICATION** | Redirect, supersession notice, migration PR, and backlink update. |
| Activation, deployment, release, correction, and rollback state | **NOT ESTABLISHED** | Reviewed receipts, manifests, policy decisions, and runtime evidence. |

[Back to top](#top)
