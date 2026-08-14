<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0017-source-descriptor-admission-process
title: "ADR-0017 — Source Descriptor Admission Process"
type: adr
adr_id: ADR-0017
version: v1.3
status: proposed
effective_decision_status: proposed
owners:
  - "NEEDS VERIFICATION — source stewardship"
  - "NEEDS VERIFICATION — governance stewardship"
  - "NEEDS VERIFICATION — rights and sensitivity review"
  - "NEEDS VERIFICATION — source registry and connector ownership"
created: 2026-05-09
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
owning_root: docs/
responsibility: "Record the proposed source descriptor admission, activation, intake, policy, connector, lifecycle, and rollback boundary."
current_path: docs/adr/ADR-0017-source-descriptor-admission-process.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 6a9c4665175edd2c32f2fafae0f3bb0dfb0492df
  target_prior_blob: 58693830fcdf9746c5494fdd85298529fa5594a9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  source_descriptor_contract_blob: b57ae5ccc042c1423b75c168438800384c9b6713
  source_descriptor_schema_blob: 582e70b834278c3c6ca9a8b31efbe0989c96f0bc
  source_descriptor_alias_schema_blob: 42da54b28a527850cce88ad89f68921c101fc56b
  source_activation_contract_blob: 3a42d5b38ec7e83623f1de58a34e0b36ee582f81
  source_activation_schema_blob: 017f9e14ba24a0ddb425ca2cfb018ec847812b7d
  source_intake_record_contract_blob: f7842c43f0419aae6a84be30b952ed6686c9c3c8
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
inspection_boundary: >
  Current-session GitHub reads of the ADR inventory, accepted Directory Rules decision,
  source contracts and schemas, fixtures, validators, tests, read-only workflows, policy
  documentation, source authority register, registry package metadata, merged pull requests,
  and current main history. No live source endpoint, deployed registry, active policy evaluator,
  connector runtime, production store, release environment, or audit dashboard was exercised.
related:
  - ./INDEX.md
  - ./ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ./ADR-0018-promotion-gate-sequence.md
  - ./ADR-0021-quarantine-has-structured-exit-paths.md
  - ./ADR-0029-adopt-directory-governance-standard-v2.md
  - ../doctrine/directory-rules.md
  - ../sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../sources/ADMISSION_PROCESS.md
  - ../../contracts/source/source_descriptor.md
  - ../../contracts/source/source_activation_decision.md
  - ../../contracts/source/source_intake_record.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../schemas/contracts/v1/source/source_activation_decision.schema.json
  - ../../control_plane/source_authority_register.yaml
  - ../../data/registry/sources/README.md
  - ../../packages/source-registry/README.md
  - ../../policy/source/README.md
  - ../../policy/intake/README.md
tags: [kfm, adr, source-descriptor, source-admission, source-activation-decision, source-intake-record, source-registry, rights, sensitivity, quarantine, connector-boundary, fail-closed]
notes:
  - "This same-path evidence refresh does not accept ADR-0017 or activate a source."
  - "Descriptor validity, activation-decision validity, admission, connector activation, policy, evidence closure, release, and publication remain separate decisions."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0017 — Source Descriptor Admission Process

