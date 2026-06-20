<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-newspapers-tests-readme
title: connectors/newspapers/tests/ — Newspaper Connector Tests
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Archives steward · Genealogy steward · People-DNA-Land steward · Settlements steward · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; rights-privacy-sensitivity-gated; no-live-by-default
proposed_path: connectors/newspapers/tests/README.md
truth_posture: CONFIRMED path exists / PROPOSED local test contract / UNKNOWN implementation depth
related:
  - ../README.md
  - ../../../connectors/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/loc/README.md
  - ../../../docs/sources/catalog/README.md
  - ../../../docs/domains/genealogy/README.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/domains/settlements/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, newspapers, tests, archives, chronicling-america, loc, ocr, iiif, genealogy, settlements, privacy, fixtures, source-admission, raw, quarantine, governance]
notes:
  - "This README replaces a greenfield stub with connector-local test guidance for the newspaper connector lane."
  - "Tests must be no-network by default and must not require live credentials, live downloads, private newspaper archives, or source-side side effects."
  - "Use synthetic, minimized, redacted, or explicitly approved fixtures only."
  - "Tests may verify connector safety and admission envelopes; they do not prove newspaper truth, OCR truth, person identity, event truth, publication eligibility, or release readiness."
  - "Living-person privacy, copyright, cultural sensitivity, archaeology, sacred/burial, and exact-location risks must fail closed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Newspaper Connector Tests

> Connector-local test guidance for `connectors/newspapers/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Scope: connector tests" src="https://img.shields.io/badge/scope-connector__tests-blue">
  <img alt="Network: off by default" src="https://img.shields.io/badge/network-off__by__default-critical">
  <img alt="Fixtures: synthetic preferred" src="https://img.shields.io/badge/fixtures-synthetic__preferred-orange">
  <img alt="Rights: fail closed" src="https://img.shields.io/badge/rights-fail__closed-red">
  <img alt="Privacy: fail closed" src="https://img.shields.io/badge/privacy-fail__closed-red">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/newspapers/tests/`

## Scope

This folder is for connector-local tests for the proposed newspaper source-admission connector.

Tests may verify:

- import safety;
- no-network defaults;
- missing-source-descriptor behavior;
- rights, license, citation, and reuse guardrails;
- provider, collection, issue, page, article, clipping, and image/OCR provenance handling;
- OCR uncertainty preservation;
- IIIF/page-image metadata preservation where applicable;
- malformed, incomplete, or ambiguous newspaper-shaped payload handling;
- living-person, minors, medical/legal/crime, reputational, cultural, sacred/burial, archaeology, tribal, and exact-location safety gates;
- RAW or QUARANTINE handoff envelopes;
- refusal to create public claims, graph truth, release artifacts, or publication outputs.

Tests must not become newspaper truth, OCR truth, corrected transcription authority, named-entity authority, person identity truth, event truth, source descriptor authority, policy authority, release authority, or publication authority.

---

## Test boundaries

Default test behavior:

```text
network: disabled
credentials: not required
live downloads: not required
private archives: not required
fixtures: synthetic, minimized, redacted, or explicitly approved
writes: no processed/catalog/triplet/published/proof/receipt/release writes
outputs: local assertions only
```

Optional live smoke tests, if they ever exist, must be isolated, steward-approved, skipped by default, and documented in a separate live-test section or file. They must not run in ordinary CI without an explicit opt-in environment variable and source-steward approval.

---

## Expected test classes

| Test class | Purpose |
|---|---|
| Import safety | Importing modules must not call the network, read live secrets, or touch local archive caches. |
| Configuration | Defaults must be no-network and source activation must be explicit. |
| Descriptor gate | Missing `SourceDescriptor` must block live activation. |
| Rights gate | Unknown copyright, reuse, citation, or platform terms must route to review-required behavior. |
| Privacy gate | Living-person, minors, medical/legal/crime, and reputationally sensitive material must fail closed. |
| Cultural/sensitive-location gate | Tribal, sacred/burial, archaeology, and exact-location risks must quarantine or restrict. |
| Provenance gate | Provider, collection, newspaper title, issue, date, page, article/clipping identity, retrieval, and source-role metadata must be preserved. |
| OCR gate | OCR text must remain source text with uncertainty; tests must reject silent promotion to corrected fact. |
| IIIF/image gate | Page-image, manifest, sequence, bounding-box, and digest metadata must survive parsing where applicable. |
| Extraction-candidate gate | NER/event candidates must carry tool/model/config metadata, confidence, and abstention/review state. |
| Admission envelope | Connector output must target RAW or QUARANTINE only. |
| Error handling | Malformed, incomplete, ambiguous, or rights-unclear payloads must produce finite outcomes. |
| Release blocking | Tests must prove connector code cannot directly publish, write release outputs, or create public claims. |

---

## Fixture rules

Use synthetic fixtures whenever possible.

Fixture requirements:

