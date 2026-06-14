<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-ingest-readme
title: Ingest Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <ingest-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-ingest-source-admission-and-quarantine-gates
path: pipelines/ingest/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipeline_specs/ingest/
  - pipelines/domains/
  - connectors/
  - data/registry/sources/
  - tests/pipelines/ingest/
  - fixtures/ingest/
  - data/raw/
  - data/work/
  - data/quarantine/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
tags: [kfm, pipelines, ingest, source-admission, raw-capture, quarantine, receipts, evidence-bundle, policy, governance]
notes:
  - "This README replaces the greenfield stub at pipelines/ingest/README.md with a governed implementation-lane contract."
  - "The pipelines root is executable pipeline logic — the how — while pipeline_specs is declarative configuration — the what."
  - "This path is a shared ingest implementation lane, not a connector root, source descriptor home, schema home, contract home, policy home, lifecycle data home, catalog home, proof store, or release authority."
  - "Domain-specific ingest remains under domain lanes such as pipelines/domains/<domain>/ingest/ unless an ADR or migration note says otherwise."
  - "Concrete executable behavior, source activation, schedules, CI coverage, fixtures, schema paths, and release wiring remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Ingest Pipelines

> Shared executable ingest lane for source-admission helpers, source-intake checks, raw-capture receipts, payload-integrity checks, quarantine routing, and domain-ingest support — without owning connectors, source descriptors, schemas, contracts, policy decisions, lifecycle truth, EvidenceBundle truth, catalog truth, release decisions, or public API/UI behavior.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-shared%20ingest-2e7d32)
![authority](https://img.shields.io/badge/authority-source%20admission%20logic-0a7ea4)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20or%20QUARANTINE-455a64)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/ingest/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Sublane:** Shared ingest helpers / source admission support  
**Placement posture:** implementation sublane under `pipelines/`; exact long-term authority remains `NEEDS VERIFICATION / ADR` if this becomes a shared ingest framework rather than a small helper lane  
**Public posture:** no direct publication; ingest outputs are source-intake records, RAW captures, WORK handoffs, QUARANTINE records, run receipts, and blocker reports only.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Ingest anti-collapse rules](#3-ingest-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Shared ingest scope](#6-shared-ingest-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Definition of done](#11-definition-of-done)
- [12. Open questions](#12-open-questions)

---

## 1. Purpose

`pipelines/ingest/` is the shared executable lane for ingest support that is useful across multiple KFM domain pipelines.

It may support:

- source-intake packet checks;
- connector-staged payload admission helpers;
- SourceDescriptor lookup helpers;
- payload hash, media type, manifest, and retrieval-context checks;
- source-role, rights, citation, cadence, source-vintage, and policy preflight checks;
- immutable RAW capture helpers;
- QUARANTINE routing helpers;
- run receipt and raw-capture receipt builders;
- no-network fixture runners;
- shared adapters used by domain-specific ingest sublanes.

This directory implements or will implement the **how** of shared ingest support. It does not fetch source data as connector authority, define source descriptors, define schemas, decide policy, normalize records, validate records, create EvidenceBundles, write catalog truth, approve release, or serve public clients.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | Ingest helpers are executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why a shared `ingest/` lane? | It can hold reusable source-admission helpers that should not be duplicated across domain lanes. | PROPOSED / NEEDS VERIFICATION |
| Does this replace domain ingest? | No. Domain-owned behavior stays under `pipelines/domains/<domain>/ingest/` or an accepted domain ingest sublane. | CONFIRMED boundary posture |
| Is this a connector home? | No. Connectors fetch or stage source material; ingest admits or holds staged/source-intake material under lifecycle controls. | CONFIRMED authority separation |
| Is this a registry home? | No. Source descriptors remain in accepted source registry homes. | CONFIRMED authority separation |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> Ingest admission is not validation, EvidenceBundle closure, catalog truth, public truth, or release approval. It is the controlled step that admits source-bound material to RAW or routes it to QUARANTINE with auditable receipts.

[⬆ Back to top](#top)

---

## 3. Ingest anti-collapse rules

Disallowed collapses:

```text
connector output -> RAW without admission
source-intake record -> SourceDescriptor
RAW capture -> normalized record
RAW capture -> EvidenceBundle
RAW capture -> catalog record
ingest success -> validation pass
payload hash -> rights approval
source role -> trusted forever
generated ingest summary -> evidence
pipeline run -> ReleaseManifest
```

Required distinctions:

- connector output, source descriptor, source-intake record, RAW capture, WORK handoff, QUARANTINE record, RunReceipt, ValidationReport, EvidenceBundle, catalog record, ReleaseManifest, CorrectionNotice, RollbackCard, and public artifact remain separate;
- source roles are read from governed descriptors and cannot be invented at ingest time;
- rights, citation, cadence, source-vintage, payload hash, time fields, review state, and policy state remain auditable;
- unclear source role, rights, evidence, or policy state fails closed.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is reusable executable ingest/source-admission support.

Appropriate contents include:

- shared ingest README files;
- fixture-only ingest dry-run entrypoints;
- source-intake packet validators;
- SourceDescriptor lookup helpers;
- connector-staged payload admission helpers;
- payload-integrity and immutable-capture helpers;
- source-role, rights, citation, cadence, source-vintage, and retrieval-context checks;
- QUARANTINE reason-code helpers;
- RAW capture receipt builders;
- shared ingest adapters used by domain lanes;
- receipt hash helpers, if not already shared elsewhere.

A good placement test:

> If the code helps multiple domain ingest lanes decide whether staged material becomes RAW, WORK-intake, or QUARANTINE with receipts, it may belong here. If it only belongs to one domain, place it in that domain's ingest lane. If it fetches upstream data, owns source descriptors, owns schemas, decides policy, writes catalog truth, approves release, or serves public clients, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Domain-specific ingest workflows | `pipelines/domains/<domain>/ingest/` |
| Source fetchers and API clients | `connectors/<source_id>/` or accepted connector home |
| Source descriptors | `data/registry/sources/<domain>/` or accepted registry home |
| Domain doctrine | `docs/domains/<domain>/` |
| Schemas | `schemas/contracts/v1/...` accepted schema home |
| Contracts/object meaning | `contracts/...` accepted contract home |
| Policy | `policy/...` responsibility roots |
| Declarative ingest specs | `pipeline_specs/ingest/` or domain-specific spec homes |
| Fixtures | `fixtures/ingest/` or domain fixture homes |
| Tests | `tests/pipelines/ingest/` or domain test homes |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Lifecycle outputs outside governed writer scope | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Release decisions | `release/...` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Shared ingest scope

| Scope area | Shared ingest responsibility | Failure behavior |
|---|---|---|
| Source descriptor | Resolve descriptor refs and required source metadata. | Quarantine or hold if missing. |
| Intake packet | Confirm source, payload, retrieval context, intended lifecycle entry, and hashes. | Hold or quarantine. |
| Payload integrity | Verify hash, size, manifest, media type, and capture timestamp metadata. | Reject or quarantine. |
| Rights/citation | Require explicit rights and attribution state before RAW admission. | Quarantine if unclear. |
| Source role | Preserve descriptor-provided source role; do not invent authority. | Fail on role ambiguity. |
| RAW capture | Support immutable source-bound capture into approved RAW homes. | No WORK/PROCESSED shortcut. |
| QUARANTINE | Emit structured reason codes and receipts for unresolved inputs. | Fail closed. |
| Handoff | Return refs to domain pipelines for normalization. | No normalize/validate/catalog/publish side effects. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every shared ingest helper must preserve the KFM lifecycle:

```text
PRE-RAW EVENT -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** fixture, source-intake, connector-staged, or approved manual-intake packet refs only when a domain pipeline authorizes the call.
2. **Check** source descriptor, source role, rights, citation, cadence, time fields, payload hash, media type, and immutable-capture requirements.
3. **Admit** source-bound material to RAW only when admission gates close.
4. **Route** unresolved or unsupported material to QUARANTINE with structured reasons.
5. **Emit** run receipts, raw-capture receipts, quarantine receipts, and downstream normalization handoff refs.
6. **Return** to the owning domain lane for normalization, validation, catalog, release, and public artifact decisions.
7. **Never normalize, validate, catalog, publish, or decide release directly.**

[⬆ Back to top](#top)

---

## 8. Required gates

Every shared ingest component must check or explicitly fail closed on:

1. **Caller ownership gate** — an owning domain pipeline or approved proof harness must provide scope.
2. **Connector/intake gate** — input comes from an approved connector, manual-intake packet, or fixture with a recorded intake ref.
3. **SourceDescriptor gate** — source identity, source family, source role, rights, citation, cadence, and source vintage are present.
4. **Payload-integrity gate** — hash, size, media type, manifest, and capture timestamp are recorded.
5. **Rights/citation gate** — rights and attribution state are explicit; unresolved rights route to QUARANTINE.
6. **Source-role gate** — source role is preserved and not invented by shared ingest code.
7. **Policy/review gate** — required policy/review preflight state is carried forward or the input holds.
8. **Receipt gate** — every ingest invocation emits deterministic receipts with input/output hashes.
9. **No-direct-normalize gate** — ingest does not rewrite fields into normalized object records.
10. **No-direct-validate/catalog gate** — ingest does not emit validation pass, catalog records, or graph/triplets.
11. **No-direct-publish gate** — ingest does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/ingest/
├── README.md
├── INGEST_SHARED_CONTRACT.md          # PROPOSED
├── run_dry_fixture.py                 # PROPOSED
├── validate_source_descriptor.py      # PROPOSED
├── validate_source_intake.py          # PROPOSED
├── validate_payload_integrity.py      # PROPOSED
├── validate_rights_citation.py        # PROPOSED
├── preserve_source_role.py            # PROPOSED
├── admit_raw_capture.py               # PROPOSED
├── route_quarantine_reason.py         # PROPOSED
├── emit_ingest_receipt.py             # PROPOSED only if not shared
└── adapters/                          # PROPOSED domain/proof adapters only
```

Declarative specs should live outside this directory:

```text
pipeline_specs/ingest/<profile>.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/raw/`, `data/work/`, `data/quarantine/`, and `data/receipts/`, with domain-owned pipelines deciding the target domain lane.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Shared fixture | `fixtures/ingest/` or domain fixture home | Synthetic/public-safe by default. |
| Declarative spec | `pipeline_specs/ingest/` or domain spec home | The what, not executable logic. |
| Source descriptor | `data/registry/sources/<domain>/` or accepted registry home | Read-only input. |
| Staged input | connector or intake staging output | Must carry stable ref and digest metadata. |
| RAW capture | `data/raw/<domain>/<source_id>/<run_id>/` | Immutable, non-public output. |
| WORK handoff | `data/work/<domain>/<run_id>/` | Owned by calling domain lane. |
| QUARANTINE record | `data/quarantine/<domain>/<reason>/<run_id>/` | Owned by calling domain lane. |
| Receipt | `data/receipts/pipeline/<domain>/ingest/` or accepted receipt home | Records inputs, checks, outcomes, hashes, and output refs. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced only; not created here. |

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- replaces the greenfield stub at `pipelines/ingest/README.md`;
- identifies this directory as a shared executable ingest/source-admission support lane under `pipelines/`;
- prevents connector, domain-specific workflow, source-profile, schema, contract, policy, fixture, test, data, proof, normalization, validation, catalog, public API, UI, and release authority from being placed here;
- preserves connector-output, source descriptor, source-intake, payload hash, rights/citation, source-role, RAW/WORK/QUARANTINE lifecycle, receipts, correction, and rollback boundaries;
- blocks connector-output-as-RAW, RAW-as-normalized-record, RAW-as-EvidenceBundle, ingest-success-as-validation-pass, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this lane is done only when it has public-safe fixtures, no-network tests, caller-scope checks, source-descriptor/source-intake/payload-integrity/rights/source-role/quarantine/no-normalize/no-validate/no-catalog/no-direct-publish tests, deterministic receipts, CI coverage, domain-steward handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-INGEST-001` | Is `pipelines/ingest/` the final accepted home for shared ingest helpers, or should this move under `packages/`, `tools/`, or domain lanes by ADR? | NEEDS VERIFICATION / ADR |
| `PIPE-INGEST-002` | Which schema owns shared ingest receipts, source-intake records, and quarantine reason codes? | NEEDS VERIFICATION |
| `PIPE-INGEST-003` | Should every domain ingest sublane call shared helpers, or only use them for common payload/source-admission checks? | NEEDS VERIFICATION |
| `PIPE-INGEST-004` | Which CI job owns shared ingest invariant tests? | UNKNOWN |
| `PIPE-INGEST-005` | Which ingest profiles belong in `pipeline_specs/ingest/` versus domain-specific specs? | NEEDS VERIFICATION |
| `PIPE-INGEST-006` | Should shared ingest emit receipts directly, or only return receipt fragments to domain ingest lanes? | NEEDS VERIFICATION |
| `PIPE-INGEST-007` | Should source-intake records live in a pre-RAW/event home or under domain WORK? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Start with synthetic/public-safe fixtures and negative tests. Do not add live source fetching, domain truth ownership, schema authority, policy authority, source-profile editing, normalization shortcuts, validation shortcuts, catalog writes, public API code, UI code, release-manifest writes, published-layer writes, or generated summaries until caller scope, source roles, source descriptors, source-intake records, payload integrity, rights/citation handling, deterministic receipts, quarantine routing, and rollback expectations are proven.
