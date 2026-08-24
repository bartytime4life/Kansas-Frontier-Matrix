<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/fauna/readme
title: Fauna Runbooks — Operational Procedure and Sensitive-Domain Boundary
type: readme
subtype: domain-runbook-boundary
version: v0.1
status: draft; repository-grounded; documentation-only; sensitive-domain; non-authoritative; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
  - "NEEDS VERIFICATION — accountable Fauna, taxonomy, source, rights, sensitivity/geoprivacy, evidence, policy, review, release, correction, rollback, operations, and independent-review authorities"
created: 2026-08-24
updated: 2026-08-24
policy_label: public-review; fauna; sensitive-location; rights-aware; fail-closed; no-publication-authority
current_path: docs/runbooks/fauna/README.md
owning_root: docs/
responsibility: >-
  Define the human-facing boundary, navigation, inheritance, current maturity,
  sensitive-domain safety posture, maintenance contract, and non-effects for
  Fauna operational procedures without granting source, taxonomy, evidence,
  policy, review, lifecycle, release, deployment, promotion, rollback-execution,
  or publication authority.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational-documentation index
canonical_relationship: same-path completion of an existing tracked one-byte file; local boundary for docs/runbooks/fauna; no sibling authority created
path_posture: PLACE
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
repository: bartytime4life/Kansas-Frontier-Matrix
stack_base_commit: af9bd74360bb00b04967516a27ee87e43a064406
main_checkpoint_before_stack: df6c3f5dadd2800fdc2356ceb540ca4e448f6c7a
target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
parent_runbooks_readme_note: >-
  The parent docs/runbooks/README.md carries an older inventory snapshot and
  should be refreshed only after this stacked Fauna boundary settles; this PR
  does not guess repository-wide counts.
stack_dependency:
  pull_request: 3509
  purpose: repository-ground the sensitive-occurrence review scaffold before this local index describes it as substantive
child_evidence:
  ebd_derivative_release_blob: fd4ce723309b3819e3c4e96dacf3b839619aca83
  no_network_test_blob: 4a8772dd1356521b11d4a568ae127acde2b2cc5e
  promotion_blob: e3c4ce643d77d887a8b74cc34f688c2d08613f5b
  publication_gate_dry_run_blob: 3a65acdf9d399c7fac0271657a9ce706350f555c
  rollback_drill_blob: 78a0c3663ef30e5edb9260c0c5ab58d6e7f860fb
  rollback_runbook_blob: d8d7d3bb9c40d3de50d484e6d13640bee5baaa58
  sensitive_occurrence_review_stack_blob: e783cb4f643b250a456162699fb9768aa8364241
  source_refresh_blob: e39e503c3470819f8364e8488cfa51b72b3859a7
  taxonomy_resolution_blob: b032de20b95b8f831993d933829741d5b8012d49
drive_lineage:
  file: KFM_Fauna_Architecture_PDF_Only_Report.pdf
  drive_id: 1mWhhtubyaAtNuWJ3vY7nuDLx50Wig7Bj
  date: 2026-04-21
related:
  - ../README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/fauna/README.md
  - ../../domains/fauna/ARCHITECTURE.md
  - ../../domains/fauna/SOURCES.md
  - ../../domains/fauna/SOURCE_REGISTRY.md
  - ../../domains/fauna/SENSITIVITY.md
  - ../../domains/fauna/POLICY.md
  - ../../domains/fauna/RELEASE_INDEX.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ./TAXONOMY_RESOLUTION_RUNBOOK.md
  - ./SENSITIVE_OCCURRENCE_REVIEW.md
  - ./EBD_DERIVATIVE_RELEASE.md
  - ./PROMOTION_RUNBOOK.md
  - ./PUBLICATION_GATE_DRY_RUN.md
  - ./ROLLBACK_RUNBOOK.md
  - ./ROLLBACK_DRILL.md
  - ../../../contracts/domains/fauna/README.md
  - ../../../schemas/contracts/v1/domains/fauna/README.md
  - ../../../fixtures/domains/fauna/README.md
  - ../../../tools/validators/domains/fauna/README.md
  - ../../../policy/domains/fauna/README.md
  - ../../../policy/sensitivity/fauna/README.md
  - ../../../data/registry/sources/fauna/README.md
  - ../../../data/proofs/fauna/README.md
  - ../../../release/candidates/fauna/README.md
  - ../../../.github/workflows/domain-fauna.yml
