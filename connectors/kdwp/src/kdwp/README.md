<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kdwp-src-package-readme
title: connectors/kdwp/src/kdwp/ — KDWP Compatibility Package Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Fauna steward · Flora steward · Habitat steward · Rights reviewer · Sensitivity reviewer · Validation steward · Package maintainer · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; package-boundary; compatibility-lane; no-network-default; sensitive-species-deny-default; rights-gated; no-publication
proposed_path: connectors/kdwp/src/kdwp/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility package README / MODULE INVENTORY NEEDS VERIFICATION
related:
  - ../../README.md
  - ../../tests/README.md
  - ../../../kansas/README.md
  - ../../../kansas/kdwp/README.md
  - ../../../kansas/kdwp_flora/README.md
  - ../../../kansas/kdwp_ert/README.md
  - ../../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../../docs/domains/fauna/README.md
  - ../../../../docs/domains/flora/README.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../data/registry/sources/
  - ../../../../data/raw/fauna/
  - ../../../../data/quarantine/fauna/
  - ../../../../data/raw/flora/
  - ../../../../data/quarantine/flora/
  - ../../../../data/raw/habitat/
  - ../../../../data/quarantine/habitat/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/biodiversity/
  - ../../../../policy/sensitivity/
  - ../../../../policy/rights/
  - ../../../../release/
