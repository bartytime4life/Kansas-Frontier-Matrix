<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-watchers-plants-watch-readme
title: tools/watchers/plants_watch/ — Plants Watcher Compatibility and Routing Boundary
type: readme; directory-readme; watcher-compatibility-lane; flora-source-drift-routing; non-publisher-boundary
version: v0.2
status: draft; repository-grounded; README-only; placement-conflicted; no-active-watcher-established; sensitive-domain; non-authoritative
owners: OWNER_TBD — Tooling steward · Watcher steward · Flora steward · Source steward · Taxonomy steward · Rights steward · Cultural/stewardship reviewer · Sensitivity/geoprivacy reviewer · Pipeline steward · Validation steward · Evidence steward · Policy steward · Release steward · Docs steward
created: 2026-07-08
updated: 2026-07-16
supersedes: v0.1 plants watcher routing guide
policy_label: "public-review; tools; watchers; flora; plants; source-drift; compatibility-routing; README-only; no-live-source; no-network-default; no-direct-fetch; no-source-activation; no-raw-admission; no-publication; no-public-path; source-role-preserving; rights-aware; cultural-rights-aware; rare-plant-deny-default; geoprivacy-fail-closed; review-gated; correction-aware; rollback-aware"
current_path: tools/watchers/plants_watch/README.md
truth_posture: >
  CONFIRMED target v0.1 README; tools root and parent watcher README; bounded direct-lane search
  returning this README only; tools/ingest/plants_watch README-only sibling; pipelines/watchers/plants
  README-only shared executable candidate; pipelines/domains/flora/watchers README-only domain
  executable candidate; pipeline_specs/flora/watchers README-only direct specification lane;
  two seven-line PROPOSED plants-drift placeholders outside that direct sublane; draft Flora source
  registry; duplicate USDA PLANTS registry paths; three draft USDA PLANTS connector aliases;
  fixture lane README without confirmed payloads; TODO-only domain-flora workflow; current absence
  of representative historical USDA PLANTS watcher scripts, workflows, schemas, policies, and tests;
  and historical guarded-live and scheduled-observer scaffold commits / PROPOSED freeze this directory
  as a documentation, compatibility, and routing boundary; canonical placement decision; minimum
  active-watcher contract; source-activation preconditions; no-network fixture path; finite outcomes;
  validation, correction, migration, deprecation, and rollback rules / CONFLICTED tools/watchers versus
  tools/ingest versus two pipelines executable homes; three declarative specification homes; duplicate
  source-registry homes; three connector aliases; historical watcher scaffolding versus absent current
  implementation / UNKNOWN accepted watcher home, active SourceDescriptor, source activation decision,
  parser, scheduler, executable consumer, network policy, current USDA PLANTS endpoint contract,
  materiality thresholds, receipt schema, emitted artifacts, substantive CI, production review integration,
  and runtime use / NEEDS VERIFICATION owners, ADR or migration record, canonical connector and registry
  paths, source rights and cadence, cultural authority, taxonomy authority, accepted schemas and reason
  codes, fixture payloads, tests, validators, policy enforcement, correction propagation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 01026cd58b1e687c4f8fa3363229b9857613102b
  prior_blob: 0a8956cf196db1c1562349baed38bf005dbf261d
  tools_root_blob: 02c9e71420af8afe029e7ce25829d86a59696cc1
  parent_watchers_blob: 0a3b47a4246a2a1f10cf1cc9ea2a335b4547ae3e
  tools_ingest_sibling_blob: bd82f1a4c4d9b54ce1c6464fd96c0365fc3dba4f
  shared_pipeline_candidate_blob: fc523e15f62f62e025d0d4586ffff929ae367eb7
  flora_pipeline_candidate_blob: ca41b4fc94582eae81fba4b91f397cf9c63004c7
  flora_spec_boundary_blob: b7d25ec9814b776164d7550202288222f4726bd6
  shared_spec_placeholder_blob: fa8ab22f84d2ac41a3a49b9633509c196d989925
  source_registry_doc_blob: 26479f938d4a08eec9d9dcd66b1a20120b119f06
  canonical_paths_blob: 367d40d9781387019443fbd5ca98070be543f31c
  registry_placeholder_blob: 4cf877d234542990be382913d0ab0917f8fb3398
  registry_tbd_template_blob: f1cba5310f760de9a0a9b9ebecca544e6a5fc0ce
  underscore_connector_alias_blob: 29cc7f518c9ad3db3b5f6918cd7f90a563b11c25
  plants_drift_fixture_readme_blob: f2e79efacbfff917c50a30a538bf6dad62f076bb
  domain_flora_workflow_blob: c7737001b3de3f0a1150ea467ef656a52c26b0fd
  historical_lineage:
    - c5e6845f5f88900302b63f6770fd283f5b082c28 added guarded USDA PLANTS live-watcher scaffolding
    - c9adf77f192ee05c5322afdaaea0f0de2e4f1bba added scheduled observe-only USDA PLANTS scaffolding
