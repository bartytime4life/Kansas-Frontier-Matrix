<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-familysearch-src-readme
title: connectors/familysearch/src/ — FamilySearch Connector Source Root
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Source steward · People/DNA/Land steward · Privacy/consent steward · Rights reviewer · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-07-11
policy_label: public-doctrine; source-root; high-sensitivity; greenfield; no-network-default; raw-or-quarantine-only; no-publication
proposed_path: connectors/familysearch/src/README.md
truth_posture: CONFIRMED source-root scaffold / PLACEHOLDER implementation / NOT ACTIVATED / live source behavior UNKNOWN
related:
  - ../README.md
  - ../pyproject.toml
  - ../tests/README.md
  - familysearch/README.md
  - familysearch/descriptor.yaml
  - familysearch/fetch.py
  - ../../../docs/sources/catalog/familysearch.md
  - ../../../docs/sources/catalog/familysearch/README.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/domains/people-dna-land/CONSENT.md
  - ../../../docs/domains/people-dna-land/CONSENT_MODEL.md
  - ../../../data/registry/people-dna-land/sources/familysearch.yaml
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, familysearch, source-root, python, genealogy, people-dna-land, consent, living-person, source-admission, greenfield, raw, quarantine, governance]
notes:
  - "The current source root contains one package directory with a README, a placeholder descriptor, and a one-line fetcher placeholder; no importable or executable connector implementation is proved."
  - "The package metadata names kfm-connector-familysearch at version 0.0.0 but does not yet prove package discovery, dependencies, entry points, build configuration, or an importable familysearch namespace."
  - "Source identity, descriptor authority, role, rights, sensitivity, and access posture remain inconsistent or unresolved across package-local, registry, and catalog artifacts."
  - "The package-local sensitivity_floor: public value is a placeholder and must not be treated as a privacy, consent, activation, or release decision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FamilySearch Connector Source Root

> Evidence-grounded contract for the greenfield FamilySearch connector source tree. This root may eventually hold importable source-admission code, but the current repository state proves only a scaffold—not a runnable connector, active source integration, or publication path.

<p>
  <img alt="Status: greenfield draft" src="https://img.shields.io/badge/status-greenfield__draft-yellow">
  <img alt="Implementation: placeholder only" src="https://img.shields.io/badge/implementation-placeholder__only-lightgrey">
  <img alt="Activation: not activated" src="https://img.shields.io/badge/activation-not__activated-critical">
  <img alt="Network: live access not implemented" src="https://img.shields.io/badge/network-live__access__not__implemented-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

`connectors/familysearch/src/`

> [!IMPORTANT]
> **Confirmed state:** this root contains this README and one package directory. The package directory contains its own README, a placeholder `descriptor.yaml`, and a one-line placeholder `fetch.py`. No `__init__.py`, parser, client, privacy gate, handoff builder, fixtures, executable tests, package installation evidence, or CI proof is confirmed.

