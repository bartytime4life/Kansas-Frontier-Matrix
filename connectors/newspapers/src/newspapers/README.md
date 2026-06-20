<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-newspapers-src-package-readme
title: connectors/newspapers/src/newspapers/ — Newspaper Connector Python Package
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Archives steward · Genealogy steward · People-DNA-Land steward · Settlements steward · Validation steward · Data steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; rights-privacy-sensitivity-gated
proposed_path: connectors/newspapers/src/newspapers/README.md
truth_posture: CONFIRMED path exists / PROPOSED package contract / UNKNOWN implementation depth
related:
  - ../../README.md
  - ../../../README.md
  - ../../tests/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/sources/catalog/loc/README.md
  - ../../../../docs/sources/catalog/README.md
  - ../../../../docs/domains/genealogy/README.md
  - ../../../../docs/domains/people-dna-land/README.md
  - ../../../../docs/domains/settlements/README.md
  - ../../../../data/registry/sources/
  - ../../../../data/raw/
  - ../../../../data/quarantine/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/rights/
  - ../../../../policy/sensitivity/
  - ../../../../release/
tags: [kfm, connectors, newspapers, python-package, archives, chronicling-america, loc, ocr, iiif, genealogy, settlements, privacy, source-admission, raw, quarantine, governance]
notes:
  - "This README documents the connector implementation package boundary, not newspaper source truth, OCR truth, person identity truth, event truth, rights authority, privacy authority, or publication authority."
  - "Package code may prepare source material for RAW or QUARANTINE admission only."
  - "Import behavior, live access, descriptors, endpoint coverage, OCR/page-image parsing, tests, fixtures, CI wiring, rights, privacy, and source terms remain NEEDS VERIFICATION until inspected in the mounted repo."
  - "OCR text and NER/event extraction output are candidate source material only, not authoritative fact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Newspaper Connector Python Package

> Python package boundary for newspaper source-intake helpers inside `connectors/newspapers/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="OCR: candidate only" src="https://img.shields.io/badge/OCR-candidate__only-orange">
  <img alt="Rights: fail closed" src="https://img.shields.io/badge/rights-fail__closed-red">
  <img alt="Privacy: fail closed" src="https://img.shields.io/badge/privacy-fail__closed-red">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/newspapers/src/newspapers/`

## Quick jumps

