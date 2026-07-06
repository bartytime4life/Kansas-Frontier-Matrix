<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-people-dna-land-dna-no-log-readme
title: People DNA Land DNA No-Log Tests README
type: test-lane-readme
version: v0.1
status: draft; directory-created-in-scratch; dna-no-log-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - People DNA Land domain steward
  - OWNER_TBD - DNA privacy steward
  - OWNER_TBD - Consent steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Security steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - QA steward
created: 2026-07-05
updated: 2026-07-05
policy_label: public-doc; tests; people-dna-land; dna; no-log; living-person-sensitive; dna-sensitive; privacy; security; no-network; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, people-dna-land, dna, no-log, privacy, security, living-person, genealogy, consent, EvidenceBundle, PolicyDecision, ConsentRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../../README.md
  - ../../../README.md
  - ../../README.md
  - ../README.md
  - ../../consent/README.md
  - ../../contracts/README.md
  - ../../connectors/README.md
  - ../../assessor_as_title_denial_test/README.md
  - ../../chain_of_title_gap_test/README.md
  - ../../../../../docs/domains/people-dna-land/
  - ../../../../../contracts/domains/people-dna-land/
  - ../../../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../../../policy/domains/people-dna-land/
  - ../../../../../fixtures/domains/people-dna-land/dna/no-log/
  - ../../../../../data/registry/sources/people-dna-land/
  - ../../../../../release/manifests/people-dna-land/
notes:
  - "This README replaces the placeholder content at tests/domains/people-dna-land/dna/no-log/README.md."
  - "The parent file at tests/domains/people-dna-land/dna/README.md was observed as placeholder content in GitHub when this README was authored; parent-lane details remain NEEDS VERIFICATION."
  - "Directory Rules place enforceability proof under tests/ and identify people-dna-land as a domain lane pattern."
  - "This is a DNA no-log test lane only. It does not define logging policy, runtime logging implementation, DNA contracts, schemas, source descriptors, EvidenceBundles, consent records, release decisions, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that logs, traces, diagnostics, AI prompts, receipts, and error surfaces may carry public-safe references and finite outcomes, but not raw DNA, genomic, living-person, consent, source-payload, secret, or unrestricted evidence payloads."
  - "Default posture is deterministic and no-network. Real people records, DNA data, genealogy provider exports, consent records, source exports, credentials, runtime telemetry, production logs, and public release artifacts do not belong in default no-log tests."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People DNA Land DNA no-log tests

> Test lane for deterministic, no-network proof that DNA-sensitive and living-person payloads do not leak into logs, traces, diagnostics, AI prompts, receipts, error messages, or public/debug surfaces.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-blue">
  <img alt="Lane: dna no-log" src="https://img.shields.io/badge/lane-dna__no--log-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: logs not evidence" src="https://img.shields.io/badge/boundary-logs__not__evidence-success">
</p>

**Path:** `tests/domains/people-dna-land/dna/no-log/README.md`  
**Status:** draft / directory-created-in-scratch / DNA no-log test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `people-dna-land`  
**Test lane family:** `dna/no-log`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED by Directory Rules that `tests/` is the canonical root for enforceability proof and that `people-dna-land` is a domain lane pattern; CONFIRMED by attached implementation doctrine that logs may include request IDs, policy decisions, adapter metadata, citation report IDs, and receipt IDs while excluding secrets, private reasoning, raw sensitive evidence, and unrestricted source dumps; CONFIRMED by attached synthesis doctrine that living-person, DNA, rights, consent, policy, review, release, correction, withdrawal, and rollback concerns can block exposure; CONFIRMED current target existed in GitHub as placeholder content before this README; NEEDS VERIFICATION for executable no-log tests, accepted logging envelopes, runtime capture helpers, redaction helpers, policy runtime, fixtures, CI coverage, and pass rates.

---

## Purpose

`tests/domains/people-dna-land/dna/no-log/` is the test lane for one privacy-critical rule:

> DNA-sensitive and living-person payloads must not become logging payloads.

This lane should prove that KFM can record enough operational evidence to review a decision without copying raw DNA data, DNA-derived relationship payloads, living-person identifiers, consent payloads, source dumps, secrets, private reasoning, unrestricted EvidenceBundle contents, or unpublished assertion material into logs, traces, diagnostics, AI prompts, error messages, receipts, or public/debug surfaces.

