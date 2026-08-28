<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-watchers-readme
title: pipeline_specs/watchers/ — Governed Shared Watcher Specification Boundary
type: readme; directory-readme; declarative-watcher-spec-boundary; compatibility-routing
version: v0.2
status: draft; repository-grounded; one-placeholder-spec-confirmed; no-active-shared-watcher-spec-established; placement-conflicted
owners:
  - OWNER_TBD — Pipeline-spec steward
  - OWNER_TBD — Watcher steward
  - OWNER_TBD — Source and rights steward
  - OWNER_TBD — Domain stewards
  - OWNER_TBD — Security and sensitivity reviewer
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Evidence and receipt steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-13
updated: 2026-07-18
supersedes: v0.1
policy_label: public-doc; pipeline-specs; watchers; declarative-only; metadata-first; no-secrets; no-live-activation; no-direct-fetch; no-direct-admission; no-direct-raw; no-direct-release; source-role-preserving; rights-aware; sensitivity-aware; security-aware; review-gated; correction-aware; rollback-aware
current_path: pipeline_specs/watchers/README.md
truth_posture: CONFIRMED target README, parent pipeline-spec boundary, one direct seven-line PROPOSED plants-drift placeholder, shared executable watcher README, repository-grounded watcher tooling routing README, README-only Fauna and Flora watcher-spec sublanes, external Flora plants-drift placeholder duplication, absent checked shared spec-test and spec-fixture READMEs, proposed source-admission ADR, current CODEOWNERS routing, and no open PR targeting this README / PROPOSED canonical shared watcher-spec contract, one accepted parser and consumer, watcher registry, source activation binding, metadata-first comparison grammar, materiality classes, finite outcomes, reason codes, receipt bindings, no-network fixtures, activation/deactivation, correction propagation, and rollback / CONFLICTED shared watcher spec versus domain watcher spec placement; pipelines/watchers versus tools/watchers and tools/ingest implementation responsibility; plants_drift shared versus Flora-specific placement / UNKNOWN exhaustive recursive inventory, accepted schema, active parser, active consumers, scheduler, source activation records, network behavior, emitted watcher receipts, substantive CI, runtime use, review integration, and production effects / NEEDS VERIFICATION named owners, accepted Directory Rules copy, source-descriptor and activation vocabulary, source-registry topology, domain delegation rules, rights and sensitivity policy, fixture/test coverage, workflow triggers, branch protection, correction handling, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: d68cc7344d50e3d739dee555ca3dbe28960369fc
  target_prior_blob: 4a1f642dd29d9894a52d5a5d2fe914025e9a02f4
  direct_lane_files_confirmed:
    - pipeline_specs/watchers/README.md
    - pipeline_specs/watchers/plants_drift.yaml
  checked_absent_paths:
    - AGENTS.md
    - pipeline_specs/AGENTS.md
    - pipeline_specs/watchers/AGENTS.md
    - tests/pipeline_specs/watchers/README.md
    - fixtures/pipeline_specs/watchers/README.md
  inventory_method: GitHub connector file reads plus bounded repository code-index queries; absence claims are limited to checked paths and indexed results
related:
  - ../README.md
  - ../../CONTRIBUTING.md
  - ../../SECURITY.md
  - ../../docs/architecture/directory-rules.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../pipelines/watchers/README.md
  - ../../tools/watchers/README.md
  - ../../tools/watchers/plants_watch/README.md
  - ../../tools/ingest/README.md
  - ../fauna/watchers/README.md
  - ../flora/watchers/README.md
  - ../flora/plants_drift_watcher.yaml
  - ./plants_drift.yaml
  - ../../fixtures/domains/flora/plants_drift/README.md
  - ../../data/registry/sources/
  - ../../data/work/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../policy/
  - ../../tests/
  - ../../fixtures/
  - ../../release/
  - ../../.github/workflows/README.md
  - ../../.github/CODEOWNERS
  - ../../.github/PULL_REQUEST_TEMPLATE.md
  - ../../data/receipts/generated/README.md
  - ../../schemas/contracts/v1/receipts/generated_receipt.schema.json
notes:
  - "v0.2 replaces the planning-only proposed watcher profile tree with a commit-pinned repository inventory and explicit placement conflicts."
  - "The direct lane contains this README and one seven-line plants_drift.yaml inventory placeholder; no active shared watcher specification is established."
  - "Watchers remain non-publishers and non-admitters. A changed source signal is not source authority, content validation, domain truth, evidence closure, release approval, or public notification authority."
  - "This documentation-only revision does not change the placeholder YAML, executable watcher code, source records, schemas, contracts, policy, fixtures, tests, workflows, lifecycle records, receipts, proofs, release objects, runtime behavior, or public artifacts."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `pipeline_specs/watchers/` — Governed Shared Watcher Specification Boundary

> Declarative boundary for shared source-change watcher intent: what admitted source signals may be compared, which metadata-first checks may run, which finite outcomes and review handoffs are expected, and which non-admission/non-publication gates remain mandatory—without becoming executable watcher logic, source authority, lifecycle authority, evidence, policy, release approval, or a public alerting surface.

<p>
  <img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-yellow">
  <img alt="Direct inventory: README plus one placeholder" src="https://img.shields.io/badge/direct__inventory-README%20%2B%201%20placeholder-lightgrey">
  <img alt="Activation: none established" src="https://img.shields.io/badge/activation-none__established-orange">
  <img alt="Placement: conflicted" src="https://img.shields.io/badge/placement-CONFLICTED-orange">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Publication: denied" src="https://img.shields.io/badge/publication-DENIED-red">
