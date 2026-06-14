<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-ingest-fauna-readme
title: Fauna Shared Ingest Adapter README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <ingest-steward>
  - <fauna-domain-steward>
  - <source-steward>
  - <geoprivacy-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-fauna-ingest-geoprivacy-and-quarantine-gates
path: pipelines/ingest/fauna/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/ingest/README.md
  - pipelines/normalize/fauna/README.md
  - pipelines/domains/fauna/README.md
  - docs/domains/fauna/ARCHITECTURE.md
  - pipeline_specs/ingest/fauna.yaml
  - pipeline_specs/fauna/
  - contracts/domains/fauna/
  - schemas/contracts/v1/domains/fauna/
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - data/registry/sources/fauna/
  - data/raw/fauna/
  - data/work/fauna/
  - data/quarantine/fauna/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
tags: [kfm, pipelines, ingest, fauna, adapter, source-admission, occurrence, monitoring, geoprivacy, quarantine, receipt, evidence-bundle, policy, governance]
notes:
  - "This README fills the blank pipelines/ingest/fauna path as a Fauna adapter/profile under the shared ingest lane."
  - "This path is not the primary Fauna domain-ingest authority. Domain-owned behavior remains under pipelines/domains/fauna/ or an accepted domain ingest sublane."
  - "Because pipelines/ingest/fauna creates a domain-named segment under a shared helper lane, long-term placement remains NEEDS VERIFICATION / ADR if it hardens beyond adapter/profile support."
  - "Fauna ingest must preserve source roles, occurrence evidence, restricted/public split, geoprivacy preflight, SourceDescriptor refs, policy state, and receipts."
  - "Concrete executable behavior, source activation, CI coverage, fixtures, schema paths, and release wiring remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Shared Ingest Adapter

