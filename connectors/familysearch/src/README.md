<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-familysearch-src-readme
title: connectors/familysearch/src/ — FamilySearch Connector Source Root
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · People/DNA/Land steward · Sensitivity reviewer · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine
proposed_path: connectors/familysearch/src/README.md
truth_posture: CONFIRMED path exists / PROPOSED source-root contract / UNKNOWN implementation depth
related:
  - ../README.md
  - familysearch/README.md
  - ../tests/README.md
  - ../../../docs/sources/catalog/familysearch/README.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../data/registry/sources/people-genealogy-dna-land/
  - ../../../data/raw/people-dna-land/
  - ../../../data/quarantine/people-dna-land/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/genealogy/publication.rego
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, familysearch, source-root, python, genealogy, people-dna-land, consent, living-person, source-admission, raw, quarantine, governance]
notes:
  - "This README documents the connector source-code root, not FamilySearch source truth, person truth, relationship truth, consent authority, or publication authority."
  - "The implementation package below this root may prepare source material for RAW or QUARANTINE admission only."
  - "Concrete package metadata, modules, imports, source descriptors, OAuth behavior, endpoint coverage, tests, fixtures, and CI wiring remain NEEDS VERIFICATION until inspected in the mounted repo."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FamilySearch Connector Source Root

> Source-code root for the FamilySearch connector implementation under `connectors/familysearch/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: connector source root" src="https://img.shields.io/badge/scope-connector__source__root-blue">
  <img alt="Sensitivity: living-person deny by default" src="https://img.shields.io/badge/sensitivity-living__person__deny__by__default-critical">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/familysearch/src/`

## Quick jumps

