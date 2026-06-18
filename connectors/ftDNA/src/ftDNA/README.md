<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ftdna-src-package-readme
title: connectors/ftDNA/src/ftDNA/ — FamilyTreeDNA Connector Python Package
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · People/DNA/Land steward · Consent steward · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: restricted-doctrine; consent-required; no-live-by-default
proposed_path: connectors/ftDNA/src/ftDNA/README.md
truth_posture: CONFIRMED path exists / PROPOSED package contract / UNKNOWN implementation depth
related:
  - ../../README.md
  - ../../../README.md
  - ../../tests/README.md
  - ../../../../docs/domains/people-dna-land/README.md
  - ../../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../../docs/domains/people-dna-land/SOURCE_FAMILIES.md
  - ../../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../../data/registry/sources/people-dna-land/
  - ../../../../data/raw/people-dna-land/
  - ../../../../data/quarantine/people-dna-land/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/consent/
  - ../../../../policy/consent/people/
  - ../../../../policy/sensitivity/people/
  - ../../../../policy/rights/
  - ../../../../release/
tags: [kfm, connectors, ftdna, familytreedna, python-package, people-dna-land, consent, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank package README for the proposed ftDNA connector implementation package."
  - "This package boundary is not a source registry, consent authority, interpretation engine, graph authority, release path, or publication surface."
  - "Import behavior, modules, source descriptor, source profile, allowed access method, consent sidecar behavior, tests, fixtures, CI wiring, and activation state remain NEEDS VERIFICATION."
  - "Package output may prepare RAW or QUARANTINE handoff candidates only; downstream validation, evidence closure, release, publication, correction, and rollback remain outside this package."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FamilyTreeDNA Connector Python Package

> Importable package boundary for the proposed ftDNA / FamilyTreeDNA connector.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Scope: package boundary" src="https://img.shields.io/badge/scope-package__boundary-blue">
  <img alt="Network: off by default" src="https://img.shields.io/badge/network-off__by__default-critical">
  <img alt="Consent: required" src="https://img.shields.io/badge/consent-required-critical">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/ftDNA/src/ftDNA/`

## Scope

This folder is the proposed implementation package for the ftDNA connector.

The package may contain small, testable helpers for:

- reading connector configuration;
- validating no-network defaults;
- checking source descriptor references;
- checking consent and rights references supplied by governed callers;
- parsing source-shaped fixture payloads;
- building source-admission envelopes;
- returning finite quarantine, abstain, review-required, or error outcomes.

The package must not contain credentials, live account material, source descriptors as authority records, policy decisions, schemas as authority records, release records, public claims, identity truth, interpretation truth, graph truth, or publication outputs.

---

## Expected package posture

Default behavior:

```text
import behavior: no network, no secret reads
live access: disabled unless explicitly enabled and reviewed
credentials: never committed
source activation: requires SourceDescriptor and review state
consent state: explicit where required
output target: RAW or QUARANTINE handoff candidates only
```

The exact module layout is **NEEDS VERIFICATION**. A possible package shape is:

```text
connectors/ftDNA/src/ftDNA/
├── README.md
├── __init__.py
├── config.py
├── client.py
├── parser.py
├── consent.py
├── envelope.py
└── errors.py
```

Treat these filenames as proposed until confirmed by the repo tree.

---

## Authority boundary

```text
THIS PACKAGE MAY:
  parse approved test fixtures
  enforce no-network defaults
  check required source and consent references
  build source-admission envelopes
  return finite review-required outcomes

THIS PACKAGE MUST NOT:
  publish data
  write processed/catalog/triplet/published outputs
  make public claims
  serve as consent authority
  serve as source registry authority
  bypass policy, review, release, or rollback gates
```

KFM lifecycle discipline remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This package participates only at the source-admission edge.

---

## Tests

Connector-local tests belong in:

```text
connectors/ftDNA/tests/
```

The package should be testable without network access, live accounts, or private exports.

Likely local command, subject to repo verification:

```bash
python -m pytest connectors/ftDNA/tests
```

---

## Definition of done

This package is ready for first review when:

- [ ] Importing the package performs no network I/O.
- [ ] Importing the package reads no live secrets.
- [ ] Live access is disabled by default.
- [ ] SourceDescriptor checks are explicit.
- [ ] Consent and rights references are explicit where required.
- [ ] Parser helpers work with synthetic or approved fixtures.
- [ ] Output is limited to RAW or QUARANTINE handoff candidates.
- [ ] Errors are finite, actionable, and safe to log.
- [ ] Tests cover no-network, missing descriptor, missing consent, revoked consent, malformed payload, rights-unclear, and review-required cases.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual package files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm Python package import name and case convention. | **NEEDS VERIFICATION** | Package metadata and import tests. |
| Confirm source profile and SourceDescriptor. | **NEEDS VERIFICATION** | Source catalog and registry entry. |
| Confirm consent-sidecar schema and storage path. | **NEEDS VERIFICATION** | Consent schemas and policy docs. |
| Confirm test runner and fixture strategy. | **NEEDS VERIFICATION** | Test tree, fixture registry, and CI workflow. |

---

## Maintainer note

Keep this package narrow and side-effect safe. It should help the connector prepare governed source-admission candidates without becoming a source registry, consent engine, interpretation engine, graph authority, release path, or public truth surface.