> Shared ingest adapter/profile for Fauna-specific source-admission checks, source-intake records, payload integrity, source-role preservation, occurrence/monitoring intake, restricted/public split preflight, geoprivacy blockers, and receipt-ready RAW/WORK/QUARANTINE handoffs — without replacing the Fauna domain pipeline, owning Fauna truth, creating EvidenceBundles, deciding policy, or publishing public artifacts.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-fauna%20ingest%20adapter-2e7d32)
![authority](https://img.shields.io/badge/authority-shared%20adapter%20only-0a7ea4)
![sensitivity](https://img.shields.io/badge/fauna%20sensitivity-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/ingest/fauna/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Sublane:** Shared ingest / Fauna adapter-profile support  
**Placement posture:** `PROPOSED / NEEDS VERIFICATION`; use this only as a shared adapter/profile lane. Domain-owned Fauna ingest remains under `pipelines/domains/fauna/` unless an ADR or migration note says otherwise.  
**Public posture:** no direct publication; outputs are RAW captures, WORK intake handoffs, QUARANTINE records, source-admission receipts, and blocker reports only.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Fauna ingest anti-collapse rules](#3-fauna-ingest-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Adapter scope](#6-adapter-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal adapter receipt](#11-minimal-adapter-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/ingest/fauna/` is a Fauna-specific adapter/profile under the shared ingest lane.

It may support reusable source-admission behavior for:

- Fauna source-intake records and connector-staged payload refs;
- animal observation, occurrence, monitoring-event, range/context, status, mortality, disease, invasive-species, and derived-indicator intake packets;
- SourceDescriptor lookup and source-role preservation;
- payload hash, media type, manifest, retrieval context, source vintage, time fields, rights, and citation checks;
- restricted/public split and geoprivacy preflight flags before RAW admission;
- QUARANTINE routing for unresolved source role, rights, citation, payload hash, geoprivacy, evidence, policy, or steward-review state;
- raw-capture receipt fragments used by the owning Fauna domain ingest process.

This directory implements or will implement **adapter support** only. It does not replace `pipelines/domains/fauna/`, does not own Fauna object meaning, does not fetch upstream data as connector authority, does not define SourceDescriptors, does not normalize records, does not create EvidenceBundles, does not decide policy/geoprivacy/review state, does not write catalog truth, and does not release public artifacts.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline/helper logic: the **how**. | CONFIRMED root responsibility |
| Why `ingest/`? | Parent lane holds shared source-admission helpers and adapter profiles. | CONFIRMED parent-lane posture |
| Why `fauna/` under shared ingest? | It can hold Fauna-specific adapter glue for shared helpers, but should not become the primary domain lane. | PROPOSED / NEEDS VERIFICATION |
| Does this replace `pipelines/domains/fauna/`? | No. Fauna domain behavior remains under the domain pipeline lane. | CONFIRMED boundary posture |
| Does this decide geoprivacy or policy? | No. It preserves and carries refs/state; policy and geoprivacy authority live in policy/review roots. | CONFIRMED authority separation |
| Can this publish? | No. It returns RAW refs, WORK handoffs, QUARANTINE refs, blocker reports, and receipt fragments only. | CONFIRMED governance posture |

> [!IMPORTANT]
> This folder is an adapter/profile lane, not a canonical Fauna domain pipeline. If it starts owning full domain ingest behavior, it should move to `pipelines/domains/fauna/ingest/` or be governed by an ADR.

[⬆ Back to top](#top)

---

## 3. Fauna ingest anti-collapse rules

Disallowed collapses:

```text
adapter output -> Fauna truth
connector output -> RAW without admission
source-intake record -> SourceDescriptor
RAW capture -> normalized record
RAW capture -> EvidenceBundle
RAW capture -> catalog record
occurrence intake -> public occurrence
OccurrenceRestricted -> OccurrencePublic
ingest success -> validation pass
payload hash -> rights approval
geoprivacy preflight -> public-safe release
generated ingest summary -> evidence
```

Required distinctions:

- connector output, SourceDescriptor, source-intake record, RAW capture, WORK handoff, QUARANTINE record, raw-capture receipt, ValidationReport, EvidenceBundle, catalog record, triplet projection, ReleaseManifest, CorrectionNotice, RollbackCard, and public artifact remain separate;
- Fauna object families stay under Fauna domain ownership;
- occurrence evidence, restricted occurrence, public occurrence, range, sensitive-site class, monitoring event, mortality, disease, invasive-species, and derived indicators remain separately labeled;
- source roles are read from governed descriptors and cannot be invented at ingest time;
- unresolved rights, sensitivity, evidence, policy, or steward-review state fails closed.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include:

- Fauna ingest adapter README files;
- fixture-only adapter dry-run entrypoints;
- Fauna SourceDescriptor lookup wrappers;
- source-intake packet shape checks for fauna source families;
- payload-integrity, media type, manifest, retrieval-context, and source-vintage helpers;
- source-role and rights/citation preservation helpers;
- restricted/public split and geoprivacy preflight blockers;
- QUARANTINE reason helpers for unresolved Fauna-specific ingest blockers;
- raw-capture receipt fragments, if not already shared;
- handoff helpers that return control to the Fauna domain ingest or normalize lane.

A good placement test:

> If the code adapts shared ingest helpers for Fauna while returning control to the Fauna domain pipeline, it may belong here. If it owns full Fauna ingest behavior, put it under `pipelines/domains/fauna/ingest/`. If it owns schema, policy, source descriptors, EvidenceBundle truth, catalog truth, release decisions, or public serving, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Primary Fauna domain workflow | `pipelines/domains/fauna/` or accepted Fauna sublane |
| Full domain-specific ingest pipeline | `pipelines/domains/fauna/ingest/` if/when accepted |
| Normalization mappers | `pipelines/domains/fauna/normalize/` or shared adapters under `pipelines/normalize/fauna/` |
| Source fetchers and API clients | `connectors/<source_id>/` or accepted connector home |
| Source descriptors | `data/registry/sources/fauna/` or accepted registry home |
| Fauna doctrine and object meaning | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| JSON Schemas | `schemas/contracts/v1/domains/fauna/` or accepted schema home |
| Policy / geoprivacy / review decisions | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, review roots |
| Fixtures | `fixtures/ingest/fauna/` or `fixtures/domains/fauna/` |
| Tests | `tests/pipelines/ingest/fauna/` or domain test homes |
| Lifecycle outputs | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, `data/processed/fauna/`, `data/catalog/domain/fauna/`, `data/published/layers/fauna/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions | `release/...` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Adapter scope

| Scope area | Adapter responsibility | Failure behavior |
|---|---|---|
| Caller scope | Require an owning Fauna pipeline or approved proof harness. | Hold if ownerless. |
| Source descriptor | Resolve source id, role, rights, citation, cadence, and source vintage refs. | Quarantine/hold if missing. |
| Payload integrity | Verify hash, media type, manifest, retrieval context, and capture timestamp metadata. | Reject or quarantine. |
| Source role | Preserve descriptor-provided source role; do not invent authority. | Fail on role ambiguity. |
| Restricted/public split | Preserve restricted/public and geoprivacy preflight state. | Hold pending review/policy. |
| Evidence | Carry EvidenceRef candidates forward; never fabricate EvidenceBundles. | Abstain if unresolved. |
| Receipts | Emit shared receipt fragments or raw-capture receipt candidates. | Fail closed on missing refs/hashes. |
| Handoff | Return RAW/WORK/QUARANTINE refs to the Fauna domain lane. | No validation/catalog/publish side effects. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every helper in this adapter must preserve KFM lifecycle posture:

```text
PRE-RAW EVENT -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** fixture, source-intake, connector-staged, or approved manual-intake refs only when an owning Fauna pipeline or proof harness provides scope.
2. **Check** source descriptor, source role, rights, citation, payload hash, media type, source vintage, observation time, restricted/public state, geoprivacy preflight, and evidence refs.
3. **Return** RAW admission decisions, WORK handoff refs, QUARANTINE reason refs, and receipt fragments to the owning caller.
4. **Never normalize, validate, catalog, create EvidenceBundles, approve geoprivacy, decide release, or publish.**

[⬆ Back to top](#top)

---

## 8. Required gates

Every adapter run must check or explicitly fail closed on:

1. **Caller ownership gate** — an owning Fauna domain pipeline or approved proof harness must provide scope.
2. **Input lifecycle gate** — input is fixture, connector-staged, source-intake, RAW-candidate, or approved QUARANTINE remediation.
3. **SourceDescriptor/source-role gate** — source identity, role, rights, citation, cadence, and source vintage are carried forward.
4. **Payload-integrity gate** — payload hash, size, media type, manifest, capture timestamp, and retrieval context are recorded.
5. **Taxon/occurrence boundary gate** — taxon, occurrence evidence, monitoring events, ranges, and derived indicators are not collapsed.
6. **Restricted/public split gate** — restricted occurrence and public derivative remain separate.
7. **Geoprivacy gate** — preflight state does not imply public-safe release.
8. **Evidence gate** — EvidenceRef candidates are carried forward; EvidenceBundles are not fabricated here.
9. **Policy/review gate** — unresolved geoprivacy, rights, sensitivity, or review state remains unresolved and blocks exposure.
10. **Receipt gate** — ingest and adapter receipt metadata is produced where material.
11. **No-direct-normalize gate** — adapter output does not rewrite object fields into normalized records.
12. **No-direct-validation gate** — adapter output does not mark data as validated.
13. **No-direct-catalog gate** — adapter output does not write catalog/triplet records.
14. **No-direct-publish gate** — adapter output does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/ingest/fauna/
├── README.md
├── FAUNA_INGEST_ADAPTER_CONTRACT.md  # PROPOSED
├── run_dry_fixture.py                # PROPOSED
├── validate_source_descriptor.py     # PROPOSED
├── validate_source_intake.py         # PROPOSED
├── validate_payload_integrity.py     # PROPOSED
├── validate_rights_citation.py       # PROPOSED
├── preserve_source_role.py           # PROPOSED
├── prepare_geoprivacy_preflight.py   # PROPOSED
├── route_quarantine_reason.py        # PROPOSED
├── emit_adapter_receipt_fragment.py  # PROPOSED
└── adapters/                         # PROPOSED caller adapters only
```

Declarative specs should live outside this directory:

```text
pipeline_specs/ingest/fauna.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use the owning Fauna domain lifecycle homes under `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, and `data/receipts/pipeline/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Adapter fixture | `fixtures/ingest/fauna/` or accepted fixture home | Synthetic/public-safe by default. |
| Caller scope | `pipelines/domains/fauna/` or approved proof harness | Required; this adapter does not run ownerless. |
| Source descriptor | `data/registry/sources/fauna/` or accepted registry home | Read-only source authority. |
| Fauna intake refs | connector-staged, source-intake, or approved remediation refs | Read by stable refs only. |
| RAW capture | `data/raw/fauna/` | Owned by the Fauna domain lane. |
| WORK handoff | `data/work/fauna/` | Owned by the Fauna domain lane. |
| QUARANTINE reason | `data/quarantine/fauna/` | Owned by the Fauna domain lane. |
| Receipt fragment | `data/receipts/pipeline/fauna/ingest/` or accepted receipt home | Method, refs, hashes, and outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced only; not created here. |

[⬆ Back to top](#top)

---

## 11. Minimal adapter receipt

The final schema is not defined here. This example shows the minimum information a Fauna ingest adapter receipt should preserve.

```yaml
schema_version: kfm.ingest.fauna_adapter_receipt.v1
adapter_run_id: fauna_ingest_adapter_run_YYYYMMDDThhmmssZ
pipeline_id: ingest.fauna
status: HELD
caller:
  owner_pipeline: pipelines/domains/fauna/ingest
  profile_ref: pipeline_specs/ingest/fauna.yaml
source:
  source_id: <source_id>
  source_descriptor_ref: data/registry/sources/fauna/<source_id>.yml
  source_role: <source_role>
  rights_state: needs_review
intake:
  source_intake_record_ref: null
  staged_payload_ref: null
  payload_hash: sha256:<hash>
checks:
  caller_scope_resolved: false
  source_descriptor_resolved: false
  payload_integrity_passed: false
  rights_citation_ready: false
  source_role_preserved: false
  restricted_public_split_preserved: false
  geoprivacy_preflight_ready: false
  raw_admission_allowed: false
anti_collapse:
  adapter_output_is_fauna_truth: false
  connector_output_is_raw_without_admission: false
  raw_capture_is_evidence_bundle: false
  occurrence_restricted_is_occurrence_public: false
  ingest_success_is_validation_pass: false
outputs:
  raw_ref: null
  work_handoff_ref: null
  quarantine_ref: null
  receipt_fragment_ref: data/receipts/pipeline/fauna/ingest/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Recommended tests:

```text
tests/pipelines/ingest/fauna/
├── test_no_network_dry_run.py              # PROPOSED
├── test_caller_scope_required.py           # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_payload_integrity_required.py      # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_rights_citation_required.py        # PROPOSED
├── test_taxon_occurrence_boundary.py       # PROPOSED
├── test_restricted_public_split.py         # PROPOSED
├── test_geoprivacy_preflight_not_release.py # PROPOSED
├── test_evidence_refs_not_fabricated.py    # PROPOSED
├── test_unclear_rights_quarantine.py       # PROPOSED
├── test_no_normalize_side_effect.py        # PROPOSED
├── test_no_validation_pass_side_effect.py  # PROPOSED
├── test_no_catalog_side_effect.py          # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, caller scope is required, SourceDescriptors are required, source roles and payload integrity are preserved, rights/citation checks fail closed, taxon/occurrence boundaries hold, restricted/public split is maintained, geoprivacy preflight does not imply release, EvidenceRefs are not fabricated, receipts are deterministic, and no run writes directly to normalization, validation, catalog, triplet, public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Fauna shared ingest adapters may prepare RAW capture refs, WORK handoff refs, QUARANTINE reasons, and receipt fragments. They do not normalize, validate, catalog, or publish.

Required chain:

```text
Fauna domain caller
  -> shared Fauna ingest adapter
  -> RAW capture / WORK handoff / QUARANTINE reason / receipt fragment
  -> Fauna domain normalization
  -> Fauna domain validation
  -> EvidenceBundle closure
  -> catalog / triplet handoff
  -> geoprivacy-reviewed release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- failed adapter runs remain auditable;
- receipts preserve source refs, source-role refs, original payload refs, taxon refs, occurrence refs, geoprivacy refs, EvidenceRef refs, policy refs, and failure reasons;
- adapter outputs are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if source refs, source-role refs, payload hashes, geoprivacy refs, EvidenceBundle refs, policy refs, correction refs, or rollback refs drift;
- rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/ingest/fauna/README.md` file;
- identifies this directory as a Fauna adapter/profile under the shared ingest lane;
- prevents primary Fauna domain logic, connectors, schemas, contracts, policy, source descriptors, lifecycle data, EvidenceBundles, release decisions, public API, UI, catalog, and publication authority from being placed here;
- preserves caller scope, source descriptors, source roles, original payloads, taxon/occurrence/monitoring boundaries, restricted/public split, geoprivacy preflight, EvidenceRef, policy, lifecycle, quarantine, correction, and rollback boundaries;
- blocks adapter-output-as-Fauna-truth, connector-output-as-RAW, RAW-as-normalized-record, RAW-as-EvidenceBundle, OccurrenceRestricted-as-OccurrencePublic, geoprivacy-preflight-as-release, ingest-success-as-validation-pass, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this adapter lane is done only when it has public-safe fixtures, no-network tests, caller-scope checks, SourceDescriptor and payload-integrity tests, source-role and rights tests, taxon/occurrence/monitoring-boundary tests, restricted/public split tests, geoprivacy preflight tests, deterministic receipts, CI coverage, Fauna steward handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-INGEST-FAUNA-001` | Should this adapter remain under `pipelines/ingest/fauna/`, or should it move to `pipelines/domains/fauna/ingest/` once domain ingest scaffolding is accepted? | NEEDS VERIFICATION / ADR |
| `PIPE-INGEST-FAUNA-002` | Which schema owns Fauna adapter ingest receipts and geoprivacy preflight fields? | NEEDS VERIFICATION |
| `PIPE-INGEST-FAUNA-003` | Which Fauna source fixture set should be first-wave for no-network dry runs? | NEEDS VERIFICATION |
| `PIPE-INGEST-FAUNA-004` | Which CI job owns shared Fauna ingest adapter invariant tests? | UNKNOWN |
| `PIPE-INGEST-FAUNA-005` | Should this adapter emit receipt fragments only, or full Fauna ingest receipts? | NEEDS VERIFICATION |
| `PIPE-INGEST-FAUNA-006` | Which source families should be accepted first for Fauna ingest proofing? | NEEDS VERIFICATION |
| `PIPE-INGEST-FAUNA-007` | Which geoprivacy preflight vocabulary is canonical for Fauna intake? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Start with synthetic/public-safe fixtures and negative tests. Do not add live source fetching, Fauna truth ownership, source-profile editing, schema authority, policy/geoprivacy authority, normalization shortcuts, validation shortcuts, catalog writes, public API code, UI code, release-manifest writes, published-layer writes, or generated summaries until caller scope, source descriptors, source roles, payload hashes, rights/citation checks, taxon/occurrence boundaries, restricted/public split, geoprivacy preflight, receipt hashes, EvidenceRef handling, policy state, deterministic receipts, and rollback expectations are proven.
