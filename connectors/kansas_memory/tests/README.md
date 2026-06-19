<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-memory-tests-readme
title: connectors/kansas_memory/tests/ — Kansas Memory Compatibility Connector Tests
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Archives steward · Rights reviewer · Sensitivity reviewer · CARE/cultural review steward · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; tests; compatibility-lane; no-network-default; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/kansas_memory/tests/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility test README / TEST INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../kansas/README.md
  - ../../kansas/kansas-memory/README.md
  - ../../../docs/sources/catalog/kansas/kansas-memory.md
  - ../../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../../docs/sources/catalog/kansas/khri.md
  - ../../../docs/standards/oai-pmh.md
  - ../../../docs/standards/iiif.md
  - ../../../docs/standards/snac-eac-cpf.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/archives/kansas-memory/
  - ../../../data/raw/archives/
  - ../../../data/quarantine/archives/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, kansas-memory, tests, archives, kshs, compatibility, no-network, fixtures, rights, sensitivity, care, source-admission, raw, quarantine, governance]
notes:
  - "This README replaces a thin greenfield tests stub under a legacy-style top-level Kansas Memory connector path."
  - "The parent `connectors/kansas_memory/README.md` documents this path as noncanonical compatibility only; canonical connector work should converge under `connectors/kansas/kansas-memory/` unless an ADR says otherwise."
  - "Tests must not require live source access by default and must not create public claims or release artifacts."
  - "Kansas Memory rights terms, API/access surface, item-count denominator, activation, fixture inventory, tests, CI wiring, and public-release classes remain NEEDS VERIFICATION."
  - "Test output may validate RAW or QUARANTINE handoff behavior only; downstream validation, EvidenceBundle closure, rights/sensitivity/CARE review, catalog/triplet projection, release review, publication, correction, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas Memory Compatibility Connector Tests

> Test contract for the legacy-style `connectors/kansas_memory/` compatibility path. These tests should protect source-admission boundaries, fixture safety, rights/sensitivity/CARE gates, and migration toward the canonical Kansas connector lane.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical path" src="https://img.shields.io/badge/canonicality-noncanonical__path-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: required" src="https://img.shields.io/badge/fixtures-required-blue">
  <img alt="Publication: none" src="https://img.shields.io/badge/publication-none-critical">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility test README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/kansas_memory/tests/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility test lane · `NEEDS VERIFICATION` actual test files, fixtures, and CI wiring  