related:
  - ../README.md
  - ../../README.md
  - ../../ingest/plants_watch/README.md
  - ../../../pipelines/watchers/README.md
  - ../../../pipelines/watchers/plants/README.md
  - ../../../pipelines/domains/flora/watchers/README.md
  - ../../../pipeline_specs/flora/watchers/README.md
  - ../../../pipeline_specs/flora/plants_drift_watcher.yaml
  - ../../../pipeline_specs/watchers/plants_drift.yaml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../docs/domains/flora/SOURCE_INTAKE.md
  - ../../../docs/runbooks/flora/SOURCE_REFRESH_RUNBOOK.md
  - ../../../data/registry/sources/flora/usda_plants.yaml
  - ../../../data/registry/flora/sources/usda_plants.yaml
  - ../../../connectors/usda_plants/README.md
  - ../../../connectors/usda-plants/README.md
  - ../../../connectors/usda/plants/README.md
  - ../../../fixtures/domains/flora/plants_drift/README.md
  - ../../../tests/domains/flora/README.md
  - ../../../policy/domains/flora/README.md
  - ../../../policy/sensitivity/flora/README.md
  - ../../../data/receipts/flora/README.md
  - ../../../release/candidates/flora/README.md
  - ../../../.github/workflows/domain-flora.yml
  - ../../../.github/PULL_REQUEST_TEMPLATE.md
  - ../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, tools, watchers, plants-watch, flora, usda-plants, source-drift, compatibility, routing, non-publisher, no-network, source-role, taxonomy, rights, sensitivity, geoprivacy, cultural-rights, review, correction, rollback]
