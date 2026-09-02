<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-flora-watchers-readme
title: Flora Watchers Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <flora-pipeline-owner>
  - <flora-domain-steward>
  - <source-steward>
  - <watcher-maintainer>
  - <sensitivity-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-flora-watcher-and-source-refresh-gates
path: pipelines/domains/flora/watchers/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/flora/README.md
  - pipelines/domains/flora/ingest/README.md
  - pipelines/domains/flora/normalize/README.md
  - pipelines/domains/flora/validate/README.md
  - docs/domains/flora/README.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/SOURCES.md
  - docs/domains/flora/SOURCE_FAMILIES.md
  - docs/domains/flora/SOURCE_REGISTRY.md
  - docs/runbooks/flora/SOURCE_REFRESH_RUNBOOK.md
  - pipeline_specs/flora/watchers.yaml
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - data/raw/flora/
  - data/work/flora/
  - data/quarantine/flora/
  - data/processed/flora/
  - data/catalog/domain/flora/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/flora/
  - release/manifests/flora/
tags:
  - kfm
  - pipelines
  - domains
  - flora
  - watchers
  - source-refresh
  - pre-raw
  - source-intake-record
  - etag
  - last-modified
  - material-change
  - event-envelope
  - receipts
  - non-publisher
  - geoprivacy
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/flora/watchers path as a nested executable Flora watcher/source-refresh sublane."
  - "Flora watcher logic is executable pre-RAW/source-refresh support only; it does not own connectors, source descriptors, schemas, policy, lifecycle data, taxonomy authority, catalog truth, sensitivity decisions, release decisions, or public API authority."
  - "Watchers detect source change and emit event envelopes, prefilter outputs, receipts, and review packets; they do not publish, normalize truth, or write catalog/published artifacts directly."
  - "Source refresh starts at the pre-RAW admission edge and must preserve source identity, source role, rights, sensitivity, material-change classification, review path, and fail-closed quarantine routing."
  - "Controlled Flora source families, rights-unclear feeds, sensitive joins, taxonomy drift, and schema drift fail closed until source descriptor, review, evidence, policy, correction, and rollback controls resolve."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Watchers Pipeline

