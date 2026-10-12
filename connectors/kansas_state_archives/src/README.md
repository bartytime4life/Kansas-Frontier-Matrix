<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-state-archives-src-readme
title: connectors/kansas_state_archives/src/ — Kansas State Archives Greenfield Source Layout
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas source steward · Archives steward · Rights reviewer · Sensitivity/privacy reviewer · CARE/cultural/sovereignty reviewer · Security reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; source-layout; greenfield-scaffold; compatibility-path; path-and-surface-conflict; source-admission; rights-fail-closed; sensitivity-fail-closed; care-review; no-network; no-activation; no-publication
current_path: connectors/kansas_state_archives/src/README.md
truth_posture: CONFIRMED one-package source layout and 0.0.0 placeholder scaffold / CONFLICTED compatibility class, final connector path, package identity, KSHS umbrella-versus-surface scope, SourceDescriptor authority, and local sensitivity floor / PROPOSED future admission contract / UNKNOWN executable tests, CI discovery, runtime, activation, source access, and deployment
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: f9b54aaade4bea73805537f35fcdb458ea58463b
  prior_blob: 2614b6cc6a23755fc5fe537c5cef66570b1325f0
related:
  - ../../README.md
  - ../README.md
  - ../pyproject.toml
  - ../tests/README.md
  - ./kansas_state_archives/README.md
  - ../../kansas/README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../../docs/sources/catalog/kansas_state_archives.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../data/registry/sources/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../docs/adr/README.md
tags: [kfm, connectors, kansas-state-archives, kshs, archives, src, python, package-layout, greenfield, compatibility, source-admission, rights, sensitivity, privacy, care, raw, quarantine, no-network, no-publication]
notes:
  - "Direct reads at base commit f9b54aaade4bea73805537f35fcdb458ea58463b confirm this README and one kansas_state_archives package directory under src/."
  - "The package directory contains a v0.2 package README, an empty __init__.py, comment-only fetch.py and admit.py files, and a four-field descriptor.yaml placeholder."
  - "The parent pyproject.toml declares project name kfm-connector-kansas_state_archives and version 0.0.0 only; it does not prove a buildable, installable, or runnable package."
  - "The exact proposed connectors/kansas/kshs-state-archives/README.md path is absent at the pinned base; current docs conflict among the top-level compatibility lane, the Kansas family lane, the nested KSHS umbrella brief, and the legacy flat catalog stub."
  - "The package-local descriptor is not a conforming SourceDescriptor, registry record, activation decision, rights decision, sensitivity decision, or release authority."
  - "Only this Markdown file is in scope. No code, package metadata, descriptor, registry record, fixture, test, policy, schema, workflow, receipt, source activation, path move, release object, or public artifact is created or changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas State Archives Greenfield Source Layout

> Source-layout boundary for the repository-present Python scaffold at `connectors/kansas_state_archives/src/`. This directory organizes one non-operational `kansas_state_archives` package inside an unresolved compatibility lane. It is not a connector authority, source registry, policy engine, lifecycle store, public API, or publication surface.

**Status:** `draft v0.2` · `CONFIRMED one-package scaffold` · `CONFLICTED connector/package/surface placement` · `no supported command` · `no activation` · `no publication`

> [!IMPORTANT]
> The current source layout contains real placeholder files, not merely two READMEs. The package initializer is empty, `fetch.py` and `admit.py` contain comments only, and `descriptor.yaml` is a four-field nonconforming placeholder. No executable source-admission behavior is established.

> [!WARNING]
> Do not add a second import package, operational client, live-source job, or migration shim under this `src/` directory until the repository resolves the connector path, compatibility class, KSHS umbrella-versus-surface scope, package identity, source-ID strategy, and losing-path disposition.

