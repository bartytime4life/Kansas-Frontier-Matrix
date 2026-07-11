<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-familysearch-src-package-readme
title: connectors/familysearch/src/familysearch/ — FamilySearch Connector Package Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Source steward · People/DNA/Land steward · Privacy/consent steward · Rights reviewer · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-07-11
policy_label: public-doctrine; package-boundary; high-sensitivity; greenfield; no-network-default; raw-or-quarantine-only; no-publication
proposed_path: connectors/familysearch/src/familysearch/README.md
truth_posture: CONFIRMED scaffold inventory / PLACEHOLDER implementation / NOT ACTIVATED / live source behavior UNKNOWN
related:
  - ../../README.md
  - ../README.md
  - ../../tests/README.md
  - ../../pyproject.toml
  - descriptor.yaml
  - fetch.py
  - ../../../../docs/sources/catalog/familysearch.md
  - ../../../../docs/sources/catalog/familysearch/README.md
  - ../../../../docs/domains/people-dna-land/README.md
  - ../../../../docs/domains/people-dna-land/CONSENT.md
  - ../../../../docs/domains/people-dna-land/CONSENT_MODEL.md
  - ../../../../data/registry/people-dna-land/sources/familysearch.yaml
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/sensitivity/
  - ../../../../release/
tags: [kfm, connectors, familysearch, python-package, genealogy, people-dna-land, consent, living-person, source-admission, greenfield, raw, quarantine, governance]
notes:
  - "The current package is a greenfield scaffold: README.md, descriptor.yaml, and a one-line fetch.py placeholder are confirmed; no importable package surface or implemented connector behavior is proved."
  - "The package-local descriptor, registry descriptor, and source-catalog documents currently disagree or remain unresolved on source identity, role, rights, sensitivity, and canonical descriptor path."
  - "The package-local sensitivity_floor: public value is a placeholder and must not be interpreted as a release or privacy decision."
  - "No live FamilySearch access, OAuth behavior, endpoint coverage, parser, privacy gate, handoff writer, fixtures, executable tests, CI wiring, or publication path is confirmed by this package."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FamilySearch Connector Package Boundary

> Evidence-grounded package contract for the greenfield FamilySearch connector scaffold. This package may eventually support governed source intake, parsing, privacy evaluation, and RAW-or-QUARANTINE handoff, but the current repository state does **not** implement those behaviors.

<p>
  <img alt="Status: greenfield draft" src="https://img.shields.io/badge/status-greenfield__draft-yellow">
  <img alt="Implementation: placeholder only" src="https://img.shields.io/badge/implementation-placeholder__only-lightgrey">
  <img alt="Activation: not activated" src="https://img.shields.io/badge/activation-not__activated-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

`connectors/familysearch/src/familysearch/`

> [!IMPORTANT]
> **Confirmed state:** this directory contains this README, a placeholder `descriptor.yaml`, and a one-line placeholder `fetch.py`. The connector is not demonstrated to be importable, executable, source-activated, rights-cleared, consent-ready, tested, or publishable.