[Scope](#scope) · [Package boundary](#package-boundary) · [Authority boundary](#authority-boundary) · [Expected modules](#expected-modules) · [Runtime posture](#runtime-posture) · [Inputs and outputs](#inputs-and-outputs) · [OCR and extraction behavior](#ocr-and-extraction-behavior) · [Rights, privacy, and sensitivity behavior](#rights-privacy-and-sensitivity-behavior) · [Errors](#errors) · [Tests](#tests) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/newspapers/src/newspapers/` is the Python implementation package for newspaper connector helpers.

It may contain code that:

- reads connector-local configuration;
- prepares reviewed newspaper source requests only when live access is explicitly allowed;
- parses newspaper-shaped source responses or synthetic fixtures;
- preserves provider, collection, newspaper title, issue, date, page, article, clipping, image, OCR, and retrieval metadata;
- preserves page-image, IIIF, manifest, bounding-box, and digest metadata where available;
- treats OCR text, names, places, dates, events, and article segments as candidate source material;
- normalizes connector output into a bounded source-admission envelope;
- routes rights-unclear, privacy-unclear, OCR-ambiguous, malformed, culturally sensitive, exact-location, or source-drift material toward deny/quarantine/review-required outcomes;
- exposes small, testable functions used by `connectors/newspapers/tests/`.

It must not become newspaper truth, OCR correction authority, named-entity truth, person identity truth, event truth, genealogy truth, settlement truth, source registry authority, schema authority, policy authority, catalog authority, release authority, or publication authority.

> [!IMPORTANT]
> This package is an intake adapter. It does not decide whether newspaper-derived material is true, rights-cleared, privacy-safe, public-safe, culturally appropriate, or publishable. Publication requires downstream validation, EvidenceBundle closure, rights and sensitivity policy, review, release decision, receipts, proofs, correction path, and rollback support.

---

## Package boundary

```text
connectors/
└── newspapers/
    ├── README.md                    # connector-lane overview
    ├── src/
    │   └── newspapers/
    │       ├── README.md            # this file
    │       ├── __init__.py          # PROPOSED / NEEDS VERIFICATION
    │       ├── config.py            # PROPOSED / NEEDS VERIFICATION
    │       ├── client.py            # PROPOSED / NEEDS VERIFICATION
    │       ├── parser.py            # PROPOSED / NEEDS VERIFICATION
    │       ├── ocr.py               # PROPOSED / NEEDS VERIFICATION
    │       ├── iiif.py              # PROPOSED / NEEDS VERIFICATION
    │       ├── extraction.py        # PROPOSED / NEEDS VERIFICATION
    │       ├── sensitivity.py       # PROPOSED / NEEDS VERIFICATION
    │       ├── envelope.py          # PROPOSED / NEEDS VERIFICATION
    │       └── errors.py            # PROPOSED / NEEDS VERIFICATION
    └── tests/
        └── README.md
```

The exact module layout is **PROPOSED**. Use the mounted repo's actual code, package manager, imports, and CI conventions before treating any filename above as implemented.

---

## Authority boundary

```text
THIS PACKAGE MAY:
  parse synthetic, minimized, redacted, public-domain-approved, or steward-approved newspaper-shaped payloads
  prepare reviewed source requests when live access is explicitly enabled
  preserve issue/page/article/clipping/image/OCR metadata
  preserve rights, provider, collection, retrieval, source-role, digest, and parser metadata
  emit connector-local source-admission envelopes
  return finite failure, deny, abstain, quarantine, or needs-verification outcomes
  support RAW or QUARANTINE admission

THIS PACKAGE MUST NOT:
  claim newspaper accounts are true
  silently correct OCR into authoritative transcription
  resolve named entities as truth
  assert person identity, family relationship, event, or place truth
  publish living-person, minor, medical/legal/crime, reputational, tribal, sacred/burial, archaeology, or exact-location material
  write directly to PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, or release stores
  bypass source descriptors, source rights, privacy/sensitivity policy, or review gates
  embed credentials, tokens, cookies, private archive exports, or session material
  treat generated summaries, OCR, or NER/event extraction as evidence by itself
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
| `config.py` | **PROPOSED** | Read connector configuration, feature flags, endpoint keys, timeout defaults, no-network posture, and live-test opt-in flags. |
| `client.py` | **PROPOSED** | Hold bounded newspaper source request behavior; no live call unless explicitly enabled. |
| `parser.py` | **PROPOSED** | Convert newspaper-shaped responses or fixtures into candidate source records without asserting truth. |
| `ocr.py` | **PROPOSED** | Preserve OCR text, OCR quality/confidence markers, and transcription uncertainty without correction authority. |
| `iiif.py` | **PROPOSED** | Preserve page-image, manifest, canvas, sequence, bounding-box, and image-service metadata where applicable. |
| `extraction.py` | **PROPOSED** | Represent names, places, dates, and events as extraction candidates with tool/config/confidence/review metadata. |
| `sensitivity.py` | **PROPOSED** | Detect living-person, minor, medical/legal/crime, reputational, tribal, sacred/burial, archaeology, exact-location, and rights-unclear markers and return safe outcomes. |
| `envelope.py` | **PROPOSED** | Build source-admission envelopes with source metadata, lifecycle target, digests, review flags, and quarantine reasons. |
| `errors.py` | **PROPOSED** | Define finite connector errors safe for logs and steward review. |
| `__init__.py` | **PROPOSED** | Expose a small public import surface; avoid importing live clients or reading secrets at module import time. |

Keep the import surface narrow. Downstream code should receive a governed connector output, not raw archive-session behavior or public UI payloads.

---

## Runtime posture

Default runtime behavior must be safe without special environment setup.

| Concern | Required posture |
|---|---|
| Network access | Disabled or mock-only by default in tests and local dry runs. |
| Archive access | Disabled by default; no private archive account required for default tests. |
| Credentials | Never required for import, parsing fixtures, or no-network tests. |
| Secrets | Never committed and never printed in exceptions. |
| Source descriptors | Required before live source activation. |
| Rights/citation | Unknown copyright, reuse, citation, or platform terms fail closed. |
| OCR uncertainty | Preserved as uncertainty, not silently corrected. |
| Living-person material | Denied, restricted, or quarantine/review-required by default. |
| Sensitive locations/content | Tribal, sacred/burial, archaeology, and exact-location material fails closed. |
| Writes | No direct writes outside allowed RAW or QUARANTINE handoff paths. |
| Publication | Not allowed from this package. |

Optional live behavior should require explicit opt-in, for example a repo-approved equivalent of:

```bash
KFM_ALLOW_LIVE_NEWSPAPER_TESTS=1
```

The exact flag name is **NEEDS VERIFICATION** against repo convention.

---

## Inputs and outputs

### Inputs

Expected input classes:

- source descriptor reference;
- connector configuration;
- newspaper endpoint, collection, issue, page, article, clipping, manifest, or image identifier approved by source steward;
- request parameters allowed by source policy;
- synthetic local fixture payload for tests;
- optional live response body only when source-steward, rights, privacy, sensitivity, and security approvals exist.

### Outputs

Expected output classes:

- parsed candidate newspaper source record;
- OCR text bundle marked as raw OCR / uncertain transcription;
- page-image or IIIF metadata bundle;
- extraction-candidate bundle for names, places, dates, events, article segments, or clipping references;
- source-admission envelope;
- rights/privacy/sensitivity gate result;
- finite error outcome;
- quarantine-safe drift signal;
- metadata bundle containing retrieval time, source label, endpoint key or source reference, digest, parser version, fixture/live status, and review flags where applicable.

Outputs should be shaped for downstream governance. They should not be shaped as direct UI payloads, public claims, authoritative transcriptions, or truth assertions.

---

## OCR and extraction behavior

This package must keep source text and interpretation separate.

Minimum behavior:

1. Raw OCR must remain distinguishable from corrected transcription.
2. OCR confidence, quality, source engine/version, or uncertainty fields should be preserved where available.
3. Article/clipping segmentation must preserve source identifiers and page context.
4. Extracted names, places, dates, and events must remain candidates until downstream evidence resolution.
5. Model-assisted extraction must preserve tool/model/config/prompt lineage where applicable.
6. Conflicting newspaper accounts must remain separate source records unless downstream review resolves them.
7. Long excerpts must not be emitted as public-ready content without rights review.

---

## Rights, privacy, and sensitivity behavior

This package must make risky cases visible instead of smoothing them over.

Minimum behavior:

1. Unknown copyright, license, citation, provider, collection, or platform terms must produce review-required outcomes.
2. Living-person indicators must produce deny/quarantine/review-required outcomes.
3. Minors, medical/legal/crime, reputational, and family-sensitive material must fail closed.
4. Tribal, sacred/burial, archaeology, and culturally sensitive material must fail closed.
5. Exact-location references that could expose sensitive people, sites, or resources must route to redaction/generalization review.
6. Private archive credentials, cookies, tokens, session files, and account exports must never be committed, logged, or embedded in fixtures.
7. Public-source availability does not automatically mean public-release eligibility.

---

## Errors

Connector errors should be finite, reviewable, and safe to log.

Recommended error categories:

| Error | Meaning |
|---|---|
| `MissingSourceDescriptor` | Source activation attempted without an approved descriptor. |
| `LiveAccessDisabled` | Live source request attempted without explicit opt-in. |
| `RightsReviewRequired` | Rights, citation, reuse, platform terms, or provider constraints are missing or unclear. |
| `PrivacyReviewRequired` | Living-person, minor, medical/legal/crime, reputational, or family-sensitive markers are present or unclear. |
| `SensitivityReviewRequired` | Tribal, sacred/burial, archaeology, cultural, or exact-location risks are present or unclear. |
| `MalformedSourcePayload` | Payload shape is incomplete, ambiguous, or not parseable under current parser rules. |
| `OcrUncertaintyRequired` | OCR was supplied without uncertainty metadata where the parser requires it. |
| `AdmissionEnvelopeError` | Candidate output cannot be bounded to RAW or QUARANTINE admission. |

Do not include secrets, private archive URLs with tokens, cookies, full copyrighted OCR dumps, or sensitive living-person details in error messages.

---

## Tests

Package code should be covered by connector-local tests under:

```text
connectors/newspapers/tests/
```

Expected test coverage:

- import safety;
- no-network defaults;
- no-secret defaults;
- descriptor gate behavior;
- rights/citation/reuse gate behavior;
- OCR uncertainty preservation;
- page-image / IIIF metadata preservation;
- provider, collection, issue, page, article, clipping, retrieval, and digest provenance;
- extraction-candidate metadata and abstention/review state;
- privacy and sensitivity fail-closed behavior;
- malformed payload handling;
- RAW or QUARANTINE envelope targeting;
- refusal to write processed/catalog/triplet/published/proof/receipt/release/API/UI outputs.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual modules are inventoried and this README is updated from `PROPOSED` layout to implementation-aware layout.
- [ ] Importing `newspapers` performs no network, secret, archive-cache, or filesystem side effects beyond safe package import.
- [ ] Source descriptors and activation decisions are required before live access.
- [ ] Rights, citation, reuse, platform terms, privacy, and sensitivity gates fail closed.
- [ ] OCR text remains uncertain source material unless downstream correction records exist.
- [ ] Issue/page/article/clipping/image/provenance metadata survives parsing.
- [ ] Extraction candidates preserve tool/config/confidence/review metadata and remain non-authoritative.
- [ ] Output is limited to RAW or QUARANTINE admission envelopes.
- [ ] Tests cover DENY, ABSTAIN, ERROR, and quarantine paths, not only happy paths.
- [ ] CI behavior is verified or marked `NEEDS VERIFICATION`.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual Python package files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm package manager and import path. | **NEEDS VERIFICATION** | `pyproject.toml`, workspace config, Makefile, or CI workflow. |
| Confirm source descriptor IDs and activation state. | **NEEDS VERIFICATION** | `data/registry/sources/` entries and accepted source schema. |
| Confirm newspaper source surfaces covered by this package. | **NEEDS VERIFICATION** | Source-catalog entries, ADR, connector inventory, and tests. |
| Confirm rights, privacy, and sensitivity gate implementation. | **NEEDS VERIFICATION** | Policy docs, parser code, tests, and steward review. |
| Confirm OCR/page-image/IIIF parser behavior. | **NEEDS VERIFICATION** | Parser code, fixtures, and test logs. |
| Confirm CI wiring. | **NEEDS VERIFICATION** | Workflow files and current CI logs. |

---

## Maintainer note

This package is a governed source-admission adapter. Keep the implementation small, import-safe, fixture-testable, and conservative. If a change makes claims true, publishes records, resolves people, corrects OCR authoritatively, chooses release posture, or bypasses rights/privacy/sensitivity review, it belongs outside this package or behind downstream governance.

<p align="right"><a href="#top">Back to top</a></p>