> Executable Flora sublane for source-refresh watchers, pre-RAW change detection, source-head checks, event envelopes, material-change classification, no-op receipts, review packets, and intake handoffs — while preserving source identity, source role, rights, sensitivity, evidence, policy, lifecycle, correction, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-flora%20watchers-2e7d32)
![authority](https://img.shields.io/badge/authority-pre--RAW%20watcher%20logic-0a7ea4)
![non-publisher](https://img.shields.io/badge/watcher-non--publisher-d62728)
![sensitivity](https://img.shields.io/badge/sensitivity-fail%20closed-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/flora/watchers/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Flora  
**Sublane:** Watchers / source refresh / pre-RAW event detection  
**Placement posture:** nested executable sublane under `pipelines/domains/flora/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; watcher outputs are pre-RAW event envelopes, no-op receipts, source-intake candidates, review packets, or quarantine handoffs only.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Watcher anti-collapse rules](#3-watcher-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Watcher scope](#6-watcher-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal watcher event record](#11-minimal-watcher-event-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Review, promotion, publication, correction, and rollback](#13-review-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/flora/watchers/` is the executable sublane for Flora source-refresh watchers and pre-RAW event handling.

It supports candidate processing for:

- scheduled or manually triggered source-head checks for admitted Flora source descriptors;
- conditional `ETag`, `Last-Modified`, content-length, checksum, version, DOI, package, API metadata, or file-manifest checks;
- no-op watcher receipts when a source has not materially changed;
- pre-RAW `EventEnvelope`, `prefilter_output`, `EventRunReceipt`, and `SourceIntakeRecord` candidates when material change is detected;
- source-family-specific refresh risks for herbarium/specimen portals, occurrence aggregators, community-science observations, conservation-status feeds, listing/status feeds, vegetation surveys, remote-sensing vegetation-index products, and restoration records;
- material-change classification before any RAW admission or downstream normalization;
- review packets or pull-request handoffs for source stewards and Flora stewards;
- quarantine or abort handoffs for rights uncertainty, source-role ambiguity, sensitive exact geometry, sensitivity join risk, taxonomy drift, schema drift, endpoint failure, stale credentials, or kill-switch state.

This directory implements or will implement the **how** of Flora watcher execution. It does not own source descriptors, connector fetch logic, source profiles, taxonomy authority, schemas, policy, sensitivity decisions, lifecycle data, catalog truth, release decisions, or public API/map output.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/flora/`? | Flora is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `watchers/`? | This is a narrow executable sublane for Flora source-refresh detection and pre-RAW event generation. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Connectors fetch source payloads; watchers detect change, classify materiality, and open review/intake handoffs. | CONFIRMED separation |
| Is this ingest? | No. Ingest admits captures into RAW/WORK/QUARANTINE; watchers live at the pre-RAW source-refresh edge. | CONFIRMED local separation |
| Can this sublane publish? | No. Watchers are non-publishers and must not write processed/catalog/published artifacts. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> A watcher detects or proposes. It does not publish, prove botanical truth, approve sensitivity handling, decide release, or write public artifacts. Material change opens review/intake work; no material change emits a no-op receipt.

[⬆ Back to top](#top)

---

## 3. Watcher anti-collapse rules

Flora watcher processing must preserve source-refresh state, pre-RAW status, source roles, rights, sensitivity, and review state.

Disallowed collapses:

```text
watcher event -> RAW payload
watcher success -> source admission approval
source-head change -> material botanical change
ETag change -> taxon update
connector availability -> source trust
prefilter pass -> policy approval
source family profile -> SourceDescriptor
SourceIntakeRecord -> processed Flora object
review packet -> release candidate
no-op receipt -> proof source is unchanged forever
watcher run -> catalog update
watcher run -> public release
```

Required distinctions:

- schedule trigger, conditional source-head response, connector result, event envelope, prefilter output, SourceIntakeRecord, RAW capture, WORK candidate, QUARANTINE record, processed object, catalog record, release candidate, and published artifact remain distinct;
- source roles and rights are read from source descriptors and are not invented at watcher runtime;
- watcher time, source observed time, source valid time, retrieval time, processing time, review time, and release time remain distinct;
- sensitivity joins and controlled source families fail closed until reviewed;
- every changed-source handoff has receipts, hashes, reason codes, and steward routing.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Flora watcher/source-refresh logic.

Appropriate contents include:

- fixture-only watcher dry-run entrypoints;
- source-head checkers that operate on admitted source descriptor metadata;
- conditional request helpers for `ETag`, `Last-Modified`, content length, version id, package digest, DOI, or manifest hashes;
- material-change classifiers;
- no-op receipt emitters;
- `EventEnvelope`, `prefilter_output`, `EventRunReceipt`, and `SourceIntakeRecord` builders;
- kill-switch and abort-state checks;
- source-role, rights, sensitivity, and source-vintage preflight helpers;
- review packet / PR handoff helpers;
- quarantine handoff helpers for uncertain rights, source-role collapse, sensitive joins, endpoint drift, schema drift, taxonomy drift, or stale credentials.

A good placement test:

> If the code detects whether a Flora source changed and emits pre-RAW events, receipts, review packets, or intake candidates without publishing, it may belong here. If it fetches full source payloads as connector authority, admits bytes into RAW, normalizes records, validates records, builds catalog truth, decides release, or serves public API/map output, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Full upstream fetchers and API clients | `connectors/<source>` or accepted connector home |
| Ingest routing / RAW admission | `pipelines/domains/flora/ingest/` |
| Normalization mappers | `pipelines/domains/flora/normalize/` |
| Validation logic | `pipelines/domains/flora/validate/` |
| Redaction transforms | `pipelines/domains/flora/redact/` |
| Catalog and triplet builders | `pipelines/domains/flora/catalog/` and lifecycle catalog/triplet homes |
| Source-family profiles | `docs/domains/flora/SOURCE_FAMILIES.md` and source docs |
| Source descriptors / source registry entries | `data/registry/sources/flora/` or approved registry home |
| Flora doctrine and object meaning | `docs/domains/flora/`, `contracts/domains/flora/` |
| JSON Schemas | `schemas/contracts/v1/domains/flora/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Fixtures | `fixtures/domains/flora/watchers/` or accepted fixture home |
| Tests | `tests/pipelines/domains/flora/watchers/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Watcher scope

| Scope area | Watcher responsibility | Failure behavior |
|---|---|---|
| SourceDescriptor | Confirm watcher has an admitted source descriptor with source role, rights, sensitivity, cadence, and endpoint/check strategy. | Abort or hold. |
| Conditional check | Run low-cost source-head / manifest / metadata check. | Emit failure receipt; do not fetch blindly. |
| Materiality | Classify no-op, metadata-only, schema, rights, sensitivity, taxonomic, geometry, payload, or endpoint change. | Hold if not classifiable. |
| Receipts | Emit deterministic no-op, change, abort, or failure receipts. | Fail run if receipt cannot be written. |
| Prefilter | Run source-role, rights, sensitivity, and schema preflight before intake. | Quarantine or review handoff. |
| Review packet | Open or prepare reviewed PR/review packet when material change is detected. | Hold if reviewer path missing. |
| Public trust | Prevent processed/catalog/published writes and public-surface exposure. | Abort on side-effect attempt. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Flora watcher run must preserve the KFM lifecycle:

```text
PRE-RAW EVENT -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, source descriptors, source registry refs, watcher specs, cadence rules, last-known source-head state, and kill-switch state.
2. **Check** source-head or metadata conditions without treating the result as source truth.
3. **Emit** no-op receipts when no material change is detected.
4. **Emit** pre-RAW event envelopes and prefilter outputs when change is detected.
5. **Route** material change into review packet, intake candidate, or quarantine/hold depending on rights, source role, sensitivity, schema, and reviewer availability.
6. **Never write** directly to processed, catalog, triplet, published, public API, public UI, or release-manifest homes.

Watcher output is pre-RAW evidence of source-change state. It is not Flora truth, catalog truth, or public truth.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Flora watcher run must check or explicitly fail closed on:

1. **SourceDescriptor gate** — source id, source role, rights, sensitivity, cadence, watcher type, and retrieval/check plan exist.
2. **Kill-switch gate** — watcher-specific and domain-wide abort flags are not engaged.
3. **Fixture/no-network gate** — dry-run fixture exists for every source-specific watcher path.
4. **Source-head gate** — conditional check result is recorded with headers, status, digest, and timestamp where applicable.
5. **Materiality gate** — change is classified before any intake or review packet is opened.
6. **Source-role gate** — watcher does not infer or upgrade source role at runtime.
7. **Rights gate** — rights-unclear sources hold or quarantine, not silently ingest.
8. **Sensitivity gate** — controlled source families and sensitive joins fail closed pending review.
9. **Receipt gate** — every no-op/change/abort/failure outcome emits a deterministic receipt.
10. **Review routing gate** — material changes identify the steward/reviewer path before downstream handoff.
11. **No-direct-processing gate** — watcher does not normalize, validate, catalog, or publish.
12. **No-direct-public gate** — watcher does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/flora/watchers/
├── README.md                         # this file
├── WATCHERS_CONTRACT.md              # PROPOSED: Flora watcher execution contract
├── run_dry_fixture.py                # PROPOSED synthetic fixture only
├── check_source_head.py              # PROPOSED
├── classify_material_change.py       # PROPOSED
├── validate_source_descriptor.py     # PROPOSED
├── validate_kill_switch.py           # PROPOSED
├── validate_rights_sensitivity.py    # PROPOSED
├── build_event_envelope.py           # PROPOSED
├── build_prefilter_output.py         # PROPOSED
├── build_source_intake_record.py     # PROPOSED
├── open_review_packet.py             # PROPOSED, no auto-merge
├── emit_watcher_receipt.py           # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin source-head adapters, no full source fetch authority
```

Declarative specs should live outside this directory:

```text
pipeline_specs/flora/watchers.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted event, work, quarantine, and receipt homes such as `data/work/flora/`, `data/quarantine/flora/`, and `data/receipts/`, with RAW admission delegated to ingest and public release delegated to release workflow.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/flora/watchers/` or accepted fixture home | Synthetic source-head responses. |
| Source descriptor | `data/registry/sources/flora/` or accepted registry home | Read-only watcher input. |
| Watcher spec | `pipeline_specs/flora/watchers.yaml` or accepted spec home | Declarative schedule/check config. |
| Last-known state | accepted registry/receipt state | Used for material-change comparison. |
| Event envelope | `data/work/flora/<run_id>/` or accepted pre-RAW event home | Pre-RAW candidate only. |
| Prefilter output | `data/work/flora/<run_id>/` | Candidate admission precheck. |
| SourceIntakeRecord | `data/work/flora/<run_id>/` | Candidate for ingest/review. |
| Quarantine / hold | `data/quarantine/flora/<reason>/<run_id>/` | Rights, sensitivity, schema, role, or endpoint failure. |
| Watcher receipt | `data/receipts/pipeline/flora/watchers/<run_id>.yml` or accepted receipt home | Records no-op/change/abort/failure state. |
| Review packet | PR/review packet path owned by workflow | Reviewed handoff only; no auto-publish. |

[⬆ Back to top](#top)

---

## 11. Minimal watcher event record

The final schema is not defined here. This example shows the minimum information a Flora watcher event should preserve.

```yaml
schema_version: kfm.flora_watcher_event.v1
watcher_event_id: flora_watcher_<source_id>_<run_id>_<hash>
pipeline_id: domains.flora.watchers
run_id: run_YYYYMMDDThhmmssZ
status: PRE_RAW_EVENT
source:
  source_id: <source_id>
  source_descriptor_ref: data/registry/sources/flora/<source_id>.yml
  source_family: <gbif|idigbio|inaturalist|kdwp|usfws_ecos|natureserve|herbarium|vegetation_index|restoration|other>
  source_role: <observed|regulatory|administrative|aggregate|model|candidate|synthetic|generated_context>
watcher:
  watcher_type: <api|file|stac|tile|manual|other>
  cadence: null
  kill_switch_state: clear
  last_known_state_ref: null
source_head:
  etag: null
  last_modified: null
  content_length: null
  version_id: null
  manifest_hash: null
  observed_at: null
materiality:
  outcome: <NO_OP|MATERIAL_CHANGE|HOLD|ABORT|FAIL>
  change_classes: []
  reason_codes: []
prefilter:
  rights_state: needs_review
  sensitivity_state: needs_review
  schema_hint_state: needs_review
  source_role_state: needs_review
outputs:
  event_envelope_ref: data/work/flora/run_YYYYMMDDThhmmssZ/event_envelope.yml
  prefilter_output_ref: data/work/flora/run_YYYYMMDDThhmmssZ/prefilter_output.yml
  source_intake_record_ref: null
  quarantine_ref: null
  receipt_ref: data/receipts/pipeline/flora/watchers/run_YYYYMMDDThhmmssZ.yml
anti_collapse:
  watcher_event_is_raw_payload: false
  watcher_success_is_admission: false
  etag_change_is_botanical_change: false
  watcher_run_is_publication: false
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic source-head replay, and no-network** until watcher specs, source descriptors, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/flora/watchers/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_kill_switch_aborts.py              # PROPOSED
├── test_noop_emits_receipt.py              # PROPOSED
├── test_material_change_classified.py      # PROPOSED
├── test_rights_unclear_holds.py            # PROPOSED
├── test_sensitive_join_holds.py            # PROPOSED
├── test_source_role_not_invented.py        # PROPOSED
├── test_event_envelope_emitted.py          # PROPOSED
├── test_prefilter_output_emitted.py        # PROPOSED
├── test_no_raw_write_without_ingest.py     # PROPOSED
├── test_no_processed_catalog_published_write.py # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors and kill-switch state are required, no-op and material-change receipts are deterministic, sensitive joins hold, source roles are not invented at runtime, review packets are opened only for material changes, and no run writes directly to RAW, PROCESSED, CATALOG, TRIPLET, PUBLISHED, public UI, public API, or release manifests.

[⬆ Back to top](#top)

---

## 13. Review, promotion, publication, correction, and rollback

Flora watcher pipelines may prepare event envelopes, receipts, and review/intake handoffs. They do not promote or publish.

Required chain:

```text
watcher schedule / manual trigger
  -> source-head check
  -> no-op receipt OR pre-RAW event envelope
  -> prefilter output
  -> review packet or ingest handoff
  -> RAW / WORK / QUARANTINE by ingest
  -> normalization
  -> validation report
  -> EvidenceBundle closure
  -> catalog / triplet handoff
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public artifact
```

Correction and rollback posture:

- no-op, changed, failed, held, aborted, stale, and quarantined watcher runs remain auditable;
- receipts preserve source refs, source-head refs, source-role refs, rights/sensitivity prefilter refs, hashes, timestamps, and failure reasons;
- watcher events are superseded by governed intake/review transitions, not hidden overwrite;
- downstream artifacts are invalidated if source descriptor refs, source-role refs, source-vintage refs, evidence refs, policy refs, review refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/flora/watchers/README.md` file;
- identifies this directory as a nested executable Flora watcher/source-refresh sublane;
- prevents connector, ingest, normalize, validate, source-profile, schema, contract, policy, fixture, test, data, proof, public API, UI, sensitivity-decision, catalog, and release authority from being placed here;
- preserves source descriptor, watcher type, source family, source role, source-vintage, rights, source-head state, materiality, event envelope, prefilter output, SourceIntakeRecord, lifecycle, quarantine, evidence, policy, correction, and rollback boundaries;
- blocks watcher-event-as-RAW, watcher-success-as-admission, ETag-as-botanical-change, source-family-profile-as-descriptor, no-op-as-permanent-proof, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor fixtures, no-network source-head fixtures, watcher specs, contract conformance, source-role/rights/sensitivity/materiality/no-RAW/no-processed/no-catalog/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `FLORA-WATCH-001` | Should Flora watchers remain one sublane, or split into api, file, stac, tile, herbarium, occurrence, taxonomy, status, and vegetation-index watcher processors? | NEEDS VERIFICATION / ADR |
| `FLORA-WATCH-002` | Which connector outputs and source-head metadata fields are allowed as watcher inputs before ingest? | NEEDS VERIFICATION |
| `FLORA-WATCH-003` | Which schema owns EventEnvelope, prefilter_output, EventRunReceipt, SourceIntakeRecord, and watcher reason codes? | NEEDS VERIFICATION |
| `FLORA-WATCH-004` | Which CI job owns Flora watcher invariant tests? | UNKNOWN |
| `FLORA-WATCH-005` | Which sources should be first-wave no-network fixtures: GBIF, iDigBio, iNaturalist, NatureServe, ECOS, USDA PLANTS, herbarium IPT, or vegetation-index sources? | NEEDS VERIFICATION |
| `FLORA-WATCH-006` | Should source-head state be stored in receipts, source registry sidecars, or a dedicated watcher state registry? | NEEDS VERIFICATION / ADR |
| `FLORA-WATCH-007` | Which review-packet format should watchers open when material change is detected? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic source-head fixtures, no-network dry runs, and negative tests. Do not add live endpoint polling, connector authority, source-descriptor editing, schema authority, policy authority, sensitivity-decision authority, ingest authority, direct catalog writes, public API code, public UI code, release-manifest writes, public layer writes, or generated botanical summaries until source descriptors, watcher specs, source roles, materiality classification, prefilter receipts, steward review, and rollback expectations are proven.
