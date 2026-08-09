# `release/` — Release Governance Root

> **One-line purpose.** `release/` is KFM's canonical append-only decision plane for release, promotion, correction, withdrawal, rollback, and signature records; it does not store published payloads or turn repository state into publication authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-readme
title: release/ — Release Governance Root
type: README
version: v2.1
status: draft; repository-grounded; ROOT_FULL; mixed-maturity; fixture-first release profiles; operational release held; non-publication
owner: NEEDS VERIFICATION — accepted machine governance routes release/ to @bartytime4life; no independent release steward, approver separation, or required-review enforcement was verified
created: 2026-07-03
updated: 2026-08-09
supersedes: v2.0 documentation at the same path; no release, promotion, rollback, correction, publication, signing, deployment, or data behavior is superseded
policy_label: repository-facing; release-governance; candidate-is-not-release; promotion-is-state-transition; no-payloads; cite-or-abstain; correction-aware; rollback-aware; fail-closed
owning_root: release/
root_class: canonical
responsibility: explain and index release-governance records without becoming a release decision, proof, receipt, policy, schema, data payload, runtime, or publication authority
truth_posture: cite-or-abstain; pinned files, schemas, fixtures, validators, tests, workflows, and repository trees prove bounded implementation surfaces only
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 9c080014926e6f3ba4dc630eaf7a615fff46c7fc
  base_tree: 570285e9643b3303cc23840f318810cf1d71e1e4
  prior_blob: 0752610b1df6d11143158f6f162f65ecd650e6a6
  release_tree: 210ccf37b9f90986590a3e0995a0eeda7f758042
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  makefile_blob: 4abc7f941ce25d7d14703e87e387cef6e96d1592
  release_manifest_schema_blob: c76cd9bdddb34cf33c8eb62801269553726c5923
  rollback_card_schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  release_alias_workflow_blob: 3a9739ee096f18ae5dee2074a90d125848ab1d6c
  pass12_release_gate_blob: 175871cb929663e7a19345fd18f97a81a850b628
directory_governance: ADR-0029 accepted Directory Rules v2; same-path update receives PLACE
related:
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../control_plane/root_registry.yaml
  - ../.github/CODEOWNERS
  - ../.github/workflows/release-dry-run.yml
  - ../.github/workflows/promotion-gate.yml
  - ../.github/workflows/rollback-drill.yml
  - ../.github/workflows/release-alias-verification.yml
  - ../.github/workflows/pass12-release-policy-v1.yml
  - ../contracts/release/
  - ../schemas/contracts/v1/release/
  - ../policy/release/
  - ../policy/rego/release_gate_v1.rego
  - ../tools/release/
  - ../tools/validators/release/
  - ../fixtures/release/
  - ../data/receipts/
  - ../data/proofs/
  - ../data/published/
notes:
  - "The first twelve H2 sections follow the adopted Directory Rules v2 §16.2 ROOT_FULL field order."
  - "The direct-child map is pinned to release tree 210ccf37b9f90986590a3e0995a0eeda7f758042 and describes direct children only."
  - "ReleaseManifest, RollbackCard, ReleaseAliasVerification, PromotionDecision, promotion-gate, and Pass 12 policy surfaces are bounded candidate or fixture-first implementation; none creates release authority."
  - "The three direct-child Rego files are existing placement drift because canonical policy source belongs under policy/; this README records but does not migrate them."
  - "No release, promotion, rollback execution, publication, deployment, source activation, settings change, or ADR transition is performed by this document."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#adoption-and-conformance-status)
