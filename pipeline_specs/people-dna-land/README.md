<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-people-dna-land-readme
title: pipeline_specs/people-dna-land/ — Governed People / Genealogy / DNA / Land Pipeline Specification Boundary
type: readme
version: v0.2
status: draft; repository-grounded; mixed-scaffold; no-active-specification-established
owners: OWNER_TBD — Pipeline-spec steward · People/DNA/Land domain steward · People assertions steward · Genealogy steward · DNA/genomic steward · Consent and revocation steward · Land-records steward · Living-person privacy steward · Rights reviewer · Sensitivity reviewer · Evidence steward · Policy steward · Validation steward · Release steward · CI steward · Migration steward · Docs steward
created: 2026-06-13
updated: 2026-07-15
supersedes: v0.1
policy_label: restricted-doctrine; people; genealogy; dna; genomic; consent; revocation; land-ownership; living-person-sensitive; private-person-parcel-deny-default; evidence-bound; source-role-aware; declarative-only; no-secrets; no-live-activation; no-public-path; no-publication; release-gated
current_path: pipeline_specs/people-dna-land/README.md
truth_posture: CONFIRMED current target, pipeline_specs root contract, People/DNA/Land executable-pipeline and domain documentation, compatibility alias README, five six-line root YAML scaffolds with empty stages arrays, governed README-only land-ownership child lane, absent checked triplets/rollback/watchers/object-profile/test paths, and TODO-only People/DNA/Land workflow / PROPOSED minimum active-spec contract, finite state model, deterministic consumer binding, source-role and rights gates, living-person classification, consent/revocation/retention requirements, DNA/genomic boundaries, assertion and identity-state rules, land-title boundaries, receipt vocabulary, finite outcomes, validation matrix, migration discipline, correction, deactivation, and rollback requirements / UNKNOWN accepted pipeline-spec schema, parser, registry, loader, scheduler, source activation, executable consumer binding, active profiles, substantive fixtures/tests, validator wiring, receipt emission, CI enforcement, release integration, and production use / NEEDS VERIFICATION owners, exhaustive recursive lane inventory, people versus people-dna-land alias resolution, flat-file versus child-lane convention, schema/contract/policy path resolution, source rights, sensitivity policy implementation, living-person determination, consent authority, DNA tokenization and retention controls, identity-resolution rules, title-interest rules, correction propagation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 37025300a2a3639c4ee68f0dba4b179f6e15b63d
  prior_blob: 235413336e04812fe15ec492384e99f208402bf9
  authoring_prompt_sha256: b061d3d8b153af8083cd1f62f447b389c396b5a882e590328ede7c3e3ff25e85
  direct_lane_files_confirmed:
    - pipeline_specs/people-dna-land/README.md
    - pipeline_specs/people-dna-land/ingest.yaml
    - pipeline_specs/people-dna-land/normalize.yaml
    - pipeline_specs/people-dna-land/validate.yaml
    - pipeline_specs/people-dna-land/catalog.yaml
    - pipeline_specs/people-dna-land/publish.yaml
    - pipeline_specs/people-dna-land/land-ownership/README.md
  compatibility_alias:
    - pipeline_specs/people/README.md
  checked_absent_paths:
    - pipeline_specs/people-dna-land/triplets.yaml
    - pipeline_specs/people-dna-land/rollback.yaml
    - pipeline_specs/people-dna-land/watchers.yaml
    - pipeline_specs/people-dna-land/people_assertions.yaml
    - pipeline_specs/people-dna-land/genealogy_relationships.yaml
    - pipeline_specs/people-dna-land/dna_evidence.yaml
    - pipeline_specs/people-dna-land/consent_revocation.yaml
    - tests/pipeline_specs/people-dna-land/README.md
    - tests/pipeline_specs/people-dna-land/test_spec_shape.py
  workflow_posture: .github/workflows/domain-people-dna-land.yml exists as TODO-only echo scaffolding
related:
  - ../README.md
  - ../people/README.md
  - ./land-ownership/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/domains/people-dna-land/ARCHITECTURE.md
  - ../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md
  - ../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../docs/domains/people-dna-land/CANONICAL_PATHS.md
  - ../../docs/domains/people-dna-land/MISSING_OR_PLANNED_FILES.md
  - ../../docs/domains/people-dna-land/LAND_OWNERSHIP.md
  - ../../pipelines/domains/people-dna-land/README.md
  - ../../pipelines/domains/people-dna-land/land-ownership/README.md
  - ../../contracts/domains/people-dna-land/
  - ../../schemas/contracts/v1/domains/people-dna-land/
  - ../../policy/domains/people-dna-land/
  - ../../policy/sensitivity/people-dna-land/
  - ../../policy/consent/people-dna-land/
  - ../../data/registry/sources/people-dna-land/
  - ../../data/receipts/pipeline/people-dna-land/
  - ../../data/proofs/evidence_bundle/
  - ../../tests/pipeline_specs/people-dna-land/
  - ../../fixtures/pipeline_specs/people-dna-land/
  - ../../release/candidates/people-dna-land/
  - ../../release/manifests/people-dna-land/
  - ../../.github/workflows/domain-people-dna-land.yml
notes:
  - "v0.2 replaces a planning-heavy flat-file proposal with a commit-pinned account of the current mixed scaffold: five inert root YAML files and one README-only Land Ownership child lane."
  - "The People compatibility path remains alias-gated and must not become a second source of pipeline-spec authority."
  - "File presence, valid YAML, a populated stages list, a workflow result, or a schedule never establishes source admission, consent, currentness, evidence closure, policy approval, release approval, or publication."
  - "Living-person fields, DNA/genomic material, raw kit/vendor identifiers, private person-parcel joins, exact sensitive locations, unresolved title claims, and unclear-rights sources fail closed by default."
  - "This revision changes documentation only. It does not activate or rewrite the five YAML scaffolds and creates no parser, schema, policy, source, fixture, test, workflow behavior, data object, receipt, proof, or release object."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed People / Genealogy / DNA / Land Pipeline Specification Boundary

`pipeline_specs/people-dna-land/`