notes:
  - "This revision changes only tools/watchers/plants_watch/README.md; a generated provenance receipt is paired separately."
  - "No watcher script, source fetcher, connector, pipeline, spec, config, schema, contract, policy, test, fixture payload, workflow, registry record, lifecycle object, receipt instance, proof, release object, runtime behavior, or public artifact is created or modified."
  - "Historical watcher scaffold commits are lineage evidence only; representative paths from those commits are absent at the pinned current base."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/watchers/plants_watch/` — Plants Watcher Compatibility and Routing Boundary

> **One-line purpose.** Preserve a reviewable, non-publishing routing surface for plant-source drift work while preventing this README-only directory from becoming another executable watcher home, a second ingest lane, a source-activation authority, botanical truth, or a sensitive-location disclosure path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tools" src="https://img.shields.io/badge/root-tools%2F-blue">
  <img alt="Inventory: README only" src="https://img.shields.io/badge/inventory-README__only-lightgrey">
  <img alt="Placement: conflicted" src="https://img.shields.io/badge/placement-CONFLICTED-orange">
  <img alt="Activation: none established" src="https://img.shields.io/badge/activation-none__established-critical">
  <img alt="Publication: denied" src="https://img.shields.io/badge/publication-DENY-red">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail__closed-critical">
</p>

> [!IMPORTANT]
> **This direct lane is README-only at the pinned repository snapshot.** No active plant watcher, live fetcher, scheduler, parser, source activation decision, accepted specification, executable consumer, fixture payload set, policy implementation, receipt emitter, or substantive CI proof is established here.

> [!CAUTION]
> **Placement is unresolved.** The repository contains three watcher/helper documentation lanes under `tools/`, two executable watcher candidates under `pipelines/`, and three declarative specification candidates under `pipeline_specs/`. Do not add implementation to this directory until ownership and delegation are settled by an accepted decision or migration note.

> [!WARNING]
> Plant-source drift can become sensitive when combined with rare or protected taxa, herbarium locality, private land, restoration sites, cultural or medicinal knowledge, community-science observations, habitat context, or precise geometry. Exact or reconstructable sensitive detail must not enter watcher logs, diffs, receipts, alerts, issues, pull-request text, generated summaries, or public surfaces.

**Quick links:** [Purpose](#purpose) · [Status](#current-evidence-and-maturity) · [Placement](#placement-and-authority) · [Lane map](#parallel-lane-reconciliation) · [Operating law](#watcher-operating-law) · [Source gates](#source-and-activation-preconditions) · [Inputs](#minimum-input-contract) · [Outputs](#bounded-output-contract) · [Outcomes](#finite-outcomes-and-reason-codes) · [Sensitivity](#sensitivity-geoprivacy-and-cultural-rights) · [Validation](#validation-tests-and-ci) · [History](#historical-lineage-and-current-absence) · [Belongs](#what-belongs-here) · [Sequence](#smallest-sound-next-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#maintenance-correction-migration-and-rollback) · [Evidence](#evidence-ledger)

---

## Purpose

`tools/watchers/plants_watch/` is a compatibility and routing boundary for plant-source watcher work.

Its durable question is:

> Which current KFM root owns each part of plant-source drift observation, and what must remain blocked until source identity, rights, sensitivity, taxonomy, cadence, specification, executable consumer, validation, review, correction, and rollback are proven?

This README may orient maintainers to:

- USDA PLANTS taxonomy, checklist, and state/county distribution drift;
- herbarium package or manifest drift;
- controlled status or listing source metadata drift;
- occurrence-aggregator dataset, schema, terms, or source-head drift;
- vegetation classification or STAC collection drift;
- source descriptor, rights, cadence, attribution, or sensitivity drift;
- no-op, change-candidate, quarantine, and steward-review outcomes.

It does not activate, fetch, admit, normalize, validate, catalog, publish, or release any source.

[Back to top](#top)

---

## Current evidence and maturity

| Surface | Inspected status | Safe conclusion |
|---|---|---|
| `tools/watchers/plants_watch/` | **CONFIRMED README-only** in bounded search | Documentation and routing only. |
| `tools/watchers/README.md` | **CONFIRMED** | Parent watcher contract exists; the v0.1 claim that it was not found is stale. |
| `tools/README.md` | **CONFIRMED** | `tools/` may hold long-lived watcher helpers, while pipeline orchestration remains separate. |
| `tools/ingest/plants_watch/` | **CONFIRMED README-only sibling** | Parallel proposed helper lane; not an accepted implementation home. |
| `pipelines/watchers/plants/` | **CONFIRMED README-only** in bounded search | Shared executable candidate described by prose, not code proof. |
| `pipelines/domains/flora/watchers/` | **CONFIRMED README-only** in bounded search | Flora executable candidate described by prose, not code proof. |
| `pipeline_specs/flora/watchers/` | **CONFIRMED README-only direct sublane** | No concrete accepted watcher profile in the direct sublane. |
| `pipeline_specs/flora/plants_drift_watcher.yaml` | **CONFIRMED seven-line `PROPOSED` placeholder** | Not active, canonical, schema-backed, or consumer-bound. |
| `pipeline_specs/watchers/plants_drift.yaml` | **CONFIRMED seven-line `PROPOSED` placeholder** | Duplicate declarative candidate; not active or reconciled. |
| Flora source registry | **CONFIRMED draft documentation** | Registry doctrine exists; active USDA PLANTS admission is not proven. |
| USDA PLANTS registry records | **CONFIRMED duplicate placeholders** | One inventory placeholder and one separate TBD template; no accepted active descriptor. |
| USDA PLANTS connectors | **CONFIRMED three draft alias READMEs** | Canonical connector placement and implementation are unresolved. |
| Plants-drift fixture lane | **CONFIRMED README-only** in bounded search | No fixture payload or expected-output suite established. |
| `domain-flora` workflow | **CONFIRMED TODO-only jobs** | No watcher validation, material-change proof, or publish-deny enforcement. |
| Historical watcher scaffolds | **CONFIRMED in Git history** | Prior guarded-live and scheduled-observer scaffolds existed; current representative paths are absent. |
| Active watcher runtime | **UNKNOWN** | No current parser, scheduler, consumer, source activation, emitted receipt, or production use established. |

**Current determination:** this folder is a documentation-only compatibility lane. Treat any attempt to add code, a schedule, source credentials, output schemas, policy rules, or lifecycle writers here as **NEEDS VERIFICATION / HOLD** until placement is resolved.

[Back to top](#top)

---

## Placement and authority

Directory Rules classify files by primary responsibility:

```text
tools/          reusable trust-bearing helpers and CLIs
pipelines/      executable lifecycle orchestration — HOW
pipeline_specs/ declarative run intent — WHAT
connectors/     upstream access and source capture
contracts/      object meaning
schemas/        machine-checkable shape
policy/         admissibility, rights, sensitivity, release decisions
data/           lifecycle records, receipts, proofs, catalog, published artifacts
release/        promotion, correction, withdrawal, supersession, rollback
apps/           governed released serving surfaces
```

The presence of a README does not establish implementation ownership.

### Safe role for this directory

Until a placement decision is accepted, this directory should:

1. index the competing plant-watcher homes;
2. document the non-publisher and sensitive-domain boundaries;
3. record current evidence and open conflicts;
4. point to accepted authority roots;
5. reject local implementation growth.

### Authority this directory does not have

This lane does not own:

- source identity, role, rights, cadence, sensitivity, or activation;
- USDA PLANTS connector implementation;
- botanical or taxonomic truth;
- specimen or occurrence evidence;
- watcher specification schemas;
- network access policy or credentials;
- lifecycle state transitions;
- `EvidenceBundle`, receipt, proof, catalog, or release authority;
- public API, map, tile, export, Focus Mode, search, graph, or AI behavior.

[Back to top](#top)

---

## Parallel-lane reconciliation

Current repository surfaces overlap without an accepted ownership decision:

| Responsibility | Current candidate paths | Current evidence |
|---|---|---|
| Tools routing/helper documentation | `tools/watchers/plants_watch/`, `tools/ingest/plants_watch/` | README-only siblings. |
| Executable shared watcher behavior | `pipelines/watchers/plants/` | README-only candidate. |
| Executable Flora-owned watcher behavior | `pipelines/domains/flora/watchers/` | README-only candidate. |
| Flora-specific declarative specs | `pipeline_specs/flora/watchers/`, `pipeline_specs/flora/plants_drift_watcher.yaml` | README-only sublane plus placeholder. |
| Shared declarative watcher spec | `pipeline_specs/watchers/plants_drift.yaml` | Placeholder. |
| USDA PLANTS connector | `connectors/usda_plants/`, `connectors/usda-plants/`, `connectors/usda/plants/` | Three draft aliases. |
| USDA PLANTS source record | `data/registry/sources/flora/usda_plants.yaml`, `data/registry/flora/sources/usda_plants.yaml` | Two incomplete, conflicting candidates. |

### Required reconciliation outcome

Before implementation expands, a reviewed decision or migration note should identify:

- one canonical executable owner;
- one canonical declarative-spec owner;
- one canonical USDA PLANTS connector path;
- one canonical source-registry path;
- delegation rules for any retained compatibility pointers;
- deprecation and removal windows;
- consumer migration and rollback steps.

Do not create duplicate code and let later convention decide. The smallest safe current change is documentation containment.

[Back to top](#top)

---

## Watcher operating law

A watcher detects possible change. It does not create truth or publication authority.

```text
admitted source descriptor + activation decision + bounded watch spec
  -> metadata-first / fixture-first comparison
  -> no-op, candidate, hold, quarantine, deny, abstain, or error
  -> steward-readable review handoff
  -> later governed connector / pipeline / validation / evidence / policy / release stages
