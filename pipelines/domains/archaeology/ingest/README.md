<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-archaeology-ingest-readme
title: Archaeology Ingest Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <archaeology-pipeline-owner>
  - <archaeology-domain-steward>
  - <source-steward>
  - <ingest-steward>
  - <review-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-archaeology-ingest-review-and-quarantine-gates
path: pipelines/domains/archaeology/ingest/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/archaeology/README.md
  - pipelines/domains/archaeology/normalize/README.md
  - pipelines/domains/archaeology/validate/README.md
  - docs/domains/archaeology/DATA_LIFECYCLE.md
  - docs/domains/archaeology/VALIDATORS.md
  - docs/runbooks/archaeology/SOURCE_REFRESH_RUNBOOK.md
  - pipeline_specs/archaeology/ingest.yaml
  - contracts/domains/archaeology/
  - schemas/contracts/v1/domains/archaeology/
  - policy/domains/archaeology/
  - policy/sensitivity/archaeology/
  - data/registry/sources/archaeology/
  - data/raw/archaeology/
  - data/work/archaeology/
  - data/quarantine/archaeology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/archaeology/
  - release/manifests/archaeology/
tags: [kfm, pipelines, domains, archaeology, ingest, source-descriptor, raw-capture, quarantine, run-receipt, evidence-bundle, policy, governance]
notes:
  - "This README fills the blank pipelines/domains/archaeology/ingest path as a nested executable Archaeology ingest/source-admission sublane."
  - "Ingest logic is executable source-admission support only; it does not own connectors, source descriptors, schemas, contracts, policy, review decisions, lifecycle truth, catalog truth, release decisions, or public API authority."
  - "Ingest admits approved source payloads to RAW or routes them to QUARANTINE with receipts; it does not normalize, validate, catalog, or publish."
  - "Inputs missing SourceDescriptor role, rights, sensitivity, citation, time fields, or payload hash fail closed to QUARANTINE."
  - "Concrete executable behavior, CI coverage, source activation, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Ingest Pipeline