> Declarative run-intent boundary for People, Genealogy, DNA/Genomic, Consent, Revocation, and Land Ownership pipelines. A file here may state **what** a verified pipeline should run, against which admitted sources, under which identity, time, rights, consent, privacy, evidence, policy, receipt, and release gates. It does not execute a pipeline, determine a person or relationship as true, authorize genomic use, determine title, approve disclosure, or publish an artifact.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-declarative__spec-green)
![inventory](https://img.shields.io/badge/inventory-5__inert__YAML__stubs%20%2B%20child__README-lightgrey)
![sensitivity](https://img.shields.io/badge/sensitivity-deny__by__default-critical)
![consent](https://img.shields.io/badge/consent-revocation__aware-critical)
![alias](https://img.shields.io/badge/people__alias-no__parallel__authority-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-and-anti-collapse) · [Status](#current-status) · [Inventory](#current-inspected-inventory) · [Placement](#repository-fit-aliases-and-sublanes) · [Scope](#specification-scope) · [File contract](#minimum-active-specification-contract) · [State model](#specification-state-and-activation-model) · [Sources](#source-descriptors-roles-rights-and-activation) · [Assertions](#assertion-identity-and-relationship-boundaries) · [Privacy](#living-person-privacy-consent-revocation-and-retention) · [DNA](#dna-genomic-and-derived-relationship-boundaries) · [Land](#land-ownership-title-and-private-person-parcel-boundaries) · [Time](#temporal-freshness-and-validity-semantics) · [Lifecycle](#lifecycle-gates-and-finite-outcomes) · [Stages](#root-stage-profile-contracts) · [Sublanes](#sublane-and-compatibility-discipline) · [Watchers](#watchers-dry-runs-and-no-op-discipline) · [Receipts](#receipts-evidence-and-emitted-artifacts) · [Security](#security-secrets-logging-network-and-retention) · [Validation](#validation-and-enforceability) · [Review](#review-migration-and-change-discipline) · [Rollback](#correction-deactivation-and-rollback) · [Directory map](#directory-map) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Evidence](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@37025300a2a3639c4ee68f0dba4b179f6e15b63d`
> **Target blob before this revision:** `235413336e04812fe15ec492384e99f208402bf9`
> **Confirmed root stage scaffolds:** `ingest.yaml`, `normalize.yaml`, `validate.yaml`, `catalog.yaml`, and `publish.yaml`; each has `stages: []`
> **Confirmed child lane:** `land-ownership/README.md`; no active child YAML profile was established
> **Activation:** path, filename, merge, valid YAML, workflow completion, source-list text, or a future schedule activates nothing

> [!CAUTION]
> This domain combines several high-consequence claim classes. A person assertion is not a canonical person. A relationship hypothesis is not a confirmed relationship. DNA evidence is not public kinship truth. A consent reference is not perpetual authorization. An assessor record is not title truth. Parcel geometry is not title-boundary proof. A successful run is not an `EvidenceBundle`, `PolicyDecision`, `ReleaseManifest`, or release.

> [!WARNING]
> Real living-person identifiers, raw DNA or genomic data, raw kit/vendor identifiers, private person↔parcel joins, exact sensitive locations, unredacted land instruments, credentials, and secrets do not belong in pipeline specs, examples, fixtures, logs, screenshots, or PR bodies. Use synthetic or irreversibly redacted examples and fail closed when classification, rights, consent, or release state is unresolved.

---

## Purpose

`pipeline_specs/people-dna-land/` is the People / Genealogy / DNA / Land segment under the `pipeline_specs/` responsibility root.

Its safe role is to hold reviewed, deterministic declarative profiles that bind:

- a stable specification identity, version, owner, digest, lineage, and finite state;
- one verified executable consumer under `pipelines/`;
- admitted `SourceDescriptor` references and explicit source roles;
- rights, access, attribution, permitted-use, retention, embargo, and deletion requirements;
- living-person classification and uncertainty behavior;
- consent scope, purpose, expiry, revocation, and dereference-time enforcement where applicable;
- assertion, candidate, reviewed, canonical, hypothesis, and derived-output distinctions;
- DNA/genomic tokenization, restricted-use, aggregation, and non-publication boundaries;
- land-instrument, parcel-version, legal-description, ownership-interval, and title-boundary controls;
- observation, event, valid, source-vintage, retrieval, processing, review, release, correction, and revocation times;
- lifecycle input and output states;
- schema, contract, policy, evidence, review, receipt, catalog, and release requirements;
- no-network fixtures and expected finite outcomes;
- correction, supersession, withdrawal, deactivation, and rollback behavior.

A spec may **require** these controls. It cannot satisfy them merely by naming them.

### Audience

- pipeline-spec and People/DNA/Land maintainers;
- people, genealogy, DNA/genomic, consent, revocation, land-record, parcel, title-assertion, and chain-review stewards;
- source, rights, privacy, sensitivity, temporal, evidence, policy, validation, release, security, and docs reviewers;
- maintainers implementing a future spec schema, parser, registry, loader, scheduler, or executable consumer;
- reviewers preventing the `people` alias, flat root profiles, and nested child lanes from becoming parallel authorities;
- reviewers ensuring all outputs remain assertion-first, consent-aware, title-safe, privacy-safe, evidence-bound, and reversible.

[Back to top](#top)

---

## Authority and anti-collapse

### Responsibility split

```text
pipeline_specs/  = declarative run intent: WHAT may run and under which gates
pipelines/       = executable behavior: HOW processing occurs
connectors/      = source fetch and admission support; never publication
configs/         = safe-to-commit consumer settings; never secrets or activation authority
data/            = lifecycle state, registries, consent/revocation state, receipts, proofs, catalog/triplets, and published artifacts
contracts/       = semantic meaning
schemas/         = machine-checkable shape
policy/          = admissibility, consent, privacy, rights, sensitivity, and release obligations
tests/fixtures/  = enforceability proof and controlled synthetic/redacted examples
release/         = release, correction, supersession, withdrawal, takedown, and rollback authority
apps/            = governed serving surfaces; never direct reads from specs or internal stores
```

Directory Rules assign declarative configuration to `pipeline_specs/` and executable pipeline behavior to `pipelines/`. `people-dna-land` is a domain segment within responsibility roots, not a new root.

### What this README may decide

This README may define the maintenance boundary for the People/DNA/Land pipeline-spec lane:

- what belongs here;
- what must remain under another responsibility root;
- what repository evidence is currently verified;
- what a future active specification must contain;
- which assertion, privacy, consent, DNA, land-title, evidence, and release boundaries must be preserved;
- how root-stage and child-lane specifications must avoid parallel authority;
- what remains `UNKNOWN`, `CONFLICTED`, or `NEEDS VERIFICATION`;
- how a documentation-only change is validated and rolled back.

### What this README cannot decide

This README cannot:

- admit, activate, suspend, retire, or supersede a source;
- determine that a person is living or deceased for release purposes;
- grant, broaden, renew, ignore, or revoke consent;
- define a canonical person, relationship, family, DNA match, or land title by assertion;
- define object meaning, machine schema, policy, source rights, sensitivity, or release authority;
- establish the canonical `people` versus `people-dna-land` segment by assertion;
- establish flat root YAML versus child-lane layout by assertion;
- implement or activate a parser, registry, loader, schedule, connector, pipeline, validator, or public route;
- make stale, provisional, candidate, modeled, or hypothetical material authoritative;
- create an `EvidenceBundle`, close a proof, issue a `PolicyDecision`, approve a release, or publish an artifact;
- authorize a normal UI, map, tile, graph, export, search, screenshot, embedding, automation, or AI path.

### Disallowed collapses

```text
README or path existence                 -> active specification
YAML file presence                       -> active specification
non-empty stages                         -> approved execution plan
valid YAML                               -> valid governed specification
spec validation                          -> data validation
source reference                         -> admitted or active source
source list                              -> source authority
schedule                                 -> freshness proof
successful fetch                         -> source correctness
successful run                           -> EvidenceBundle
successful run                           -> release approval
PersonAssertion                          -> PersonCanonical
identity candidate                       -> canonical identity
RelationshipHypothesis                   -> confirmed relationship
GEDCOM/tree import                       -> authoritative genealogy
DNA match or segment                     -> public kinship truth
consent reference                        -> current or unlimited authorization
missing revocation check                 -> consent still valid
administrative address                   -> verified residence
assessor/tax record                      -> title truth
parcel polygon                           -> title boundary
recorded instrument                      -> automatic current ownership
private person-parcel relation           -> public ownership fact
catalog record                           -> publication
receipt                                  -> proof
proof                                    -> release decision
publish profile                          -> PUBLISHED state
people compatibility alias               -> second canonical authority
generated summary                        -> evidence, legal advice, or genealogy determination
```

[Back to top](#top)

---

## Current status

### Safe conclusion

`pipeline_specs/people-dna-land/` is a repository-present declarative lane in a **mixed scaffold state**:

- the root README exists;
- five root stage YAML files exist as inert six-line scaffolds with empty `stages` arrays;
- a governed `land-ownership/README.md` child lane exists but no active child profile was established;
- `pipeline_specs/people/README.md` exists as a compatibility alias outside this directory;
- no parser-bound, consumer-bound, source-bound, scheduled, fixture-proven, receipt-emitting, release-linked active People/DNA/Land specification was established by the bounded inspection.

### Maturity matrix

| Capability or artifact | Status | Evidence-bounded conclusion |
|---|---:|---|
| Root README | `CONFIRMED` | `pipeline_specs/people-dna-land/README.md` existed as v0.1 before this revision. |
| `ingest.yaml` | `CONFIRMED SCAFFOLD` | Six lines; `name: people-dna-land-ingest`, `version: 1`, `stages: []`. |
| `normalize.yaml` | `CONFIRMED SCAFFOLD` | Six lines; `name: people-dna-land-normalize`, `version: 1`, `stages: []`. |
| `validate.yaml` | `CONFIRMED SCAFFOLD` | Six lines; `name: people-dna-land-validate`, `version: 1`, `stages: []`. |
| `catalog.yaml` | `CONFIRMED SCAFFOLD` | Six lines; `name: people-dna-land-catalog`, `version: 1`, `stages: []`. |
| `publish.yaml` | `CONFIRMED SCAFFOLD` | Six lines; `name: people-dna-land-publish`, `version: 1`, `stages: []`. |
| Land Ownership child README | `CONFIRMED DOCUMENTATION` | Governed README-only child lane; not an active specification. |
| `people` compatibility alias | `CONFIRMED DOCUMENTATION / CONFLICTED` | Alias README exists; canonical segment decision remains unresolved. |
| Root `triplets.yaml`, `rollback.yaml`, `watchers.yaml` | `NOT FOUND AT CHECKED PATHS` | Exact path checks returned not found. |
| Object-profile YAML files checked | `NOT FOUND AT CHECKED PATHS` | People assertions, genealogy relationships, DNA evidence, and consent/revocation profile names were absent at checked paths. |
| Pipeline-spec tests checked | `NOT FOUND AT CHECKED PATHS` | Root pipeline-spec test README and `test_spec_shape.py` were absent. |
| Accepted spec schema | `UNKNOWN` | No accepted machine schema or validator was established. |
| Parser, registry, loader, scheduler | `UNKNOWN` | No deterministic runtime binding was established. |
| Executable consumers | `NEEDS VERIFICATION` | Documentation names intended lanes; runtime behavior was not proven. |
| Active source descriptors | `NEEDS VERIFICATION` | Source activation, rights, and sensitivity review require separate evidence. |
| Consent/revocation enforcement | `NEEDS VERIFICATION` | Doctrine requires it; operational enforcement was not established. |
| Domain workflow | `CONFIRMED TODO SCAFFOLD` | Workflow jobs only echo TODO text. |
| Public or production use | `NOT ESTABLISHED` | No release or runtime evidence was established. |

### Truth labels used here

- **CONFIRMED** — verified from current repository content in this session.
- **PROPOSED** — a design or requirement not yet established in implementation.
- **UNKNOWN** — not verified strongly enough to claim.
- **NEEDS VERIFICATION** — checkable, but more evidence is required.
- **CONFLICTED** — current documentation exposes competing conventions requiring resolution.

[Back to top](#top)

---

## Current inspected inventory

### Confirmed direct-lane structure

```text
pipeline_specs/people-dna-land/
├── README.md                 # governed parent boundary
├── ingest.yaml               # CONFIRMED inert scaffold; stages: []
├── normalize.yaml            # CONFIRMED inert scaffold; stages: []
├── validate.yaml             # CONFIRMED inert scaffold; stages: []
├── catalog.yaml              # CONFIRMED inert scaffold; stages: []
├── publish.yaml              # CONFIRMED inert scaffold; stages: []
└── land-ownership/
    └── README.md             # CONFIRMED governed child boundary; README-only in bounded inspection
```

### Current root YAML shape

Each inspected root YAML uses the same scaffold pattern:

```yaml
# pipeline_specs :: people-dna-land :: <stage>
name: people-dna-land-<stage>
version: 1
stages: []
```

This proves only file presence and current text. It does **not** prove:

- accepted schema compliance;
- a valid stage vocabulary;
- source admission or activation;
- consent or revocation enforcement;
- fixture or negative-test coverage;
- executable consumer binding;
- deterministic outputs;
- receipt emission;
- policy evaluation;
- release integration;
- production use.

### Checked absent candidates

The following exact paths were checked and were not present:

```text
pipeline_specs/people-dna-land/triplets.yaml
pipeline_specs/people-dna-land/rollback.yaml
pipeline_specs/people-dna-land/watchers.yaml
pipeline_specs/people-dna-land/people_assertions.yaml
pipeline_specs/people-dna-land/genealogy_relationships.yaml
pipeline_specs/people-dna-land/dna_evidence.yaml
pipeline_specs/people-dna-land/consent_revocation.yaml
tests/pipeline_specs/people-dna-land/README.md
tests/pipeline_specs/people-dna-land/test_spec_shape.py
```

This is a bounded path check, not a complete recursive filesystem proof.

### Compatibility lane

`pipeline_specs/people/README.md` exists and explicitly describes itself as a compatibility alias. It cannot be used to bypass or weaken People/DNA/Land controls, and it must not become an independent source registry, schema home, policy home, activation registry, or release path.

### Child lane

`pipeline_specs/people-dna-land/land-ownership/README.md` exists as a governed child boundary. Its presence establishes documentation structure, not a child spec registry. Any future child profiles must resolve their relationship to the five root stage profiles and avoid duplicate execution or release authority.

[Back to top](#top)

---

## Repository fit, aliases, and sublanes

### Directory Rules basis

The owning root is `pipeline_specs/` because the target's responsibility is declarative pipeline intent. Executable behavior remains under `pipelines/`. Domain material is placed as a segment under responsibility roots rather than as a new top-level domain root.

### Current segment posture

| Path | Current role | Authority posture |
|---|---|---|
| `pipeline_specs/people-dna-land/` | Parent People/DNA/Land declarative lane | Preferred repository-present bounded-context lane; active-spec authority not established. |
| `pipeline_specs/people/` | Compatibility alias documentation | Must not become parallel authority; canonical disposition requires ADR/migration evidence. |
| `pipeline_specs/people-dna-land/land-ownership/` | Child documentation lane | Narrow title/privacy-safe boundary; no active child specification established. |
| `pipelines/domains/people-dna-land/` | Intended executable companion | Documentation exists; substantive execution needs verification. |

### Open layout conflict

The repository currently exposes two axes of unresolved organization:

1. **segment naming:** `people-dna-land` versus `people`;
2. **profile layout:** root stage profiles versus nested domain/sublane profiles.

This README does not resolve either by assertion.

Before adding a new profile, maintainers must determine whether it is:

- a root lifecycle-stage profile;
- a sublane profile referenced by a root stage;
- a source-family variant;
- a generated derivative of a canonical profile;
- a compatibility alias;
- or a duplicate that should not be created.

A path decision with runtime impact needs a root note or ADR, consumer migration plan, compatibility behavior, and rollback path.

### Public boundary

Public clients must not read pipeline specs or internal lifecycle stores directly. They consume released artifacts through governed interfaces. A spec may configure release prerequisites; it is never itself public truth or a release decision.

[Back to top](#top)

---

## Specification scope

People/DNA/Land specs may describe declarative requirements for these bounded classes.

### People and identity

- person and name assertions;
- identity candidates and reviewed canonicalization inputs;
- life, residence, migration, occupation, membership, burial, and other events;
- as-stated names and identifiers;
- source-specific identity crosswalks;
- historical/non-living public-safe derivatives;
- living-person detection and deny/restrict behavior.

### Genealogy and relationships

- relationship assertions and hypotheses;
- family groups and household candidates;
- parent/child, spouse/partner, guardian, adoption, witness, associate, and other relation types where supported;
- GEDCOM, tree, compiled-genealogy, and user-contributed candidate imports;
- contradiction, conflict, ambiguity, and review profiles;
- public-safe derived relationship products only after release review.

### DNA and genomic evidence

- tokenized DNA evidence references;
- restricted relationship-hypothesis inputs;
- consent, purpose, retention, and revocation requirements;
- aggregate or research-restricted derivatives where policy permits;
- match-quality, method, vendor, and uncertainty metadata by stable reference;
- no-public-raw-data and no-public-segment constraints.

### Land ownership

- land instruments and recorded-document evidence;
- assessor and tax administrative context;
- parcel and geography versions;
- legal descriptions and parsing caveats;
- ownership assertion and interval candidates;
- chain gaps, contradictions, and review handoffs;
- private person-parcel deny/restrict behavior;
- public-safe land derivatives that avoid title and boundary claims.

### Cross-lane context

The lane may reference Spatial Foundation, Settlements, Roads/Rail, Agriculture, Hydrology, Archaeology, Hazards, and other domains for context. Those references do not transfer authority or weaken People/DNA/Land privacy, consent, title, rights, evidence, or release controls.

[Back to top](#top)

---

## Minimum active specification contract

The following is a **PROPOSED minimum**. It is not a claim that the repository has accepted this exact field shape.

### Identity and lineage

An active spec must declare or resolve:

- canonical `schema_version`;
- stable `spec_id`;
- human-readable name and purpose;
- semantic version;
- finite status;
- owner and required reviewers;
- created, approved, superseded, and retired timestamps where applicable;
- canonical content digest;
- predecessor/successor references;
- generator source if generated;
- compatibility aliases;
- correction and rollback references.

### Consumer binding

An active spec must bind deterministically to:

- one executable pipeline consumer;
- an implementation revision or release;
- an accepted entrypoint or registry key;
- supported spec versions;
- allowed execution modes;
- input and output contracts;
- network and permission posture;
- deterministic dry-run behavior;
- finite failure behavior.

A name such as `people-dna-land-ingest` is not a binding by itself.

### Source and rights binding

For each source, the spec must resolve:

- stable `SourceDescriptor` reference;
- activation state;
- source role;
- original provider and authority;
- rights, terms, attribution, access, and redistribution obligations;
- sensitivity and personal-data classification;
- allowed purpose and audience;
- retention and deletion requirements;
- source cadence and expected vintage;
- correction, withdrawal, and outage behavior.

### Classification and policy

An active spec must declare:

- object/claim classes it may process;
- living-person classification behavior;
- consent applicability and authority;
- purpose limitation;
- sensitivity tier or policy reference;
- allowed transforms;
- review requirements;
- public, restricted, denied, quarantine, and abstain outcomes;
- re-identification and sensitive-join controls;
- release blockers.

### Evidence and receipts

An active spec must declare:

- required `EvidenceRef` inputs;
- when those references must resolve to `EvidenceBundle`;
- required source, transform, validation, review, policy, consent, revocation, redaction, aggregation, lineage, release-readiness, correction, and rollback receipts;
- receipt schema versions;
- content hashing and deterministic replay rules;
- evidence failure behavior;
- proof versus receipt separation.

### Example shape

```yaml
# PROPOSED EXAMPLE ONLY — not an accepted repository schema
schema_version: kfm.pipeline_spec.people_dna_land.v1
spec_id: people-dna-land.<profile>
version: 0.2.0
status: draft
owner: <owner-ref>
consumer:
  pipeline_ref: pipelines/domains/people-dna-land/<entrypoint>
  implementation_ref: <immutable-revision>
  execution_mode: dry_run_first
sources:
  descriptor_refs: []
  require_active: true
  require_explicit_roles: true
lifecycle:
  accepted_input_states: [WORK]
  intended_output_state: PROCESSED
  quarantine_on_failure: true
privacy:
  living_person_fail_closed: true
  private_person_parcel_fail_closed: true
consent:
  required_when_applicable: true
  revocation_check_at_use: true
  purpose_binding_required: true
dna:
  raw_kit_ids_forbidden: true
  raw_segments_public_forbidden: true
land:
  assessor_tax_context_only: true
  parcel_geometry_not_title_boundary: true
evidence:
  evidence_bundle_required_for_claims: true
receipts:
  required: []
release:
  release_ready: false
  release_authority_external: true
failure:
  default: quarantine
```

[Back to top](#top)

---

## Specification state and activation model

### Proposed finite states

```text
DRAFT
  -> REVIEW
  -> APPROVED_INACTIVE
  -> ACTIVE
  -> SUSPENDED
  -> RETIRED
  -> SUPERSEDED
  -> WITHDRAWN
```

The accepted state vocabulary is `UNKNOWN`; the labels above express the minimum lifecycle distinction needed for safe operation.

### Activation prerequisites

Activation must require evidence of:

1. accepted schema and successful validation;
2. approved owner and reviewers;
3. deterministic consumer binding;
4. active and reviewed source descriptors;
5. rights, sensitivity, purpose, consent, retention, and deletion closure;
6. valid and negative no-network fixtures;
7. assertion, living-person, DNA, land-title, and alias-boundary tests;
8. receipt and evidence resolution;
9. dry-run output review;
10. operational and release approval distinct from authorship;
11. correction, suspension, and rollback procedures;
12. audit record of the activation decision.

### Non-activation events

None of the following activates a specification:

- creating a file;
- adding non-empty stages;
- merging a PR;
- passing YAML syntax validation;
- passing the current TODO-only domain workflow;
- adding a schedule;
- naming a source;
- producing a run receipt;
- producing an evidence bundle;
- adding a publish profile.

### Suspension and fail-safe behavior

A spec must support suspension for:

- revoked or expired consent;
- unresolved living-person classification;
- source terms or rights changes;
- sensitivity reclassification;
- source schema drift;
- source-role ambiguity;
- identity-resolution defects;
- DNA/genomic leakage risk;
- private person-parcel leakage;
- title or boundary overclaim;
- evidence or digest failure;
- security incident;
- erroneous public output;
- correction or takedown request;
- loss of rollback capability.

Suspension preserves prior audit records and blocks future execution or release eligibility. It should not depend on deleting the file.

[Back to top](#top)

---

## Source descriptors, roles, rights, and activation

### Descriptor-first rule

Specs reference source descriptors by stable identifier. They do not define source authority inside YAML and do not activate sources by listing them.

A descriptor must resolve before execution and must carry enough evidence for:

- provider and upstream origin;
- source role;
- rights and attribution;
- access and redistribution constraints;
- sensitivity and personal-data posture;
- purpose limitations;
- cadence and source vintage;
- citation requirements;
- retention/deletion posture;
- current activation state;
- correction and withdrawal path.

### Source-role separation

Source role is preserved through promotion. Typical distinctions include:

- observed or first-hand evidence;
- regulatory or official determination;
- administrative compilation;
- modeled or inferred material;
- aggregate summary;
- candidate or user-contributed material;
- synthetic fixture material.

The canonical vocabulary remains `NEEDS VERIFICATION`; a spec must reference the accepted contract rather than inventing local synonyms.

### Rights and public-record caution

Public availability does not automatically authorize unrestricted copying, republication, aggregation, bulk redistribution, person-level linking, or public map display. Source-by-source rights and jurisdictional restrictions must be reviewed at activation and release time.

### Source withdrawal

A source withdrawal, terms change, correction, or access revocation must support:

- future-run suspension;
- affected-run lookup;
- evidence and release impact analysis;
- downstream cache and derivative review;
- correction, restriction, withdrawal, or rollback;
- retained audit record without retaining prohibited payloads.

[Back to top](#top)

---

## Assertion, identity, and relationship boundaries

### Assertion-first posture

People/DNA/Land processing is assertion-first. Inputs and derived outputs remain in the correct claim state:

```text
source statement
  -> assertion
  -> identity or relationship candidate
  -> reviewed assertion or canonicalization input
  -> release-reviewed derivative
```

A pipeline run cannot skip review state by writing a stronger label.

### Required distinctions

A spec must keep separate:

- as-stated person name and canonical person;
- source identifier and KFM deterministic identifier;
- person assertion and person canonical record;
- relationship assertion and relationship hypothesis;
- family-tree import and reviewed genealogy;
- residence statement and verified residence interval;
- historical/non-living classification and living-person status;
- source contradiction and data error;
- reviewed identity link and speculative link;
- public-safe derivative and canonical/internal record.

### Identity resolution

A spec that participates in identity resolution must declare:

- normalization rules;
- stable source keys;
- deterministic candidate identity;
- similarity or matching method by reference;
- threshold and ambiguity behavior;
- conflict and contradiction handling;
- manual review requirements;
- merge and unmerge receipts;
- correction and downstream invalidation behavior;
- protection against living-person exposure.

Fluent generation, name similarity, or a single source match cannot establish canonical identity.

### Graph and triplet caution

Graph projection is derived. A relationship edge cannot outrank the underlying reviewed assertions, consent state, evidence, policy, and release state. A future `triplets.yaml` could declare projection requirements; it would not create canonical relationship truth.

[Back to top](#top)

---

## Living-person privacy, consent, revocation, and retention

### Fail-closed living-person posture

When living-person status is unknown or disputed, the spec must use the more restrictive applicable policy. It must not infer that a person is deceased merely because a source is old, public, incomplete, or genealogical.

### Minimum privacy controls

A spec must declare or reference:

- living-person determination policy;
- data minimization;
- allowed purpose and audience;
- field-level redaction or withholding;
- relation and join restrictions;
- exact-location restrictions;
- logging and telemetry redaction;
- retention and deletion schedules;
- review requirements;
- correction and takedown behavior;
- public-safe transform receipts;
- re-identification testing where applicable.

### Consent boundary

Where consent is required, a spec must bind to a machine-verifiable consent authority and declare:

- data subject or authorized rights-holder reference;
- allowed purpose;
- allowed data classes;
- allowed audience or processor;
- effective and expiry times;
- jurisdiction or agreement reference;
- retention and deletion terms;
- derivative-use rules;
- revocation endpoint or authority;
- fail-closed behavior when consent cannot be verified.

A static `ConsentGrant` identifier in a spec is not proof that consent is current or applicable to a run.

### Revocation

Revocation must be checked at the policy-defined use point. A revocation or withdrawal must be able to trigger:

- future-run suspension;
- quarantine or denial of pending outputs;
- derivative and cache impact analysis;
- release withdrawal or restriction;
- correction notice;
- deletion or retention action according to policy;
- new audit and rollback records.

### Retention and deletion

Specs must not retain sensitive payloads, logs, fixtures, or derived joins merely because a pipeline completed. Retention and deletion are governed obligations, not optional cleanup.

[Back to top](#top)

---

## DNA, genomic, and derived relationship boundaries

### Default posture

DNA/genomic material and DNA-derived relationship outputs are restricted or denied by default according to applicable policy. The repository doctrine describes a strongest-default-deny posture; accepted policy implementation remains `NEEDS VERIFICATION`.

### Forbidden content in specs and examples

Do not place in this directory:

- raw sequence or genotype data;
- DNA segment coordinates;
- raw match lists;
- vendor kit identifiers;
- account identifiers;
- authentication tokens;
- triangulation details tied to identifiable people;
- unredacted screenshots or exports;
- real consent tokens or agreement documents;
- real living-person DNA-derived hypotheses.

### Required DNA controls

An active DNA-related spec must declare or reference:

- tokenized or opaque evidence references;
- approved purpose and audience;
- consent and revocation requirements;
- vendor/source rights and export restrictions;
- retention and deletion rules;
- encryption and access-control expectations;
- permitted methods and uncertainty representation;
- non-public raw-data boundary;
- hypothesis-versus-assertion distinction;
- aggregation or anonymization requirements;
- re-identification risk testing;
- denial behavior when controls cannot be proven.

### Derived relationship rule

DNA evidence may support a relationship hypothesis under governed review. It cannot, by itself, become a public kinship claim, canonical family edge, legal relationship, inheritance conclusion, or identity determination.

[Back to top](#top)

---

## Land ownership, title, and private person-parcel boundaries

### Evidence, not title

Land-related specs must preserve:

```text
assessor/tax record    = administrative context, not title
parcel geometry        = versioned spatial record, not title boundary
recorded instrument    = evidence of recorded content, not automatic current title
ownership assertion    = evidence-bound candidate, not public ownership label
chain-of-title output  = candidate/gap/contradiction report, not title opinion
```

### Private person-parcel joins

A relation between an identifiable living person and a precise parcel is denied or restricted by default. Any more-public derivative requires explicit policy, transformation, review, release, correction, and rollback closure.

### Land child lane

The current `land-ownership/README.md` child defines a narrower declarative boundary. Parent and child maintainers must prevent:

- duplicate stage execution;
- conflicting source activation;
- inconsistent sensitivity rules;
- competing title or parcel vocabularies;
- duplicate receipts or release authority;
- mismatched correction/rollback behavior.

### Legal authority boundary

KFM is not a recorder, court, surveyor, title company, title insurer, attorney, or legal authority. Specs and generated output must not present legal advice, marketable-title determinations, boundary adjudications, heirship rulings, or official ownership certification.

[Back to top](#top)

---

## Temporal, freshness, and validity semantics

People/DNA/Land claims are time-aware. A spec must preserve the distinct times that apply to its inputs and outputs.

### Candidate time kinds

Depending on the profile, relevant times may include:

- event time;
- assertion or statement time;
- birth/death or life-event interval;
- relationship valid interval;
- residence interval;
- instrument execution/effective/acknowledgment/recording time;
- ownership valid interval;
- source-vintage time;
- consent effective/expiry/revocation time;
- embargo time;
- retrieval time;
- processing time;
- review time;
- release time;
- correction, withdrawal, or rollback time.

The accepted temporal contract remains `NEEDS VERIFICATION`; a spec must reference it rather than redefining field meanings locally.

### Freshness

A schedule is not freshness proof. Freshness must consider:

- source cadence;
- expected update latency;
- last successful source check;
- source vintage;
- correction or withdrawal notices;
- consent and revocation state;
- review age;
- release age;
- policy-defined stale threshold;
- outage behavior.

### Time ordering

Validation must reject or quarantine impossible or unsupported ordering, such as:

- processing before retrieval;
- release before review;
- consent use outside its valid interval;
- continued use after revocation when policy forbids it;
- ownership interval unsupported by instrument timing;
- event or relationship intervals that contradict accepted evidence without an explicit contradiction state.

### Historical does not mean safe

Old records may still identify living people, expose family relations, reveal sensitive ancestry or DNA implications, or enable private parcel linkage. Age alone is not a public-release rule.

[Back to top](#top)

---

## Lifecycle gates and finite outcomes

The governing lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare intended transitions. It cannot perform or approve them merely by existing.

### RAW admission requirements

- active source descriptor;
- source role;
- rights and access posture;
- sensitivity and personal-data classification;
- content hash or governed reference;
- retrieval and source-vintage time;
- consent/purpose posture where applicable;
- immutable capture or approved reference behavior;
- admission receipt.

### WORK / QUARANTINE requirements

- normalization rules;
- assertion and identity-state preservation;
- living-person classification;
- consent and revocation check;
- rights and sensitivity evaluation;
- DNA and private-join controls;
- title/parcel anti-collapse checks;
- deterministic identifiers;
- temporal checks;
- quarantine reason on failure;
- transform and validation receipts.

### PROCESSED requirements

- accepted contracts and schemas;
- successful validation;
- evidence references;
- policy outcome;
- privacy/sensitivity transform state;
- correction lineage;
- stable content digest;
- no unresolved deny condition.

### CATALOG / TRIPLET requirements

- catalog closure;
- evidence bundle resolution appropriate to the claim;
- source and assertion-state preservation;
- sensitivity and access metadata;
- graph projections subordinate to canonical evidence;
- lineage and correction support;
- no public alias implied.

### PUBLISHED requirements

- public-safe representation;
- resolved rights and purpose;
- living-person and consent closure;
- DNA, title, parcel, and sensitive-join closure;
- release manifest;
- independent review where required;
- rollback target;
- correction and takedown path;
- governed API/public-surface integration.

### Proposed finite outcomes

A validator or execution consumer should emit a finite, machine-checkable outcome such as:

```text
PASS
NO_OP
QUARANTINE
HOLD_REVIEW
DENY_POLICY
DENY_CONSENT
DENY_RIGHTS
DENY_LIVING_PERSON
DENY_DNA
DENY_PRIVATE_JOIN
DENY_TITLE_OVERCLAIM
DENY_RELEASE
RETRY_LATER
SUSPEND_SPEC
FAIL_VALIDATION
```

The accepted vocabulary remains `NEEDS VERIFICATION`. Free-form prose alone is not an operational failure state.

[Back to top](#top)

---

## Root stage profile contracts

The five present YAML files are scaffolds. The requirements below describe how each would graduate; they do not activate or rewrite them.

### `ingest.yaml`

Before activation, an ingest profile must declare:

- source descriptor references;
- source activation and role checks;
- rights, access, sensitivity, purpose, consent, and retention prerequisites;
- network allowlist and credential reference behavior;
- immutable RAW capture or governed reference behavior;
- content hashing;
- retrieval and source-vintage time;
- no-op behavior;
- admission receipt;
- quarantine and source-withdrawal behavior.

### `normalize.yaml`

Before activation, a normalization profile must declare:

- input contract/schema;
- output contract/schema;
- assertion and candidate-state preservation;
- identity normalization and ambiguity handling;
- temporal normalization;
- DNA tokenization/redaction boundaries;
- person-parcel and exact-location controls;
- land-instrument and parcel-version rules;
- deterministic output and digest behavior;
- transform receipts;
- quarantine conditions.

### `validate.yaml`

Before activation, a validation profile must declare:

- schema and contract checks;
- source descriptor and role checks;
- living-person and consent/revocation checks;
- rights, purpose, sensitivity, and retention checks;
- assertion/canonical/hypothesis anti-collapse checks;
- DNA leakage checks;
- private person-parcel checks;
- assessor/tax/title and geometry/boundary checks;
- evidence resolution;
- negative fixture expectations;
- finite failure outcomes;
- validation receipts.

### `catalog.yaml`

Before activation, a catalog profile must declare:

- catalog object and identifier rules;
- EvidenceRef/EvidenceBundle closure;
- source and assertion-state preservation;
- access and sensitivity metadata;
- public/restricted/denied alias behavior;
- correction and lineage references;
- graph/triplet handoff behavior;
- catalog closure receipt;
- prohibition on treating catalog existence as publication.

### `publish.yaml`

Before activation, a publish-readiness profile must declare:

- release-candidate inputs;
- public-safe representation contract;
- rights and attribution closure;
- living-person and consent closure;
- DNA/genomic and private-join closure;
- title/parcel/legal-authority disclaimers and checks;
- evidence, policy, review, and release dependencies;
- correction, takedown, and rollback targets;
- governed API/public alias behavior;
- denial when any dependency is unresolved.

A publish profile never becomes release authority.

[Back to top](#top)

---

## Sublane and compatibility discipline

### Root versus child responsibilities

The parent lane should own shared People/DNA/Land spec conventions. A child lane should exist only when it has a distinct, reviewable responsibility that cannot be expressed safely as a root variant.

Child profiles must inherit or explicitly reference the parent contract for:

- spec identity and state;
- source descriptor requirements;
- rights and sensitivity;
- lifecycle and finite outcomes;
- evidence and receipts;
- correction and rollback;
- public trust-membrane behavior.

### Land Ownership child

The confirmed Land Ownership child is documentation-only in the bounded inspection. It does not authorize creating parallel stage files or a second scheduler. Any future child activation must identify how the root stage profiles invoke or compose it.

### People alias

The `pipeline_specs/people/` path is compatibility documentation. It must not:

- own a second activation registry;
- own independent source descriptors;
- define weaker privacy or consent rules;
- create divergent object or receipt vocabularies;
- produce independent public aliases;
- bypass child or parent review;
- become canonical merely through usage volume.

### Future DNA or consent child lanes

A future `dna/`, `consent/`, or `revocation/` child lane would require Directory Rules preflight, duplicate analysis, accepted policy/contract boundaries, explicit consumer binding, and an ADR or root note where authority could be split.

[Back to top](#top)

---

## Watchers, dry runs, and no-op discipline

### Watchers are non-publishers

A future watcher profile may detect source changes, consent/revocation changes, terms changes, policy changes, schema drift, or source withdrawal. It may enqueue governed work. It must not:

- admit a source by itself;
- mint canonical people or relationships;
- alter consent authority;
- publish sensitive data;
- approve title or ownership claims;
- bypass evidence, policy, review, or release.

### No-op behavior

A run should produce `NO_OP` or an accepted equivalent when there is no material governed change. A no-op may still emit a lightweight check receipt, but it should not mint new canonical entities, evidence bundles, or releases solely because a schedule fired.

### Dry runs

Dry runs must:

- use synthetic, irreversibly redacted, or approved no-network fixtures;
- write only to approved QA locations;
- never use production credentials by default;
- never create public aliases;
- never persist real sensitive payloads in logs or artifacts;
- produce deterministic outputs and finite outcomes;
- make side effects explicit;
- support safe cleanup.

### Retry and circuit posture

A consumer should distinguish retryable outages from policy denials, consent failures, identity ambiguity, validation failures, and permanent rights restrictions. Retrying cannot convert a denial into permission.

[Back to top](#top)

---

## Receipts, evidence, and emitted artifacts

### Receipt is not proof

Receipts record events and decisions. Proof requires the governed closure appropriate to a claim. A successful run receipt cannot replace an `EvidenceBundle`, policy outcome, review record, or release manifest.

### Candidate receipt families

Depending on the profile, requirements may include:

- source admission/check receipt;
- run receipt;
- transform receipt;
- validation report;
- identity-match or merge/unmerge receipt;
- living-person classification receipt;
- consent verification receipt;
- revocation check receipt;
- redaction or aggregation receipt;
- DNA tokenization or restricted-use receipt;
- land title-boundary validation receipt;
- chain gap/contradiction review receipt;
- policy decision;
- review record;
- catalog closure receipt;
- release-readiness receipt;
- correction notice;
- withdrawal/takedown record;
- rollback card.

The accepted names and schemas remain `NEEDS VERIFICATION`.

### Minimum receipt properties

Receipts should resolve:

- receipt identity and type;
- spec identity/version/digest;
- implementation revision;
- source descriptor refs and source digests;
- run identity;
- lifecycle input/output states;
- actor or service identity;
- times;
- finite outcome;
- evidence and policy refs;
- affected artifact refs;
- correction and rollback lineage;
- content digest/signature where required.

### Evidence resolution

When a claim depends on evidence, an `EvidenceRef` must resolve to the required `EvidenceBundle`. Broken, incomplete, unauthorized, revoked, or policy-blocked evidence fails closed.

[Back to top](#top)

---

## Security, secrets, logging, network, and retention

### Secrets

Never commit:

- API keys;
- passwords;
- OAuth tokens;
- session cookies;
- consent bearer tokens;
- vendor DNA credentials;
- database URLs containing credentials;
- private key material;
- real secret values disguised as examples.

Specs may reference an approved secret identifier only after the configuration contract is verified.

### Network posture

Network access must be explicit, least-privilege, deny-by-default where risk warrants, and limited to approved source hosts and methods. Dry-run and validation paths should prefer no-network fixtures.

### Logging

Logs must not expose:

- living-person identifiers;
- DNA or genomic content;
- raw kit/vendor IDs;
- private person-parcel relations;
- exact sensitive locations;
- unredacted title or court records;
- secrets or authorization headers;
- full source payloads when summaries/digests suffice.

### Retention

Specs must reference approved retention/deletion policy for sensitive inputs, fixtures, outputs, logs, receipts, caches, and workflow artifacts. CI retention defaults are not automatically appropriate for sensitive-domain evidence.

### Supply-chain and parser posture

A future parser or loader must:

- use safe YAML handling;
- reject unknown fields where governance requires;
- avoid arbitrary code execution;
- constrain includes and external references;
- verify schemas and digests;
- prevent path traversal;
- produce deterministic validation results;
- record parser/version identity.

[Back to top](#top)

---

## Validation and enforceability

### Validation layers

An active spec requires more than YAML syntax.

| Layer | Required evidence |
|---|---|
| syntax | safe parser succeeds |
| schema | accepted machine schema validates |
| semantics | contracts and identifiers resolve |
| source | descriptors, roles, rights, activation, vintage resolve |
| privacy | living-person, exact-location, sensitive-join, logging, retention checks pass |
| consent | purpose, scope, expiry, revocation, authority checks pass where applicable |
| DNA | raw-data, tokenization, restricted-use, and re-identification controls pass |
| land | assessor/tax/title, parcel/boundary, instrument/current-title checks pass |
| lifecycle | input/output states and quarantine behavior are legal |
| evidence | EvidenceRef/EvidenceBundle dependencies resolve |
| policy | finite allow/restrict/deny/quarantine/abstain outcome is recorded |
| receipts | required receipt schemas and refs validate |
| consumer | deterministic executable binding resolves |
| fixture | valid and negative no-network fixtures pass |
| release | release dependencies, correction, takedown, and rollback resolve |
| security | secret, network, parser, logging, retention, and permissions checks pass |

### Minimum negative fixtures

A meaningful test corpus should include synthetic or redacted cases for:

- unknown or living person;
- insufficient death evidence;
- ambiguous identity candidate;
- conflicting relationship assertions;
- unsupported genealogy import;
- consent absent, expired, mismatched-purpose, or revoked;
- DNA raw identifier or segment leakage;
- re-identifiable aggregate;
- private person-parcel join;
- exact sensitive location;
- assessor/tax record mislabeled as title;
- parcel geometry mislabeled as boundary proof;
- instrument evidence mislabeled as current ownership;
- chain candidate mislabeled as title opinion;
- inactive or withdrawn source;
- unclear rights;
- stale or future-dated source;
- lifecycle skip;
- missing evidence/receipt/release dependency;
- no material change;
- correction, takedown, and rollback scenarios.

### Current workflow caution

`.github/workflows/domain-people-dna-land.yml` is confirmed as a greenfield scaffold whose jobs only echo TODO text. A successful run of that workflow does **not** establish pipeline-spec validation, privacy enforcement, consent enforcement, proof generation, publish dry-run fidelity, or release readiness.

### Bounded repair rule

A README update must not quietly create code, schemas, policies, descriptors, tests, or workflow behavior to make its claims appear implemented. Missing enforcement remains explicit and belongs in separate, reviewable changes.

[Back to top](#top)

---

## Review, migration, and change discipline

### Review-impact matrix

| Change | Minimum review pressure |
|---|---|
| prose-only clarification with no contract effect | docs + pipeline-spec steward |
| add or rename a root spec | pipeline-spec, domain, consumer, validation, migration, docs |
| add or rename a child lane | Directory Rules preflight, affected sublane, consumer, validation, migration, rollback |
| populate or modify stages | pipeline owner, domain steward, source/rights, privacy/consent, evidence, policy, validation, release as applicable |
| change source refs or roles | source steward + affected domain/policy reviewers |
| change living-person, consent, DNA, or private-join behavior | privacy, consent, rights, DNA/genomic, policy, security, release reviewers |
| change identity or relationship behavior | people/genealogy, evidence, review, downstream consumer reviewers |
| change land title or parcel behavior | land-record, title-assertion, spatial/parcel, policy, release reviewers |
| change release or rollback requirements | release + policy + evidence + domain |
| move or rename the lane or alias | Directory Rules preflight + ADR/migration note + compatibility and rollback plan |

### Duplicate and supersession checks

Before adding a profile:

1. inspect root and child lane files;
2. inspect `pipeline_specs/people/` alias behavior;
3. check whether an existing stage can own the behavior;
4. inspect accepted contracts, schemas, ADRs, and drift registers;
5. identify the single owning responsibility root and consumer;
6. record generation, supersession, or compatibility behavior;
7. avoid parallel spec registries, source lists, policy lists, schema homes, activation mechanisms, or release paths.

### Generated, mirrored, and localized files

A generated or mirrored spec must declare its canonical source, generator version, digest, and edit prohibition. No verified generator or mirror contract was established for this lane.

### Base drift

When the base branch changes during work, compare the old and new base. If the target, child lane, governing docs, schema, workflow, alias, or consumer changed, re-read the affected evidence before mutation.

[Back to top](#top)

---

## Correction, deactivation, and rollback

### Spec correction

A material correction should:

- create a new version rather than silently rewrite historical meaning;
- preserve prior spec identity, digest, and approval lineage;
- explain the defect and affected runs/artifacts;
- identify source, consent, evidence, policy, receipt, catalog, release, and public-surface impact;
- provide re-run, restriction, correction, takedown, withdrawal, or rollback steps;
- prevent reuse of stale approval without review.

### Data-subject, rights-holder, and source corrections

The system must support governed correction or restriction when:

- a living-person classification is wrong;
- identity or relationship linkage is wrong;
- consent is revoked or scope was misapplied;
- a DNA-derived inference is wrong or unauthorized;
- a private person-parcel relation was exposed;
- a title, parcel, or instrument conclusion was overstated;
- a source corrects or withdraws material;
- rights or terms change.

### Deactivation

A source outage, rights change, revocation, privacy issue, schema drift, identity defect, DNA leakage risk, title overclaim, evidence failure, security concern, or incorrect public output may require suspension. Deactivation must be auditable and should not depend on deleting the file.

### Rollback

Rollback may involve:

- returning scheduler/registry binding to a prior approved spec;
- stopping future runs;
- quarantining pending outputs;
- invalidating affected evidence, catalog, graph, and release candidates;
- withdrawing or restricting public artifacts;
- purging governed caches/aliases where required;
- emitting correction, takedown, and rollback records;
- performing a downstream impact sweep.

A future `rollback.yaml` could declare rollback-readiness requirements. It would not execute rollback or become release authority.

### Documentation-only rollback

This README revision can be reverted by reverting its commit. The five existing YAML scaffolds and the Land Ownership child README are not modified by this documentation change.

[Back to top](#top)

---

## Directory map

```text
pipeline_specs/people-dna-land/
├── README.md                 # governed parent boundary; this file
├── ingest.yaml               # CONFIRMED inert scaffold; stages: []
├── normalize.yaml            # CONFIRMED inert scaffold; stages: []
├── validate.yaml             # CONFIRMED inert scaffold; stages: []
├── catalog.yaml              # CONFIRMED inert scaffold; stages: []
├── publish.yaml              # CONFIRMED inert scaffold; stages: []
└── land-ownership/
    └── README.md             # CONFIRMED governed child boundary; no active YAML established

pipeline_specs/people/
└── README.md                 # CONFIRMED compatibility alias; no parallel authority

# Prior README proposals absent at checked paths and not created here:
# triplets.yaml
# rollback.yaml
# watchers.yaml
# people_assertions.yaml
# genealogy_relationships.yaml
# dna_evidence.yaml
# consent_revocation.yaml
```

### Placement rule

Do not create a file merely to make a proposed tree look complete. Each new profile needs:

- verified owner and reviewers;
- accepted spec contract/schema;
- one deterministic consumer;
- active source descriptors;
- rights, privacy, consent, sensitivity, and retention posture;
- lifecycle need;
- valid and negative fixtures;
- substantive tests and receipts;
- correction, deactivation, takedown, and rollback plan;
- duplicate/supersession analysis;
- resolution of root-versus-child and alias relationships.

### Files that do not belong here

| Material | Correct responsibility root |
|---|---|
| executable People/DNA/Land code | `pipelines/domains/people-dna-land/` or accepted sublane |
| source clients | `connectors/<source>/` |
| source descriptors and activation | `data/registry/sources/` |
| consent/revocation records | governed consent/policy/data homes, not spec text |
| object meaning | `contracts/` |
| machine schemas | `schemas/` |
| privacy, consent, rights, sensitivity, title, release policy | `policy/` |
| fixtures and tests | `fixtures/`, `tests/` |
| lifecycle outputs | governed `data/` lifecycle homes |
| receipt and proof instances | `data/receipts/`, `data/proofs/` |
| release decisions, corrections, takedown, rollback | `release/` |
| public API, UI, maps, exports, AI answers | governed `apps/` and released artifacts |
| real people, DNA, title, parcel, court, or source payloads | governed restricted lifecycle stores, never specs |
| secrets | never in the repository |

[Back to top](#top)

---

## Definition of done

### This README revision

| Criterion | Status |
|---|---:|
| identifies the declarative root and executable-companion boundary | `PASS` |
| records the mixed scaffold inventory without overclaiming activation | `PASS` |
| records the five inert root YAML files and governed Land Ownership child | `PASS` |
| surfaces `people` alias and root-versus-child layout conflicts | `PASS` |
| preserves RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED | `PASS` |
| preserves assertion/canonical, hypothesis/relationship, DNA/public, consent/current, assessor/title, geometry/boundary, and private-join separation | `PASS` |
| defines minimum active-spec source, rights, time, privacy, consent, DNA, land, evidence, receipt, validation, correction, and rollback requirements | `PASS` |
| avoids changing YAML, code, schemas, policies, sources, tests, fixtures, workflows, data, receipts, proofs, or releases | `PASS` |
| verifies repository-native checks after PR creation | `PENDING UNTIL CI` |

### Future active specification

A People/DNA/Land spec is not done until:

- identity, version, owner, digest, lineage, and finite state validate;
- one consumer and implementation revision resolve;
- all source descriptors are active and rights/access/retention reviewed;
- source roles remain explicit;
- assertion, identity, relationship, time, living-person, consent, revocation, DNA, land-title, and private-join behavior is explicit;
- accepted contracts, schemas, policies, evidence, reviews, and receipts resolve;
- valid and negative no-network fixtures pass substantive tests;
- secrets, logs, network, access, and retention controls pass;
- dry-run output is deterministic and confined to approved QA locations;
- correction, suspension, takedown, supersession, and rollback are exercised;
- public output remains separately governed by release authority;
- alias and child-lane behavior cannot create parallel authority.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| `PIPE-SPEC-PDL-001` | What is the accepted People/DNA/Land pipeline-spec semantic contract and machine schema? | `UNKNOWN` | Accepted contract/schema and validator evidence. |
| `PIPE-SPEC-PDL-002` | Is there a canonical parser, registry, loader, or scheduler for `pipeline_specs/`? | `UNKNOWN` | Code, tests, runtime/config binding, operation receipt. |
| `PIPE-SPEC-PDL-003` | Which executable consumer owns each of the five present root stubs? | `NEEDS VERIFICATION` | Consumer code and deterministic binding. |
| `PIPE-SPEC-PDL-004` | How is `people-dna-land` versus `people` resolved across specs and other responsibility roots? | `CONFLICTED / NEEDS VERIFICATION` | Directory Rules, accepted ADR, migration state. |
| `PIPE-SPEC-PDL-005` | What is the accepted relationship between root stage specs and nested child lanes? | `CONFLICTED / NEEDS VERIFICATION` | Pipeline-spec architecture decision, root note/ADR, composition and migration plan. |
| `PIPE-SPEC-PDL-006` | Which People/DNA/Land source descriptors are admitted and active? | `NEEDS VERIFICATION` | Registry records, activation decisions, rights/access/retention review. |
| `PIPE-SPEC-PDL-007` | What source-role vocabulary and per-source assignments are accepted? | `NEEDS VERIFICATION` | Contract/ADR, descriptors, fixtures, tests. |
| `PIPE-SPEC-PDL-008` | What living-person classification and uncertainty policy is enforced? | `NEEDS VERIFICATION` | Policy, contracts, negative fixtures, runtime proof. |
| `PIPE-SPEC-PDL-009` | What consent authority, purpose vocabulary, revocation check, retention, and deletion behavior is enforced? | `NEEDS VERIFICATION` | Policy/contract, integration tests, operational receipts. |
| `PIPE-SPEC-PDL-010` | What DNA/genomic evidence, tokenization, restricted-use, and re-identification controls are accepted? | `NEEDS VERIFICATION` | Contracts, policies, security review, fixtures, tests. |
| `PIPE-SPEC-PDL-011` | What assertion, identity-candidate, canonicalization, relationship, contradiction, merge, and unmerge rules are accepted? | `NEEDS VERIFICATION` | Semantic contracts, schemas, validators, review procedures. |
| `PIPE-SPEC-PDL-012` | What time kinds, freshness, interval, and precedence rules are canonical? | `NEEDS VERIFICATION` | Temporal contract, source rules, fixtures, tests. |
| `PIPE-SPEC-PDL-013` | What land title, parcel-version, legal-description, instrument, ownership-interval, and private-join rules are accepted? | `NEEDS VERIFICATION` | Contracts, policies, child-lane tests, review procedure. |
| `PIPE-SPEC-PDL-014` | Where are root pipeline-spec tests and fixtures, and what do they enforce? | `UNKNOWN` | Recursive inventory and executable results. |
| `PIPE-SPEC-PDL-015` | Which receipt and finite-outcome vocabularies are accepted? | `NEEDS VERIFICATION` | Contracts/schemas, emitted examples, validator tests. |
| `PIPE-SPEC-PDL-016` | Does any workflow substantively validate the root YAML files? | `UNKNOWN` | Workflow commands, logs, failure fixtures; current domain workflow is TODO-only. |
| `PIPE-SPEC-PDL-017` | How are activation, suspension, retirement, source withdrawal, consent revocation, correction, takedown, and rollback recorded? | `UNKNOWN` | Accepted governance contract and operational evidence. |
| `PIPE-SPEC-PDL-018` | What is the exhaustive direct-lane and child-lane inventory at the current commit? | `NEEDS VERIFICATION` | Repository-generated recursive inventory. |
| `PIPE-SPEC-PDL-019` | Which current source terms, jurisdictional restrictions, public-record limits, and genomic-use restrictions apply? | `NEEDS VERIFICATION` | Current source-by-source authoritative review. |
| `PIPE-SPEC-PDL-020` | Which outputs, if any, may reach a public tier without exposing living people, DNA/genomic inferences, sensitive relations, or private person-parcel joins? | `NEEDS VERIFICATION` | Accepted policy, transforms, re-identification testing, release review. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | What it supports | What it does not prove |
|---|---:|---|---|
| target prior blob `23541333…` | `CONFIRMED` | Existing root boundary, proposed profile families, and anti-collapse language. | Active specs or enforcement. |
| `pipeline_specs/README.md` | `CONFIRMED DOCUMENTATION` | Root declarative-versus-executable separation and lifecycle posture. | People/DNA/Land runtime behavior. |
| five root YAML blobs | `CONFIRMED SCAFFOLDS` | Direct presence, names, version `1`, and empty `stages`. | Activation, completeness, validity, or correctness. |
| Land Ownership child README blob `71fe7263…` | `CONFIRMED DOCUMENTATION` | Governed child boundary and README-only maturity statement. | Active child profiles or consumer binding. |
| `pipeline_specs/people/README.md` blob `205ff718…` | `CONFIRMED ALIAS DOCUMENTATION` | Compatibility and no-parallel-authority posture. | Accepted canonical alias decision. |
| executable domain README blob `54717daa…` | `CONFIRMED DOCUMENTATION` | Intended executable companion and deny-by-default posture. | Executable behavior or tests. |
| People/DNA/Land sensitivity profile | `CONFIRMED DOCTRINE DOCUMENT` | Living-person, DNA/genomic, consent, private-join, and land-title sensitivity expectations. | Accepted policy implementation. |
| People/DNA/Land canonical-path register | `CONFIRMED PATH DOCUMENT / OPEN CONFLICTS` | Responsibility-root fan-out and segment conflicts. | ADR resolution or runtime binding. |
| People/DNA/Land missing/planned inventory | `CONFIRMED PLANNING DOCUMENT` | Planning lineage and explicit non-proof posture. | Current file presence. |
| `.github/workflows/domain-people-dna-land.yml` blob `2f5c3403…` | `CONFIRMED TODO SCAFFOLD` | Workflow presence and exact echo-only commands. | Substantive validation, consent enforcement, or proof. |
| attached authoring prompt SHA-256 `b061d3d8…` | `CONFIRMED INPUT` | Evidence, concurrency, validation, PR, and rollback discipline. | Repository behavior. |

### Evidence hierarchy

Current repository files and CI/runtime evidence outrank planning documents for implementation behavior. Governing doctrine controls KFM invariants and responsibility placement. Where documents and repository state differ, this README surfaces the difference rather than smoothing it.

[Back to top](#top)

---

## Maintainer note

Keep this lane declarative, assertion-first, privacy-safe, consent-aware, DNA-restrictive, title-safe, evidence-bound, and reversible.

Do not add source clients, executable processing, schemas, contracts, policy decisions, lifecycle outputs, consent records, receipts, EvidenceBundles, release decisions, real people, DNA/genomic payloads, private person-parcel joins, title files, exact sensitive locations, public API/UI behavior, or secrets here.

Do not treat the five root YAML files as active because they exist, and do not create speculative object-profile files merely to complete the old proposed tree. Graduate one profile at a time through explicit placement, schema, consumer, source, rights, privacy, consent, fixture, test, receipt, review, correction, takedown, and rollback gates.

<p align="right"><a href="#top">Back to top</a></p>
