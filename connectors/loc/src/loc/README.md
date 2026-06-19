<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-loc-src-package-readme
title: connectors/loc/src/loc/ — Library of Congress Connector Candidate Package Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Source steward for LOC · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; package-boundary; connector-family-candidate; beyond-directory-rules-7-3; open-dsc-14; no-network-default; fixture-safe; rights-gated; no-publication
proposed_path: connectors/loc/src/loc/README.md
truth_posture: CONFIRMED path exists / PROPOSED beyond §7.3 connector-family package path / MODULE INVENTORY NEEDS VERIFICATION
related:
  - ../../README.md
  - ../../tests/README.md
  - ../../../../docs/sources/catalog/loc/README.md
  - ../../../../docs/sources/catalog/loc/loc-iiif-presentations.md
  - ../../../../docs/sources/catalog/loc/loc-historic-maps.md
  - ../../../../docs/sources/catalog/loc/lcnaf-name-authority.md
  - ../../../../docs/sources/catalog/loc/lcsh-subject-headings.md
  - ../../../../docs/sources/catalog/loc/chronicling-america.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../data/registry/sources/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/rights/
  - ../../../../policy/sources/
  - ../../../../release/
tags: [kfm, connectors, loc, library-of-congress, package, python, lcnaf, lcsh, iiif, chronicling-america, maps, archives, linked-data, source-admission, open-dsc-14, no-network, raw, quarantine, governance]
notes:
  - "This README fills a blank package-boundary README under the proposed LOC connector-family candidate."
  - "The LOC catalog README says `connectors/loc/` is proposed beyond Directory Rules §7.3 and awaits OPEN-DSC-14 ADR ratification."
  - "This README describes allowed implementation responsibilities only; it does not prove parser modules, fixtures, tests, endpoint access, or CI wiring exist."
  - "Package code must be no-network by default and may only emit RAW or QUARANTINE handoff envelopes after SourceDescriptor and activation gates are satisfied."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Library of Congress Connector Candidate Package Boundary

> Implementation-boundary README for the `loc` package namespace under the proposed Library of Congress connector-family candidate. This package may support source-admission parsing and validation helpers only; it is **not** a live harvester, truth store, release engine, public API, canonical family proof, or publication path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family status: beyond §7.3" src="https://img.shields.io/badge/family-beyond__%C2%A77.3-orange">
  <img alt="Open item: OPEN-DSC-14" src="https://img.shields.io/badge/open-OPEN--DSC--14-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` connector-candidate package README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/loc/src/loc/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` beyond §7.3 package path · `NEEDS VERIFICATION` actual modules, fixtures, and CI wiring  