</p>

**Path:** `pipeline_specs/watchers/README.md`
**Version:** `v0.2`
**Status:** draft / repository-grounded / one placeholder spec confirmed / no active shared watcher spec established
**Owning root:** `pipeline_specs/` — declarative pipeline configuration
**Cross-cutting lane:** shared watcher intent that is not yet assigned to a single domain
**Public posture:** no direct public path; watcher specs and watcher outputs are non-publishing
**Evidence snapshot:** `main@d68cc7344d50e3d739dee555ca3dbe28960369fc`

> [!IMPORTANT]
> The direct lane contains one YAML file, [`plants_drift.yaml`](plants_drift.yaml). It is a seven-line `PROPOSED` inventory placeholder pointing to Flora planning documentation. It has no stable spec identity, schema, parser, source descriptor, cadence, checks, consumer, fixtures, receipts, activation record, or release binding. Its presence activates nothing.

> [!CAUTION]
> A changed ETag, checksum, timestamp, manifest, version, header, taxonomy list, source descriptor, endpoint response, or file size does not prove that the source payload changed materially, that domain truth changed, that rights remain valid, that sensitive content is safe, or that a public artifact should be refreshed.

> [!WARNING]
> Watcher logs, diffs, reports, receipts, notifications, issues, and generated summaries can leak secrets, private endpoint details, exact sensitive locations, rare-species or rare-plant clues, archaeology or cultural knowledge, living-person or DNA context, infrastructure detail, or restricted source terms. Shared watcher specs must minimize outputs and fail closed before such detail reaches review or public systems.

---

## Quick navigation

