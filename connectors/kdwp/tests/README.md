<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kdwp-tests-readme
title: connectors/kdwp/tests/ — KDWP Compatibility Connector Tests
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Fauna steward · Flora steward · Habitat steward · Rights reviewer · Sensitivity reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; tests; compatibility-lane; no-network-default; sensitive-species-deny-default; rights-gated; no-publication
proposed_path: connectors/kdwp/tests/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility test README / TEST INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../kansas/README.md
  - ../../kansas/kdwp/README.md
  - ../../kansas/kdwp_flora/README.md
  - ../../kansas/kdwp_ert/README.md
  - ../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/
  - ../../../data/raw/fauna/
  - ../../../data/quarantine/fauna/
  - ../../../data/raw/flora/
  - ../../../data/quarantine/flora/
  - ../../../data/raw/habitat/
  - ../../../data/quarantine/habitat/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/biodiversity/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, kdwp, tests, kansas, wildlife, parks, sinc, fauna, flora, habitat, compatibility, no-network, fixtures, sensitive-species, rights, source-admission, raw, quarantine, governance]
notes:
  - "This README replaces a thin greenfield tests stub under a top-level KDWP compatibility connector path."
  - "The parent `connectors/kdwp/README.md` documents this path as noncanonical compatibility only; canonical KDWP work belongs under `connectors/kansas/kdwp/` unless an ADR says otherwise."
  - "Tests must not require live source access by default and must not create public claims, maps, releases, or precise sensitive-species exposure."
  - "KDWP-as-authority, KDWP-as-regulatory/listed-status context, and KDWP-as-observation must remain separate source-role surfaces."
  - "Test output may validate RAW or QUARANTINE handoff behavior only; downstream validation, EvidenceBundle closure, rights/sensitivity review, catalog/triplet projection, release review, publication, correction, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KDWP Compatibility Connector Tests

> Test contract for the legacy-style `connectors/kdwp/` compatibility path. These tests should protect source-admission boundaries, fixture safety, source-role separation, sensitive-species fail-closed behavior, and migration toward the canonical `connectors/kansas/kdwp/` lane.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical path" src="https://img.shields.io/badge/canonicality-noncanonical__path-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Sensitive species: fail closed" src="https://img.shields.io/badge/sensitive__species-fail__closed-critical">
  <img alt="Publication: none" src="https://img.shields.io/badge/publication-none-critical">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility test README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/kdwp/tests/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility test lane · `NEEDS VERIFICATION` actual test files, fixtures, and CI wiring  
