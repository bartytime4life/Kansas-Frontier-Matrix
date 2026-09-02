<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0028-state-scale-focus-mode-scope
title: ADR-0028 — State-scale Focus Mode scope and cross-scale domain-coverage rule
type: adr
adr_id: ADR-0028
version: v0.3
status: proposed
effective_decision_status: proposed
owners:
  - "NEEDS VERIFICATION — architecture decision owner"
  - "NEEDS VERIFICATION — Focus Mode and composition-scope steward"
  - "NEEDS VERIFICATION — domain-profile steward"
  - "NEEDS VERIFICATION — contracts, schemas, policy, sensitivity, evidence, release, correction, rollback, validation, UI, and docs stewards"
reviewers_required:
  - Architecture steward
  - Docs steward
  - Focus Mode and composition-scope steward
  - Domain-profile steward
  - Contracts and schemas stewards
  - Policy and sensitivity steward
  - Evidence and release steward
  - Correction and rollback steward
  - Governed API and Explorer Web maintainers
  - Validation and CI steward
  - At least one affected domain steward
created: 2026-05-23
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
current_path: "docs/adr/ADR-0028 — State-scale Focus Mode scope.md"
supersedes: []
superseded_by: null
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: a59c9005ca3a790846cabdcf1a160222ed73bbe4
  target_prior_blob: 678ec10d1e921a119de66b5677488f8f2ad4f56a
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  adr_0027_blob: 4dfb29c963cd5662265d3cb97f98be82212d5e08
  legacy_focus_control_readme_blob: 008cf7b3496fdfe56ff3a23b12cb470c27dcf76e
  focus_state_doctrine_readme_blob: ad89a66c4a1e5de0678bffd95c9502f0aee23c96
  legacy_state_index_blob: 8d0b631bd53e6af3747417ee813c791fc67a9c3c
  legacy_state_template_blob: e7d2f2542ddcfee416c4d3fd709e972ff193d446
  focus_mode_payload_contract_blob: 7fe687d587cd60dafd6e3fa34306cd58fd125c73
  focus_mode_index_validator_blob: 89391d75680e859dddf3696b9b782369f364c73e
  validator_entrypoint_blob: c308015da780d7b72f56277b521fb0e42317651e
  validator_orchestrator_blob: 728cf1404839a5b95e03d70d44567863a6f9b6df
  domain_lane_machine_register_blob: 1bfc6f91cfa713a5e3d51ece011b63b46310734f
  drift_register_blob: 5c5078b93c467e66f4cc8b86a7a696dbce5ae7e0
  focus_mock_workflow_blob: fbd56c7cda991ff8f3b804cc0c278e62daaa7abf
  canonical_focus_modes_tree_at_base: absent
  focus_mode_payload_schema_at_base: absent
  layer_registry_entry_schema_at_base: absent
  focus_mode_payload_validator_at_base: absent
  kansas_state_geographic_lane_at_base: absent
inspection_boundary: >
  Current-session GitHub reads against the exact main commit covering the ADR index,
  accepted ADR-0029, the adopted Directory Rules v2 bytes, ADR-0027, this ADR,
  the singular Focus control-plane tree, the state-vocabulary doctrine tree, the
  proposed state-scale index and template, the FocusModePayload semantic contract,
  the county-only Focus index validator, the validator entrypoint and bounded
  orchestrator, the populated but proposed domain-lane machine projection, the
  drift register, and the Focus mock workflow. Exact path checks were performed for
  the plural Focus tree, the FocusModePayload and LayerRegistryEntry schemas, the
  payload validator, and a Kansas state geographic lane. No complete repository
  clone, state-scope registry, schema or policy execution, state Focus payload,
  state EvidenceBundle, live source admission, governed API state request, map
  render, ReleaseManifest, correction, rollback, deployment, or publication was
  exercised.
source_lineage:
  - docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md
  - docs/registers/DOMAIN_LANE.md
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0027-county-focus-mode-control-plane.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/focus-mode/README.md
  - docs/focus-mode/state/README.md
  - docs/focus-mode/state/STATE_INDEX.md
  - docs/focus-mode/state/_template/state-build-plan.md
  - contracts/focus_mode/focus_mode_payload.md
  - tools/validators/validate_focus_mode_index.py
  - tools/validate_all.py
  - tools/validators/validate_all.py
  - control_plane/domain_lane_register.yaml
  - docs/registers/DRIFT_REGISTER.md
  - .github/workflows/focus-mock-test.yml
tags: [kfm, adr, focus-mode, state-scale, kansas-state, domain-coverage, composition-scope, directory-rules-v2, evidence, sensitivity, release, rollback, cite-or-abstain]
notes:
  - "v0.3 is a same-path repository-grounded modernization. It preserves source and effective status proposed; it does not accept ADR-0028, register state scope, authorize structural migration, or create a state-scale implementation."
  - "ADR-0029 is now accepted and adopts the exact Directory Rules v2 bytes. This supersedes v0.2's reliance on the older v1.2 Focus path grammar."
  - "Directory Rules v2 requires a stable scope_id and one authority owner, but it does not by itself assign an exact state-scale Focus documentation path."
  - "The tracked docs/focus-mode/state/ tree now mixes a proposed geographic state index/template with cross-cutting finite-outcome, lifecycle, review, payload, and revocation state doctrine."
  - "The 13-entry machine domain-lane projection is now populated but remains PROPOSED and machine_projection_only."
  - "The validator orchestrator is now real, while the Focus index validator remains county-only and the state payload schema and payload validator remain absent."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0028 — State-scale Focus Mode scope and cross-scale domain-coverage rule

