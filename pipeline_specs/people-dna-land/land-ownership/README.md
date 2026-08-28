<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-people-dna-land-land-ownership-readme
title: pipeline_specs/people-dna-land/land-ownership/ — Governed Land Ownership Pipeline Specification Boundary
type: readme
version: v0.2
status: draft; repository-grounded; readme-only; no-active-specification-established
owners: OWNER_TBD — Pipeline-spec steward · People/DNA/Land domain steward · Land-records steward · Title-assertion steward · Parcel/legal-description steward · Living-person privacy steward · Rights reviewer · Sensitivity reviewer · Evidence steward · Policy steward · Validation steward · Release steward · CI steward · Migration steward · Docs steward
created: 2026-06-13
updated: 2026-07-15
supersedes: v0.1
policy_label: restricted-doctrine; title-sensitive; parcel-sensitive; living-person-sensitive; person-parcel-deny-default; evidence-bound; source-role-aware; declarative-only; not-title-opinion; not-legal-advice; no-secrets; no-live-activation; no-public-path; no-publication; release-gated
current_path: pipeline_specs/people-dna-land/land-ownership/README.md
truth_posture: CONFIRMED current target, parent pipeline-spec contract, adjacent executable-pipeline and semantic-contract READMEs, land-ownership and sensitivity doctrine, canonical-path conflict documentation, bounded README-only direct-lane inventory, absent checked single-file and nested-spec paths, TODO-only people-dna-land workflow, and absent checked pipeline-spec test paths / PROPOSED minimum active-spec contract, finite state model, deterministic consumer binding, source-role and rights gates, title/parcel/legal-description boundaries, temporal semantics, living-person and private person-parcel controls, receipt vocabulary, finite failure outcomes, validation matrix, migration discipline, correction, deactivation, and rollback requirements / UNKNOWN accepted pipeline-spec schema, parser, registry, loader, scheduler, source activation, executable consumer binding, active profiles, substantive fixtures/tests, validator wiring, receipt emission, CI enforcement, release integration, and production use / NEEDS VERIFICATION owners, exhaustive recursive inventory, nested-directory versus single-file spec convention, people versus people-dna-land alias resolution, schema/contract/policy path resolution, source rights, living-person classification, parcel identity/version rules, title-interest vocabulary, chain-review controls, correction propagation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: a8cf7411b3ba865495734fb0e9173a717585a488
  prior_blob: cca2a7ac27c5f037480f1caa870b2c9f8d3193be
  direct_lane_files_confirmed:
    - pipeline_specs/people-dna-land/land-ownership/README.md
  checked_absent_paths:
    - pipeline_specs/people-dna-land/land-ownership.yaml
    - pipeline_specs/people-dna-land/land-ownership/ingest.yaml
    - tests/pipeline_specs/people-dna-land/land-ownership/README.md
    - tests/pipeline_specs/people-dna-land/land-ownership/test_spec_shape.py
  bounded_search_result: repository code search surfaced the requested README plus adjacent implementation and contract documentation; no concrete land-ownership YAML profile surfaced
  workflow_posture: .github/workflows/domain-people-dna-land.yml exists as TODO-only echo scaffolding
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../people/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/lifecycle-law.md
  - ../../../../docs/doctrine/trust-membrane.md
  - ../../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md
  - ../../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../../docs/domains/people-dna-land/CANONICAL_PATHS.md
  - ../../../../docs/domains/people-dna-land/MISSING_OR_PLANNED_FILES.md
  - ../../../../pipelines/domains/people-dna-land/README.md
  - ../../../../pipelines/domains/people-dna-land/land-ownership/README.md
  - ../../../../contracts/domains/people-dna-land/land-ownership/README.md
  - ../../../../data/registry/sources/people-dna-land/
  - ../../../../data/receipts/pipeline/people-dna-land/
  - ../../../../data/proofs/evidence_bundle/
  - ../../../../policy/domains/people-dna-land/
  - ../../../../policy/sensitivity/people-dna-land/
  - ../../../../tests/pipeline_specs/people-dna-land/land-ownership/
  - ../../../../fixtures/pipeline_specs/people-dna-land/land-ownership/
  - ../../../../release/candidates/people-dna-land/
  - ../../../../release/manifests/people-dna-land/
  - ../../../../.github/workflows/domain-people-dna-land.yml
notes:
  - "v0.2 applies the KFM repository-grounded documentation implementation profile to the Land Ownership pipeline-spec boundary."
  - "The bounded direct lane is README-only. No active, parser-bound, consumer-bound, source-bound, scheduled, fixture-proven, receipt-emitting, or release-linked Land Ownership specification was established."
  - "The executable sublane README references a proposed single-file pipeline_specs/people-dna-land/land-ownership.yaml, while the current documentation lane is nested at pipeline_specs/people-dna-land/land-ownership/README.md. Neither convention is activated or made canonical by this revision."
  - "Assessor/tax records are administrative context, parcel geometry is not title-boundary proof, recorded instruments are evidence rather than automatic title conclusions, and chain-of-title output remains candidate/review material."
  - "Living-person and private person-parcel joins fail closed by default. No real personal identifiers, title files, parcel-source payloads, or restricted relations belong in pipeline spec files, fixtures, logs, or examples."
  - "This revision changes documentation only. It creates no YAML profile, parser, schema, policy, source activation, fixture, test, workflow behavior, data object, receipt, proof, or release object."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Land Ownership Pipeline Specification Boundary

`pipeline_specs/people-dna-land/land-ownership/`