tags: [kfm, connectors, kdwp, package, python, kansas, wildlife, parks, sinc, fauna, flora, habitat, compatibility, no-network, sensitive-species, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a blank package-boundary README under the top-level KDWP compatibility connector path."
  - "The parent connector README documents `connectors/kdwp/` as a noncanonical compatibility path; canonical KDWP work belongs under `connectors/kansas/kdwp/` unless an ADR says otherwise."
  - "This README describes allowed implementation responsibilities only; it does not prove parser modules, fixtures, tests, endpoint access, or CI wiring exist."
  - "Package code must be no-network by default and may only emit RAW or QUARANTINE handoff envelopes after SourceDescriptor and activation gates are satisfied."
  - "KDWP-as-authority, KDWP-as-regulatory/listed-status context, and KDWP-as-observation must remain separate source-role surfaces."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KDWP Compatibility Package Boundary

> Implementation-boundary README for the legacy `kdwp` package namespace under the top-level compatibility connector. This package may support source-admission parsing and validation helpers only; it is **not** a live harvester, truth store, release engine, public API, or canonical connector home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical package path" src="https://img.shields.io/badge/canonicality-noncanonical__package-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Sensitive species: fail closed" src="https://img.shields.io/badge/sensitive__species-fail__closed-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility package README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/kdwp/src/kdwp/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility package path · `NEEDS VERIFICATION` actual modules, fixtures, and CI wiring  
> **Boundary:** parser/validation helpers only; no live-network default, no source activation, no release artifact, no public sensitive-species claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Expected module map](#expected-module-map) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation contract](#validation-contract) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/kdwp/src/kdwp/` is a compatibility package namespace for KDWP source-admission helpers.

It may contain parser, normalizer, fixture loader, validation, source-role, sensitivity, taxonomy, geometry, and handoff-envelope helpers for KDWP metadata after SourceDescriptor and activation gates are satisfied.

It must not become a live ingestion job, public service, canonical connector home, SourceDescriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, or publication authority.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/kdwp/src/kdwp/` | Compatibility package namespace. | **CONFIRMED path / NEEDS VERIFICATION modules** |
| `connectors/kdwp/README.md` | Parent compatibility connector README. | **CONFIRMED** |
| `connectors/kdwp/tests/README.md` | Compatibility-path test contract. | **CONFIRMED** |
| `connectors/kansas/kdwp/` | Canonical KDWP connector lane. | **CONFIRMED README path** |
| `connectors/kansas/kdwp_flora/` | KDWP flora/listed-species compatibility or sublane. | **CONFIRMED README path / PLACEMENT NEEDS VERIFICATION** |
| `connectors/kansas/kdwp_ert/` | KDWP Ecological Review Tool compatibility or sublane. | **CONFIRMED README path / PLACEMENT NEEDS VERIFICATION** |
| `docs/sources/catalog/kansas/kdwp.md` | Human-facing KDWP source catalog entry. | **CONFIRMED** |
| `data/raw/fauna/`, `data/raw/flora/`, `data/raw/habitat/` | Candidate RAW handoff targets. | **PROPOSED / NEEDS VERIFICATION** |
| `data/quarantine/fauna/`, `data/quarantine/flora/`, `data/quarantine/habitat/` | Candidate quarantine handoff targets. | **PROPOSED / NEEDS VERIFICATION** |
| `release/` | Release and publication controls. | **Out of scope for this package** |

[Back to top ↑](#top)

---

## Allowed responsibilities

Package code may support:

- fixture-only parser tests;
- KDWP metadata shape normalization;
- source-role separation helpers;
- KDWP authority/regulatory/listed-status context preservation;
- KDWP observation identity preservation;
- taxon identity helpers;
- sensitivity/rank-context preservation for downstream policy review;
- geometry/uncertainty preservation helpers;
- rights statement extraction or preservation;
- source-role and activation precondition checks;
- RAW or QUARANTINE handoff-envelope construction;
- deterministic error objects for quarantine/abstention;
- compatibility shims that point toward the canonical `connectors/kansas/kdwp/` lane.

---

## Forbidden responsibilities

Package code must not:

- fetch live source material by default;
- store credentials, tokens, cookies, or session state;
- decide source activation;
- decide rights, sensitivity, redaction, release class, or public visibility;
- collapse KDWP-as-authority, KDWP-as-regulatory/listed-status context, and KDWP-as-observation into one untyped feed;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- emit public sensitive-species claims, public precise locations, public range maps, public habitat claims, or public artifacts;
- silently treat `connectors/kdwp/` as canonical;
- collapse generated summaries, raw source records, stewardship determinations, and verified biodiversity claims;
- bypass SourceDescriptor, validation, EvidenceBundle, policy, release, correction, or rollback gates.

[Back to top ↑](#top)

---

## Expected module map

The following module map is **PROPOSED**, not confirmed implementation:

```text
connectors/kdwp/src/kdwp/
├── README.md              # CONFIRMED — this package-boundary README
├── __init__.py            # NEEDS VERIFICATION
├── descriptors.py         # PROPOSED — SourceDescriptor gate helpers
├── fetch.py               # PROPOSED — opt-in source access only; no-network default
├── parse.py               # PROPOSED — metadata parser helpers
├── normalize.py           # PROPOSED — field normalization without truth upgrade
├── roles.py               # PROPOSED — authority/regulatory/observed separation helpers
├── taxonomy.py            # PROPOSED — taxon identity preservation helpers
├── sensitivity.py         # PROPOSED — sensitivity/rank/redaction-state preservation helpers
├── geometry.py            # PROPOSED — geometry/uncertainty preservation helpers
├── handoff.py             # PROPOSED — RAW/QUARANTINE handoff envelope helpers
└── errors.py              # PROPOSED — deterministic fail-closed errors
```

Do not create these modules from this README alone; verify repo conventions, tests, and migration plan first.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/kdwp/src/kdwp/README.md` | **CONFIRMED** | Target package README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/kdwp/README.md` | **CONFIRMED** | Parent path is documented as noncanonical compatibility lane. | Does not prove canonical migration status. |
| `connectors/kdwp/tests/README.md` | **CONFIRMED** | Test posture is no-network by default, fixture-safe, sensitive-species fail-closed, and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/kansas/kdwp.md` | **CONFIRMED** | KDWP source profile identifies canonical `connectors/kansas/kdwp/`, KDWP-as-authority and KDWP-as-observation separation, and sensitivity/rights gates. | Does not prove endpoint availability or implementation. |
| Package modules below this path | **NEEDS VERIFICATION** | This README defines expected implementation boundaries. | Actual files, behavior, and CI status remain unverified. |

---

## Runtime posture

Default runtime posture for this package:

- no network unless explicitly enabled by reviewed configuration;
- no activation without SourceDescriptor and SourceActivationDecision;
- no public output;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- no secrets in source, fixtures, logs, or test outputs;
- deterministic failure when rights, sensitivity, redaction state, source role, taxon identity, listed-status context, observation identity, geometry, source shape, or activation state is unresolved.

A live-source path, if later approved, must be opt-in, source-steward reviewed, credential-safe, terms-reviewed, rate-limited, sensitivity-reviewed, auditable, and excluded from default tests unless governance explicitly permits it.

---

## Validation contract

The package should provide or support validation for:

- SourceDescriptor and activation preconditions;
- KDWP source-role separation;
- taxon identity preservation;
- listed-status and SINC/sensitivity context preservation;
- observation identity preservation;
- source URI and retrieval timestamp preservation;
- rights statement presence and preservation;
- sensitivity/redaction-state preservation;
- geometry and uncertainty preservation;
- fail-closed quarantine/abstention errors;
- RAW/QUARANTINE-only handoff envelopes;
- refusal to emit release/public artifacts.

Validation must be paired with tests before any implementation maturity is claimed.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, canonical status, public release, rights/sensitivity bypass, sensitive-species exposure, source-role collapse, or implementation maturity without tests.

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
| Confirm canonical KDWP package path. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Confirm current access methods and metadata shapes. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm rights/sensitivity/redaction handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this package small, deterministic, and reversible. It should parse and preserve KDWP source material for governed admission only. Public truth, sensitivity policy decisions, release approval, correction, and rollback live outside this package.

[Back to top ↑](#top)