**Quick jumps:** [Purpose](#purpose) · [Verified repository state](#verified-repository-state) · [Evidence ledger](#evidence-ledger) · [Responsibility boundary](#responsibility-boundary) · [Blocking drift](#blocking-drift) · [Required source-root posture](#required-source-root-posture) · [Target structure](#target-structure) · [Packaging contract](#packaging-contract) · [Lifecycle handoff](#lifecycle-handoff) · [Privacy and consent](#privacy-and-consent) · [Testing relationship](#testing-relationship) · [Implementation sequence](#implementation-sequence) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Purpose

`connectors/familysearch/src/` is the source-code root reserved for the FamilySearch connector package.

Its future responsibility is limited to implementation code that can:

- read explicit, validated connector configuration;
- consume synthetic fixtures or steward-approved FamilySearch responses;
- perform opt-in source access only after source activation, rights, privacy, consent, and security gates are satisfied;
- preserve source identifiers, contributor labels, citations, retrieval times, temporal fields, and digests;
- keep person, relationship, event, place, and citation material as source-attributed candidate assertions;
- detect conditions requiring `DENY`, `ABSTAIN`, `ERROR`, quarantine, or human review;
- construct bounded handoff envelopes for governed RAW or QUARANTINE admission;
- remain deterministic and testable without a network, account, token, cookie, browser session, or private export.

This source root does not establish genealogy truth, person identity, relationship truth, consent, rights, sensitivity, source activation, release eligibility, or publication authority.

[Back to top ↑](#top)

---

## Verified repository state

The following structure is confirmed on the repository's `main` branch at the time of this update:

```text
connectors/familysearch/
├── README.md
├── pyproject.toml
├── src/
│   ├── README.md
│   └── familysearch/
│       ├── README.md
│       ├── descriptor.yaml
│       └── fetch.py
└── tests/
    └── README.md
```

### Current maturity

| Surface | Confirmed content | Maturity |
|---|---|---:|
| `src/README.md` | This source-root contract. | **DOCUMENTED** |
| `src/familysearch/README.md` | Evidence-grounded package-boundary contract. | **DOCUMENTED** |
| `src/familysearch/fetch.py` | One-line greenfield placeholder comment. | **PLACEHOLDER** |
| `src/familysearch/descriptor.yaml` | `name: familysearch`; unresolved role and rights; placeholder `sensitivity_floor: public`. | **PLACEHOLDER / BLOCKED** |
| `pyproject.toml` | Project name `kfm-connector-familysearch`; version `0.0.0`. | **PLACEHOLDER** |
| `tests/README.md` | Proposed connector-local test contract. | **DOCUMENTED / UNIMPLEMENTED** |

The directory resembles a `src`-layout Python project, but the repository evidence does not yet prove:

- that `familysearch` is importable;
- that the package is discoverable by a build backend;
- that dependencies or entry points are declared;
- that the connector can run;
- that a source is activated;
- that any live endpoint, OAuth flow, rate limit, cache, retry, or retention behavior exists;
- that tests execute or CI includes this connector.

> [!CAUTION]
> Do not describe this connector as installed, operational, integrated, compliant, or publication-ready until code, tests, activation records, and validation evidence support those claims.

[Back to top ↑](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not support |
|---|---:|---|---|
| `connectors/familysearch/src/` tree | **CONFIRMED** | The source root and package scaffold exist. | Runtime maturity, package installation, source activation, or CI. |
| `familysearch/fetch.py` | **CONFIRMED placeholder** | A future fetcher location has been reserved. | HTTP behavior, OAuth, retry, rate limiting, parsing, or handoff behavior. |
| `familysearch/descriptor.yaml` | **CONFIRMED placeholder** | The scaffold anticipates connector-local source metadata. | Canonical SourceDescriptor authority, rights clearance, role assignment, sensitivity approval, or activation. |
| `../pyproject.toml` | **CONFIRMED placeholder** | A project name and version are reserved. | Build backend, package discovery, dependencies, executable commands, or import success. |
| `familysearch/README.md` | **CONFIRMED** | The package boundary, current scaffold, blockers, and future contract are documented. | Implemented package behavior. |
| `../tests/README.md` | **CONFIRMED documentation** | Expected no-network, synthetic-fixture, privacy, drift, and error test classes are described. | Executable tests or passing CI. |
| `data/registry/people-dna-land/sources/familysearch.yaml` | **CONFIRMED proposed registry record** | A registry candidate exists under the current People/DNA/Land path. | Final role, rights, sensitivity, access posture, or activation. |
| FamilySearch catalog documents | **CONFIRMED draft documentation** | FamilySearch is treated as a high-sensitivity genealogy upstream with deny-by-default living-person posture. | Current live API behavior, source terms, implemented OAuth, or approved release. |
| People/DNA/Land consent documentation | **CONFIRMED doctrine / proposed implementation** | Consent is independent, revocable, fail-closed, and does not itself publish data. | Implemented consent runtime or connector integration. |

[Back to top ↑](#top)

---

## Responsibility boundary

### This source root may contain

- importable FamilySearch connector package code;
- configuration models and explicit feature gates;
- bounded client helpers;
- payload parsers and source-shape adapters;
- privacy, consent-state, rights-state, and sensitivity signal evaluators;
- candidate-assertion models local to connector intake;
- RAW/QUARANTINE handoff-envelope builders;
- deterministic error and drift types;
- package-local constants that do not become policy authority;
- package documentation.

### This source root must not contain

- canonical SourceDescriptor records;
- SourceActivationDecision authority;
- consent grants, revocation authority, or consent policy decisions;
- rights or sensitivity policy authority;
- canonical object contracts or schemas;
- private account exports or copied living-person payloads;
- credentials, OAuth tokens, cookies, browser sessions, or refresh tokens;
- processed, catalog, triplet, published, proof, receipt, release, or rollback artifacts;
- public claims about people, relationships, dates, places, DNA, or land ownership;
- generated summaries treated as evidence;
- hidden publication or promotion side effects.

The connector source tree participates only at the source-admission edge.

[Back to top ↑](#top)

---

## Blocking drift

The repository currently contains unresolved conflicts that must be settled before implementation or live activation.

| Drift | Current evidence | Required resolution |
|---|---|---|
| Source identity | Package and registry use `familysearch`; one catalog document proposes `familysearch-api`. | Select one canonical `source_id`; migrate references intentionally. |
| Descriptor authority | A descriptor-like file exists inside the package, while a registry record exists under `data/registry/people-dna-land/sources/`. | Confirm the canonical registry home; treat the package-local file as non-authoritative or remove it. |
| Source role | Package-local and registry descriptors leave role as `TBD`; catalog prose uses broader source-role language. | Assign an allowed governed role only through source-steward review. |
| Rights | Package-local and registry descriptors leave rights unresolved. | Complete terms, attribution, redistribution, caching, retention, and derived-use review. |
| Sensitivity | Package-local descriptor says `public`; registry record says `TBD`; doctrine treats living-person material as deny-by-default. | Remove or replace the unsafe placeholder; establish a reviewed sensitivity floor and handling obligations. |
| Access posture | Registry access posture is unresolved; package contains no client or OAuth code. | Define approved access mode, credential custody, scopes, revocation, and no-network default. |
| Catalog placement | Both flat and nested FamilySearch catalog surfaces exist, and the nested umbrella remains a stub. | Select canonical documentation placement and maintain redirects or migration notes as needed. |
| Domain path naming | Repository references use both `people-dna-land` and `people-genealogy-dna-land`. | Follow the accepted Directory Rules and ADR outcome before creating new paths. |

> [!WARNING]
> The package-local `sensitivity_floor: public` field is not a safe default. Until reviewed sensitivity, consent, rights, and activation records exist, FamilySearch-derived living-person, private-tree, account-mediated, person-place, and relationship material must fail closed or remain in quarantine-safe handling.

[Back to top ↑](#top)

---

## Required source-root posture

Any future code under this root must satisfy these defaults:

| Concern | Required posture |
|---|---|
| Network | Disabled unless an explicit reviewed live-access path is invoked. |
| Account access | Not required for imports, fixture parsing, unit tests, or default CI. |
| Secrets | Never stored in source, descriptors, fixtures, logs, exceptions, or committed configuration. |
| Source activation | Required before any live request. |
| Rights | Unresolved rights produce abstention or quarantine, never silent continuation. |
| Sensitivity | Living-person and private-account material fails closed by default. |
| Consent | Missing, expired, revoked, unverifiable, or mismatched consent is never treated as consent. |
| Assertions | Person and relationship records remain source-attributed candidates. |
| Writes | No direct writes beyond an approved RAW or QUARANTINE handoff boundary. |
| Publication | Forbidden from connector code. |
| Errors | Finite, deterministic, actionable, and safe to log. |
| Retries | Bounded and explicit; never infinite or silent. |
| Caching | Disabled until rights, retention, revocation, encryption, and invalidation rules are approved. |

[Back to top ↑](#top)

---

## Target structure

The current scaffold is not the target implementation. A possible reviewed package structure is:

```text
connectors/familysearch/src/
├── README.md
└── familysearch/
    ├── README.md
    ├── __init__.py
    ├── config.py
    ├── client.py
    ├── parser.py
    ├── privacy.py
    ├── handoff.py
    ├── errors.py
    └── fetch.py
```

| Module | Proposed responsibility |
|---|---|
| `__init__.py` | Small side-effect-free public import surface. |
| `config.py` | Validated configuration, activation references, no-network defaults, timeouts, and bounded retry settings. |
| `client.py` | Explicit opt-in HTTP/OAuth behavior after activation and security review. |
| `fetch.py` | Orchestrate bounded retrieval without parsing, truth promotion, or publication. |
| `parser.py` | Convert source-shaped payloads into source-attributed candidate records. |
| `privacy.py` | Produce privacy, consent-state, rights-state, sensitivity, and review signals without becoming policy authority. |
| `handoff.py` | Construct governed RAW or QUARANTINE admission envelopes. |
| `errors.py` | Define finite connector failures and source-shape drift outcomes safe for logs. |

This map is **PROPOSED**. Do not create modules merely because they appear here; implementation must follow accepted contracts, schemas, tests, source-review decisions, and repository conventions.

[Back to top ↑](#top)

---

## Packaging contract

Before the source root can be called an importable Python package, `pyproject.toml` and the package tree must prove:

- an accepted build backend;
- `src`-layout package discovery;
- the intended import name;
- supported Python versions;
- runtime and development dependencies;
- optional live-access dependency separation, if needed;
- entry points or commands, if any;
- no import-time network or secret access;
- reproducible installation in the repository's supported environment;
- executable import tests.

A project name alone does not prove an import name. The current `kfm-connector-familysearch` metadata must not be used as evidence that `import familysearch` succeeds.

[Back to top ↑](#top)

---

## Lifecycle handoff

Future connector code may prepare source material for the beginning of the KFM lifecycle only:

```text
FamilySearch source material
  -> explicit source activation and access gate
  -> connectors/familysearch/src/familysearch/
  -> RAW or QUARANTINE handoff
  -> downstream governed processing, evidence closure, policy, review, release, and rollback
```

The full lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

| Lifecycle surface | Source-root role |
|---|---|
| Pre-RAW contact | May perform bounded access only after activation and review. |
| RAW | May construct an admission payload and metadata envelope if the accepted intake contract permits it. |
| QUARANTINE | May route malformed, private, living-person, rights-unclear, consent-unclear, sensitivity-unclear, or source-drift material to a quarantine-safe outcome. |
| WORK / PROCESSED | No direct ownership. |
| CATALOG / TRIPLET | No direct ownership. |
| PUBLISHED | Forbidden. |
| PROOF / RECEIPT / RELEASE | May supply safe inputs for downstream systems, but must not claim authority or write directly without an accepted contract. |

Publication is a governed state transition, not a connector write or file move.

[Back to top ↑](#top)

---

## Privacy and consent

FamilySearch material may expose living people, private family relationships, contributor notes, private-tree state, account-mediated records, person-place assertions, or inferred relationship claims.

Minimum future behavior:

1. Living-person indicators produce denial, quarantine, or review-required outcomes by default.
2. Missing consent is not consent.
3. Revoked, expired, unverifiable, or scope-mismatched consent blocks re-emission.
4. Consent does not create publication authority.
5. Private account access does not make retrieved material public-safe.
6. Relationship assertions remain candidate assertions until downstream evidence and review support them.
7. Person-place assertions involving living people fail closed.
8. DNA data and DNA-derived hints remain out of this connector's default scope.
9. Caching, retention, tombstone, and invalidation behavior must be approved before live activation.
10. Source terms and rights must be evaluated independently from consent and sensitivity.

[Back to top ↑](#top)

---

## Testing relationship

Connector-local executable tests belong under:

```text
connectors/familysearch/tests/
```

The source root should be designed for tests that require no internet or account access:

- import safety;
- package installation and discovery;
- default no-network configuration;
- bounded client behavior with mocked transport;
- synthetic person, relationship, event, place, and citation parsing;
- living-person, private, consent-missing, revoked, rights-unclear, and sensitivity-unclear gates;
- malformed, empty, unauthorized, forbidden, timeout, rate-limit, and schema-drift outcomes;
- RAW/QUARANTINE-only handoff validation;
- secret and payload leakage prevention;
- proof that no processed, catalog, triplet, published, proof, receipt, or release writes occur.

No executable test files are currently confirmed. A command such as the following remains **NEEDS VERIFICATION** until packaging and test configuration exist:

```bash
python -m pytest connectors/familysearch/tests
```

[Back to top ↑](#top)

---

## Implementation sequence

Build work should proceed in this order:

1. Resolve canonical source ID, descriptor authority, domain path, source role, rights, sensitivity, and access posture.
2. Replace unsafe descriptor placeholders with governed references or remove the package-local descriptor.
3. Complete `pyproject.toml` with accepted build and package-discovery configuration.
4. Add a side-effect-free import surface and executable import tests.
5. Define connector-local configuration and finite error models.
6. Add synthetic fixtures and parser tests before live access code.
7. Implement privacy, consent-state, rights-state, sensitivity, and drift signals with fail-closed tests.
8. Define and validate the RAW/QUARANTINE handoff envelope against accepted contracts and schemas.
9. Add a fully mocked bounded client.
10. Consider live access only after source activation, terms, security, credential, privacy, consent, retention, and audit review.
11. Wire default no-network tests into CI and retain evidence of passing runs.
12. Document rollback, cache invalidation, source suspension, and deactivation behavior before production use.

[Back to top ↑](#top)

---

## Definition of done

This source root is ready to move beyond greenfield status only when:

- [x] The source-root responsibility boundary is documented.
- [x] The package-boundary README reflects the confirmed scaffold.
- [ ] Canonical source identity and descriptor authority are resolved.
- [ ] Source role, rights, sensitivity, and access posture are reviewed and no longer `TBD`.
- [ ] The unsafe package-local `sensitivity_floor: public` placeholder is removed or replaced through governance.
- [ ] `pyproject.toml` defines a working, reproducible package build.
- [ ] The intended package import succeeds in a clean supported environment.
- [ ] Imports perform no network or secret access.
- [ ] Synthetic fixtures cover valid, empty, malformed, private, living-person, revoked, rights-unclear, and drift cases.
- [ ] Parser, privacy, error, and handoff behaviors have executable tests.
- [ ] Live access is absent or explicitly opt-in, activated, reviewed, bounded, and credential-safe.
- [ ] Connector outputs are limited to governed RAW or QUARANTINE handoff.
- [ ] No connector code publishes, promotes, merges identities as truth, or writes directly to downstream authority roots.
- [ ] CI runs the no-network connector test suite.
- [ ] Source suspension, deactivation, rollback, retention, and cache invalidation are documented and testable.

[Back to top ↑](#top)

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm canonical FamilySearch `source_id`. | **BLOCKED** | Accepted source-registry decision and migrated references. |
| Confirm descriptor authority and remove duplicate authority signals. | **BLOCKED** | Directory Rules/ADR plus registry steward decision. |
| Resolve role, rights, sensitivity, and access posture. | **BLOCKED** | Source, rights, privacy, consent, and security review. |
| Confirm current FamilySearch source terms and supported access model. | **NEEDS VERIFICATION** | Current source-steward evidence; do not infer from stale docs. |
| Confirm package build backend and `src` discovery. | **NEEDS VERIFICATION** | Completed `pyproject.toml` and clean installation test. |
| Confirm intended import name. | **NEEDS VERIFICATION** | Import test and package metadata. |
| Confirm source-admission envelope contract and schema. | **NEEDS VERIFICATION** | Accepted contracts, schemas, and validation tests. |
| Confirm consent, revocation, retention, tombstone, and cache-invalidation implementation. | **NEEDS VERIFICATION** | Code, policy wiring, tests, and review evidence. |
| Confirm fixture authority and synthetic-fixture review. | **NEEDS VERIFICATION** | Fixture files, metadata, and sensitivity review. |
| Confirm executable connector tests and CI wiring. | **NEEDS VERIFICATION** | Test files, workflow configuration, and passing logs. |
| Confirm canonical FamilySearch catalog placement. | **NEEDS VERIFICATION** | Documentation ADR or maintained migration decision. |
| Confirm People/DNA/Land domain path convention. | **NEEDS VERIFICATION** | Accepted Directory Rules and ADR outcome. |

---

## Maintainer note

Keep `connectors/familysearch/src/` small, explicit, reversible, and privacy-forward. The source tree may help retrieve, parse, classify, and quarantine FamilySearch material, but it must never make that material appear more true, more public, more consented, more rights-cleared, or more release-ready than the governing evidence supports.

[Back to top ↑](#top)