**Quick jumps:** [Purpose](#purpose) · [Verified repository state](#verified-repository-state) · [Evidence ledger](#evidence-ledger) · [Authority boundary](#authority-boundary) · [Blocking drift](#blocking-drift) · [Required runtime posture](#required-runtime-posture) · [Target package contract](#target-package-contract) · [Data handling](#data-handling) · [Validation](#validation) · [Implementation sequence](#implementation-sequence) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Purpose

`connectors/familysearch/src/familysearch/` is the proposed Python package namespace for FamilySearch-specific source-admission helpers.

Its future role is narrow:

- accept only steward-approved configuration and source references;
- retrieve source material only through an explicit, reviewed, opt-in live-access path;
- parse synthetic fixtures or approved source responses without upgrading them to truth;
- preserve source, contributor, citation, retrieval, temporal, and digest metadata;
- keep person, relationship, event, place, and citation records as candidate assertions;
- detect privacy, consent, rights, sensitivity, and source-shape conditions that require denial, abstention, quarantine, or review;
- construct bounded handoff envelopes for governed RAW or QUARANTINE admission;
- expose deterministic behavior that can be tested without a network, account, token, cookie, or private export.

This package is an adapter boundary. It is not a genealogy knowledge base, person registry, relationship authority, consent registry, public API, release engine, or publication surface.

[Back to top ↑](#top)

---

## Verified repository state

The following scaffold is confirmed on the repository's `main` branch at the time of this update:

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

### Current file maturity

| File | Confirmed content | Maturity |
|---|---|---:|
| `README.md` | This package-boundary document. | **DOCUMENTED** |
| `descriptor.yaml` | `name: familysearch`; `role: TBD`; `rights: TBD`; `sensitivity_floor: public`. | **PLACEHOLDER / BLOCKED** |
| `fetch.py` | One comment identifying a greenfield fetcher placeholder. | **PLACEHOLDER** |
| `../../pyproject.toml` | Project name `kfm-connector-familysearch`; version `0.0.0`; no confirmed build, dependencies, entry points, or package discovery. | **PLACEHOLDER** |
| `../../tests/README.md` | Detailed proposed test contract; no executable connector tests are confirmed beside it. | **DOCUMENTED / UNIMPLEMENTED** |

No `__init__.py`, parser, client, configuration module, privacy gate, handoff-envelope builder, error model, fixtures, or executable tests are confirmed in this package.

> [!CAUTION]
> The directory name resembles a Python package, but the current scaffold does not prove that `import familysearch` works. Do not describe this connector as installed, runnable, or integrated until package metadata, an import surface, tests, and CI evidence exist.

[Back to top ↑](#top)

---

## Evidence ledger

| Evidence | Status | What it supports | What it does not support |
|---|---:|---|---|
| `connectors/familysearch/src/familysearch/README.md` | **CONFIRMED** | Package documentation exists. | Runtime implementation or activation. |
| `connectors/familysearch/src/familysearch/fetch.py` | **CONFIRMED placeholder** | A future fetcher filename has been reserved. | HTTP behavior, OAuth, retries, rate limiting, parsing, or safe output. |
| `connectors/familysearch/src/familysearch/descriptor.yaml` | **CONFIRMED placeholder** | A connector-local descriptor sketch exists. | Canonical descriptor authority, approved role, rights, or sensitivity. |
| `connectors/familysearch/pyproject.toml` | **CONFIRMED placeholder** | Intended distribution name and initial version are visible. | Build backend, dependencies, importability, packaging, or installation. |
| `data/registry/people-dna-land/sources/familysearch.yaml` | **CONFIRMED greenfield descriptor** | A domain registry record exists with `id: familysearch`. | Approved source activation, role, authority, rights, sensitivity, cadence, or access posture. |
| `docs/sources/catalog/familysearch/README.md` | **CONFIRMED draft dossier** | Human-facing source governance, lifecycle, consent, and sensitivity posture. | Runtime authorization or implementation proof. |
| `docs/sources/catalog/familysearch.md` | **CONFIRMED stub** | Umbrella source-family placeholder and links. | Canonical descriptor path or completed source-family documentation. |
| `docs/domains/people-dna-land/CONSENT.md` | **CONFIRMED draft doctrine** | Consent is separate from rights and sensitivity; missing, expired, or revoked consent fails closed; consent does not publish. | Implemented consent-gate machinery. |
| Package tests and CI | **NOT CONFIRMED** | Nothing beyond documentation. | Passing behavior, no-network enforcement, privacy safety, or integration readiness. |

Documentation and placeholders are evidence of intent, not evidence of working connector behavior.

[Back to top ↑](#top)

---

## Authority boundary

```text
THIS PACKAGE MAY EVENTUALLY:
  load explicit connector configuration
  validate descriptor and activation preconditions
  retrieve approved FamilySearch source material through opt-in live access
  parse synthetic fixtures or approved responses
  preserve source and citation provenance
  classify records for RAW or QUARANTINE handoff
  return finite ALLOW-TO-ADMIT / DENY / ABSTAIN / ERROR-style connector outcomes

THIS PACKAGE MUST NOT:
  decide that a person identity is canonical
  decide that a family relationship is true
  infer consent from source availability or account access
  treat rights clearance as consent
  treat consent as publication permission
  publish living-person or private genealogy material
  handle raw DNA or DNA-derived hypotheses without a separately approved restricted workflow
  decide source activation, sensitivity tier, redaction, release class, or public visibility
  write directly to WORK, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, or release authority stores
  embed credentials, OAuth tokens, cookies, session exports, or private account payloads
  turn generated summaries into evidence
```

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This package may participate only at the source-contact and admission edge. Promotion is a governed state transition performed elsewhere.

[Back to top ↑](#top)

---

## Blocking drift

The current scaffold contains unresolved conflicts that must be corrected before live implementation or activation.

| Concern | Observed state | Required resolution |
|---|---|---|
| Source identity | Package and registry use `familysearch`; the source dossier proposes `familysearch-api`. | Select one canonical `source_id`, document aliases if needed, and update all descriptors, receipts, catalog pages, fixtures, and tests consistently. |
| Descriptor authority | A package-local `descriptor.yaml` exists, while the domain registry contains `data/registry/people-dna-land/sources/familysearch.yaml`; the umbrella stub names another path pattern. | Confirm the authoritative registry home. Package-local descriptors must be examples, generated copies, or references—not parallel authority. |
| Source role | Package and registry descriptors leave role as `TBD`; the dossier describes scoped candidate/observation behavior. | Approve a role from the accepted source-role vocabulary and preserve it through handoff. |
| Rights | Both descriptors leave rights unresolved. | Complete terms, attribution, redistribution, retention, and permitted-use review before activation. |
| Sensitivity | Package-local descriptor says `public`; registry says `TBD`; domain and source docs treat living-person material as deny-by-default. | Remove or replace the unsafe placeholder. No source-wide `public` floor may override record-level privacy, consent, rights, and sensitivity evaluation. |
| Access posture | Registry access posture is `TBD`; no client or OAuth implementation exists. | Define approved access mode, credential handling, scopes, rate limits, logging, retention, and revocation behavior. |
| Packaging | `pyproject.toml` has only name and version; package has no confirmed import surface. | Add reviewed build metadata, package discovery, supported Python range, dependencies, and import-safety tests. |
| Tests | Only a test README is confirmed. | Add deterministic synthetic tests and CI wiring before claiming implementation maturity. |

> [!WARNING]
> `sensitivity_floor: public` in the package-local placeholder is **not** an approved policy decision. Until descriptor reconciliation and privacy review are complete, FamilySearch-derived material must be treated as unresolved and routed to deny, abstain, or quarantine-safe handling.

[Back to top ↑](#top)

---

## Required runtime posture

Any future implementation must start from these defaults:

| Concern | Required posture |
|---|---|
| Network | Off by default. No network access during import, fixture parsing, or default tests. |
| Account access | Off by default. A personal FamilySearch account must never be required for normal development or CI. |
| Live activation | Requires an approved canonical descriptor, activation decision, source/rights review, security review, and privacy/consent review. |
| Credentials | Supplied only through approved secret management; never committed, cached in fixtures, or printed. |
| Source role | Explicit and preserved; never silently upgraded from candidate or observation material to authority. |
| Consent | Never inferred. Missing, unverifiable, expired, revoked, or scope-mismatched consent fails closed. |
| Rights | Evaluated independently from consent and sensitivity. Unresolved rights block live admission or route to quarantine. |
| Living-person data | Deny, abstain, or quarantine/review-required by default. |
| Private account material | Not public-safe and not retained without an approved retention purpose and deletion path. |
| DNA-like content | Outside this package's default scope; trigger deny/quarantine and a drift signal. |
| Writes | Limited to an approved RAW or QUARANTINE handoff interface; no hidden filesystem or database side effects. |
| Errors | Finite, deterministic, actionable, and safe to log without copying sensitive payloads. |
| Publication | Impossible from this package. |

Importing the package must remain side-effect free. Live behavior must be called explicitly and must be impossible to trigger through import-time configuration.

[Back to top ↑](#top)

---

## Target package contract

The following map is a **proposed implementation decomposition**, not a claim that these modules exist:

```text
connectors/familysearch/src/familysearch/
├── README.md            # CONFIRMED — this document
├── __init__.py          # PROPOSED — narrow, side-effect-free public surface
├── config.py            # PROPOSED — explicit no-network defaults and validated settings
├── descriptors.py       # PROPOSED — canonical descriptor reference and activation checks
├── client.py            # PROPOSED — bounded, opt-in live-source access
├── parser.py            # PROPOSED — source-shaped payload to candidate records
├── privacy.py           # PROPOSED — living-person, consent, private, DNA-like, and retention gates
├── handoff.py           # PROPOSED — RAW/QUARANTINE admission envelope construction
├── errors.py            # PROPOSED — finite connector outcomes and safe errors
├── descriptor.yaml      # CONFIRMED placeholder — reconcile or remove as parallel authority
└── fetch.py             # CONFIRMED placeholder — replace, rename, or retire through review
```

### Responsibility rules

- `config.py` must validate explicit settings and default to no network and no account.
- `descriptors.py` must reference the accepted registry authority rather than inventing a second descriptor authority.
- `client.py` must not own policy decisions and must not perform unbounded retries.
- `parser.py` must preserve uncertainty and unsupported fields without fabricating values.
- `privacy.py` may produce connector-level routing signals, but final consent, sensitivity, and release authority remain outside the connector.
- `handoff.py` must create admission-ready envelopes, not processed records or public API payloads.
- `errors.py` must separate source unavailability, auth failure, malformed data, drift, policy denial, and unresolved governance conditions.
- `__init__.py` must not instantiate a client, read secrets, or perform network I/O.

Do not create these modules solely because they appear in this README. Implement them only with corresponding contracts, tests, and reviewed repository conventions.

[Back to top ↑](#top)

---

## Data handling

### Candidate inputs

A future implementation may accept:

- a canonical FamilySearch source descriptor reference;
- an approved source activation decision or activation identifier;
- explicit connector configuration;
- approved endpoint, collection, record, export, or source identifiers;
- synthetic source-shaped fixtures;
- approved response payloads supplied directly to parser functions;
- request context needed for rights, privacy, consent, retention, and audit evaluation.

### Candidate outputs

A governed connector output should contain only what downstream admission needs, such as:

- candidate person, relationship, event, place, and citation records;
- source identity and source-role metadata;
- retrieval time and request-scope metadata;
- upstream record, collection, or citation references;
- parser and connector version identifiers;
- content digest or payload digest references where permitted;
- rights, sensitivity, consent, retention, and review flags;
- explicit uncertainty and unsupported-field notes;
- lifecycle target limited to RAW or QUARANTINE;
- finite connector outcome and safe reasons.

### Prohibited outputs

This package must not emit:

- canonical person or household records;
- confirmed family relationships;
- public biography or family-tree prose;
- public person-place coordinates;
- DNA matches or DNA-derived relationship claims;
- processed, catalog, triplet, published, proof, release, or rollback authority records;
- credentials, tokens, cookies, private notes, or unminimized account payloads;
- a public-safe flag based only on the package-local descriptor.

[Back to top ↑](#top)

---

## Validation

Executable tests should live under `connectors/familysearch/tests/` and use synthetic fixtures by default.

Minimum validation classes:

1. **Packaging and import safety** — package installs under the supported workflow; imports perform no network, secret reads, client construction, or filesystem writes.
2. **Configuration** — defaults are no-network/no-account; invalid or incomplete live settings fail closed.
3. **Descriptor reconciliation** — canonical source identity, role, rights, sensitivity, and activation state are required and cannot be overridden by a package-local placeholder.
4. **Parser behavior** — valid, empty, partial, malformed, unknown-field, and drift payloads produce deterministic candidate records or finite errors.
5. **Provenance preservation** — source references, citation metadata, contributor/source labels, timestamps, and digests survive parsing and handoff.
6. **Privacy and consent routing** — living-person, private-account, consent-missing, consent-expired, consent-revoked, rights-unclear, retention-expired, and DNA-like cases fail closed.
7. **Handoff boundary** — outputs target RAW or QUARANTINE only and cannot write to later lifecycle or release roots.
8. **Credential safety** — exceptions and logs redact secrets and do not reproduce sensitive payloads.
9. **Network isolation** — default tests fail if an unexpected socket or HTTP request occurs.
10. **Drift handling** — changed source shape produces a reviewable drift outcome, not silent data loss or truth upgrade.

A likely local command is:

```bash
python -m pytest connectors/familysearch/tests
```

That command remains **NEEDS VERIFICATION** until package metadata and executable tests are implemented.

[Back to top ↑](#top)

---

## Implementation sequence

Implement this connector in governed increments:

1. **Reconcile authority records.** Resolve canonical source ID, descriptor home, source role, rights, sensitivity, access posture, and activation workflow.
2. **Repair the scaffold.** Complete `pyproject.toml`, add a side-effect-free import surface, and decide whether `fetch.py` and package-local `descriptor.yaml` remain.
3. **Add deterministic configuration.** Establish explicit no-network/no-account defaults and typed validation.
4. **Build fixture-first parsing.** Parse synthetic payloads without any live source dependency.
5. **Add provenance-preserving handoff models.** Define the accepted RAW/QUARANTINE envelope against repository contracts.
6. **Add privacy and consent routing.** Implement fail-closed connector signals without claiming final policy authority.
7. **Add bounded live access only after approval.** Introduce credential-safe, rate-limited, opt-in client behavior after source and governance review.
8. **Wire tests and CI.** Prove import safety, network isolation, descriptor gates, privacy behavior, deterministic errors, and lifecycle boundaries.
9. **Run activation review.** Do not activate until evidence, test results, rights, sensitivity, retention, consent, rollback, and operational ownership are inspectable.

Each increment should be independently reviewable and reversible.

[Back to top ↑](#top)

---

## Definition of done

The package is ready to claim an initial implemented state only when:

- [ ] A canonical FamilySearch `source_id` and descriptor home are approved and used consistently.
- [ ] Source role, authority, rights, attribution, redistribution, sensitivity floor, access posture, retention, and citation requirements are no longer `TBD`.
- [ ] The package-local `sensitivity_floor: public` placeholder is removed or replaced with an explicitly governed, non-authoritative example.
- [ ] `pyproject.toml` defines a valid build and package-discovery configuration.
- [ ] The package has a narrow, side-effect-free import surface.
- [ ] Importing modules performs no network, account, secret, or write operations.
- [ ] Default configuration disables live access.
- [ ] Parser behavior works entirely from synthetic fixtures.
- [ ] Person and relationship records remain source-attributed candidate assertions.
- [ ] Provenance, citation, retrieval, temporal, and digest metadata are preserved.
- [ ] Living-person, private, consent-unclear, revoked, rights-unclear, retention-expired, and DNA-like cases fail closed.
- [ ] Connector outputs are limited to governed RAW or QUARANTINE handoff.
- [ ] No connector code writes directly to later lifecycle, proof, receipt-authority, or release stores.
- [ ] Errors and logs are finite, actionable, and safe for sensitive data.
- [ ] Executable tests cover packaging, import safety, network isolation, parsing, drift, privacy, descriptor gates, and handoff boundaries.
- [ ] CI runs the no-network test suite successfully.
- [ ] Live behavior, if present, is explicit, opt-in, reviewed, credential-safe, bounded, auditable, and excluded from default tests.
- [ ] Activation, rollback, revocation, cache invalidation, and retention responsibilities have named owners.

Documentation completeness alone does not satisfy this checklist.

[Back to top ↑](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Canonical FamilySearch source ID: `familysearch` or `familysearch-api`. | **BLOCKED** | Accepted registry decision and synchronized references. |
| Canonical descriptor home and package-local descriptor treatment. | **BLOCKED** | Directory/registry decision; package descriptor removed, generated, or marked non-authoritative. |
| Approved source role and authority posture. | **NEEDS REVIEW** | Source steward decision using accepted vocabulary. |
| Rights, attribution, redistribution, retention, and permitted-use posture. | **NEEDS REVIEW** | Current terms review and recorded decision. |
| Sensitivity floor and record-level classification behavior. | **BLOCKED** | Privacy/sensitivity review; removal of unsafe `public` placeholder. |
| Approved access and OAuth model. | **UNKNOWN** | Current source documentation, security review, and implementation plan. |
| Package build, supported Python version, and dependency policy. | **UNIMPLEMENTED** | Completed `pyproject.toml` and install/import tests. |
| Parser, client, privacy, handoff, and error modules. | **UNIMPLEMENTED** | Code and unit tests. |
| RAW/QUARANTINE envelope contract and write interface. | **NEEDS VERIFICATION** | Accepted contracts/schemas and tests. |
| Synthetic fixture inventory and sensitivity review. | **UNIMPLEMENTED** | Fixture files, metadata, and review record. |
| Executable connector tests. | **UNIMPLEMENTED** | Test files and passing local results. |
| CI wiring and no-network enforcement. | **UNKNOWN** | Workflow configuration and passing run. |
| Activation, rollback, revocation, deletion, and cache-invalidation runbooks. | **UNIMPLEMENTED / NEEDS REVIEW** | Governed runbooks and named owners. |

[Back to top ↑](#top)

---

## Maintainer note

Keep this package small, explicit, fixture-first, and reversible. FamilySearch material may be useful evidence, but availability through a source or account does not establish identity, relationship truth, consent, rights clearance, public safety, or publication eligibility. Preserve provenance, surface uncertainty, fail closed, and hand unresolved material to governance rather than smoothing it into a claim.

[Back to top ↑](#top)