> **Boundary:** tests may verify source-admission behavior only; no live-network default, no release artifact, no public archive claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Test posture](#test-posture) · [Required test families](#required-test-families) · [Fixture rules](#fixture-rules) · [Evidence ledger](#evidence-ledger) · [Validation matrix](#validation-matrix) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/kansas_memory/tests/` is a compatibility-path test lane for Kansas Memory source-admission behavior.

It may contain or document tests for fixture-only parsing, SourceDescriptor gating, metadata preservation, rights/sensitivity/CARE fail-closed behavior, RAW/QUARANTINE handoff, migration safety, and prevention of direct release behavior.

It must not become a live ingestion job, source activation decision, fixture dump of unreviewed archive material, canonical schema home, policy home, release test fixture, public-output test, or proof of implementation maturity without actual test logs.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/kansas_memory/tests/` | Tests for noncanonical compatibility path. | **CONFIRMED path / NEEDS VERIFICATION test files** |
| `connectors/kansas_memory/README.md` | Parent compatibility README. | **CONFIRMED** |
| `connectors/kansas/` | Canonical Kansas connector-family lane. | **CONFIRMED** |
| `connectors/kansas/kansas-memory/` | Proposed canonical Kansas Memory connector home. | **PROPOSED / NEEDS VERIFICATION** |
| `docs/sources/catalog/kansas/kansas-memory.md` | Human-facing Kansas Memory source profile. | **CONFIRMED** |
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
- no committed fixture containing unreviewed rights, sensitivity, cultural-care, or living-person material;
- fixture-driven parser and boundary tests only;
- fail closed for unresolved rights, source role, item identity, access method, metadata shape, sensitivity, cultural-care, or schema drift.

A live-source integration test, if ever allowed, must be opt-in, source-steward reviewed, credential-safe, terms-reviewed, rate-limited, and excluded from default CI unless governance explicitly approves it.

---

## Required test families

| Test family | Purpose | Status |
|---|---|---:|
| Import/smoke tests | Verify modules can import without network or side effects. | **PROPOSED** |
| Fixture parser tests | Validate representative archive metadata fixtures. | **PROPOSED** |
| SourceDescriptor gate tests | Deny activation when descriptor or activation decision is missing. | **PROPOSED** |
| Rights fail-closed tests | Route unclear rights to quarantine/abstention. | **PROPOSED** |
| Sensitivity/CARE fail-closed tests | Route unresolved sensitivity/cultural-care conditions to quarantine/abstention. | **PROPOSED** |
| Identity preservation tests | Preserve collection ID, item ID, source URI, title/creator/date, access method, and retrieval time. | **PROPOSED** |
| Boundary tests | Deny writes outside RAW/QUARANTINE handoff. | **PROPOSED** |
| Migration tests | Prevent this noncanonical path from being treated as canonical without ADR/migration evidence. | **PROPOSED** |

---

## Fixture rules

Fixtures for this lane must be one of:

- synthetic fixtures that cannot be mistaken for live archive records;
- tiny public-domain/rights-reviewed samples with explicit fixture receipt;
- redacted/generalized metadata fixtures approved for repository use;
- generated shape-only fixtures with a reality-boundary note.

Fixtures must preserve enough structure to test parser behavior without turning committed test data into a public archive release.

Do not commit bulk harvests, private records, unclear-rights material, restricted cultural material, living-person-sensitive material, credentials, session tokens, API keys, or unreviewed media assets.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/kansas_memory/tests/README.md` | **CONFIRMED** | Target tests README exists and previously contained only a greenfield stub. | Does not prove tests exist or pass. |
| `connectors/kansas_memory/README.md` | **CONFIRMED** | Parent path is documented as noncanonical compatibility lane. | Does not prove canonical migration status. |
| `docs/sources/catalog/kansas/kansas-memory.md` | **CONFIRMED** | Kansas Memory source profile identifies rights/access/item-count verification needs and proposed canonical connector home under `connectors/kansas/`. | Does not prove endpoint availability or fixture safety. |
| Test files below this path | **NEEDS VERIFICATION** | This README defines expected test contract. | Actual files, coverage, and CI status remain unverified. |

---

## Validation matrix

| Validation target | Expected result |
|---|---|
| Missing SourceDescriptor | Deny activation or route to quarantine/abstention. |
| Missing activation decision | Deny activation. |
| Live network in default test run | Fail. |
| Output path outside RAW/QUARANTINE handoff | Fail. |
| Missing rights statement | Quarantine/abstain. |
| Unresolved sensitivity or cultural-care flag | Quarantine/abstain. |
| Missing item identity or source URI | Quarantine/abstain. |
| Unknown access method or metadata shape | Quarantine/abstain. |
| Attempt to create release/public artifact | Fail. |
| Treating `connectors/kansas_memory/` as canonical | Fail unless ADR/migration evidence is provided. |

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, public release, fixture dumping, rights/sensitivity/CARE bypass, or treating this top-level underscore path as canonical.

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
| Confirm canonical Kansas Memory connector/test path. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo tree. |
| Confirm fixture home and fixture receipts. | **NEEDS VERIFICATION** | Fixture registry and review receipts. |
| Confirm rights/sensitivity/CARE test cases. | **NEEDS VERIFICATION** | Policy references, tests, and review notes. |
| Confirm no-network default behavior. | **NEEDS VERIFICATION** | Test code and CI logs. |
| Confirm CI wiring and passing status. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

Tests here should make the compatibility path safer, not more authoritative. When Kansas Memory work moves under the canonical `connectors/kansas/` lane, migrate or retire these tests with a documented rollback path.

[Back to top ↑](#top)