[Scope](#scope) · [Repository fit](#repository-fit) · [Authority boundary](#authority-boundary) · [Expected contents](#expected-contents) · [Import and packaging posture](#import-and-packaging-posture) · [Lifecycle handoff](#lifecycle-handoff) · [Privacy posture](#privacy-posture) · [Testing relationship](#testing-relationship) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/familysearch/src/` is the implementation source root for the FamilySearch connector lane.

This folder may contain importable connector code that supports FamilySearch source intake, parsing, privacy gating, normalization into source-admission envelopes, and safe handoff toward RAW or QUARANTINE lifecycle states.

It must not contain:

- FamilySearch source truth;
- person identity authority;
- relationship truth;
- DNA truth;
- land-title truth;
- consent authority;
- source registry authority;
- policy authority;
- schema authority;
- processed domain records;
- published records;
- release decisions;
- proof packs;
- credentials, OAuth tokens, cookies, or session exports;
- private account exports;
- UI-facing claim text.

> [!IMPORTANT]
> This root is for connector implementation code. It does not replace `connectors/familysearch/README.md`, `connectors/familysearch/tests/README.md`, source catalog documentation, source descriptors, contracts, schemas, privacy/consent policy, release records, or downstream pipeline documentation.

---

## Repository fit

```text
connectors/
└── familysearch/
    ├── README.md                  # connector-lane overview
    ├── src/
    │   ├── README.md              # this file
    │   └── familysearch/
    │       └── README.md          # implementation-package boundary
    └── tests/
        └── README.md              # connector-local tests
```

Related responsibility roots:

```text
connectors/                                      # source-specific fetch and admission code
docs/sources/catalog/familysearch/               # FamilySearch source-family briefing
docs/domains/people-dna-land/                    # People/Genealogy/DNA/Land doctrine
data/registry/sources/people-genealogy-dna-land/ # source descriptors and activation state
data/raw/people-dna-land/                        # raw staged source outputs, if admitted
data/quarantine/people-dna-land/                 # held material requiring review
fixtures/                                        # shared test fixtures, when promoted out of connector-local scope
schemas/contracts/v1/source/                     # source/admission schemas, subject to ADR/schema-home convention
policy/genealogy/                                # genealogy-specific publication policy, if present
policy/sensitivity/                              # sensitivity and release policy
release/                                         # release decisions, rollback, and correction state
```

Path names involving `people-dna-land` versus `people-genealogy-dna-land` may be affected by domain-segment naming decisions. Verify against accepted Directory Rules and ADRs before adding new sibling paths.

---

## Authority boundary

```text
THIS SOURCE ROOT MAY CONTAIN:
  connector implementation code
  parser helpers
  privacy-gate helpers
  bounded client helpers
  envelope builders
  connector-local error classes
  small package-local constants
  package README files

THIS SOURCE ROOT MUST NOT CONTAIN:
  source descriptors as authority records
  consent decisions as authority records
  policy decisions
  schemas as authority records
  release manifests
  publication outputs
  raw private source dumps
  credentials, tokens, cookies, or private session material
  generated truth claims
```

The FamilySearch connector source root participates at the source-admission edge only:

```text
FamilySearch source material
  -> connectors/familysearch/src/
  -> data/raw/ or data/quarantine/
  -> downstream governed processing, validation, evidence closure, consent, policy, review, release
```

It must not short-circuit the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

---

## Expected contents

The exact implementation inventory is **NEEDS VERIFICATION**. A minimal source-root structure may look like this:

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
    ├── envelope.py
    └── errors.py
```

Recommended separation:

| Area | Responsibility |
|---|---|
| `familysearch/config.py` | Configuration parsing, feature flags, no-network/no-account defaults, endpoint keys. |
| `familysearch/client.py` | Bounded request helpers; no live access unless explicitly enabled and reviewed. |
| `familysearch/parser.py` | Payload parsing from synthetic fixtures or steward-approved responses without asserting truth. |
| `familysearch/privacy.py` | Living-person, consent, revocation, private-account, and DNA-like field gate helpers. |
| `familysearch/envelope.py` | Source-admission envelope construction with metadata, source references, lifecycle target, and digest support. |
| `familysearch/errors.py` | Finite connector errors safe for logs and review. |
| `familysearch/__init__.py` | Small import surface that does not trigger network, account, or secret behavior. |

Avoid adding shared utilities here until more than one connector needs them. Shared connector patterns should move to a governed shared package or tool home after review.

---

## Import and packaging posture

Expected posture:

- importing the package should not make network calls;
- importing the package should not require a FamilySearch account;
- importing the package should not read OAuth tokens, cookies, or session exports;
- package-level code should avoid reading live environment secrets at import time;
- optional live behavior should be invoked explicitly;
- parser and privacy-gate functions should operate on supplied payloads or fixtures;
- connector outputs should be deterministic for the same input payload and connector configuration;
- source descriptors, schema validation, consent checks, and policy checks should remain explicit dependencies, not hidden side effects.

Likely import shape, subject to repo verification:

```python
from familysearch.parser import parse_payload
from familysearch.privacy import evaluate_privacy_gate
from familysearch.envelope import build_source_admission_envelope
```

Do not treat this example as implementation proof until the mounted repo confirms module names and packaging configuration.

---

## Lifecycle handoff

Connector source code may prepare data for lifecycle handoff, but it does not own later lifecycle phases.

| Phase | Connector source-root role |
|---|---|
| Pre-RAW / source contact | May prepare bounded source requests only when source, security, and privacy gates allow it. |
| RAW | May write or prepare raw-admission payloads only if the repo’s intake convention allows it. |
| QUARANTINE | May route private, rights-unclear, consent-unclear, malformed, or sensitive material to quarantine-safe output. |
| WORK / PROCESSED | Out of scope unless a downstream governed pipeline imports connector helpers explicitly. |
| CATALOG / TRIPLET | Out of scope. |
| PUBLISHED | Out of scope. |
| RELEASE / ROLLBACK | Out of scope. |

When in doubt, route uncertain material toward quarantine, deny, or explicit abstention rather than guessing.

---

## Privacy posture

FamilySearch source material may involve living people, private family relationships, account-mediated data, contributor notes, private tree material, or person-place assertions.

Minimum implementation posture:

- living-person material is denied or quarantine/review-required by default;
- missing, expired, revoked, or ambiguous consent is not treated as consent;
- private account-only material is not public-safe by default;
- relationship assertions remain candidate assertions until downstream evidence and review support them;
- person-place assertions involving living people fail closed;
- raw DNA or DNA-derived hints are out of scope unless a separate approved quarantine-only policy exists;
- cache, retention, revocation, and tombstone behavior must be explicit before live activation.

---

## Testing relationship

Connector-local tests live outside this source root:

```text
connectors/familysearch/tests/
```

The source root should be easy to test with synthetic, no-network fixtures:

- import tests should prove no network, no account, and no secret read at import time;
- parser tests should pass with static synthetic payloads;
- client tests should mock all HTTP and OAuth behavior by default;
- privacy-gate tests should cover living-person, consent-missing, revoked, private, rights-unclear, and DNA-like cases;
- envelope tests should check metadata, source references, lifecycle target, review flags, and digest fields;
- live smoke tests, if any, should be opt-in and isolated from default CI.

Likely local command, subject to repo verification:

```bash
python -m pytest connectors/familysearch/tests
```

---

## Definition of done

This source root is ready for first review when:

- [ ] `connectors/familysearch/src/README.md` explains the source-root boundary.
- [ ] `connectors/familysearch/src/familysearch/README.md` explains the package boundary.
- [ ] Importing package modules does not perform network I/O.
- [ ] Importing package modules does not require account access, OAuth tokens, cookies, or session exports.
- [ ] No credentials or private endpoint material are committed.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] Parser and privacy behavior are fixture-testable without live FamilySearch calls.
- [ ] Living-person, consent-unclear, revoked, private, and rights-unclear cases fail closed.
- [ ] Errors are finite, actionable, and safe to log.
- [ ] Live source activation requires source descriptor, source steward review, security review, and privacy/consent review.
- [ ] The connector does not write directly to processed, catalog, triplet, published, proof, receipt, or release stores.
- [ ] Test and CI wiring is documented once verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual files below `connectors/familysearch/src/`. | **NEEDS VERIFICATION** | Mounted repo tree or GitHub file listing. |
| Confirm whether `src/` is packaged by `pyproject.toml`, workspace config, or connector-specific metadata. | **NEEDS VERIFICATION** | Packaging files and CI. |
| Confirm package import name is `familysearch`. | **NEEDS VERIFICATION** | Python package metadata and import tests. |
| Confirm shared connector helper home, if any. | **NEEDS VERIFICATION** | Repo tree and ADRs. |
| Confirm source-admission envelope schema. | **NEEDS VERIFICATION** | Contracts and schemas under the accepted schema home. |
| Confirm source descriptor location and FamilySearch source-family coverage. | **NEEDS VERIFICATION** | Source registry and source catalog docs. |
| Confirm consent, revocation, retention, tombstone, and cache invalidation policy. | **NEEDS VERIFICATION** | Policy docs and review decisions. |
| Confirm default no-network/no-account test behavior. | **NEEDS VERIFICATION** | Test config and CI workflows. |
| Confirm People/DNA/Land path segment convention. | **NEEDS VERIFICATION** | Directory Rules, ADRs, and current repo paths. |

---

## Maintainer note

Keep `connectors/familysearch/src/` boring, narrow, and privacy-forward. It should make FamilySearch source material easier to parse, inspect, quarantine, and review. It should not become a hidden pipeline, a source registry, a consent authority, a policy engine, or a publication path.