1. Do not commit live credentials, private archive exports, tokens, cookies, session state, copyrighted bulk text, or platform-restricted downloads unless explicitly approved by a steward.
2. Keep fixtures minimal and purpose-specific.
3. Mark fixture status clearly: synthetic, redacted, minimized, public-domain-approved, or steward-approved.
4. Include rights, citation, provider, collection, issue/page/article identity, retrieval, source-role, and OCR-quality metadata when the test path requires it.
5. Include negative fixtures for missing descriptor, missing rights, missing citation, unclear provider, malformed OCR, ambiguous date, missing page identity, living-person risk, minor risk, cultural sensitivity risk, exact-location risk, and restricted-record cases.
6. Avoid large page images or bulk OCR dumps in connector-local tests; use minimized fixture slices and digest expectations instead.
7. Promote shared fixtures to the repo fixture authority only after review.

Example fixture metadata:

```yaml
fixture_id: newspapers-synthetic-admission-001
fixture_status: synthetic
source_family: newspapers
source_surface: loc-chronam-candidate
source_role: candidate
supports_tests:
  - descriptor_gate
  - rights_gate
  - ocr_gate
  - privacy_gate
  - admission_envelope
rights_posture: test-only
privacy_posture: synthetic-no-real-person-claim
review_state: draft
```

---

## Expected assertions

Tests should prefer small, explicit assertions over broad integration claims.

| Assertion area | Required proof |
|---|---|
| No-network default | Test run succeeds with live-network blockers active. |
| No-secret default | Missing credentials produce a finite skipped/blocked outcome, not a crash or secret read. |
| Source descriptor | Activation requires a descriptor or source-activation decision fixture. |
| Raw/quarantine envelope | Output path and envelope target only raw or quarantine candidate locations. |
| Rights handling | Unknown or restricted rights never produce public-ready output. |
| OCR uncertainty | OCR text remains marked as raw OCR or uncertain transcription. |
| Provenance | Issue/page/article identifiers, provider, collection, retrieval time, and digest survive parsing. |
| Candidate extraction | Names, places, dates, and events are candidates, not claims. |
| Sensitive material | Privacy/sensitivity fixtures trigger quarantine, restriction, redaction, generalization, or denial. |
| Release blocking | No test path writes published, catalog, triplet, proof, receipt, release, API, or UI artifacts. |

---

## Running tests

The exact command is **NEEDS VERIFICATION** against the repo's package manager and CI configuration.

Likely local command:

```bash
python -m pytest connectors/newspapers/tests
```

Likely no-network command:

```bash
KFM_ALLOW_LIVE_NEWSPAPER_TESTS=0 python -m pytest connectors/newspapers/tests
```

Optional live-test command, only if later approved:

```bash
KFM_ALLOW_LIVE_NEWSPAPER_TESTS=1 python -m pytest connectors/newspapers/tests/live
```

Use the repo-standard runner if Makefile, `uv`, Poetry, tox, nox, or CI conventions say otherwise.

---

## Acceptance checklist

- [ ] Default tests do not access the network.
- [ ] Tests do not require live credentials, private archives, live downloads, cookies, or session state.
- [ ] Fixtures are synthetic, minimized, redacted, public-domain-approved, or explicitly steward-approved.
- [ ] SourceDescriptor is required before source activation.
- [ ] Rights, license, citation, platform terms, and reuse uncertainty fail closed.
- [ ] Provider, collection, issue, date, page, article/clipping, retrieval, and digest provenance are preserved.
- [ ] OCR uncertainty is preserved and never silently promoted to fact.
- [ ] NER/event extraction outputs remain candidates with tool/config/confidence/review metadata.
- [ ] Living-person, minors, medical/legal/crime, reputational, tribal, sacred/burial, archaeology, and exact-location risks fail closed.
- [ ] Connector output is limited to RAW or QUARANTINE handoff candidates.
- [ ] Tests do not write to processed, catalog, triplet, published, proof, receipt, release, API, or UI stores.
- [ ] Tests do not produce public claims.
- [ ] CI wiring is documented once verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual test files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm test runner and package manager. | **NEEDS VERIFICATION** | Makefile, pyproject, CI workflow, tox, nox, or equivalent. |
| Confirm fixture authority. | **NEEDS VERIFICATION** | Root fixture docs and validation review. |
| Confirm source descriptor and source IDs. | **NEEDS VERIFICATION** | Source registry entries and accepted schema. |
| Confirm newspaper source surfaces to test. | **NEEDS VERIFICATION** | Source-catalog entries, ADR, and connector inventory. |
| Confirm OCR/page-image metadata assertions. | **NEEDS VERIFICATION** | Parser tests and source descriptor. |
| Confirm privacy/sensitivity fixture expectations. | **NEEDS VERIFICATION** | Policy docs, redaction profile, and steward review. |
| Confirm live-test policy, if any. | **NEEDS VERIFICATION** | Source steward and CI policy. |
| Confirm CI wiring. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

This test lane is a guardrail for connector behavior, not proof that newspaper-derived claims are true or publishable. Passing connector tests means only that the tested code respects admission boundaries, provenance capture, rights/privacy/sensitivity gates, and no-network safety under the tested fixture conditions.

<p align="right"><a href="#top">Back to top</a></p>
