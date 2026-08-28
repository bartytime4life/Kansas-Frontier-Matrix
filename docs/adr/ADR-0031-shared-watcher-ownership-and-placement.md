<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0031
title: "ADR-0031 — Shared Watcher Ownership and Placement"
type: adr
version: v1.1
status: proposed
effective_decision_status: proposed
owners:
  - "OWNER_TBD — architecture decision owner"
  - "OWNER_TBD — pipeline and watcher steward"
  - "OWNER_TBD — source/evidence steward"
  - "OWNER_TBD — affected domain stewards"
owner_status: "CODEOWNERS routes affected paths to @bartytime4life; accepted stewardship, independent review, source activation, and release authority remain unverified"
created: 2026-08-08
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
owning_root: docs/
responsibility: "Record the proposed ownership and placement split for watcher registries, declarative specifications, shared and domain executable orchestration, connectors, helpers, candidate outputs, migration, and rollback without granting source activation, execution, lifecycle-write, release, notification, publication, deployment, or repository-settings authority."
current_path: docs/adr/ADR-0031-shared-watcher-ownership-and-placement.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: b7352aba93f7298bdd5a6ee6fd8de475b05c9e42
  target_prior_blob: 8cffe2917e9d9646ef1ddd62d5cdda3331b50ac0
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  watcher_registry_blob: 03eaa309c5aac01f7755e7f1df4f04073bf1ad0f
  soil_watcher_spec_blob: e592a06765ce9f2a61aef50ae8f20b2f5d9d6209
  last_green_registry_run: 31263074530
  latest_registry_run: 31654972163
related:
  - docs/adr/INDEX.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - pipelines/watchers/README.md
  - pipelines/domains/flora/watchers/README.md
  - pipeline_specs/watchers/README.md
  - pipeline_specs/watchers/soil_ssurgo_gnatsgo.json
  - tools/watchers/README.md
  - contracts/source/watcher_registry.md
  - schemas/contracts/v1/source/watcher_registry.schema.json
  - control_plane/watcher_registry.json
  - tools/validators/validate_watcher_registry.py
  - tests/validators/test_validate_watcher_registry.py
  - .github/workflows/watcher-registry.yml
  - data/receipts/generated/genrec-watcher-registry-soil-extension-20260808.json
tags: [adr, kfm, pipelines, watchers, watcher-registry, non-publisher, placement]
notes:
  - "Same-path documentation-only reconciliation; ADR-0031 remains proposed and no migration is authorized."
  - "A fixture-first WatcherRegistry packet and inactive Soil watcher specification exist; no shared executable watcher runtime is confirmed."
  - "Latest focused registry logic passed before generated-receipt validation failed with ARTIFACT_DIGEST_MISMATCH."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0031 — Shared Watcher Ownership and Placement