> **Boundary:** parser/validation helpers only; no live-network default, no source activation, no release artifact, no canonical-family claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Expected module map](#expected-module-map) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation contract](#validation-contract) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/loc/src/loc/` is a package namespace for source-admission helpers under the proposed LOC connector-family candidate.

It may contain parser, normalizer, fixture loader, validation, source-role, sub-source identity, rights-state, provenance, source fingerprint, uncertainty, and handoff-envelope helpers for LOC source metadata after SourceDescriptor and activation gates are satisfied.

It must not become a live ingestion job, public service, canonical family root, SourceDescriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, or publication authority.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/loc/src/loc/` | LOC connector-candidate package namespace. | **CONFIRMED path / NEEDS VERIFICATION modules** |
| `connectors/loc/README.md` | Parent LOC connector-family candidate README. | **CONFIRMED** |
| `connectors/loc/tests/README.md` | LOC candidate-family test contract. | **CONFIRMED** |
| `docs/sources/catalog/loc/README.md` | LOC source-family catalog README. | **CONFIRMED** |
| LOC per-sub-source catalog pages | Source profiles for distinct LOC surfaces. | **CONFIRMED search results / NEEDS FILE REVIEW** |
| `release/` | Release and publication controls. | **Out of scope for this package** |

[Back to top ↑](#top)

---

## Allowed responsibilities

Package code may support:

- fixture-only parser tests;
- LOC metadata shape normalization;
- LOC sub-source identity helpers;
- source-role preservation;
- source URI and retrieval timestamp preservation;
- source fingerprint preservation, such as manifest hashes when applicable;
- rights statement extraction or preservation;
- provenance preservation helpers;
- uncertainty metadata helpers;
- SourceDescriptor and activation precondition checks;
- RAW or QUARANTINE handoff-envelope construction;
- deterministic error objects for quarantine or abstention;
- compatibility shims that keep `connectors/loc/` marked as proposed until `OPEN-DSC-14` is resolved.

---

## Forbidden responsibilities

Package code must not:

- fetch live source surfaces by default;
- store credentials, tokens, cookies, or session state;
- decide source activation;
- decide rights, sensitivity, redaction, release class, or public visibility;
- collapse LOC sub-sources into each other or into generated summaries;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- emit public archival, identity, map, OCR, linked-data, or release claims;
- silently treat `connectors/loc/` as canonical;
- bypass SourceDescriptor, validation, EvidenceBundle, policy, release, correction, or rollback gates.

[Back to top ↑](#top)

---

## Expected module map

The following module map is **PROPOSED**, not confirmed implementation:

```text
connectors/loc/src/loc/
├── README.md              # CONFIRMED — this package-boundary README
├── __init__.py            # NEEDS VERIFICATION
├── descriptors.py         # PROPOSED — SourceDescriptor gate helpers
├── fetch.py               # PROPOSED — opt-in source access only; no-network default
├── parse.py               # PROPOSED — source-shape parser helpers
├── normalize.py           # PROPOSED — field normalization without truth upgrade
├── roles.py               # PROPOSED — source-role separation helpers
├── surfaces.py            # PROPOSED — LOC sub-source identity helpers
├── provenance.py          # PROPOSED — source URI, timestamp, and fingerprint helpers
├── uncertainty.py         # PROPOSED — OCR/map/identity/crosswalk uncertainty helpers
├── handoff.py             # PROPOSED — RAW/QUARANTINE handoff envelope helpers
└── errors.py              # PROPOSED — deterministic fail-closed errors
```

Do not create these modules from this README alone; verify repo conventions, tests, and migration plan first.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/loc/src/loc/README.md` | **CONFIRMED** | Target package README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/loc/README.md` | **CONFIRMED** | Parent path is documented as proposed beyond §7.3 under OPEN-DSC-14. | Does not prove ADR resolution or implementation maturity. |
| `connectors/loc/tests/README.md` | **CONFIRMED** | Test posture is no-network by default, fixture-safe, and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/loc/README.md` | **CONFIRMED** | LOC catalog README says `connectors/loc/` is proposed beyond §7.3 and lists LOC sub-sources and admission concerns. | Does not prove endpoint availability, rights clearance, activation, or implementation. |
| Package modules below this path | **NEEDS VERIFICATION** | This README defines expected implementation boundaries. | Actual files, behavior, and CI status remain unverified. |

---

## Runtime posture

Default runtime posture for this package:

- no network unless explicitly enabled by reviewed configuration;
- no activation without SourceDescriptor and SourceActivationDecision;
- no public output;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- no secrets in source, fixtures, logs, or test outputs;
- deterministic failure when rights state, source role, sub-source identity, provenance, uncertainty, source shape, or activation state is unresolved.

A live-source path, if later approved, must be opt-in, reviewed, credential-safe, terms-reviewed, rate-limited, auditable, and excluded from default tests unless governance explicitly permits it.

---

## Validation contract

The package should provide or support validation for:

- SourceDescriptor and activation preconditions;
- candidate-family status under `OPEN-DSC-14`;
- LOC sub-source identity preservation;
- source-role preservation;
- source URI and retrieval timestamp preservation;
- source fingerprint preservation where applicable;
- rights statement presence and preservation;
- provenance preservation;
- explicit uncertainty preservation;
- fail-closed quarantine or abstention errors;
- RAW/QUARANTINE-only handoff envelopes;
- refusal to emit release/public artifacts.

Validation must be paired with tests before any implementation maturity is claimed.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, canonical-family status, public release, rights bypass, sub-source collapse, or implementation maturity without tests.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter package-candidate note until `OPEN-DSC-14` and implementation are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual package module inventory. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Resolve `OPEN-DSC-14` for LOC connector-family placement. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Confirm rights and provenance handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this package small, deterministic, and reversible. It should parse and preserve LOC source material for governed admission only. Public truth, release approval, correction, and rollback live outside this package.

[Back to top ↑](#top)
