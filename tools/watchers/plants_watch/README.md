<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-watchers-plants-watch-readme
title: tools/watchers/plants_watch README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-flora-steward-plus-source-steward-plus-watcher-steward-plus-rights-steward-plus-sensitivity-reviewer-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; plants-watch; flora-watcher; source-drift; USDA-PLANTS-aware; taxa-drift-aware; SourceIntakeRecord-aware; source-head-aware; non-publisher; no-public-path; rights-aware; sensitivity-aware; geoprivacy-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: plants watcher README under tools/watchers; documents watcher expectations for Flora plant-source drift detection, especially PLANTS taxa drift and related plant source-head checks, source descriptor activation, source role preservation, rights and sensitivity gates, cadence and freshness checks, source-head capture, set-difference summaries, join-induced sensitivity warnings, steward summary generation, SourceIntakeRecord candidate output, quarantine/no-public-path routing, policy/review triggers, correction and rollback references, fixture/test routing, and finite outcomes while deferring source registry authority, Flora meaning, taxonomy authority, evidence records, receipts, lifecycle data, validation authority, policy decisions, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../validators/README.md
  - ../../validators/source/README.md
  - ../../validators/source_descriptor/README.md
  - ../../validators/source_role/README.md
  - ../../validators/rights/README.md
  - ../../validators/sensitivity/README.md
  - ../../validators/geoprivacy/README.md
  - ../../validators/taxonomy_resolver/README.md
  - ../../validators/vegetation_community/README.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../../docs/domains/flora/SOURCES.md
  - ../../../docs/domains/flora/SOURCE_INTAKE.md
  - ../../../docs/domains/flora/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../docs/domains/flora/CROSSWALKS.md
  - ../../../docs/runbooks/flora/SOURCE_REFRESH_RUNBOOK.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/flora/
  - ../../../data/raw/flora/
  - ../../../data/work/flora/
  - ../../../data/quarantine/flora/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../release/
  - ../../../fixtures/domains/flora/sources/
  - ../../../fixtures/domains/flora/plants_drift/
  - ../../../tests/domains/flora/no_network/
  - ../../../tests/domains/flora/source_descriptor/