notes:
  - "The prior target contained only a newline. This edition supplies the missing local boundary without moving or renaming any child procedure."
  - "The current lane contains substantial fixture-first validation, source-refresh preparation, taxonomy handoff, sensitive-occurrence review, EBD rights review, promotion-readiness, publication-denial rehearsal, and rollback-drill documentation."
  - "The legacy ROLLBACK_RUNBOOK.md remains proposal-era and is explicitly classified as stale/needs modernization rather than silently treated as operationally grounded."
  - "Live Fauna sources, production sensitivity policy, accountable stewardship, proof/release closure, operational rollback, deployment, and publication remain held or unverified."
  - "No exact or reconstructable sensitive wildlife location, geoprivacy parameter, credential, source payload, private-land detail, or observer-linked record is included."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Runbooks — Operational Procedure and Sensitive-Domain Boundary

> **Start here for Fauna fixture-only validation, source-refresh preparation, taxonomy-resolution handoff, sensitive-occurrence review, rights-sensitive derivative review, promotion-readiness assessment, publication-denial rehearsal, and rollback preparation.** This directory explains how an authorized actor should proceed; it does not create source, taxonomy, evidence, policy, review, release, rollback, or publication authority.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-state)
[![Sensitive domain: fail closed](https://img.shields.io/badge/sensitive%20domain-fail%20closed-b42318?style=flat-square)](#fauna-specific-safety-rules)
[![Live source operation: HOLD](https://img.shields.io/badge/live%20source%20operation-HOLD-d4a72c?style=flat-square)](#current-repository-state)
[![Publication: HOLD](https://img.shields.io/badge/publication-HOLD-d4a72c?style=flat-square)](#current-repository-state)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-negative-authority)

> [!IMPORTANT]
> **Runbooks are instruction and review-handoff surfaces, not authority surfaces.** A runbook may cite a `SourceDescriptor`, `Taxon`, `OccurrenceEvidence`, `EvidenceRef`, `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, `PromotionDecision`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, or `RollbackCard`. It cannot create, approve, replace, or execute those objects by prose alone.

> [!WARNING]
> **Never put protected Fauna detail in public operational artifacts.** Exact or reverse-engineerable occurrences, nests, dens, roosts, hibernacula, breeding/spawning locations, telemetry, private-land joins, observer identity, steward-controlled identifiers, credentials, source-restricted payloads, and geoprivacy parameters do not belong in public runbooks, issues, pull requests, logs, screenshots, workflow summaries, exports, or generated text.

> [!CAUTION]
> **Repository-grounded does not mean operationally admitted.** Several child procedures now accurately describe current fixtures, validators, workflows, and held lanes, but live source admission, production sensitivity policy, accountable reviewer authority, candidate-specific proof/release closure, operational rollback, deployment, and publication remain `HOLD`, `UNKNOWN`, or `NEEDS VERIFICATION`.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-negative-authority) · [Placement](#placement-and-canonical-relationship) · [State](#current-repository-state) · [Children](#direct-child-map) · [Start here](#start-here) · [Lifecycle](#lifecycle-and-state-separation) · [Inputs/outputs](#inputs-outputs-and-permitted-actors) · [Safety](#fauna-specific-safety-rules) · [Outcomes](#finite-outcomes-and-stop-conditions) · [Validation](#validation-and-rehearsal-boundary) · [Maintenance](#maintenance-review-and-correction-triggers) · [Open work](#open-verification-backlog) · [Related](#related-responsibility-roots) · [Evidence](#evidence-basis) · [Rollback](#document-change-rollback)

---

## Purpose

`docs/runbooks/fauna/` is the Fauna domain lane inside KFM's human-readable operational-procedure root. It helps maintainers, reviewers, stewards, developers, and operators answer bounded questions such as:

- Which Fauna procedure applies to a fixture check, source refresh, taxonomy ambiguity, sensitive occurrence, derivative release review, promotion candidate, publication rehearsal, correction, withdrawal, or rollback state?
- What is actually executable at the pinned repository revision and what remains proposal-only?
- Which source, taxonomy, evidence, rights, sensitivity, policy, review, release, correction, and rollback prerequisites must close before an action can continue?
- Which information must stay restricted even when a schema, validator, or workflow passes?
- Which finite state means continue, quarantine/hold, abstain, deny, error, or escalate?
- Which owning responsibility root must receive the next action?

Executable behavior and trust-bearing objects remain in their owning roots. This directory should make the safe path discoverable without embedding a second source registry, taxonomy authority, schema system, policy engine, evidence store, release plane, or public-serving mechanism in Markdown.

[Back to top](#top)

---

## Authority and negative authority

Accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md). Those rules place human operational procedures under `docs/runbooks/` and require local README boundaries where ownership, exposure, mutation, generation, or lifecycle risk needs explicit routing.

| Concern | Owning authority | This directory's role |
|---|---|---|
| Procedure placement and inheritance | Accepted Directory Rules plus the parent [`docs/runbooks/` index](../README.md) | define the local Fauna boundary and disclose drift |
| Fauna domain meaning | [`docs/domains/fauna/`](../../domains/fauna/) and semantic contracts | orient; do not redefine |
| Machine shape | `schemas/` | cite current shape/maturity; do not host schema authority |
| Source identity, role, rights, cadence | source registries and accepted source-admission controls | require closure; do not admit or activate |
| Taxonomic authority | admitted/version-pinned taxonomy sources and accountable review | require closure; do not invent mappings |
| Sensitivity/geoprivacy | `policy/sensitivity/fauna/`, domain policy, accountable sensitivity review | explain stop conditions; do not invent rules or transform parameters |
| Evidence/citations | `EvidenceRef`, `EvidenceBundle`, receipts, and proofs | require support; do not manufacture evidence |
| Executable behavior | `tools/`, `tests/`, `fixtures/`, `pipelines/`, connectors, packages, applications, and workflows | point to exact entry points and interpret bounded results |
| Promotion/release/correction/rollback | `release/` and linked accountability objects | prepare review/rehearsal; do not approve or execute public state |
| Public delivery | governed APIs and released public-safe carriers | state the boundary; do not expose internal/restricted stores |
| This README | navigation, maturity disclosure, safety posture, maintenance contract | no operational, policy, release, or publication authority |

A procedure stops when its named identity, authority, permission, evidence, policy, review, release decision, correction path, or rollback target is unresolved. A README cannot convert `UNKNOWN`, `NEEDS VERIFICATION`, `CONFLICTED`, or `HOLD` into permission.

[Back to top](#top)

---

## Placement and canonical relationship

**Placement outcome: `PLACE` — CONFIRMED for this same-path additive update.**

| Property | Current result |
|---|---|
| Path | `docs/runbooks/fauna/README.md` |
| Owning root | `docs/` — human-readable operational documentation |
| Scope | Fauna operational-procedure lane |
| Prior path state | Existing tracked one-byte file at blob `8b137891...` |
| Structural effect | None; no create, move, rename, mirror, compatibility lane, or delete |
| GitHub review route | `@bartytime4life` through current CODEOWNERS routing |
| Accountable domain/sensitivity/release stewardship | `NEEDS VERIFICATION` |
| Release/publication effect | None |

This README is the local boundary for the procedure files in this directory. Domain-side documents under `docs/domains/fauna/` remain domain meaning, architecture, source, sensitivity, and planning surfaces; they do not become parallel operational-procedure authority merely because some carry runbook-like names.

The parent [`docs/runbooks/README.md`](../README.md) has an older repository-wide inventory snapshot. This stack intentionally does **not** rewrite its counts from connector inference. Refresh the parent only after the Fauna stack settles and an exact subtree inventory can be recomputed without guessing.

[Back to top](#top)

---

## Current repository state

The main checkpoint before this stack is `df6c3f5dadd2800fdc2356ceb540ca4e448f6c7a`; this README is stacked after draft PR #3509 so the sensitive-occurrence procedure can be described from the stack's actual bytes. The table separates documentation state from executable proof and operational authority.

| Surface | Current evidence | Bounded conclusion |
|---|---|---|
| This README | Prior file contained only a newline | Local Fauna procedure boundary was missing in substance |
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Repository-grounded v0.2; deterministic fixture-safety profile plus adjacent bounded profiles | Useful for named synthetic checks only; live source/evidence/policy/release remain held |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Repository-grounded v1.0; source-authority projection empty at its snapshot; live refresh held | Safe preparation/review guidance; not source activation |
| [`TAXONOMY_RESOLUTION_RUNBOOK.md`](./TAXONOMY_RESOLUTION_RUNBOOK.md) | Repository-grounded v1.0; manual handoff; executable resolver absent | Taxonomy ambiguity can be preserved and routed; taxonomic resolution remains `HOLD` |
| [`SENSITIVE_OCCURRENCE_REVIEW.md`](./SENSITIVE_OCCURRENCE_REVIEW.md) | Repository-grounded on prerequisite draft #3509; executable OccurrenceEvidence lane exists, production sensitivity policy does not | Safe review/handoff procedure; public sensitive-occurrence clearance remains `HOLD` |
| [`EBD_DERIVATIVE_RELEASE.md`](./EBD_DERIVATIVE_RELEASE.md) | Repository-grounded v1.0; rights-sensitive; current eBird source terms checked; no EBD data accessed | Review/handoff only; derivative release remains held |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Repository-grounded v1.0.0; generic A–G readiness validator present; Fauna candidate absent; promotion policy inactive | Readiness preparation only; no promotion/release authority |
| [`PUBLICATION_GATE_DRY_RUN.md`](./PUBLICATION_GATE_DRY_RUN.md) | Repository-grounded v1.0.1; shared synthetic publication-denial rehearsal executable; Fauna candidate-specific path held | Can rehearse denial; cannot publish |
| [`ROLLBACK_DRILL.md`](./ROLLBACK_DRILL.md) | Repository-grounded v0.1; shared marker-protected synthetic rehearsal executable; Fauna integrated rollback held | Bounded drill handoff only |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Proposal-era v0.1 dated 2026-05-13; placeholder owners; stale no-mounted-repo assumptions; stale links | **STALE / NEEDS MODERNIZATION**; do not treat as current operational rollback proof |
| Live source, production policy, proof, release, deployed public behavior | Not established by this index | `UNKNOWN` / `HOLD` unless proven by owning surfaces |

### Important maturity distinction

A substantive runbook can still describe an unimplemented operation. The current Fauna lane has strong documentation and several bounded synthetic executables, but that does not mean live Fauna operations or public release are commissioned.

[Back to top](#top)

---

## Direct child map

```text
docs/runbooks/fauna/
├── README.md                         # this local boundary
├── EBD_DERIVATIVE_RELEASE.md         # rights-sensitive derivative review/handoff
├── NO_NETWORK_TEST_RUNBOOK.md        # fixture-only validation
├── PROMOTION_RUNBOOK.md              # promotion-readiness assessment
├── PUBLICATION_GATE_DRY_RUN.md       # synthetic publication-denial rehearsal
├── ROLLBACK_DRILL.md                 # synthetic rollback rehearsal/tabletop
├── ROLLBACK_RUNBOOK.md               # stale proposal-era rollback procedure
├── SENSITIVE_OCCURRENCE_REVIEW.md    # sensitive-occurrence review/handoff
├── SOURCE_REFRESH_RUNBOOK.md         # admitted-source refresh preparation
└── TAXONOMY_RESOLUTION_RUNBOOK.md    # taxonomy ambiguity and review handoff
```

No child file above is a publisher. Where a child conflicts with accepted doctrine, current contracts/schemas/policy, or executable behavior, the higher/current owning evidence wins and the document requires correction.

[Back to top](#top)

---

## Start here

| Need | Current entry point | Terminal boundary |
|---|---|---|
| Verify synthetic Fauna fixture safety without network | [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | bounded validation handoff |
| Prepare a refresh of an already admitted source | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | source-edge review; live refresh currently `HOLD` |
| Preserve and route taxonomy ambiguity | [`TAXONOMY_RESOLUTION_RUNBOOK.md`](./TAXONOMY_RESOLUTION_RUNBOOK.md) | manual review handoff; resolver `HOLD` |
| Review a potentially sensitive occurrence | [`SENSITIVE_OCCURRENCE_REVIEW.md`](./SENSITIVE_OCCURRENCE_REVIEW.md) | public-safe review handoff; no production sensitivity clearance |
| Assess eBird/EBD derivative rights and release prerequisites | [`EBD_DERIVATIVE_RELEASE.md`](./EBD_DERIVATIVE_RELEASE.md) | rights-sensitive review handoff; release `HOLD` |
| Ask whether a named Fauna candidate is promotion-ready | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | readiness result for accountable review; no promotion |
| Rehearse publication denial / candidate gate posture | [`PUBLICATION_GATE_DRY_RUN.md`](./PUBLICATION_GATE_DRY_RUN.md) | no-write rehearsal; no publication |
| Exercise current shared rollback rehearsal | [`ROLLBACK_DRILL.md`](./ROLLBACK_DRILL.md) | bounded synthetic drill handoff |
| Operate a real Fauna rollback | **No current grounded procedure established** | `HOLD`; legacy [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) requires modernization first |

When more than one procedure applies, use the earliest trust boundary first. For example, do not enter promotion review to solve unresolved source admission, taxonomy, rights, or sensitivity questions.

[Back to top](#top)

---

## Lifecycle and state separation

KFM's lifecycle shorthand remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

These runbooks do not perform that lifecycle merely by describing it. Keep the following axes separate:

| Axis | Example |
|---|---|
| Documentation state | scaffold, repository-grounded draft, stale, corrected |
| Validator state | `PASS`/`ERROR` or profile-specific finite result |
| Candidate state | `quarantine`, `deny`, `error`, or profile-specific state |
| Policy state | allow/restrict/deny/abstain/hold according to the owning policy vocabulary |
| Review state | pending, approved, changes requested, rejected, or owning-record equivalent |
| Lifecycle state | RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLETS, PUBLISHED |
| Release state | candidate, decision/review status, immutable release/withdrawal/correction state |
| Deployment/publication | actual governed service/artifact exposure, separately evidenced |

A green test or successful rehearsal is not a lifecycle transition. A merged runbook is not release approval. A `PASS` on a sensitive held fixture can be correct while public exposure remains denied or held.

[Back to top](#top)

---

## Inputs, outputs, and permitted actors

### Common permitted inputs

Depending on the child procedure, inputs may include:

- exact repository revision and target blob/digest;
- repository-controlled synthetic fixtures;
- opaque candidate IDs and content hashes;
- already-admitted source references and source-role metadata;
- EvidenceRef/EvidenceBundle state references;
- rights, sensitivity, policy, and review state references;
- validator results and workflow URLs bound to the exact head;
- correction, withdrawal, supersession, and rollback target identifiers; and
- public-safe carrier metadata when already governed elsewhere.

### Common outputs

Runbooks should emit or describe only bounded handoffs such as:

- deterministic validator result or exact finding set;
- `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, `ESCALATE`, or profile-specific review-ready status;
- public-safe review packet;
- unresolved dependency list;
- correction/rollback recommendation; and
- next owning responsibility class.

### Permitted actors

GitHub CODEOWNERS establishes a repository review route, not biological, scientific, rights-holder, sensitivity, policy, or release authority. Where a procedure requires those roles, the runbook must record them as `NEEDS VERIFICATION` until an accountable authority record establishes them.

[Back to top](#top)

---

## Fauna-specific safety rules

1. **No exact sensitive location in public operational artifacts.** Avoid coordinates, reverse-engineerable labels, sensitive-site IDs, telemetry, private-land clues, or source-restricted detail.
2. **Do not publish geoprivacy recipes.** Transform parameters, seeds, radii, thresholds, or reconstruction hints remain outside public runbooks.
3. **Source role does not upgrade through aggregation.** An aggregator, model, administrative record, candidate, or synthetic record cannot masquerade as direct observation or legal/conservation authority.
4. **Rights and sensitivity are independent of evidence quality.** A well-supported record can still be non-public.
5. **Re-identifying joins are sensitive.** Public-safe fields may become unsafe when combined across time, place, parcels, habitat, imagery, observer information, or other domains.
6. **Taxonomy ambiguity fails closed.** A name match or model suggestion is not taxonomic authority.
7. **Public clients stay downstream.** Browsers, maps, search, exports, Evidence Drawer, Focus Mode, and AI must not become paths to restricted/internal occurrence detail.
8. **Correction/withdrawal must propagate.** A public-safe derivative cannot remain current after its supporting source/evidence/policy/review state is invalidated.
9. **KFM is not a wildlife emergency, veterinary, hunting, law-enforcement, or regulatory authority.** Redirect consequential operational action to the appropriate official authority rather than overstating a KFM result.

[Back to top](#top)

---

## Finite outcomes and stop conditions

Use the finite result grammar defined by the owning child profile. Across the lane, the common operational meanings are:

- **`PASS`** — the bounded validator/rehearsal satisfied its declared profile only;
- **`HOLD`** — required identity, authority, evidence, rights, sensitivity, policy, review, release, or rollback closure is incomplete;
- **`ABSTAIN`** — the requested claim or public conclusion outruns supported/safe evidence;
- **`DENY`** — the requested operation or representation conflicts with an applicable boundary;
- **`ERROR`** — malformed input, identity mismatch, parser/validator failure, or inconsistent state prevents trustworthy classification;
- **`ESCALATE`** — accountable specialist review is required and cannot be inferred locally.

Do not force these prose-level common meanings into a child machine schema that already owns a different enum. State separation is part of correctness.

Always stop when:

- a live-source action lacks admitted source identity and rights closure;
- protected values would enter an inappropriate/public surface;
- taxonomy or source role is unresolved for a consequential claim;
- sensitivity or geoprivacy policy is required but unimplemented/unapproved;
- EvidenceRef/EvidenceBundle support is missing for a claim;
- review authority is absent;
- a public/restricted conversion depends on a permissive scaffold as if it were a closed gate;
- release/correction/rollback prerequisites are incomplete; or
- another active PR/migration owns the same authority surface.

[Back to top](#top)

---

## Validation and rehearsal boundary

Current Fauna executable evidence is deliberately bounded:

- synthetic fixture safety validation;
- draft `OccurrenceEvidence` schema/semantic validation;
- tile-field allowlist and occurrence-related bounded profiles where documented;
- generic promotion-readiness validation;
- shared synthetic publication-denial rehearsal; and
- shared marker-protected synthetic rollback rehearsal.

Those controls test repository behavior, not wildlife truth. They do not prove:

- a live Fauna source is admitted or current;
- a real occurrence or taxonomy resolution is authoritative;
- production sensitivity policy or geoprivacy transformation works;
- restricted-access controls prevent every leak path;
- a Fauna release candidate is complete;
- an accountable reviewer approved public exposure;
- operational rollback/invalidation is wired; or
- a public deployment exists.

Hosted CI must be bound to the exact PR head. `SKIPPED`, `NOT_RUN`, `HOLD`, and missing workflow coverage must not be reported as `PASS`.

[Back to top](#top)

---

## Maintenance, review, and correction triggers

Update this README when:

- a child runbook is added, retired, renamed, superseded, or materially changes maturity;
- a Fauna schema moves from scaffold to closed/enforced or vice versa;
- source-role, taxonomy, sensitivity, rights, evidence, policy, review, or release vocabulary changes;
- a new executable profile or workflow becomes part of a procedure;
- an operational source, candidate-specific release, restricted-access path, or rollback executor is actually admitted;
- a child document retains stale path/owner/no-mounted-repo assumptions;
- parent runbook inventory is refreshed; or
- a new safety/re-identification risk is discovered.

Corrections should be additive and reviewable. Preserve historical receipts, prior review results, source snapshots, and release/correction lineage rather than rewriting them to match newer doctrine.

[Back to top](#top)

---

## Open verification backlog

Highest-value remaining work after this stack:

1. **Modernize `ROLLBACK_RUNBOOK.md`** against the current shared RollbackCard validator, synthetic rehearsal, Fauna release holds, and actual correction/rollback roots; remove stale nonexistent links and placeholder-owner claims without implying operational rollback.
2. **Refresh the parent `docs/runbooks/README.md` inventory** only after this stack settles and exact recursive counts can be recomputed rather than guessed.
3. **Implement production Fauna sensitivity policy only through a separately reviewed policy slice** with safe synthetic positive/negative tests; the current scaffold/no-op Rego files are not clearance.
4. **Close and test public/restricted occurrence machine shapes** before claiming enforced conversion or restricted-access behavior.
5. **Resolve RedactionReceipt authority/home conflict** before making it a release prerequisite with machine enforcement.
6. **Establish accountable stewards and independent-review routes** for Fauna, taxonomy, rights, sensitivity, evidence, policy, and release decisions.
7. **Prove restricted-content non-leakage** across API, MapLibre, search, graph, export, Evidence Drawer, Focus Mode, logs, and AI composition before any sensitive public mission graduates.
8. **Keep live source activation, release, deployment, and publication separate** from documentation and fixture completion.

[Back to top](#top)

---

## Related responsibility roots

| Responsibility | Representative surface |
|---|---|
| Domain meaning and architecture | [`docs/domains/fauna/`](../../domains/fauna/) |
| Semantic contracts | [`contracts/domains/fauna/`](../../../contracts/domains/fauna/) |
| Machine schemas | [`schemas/contracts/v1/domains/fauna/`](../../../schemas/contracts/v1/domains/fauna/) |
| Synthetic fixtures | [`fixtures/domains/fauna/`](../../../fixtures/domains/fauna/) |
| Executable validators | [`tools/validators/domains/fauna/`](../../../tools/validators/domains/fauna/) |
| Tests | `tests/domains/fauna/` |
| Source registry | [`data/registry/sources/fauna/`](../../../data/registry/sources/fauna/) |
| Domain/sensitivity policy | [`policy/domains/fauna/`](../../../policy/domains/fauna/), [`policy/sensitivity/fauna/`](../../../policy/sensitivity/fauna/) |
| Proofs | [`data/proofs/fauna/`](../../../data/proofs/fauna/) |
| Release candidates | [`release/candidates/fauna/`](../../../release/candidates/fauna/) |
| Workflow orchestration | `.github/workflows/domain-fauna.yml` and profile-specific workflows |

[Back to top](#top)

---

## Evidence basis

### Repository evidence

Current-state claims in this README come from the pinned main checkpoint plus the prerequisite sensitive-occurrence branch. The most important facts are the one-byte prior README, the now-substantive child runbooks, current occurrence validator/fixture evidence, explicit Fauna candidate/release holds, and the still-stale rollback runbook.

### Drive lineage

`KFM_Fauna_Architecture_PDF_Only_Report.pdf` is retained as design lineage. Its high-value principles—synthetic-first validation, source-role separation, fail-closed sensitive occurrence handling, geoprivacy/redaction review, rights checks, continuity, and no live-source-first implementation—are useful only where current repository evidence still supports them. The report's no-mounted-repository assumptions are superseded by current GitHub evidence.

No Drive file is modified, reorganized, or promoted to repository authority by this README.

[Back to top](#top)

---

## Document change rollback

This change modifies one documentation file only.

Before merge, close the draft pull request and abandon the branch. After an authorized merge, revert this README through normal Git history if its inventory, routing, or maturity classification proves inaccurate. Do not delete child procedures, rewrite source/evidence history, weaken sensitivity policy, change lifecycle state, or alter release/publication state as part of documentation rollback.

**Non-effects:** this README does not admit or retrieve a source, resolve taxonomy, expose or transform an occurrence, create evidence, decide rights/sensitivity/policy, authenticate review, change lifecycle data, execute rollback, release, deploy, promote, publish, or change repository settings.

[Back to top](#top)