A passing no-log test should **not** mean that a DNA assertion is true, a consent record is valid, a source is admitted, a claim is publishable, a log sink is production-ready, or a release is approved. It should mean only that the scoped logging/redaction guardrail behaved as expected against bounded synthetic fixtures and local files.

[Back to top](#top)

---

## Placement Basis

Directory Rules separate responsibility roots:

| Responsibility | Canonical root |
|---|---|
| Enforceability proof | `tests/` |
| Reusable golden, valid, invalid, or synthetic test data | `fixtures/` or accepted test fixture home |
| Semantic contract meaning | `contracts/` |
| Machine-checkable shape | `schemas/` |
| Allow, deny, restrict, abstain, redact, and release policy | `policy/` |
| Source identity, role, rights, cadence, and caveats | `data/registry/sources/` |
| Publication, correction, withdrawal, rollback, and release artifacts | `release/` and accepted release/proof homes |

This directory is therefore a **test lane**, not a logging policy home, runtime logger, DNA data store, evidence store, source registry, consent system, contract authority, schema authority, or release root.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| DNA no-log enforceability tests | `tests/domains/people-dna-land/dna/no-log/` | This directory. |
| Parent DNA test index | `tests/domains/people-dna-land/dna/` | Placeholder observed; NEEDS VERIFICATION before relying on parent guidance. |
| Consent behavior tests | `tests/domains/people-dna-land/consent/` | Adjacent consent exposure gates. |
| Contract behavior tests | `tests/domains/people-dna-land/contracts/` | Adjacent assertion/envelope tests. |
| Synthetic no-log fixtures | `fixtures/domains/people-dna-land/dna/no-log/` | Preferred reusable fixture home if populated. |
| Logging policy | `policy/` or accepted policy home | Decides what is allowed, denied, redacted, restricted, or abstained. |
| Runtime logging implementation | `runtime/`, `packages/`, `pipelines/`, or accepted implementation home | Emits logs; not defined here. |
| Evidence and receipts | accepted evidence/proof/receipt homes | Logs may reference these objects, not inline sensitive payloads. |
| Release decisions | `release/` | Publication remains a governed state transition. |

[Back to top](#top)

---

## Invariant Under Test

> **Logs may prove that a gate ran; logs must not become the payload.** Operational records can carry opaque identifiers, finite outcomes, redaction summaries, receipt references, and policy decision references. They must not carry raw or reconstructable DNA/living-person material unless a narrower, explicitly governed object family allows it.

Core no-log checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Raw DNA exclusion | Raw genotype, sequence, segment, kit, sample, match, or upload payloads are absent from logs. | test failure / `DENY` recommendation. |
| Living-person exclusion | Names, direct identifiers, private contact data, precise private locations, and identifying family details are absent unless already governed as public-safe references. | test failure / `DENY` recommendation. |
| DNA-derived relationship exclusion | Kinship, match-list, inferred-parentage, triangulation, or relationship payloads do not leak through logs or errors. | test failure / `DENY` recommendation. |
| Consent payload exclusion | Consent form text, signatures, withdrawal reasons, subject identifiers, and private consent metadata are not logged directly. | test failure / `DENY` recommendation. |
| Evidence payload exclusion | EvidenceBundle contents are not copied into operational logs; logs use references and receipt IDs. | test failure / `ABSTAIN` or `DENY`. |
| Source payload exclusion | Provider exports, raw source records, unrestricted dumps, and credentials are not logged. | test failure / security review. |
| Error path redaction | Exceptions, validation errors, policy denials, and adapter failures preserve redaction. | test failure / `ERROR` review. |
| AI boundary | Prompt, context, trace, and answer envelopes do not log raw DNA or living-person payloads. | test failure / AI surface block. |
| Release boundary | Logging success does not imply release, publication, or public display. | test failure / release block. |

[Back to top](#top)

---

## Accepted Inputs

Only bounded, synthetic, reviewable inputs belong in this lane:

- Synthetic DNA-sensitive fixture records designed for redaction testing.
- Synthetic living-person identifiers that are clearly fake and public-safe.
- Synthetic consent records with fake subject IDs and fake withdrawal/scope states.
- Synthetic EvidenceRef, EvidenceBundle stub, PolicyDecision, RedactionReceipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard references.
- Captured log envelopes emitted by local test helpers.
- Static deny/abstain/error examples that prove redaction in success and failure paths.
- Fixture strings intentionally designed to fail if copied into logs.

The lane may assert that logs contain safe operational fields such as:

- request ID
- fixture ID
- validator name
- policy decision ID
- finite outcome
- redaction reason code
- receipt reference
- release ID only when the release object is already public-safe
- schema or spec hash
- synthetic adapter name

> [!IMPORTANT]
> The presence of a safe reference does not authorize dereferencing sensitive material in a public surface. EvidenceBundle resolution, policy decision, review state, consent state, and release state still outrank log convenience.

---

## Exclusions

Do **not** place these materials in this lane:

| Excluded material | Why it does not belong here | Correct direction |
|---|---|---|
| Real DNA data, sample IDs, kit exports, match lists, segment data, genotype data, or provider exports | Sensitive and potentially identifying. | Keep out of default tests; use synthetic fixtures only. |
| Real living-person records, addresses, contacts, family links, or private land associations | Living-person-sensitive and not needed for deterministic tests. | Use fake fixtures with explicit redaction canaries. |
| Consent records with real subject data or signatures | Consent payloads are not logging fixtures. | Use synthetic ConsentRecord-like stubs. |
| Runtime/production logs | This lane proves patterns; it is not a telemetry store. | Runtime/logging home plus reviewed sampling/redaction process. |
| Secrets, credentials, tokens, cookies, provider keys, API URLs with secrets, or auth headers | Security exposure. | Secret manager or local test fake only. |
| Logging policy | Policy authority does not live in tests. | `policy/` or accepted policy home. |
| Logger implementation | Runtime behavior does not live in README files. | `runtime/`, `packages/`, `pipelines/`, or accepted implementation home. |
| Published artifacts, public tiles, public API payloads, or public map screenshots | Release artifacts require governed publication. | `release/`, governed APIs, map artifact homes. |
| Raw EvidenceBundle contents | Logs may reference evidence, not become evidence. | Evidence/proof homes plus governed resolution. |

[Back to top](#top)

---

## Expected Scope

This lane should include tests that inspect log-like outputs from local helpers or runtime adapters and assert that sensitive canaries are absent.

| Scenario | Expected assertion |
|---|---|
| Valid policy denial | Log contains finite outcome and policy decision ID; raw DNA and living-person fields are absent. |
| Validation error | Error log contains safe reason code; original input payload is not echoed. |
| Consent missing | Log identifies missing consent by code/reference; consent payload and subject data are absent. |
| Consent revoked | Log carries withdrawal/redaction reference; revoked subject payload is absent. |
| DNA match rejected | Log carries denial and fixture ID; match list, kit data, and inferred relationship payload are absent. |
| Evidence resolution attempted | Log carries EvidenceRef or receipt reference; EvidenceBundle contents are absent. |
| AI context assembled | Trace proves prompt assembly was bounded; raw DNA and unrestricted evidence are absent. |
| Public-safe summary emitted | Log includes only public-safe summary fields and cannot be used to reconstruct the sensitive payload. |

The default test runner should require no network access, no live providers, no production telemetry, no credentials, no real person data, and no real DNA data.

---

## Suggested Layout

```text
tests/domains/people-dna-land/dna/no-log/
|-- README.md
|-- test_raw_dna_payload_not_logged.py
|-- test_living_person_identifiers_not_logged.py
|-- test_dna_match_list_not_logged.py
|-- test_consent_payload_not_logged.py
|-- test_error_paths_redact_sensitive_payloads.py
|-- test_evidence_bundle_contents_not_logged.py
|-- test_ai_prompt_and_trace_exclude_dna_payload.py
|-- test_receipts_use_refs_not_payloads.py
|-- test_public_safe_log_summary_only.py
`-- test_no_network_dna_no_log.py
```

This layout is **PROPOSED** until executable files exist in the repository.

---

## Run Posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/domains/people-dna-land/dna/no-log
```

Required run posture:

- no network access
- no real DNA data
- no real living-person data
- no credentials
- no production logs
- no source-provider calls
- no public artifact writes
- deterministic fixture inputs
- finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`

---

## Minimal Fixture Contract

Synthetic fixtures should contain canary values that make leakage obvious. A test should fail if any canary appears in logs, traces, diagnostics, prompts, errors, receipts, or public/debug summaries.

```json
{
  "fixture_id": "people-dna-land-dna-no-log-example",
  "policy_decision_id": "policy-decision-fixture-001",
  "safe_log_fields": {
    "request_id": "request-fixture-001",
    "outcome": "DENY",
    "reason_code": "DNA_PAYLOAD_NOT_LOGGABLE",
    "redaction_receipt_ref": "redaction-receipt-fixture-001"
  },
  "must_not_log": [
    "RAW_DNA_CANARY",
    "LIVING_PERSON_CANARY",
    "CONSENT_PAYLOAD_CANARY",
    "DNA_MATCH_LIST_CANARY",
    "UNRESTRICTED_EVIDENCE_CANARY",
    "SOURCE_DUMP_CANARY",
    "SECRET_CANARY"
  ]
}
```

The JSON above is illustrative. Accepted schema, field names, and fixture homes remain **NEEDS VERIFICATION**.

---

## Evidence Ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` | CONFIRMED | `tests/` is the canonical enforceability root; domain-specific materials appear as segments under responsibility roots; `people-dna-land` is a domain lane pattern. | Does not prove this no-log lane has executable tests or accepted fixture shapes. |
| `Unified Implementation Architecture Build Manual.md` | CONFIRMED doctrine | Logs may include request IDs, policy decisions, adapter metadata, citation report IDs, and receipt IDs; logs exclude secrets, private reasoning, raw sensitive evidence, and unrestricted source dumps. | Does not prove current runtime logging implementation, CI, or pass rates. |
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | CONFIRMED synthesis / PROPOSED implementation pressure | Reiterates evidence-first, cite-or-abstain, fail-closed, policy-aware, living-person/DNA sensitivity, release, correction, and rollback posture. | Static synthesis does not prove current repository implementation. |
| `tests/domains/people-dna-land/consent/README.md` | CONFIRMED adjacent pattern | Shows current README style for People DNA Land test lanes: meta block, badges, no-network posture, explicit exclusions, and truth labels. | Consent lane does not define DNA no-log behavior. |
| `tests/domains/people-dna-land/contracts/README.md` | CONFIRMED adjacent pattern | Shows the contract-test index pattern and responsibility-root separation used nearby. | Contract lane does not define logging policy. |
| GitHub target file before update | CONFIRMED | `tests/domains/people-dna-land/dna/no-log/README.md` existed as placeholder content `y` before replacement. | Placeholder proves path existence only. |
| `tests/domains/people-dna-land/dna/README.md` | CONFIRMED placeholder | Parent DNA README existed as placeholder content when this file was authored. | Parent DNA lane guidance remains NEEDS VERIFICATION. |

---

## Validation Checklist

- [ ] Replace or confirm parent DNA test index at `tests/domains/people-dna-land/dna/README.md`.
- [ ] Confirm accepted logging envelope fields and redaction helper names.
- [ ] Confirm accepted fixture home for DNA no-log canary fixtures.
- [ ] Add executable tests for success, denial, abstain, error, consent, evidence, AI, and receipt paths.
- [ ] Ensure tests assert absence of canaries across logs, traces, diagnostics, prompts, errors, receipts, and public/debug summaries.
- [ ] Confirm no test requires network access, credentials, live genealogy/DNA services, production logs, real people data, or real DNA data.
- [ ] Confirm logs may reference EvidenceBundle, PolicyDecision, ConsentRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard objects without inlining sensitive payloads.
- [ ] Confirm public or semi-public outputs still require evidence, policy, review, consent where applicable, release, correction, withdrawal, and rollback support.
- [ ] Wire the lane into CI only after executable tests and safe fixtures exist.

---

## Rollback

Rollback is required if this lane starts to:

- store real DNA, living-person, consent, source, credential, or production-log payloads
- define logging policy instead of testing it
- implement runtime logging behavior inside the test README
- treat logs as EvidenceBundles, receipts, proof stores, or release manifests
- allow logs to become public truth, public API payloads, public map payloads, tiles, screenshots, or generated answer authority
- normalize raw EvidenceBundle contents, private reasoning, source dumps, or secrets as log-safe
- weaken fail-closed behavior for living-person or DNA-sensitive material

Rollback target: restore the previous safe README revision or remove the lane until policy, fixtures, runtime behavior, and CI integration are reverified.

[Back to top](#top)