[Purpose](#purpose) · [Authority](#authority-boundary) · [Current state](#confirmed-current-state) · [Topology](#watcher-topology-and-placement-conflicts) · [Inventory](#direct-lane-inventory) · [Shared versus domain](#shared-versus-domain-specific-specs) · [Contract](#minimum-future-active-spec-contract) · [Signals](#watch-signals-and-comparison-boundaries) · [Materiality](#material-change-and-finite-outcomes) · [Sources](#source-admission-rights-and-activation) · [Lifecycle](#lifecycle-and-non-publication-gates) · [Security](#security-sensitivity-and-data-minimization) · [Receipts](#reports-receipts-evidence-and-release) · [Validation](#validation-tests-fixtures-and-ci) · [Review](#review-versioning-and-change-discipline) · [Rollback](#deactivation-correction-and-rollback) · [Done](#definition-of-done-for-an-active-shared-watcher-spec) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [History](#change-history)

---

## Purpose

`pipeline_specs/watchers/` is the declarative configuration lane for watcher behavior that is genuinely shared across multiple domains or source families.

A future active shared watcher specification may declare:

- stable spec identity, immutable version/digest, owner, status, and supersession;
- one accepted parser and one verified executable consumer;
- admitted `SourceDescriptor` references and activation-state requirements;
- source role, rights, attribution, sensitivity, sovereignty/cultural authority, and cadence expectations;
- metadata-first comparison signals and a pinned prior-state baseline;
- retry, outage, stale-state, debounce, backoff, and deterministic no-op behavior;
- material-change classes, finite outcomes, and stable reason codes;
- candidate `MaterialChangeReport`, proposed work, quarantine, and review handoffs;
- watcher-run and material-change receipt requirements;
- deterministic no-network fixtures and replay;
- explicit no-fetch, no-admission, no-RAW, no-normalize, no-catalog, no-release, and no-public-notification constraints;
- deactivation, correction, supersession, withdrawal, and rollback targets.

This lane does not own domain truth, source identity, source activation, endpoint credentials, executable orchestration, connector access, lifecycle data, evidence closure, policy decisions, catalog closure, release state, or public notification behavior.

### Primary audience

- pipeline-spec and watcher stewards;
- source, rights, sensitivity, security, policy, evidence, and release reviewers;
- domain stewards deciding whether a watcher is truly shared or domain-specific;
- connector and pipeline maintainers designing bounded metadata checks;
- QA and CI maintainers building no-network fixture coverage;
- maintainers reconciling duplicated plants-drift and watcher implementation lanes.

### Non-goals

This README does not:

- activate, schedule, or execute a watcher;
- accept a canonical watcher-spec schema or parser;
- resolve `pipelines/watchers/`, `tools/watchers/`, `tools/ingest/`, and domain implementation ownership;
- resolve the shared-versus-Flora placement of the plants-drift placeholder;
- admit a source or fetch a payload;
- define a `MaterialChangeReport`, receipt, evidence, or release schema;
- approve rights, sensitivity, cultural authority, source terms, or public exposure;
- create an alerting, incident-response, enforcement, public-health, emergency, or official-notification service;
- prove current data, source freshness, domain truth, catalog integrity, release readiness, or production runtime use.

[Back to top](#top)

---

## Authority boundary

### Responsibility split

```text
pipeline_specs/  declarative watcher intent: WHAT may be compared and under which gates
pipelines/       executable orchestration: HOW comparisons and handoffs occur
tools/           reusable side-effect-limited validators/checkers/helpers
connectors/      source-specific upstream access and payload retrieval
data/registry/   source identity, role, rights, sensitivity, cadence, activation
contracts/       semantic meaning of watcher reports, receipts, and domain objects
schemas/         machine-checkable shape
policy/          allow, deny, restrict, hold, abstain, and release obligations
tests/fixtures/  deterministic enforceability proof and synthetic examples
data/            lifecycle records, receipts, proofs, catalogs, and published artifacts
release/         promotion, correction, withdrawal, supersession, and rollback decisions
apps/            governed released serving surfaces
```

A watcher spec may require a gate. It cannot satisfy the gate merely by naming it.

### Disallowed collapses

```text
README or path existence       -> active watcher specification
merged watcher spec            -> scheduled execution
schedule text                  -> source activation
watcher invocation             -> source fetch
source signal changed          -> payload changed
payload changed                -> material domain change
material change                -> source admission
candidate report               -> RAW capture
candidate report               -> ValidationReport
candidate report               -> EvidenceBundle
source-head match              -> rights or sensitivity approval
checksum match                 -> content validation
cadence completed              -> freshness proof
watcher receipt                -> proof or catalog closure
watcher handoff                -> release approval
watcher notification           -> public or official alert
generated summary              -> evidence or domain truth
```

### Watchers are non-publishers

A shared watcher may report that a source-facing signal changed. It must not:

- fetch or persist an unapproved payload merely because a signal changed;
- activate a source;
- admit data into RAW;
- normalize or validate domain records;
- write to processed, catalog, triplet, or published authority;
- create an `EvidenceBundle` or claim proof closure;
- mutate public APIs, maps, tiles, indexes, search, embeddings, dashboards, or generated answers;
- issue public safety, emergency, conservation, regulatory, legal, health, or operational instructions.

[Back to top](#top)

---

## Confirmed current state

### Safe conclusions

- **CONFIRMED:** `pipeline_specs/watchers/README.md` exists.
- **CONFIRMED:** [`plants_drift.yaml`](plants_drift.yaml) is the only direct non-README file surfaced by bounded search.
- **CONFIRMED:** `plants_drift.yaml` is a seven-line `PROPOSED` placeholder created from `docs/domains/flora/FILE_SYSTEM_PLAN.md`.
- **CONFIRMED:** the shared executable watcher README exists at [`pipelines/watchers/README.md`](../../pipelines/watchers/README.md), but concrete behavior, schedules, activation, tests, and release wiring remain unverified.
- **CONFIRMED:** [`tools/watchers/README.md`](../../tools/watchers/README.md) classifies its direct tree as documentation/compatibility and records unresolved ownership with `tools/ingest/` and `pipelines/watchers/`.
- **CONFIRMED:** Fauna and Flora have domain-specific watcher-spec README lanes.
- **CONFIRMED:** the Flora watcher README records two competing plants-drift placeholders: one in `pipeline_specs/flora/` and one here.
- **CONFIRMED:** checked `tests/pipeline_specs/watchers/README.md` and `fixtures/pipeline_specs/watchers/README.md` paths do not exist.
- **CONFIRMED:** the source-descriptor admission ADR exists but remains `proposed`.
- **CONFIRMED:** no open pull request targeting this README was found before authoring.
- **UNKNOWN:** exhaustive inventory, accepted schema/parser/registry, active consumers, schedules, network behavior, emitted receipts, runtime use, CI enforcement, and production effects.

### Maturity matrix

| Surface | Current status | Evidence-bounded conclusion |
|---|---:|---|
| Parent README | `CONFIRMED` | Declarative shared watcher boundary exists. |
| Direct concrete YAML | `ONE PLACEHOLDER` | No active shared spec is established. |
| Stable spec identity/version | `ABSENT FROM PLACEHOLDER` | `plants_drift.yaml` has only status, source doc, path, and note. |
| Accepted schema | `UNKNOWN` | No accepted shared watcher-spec schema established. |
| Parser and consumer | `UNKNOWN` | No binding from placeholder to executable consumer established. |
| SourceDescriptor refs | `ABSENT` | No source identity, role, rights, cadence, or activation fields. |
| Comparison checks | `ABSENT` | No ETag, checksum, manifest, source-head, or metadata grammar. |
| Materiality/outcomes | `ABSENT` | No finite outcomes or reason codes. |
| Shared test/fixture lane | `NOT FOUND AT CHECKED PATHS` | Spec-specific enforceability is not established. |
| Executable shared watcher | `DOCUMENTED / UNPROVED` | Pipeline README exists; implementation maturity remains unknown. |
| Reusable watcher tooling | `PLACEMENT-CONFLICTED` | Tools watchers and tools ingest both expose watcher-shaped lanes. |
| Domain watcher delegation | `PARTIAL / CONFLICTED` | Flora/Fauna lanes exist; shared/domain rule is not accepted. |
| Scheduled execution | `UNKNOWN` | No accepted scheduler or active registry established. |
| Receipt emission | `UNKNOWN` | No emitted watcher receipt inventory established. |
| Release/publication | `DENIED BY BOUNDARY` | No spec may publish. |

[Back to top](#top)

---

## Watcher topology and placement conflicts

The repository currently exposes several watcher-shaped surfaces:

```text
pipeline_specs/watchers/                 shared declarative intent; this lane
pipeline_specs/flora/watchers/           Flora-specific declarative intent
pipeline_specs/fauna/watchers/           Fauna-specific declarative intent
pipeline_specs/flora/plants_drift_watcher.yaml
pipeline_specs/watchers/plants_drift.yaml
pipelines/watchers/                      shared executable orchestration claim
pipelines/watchers/plants/               plants executable sublane claim
pipelines/domains/flora/watchers/        Flora executable watcher claim
tools/watchers/                          reusable tooling/compatibility claim
tools/watchers/plants_watch/             plants tooling compatibility claim
tools/ingest/                             parallel watcher-named helper lanes
```

This topology is evidence of repository structure and documentation, not an accepted ownership model.

### Current conflicts

| Conflict | Safe posture |
|---|---|
| Shared versus domain-specific watcher specs | No duplicate active specs. Keep placeholders inactive until delegation is governed. |
| `plants_drift.yaml` here versus `plants_drift_watcher.yaml` under Flora | Treat both as lineage/placeholders; do not activate either by path presence. |
| `pipelines/watchers/` versus domain executable lanes | One implementation per concern after ownership review. |
| `tools/watchers/` versus `tools/ingest/` | Reusable helper placement requires responsibility-based migration, not duplication. |
| Tools helper versus pipeline orchestration | Side-effect-limited checker may be a tool; lifecycle orchestration belongs in pipelines. |
| Watcher versus connector | Metadata checks may call an approved connector interface; watcher spec never owns credentials or direct access authority. |

### Freeze rule

Until placement is resolved:

- do not add another plants-drift or shared watcher implementation;
- do not copy a domain spec into the shared lane;
- do not create aliases that can execute independently;
- do not assign schedules to placeholders;
- do not infer canonical authority from the shortest path;
- preserve rollback and history through an ADR or migration note when consolidation occurs.

[Back to top](#top)

---

## Direct lane inventory

```text
pipeline_specs/watchers/
├── README.md          # CONFIRMED — this boundary and inventory
└── plants_drift.yaml  # CONFIRMED — seven-line PROPOSED inventory placeholder
```

### `plants_drift.yaml`

Current payload:

```yaml
status: PROPOSED
source_doc: docs/domains/flora/FILE_SYSTEM_PLAN.md
path: pipeline_specs/watchers/plants_drift.yaml
notes:
  - Placeholder created from docs/domains markdown inventory.
```

It does not define:

- `spec_id`, semantic version, digest, owner, or supersession;
- source descriptors, source roles, rights, sensitivity, or activation state;
- parser or executable consumer;
- cadence, retry, stale-state, debounce, or backoff;
- source-head, ETag, checksum, manifest, timestamp, schema, or metadata checks;
- prior-state baseline;
- materiality classes, finite outcomes, or reason codes;
- candidate, quarantine, review, or no-op handoff;
- watcher receipts;
- fixtures, tests, validation, CI, correction, or rollback.

Therefore its safe status is **placeholder / inactive / non-authoritative**.

[Back to top](#top)

---

## Shared versus domain-specific specs

A profile belongs in the shared lane only when its primary declarative responsibility is reusable across domains without embedding domain truth, domain sensitivity policy, domain source roles, or domain review semantics.

### Shared-lane candidates

Potential shared concerns include:

- generic source-head and version comparison;
- HTTP metadata fields such as ETag and Last-Modified;
- package manifest and checksum comparison;
- source descriptor drift against an accepted common contract;
- cadence, retry, outage, backoff, and stale-state mechanics;
- generic deterministic no-op and prior-state requirements;
- generic receipt and bounded handoff fields.

### Domain-lane requirements

A profile should remain under `pipeline_specs/<domain>/watchers/` when it carries:

- domain-specific source-role meaning;
- rare-species, rare-plant, archaeology, cultural, infrastructure, living-person, DNA, land, or other sensitivity rules;
- domain taxonomy, identity, geometry, temporal, or evidence semantics;
- domain steward review requirements;
- domain-specific materiality and reason codes;
- public-safe representation or generalization obligations;
- domain correction and release dependencies.

### Delegation contract

A domain watcher spec may reference an accepted shared profile only when:

- the shared profile has stable identity and version;
- inheritance/override semantics are machine-defined;
- domain restrictions can tighten but not weaken shared fail-closed controls;
- effective configuration is deterministic and reviewable;
- one executable consumer resolves the combined profile;
- fixtures test both base and domain-specific obligations;
- receipts record the effective profile digest.

[Back to top](#top)

---

## Minimum future active spec contract

No accepted machine schema was established by this review. The following is a **PROPOSED contract**, not a current executable format.

| Field family | Minimum obligation |
|---|---|
| Identity | Stable `spec_id`, semantic version, status, digest, owner refs, and supersession. |
| Responsibility | Shared or domain-delegated classification and explicit non-authority statements. |
| Consumer | One parser and one executable consumer with accepted versions. |
| Sources | Stable SourceDescriptor refs, activation requirements, roles, rights, sensitivity, and terms. |
| Baseline | Prior source-head, digest, manifest, metadata, or receipt reference. |
| Watch signals | Explicit metadata fields/checks; payload retrieval remains separately governed. |
| Cadence | Manual/scheduled/event cadence, jitter, retry, backoff, stale-state, and outage behavior. |
| Materiality | Classes, thresholds, review requirements, and no silent auto-promotion. |
| Outcomes | Finite outcomes and stable reason codes. |
| Handoffs | Candidate work, quarantine, review, no-op, and error destinations. |
| Security | Secret references, logging minimization, endpoint privacy, and sensitive-diff suppression. |
| Receipts | Run and material-change receipt refs, digests, and safe observability fields. |
| Execution | No-network fixture default, idempotency, replay, concurrency, and side-effect limits. |
| Lifecycle | Explicit prohibition on direct admission, normalization, catalog, release, and publication. |
| Maintenance | Activation, deactivation, correction, supersession, migration, and rollback. |

### Illustrative inactive YAML

```yaml
spec_id: kfm.pipeline_spec.watchers.example
version: 0.0.0-proposed
status: proposed
scope: shared
role: declarative

consumer:
  implementation_ref: NEEDS_VERIFICATION
  accepted_versions: []

sources:
  source_descriptor_refs: []
  activation_required: true

watch:
  cadence: manual
  network_default: deny
  metadata_first: true
  checks: []
  prior_state_ref: null

materiality:
  classes: []
  review_required: true
  auto_admit: false
  auto_publish: false

outcomes:
  allowed:
    - NO_OP
    - CANDIDATE
    - QUARANTINE
    - NEEDS_REVIEW
    - ABSTAIN
    - DENY
    - ERROR

receipts:
  watcher_run_required: true
  material_change_required: false

anti_collapse:
  spec_is_executable: false
  watcher_is_connector: false
  signal_change_is_domain_change: false
  report_is_evidence: false
  result_is_release_approval: false
```

Do not copy this into an active file until schema, parser, consumer, registry, policy, fixtures, tests, review, and activation controls exist.

[Back to top](#top)

---

## Watch signals and comparison boundaries

Watcher specs should prefer the least invasive signal that can answer the change-observation question.

| Signal | May indicate | Does not prove |
|---|---|---|
| Source-head/version | Upstream version identifier changed. | Payload validity, rights, material domain change. |
| ETag | Server representation tag changed or stayed stable. | Content equivalence across servers or semantic change. |
| Last-Modified/date | Server-reported timestamp changed. | Complete freshness, correctness, or actual payload change. |
| Checksum/digest | Compared bytes differ or match. | Semantic materiality, schema validity, rights, policy safety. |
| Manifest/package index | Membership or package metadata changed. | Each member is admissible or meaningful. |
| Header/schema version | Declared format metadata changed. | Records conform or domain meaning is preserved. |
| Record count/file size | Volume changed. | Which records changed or whether the change matters. |
| Source descriptor diff | KFM source-control metadata changed. | Upstream content changed or activation remains approved. |
| Terms/license page diff | Rights text may have changed. | Legal interpretation or continued use approval. |
| Taxonomy/codelist diff | Authority list changed. | Accepted domain revision or identity remapping. |

### Metadata-first does not mean metadata-only forever

A watcher may create a candidate requiring a connector dry run or bounded payload comparison. Any payload access remains:

- source-activated;
- connector-owned or explicitly governed;
- rights- and sensitivity-reviewed;
- no-network in default CI;
- restricted to RAW/QUARANTINE candidates;
- unable to publish directly.

[Back to top](#top)

---

## Material change and finite outcomes

### Materiality is a reviewable classification

A detected signal may be:

- non-material operational noise;
- expected cadence update;
- source metadata drift;
- schema/format drift;
- rights/terms drift;
- source-role or authority drift;
- data availability/outage change;
- candidate content change;
- sensitive or security-relevant change;
- unknown and requiring review.

A watcher must not convert a signal into domain truth by itself.

### Finite outcomes

| Outcome | Meaning |
|---|---|
| `NO_OP` | Checked signals are unchanged or below accepted non-material thresholds. |
| `CANDIDATE` | Bounded material-change candidate created for later governed processing. |
| `QUARANTINE` | Change cannot safely proceed because shape, rights, sensitivity, identity, or support is unresolved. |
| `NEEDS_REVIEW` | Human/source/domain/policy/security review is required before further action. |
| `ABSTAIN` | Available signals cannot support a materiality conclusion. |
| `DENY` | Policy, rights, sensitivity, source state, or prohibited side effect blocks the operation. |
| `ERROR` | Parser, connector interface, comparison, storage, receipt, or other operation failed. |
| `STALE` | Expected source signal is late or unavailable; this is not proof the underlying source is unchanged. |

### Candidate reason codes

```text
SPEC_SCHEMA_MISSING
SPEC_CONSUMER_UNRESOLVED
SOURCE_DESCRIPTOR_MISSING
SOURCE_NOT_ACTIVE
SOURCE_ROLE_MISMATCH
RIGHTS_OR_TERMS_CHANGED
SENSITIVITY_REVIEW_REQUIRED
PRIOR_STATE_MISSING
SOURCE_HEAD_CHANGED
ETAG_CHANGED
LAST_MODIFIED_CHANGED
MANIFEST_CHANGED
CHECKSUM_CHANGED
SCHEMA_OR_HEADER_CHANGED
SOURCE_DESCRIPTOR_DRIFT
UPSTREAM_OUTAGE
STALE_SOURCE_SIGNAL
MATERIALITY_UNKNOWN
SENSITIVE_DIFF_SUPPRESSED
RECEIPT_MISSING
REVIEW_PENDING
PROHIBITED_SIDE_EFFECT
```

Final vocabulary requires contract, schema, policy, validator, test, and steward alignment.

[Back to top](#top)

---

## Source admission, rights, and activation

The proposed [`ADR-0017`](../../docs/adr/ADR-0017-source-descriptor-admission-process.md) separates descriptor-level source activation from record-level admission. Its status is `proposed`, so this README does not treat its paths or state machine as accepted implementation.

A future watcher spec should require a source-control record that resolves:

- stable source identity and source family;
- allowed and denied source roles;
- activation status and reviewer;
- rights, license, attribution, redistribution, API terms, and access constraints;
- sensitivity, sovereignty/cultural authority, geoprivacy, living-person, infrastructure, and security posture;
- expected cadence, source head, endpoint or artifact identity, and re-review date;
- allowed comparison signals;
- credential and network requirements;
- permitted candidate outputs;
- correction, withdrawal, and rollback references.

### Activation is not release

Even an internally active source does not authorize:

- public use;
- all source roles;
- all fields or geometry;
- exact locations;
- downstream claim families;
- automated refresh;
- release or publication.

### Terms and rights drift

A terms/license watcher must route changes to review and suspend affected operations when policy requires. It must not:

- interpret legal meaning automatically;
- retain restricted page content unnecessarily;
- expose account, token, or private endpoint detail;
- assume silence means continued permission.

[Back to top](#top)

---

## Lifecycle and non-publication gates

Watcher observation sits before governed source admission and publication:

```text
source-facing signal
  -> watcher comparison
  -> NO_OP / ABSTAIN / DENY / ERROR
     or bounded CANDIDATE / QUARANTINE / NEEDS_REVIEW
  -> source steward / connector / ingest decision
  -> RAW or QUARANTINE only when separately authorized
  -> WORK / QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> PUBLISHED through separate release authority
```

### Required gates

1. **Identity gate** — stable spec ID, version, digest, owner, and status.
2. **Placement gate** — shared versus domain-specific responsibility is resolved.
3. **Consumer gate** — one accepted parser/consumer is named.
4. **Source gate** — SourceDescriptor and activation state resolve.
5. **Rights/sensitivity gate** — terms and sensitive-detail handling are current.
6. **Baseline gate** — prior state is pinned and inspectable.
7. **Signal gate** — checks and limitations are explicit.
8. **Cadence gate** — retry, outage, stale-state, and no-op behavior are bounded.
9. **Materiality gate** — finite classification and review behavior are defined.
10. **Security gate** — no secret or restricted-detail leakage in logs/outputs.
11. **Receipt gate** — deterministic run inputs, checks, digests, outcomes, and handoffs are recorded.
12. **No-fetch gate** — direct payload access is denied unless separately governed.
13. **No-admission gate** — watcher result cannot admit RAW.
14. **No-normalize/catalog gate** — watcher cannot produce normalized or catalog truth.
15. **No-release gate** — watcher cannot publish or approve release.
16. **Correction/rollback gate** — downstream invalidation and deactivation are defined.

[Back to top](#top)

---

## Security, sensitivity, and data minimization

### Sensitive domains inherit stricter controls

Shared watcher profiles must support domain-specific tightening for:

- rare species and rare plants;
- archaeology, burial, sacred, Indigenous, or culturally restricted information;
- critical infrastructure and operational facility detail;
- living-person, genealogy, DNA, and genomic information;
- private land, parcel, title, owner, farm, or stewardship detail;
- emergency, hazard, public-health, or security-relevant sources;
- private endpoints, credentials, account-bound exports, and restricted terms.

### Output minimization

Watcher outputs should contain only what reviewers need:

- spec ID/version/digest;
- source descriptor ref;
- safe signal names;
- prior/current digests or opaque refs;
- finite outcome and reason code;
- timestamps and run identity;
- candidate/quarantine/review refs;
- receipt ref.

Avoid:

- payload excerpts by default;
- exact coordinates;
- source credentials or signed URLs;
- sensitive record IDs;
- diffs that enable reconstruction;
- unrestricted headers or response bodies;
- private terms text;
- hidden reasoning or generated speculation.

### Security findings

Credentials, unauthorized access, private endpoint exposure, or exploitable workflow behavior must use the repository's private security-reporting path rather than public watcher reports or issues.

[Back to top](#top)

---

## Reports, receipts, evidence, and release

### Material-change report

A watcher may create a bounded candidate report. That report is not evidence closure or source admission.

A future report should distinguish:

- observed signal;
- comparison baseline;
- method;
- uncertainty and limitations;
- potentially affected source/product/domain;
- sensitive fields suppressed;
- required next reviewer;
- prohibited automated actions.

### Receipts

Watcher receipts are process memory. They may record:

- effective spec digest;
- consumer version;
- source descriptor and baseline refs;
- comparison methods;
- safe input/output hashes;
- finite outcome and reason;
- handoff refs;
- timestamps and environment metadata.

A receipt is not:

- an `EvidenceBundle`;
- a policy decision;
- a catalog record;
- a release manifest;
- proof that the source or domain changed;
- public notification authority.

### Evidence, catalog, and release remain downstream

Any later EvidenceBundle, catalog update, graph delta, layer rebuild, API refresh, map update, or release requires separate governed processing, validation, policy, review, correction, and rollback closure.

[Back to top](#top)

---

## Validation, tests, fixtures, and CI

### Current limitations

- The direct shared lane has no active schema-backed spec.
- `plants_drift.yaml` is an inventory placeholder.
- Checked shared watcher-spec test and fixture README paths are absent.
- Shared executable and tooling watcher roots remain documentation-heavy and placement-conflicted.
- No accepted registry, parser, scheduler, emitted receipt, or current runtime report was established.
- No watcher-specific branch protection or required check was verified.

### Minimum future test matrix

An active shared watcher spec should have deterministic no-network tests for:

- YAML/JSON parse and schema conformance;
- stable identity, digest, version, and supersession;
- one parser/consumer binding;
- shared-versus-domain delegation and override rules;
- source descriptor resolution and activation states;
- source-role, rights, terms, sensitivity, and security holds;
- prior-state requirements;
- ETag, checksum, manifest, source-head, timestamp, and descriptor-drift comparisons;
- false positives, false negatives, missing headers, weak ETags, clock skew, redirects, outages, and partial responses;
- finite outcomes and stable reason codes;
- no-op, retry, backoff, stale-state, replay, idempotency, and concurrency;
- sensitive-diff suppression and safe logs;
- no direct payload access in default tests;
- no direct RAW admission, normalize, catalog, release, or public writes;
- receipt generation and digest verification;
- correction, deactivation, supersession, and rollback.

### CI posture

A substantive watcher-spec workflow should:

- use path-scoped triggers;
- declare least-privilege permissions;
- use GitHub-hosted runners unless separately justified;
- avoid privileged pull-request events for untrusted code;
- invoke repository-owned validators rather than duplicating logic inline;
- run without live source access by default;
- fail closed on missing schema, parser, source, fixtures, policy, or receipt;
- expose stable check names only after branch-protection coordination;
- never publish from an ordinary validation job.

No current workflow result is claimed by this README.

[Back to top](#top)

---

## Review, versioning, and change discipline

### Review roles

Material shared watcher-spec changes should identify:

- pipeline-spec steward;
- watcher/pipeline steward;
- affected source steward;
- each affected domain steward;
- rights, sensitivity/cultural, and security reviewer;
- validation and fixture owner;
- evidence/receipt steward;
- policy steward;
- release steward when downstream refresh behavior changes;
- docs steward.

[`CODEOWNERS`](../../.github/CODEOWNERS) currently routes `/pipeline_specs/` to `@bartytime4life`. That is GitHub review routing, not proof that domain, rights, security, evidence, policy, or release review occurred.

### Change classes

| Change | Minimum consequence |
|---|---|
| README clarification | Documentation review, link/meta checks, generated receipt when AI-authored. |
| Populate the placeholder | Schema, parser, consumer, source, fixture, test, and placement review. |
| Add a source ref | Admission/activation, rights, sensitivity, and terms review. |
| Add network or schedule behavior | Security, secret, rate-limit, outage, kill-switch, and no-network-CI review. |
| Change materiality | Domain, source, policy, evidence, and false-positive/negative review. |
| Add a domain inheritance rule | Deterministic effective-config and no-weakening tests. |
| Add catalog/release handoff | Evidence, receipt, review, release, correction, and rollback review. |
| Move/rename/consolidate a watcher lane | ADR or migration note, consumer inventory, deprecation, and rollback. |

### Versioning

- Do not reuse a version for different semantics.
- Preserve content digests and supersession lineage.
- Distinguish `proposed`, `candidate`, `active_internal`, `active`, `disabled`, `deprecated`, `superseded`, and `retired`.
- Merge state is not activation.
- Activation is not release.
- Schedule configuration is not proof of successful execution.
- Successful execution is not proof of material domain change.

[Back to top](#top)

---

## Deactivation, correction, and rollback

### Documentation rollback

This README update is reversible through normal Git rollback. It changes no executable or public state.

### Future spec deactivation

An active watcher spec should be disabled through an explicit control record that preserves:

- spec ID/version/digest;
- source and consumer bindings;
- reason and effective time;
- schedules and last run refs;
- affected domains and downstream candidates;
- reviewer and decision state;
- correction/withdrawal obligations;
- rollback target.

### Correction propagation

A corrected source descriptor, rights decision, sensitivity decision, comparison baseline, parser, consumer, materiality rule, or watcher spec may invalidate:

- prior candidate reports;
- quarantine/review handoffs;
- watcher receipts;
- downstream ingest decisions;
- processed derivatives;
- EvidenceBundles;
- catalog/triplet records;
- released layers, APIs, exports, screenshots, and generated summaries.

Dependency tracking and invalidation behavior remain `UNKNOWN` until verified by implementation, tests, records, and drills.

### Consolidation rollback

If duplicated watcher lanes are consolidated:

1. inventory every reference and consumer;
2. choose authority through ADR/migration review;
3. add compatibility pointers only where needed;
4. prevent both paths from executing;
5. preserve history and old digests;
6. validate effective configuration;
7. retain a mechanical rollback target.

[Back to top](#top)

---

## Definition of done for an active shared watcher spec

A shared watcher YAML is not active merely because it exists, parses, merges, or contains a schedule.

- [ ] Canonical placement and shared/domain delegation are approved.
- [ ] Stable spec ID, version, digest, status, owners, and supersession exist.
- [ ] Accepted machine schema exists.
- [ ] One parser and one executable consumer are verified.
- [ ] SourceDescriptor refs and activation states resolve.
- [ ] Rights, terms, sensitivity, sovereignty/cultural, and security posture are reviewed.
- [ ] Prior-state baseline and comparison methods are explicit.
- [ ] Cadence, retry, outage, stale-state, no-op, replay, idempotency, and concurrency are bounded.
- [ ] Materiality classes, finite outcomes, and reason codes are accepted.
- [ ] Candidate, quarantine, review, and error handoffs are schema-backed.
- [ ] Sensitive diffs and logs are minimized.
- [ ] Deterministic no-network valid/invalid/denied/abstain/error fixtures exist.
- [ ] Parser-consumer agreement and no-weakening delegation tests pass.
- [ ] No direct fetch, RAW admission, normalization, catalog, release, or public writes are enforced.
- [ ] Watcher receipts are emitted and validated.
- [ ] CI invokes real repository-owned checks and fails closed.
- [ ] Activation, deactivation, correction, supersession, migration, and rollback are documented.
- [ ] Human review is separate from generation, validation, merge, activation, release, and publication.

Until then, label the file `PROPOSED`, `PLACEHOLDER`, or `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Open verification register

| Item | Status | Evidence needed |
|---|---|---|
| Exhaustive direct and recursive watcher-spec inventory | `NEEDS VERIFICATION` | Recursive tree at pinned commit. |
| Canonical shared watcher-spec schema | `UNKNOWN` | Accepted schema/ADR plus fixtures and validator. |
| Parser and shared consumer | `UNKNOWN` | Executable implementation and agreement tests. |
| Active watcher registry/discovery | `UNKNOWN` | Machine registry and current entries. |
| Shared-versus-domain delegation rule | `NEEDS VERIFICATION` | ADR/contract/schema/tests. |
| `plants_drift` canonical placement | `CONFLICTED` | Flora/shared decision and migration note. |
| Executable watcher ownership | `CONFLICTED` | Responsibility review across pipelines/tools/ingest/domain lanes. |
| Source activation and descriptor vocabulary | `NEEDS VERIFICATION` | Accepted ADR/register/schema/policy. |
| Rights, terms, sensitivity, sovereignty, and security enforcement | `NEEDS VERIFICATION` | Binding policy, fixtures, tests, and review records. |
| Shared watcher fixtures and tests | `NOT ESTABLISHED` | Concrete files and current pass results. |
| Default no-network enforcement | `NEEDS VERIFICATION` | Harness and CI evidence. |
| Scheduler, cadence, retry, and stale-state implementation | `UNKNOWN` | Config/runtime/tests/logs. |
| Materiality and reason-code vocabulary | `NEEDS VERIFICATION` | Contracts, schemas, policy, tests. |
| Watcher report/receipt schemas and emitted instances | `UNKNOWN` | Accepted schemas and validated records. |
| Branch protection and required checks | `UNKNOWN` | Repository settings evidence. |
| Production use and operational monitoring | `UNKNOWN` | Deployment, logs, dashboards, run records. |
| Correction propagation and rollback execution | `UNKNOWN` | Dependency graph, tests, runbooks, records, drills. |
| Named owners and separation of duties | `NEEDS VERIFICATION` | Verified assignments and review records. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observation supported | Status |
|---|---|---:|
| [`pipeline_specs/README.md`](../README.md) | `pipeline_specs/` owns declarative configuration and cannot satisfy gates by existence. | `CONFIRMED` |
| [`plants_drift.yaml`](plants_drift.yaml) | One seven-line direct `PROPOSED` placeholder exists. | `CONFIRMED` |
| [`pipelines/watchers/README.md`](../../pipelines/watchers/README.md) | Shared executable orchestration is documented; concrete behavior remains unverified. | `CONFIRMED README / NEEDS VERIFICATION behavior` |
| [`tools/watchers/README.md`](../../tools/watchers/README.md) | Tooling watcher tree is documentation/compatibility and placement-conflicted. | `CONFIRMED` |
| [`pipeline_specs/flora/watchers/README.md`](../flora/watchers/README.md) | Flora lane is README-only and records duplicate plants-drift placeholders. | `CONFIRMED` |
| [`pipeline_specs/fauna/watchers/README.md`](../fauna/watchers/README.md) | Fauna lane is README-only and has no active watcher spec established. | `CONFIRMED` |
| Checked `tests/pipeline_specs/watchers/README.md` | Path not found. | `CONFIRMED checked-path absence` |
| Checked `fixtures/pipeline_specs/watchers/README.md` | Path not found. | `CONFIRMED checked-path absence` |
| [`ADR-0017`](../../docs/adr/ADR-0017-source-descriptor-admission-process.md) | Source activation/admission process is documented but status is proposed. | `CONFIRMED proposed ADR` |
| [`CODEOWNERS`](../../.github/CODEOWNERS) | `/pipeline_specs/` routes to the verified repository owner; review enforcement remains separate. | `CONFIRMED routing` |
| [`CONTRIBUTING.md`](../../CONTRIBUTING.md) | Responsibility-root placement, scoped branches, generated receipt, validation, and rollback expectations. | `CONFIRMED repository guide` |
| Directory Rules copies | Placement doctrine exists in architecture and doctrine paths with an unresolved placement conflict. | `CONFIRMED files / unresolved placement` |
| [`data/receipts/generated/README.md`](../../data/receipts/generated/README.md) | Generated receipts are process provenance, not proof, approval, release, or publication. | `CONFIRMED` |

### Evidence limits

- Repository search is bounded and index-dependent.
- Checked-path absence is not a full-history or all-branch absence claim.
- Documentation may lag later files or branch-local work.
- No repository clone, recursive tree command, local test run, workflow run log, branch-protection setting, scheduler, source system, runtime dashboard, release artifact, or production environment was inspected by this documentation update.
- Memory and generic watcher best practice were not treated as implementation proof.

[Back to top](#top)

---

## Change history

### v0.2 — 2026-07-18

- replaced planning-only proposed profile trees with a pinned current-state inventory;
- confirmed one direct seven-line plants-drift placeholder and no active shared watcher spec;
- surfaced shared/domain and pipelines/tools/ingest watcher placement conflicts;
- strengthened non-admission, non-publication, metadata-first, source-role, rights, sensitivity, security, evidence, correction, and rollback boundaries;
- added a proposed minimum active spec contract, signal limits, materiality classes, finite outcomes, reason codes, validation matrix, definition of done, and evidence ledger;
- changed documentation only.

### v0.1 — 2026-06-13

- established the initial shared watcher-spec planning contract;
- documented proposed profile families, gates, fixtures, tests, receipts, and handoffs;
- did not verify the direct inventory or current implementation/enforcement state.

[Back to top](#top)
