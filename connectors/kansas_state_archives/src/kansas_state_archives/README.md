<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-state-archives-src-package-readme
title: connectors/kansas_state_archives/src/kansas_state_archives/ — Kansas State Archives Greenfield Package Scaffold
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas source steward · Archives steward · Rights reviewer · Sensitivity/privacy reviewer · CARE/cultural/sovereignty reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; greenfield-scaffold; compatibility-path; path-and-surface-conflict; source-admission; rights-fail-closed; sensitivity-fail-closed; care-review; no-network; no-activation; no-publication
current_path: connectors/kansas_state_archives/src/kansas_state_archives/README.md
truth_posture: CONFIRMED 0.0.0 scaffold and placeholder package files / CONFLICTED compatibility class, final connector path, package scope, SourceDescriptor authority, and local sensitivity floor / PROPOSED future admission contract / UNKNOWN executable tests, CI, runtime, activation, source access, and deployment
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 0e0b6bfdc3e1cb6711acd9f495c72b906a2845fb
  prior_blob: be673318c33af77eb9008b095bbf6adc6e1aa5f2
related:
  - ../README.md
  - ../../README.md
  - ../../pyproject.toml
  - ../../tests/README.md
  - ../../../kansas/README.md
  - ../../../../CONTRIBUTING.md
  - ../../../../.github/CODEOWNERS
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../../../docs/sources/catalog/kansas_state_archives.md
  - ../../../../contracts/source/source_descriptor.md
  - ../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../data/registry/sources/README.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../policy/rights/README.md
  - ../../../../policy/sensitivity/README.md
  - ../../../../docs/adr/README.md
tags: [kfm, connectors, kansas-state-archives, kshs, archives, package, python, greenfield, compatibility, source-admission, rights, sensitivity, privacy, care, raw, quarantine, no-network, no-publication]
notes:
  - "Direct reads at base commit 0e0b6bfdc3e1cb6711acd9f495c72b906a2845fb confirm package version 0.0.0, an empty __init__.py, comment-only fetch.py and admit.py files, and a four-field descriptor.yaml placeholder."
  - "The exact proposed connectors/kansas/kshs-state-archives/README.md path is absent at the inspected base; repository documents conflict between the live top-level compatibility lane, the Kansas family lane, a legacy flat catalog stub, and the newer nested KSHS umbrella brief."
  - "The connector-local descriptor uses deprecated minimal aliases, leaves role and rights unresolved, and asserts sensitivity_floor: public; it is not a conforming SourceDescriptor, registry record, or activation decision."
  - "No live KSHS source, current terms, credential, source payload, executable test result, runtime log, lifecycle artifact, deployment, release, or public client was inspected for this revision."
  - "This package performs no fetch, admission decision, lifecycle write, release, or publication in its current state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas State Archives Greenfield Package Scaffold

> Repository-grounded boundary for the Python namespace at `connectors/kansas_state_archives/src/kansas_state_archives/`. The package exists, but it is a non-operational `0.0.0` scaffold inside an unresolved compatibility lane. It is not an active connector, a `SourceDescriptor` authority, a lifecycle writer, or a publication surface.

**Document lifecycle:** `draft`  
**Component maturity:** `CONFIRMED` greenfield scaffold · executable runtime not implemented in the named package files  
**Owner:** `OWNER_TBD`  
**Authority level:** package inside a compatibility lane; exact compatibility class and final connector path are `CONFLICTED / NEEDS VERIFICATION`  
**Boundary:** no live network, no activation, no direct lifecycle persistence, no release, no publication

> [!IMPORTANT]
> `fetch.py` and `admit.py` contain comments only, `__init__.py` is empty, and `descriptor.yaml` is a nonconforming placeholder. Nothing in this package fetches KSHS material, makes an admission decision, emits a candidate envelope, or writes to a KFM lifecycle root.

> [!CAUTION]
> Do not add operational code here merely because the import namespace exists. Resolve connector placement, KSHS umbrella-versus-surface scope, descriptor authority, ownership, migration, and rollback before this package gains behavior.

