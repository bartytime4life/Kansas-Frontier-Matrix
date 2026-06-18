<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ftdna-src-readme
title: connectors/ftDNA/src/ — FamilyTreeDNA Connector Source Root
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · People/DNA/Land steward · Consent steward · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: restricted-doctrine; consent-required; no-live-by-default
proposed_path: connectors/ftDNA/src/README.md
truth_posture: CONFIRMED path exists / PROPOSED source-root contract / UNKNOWN implementation depth
related:
  - ../README.md
  - ftDNA/README.md
  - ../tests/README.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../docs/domains/people-dna-land/SOURCE_FAMILIES.md
  - ../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../data/registry/sources/people-dna-land/
  - ../../../data/raw/people-dna-land/
  - ../../../data/quarantine/people-dna-land/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/consent/
  - ../../../policy/consent/people/
  - ../../../policy/sensitivity/people/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, ftdna, familytreedna, source-root, people-dna-land, consent, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank source-root README for the proposed ftDNA connector implementation."
  - "The implementation package boundary is documented at connectors/ftDNA/src/ftDNA/README.md."
  - "This source root is not a source registry, consent authority, interpretation engine, graph authority, release path, or publication surface."
  - "Source-root output may prepare RAW or QUARANTINE handoff candidates only; downstream validation, evidence closure, release, publication, correction, and rollback remain outside this source root."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FamilyTreeDNA Connector Source Root

> Source-code root for the proposed ftDNA / FamilyTreeDNA connector implementation.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Scope: source root" src="https://img.shields.io/badge/scope-source__root-blue">
  <img alt="Network: off by default" src="https://img.shields.io/badge/network-off__by__default-critical">
  <img alt="Consent: required" src="https://img.shields.io/badge/consent-required-critical">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/ftDNA/src/`

## Scope

`connectors/ftDNA/src/` is the source-code root for the proposed ftDNA connector.

It may contain the importable implementation package plus package metadata and source-level documentation. The deeper package boundary is documented in:

```text
connectors/ftDNA/src/ftDNA/README.md
```

This source root must not contain credentials, private exports, source descriptors as authority records, policy decisions, schemas as authority records, release records, public claims, graph truth, or publication outputs.

---

## Repo fit

```text
connectors/
└── ftDNA/
    ├── README.md
    ├── src/
    │   ├── README.md
    │   └── ftDNA/
    │       └── README.md
    └── tests/
        └── README.md
```

---

## Source-root posture

Default posture for this folder:

```text
import behavior: no network, no secret reads
live access: disabled unless explicitly enabled and reviewed
credentials: never committed
source activation: requires SourceDescriptor and review state
consent state: explicit where required
output target: RAW or QUARANTINE handoff candidates only
```

Implementation files and module names remain **NEEDS VERIFICATION** until the repo tree is inspected.

---

## Authority boundary

```text
THIS SOURCE ROOT MAY CONTAIN:
  connector implementation code
  package docs
  safe parser helpers
  source-admission envelope helpers
  finite error helpers

THIS SOURCE ROOT MUST NOT CONTAIN:
  source registry authority
  consent authority
  policy authority
  schema authority
  public claims
  processed records
  catalog or triplet records
  release records
  published outputs
```

KFM lifecycle discipline remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This source root participates only at the source-admission edge.

---

## Testing relationship

Connector-local tests live in:

```text
connectors/ftDNA/tests/
```

The source root should be testable without network access, live accounts, private exports, or secrets.

Likely local command, subject to repo verification:

```bash
python -m pytest connectors/ftDNA/tests
```

---

## Definition of done

This source root is ready for first review when:

- [ ] Source-root README exists and points to the package README.
- [ ] Importing package modules performs no network I/O.
- [ ] Importing package modules reads no live secrets.
- [ ] Live access is disabled by default.
- [ ] SourceDescriptor checks are explicit.
- [ ] Consent and rights references are explicit where required.
- [ ] Parser helpers work with synthetic or approved fixtures.
- [ ] Output is limited to RAW or QUARANTINE handoff candidates.
- [ ] Tests cover no-network, missing descriptor, missing consent, revoked consent, malformed payload, rights-unclear, and review-required cases.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual files below this source root. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm Python package import name and case convention. | **NEEDS VERIFICATION** | Package metadata and import tests. |
| Confirm source profile and SourceDescriptor. | **NEEDS VERIFICATION** | Source catalog and registry entry. |
| Confirm consent-sidecar schema and storage path. | **NEEDS VERIFICATION** | Consent schemas and policy docs. |
| Confirm test runner and fixture strategy. | **NEEDS VERIFICATION** | Test tree, fixture registry, and CI workflow. |

---

## Maintainer note

Keep this source root narrow and side-effect safe. It should organize connector implementation code without becoming a source registry, consent engine, interpretation engine, graph authority, release path, or public truth surface.