notes:
  - "This README replaces an empty placeholder at tools/watchers/plants_watch/README.md. It does not confirm executable watcher scripts, scheduler wiring, network access, source activation records, fixture coverage, generated SourceIntakeRecord outputs, receipt emission, runtime behavior, or CI behavior."
  - "A watcher detects change; it does not declare Flora truth, admit a source, create EvidenceBundles, decide policy, publish artifacts, write catalog/triplet/published data, or authorize public API/UI/map/AI surfaces."
  - "The Flora source registry documents PLANTS taxa drift as a confirmed design and proposed implementation. This README preserves that boundary and does not assert the watcher is implemented."
  - "Watcher success means only that a source-head or drift signal was observed. It is intake evidence, not substantive validation, rights clearance, sensitivity clearance, evidence closure, policy approval, release approval, or publication readiness."
  - "PLANTS taxa drift can become sensitivity-prone when joined with occurrence, listing, herbarium, iNaturalist, GBIF, KDWP, USFWS, or other sensitive plant context. Sensitive intersections must route to review and must not expose exact or reconstructable locations."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/watchers/plants_watch

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-plants--watcher-informational)
![posture](https://img.shields.io/badge/posture-non--publisher-critical)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/watchers/plants_watch/` is the watcher lane for Flora plant-source drift detection, especially PLANTS taxa drift and adjacent plant source-head checks, emitting reviewable source-intake candidates without becoming source authority, Flora truth, evidence authority, policy authority, release authority, or a public publisher.

---

## Purpose

`tools/watchers/plants_watch/` exists to document the safe operating boundary for plant-source watchers.

The durable KFM question for this lane is:

> Did a governed plant source appear to change, and can that change be recorded as a reviewable `SourceIntakeRecord` candidate without declaring truth, bypassing source activation, weakening source roles, exposing sensitive plant context, or writing beyond allowed intake/hold lanes?

The answer should be a small watcher output or a fail-closed routing decision. This folder should not create botanical truth, taxonomic authority, occurrence proof, source admission, EvidenceBundles, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/watchers/plants_watch/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `tools/watchers/README.md` | **NOT FOUND in this edit** | No parent watcher README was verified before creating this child README. |
| `docs/domains/flora/README.md` | **CONFIRMED Flora doctrine / implementation NEEDS VERIFICATION** | Flora governs plant identity, occurrences, vegetation communities, sensitive flora controls, public-safe outputs, correction, and rollback. |
| `docs/domains/flora/SOURCE_REGISTRY.md` | **CONFIRMED source-registry doctrine / implementation NEEDS VERIFICATION** | Defines Flora source admission, watcher-as-non-publisher gates, PLANTS taxa drift design, SourceIntakeRecord candidate posture, and source-head evidence limits. |
| `docs/domains/flora/FILE_SYSTEM_PLAN.md` | **CONFIRMED placement doctrine / implementation NEEDS VERIFICATION** | Proposes watcher/spec/test/fixture placement for Flora, including PLANTS drift watcher specs and fixtures. |
| Executable watcher scripts, schedule triggers, source activation records, network policy, fixture coverage, generated summaries, SourceIntakeRecord emission, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Watcher posture

A watcher is a **change detector**, not a publisher.

| Watcher may do | Watcher must not do |
|---|---|
| Check an activated Flora source according to its descriptor, cadence, and allowed signal. | Fetch from unactivated sources or bypass rights/sensitivity gates. |
| Capture source-head metadata such as content hash, ETag, Last-Modified, content length, spec hash, and capture time where permitted. | Treat source-head metadata as substantive validation or source acceptance. |
| Compare a current source package, checklist, feed, archive, snapshot, or STAC item against a prior governed baseline. | Declare the new source content admissible, true, or publishable. |
| Emit a `SourceIntakeRecord` candidate with `publication_state = WORK_CANDIDATE` and `promotion_required = true`. | Write directly to `processed/`, `catalog/`, `triplets/`, `published/`, public maps, public APIs, or AI answer surfaces. |
| Produce a steward-readable markdown summary explaining the drift signal. | Emit only opaque machine deltas with no human review surface. |
| Route sensitive or ambiguous changes to quarantine/review. | Join sensitive taxa with exact occurrence or private-location data for public display. |

[Back to top](#top)

---

## Expected watch families

| Watch family | Signal | Safe output | Status |
|---|---|---|---|
| PLANTS taxa drift | Taxa added/removed under a stable taxonomy/version and declared geographic scope. | `SourceIntakeRecord` candidate plus steward summary. | **CONFIRMED design / PROPOSED implementation** |
| Herbarium snapshot drift | Archive timestamp, package digest, record-count delta, or new taxa signal. | Per-institution `SourceIntakeRecord` candidate. | **PROPOSED** |
| GBIF/iDigBio/iNaturalist Flora deltas | Dataset/snapshot/hash/range/count delta for admitted Flora scope. | Source-scoped `SourceIntakeRecord` candidate. | **PROPOSED** |
| USFWS/KDWP/NatureServe status drift | Listing/rank/status revision signal for plant taxa. | `SourceIntakeRecord` candidate plus sensitivity recompute trigger. | **PROPOSED** |
| Vegetation index/STAC drift | STAC item update, asset checksum, or collection update. | Modeled-role source-intake candidate. | **PROPOSED** |

[Back to top](#top)

---

## Required input packet

A plant watcher run should have explicit, reviewable inputs before it runs.

| Input family | Required posture | Fail-closed condition |
|---|---|---|
| Source descriptor | Source descriptor ref, source role, rights, sensitivity, cadence, access method, contact/steward, and admissibility limits are present. | Missing or inactive descriptor. |
| Activation decision | Connector/watcher activation is allowed, restricted, denied, or needs-review. | No activation decision or denied activation. |
| Watch scope | Source family, taxon scope, geography scope, version/snapshot, baseline ref, and allowed signal are explicit. | Ambiguous scope or hidden baseline. |
| Source-head policy | Allowed source-head fields and capture method are declared. | Using source-head checks as validation or publication support. |
| Sensitivity posture | Sensitive taxa, join-induced sensitivity, rare/protected/culturally sensitive flora, and private-location risks are acknowledged. | Sensitive intersection without review route. |
| Fixture mode | No-network fixture path or test fixture posture exists for deterministic tests. | Live-only behavior with no reproducible fixture. |
| Output destination | Candidate queue, WORK/QUARANTINE route, steward summary ref, and report path are declared. | Any write to processed/catalog/published/public surfaces. |

[Back to top](#top)

---

## SourceIntakeRecord expectations

A watcher output should be a candidate envelope, not a truth claim.

| Field family | Expectation | Must not be treated as |
|---|---|---|
| Source refs | `source_descriptor_ref`, source role, source id, source family, and source activation context. | Evidence that source claims are true. |
| Publication posture | Candidate remains `WORK_CANDIDATE` or equivalent and `promotion_required` remains true. | Publication approval. |
| Drift summary | Added/removed/changed taxa, count deltas, status changes, version deltas, or source-head deltas are summarized. | Admitted Flora fact. |
| Sensitive intersection | Sensitive taxa, listed status, private-location, cultural, source-rights, or join-induced risk is flagged without exposing details. | Public-safe output by default. |
| Source-head | Digest/checksum/ETag/Last-Modified/content-length/spec-hash where permitted. | Substantive validation or rights approval. |
| Steward summary | Human-readable markdown summary for review. | Automated approval. |
| Review and routing | Policy review, sensitivity review, rights review, quarantine/review routing, correction, and rollback refs are present where required. | Release readiness by itself. |

[Back to top](#top)

---

## Non-publisher invariants

| Invariant | Watcher expectation | Fail / deny condition |
|---|---|---|
| Watchers detect change only | Watcher output is intake evidence and candidate routing. | Watcher declares Flora truth. |
| No direct promotion | Watcher does not write beyond allowed RAW/WORK/QUARANTINE candidate surfaces. | Watcher writes to processed, catalog, triplets, published, release, public map, public API, or AI surface. |
| Descriptor activation gates fetching | Source descriptors, rights, sensitivity, cadence, fixtures, validators, and no-publish edge are checked before activation. | Watcher runs against unactivated source. |
| Fetch success is not acceptance | HTTP success, ETag match, source-head delta, or checksum capture does not prove admissibility. | Watcher marks fetched content admissible or released. |
| Source roles remain fixed | Source role comes from descriptor/admission, not AI prose, popularity, or source name. | Watcher invents or upgrades source role. |
| Join sensitivity is recomputed | Taxa drift joined with occurrence/status/private/context sources is reviewed as a new product. | Input-level sensitivity is reused for a joined product. |
| Public sensitive geometry is denied | Exact rare-plant, culturally sensitive, private-land, or reconstructable plant-location context never leaves steward/review lanes. | Output includes exact/reconstructable sensitive location detail. |
| Steward summary is required | Machine diff is paired with human-readable review summary. | Delta has no steward-actionable explanation. |

[Back to top](#top)

---

## Fail-closed conditions

A plant watcher candidate should fail closed, deny, restrict, hold, abstain, or route to steward review when:

- source descriptor, source activation decision, source role, rights, sensitivity, cadence, access method, attribution, or steward contact is missing;
- the source is inactive, denied, rights-limited, sensitivity-limited, stale, unreachable, contradictory, or outside declared watch scope;
- source-head metadata is missing where required or is treated as substantive validation;
- baseline package, taxonomy version, snapshot id, source digest, or prior comparison target is missing;
- added/removed taxa intersect rare/protected/culturally sensitive/private-location/source-restricted context;
- a drift output would enable poaching, private-land inference, rare-habitat reconstruction, or sensitive taxa triangulation;
- the watcher attempts to write directly to processed, catalog, triplets, published, release, public map, public API, graph/search/export/Focus Mode, embedding, or AI-answer surfaces;
- the watcher emits no steward-readable summary;
- policy decision, rights review, sensitivity review, EvidenceRef/EvidenceBundle support, receipt, correction path, rollback target, or release reference is required but absent.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Plant watcher routing/docs | `tools/watchers/plants_watch/` |
| Watcher parent docs | `tools/watchers/README.md` — **NOT FOUND in this edit** |
| Source admission doctrine | `docs/domains/flora/SOURCE_REGISTRY.md`, `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` |
| Flora domain doctrine | `docs/domains/flora/` |
| Machine-readable Flora source descriptors | `data/registry/sources/flora/` |
| Watcher specs | `pipeline_specs/flora/` or accepted watcher/spec homes when verified |
| Executable pipeline logic | `pipelines/domains/flora/` or accepted tool/pipeline homes when verified |
| RAW/WORK/QUARANTINE candidate data | governed `data/` lifecycle roots |
| Validators | `tools/validators/`, `tests/`, `fixtures/` |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Policy | `policy/domains/flora/`, `policy/sensitivity/flora/`, accepted policy homes |
| Release records and rollback | `release/` |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** watcher code may live here only if it remains a non-publisher, side-effect-limited change detector and delegates source admission, evidence, validation, policy, release, data lifecycle, public runtime, and AI authority to owning roots.
- **NEEDS VERIFICATION:** executable files, scheduler integration, source activation records, network policy, no-network fixtures, baseline packages, taxonomy-version registry, SourceIntakeRecord schema, steward-summary destinations, report destinations, receipts, runtime behavior, and CI wiring.
- **DENY:** using this folder as source registry, botanical truth, taxonomy authority, occurrence proof, EvidenceBundle store, receipt store, policy home, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/watchers/plants_watch/` include:

- this README;
- small watcher scripts or shims that detect activated plant-source drift;
- source-head capture helpers that write only to accepted candidate/report destinations;
- PLANTS taxa-drift comparison helpers that preserve taxonomy version and baseline refs;
- steward-summary templates for drift review;
- no-network fixture runner notes;
- finite watcher outcome mapping;
- documentation that routes validation, evidence, policy, release, correction, rollback, fixtures, and tests to owning roots.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Source descriptors, source activation records, source registry authority | `data/registry/sources/flora/` and accepted source registry/control-plane homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads | governed `data/` lifecycle roots |
| Botanical/taxonomic contracts or schemas | `contracts/domains/flora/`, `schemas/contracts/v1/domains/flora/`, accepted source schemas |
| Policy rules, rights decisions, sensitivity decisions, release decisions, steward approvals | `policy/`, `release/`, accepted governance homes |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Tests and fixtures | `tests/`, `fixtures/` conventions unless a local shim is explicitly accepted |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Exact rare-plant locations, rare-habitat reconstruction hints, private stewardship details, cultural plant knowledge, source credentials, hidden redaction values, or production signing keys | denied here |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `PLANTS_WATCH_NO_CHANGE` | Watcher ran and detected no material source-head or drift signal. |
| `PLANTS_WATCH_CHANGE_CANDIDATE` | Watcher detected a change and emitted a reviewable candidate. |
| `PLANTS_WATCH_RESTRICT` | Watcher may run only under stated restrictions. |
| `PLANTS_WATCH_HOLD` | Candidate is held pending source, rights, sensitivity, policy, fixture, or steward review. |
| `PLANTS_WATCH_DENY` | Watcher or candidate must not proceed. |
| `PLANTS_WATCH_ABSTAIN` | Watcher lacks enough support to classify the signal. |
| `PLANTS_WATCH_NEEDS_REVIEW` | Steward review is required before downstream use. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor is missing or unresolved. |
| `SOURCE_ACTIVATION_MISSING` | Required watcher/connector activation decision is missing. |
| `SOURCE_RIGHTS_UNRESOLVED` | Rights, license, attribution, consent, or redistribution posture is unresolved. |
| `SOURCE_SENSITIVITY_UNRESOLVED` | Sensitivity, geoprivacy, rare/protected/cultural/private-location posture is unresolved. |
| `CADENCE_OR_BASELINE_MISSING` | Cadence, source-head, baseline, taxonomy version, or comparison target is missing. |
| `SENSITIVE_INTERSECTION_REVIEW_REQUIRED` | Drift intersects sensitive taxa or join-induced sensitivity requiring review. |
| `SOURCE_HEAD_ONLY_ABSTAIN` | Only weak source-head evidence exists; substantive validation is absent. |
| `STEWARD_SUMMARY_MISSING` | Candidate lacks a human-readable steward summary. |
| `WATCHER_PUBLISH_EDGE_DENIED` | Watcher attempted to write to processed/catalog/triplets/published/release/public surfaces. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsupported or sensitive Flora content to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `WATCHER_SYSTEM_ERROR` | Watcher could not complete because of malformed input, missing dependency, network/scheduler error, missing registry entry, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/watchers/plants_watch/
├── README.md
├── plants_watch.py                  # PROPOSED; not confirmed
├── compare_plants_taxa_drift.py     # PROPOSED; not confirmed
├── source_head.py                   # PROPOSED; not confirmed
├── steward_summary.md               # PROPOSED template; not confirmed
└── registry_notes.md                # PROPOSED; documentation only
```

Do not add watcher code, scheduler configs, source credentials, source payloads, local source descriptors, policy bundles, hidden geoprivacy parameters, release records, or fixtures unless the placement decision is documented, the source activation boundary is explicit, and tests prove no-publication behavior.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/watchers/plants_watch/README.md`.
- [x] It marks this path as watcher routing, not source registry, Flora truth, taxonomy authority, occurrence proof, evidence authority, policy authority, release authority, public runtime, or AI authority.
- [x] It preserves the watcher-as-non-publisher invariant.
- [x] It preserves source descriptor activation, source-role, rights, sensitivity, cadence, source-head, SourceIntakeRecord, steward-summary, quarantine/review, correction, rollback, and public-surface boundaries.
- [x] It routes source descriptors to `data/registry/sources/flora/`, validation to `tools/validators/`, tests/fixtures to `tests/` and `fixtures/`, policy to `policy/`, evidence/receipts to `data/`, release records to `release/`, and public surfaces to governed runtime roots.
- [x] It marks executable scripts, scheduler integration, source activation records, network policy, fixtures, generated SourceIntakeRecords, reports, receipts, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] `tools/watchers/` parent README or watcher-root contract is created or verified.
- [ ] Validator registry, scheduler, CLI, or pipeline references to `plants_watch` are searched and classified.
- [ ] Source activation decision storage and `SourceIntakeRecord` schema home are verified.
- [ ] PLANTS taxonomy-version registry, baseline package home, and source descriptor refs are verified.
- [ ] Fixture files are added only as synthetic/minimized public-safe no-network payloads with documented expected outcomes.
- [ ] Tests prove no-change, change-candidate, deny, restrict, hold, abstain, needs-review, descriptor-missing, activation-missing, rights-unresolved, sensitivity-unresolved, baseline-missing, sensitive-intersection-review-required, steward-summary-missing, publish-edge-denied, and public-surface-blocked cases.
- [ ] CI or scheduled runs prove the watcher cannot write beyond accepted intake/hold/report destinations.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with plants watcher README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