> **Boundary:** tests may verify source-admission behavior only; no live-network default, no release artifact, no public sensitive-species claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Test posture](#test-posture) · [Required test families](#required-test-families) · [Fixture rules](#fixture-rules) · [Evidence ledger](#evidence-ledger) · [Validation matrix](#validation-matrix) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/kdwp/tests/` is a compatibility-path test lane for KDWP source-admission behavior.

It may contain or document tests for fixture-only parsing, SourceDescriptor gating, source-role separation, taxon identity preservation, listed-status context preservation, sensitivity/rank handling, rights fail-closed behavior, RAW/QUARANTINE handoff, migration safety, and prevention of direct release behavior.

It must not become a live ingestion job, source activation decision, fixture dump of unreviewed sensitive ecological material, canonical schema home, policy home, release test fixture, public-output test, or proof of implementation maturity without actual test logs.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/kdwp/tests/` | Tests for noncanonical compatibility path. | **CONFIRMED path / NEEDS VERIFICATION test files** |
| `connectors/kdwp/README.md` | Parent compatibility README. | **CONFIRMED** |
| `connectors/kansas/kdwp/` | Canonical KDWP connector lane. | **CONFIRMED README path** |
| `connectors/kansas/kdwp_flora/` | KDWP flora/listed-species compatibility or sublane. | **CONFIRMED README path / PLACEMENT NEEDS VERIFICATION** |
| `connectors/kansas/kdwp_ert/` | KDWP Ecological Review Tool compatibility or sublane. | **CONFIRMED README path / PLACEMENT NEEDS VERIFICATION** |
| `docs/sources/catalog/kansas/kdwp.md` | Human-facing KDWP source catalog entry. | **CONFIRMED** |
| `fixtures/` | Candidate fixture home. | **NEEDS VERIFICATION** |
| `release/` | Release and publication controls. | **Out of scope for these tests** |

[Back to top ↑](#top)

---

## Test posture

Default test posture:

- no live network by default;
- no source activation by default;
- no public release artifact creation;
- no direct writes to `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`, proof, receipt, or release stores;
- no committed fixture containing unreviewed precise sensitive-species locations, restricted taxa exposure, private coordinates, unclear-rights data, or living-person material;
- fixture-driven parser and boundary tests only;
- fail closed for unresolved rights, source role, taxon identity, listed-status context, sensitivity/rank context, observation identity, geometry, access method, metadata shape, or schema drift.

A live-source integration test, if ever allowed, must be opt-in, source-steward reviewed, credential-safe, terms-reviewed, rate-limited, sensitivity-reviewed, and excluded from default CI unless governance explicitly approves it.

---

## Required test families

| Test family | Purpose | Status |
|---|---|---:|
| Import/smoke tests | Verify modules can import without network or side effects. | **PROPOSED** |
| Fixture parser tests | Validate representative KDWP metadata fixtures without exposing sensitive material. | **PROPOSED** |
| SourceDescriptor gate tests | Deny activation when descriptor or activation decision is missing. | **PROPOSED** |
| Source-role tests | Keep KDWP authority/regulatory/listed-status material separate from observation material. | **PROPOSED** |
| Sensitivity fail-closed tests | Route sensitive taxa, rank-triggered sensitivity, unresolved geometry, or unresolved redaction state to quarantine/abstention. | **PROPOSED** |
| Rights fail-closed tests | Route unclear rights/current terms to quarantine/abstention. | **PROPOSED** |
| Identity preservation tests | Preserve source ID, program/surface, taxon identity, listed-status context, sensitivity/rank context, observation identity, source URI, date/vintage, and geometry/uncertainty fields. | **PROPOSED** |
| Boundary tests | Deny writes outside RAW/QUARANTINE handoff. | **PROPOSED** |
| Migration tests | Prevent this noncanonical path from being treated as canonical without ADR/migration evidence. | **PROPOSED** |

---

## Fixture rules

Fixtures for this lane must be one of:

- synthetic fixtures that cannot be mistaken for live sensitive-species records;
- tiny public/rights-reviewed samples with explicit fixture receipt and sensitivity review;
- redacted, generalized, or withheld-location metadata fixtures approved for repository use;
- generated shape-only fixtures with a reality-boundary note.

Fixtures must preserve enough structure to test parser and policy-boundary behavior without turning committed test data into public ecological disclosure.

Do not commit bulk harvests, private coordinates, restricted taxa location details, unclear-rights material, credentials, session tokens, API keys, or unreviewed media assets.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/kdwp/tests/README.md` | **CONFIRMED** | Target tests README exists and previously contained only a greenfield stub. | Does not prove tests exist or pass. |
| `connectors/kdwp/README.md` | **CONFIRMED** | Parent path is documented as noncanonical compatibility lane. | Does not prove canonical migration status. |
| `docs/sources/catalog/kansas/kdwp.md` | **CONFIRMED** | KDWP source profile identifies canonical `connectors/kansas/kdwp/`, KDWP-as-authority and KDWP-as-observation separation, and sensitivity/right gates. | Does not prove endpoint availability, fixture safety, or tests. |
| Test files below this path | **NEEDS VERIFICATION** | This README defines expected test contract. | Actual files, coverage, and CI status remain unverified. |

---

## Validation matrix

| Validation target | Expected result |
|---|---|
| Missing SourceDescriptor | Deny activation or route to quarantine/abstention. |
| Missing activation decision | Deny activation. |
| Live network in default test run | Fail. |
| Output path outside RAW/QUARANTINE handoff | Fail. |
| Missing rights/current-terms state | Quarantine/abstain. |
| Unresolved sensitive-taxon or sensitivity/rank state | Quarantine/abstain. |
| Missing source role | Quarantine/abstain. |
| Authority/regulatory material mixed with observation material without role split | Fail. |
| Missing taxon identity or listed-status context | Quarantine/abstain. |
| Missing observation identity or source URI where required | Quarantine/abstain. |
| Unresolved geometry, precision, or redaction state | Quarantine/abstain. |
| Attempt to create release/public artifact | Fail. |
| Treating `connectors/kdwp/` as canonical | Fail unless ADR/migration evidence is provided. |

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, public release, fixture dumping, rights/sensitivity bypass, source-role collapse, or treating this top-level path as canonical.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the previous file was only a greenfield stub, a safe rollback is to restore that stub or replace this document with a shorter redirect-only tests README until canonical placement and fixture strategy are resolved.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual test files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm whether this top-level tests path should remain. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm canonical KDWP connector/test path. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo tree. |
| Confirm fixture home and fixture receipts. | **NEEDS VERIFICATION** | Fixture registry and review receipts. |
| Confirm rights/sensitivity test cases. | **NEEDS VERIFICATION** | Policy references, tests, and review notes. |
| Confirm no-network default behavior. | **NEEDS VERIFICATION** | Test code and CI logs. |
| Confirm CI wiring and passing status. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

Tests here should make the compatibility path safer, not more authoritative. KDWP implementation and tests should converge under the canonical `connectors/kansas/kdwp/` lane unless governance keeps this path as a compatibility redirect.

[Back to top ↑](#top)