[![Root: canonical release](https://img.shields.io/badge/root-canonical%20release%2F-0969da?style=flat-square)](#root-class-and-authority-owner)
[![Directory Rules: adopted](https://img.shields.io/badge/Directory%20Rules-v2%20adopted-2da44e?style=flat-square)](#governing-adrs-migrations-aliases-and-canonical-target)
[![Profiles: fixture first](https://img.shields.io/badge/profiles-fixture%20first-8250df?style=flat-square)](#current-maturity-and-readiness)
[![Operational release: held](https://img.shields.io/badge/operational%20release-held-b42318?style=flat-square)](#workflow-readiness-boundaries)
[![Publication: not performed](https://img.shields.io/badge/publication-not%20performed-6e7781?style=flat-square)](#public-exposure-and-sensitivity-posture)

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs and exclusions](#what-belongs-and-what-is-prohibited) · [Inputs and outputs](#inputs-outputs-and-permitted-writers) · [Exposure](#public-exposure-and-sensitivity-posture) · [Storage](#mutability-retention-generation-and-physical-storage) · [Validation](#validation) · [Review](#review-burden) · [ADRs](#adrs) · [Direct children](#current-repository-lane-map) · [Last review](#last-reviewed) · [Maturity](#current-maturity-and-readiness) · [Workflow boundaries](#workflow-readiness-boundaries) · [States](#release-state-model) · [Record contract](#release-record-minimum-contract) · [Open verification](#open-verification-register) · [Rollback](#maintenance-correction-and-rollback)

> [!IMPORTANT]
> **Release governance is not publication.** A candidate, manifest, review, decision, signature, correction notice, rollback card, workflow result, pull request, merge, GitHub release, or badge is not automatically a released public artifact. Public-safe carriers belong under [`data/published/`](../data/published/) only after the applicable evidence, policy, validation, review, release, correction, and rollback requirements are satisfied.

> [!CAUTION]
> **Green checks are bounded evidence.** Current fixture-first validators and readiness workflows prove only their declared synthetic shapes, polarity, and no-write boundaries. They do not authenticate evidence or reviewers, mutate an alias, assemble or approve a release, invalidate caches, deploy, or publish.

> [!NOTE]
> This README is a same-path documentation and navigation contract. It records current implementation surfaces, conflicts, and holds without accepting a new ADR, resolving lane duplication, moving policy files, or changing release state.

---

## Purpose

`release/` owns the repository records that govern a transition toward, away from, or between release states.

The root makes these questions inspectable:

- What candidate, manifest, or prior release is in scope?
- Which evidence, validation, policy, integrity, and review records support the proposed transition?
- Which finite decision was made, by whom, for what scope, and under which obligations?
- Which public-safe carrier is affected?
- Which correction, withdrawal, supersession, notice, signature, or changelog record carries the transition?
- Which prior state, rollback target, and invalidation plan bound reversal?

The root must not answer those questions by implication, path movement, workflow success, generated prose, a signature alone, or repository merge state.

[Back to top](#top)

---

<a id="status--authority"></a>
<a id="authority-level"></a>
<a id="placement-basis"></a>

## Root class and authority owner

Accepted [ADR-0029](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) makes [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) the writable Directory Rules authority. Its machine projection classifies `release/` as follows:

| Field | Current bounded result |
|---|---|
| Root class | `canonical` |
| Primary responsibility | Release, correction, withdrawal, rollback, promotion, and signature decisions |
| Allowed artifact kind | `release_decision` |
| Prohibited artifact kinds | `data_instance`, `generated_output`, `policy_rule` |
| Exposure | `internal` |
| Mutation | `append_only` |
| Retention | `audit_bound` |
| Validation profile | `release_decision_plane` |
| Repository owner and permitted writer | `@bartytime4life` in the current machine projection |
| Reviewer route | `@bartytime4life`; independent release stewardship remains `NEEDS VERIFICATION` |

The machine projection does not create authority by itself. It cites the accepted doctrine and records current routing. CODEOWNERS and the root registry do not authenticate a release reviewer, prove separation of duties, or approve a transition.

### Authority boundaries

| Responsibility | Canonical home | `release/` relationship |
|---|---|---|
| Public-safe released carriers | [`data/published/`](../data/published/) | Point to the carrier; do not duplicate it. |
| Process receipts | [`data/receipts/`](../data/receipts/) | Reference process memory; do not store it here. |
| Proof and evidence closure | [`data/proofs/`](../data/proofs/) | Reference proof; do not turn a decision into proof. |
| Semantic meaning | [`contracts/release/`](../contracts/release/) | Consume accepted meaning; do not redefine it in a record. |
| Machine shape | [`schemas/contracts/v1/release/`](../schemas/contracts/v1/release/) | Validate records; passing is not approval. |
| Canonical policy source | [`policy/`](../policy/) | Consume decisions or review pointers; do not host new policy source. |
| Validator and operator code | [`tools/validators/release/`](../tools/validators/release/) and [`tools/release/`](../tools/release/) | Execute bounded checks or operators outside the decision root. |
| Repository automation | [`.github/workflows/`](../.github/workflows/) | Run read-only or bounded checks; workflow presence is not release authority. |

No second release-decision root, receipt home, proof home, policy home, or published-data home is authorized by this README.

[Back to top](#top)

---

<a id="status"></a>

## Adoption and conformance status

| Surface | Current status at `main@9c080014926e` | Safe conclusion |
|---|---:|---|
| `release/` placement | **CONFIRMED / adopted** | Canonical append-only release-decision root under ADR-0029 and the root registry. |
| Root README | **CONFIRMED v2.0 baseline** | This v2.1 change updates it in place and preserves `kfm://doc/release-readme`. |
| Direct-child inventory | **CONFIRMED mixed** | Eighteen directories and three policy-shaped Rego files exist beside this README; child maturity and authority differ. |
| Candidate lane | **CONFIRMED guidance-only** | No candidate packet payload exists under `release/candidates/`. |
| `ReleaseManifest` | **CONFIRMED dual-profile / `PROPOSED_INACTIVE` strict profile** | Legacy permissive input remains accepted; a closed fixture-only profile, four valid cases, seventeen invalid cases, validator, tests, and workflow checks now exist. No references, bytes, signatures, policy, review, release, or public use are authenticated. |
| `PromotionDecision` | **CONFIRMED proposed bounded shape** | Nonempty fixtures and dedicated tests exist; a shape-valid decision is not an authenticated release decision. |
| Promotion gates | **CONFIRMED bounded fixture proof** | `make publish-check` runs review and promotion-gate fixtures/tests, including bounded A–G semantics; it does not evaluate a live candidate or emit a transition. |
| Pass 12 Rego release gate | **CONFIRMED executable / `PROPOSED_INACTIVE`** | Canonical policy source defaults deny and has native tests plus checksum-pinned OPA CI; no active repository-wide bundle or release approval is established. |
| `RollbackCard` | **CONFIRMED proposed fixture-first candidate profile** | Closed schema, bounded validator, valid/invalid fixtures, and readiness checks exist; two root JSON cards remain documentation placeholders and no rollback is executed. |
| Release alias verification | **CONFIRMED fixture-only preflight / `PROPOSED_INACTIVE`** | Deterministic checks cover declared initial bind, advance, correction, and rollback cases; no live alias is resolved or mutated. |
| Review records | **HOLD** | Parent guidance exists; accountable authenticated review records were not established from the inspected release lane. |
| Candidate assembly | **WORKFLOW_SKIPPED_EXPLICIT / HOLD** | `make release-dry-run` and `tools/release/release_dry_run.py` remain explicit placeholders. |
| Promotion execution | **WORKFLOW_SKIPPED_EXPLICIT / HOLD** | No accepted evaluator turns a reviewed candidate into release state. |
| Rollback execution | **WORKFLOW_SKIPPED_EXPLICIT / HOLD** | The apply helper remains a placeholder; no target mutation, invalidation, or rollback receipt is executed. |
| Human review enforcement | **NEEDS VERIFICATION** | CODEOWNERS, rulesets, required checks, reviewer authority, and separation of duties were not proved as a complete control. |
| Production release/runtime parity | **UNKNOWN** | No production registry, deployment, release dashboard, runtime log, recovery exercise, or public endpoint is claimed here. |

> [!IMPORTANT]
> The repository has materially more fixture-first release validation than the v2.0 README recorded. That improvement narrows shape and readiness unknowns; it does not upgrade any candidate profile to operational release machinery.

[Back to top](#top)

---

<a id="what-belongs-here"></a>
<a id="what-does-not-belong-here"></a>

## What belongs and what is prohibited

### Belongs in `release/`

- this root README and boundary READMEs for release-decision lanes;
- candidate review packets and candidate indexes;
- accountable review records and finite promotion or release decisions;
- release manifests and manifest indexes;
- correction, withdrawal, supersession, and no-action decisions;
- correction and withdrawal notices that point to governed decisions;
- rollback review records and rollback cards;
- signature and signoff packets that bind accepted records without exposing secrets;
- changelog entries tied to governed transitions;
- stable references to evidence, validation, policy decisions, reviews, receipts, proofs, source records, public-safe carriers, correction lineage, and rollback targets;
- explicit `DRAFT`, `READY_FOR_REVIEW`, `HELD`, `READY_FOR_MANIFEST`, `APPROVED`, `RELEASED`, `CORRECTED`, `SUPERSEDED`, `WITHDRAWN`, and `NO_ACTION` record states;
- documentation of unresolved lane semantics while compatibility or migration decisions remain open.

### Prohibited from `release/`

| Prohibited material | Correct responsibility or disposition |
|---|---|
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads | `data/<phase>/` |
| Bulk datasets, tiles, PMTiles, COGs, GeoParquet, exports, API payloads, or map-ready artifacts | Accepted data/delivery lanes; public-safe releases under `data/published/` |
| Receipts of record | `data/receipts/` |
| Proof objects | `data/proofs/` |
| Source descriptors and source registries | Accepted registry and source roots |
| Semantic contracts | `contracts/` |
| JSON Schemas and generated types | `schemas/` and declared generated projections |
| New canonical policy rules or policy fixtures | `policy/`, `fixtures/`, and `tests/` |
| Validator, pipeline, connector, application, package, or runtime code | `tools/`, `pipelines/`, `connectors/`, `apps/`, `packages/`, or `runtime/` by responsibility |
| Generated summaries presented as evidence, review, or approval | Governed evidence and accountable review |
| Silent promotion, correction, withdrawal, or rollback by file movement | Denied; use governed decisions and operators |
| Duplicate release, proof, receipt, catalog, source, schema, contract, policy, or published-data authority | Denied or migration-only under accepted authority |
| Secrets, private keys, signing credentials, personal data, genomic records, protected material, or harmful precise locations | Denied; use secret stores and public-safe references |

The direct-child Rego files are existing nonconforming policy-shaped surfaces. Their presence is repository evidence, not permission to add more policy source under `release/`.

[Back to top](#top)

---

<a id="inputs"></a>
<a id="outputs"></a>

## Inputs, outputs, and permitted writers

### Inputs

Release governance consumes stable references and review state, not ungoverned payload copies.

| Input family | Minimum posture | Failure behavior |
|---|---|---|
| Candidate | Stable identity, bounded scope, artifact refs, proposed target, and current candidate state | `HOLD` or `ERROR` |
| Evidence | Resolvable `EvidenceRef` / `EvidenceBundle` support where claims depend on evidence | `ABSTAIN` or `DENY` |
| Validation and integrity | Applicable schema, contract, hash, catalog, citation, boundary, and public-safety results | `HOLD`, `DENY`, or `ERROR` |
| Policy | Rights, consent, sensitivity, access, stale-state, correction, and public-surface decisions | Fail closed |
| Review | Accountable actor, subject binding, scope, outcome, reason, timing, and separation-of-duties posture | `HOLD` |
| Manifest inputs | Included records, artifact identities, prior state, release scope, correction path, and rollback target | `HOLD` |
| Correction or withdrawal support | Affected state, reason, public effect, notice requirements, replacement, and invalidation plan | `HOLD` |
| Signature support | Verified attestation references and revocation posture; never private key material | `DENY` or `ERROR` |
| Repository evidence | Pinned contracts, schemas, fixtures, validators, tests, workflows, records, and outputs tied to a known revision | `NEEDS VERIFICATION` |

### Outputs

The root may contain or route:

- candidate and review records;
- promotion and release decisions;
- release manifests;
- correction, withdrawal, supersession, and no-action decisions;
- correction and withdrawal notices;
- rollback review records and rollback cards;
- signature/signoff packets;
- release changelog records;
- explicit hold, abstain, deny, error, repair, or defer outcomes.

An output record does not create a public artifact merely because it exists or validates.

### Permitted writers

The machine root registry currently names `@bartytime4life` as repository owner, permitted writer, and reviewer. That is a repository routing fact, not a complete operational identity model. Runtime or release-writing capabilities must be authenticated and policy-bound separately.

| Writer class | Permitted durable effect |
|---|---|
| Documentation maintainer | Update README/index guidance through reviewed Git changes; no release-state mutation. |
| Release authority | Append a governed decision only after required evidence, validation, policy, and review. |
| Publisher | Write versioned public-safe carriers only after an accepted release decision; published bytes remain outside `release/`. |
| Corrector or withdrawal authority | Append correction/withdrawal records and trigger accepted invalidation behavior; never erase history. |
| Rollback operator | Execute only an accepted, authenticated, no-ambiguity rollback plan and emit receipts; no such operator is established here. |
| Watcher, AI agent, validator, or CI workflow | Propose, inspect, validate, or emit bounded process evidence; never self-approve or publish. |

[Back to top](#top)

---

## Public exposure and sensitivity posture

The root registry classifies `release/` as **internal**. Normal public clients must consume governed APIs, public catalog records, and released carriers—not repository decision files as a live authority surface.

A public-facing release summary may be derived only when its source decision permits that exposure and the summary preserves:

- stable release identity and public scope;
- evidence and citation pointers appropriate to the audience;
- rights, consent, sensitivity, and generalization posture;
- correction, withdrawal, supersession, and stale-state signals;
- public-safe reason codes without leaking protected policy or location detail;
- release version and rollback/correction links.

Release records must not contain raw secrets, private signing material, exact restricted coordinates, living-person detail, DNA/genomic content, private-land evidence, protected archaeology, rare-species precision, or infrastructure details merely to make a decision self-contained. Use stable governed references and record public-safe transformations.

Unknown rights, consent, sovereignty, sensitivity, review, or public-use scope remains a hold or denial.

[Back to top](#top)

---

## Mutability, retention, generation, and physical storage

| Concern | Root contract |
|---|---|
| Mutation | `append_only` for decision records. Corrections and supersessions append lineage; they do not rewrite prior history. |
| Retention | `audit_bound`. Retain decisions, scopes, reasons, review bindings, signatures, correction lineage, and rollback references according to accepted policy. |
| README maintenance | Versioned Git documentation may be corrected in place while preserving `doc_id`, stable anchors, changelog, and no-loss history. |
| Generation | Durable generated output is prohibited here. A generated decision candidate remains a candidate and requires accountable review. |
| Physical payload storage | Release carriers remain under the accepted `data/published/` or external governed storage location; `release/` stores decision records and pointers. |
| External storage | A manifest or decision may point to immutable external artifacts only with stable locators, digests, rights, retention, verification, and rollback behavior. |
| Signatures | Store public verification material or references, never private keys or signing credentials. |
| Cache and alias state | Live cache, CDN, alias, or pointer state belongs behind accepted operators and receipts; repository fixtures do not become live state. |

### Existing placement drift

The following direct-child policy-shaped files are `CONFIRMED` at the pinned release tree:

- `hydrology_publication.rego`
- `public_safe_geometry.rego`
- `source_role_anti_collapse.rego`

Directory Rules and the root registry prohibit `policy_rule` under `release/`; canonical policy source belongs under [`policy/`](../policy/). This README does not edit, move, delete, mirror, or canonize those files. A migration requires object classification, producer/consumer inventory, accepted authority, reference repair, validation, and rollback.

[Back to top](#top)

---

<a id="validation"></a>

## Validation and negative checks

Validation must distinguish source correctness, candidate shape, readiness inspection, policy execution, authenticated review, state mutation, and publication.

### Repository commands and workflows

| Surface | What it proves now | What it does not prove |
|---|---|---|
| `make validate` | Runs configured aggregate schema validators and schema/contract tests. | Complete release assembly, authenticated review, policy execution, state transition, rollback, or publication. |
| `make release-dry-run` | Prints the explicit candidate-assembly TODO marker. | Candidate assembly or dry-run execution. |
| `make publish-check` | Runs bounded review-record and promotion-gate validators/tests with no network. | A live candidate, external evidence resolution, actor authentication, policy decision, release state, or publication. |
| `release-dry-run` workflow | Confirms candidate-lane hold, dual-profile `ReleaseManifest`, fixture counts, bounded promotion-gate checks, and rollback-card readiness. | Candidate or manifest creation, release decision, rollback execution, or publication. |
| `promotion-gate` workflow | Exercises bounded fixture semantics and keeps missing operational prerequisites fail-closed. | Authenticated evidence, reviewers, signatures, live policy, or a release transition. |
| `rollback-drill` workflow | Inspects rollback candidates/placeholders and no-write readiness boundaries. | Alias/cache mutation, restoration, invalidation, rollback receipt, or recovery proof. |
| `release-alias-verification` workflow | Runs fixture-only alias-transition validation and validates its generated receipt. | Live alias lookup/mutation, cache invalidation, deployment, release issue, or publication. |
| `pass12-release-policy-v1` workflow | Executes checksum-pinned OPA against one bounded `PROPOSED_INACTIVE` Rego profile and native tests. | Active bundle selection, `PolicyDecision` normalization, reviewer authentication, release approval, or publication. |
| `validate_release_manifest.py --fixtures` | Proves closed fixture shape, deterministic identity/hash rules, reference-array canonicalization, and named negative cases. | Reference resolution, artifact-byte verification, policy, review, signatures, release, or public use. |
| `validate_rollback_card.py --fixtures` | Proves rollback-candidate shape and local consistency for synthetic cases. | Target existence, authority, execution, invalidation, restoration, or publication. |
| `validate_release_alias_verification.py --fixtures` | Proves declared transition consistency for synthetic alias cases. | Live pointer state or mutation. |

### Required README checks

- exactly one H1;
- the first twelve H2s match adopted Directory Rules v2 §16.2 in order;
- `kfm://doc/release-readme` and legacy anchors remain stable;
- metadata and fenced blocks are balanced;
- custom anchors are unique and internal fragments resolve;
- the direct-child map matches pinned release tree `210ccf37...`;
- repository-relative links resolve at the pinned base;
- no invented owner, approval, release, runtime, deployment, rights, or test claim;
- no credential, private material, living-person record, DNA/genomic content, or harmful precise location;
- the generated receipt binds the exact README SHA-256;
- the remote branch bytes and changed-path set match the reviewed packet.

### Negative checks

A review must fail or hold when:

- a policy rule, receipt, proof, payload, or generated artifact is added under `release/`;
- a record implies approval without authenticated review and a finite decision;
- a public scope lacks evidence, policy, rights, sensitivity, correction, or rollback support;
- a candidate uses floating `latest` references or role-collapsed pointers;
- a correction overwrites prior history;
- a rollback target is missing, circular, mutable without a digest, or broader than the approved scope;
- a workflow writes release state or receives secrets from untrusted pull-request code;
- a map, tile, AI answer, commit, PR, merge, signature, or workflow result is presented as sovereign release proof.

[Back to top](#top)

---

<a id="review-burden"></a>

## Owner, reviewers, and escalation path

| Role or question | Current posture |
|---|---|
| Repository owner / default route | `@bartytime4life` through current machine projection and CODEOWNERS. |
| Release steward | `NEEDS VERIFICATION`; no independent named steward was established. |
| Policy and sensitivity reviewer | Required when rights, consent, sensitivity, public precision, or restricted material is affected; assignment remains evidence-dependent. |
| Domain reviewer | Required when domain semantics, source role, interpretation, or public safety is material. |
| Security/signing reviewer | Required for key management, attestations, supply chain, alias mutation, cache invalidation, or recovery operations. |
| Independent approval | `NEEDS VERIFICATION`; owner routing alone does not prove separation of duties. |
| Escalation | Hold the transition and open a bounded review/decision item when authority, evidence, policy, lane ownership, or rollback is unresolved. |

Review depth is proportional to consequence:

- documentation-only changes still require accuracy, identity, link, no-loss, and claim-boundary review;
- new or changed record shapes require contract, schema, fixture, validator, compatibility, and migration review;
- state-changing decisions require evidence, policy, authenticated review, correction, rollback, and public-effect review;
- sensitive or high-consequence release requires qualified domain/policy review and separation of duties appropriate to risk.

A workflow PASS, CODEOWNER route, signature packet, or mergeability result is never independent approval by itself.

[Back to top](#top)

---

<a id="related-folders"></a>
<a id="adrs"></a>

## Governing ADRs, migrations, aliases, and canonical target

### Governing decisions

| Decision or conflict | Status | Consequence |
|---|---|---|
| [ADR-0029 — Adopt Directory Governance Standard v2](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | `accepted` | `release/` is the canonical release-decision root; the adopted doctrine and machine projection govern placement. |
| [ADR-0011 — Receipts vs Proofs vs Manifests vs Catalog Separation](../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | `proposed` | It is design evidence, not migration or release authority. |
| Manifest naming and migration | adopted name / migration unresolved | Directory Rules name `manifests/` canonical and `manifest/` a compatibility or migration source; preserve both until producers, consumers, identities, and rollback are verified. |
| Correction naming and object classification | partly decided | Directory Rules name `correction_notices/` canonical for public correction objects; `correction/` and `corrections/` require object-family classification before migration. |
| Rollback decision and execution placement | partly decided | Directory Rules name `rollback_cards/` canonical for decisions and `data/receipts/rollback/` for execution receipts; the generic `rollback/` lane still requires classification. |
| Review/decision/promotion-decision semantics | unresolved | Do not collapse lanes from README prose. |
| Direct-child Rego placement | confirmed drift | No new writes; migrate only through accepted classification and rollback discipline. |
| Live release alias | fixture-only preflight exists; operational target unresolved | Do not represent synthetic verification as current alias state. |

### Canonical target and aliases

`release/` is already canonical. It has no replacement target or authorized root alias. Adopted naming identifies preferred child homes, but current compatibility lanes remain present and no child alias, move, or retirement is declared by this README.

### Migration boundary

No lane, record, policy file, manifest, correction, rollback card, or alias is moved or deleted by this change. A future migration must:

1. freeze governing doctrine, object family, producers, consumers, identifiers, and digests;
2. accept the authority decision before structural implementation;
3. preserve single-write authority;
4. record old-to-new mappings and compatibility mode;
5. repair links/imports and validate fixtures, workflows, records, and rollback;
6. prove zero writers and zero consumers before retirement.

[Back to top](#top)

---

<a id="repo-fit"></a>
<a id="current-lane-index"></a>
<a id="current-repository-lane-map"></a>

## Direct-child directory map

Verified against release tree `210ccf37b9f90986590a3e0995a0eeda7f758042` at `main@9c080014926e`.

```text
release/
├── README.md                    # This ROOT_FULL documentation contract
├── agriculture/                 # Agriculture release-governance router
├── candidates/                  # Candidate review packets; current payload hold
├── changelog/                   # Human-readable transition history
├── correction/                  # Existing correction lane; object classification required
├── correction_notices/          # Canonical public correction objects under v2 naming
├── corrections/                 # Existing plural/domain lane; classification required
├── decisions/                   # Release decision records
├── hydrology_publication.rego   # Existing policy-shaped placement drift
├── manifest/                    # Noncanonical compatibility or migration source
├── manifests/                   # Canonical manifest collection under v2 naming
├── people-dna-land/             # Sensitive-domain release-review material
├── policy/                      # Release-facing policy review pointers, not canonical policy
├── promotion_decisions/         # Promotion-decision records
├── public_safe_geometry.rego    # Existing policy-shaped placement drift
├── reviews/                     # Accountable release-review records
├── rollback/                    # Existing generic lane; object classification required
├── rollback_cards/              # Canonical rollback-decision cards under v2 naming
├── signatures/                  # Signature and signoff packets
├── source_role_anti_collapse/   # Release-facing source-role review material
├── source_role_anti_collapse.rego # Existing policy-shaped placement drift
└── withdrawal_notices/          # Withdrawal communication records
```

The map is descriptive and direct-child-only. It does not claim equal maturity, authorize a child, or resolve overlap.

### Related responsibility roots

| Responsibility | Canonical or current home |
|---|---|
| Published public-safe payloads | [`data/published/`](../data/published/) |
| Receipts | [`data/receipts/`](../data/receipts/) |
| Proofs | [`data/proofs/`](../data/proofs/) |
| Release contracts | [`contracts/release/`](../contracts/release/) |
| Release schemas | [`schemas/contracts/v1/release/`](../schemas/contracts/v1/release/) |
| Canonical policy | [`policy/`](../policy/) and release policy lane [`policy/release/`](../policy/release/) |
| Release validators | [`tools/validators/release/`](../tools/validators/release/) |
| Release operators | [`tools/release/`](../tools/release/) |
| Release fixtures | [`fixtures/release/`](../fixtures/release/) |
| Release tests | [`tests/release/`](../tests/release/) and validator tests under [`tests/validators/`](../tests/validators/) |
| Governance projection | [`control_plane/root_registry.yaml`](../control_plane/root_registry.yaml) |
| Platform workflows | [`.github/workflows/`](../.github/workflows/) |

[Back to top](#top)

---

<a id="last-reviewed"></a>

## Last evidence review and review trigger

| Field | Value |
|---|---|
| Last evidence review | 2026-08-09 |
| Base | `main@9c080014926e6f3ba4dc630eaf7a615fff46c7fc` |
| Prior README blob | `0752610b1df6d11143158f6f162f65ecd650e6a6` |
| Release tree | `210ccf37b9f90986590a3e0995a0eeda7f758042` |
| Adopted Directory Rules blob | `fd49a0b83e55cef52c1124281f093e263526898d` |
| Root registry blob | `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` |
| Review result | Same-path ROOT_FULL modernization; stale readiness claims corrected; release behavior unchanged. |
| Review trigger | Authority, root class, writer, exposure, sensitivity, storage, direct-child inventory, accepted ADR, validator/workflow semantics, candidate/review/manifest/decision/alias/rollback implementation, drift, correction, withdrawal, rollback, or production release evidence changes. |
| Maximum interval | No accepted root-specific interval was found; apply event- and risk-based review under Directory Rules §16.5. |

[Back to top](#top)

---

<a id="current-maturity"></a>

## Current maturity and readiness

KFM release support is **mixed**. The repository now has real fixture-first contracts, schemas, validators, negative cases, tests, and workflows. The operational transition remains held.

| Layer | Current evidence | Bounded interpretation |
|---|---|---|
| Placement and root contract | Accepted doctrine plus active machine projection | `release/` is canonical; this does not approve any record. |
| Candidate shapes | ReleaseManifest, PromotionDecision, RollbackCard, ReleaseAliasVerification | Useful deterministic candidate profiles; most are proposed/inactive and non-authoritative. |
| Negative testing | Nonempty invalid fixtures and named findings/reasons | Fail-closed behavior is testable for declared fixture scope. |
| Policy | One executable Pass 12 Rego profile, default deny | Profile is inactive and not an accepted general release evaluator. |
| Review | Review-record fixture validators and A–G bounded checks | Synthetic closure, not authenticated review. |
| Candidate assembly | Explicit TODO helper and Make target | Not implemented. |
| Manifest resolution | Fixture-only candidate validation | Does not resolve refs or verify artifact bytes. |
| Alias behavior | Fixture-only transition verification | No live alias state or mutation. |
| Rollback | Candidate schema/validator and readiness inspection | No operator, invalidation, restoration, or receipt flow. |
| Production release | No current evidence in this review | `UNKNOWN`; do not infer from GitHub state. |

A useful next implementation must close one dependency-bounded operational path without allowing a validator, policy fixture, workflow, or AI-generated record to approve itself.

[Back to top](#top)

---

<a id="lifecycle-boundary"></a>
<a id="root-responsibilities"></a>

## Lifecycle and authority boundary

```text
candidate / review inputs
  -> evidence + validation + policy + accountable review
  -> decision + manifest + correction/withdrawal/rollback support
  -> governed release state
  -> public-safe carrier under data/published/
```

The canonical lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

`release/` governs the decision crossing; it does not own the lifecycle payload.

| Responsibility | Required boundary |
|---|---|
| Identity | Stable IDs, versions, digests, and subject pointers; filenames alone are insufficient. |
| Evidence | Resolve evidence where claims depend on it; otherwise abstain or hold. |
| Validation | Bind applicable shape, semantic, integrity, catalog, citation, and safety results. |
| Policy | Record rights, consent, sensitivity, access, stale-state, and public-use posture. |
| Review | Authenticate the subject, actor, authority, scope, outcome, reason, and timing. |
| Decision | Use finite outcomes and reason codes; no approval by implication. |
| Manifest | Bind included records, prior state, public scope, correction path, and rollback target. |
| Correction | Preserve forward correction, supersession, withdrawal, and public notice. |
| Rollback | Name a valid prior target and invalidation consequences before state change. |
| Publication | Keep released bytes in the published-data plane and preserve lineage. |

[Back to top](#top)

---

## Workflow readiness boundaries

### `release-dry-run`

Current bounded behavior:

- confirms that `release/candidates/` contains no candidate packet payload;
- confirms `tools/release/release_dry_run.py` and `make release-dry-run` remain placeholders;
- verifies the dual-profile ReleaseManifest metadata, four valid fixture groups, and seventeen invalid groups;
- runs bounded promotion-gate checks;
- validates RollbackCard fixture readiness.

It emits summaries only. It creates no candidate, manifest, decision, receipt, proof, rollback card, release, or publication authority.

### `promotion-gate` and `make publish-check`

Current bounded behavior exercises fixture-only review and promotion-gate semantics, including A–G closure checks. PASS means the synthetic input met the declared bounded profile.

It does not authenticate EvidenceRefs, reviewers, assignments, signatures, or external state; evaluate an accepted live release policy; bind another workflow result as proof; or emit a release transition.

### `release-alias-verification`

Current bounded behavior validates synthetic `INITIAL_BIND`, `ADVANCE`, `CORRECTION`, and `ROLLBACK` declarations and deterministic identities. The workflow has read-only contents permission and states its non-effects.

It does not look up or mutate a production alias, switch a current pointer, invalidate caches, deploy, open a release issue, or publish.

### `pass12-release-policy-v1`

Current bounded behavior executes checksum-pinned OPA 1.19.0 against one default-deny `PROPOSED_INACTIVE` policy profile and its native tests/fixtures. Reasons remain explicit.

It does not activate a policy bundle, resolve evidence, verify attestations, authenticate review, normalize an authoritative `PolicyDecision`, promote, release, deploy, or publish.

### `rollback-drill`

Current bounded behavior inspects proposed RollbackCard shape, fixtures, root placeholder cards, helper placeholders, and published-alias readiness.

It does not select a live target, verify current public state, mutate aliases, invalidate API/CDN/tile/catalog/search/AI caches, restore bytes, issue notices, or emit rollback receipts.

> [!IMPORTANT]
> These workflows are valuable because they make incomplete machinery testable and visible. Describing them as operational release, promotion, alias management, or rollback would be a documentation defect.

[Back to top](#top)

---

## Release state model

Record state and public artifact state remain distinct.

| State | Meaning |
|---|---|
| `DRAFT` | Record exists but is incomplete or not ready for accountable review. |
| `READY_FOR_REVIEW` | Required inputs appear complete enough for review; no approval implied. |
| `HELD` | Evidence, validation, policy, rights, sensitivity, review, correction, or rollback support is unresolved. |
| `READY_FOR_MANIFEST` | A reviewed candidate may support manifest preparation; it is not released. |
| `APPROVED` | A governed decision approves the named scope; publication still depends on the complete release path. |
| `RELEASED` | Governed release state is complete for the named target and public scope. |
| `CORRECTED` | A governed correction changes or replaces prior release state while preserving lineage. |
| `SUPERSEDED` | A newer governed state replaces the prior state. |
| `WITHDRAWN` | The release-facing state is withdrawn through governed process. |
| `NO_ACTION` | Review authorizes no release-state change. |

Lane-specific decision outcomes such as `APPROVE`, `DENY`, `ABSTAIN`, `PROMOTE_TO_MANIFEST`, `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, and `NO_ACTION` must not be silently collapsed without an accepted contract.

[Back to top](#top)

---

<a id="required-release-root-record-fields"></a>

## Release record minimum contract

A state-bearing record should include the fields appropriate to its accepted lane and, at minimum:

- stable record ID;
- object type and contract/schema version;
- record status, finite outcome, and stable reason codes;
- subject or affected-record pointer;
- domain, layer, artifact, geography, time, audience, and public-scope boundaries as applicable;
- candidate, manifest, decision, release, correction, withdrawal, notice, changelog, signature, or carrier pointer;
- evidence pointer where claims depend on evidence;
- validation, integrity, and catalog-closure pointers where applicable;
- policy review/decision pointer where applicable;
- authenticated reviewer/decider identity, authority, scope, and review state;
- manifest pointer when a release target is prepared or changed;
- correction, withdrawal, supersession, and notice pointers when applicable;
- rollback target plus cache/alias/invalidation posture when public state may change;
- release-facing effect;
- recorded time and actor;
- unresolved holds and follow-up.

A missing dependency produces `HELD`, `ABSTAIN`, `DENY`, or `ERROR`; it must not be represented as completion.

[Back to top](#top)

---

## Minimal release-root record

```markdown
# <stable-release-record-id>

## Record type
CANDIDATE / REVIEW / PROMOTION_DECISION / MANIFEST / DECISION /
CORRECTION / CORRECTION_NOTICE / WITHDRAWAL / WITHDRAWAL_NOTICE /
ROLLBACK_REVIEW / ROLLBACK_CARD / SIGNATURE_PACKET / CHANGELOG / NO_ACTION

## Status and outcome
- Status: DRAFT / READY_FOR_REVIEW / HELD / READY_FOR_MANIFEST /
  APPROVED / RELEASED / CORRECTED / SUPERSEDED / WITHDRAWN / NO_ACTION
- Outcome: <finite lane-specific outcome>
- Reason codes: <stable reason codes>

## Scope
<domain, object, artifact family, geography, time, audience, target, and public scope>

## Subject
<candidate, manifest, decision, release, correction, notice, signature, or carrier pointer>

## Governed support
- Evidence: <EvidenceRef/EvidenceBundle pointer or N/A with reason>
- Validation/integrity: <pointer or N/A with reason>
- Policy: <PolicyDecision/review pointer or N/A with reason>
- Review: <authenticated review record and reviewer>
- Manifest: <pointer or N/A>
- Correction/withdrawal/supersession: <pointer or N/A>
- Rollback target: <stable prior target or N/A with reason>
- Alias/cache/invalidation: <plan or N/A>
- Changelog/notice: <pointer or N/A>

## Release-facing effect
<none / held / ready for manifest / released / corrected / withdrawn / superseded>

## Date and actor
- Recorded at: <ISO-8601>
- Recorded by: <verified actor identity>

## Follow-up
<open items or none>
```

This is guidance. Accepted semantic contracts and machine schemas outrank it.

[Back to top](#top)

---

## Review checklist

Before treating a release-facing transition as complete:

- [ ] The record is in the correct release lane.
- [ ] Stable identity, subject, scope, audience, and time are explicit.
- [ ] Evidence resolves where claims depend on it.
- [ ] Validation, integrity, and catalog support are linked.
- [ ] Rights, consent, sensitivity, access, stale-state, and public-safety posture are resolved.
- [ ] Accountable review and decision authority are authenticated.
- [ ] The outcome is finite and carries reason codes.
- [ ] The manifest binds included records, prior state, and public effect.
- [ ] Correction, withdrawal, supersession, notice, signature, and changelog pointers are present when applicable.
- [ ] A valid rollback target and alias/cache/invalidation plan exist when public state may change.
- [ ] No payload, receipt, proof, source, schema, contract, policy, validator, or application authority is duplicated under `release/`.
- [ ] No generated text, map, tile, AI response, workflow result, pull request, merge, GitHub release, or signature is used as approval by itself.
- [ ] Sensitive or restricted material is not exposed.
- [ ] The reviewed diff is bounded and a revert or forward-correction path is documented.
- [ ] Hosted checks are classified by what they actually proved.

[Back to top](#top)

---

## Naming guidance

Prefer stable object IDs and readable filenames. A useful human-facing pattern is:

```text
<YYYY-MM-DD>_<scope>_<record-type>.md
```

Examples:

```text
2026-08-09_hydrology-watershed_release-review.md
2026-08-09_fauna-public-range_correction-notice.md
2026-08-09_agriculture-county-panel_rollback-card.md
```

Rules:

- use lowercase filenames and hyphenated human-readable scope;
- keep stable IDs inside records so identity does not depend on path;
- preserve approved record names unless a migration records lineage;
- do not create a new lane merely to obtain preferred naming;
- preserve current singular/plural paths until an accepted decision resolves them;
- never use `latest`, `final`, or mutable aliases as the only identity for a state-bearing record.

[Back to top](#top)

---

## Evidence and no-loss ledger

| Baseline surface | v2.1 disposition |
|---|---|
| `kfm://doc/release-readme`, path, H1, and one-line purpose | Preserved. |
| Release-vs-published distinction | Preserved and aligned with the active root registry. |
| Root authority and placement basis | Updated to accepted ADR-0029 and Directory Rules v2. |
| First twelve root-contract sections | Replaced with the exact v2 `ROOT_FULL` field order; legacy fragment anchors preserved. |
| Status and workflow maturity | Corrected for fixture-first ReleaseManifest, RollbackCard, promotion-gate, alias, and Pass 12 policy work added after v2.0. |
| Belongs/prohibited, inputs/outputs, and review burden | Preserved and consolidated under v2 fields. |
| Related roots and lane index | Preserved and expanded to the complete direct-child tree, including source-role and Rego drift surfaces. |
| Lifecycle invariant and release state model | Preserved. |
| Required fields, minimal record, checklist, and naming guidance | Preserved and strengthened. |
| Manifest/correction/rollback naming conflicts | Preserved as unresolved; no migration selected. |
| Open verification | Refreshed below. |
| Last reviewed | Repinned to current main and event-based review triggers. |
| Documentation-vs-operational rollback boundary | Preserved. |
| Release behavior | Unchanged; no release or publication claim added. |

[Back to top](#top)

---

<a id="open-verification"></a>

## Open verification register

1. **Stewardship and enforcement:** accepted release, policy, security/signing, correction, rollback, and domain stewards; branch rules; required checks; independent review.
2. **Candidate assembly:** deterministic no-write command, stable candidate identity, source inputs, and complete negative tests.
3. **Manifest profiles:** retirement or bounded support of the permissive legacy branch; reference resolution; artifact-byte and signature verification.
4. **Manifest migration:** producer/consumer inventory and safe cutover from compatibility `manifest/` to canonical `manifests/`.
5. **Correction classification:** classify objects under `correction/` and `corrections/` before convergence on canonical public `correction_notices/` where applicable.
6. **Rollback classification:** separate decisions under `rollback_cards/`, execution receipts under `data/receipts/rollback/`, and classify the existing generic `rollback/` lane.
7. **Decision lanes:** accepted relationship among `reviews/`, `decisions/`, and `promotion_decisions/`.
8. **Policy drift:** classification and migration of direct-child Rego files without creating dual-write authority.
9. **Review authentication:** real review records, subject binding, actor authority, obligations, self-review denial, and separation of duties.
10. **Policy activation:** accepted bundle selector, evaluator, input contract, normalized outcomes, decision receipts, and consumer binding.
11. **Evidence closure:** operational `EvidenceRef -> EvidenceBundle` resolution and stale/corrected/revoked history handling.
12. **Promotion execution:** policy-aware evaluation that cannot self-approve, publish, or infer approval from CI.
13. **Alias state:** accepted live alias/pointer mechanism, storage, concurrency, authentication, mutation receipt, and recovery behavior.
14. **Rollback execution:** target verification, signature/review checks, no-write simulation, invalidation, restoration, notices, and receipts.
15. **Signatures:** signing profile, key management, verification, revocation, and offline behavior.
16. **Corrections and withdrawal:** API, catalog, map, tile, search, AI, cache, citation, and downstream invalidation behavior.
17. **Release reason vocabulary:** accepted mapping among lane-specific outcomes without semantic collapse.
18. **Production parity:** registry, deployment, logs, dashboards, retention, recovery, and incident evidence.
19. **Compatibility roots:** `artifacts/release/` and other trust-shaped drift remain outside this README's migration scope.
20. **Human adoption:** review and acceptance of this README update and generated receipt.

[Back to top](#top)

---

## Maintenance, correction, and rollback

### Documentation correction

When this README becomes stale or wrong:

1. pin the current repository revision and read the complete file;
2. inspect adopted Directory Rules, root registry, accepted ADRs, direct-child tree, relevant contracts/schemas/validators/tests/workflows, and open overlap;
3. identify the exact claim, lane, workflow, or link that drifted;
4. update the smallest dependency-closed section while preserving identity and anchors;
5. validate the full Markdown and connected release-document neighborhood;
6. update provenance;
7. deliver through a focused review branch.

### Before merge

Close or abandon the draft pull request and branch. No release state changes, so no operational rollback is needed. Remote branch deletion requires separate authority.

### After merge

Use a transparent revert or corrective documentation/provenance pull request against the actual merged commit. Never rewrite shared history.

### Operational correction

A documentation revert is not a release rollback. Operational correction, withdrawal, supersession, alias change, cache invalidation, and rollback require accepted records and operators in their governed lanes, with receipts and public-effect handling appropriate to consequence.

[Back to top](#top)

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 2026-07-03 | Expanded the compact root stub into release-governance guidance. |
| v2.0 | 2026-07-23 | Reordered the root contract to the then-current README profile; exposed workflow holds, lane conflicts, CODEOWNERS limits, no-loss, and documentation-vs-release rollback boundaries. |
| v2.1 | 2026-08-09 | Adopted the Directory Rules v2 `ROOT_FULL` field order; repinned current main and direct children; corrected stale ReleaseManifest, RollbackCard, promotion-gate, alias, and Pass 12 policy claims; recorded Rego placement drift; preserved all release/publication holds. |

[Back to top](#top)