> Declarative run-intent boundary for evidence-bound Land Ownership pipelines inside the People / Genealogy / DNA / Land domain. A file here may state **what** a verified pipeline should run, against which admitted sources, under which title, parcel, time, privacy, evidence, policy, receipt, and release gates. It does not execute a pipeline, determine title, adjudicate a boundary, certify ownership, publish a private person-parcel relation, or authorize release.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-declarative__spec-green)
![inventory](https://img.shields.io/badge/inventory-README__only-lightgrey)
![title](https://img.shields.io/badge/title-evidence__not__determination-critical)
![privacy](https://img.shields.io/badge/private__person%E2%86%94parcel-T4__deny-critical)
![legal](https://img.shields.io/badge/legal-not__legal__advice-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-and-anti-collapse) · [Status](#current-status) · [Inventory](#current-inspected-inventory) · [Placement](#repository-fit-and-path-conflicts) · [Scope](#land-ownership-specification-scope) · [File contract](#minimum-active-specification-contract) · [State model](#specification-state-and-activation-model) · [Sources](#source-descriptors-roles-rights-and-activation) · [Time](#temporal-and-recording-semantics) · [Identity](#party-parcel-legal-description-and-interest-identity) · [Title boundary](#title-boundary-chain-of-title-and-legal-authority) · [Privacy](#living-person-private-person-parcel-and-sensitive-join-posture) · [Lifecycle](#lifecycle-gates-and-finite-outcomes) · [Stage profiles](#stage-profile-contracts) · [Watchers](#watchers-dry-runs-and-no-op-discipline) · [Receipts](#receipts-evidence-and-emitted-artifacts) · [Security](#security-secrets-retention-and-network-posture) · [Validation](#validation-and-enforceability) · [Review](#review-migration-and-change-discipline) · [Rollback](#correction-deactivation-and-rollback) · [Directory map](#directory-map) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Evidence](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@a8cf7411b3ba865495734fb0e9173a717585a488`
> **Target blob before this revision:** `cca2a7ac27c5f037480f1caa870b2c9f8d3193be`
> **Bounded direct-lane result:** this README only; no concrete Land Ownership YAML profile surfaced
> **Checked absent candidates:** parent `land-ownership.yaml`, nested `ingest.yaml`, and two proposed pipeline-spec test paths
> **Activation:** path, filename, merge, valid YAML, workflow completion, source-list text, or a future schedule activates nothing

> [!CAUTION]
> **KFM land ownership is evidence, not title.** Assessor and tax records are administrative context, parcel geometry is not title-boundary proof, a recorded instrument is evidence of its recorded content rather than an automatic conclusion about current title, and a chain-of-title candidate is not a title opinion. This lane is not legal advice, title insurance, a survey, a court, a recorder, or a legal authority.

> [!WARNING]
> **Sensitive relation boundary:** living-person and private person↔parcel joins are denied or restricted by default. A pipeline spec must never contain real private identifiers, restricted party-parcel joins, raw title files, unredacted instrument images, tax-roll payloads, or secrets. Public exposure requires separate evidence, policy, review, transformation, release, correction, and rollback closure.

---

## Purpose

`pipeline_specs/people-dna-land/land-ownership/` is the Land Ownership sublane under the `pipeline_specs/` responsibility root.

Its safe role is to hold reviewed, deterministic declarative profiles that bind:

- a stable specification identity, version, owner, hash, lineage, and finite state;
- one verified executable consumer under `pipelines/`;
- admitted `SourceDescriptor` references and explicit source roles;
- source rights, access, attribution, retention, and permitted-use requirements;
- instrument type, recording jurisdiction, source citation, and source-vintage requirements;
- execution, effective, acknowledgment, recording, valid, retrieval, processing, release, and correction times where applicable;
- as-stated party references without silently resolving them to canonical living persons;
- parcel identity, parcel version, geography version, geometry source, CRS, scale, and uncertainty constraints;
- original legal-description text plus any normalized or parsed representation and its confidence/caveats;
- interest type, estate, share, encumbrance, easement, lease, lien, mineral, water, access, or other right distinctions when supported;
- ownership-assertion and ownership-interval candidate rules;
- chain-of-title gap, contradiction, ambiguity, supersession, and review behavior;
- living-person, private person-parcel, sensitive-location, and restricted-join controls;
- lifecycle input and output states;
- schema, contract, policy, evidence, review, receipt, catalog, and release requirements;
- no-network fixtures and expected finite failure outcomes;
- correction, supersession, withdrawal, deactivation, and rollback behavior.

A spec may **require** these controls. It cannot satisfy them merely by naming them.

### Audience

- pipeline-spec and People/DNA/Land maintainers;
- land-record, recorder, assessor, tax, parcel, survey, legal-description, title-assertion, and chain-review stewards;
- source, rights, privacy, sensitivity, temporal, spatial, evidence, policy, validation, release, and docs reviewers;
- maintainers implementing a future spec schema, parser, registry, loader, scheduler, or executable consumer;
- reviewers ensuring that Land Ownership outputs remain assertion-first, title-safe, privacy-safe, evidence-bound, non-adjudicative, and reversible.

[Back to top](#top)

---

## Authority and anti-collapse

### Responsibility split

```text
pipeline_specs/  = declarative run intent: WHAT may run and under which gates
pipelines/       = executable behavior: HOW processing occurs
connectors/      = source fetch and admission support; never title or publication authority
configs/         = safe-to-commit consumer settings; never secrets or activation authority
data/            = lifecycle state, registries, receipts, proofs, catalog/triplets, published artifacts
contracts/       = semantic meaning
schemas/         = machine-checkable shape
policy/          = admissibility, rights, privacy, sensitivity, retention, and release obligations
tests/fixtures/  = enforceability proof and controlled examples
release/         = release, correction, supersession, withdrawal, and rollback authority
apps/            = governed serving surfaces; never direct reads from specs or internal stores
external legal authorities = title, boundary, survey, court, recorder, and legal determinations
```

Directory Rules assign declarative configuration to `pipeline_specs/` and executable pipeline behavior to `pipelines/`. `people-dna-land` is a domain segment, and `land-ownership` is a proposed/documented sublane inside that responsibility-root pattern—not a new authority root.

### What this README may decide

This README may define the maintenance boundary for the Land Ownership pipeline-spec lane:

- what belongs here;
- what must remain under another responsibility root;
- what a future active Land Ownership specification must contain;
- which title, parcel, legal-description, source-role, temporal, privacy, evidence, policy, and failure boundaries must be preserved;
- what repository evidence is currently verified;
- what remains `UNKNOWN`, `CONFLICTED`, or `NEEDS VERIFICATION`;
- how a documentation-only change is reviewed and rolled back.

### What this README cannot decide

This README cannot:

- admit, activate, suspend, retire, or supersede a source;
- define legal title, marketable title, ownership certification, boundary adjudication, survey truth, heirship, probate disposition, or legal advice;
- define Land Ownership object meaning, machine schema, policy, rights, sensitivity, retention, or release authority;
- establish a canonical nested-directory versus single-file spec convention by assertion;
- resolve the `people` versus `people-dna-land` naming conflict;
- implement or activate a parser, registry, loader, schedule, connector, pipeline, validator, public route, or map layer;
- convert a source list into source authority;
- convert an assessor or tax record into title truth;
- convert parcel geometry, a parcel ID, PLSS reference, georeference, or legal-description parse into boundary proof;
- convert a recorded instrument mention into proof of current ownership;
- convert an ownership assertion or interval candidate into a public fact;
- convert a chain candidate into a title opinion;
- disclose a private living-person or private person-parcel relation;
- create an `EvidenceBundle`, close a proof, issue a `PolicyDecision`, approve a release, or publish an artifact;
- authorize an AI-generated chain narrative, title summary, or ownership answer as evidence.

### Disallowed collapses

```text
README or path existence                -> active specification
valid YAML                              -> valid governed specification
nested folder                           -> canonical spec layout
single-file proposal                    -> canonical spec layout
spec validation                         -> source/data/title validation
source reference                        -> admitted or active source
recording index                         -> complete instrument
recorded instrument                     -> current title determination
assessor record                         -> title truth
tax record                              -> title truth
parcel polygon                          -> title-boundary proof
current parcel identifier               -> stable historical parcel identity
legal-description parse                 -> survey-grade geometry
grantor/grantee string                  -> canonical living-person identity
instrument party mention                -> confirmed ownership
ownership assertion                     -> public ownership fact
ownership interval candidate            -> complete chain
chain-of-title candidate                -> title opinion
absence of a record                     -> absence of an interest
no contradiction found                  -> chain completeness
private person↔parcel relation          -> public map label
successful pipeline run                 -> EvidenceBundle
successful pipeline run                 -> policy approval
proof                                   -> release decision
publish profile                         -> PUBLISHED state
generated summary                       -> evidence or legal guidance
```

[Back to top](#top)

---

## Current status

### Safe conclusion

`pipeline_specs/people-dna-land/land-ownership/` is a repository-present documentation lane containing this README. No concrete, active, parser-bound, consumer-bound, source-bound, scheduled, fixture-proven, receipt-emitting, policy-approved, or release-linked Land Ownership specification was established by the bounded inspection.

### Maturity matrix

| Capability or artifact | Status | Evidence-bounded conclusion |
|---|---:|---|
| Requested README | `CONFIRMED` | `pipeline_specs/people-dna-land/land-ownership/README.md` exists and was v0.1 before this revision. |
| Direct nested YAML profile | `NOT ESTABLISHED` | Bounded search surfaced no concrete YAML profile in the nested lane. |
| Parent single-file profile | `CHECKED ABSENT` | `pipeline_specs/people-dna-land/land-ownership.yaml` returned not found. |
| Nested `ingest.yaml` | `CHECKED ABSENT` | Proposed path returned not found. |
| Parent lane contract | `CONFIRMED DOCUMENTATION` | `pipeline_specs/people-dna-land/README.md` defines declarative, privacy, consent, assertion, and title boundaries. |
| Executable sublane README | `CONFIRMED DOCUMENTATION` | `pipelines/domains/people-dna-land/land-ownership/README.md` exists and describes intended executable behavior. |
| Executable Land Ownership implementation | `UNKNOWN` | The adjacent README does not prove source-bound executable code, tests, schedules, or receipt emission. |
| Land Ownership semantic-contract README | `CONFIRMED DOCUMENTATION / PROPOSED SUBDIVISION` | Contract orientation exists; it explicitly denies title/legal authority. |
| Domain land-ownership doctrine | `CONFIRMED DOCUMENT` | `LAND_OWNERSHIP.md` preserves evidence-not-title and parcel-geometry boundaries. |
| Sensitivity profile | `CONFIRMED DOCUMENT` | Default-deny posture exists for living-person and private person-parcel material. |
| Canonical path register | `CONFIRMED DOCUMENT / OPEN CONFLICTS` | It records `people` versus `people-dna-land` and responsibility-root path conflicts. |
| Pipeline-spec tests | `NOT ESTABLISHED AT CHECKED PATHS` | Checked README and `test_spec_shape.py` paths returned not found. |
| Domain workflow | `CONFIRMED TODO SCAFFOLD` | `.github/workflows/domain-people-dna-land.yml` only echoes TODO validation/proof/publish-dry-run commands. |
| Accepted pipeline-spec schema | `UNKNOWN` | No accepted semantic contract, machine schema, or validator was established. |
| Active sources and rights | `UNKNOWN` | No active descriptor set, rights decision, or permitted-use binding was established. |
| Release integration | `UNKNOWN` | No release candidate, manifest, correction, or rollback binding was verified for a Land Ownership spec. |

### Evidence labels

- `CONFIRMED` means directly inspected repository content.
- `CHECKED ABSENT` means one exact path was checked and returned not found.
- `NOT ESTABLISHED` means the bounded inspection did not prove the artifact or behavior.
- `PROPOSED` means a recommended contract or design, not implementation.
- `UNKNOWN` means insufficient evidence.
- `NEEDS VERIFICATION` means checkable before activation or release.
- `CONFLICTED` means repository/docs/doctrine surfaces disagree and require explicit resolution.

[Back to top](#top)

---

## Current inspected inventory

### Direct lane

```text
pipeline_specs/people-dna-land/land-ownership/
└── README.md    # CONFIRMED; this file
```

Repository code search for the direct lane surfaced this README plus adjacent implementation and contract documentation. It did not surface a concrete Land Ownership YAML profile.

This is a bounded search result, not a recursive tree guarantee.

### Checked absent candidates

```text
pipeline_specs/people-dna-land/land-ownership.yaml
pipeline_specs/people-dna-land/land-ownership/ingest.yaml
tests/pipeline_specs/people-dna-land/land-ownership/README.md
tests/pipeline_specs/people-dna-land/land-ownership/test_spec_shape.py
```

These exact paths were checked and returned not found at the evidence snapshot commit. Other unqueried files remain `UNKNOWN`; do not treat this list as exhaustive.

### Adjacent evidence surfaces

| Surface | Confirmed role | Does not prove |
|---|---|---|
| `pipeline_specs/people-dna-land/README.md` | Parent declarative boundary and alias warning. | A child profile, parser, or active schedule. |
| `pipelines/domains/people-dna-land/land-ownership/README.md` | Intended executable boundary. | Executable behavior or source integration. |
| `contracts/domains/people-dna-land/land-ownership/README.md` | Proposed semantic-contract subdivision and title/legal exclusions. | Accepted semantic contracts or schemas. |
| `docs/domains/people-dna-land/LAND_OWNERSHIP.md` | Evidence-not-title doctrine and object distinctions. | Current runtime enforcement. |
| `docs/domains/people-dna-land/SENSITIVITY_PROFILE.md` | T4 deny-default and tier-transition posture. | Accepted policy implementation. |
| `docs/domains/people-dna-land/CANONICAL_PATHS.md` | Responsibility-root mapping and path conflicts. | Resolution of those conflicts. |
| `.github/workflows/domain-people-dna-land.yml` | Workflow presence. | Substantive validation; steps currently echo TODO text. |

[Back to top](#top)

---

## Repository fit and path conflicts

### Responsibility-root fit

The current README is correctly located under the `pipeline_specs/` responsibility root for declarative pipeline intent. Land Ownership executable behavior belongs under `pipelines/`, semantic meaning under `contracts/`, machine shape under `schemas/`, policy under `policy/`, test evidence under `tests/` and `fixtures/`, lifecycle objects under `data/`, and release authority under `release/`.

### Nested directory versus single-file conflict

Two current documentation surfaces imply different possible spec layouts:

```text
pipeline_specs/people-dna-land/land-ownership/README.md
pipeline_specs/people-dna-land/land-ownership.yaml    # referenced/proposed elsewhere
```

The nested directory exists as documentation. The single-file candidate was checked and is absent. This README does not decide whether future active specs should be:

- one parent-level `land-ownership.yaml`;
- multiple stage/object profiles under the nested directory;
- one generated form mirrored from another;
- or a different accepted registry layout.

Creating both as independent authorities would be drift. Resolve the convention through an accepted pipeline-spec contract, per-root note, ADR, or migration plan before adding active files.

### Domain-segment conflict

The repository and Directory Rules-oriented docs use `people-dna-land`, while other corpus crosswalks sometimes use `people`. The parent pipeline-spec README also identifies `pipeline_specs/people/` as an alias/conflict path.

This revision follows the current target path and does not create, remove, or ratify either alias. New authority must not be duplicated across both segments.

### Sublane subdivision posture

The `land-ownership` subfolder is a useful documentation and maintenance boundary. It does not automatically authorize sublane-specific parallel schema, policy, source-registry, data-lifecycle, receipt, proof, or release homes. Whole-domain responsibility roots remain authoritative unless an ADR or migration note establishes a narrower split.

[Back to top](#top)

---

## Land Ownership specification scope

A future active specification may declare controlled behavior for these evidence and candidate families:

| Family | Declarative concern | Required boundary |
|---|---|---|
| Land instruments | source, instrument class, jurisdiction, citation, dates, parties as stated | instrument existence/content is evidence, not automatic title conclusion |
| Deed/title instruments | candidate conveyance or title-interest evidence | preserve estate/interest/caveats; no legal opinion |
| Patents, grants, mortgages, liens, easements, leases, probate/court instruments | distinct interest or proceeding classes | do not collapse distinct legal effects |
| Assessor records | administrative assessment context | never title truth |
| Tax records | administrative payment, delinquency, valuation, or roll context | never title truth |
| Parcel versions | source-vintage parcel identity and geometry reference | geometry and current parcel ID are not title-boundary or historical identity proof |
| Legal descriptions | original text, normalized tokens, parsed components, uncertainty | preserve original text; parse is not survey or adjudication |
| Party references | grantor, grantee, owner-of-record, claimant, trustee, executor, heir, entity strings | as-stated reference is not canonical living-person identity |
| Ownership assertions | evidence-bound claim about a party, interest, parcel/version, and interval | assertion remains reviewable and source-cited |
| Ownership intervals | candidate interval composed from assertions | gaps and conflicts remain explicit |
| Chain candidates | ordered candidate links, gaps, contradictions, uncertainty, review handoff | never title determination or completeness claim |
| Public-safe derivatives | aggregate, generalized, redacted, delayed, or restricted products | separate transform, policy, review, release, correction, and rollback closure |

### Explicit non-scope

A spec in this lane must not:

- contain raw deeds, scans, title files, tax rolls, assessor tables, parcel payloads, OCR text, probate packets, survey files, or legal correspondence;
- adjudicate title, ownership, boundary, heirship, probate, easement, mineral, water, access, lien, lease, or severed-estate rights;
- resolve an as-stated party string directly to a living `PersonCanonical` without governed identity review;
- create public person-parcel labels;
- infer absence of an interest from absence of a record;
- hide chain gaps or contradictions;
- turn model/georeference output into authoritative boundary truth;
- issue legal advice or a title opinion;
- bypass source, rights, privacy, sensitivity, evidence, policy, review, and release gates.

[Back to top](#top)

---

## Minimum active specification contract

The following is a **PROPOSED minimum**. It is not a canonical schema. Field names and enumerations remain `NEEDS VERIFICATION` until an accepted contract and machine schema exist.

### Identity and provenance

An active spec should bind:

- `spec_id`;
- `spec_version`;
- finite lifecycle state;
- owner and required reviewers;
- canonical serialized form and digest;
- prior version or superseded spec;
- change reason and migration note;
- created, approved, activated, suspended, retired, and corrected times;
- contract and schema versions;
- policy bundle/version;
- implementation revision;
- fixture-set digest;
- rollback target.

A material change to source scope, title-interest meaning, temporal behavior, identity/parcel rules, privacy posture, policy, output, or release requirements should create a new version rather than silently rewriting prior meaning.

### Deterministic consumer binding

The spec should identify exactly one executable consumer or orchestrated composition:

- implementation path or registry identifier;
- implementation revision or digest;
- accepted input and output lifecycle states;
- supported spec schema versions;
- dry-run entrypoint;
- network permission mode;
- secrets/credential reference names without values;
- expected receipt types;
- output roots;
- timeout, retry, concurrency, and resource budgets;
- correction and rollback handler.

If no consumer can be resolved and verified, the spec is not active.

### Source descriptors and activation

Each source reference should resolve to an admitted `SourceDescriptor` carrying:

- stable source identity;
- product/distribution identity;
- source role;
- role authority;
- jurisdiction and coverage;
- rights, attribution, access, redistribution, and retention posture;
- sensitivity and living-person posture;
- update cadence and freshness expectations;
- source schema/version/vintage;
- endpoint, package, file, or collection identity;
- allowed uses and prohibited uses;
- activation, suspension, and retirement state;
- correction and revocation behavior.

A URL, office name, source list, or README link is not a descriptor and cannot activate a source.

### Source-role requirements

The spec must preserve the admitted role rather than infer one from appearance. Typical land-record classes may include administrative, regulatory, observed, modeled, aggregate, candidate, or other accepted roles, but the exact vocabulary is controlled elsewhere.

At minimum:

- assessor and tax material remains administrative context;
- modeled/georeferenced parcel or boundary material remains modeled or derived;
- chain output remains candidate/review material;
- a recorded instrument is authoritative for its own recorded content only to the extent supported by source role and citation;
- promotion never upgrades source role by implication.

### Rights, access, and permitted use

Before activation, the spec should resolve:

- source terms and legal-use review;
- attribution requirements;
- access restrictions and authentication;
- redistribution and derivative-product permissions;
- public-record access versus unrestricted republication distinctions;
- retention and deletion obligations;
- embargo, seal, expungement, suppression, and restricted-record behavior;
- jurisdiction-specific caveats;
- source shutdown and rights-change response.

Unclear rights or prohibited redistribution routes to `DENY` or `QUARANTINE`, not optimistic publication.

### Living-person and private relation controls

The spec should declare:

- living-person detection or classification source;
- default deny/restrict tier;
- private person-parcel join posture;
- authorized reviewer roles;
- de-identification, aggregation, generalization, redaction, or delay requirements;
- minimum aggregation thresholds where accepted;
- transform receipts;
- review records;
- policy decisions;
- downstream cache/export invalidation;
- correction and withdrawal handling.

No transform makes a private living-person parcel relation public by default. A public aggregate must not permit easy re-identification through small cells, unique geometry, rare names, or cross-layer joins.

### Instrument contract

A Land Ownership spec should require, when applicable:

- stable source-native instrument identifier;
- instrument class and subtype;
- recording jurisdiction and office;
- book/page, reception, document, or equivalent source locator;
- original citation and source URL/reference;
- execution, acknowledgment, effective, recording, filing, retrieval, and processing times as distinct fields;
- parties exactly as stated;
- normalized party references separately;
- consideration or interest text where lawful and necessary;
- legal-description reference;
- parcel/version references as contextual links;
- referenced prior/subsequent instruments;
- OCR/transcription confidence and source;
- correction, re-recording, release, satisfaction, assignment, amendment, or supersession links;
- source-role, rights, sensitivity, and review state.

Missing fields should remain missing or explicitly unresolved. They must not be fabricated from adjacent records.

### Temporal and recording semantics

The spec must not collapse:

- instrument execution time;
- acknowledgment/notarization time;
- effective time;
- recording/filing time;
- source snapshot or roll vintage;
- parcel geometry valid time;
- asserted ownership valid-from / valid-to interval;
- retrieval time;
- processing time;
- review time;
- release time;
- correction or withdrawal time.

Required temporal behavior should include:

- explicit timezone or source convention;
- precision and uncertainty;
- open, closed, and unknown interval semantics;
- precedence rules only when accepted and source-supported;
- gap and overlap detection;
- future/impossible ordering checks;
- late-recording and re-recording handling;
- source-vintage compatibility;
- correction lineage rather than in-place erasure.

A recording date alone does not prove the effective date, duration, or current status of an interest.

### Party identity

The spec should preserve:

- party string exactly as recorded;
- normalized text separately;
- party role within the instrument;
- entity/person classification confidence;
- address or context only when rights and sensitivity permit;
- source citation;
- candidate identity link;
- ambiguity, conflict, and review state.

A grantor, grantee, owner-of-record, heir, trustee, executor, claimant, or entity string is not automatically a canonical person or organization. Living-person resolution remains behind identity, privacy, and policy gates.

### Parcel and geography identity

The spec should bind parcel context to:

- source system;
- source-native parcel identifier;
- parcel version or source vintage;
- geography version;
- geometry source and digest;
- CRS;
- spatial support and scale;
- precision/uncertainty;
- parent/split/merge/supersession relations when supported;
- legal-description reference;
- administrative jurisdiction;
- retrieval and validity times.

A current parcel identifier may be reused, retired, split, merged, or changed. It cannot serve as a timeless ownership key without versioned evidence.

### Legal-description posture

The spec should preserve:

- original legal-description text verbatim;
- source citation and image/page reference;
- normalized form separately;
- PLSS, lot/block, subdivision, metes-and-bounds, or other parsed components when supported;
- parser version and digest;
- confidence and unresolved tokens;
- reference datum/survey/plat context where known;
- geometry derivation method;
- model/run receipt for any derived geometry;
- reviewer disposition.

A parsed legal description or georeferenced polygon is not a survey, boundary adjudication, or title conclusion.

### Interest and estate distinctions

When evidence supports them, the spec should keep distinct:

- fee/title interests;
- life estates;
- tenancy or co-ownership forms;
- leasehold interests;
- mortgages and liens;
- easements and rights-of-way;
- mineral, water, access, railroad, reservation, or severed interests;
- trust, probate, court, tax, foreclosure, or administrative contexts;
- releases, assignments, satisfactions, amendments, and terminations.

The exact vocabulary belongs in accepted contracts and schemas. Unknown or ambiguous interests remain unresolved rather than being forced into a generic owner field.

### Ownership assertion contract

A candidate assertion should bind:

- assertion identity and version;
- party reference;
- parcel/version or legal-description reference;
- interest type and share when supported;
- valid interval or time uncertainty;
- supporting instrument/evidence references;
- source roles;
- contradiction and gap state;
- reviewer state;
- sensitivity tier;
- policy decision;
- correction lineage.

The assertion is a cited claim, not a certified title determination.

### Chain-of-title candidate contract

A chain profile should declare:

- bounded parcel/version or legal-description scope;
- source set and coverage limits;
- ordering rules;
- predecessor/successor candidate rules;
- interval composition rules;
- contradiction detection;
- duplicate and re-recording handling;
- missing-link/gap behavior;
- unresolved party/parcel/interest behavior;
- completeness disclaimer;
- review requirement;
- evidence bundle requirements;
- chain-review receipt;
- correction and re-run behavior.

The pipeline must surface gaps, overlaps, conflicts, and ambiguity. It must not smooth them, invent missing conveyances, or claim completeness because no contradiction was found.

### Lifecycle contract

The spec should declare:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

For each transition it should identify:

- allowed input states;
- proposed output state;
- source, rights, privacy, and sensitivity prerequisites;
- schema/contract versions;
- validation and review gates;
- evidence and receipt requirements;
- quarantine reasons;
- catalog/triplet projection rules;
- public-safe transform requirements;
- release prerequisites;
- correction and rollback obligations.

The spec does not perform the transition. A pipeline run does not promote itself.

### Evidence, policy, review, and release

A claim-bearing output should require resolvable references to:

- source descriptors;
- source payload or source citation;
- validation reports;
- instrument/parcel/legal-description evidence;
- EvidenceRefs and EvidenceBundles where applicable;
- policy decisions;
- redaction/generalization/aggregation receipts;
- review records;
- release manifest;
- correction/withdrawal records;
- rollback target.

Missing closure yields hold, quarantine, abstention, or denial—not a persuasive summary.

### Receipts

Use accepted receipt contracts. The exact canonical receipt vocabulary is `NEEDS VERIFICATION`.

Likely required families include:

- run or execution receipt;
- source/retrieval receipt;
- transform receipt;
- validation report;
- source-role decision;
- identity/crosswalk decision;
- parcel-version decision;
- legal-description parse/model receipt;
- chain-review or contradiction report;
- privacy/sensitivity decision;
- redaction/generalization/aggregation receipt;
- policy decision;
- review record;
- catalog/projection receipt;
- release-readiness receipt;
- correction notice;
- withdrawal record;
- rollback card/receipt.

A receipt records process memory. It is not title, proof, or release authority by itself.

### Fixtures and tests

An active spec should have:

- valid no-network fixtures;
- invalid and negative fixtures;
- synthetic or legally approved minimized samples;
- no real private person-parcel joins;
- no raw title package, restricted probate file, private correspondence, or secret;
- expected finite outcomes;
- deterministic replay expectations;
- parser/schema tests;
- reference-resolution tests;
- source-role tests;
- temporal tests;
- party/parcel/legal-description identity tests;
- assessor/tax anti-collapse tests;
- title/boundary overclaim tests;
- living-person/privacy tests;
- chain gap/contradiction tests;
- no-leak and log-redaction tests;
- correction, suspension, and rollback tests.

### Security and observability

The spec should require:

- no embedded credentials or secret values;
- no secrets in URLs, logs, receipts, fixtures, digests, or errors;
- least-privilege source and storage access;
- no live network by default in unit/CI tests;
- approved egress destinations for any integration run;
- bounded timeouts, retries, concurrency, and circuit breakers;
- structured logs with personal and title-sensitive values redacted;
- metrics that do not expose names, addresses, document numbers, parcel relations, or restricted counts;
- retention and purge behavior;
- auditable access and review events;
- fail-closed behavior when policy, rights, identity, or privacy services are unavailable.

[Back to top](#top)

---

## Specification state and activation model

A file should have a finite state. The exact vocabulary is `PROPOSED` until accepted.

| State | Meaning | May execute? |
|---|---|---:|
| `scaffold` | Placeholder or documentation example; incomplete. | No |
| `proposed` | Authored for review; no activation. | No |
| `validated` | Syntax, schema, references, policy bindings, and fixtures pass. | No |
| `approved` | Required stewards approved a specific digest. | Not until explicit activation |
| `active` | Registry/scheduler binding explicitly enables the approved digest. | Yes, within approved scope |
| `suspended` | Temporarily disabled because of source, rights, privacy, title, security, or operational risk. | No |
| `retired` | Superseded and preserved for lineage/replay. | No |
| `rejected` | Not accepted; reason recorded. | No |

### Activation requirements

Activation should require all of the following:

1. accepted spec contract and schema;
2. canonical digest;
3. verified owner and reviewers;
4. deterministic executable consumer binding;
5. active source descriptors;
6. rights, access, retention, privacy, and sensitivity decisions;
7. title/parcel/legal-description anti-collapse rules;
8. temporal, identity, and chain-review rules;
9. valid and negative no-network fixtures;
10. substantive validator and consumer tests;
11. approved receipt and output contracts;
12. correction, suspension, withdrawal, and rollback plan;
13. explicit activation record separate from merge;
14. dry run and review evidence.

A merge, schedule field, successful syntax check, or green TODO workflow is not activation.

### Proposed gate outcomes

The accepted contract should use a finite, machine-checkable outcome set. Until that set is confirmed, implementations should at least distinguish:

- eligible to continue;
- no material change / no-op;
- quarantine / hold for review;
- deny;
- error.

No implementation should silently convert an unresolved or denied case into success.

[Back to top](#top)

---

## Source descriptors, roles, rights, and activation

### Source admission before spec execution

A future spec may reference admitted sources such as recorder, assessor, tax, parcel, public-land, court, probate, survey, plat, or approved user-supplied materials. The exact source inventory and activation state remain `NEEDS VERIFICATION`.

Each referenced descriptor should establish:

- source identity and authority;
- product/distribution identity;
- jurisdiction and coverage;
- source role;
- rights, access, retention, redistribution, and attribution;
- sensitivity and living-person posture;
- cadence/vintage and change model;
- schema/version;
- source-native identifiers;
- permitted and prohibited uses;
- activation/suspension/retirement;
- correction and source-withdrawal behavior.

### Role preservation

At minimum, the spec should prevent:

```text
assessor/tax administrative context -> title authority
modeled/georeferenced boundary       -> surveyed/legal boundary
user-supplied assertion              -> verified ownership
aggregate parcel statistics          -> parcel/person fact
chain candidate                       -> regulatory/legal determination
```

### Rights and access failures

Route to `DENY` or `QUARANTINE` when:

- source terms are unknown;
- access was unauthorized;
- redistribution is prohibited;
- sealed, expunged, suppressed, or restricted material is detected;
- retention/deletion obligations cannot be met;
- attribution cannot be preserved;
- the requested use exceeds the descriptor's allowed purposes;
- a source or rights holder withdraws permission.

[Back to top](#top)

---

## Temporal and recording semantics

Land Ownership is inherently multi-temporal. A spec should never use one generic timestamp.

### Required time kinds where applicable

| Time | Meaning |
|---|---|
| `execution_time` | When an instrument was executed/signed. |
| `acknowledgment_time` | When acknowledged/notarized, where recorded and relevant. |
| `effective_time` | When the instrument states it becomes effective. |
| `recording_time` | When recorded/filed by the office. |
| `source_vintage` | Snapshot, roll, parcel layer, tax year, or database edition. |
| `parcel_valid_time` | Period for which a parcel version or geography is treated as valid. |
| `asserted_valid_from/to` | Candidate interval for the asserted interest. |
| `retrieval_time` | When KFM acquired the payload/reference. |
| `processing_time` | When the pipeline transformed it. |
| `review_time` | When a reviewer made a decision. |
| `release_time` | When a governed release became effective. |
| `correction_time` | When correction, withdrawal, or rollback was recorded. |

### Temporal safeguards

The spec should require:

- source timezone/convention;
- precision and uncertainty;
- unknown/open interval representation;
- instrument-time versus recording-time separation;
- parcel/source-vintage compatibility;
- overlap, gap, and impossible-order detection;
- re-recording, correction, assignment, release, and satisfaction linkage;
- no assumption that latest record equals current title;
- no assumption that assessor/tax year equals ownership interval;
- no backfilling missing dates from unrelated sources without a cited rule and receipt.

[Back to top](#top)

---

## Party, parcel, legal-description, and interest identity

### Party identity

Keep distinct:

```text
as-stated party string
normalized party string
party role in instrument
candidate person/entity link
reviewed canonical identity
living-person classification
public-safe representation
```

A spec must not skip directly from a recorded name to a canonical living person.

### Parcel identity

Keep distinct:

```text
source parcel identifier
parcel version
geography version
administrative geometry
legal-description reference
derived/georeferenced geometry
ownership assertion
title interest
```

A spec should fail closed when parcel vintage, geometry source, or crosswalk ambiguity cannot support the requested operation.

### Legal descriptions

- preserve original text;
- preserve source/page/image citation;
- store normalized/parsed output separately;
- carry parser/model version and confidence;
- surface unresolved calls, bearings, distances, aliquots, lot/block references, exceptions, reservations, and inconsistencies;
- require review before geometry derivation is used beyond QA/context;
- never describe derived geometry as a survey or title boundary.

### Interest identity

Do not flatten all rights into `owner`. Preserve the interest or encumbrance class supported by evidence. Unknown classes remain unknown.

[Back to top](#top)

---

## Title boundary, chain of title, and legal authority

### Evidence-not-title rule

The lane may build and compare cited assertions. It may not certify title.

### Chain candidate behavior

A chain profile should:

- be bounded to a parcel/version, legal description, jurisdiction, and source set;
- list coverage and known exclusions;
- order evidence using explicit accepted temporal rules;
- preserve instrument and party citations;
- retain candidate links separately from reviewed links;
- identify gaps, overlaps, contradictions, ambiguous parties, ambiguous parcels, and ambiguous interests;
- record unresolved predecessor/successor relations;
- distinguish recorded releases, satisfactions, assignments, amendments, and corrections;
- avoid claiming completeness;
- require qualified review for consequential use;
- carry a disclaimer that KFM is not a title abstract or legal opinion.

### Required denial examples

The spec should deny or quarantine:

- a request to label a current owner from assessor data alone;
- a request to draw a title boundary from parcel geometry alone;
- a request to infer ownership from a party name without an instrument link;
- a request to claim complete chain where gaps or source exclusions exist;
- a request to expose a living private person-parcel relation;
- a request to present generated prose as legal conclusion;
- a request to use KFM output instead of an official record, survey, title search, court order, or qualified professional.

[Back to top](#top)

---

## Living-person, private person-parcel, and sensitive-join posture

### Default posture

The domain sensitivity profile treats private person↔parcel joins as T4/deny by default. A generalized and de-identified relation may remain restricted to reviewer-tier use; public release is not automatic.

### Required controls

A spec handling party or ownership data should declare:

- living/deceased/unknown status and evidence source;
- private/public/entity distinction;
- sensitivity tier;
- consent or legal-basis requirement where applicable;
- purpose limitation;
- access-control group;
- aggregation/generalization/redaction strategy;
- re-identification risk test;
- cross-layer join restrictions;
- review and release authority;
- cache/export invalidation;
- correction and takedown path;
- downstream derivative sweep.

### Public-safe derivatives

A derivative may be considered only when:

- individual living persons are removed or lawfully/reviewedly handled;
- private person-parcel relations are not exposed;
- small-cell and uniqueness risks are controlled;
- exact sensitive residence or family context is withheld/generalized;
- rights and source restrictions permit the derivative;
- transform receipt and review record exist;
- public release manifest and rollback target exist.

A published parcel layer does not authorize ownership labels.

[Back to top](#top)

---

## Lifecycle gates and finite outcomes

### Lifecycle invariant

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

### Declarative gate matrix

| Transition | Spec may require | Spec cannot do |
|---|---|---|
| source edge → RAW | active descriptor, rights/access, role, checksum, source citation, sensitivity | fetch without authorized connector; declare source admitted by text |
| RAW → WORK | immutable input, parser/profile, retention, access, instrument/parcel context | mutate source truth or expose raw material |
| WORK → PROCESSED | schema/contract validation, temporal/identity/title/privacy gates, receipts | convert candidate into title determination |
| WORK → QUARANTINE | finite reason, held artifact ref, review owner, remediation path | silently drop evidence or publish partial result |
| PROCESSED → CATALOG/TRIPLET | evidence refs, projection rules, sensitivity, candidate/review state | make graph/triplet projection canonical truth |
| CATALOG/TRIPLET → PUBLISHED | EvidenceBundle, PolicyDecision, ReviewRecord, transform receipts, ReleaseManifest, correction/rollback | self-promote or expose private/title-sensitive data |

### Minimum finite outcomes

Until a canonical outcome contract is accepted, the behavior must still distinguish:

| Outcome | Meaning |
|---|---|
| continue/eligible | Preconditions pass for the next governed step; not release approval. |
| no-op | No material change or no eligible work; receipt emitted. |
| quarantine/hold | Remediation or qualified review is required. |
| deny | Rights, privacy, title, policy, or prohibited-use rule blocks execution/output. |
| error | Operational failure; no unsafe fallback. |

### Example reason families

- inactive/suspended source;
- rights or access unresolved;
- sealed/restricted record;
- living-person/private join denied;
- unsupported public release;
- instrument identity missing;
- instrument/recording time invalid;
- source-role collapse;
- assessor/tax used as title;
- parcel version or geography mismatch;
- geometry treated as boundary proof;
- legal-description parse unresolved;
- party identity ambiguous;
- interest type ambiguous;
- chain gap or contradiction;
- chain completeness overclaim;
- missing evidence/policy/review/release dependency;
- lifecycle skip;
- no material change;
- retry exhaustion or circuit open;
- correction/rollback required.

[Back to top](#top)

---

## Stage profile contracts

No stage profile is established in the current direct lane. The following rows define what a future profile would need before it could graduate from scaffold to active.

| Profile | Required declarative content | Blocking examples |
|---|---|---|
| `ingest` | source descriptors, allowed products, access/rights, retention, source role, identifiers, checksums, raw/quarantine targets | inactive source, restricted record, missing rights, secret leakage |
| `normalize` | parser/transform versions, original-field preservation, temporal mapping, party/parcel/legal-description handling, receipts | destructive normalization, invented values, identity collapse |
| `validate` | instrument, source-role, temporal, parcel-version, geometry, legal-description, title, privacy, evidence, and policy rules | assessor-as-title, geometry-as-boundary, private join, unresolved chain |
| `catalog` | catalog identity, evidence refs, candidate/review state, rights/sensitivity, correction lineage | uncited catalog item, restricted data leakage, unresolved identity |
| `triplets` | allowed predicates, candidate/review semantics, evidence on every edge, no canonical replacement | graph edge presented as title truth |
| `publish` | public-safe transform, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, rollback/correction | private person-parcel output, title overclaim, absent release |
| `rollback` | affected spec/runs/releases, prior target, alias reversion, cache/export sweep, receipts | delete history, partial rollback, stale public derivative |
| `watchers` | source-change checks, materiality, no-op behavior, candidate emission only | watcher publishes, rewrites chain, or changes title state |
| `instrument` | instrument-type/source/date/party/legal-description gates | recorded mention treated as current ownership |
| `parcel` | parcel-version/geography/geometry/source-vintage/crosswalk gates | current ID treated as timeless identity |
| `chain` | ordering, gaps, contradictions, source coverage, review handoff, disclaimer | completeness/title claim without closure |
| `public-safe derivative` | aggregation/generalization/redaction, re-identification review, release gates | direct ownership label or small-cell disclosure |

[Back to top](#top)

---

## Watchers, dry runs, and no-op discipline

### Watchers observe; they do not publish

A future watcher profile may detect:

- source package or endpoint changes;
- new or corrected recordings;
- source schema changes;
- parcel layer/source-vintage changes;
- rights, access, seal, or retention changes;
- withdrawn/corrected instruments;
- new chain contradictions;
- descriptor suspension or retirement.

It may emit a candidate event or receipt. It must not:

- activate a source;
- rewrite ownership assertions;
- resolve party or parcel identity;
- certify title;
- publish a person-parcel relation;
- update a public map;
- approve a release.

### Dry-run requirements

A dry run should:

- use no network by default;
- use synthetic, minimized, redacted, or explicitly approved fixtures;
- write only to approved QA/temporary locations;
- produce deterministic outputs and receipts;
- exercise denial and quarantine paths;
- never contain real private people, instrument payloads, title files, tax rolls, or parcel joins;
- be clearly labeled non-authoritative.

### No-op

When no material change exists, emit a no-op receipt rather than minting new candidate, catalog, or release objects.

[Back to top](#top)

---

## Receipts, evidence, and emitted artifacts

### Spec versus emitted artifacts

| Artifact | Owned by | Spec relationship |
|---|---|---|
| source descriptor | source registry | stable reference only |
| source payload/reference | RAW/quarantine lifecycle | input contract only |
| normalized candidate | WORK/PROCESSED lifecycle | expected shape/state only |
| validation report | validation/receipt home | required output |
| identity/crosswalk decision | accepted receipt/review home | required when ambiguity is resolved |
| legal-description parse/model receipt | accepted receipt/proof home | required for derived interpretation/geometry |
| chain gap/contradiction report | review/receipt/report home | required chain output |
| EvidenceBundle | proof home | required for claim-bearing output |
| PolicyDecision | policy/receipt home | required for sensitive/release decisions |
| Redaction/Aggregation receipt | receipt home | required for transformed derivative |
| ReviewRecord | review/control-plane home | required where policy says |
| ReleaseManifest | release root | required for publication |
| CorrectionNotice / Withdrawal / RollbackCard | release/correction roots | required for reversibility |

### Citation integrity

Every claim-bearing output should permit a reviewer to reconstruct:

- which source and record support it;
- which party, parcel/version, legal-description, interest, and interval were asserted;
- what transformations occurred;
- what ambiguity, gap, or contradiction remains;
- what rights and sensitivity rules applied;
- who reviewed it;
- whether it was released, corrected, withdrawn, or rolled back.

[Back to top](#top)

---

## Security, secrets, retention, and network posture

### Secrets

Pipeline specs must not contain:

- passwords;
- API keys;
- tokens;
- database URLs with credentials;
- private keys;
- session cookies;
- private document-access URLs;
- raw secret headers;
- sensitive values disguised as examples.

Reference approved secret names only after the consumer/config contract establishes them. Do not invent a canonical environment-variable name in this README.

### Sensitive content

Do not store in a spec, fixture, log, receipt, or example:

- real living-person identifiers;
- private person-parcel joins;
- raw title files or title-company packages;
- unredacted deed/probate/court images;
- private correspondence;
- restricted instrument/document numbers where disclosure is prohibited;
- tax/assessor payloads beyond approved minimized fixtures;
- addresses or contact details used for re-identification;
- DNA or genomic material;
- exact sensitive burial/family/place data;
- sealed, expunged, suppressed, or embargoed content.

### Retention and deletion

A spec should reference—not redefine—approved retention, purge, legal hold, consent/revocation, source withdrawal, correction, and derivative-invalidation policy.

### Network posture

- unit and CI tests use no network by default;
- integration access requires explicit approval and descriptor-gated endpoints;
- egress is allowlisted;
- timeouts, retries, concurrency, and rate behavior are bounded;
- logs redact identifiers and source access details;
- denied or unavailable policy/identity services fail closed.

[Back to top](#top)

---

## Validation and enforceability

### Validation layers

1. **Syntax** — parseable format.
2. **Schema** — accepted pipeline-spec schema.
3. **Semantic** — required fields and coherent combinations.
4. **Reference** — consumer, descriptors, contracts, schemas, policies, fixtures, receipts, release refs resolve.
5. **Source/rights** — active sources and permitted use.
6. **Temporal** — time kinds, precision, ordering, intervals, vintage.
7. **Identity** — instrument, party, parcel/version, geography, legal description, interest.
8. **Anti-collapse** — assessor/tax/title, geometry/boundary, party/canonical person, chain/title.
9. **Privacy/sensitivity** — living-person, private joins, re-identification, restricted records.
10. **Lifecycle** — permitted transitions and quarantine.
11. **Consumer** — deterministic executable binding and supported version.
12. **Fixture/replay** — valid and negative no-network cases.
13. **Receipt/evidence** — expected artifacts and closure.
14. **Release/rollback** — public-safe release and reversal.
15. **Security** — secrets, logs, network, access, retention.

Syntax success alone proves almost nothing about governed readiness.

### Required negative fixtures

At minimum:

- source inactive or suspended;
- rights/redistribution unresolved;
- sealed/restricted record;
- living-person private join;
- re-identification through unique parcel/name combination;
- assessor record presented as title;
- tax record presented as title;
- parcel polygon presented as legal boundary;
- current parcel ID used across incompatible vintages;
- legal-description parse with unresolved calls;
- modeled geometry presented as survey truth;
- ambiguous party identity;
- ambiguous interest;
- missing instrument citation;
- impossible date ordering;
- chain gap;
- contradictory conveyances;
- chain completeness overclaim;
- missing evidence/policy/review/release dependency;
- lifecycle skip;
- no material change;
- retry exhaustion or circuit open;
- correction and rollback scenario.

### Current workflow caution

`.github/workflows/domain-people-dna-land.yml` is confirmed as a greenfield scaffold whose jobs only echo TODO text. A successful run does **not** establish Land Ownership pipeline-spec validation, privacy/title enforcement, evidence closure, proof generation, publish dry-run fidelity, or release readiness.

### Bounded repair rule

A README update must not quietly create YAML, code, schemas, policies, tests, fixtures, sources, or workflow behavior to make its claims appear implemented. Missing enforcement remains explicit in the verification register and is addressed in separate, reviewable changes.

[Back to top](#top)

---

## Review, migration, and change discipline

### Review-impact matrix

| Change | Minimum review pressure |
|---|---|
| prose-only clarification with no contract effect | docs + pipeline-spec steward |
| add or rename a spec file | pipeline-spec, People/DNA/Land, Land Ownership, consumer, validation, docs |
| choose nested directory versus parent single-file layout | Directory Rules + pipeline-spec architecture + migration/ADR review |
| populate or modify executable stages | pipeline owner, source/rights, privacy, evidence, policy, validation, release |
| change source descriptor refs or source roles | source steward + rights + affected domain/policy reviewers |
| change temporal behavior | land-record + temporal + affected consumers |
| change party/parcel/legal-description identity | People identity + spatial/parcel + land/title reviewers |
| change chain/order/title-interest rules | land/title assertion steward + evidence + legal-risk reviewer |
| change privacy/sensitivity behavior | privacy/sensitivity + policy + release |
| change release or rollback requirements | release + policy + evidence + domain |
| move or rename lane/alias | Directory Rules preflight + ADR/migration note + rollback plan |

### Duplicate and supersession checks

Before adding a profile:

1. inspect current nested lane, parent lane, `pipeline_specs/people/`, adjacent configs, and executable consumers;
2. verify whether a single-file `land-ownership.yaml` convention is already accepted elsewhere;
3. check accepted contracts, schemas, ADRs, path registers, and drift registers;
4. identify one canonical source for generated/mirrored forms;
5. record supersession and compatibility behavior;
6. avoid parallel spec registries, source lists, schema homes, or activation mechanisms.

### Generated, mirrored, and localized files

A generated or mirrored spec must declare its canonical source and must not be edited independently. This lane currently has no verified generator or mirror contract.

### Base drift

When the base branch changes during work, compare old and new bases. If the target, parent lane, governing docs, schema, workflow, or consumer changes, re-read affected evidence before mutation. Do not overwrite concurrent work from an earlier blob.

[Back to top](#top)

---

## Correction, deactivation, and rollback

### Spec correction

A material correction should:

- create a new version rather than silently rewrite historical meaning;
- preserve prior spec, digest, approvals, and activation record;
- explain the defect and affected runs/artifacts;
- identify affected assertions, chains, catalog/triplets, releases, exports, caches, and public surfaces;
- provide re-run, re-review, correction, withdrawal, or rollback steps;
- prevent stale approval from applying to the corrected spec.

### Deactivation

A source outage, rights change, sealed/restricted-record discovery, privacy issue, incorrect living-person classification, parcel-version defect, legal-description defect, chain contradiction, evidence failure, security concern, or incorrect public output may require suspension.

Deactivation must be auditable and should not depend on deleting the file.

### Downstream impact sweep

Correction or withdrawal should inspect:

- source and raw/work/quarantine references;
- normalized candidates;
- ownership assertions and intervals;
- party/person and parcel crosswalks;
- chain candidates and reports;
- catalog items and triplets;
- EvidenceBundles and receipts;
- review and policy decisions;
- release manifests;
- public APIs, maps, exports, screenshots, stories, and AI-derived summaries;
- caches, search indexes, embeddings, and downstream mirrors where applicable.

### Rollback

Rollback may involve:

- returning scheduler/registry binding to a prior approved spec digest;
- stopping future runs;
- quarantining affected candidates;
- withdrawing or superseding releases;
- restoring prior public-safe artifacts or removing unsafe aliases;
- purging/invalidation of caches and derived outputs;
- emitting correction, withdrawal, and rollback records;
- performing the downstream sweep.

A future `rollback.yaml` would declare rollback-readiness requirements. It would not execute rollback or become release authority.

### Documentation-only rollback

This README revision can be reverted by reverting its commit. No spec, source, pipeline, data, receipt, proof, policy, workflow, or release artifact is modified by the documentation change.

[Back to top](#top)

---

## Directory map

```text
pipeline_specs/people-dna-land/land-ownership/
└── README.md    # CONFIRMED governed lane boundary; this file

# Exact candidates checked and absent:
# pipeline_specs/people-dna-land/land-ownership.yaml
# pipeline_specs/people-dna-land/land-ownership/ingest.yaml
# tests/pipeline_specs/people-dna-land/land-ownership/README.md
# tests/pipeline_specs/people-dna-land/land-ownership/test_spec_shape.py

# Prior README proposals not established by the bounded inspection:
# normalize.yaml
# validate.yaml
# catalog.yaml
# triplets.yaml
# publish.yaml
# rollback.yaml
# watchers.yaml
# land_instruments.yaml
# deed_title_instruments.yaml
# assessor_tax_records.yaml
# parcel_versions.yaml
# ownership_intervals.yaml
# legal_descriptions.yaml
# chain_of_title_candidates.yaml
```

### Placement rule

Do not create a file simply to make this tree look complete. Each new profile needs:

- verified owner and reviewers;
- accepted spec contract/schema;
- one deterministic consumer;
- active source descriptors;
- rights, privacy, sensitivity, and title-boundary posture;
- lifecycle need;
- valid and negative fixtures;
- substantive tests and receipts;
- correction, deactivation, and rollback plan;
- duplicate/supersession analysis;
- resolution of nested versus single-file placement.

### Files that do not belong here

| Material | Correct responsibility root |
|---|---|
| executable Land Ownership code | `pipelines/domains/people-dna-land/land-ownership/` or accepted shared pipeline lane |
| source clients | `connectors/<source>/` |
| source descriptors and activation | `data/registry/sources/` |
| object meaning | `contracts/` |
| machine schemas | `schemas/` |
| rights/privacy/sensitivity/title policy | `policy/` |
| fixtures and tests | `fixtures/`, `tests/` |
| raw deeds, title files, tax/assessor/parcel payloads, OCR, probate/court packets | governed `data/` lifecycle homes with access controls |
| receipt and proof instances | `data/receipts/`, `data/proofs/` |
| release decisions, corrections, withdrawal, rollback | `release/` |
| public API, UI, map, exports, AI answers | governed `apps/` and released artifact paths |
| title opinions, surveys, legal determinations | qualified external authorities; outside KFM |
| secrets | never in the repository |

[Back to top](#top)

---

## Definition of done

### This README revision

| Criterion | Status |
|---|---:|
| identifies the declarative responsibility root and executable-companion boundary | `PASS` |
| records the bounded README-only inventory without overclaiming activation | `PASS` |
| surfaces nested-directory versus parent single-file and segment-name conflicts | `PASS` |
| preserves RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED | `PASS` |
| preserves assessor/tax/title, geometry/boundary, instrument/current-title, chain/title, and private-join separation | `PASS` |
| defines minimum active-spec source, rights, time, identity, title, privacy, evidence, receipt, validation, correction, and rollback requirements | `PASS` |
| avoids changing YAML, code, schemas, policies, sources, tests, fixtures, workflows, data, receipts, proofs, or releases | `PASS` |
| verifies repository-native checks after PR creation | `PENDING UNTIL CI` |

### Future active specification

A Land Ownership spec is not done until:

- identity, version, owner, digest, lineage, and finite state validate;
- one consumer and implementation revision resolve;
- all source descriptors are active and rights/access/retention reviewed;
- source roles remain explicit;
- instrument, temporal, party, parcel/version, legal-description, interest, chain, and title-boundary behavior is explicit;
- living-person and private person-parcel controls pass policy and negative tests;
- contracts, schemas, evidence, reviews, and receipts resolve;
- no-network fixtures and substantive tests pass;
- secrets, logs, network, retention, and access controls pass;
- dry-run output is deterministic and confined to approved QA locations;
- correction, suspension, withdrawal, and rollback are exercised;
- publication remains separately governed by release authority;
- the output is clearly not a title opinion, legal advice, survey, or official determination.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| `PIPE-SPEC-PDL-LAND-001` | What is the accepted Land Ownership pipeline-spec semantic contract and machine schema? | `UNKNOWN` | Accepted contract/schema and validator evidence. |
| `PIPE-SPEC-PDL-LAND-002` | Is the canonical layout a parent `land-ownership.yaml`, nested profiles, a generated mirror, or another registry? | `CONFLICTED / NEEDS VERIFICATION` | Pipeline-spec architecture decision, root note/ADR, migration plan. |
| `PIPE-SPEC-PDL-LAND-003` | How is `people-dna-land` versus `people` resolved across spec, contract, schema, policy, data, and release lanes? | `CONFLICTED / NEEDS VERIFICATION` | Directory Rules, accepted ADRs, repo migration state. |
| `PIPE-SPEC-PDL-LAND-004` | Is there a canonical parser, registry, loader, or scheduler for `pipeline_specs/`? | `UNKNOWN` | Code, tests, runtime/config binding, operation receipt. |
| `PIPE-SPEC-PDL-LAND-005` | Which executable consumer owns a future Land Ownership spec? | `NEEDS VERIFICATION` | Consumer code, accepted path, deterministic binding. |
| `PIPE-SPEC-PDL-LAND-006` | Which land-record source descriptors are admitted and active? | `NEEDS VERIFICATION` | Registry records, activation decisions, rights/access/retention review. |
| `PIPE-SPEC-PDL-LAND-007` | What source-role vocabulary and per-source role assignments are accepted? | `NEEDS VERIFICATION` | Contract/ADR, descriptors, fixtures, tests. |
| `PIPE-SPEC-PDL-LAND-008` | Which time kinds, interval semantics, and precedence rules are canonical? | `NEEDS VERIFICATION` | Temporal contract, schemas, source rules, fixtures, tests. |
| `PIPE-SPEC-PDL-LAND-009` | What party, parcel/version, geography, legal-description, and interest identity rules are accepted? | `NEEDS VERIFICATION` | Contracts, schemas, crosswalks, validators, review procedure. |
| `PIPE-SPEC-PDL-LAND-010` | What constitutes an ownership assertion, reviewed link, interval candidate, chain gap, contradiction, and completeness disclaimer? | `NEEDS VERIFICATION` | Semantic contracts, evidence model, chain-review tests. |
| `PIPE-SPEC-PDL-LAND-011` | What living-person/private person-parcel detection and sensitivity policy is enforced? | `NEEDS VERIFICATION` | Policy bundles, reviewer rules, negative fixtures, runtime proof. |
| `PIPE-SPEC-PDL-LAND-012` | Where are Land Ownership pipeline-spec tests and fixtures, and what do they enforce? | `UNKNOWN` | Recursive inventory and executable results. |
| `PIPE-SPEC-PDL-LAND-013` | Which receipt and finite-outcome vocabularies are accepted? | `NEEDS VERIFICATION` | Contracts/schemas, emitted examples, validator tests. |
| `PIPE-SPEC-PDL-LAND-014` | Does any workflow substantively validate this sublane? | `UNKNOWN` | Workflow commands, logs, failure fixtures; current domain workflow is TODO-only. |
| `PIPE-SPEC-PDL-LAND-015` | How are activation, suspension, retirement, source withdrawal, correction, takedown, and rollback recorded? | `UNKNOWN` | Accepted governance contract and operational evidence. |
| `PIPE-SPEC-PDL-LAND-016` | What is the exhaustive direct-lane inventory at the current commit? | `NEEDS VERIFICATION` | Repository-generated recursive inventory. |
| `PIPE-SPEC-PDL-LAND-017` | Which source terms, jurisdictional restrictions, and public-record republication limits apply to each source? | `NEEDS VERIFICATION` | Current source-by-source legal/rights review. |
| `PIPE-SPEC-PDL-LAND-018` | Which outputs, if any, may reach public tier without exposing a private person-parcel relationship or making a title claim? | `NEEDS VERIFICATION` | Accepted policy, transform profiles, re-identification testing, release review. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | What it supports | What it does not prove |
|---|---:|---|---|
| target prior blob `cca2a7ac…` | `CONFIRMED` | Existing boundary, proposed profile families, title/privacy anti-collapse language. | Active spec or enforcement. |
| `pipeline_specs/people-dna-land/README.md` blob `23541333…` | `CONFIRMED DOCUMENTATION` | Parent declarative and alias-conflict boundary. | Child parser, profiles, or schedules. |
| direct lane search and exact path checks | `CONFIRMED BOUNDED RESULT` | README-only surfaced; four exact candidates absent. | Complete recursive absence. |
| executable sublane README blob `457d5fb3…` | `CONFIRMED DOCUMENTATION` | Intended executable boundary and evidence-not-title posture. | Executable behavior. |
| semantic-contract README blob `94f1e792…` | `CONFIRMED DOCUMENTATION / PROPOSED SUBDIVISION` | Meaning boundary and title/legal exclusions. | Accepted contract/schema set. |
| `LAND_OWNERSHIP.md` blob `c8d26bf1…` | `CONFIRMED DOCTRINE DOCUMENT` | Land object distinctions, source-role spine, evidence-not-title rule. | Runtime enforcement. |
| `SENSITIVITY_PROFILE.md` blob `b599188f…` | `CONFIRMED DOCTRINE DOCUMENT` | T4 deny-default for living-person/private joins and tier gates. | Accepted policy implementation. |
| `CANONICAL_PATHS.md` blob `28ed7d98…` | `CONFIRMED PATH DOCUMENT / OPEN CONFLICTS` | Domain fan-out and `people`/`people-dna-land` conflict. | ADR resolution. |
| `MISSING_OR_PLANNED_FILES.md` blob `6b25f47e…` | `CONFIRMED PLANNING DOCUMENT` | Planned inventory and explicit non-proof posture. | Current file presence. |
| `.github/workflows/domain-people-dna-land.yml` blob `2f5c3403…` | `CONFIRMED TODO SCAFFOLD` | Workflow presence and echo-only commands. | Substantive validation or proof. |

### Evidence hierarchy

Current repository files and CI/runtime evidence outrank planning documents for implementation behavior. Governing doctrine controls KFM invariants and responsibility placement. Where documents and repository state differ, this README surfaces the difference rather than smoothing it.

[Back to top](#top)

---

## Maintainer note

Keep this lane declarative, title-safe, privacy-safe, and evidence-bound.

Do not add source clients, executable processing, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, title files, private person-parcel joins, legal conclusions, public API/UI behavior, or secrets here.

Do not create speculative YAML files merely to complete the old proposed tree. Graduate one profile at a time through explicit placement, schema, consumer, source, rights, privacy, fixture, test, receipt, review, correction, and rollback gates.

<p align="right"><a href="#top">Back to top</a></p>
