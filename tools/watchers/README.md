<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-watchers-readme
title: tools/watchers README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-watcher-steward-plus-source-steward-plus-domain-stewards-plus-rights-steward-plus-sensitivity-reviewer-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; watcher-root-index; source-drift; source-head-aware; SourceIntakeRecord-aware; non-publisher; no-public-path; rights-aware; sensitivity-aware; cadence-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: parent watcher routing README under tools/watchers; indexes KFM watcher lanes and documents non-publisher expectations for source drift detection, source descriptor activation, source role preservation, rights and sensitivity gates, cadence/freshness checks, source-head capture, source-intake candidate output, steward summaries, quarantine/review routing, validation handoff, policy/review triggers, correction and rollback references, fixture/test routing, and finite outcomes while deferring source registry authority, domain meaning, taxonomy authority, evidence records, receipts, lifecycle data, validation authority, policy decisions, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - plants_watch/README.md
  - ../validators/README.md
  - ../validators/source/README.md
  - ../validators/source_descriptor/README.md
  - ../validators/source_role/README.md
  - ../validators/rights/README.md
  - ../validators/sensitivity/README.md
  - ../validators/policy/README.md
  - ../validators/evidence/README.md
  - ../validators/release/README.md
  - ../validators/promotion_gate/README.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../docs/domains/flora/SOURCE_INTAKE.md
  - ../../docs/domains/flora/FILE_SYSTEM_PLAN.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/work/
  - ../../data/quarantine/
  - ../../data/proofs/
  - ../../data/receipts/
  - ../../policy/
  - ../../release/
  - ../../fixtures/
  - ../../tests/
