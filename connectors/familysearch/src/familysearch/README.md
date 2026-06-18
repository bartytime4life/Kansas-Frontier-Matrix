<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-familysearch-src-package-readme
title: connectors/familysearch/src/familysearch/ — FamilySearch Connector Python Package
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · People/DNA/Land steward · Sensitivity reviewer · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine
proposed_path: connectors/familysearch/src/familysearch/README.md
truth_posture: CONFIRMED path exists / PROPOSED package contract / UNKNOWN implementation depth
related:
  - ../../README.md
  - ../../../README.md
  - ../../tests/README.md
  - ../../../../docs/sources/catalog/familysearch/README.md
  - ../../../../docs/domains/people-dna-land/README.md
  - ../../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../../data/registry/sources/people-genealogy-dna-land/
  - ../../../../data/raw/people-dna-land/
  - ../../../../data/quarantine/people-dna-land/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/genealogy/publication.rego
  - ../../../../policy/sensitivity/
  - ../../../../release/
tags: [kfm, connectors, familysearch, python-package, genealogy, people-dna-land, consent, living-person, source-admission, raw, quarantine, governance]
notes:
  - "This README documents the connector implementation package boundary, not FamilySearch source truth, person truth, relationship truth, consent authority, or publication authority."
  - "Package code may prepare source material for RAW or QUARANTINE admission only."
  - "Import, live access, OAuth behavior, descriptors, endpoint coverage, tests, fixtures, CI wiring, and source terms remain NEEDS VERIFICATION until inspected in the mounted repo."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FamilySearch Connector Python Package

> Python package boundary for FamilySearch source-intake helpers inside `connectors/familysearch/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Sensitivity: living-person deny by default" src="https://img.shields.io/badge/sensitivity-living__person__deny__by__default-critical">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/familysearch/src/familysearch/`

## Quick jumps