> Executable Archaeology sublane for admitting approved source payloads into RAW, creating source-intake records, raw-capture receipts, quarantine records, and ingest receipts while preserving source identity, source role, rights, review needs, evidence refs, policy posture, correction paths, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-archaeology%20ingest-8a6d3b)
![authority](https://img.shields.io/badge/authority-source%20admission%20logic-0a7ea4)
![posture](https://img.shields.io/badge/posture-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/domains/archaeology/ingest/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Archaeology  
**Sublane:** Ingest / source admission / RAW or QUARANTINE routing  
**Placement posture:** nested executable sublane under `pipelines/domains/archaeology/`; concrete behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; ingest outputs remain RAW captures, WORK intake candidates, QUARANTINE records, and receipts until normalization, validation, EvidenceBundle, catalog/triplet, release, correction, and rollback closure.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Ingest anti-collapse rules](#3-ingest-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ingest scope](#6-ingest-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal ingest receipt](#11-minimal-ingest-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/archaeology/ingest/` is the executable sublane for Archaeology source admission.

It supports candidate processing for:

- source-refresh handoffs and source-intake records;
- source descriptor resolution before admission;
- raw payload integrity checks, payload hashes, content-addressed storage hints, source-vintage capture, and raw-capture receipts;
- rights, source-role, citation, review, policy, and sensitivity preflight checks;
- routing to RAW when minimum admission controls close;
- routing to QUARANTINE when source identity, rights, review, source role, citation, time fields, payload hash, sensitivity posture, or policy state is unresolved;
- run receipts, ingest receipts, quarantine reason codes, and downstream normalization handoffs.

This directory implements or will implement the **how** of Archaeology ingest. It does not fetch source data as connector authority, define SourceDescriptors, define schemas, decide policy, decide review outcomes, normalize records, validate records, own EvidenceBundle truth, own catalog truth, decide release, or publish public API/map payloads.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/archaeology/`? | Archaeology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path pattern; behavior NEEDS VERIFICATION |
| Why `ingest/`? | This sublane admits approved source payloads into RAW or routes them to QUARANTINE. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Connectors fetch or stage source payloads; ingest admits or rejects them under lifecycle controls. | CONFIRMED separation |
| Does this normalize or validate? | No. It prepares source-bound RAW/WORK/QUARANTINE records for later sublanes. | CONFIRMED separation |
| Can this sublane publish? | No. It has no catalog, release, or public-serving authority. | CONFIRMED governance posture |

> [!IMPORTANT]
> Ingest admission is not evidence closure, validation pass, catalog truth, public truth, or release approval. A source payload admitted to RAW remains non-public and must pass every downstream governed gate before public-safe release.

[⬆ Back to top](#top)

---

## 3. Ingest anti-collapse rules

Archaeology ingest must preserve connector output, source descriptor, source-intake record, RAW capture, WORK candidate, QUARANTINE record, evidence, and release artifacts as separate objects.

Disallowed collapses:

```text
connector output -> RAW without admission
source-intake record -> SourceDescriptor
RAW payload -> normalized record
RAW payload -> evidence bundle
RAW payload -> catalog record
watcher event -> admitted source
source admission -> source trust forever
ingest success -> validation pass
payload hash -> rights approval
review-needed -> reviewer-approved
generated ingest summary -> evidence
pipeline run -> release approval
```

Required distinctions:

- connector output, source descriptor, source-intake record, RAW capture, WORK handoff, QUARANTINE record, RunReceipt, ValidationReport, EvidenceBundle, catalog record, ReleaseManifest, CorrectionNotice, and RollbackCard remain separate;
- source roles are read from governed descriptors and cannot be invented at ingest time;
- rights, citation, sensitivity, cadence, source-vintage, payload-hash, and review state remain auditable;
- unclear source role, rights, review, evidence, or policy state fails closed;
- public clients never read RAW, WORK, QUARANTINE, candidate stores, source APIs, graph internals, vector indexes, or direct model outputs.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Archaeology ingest/source-admission logic.

Appropriate contents include:

- fixture-only ingest dry-run entrypoints;
- source-intake record parsers and validators;
- source descriptor lookup and admission preflight helpers;
- raw payload hash and immutable-capture checks;
- rights/citation/source-vintage/cadence preflight helpers;
- source-role and review-state preflight helpers;
- RAW write adapters that only write to approved RAW homes after admission gates close;
- QUARANTINE routing helpers for unresolved rights, source-role, review, payload, citation, sensitivity, or policy defects;
- run receipt and raw-capture receipt emitters;
- normalization handoff helpers that do not normalize records.

A good placement test:

> If the code decides whether an approved source payload is admitted to RAW, routed to WORK as an intake candidate, or quarantined with receipts, it may belong here. If it fetches from an upstream, authors a SourceDescriptor, normalizes fields, validates objects, writes catalog truth, approves release, or serves public API/map output, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Upstream fetchers and API clients | `connectors/<source>` or accepted connector home |
| Watcher/source-refresh detection | watcher/runbook roots or accepted watcher sublane |
| Source descriptors / source registry entries | `data/registry/sources/archaeology/` or approved registry home |
| Normalization mappers | `pipelines/domains/archaeology/normalize/` |
| Validation logic | `pipelines/domains/archaeology/validate/` |
| Catalog and triplet builders | catalog sublanes and lifecycle catalog/triplet homes |
| Domain doctrine and object meaning | `docs/domains/archaeology/`, `contracts/domains/archaeology/` |
| JSON Schemas | `schemas/contracts/v1/domains/archaeology/` or accepted schema home |
| Policy, rights, review, release rules | `policy/...` and review responsibility roots |
| Fixtures | `fixtures/domains/archaeology/ingest/` or accepted fixture home |
| Tests | `tests/pipelines/domains/archaeology/ingest/` or accepted test home |
| Processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Ingest scope

| Scope area | Ingest responsibility | Failure behavior |
|---|---|---|
| Source descriptor | Resolve descriptor with role, rights, citation, sensitivity, cadence, time fields, and payload-hash expectations. | Quarantine if missing. |
| Intake record | Confirm source-intake record identifies payload, source, retrieval context, and intended lifecycle entry. | Hold or quarantine. |
| Payload integrity | Verify hash, size, manifest, expected media type, and immutable capture behavior. | Reject or quarantine. |
| Rights/citation | Confirm rights and attribution state exist before RAW admission. | Quarantine if unclear. |
| Source role | Preserve source role and prohibit runtime role invention. | Quarantine on role ambiguity. |
| Review/policy | Confirm required review/policy preflight state is present or explicitly pending. | Hold/quarantine. |
| RAW admission | Write only immutable source-bound captures to accepted RAW homes. | No WORK/PROCESSED shortcut. |
| Handoff | Emit receipts and normalization handoff refs. | No validation/catalog/publish side effects. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Archaeology ingest run must preserve the KFM lifecycle:

```text
PRE-RAW EVENT -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, source-intake records, connector-staged payload refs, source descriptors, source registry refs, policy preflight refs, and prior receipts.
2. **Check** source identity, source role, rights, citation, sensitivity, time fields, cadence, payload hash, and immutable capture requirements.
3. **Admit** only source-bound payloads into RAW when admission gates close.
4. **Route** unresolved or unsafe payloads to QUARANTINE with structured reasons.
5. **Emit** run receipts, raw-capture receipts, quarantine receipts, and downstream normalization handoff refs.
6. **Never normalize, validate, catalog, publish, or issue release decisions directly.**

Ingest is the admission gate. It is not source fetching authority, normalization, validation, catalog closure, release approval, or public serving.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Archaeology ingest run must check or explicitly fail closed on:

1. **SourceDescriptor gate** — source identity, source family, source role, rights, citation, cadence, sensitivity, and source vintage are present.
2. **Connector/staging gate** — payload comes from an approved connector, manual intake packet, or fixture path with a recorded intake ref.
3. **Payload-integrity gate** — hash, size, manifest, media type, and capture timestamp are recorded.
4. **Rights/citation gate** — rights and attribution state are explicit; unresolved rights block RAW admission or route to QUARANTINE.
5. **Source-role gate** — source role is preserved and not invented by ingest code.
6. **Review/policy gate** — required review/policy preflight state exists or the material is held.
7. **No-public gate** — RAW, WORK, and QUARANTINE are non-public and cannot be served to clients.
8. **Quarantine reason gate** — every denied/held source has a structured reason code and receipt.
9. **Receipt gate** — every ingest invocation emits deterministic receipts with input/output hashes.
10. **No-direct-normalize gate** — ingest does not rewrite fields into normalized object records.
11. **No-direct-validate/catalog gate** — ingest does not emit validation pass, catalog records, or graph/triplets.
12. **No-direct-publish gate** — ingest does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/archaeology/ingest/
├── README.md                         # this file
├── INGEST_CONTRACT.md                # PROPOSED: Archaeology ingest execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/public-safe fixture only
├── validate_source_descriptor.py     # PROPOSED
├── validate_source_intake.py         # PROPOSED
├── validate_payload_integrity.py     # PROPOSED
├── validate_rights_citation.py       # PROPOSED
├── validate_review_policy.py         # PROPOSED
├── admit_raw_capture.py              # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_ingest_receipt.py            # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/archaeology/ingest.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/raw/archaeology/`, `data/work/archaeology/`, `data/quarantine/archaeology/`, and `data/receipts/` before downstream normalization, validation, processed, catalog, release, and published-layer roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/archaeology/ingest/` or accepted fixture home | Synthetic/public-safe intake fixture. |
| Source descriptor | `data/registry/sources/archaeology/` or accepted registry home | Read-only input to ingest. |
| Connector-staged payload | connector/staging output home | Must carry intake refs and hashes. |
| SourceIntakeRecord | `data/work/archaeology/<run_id>/` or accepted pre-RAW/intake home | Candidate admission record. |
| RAW capture | `data/raw/archaeology/<source_id>/<run_id>/` | Immutable admitted source payload; not public. |
| WORK handoff | `data/work/archaeology/<run_id>/` | Normalization handoff only. |
| QUARANTINE record | `data/quarantine/archaeology/<reason>/<run_id>/` | Failed, restricted, malformed, unresolved, or unsafe material. |
| Receipt | `data/receipts/pipeline/archaeology/ingest/<run_id>.yml` or accepted receipt home | Records inputs, checks, decisions, hashes, and output refs. |

[⬆ Back to top](#top)

---

## 11. Minimal ingest receipt

The final schema is not defined here. This example shows the minimum information an Archaeology ingest receipt should preserve.

```yaml
schema_version: kfm.archaeology_ingest_receipt.v1
ingest_run_id: archaeology_ingest_run_YYYYMMDDThhmmssZ
pipeline_id: domains.archaeology.ingest
status: QUARANTINED
source:
  source_id: <source_id>
  source_family: <source_family>
  source_role: <record|survey|candidate|model|aggregate|interpretation|synthetic>
  source_descriptor_ref: data/registry/sources/archaeology/<source_id>.yml
  source_vintage: null
  rights_state: needs_review
intake:
  source_intake_record_ref: data/work/archaeology/run_YYYYMMDDThhmmssZ/source_intake_record.yml
  connector_payload_ref: null
  payload_hash: sha256:<hash>
  received_at: null
checks:
  source_descriptor_resolved: false
  payload_integrity_passed: false
  rights_citation_ready: false
  source_role_preserved: false
  review_policy_ready: false
  raw_admission_allowed: false
outcome:
  raw_ref: null
  work_handoff_ref: null
  quarantine_ref: data/quarantine/archaeology/<reason>/run_YYYYMMDDThhmmssZ/
  reason_codes: []
anti_collapse:
  connector_output_is_raw_without_admission: false
  raw_payload_is_normalized_record: false
  raw_payload_is_evidence_bundle: false
  ingest_success_is_validation_pass: false
outputs:
  receipt_ref: data/receipts/pipeline/archaeology/ingest/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/public-safe, and no-network** until ingest specs, source descriptors, policy, review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/archaeology/ingest/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_source_intake_record_required.py   # PROPOSED
├── test_payload_integrity_required.py      # PROPOSED
├── test_rights_citation_required.py        # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_review_policy_preflight.py         # PROPOSED
├── test_unclear_rights_quarantine.py       # PROPOSED
├── test_missing_hash_quarantine.py         # PROPOSED
├── test_no_normalize_side_effect.py        # PROPOSED
├── test_no_validation_pass_side_effect.py  # PROPOSED
├── test_no_catalog_side_effect.py          # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, SourceDescriptors are required, source-intake records are required, payload integrity is recorded, rights/citation/source-role checks fail closed, quarantine routing is deterministic, receipts are deterministic, and no run writes directly to normalization pass state, validation pass state, catalog, triplet, public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Archaeology ingest pipelines may prepare RAW captures, WORK intake handoffs, QUARANTINE records, and receipts. They do not normalize, validate, catalog, or publish.

Required chain:

```text
source refresh / intake packet / fixture
  -> source descriptor + payload-integrity + rights/review/policy checks
  -> RAW capture or QUARANTINE hold
  -> normalization handoff
  -> validation report
  -> EvidenceBundle closure
  -> processed Archaeology object
  -> catalog / triplet handoff
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, malformed, restricted, stale, conflicted, and quarantined ingest runs remain auditable;
- receipts preserve source refs, source-role refs, source-vintage refs, payload refs, payload hashes, rights/citation refs, policy refs, review refs, and failure reasons;
- RAW captures are immutable and superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if source descriptors, source roles, payload hashes, rights, review, evidence, policy, correction, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/archaeology/ingest/README.md` file;
- identifies this directory as a nested executable Archaeology ingest/source-admission sublane;
- prevents connector, watcher, source-profile, schema, contract, policy, review-decision, fixture, test, data, proof, normalization, validation, catalog, public API, UI, and release authority from being placed here;
- preserves source descriptor, source role, source vintage, source-intake record, payload hash, rights/citation state, review state, policy preflight, RAW/WORK/QUARANTINE lifecycle, receipts, correction, and rollback boundaries;
- blocks connector-output-as-RAW, watcher-event-as-admission, RAW-as-normalized-record, RAW-as-EvidenceBundle, ingest-success-as-validation-pass, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor fixtures, no-network tests, schema-backed intake receipts, source-intake/payload-integrity/rights/source-role/review-policy/quarantine/no-normalize/no-validate/no-catalog/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `ARCH-INGEST-001` | Should Archaeology ingest remain one sublane, or split into source-intake, RAW capture, quarantine routing, and receipt emission processors? | NEEDS VERIFICATION / ADR |
| `ARCH-INGEST-002` | Which schema owns SourceIntakeRecord, RawCaptureReceipt, RunReceipt, and ingest quarantine reason codes? | NEEDS VERIFICATION |
| `ARCH-INGEST-003` | Which fixture set should be first-wave for no-network dry runs? | NEEDS VERIFICATION |
| `ARCH-INGEST-004` | Which CI job owns Archaeology ingest invariant tests? | UNKNOWN |
| `ARCH-INGEST-005` | Should source-intake records live in `data/work/archaeology/` or a pre-RAW/event home? | NEEDS VERIFICATION / ADR |
| `ARCH-INGEST-006` | Which role can approve source descriptor admission versus raw payload admission? | NEEDS VERIFICATION |
| `ARCH-INGEST-007` | How should correction-driven re-pulls be linked to prior releases and rollback targets? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe fixture-only dry runs and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, review-decision authority, normalization shortcuts, validation shortcuts, direct catalog writes, public API code, public UI code, release-manifest writes, public layer writes, or generated archaeology summaries until source roles, source descriptors, source-intake records, payload integrity, rights/citation handling, review preflight, deterministic receipts, quarantine routing, and rollback expectations are proven.