```

### Non-publisher invariants

A plant watcher must not:

- activate an unreviewed source;
- silently fetch full payloads when a metadata check is sufficient;
- treat HTTP success, an ETag, timestamp, checksum, or count as source acceptance;
- upgrade source role or taxonomic authority;
- write directly to `processed/`, `catalog/`, `triplets/`, `published/`, or `release/`;
- expose exact or reconstructable sensitive plant information;
- create public map, API, search, graph, export, Focus Mode, or AI-answer content;
- treat a watcher receipt or diff as an `EvidenceBundle`;
- approve its own downstream work.

[Back to top](#top)

---

## Source and activation preconditions

A future plant watcher run must resolve all required preconditions before live access:

| Precondition | Required evidence | Fail-closed outcome |
|---|---|---|
| Canonical source descriptor | Stable source id, source role, authority, rights, attribution, cadence, access posture, sensitivity, steward, citation. | `SOURCE_DESCRIPTOR_MISSING` or `HOLD`. |
| Source activation decision | `allowed`, `restricted`, `denied`, or `needs_review`, with scope and reviewer. | No live run. |
| Canonical connector | One accepted connector path and bounded output contract. | `PLACEMENT_CONFLICT`. |
| Watch specification | Immutable id/version/digest, source refs, allowed checks, cadence, materiality rules, outputs, kill switch. | `SPEC_MISSING` or `ABSTAIN`. |
| Prior state | Prior source-head, manifest, snapshot, hash, or no-baseline policy. | `BASELINE_MISSING`. |
| Rights and cultural authority | Current terms, redistribution posture, attribution, cultural/stewardship restrictions. | `RIGHTS_OR_AUTHORITY_UNRESOLVED`. |
| Sensitivity profile | Rare/protected taxa, locality risk, private-land risk, geoprivacy and join-risk controls. | `SENSITIVITY_UNRESOLVED`. |
| Fixture path | Deterministic no-network inputs and expected outputs. | CI/live activation blocked. |
| Reviewer path | Named source, Flora, rights, sensitivity, and release review where applicable. | `REVIEW_PATH_MISSING`. |

The current USDA PLANTS registry files do not satisfy these preconditions: one is an inventory placeholder and the other retains `TBD` authority, rights, sensitivity, cadence, and access fields.

[Back to top](#top)

---

## Minimum input contract

A future implementation should accept an explicit bounded packet rather than ambient repository state:

```yaml
watcher_id: kfm.flora.plants-drift
watcher_version: 1.0.0
mode: fixture_only
source_descriptor_ref: data/registry/sources/flora/<source_id>.yaml
source_activation_ref: <governed decision ref>
watch_spec_ref: pipeline_specs/<accepted-home>/<profile>.yaml
baseline_ref: <immutable prior-state ref>
allowed_signal_classes:
  - source_head
  - manifest
  - taxonomy_metadata
  - terms_metadata