[Scope](#scope) · [Package boundary](#package-boundary) · [Authority boundary](#authority-boundary) · [Expected modules](#expected-modules) · [Runtime posture](#runtime-posture) · [Inputs and outputs](#inputs-and-outputs) · [Privacy and consent behavior](#privacy-and-consent-behavior) · [Errors](#errors) · [Tests](#tests) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/familysearch/src/familysearch/` is the Python implementation package for FamilySearch connector helpers.

It may contain code that:

- reads connector-local configuration;
- prepares FamilySearch source requests only when live access is explicitly allowed and reviewed;
- parses FamilySearch-shaped source responses or synthetic fixtures;
- normalizes connector output into a bounded source-admission envelope;
- preserves source metadata, citation metadata, contributor/source labels, timestamps, and digests where applicable;
- treats person, relationship, event, place, and citation fragments as candidate assertions;
- routes living-person, consent-unclear, rights-unclear, private, malformed, or source-drift material toward deny/quarantine/review-required outcomes;
- exposes small, testable functions used by `connectors/familysearch/tests/`.

It must not become genealogy truth, person identity authority, relationship truth, DNA truth, land-title truth, consent authority, source registry authority, schema authority, policy authority, catalog authority, release authority, or publication authority.

> [!IMPORTANT]
> This package is an intake adapter. It does not decide whether FamilySearch-derived material is true, consented, rights-cleared, public-safe, or publishable. Publication requires downstream validation, EvidenceBundle closure, consent and sensitivity policy, review, release decision, receipts, proofs, and rollback support.

---

## Package boundary

```text
connectors/
└── familysearch/
    ├── README.md                  # connector-lane overview
    ├── src/
    │   └── familysearch/
    │       ├── README.md          # this file
    │       ├── __init__.py        # PROPOSED / NEEDS VERIFICATION
    │       ├── config.py          # PROPOSED / NEEDS VERIFICATION
    │       ├── client.py          # PROPOSED / NEEDS VERIFICATION
    │       ├── parser.py          # PROPOSED / NEEDS VERIFICATION
    │       ├── privacy.py         # PROPOSED / NEEDS VERIFICATION
    │       ├── envelope.py        # PROPOSED / NEEDS VERIFICATION
    │       └── errors.py          # PROPOSED / NEEDS VERIFICATION
    └── tests/
        └── README.md
```

The exact module layout is **PROPOSED**. Use the mounted repo’s actual code, package manager, imports, and CI conventions before treating any filename above as implemented.

---

## Authority boundary

```text
THIS PACKAGE MAY:
  parse synthetic or steward-approved FamilySearch-shaped payloads
  prepare reviewed source requests when live access is explicitly enabled
  emit connector-local source-admission envelopes
  preserve source references, retrieval metadata, citation metadata, timestamps, and digests
  return finite failure, deny, abstain, quarantine, or needs-verification outcomes
  support RAW or QUARANTINE admission

THIS PACKAGE MUST NOT:
  merge person identities as truth
  assert family relationships as truth
  infer consent
  publish living-person material
  handle raw DNA or DNA-derived hypotheses unless a separate deny-by-default policy allows quarantine-only handling
  write directly to PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, or release stores
  bypass source descriptors, source rights, sensitivity policy, consent policy, or review gates
  embed credentials, tokens, cookies, private account exports, or session material
  treat generated summaries as evidence
```

KFM lifecycle discipline remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This package participates only at the source-admission edge.

---

## Expected modules

The module names below are a recommended package contract, not a verified implementation inventory.

| Module | Status | Responsibility |
|---|---:|---|
| `config.py` | **PROPOSED** | Read connector configuration, feature flags, endpoint keys, timeout defaults, and no-network/no-account posture. |
| `client.py` | **PROPOSED** | Hold bounded FamilySearch request behavior; no live call unless explicitly enabled. |
| `parser.py` | **PROPOSED** | Convert FamilySearch-shaped responses or fixtures into candidate source records without asserting truth. |
| `privacy.py` | **PROPOSED** | Detect living-person, consent-unclear, private, revoked, account-only, or DNA-like markers and return safe outcomes. |
| `envelope.py` | **PROPOSED** | Build source-admission envelopes with source metadata, lifecycle target, digests, and review flags. |
| `errors.py` | **PROPOSED** | Define finite connector errors safe for logs and review. |
| `__init__.py` | **PROPOSED** | Expose a small public import surface; avoid importing live clients or reading secrets at module import time. |

Keep the import surface narrow. Downstream code should receive a governed connector output, not raw FamilySearch account behavior.

---

## Runtime posture

Default runtime behavior must be safe without special environment setup.

| Concern | Required posture |
|---|---|
| Network access | Disabled or mock-only by default in tests and local dry runs. |
| Account access | Disabled by default; no personal account required for default tests. |
| Credentials | Never required for import, parsing fixtures, or no-network tests. |
| Secrets | Never committed and never printed in exceptions. |
| Source descriptors | Required before live source activation. |
| Consent | Never inferred; missing, revoked, expired, or ambiguous consent fails closed. |
| Living-person material | Denied or quarantine/review-required by default. |
| Raw DNA / DNA-derived hints | Out of package scope unless an approved quarantine-only policy exists. |
| Writes | No direct writes outside allowed RAW or QUARANTINE handoff paths. |
| Publication | Not allowed from this package. |

Optional live behavior should require explicit opt-in, for example a repo-approved equivalent of:

```bash
KFM_ALLOW_LIVE_FAMILYSEARCH_TESTS=1
```

The exact flag name is **NEEDS VERIFICATION** against repo convention.

---

## Inputs and outputs

### Inputs

Expected input classes:

- source descriptor reference;
- connector configuration;
- FamilySearch endpoint or export identifier approved by source steward;
- request parameters allowed by source policy;
- synthetic local fixture payload for tests;
- optional live response body only when source-steward, privacy, and security approvals exist.

### Outputs

Expected output classes:

- parsed candidate person, relationship, event, place, or citation source object;
- source-admission envelope;
- privacy-gate result;
- finite error outcome;
- quarantine-safe drift signal;
- metadata bundle containing retrieval time, source label, endpoint key or source reference, digest, parser version, and review flags where applicable.

Outputs should be shaped for downstream governance. They should not be shaped as direct UI payloads, public claims, or truth assertions.

---

## Privacy and consent behavior

This package must make sensitive cases visible instead of smoothing them over.

Minimum behavior:

1. Living-person indicators must produce deny/quarantine/review-required outcomes.
2. Missing consent must never be treated as consent.
3. Revoked or expired consent must block re-emission.
4. Private account-only material must not be treated as public-safe.
5. Relationship assertions must remain candidate assertions until downstream evidence and review support them.
6. Person-place assertions involving living people must fail closed.
7. DNA-like fields must trigger deny/quarantine/drift behavior unless a separate approved policy exists.
8. Cache and retention behavior must be explicit before any live activation.

---

## Errors

Prefer explicit outcomes over ambiguous exceptions.

| Condition | Package behavior |
|---|---|
| Missing source descriptor | Refuse live activation; return actionable error. |
| Network disabled | Skip or fail with clear no-network outcome. |
| OAuth token missing | Default parser behavior still works with fixtures; live access abstains. |
| Unauthorized or forbidden response | Return finite error without credential leakage. |
| Timeout or rate limit | Return bounded connector error; do not spin or silently retry forever. |
| Empty response | Return `ABSTAIN`-style outcome unless empty is valid for that source. |
| Malformed payload | Return `ERROR` or quarantine-safe parser failure. |
| Living-person marker | Return `DENY`, quarantine, or review-required outcome. |
| Consent missing or revoked | Block public-safe output. |
| Unexpected schema drift | Return `NEEDS_VERIFICATION`-style drift signal. |
| Rights or sensitivity unknown | Route toward quarantine-safe handoff; do not publish. |

Exception messages should help maintainers fix the connector without leaking credentials, private account state, or over-copying source payloads.

---

## Tests

Connector-local tests belong in:

```text
connectors/familysearch/tests/
```

The local test README defines the no-network/no-account default, fixture posture, privacy gates, connector-local test classes, and acceptance checklist.

Likely test command, subject to repo verification:

```bash
python -m pytest connectors/familysearch/tests
```

The package should be easy to test with synthetic fixtures. Parser and privacy-gate functions should be callable without performing network I/O or reading credentials.

---

## Definition of done

This package is ready for first review when:

- [ ] Importing `familysearch` does not perform network I/O.
- [ ] Importing `familysearch` does not require credentials, OAuth tokens, cookies, or session exports.
- [ ] Connector configuration is explicit and testable.
- [ ] Live calls are opt-in and guarded.
- [ ] Source descriptor requirements are enforced before live activation.
- [ ] Parser behavior is covered by synthetic valid, empty, malformed, private, revoked, forbidden, timeout, and drift fixtures.
- [ ] Living-person and consent-missing cases fail closed.
- [ ] Candidate person and relationship assertions remain source-attributed.
- [ ] Connector outputs include retrieval metadata and digest support where applicable.
- [ ] Outputs target RAW or QUARANTINE handoff only.
- [ ] No code writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.
- [ ] Errors are finite, actionable, and safe to log.
- [ ] CI or local validation can run the no-network/no-account test suite.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual files under `connectors/familysearch/src/familysearch/`. | **NEEDS VERIFICATION** | Mounted repo tree or GitHub file listing beyond this README. |
| Confirm Python package manager and import path. | **NEEDS VERIFICATION** | `pyproject.toml`, workspace config, or connector package metadata. |
| Confirm root connector README contract. | **CONFIRMED path / NEEDS VERIFICATION content maturity** | `connectors/familysearch/README.md`. |
| Confirm source catalog page and source descriptor names. | **NEEDS VERIFICATION** | `docs/sources/catalog/familysearch/README.md` and source registry entries. |
| Confirm expected source-admission envelope schema. | **NEEDS VERIFICATION** | `schemas/contracts/v1/source/` and related contract docs. |
| Confirm test runner and no-network/no-account policy. | **NEEDS VERIFICATION** | `connectors/familysearch/tests/README.md`, root `tests/`, Makefile, and CI workflows. |
| Confirm consent, revocation, retention, tombstone, and cache invalidation rules. | **NEEDS VERIFICATION** | Policy docs and review decisions. |
| Confirm People/DNA/Land path segment convention. | **NEEDS VERIFICATION** | Directory Rules, ADRs, and current repo paths. |

---

## Maintainer note

Keep this package narrow and privacy-forward. It should make FamilySearch source material easier to parse, inspect, quarantine, and review. It must not turn private genealogy material, living-person details, weakly sourced relationships, or consent-unclear records into public KFM truth.
