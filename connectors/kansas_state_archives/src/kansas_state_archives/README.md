<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-state-archives-src-package-readme
title: connectors/kansas_state_archives/src/kansas_state_archives/ — Kansas State Archives Compatibility Package Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Archives steward · Rights reviewer · Sensitivity reviewer · CARE/cultural review steward · Validation steward · Package maintainer · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; package-boundary; compatibility-lane; no-network-default; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/kansas_state_archives/src/kansas_state_archives/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility package README / MODULE INVENTORY NEEDS VERIFICATION
related:
  - ../../README.md
  - ../../tests/README.md
  - ../../../kansas/README.md
  - ../../../kansas/kshs-state-archives/README.md
  - ../../../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../../../docs/sources/catalog/kansas/kansas-memory.md
  - ../../../../docs/sources/catalog/kansas/khri.md
  - ../../../../docs/standards/oai-pmh.md
  - ../../../../docs/standards/iiif.md
  - ../../../../docs/standards/snac-eac-cpf.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../data/registry/sources/archives/
  - ../../../../data/raw/archives/
  - ../../../../data/quarantine/archives/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/sensitivity/
  - ../../../../policy/rights/
  - ../../../../release/
tags: [kfm, connectors, kansas-state-archives, package, python, kshs, archives, compatibility, no-network, rights, sensitivity, care, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a blank package-boundary README under the legacy-style Kansas State Archives compatibility connector path."
  - "The parent connector README documents `connectors/kansas_state_archives/` as a noncanonical compatibility path; canonical connector work should converge under `connectors/kansas/` unless an ADR says otherwise."
  - "This README describes allowed implementation responsibilities only; it does not prove parser modules, fixtures, tests, endpoint access, or CI wiring exist."
  - "Package code must be no-network by default and may only emit RAW or QUARANTINE handoff envelopes after SourceDescriptor and activation gates are satisfied."
  - "KSHS/Kansas State Archives rights terms, access surfaces, per-surface descriptors, activation, fixture inventory, tests, CI wiring, and public-release classes remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas State Archives Compatibility Package Boundary

> Implementation-boundary README for the legacy `kansas_state_archives` package namespace. This package may support source-admission parsing and validation helpers only; it is **not** a live harvester, truth store, release engine, public API, or canonical connector home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical package path" src="https://img.shields.io/badge/canonicality-noncanonical__package-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
  <img alt="Publication: none" src="https://img.shields.io/badge/publication-none-critical">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility package README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/kansas_state_archives/src/kansas_state_archives/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility package path · `NEEDS VERIFICATION` actual modules, fixtures, and CI wiring  
> **Boundary:** parser/validation helpers only; no live-network default, no source activation, no release artifact, no public archive claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Expected module map](#expected-module-map) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation contract](#validation-contract) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/kansas_state_archives/src/kansas_state_archives/` is a compatibility package namespace for Kansas State Archives / KSHS source-admission helpers.

It may contain parser, normalizer, fixture loader, validation, surface-identity, and handoff-envelope helpers for archive metadata after SourceDescriptor and activation gates are satisfied.

It must not become a live ingestion job, public service, canonical connector home, SourceDescriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, or publication authority.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/kansas_state_archives/src/kansas_state_archives/` | Compatibility package namespace. | **CONFIRMED path / NEEDS VERIFICATION modules** |
| `connectors/kansas_state_archives/README.md` | Parent compatibility connector README. | **CONFIRMED** |
| `connectors/kansas_state_archives/tests/README.md` | Compatibility-path test contract. | **CONFIRMED** |
| `connectors/kansas/` | Canonical Kansas connector-family lane. | **CONFIRMED** |
| `connectors/kansas/kshs-state-archives/` | Proposed canonical State Archives proper connector home. | **PROPOSED / NEEDS VERIFICATION** |
| `connectors/kansas/kansas-memory/` | Proposed canonical Kansas Memory connector home. | **PROPOSED / NEEDS VERIFICATION** |
| `connectors/kansas/khri/` | Proposed canonical KHRI connector home. | **PROPOSED / NEEDS VERIFICATION** |
| `docs/sources/catalog/kansas/kansas-state-archives.md` | Human-facing KSHS umbrella source-family brief. | **CONFIRMED** |
| `data/raw/archives/`, `data/quarantine/archives/` | Candidate handoff targets. | **PROPOSED / NEEDS VERIFICATION** |
| `release/` | Release and publication controls. | **Out of scope for this package** |

[Back to top ↑](#top)

---

## Allowed responsibilities

Package code may support:

- fixture-only parser tests;
- archive metadata shape normalization;
- KSHS surface-identity helpers;
- source URI and item identity preservation;
- collection/item identity helpers;
- rights statement extraction or preservation;
- sensitivity/CARE flag preservation for downstream policy review;
- source-role and activation precondition checks;
- RAW or QUARANTINE handoff-envelope construction;
- deterministic error objects for quarantine/abstention;
- compatibility shims that point toward the canonical Kansas connector lane.

---

## Forbidden responsibilities

Package code must not:

- fetch live source material by default;
- store credentials, tokens, cookies, or session state;
- decide source activation;
- decide rights, sensitivity, CARE/cultural review, release class, or public visibility;
- collapse Kansas Memory, KHRI, State Archives proper, and adjacent KSHS surfaces into one untyped feed;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- emit public claims, public summaries, public maps, public timelines, or public artifacts;
- silently treat `connectors/kansas_state_archives/` as canonical;
- collapse generated summaries, OCR text, archive metadata, and verified historical claims;
- bypass SourceDescriptor, validation, EvidenceBundle, policy, release, correction, or rollback gates.

[Back to top ↑](#top)

---

## Expected module map

The following module map is **PROPOSED**, not confirmed implementation:

```text
connectors/kansas_state_archives/src/kansas_state_archives/
├── README.md              # CONFIRMED — this package-boundary README
├── __init__.py            # NEEDS VERIFICATION
├── descriptors.py         # PROPOSED — SourceDescriptor gate helpers
├── fetch.py               # PROPOSED — opt-in source access only; no-network default
├── parse.py               # PROPOSED — metadata parser helpers
├── normalize.py           # PROPOSED — field normalization without truth upgrade
├── surfaces.py            # PROPOSED — KSHS surface identity helpers
├── rights.py              # PROPOSED — rights metadata preservation helpers
├── sensitivity.py         # PROPOSED — sensitivity/CARE flag preservation helpers
├── handoff.py             # PROPOSED — RAW/QUARANTINE handoff envelope helpers
└── errors.py              # PROPOSED — deterministic fail-closed errors
```

Do not create these modules from this README alone; verify repo conventions, tests, and migration plan first.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/kansas_state_archives/src/kansas_state_archives/README.md` | **CONFIRMED** | Target package README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/kansas_state_archives/README.md` | **CONFIRMED** | Parent path is documented as noncanonical compatibility lane. | Does not prove canonical migration status. |
| `connectors/kansas_state_archives/tests/README.md` | **CONFIRMED** | Test posture is no-network by default and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/kansas/kansas-state-archives.md` | **CONFIRMED** | KSHS/Kansas State Archives source brief identifies a KSHS umbrella layer, per-surface adapters under `connectors/kansas/`, and rights/sensitivity verification needs. | Does not prove endpoint availability or implementation. |
| Package modules below this path | **NEEDS VERIFICATION** | This README defines expected implementation boundaries. | Actual files, behavior, and CI status remain unverified. |

---

## Runtime posture

Default runtime posture for this package:

- no network unless explicitly enabled by reviewed configuration;
- no activation without SourceDescriptor and SourceActivationDecision;
- no public output;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- no secrets in source, fixtures, logs, or test outputs;
- deterministic failure when rights, sensitivity, CARE review, surface identity, item identity, source role, metadata shape, or activation state is unresolved.

A live-source path, if later approved, must be opt-in, source-steward reviewed, credential-safe, terms-reviewed, rate-limited, auditable, and excluded from default tests unless governance explicitly permits it.

---

## Validation contract

The package should provide or support validation for:

- SourceDescriptor and activation preconditions;
- KSHS surface identity;
- collection identity and item identity;
- source URI and retrieval timestamp preservation;
- title, creator, date, description, and collection metadata preservation where present;
- rights statement presence and preservation;
- sensitivity and CARE/cultural review flag preservation;
- archive access-method metadata, when verified;
- fail-closed quarantine/abstention errors;
- RAW/QUARANTINE-only handoff envelopes;
- refusal to emit release/public artifacts.

Validation must be paired with tests before any implementation maturity is claimed.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, canonical status, public release, rights/sensitivity/CARE bypass, surface-role collapse, or implementation maturity without tests.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter package-compatibility note until canonical placement and implementation are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual package module inventory. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm canonical KSHS / Kansas State Archives package path. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm per-surface connector package strategy. | **NEEDS VERIFICATION** | Repo tree and migration note. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Confirm current access methods and metadata shapes. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm rights/sensitivity/CARE handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this package small, deterministic, and reversible. It should parse and preserve KSHS archive source material for governed admission only. Public truth, policy decisions, release approval, correction, and rollback live outside this package.

[Back to top ↑](#top)