output_route: <accepted candidate/review lane>
promotion_required: true
public_release: false
```

This shape is illustrative, not an accepted schema. Field names and enum values remain **PROPOSED** until contract and schema authority are established.

[Back to top](#top)

---

## Bounded output contract

### Allowed output families

A watcher may emit or prepare bounded candidate artifacts such as:

- no-change or no-op run receipt;
- source-head or manifest observation;
- material-change candidate;
- source-intake candidate;
- quarantine or hold handoff;
- steward-readable review summary;
- reason-coded error or abstention;
- references to deterministic inputs and prior state.

### Required output properties

Every output should preserve:

- watcher and source identity;
- immutable input and specification references;
- source role without upgrade;
- source, observed, retrieval, watcher-run, review, and release time distinctions where material;
- changed and unchanged signal classes;
- materiality posture and reason codes;
- rights, sensitivity, cultural-authority, and review flags;
- `promotion_required = true` or equivalent candidate posture;
- `publication_state = not_published` or equivalent;
- correction, supersession, and rollback references when a prior candidate is replaced.

### Forbidden outputs

This lane must not emit:

- admitted RAW payloads of record;
- normalized or processed Flora objects;
- taxonomic acceptance decisions;
- exact sensitive occurrence or locality data;
- catalog or graph truth;
- `EvidenceBundle` closure;
- policy approval;
- release manifest, published layer, tile archive, API payload, or AI answer;
- automatic PR merge or self-approval.

[Back to top](#top)

---

## Finite outcomes and reason codes

| Outcome | Meaning |
|---|---|
| `NO_CHANGE` | Compared allowed signals and detected no material difference. |
| `CHANGE_CANDIDATE` | Detected a bounded change requiring downstream review. |
| `NEEDS_REVIEW` | Human interpretation or authority review is required. |
| `HOLD` | Prerequisite, baseline, policy, or review support is incomplete. |
| `QUARANTINE` | Candidate is isolated because risk or validity cannot be resolved. |
| `RESTRICT` | Run or output is allowed only under stated constraints. |
| `ABSTAIN` | Available evidence cannot support a classification. |
| `DENY` | The requested action or exposure is prohibited. |
| `ERROR` | The run failed operationally; no unsafe fallback is allowed. |

Recommended reason-code families:

```text
PLACEMENT_CONFLICT
SOURCE_DESCRIPTOR_MISSING
SOURCE_ACTIVATION_MISSING
CONNECTOR_UNRESOLVED
SPEC_MISSING
BASELINE_MISSING
RIGHTS_OR_AUTHORITY_UNRESOLVED
SENSITIVITY_UNRESOLVED
TAXONOMY_AUTHORITY_UNRESOLVED
CADENCE_OR_FRESHNESS_UNRESOLVED
FIXTURE_MISSING
REVIEW_PATH_MISSING
SOURCE_HEAD_ONLY_ABSTAIN
SENSITIVE_INTERSECTION_REVIEW_REQUIRED
PUBLIC_SURFACE_LEAKAGE_DENIED
DIRECT_PROMOTION_DENIED
WATCHER_SYSTEM_ERROR
```

A future schema may rename or refine these values. The governing requirement is finite, reviewable, fail-closed behavior.

[Back to top](#top)

---

## Sensitivity, geoprivacy, and cultural rights

The watcher must treat joined sensitivity as a new product-level decision.

A public source list may become sensitive when joined with:

- precise occurrence or specimen locality;
- private or small-area land context;
- restoration planting sites;
- rare, protected, threatened, or culturally significant taxa;
- community-science observations;
- habitat suitability or corridor context;
- medicinal or traditional knowledge;
- reviewer-only status or stewardship notes.

### Required controls

- metadata-first checks before payload retrieval;
- minimization of taxa, locality, and private-party detail in logs and reports;
- no exact coordinates in issue, pull-request, notification, or artifact names;
- separate steward-only and public-safe views where needed;
- deterministic redaction or generalization outside this directory;
- most-restrictive-input and join-induced sensitivity review;
- explicit denial when public-safe transformation cannot be proven.

### Denied assumptions

```text
public source availability != unrestricted reuse
county distribution        != exact occurrence
specimen locality          != current presence
source-head change         != botanical change
source role                != taxonomic authority
watcher success            != public safety
```

[Back to top](#top)

---

## Network, scheduling, and side effects

Default development and CI posture is **no network**.

A future live observer requires all of the following:

1. accepted source activation and connector placement;
2. allowed host and request-method policy;
3. explicit timeout, retry, backoff, and rate-limit handling;
4. no secret or credential material in repository files or logs;
5. metadata-first observation before large download;
6. bounded temporary output outside canonical stores;
7. receipt and reviewer handoff;
8. kill switch and incident response;
9. no publication, promotion, automatic merge, or direct lifecycle advancement;
10. deterministic fixture parity.

A schedule is not activation proof. A workflow file is not review approval. A successful request is not source admission.

[Back to top](#top)

---

## Validation, tests, and CI

### Current bounded state

- no current executable file is established in this direct directory;
- the plants-drift fixture lane is README-only in bounded search;
- the two visible plants-drift YAML files are placeholders;
- the Flora workflow contains TODO-only jobs;
- representative historical watcher scripts, workflows, policy, schemas, and tests are absent at the pinned base.

### Required no-network test matrix

| Case | Expected outcome |
|---|---|
| Same metadata and digest | `NO_CHANGE` |
| Allowed metadata field changed | `CHANGE_CANDIDATE` |
| Descriptor missing | `HOLD` or `DENY` |
| Activation missing or denied | `DENY` |
| Baseline missing | `HOLD` or `ABSTAIN` |
| Rights changed or unclear | `NEEDS_REVIEW` or `DENY` |
| Rare-plant or cultural join risk | `NEEDS_REVIEW`, `RESTRICT`, or `DENY` |
| Exact locality appears in output | test failure and `PUBLIC_SURFACE_LEAKAGE_DENIED` |
| Candidate targets processed, catalog, published, or release | test failure and `DIRECT_PROMOTION_DENIED` |
| Network attempted in fixture mode | test failure |
| Malformed input or output | `ERROR` with no partial publication |
| Replayed identical inputs | identical deterministic result and hash |

### Required validation layers

- specification schema and semantic checks;
- source descriptor and activation validation;
- connector/output-boundary checks;
- rights, attribution, cultural-authority, sensitivity, and geoprivacy policy;
- deterministic identity and hash closure;
- no-network enforcement;
- path and side-effect guards;
- receipt/reference closure;
- negative public-surface tests;
- correction and rollback tests.

### CI admission

Do not label the watcher implemented until substantive CI calls the accepted parser and executable against real valid and invalid fixtures and fails closed. TODO-only workflow jobs do not count.

[Back to top](#top)

---

## Historical lineage and current absence

Two earlier commits provide implementation lineage:

| Commit | Historical addition | Current posture |
|---|---|---|
| `c5e6845f5f88900302b63f6770fd283f5b082c28` | Guarded USDA PLANTS manual/live watcher scaffolding, source fetch plan, snapshot diff/lock, review handoff, policy, schemas, tests, and workflow. | **LINEAGE only.** Representative paths are absent at current base. |
| `c9adf77f192ee05c5322afdaaea0f0de2e4f1bba` | Scheduled observe-only watcher, watch state, change alert, reviewer queue, artifact bundle, policy, schemas, tests, and workflow. | **LINEAGE only.** Representative paths are absent at current base. |

Current `Not Found` probes included representative scripts, workflows, policy, schemas, and tests from those commits. This supports a bounded conclusion that those paths are not current implementation. It does not reconstruct every deletion or prove no related code exists under another name.

Do not copy historical scaffolds back into the repository without re-running placement, source, rights, sensitivity, dependency, security, and test review against current doctrine.

[Back to top](#top)

---

## What belongs here

Allowed now:

- this README;
- compatibility and placement notes;
- pointer indexes to accepted watcher, spec, connector, source, fixture, test, and review homes;
- migration and deprecation notices;
- public-safe, non-operational examples that contain no live source details or sensitive reconstruction clues.

Allowed only after a placement decision:

- a thin forwarding shim with no duplicate implementation;
- a stable command alias whose owning implementation lives elsewhere;
- migration warnings and compatibility tests;
- a deliberately accepted reusable helper whose responsibility is proven to belong under `tools/`.

[Back to top](#top)

---

## What does not belong here

| Item | Owning home or required decision |
|---|---|
| Executable watcher orchestration | Accepted `pipelines/` lane. |
| Declarative watcher profile | Accepted `pipeline_specs/` lane. |
| Source client or full fetcher | Canonical `connectors/` path. |
| Source descriptor and activation | Canonical `data/registry/` and control-plane decision paths. |
| Domain meaning | `contracts/domains/flora/` and Flora doctrine. |
| Machine schema | Canonical `schemas/contracts/v1/` home. |
| Rights, sensitivity, cultural, release policy | `policy/` authority roots. |
| Fixture payloads | `fixtures/` accepted lane. |
| Tests | `tests/` accepted lane. |
| Lifecycle data and emitted receipts/proofs | `data/` lifecycle and trust-artifact homes. |
| Release, correction, withdrawal, rollback records | `release/`. |
| Public API, map, tile, graph, search, export, Focus Mode, or AI logic | Governed application and released-artifact paths. |
| Credentials, private endpoints, exact sensitive locations, hidden redaction values, signing keys | Denied from this directory. |

[Back to top](#top)

---

## Smallest sound next sequence

1. **Freeze this lane as documentation-only.** Add no watcher implementation here.
2. **Resolve placement.** Select one executable, one spec, one connector, and one registry home through reviewed doctrine/ADR/migration work.
3. **Complete source admission.** Resolve USDA PLANTS role, authority, rights, attribution, cadence, sensitivity, access, steward, and activation.
4. **Create fixture-first specification.** Add one inactive, schema-backed profile with immutable identity and no-network cases.
5. **Implement one bounded observer.** Metadata-first, side-effect-limited, no publication, explicit kill switch.
6. **Add negative tests and policy.** Include sensitive joins, direct-publish attempts, missing prerequisites, and network denial.
7. **Emit reviewable receipts and handoffs.** Keep evidence, policy, and release authority external.
8. **Exercise correction and rollback.** Disable the observer and restore prior state without deleting audit history.
9. **Retire duplicate lanes.** Preserve pointers only for a defined compatibility window.

[Back to top](#top)

---

## Definition of done

### Documentation boundary

- [x] Parent watcher README is correctly recognized as present.
- [x] Direct lane is bounded as README-only.
- [x] Parallel tools, pipelines, specs, registries, and connector aliases are surfaced.
- [x] Historical scaffolding is separated from current implementation.
- [x] Non-publisher, source-role, sensitivity, cultural-rights, correction, and rollback rules are explicit.

### Placement and authority

- [ ] Canonical executable watcher home is accepted.
- [ ] Canonical watcher-spec home is accepted.
- [ ] Canonical USDA PLANTS connector home is accepted.
- [ ] Canonical USDA PLANTS registry home is accepted.
- [ ] Retained compatibility lanes have owners and removal dates.

### Implementation proof

- [ ] Active source descriptor and activation decision validate.
- [ ] Accepted profile schema and parser validate.
- [ ] No-network valid and invalid fixtures exist.
- [ ] Executable consumer is present and tested.
- [ ] Rights, cultural-authority, sensitivity, and geoprivacy policies fail closed.
- [ ] Output path and public-surface denial tests pass.
- [ ] Deterministic receipts and reviewer handoffs are emitted.
- [ ] Substantive CI runs the watcher suite.
- [ ] Correction, deactivation, incident, and rollback drills pass.

Until these close, the accurate status is **README-only compatibility boundary; no active plant watcher established**.

[Back to top](#top)

---

## Open verification register

| ID | Item | Status |
|---|---|---|
| PW-01 | Assign owners and required reviewers. | NEEDS VERIFICATION |
| PW-02 | Decide `tools/watchers` versus `tools/ingest` responsibility. | NEEDS VERIFICATION |
| PW-03 | Select shared versus Flora-domain executable pipeline home. | NEEDS VERIFICATION |
| PW-04 | Select one declarative watcher-spec home. | NEEDS VERIFICATION |
| PW-05 | Select canonical USDA PLANTS connector path. | NEEDS VERIFICATION |
| PW-06 | Select canonical USDA PLANTS registry path. | NEEDS VERIFICATION |
| PW-07 | Complete source role, authority, rights, cadence, sensitivity, access, citation, and steward fields. | NEEDS VERIFICATION |
| PW-08 | Create or locate source activation decision. | NEEDS VERIFICATION |
| PW-09 | Verify current upstream endpoint and terms before any live use. | NEEDS VERIFICATION |
| PW-10 | Define accepted materiality classes and reason codes. | NEEDS VERIFICATION |
| PW-11 | Define watcher, no-op, change, quarantine, and review receipt schemas. | NEEDS VERIFICATION |
| PW-12 | Add deterministic fixtures and expected outputs. | NEEDS VERIFICATION |
| PW-13 | Add executable tests, validators, and fail-closed policy. | NEEDS VERIFICATION |
| PW-14 | Wire substantive CI and no-network enforcement. | NEEDS VERIFICATION |
| PW-15 | Define steward queue and notification limits. | NEEDS VERIFICATION |
| PW-16 | Define sensitive-output minimization and log retention. | NEEDS VERIFICATION |
| PW-17 | Define correction, deactivation, supersession, and rollback. | NEEDS VERIFICATION |
| PW-18 | Reconcile historical scaffold lineage and current removal rationale. | NEEDS VERIFICATION |

[Back to top](#top)

---

## Maintenance, correction, migration, and rollback

### Documentation maintenance

Update this README when:

- a canonical owner or path is accepted;
- a source is activated, restricted, denied, retired, or superseded;
- an executable watcher, parser, schema, policy, fixture, test, workflow, or receipt is added or removed;
- upstream terms, cadence, endpoint, or sensitivity posture changes;
- a correction or incident reveals a missing guard.

### Correction

When a documentation claim is wrong:

1. preserve the prior version and evidence snapshot;
2. identify the affected path or claim;
3. correct through a reviewed change;
4. update related parent, spec, pipeline, source, fixture, test, and runbook docs;
5. retain a changelog and forward link.

### Placement migration

A future migration should:

1. inventory files and consumers across all candidate lanes;
2. select the owning responsibility root;
3. create an ADR or migration note when authority or compatibility changes;
4. move with history preservation;
5. provide temporary pointers, not duplicate evolving implementations;
6. update specs, imports, workflows, tests, docs, receipts, and CODEOWNERS;
7. set a compatibility removal date;
8. verify rollback to the prior revision.

### Runtime rollback

If an implemented watcher behaves unsafely:

- disable schedule and live-network activation;
- preserve logs, inputs, outputs, hashes, receipts, and reviewer decisions;
- quarantine affected candidates;
- prevent downstream promotion and public exposure;
- revoke or rotate credentials where relevant;
- correct source, spec, code, policy, or fixture state through review;
- replay deterministically before reactivation;
- issue correction or withdrawal records for affected downstream products.

### Documentation rollback for this change

Before merge, close the review branch. After merge, revert the documentation commit or restore prior blob `0a8956cf196db1c1562349baed38bf005dbf261d` through a review branch. This README update changes no runtime, source, data, policy, or release state.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Supports | Does not prove |
|---|---|---|
| Current target README | Prior intent and stale claims needing correction. | Executable watcher behavior. |
| `tools/README.md` | Tools-root responsibility and watcher non-publisher rule. | Canonical plant watcher placement. |
| `tools/watchers/README.md` | Parent watcher routing contract now exists. | Active scripts or schedules. |
| `tools/ingest/plants_watch/README.md` | Parallel proposed tools helper lane. | Accepted implementation authority. |
| `pipelines/watchers/README.md` | Shared executable watcher responsibility proposal. | Current code or canonical ownership. |
| `pipelines/watchers/plants/README.md` | Plant watcher pipeline design. | Active implementation. |
| `pipelines/domains/flora/watchers/README.md` | Flora-domain executable watcher design. | Active implementation. |
| `pipeline_specs/flora/watchers/README.md` | Repository-grounded spec conflict and README-only maturity. | Accepted profile or parser. |
| plants-drift YAML placeholders | File presence and `PROPOSED` inventory status. | Active specification. |
| Flora source registry docs | Admission, watcher-as-non-publisher, `SourceIntakeRecord` posture. | Active USDA PLANTS descriptor. |
| duplicate USDA PLANTS YAMLs | Registry topology conflict and incomplete fields. | Source activation. |
| connector alias READMEs | Connector naming and placement conflict. | Connector implementation. |
| plants-drift fixture README | Intended synthetic no-network scenarios. | Fixture payloads or passing tests. |
| `domain-flora.yml` | Workflow trigger and TODO-only state. | Substantive validation. |
| historical commits `c5e6845…`, `c9adf77…` | Prior scaffold concepts and file families. | Current implementation or suitability. |
| current `Not Found` checks | Representative historical paths are absent at the pinned base. | Exhaustive deletion history or absence of every related file. |
| Directory Rules and PR/receipt contracts | Placement, review, provenance, and rollback expectations. | Acceptance of a watcher-specific ADR. |

[Back to top](#top)

---

## Changelog

| Version | Date | Change | Status |
|---|---|---|---|
| v0.1 | 2026-07-08 | Replaced an empty placeholder with a planning-oriented plants watcher README. | Superseded |
| v0.2 | 2026-07-16 | Reconciled current repository evidence; corrected parent README status; bounded the direct lane as README-only; surfaced tools, pipelines, spec, registry, and connector conflicts; separated historical scaffolds from current implementation; added fixture-first, source-activation, finite-outcome, sensitivity, validation, migration, correction, and rollback contracts. | Draft / repository-grounded |

---

> **Final rule:** this directory may explain where plant-source watcher work belongs. It must not become the place where unresolved placement, inactive sources, sensitive data, or historical scaffolds are converted into active behavior by convenience.

[Back to top](#top)