> **Proposed decision.** KFM may recognize one Kansas-wide geographic Focus composition with `scope_kind: state` and stable `scope_id: kansas-state`. Every accepted Focus composition must evaluate a version-pinned domain profile and record exactly one governed disposition for every domain in that profile. The Kansas state composition must resolve its own evidence, policy, review, release, correction, and rollback chain; county Focus outputs may be compared or cross-referenced, but they may not become the root evidence for statewide claims. Before implementation, KFM must also split the overloaded term **state**—geographic scope versus runtime, lifecycle, review, payload, and revocation state—and resolve the mixed authority currently stored under `docs/focus-mode/state/`.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![ADR ID: confirmed](https://img.shields.io/badge/ADR--0028-confirmed-0969da?style=flat-square)](#current-repository-evidence)
[![Directory Rules v2: accepted](https://img.shields.io/badge/Directory%20Rules%20v2-accepted-1a7f37?style=flat-square)](#accepted-directory-authority)
[![State scope: unregistered](https://img.shields.io/badge/state%20scope-unregistered-b42318?style=flat-square)](#current-enforcement-maturity)
[![State term: conflicted](https://img.shields.io/badge/state%20term-geography%20%2F%20system%20state-b42318?style=flat-square)](#state-terminology-and-object-boundaries)
[![Domain projection: 13 proposed](https://img.shields.io/badge/domain%20projection-13%20PROPOSED-f59e0b?style=flat-square)](#proposed-domain-profile)
[![State validator: absent](https://img.shields.io/badge/state%20validator-absent-b42318?style=flat-square)](#current-enforcement-maturity)
[![Implementation: hold](https://img.shields.io/badge/implementation-HOLD-b42318?style=flat-square)](#current-enforcement-maturity)
[![Publication effect: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **Identity is confirmed; acceptance is not.** [`docs/adr/INDEX.md`](./INDEX.md) uniquely assigns `ADR-0028` to this exact file and records source and effective status as `proposed`. Editing, validating, merging, or citing this Markdown does not accept the decision, register `kansas-state`, authorize a path, or create release authority.

> [!CAUTION]
> **The governing directory evidence changed after v0.2.** [ADR-0029](./ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts the exact bytes at [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md). Directory Rules v2 recognizes geography and Focus composition scopes and requires stable scope identity, but it does not preserve the old v1.2 claim that one exact plural Focus documentation tree is already canonical. Future paths therefore remain `HOLD` until a current v2 path decision resolves them.

> [!WARNING]
> **`state` is currently overloaded.** The tracked `docs/focus-mode/state/` tree contains both a proposed Kansas-scale index/template and a cross-cutting doctrine set for finite outcomes, lifecycle, review, payload, revocation, and rollback state. Geographic state scope and system state must not share one independently writable authority lane.

> [!NOTE]
> **Coverage does not mean “publish data for every domain.”** A Focus composition closes domain coverage by recording one reviewed disposition per domain: `populated`, `abstain`, or `deny` at release. Candidate work may use `hold`; `hold`, missing entries, duplicate entries, aliases, unresolved profile identity, and unsupported populated entries block release.

> [!NOTE]
> **No-roll-up does not ban county-granular source records.** State processing may use authoritative records organized by county and may share scope-valid source or EvidenceBundle support with county compositions. It may not use released or candidate county **FocusModePayloads, layers, summaries, or release records** as the authoritative evidence root for a statewide claim.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Accepted directory authority](#accepted-directory-authority) · [Context](#context) · [Decision](#proposed-decision) · [State terminology](#state-terminology-and-object-boundaries) · [Domain profile](#proposed-domain-profile) · [State/county relation](#state-and-county-evidence-relationship) · [Placement](#placement-and-migration-boundary) · [Authority](#authority-and-publication-boundary) · [Outcomes](#coverage-dispositions-and-runtime-outcomes) · [Current evidence](#current-repository-evidence) · [Maturity](#current-enforcement-maturity) · [Validation](#proposed-validation-and-negative-tests) · [Convergence](#implementation-and-convergence-plan) · [Acceptance](#acceptance-gates) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Risks](#risk-and-open-question-ledger) · [Migration](#migration-and-compatibility) · [Incident](#incident-correction-and-rollback) · [Rollback](#rollback-and-supersession) · [Checklist](#verification-checklist) · [References](#references) · [History](#revision-history)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0028` — unique and confirmed in [`INDEX.md`](./INDEX.md) |
| **Tracked path** | `docs/adr/ADR-0028 — State-scale Focus Mode scope.md` |
| **Record edition** | `v0.3` |
| **Source metadata** | `proposed` |
| **Effective decision status** | `proposed` |
| **Decision class** | Geographic Focus scope identity, exactly-one Kansas cardinality, domain-profile closure, cross-scale evidence rules, state-term disambiguation, release and rollback boundary |
| **Accepted placement authority** | Directory Rules v2 exact bytes, adopted by ADR-0029 |
| **Proposed scope kind** | `state` |
| **Proposed scope ID** | `kansas-state` |
| **Proposed current cardinality** | Exactly one Kansas state-scale Focus composition |
| **Exact future docs path** | `HOLD` — not established by the accepted Directory Rules v2 bytes |
| **Current tracked state tree** | Mixed authority under legacy `docs/focus-mode/state/` |
| **Current state-scale implementation** | No verified geographic lane, schema, state-aware validator, payload, release, correction, or rollback |
| **Implementation effect of this revision** | Documentation only |
| **Release/publication effect** | None |
| **Supersedes / superseded by** | None / none |
| **Relationship to ADR-0027** | ADR-0027 remains proposed county-control-plane lineage. ADR-0028 owns state-scope and cross-scale semantics; neither record currently authorizes the mixed state-tree migration. |
| **Relationship to ADR-0029** | ADR-0029 is accepted and controls placement questions through the adopted Directory Rules v2 bytes. |

### Acceptance, placement, and implementation are separate transitions

1. **ADR acceptance** would approve the `state` scope kind, `kansas-state` identity/cardinality, domain-profile closure, direct-evidence rule, state-term split requirement, and release boundary.
2. **Placement resolution** would classify the current mixed state tree with Directory Rules v2 outcomes such as `SPLIT`, `MIGRATE`, or `HOLD`; acceptance of this ADR does not by itself choose the future paths.
3. **Implementation graduation** would require registered scope identity, separated documentation authorities, semantic and machine contracts, fixtures, state-aware validators, governed API and UI behavior, direct evidence closure, release records, correction propagation, and rollback drills.

This same-path revision performs none of those transitions.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This revision is grounded in repository bytes at `main@a59c9005ca3a790846cabdcf1a160222ed73bbe4`.

| Evidence surface | CONFIRMED current state | What remains unproved |
|---|---|---|
| ADR inventory | ADR-0028 maps to this exact filename and remains effectively `proposed`; ADR-0029 is the only accepted numbered ADR | Acceptance of ADR-0028 |
| ADR-0029 | Accepted; adopts exact Directory Rules v2 bytes and makes `docs/doctrine/directory-rules.md` the writable human authority | Independent state-scope decision |
| Directory Rules v2 §12.4 | County, corridor, watershed, region, and Focus Mode are composition scopes; a stable `scope_id` is required; scope does not become a root or domain | `state` registration, exact Focus docs path, or geographic lane |
| Directory Rules v2 placement protocol | Mixed authority returns `SPLIT`; unresolved authority returns `HOLD`; known noncanonical placement may return `MIGRATE` | The reviewed PathDecisionRecord for the current state tree |
| Singular Focus tree | `docs/focus-mode/` exists with README, county, and state material | Canonical write authority |
| Plural Focus tree | `docs/focus-modes/` is absent at the exact checked path | Whether a future plural lane should be created |
| State doctrine tree | `docs/focus-mode/state/README.md` and state-family documents define finite-outcome, lifecycle, review, payload, revocation, and rollback state | Accepted home and separation from geographic state scope |
| Proposed state-scale index | `STATE_INDEX.md` declares one planned `kansas-state` row and claims a validator relationship | A matching lane or executable state parser |
| Kansas state geographic lane | No `kansas-state` lane appears in the checked state tree; no canonical plural tree exists | Any complete state-scale composition |
| FocusModePayload contract | Proposed semantic contract exists and remains county-oriented | State semantics, machine closure, runtime conformance |
| Focus schemas | `schemas/contracts/v1/focus_mode/` is absent at the exact checked path | Machine shape and compatibility |
| Payload validator | `tools/validators/validate_focus_mode_payload.py` is absent | Payload admission |
| Focus index validator | Exists, but `VALID_SCOPES` remains `county`, `region`, `corridor`; implementation is county-only and expects a plural tree | State index parsing, cardinality, domain coverage |
| Domain-lane machine projection | Now contains 13 entries and cites ADR-0029/Directory Rules v2; metadata remains `PROPOSED` and `machine_projection_only` | Adopted domain-set profile and registration authority |
| Validator orchestration | `tools/validate_all.py` is a real thin entrypoint to a bounded deterministic registry orchestrator | State Focus validator registration and a passing exact-head run |
| Focus mock workflow | Proves a deterministic no-network finite-envelope and MockAdapter surface while explicitly stating no accepted mock Focus command exists | State-scale Focus runtime, payload, route, or release |
| Drift register | Current register does not record the state-term/path collision identified here | Reviewed drift disposition |
| State release | No state payload, ReleaseManifest, PromotionDecision, correction record, or rollback drill was verified | Any state publication |

### Truth labels and work states

- **CONFIRMED** — verified from current repository bytes or adopted doctrine.
- **PROPOSED** — candidate decision, profile, field, migration, or implementation.
- **CONFLICTED** — admissible surfaces use incompatible meanings or claim competing authority.
- **HOLD** — current evidence intentionally blocks the next transition.
- **NEEDS VERIFICATION** — a concrete check remains.
- **UNKNOWN** — available evidence does not support a stronger conclusion.
- **PARTIAL** — a bounded implementation surface exists, but its full acceptance boundary is not closed.

### Out of scope

This ADR revision does not:

- accept ADR-0028;
- change ADR-0029 or the adopted Directory Rules bytes;
- accept or repair ADR-0027;
- register a geographic scope, path slug, owner, or domain profile;
- create, move, rename, split, mirror, or retire Focus files;
- create `kansas-state`;
- define final JSON Schema field names or versions;
- activate sources, ingest statewide data, or build statewide claims;
- authorize emergency, legal, title, medical, regulatory, or life-safety advice;
- change rights, sovereignty, consent, sensitivity, review, release, correction, or rollback policy;
- release, deploy, promote, publish, merge, or change repository settings.

[Back to top](#top)

---

<a id="accepted-directory-authority"></a>

## Accepted directory authority

ADR-0029 changes the placement basis that v0.2 used.

### What is now accepted

- The exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` are adopted.
- A path is an authority claim.
- Each artifact has one authority owner.
- Mixed-authority artifacts are split rather than made jointly editable.
- Scope is added only after the owning responsibility root is selected.
- A geography or Focus scope requires a stable registered `scope_id`.
- A domain, source, geography, Focus Mode, renderer, or topic does not justify a repository root.
- Current convention that conflicts with adopted authority is drift, not precedent.
- Decision and structural implementation are separated by the two-change rule.

### What Directory Rules v2 does not decide for this ADR

Directory Rules v2 does **not** itself:

- accept `state` as a Focus scope kind;
- register `kansas-state`;
- choose the exact human documentation path for a geographic state composition;
- declare the old v1.2 `docs/focus-modes/<area>-<scope>/` pattern current authority;
- decide where the cross-cutting state-vocabulary doctrine belongs;
- authorize migration from the singular Focus tree;
- make the existing state index or template canonical;
- define FocusModePayload fields or release policy.

### Placement consequence

The future state-scope path cannot be asserted from topic name or old lineage. The current evidence produces:

| Artifact or group | Directory Rules v2 classification |
|---|---|
| This ADR at its tracked same path | `PLACE` — existing ADR identity and responsibility are confirmed |
| Geographic state-scale index/template content | `HOLD` pending accepted scope identity and one authority owner |
| Cross-cutting state-vocabulary doctrine | `HOLD` pending one doctrine owner and target decision |
| Mixed `docs/focus-mode/state/` tree as one authority | `SPLIT` — it carries geographic and system-state meanings |
| Existing singular tree after targets are decided | Likely `MIGRATE` or bounded `MIRROR`, but not yet a current fact |
| Creating a new Focus root from this ADR alone | `DENY` |

[Back to top](#top)

---

<a id="context"></a>

## Context

A Focus Mode is an evidence-bounded composition and interaction surface for a named scope. It is not a domain, source, lifecycle stage, or repository root.

Kansas-wide questions create a legitimate need for a state-scale composition:

- statewide source families and statewide geometry cannot always be represented honestly as one county;
- users need a bounded Kansas frame with inspectable evidence, time, policy, release, correction, and rollback state;
- state/county comparisons should be possible without making either scale sovereign over the other;
- umbrella views need explicit domain omission and sensitivity handling.

The original ADR also identified a broader problem: a Focus composition can look complete while silently omitting domains. That problem exists at county, corridor, watershed, region, and state scales. The right closure is an explicit disposition for every domain in a pinned profile—not fabricated layers.

### New current-state conflict

The repository now uses **state** in at least two materially different senses:

1. **Geographic state scope** — Kansas as one composition area, represented by the proposed `STATE_INDEX.md` and state build-plan template.
2. **System state vocabulary** — finite outcomes, lifecycle stages, review status, payload freshness, revocation, and rollback, represented by `docs/focus-mode/state/README.md` and its companion documents.

These meanings have different owners, contracts, validation rules, consumers, and change cadence. Keeping both beneath one writable lane would violate the one-authority-owner rule and would make a path such as `state/README.md` impossible to interpret reliably.

### Why state is a scope, not a domain

`state` describes geographic composition scale. It does not add a thematic domain. Hydrology, soil, atmosphere, archaeology, and the other lanes remain domains under their owning responsibility roots. Frontier Matrix or spatial-foundation objects may participate as cross-cutting analytical support without becoming a thirteenth or fourteenth state-specific truth source.

### Why coverage is cross-scale

Silent omission is not unique to Kansas state scope. Every accepted Focus composition should answer:

> For the exact domain profile used by this composition, what is the reviewed release disposition for each domain?

A domain with no admissible evidence uses `abstain`. A domain blocked by policy uses `deny`. A domain with governed support uses `populated`. Candidate uncertainty uses `hold`, which blocks release.

### Relationship to ADR-0027

ADR-0027 remains `proposed`. It documents county-control-plane convergence and the historical plural-path concept, but it cannot amend accepted Directory Rules v2 or authorize the current state-tree migration.

This ADR narrows its responsibility to:

- state-scope identity and cardinality;
- domain-profile closure;
- state/county evidence relationships;
- state-term disambiguation;
- state-scale release and rollback consequences.

A separate reviewed path decision or successor control-plane decision must own structural convergence.

[Back to top](#top)

---

<a id="proposed-decision"></a>

## Proposed decision

Upon reviewed acceptance, KFM adopts these state-scope semantics.

### Scope identity and cardinality

1. **Recognize `state` as a geographic Focus scope kind.**
2. **Register one current state scope ID:** `kansas-state`.
3. **Limit current cardinality to one.** Historical periods, releases, themes, stories, and UI presets are versions or views of `kansas-state`, not sibling state scopes.
4. **Keep identity explicit.** Display label `Kansas`, scope kind `state`, scope ID `kansas-state`, geometry version, and valid-time profile are separate fields.
5. **Do not infer path from identity.** The scope ID does not itself create `docs/focus-mode/state/`, `docs/focus-modes/kansas-state/`, or any other path.

### State-term separation

6. **Reserve geographic fields for geographic scope.** Use names such as `scope_kind`, `scope_id`, `geometry_ref`, and `time_profile_ref`.
7. **Name system-state fields by family.** Use distinct names such as `runtime_outcome`, `lifecycle_stage`, `review_state`, `payload_state`, and `revocation_state`.
8. **Prohibit a bare ambiguous `state` field** in new state-scope contracts unless a containing object makes the namespace unambiguous.
9. **Split mixed documentation authority before implementation.** Geographic state composition and cross-cutting system-state doctrine cannot remain one independently editable artifact family.

### Domain-profile closure

10. **Reference a version-pinned domain profile.** Every Focus candidate and payload identifies the exact profile used for coverage.
11. **Require one entry per profile domain.** Missing, duplicate, extra, aliased, or unresolved domain IDs fail validation.
12. **Use release dispositions `populated`, `abstain`, or `deny`.** Candidate `hold` is allowed but blocks release.
13. **Require evidence and release support for `populated`.**
14. **Require reason, owner, and review posture for `abstain`.**
15. **Require policy and review support for `deny`.**
16. **Preserve the domain profile used by prior releases.** A later profile does not silently rewrite historical coverage.

### Cross-scale evidence

17. **Do not treat county Focus outputs as statewide evidence authority.** County payloads, build plans, layers, generated summaries, or releases are not the root support for a state claim.
18. **Allow shared underlying evidence when support is valid.** State and county claims may cite the same authoritative source, record, EvidenceRef, or EvidenceBundle when spatial, temporal, source-role, rights, and sensitivity scope supports both.
19. **Allow county-granular authoritative source records.** A statewide transform may aggregate county-organized records when the transform, time profile, uncertainty, and receipt are explicit.
20. **Keep cross-scale crosswalks derivative.** A comparison or navigation crosswalk cannot become evidence authority.

### Sensitivity, runtime, and release

21. **State scale never automatically lowers sensitivity.** Aggregation is a reviewed transform, not a universal clearance.
22. **Preserve finite runtime outcomes:** `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.
23. **Keep AI interpretive.** Generated language may summarize release-resolved evidence; it cannot create a state claim or fill missing coverage.
24. **Keep release separate from composition.** A complete domain matrix, lane, payload, map, or validator pass is not publication.
25. **Require correction and rollback.** Every released state claim must resolve correction, withdrawal, cache invalidation, and rollback targets appropriate to its consequence.

### Decision and implementation separation

26. **Acceptance changes governance semantics only.** It does not move files or create the state lane.
27. **A later placement/convergence change must classify and split the current state tree.**
28. **A later implementation change must register scope identity, close contracts and schemas, add fixtures and validators, and build the candidate lane.**
29. **A later release decision must independently approve any public state payload.**

[Back to top](#top)

---

<a id="state-terminology-and-object-boundaries"></a>

## State terminology and object boundaries

### Required vocabulary split

| Meaning | Preferred field or family | Example | Must not be collapsed into |
|---|---|---|---|
| Geographic scale | `scope_kind` | `state` | Lifecycle or review state |
| Geographic identity | `scope_id` | `kansas-state` | Folder name alone |
| Runtime result | `runtime_outcome` | `ABSTAIN` | Payload freshness |
| Data lifecycle | `lifecycle_stage` | `PROCESSED` | Release approval |
| Human/policy review | `review_state` | `approved` | `PUBLISHED` |
| Payload freshness/exposure | `payload_state` | `fresh` | Evidence sufficiency |
| Revocation/rollback | `revocation_state` | `live`, `revoked`, `rolled-back` | Geographic scope |
| Release identity | `release_ref` | immutable release ID | Mutable `current` alias |

Illustrative semantic shape:

```yaml
scope:
  scope_kind: state
  scope_id: kansas-state
  geometry_ref: kfm://geography/kansas/<version>
  time_profile_ref: kfm://time-profile/example
system_state:
  runtime_outcome: ABSTAIN
  lifecycle_stage: PUBLISHED
  review_state: approved
  payload_state: fresh
  revocation_state: live
release_ref: kfm://release/example
```

This is illustrative, not a final schema.

### Documentation split requirement

The current state tree contains at least these two authority groups:

| Current material | Primary responsibility |
|---|---|
| `STATE_INDEX.md` and `_template/state-build-plan.md` | Geographic state-scale composition planning |
| `README.md`, finite outcomes, lifecycle, review, payload, revocation, and transition docs | Cross-cutting Focus/system-state doctrine |

The implementation change must not merely rename the directory. It must:

1. classify each file by one authority owner;
2. split the two groups;
3. resolve target paths under accepted Directory Rules v2;
4. repair links and metadata;
5. preserve history and compatibility;
6. verify that no duplicate writable authority remains.

[Back to top](#top)

---

<a id="proposed-domain-profile"></a>

## Proposed domain profile

### Current machine-projection evidence

`control_plane/domain_lane_register.yaml` now contains 13 entries. It is stronger implementation evidence than the empty projection inspected for v0.2, but it declares:

- `status: PROPOSED`;
- `authority: machine_projection_only`;
- unresolved registration and owner authority;
- non-effects that prohibit domain creation, source activation, and release.

ADR-0028 therefore uses the current IDs as a **candidate profile basis**, not as adopted domain authority.

### Candidate core IDs

| # | Domain ID | Current projection label |
|---|---|---|
| 1 | `agriculture` | Agriculture |
| 2 | `archaeology` | Archaeology |
| 3 | `atmosphere` | Atmosphere |
| 4 | `fauna` | Fauna |
| 5 | `flora` | Flora |
| 6 | `geology` | Geology |
| 7 | `habitat` | Habitat |
| 8 | `hazards` | Hazards |
| 9 | `hydrology` | Hydrology |
| 10 | `people-dna-land` | People, DNA & Land |
| 11 | `roads-rail-trade` | Roads, Rail & Trade |
| 12 | `settlements-infrastructure` | Settlements & Infrastructure |
| 13 | `soil` | Soil |

Draft aliases such as `air`, `atmosphere_air`, `roads_rail`, `settlement`, or `transport` must not become parallel profile IDs. Any compatibility alias is resolved through the accepted register and never emitted as canonical release identity.

### Versioned profile requirement

A future payload should reference a stable profile identity and digest, rather than assuming “13” forever.

Illustrative shape:

```yaml
domain_profile_ref: kfm://domain-profile/core-v1
domain_profile_digest: sha256:<digest>
coverage:
  - domain_ref: hydrology
    disposition: populated
    owner_ref: kfm://role/hydrology-steward
    evidence_refs:
      - kfm://evidence/example
    release_refs:
      - kfm://release/example
  - domain_ref: archaeology
    disposition: deny
    owner_ref: kfm://role/archaeology-steward
    policy_decision_refs:
      - kfm://policy-decision/example
    reason_codes:
      - sensitive_exact_location
```

The final contract may use an array or map, but validation must enforce:

- one resolved profile reference and digest;
- exactly one coverage entry per profile domain;
- no extras, duplicates, or aliases;
- stable identity and accountable owner per entry;
- direct evidence and release support for populated entries;
- reason and next-review posture for abstentions;
- policy and review support for denials;
- no unresolved hold at release.

### Why `not_applicable` is not a release disposition

Every profile domain is applicable to the coverage question:

> What is the governed disposition for this domain in this composition?

No supported claim becomes `abstain`. Prohibited exposure becomes `deny`. A `not_applicable` escape would recreate silent omission.

### Profile evolution

Adding, removing, renaming, splitting, or merging a registered domain requires its own governed change. A successor profile may supersede a prior profile through compatibility and migration. Existing releases retain the profile identity under which they were validated.

[Back to top](#top)

---

<a id="state-and-county-evidence-relationship"></a>

## State and county evidence relationship

### Independent composition rule

A state Focus composition is not a collection of county Focus outputs.

The following are forbidden as the sole or root support for a statewide claim:

- county `FocusModePayload` objects;
- county build plans or layer registries;
- county-generated summaries or AI responses;
- county release manifests treated as source evidence;
- a union of county public layers with no new source/evidence processing;
- “all counties agree” without a direct statewide claim, evidence scope, and time profile;
- a cross-scale crosswalk treated as proof.

### Allowed shared support

The following may be shared when source role, rights, sensitivity, geography, time, and method support both scales:

- one authoritative SourceDescriptor;
- authoritative records whose native organization is county-by-county;
- a scope-valid EvidenceBundle;
- taxonomy, boundary, identity, or temporal reference objects;
- a deterministic statewide transformation of county-granular source records;
- source snapshots and receipts referenced independently by each composition.

### State-owned closure

A state candidate emits or resolves its own:

- scope and geometry identity;
- time profile;
- claim identity;
- evidence-resolution record;
- aggregation/transform receipt where applicable;
- uncertainty and fitness statement;
- policy and sensitivity decision;
- domain-profile coverage;
- review record;
- release decision and manifest;
- correction, withdrawal, cache, and rollback targets.

### Comparison without authority collapse

A state/county crosswalk may describe:

- shared source records;
- differing time profiles;
- differing transforms;
- claim relationships;
- release relationships;
- disagreements and correction lineage.

It remains a comparison and navigation projection. It does not synchronize releases automatically or decide which scale is true.

[Back to top](#top)

---

<a id="placement-and-migration-boundary"></a>

## Placement and migration boundary

### Directory Rules v2 basis

This ADR creates no root and does not choose a future path. Directory Rules v2 requires:

- one authority owner;
- root selection before scope segmentation;
- stable registered scope identity;
- `SPLIT` for mixed authority;
- `HOLD` when ownership or target evidence is unresolved;
- `MIGRATE` only after a unique target is known;
- decision before structural implementation.

### Current placement outcomes

| Artifact family | Owning responsibility | Current or candidate home | Current outcome |
|---|---|---|---|
| This ADR | Human governance decision record | Existing `docs/adr/` path | `PLACE` |
| Geographic state-scope registration | Machine governance/identity projection | Exact home `NEEDS VERIFICATION` | `HOLD` |
| Geographic state composition docs | Human planning and acceptance docs | Must remain under `docs/`; exact lane undecided | `HOLD` |
| Cross-cutting Focus state doctrine | Human architecture/standard doctrine | Must remain under `docs/`; exact lane undecided | `HOLD` |
| Mixed `docs/focus-mode/state/` tree | Two authority owners | Current singular tree | `SPLIT` |
| Focus semantic contract | Object meaning | Existing `contracts/focus_mode/` family | `PLACE` for the family; state extension proposed |
| Focus machine schema | Machine shape | Canonical schema root; exact Focus schema family currently absent | `HOLD` pending contract/version decision |
| Fixtures | Test evidence | `fixtures/` responsibility root | `HOLD` pending contract and path identity |
| Validators | Repository validation | `tools/validators/` | `PLACE` for validator code; state validator absent |
| UI implementation | Deployable app | `apps/explorer-web/` if that app remains the accepted implementation target | `NEEDS VERIFICATION` because ADR-0005 is proposed |
| Lifecycle data instances | Lifecycle/accountability lanes | `data/<owning_lane>/` | `HOLD` pending object-family contracts |
| Release decisions | Release object families | `release/<object_family>/` | `HOLD` pending candidate and release authority |
| Published state carriers | Release-approved delivery objects | `data/published/` | `DENY` until governed release closure |

The historical candidate `docs/focus-modes/kansas-state/` may remain design lineage, but v0.3 does not present it as current accepted placement.

### Required structural sequence

1. **Freeze the authority snapshot.**
2. **Inventory the entire singular Focus tree and every inbound/outbound reference.**
3. **Classify each state file as geographic composition, cross-cutting system-state doctrine, compatibility, generated output, or obsolete claim.**
4. **Create PathDecisionRecords for each authority group.**
5. **Accept any necessary control-plane or naming decision.**
6. **Split and migrate with history preservation.**
7. **Repair docs, validators, workflows, contracts, examples, and links in the same dependency-closed sequence.**
8. **Keep compatibility one-way and read-only, with exit criteria.**
9. **Prove no duplicate writable authority.**
10. **Record an exact pre-migration rollback target.**
11. **Verify no data, release, route, or publication state changed because of documentation movement.**

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

State scope does not make a Focus composition authoritative by itself. Every state claim remains downstream of:

- registered source identity and source role;
- rights, sovereignty, consent, and sensitivity;
- admissible evidence and provenance;
- semantic contracts and machine schemas;
- deterministic transformations and receipts;
- policy and accountable review;
- promotion and release;
- correction, withdrawal, supersession, and rollback.

A statewide map, layer, count, summary, domain matrix, generated explanation, comparison view, or “all counties” aggregate is a carrier or projection. It is not sovereign truth.

Public clients may consume a state Focus response only through the governed runtime or a separately approved released-static profile. They must not read:

- control-plane Markdown;
- candidate payloads;
- RAW, WORK, QUARANTINE, or restricted stores;
- canonical/internal data stores;
- proof or receipt stores as public APIs;
- model runtimes directly;
- denied payload details;
- unreleased state indexes or build plans as data.

State-scale content must not be presented as emergency alert authority, legal/title advice, access permission, regulatory direction, medical advice, or definitive living-person or DNA interpretation.

[Back to top](#top)

---

<a id="coverage-dispositions-and-runtime-outcomes"></a>

## Coverage dispositions and runtime outcomes

### Composition-level domain dispositions

| Disposition | Meaning | Required closure | Release effect |
|---|---|---|---|
| `populated` | One or more governed claims/layers exist for the domain at this scope | Evidence, policy, owner, time, sensitivity, review, and release references | Eligible when all gates pass |
| `abstain` | No sufficiently supported or admissible public claim exists | Stable reason, owner, evidence-gap statement, next-review posture | Eligible as explicit cite-or-abstain closure |
| `deny` | Policy, rights, sovereignty, sensitivity, or safety prohibits exposure | Policy/review reference and public-safe non-disclosure behavior | Eligible as explicit fail-closed closure |
| `hold` | Evidence, profile, owner, schema, policy, review, path, or release is unresolved | Remediation obligation | Candidate only; blocks release |

Missing entries, aliases, invalid states, contradictory records, and validator errors block release.

### Runtime outcomes

A governed state Focus request resolves to exactly one outward outcome:

| Outcome | Client meaning |
|---|---|
| `ANSWER` | A bounded response is evidence-supported, allowed, and covered by the active release |
| `ABSTAIN` | Evidence, scope, freshness, or admissibility is insufficient |
| `DENY` | Policy, rights, sensitivity, role, or release state blocks exposure |
| `ERROR` | The request cannot be processed safely or deterministically |

Coverage and runtime are different axes. A `populated` domain may still return `ABSTAIN` or `DENY` for a particular question. A `deny` disposition never permits client-side recovery of protected payloads.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | Current verified state | Safe conclusion |
|---|---|---|
| ADR-0028 | Exact indexed file; source/effective `proposed` | Decision not accepted |
| ADR-0029 | Accepted; adopts exact Directory Rules v2 bytes | Placement authority is established |
| Directory Rules v2 | Stable scope identity and one-owner placement model; no exact state Focus path | Scope and path still need decisions |
| ADR-0027 | Proposed county-control-plane ADR still describes older v1.2 path assumptions | Lineage, not current placement authority |
| `docs/focus-mode/` | Singular tree exists | Current convention only; canonicality unresolved |
| `docs/focus-modes/` | Exact path absent | No plural implementation |
| `docs/focus-mode/state/README.md` | Defines cross-cutting system-state doctrine | Substantive docs exist, but meaning conflicts with geographic state scope |
| State doctrine companions | Finite outcome, lifecycle, review, payload, revocation, and transition docs exist | Documentation depth increased; authority split remains unresolved |
| `STATE_INDEX.md` | One `planned` Kansas row; claims validator parsing and a lane requirement | Inert proposal and stale/unsupported claim |
| State template | Exists and depends on ADR-0028 | Design scaffold only |
| `kansas-state` geographic lane | Not found in the checked state tree | No state composition |
| FocusModePayload contract | Proposed county-oriented semantic contract | State contract not closed |
| Focus schema family | Absent at exact checked path | No machine state payload shape |
| Payload validator | Absent | No state payload admission |
| Focus index validator | County-only; scopes county/region/corridor; expects plural tree | No state/cardinality/coverage enforcement |
| Domain-lane projection | 13 populated entries; `PROPOSED`, machine projection only | Candidate profile basis, not adopted profile |
| Validator orchestrator | Real bounded registry orchestrator behind `tools/validate_all.py` | Old placeholder claim is superseded |
| Focus mock workflow | Deterministic finite-envelope and MockAdapter proof; no accepted Focus command | Runtime foundation is partial, not state Focus implementation |
| Drift register | Does not record this Focus state collision | Register update remains separate work |
| State release/publication | No state payload or release evidence verified | None |

### Confirmed absent at exact checked paths

- `docs/focus-modes/`
- `schemas/contracts/v1/focus_mode/`
- `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json`
- `schemas/contracts/v1/focus_mode/layer_registry_entry.schema.json`
- `tools/validators/validate_focus_mode_payload.py`
- a `kansas-state` geographic lane beneath the checked state tree

Exact-path absence does not prove no related idea exists elsewhere. It proves the currently claimed implementation chain is not closed at those paths.

[Back to top](#top)

---

<a id="current-enforcement-maturity"></a>

## Current enforcement maturity

| Capability | Current state |
|---|---|
| ADR identity/status | `CONFIRMED / proposed` |
| Directory placement authority | `CONFIRMED / accepted through ADR-0029` |
| State scope kind | `PROPOSED / unregistered` |
| `kansas-state` scope ID | `PROPOSED / unregistered` |
| Exact state composition path | `HOLD` |
| State-term separation | `CONFLICTED` |
| Singular Focus tree | Present; authority unresolved |
| Plural Focus tree | Absent |
| State-system doctrine | Present as draft/proposed documentation |
| Geographic state index/template | Present as proposed scaffolds |
| Geographic state lane | Absent |
| Domain-profile identity | 13-entry proposed machine projection; adoption unresolved |
| Coverage contract | Proposed in prose only |
| FocusModePayload semantic contract | Present; county-oriented and proposed |
| FocusModePayload schema | Absent |
| LayerRegistryEntry schema | Absent |
| State-aware index validator | Absent |
| Focus payload validator | Absent |
| Validator orchestration | Present and deterministic |
| State fixtures/negative tests | Not established |
| Mock finite-envelope proof | `PARTIAL / deterministic no-network proof` |
| Accepted Focus runtime command | Absent |
| Governed API state Focus route | Not established |
| State evidence/release/correction/rollback | Not established |
| Production state publication | None |

**Overall maturity: `PROPOSED DESIGN / IMPLEMENTATION HOLD`.** KFM has stronger directory authority, a populated domain projection, a real validator orchestrator, and a bounded finite-envelope proof. It still lacks the scope registration, authority split, state contract/schema/validator chain, geographic lane, and release evidence required for a state Focus composition.

[Back to top](#top)

---

<a id="proposed-validation-and-negative-tests"></a>

## Proposed validation and negative tests

Validation must be deterministic, non-vacuous, local/offline-capable for core checks, and fail closed.

### Required validation families

| Family | Required checks |
|---|---|
| ADR status | ADR and index agree; acceptance is reviewed; no file move or release is inferred |
| Directory authority | Adopted v2 digest resolves; current path decisions cite v2 rule IDs |
| State terminology | Geographic scope and system-state fields are distinct; bare ambiguous `state` rejected |
| Placement | Mixed state tree is split; one writable authority per artifact family; compatibility is one-way |
| Scope identity | `scope_kind=state`; one registered `scope_id=kansas-state`; no duplicate state scope |
| Geometry/time | Geometry version and time profile are explicit and coherent |
| Domain profile | Profile reference and digest resolve; exact registered IDs; no aliases, duplicates, or extras |
| Coverage | One disposition per domain; populated support; abstain reason; deny policy; no release hold |
| Evidence | Direct state support resolves; county Focus outputs are not root evidence |
| Transform | County-granular aggregation is deterministic, receipt-bearing, and scope-valid |
| Sensitivity | Protected content is transformed before delivery; styling alone is not protection |
| Contracts/schemas | Semantic and machine shapes agree; version compatibility is declared |
| Fixtures | Non-empty valid and invalid state/cross-scale cases |
| Runtime | Governed API and client preserve finite outcomes and obligations |
| Release | Promotion, release, correction, withdrawal, rollback, and cache behavior resolve |
| Public boundary | No internal store, candidate payload, or direct model-runtime path |

### Stable reason-code families

- `state_scope_not_accepted`
- `state_scope_id_unregistered`
- `state_scope_cardinality_invalid`
- `state_path_decision_missing`
- `state_term_ambiguous`
- `state_doctrine_scope_collision`
- `mixed_authority_not_split`
- `focus_control_plane_authority_unresolved`
- `state_index_claim_unenforced`
- `state_index_lane_mismatch`
- `state_lane_missing`
- `multiple_state_lanes`
- `domain_profile_unresolved`
- `domain_profile_digest_mismatch`
- `domain_id_unregistered`
- `domain_alias_forbidden`
- `domain_coverage_missing`
- `domain_coverage_duplicate`
- `coverage_disposition_invalid`
- `coverage_hold_unresolved`
- `coverage_abstain_reason_missing`
- `coverage_deny_policy_missing`
- `populated_domain_evidence_unresolved`
- `county_focus_output_used_as_state_authority`
- `state_evidence_scope_mismatch`
- `state_time_profile_incoherent`
- `state_aggregation_receipt_missing`
- `sensitivity_review_missing`
- `focus_schema_missing`
- `focus_payload_validator_missing`
- `state_fixture_inventory_vacuous`
- `state_runtime_unverified`
- `release_manifest_unresolved`
- `rollback_target_unresolved`
- `public_state_route_unverified`

### Required negative and positive fixtures

At minimum:

- `scope_kind: state` before ADR acceptance;
- unregistered `scope_id`;
- two active Kansas state scopes;
- historical period represented as a sibling state scope rather than time profile/release;
- bare `state` field with ambiguous meaning;
- one file combining state-scope registry and runtime-state doctrine;
- state index says `planned` while lane is absent;
- validator claims state support but parses county only;
- missing domain-profile reference or digest;
- old aliases such as `atmosphere_air` or `roads_rail`;
- one domain missing, duplicated, or extra;
- `hold` at release;
- abstain without reason, owner, or next review;
- deny without policy/review support;
- populated without evidence or release support;
- exact archaeology, rare-species, living-person, DNA, or infrastructure detail made public by aggregation;
- state claim supported only by county Focus output;
- county-granular authoritative records transformed into a direct state evidence chain — **valid positive case**;
- shared EvidenceBundle whose scope explicitly supports both scales — **valid positive case**;
- cross-scale crosswalk treated as evidence;
- incompatible times aggregated without a state time profile;
- validator reports pass with zero state fixtures;
- public client reads a state candidate or control-plane document.

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

Use small, dependency-ordered, reversible changes. Directory Rules v2's decision-before-implementation rule applies.

### Wave A — Decision convergence

1. Review ADR-0028 against accepted Directory Rules v2.
2. Confirm ADR-0028 owns state-scope semantics, not structural placement.
3. Reconcile its non-overlapping relationship with proposed ADR-0027.
4. Accept or reject the `state` scope, `kansas-state` identity/cardinality, domain-profile closure, direct-evidence rule, and state-term split requirement.
5. Synchronize ADR/index status in the reviewed decision change.
6. Do not move files or claim implementation graduation.

### Wave B — Authority inventory and placement decisions

1. Inventory the complete singular Focus tree and every consumer.
2. Classify state-scope planning separately from system-state doctrine.
3. Produce v2 PathDecisionRecords with `SPLIT`, `MIGRATE`, `MIRROR`, `HOLD`, or `DENY`.
4. Register the scope identity in the accepted machine authority selected by that decision.
5. Define canonical targets and bounded compatibility.
6. Record migration and rollback targets.
7. Do not create a released payload.

### Wave C — Domain profile, contracts, schemas, and fixtures

1. Ratify or supersede the current proposed domain-lane projection.
2. Create a versioned domain profile and digest.
3. Version the FocusModePayload semantic contract.
4. Create closed machine schemas in the accepted schema family.
5. Define scope, coverage, state/county evidence, and system-state namespaces.
6. Add deterministic valid/invalid fixtures.
7. Preserve compatibility for county candidates through explicit versions, not silent required-field changes.

### Wave D — Validators and CI

1. Extend or replace the county-only index validator only after path decisions are effective.
2. Add state scope/cardinality and domain-profile checks.
3. Implement the payload validator.
4. Register validators in the bounded orchestrator.
5. Add non-vacuity, policy, API, UI, release, and public-boundary tests.
6. Keep validators read-only and non-publishing.

### Wave E — Kansas state candidate

1. Create the geographic composition only at the accepted target.
2. Populate required planning and acceptance artifacts.
3. Record all domain dispositions.
4. Admit direct statewide or scope-valid authoritative support.
5. Produce evidence, policy, sensitivity, aggregation, and time-profile records.
6. Keep the candidate non-public until every gate closes.

### Wave F — Runtime, release, correction, and rollback proof

1. Produce a validated state FocusModePayload.
2. Integrate the governed API and Explorer client with finite outcomes.
3. Verify no direct internal-store or model-runtime path.
4. Assemble accountable review, PromotionDecision, ReleaseManifest, correction, withdrawal, and rollback records.
5. Run state/county comparison without authority collapse.
6. Exercise cache invalidation, correction propagation, withdrawal, and rollback.
7. Graduate only from observed evidence.

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance gates

### ADR acceptance

- [ ] Architecture, Focus composition, domain-profile, contract/schema, policy/sensitivity, evidence/release, correction/rollback, validation, API/UI, and docs reviewers approve.
- [ ] ADR-0029 and the adopted Directory Rules v2 digest are cited as placement authority.
- [ ] ADR-0027 remains proposed and is not treated as authority.
- [ ] `scope_kind: state` and `scope_id: kansas-state` semantics are approved.
- [ ] Exactly-one current Kansas state cardinality is approved.
- [ ] Geographic scope and system-state vocabularies are explicitly separated.
- [ ] Domain-profile reference/digest and complete-coverage rules are approved.
- [ ] `populated`, `abstain`, `deny`, and candidate `hold` semantics are approved.
- [ ] County Focus outputs are prohibited as root state evidence; shared underlying evidence is allowed under explicit scope.
- [ ] Sensitivity does not weaken automatically at state scale.
- [ ] Exact future paths remain unresolved unless separately decided under Directory Rules v2.
- [ ] ADR and index status match.
- [ ] No state lane, schema, validator, payload, route, release, or publication is represented as implemented.
- [ ] Rollback of the decision record is defined.

### Placement/convergence graduation

- [ ] Complete state-tree and consumer inventory exists.
- [ ] Each file has one authority owner.
- [ ] Geographic state planning and system-state doctrine are split.
- [ ] PathDecisionRecords identify accepted targets and rule IDs.
- [ ] Compatibility is one-way, read-only, and time-bounded.
- [ ] Links, validators, workflows, contracts, and docs are updated.
- [ ] No duplicate writable authority remains.
- [ ] Structural rollback is tested.
- [ ] No data/release side effect occurred.

### Implementation graduation

- [ ] Scope identity is registered and machine-readable.
- [ ] Domain profile is accepted, versioned, and digest-bound.
- [ ] Semantic contract and closed schemas agree.
- [ ] State-aware index and payload validators are registered.
- [ ] Valid and invalid fixtures are non-empty.
- [ ] The Kansas state candidate has all required artifacts.
- [ ] Every domain has a release-valid disposition.
- [ ] Direct state evidence, geometry, and time profiles resolve.
- [ ] Sensitive and rights-constrained lanes fail closed.
- [ ] Governed API/client finite outcomes pass.
- [ ] State/county comparison does not collapse authority.
- [ ] Release, correction, withdrawal, cache, and rollback drills pass.
- [ ] Public clients cannot read candidates or internal stores.
- [ ] Accountable independent review is recorded.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- Provides a governed Kansas-wide composition without creating a new root or domain.
- Makes domain omission explicit at every scale.
- Preserves cite-or-abstain and deny-by-default.
- Separates geographic scope from runtime and lifecycle state.
- Prevents county Focus outputs from becoming accidental statewide authority.
- Permits valid shared evidence and county-granular source organization.
- Uses accepted Directory Rules v2 rather than stale path assumptions.
- Pins coverage to a versioned domain profile instead of a magic count or alias set.
- Creates explicit correction and rollback requirements for a high-visibility umbrella view.
- Converts the mixed state tree into a visible governance problem rather than silently legitimizing it.

### Costs

- Requires an authority inventory and structural split before geographic implementation.
- Requires a scope register or equivalent machine authority that is not yet identified.
- Requires domain-profile governance, schemas, validators, fixtures, and runtime work.
- Adds review burden because every domain disposition is explicit.
- May block state release while one domain, path, profile, or sensitivity question remains unresolved.
- Requires direct evidence and aggregation records instead of convenient county output roll-up.
- Adds cross-scale consistency, performance, cache, and temporal-coherence work.
- Requires accountable state and domain reviewers.

### Preserved invariants

- Focus Mode remains a composition, not a root or domain.
- EvidenceBundle outranks generated language.
- Public clients use governed interfaces.
- Promotion remains a governed state transition.
- State scale does not reduce sensitivity automatically.
- Receipts, proofs, catalogs, reviews, release decisions, corrections, and published carriers remain distinct.
- Structural decisions precede implementation.
- Unknown authority returns `HOLD`, not a plausible path.

[Back to top](#top)

---

<a id="alternatives-considered"></a>

## Alternatives considered

| Alternative | Disposition |
|---|---|
| Keep county/corridor/watershed/region only | Rejected as the target design: no governed Kansas-wide composition |
| Use ordinary statewide layers without a Focus composition | Retained for simple delivery, but insufficient for state-level claim, coverage, review, correction, and rollback closure |
| Treat `state` as a thematic domain | Rejected: it is geographic scope |
| Reuse `docs/focus-mode/state/` as the Kansas geographic lane | Rejected: the path currently carries cross-cutting system-state doctrine and mixed authority |
| Treat the state-doctrine documents as proof that state-scale Focus exists | Rejected: system-state vocabulary is not geographic composition implementation |
| Restore the old v1.2 plural path assertion as current fact | Rejected: ADR-0029 adopted Directory Rules v2, whose current rules require a new path decision |
| Create `docs/focus-modes/kansas-state/` immediately | Rejected for this change: candidate lineage is not accepted placement evidence |
| Permit multiple Kansas state scopes for themes or time | Rejected: use versions, time profiles, stories, or views |
| Derive state output by unioning county Focus outputs | Rejected: weakens evidence, time, and release integrity |
| Ban all county-granular records from state processing | Rejected: authoritative statewide sources may be county-organized |
| Require every domain to be populated | Rejected: would fabricate or overexpose; explicit abstain/deny is valid closure |
| Add `not_applicable` as a disposition | Rejected: recreates silent omission |
| Hard-code 13 forever | Rejected: use a versioned profile and digest |
| Hard-code old aliases | Rejected: use registered IDs and explicit compatibility mapping |
| Use a cross-scale crosswalk as evidence | Rejected: crosswalk is navigation/comparison, not proof |
| Allow release while one domain is `hold` | Rejected: unresolved umbrella coverage blocks release |
| Resolve placement inside the same PR that first accepts this ADR | Rejected by default: Directory Rules v2 separates decision and structural implementation |

[Back to top](#top)

---

<a id="risk-and-open-question-ledger"></a>

## Risk and open-question ledger

| Item | Status | Required resolution |
|---|---|---|
| ADR-0028 acceptance | `HOLD` | Reviewed decision and synchronized index |
| ADR-0027 relationship | `NEEDS VERIFICATION` | Confirm non-overlapping ownership or successor model |
| State scope registration authority | `UNKNOWN` | Select accepted machine register/object family |
| Exact state composition docs path | `HOLD` | Directory Rules v2 PathDecisionRecord |
| Exact system-state doctrine path | `HOLD` | Directory Rules v2 PathDecisionRecord |
| Mixed state tree | `CONFIRMED CONFLICT` | Inventory, split, migration, compatibility, rollback |
| Singular vs plural Focus tree | `CONFIRMED DRIFT` | Current v2 decision rather than inherited v1.2 assumption |
| State index planned row without lane | `CONFIRMED DRIFT` | Demote/correct or implement only after prerequisites |
| State index validator claim | `CONFIRMED DRIFT` | Implement state parser or correct the claim |
| Domain-profile authority | `HOLD` | Ratify/version current 13-entry projection or successor |
| Domain aliases | `CONFLICTED` | Accepted IDs and explicit compatibility crosswalk |
| FocusModePayload state extension | `OPEN` | Versioned semantic contract |
| Focus machine schemas | `CONFIRMED GAP` | Create closed schemas after contract decision |
| Focus payload validator | `CONFIRMED GAP` | Implement and register |
| State fixtures | `CONFIRMED GAP` | Non-empty positive/negative inventory |
| State source inventory | `UNKNOWN` | Source descriptors, rights, cadence, scope |
| State aggregation methodology | `OPEN` | Transform contract, receipt, uncertainty, time profile |
| State/county disagreement | `OPEN` | Comparison and correction policy without authority collapse |
| State sensitivity overrides | `OPEN` | Default none; require policy, reviewer, and negative fixture |
| State lane ownership | `NEEDS VERIFICATION` | Accountable owner and backup |
| Focus mock runtime | `PARTIAL / HOLD` | Accepted command, runtime fixtures, API/client proof |
| State release path and objects | `UNKNOWN` | Resolve only after candidate and release authority |
| Mutable state alias/cache | `UNKNOWN` | Atomic release alias, invalidation, correction |
| State performance budgets | `NEEDS VERIFICATION` | Correctness-first benchmark |
| Drift-register coverage | `OPEN` | Record the state-term/path collision separately |
| Public emergency-authority ambiguity | `RISK` | Explicit non-authority policy and UI labels |

Unknowns narrow implementation and block release. They do not authorize plausible defaults.

[Back to top](#top)

---

<a id="migration-and-compatibility"></a>

## Migration and compatibility

### Current facts

- The accepted Directory Rules v2 authority exists.
- The singular Focus tree exists.
- The plural Focus tree is absent at the checked path.
- The state tree combines system-state doctrine with geographic state-scale index/template material.
- No geographic `kansas-state` lane was found in that tree.
- The state index's validator and `planned` claims are unsupported by current executable behavior.
- The semantic Focus contract exists; the machine schema family and payload validator are absent.
- The complete county-plan and external-consumer inventory is not established in this revision.

### Migration rules

1. **Inventory before move.**
2. **Classify by authority, not filename.**
3. **Split geographic state scope from system-state doctrine.**
4. **Use accepted v2 rule IDs and PathDecisionRecords.**
5. **Do not infer a target from old v1.2 examples.**
6. **Preserve object identity, history, attribution, and correction notes.**
7. **No blind bulk backfill.** Existing county and state plans are inspected against the accepted profile and contract.
8. **Version machine shapes.** Do not silently add required fields to an unknown or absent schema.
9. **Use staged enforcement only after inventory and compatibility evidence.**
10. **Repair overclaims during migration.** Index and validator statements must match executable behavior.
11. **Update every consumer.** Docs, links, validators, workflows, examples, contracts, API/UI clients, and release references converge together.
12. **Keep compatibility one-way.** A mirror or redirect is read-only and generated or minimal.
13. **Retain an exact rollback target.**
14. **No release side effects.** Documentation migration does not promote data or publish a state composition.

### Compatibility artifact requirements

Any temporary compatibility file must:

- identify its noncanonical class;
- point to one accepted canonical destination;
- contain no competing registry, plan, or doctrine body;
- prohibit direct edits;
- record the governing decision and migration date;
- be covered by duplicate-authority and link tests;
- have a reviewed retirement trigger.

[Back to top](#top)

---

<a id="incident-correction-and-rollback"></a>

## Incident, correction, and rollback

### State-scale claim incident

If a released state Focus composition exposes unsupported, stale, overgeneralized, undergeneralized, rights-constrained, sensitive, or county-derived claims:

1. reduce exposure through the governed release route or alias;
2. preserve the affected payload, domain profile, evidence, receipts, policies, reviews, release, and cache identities;
3. identify affected domains, sources, counties, time profiles, transforms, and public claims;
4. determine whether county releases share the same underlying defect;
5. issue correction, withdrawal, or rollback records;
6. invalidate API, tile, CDN, service-worker, browser, search, vector, and story caches;
7. verify no alternate state or county path continues serving the claim;
8. rebuild from direct admissible evidence;
9. obtain independent review before restoration;
10. record post-incident verification.

A county disagreement does not automatically prove the state release wrong, and a state release is not automatically authority over a county release. Compare evidence, geography, time, source role, policy, and transforms.

### Authority-split or migration incident

If the state-tree split creates broken links, duplicate authorities, lost history, or mismatched validators:

- stop writes to both candidate authorities;
- revert to the exact pre-migration commit or restoration plan;
- preserve the accepted decision records and PathDecisionRecords;
- restore one writable authority;
- repair links and consumers;
- rerun topology, docs, validator, and changed-area checks;
- do not compensate by making both trees writable.

### Rollout failure

When state-scope enforcement breaks candidate work:

- hold or narrow the candidate;
- keep state scope non-public;
- preserve explicit abstain, deny, and hold outcomes;
- repair scope identity, path decisions, contracts, schemas, fixtures, or validation;
- do not restore an unreviewed legacy authority or bypass the validator;
- resume only through the accepted path.

[Back to top](#top)

---

<a id="rollback-and-supersession"></a>

## Rollback and supersession

### Documentation-only rollback

Restore the prior ADR blob:

```text
678ec10d1e921a119de66b5677488f8f2ad4f56a
```

A transparent revert restores the v0.2 proposed documentation. It does not alter ADR-0029, Directory Rules, Focus files, schemas, validators, data, releases, routes, or public state.

### If this ADR is later accepted

An accepted ADR is governance history. Material relaxation, removal of state scope, change to exactly-one cardinality, weakening of complete domain coverage, permission to roll county Focus outputs into state evidence, or re-collapse of geographic and system state requires:

- a successor ADR;
- reciprocal supersession links;
- matching ADR index update;
- compatibility analysis;
- migration for scope registers, contracts, schemas, fixtures, validators, data, clients, and releases;
- correction/withdrawal analysis for released state claims;
- rollback at least as strong as the rule being changed.

Do not flip an accepted ADR back to `proposed`, delete its evidence trail, remove coverage entries to make validation pass, or recreate a public bypass.

### Implemented state-scope rollback

- **Before release:** preserve candidate history; demote, hold, migrate, or retire transparently.
- **After release:** issue governed withdrawal/rollback records, retain immutable artifacts and evidence, update aliases atomically, invalidate caches, and publish correction notices where required.
- **Placement rollback:** restore the exact pre-migration tree and references; do not leave both old and new homes writable.
- **Scope-registration rollback:** preserve identity history and aliases; do not silently reuse `kansas-state` for a different object.

[Back to top](#top)

---

<a id="verification-checklist"></a>

## Verification checklist

### Current revision

- [x] Current `main` SHA recorded.
- [x] ADR ID, exact filename, H1, and index status verified.
- [x] ADR-0029 acceptance and Directory Rules v2 adopted blob verified.
- [x] Directory Rules v2 scope, one-owner, split, hold, migration, and naming rules inspected.
- [x] ADR-0027 current proposed status inspected.
- [x] Singular Focus tree inspected.
- [x] Exact plural Focus tree absence checked.
- [x] Mixed state tree and its state-doctrine companions inspected.
- [x] State index and state template inspected.
- [x] Geographic `kansas-state` lane absence checked in the inspected state tree.
- [x] FocusModePayload semantic contract inspected.
- [x] Focus schema-family and payload-validator exact paths checked.
- [x] County-only Focus index validator inspected.
- [x] Domain-lane machine projection inspected and updated maturity recorded.
- [x] Validator entrypoint and bounded orchestrator inspected.
- [x] Focus mock workflow inspected and its partial proof bounded.
- [x] Drift register checked for Focus state collision coverage.
- [x] Stale v1.2 path authority removed from the proposed decision.
- [x] Geographic and system state terminology separated.
- [x] County-output prohibition remains narrow enough to allow valid county-granular source evidence.
- [x] No implementation, release, or publication claim introduced.
- [ ] Human review completed.
- [ ] ADR accepted.
- [ ] Scope registered.
- [ ] Placement decisions accepted.
- [ ] Structural split/migration completed.
- [ ] Implementation graduated.
- [ ] State release observed.

### Future implementation

- [ ] ADR-0027/ADR-0028 responsibilities reconciled.
- [ ] State scope authority and registration home selected.
- [ ] Mixed state tree split by authority.
- [ ] Canonical targets and compatibility rules accepted.
- [ ] Domain profile accepted and digest-bound.
- [ ] Contracts, schemas, fixtures, and validators agree.
- [ ] State cardinality and profile coverage validate.
- [ ] Direct evidence and transform receipts close.
- [ ] Sensitive lanes fail closed.
- [ ] Governed API/client finite outcomes pass.
- [ ] State/county comparison does not collapse authority.
- [ ] Release, correction, withdrawal, cache, and rollback drills pass.
- [ ] Public clients cannot read candidates or internal stores.

[Back to top](#top)

---

<a id="references"></a>

## References

| Reference | Relationship and current boundary |
|---|---|
| [`docs/adr/README.md`](./README.md) | ADR operating contract; merge does not accept a decision |
| [`docs/adr/INDEX.md`](./INDEX.md) | Confirms ADR-0028 proposed and ADR-0029 accepted |
| [ADR-0027](./ADR-0027-county-focus-mode-control-plane.md) | Proposed county-control-plane lineage; not placement authority |
| [ADR-0029](./ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted Directory Rules v2 adoption authority |
| [Directory Rules v2](../doctrine/directory-rules.md) | Adopted placement doctrine and finite placement outcomes |
| [Legacy Focus control README](../focus-mode/README.md) | Singular control-plane doctrine and path lineage |
| [Focus state doctrine README](../focus-mode/state/README.md) | Cross-cutting system-state vocabulary and explicit path ambiguity |
| [Proposed state index](../focus-mode/state/STATE_INDEX.md) | One planned Kansas row with unsupported state-validator claim |
| [Proposed state template](../focus-mode/state/_template/state-build-plan.md) | Geographic state build-plan scaffold |
| [FocusModePayload contract](../../contracts/focus_mode/focus_mode_payload.md) | Proposed county-oriented semantic contract |
| [Focus index validator](../../tools/validators/validate_focus_mode_index.py) | Current county-only validator |
| [Validator entrypoint](../../tools/validate_all.py) | Canonical thin orchestrator entrypoint |
| [Validator orchestrator](../../tools/validators/validate_all.py) | Bounded deterministic registry execution |
| [Domain-lane machine projection](../../control_plane/domain_lane_register.yaml) | Populated 13-entry proposed machine projection |
| [Drift Register](../registers/DRIFT_REGISTER.md) | Existing drift ledger; Focus state collision not yet recorded |
| [Focus mock workflow](../../.github/workflows/focus-mock-test.yml) | Deterministic finite-envelope/MockAdapter proof with no accepted Focus command |

[Back to top](#top)

---

<a id="revision-history"></a>

## Revision history

| Version | Date | Summary |
|---|---|---|
| v0.1 | 2026-05-23 | Initial proposed ADR coupling `-state`, one `kansas-state` lane, 13-domain coverage, no county roll-up, migration, acceptance, and rollback. |
| v0.2 | 2026-07-24 | Re-grounded the decision against the pre-ADR-0029 repository; surfaced singular/plural drift, unsupported state index, absent state lane/schemas/payload validator, county-only validator, empty machine domain register, and Focus runtime hold; refined domain IDs, coverage dispositions, state/county evidence rules, and migration waves. |
| v0.3 | 2026-08-14 | Rebased the ADR on current `main` and accepted ADR-0029/Directory Rules v2; removed stale v1.2 path assertions; separated geographic state scope from finite-outcome/lifecycle/review/payload/revocation state; classified the mixed state tree as a required `SPLIT`; recorded the populated-but-proposed 13-entry domain projection, real validator orchestrator, and bounded MockAdapter proof; preserved absent state schemas, payload validator, geographic lane, and release as implementation holds; updated validation, migration, risk, incident, and rollback discipline. |

---

<sub>This ADR remains proposed. A Kansas state Focus composition is a governed geographic scope, not a root, domain, lifecycle stage, review status, payload freshness state, or source of truth. Every material claim must resolve admissible evidence or abstain; sensitive content fails closed; public clients use governed surfaces; and no statewide umbrella may outrank its evidence, policy, review, release, correction, or rollback records.</sub>