notes:
  - "This README replaces an empty placeholder at tools/watchers/README.md. It does not confirm executable watcher scripts, scheduler wiring, source activation records, network access, generated SourceIntakeRecord outputs, receipt emission, runtime behavior, or CI behavior."
  - "Watchers detect change. They do not declare truth, admit sources, create EvidenceBundles, decide policy, approve release, publish artifacts, write catalog/triplet/published data, or authorize public API/UI/map/AI surfaces."
  - "A watcher run may produce intake evidence and a reviewable candidate. It must remain downstream from SourceDescriptor activation and upstream from substantive validation, evidence closure, policy review, release, correction, and rollback."
  - "No watcher should write past the accepted RAW/WORK/QUARANTINE candidate/report boundary unless an explicitly governed pipeline step, validator, policy decision, and release process takes over in the correct root."
  - "Sensitive joins, source-rights changes, stale cadence, ambiguous source-head signals, and public-surface risks must fail closed or route to steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/watchers

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-watcher--root--index-informational)
![posture](https://img.shields.io/badge/posture-non--publisher-critical)
![boundary](https://img.shields.io/badge/boundary-candidate--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/watchers/` is the parent routing surface for KFM watchers: side-effect-limited change detectors that observe source-head or drift signals and emit reviewable candidates without becoming source authority, domain truth, evidence authority, policy authority, release authority, or public publishers.

---

## Purpose

`tools/watchers/` exists to organize watcher lanes under the durable `tools/` responsibility root.

The durable KFM question for this root is:

> Did an admitted source, package, feed, archive, dataset, registry, layer, status table, or external reference appear to change, and can that change be recorded as reviewable intake evidence without declaring truth, bypassing activation, leaking sensitive data, or writing beyond governed candidate/hold lanes?

A watcher may help decide whether a pipeline should be alerted. It does not decide whether the changed source is admissible, true, policy-allowed, evidence-closed, release-ready, or public-safe.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/watchers/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `tools/watchers/plants_watch/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Child watcher lane for Flora plant-source drift, especially PLANTS taxa drift and adjacent source-head checks. |
| `docs/domains/flora/SOURCE_REGISTRY.md` | **CONFIRMED source-registry doctrine / implementation NEEDS VERIFICATION** | Defines watcher-as-non-publisher gates, Flora watcher families, SourceIntakeRecord candidate posture, and source-head evidence limits. |
| `docs/domains/flora/FILE_SYSTEM_PLAN.md` | **CONFIRMED placement doctrine / implementation NEEDS VERIFICATION** | Proposes watcher/spec/test/fixture placement, including PLANTS drift watcher specs and fixtures. |
| Executable watcher scripts, scheduler integration, source activation records, network policy, fixture coverage, generated summaries, SourceIntakeRecord emission, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This root README is documentation only. |

[Back to top](#top)

---

## Watcher root rules

| Rule | Watcher posture | Forbidden shortcut |
|---|---|---|
| Detect change only | A watcher observes source-head, hash, ETag, timestamp, package, count, status, or set-difference signals. | Declaring the changed content true, admissible, or publishable. |
| Activation first | Watchers run only for admitted and activated sources, or in explicit no-network fixture mode. | Fetching from unactivated sources or bypassing descriptor gates. |
| Candidate output only | Watchers emit reviewable candidates such as `SourceIntakeRecord`, steward summaries, or report artifacts. | Writing directly to `processed/`, `catalog/`, `triplets/`, `published/`, `release/`, public maps, public APIs, or AI answer surfaces. |
| Source-head is weak evidence | HEAD/ETag/Last-Modified/content-length/source-hash signals are intake evidence. | Treating source-head as substantive validation, rights clearance, policy approval, or release readiness. |
| Preserve source roles | Source role comes from governed admission records. | Role invention by AI, source popularity, file name, URL, or watcher label. |
| Preserve rights and sensitivity | Rights, license, attribution, consent, sensitivity, geoprivacy, and public-surface posture must be checked before downstream use. | Assuming source availability means public reuse. |
| Recompute joined sensitivity | Watcher deltas joined to other source families or precise locations become new products with their own sensitivity. | Inheriting the weakest input sensitivity for a joined product. |
| Steward-readable outputs | Machine deltas should have human-readable summaries when review is needed. | Opaque diffs with no steward-actionable explanation. |
| Fail closed | Missing descriptors, activation, cadence, baseline, rights, sensitivity, evidence, policy, release, correction, or rollback support routes to hold/deny/review. | Silent pass or best-effort public continuation. |

[Back to top](#top)

---

## Watcher lifecycle boundary

Watcher output sits before normal validation and publication gates.

```text
External source signal
  -> watcher source-head / drift check
  -> SourceIntakeRecord or equivalent candidate
  -> RAW / WORK / QUARANTINE candidate or report lane
  -> validators, evidence closure, policy review, sensitivity review
  -> governed pipeline promotion
  -> CATALOG / TRIPLET
  -> release decision
  -> PUBLISHED public-safe artifact
```

A watcher must not collapse that chain. If a watcher discovers a change that seems obvious, the safe output is still a candidate and review trail, not a published artifact.

[Back to top](#top)

---

## Known watcher lanes

| Lane | Scope | Status |
|---|---|---|
| [`plants_watch/`](plants_watch/README.md) | Flora plant-source drift detection, especially PLANTS taxa drift and adjacent source-head checks. | **CONFIRMED README / executable behavior NEEDS VERIFICATION** |

Future watcher lanes should be added only when their source family, activation gates, cadence, allowed source-head signal, output envelope, fixture mode, validation handoff, policy/review path, correction/rollback posture, and public-surface denial rules are explicit.

[Back to top](#top)

---

## Watcher input packet

A watcher run should have explicit inputs before it runs.

| Input family | Required posture | Fail-closed condition |
|---|---|---|
| Source descriptor | Source descriptor ref, source role, rights, sensitivity, cadence, access method, contact/steward, and admissibility limits are present. | Missing descriptor or unresolved source posture. |
| Activation decision | Watcher/connector activation is allowed, restricted, denied, or needs-review. | No activation record, denied activation, or incompatible restriction. |
| Watch scope | Source family, geographic/thematic scope, version, baseline ref, allowed signal, and materiality posture are explicit. | Hidden baseline or ambiguous scope. |
| Source-head policy | Allowed source-head fields and capture method are declared. | Treating source-head as validation or release support. |
| Rights/sensitivity posture | Source-rights, attribution, consent, geoprivacy, join-induced sensitivity, and public-surface risks are known. | Rights/sensitivity unresolved. |
| Fixture mode | No-network fixture path or deterministic test posture exists. | Live-only behavior with no reproducible fixture. |
| Output destination | Candidate/report destination, steward-summary ref, and quarantine/review route are declared. | Any write to processed/catalog/published/release/public surfaces. |

[Back to top](#top)

---

## Watcher output expectations

| Output family | Expectation | Must not be treated as |
|---|---|---|
| Candidate envelope | SourceIntakeRecord or domain-equivalent candidate with source refs, source role, source-head, drift summary, review flags, and promotion-required posture. | Evidence closure or release readiness. |
| Source-head metadata | Hash, ETag, Last-Modified, content length, spec hash, captured-at, or equivalent when allowed. | Source acceptance or substantive validation. |
| Drift summary | Added/removed/changed records, count delta, timestamp delta, status delta, asset checksum delta, or schema/version delta. | Truth that the domain claim changed. |
| Review flags | Sensitive intersection, rights drift, cadence drift, schema drift, source-role conflict, materiality, stale baseline, or review-required markers. | Policy decision by itself. |
| Steward summary | Human-readable explanation and next-step routing. | Automated approval. |
| Report/receipt refs | Output references to accepted report/receipt locations where implemented. | Proof that the candidate is publishable. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Watcher routing/docs | `tools/watchers/` |
| Watcher child lanes | `tools/watchers/<watcher>/` |
| Validator checks | `tools/validators/` |
| Source doctrine | `docs/sources/`, domain source docs |
| Source descriptors and activation records | `data/registry/sources/`, accepted source registry/control-plane homes |
| Domain meaning | `docs/domains/`, `contracts/domains/` |
| Machine schemas | `schemas/contracts/v1/` and accepted schema homes |
| RAW/WORK/QUARANTINE candidate data | governed `data/` lifecycle roots |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Policy | `policy/` and accepted domain/sensitivity/rights policy homes |
| Release records, corrections, rollbacks | `release/` and accepted correction/rollback homes |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists at `tools/watchers/README.md`.
- **PROPOSED:** watcher code may live under `tools/watchers/` only when it is a side-effect-limited change detector with explicit source activation, no-publication behavior, fixtures, validation handoff, policy/review path, correction/rollback path, and public-surface denial.
- **NEEDS VERIFICATION:** executable files, scheduler integration, watcher registry ids, source activation records, network policy, fixture paths, SourceIntakeRecord schema, report destinations, receipt emission, runtime behavior, and CI wiring.
- **DENY:** using this tree as source registry, source admission authority, domain truth, taxonomy authority, EvidenceBundle store, policy home, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/watchers/` include:

- watcher-root and watcher-child README files;
- side-effect-limited watcher scripts that only detect source/head/drift signals and emit candidates;
- source-head capture helpers that write to accepted candidate/report destinations;
- drift comparison helpers that preserve source descriptor refs, source roles, baselines, versions, and cadence posture;
- steward-summary templates;
- no-network fixture-mode runner notes;
- watcher registry notes and finite outcome vocabularies;
- documentation that routes validation, evidence, policy, release, correction, rollback, fixtures, and tests to owning roots.

[Back to top](#top)

---

## What does not belong here

| Do not put in this tree | Correct home |
|---|---|
| Source descriptors, source activation records, source registry authority | `data/registry/sources/` and accepted control-plane/source registry homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads | governed `data/` lifecycle roots |
| Domain contracts or schemas | `contracts/`, `schemas/contracts/v1/` |
| Policy rules, rights decisions, sensitivity decisions, release decisions, steward approvals | `policy/`, `release/`, accepted governance homes |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Tests and fixtures | `tests/`, `fixtures/` conventions unless a local shim is explicitly accepted |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Secrets, source credentials, private source content, exact sensitive locations, hidden policy values, signing keys, or reconstruction hints | denied here |

[Back to top](#top)

---

## Standard watcher outcomes

| Outcome | Meaning |
|---|---|
| `WATCHER_NO_CHANGE` | Watcher ran and detected no material source-head or drift signal. |
| `WATCHER_CHANGE_CANDIDATE` | Watcher detected a change and emitted a reviewable candidate. |
| `WATCHER_RESTRICT` | Watcher may run only under stated restrictions. |
| `WATCHER_HOLD` | Candidate is held pending source, rights, sensitivity, policy, fixture, evidence, or steward review. |
| `WATCHER_DENY` | Watcher or candidate must not proceed. |
| `WATCHER_ABSTAIN` | Watcher lacks enough support to classify the signal. |
| `WATCHER_NEEDS_REVIEW` | Steward review is required before downstream use. |
| `WATCHER_SOURCE_DESCRIPTOR_MISSING` | Required source descriptor is missing or unresolved. |
| `WATCHER_SOURCE_ACTIVATION_MISSING` | Required watcher/connector activation decision is missing. |
| `WATCHER_SOURCE_RIGHTS_UNRESOLVED` | Rights, license, attribution, consent, or redistribution posture is unresolved. |
| `WATCHER_SOURCE_SENSITIVITY_UNRESOLVED` | Sensitivity, geoprivacy, private-location, cultural, infrastructure, or restricted-use posture is unresolved. |
| `WATCHER_CADENCE_OR_BASELINE_MISSING` | Cadence, source-head, baseline, version, or comparison target is missing. |
| `WATCHER_SOURCE_HEAD_ONLY_ABSTAIN` | Only weak source-head evidence exists; substantive validation is absent. |
| `WATCHER_STEWARD_SUMMARY_MISSING` | Candidate lacks a human-readable steward summary. |
| `WATCHER_PUBLISH_EDGE_DENIED` | Watcher attempted to write to processed/catalog/triplets/published/release/public surfaces. |
| `WATCHER_PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsupported or sensitive content to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `WATCHER_SYSTEM_ERROR` | Watcher could not complete because of malformed input, missing dependency, network/scheduler error, missing registry entry, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/watchers/
├── README.md
├── plants_watch/
│   └── README.md
├── _common/                         # PROPOSED; not confirmed
├── registry_notes.md                # PROPOSED; documentation only
└── <watcher_lane>/                   # PROPOSED; side-effect-limited watcher lanes
```

Do not add watcher code, scheduler configs, credentials, source payloads, source descriptors, policy bundles, release records, fixtures, or tests unless the placement decision is documented, the source activation boundary is explicit, and tests prove no-publication behavior.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/watchers/README.md`.
- [x] It marks this path as watcher routing, not source registry, source admission authority, domain truth, evidence authority, policy authority, release authority, public runtime, or AI authority.
- [x] It establishes the watcher-as-non-publisher invariant for all child lanes.
- [x] It preserves source descriptor activation, source-role, rights, sensitivity, cadence, source-head, SourceIntakeRecord/candidate, steward-summary, quarantine/review, validation, correction, rollback, and public-surface boundaries.
- [x] It routes source descriptors to `data/registry/sources/`, validation to `tools/validators/`, tests/fixtures to `tests/` and `fixtures/`, policy to `policy/`, evidence/receipts to `data/`, release records to `release/`, and public surfaces to governed runtime roots.
- [x] It marks executable scripts, scheduler integration, source activation records, network policy, fixtures, generated SourceIntakeRecords, reports, receipts, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Watcher registry, scheduler, CLI, or pipeline references are searched and classified.
- [ ] Source activation decision storage and candidate envelope schema homes are verified.
- [ ] No-network fixture conventions are verified.
- [ ] Tests prove no-change, change-candidate, deny, restrict, hold, abstain, needs-review, descriptor-missing, activation-missing, rights-unresolved, sensitivity-unresolved, baseline-missing, steward-summary-missing, publish-edge-denied, and public-surface-blocked cases.
- [ ] CI or scheduled runs prove watchers cannot write beyond accepted intake/hold/report destinations.
- [ ] Any generated watcher outputs write only to accepted report, candidate, proof, receipt, artifact, or quarantine/review homes.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with watcher-root README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
