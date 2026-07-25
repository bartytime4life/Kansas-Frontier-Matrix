<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0028-state-scale-focus-mode-scope
title: ADR-0028 — State-scale Focus Mode scope and cross-scale domain-coverage rule
type: adr
adr_id: ADR-0028
version: v0.2
status: proposed
effective_decision_status: proposed
owners:
  - "NEEDS VERIFICATION — architecture decision owner"
  - "NEEDS VERIFICATION — Focus Mode and control-plane steward"
  - "NEEDS VERIFICATION — Directory Rules steward"
  - "NEEDS VERIFICATION — domain-registry, contracts, schemas, policy, sensitivity, evidence, release, correction, rollback, validation, UI, and docs stewards"
reviewers_required:
  - Architecture steward
  - Docs steward
  - Focus Mode and control-plane steward
  - Directory Rules steward
  - Domain-registry steward
  - Contracts and schemas stewards
  - Policy and sensitivity steward
  - Evidence and release steward
  - Correction and rollback steward
  - Governed API and Explorer Web maintainers
  - Validation and CI steward
  - At least one affected domain steward
created: 2026-05-23
updated: 2026-07-24
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
current_path: "docs/adr/ADR-0028 — State-scale Focus Mode scope.md"
supersedes: []
superseded_by: null
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 8df9bd2b723c0d4cf88a32d357ea8c70895f1177
  target_prior_blob: 09605b531116857e741e2f2cb8f8a9177c224734
  adr_index_blob: cf08fae322ac53426f7394d97897fdb942253049
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  adr_0027_blob: b1894474f8dc402f5d47abea8dd2d0cf1d0571b8
  legacy_focus_control_readme_blob: 008cf7b3496fdfe56ff3a23b12cb470c27dcf76e
  legacy_county_index_blob: ba888a806148866501bf1f6c730a7b411ca67277
  legacy_state_index_blob: 8d0b631bd53e6af3747417ee813c791fc67a9c3c
  legacy_state_template_blob: e7d2f2542ddcfee416c4d3fd709e972ff193d446
  focus_mode_payload_contract_blob: 7fe687d587cd60dafd6e3fa34306cd58fd125c73
  focus_mode_index_validator_blob: 89391d75680e859dddf3696b9b782369f364c73e
  domain_lane_register_blob: 7cd641d99e1e4e3b3823f608d63679a438590c3a
  domain_lane_machine_register_blob: 81b23beb3178b59d5c1fdb50edbc9f98f8664930
  drift_register_blob: 5c5078b93c467e66f4cc8b86a7a696dbce5ae7e0
  focus_mock_workflow_blob: aa97ee5ad099d1e10922d037061abde17ceb3a93
  canonical_focus_modes_readme_at_base: absent
  focus_mode_payload_schema_at_base: absent
  layer_registry_entry_schema_at_base: absent
  focus_mode_payload_validator_at_base: absent
  kansas_state_lane_at_base: absent
inspection_boundary: >
  Current-session GitHub reads and bounded repository search covering the ADR inventory,
  Directory Rules, ADR-0027, this ADR, the actual singular Focus Mode control-plane README,
  county and state indexes, state template, FocusModePayload semantic contract, focus-mode
  index validator, domain-lane human and machine registers, drift register, Focus mock
  readiness workflow, and exact checks for the canonical plural README, FocusModePayload
  schemas, payload validator, and Kansas state lane. No complete repository clone, accepted
  ReviewRecord, Directory Rules amendment, structural migration, schema or policy execution,
  state Focus payload, state EvidenceBundle, source admission, governed API Focus request,
  map render, release manifest, correction, rollback, deployment, or production publication
  was exercised.
source_lineage:
  - docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md
  - docs/registers/DOMAIN_LANE.md
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/adr/ADR-0003-policy-singular-is-canonical-(policies-is-compatibility).md
  - docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - docs/adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md
  - docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - docs/adr/ADR-0018-promotion-gate-sequence.md
  - docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0024-steward-separation-of-duties-for-release.md
  - docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - docs/adr/ADR-0027-county-focus-mode-control-plane.md
  - docs/doctrine/directory-rules.md
  - docs/focus-mode/README.md
  - docs/focus-mode/counties/COUNTY_INDEX.md
  - docs/focus-mode/state/STATE_INDEX.md
  - docs/focus-mode/state/_template/state-build-plan.md
  - docs/focus-mode/counties/_template/county-build-plan.md
  - contracts/focus_mode/focus_mode_payload.md
  - tools/validators/validate_focus_mode_index.py
  - docs/registers/DOMAIN_LANE.md
  - control_plane/domain_lane_register.yaml
  - docs/registers/DRIFT_REGISTER.md
  - .github/workflows/focus-mock-test.yml
tags: [kfm, adr, focus-mode, state-scale, kansas-state, domain-coverage, control-plane, directory-rules, evidence, sensitivity, release, rollback, cite-or-abstain]
notes:
  - "v0.2 is a same-path repository-grounded modernization. It preserves source and effective status proposed; it does not accept ADR-0028 or authorize state-scale implementation."
  - "The canonical ADR index uniquely assigns ADR-0028 to this exact filename, including the em dash and spaces."
  - "Directory Rules currently permits only county, region, and corridor suffixes and names docs/focus-modes/ as the canonical human lane."
  - "Current Focus materials are under legacy singular docs/focus-mode/; the canonical plural README and kansas-state lane are absent."
  - "The state index and template exist as inert proposed scaffolds, but the current validator is county-only and does not parse the state index."
  - "The proposed 13-domain profile now uses the canonical lane IDs from docs/registers/DOMAIN_LANE.md rather than draft aliases such as atmosphere_air or roads_rail."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0028 — State-scale Focus Mode scope and cross-scale domain-coverage rule