> **The gate at which the world becomes KFM-admissible source material.**
>
> No source enters the lifecycle without an admitted descriptor; no descriptor is admitted without a record-level admission contract.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![Descriptor paths: converged](https://img.shields.io/badge/descriptor%20paths-converged-1a7f37?style=flat-square)](#source-descriptor)
[![Activation: fixture first](https://img.shields.io/badge/activation-fixture--first-8250df?style=flat-square)](#source-activation-decision)
[![Authority: held](https://img.shields.io/badge/authority-HELD-b42318?style=flat-square)](#remaining-holds)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#non-goals)

## Summary

Source admission SHALL be governed, staged, reviewable, fail-closed, and reversible. Shape validation is necessary but not sufficient. A valid `SourceDescriptor` does not admit a source, and a schema-valid `SourceActivationDecision` candidate does not authenticate decision authority.

Current repository evidence now proves executable SourceDescriptor path convergence and a fixture-first activation-decision profile. It does **not** prove accepted authority, a populated registry, active policy, connector enforcement, lifecycle writes, release, deployment, or publication. The decision therefore remains **`proposed`**.

<a id="status"></a>

## Status

| Field | Current state |
|---|---|
| ADR identity and path | **CONFIRMED** |
| Decision status | **PROPOSED** |
| Evidence base | `main@6a9c4665175edd2c32f2fafae0f3bb0dfb0492df` |
| Directory authority | ADR-0029 accepted; exact Directory Rules v2 bytes adopted |
| Descriptor validation | Implemented and converged across singular/plural entrypoints |
| Activation-decision profile | Implemented fixture-first; authority and runtime held |
| Authority register | Present, `PROPOSED`, `entries: []` |
| Registry mechanics | Placeholder package metadata at `0.0.0` |
| Source/intake policy | Non-enforcing or documentation-only |
| Effect of this revision | Documentation only; no source or publication effect |

A green workflow cannot accept this ADR. An accepted ADR would not, by itself, prove an operational source-admission system.

<a id="decision"></a>

## Decision

If accepted, KFM SHALL require an admitted `SourceDescriptor` and a separately resolved, operation-specific admission decision before any connector may produce an admitted lifecycle effect. Record-level admission SHALL remain a separate source-specific check after capture.

1. **No implicit admission.** Repository presence, HTTP success, valid JSON, fixtures, green CI, merge, or generated language SHALL NOT admit a source.
2. **No source without an admitted descriptor.** Identity, role, authority rank, rights, sensitivity, access, cadence, citation, source-head posture, and use limits must be reviewable.
3. **Shape is not authority.** Schema-valid objects remain candidates until accepted authority resolves them.
4. **Activation is operation-specific.** It binds exact descriptor identity/digest, operation, scope, policy/review references, timing, lineage, and obligations.
5. **Capture is bounded.** Permitted effects are governed RAW, governed QUARANTINE, or no write; admission never creates PUBLISHED state.
6. **Watcher intake is separate.** `SourceIntakeRecord` records WORK/QUARANTINE observations and cannot authorize RAW admission.
7. **Record admission remains separate.** Captured records must meet source-specific minimum bars before normalized use.
8. **Promotion and release remain downstream.** Evidence, proof, catalog, policy, review, correction, rollback, and release are separate transitions.
9. **Fail closed.** Missing, stale, conflicted, expired, unresolved, or invalid authority yields `DENY`, `HOLD`, `QUARANTINE`, `ABSTAIN`, or `ERROR`.
10. **AI cannot mint authority.** AI may assist drafting and classification but cannot infer source role, rights, sensitivity, admission, or release authority.

## Responsibility boundaries

| Responsibility | Owning surface |
|---|---|
| Architecture decision | `docs/adr/` |
| Human source guidance | `docs/sources/` |
| Object meaning | `contracts/source/` |
| Machine shape | `schemas/contracts/v1/source/`; compatibility aliases delegate |
| Fixtures, tests, validators | `fixtures/`, `tests/`, `tools/validators/` |
| Admissibility rules | `policy/source/`, `policy/intake/`, accepted policy families |
| Machine governance index | `control_plane/` — index only, not authority by itself |
| Registry instances | `data/registry/sources/` |
| Reusable registry mechanics | `packages/source-registry/` — read-only resolution, no authority minting |
| Acquisition | `connectors/` |
| Capture persistence | `data/raw/`, `data/quarantine/`, `data/receipts/` |
| Promotion and release | evidence/proof/catalog/policy/review/`release/` surfaces |
| Public delivery | governed API or approved static release surface |

Accepted Directory Rules v2 support this same-path `docs/adr/` update. No responsibility root or parallel authority home changes here.

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | Finding |
|---|---|
| ADR inventory | Exact identity/path confirmed; status remains `proposed` |
| SourceDescriptor contract | Rich semantic contract exists; draft/PROPOSED |
| Singular descriptor schema | Rich, closed implementation schema exists |
| Plural descriptor schema | `$ref`-only compatibility alias; no competing shape |
| Descriptor validators | Generic and declared CWD-independent entrypoints exist |
| Descriptor tests/workflow | Path parity, fixture polarity, rights checks, receipt closure, read-only workflow exist |
| `SourceActivationDecision` | Proposed contract, closed schema, synthetic fixtures, validator, tests, read-only workflow exist |
| `SourceIntakeRecord` | Separate WORK/QUARANTINE watcher-candidate contract exists |
| Authority register | File exists with `entries: []` |
| Registry package | Metadata remains `0.0.0`; no supported operational API established |
| Source/intake policy | Source prerequisite is non-enforcing; intake lane is documentation-only |
| Live systems | No connector run, registry service, evaluator, lifecycle write, release, or publication surface was exercised |

Merged implementation evidence includes PRs `#2200` for CWD-independent generic validation, `#2221` for descriptor path convergence, and `#1963` for the fixture-first activation profile. A merge proves tracked bytes at a revision; it does not authenticate review, accept this ADR, activate a source, approve rights or sensitivity, execute policy, or publish.

## Admission layers

| Layer | Question | Minimum output | Does not prove |
|---|---|---|---|
| Descriptor shape | Is the descriptor structurally valid? | Validation result | Source truth, rights, activation |
| Source posture review | Are role, rights, sensitivity, access, citation, cadence, source head, and limits reviewable? | Review evidence | Connector permission or release |
| Source activation | May KFM attempt this bounded operation? | Resolved decision and authority lineage | Safe capture or publication |
| Capture disposition | Where may this payload land? | RAW, QUARANTINE, or no-write plus receipt | Record admission or evidence sufficiency |
| Source-health intake | Did a watcher observe a material delta? | WORK/QUARANTINE `SourceIntakeRecord` | RAW admission or promotion |
| Record-level admission | Does a captured record meet the source-specific bar? | Candidate, hold, denial, abstention, or error | Publication |
| Promotion/release | May the result advance or become public? | Policy, proof, catalog, release, correction, rollback | Authority beyond released scope |

Collapsing any two layers is an incomplete implementation.

<a id="source-descriptor"></a>

## SourceDescriptor

`SourceDescriptor` is the stable governance handle for a source. It records how material may be treated; it is not source truth, a payload, receipt, `EvidenceBundle`, `PolicyDecision`, activation decision, release manifest, or public permission.

```text
schemas/contracts/v1/sources/source_descriptor.schema.json
  -> $ref
schemas/contracts/v1/source/source_descriptor.schema.json
```

The plural path is a compatibility alias only. Both validators use the same executable fixture family, and direct tests prove equivalent polarity and working-directory independence. This is implementation convergence, not ADR acceptance.

The rich schema still carries historical fixture metadata naming `tests/fixtures/sources/source_descriptor/`, while executable validation uses `fixtures/contracts/v1/source/source_descriptor/`. That drift remains a bounded hold and must not create a second fixture authority.

<a id="source-activation-decision"></a>

## SourceActivationDecision

`SourceActivationDecision` is the proposed pre-RAW gate record for one activation, re-admission, scope change, deactivation, or retirement operation. It binds descriptor identity/digest, role, rights/sensitivity/access context, policy/review references, route, obligations, timing, lineage, and governance metadata.

| Route | Maximum candidate effect |
|---|---|
| `ADMIT_TO_RAW` | Candidate governed RAW capture under obligations |
| `QUARANTINE` | Governed hold with case and review obligations |
| `DENY_INTAKE` | No admitted lifecycle write |
| `HOLD` | Time-bounded no-write pending review |
| `ERROR` | No partial or permissive fallback |

The fixture-first profile proves local shape and consistency only. Operational graduation also requires authenticated authority, resolved policy/review references, append-only persistence, expiry and supersession enforcement, connector consumption, and exact decision/descriptor/source-head binding in capture receipts.

<a id="source-intake-record"></a>

## SourceIntakeRecord

`SourceIntakeRecord` is a separate watcher/source-health candidate envelope. It records a material observation and finite disposition limited to WORK or QUARANTINE, with later promotion required.

| Concern | `SourceActivationDecision` | `SourceIntakeRecord` |
|---|---|---|
| Primary question | May this bounded operation proceed? | What source change or health condition was observed? |
| Maximum route | RAW, QUARANTINE, or no-write after authority resolution | WORK or QUARANTINE only |
| Candidate delta | Not a change proposal | Optional only for `PROPOSED_WORK_RECORD` |
| Publication authority | None | None |

Watchers may observe and propose. They cannot self-admit, activate, create evidence, promote, release, or publish.

## Connector, policy, and record boundary

Before live use, a connector SHALL resolve the exact descriptor and current activation decision; remain within role, scope, and obligations; preserve descriptor/decision/source-head/capture identity; write only to governed RAW or QUARANTINE; emit accepted receipts; expose no direct PUBLISHED edge; and stop on authority drift.

After capture, source-specific record checks SHALL cover native identity, provenance, time, geometry/CRS/precision, domain semantics, role, rights/sensitivity/consent overrides, duplicates/conflicts, citation capability, validity flags, uncertainty, and deterministic reason codes. The result remains a candidate, hold, denial, abstention, or error—not evidence closure or publication.

Current evidence supports fail-closed policy intent, not an operational source-admission evaluator. Unknown rights, living-person or genomic data, rare species, archaeology, cultural or tribal material, infrastructure, private land or wells, and harmful precision remain deny- or quarantine-by-default. Redaction and generalization occur before public rendering, never through client-only hiding.

<a id="remaining-holds"></a>

## Remaining holds

- Descriptor and activation semantics remain proposed governance authority.
- Activation candidates cannot authenticate actors or reviewers, resolve policy/review references, or persist authoritative decisions.
- The source authority register is empty; registry mechanics remain placeholder-only.
- Source/intake policy is not a graduated evaluated bundle.
- No repository-wide connector binding proves current activation resolution before acquisition.
- No atomic RAW/QUARANTINE disposition-and-receipt transaction was observed.
- Record-level minimum bars, re-review, correction, retirement, rollback, and public-consumer behavior remain unproven.

## Implementation maturity

| Capability | Status |
|---|---|
| ADR identity and placement | **CONFIRMED** |
| Rich descriptor contract/schema | **CONFIRMED implementation / PROPOSED authority** |
| Descriptor alias, fixtures, validators, tests, workflow | **CONFIRMED implemented** |
| Fixture-first activation-decision slice | **CONFIRMED implemented / PROPOSED authority** |
| Accepted object authority and authenticated review | **NOT MET** |
| Evaluated source/intake/rights/sensitivity policy | **NOT MET** |
| Registry resolver and connector enforcement | **NOT MET** |
| Atomic capture routing, receipts, record admission | **NOT MET** |
| Monitoring, correction, retirement, rollback, audited public integration | **UNKNOWN / NOT ESTABLISHED** |

The repository is at bounded validation and fixture-first decision-profile maturity, not source-admission graduation.

## Implementation sequence

1. Reconcile stale fixture metadata without creating another fixture home.
2. Accept and version descriptor and activation meaning and shape separately from ADR status.
3. Define immutable authority records versus machine indexes and append-only lineage.
4. Implement fail-closed source/intake/rights/sensitivity/access policy with native tests.
5. Implement deterministic read-only descriptor/decision resolution and one internal consumer.
6. Bind connector gates and atomic RAW/QUARANTINE/no-write receipts.
7. Implement source-specific record profiles for two materially different public-safe source families.
8. Exercise re-review, drift, correction, retirement, rollback, and no-public-bypass pilots.
9. Decide ADR acceptance explicitly after decision-significant evidence exists.

Each wave must be independently reviewable and reversible. Live source activation is not required for early waves.

<a id="acceptance-gates"></a>

## Acceptance gates

| Gate | Current state |
|---|---|
| ADR identity/index and Directory placement | **PASS — implementation evidence** |
| Rich descriptor shape and compatibility alias | **PASS — proposed implementation** |
| Both validators CWD-independent; fixture polarity agrees | **PASS — implementation evidence** |
| Rich-schema fixture metadata matches executable root | **HOLD** |
| Activation contract/schema/routes/negative cases | **PASS — fixture-first proposed implementation** |
| Owners, authenticated independent review, accepted authority store | **OPEN** |
| Deterministic authority lookup and supported registry API | **OPEN** |
| Evaluated source/intake/rights/sensitivity policy | **OPEN** |
| Connector requires current activation; no bypass | **OPEN** |
| Every acquisition has one disposition and receipt | **OPEN** |
| Two record-level profiles and governed pilots | **OPEN** |
| Re-review, correction, retirement, rollback exercised | **OPEN** |
| Explicit human acceptance synchronized in ADR/index | **OPEN** |

ADR-0017 SHALL remain `proposed` until decision-significant gates close.

## Consequences and alternatives

**Benefits:** source authority becomes inspectable; compatibility uses one implementation shape; activation semantics are testable before live work; rights, sensitivity, role, and connector permissions can fail closed; watcher observations remain candidates; correction and rollback can carry stable identity.

**Costs:** every source requires descriptor, review, policy, activation, registry lineage, and re-review; every live connector requires authority resolution and destination enforcement; record-level minimum bars and compatibility aliases require maintenance.

Rejected alternatives include connector-local admission, descriptor validity as activation, fixture validity as authority, one global source rule set, activation stored only in PR prose, authority register alone as truth, a permissive plural schema, premature alias deletion, collapsing activation and watcher intake, post-admission rights review, AI-inferred authority, live-endpoint tests before fixture-first validation, and activation implying release.

<a id="non-goals"></a>

## Non-goals

This revision does not accept ADR-0017, change index status, alter contracts, schemas, validators, fixtures, tests, workflows, or policy, populate authority or registry records, activate or retire a source, access a live endpoint, modify connectors, evaluate live policy, write RAW or QUARANTINE, emit receipts or evidence, approve rights or sensitivity, release, deploy, publish, or change repository settings.

<a id="rollback-and-supersession"></a>

## Rollback and supersession

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the documentation commit through a reviewed corrective pull request or restore prior blob `58693830fcdf9746c5494fdd85298529fa5594a9`. Do not rewrite shared history.

Future implementation waves must record migrations, prior versions, rollback targets, connector-disable paths, policy-bundle rollback, affected digests, downstream invalidation, and correction or withdrawal obligations. A material decision change requires a successor ADR, reciprocal supersession links, and retention of this record as governance history.

## References

- [`docs/adr/INDEX.md`](./INDEX.md)
- [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md)
- [`docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`](../sources/SOURCE_DESCRIPTOR_STANDARD.md)
- [`docs/sources/ADMISSION_PROCESS.md`](../sources/ADMISSION_PROCESS.md)
- [`contracts/source/source_descriptor.md`](../../contracts/source/source_descriptor.md)
- [`contracts/source/source_activation_decision.md`](../../contracts/source/source_activation_decision.md)
- [`contracts/source/source_intake_record.md`](../../contracts/source/source_intake_record.md)
- [`schemas/contracts/v1/source/source_descriptor.schema.json`](../../schemas/contracts/v1/source/source_descriptor.schema.json)
- [`schemas/contracts/v1/sources/source_descriptor.schema.json`](../../schemas/contracts/v1/sources/source_descriptor.schema.json)
- [`schemas/contracts/v1/source/source_activation_decision.schema.json`](../../schemas/contracts/v1/source/source_activation_decision.schema.json)
- [`control_plane/source_authority_register.yaml`](../../control_plane/source_authority_register.yaml)
- [`data/registry/sources/README.md`](../../data/registry/sources/README.md)
- [`packages/source-registry/README.md`](../../packages/source-registry/README.md)
- [`policy/source/README.md`](../../policy/source/README.md)
- [`policy/intake/README.md`](../../policy/intake/README.md)

## Change ledger

Retained the ADR identity, proposed status, exact operating phrase, descriptor-versus-record distinction, rights/sensitivity/role/cadence/citation/source-head requirements, connector and watcher non-publisher invariant, fail-closed posture, rollback, consequences, alternatives, and open gates.

Corrected stale claims about plural schema authority, validator availability, descriptor path conflict, and absent activation profile. Added current evidence, `SourceIntakeRecord` anti-collapse boundary, admission layers, maturity, implementation sequence, and status-bearing acceptance gates. No implementation or publication behavior changed.

**Decision remains `proposed`.**

[Back to top](#top)