**Quick links:** [Purpose](#purpose) · [Current package](#current-package) · [Repository fit](#repository-fit) · [Descriptor conflict](#descriptor-conflict) · [Surface boundaries](#kshs-surface-boundaries) · [Inputs and outputs](#inputs-and-outputs) · [Implementation boundary](#implementation-boundary) · [Failure contract](#failure-contract) · [Validation](#validation) · [Evidence](#evidence) · [Review and rollback](#review-and-rollback) · [Definition of done](#definition-of-done)

---

## Purpose

This README describes what the current Python namespace is, what it demonstrably does not do, and which gates must close before implementation can begin.

Today the package is useful only as:

- a visible marker for the live `kansas_state_archives` scaffold;
- a fail-closed boundary around placeholder code and metadata;
- a record of the unresolved connector-path and KSHS surface-scope conflict;
- a migration input for a future Kansas archives connector decision.

The intended audience is connector and package maintainers, Kansas source and archives stewards, rights and sensitivity reviewers, CARE/cultural/sovereignty reviewers, security reviewers, validation/test stewards, and migration reviewers.

It does not prove that this package name should survive, that this directory is canonical, that one adapter should represent every KSHS surface, or that any archive source is approved for access or admission.

---

## Current package

Direct file reads at base commit `0e0b6bfdc3e1cb6711acd9f495c72b906a2845fb` confirm this inspected surface:

```text
connectors/kansas_state_archives/
├── pyproject.toml                  # project kfm-connector-kansas_state_archives, version 0.0.0
├── src/
│   ├── README.md                   # compatibility source-layout documentation
│   └── kansas_state_archives/
│       ├── README.md               # this package boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only greenfield placeholder
│       ├── admit.py                # comment-only greenfield placeholder
│       └── descriptor.yaml         # four-field greenfield placeholder
└── tests/
    └── README.md                   # test-boundary documentation
```

| Surface | Confirmed state | Consequence |
|---|---|---|
| [`pyproject.toml`](../../pyproject.toml) | Declares `kfm-connector-kansas_state_archives` at `0.0.0`; no build system, dependencies, Python constraint, package-discovery rule, or command is declared. | Buildability, installability, supported runtime, and public API are `UNKNOWN`. |
| [`__init__.py`](./__init__.py) | Empty file. | No package API or import-time behavior is implemented. |
| [`fetch.py`](./fetch.py) | Comment-only placeholder. | No transport, endpoint, authentication, retry, timeout, rate-limit, pagination, caching, or source-head behavior exists. |
| [`admit.py`](./admit.py) | Comment-only placeholder. | No validation, quarantine, admission, receipt, or handoff behavior exists. |
| [`descriptor.yaml`](./descriptor.yaml) | `name: kansas_state_archives`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public`. | Placeholder is incomplete, internally unsafe as an activation basis, and not authoritative. |
| [`tests/README.md`](../../tests/README.md) | Documentation contract at the directly inspected path. | Executable package tests, coverage, and CI wiring remain absent or `UNKNOWN`. |

The inspected file set is not a recursive tree receipt. Any broader presence or absence claim must be regenerated from the repository at the commit under review.

---

## Repository fit

KFM's `connectors/` root owns source-specific fetch, probe, packaging, and admission support. Source doctrine, registry instances, schemas, policy decisions, evidence closure, lifecycle promotion, release decisions, and public-client behavior live elsewhere.

The Kansas State Archives topology is currently conflicted:

| Surface | Observed posture | Package implication |
|---|---|---|
| [`connectors/kansas_state_archives/`](../../README.md) | Repository-present top-level `0.0.0` scaffold; its READMEs describe noncanonical compatibility posture. | Presence does not grant canonical status or permission to implement. |
| [`connectors/kansas/`](../../../kansas/README.md) | Repository-present Kansas source-family coordination lane. | Current family context, not proof that an archives child exists. |
| `connectors/kansas/kshs-state-archives/` | Exact README probe returned Not Found at the pinned base. | Keep the child path `PROPOSED`; do not claim it is implemented. |
| [Nested KSHS source-family brief](../../../../docs/sources/catalog/kansas/kansas-state-archives.md) | Draft umbrella brief that proposes separate adapters and descriptors for State Archives proper, Kansas Memory, KHRI, and related surfaces. | Human-facing planning evidence, not machine activation authority. |
| [Legacy flat catalog stub](../../../../docs/sources/catalog/kansas_state_archives.md) | Repository-present generated stub that still points to the top-level connector and a legacy descriptor path. | Stale/conflicting documentation until separately redirected, superseded, or retired. |

The exact compatibility class of the current package is also unresolved. Calling it `legacy`, `transitional`, `deprecated`, or `mirror` would each require evidence not verified here.

Choosing, renaming, consolidating, or deleting this lane may affect imports, source IDs, per-surface descriptors, fixtures, receipts, backlinks, and lineage. Resolve that work through an accepted ADR or explicit migration plan with rollback; this README does not select a winner.

---

## Descriptor conflict

[`descriptor.yaml`](./descriptor.yaml) is not a usable `SourceDescriptor`.

| Connector-local field | Current value | Current contract posture |
|---|---|---|
| `name` | `kansas_state_archives` | Not the canonical required `source_id`; the package may represent an umbrella rather than one source product. |
| `role` | `TBD` | Deprecated alias; unexplained `TBD` is not an accepted role. Each KSHS surface and record class requires independent review. |
| `rights` | `TBD` | Unresolved rights must fail closed. |
| `sensitivity_floor` | `public` | Deprecated alias and unsafe as a permissive default while rights, surface identity, privacy, cultural context, and review state are unresolved. |

The inspected [`SourceDescriptor` contract](../../../../contracts/source/source_descriptor.md) and [paired singular-path schema](../../../../schemas/contracts/v1/source/source_descriptor.schema.json) require a richer closed object: identity and version, source type and role, authority rank, publisher and steward, rights, sensitivity, cadence, access, citation, source-head evidence, admissibility limits, public-release posture, review state, release state, and lifecycle state.

The same schema records `role` and `sensitivity_floor` as deprecated migration aliases. Therefore:

- do not load the local YAML as registry or activation authority;
- do not infer public safety from `sensitivity_floor: public`;
- do not assign one role or rights posture to every KSHS surface;
- do not place authoritative descriptors or activation decisions in this package;
- do not enable transport until conforming per-surface descriptors, review state, and activation decisions exist in accepted authority surfaces;
- do not treat any descriptor as proof that source claims are true or approved for release.

The machine [source-authority register](../../../../control_plane/source_authority_register.yaml) is `PROPOSED` with `entries: []`. The inspected [rights](../../../../policy/rights/README.md) and [sensitivity](../../../../policy/sensitivity/README.md) policy READMEs are greenfield stubs. Those facts reinforce default deny; they do not authorize package-local substitutes.

---

## KSHS surface boundaries

The current source-family brief uses "Kansas State Archives" as a KSHS umbrella, but explicitly requires per-surface descriptors because access mechanics, rights, identifiers, cadence, and source roles differ.

| Surface | Repository-documented distinction | Denied collapse |
|---|---|---|
| Kansas State Archives proper | Government records, manuscripts, maps, photographs, and related archival holdings. | One role or rights posture applied to every record class. |
| Kansas Memory | Digital portal and surrogate layer over underlying historical material. | Digitization treated as a new observation or as removal of underlying rights, provenance, or restrictions. |
| Kansas Historic Resources Inventory (KHRI) | Historic-resource inventory surface. | Inventory entry presented as regulatory designation, legal determination, current site condition, or unrestricted exact-location truth. |
| *Kansas Historical Quarterly* index and adjacent indexes | Bibliographic/discovery surfaces. | Index entry presented as the primary source for a substantive claim. |

A future package may share low-level helpers only when it preserves surface identity and dispatches through independently reviewed descriptors. Institutional common ownership does not make the surfaces interchangeable.

Archival material can contain living-person information, donor or third-party rights restrictions, archaeological coordinates, sacred or culturally sensitive places, private-land context, and infrastructure detail. Upstream public access is not equivalent to KFM rights clearance, sensitivity clearance, CARE review, or release approval.

---

## Inputs and outputs

### Current inputs

None. The package declares no supported function, class, command, configuration contract, endpoint, credential variable, or fixture format.

### Current outputs

None. The placeholders emit no payload, candidate envelope, receipt, validation report, RAW record, QUARANTINE record, or public artifact.

### Future admissible inputs

Only after placement and activation gates are accepted, a narrow package contract may accept:

- a conforming, reviewed, per-surface `SourceDescriptor` reference;
- an explicit activation decision and approved access configuration;
- approved source, collection, item, and record identifiers;
- caller-supplied bytes, files, or approved transport results;
- synthetic or rights-cleared fixtures for offline tests;
- explicit run identity, retrieval time, source-head evidence, and destination intent;
- caller-owned RAW-candidate, QUARANTINE-candidate, and receipt-candidate sinks.

### Future admissible outputs

A future package may return deterministic parse results, validation failures, or RAW/QUARANTINE candidate envelopes to governed orchestration. It must not select release, persist directly into lifecycle roots, or convert connector success into evidence or truth.

---

## Implementation boundary

### Allowed only after the path and surface decisions

- narrow, surface-dispatched parsing and source-head helpers;
- explicit opt-in transport behind reviewed configuration;
- deterministic normalization that preserves source-native values, uncertainty, and provenance;
- collection, item, role, rights, sensitivity, privacy, cultural, CARE, geometry, date, and access checks;
- structured errors suitable for abstention, denial, hold, or quarantine;
- side-effect-free candidate-envelope construction;
- offline, synthetic, rights-cleared, negative-first fixtures and tests;
- a migration shim if an accepted decision retains `kansas_state_archives` as a compatibility import.

### Forbidden

- network calls on import or by default;
- credentials, tokens, cookies, account data, private endpoints, or access agreements in source, fixtures, docs, logs, or exceptions;
- one publisher-wide default role, rights profile, sensitivity class, or activation state;
- authoritative `SourceDescriptor` instances or activation decisions inside the package;
- direct writes to RAW, QUARANTINE, receipts, processed, catalog, triplet, proof, release, or published roots;
- silent aliasing among the umbrella, State Archives proper, Kansas Memory, KHRI, or publication-index identities;
- bulk archival payloads, media, OCR corpora, or unclear-rights fixtures in Git;
- reconstruction or exposure of withheld living-person, archaeological, sacred, cultural, private-land, or infrastructure detail;
- generated summaries, OCR, transcriptions, entity links, embeddings, or AI output presented as source truth;
- claims of implementation, coverage, validation, activation, or CI maturity without current evidence.

There is intentionally no quickstart. A runnable example would imply an API and behavior that do not exist.

---

## Failure contract

A future implementation must fail deterministically and without sensitive payload echo. Minimum reason families include:

- unresolved connector path, compatibility class, package scope, or source identity;
- missing, nonconforming, unreviewed, stale, or inactive descriptor;
- unknown KSHS surface, collection, item, record class, or unsupported source shape;
- unresolved role, rights, attribution, privacy, sensitivity, cultural, sovereignty, CARE, or access posture;
- missing source URI, upstream identifier, retrieval time, source-head evidence, checksum, or provenance;
- collapse among original record, digital surrogate, OCR, transcription, annotation, entity resolution, index, or generated summary;
- denied network posture, unapproved host, rate limit, byte limit, cancellation, or credential requirement;
- attempted lifecycle persistence or public-release target.

Unknowns route to `DENY`, `ABSTAIN`, `HOLD`, or a QUARANTINE candidate. They never receive permissive defaults.

---

## Validation

No package build or test command is documented because none is supported by the inspected project metadata.

Before implementation maturity can be claimed, evidence must cover:

1. accepted connector path, package/import name, compatibility class, and losing-path migration;
2. KSHS umbrella versus per-surface adapter and source-ID decisions;
3. complete recursive package and backlink inventory;
4. build backend, package discovery, supported Python versions, dependency policy, and clean install/import;
5. per-surface conforming descriptors and explicit activation decisions;
6. reviewed access methods, current terms, attribution, redistribution, cadence, source schemas, and correction behavior;
7. no-network default and host/credential controls for opt-in transport;
8. synthetic or rights-cleared fixtures with negative-path coverage;
9. surface identity, source-role, rights, sensitivity, privacy, cultural, CARE, provenance, derivative-identity, and precise-location tests;
10. deterministic candidate-envelope and lifecycle-boundary tests;
11. migration/delegation tests if this compatibility import survives;
12. CI discovery and passing package-specific evidence.

Documentation checks for this revision should include one H1, balanced fences, working repository-relative links, no remote badge images, no credential-like strings, a final newline, and an exact one-file diff.

---

## Evidence

Evidence for this revision is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at commit `0e0b6bfdc3e1cb6711acd9f495c72b906a2845fb`.

| Evidence | Status | Supports | Does not support |
|---|---|---|---|
| [`pyproject.toml`](../../pyproject.toml) | `CONFIRMED` | Project name and version `0.0.0`. | Buildability, dependencies, installability, API, or command. |
| Package files under this path | `CONFIRMED` for exact reads | Empty initializer; comment-only fetch/admit placeholders; four-field descriptor placeholder. | Executable behavior, exhaustive recursive inventory, validation, or activation. |
| [`tests/README.md`](../../tests/README.md) | `CONFIRMED` | Intended offline compatibility-test posture. | Executable tests or CI success. |
| [`connectors/kansas/README.md`](../../../kansas/README.md) | `CONFIRMED` | Current Kansas family coordination lane and unresolved archives child migration. | Accepted final child path. |
| [Nested KSHS brief](../../../../docs/sources/catalog/kansas/kansas-state-archives.md) | `CONFIRMED draft` | Institutional/per-surface framing, anti-collapse, rights, and sensitivity posture. | Registry authority, current upstream behavior, rights clearance, or activation. |
| [Legacy flat catalog stub](../../../../docs/sources/catalog/kansas_state_archives.md) | `CONFIRMED` | Current documentation/path conflict. | Canonicality or accepted migration. |
| [`SourceDescriptor` contract](../../../../contracts/source/source_descriptor.md) and [paired schema](../../../../schemas/contracts/v1/source/source_descriptor.schema.json) | `CONFIRMED draft/PROPOSED` | Richer descriptor contract, deprecated aliases, and fail-closed constraints. | Accepted schema-path migration, persisted archive descriptor, or runtime enforcement. |
| [`control_plane/source_authority_register.yaml`](../../../../control_plane/source_authority_register.yaml) | `CONFIRMED` | Register is `PROPOSED` and contains `entries: []`. | Any KSHS activation decision. |
| [Rights](../../../../policy/rights/README.md) and [sensitivity](../../../../policy/sensitivity/README.md) READMEs | `CONFIRMED` | Both are greenfield stubs. | Executable or reviewed archive policy. |
| Exact `connectors/kansas/kshs-state-archives/README.md` probe | `CONFIRMED absent at base` | Proposed child README was not present at the pinned commit. | Permanent nonexistence or final path decision. |
| [Directory Rules](../../../../docs/doctrine/directory-rules.md), [CONTRIBUTING](../../../../CONTRIBUTING.md), [CODEOWNERS](../../../../.github/CODEOWNERS), and PR template | `CONFIRMED` | Placement, connector non-publication, smallest reversible change, review fallback, and PR discipline. | Branch protection, required checks, or workflow results for this change. |

Not inspected: live KSHS sources, current terms, credentials, source payloads, private or sensitive records, runtime logs, deployed configuration, emitted receipts, releases, or public clients. Treat all associated claims as `UNKNOWN` or `NEEDS VERIFICATION`.

---

## Review and rollback

Review changes here as connector-placement, package identity, KSHS surface identity, source-role, rights, privacy, sensitivity, cultural/CARE, security, lifecycle-boundary, and migration changes—even when the diff is documentation-only.

Current [CODEOWNERS](../../../../.github/CODEOWNERS) provides only the repository-wide `@kfm/maintainers` fallback for this path. A substantive implementation or migration should additionally involve the affected connector/package, Kansas source, archives, rights, sensitivity/privacy, CARE/cultural/sovereignty, security, validation/test, and docs stewards.

Rollback this README revision if it is used to:

- treat this package or any proposed path as canonical without an accepted decision;
- activate the placeholder descriptor;
- infer public safety from `sensitivity_floor: public`;
- claim working fetch, admission, tests, fixtures, CI, or lifecycle output;
- collapse KSHS surfaces, record classes, or derivatives into one source role or truth layer;
- bypass rights, sensitivity, privacy, cultural/CARE, descriptor, activation, evidence, release, correction, or rollback gates.

Before merge, close the draft change and abandon its scoped branch. After merge, create a transparent revert of the documentation commit; do not rewrite shared history. The baseline target blob is `be673318c33af77eb9008b095bbf6adc6e1aa5f2` at base commit `0e0b6bfdc3e1cb6711acd9f495c72b906a2845fb`.

---

## Definition of done

### Documentation boundary

- [x] Current package files and `0.0.0` maturity are explicit.
- [x] Placeholder fetch, admission, and descriptor behavior is not overstated.
- [x] Connector-path, compatibility-class, catalog-doc, and KSHS surface conflicts are visible.
- [x] Descriptor/schema conflict and default-deny result are explicit.
- [x] Surface, role, rights, privacy, sensitivity, cultural/CARE, derivative, and precise-location anti-collapse rules are explicit.
- [x] Current inputs, outputs, API, commands, tests, activation, and publication are stated as absent or unknown.
- [x] Evidence limits and immutable rollback target are recorded.
- [x] Remote badge images and the prior unresolved rollback placeholder are removed.

### Implementation readiness

- [ ] Connector-path, compatibility-class, package/import, source-ID, and migration decision is accepted.
- [ ] KSHS umbrella versus per-surface adapter strategy is accepted.
- [ ] Owners and required reviewers are assigned.
- [ ] Per-surface conforming descriptors and activation decisions exist.
- [ ] Current source access, schemas, terms, rights, attribution, cadence, and corrections are reviewed.
- [ ] Privacy, sensitivity, cultural, sovereignty, CARE, derivative-identity, and precise-location policy is executable.
- [ ] Build, install, import, fixture, test, candidate-envelope, and lifecycle-boundary contracts are implemented.
- [ ] Default tests are offline, deterministic, negative-first, and CI-discovered.
- [ ] Documentation stubs and losing paths have an accepted supersession/migration and backlink plan.
- [ ] Correction, invalidation, migration, and rollback are tested.

Until every applicable implementation-readiness item closes, keep this package inert and fail closed.

<p align="right"><a href="#top">Back to top</a></p>