> **Proposed decision.** KFM may add `state` as a Focus Mode scope class and define exactly one Kansas state-scale composition, `kansas-state`, only through an accepted amendment to the Focus Mode placement contract and a governed migration to the canonical control-plane home. Every Focus Mode at every accepted scope must record an explicit disposition for every domain in the pinned canonical domain-set profile. A Kansas state composition must establish its own evidence, policy, release, correction, and rollback chain; it must not treat county Focus Mode outputs as authoritative source inputs.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![ADR ID: confirmed](https://img.shields.io/badge/ADR--0028-confirmed-0969da?style=flat-square)](#current-repository-evidence)
[![Directory scopes: 3](https://img.shields.io/badge/Directory%20Rules-county%20%7C%20region%20%7C%20corridor-f59e0b?style=flat-square)](#current-repository-evidence)
[![Control plane: conflicted](https://img.shields.io/badge/control%20plane-singular%20legacy%20%2F%20plural%20canonical-b42318?style=flat-square)](#current-enforcement-maturity)
[![State validator: absent](https://img.shields.io/badge/state%20validator-absent-b42318?style=flat-square)](#current-enforcement-maturity)
[![Schemas: absent](https://img.shields.io/badge/focus%20schemas-absent-b42318?style=flat-square)](#current-enforcement-maturity)
[![Implementation: hold](https://img.shields.io/badge/implementation-HOLD-b42318?style=flat-square)](#current-enforcement-maturity)
[![Publication effect: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **Identity is confirmed; acceptance is not.** [`docs/adr/INDEX.md`](./INDEX.md) uniquely assigns `ADR-0028` to this exact file and records both source and effective status as `proposed`. Editing, validating, merging, or referencing this Markdown does not accept the decision.

> [!CAUTION]
> **The repository is internally inconsistent and remains pre-acceptance.** Directory Rules names canonical `docs/focus-modes/<area>-<scope>/` and allows only `-county`, `-region`, and `-corridor`. Actual Focus control-plane materials are stored under legacy singular `docs/focus-mode/`. The state index marks `kansas-state` as planned even though the lane is absent, and it claims validator support that the current county-only validator does not provide.

> [!WARNING]
> **Coverage does not mean “publish data for every domain.”** A Focus Mode satisfies the cross-domain rule by recording exactly one reviewed disposition for every domain in the pinned domain-set profile: `populated`, `abstain`, or `deny` at release. Candidate work may use `hold`, but `hold`, missing entries, unregistered aliases, and unresolved domain-set identity block release.

> [!NOTE]
> **No-roll-up does not ban county-granular source records.** A state composition may transform authoritative source records that are organized by county, and it may share underlying sources or EvidenceBundles with county compositions when scope and time support it. What it must not do is use released or candidate county **Focus Mode outputs** as the authoritative evidence chain for a statewide claim.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Context](#context) · [Decision](#proposed-decision) · [Domain profile](#proposed-domain-set-and-coverage-profile) · [State/county relation](#state-and-county-evidence-relationship) · [Placement](#proposed-placement-and-migration-boundary) · [Authority](#authority-and-publication-boundary) · [Outcomes](#coverage-dispositions-and-runtime-outcomes) · [Current evidence](#current-repository-evidence) · [Maturity](#current-enforcement-maturity) · [Validation](#proposed-validation-and-negative-tests) · [Convergence](#implementation-and-convergence-plan) · [Acceptance](#acceptance-gates) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Risks](#risk-and-open-question-ledger) · [Migration](#migration-and-compatibility) · [Incident](#incident-correction-and-rollback) · [Rollback](#rollback-and-supersession) · [Checklist](#verification-checklist) · [References](#references) · [History](#revision-history)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0028` — unique and confirmed in [`INDEX.md`](./INDEX.md) |
| **Tracked path** | `docs/adr/ADR-0028 — State-scale Focus Mode scope.md` |
| **Source metadata** | `proposed` |
| **Effective decision status** | `proposed` |
| **Decision class** | Directory Rules amendment, Focus Mode scope grammar, canonical control-plane placement, cross-scale domain coverage, evidence composition, release, and rollback |
| **Current Directory Rules scope** | `county`, `region`, `corridor` |
| **Proposed added scope** | `state` |
| **Proposed state instance** | Exactly one Kansas lane: `kansas-state` |
| **Current repository posture** | Legacy singular control-plane scaffolds, county-only validator, missing schemas/payload validator, no state lane, no state release |
| **Implementation effect of this revision** | Documentation only |
| **Release/publication effect** | None |
| **Supersedes / superseded by** | None / none |
| **Relationship to ADR-0027** | ADR-0027 proposes canonical control-plane naming and migration; ADR-0028 proposes the state scope and cross-scale coverage profile. Both remain proposed. |

### Acceptance versus implementation graduation

Three states must remain visible:

1. **ADR acceptance** would approve the `state` scope, `kansas-state` cardinality, domain-coverage rule, evidence-independence rule, and migration responsibilities.
2. **Directory Rules effectiveness** would require the accepted ADR, ADR index, and Directory Rules amendment to land together in one reviewed change or atomic merge group.
3. **Implementation graduation** would require canonical path convergence, accepted domain-set identity, semantic contracts, closed schemas, non-vacuous fixtures, state-aware validators, executable Focus runtime tests, governed API integration, a complete Kansas state lane, release evidence, correction, and rollback drills.

This one-file revision performs none of those transitions.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This revision is grounded in repository bytes at `main@8df9bd2b723c0d4cf88a32d357ea8c70895f1177`.

| Evidence surface | CONFIRMED current state | What remains unproved |
|---|---|---|
| ADR inventory | ADR-0028 uniquely maps to this exact filename; source/effective status `proposed` | Acceptance |
| Directory Rules §6.7 | Canonical docs pattern is `docs/focus-modes/<area>-<scope>/`; allowed suffixes are county, region, corridor | State scope or canonical state lane |
| ADR-0027 | Proposes plural canonical control plane and singular-to-plural migration | Acceptance or migration |
| Actual control README | File exists at legacy `docs/focus-mode/README.md`, while its H1 and prose claim `docs/focus-modes/` | Canonicality or migration completion |
| Canonical plural README | `docs/focus-modes/README.md` not found | Implemented canonical control plane |
| County index | Exists under legacy `docs/focus-mode/counties/`; now functions mainly as a collision register | Validator-compatible canonical county control plane |
| State index | Exists under legacy `docs/focus-mode/state/`; marks `kansas-state` planned | Valid state index or implemented lane |
| Kansas state lane | `docs/focus-mode/state/kansas-state/README.md` not found | Any state-lane content or readiness |
| State template | Exists under legacy `docs/focus-mode/state/_template/` and declares itself blocked | Accepted template or validator support |
| Focus index validator | County-only; `VALID_SCOPES = ("county", "region", "corridor")`; expects `docs/focus-modes/COUNTY_INDEX.md` | State index parsing, state cardinality, domain coverage |
| FocusModePayload contract | Proposed county-oriented semantic contract; scope enum names county, region, corridor | State semantics or accepted domain coverage |
| Focus schemas | Declared `focus_mode_payload` and `layer_registry_entry` schema paths not found | Machine shape or compatibility |
| Payload validator | `tools/validators/validate_focus_mode_payload.py` not found | Payload validation |
| Human domain register | Lists 13 domain lanes and their current lane IDs | Accepted machine domain-set version |
| Machine domain register | `entries: []`, status proposed | Executable domain identity/profile |
| Focus mock workflow | Explicit readiness hold; no accepted runtime, fixtures, or command | Working Focus flow or state-scale response |
| State release | No state lane, payload, release manifest, correction, or rollback was verified | State publication |

### Truth labels

- **CONFIRMED** — verified from repository bytes or supplied governing doctrine.
- **PROPOSED** — candidate decision, field, path role, migration, or implementation profile.
- **CONFLICTED** — current repository surfaces assign incompatible names, homes, shapes, or claims.
- **HOLD** — current evidence deliberately blocks graduation.
- **NEEDS VERIFICATION** — a concrete check remains open.
- **UNKNOWN** — evidence does not support a stronger conclusion.

### Out of scope

This ADR does not:

- create or populate `kansas-state`;
- accept ADR-0027 or choose a migration implementation on its behalf;
- alter the canonical 13-domain membership;
- define final JSON Schema field names or version numbers;
- ingest statewide data or activate sources;
- authorize public emergency, legal, title, medical, regulatory, or life-safety advice;
- change the trust membrane, lifecycle, source-role, sensitivity, release, correction, or rollback laws;
- merge, deploy, release, or publish anything.

[Back to top](#top)

---

<a id="context"></a>

## Context

A Focus Mode is a cross-cutting, evidence-bounded composition for one spatial frame. It is not a domain and not a root. The current placement contract recognizes county, region, and corridor frames. Kansas-wide questions and statewide source families can be represented as ordinary layers or analytical objects, but the repository has no accepted state-scale Focus Mode grammar or governed state lane.

The original proposal correctly identifies two distinct governance needs:

1. **State scope.** A whole-Kansas composition can provide an inspectable statewide frame with its own evidence, policy, release, correction, and rollback lineage.
2. **No silent domain omission.** Every Focus Mode should visibly address each canonical domain lane, even when the correct outcome is abstention or denial.

The repository has already accumulated proposed state-control documents, but they do not create authority:

- the state index and template live under a noncanonical singular path;
- the state index claims one planned lane that does not exist;
- the county-only validator does not parse the state index;
- the required machine schemas and payload validator are absent;
- the machine domain registry is empty;
- the Focus runtime remains a readiness hold.

The decision must therefore govern convergence before it governs state content.

### Why state is a scope, not a domain

`state` describes the spatial bound of the composition. It does not create a new thematic domain. Hydrology, soil, habitat, archaeology, and the other domain lanes remain segments inside responsibility roots. Cross-cutting analytical families such as spatial foundation or Frontier Matrix objects may appear inside a state composition without replacing its Focus Mode release boundary.

### Why the coverage rule is cross-scale

Silent omission is not uniquely a state problem. A county, region, corridor, or state Focus Mode can appear complete while omitting a domain that lacks admissible evidence or is blocked by policy. The correct cure is an explicit disposition for every domain, not a requirement to fabricate a layer.

[Back to top](#top)

---

<a id="proposed-decision"></a>

## Proposed decision

Upon reviewed acceptance and the coordinated Directory Rules amendment:

1. **Add `state` to the Focus Mode scope-class enumeration.** The accepted values become `state`, `county`, `region`, and `corridor`.
2. **Define one Kansas state instance.** The only state-scale area in current KFM scope is `kansas-state`. Time periods, historical frames, themes, releases, and UI presets are versions or views of that lane—not sibling state lanes.
3. **Use the canonical control-plane home selected by governing doctrine.** Under current Directory Rules, the proposed docs lane is `docs/focus-modes/kansas-state/`. Existing singular `docs/focus-mode/` materials are migration inputs, not parallel authority.
4. **Require an explicit domain-set reference.** Every Focus Mode candidate and payload must identify the exact accepted domain-set profile against which coverage is evaluated.
5. **Require complete domain coverage records.** Every domain ID in the referenced profile appears exactly once with a reviewed disposition and owner. Missing, duplicate, unregistered, aliased, or unresolved entries fail validation.
6. **Permit release dispositions `populated`, `abstain`, or `deny`.** Candidate work may temporarily use `hold`, but `hold` blocks release.
7. **Keep state evidence independent from county Focus Mode outputs.** A state claim cannot cite a county Focus Mode payload, layer registry, generated summary, or release as its root evidence. It must resolve source and evidence support directly.
8. **Permit shared underlying evidence where valid.** State and county claims may share authoritative sources, records, EvidenceRefs, or EvidenceBundles when their spatial and temporal scope supports both claims. Each composition still carries its own claim, policy, review, release, correction, and rollback references.
9. **Preserve sensitivity across scales.** Aggregation may support an approved public-safe derivative, but state scale never automatically lowers rights, sovereignty, living-person, DNA, archaeology, rare-species, infrastructure, or alert-authority restrictions.
10. **Make acceptance atomic.** ADR status/index updates, Directory Rules amendment, control-plane migration decision, and rollback plan must be reviewed together. No state lane becomes canonical merely because a template, index row, schema, or validator exists.
11. **Keep generation subordinate to evidence.** Focus Mode AI surfaces may interpret only governed, release-resolved context and must return bounded finite outcomes.
12. **Keep release separate from composition.** A complete lane, payload, or coverage matrix is not publication. Public state-scale claims require the normal governed release path.

### Proposed Directory Rules amendment

The accepted amendment should update §6.7 without inventing a new root:

- definition: “state-, county-, region-, or corridor-scale proof slice”;
- docs suffix enumeration: `-state`, `-county`, `-region`, `-corridor`;
- one-area rule: exactly one Kansas state lane;
- anti-patterns: county-output roll-up as state evidence, silent domain omission, and parallel singular/plural control planes;
- change history and drift records;
- migration and rollback references to this ADR.

Exact wording remains a Directory Rules change reviewed under its own authority.

[Back to top](#top)

---

<a id="proposed-domain-set-and-coverage-profile"></a>

## Proposed domain-set and coverage profile

### Candidate core domain IDs

The current human Domain Lane Register identifies these 13 canonical lane IDs:

| # | Domain ID | Scope summary |
|---|---|---|
| 1 | `hydrology` | Watersheds, streamflow, flood and water context |
| 2 | `soil` | Soil map units, components, and properties |
| 3 | `habitat` | Habitat patches, ecological systems, stewardship context |
| 4 | `fauna` | Species occurrence and range context |
| 5 | `flora` | Vegetation, rare plants, ethnobotanical context |
| 6 | `agriculture` | Crop, yield, and producer-adjacent aggregate context |
| 7 | `geology` | Geologic units, lithology, resources, subsurface context |
| 8 | `atmosphere` | Weather, climate, and air-quality context |
| 9 | `hazards` | Hazard observations and cited warning context |
| 10 | `roads-rail-trade` | Road, rail, route, corridor, and trade-network context |
| 11 | `settlements-infrastructure` | Settlements, municipalities, townsites, infrastructure |
| 12 | `archaeology` | Cultural periods, surveys, and protected site context |
| 13 | `people-dna-land` | Person, genealogy, DNA, land, title, and sovereignty context |

These are candidate IDs for the first domain-set profile. They remain subject to accepted human/machine register reconciliation. Draft aliases such as `atmosphere_air` and `roads_rail` must not become a second vocabulary.

### Versioned profile requirement

A future payload should reference a versioned domain set rather than assuming “13” forever.

Illustrative semantic shape:

```yaml
domain_set_ref: kfm://domain-set/core-v1
coverage:
  - domain_ref: hydrology
    disposition: populated
    owner_ref: kfm://steward/hydrology
    evidence_refs:
      - kfm://evidence/example
    policy_decision_refs:
      - kfm://policy-decision/example
  - domain_ref: archaeology
    disposition: deny
    owner_ref: kfm://steward/archaeology
    reason_codes:
      - sensitive_exact_location
```

The final contract/schema may use a map or an array, but it must enforce:

- one resolved `domain_set_ref`;
- exactly one entry for every domain in that set;
- no extra or alias domain IDs;
- stable identity for each entry;
- explicit owner and reason for non-populated entries;
- evidence and release support for populated entries;
- policy support for denied entries;
- review timing and next-review posture for abstentions;
- no `hold` at release.

### Why `not_applicable` is not a release disposition

Every canonical domain is applicable to the coverage question: “What is the disposition for this domain at this area and scale?” A domain with no admissible claim uses `abstain`; a domain blocked by policy uses `deny`. `not_applicable` would recreate silent omission under a different label.

### Domain-set changes

Adding, removing, renaming, splitting, or merging a canonical domain lane requires its own accepted governance change. A new domain-set profile may then supersede the prior profile through explicit compatibility and migration. Existing released Focus Modes retain the domain-set reference under which they were validated.

[Back to top](#top)

---

<a id="state-and-county-evidence-relationship"></a>

## State and county evidence relationship

### Independent composition rule

A state Focus Mode is not a collection of county Focus Mode outputs. The following are forbidden as the sole or root support for a statewide claim:

- county `FocusModePayload` objects;
- county layer registries or build plans;
- county-generated summaries or AI responses;
- county release manifests treated as source evidence;
- a spatial union of county public layers with no new source/evidence processing;
- “all counties agree” without a direct statewide evidence bundle and time profile.

### Allowed shared support

The following may be shared when scope, source role, rights, sensitivity, time, and geometry support it:

- a statewide source descriptor;
- authoritative records whose native organization is county-by-county;
- an EvidenceBundle whose support explicitly covers both state and county claims;
- a versioned statewide transformation from county-granular source records;
- shared taxonomy, identity, boundary, or temporal reference objects.

The state composition must emit its own:

- build/run receipt;
- claim and EvidenceRef resolution;
- transformation and aggregation record where applicable;
- policy and sensitivity decision;
- coverage dispositions;
- promotion/release decision;
- correction and rollback target.

### Cross-scale crosswalk

An optional cross-scale crosswalk may describe relationships between state and county claims, layers, sources, boundaries, and releases. It is a navigation and comparison object. It must not become the evidence root or silently synchronize incompatible releases.

[Back to top](#top)

---

<a id="proposed-placement-and-migration-boundary"></a>

## Proposed placement and migration boundary

### Directory Rules basis

This ADR adds no root. The proposed state composition follows the current §6.7 responsibility-root pattern.

| Responsibility | Proposed canonical state-scale home | Current evidence boundary |
|---|---|---|
| Human control plane | `docs/focus-modes/STATE_INDEX.md`, `docs/focus-modes/_template/state-build-plan.md`, `docs/focus-modes/kansas-state/` | Canonical plural root absent; legacy singular scaffolds exist |
| Semantic Focus contract | `contracts/focus_mode/` | County-oriented proposed contract exists |
| Machine schemas | `schemas/contracts/v1/focus_mode/` | Declared schemas absent |
| Fixtures | `fixtures/focus_modes/kansas/{valid,invalid}/` | State fixtures unverified |
| Explorer UI | `apps/explorer-web/src/focus-modes/kansas/` | Explorer/Focus implementation unverified |
| Validators | `tools/validators/` | County-only index validator; payload validator absent |
| Catalog/source slices | `data/catalog/sources/kansas/`, `data/catalog/stac/kansas/` where justified | Inventory unknown |
| Published carriers | `data/published/layers/kansas/`, `data/published/api_payloads/focus-modes/kansas.json` | No state payload/release verified |
| Registry view | `data/registry/sources/kansas/` only if required | Machine domain register empty; source inventory unknown |
| Release candidate | `release/candidates/kansas-focus-mode/` | Proposed naming; no candidate verified |
| Release manifest | Accepted release-manifest responsibility home | Singular/plural manifest-path conflict remains outside this ADR |
| Pipeline composition | `pipeline_specs/focus_modes/kansas/` only if a distinct declarative composition is justified | Absent/unverified |
| Examples | `examples/focus-modes/kansas/` | Examples remain non-authoritative |
| Policy override | Accepted policy sublane only when a state-specific override is justified | Default should inherit cross-domain policy |

### Singular/plural migration rule

The current `docs/focus-mode/` tree is not silently promoted. A migration must:

1. inventory every tracked file and inbound link;
2. classify canonical content, compatibility redirects, generated artifacts, and obsolete claims;
3. move or rewrite state/county control-plane materials into `docs/focus-modes/`;
4. preserve stable history and add migration notes;
5. update all links, validator inputs, workflows, and docs;
6. prevent dual-authority editing;
7. retain a bounded compatibility redirect only when needed;
8. verify no payload, release, or public state changed;
9. provide a one-commit or otherwise reversible rollback target.

ADR-0027 and this ADR must be reconciled so one accepted decision owns the migration sequence and neither creates a second control plane.

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

State scope does not turn a Focus Mode into a source of truth. The state composition remains downstream of:

- source identity and source-role decisions;
- rights, sovereignty, consent, and sensitivity;
- evidence and provenance;
- contracts and schemas;
- deterministic transforms and receipts;
- policy and independent review;
- promotion and release;
- correction, withdrawal, supersession, and rollback.

A statewide map, count, summary, layer, domain matrix, generated explanation, or “all counties” aggregate is a carrier or projection. It does not independently prove a claim.

Public clients must receive state Focus results through the Governed API or an approved released-static profile. They must not read Focus control-plane Markdown, canonical data stores, proof stores, release internals, model runtimes, or candidate outputs directly.

State-scale content must not be presented as emergency alert authority, legal/title advice, access permission, regulatory direction, medical advice, or definitive living-person or DNA interpretation.

[Back to top](#top)

---

<a id="coverage-dispositions-and-runtime-outcomes"></a>

## Coverage dispositions and runtime outcomes

### Composition-level coverage dispositions

| Disposition | Meaning | Release effect |
|---|---|---|
| `populated` | One or more governed layer/claim entries exist with evidence, policy, sensitivity, owner, time, and release support | Eligible when all other gates pass |
| `abstain` | No sufficiently supported or admissible public claim is available for this domain/area/scale; reason and review posture are recorded | Eligible as explicit cite-or-abstain closure |
| `deny` | Policy, rights, sovereignty, sensitivity, or safety prohibits public exposure; no protected payload reaches the client | Eligible as explicit fail-closed closure |
| `hold` | Evidence, owner, policy, schema, review, release, or migration is unresolved | Candidate only; blocks release |

Missing entries, unknown aliases, invalid states, validator errors, and contradictory records block release.

### Runtime outcomes

A public Focus request still resolves to exactly one finite runtime outcome:

| Outcome | Client meaning |
|---|---|
| `ANSWER` | A bounded response is supported and allowed under the current state release |
| `ABSTAIN` | Evidence, scope, freshness, or admissibility is insufficient |
| `DENY` | Policy, rights, sensitivity, role, or release state blocks exposure |
| `ERROR` | The request could not be processed safely or deterministically |

A domain coverage disposition does not predetermine every query outcome. A `populated` domain may still abstain or deny for a specific question. A `deny` disposition never permits client-side recovery of the blocked payload.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | Current verified state | Safe conclusion |
|---|---|---|
| ADR-0028 | Exact indexed file; source/effective `proposed` | Decision not accepted |
| Directory Rules | Focus definition is county/region scale; suffixes county/region/corridor; plural docs home | State scope not canonical |
| ADR-0027 | Proposed plural control-plane migration | Naming/migration not accepted |
| `docs/focus-mode/README.md` | Exists at singular path but labels itself `docs/focus-modes/`; state extension marked proposed | Documentary/path conflict |
| `docs/focus-modes/README.md` | Not found | Canonical control-plane README absent |
| County index | Legacy singular path; collision-prevention semantics; validator compatibility needs verification | Not a confirmed canonical validator input |
| State index | Legacy singular path; one `planned` row; says validator parses it | Inert proposal and overclaim |
| `kansas-state` lane | Not found at checked legacy path; canonical plural tree also absent | Planned status unsupported |
| State template | Legacy singular path; blocked on ADR acceptance | Design scaffold only |
| FocusModePayload contract | County-oriented scope and paths; references absent schema | Semantic draft requires convergence |
| FocusModePayload schema | Not found | No machine payload shape |
| LayerRegistryEntry schema | Not found | No machine domain/scale shape |
| Focus payload validator | Not found | No payload validation |
| Focus index validator | 105-county parser; valid scopes county/region/corridor; expects plural root | No state or domain-coverage enforcement |
| Human Domain Lane Register | Lists 13 lane IDs | Candidate narrative domain-set source |
| Machine domain register | Proposed with `entries: []` | Domain-set identity not executable |
| Drift register | Exists but does not record the Focus singular/plural/state contradictions inspected here | Drift registration incomplete |
| Focus mock workflow | Explicit `WORKFLOW_HOLD`; no accepted runtime/fixtures/command | No executable Focus flow |
| State release/publication | No state lane or state release evidence verified | None |

### Confirmed absent at checked paths

- `docs/focus-modes/README.md`
- `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json`
- `schemas/contracts/v1/focus_mode/layer_registry_entry.schema.json`
- `tools/validators/validate_focus_mode_payload.py`
- `docs/focus-mode/state/kansas-state/README.md`

Absence at checked paths does not prove no conceptually related material exists elsewhere. It proves that the paths claimed by the current Focus documentation are not implementation-complete.

[Back to top](#top)

---

<a id="current-enforcement-maturity"></a>

## Current enforcement maturity

| Capability | Current state |
|---|---|
| ADR identity/status | `CONFIRMED / proposed` |
| State scope in Directory Rules | Not present |
| Canonical Focus control-plane home | `CONFLICTED` |
| Canonical plural control plane | Absent |
| Legacy singular control plane | Present, proposed, internally inconsistent |
| State index | Present but unsupported/inert |
| State lane | Absent |
| State template | Present as blocked scaffold |
| Domain-set identity | Human draft register only; machine entries empty |
| Domain-coverage contract | Proposed in prose only |
| FocusModePayload semantic contract | County-oriented draft |
| FocusModePayload schema | Absent |
| LayerRegistryEntry schema | Absent |
| State-aware index validator | Absent |
| Focus payload validator | Absent |
| State fixtures/negative tests | Not established |
| Mock Focus runtime | `WORKFLOW_HOLD` |
| Governed API state Focus route | Not established |
| State evidence/release/correction/rollback | Not established |
| Production state publication | None |

**Overall maturity: `DESIGN DRIFT / HOLD`.** The repository contains useful state-scale design scaffolds, but it does not contain a canonical, machine-enforced, release-capable state Focus Mode.

[Back to top](#top)

---

<a id="proposed-validation-and-negative-tests"></a>

## Proposed validation and negative tests

Validation must be deterministic, non-vacuous, local/offline-capable for core checks, and fail closed.

### Required validation families

| Family | Required checks |
|---|---|
| ADR/doctrine | ADR accepted; Directory Rules and index agree; no stale proposed text claims authority |
| Placement | One canonical control plane; no dual singular/plural authority; state lane at canonical path |
| State cardinality | Exactly one current Kansas state lane; no historical/modern sibling lanes |
| Domain set | Resolved accepted profile; exact registered IDs; no aliases, duplicates, or extras |
| Coverage | One disposition per domain; populated support; abstain reason; deny policy; no release hold |
| Evidence | State claim resolves direct support; no county Focus output as root evidence |
| Scope/time | State geometry, valid time, source cadence, aggregation, and transform support the claim |
| Sensitivity | Exact protected content never becomes public through aggregation or styling |
| Schemas/contracts | Semantic and machine shapes agree; compatible version declared |
| Fixtures | Non-empty valid and invalid state/cross-scale cases |
| Runtime | Governed API and Focus client preserve finite outcomes and obligations |
| Release | Promotion, release, correction, withdrawal, rollback, and cache behavior resolve |
| Public boundary | No direct internal-store or model-runtime path |

### Stable reason-code families

- `state_scope_not_accepted`
- `focus_control_plane_path_conflict`
- `canonical_focus_control_plane_missing`
- `state_index_unsupported`
- `state_index_lane_mismatch`
- `state_lane_missing`
- `multiple_state_lanes`
- `domain_set_unresolved`
- `domain_set_version_mismatch`
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
- `sensitivity_review_missing`
- `focus_schema_missing`
- `focus_payload_validator_missing`
- `state_fixture_inventory_vacuous`
- `release_manifest_unresolved`
- `rollback_target_unresolved`
- `public_state_route_unverified`

### Required negative fixtures

At minimum:

- `state` used before ADR/Directory Rules acceptance;
- canonical plural control plane absent;
- legacy singular path treated as new authority;
- state index row says planned but lane does not exist;
- more than one state lane;
- `kansas-historical-state` created as a sibling instead of a release/time view;
- wrong `scale_class`;
- missing domain-set reference;
- old aliases `atmosphere_air` or `roads_rail` used instead of registered IDs;
- one domain missing;
- one domain duplicated;
- extra unregistered domain;
- `hold` at release;
- abstain without reason, owner, or next review;
- deny without policy/review reference;
- populated without evidence or release support;
- archaeology/rare-species/living-person/DNA/infrastructure exact data made public by state aggregation;
- state claim supported only by county Focus Mode output;
- state claim built from county-granular authoritative records with a new direct evidence chain — **valid positive case**;
- cross-scale crosswalk treated as evidence;
- stale or temporally incompatible county records aggregated without an explicit statewide time profile;
- validator reports pass with zero state fixtures or zero lane files;
- public client reads a state candidate or internal proof/control-plane file.

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

Use small, dependency-ordered, reversible waves. Do not build the state lane inside the legacy path and promise to migrate later.

### Wave A — Decision and doctrine convergence

1. Review and revise ADR-0028.
2. Reconcile ADR-0027 and ADR-0028 responsibility: one owns canonical control-plane migration; the other extends scope and coverage.
3. In one reviewed acceptance change or atomic merge group:
   - set matching accepted status in ADR/index;
   - amend Directory Rules §6.7;
   - record the structural migration and rollback plan;
   - define the state scope/cardinality and coverage profile;
   - identify accountable owners.
4. Do not claim implementation graduation.

### Wave B — Canonical control-plane migration

1. Inventory `docs/focus-mode/` and all inbound links.
2. Create the Directory-Rules-compliant `docs/focus-modes/` control plane.
3. Migrate README, county index/template, state index/template, and any area lanes.
4. Correct state index from `planned` to `not-started` unless the required lane scaffold exists.
5. Keep at most a bounded redirect/compatibility README at the singular path.
6. Update validator inputs, docs, workflows, and links.
7. Validate no dual authority or data/release change.

### Wave C — Domain-set, contracts, schemas, and fixtures

1. Reconcile the human Domain Lane Register with an accepted machine domain-set profile.
2. Version the FocusModePayload semantic contract.
3. Create closed schemas in the canonical schema home.
4. Define `scale_class`, `domain_set_ref`, coverage entry/disposition, and state-area identity.
5. Add deterministic valid/invalid fixtures, including state/county evidence relationship cases.
6. Add migration fixtures for existing county plans; do not invent a fixed warning deadline before inventory.

### Wave D — Validators and CI

1. Extend or replace the county-only index validator.
2. Parse canonical county and state indexes.
3. Require non-empty state and county inventories for applicable checks.
4. Implement the payload validator.
5. Register validators in the accepted orchestration path.
6. Add policy, runtime-proof, API, UI, and release negative tests.
7. Keep all checks read-only until release tooling is separately approved.

### Wave E — Kansas state candidate

1. Create `docs/focus-modes/kansas-state/` only after Waves A–D establish the accepted path and checks.
2. Populate all required lane files.
3. Record all domain coverage entries.
4. Admit direct statewide or scope-valid authoritative sources.
5. Produce evidence, policy, sensitivity, aggregation, and time-profile records.
6. Keep status candidate/draft until every validator and review gate closes.

### Wave F — Runtime, release, and rollback proof

1. Produce a validated state FocusModePayload.
2. Integrate the governed API and Explorer client with finite outcomes.
3. Validate public-safe layers and no-direct-store access.
4. Assemble accountable review, PromotionDecision, ReleaseManifest, correction, and rollback records.
5. Run state/county consistency checks without treating one scale as authority for the other.
6. Exercise withdrawal, cache invalidation, correction, and rollback.
7. Graduate only from observed evidence.

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance gates

### ADR acceptance

- [ ] Architecture, Directory Rules, Focus Mode, domain-registry, schema/contract, policy/sensitivity, evidence/release, correction/rollback, validation, API/UI, and docs reviewers approve.
- [ ] ADR-0027/ADR-0028 control-plane ownership and migration responsibilities are reconciled.
- [ ] The `state` scope definition and exactly-one-`kansas-state` cardinality are approved.
- [ ] The no-county-output-as-state-authority rule and allowed shared-evidence rule are approved.
- [ ] The domain-set reference and candidate canonical lane IDs are approved or explicitly deferred behind a versioned registry gate.
- [ ] Coverage dispositions and release closure rules are approved.
- [ ] Directory Rules amendment text and rollback are included in the same acceptance change or atomic merge group.
- [ ] ADR and index status match; no index edit alone implies acceptance.
- [ ] No state lane, payload, or release is represented as implemented.
- [ ] Legacy singular control-plane materials are classified for migration and not promoted as parallel authority.
- [ ] Release-manifest path conflict is not silently resolved here.

### Implementation graduation

- [ ] Canonical plural control plane exists and singular compatibility is bounded.
- [ ] State and county indexes validate from the canonical root.
- [ ] Domain-set human and machine identities agree.
- [ ] Focus semantic contract and closed schemas agree.
- [ ] State-aware index and payload validators are real and registered.
- [ ] Valid/invalid fixture inventories are non-empty.
- [ ] `kansas-state` has all required lane artifacts.
- [ ] Every domain has a valid release disposition.
- [ ] State evidence chain is direct and time/spatially coherent.
- [ ] Sensitive and rights-constrained lanes fail closed.
- [ ] Governed API/client runtime produces finite outcomes.
- [ ] Release, correction, withdrawal, cache invalidation, and rollback drills pass.
- [ ] No public claim reads candidate or internal stores.
- [ ] Accountable independent review is recorded.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- Gives Kansas-wide questions a governed spatial composition without creating a new root or domain.
- Makes domain omissions visible and reviewable at every scale.
- Preserves cite-or-abstain and deny-by-default rather than forcing empty or fabricated layers.
- Separates statewide evidence from county Focus Mode outputs while allowing valid shared sources.
- Pins coverage to a versioned domain set instead of hard-coded aliases.
- Forces singular/plural control-plane drift to be resolved before state implementation.
- Makes state/county comparison possible without collapsing provenance.
- Creates explicit correction and rollback requirements for a high-visibility umbrella view.

### Costs

- Requires a structural documentation migration and broad link repair.
- Requires domain-set governance, schemas, validators, fixtures, and runtime work.
- Adds review burden to every Focus Mode because coverage must be explicit.
- May block state release when one domain remains unresolved.
- Requires direct statewide evidence and aggregation records rather than convenient county roll-up.
- Adds cross-scale consistency, performance, cache, and temporal-coherence work.
- Requires qualified statewide and domain reviewers.

### Preserved invariants

- Focus Mode remains a composition, not a root or domain.
- EvidenceBundle outranks generated language.
- Public clients use governed interfaces.
- Promotion remains a governed state transition.
- State scale does not reduce sensitivity automatically.
- Receipts, proofs, catalogs, review, release, correction, and publication remain distinct.

[Back to top](#top)

---

<a id="alternatives-considered"></a>

## Alternatives considered

| Alternative | Disposition |
|---|---|
| Keep county/region/corridor only | Rejected as the target design: no governed Kansas-wide Focus composition |
| Use informal statewide context inside each county lane | Rejected: duplicates and drifts statewide claims |
| Treat state scope as a Frontier Matrix/domain object | Rejected: analytical object family is not a spatial release composition |
| Use `-statewide` or `-kansas` suffix | Rejected: `state` is the scope class; `kansas` is the area |
| Permit multiple Kansas state lanes for themes or time | Rejected: use releases, time profiles, views, or stories |
| Derive state output by unioning county Focus outputs | Rejected: weakens evidence, time, and release integrity |
| Ban all county-granular records from state pipelines | Rejected: authoritative statewide sources may be county-granular |
| Split state scope and domain coverage into separate ADRs | Rejected by default: schema, validator, and acceptance behavior are coupled |
| Require every domain to be populated | Rejected: would fabricate or overexpose; explicit abstain/deny is valid closure |
| Add `not_applicable` as a disposition | Rejected: recreates silent omission |
| Hard-code the old draft machine aliases | Rejected: use accepted domain-register IDs and a versioned profile |
| Treat legacy `docs/focus-mode/` as canonical because it exists | Rejected: convention does not outrank Directory Rules |
| Create state lane first and migrate later | Rejected: creates parallel authority and invalidates review evidence |
| Use a cross-scale crosswalk as the state evidence chain | Rejected: crosswalk is navigation, not proof |
| Allow state release while one domain is `hold` | Rejected: unresolved coverage blocks umbrella release |

[Back to top](#top)

---

<a id="risk-and-open-question-ledger"></a>

## Risk and open-question ledger

| Item | Status | Required resolution |
|---|---|---|
| ADR-0027/ADR-0028 responsibility overlap | `CONFLICTED` | Accepted ownership/supersession/cross-reference model |
| Singular vs plural docs home | `CONFIRMED DRIFT` | Governed migration and compatibility plan |
| Control README path/H1 mismatch | `CONFIRMED DRIFT` | Correct after canonical migration |
| State index “planned” without lane | `CONFIRMED DRIFT` | Demote or create lane only after prerequisites |
| State index validator claim | `CONFIRMED DRIFT` | Implement state parser or correct documentation |
| County index semantics vs validator parser | `NEEDS VERIFICATION` | Reconcile collision register and canonical validation index |
| Domain-set machine identity | `HOLD` | Populate/version accepted machine profile |
| Domain ID aliases | `CONFLICTED` | Use registered IDs; migration/crosswalk for old aliases |
| FocusModePayload schema | `CONFIRMED GAP` | Create closed schema at canonical home |
| LayerRegistryEntry schema | `CONFIRMED GAP` | Create closed schema at canonical home |
| Payload validator | `CONFIRMED GAP` | Implement and register |
| Focus runtime/fixtures | `WORKFLOW_HOLD` | Accepted deterministic mock/real profile |
| State source inventory | `UNKNOWN` | Source descriptors, rights, cadence, scope |
| State aggregation methodology | `OPEN` | Transform contract, receipt, uncertainty, time profile |
| State/county claim disagreement | `OPEN` | Comparison and correction policy without authority collapse |
| State sensitivity overrides | `OPEN` | Default none; require policy/review/negative fixture |
| State lane ownership | `NEEDS VERIFICATION` | Accountable steward and backup |
| Release manifest singular/plural home | `CONFLICTED` | Separate accepted responsibility/path decision |
| Mutable state alias/cache | `UNKNOWN` | Atomic release source, invalidation, correction |
| State performance budgets | `NEEDS VERIFICATION` | Correctness-first benchmark |
| Cross-scale crosswalk | `PROPOSED` | Optional semantic contract; never evidence authority |
| Historical proposed state scaffolds | `OPEN` | Preserve lineage, migrate, correct claims, or retire transparently |
| Public emergency-authority ambiguity | `RISK` | Explicit advisory/non-authority policy and UI labels |

Unknowns narrow implementation and block release. They do not authorize plausible defaults.

[Back to top](#top)

---

<a id="migration-and-compatibility"></a>

## Migration and compatibility

### Current-state migration facts

- No canonical plural Focus control-plane README was found.
- Legacy singular state and county materials exist.
- No `kansas-state` lane or state release was verified.
- The declared Focus machine schemas and payload validator are absent.
- Existing county plan material may use divergent paths and draft shapes; its complete inventory is not established.

### Migration rules

1. **Inventory before move.** Produce a pinned file/link/consumer inventory.
2. **Choose one canonical home.** Current Directory Rules selects `docs/focus-modes/`; do not operate both trees as authorities.
3. **Preserve history.** Moves retain content, attribution, prior paths, and correction notes.
4. **No blind bulk backfill.** Existing county plans are inspected and migrated against the accepted domain-set/schema profile.
5. **Version machine shapes.** Do not silently add required fields to an unknown or absent schema.
6. **Use staged enforcement.** Warnings may precede denial only after a complete inventory, compatibility plan, and reviewed effective date.
7. **No arbitrary deadline.** The prior draft’s fixed 14-day window is not adopted without owner capacity and migration evidence.
8. **Repair claims during migration.** The state index cannot remain “planned” without a qualifying lane; validator claims must match executable behavior.
9. **Update every consumer.** Validators, workflows, docs, links, API/UI clients, examples, release paths, and registries migrate together.
10. **Retain rollback.** The migration has an exact pre-move tree/commit and a tested restoration plan.
11. **No release side effects.** Moving control-plane Markdown does not promote data or publish a state lane.

### Compatibility redirects

A temporary singular-path README may point to the canonical plural home, but it must:

- contain no competing plan or index data;
- state its compatibility status;
- identify the canonical destination;
- record the migration decision and date;
- be covered by link and duplicate-authority tests;
- have a reviewed retirement trigger.

[Back to top](#top)

---

<a id="incident-correction-and-rollback"></a>

## Incident, correction, and rollback

### State-scale claim incident

If a state Focus release exposes unsupported, stale, overgeneralized, undergeneralized, rights-constrained, sensitive, or county-derived claims:

1. reduce exposure through the governed route or release alias;
2. preserve the affected payload, coverage profile, evidence, receipts, policies, reviews, release, and cache identities;
3. identify affected domains, sources, counties, times, and public claims;
4. determine whether county releases share the same underlying defect;
5. issue correction, withdrawal, or rollback records;
6. invalidate API, tile, CDN, service-worker, browser, search, vector, and story caches;
7. verify no alternate state or county path continues serving the claim;
8. rebuild from direct admissible evidence;
9. obtain independent review before restoration;
10. record post-incident verification.

A county disagreement is not automatically proof the state release is wrong, and a state release is not automatically authority over a county release. Compare evidence, scope, time, policy, and transforms.

### Rollout failure

When state-scope enforcement breaks candidate work:

- hold or narrow the candidate;
- do not restore a legacy singular authority or bypass the validator;
- keep state scope non-public;
- preserve explicit abstain/deny/hold outcomes;
- repair doctrine, migration, schema, fixtures, and validation;
- resume only through the accepted path.

[Back to top](#top)

---

<a id="rollback-and-supersession"></a>

## Rollback and supersession

### Documentation-only rollback

Restore prior ADR blob:

```text
09605b531116857e741e2f2cb8f8a9177c224734
```

A transparent revert restores prior proposed documentation only. It does not alter Directory Rules, control-plane files, schemas, validators, data, releases, or public state.

### If this ADR is later accepted

An accepted ADR is governance history. Material relaxation, removal of `state`, change to the coverage rule, or a new state-lane cardinality requires:

- a successor ADR;
- reciprocal supersession links;
- matching ADR index update;
- Directory Rules amendment;
- compatibility and migration for control planes, contracts, schemas, fixtures, validators, data, clients, releases, and caches;
- correction/withdrawal analysis for released state claims;
- a rollback plan at least as strong as the rule being changed.

Do not flip an accepted ADR back to `proposed`, delete the state evidence trail, remove coverage entries to make validation pass, or recreate a legacy public bypass.

### Implemented state-lane rollback

- **Before release:** preserve candidate history; demote/hold and migrate or retire transparently.
- **After release:** issue governed withdrawal/rollback records, retain immutable artifacts and evidence, update aliases atomically, invalidate caches, and publish correction notices where needed.
- **Directory Rules rollback:** only through the accepted successor decision—not by editing doctrine to match a broken implementation.
- **Control-plane migration rollback:** restore the exact pre-migration tree and links; do not leave both singular and plural trees writable.

[Back to top](#top)

---

<a id="verification-checklist"></a>

## Verification checklist

### Current revision

- [x] ADR ID, exact filename, H1, and index row verified.
- [x] Source and effective status preserved as `proposed`.
- [x] Directory Rules §6.7 inspected.
- [x] ADR-0027 and singular/plural naming decision inspected.
- [x] Actual singular control-plane README, county index, state index, and state template inspected.
- [x] Canonical plural README and Kansas state lane checked at exact paths.
- [x] FocusModePayload semantic contract inspected.
- [x] Declared Focus schemas and payload validator checked at exact paths.
- [x] County-only index validator inspected.
- [x] Human and machine domain registers inspected.
- [x] Focus mock readiness workflow inspected.
- [x] Old draft aliases replaced by current canonical lane IDs as candidate profile keys.
- [x] County-output prohibition narrowed to authority/evidence roll-up rather than banning valid county-granular source records.
- [x] Coverage dispositions expanded to explicit populated/abstain/deny, with hold blocking release.
- [x] No implementation, release, or publication claim introduced.
- [ ] Human review completed.
- [ ] ADR accepted.
- [ ] Directory Rules amended.
- [ ] Implementation graduated.
- [ ] State release observed.

### Future implementation

- [ ] ADR-0027/ADR-0028 relationship resolved.
- [ ] Canonical plural control plane established.
- [ ] Singular compatibility lane bounded.
- [ ] Domain-set profile accepted and machine-readable.
- [ ] Contracts/schemas/fixtures/validators agree.
- [ ] State index and lane cardinality validate.
- [ ] All domain dispositions close.
- [ ] State evidence chain is direct.
- [ ] Sensitive lanes fail closed.
- [ ] Governed API/client finite outcomes pass.
- [ ] State/county comparison does not collapse authority.
- [ ] Release/correction/rollback/cache drills pass.
- [ ] Public clients cannot read candidates or internal stores.

[Back to top](#top)

---

<a id="references"></a>

## References

| Reference | Relationship and current boundary |
|---|---|
| [`docs/adr/README.md`](./README.md) | ADR operating contract; merge does not accept a decision |
| [`docs/adr/INDEX.md`](./INDEX.md) | Confirms ADR-0028 exact identity and proposed status |
| [ADR-0001](./ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Canonical machine-schema home |
| [ADR-0003](<./ADR-0003-policy-singular-is-canonical-(policies-is-compatibility).md>) | Canonical singular policy root |
| [ADR-0004](./ADR-0004-apps-governed-api-is-the-trust-membrane.md) | Dynamic public trust boundary |
| [ADR-0005](./ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md) | Proposed public map-first shell |
| [ADR-0010](./ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | Sensitive-domain fail-closed posture |
| [ADR-0018](./ADR-0018-promotion-gate-sequence.md) | Promotion sequence and readiness holds |
| [ADR-0019](./ADR-0019-ai-adapter-contract-and-finite-envelopes.md) | Focus/AI adapter and finite envelope boundary |
| [ADR-0020](./ADR-0020-abstain-is-a-first-class-decision.md) | Explicit abstention when support is insufficient |
| [ADR-0024](./ADR-0024-steward-separation-of-duties-for-release.md) | Independent release and restoration review |
| [ADR-0025](./ADR-0025-public-client-never-reads-canonical-internal-stores.md) | Public-client anti-bypass boundary |
| [ADR-0027](./ADR-0027-county-focus-mode-control-plane.md) | Proposed canonical Focus control-plane naming/migration |
| [Directory Rules](../doctrine/directory-rules.md) | Current Focus placement contract and authority boundary |
| [Legacy Focus control README](../focus-mode/README.md) | Proposed state/county design at noncanonical singular path |
| [Legacy county index](../focus-mode/counties/COUNTY_INDEX.md) | Collision-prevention register; validator compatibility unresolved |
| [Legacy state index](../focus-mode/state/STATE_INDEX.md) | Proposed inert state index with unsupported validator claim |
| [Legacy state template](../focus-mode/state/_template/state-build-plan.md) | Proposed blocked state template |
| [Legacy county template](../focus-mode/counties/_template/county-build-plan.md) | County planning template |
| [FocusModePayload contract](../../contracts/focus_mode/focus_mode_payload.md) | Proposed county-oriented semantic contract |
| [Focus index validator](../../tools/validators/validate_focus_mode_index.py) | Current county-only validator |
| [Human Domain Lane Register](../registers/DOMAIN_LANE.md) | Current narrative 13-lane IDs |
| [Machine domain register](../../control_plane/domain_lane_register.yaml) | Empty proposed machine register |
| [Drift Register](../registers/DRIFT_REGISTER.md) | Existing drift ledger; Focus conflicts not yet recorded |
| [Focus mock workflow](../../.github/workflows/focus-mock-test.yml) | Explicit runtime/fixture readiness hold |

[Back to top](#top)

---

<a id="revision-history"></a>

## Revision history

| Version | Date | Summary |
|---|---|---|
| v0.1 | 2026-05-23 | Initial proposed ADR coupling `-state`, one `kansas-state` lane, 13-domain coverage, schema/template/validator amendments, no county roll-up, migration, acceptance, and rollback. |
| v0.2 | 2026-07-24 | Re-grounded the decision in current repository evidence; confirmed ADR identity and Directory Rules’ three-scope state; surfaced singular/plural control-plane drift, unsupported state index, absent state lane/schemas/payload validator, county-only validator, empty machine domain register, and Focus runtime hold; replaced draft domain aliases with current lane IDs; versioned the domain-set concept; refined coverage dispositions; distinguished forbidden county Focus-output roll-up from valid county-granular source evidence; made Directory Rules acceptance atomic; added canonical migration, non-vacuous tests, implementation waves, risk, incident, cache, correction, rollback, and successor-ADR discipline. |

---

<sub>This ADR is governed by KFM doctrine: a Focus Mode is a cross-cutting proof composition, not a root or domain; every material claim resolves evidence or abstains; sensitive content fails closed; public clients use governed surfaces; and no state-scale umbrella may outrank its evidence, policy, review, release, correction, or rollback records.</sub>
