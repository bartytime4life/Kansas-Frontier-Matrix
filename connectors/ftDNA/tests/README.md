<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ftdna-tests-readme
title: connectors/ftDNA/tests/ — FamilyTreeDNA Connector Tests
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · People/DNA/Land steward · Consent steward · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: restricted-doctrine; consent-required; no-live-by-default
proposed_path: connectors/ftDNA/tests/README.md
truth_posture: CONFIRMED path exists / PROPOSED local test contract / UNKNOWN implementation depth
related:
  - ../README.md
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
tags: [kfm, connectors, ftdna, tests, familytreedna, people-dna-land, consent, source-admission, fixtures, raw, quarantine, governance]
notes:
  - "This README replaces a greenfield stub with connector-local test guidance for the ftDNA lane."
  - "Tests must be no-network by default and must not require live credentials, live accounts, or private source exports."
  - "Use synthetic, minimized, or explicitly approved fixtures only."
  - "Tests may verify connector safety and admission envelopes; they do not prove identity, kinship, interpretation, publication eligibility, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FamilyTreeDNA Connector Tests

> Connector-local test guidance for `connectors/ftDNA/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Scope: connector tests" src="https://img.shields.io/badge/scope-connector__tests-blue">
  <img alt="Network: off by default" src="https://img.shields.io/badge/network-off__by__default-critical">
  <img alt="Fixtures: synthetic preferred" src="https://img.shields.io/badge/fixtures-synthetic__preferred-orange">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/ftDNA/tests/`

## Scope

This folder is for connector-local tests for the proposed ftDNA / FamilyTreeDNA source-admission connector.

Tests may verify:

- import safety;
- no-network defaults;
- missing-source-descriptor behavior;
- consent-sidecar requirements;
- revocation and cleanup signals;
- rights and terms guardrails;
- malformed or incomplete source-shaped payload handling;
- RAW or QUARANTINE handoff envelopes;
- refusal to create public claims, graph truth, release artifacts, or publication outputs.

Tests must not become identity truth, kinship truth, DNA interpretation truth, consent authority, source descriptor authority, policy authority, release authority, or publication authority.

---

## Test boundaries

Default test behavior:

```text
network: disabled
credentials: not required
live accounts: not required
fixtures: synthetic, minimized, or explicitly approved
writes: no processed/catalog/triplet/published/proof/receipt/release writes
outputs: local assertions only
```

Optional live smoke tests, if they ever exist, must be isolated, steward-approved, skipped by default, and documented in a separate live-test section or file.

---

## Expected test classes

| Test class | Purpose |
|---|---|
| Import safety | Importing modules must not call the network or read live secrets. |
| Configuration | Defaults must be no-network and source-activation must be explicit. |
| Descriptor gate | Missing SourceDescriptor must block live activation. |
| Consent gate | Missing, expired, revoked, or unclear consent state must fail closed. |
| Rights gate | Unknown terms or unclear permitted use must route to review-required behavior. |
| Parser behavior | Source-shaped test payloads must preserve metadata and uncertainty fields. |
| Admission envelope | Connector output must target RAW or QUARANTINE only. |
| Error handling | Malformed, incomplete, or ambiguous payloads must produce finite outcomes. |
| Release blocking | Tests must prove connector code cannot directly publish or create release outputs. |

---

## Fixture rules

Use synthetic fixtures whenever possible.

Fixture requirements:

1. Do not commit private exports, live identifiers, live account material, credentials, tokens, cookies, or session state.
2. Keep fixtures minimal and purpose-specific.
3. Mark fixture status clearly: synthetic, redacted, minimized, or approved.
4. Include consent and rights metadata when the test path requires it.
5. Include negative fixtures for missing descriptor, missing consent, revoked consent, rights unclear, malformed payload, and identity-unclear cases.
6. Promote shared fixtures to the repo fixture authority only after review.

Example fixture metadata:

```yaml
fixture_id: ftdna-synthetic-admission-001
fixture_status: synthetic
source_family: ftdna
source_role: candidate
supports_tests:
  - descriptor_gate
  - consent_gate
  - admission_envelope
rights_posture: test-only
consent_posture: synthetic-sidecar
review_state: draft
```

---

## Running tests

The exact command is **NEEDS VERIFICATION** against the repo’s package manager and CI configuration.

Likely local command:

```bash
python -m pytest connectors/ftDNA/tests
```

Likely no-network command:

```bash
KFM_ALLOW_LIVE_FTDNA_TESTS=0 python -m pytest connectors/ftDNA/tests
```

Optional live-test command, only if later approved:

```bash
KFM_ALLOW_LIVE_FTDNA_TESTS=1 python -m pytest connectors/ftDNA/tests/live
```

Use the repo-standard runner if Makefile, `uv`, Poetry, tox, nox, or CI conventions say otherwise.

---

## Acceptance checklist

- [ ] Default tests do not access the network.
- [ ] Tests do not require live credentials or live accounts.
- [ ] Fixtures are synthetic, minimized, redacted, or explicitly approved.
- [ ] SourceDescriptor is required before source activation.
- [ ] Consent-sidecar behavior is checked where required.
- [ ] Revocation behavior is checked where applicable.
- [ ] Rights and terms uncertainty fails closed.
- [ ] Connector output is limited to RAW or QUARANTINE handoff candidates.
- [ ] Tests do not write to processed, catalog, triplet, published, proof, receipt, or release stores.
- [ ] Tests do not produce public claims.
- [ ] CI wiring is documented once verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual test files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm test runner and package manager. | **NEEDS VERIFICATION** | Makefile, pyproject, CI workflow, tox, nox, or equivalent. |
| Confirm fixture authority. | **NEEDS VERIFICATION** | Root fixture docs and validation review. |
| Confirm source descriptor and source ID. | **NEEDS VERIFICATION** | Source registry entry and accepted schema. |
| Confirm consent-sidecar schema and policy. | **NEEDS VERIFICATION** | Consent schema and policy docs. |
| Confirm live-test policy, if any. | **NEEDS VERIFICATION** | Source steward and CI policy. |
| Confirm CI wiring. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

These tests should prove restraint. A passing suite should show that the ftDNA connector can be imported, configured, and exercised with safe fixtures while refusing to bypass source descriptors, consent, rights review, lifecycle gates, or release controls.