**Quick links:** [Purpose](#purpose) · [Authority level](#authority-level) · [Status](#status) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review burden](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Current layout](#current-layout) · [Descriptor boundary](#descriptor-boundary) · [Surface boundaries](#kshs-surface-boundaries) · [Runtime boundary](#runtime-and-admission-boundary) · [Evidence](#evidence-basis) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/kansas_state_archives/src/` is a Python source-layout container. Its only confirmed child package is `kansas_state_archives/`, and that package is a `0.0.0` greenfield scaffold.

The layout may eventually organize narrow, source-specific code that:

- consumes caller-supplied, approved KSHS archive material or an explicitly reviewed transport result;
- preserves KSHS surface identity, collection identity, item identity, source URI, source role, rights, privacy, sensitivity, cultural/CARE posture, provenance, dates, geometry, uncertainty, access method, and source vintage;
- distinguishes original records from digital surrogates, OCR, transcription, annotation, entity resolution, indexes, and generated summaries;
- returns deterministic parse, validation, denial, abstention, hold, or RAW/QUARANTINE candidate results to caller-owned orchestration;
- supports a compatibility import only if an accepted migration explicitly retains `kansas_state_archives`.

This directory cannot decide which connector path is canonical, collapse every KSHS surface into one product, activate a source, make the package descriptor authoritative, write lifecycle state, close evidence, approve release, or publish archive-derived claims.

---

## Authority level

**Implementation source layout inside a repository-present compatibility scaffold. The exact compatibility class, final connector home, package identity, and per-surface topology remain unresolved.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Responsibility root | `CONFIRMED` | Source-specific fetch and admission implementation belongs under `connectors/`; registry, contract, schema, policy, evidence, release, and publication authority remain elsewhere. |
| Current `src/` path | `CONFIRMED` | This README and one `kansas_state_archives/` package child exist at the pinned base. |
| Current package name | `CONFIRMED scaffold / CONFLICTED final` | The live import directory is `kansas_state_archives` and project metadata is `kfm-connector-kansas_state_archives`; neither is ratified as the final product identity or compatibility import. |
| Compatibility class | `CONFLICTED` | Evidence does not safely establish `legacy`, `transitional`, `deprecated`, `mirror`, or `external-export`. |
| Final connector path | `CONFLICTED` | The top-level lane exists, the Kansas family lane exists, and repository docs propose per-surface Kansas children whose final homes remain unresolved. |
| Proposed Kansas child | `CONFIRMED absent at base` | An exact read of `connectors/kansas/kshs-state-archives/README.md` returned `404`; source-catalog prose does not make the path present. |
| Package implementation | `GREENFIELD PLACEHOLDER` | Empty initializer and comment-only fetch/admit modules establish no supported behavior. |
| Package-local descriptor | `NONCONFORMING / DENY FOR AUTHORITY USE` | Four minimal or unresolved fields do not satisfy the richer `SourceDescriptor` contract and cannot activate a source. |
| Tests and fixtures | `README-ONLY AT INSPECTED PATH / OTHERWISE UNKNOWN` | The connector-local test README exists; executable package coverage, fixtures, and CI discovery were not established by this review. |
| Source access and activation | `UNKNOWN / DISABLED BY DEFAULT` | No approved endpoint, transport, credential mode, terms review, source head, per-surface descriptor, or activation decision was verified. |
| Public output | `NONE` | The layout creates no public map, API response, archive claim, timeline, search index, release artifact, or published record. |

This README records repository state and safe layout constraints. It does not ratify the current snake_case slug, create a Kansas-family child, choose one adapter for every KSHS surface, or authorize implementation.

---

## Status

| Item | Current state | What that means |
|---|---|---|
| This README | `DRAFT v0.2` | Reviewable layout boundary, not runtime evidence or KFM publication. |
| Source-layout directory | `CONFIRMED` | One package child was directly inspected. |
| Project metadata | `0.0.0 PLACEHOLDER` | Name and version only; build backend, dependencies, supported Python, package discovery, and entry points are not declared. |
| Package initializer | `EMPTY` | No package API, version export, registration, or initialization behavior. |
| Fetch and admit modules | `COMMENT-ONLY` | No endpoint access, parser, validator, finite outcome, receipt, or handoff. |
| Local descriptor | `UNSAFE PLACEHOLDER` | Unresolved role and rights plus `sensitivity_floor: public`; it must fail closed. |
| Source authority register | `PROPOSED / EMPTY` | The inspected register contains `entries: []`; no KSHS archive activation record is established. |
| Rights and sensitivity policy | `GREENFIELD STUBS` | No executable KSHS-specific rights, privacy, sensitivity, cultural/CARE, or public-release policy is established. |
| Runtime, tests, CI, deployment | `ABSENT or UNKNOWN` | A README, merged PR, or green repository-wide check does not prove this package is implemented or activated. |
| Public release | `DENY BY DEFAULT` | Connector presence, archive access, or upstream public availability does not authorize KFM release. |

---

## What belongs here

Subject to an accepted path, package, and surface decision, this `src/` layout may contain:

- one Python import package;
- package-local implementation-boundary documentation;
- narrow surface-dispatch, parse, normalize, validation, and source-head helpers;
- explicit opt-in transport behind reviewed host, timeout, retry, rate-limit, byte-limit, cancellation, and credential controls;
- deterministic errors and stable reason codes;
- preservation helpers for source, surface, collection, item, record class, derivative identity, dates, rights, sensitivity, and provenance;
- side-effect-free candidate-envelope builders;
- a compatibility shim only when an accepted migration defines ownership, delegation, warnings, sunset criteria, tests, and rollback.

Every new executable module requires corresponding offline, negative-first tests. A new sibling import package is a migration decision, not a convenience refactor.

---

## What does NOT belong here

Do not place, bundle, or authorize the following under this layout:

- authoritative `SourceDescriptor` instances or source-activation decisions;
- contracts, schemas, source-registry authority, rights policy, sensitivity policy, evidence closure, release decisions, or publication authority;
- source payload archives, bulk exports, images, audiovisual media, OCR corpora, manuscripts, maps, or fixture dumps;
- credentials, tokens, cookies, account data, session state, private endpoints, or access agreements;
- network calls triggered by import, installation, package discovery, or default test execution;
- direct writes to RAW, QUARANTINE, receipts, processed, catalog, triplet, proof, release, correction, withdrawal, or published roots;
- public APIs, maps, tiles, item summaries, timelines, search indexes, graph projections, embeddings, or generated narratives;
- a second Kansas State Archives package or silent alias among the KSHS umbrella, State Archives proper, Kansas Memory, KHRI, and publication-index identities;
- one publisher-wide role, rights profile, sensitivity class, or activation state;
- generated summaries, OCR, transcriptions, annotations, entity links, or AI output presented as source truth;
- living-person data, donor-restricted material, exact archaeological or sacred locations, private-land detail, infrastructure-sensitive detail, or harmful cross-source joins;
- implementation, validation, activation, CI, deployment, or release claims without current evidence.

Fixtures belong in an accepted fixture/test lane and require rights, privacy, sensitivity, cultural/CARE, and source-steward review.

---

## Inputs

### Current inputs

None. A source-layout directory has no callable contract, and the child package declares no supported function, class, command, endpoint, configuration contract, credential variable, or fixture shape.

### Future permitted package inputs

Only after placement, contracts, review, and activation are accepted, the child package may consume:

- a conforming, reviewed, per-surface `SourceDescriptor` reference;
- an explicit activation state and approved access configuration;
- approved KSHS surface, collection, item, record-class, and source identifiers;
- caller-supplied bytes, files, metadata, or approved transport results;
- source URI, source-head evidence, retrieval time, checksum, run identity, and destination intent;
- rights, attribution, redistribution, privacy, sensitivity, cultural/sovereignty, CARE, access-class, and review context;
- synthetic, generated-shape-only, redacted, or explicitly rights-cleared fixtures for offline validation;
- correction, withdrawal, supersession, and replay context where applicable.

Missing, stale, conflicted, malformed, or unsafe trust-bearing inputs must fail closed before network access or handoff.

---

## Outputs

### Current outputs

None. The child placeholder modules emit no payload, parsed record, validation report, candidate envelope, receipt, lifecycle write, or public artifact.

### Future permitted package outputs

Future code may return in-memory, caller-owned:

- source-faithful parse results;
- deterministic `DENY`, `ABSTAIN`, `HOLD`, error, rate-limit, cancellation, or no-op outcomes;
- RAW candidates containing approved source-native bytes or references plus identity and retrieval metadata;
- QUARANTINE candidates with stable reason codes and bounded diagnostics;
- receipt candidates describing the attempted operation without claiming evidence closure, policy approval, or release.

The package must not select a lifecycle sink, persist directly into repository data roots, close an `EvidenceBundle`, catalog a claim, authorize public release, or convert connector success into truth.

---

## Validation

### Documentation checks for this revision

- preserve the document ID and creation date;
- record the pinned base commit and prior target blob;
- use one H1, logical heading order, balanced fences, and a final newline;
- make repository-relative links resolve from `connectors/kansas_state_archives/src/`;
- remove remote badges and tracking images;
- contain no credentials, source payloads, private records, or exact sensitive locations;
- keep current-state claims bounded to the pinned commit and directly inspected paths;
- change only `connectors/kansas_state_archives/src/README.md`.

### Required future package checks

Before implementation maturity can be claimed, tests must prove:

- clean build, install, and import for accepted Python versions;
- imports perform no network, filesystem write, registration, activation, secret logging, thread creation, or mutable global-state setup;
- the package-local descriptor is rejected as registry or activation authority;
- missing or conflicted path, package, surface, descriptor, activation, role, rights, attribution, privacy, sensitivity, cultural/CARE, and access state fail closed;
- KSHS umbrella, State Archives proper, Kansas Memory, KHRI, and publication-index identities remain distinct;
- original records, digital surrogates, OCR, transcription, annotation, entity resolution, indexes, and generated summaries remain distinct;
- collection identity, item identity, source URI, source fields, dates, checksums, provenance, and uncertainty survive parsing;
- living-person, archaeology, sacred/cultural, private-land, infrastructure, donor-restricted, and unclear-rights cases deny or quarantine as policy requires;
- malformed inputs, schema drift, stale source heads, unsupported surfaces, and access changes return finite outcomes without sensitive payload echo;
- outputs remain caller-owned RAW, QUARANTINE, or receipt candidates;
- no direct lifecycle, evidence, catalog, release, correction, withdrawal, or public writes occur;
- live-source tests, if ever approved, are opt-in, isolated, credential-safe, terms-reviewed, rate-limited, byte-limited, and excluded from default CI;
- migration shims carry delegation tests, warnings, owners, sunset criteria, and rollback coverage.

No package build or test command is documented because none is supported by the inspected project metadata.

---

## Review burden

Current [CODEOWNERS](../../../.github/CODEOWNERS) provides only the repository-wide `@kfm/maintainers` fallback for this path.

Documentation-only changes should be reviewed by the connector/package maintainer and docs steward. Any implementation, descriptor, transport, fixture, or migration change should additionally involve the Kansas source steward, archives steward, rights reviewer, sensitivity/privacy reviewer, CARE/cultural/sovereignty reviewer, security reviewer, and validation/test steward. Source activation and public release require their owning governance and release reviews outside this directory.

This README does not request reviewers automatically and does not establish ownership by naming roles.

---

## Related folders

| Surface | Relationship | Status at the pinned base |
|---|---|---:|
| [Connectors root](../../README.md) | Source-specific fetch and admission responsibility. | `CONFIRMED` |
| [Connector lane](../README.md) | Repository-present top-level compatibility scaffold. | `CONFIRMED path / v0.1 documentation` |
| [Project metadata](../pyproject.toml) | Distribution name and version. | `CONFIRMED 0.0.0 placeholder` |
| [Test boundary](../tests/README.md) | Intended offline compatibility tests. | `CONFIRMED README / executable tests unverified` |
| [Child package](kansas_state_archives/README.md) | Package-level scaffold, descriptor, surface, runtime, and rollback boundary. | `CONFIRMED v0.2` |
| [Kansas family](../../kansas/README.md) | Kansas source-family coordination lane. | `CONFIRMED / child topology provisional` |
| `../../kansas/kshs-state-archives/README.md` | Catalog-proposed State Archives proper child. | `CONFIRMED exact path absent` |
| [Nested KSHS source-family brief](../../../docs/sources/catalog/kansas/kansas-state-archives.md) | Human-facing umbrella/per-surface planning and anti-collapse context. | `CONFIRMED draft / not registry authority` |
| [Legacy flat catalog stub](../../../docs/sources/catalog/kansas_state_archives.md) | Older generated pointer to this top-level lane and a legacy descriptor path. | `CONFIRMED conflicting stub` |
| [`SourceDescriptor` contract](../../../contracts/source/source_descriptor.md) | Rich descriptor meaning and fail-closed rules. | `CONFIRMED draft / PROPOSED` |
| [Populated SourceDescriptor schema](../../../schemas/contracts/v1/source/source_descriptor.schema.json) | Rich machine shape and legacy-field mapping. | `CONFIRMED PROPOSED / schema-path conflict remains` |
| [Source registry](../../../data/registry/sources/README.md) | Governed source-instance responsibility. | `CONFIRMED README / archive entries unverified` |
| [Source authority register](../../../control_plane/source_authority_register.yaml) | Machine authority/activation register. | `CONFIRMED PROPOSED / entries empty` |
| [Rights policy](../../../policy/rights/README.md) and [sensitivity policy](../../../policy/sensitivity/README.md) | External fail-closed policy authority. | `CONFIRMED greenfield stubs` |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Placement, README contract, connector boundary, migration, and rollback doctrine. | `CONFIRMED doctrine` |
| [ADR operating guide](../../../docs/adr/README.md) | Decision-record and supersession discipline. | `CONFIRMED README / path-specific ADR absent` |
| [Contribution guide](../../../CONTRIBUTING.md) | Smallest reversible change and truth-label expectations. | `CONFIRMED` |

---

## ADRs

No accepted ADR or path-specific migration record was verified that settles:

- whether the current top-level connector is legacy, transitional, deprecated, mirror, or another compatibility class;
- whether `kansas_state_archives` survives as a package/import alias;
- whether one package may support several KSHS surfaces or each surface requires a separate adapter;
- the final connector child path, package name, and source-ID convention;
- the disposition of the package-local `descriptor.yaml`;
- the losing-path migration, deprecation, backlink, fixture, receipt, and rollback plan.

Updating this README does not require an ADR because it creates, moves, renames, or deletes no path and changes no authority root or lifecycle phase. A future path, package-identity, or compatibility-class decision may require an accepted ADR or explicit migration plan before implementation changes.

---

## Last reviewed

**2026-07-13** against repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `f9b54aaade4bea73805537f35fcdb458ea58463b`.

Re-review after six months, after any connector-path or package migration, after a `SourceDescriptor`/activation authority decision, or before adding executable source access.

---

## Current layout

The following map is bounded to the pinned base and the exact paths read for this revision:

```text
connectors/kansas_state_archives/
├── pyproject.toml                  # project kfm-connector-kansas_state_archives, version 0.0.0
├── src/
│   ├── README.md                   # this source-layout boundary
│   └── kansas_state_archives/
│       ├── README.md               # v0.2 package scaffold boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only greenfield placeholder
│       ├── admit.py                # comment-only greenfield placeholder
│       └── descriptor.yaml         # four-field unsafe placeholder
└── tests/
    └── README.md                   # documentation contract; executable tests unverified
```

The parent package metadata contains only:

```toml
[project]
name = "kfm-connector-kansas_state_archives"
version = "0.0.0"
```

| File | Confirmed bytes/posture | Does not prove |
|---|---|---|
| `README.md` | This source-layout document. | Runtime behavior or canonical placement. |
| `kansas_state_archives/README.md` | Repository-grounded v0.2 package boundary merged before this revision. | Executable modules, activation, or deployment. |
| `kansas_state_archives/__init__.py` | Empty. | Stable import API or side-effect contract. |
| `kansas_state_archives/fetch.py` | One comment. | Network behavior, endpoint support, authentication, retries, pagination, caching, or source-head logic. |
| `kansas_state_archives/admit.py` | One comment. | Validation, admission, quarantine, receipt, or candidate-envelope behavior. |
| `kansas_state_archives/descriptor.yaml` | `name: kansas_state_archives`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public`. | Schema validity, registry authority, activation, rights clearance, sensitivity clearance, or public safety. |

This is a bounded inspected map, not a recursive tree receipt. Differently named or unindexed files remain possible until a complete inventory is generated.

---

## Descriptor boundary

The package-local `kansas_state_archives/descriptor.yaml` is not a governed `SourceDescriptor`.

| Local field | Current value | Required disposition |
|---|---|---|
| `name` | `kansas_state_archives` | Do not convert into one stable source ID until the umbrella-versus-surface and package-identity decisions are accepted. |
| `role` | `TBD` | Reject as unresolved; source role is surface- and record-class-specific and must use an accepted vocabulary. |
| `rights` | `TBD` | Fail closed; no transport, admission, redistribution, or release authority. |
| `sensitivity_floor` | `public` | Ignore as authority; unresolved rights, privacy, cultural context, surface identity, and review state prohibit a permissive default. |

The inspected [`SourceDescriptor` contract](../../../contracts/source/source_descriptor.md) and [populated schema](../../../schemas/contracts/v1/source/source_descriptor.schema.json) require a richer closed object covering identity, version, source type and role, authority rank, publisher/steward, rights, sensitivity, cadence, access, citation, source-head evidence, admissibility limits, public-release posture, review state, release state, and lifecycle state. The schema treats `role` and `sensitivity_floor` as deprecated migration aliases.

The source authority register is `PROPOSED` with no entries, and the rights and sensitivity READMEs are greenfield stubs. Until the relevant authorities are accepted and populated:

- no local YAML field activates the connector;
- no publisher-wide role, rights state, sensitivity class, or public-release posture applies to every KSHS surface;
- unknown rights, privacy, sensitivity, cultural/CARE, source role, or access state routes to `DENY`, `ABSTAIN`, `HOLD`, or a QUARANTINE candidate;
- `public` in the placeholder never implies public-release safety.

---

## KSHS surface boundaries

Repository documentation currently uses “Kansas State Archives” in two ways: the State Archives Division proper and a broader KSHS archival umbrella. This layout must not collapse those meanings.

| Surface or derivative | Required distinction | Denied collapse |
|---|---|---|
| Kansas State Archives proper | Government records, manuscripts, maps, photographs, and related holdings with record-class-specific rights and access. | One umbrella role or rights posture applied to every record class. |
| Kansas Memory | Digital portal and surrogate layer over underlying historical material. | Digitization treated as a new observation or as removal of underlying rights, provenance, or restrictions. |
| Kansas Historic Resources Inventory (KHRI) | Historic-resource inventory surface with its own identifiers, authority posture, and location concerns. | Inventory entry presented as regulatory designation, legal determination, current site condition, or unrestricted exact-location truth. |
| *Kansas Historical Quarterly* and adjacent indexes | Bibliographic/discovery surfaces. | Index entry presented as the primary evidence for a substantive claim. |
| Original record | Source-native evidence created in its historical/administrative context. | OCR, transcription, annotation, or generated prose presented as the original. |
| Digital surrogate | Representation of an underlying record. | Surrogate existence treated as rights clearance or source-role upgrade. |
| OCR / transcription / annotation | Derived text with transform and review lineage. | Derived text presented as verified historical truth without the underlying record and evidence chain. |
| Entity resolution / generated summary | Interpretive derivative. | Generated link or language presented as archive authority, release approval, or evidence closure. |

A future package may share low-level helpers only when it preserves surface and derivative identity and dispatches through independently reviewed descriptors. Common institutional stewardship does not make these surfaces interchangeable.

Archival material can contain living-person information, donor or third-party restrictions, archaeological coordinates, sacred or culturally sensitive places, private-land context, and infrastructure detail. Upstream public access is not equivalent to KFM rights clearance, sensitivity clearance, CARE review, or release approval.

---

## Runtime and admission boundary

The `src/` directory itself performs no runtime action. Any future child implementation must complete this sequence before source access:

1. Accept one connector path, compatibility class, distribution name, import name, and source-ID strategy.
2. Decide KSHS umbrella versus per-surface adapter responsibilities and inventory losing paths and backlinks.
3. Accept one `SourceDescriptor` contract, schema, registry, validator, and activation authority.
4. Approve per-surface identity, role, rights, attribution, privacy, sensitivity, cultural/CARE posture, cadence, source head, access method, and correction behavior.
5. Require explicit opt-in transport with bounded hosts, paths, timeouts, retries, pagination, rate limits, byte limits, credential handling, cancellation, and audit behavior.
6. Preserve surface, collection, item, record-class, source URI, original/derivative identity, source fields, dates, checksums, uncertainty, and provenance.
7. Return a finite, side-effect-free outcome to caller-owned orchestration.
8. Leave lifecycle persistence, evidence closure, cataloging, release, correction, withdrawal, and public delivery to their owning systems.

| Condition | Required outcome |
|---|---|
| Path, package identity, surface strategy, descriptor, or activation unresolved | `DENY` or `ABSTAIN`; no network. |
| Role, rights, attribution, privacy, sensitivity, cultural/CARE, or access posture unresolved | `HOLD`, `DENY`, or QUARANTINE candidate. |
| Source shape, source head, item identity, or access terms drifted | QUARANTINE candidate or structured error; preserve bounded diagnostics. |
| Surface, collection, item, source URI, dates, checksum, or provenance lost | Hard validation failure. |
| Original, surrogate, OCR, transcription, annotation, entity resolution, index, or generated-summary identity collapsed | Hard semantic failure. |
| Exact living-person, archaeological, sacred/cultural, private-land, or infrastructure-sensitive detail would be exposed | `DENY` or policy-governed generalization candidate. |
| Valid approved material | Caller-owned RAW candidate only. |
| Downstream persistence, evidence closure, cataloging, or public release requested | Refuse; outside this layout. |

There is intentionally no quickstart. A runnable example would invent an API and behavior not present in the repository.

---

## Evidence basis

Evidence is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at commit `f9b54aaade4bea73805537f35fcdb458ea58463b`.

| Evidence | Supports | Does not support |
|---|---|---|
| Target blob `2614b6cc6a23755fc5fe537c5cef66570b1325f0` | Exact v0.1 baseline, stale two-README layout, remote badges, false “blank before update” claim, speculative module posture, and unresolved rollback placeholder. | Runtime or source readiness. |
| Direct reads of child package files | Empty initializer, comment-only fetch/admit placeholders, and four-field local descriptor. | Executable behavior, exhaustive recursive inventory, or safe configuration. |
| Parent `pyproject.toml` | Project name and version `0.0.0`. | Buildability, dependencies, supported runtime, or entry points. |
| Merged child package README | Package-level state, path conflict, descriptor conflict, KSHS surface boundaries, implementation gates, and immutable rollback target. | Runtime behavior or accepted canonicality. |
| Parent connector, test, Kansas-family, and source-catalog READMEs | Current documentation topology, proposed per-surface strategy, and catalog/path conflicts. | Accepted migration, activation, current upstream behavior, or rights clearance. |
| `SourceDescriptor` contract and populated schema | Rich descriptor meaning, required field surface, legacy-field mapping, and fail-closed constraints. | One accepted schema-path migration, persisted archive descriptor, or runtime enforcement. |
| Authority register and policy stubs | Empty proposed source authority and missing executable rights/sensitivity policy. | Permission to implement package-local substitutes. |
| Exact absent-path probe | Proposed `connectors/kansas/kshs-state-archives/README.md` was absent at the pinned base. | Permanent nonexistence or final path decision. |
| Directory Rules, contribution guidance, CODEOWNERS, and recent sibling layout precedent | Responsibility boundaries, folder-README contract, connector non-publication, review fallback, reversible change, and evidence-grounded source-layout style. | Product approval, package maturity, or branch-protection state. |

Not inspected: live KSHS services, current terms, credentials, source payloads, private or sensitive records, runtime logs, deployed configuration, emitted receipts, releases, or public clients. Associated claims remain `UNKNOWN` or `NEEDS VERIFICATION`.

---

## Rollback

Rollback is required if this README is used to justify canonical placement, a second import package, umbrella/surface collapse, live source access, package-local descriptor authority, source activation, direct lifecycle writes, public archive claims, rights/privacy/sensitivity/CARE bypass, or implementation maturity without code and tests.

Before merge, keep the draft change unmerged and abandon the scoped branch. Closing the pull request or deleting the branch is a separate repository action.

After merge, restore prior README blob `2614b6cc6a23755fc5fe537c5cef66570b1325f0` from base `f9b54aaade4bea73805537f35fcdb458ea58463b` through a transparent revert commit or revert pull request, then rerun documentation and connector-boundary validation. Do not reset, force-push, or rewrite shared history.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Resolve final connector path, compatibility class, distribution, import, and source-ID strategy. | `CONFLICTED` | Accepted ADR or migration record, backlink/import inventory, losing-path disposition, tests, and rollback. |
| Decide KSHS umbrella versus per-surface adapter boundaries. | `OPEN DECISION` | Product/source matrix, steward review, package responsibilities, delegation rules, and migration tests. |
| Decide whether `kansas_state_archives` survives as a compatibility import. | `OPEN DECISION` | Explicit alias semantics, ownership, warnings, sunset criteria, and rollback coverage. |
| Reconcile the top-level lane, Kansas family lane, nested source brief, and legacy flat catalog stub. | `CONFLICTED` | Supersession/migration plan, backlink inventory, deprecation record, and rollback. |
| Decide disposition of package-local `descriptor.yaml`. | `NEEDS VERIFICATION` | Registry, contract, schema, policy, package, and migration review. |
| Resolve `SourceDescriptor` schema, registry, validator, and activation authority. | `CONFLICTED` | Accepted contract/ADR, one enforceable schema path, fixtures, validator, and registry workflow. |
| Create per-surface descriptors and activation decisions. | `BLOCKED` | Surface identity, role, rights, sensitivity, access, cadence, source head, and steward review. |
| Confirm current KSHS access surfaces, schemas, identifiers, and correction behavior. | `NEEDS VERIFICATION` | Current source documentation, terms snapshots, source-steward review, and approved fixtures. |
| Confirm rights, attribution, redistribution, donor restrictions, privacy, and cultural/CARE posture per surface and record class. | `NEEDS VERIFICATION / DEFAULT DENY` | Rights/privacy/sensitivity review, policy bindings, negative fixtures, and release tests. |
| Confirm living-person, archaeology, sacred/cultural, private-land, infrastructure, and harmful-join handling. | `NEEDS VERIFICATION / DEFAULT DENY` | Executable policy, transforms, receipts, negative fixtures, and public-release tests. |
| Define build, import, dependency, configuration, and transport behavior. | `ABSENT` | Package implementation plus clean build/install/import evidence. |
| Define candidate envelopes, outcomes, reason codes, receipts, retries, replay, idempotency, and drift behavior. | `NEEDS VERIFICATION` | Accepted contracts, schemas, fixtures, and runtime tests. |
| Add safe offline fixtures and negative-first executable tests. | `UNVERIFIED` | Fixture review, package tests, CI discovery, and logs. |
| Assign package and connector owners and required reviewers. | `UNKNOWN` | CODEOWNERS or accepted ownership record. |

---

## Maintainer note

Keep `src/` boring: one explicit package, no hidden side effects, no bundled source payloads, no policy or registry authority, and no implementation maturity inferred from documentation.

When implementation begins, start with an offline proof-bearing slice: a synthetic or explicitly rights-cleared fixture, deterministic surface/collection/item identity, rejection of the local placeholder descriptor, original-versus-derivative anti-collapse, fail-closed rights/privacy/sensitivity/CARE behavior, and a caller-owned quarantine candidate. Add reviewed source access only after that foundation passes.

<p align="right"><a href="#top">Back to top</a></p>