> **Proposed decision.** KFM separates watcher responsibilities by ownership: `control_plane/` indexes watcher identity and non-authority state; `pipeline_specs/` declares intent; `pipelines/` owns executable orchestration; domain lanes own domain meaning; `connectors/` own approved upstream access; and `tools/` owns bounded helpers and validators. Shared executable placement requires proven reuse. Watchers remain candidate producers and non-publishers.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![Registry: partial](https://img.shields.io/badge/registry-PARTIAL-0969da?style=flat-square)](#evidence)
[![Shared runtime: absent](https://img.shields.io/badge/shared%20runtime-ABSENT-6e7781?style=flat-square)](#evidence)
[![Receipt: hold](https://img.shields.io/badge/receipt-HOLD-b42318?style=flat-square)](#evidence)

> [!IMPORTANT]
> ADR-0031 remains `proposed`. ADR-0029 separately accepted Directory Rules v2. The current registry and Soil specification neither accept this ADR nor grant source activation, scheduling, lifecycle-write, release, notification, or publication authority.

> [!CAUTION]
> `pipeline_specs/watchers/soil_ssurgo_gnatsgo.json` is Soil-specific through its contract, policy, source families, and outputs. Its shared-lane path is migration evidence, not authority to move it in this documentation-only update.

**Quick navigation:** [Status](#status) · [Context](#context) · [Evidence](#evidence) · [Decision](#decision) · [Admission](#admission) · [Non-authority](#non-authority) · [Graduation](#graduation) · [Migration](#migration) · [Validation](#validation) · [Open work](#open-questions)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| ADR ID / path | `ADR-0031`; `docs/adr/ADR-0031-shared-watcher-ownership-and-placement.md` |
| Source / effective status | `proposed` / `proposed` |
| Placement authority | Accepted ADR-0029 and its pinned Directory Rules v2 bytes |
| Repository posture | Registry packet present; inactive Soil packet present; shared executable runtime absent; declarative placement partly conflicted; receipt closure stale |
| Evidence checkpoint | `main@b7352aba93f7298bdd5a6ee6fd8de475b05c9e42` |
| Migration / publication effect | None while proposed |

Acceptance would establish responsibility and migration rules only. It would not activate a source, authorize network or credentials, schedule execution, create RAW state, resolve evidence, approve policy, release an artifact, notify the public, or publish a claim.

---

<a id="context"></a>

## Context

KFM has watcher-shaped surfaces under shared pipelines, domain pipelines, declarative specs, tools, contracts, schemas, control-plane registry, tests, workflows, and receipts. Without an explicit ownership rule, documentation, intent, execution, source access, domain semantics, validation, lifecycle writes, and release authority can collapse into one ambiguous “watcher” bucket.

**CONFIRMED:** `pipelines/watchers/` contains documentation but no direct executable at the evidence checkpoint; domain watcher documentation exists; shared and Flora plants placeholders coexist; an inactive shared gate profile and inactive Soil specification exist; the WatcherRegistry contract/schema/projection/validator/tests/workflow exist; registry authority flags are false; focused registry logic passed before receipt validation failed.

**PROPOSED:** the ownership matrix, shared-admission test, domain-spec migration, duplicate-placeholder retirement, and graduation gates below.

**UNKNOWN:** an accepted shared executable, scheduler, live source activation, production run, watcher-generated EvidenceBundle or release object, independent decision quorum, and unseen external consumers.

**NEEDS VERIFICATION:** the complete watcher inventory, real consumers of the generic gate profile, and whether later bytes repaired the receipt mismatch without a new watcher run.

---

<a id="evidence"></a>

## Repository and hosted evidence

| Surface | Verified state | Bounded meaning |
|---|---|---|
| `pipelines/watchers/` | README plus plants documentation; no direct executable | Candidate shared runtime owner only |
| `pipelines/domains/flora/watchers/` | Domain README | Supports domain ownership; does not prove execution |
| `tools/watchers/` | Helper/compatibility documentation | Helpers only; no scheduler or hidden fetch |
| Shared and Flora plants specs | Separate placeholders | Duplicate concept; canonical owner unresolved |
| `watcher_gate_profile.v1.json` | `PROPOSED_INACTIVE`, governance false | Shared profile candidate; consumers unproved |
| `soil_ssurgo_gnatsgo.json` | Fixture-only; network denied; WORK/QUARANTINE outputs | Substantive domain spec in a conflicted shared lane |
| WatcherRegistry packet | Contract, closed schema, projection, validator, fixtures, tests, workflow | Index and enforceability proof only; not runtime or activation |
| Registry-extension receipt | Stale against current first artifact bytes | Rebind before current byte closure is claimed |

Run `31263074530` is the last observed green watcher-registry run. Run `31654972163` passed five focused tests plus registry and fixture-polarity validation, then failed generated-receipt validation with `ARTIFACT_DIGEST_MISMATCH`. Current classification is **logic PASS / receipt HOLD**.

---

<a id="decision"></a>

## Decision

If accepted, KFM uses this ownership split:

| Responsibility | Owning surface | Boundary |
|---|---|---|
| Decision record | `docs/adr/` | Rationale and status only |
| Watcher index | `control_plane/watcher_registry.json` | Identity, state, references, outputs, exact spec binding, non-authority flags; no execution |
| Registry meaning / shape | `contracts/source/` / `schemas/contracts/v1/source/` | Contract and machine shape only |
| Shared declarative intent | `pipeline_specs/watchers/` | Only meaning genuinely shared across accepted lanes |
| Domain declarative intent | Lowest verified `pipeline_specs/<domain>/...` lane | Domain source roles, materiality, policy, sensitivity, outputs, reason codes, reviewers |
| Shared executable orchestration | `pipelines/watchers/` | Only after the shared-admission test passes |
| Domain executable behavior | `pipelines/domains/<domain>/watchers/` | Domain interpretation and domain-specific gates |
| Upstream access | `connectors/` | Approved endpoint, authentication, transport, retries, source capture |
| Reusable helper / validation | `tools/watchers/` and `tools/validators/` | Bounded helpers and checks; no scheduler, hidden fetch, or lifecycle authority |
| Candidate/process memory | Governed WORK, QUARANTINE, and receipt surfaces | No direct catalog, published, release, or notification write |
| Release/correction/rollback | `release/` | Separate reviewed transition outside watcher authority |

A watcher is domain-owned when source-role interpretation, materiality, rights, sovereignty, sensitivity, harmful precision, output contract, reason codes, reviewer class, or correction behavior is domain-specific. Shared placement follows shared responsibility, not a shared-looking filename.

`packages/` admission requires two verified executable consumers, a stable API and owner, compatibility tests, and retirement of competing homes.

---

<a id="admission"></a>

## Shared-admission test

`pipelines/watchers/` may receive executable code only when every gate passes:

| Gate | Requirement | Failure outcome |
|---|---|---|
| S1 | Two accepted executable consumers in distinct source or domain lanes | `DOMAIN_OWNED` or `HOLD` |
| S2 | No embedded domain source-role, sensitivity, policy, output, or reviewer semantics | `DOMAIN_OWNED` |
| S3 | Materiality profiles, outputs, and extensions are versioned inputs | `HOLD` |
| S4 | No-network fixtures prove no-change, change, malformed, stale, hold, and replay behavior | `HOLD` |
| S5 | Finite outcomes route only to allowed candidate/process-memory surfaces | `HOLD` or `DENY` |
| S6 | Checks deny direct catalog, published, release, and notification paths | `DENY` |
| S7 | Current spec, policy, fixtures, implementation, and outputs are receipt-bound | `HOLD` |
| S8 | No competing active executable owner remains | `MIGRATE` or `HOLD` |

Docs, specs, registry rows, proposed consumers, and generic profiles do not satisfy S1. Passing S1–S8 establishes placement fitness only, not activation or production authority.

---

<a id="non-authority"></a>

## Watcher non-authority law

Allowed bounded outcomes include `NO_CHANGE`/`NO_ACTION` with a receipt, `CHANGE_CANDIDATE` routed to WORK, `HOLD`/`ABSTAIN`/`QUARANTINE` with reason codes, or `ERROR` with auditable failure memory.

```text
registry row != source registry or activation
specification != executable authority
source changed != domain truth changed
candidate != EvidenceBundle or PolicyDecision
RunReceipt != ProofPack, PromotionDecision, or ReleaseManifest
green workflow != activation, release, notification, or publication
commit, PR, merge, deployment, map, or AI text != KFM publication
```

A watcher may route candidates to WORK or QUARANTINE through governed interfaces. It may not impersonate connector RAW capture and may never write CATALOG, TRIPLET, PUBLISHED, or release state directly.

### Consequences and alternatives

This split keeps responsibility inspectable, preserves domain meaning, and prevents the registry or tools from becoming hidden runtime authority. It also means small domain watchers may duplicate limited code until real reuse is proved, and acceptance alone will not resolve the plants or Soil placement conflicts.

Rejected alternatives: put every watcher under `tools/watchers/`; put every watcher under `pipelines/watchers/`; require every watcher to remain domain-local forever; or let the registry activate and schedule watchers.

---

<a id="graduation"></a>

## Graduation gates

| Gate | Required evidence | Current state |
|---|---|---|
| G0 | ADR and index carry matching reviewed `accepted` status | `PROPOSED` |
| G1 | Complete executable/spec/helper/consumer/receipt inventory | `NEEDS VERIFICATION` |
| G2 | One canonical executable and declarative owner per watcher | `CONFLICTED` for plants and Soil placement |
| G3 | Two real consumers for shared execution/package placement | `ABSENT` |
| G4 | Registry, contracts, schemas, policy refs, outputs, IDs, and exact spec bytes close | `PARTIAL` |
| G5 | Deterministic positive, negative, hold, stale, replay, and correction tests | `PARTIAL` |
| G6 | Non-publisher enforcement and current receipt binding | `HOLD` |
| G7 | Migration, references, compatibility, correction, rollback, and exact-head CI close | `NOT STARTED` |
| G8 | Activation, network, credentials, scheduling, operations, and release stay separate | Preserved; no activation |

A fixture-first domain watcher may graduate in its domain lane without waiting for shared admission, provided domain gates pass and it does not claim shared ownership.

---

<a id="migration"></a>

## Migration and rollback

> **HOLD while this ADR is proposed.** This edition changes documentation only.

After acceptance, a separate dependency-closed PR must inventory watcher surfaces, classify each by responsibility, choose one plants spec, decide the Soil spec home, update registry paths/digests and workflow filters atomically, repair links and receipts, test the generic profile against real consumers, prove WORK/QUARANTINE-only outputs, run focused and exact-head checks, and record compatibility and rollback before retiring any path.

No live source, credentials, network schedule, public alert, release, deployment, or publication belongs in that migration PR.

Before acceptance, rollback is closing or reverting this documentation PR. After a later migration, rollback must restore prior routing, registry paths/digests, workflow filters, links, tests, and receipts without reintroducing two writable authorities or deleting relied-on history.

---

<a id="validation"></a>

## Validation

For this same-path documentation update:

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
```

Also verify one changed file, one H1, unique explicit anchors, resolved quick-navigation links, unchanged ADR identity/status/supersession, valid relative links, and no claim that this update performed migration or runtime work.

Later implementation must add watcher-registry and domain tests, policy-boundary checks, generated-receipt validation, topology checks, and exact-head workflows. Migration is incomplete while receipt or consumer closure is red.

---

<a id="open-questions"></a>

## Open questions

- Which first two executable consumers can prove real shared reuse?
- Should the Soil spec move to a Soil watcher sublane or split into a shared comparison profile plus domain wrapper?
- Is `watcher_gate_profile.v1.json` truly cross-domain?
- What accepted object represents watcher activation without turning the registry into activation authority?
- What scheduler/worker boundary is appropriate after fixture-first proof and operational ownership exist?
- Which rights, sovereignty, sensitivity, security, and harmful-precision gates block the first live activation?
- Which hosted checks must become required before executable watcher code is admitted?

## References

- [`docs/adr/README.md`](./README.md) and [`INDEX.md`](./INDEX.md)
- [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules](../doctrine/directory-rules.md)
- [`pipelines/watchers/README.md`](../../pipelines/watchers/README.md)
- [`pipelines/domains/flora/watchers/README.md`](../../pipelines/domains/flora/watchers/README.md)
- [`tools/watchers/README.md`](../../tools/watchers/README.md)
- [`pipeline_specs/watchers/README.md`](../../pipeline_specs/watchers/README.md)
- [`contracts/source/watcher_registry.md`](../../contracts/source/watcher_registry.md)
- [`control_plane/watcher_registry.json`](../../control_plane/watcher_registry.json)
- [`tools/validators/validate_watcher_registry.py`](../../tools/validators/validate_watcher_registry.py)
- [`.github/workflows/watcher-registry.yml`](../../.github/workflows/watcher-registry.yml)

The attached KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0 controls the implementation method for this update; it is not repository evidence and does not accept the ADR.

## No-loss reconciliation

v1.1 preserves the original shared-pipeline proposal, domain watcher ownership, shared/domain spec split, helper-only tools boundary, non-publisher law, consequences, alternatives, migration HOLD, rollback, and open questions. It adds the accepted Directory Rules relationship, WatcherRegistry implementation, inactive Soil packet, placement conflicts, logic/receipt distinction, admission and graduation gates, and current migration controls.

## Change history

| Date | Edition | Change |
|---|---|---|
| 2026-08-08 | v1 | Initial proposed watcher ownership and placement decision. |
| 2026-08-14 | v1.1 | Repository-grounded reconciliation; decision remains proposed. |
