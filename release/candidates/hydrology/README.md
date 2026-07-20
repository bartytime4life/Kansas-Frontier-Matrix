# `release/candidates/hydrology/` - Hydrology Candidate Review Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-hydrology-readme
title: release/candidates/hydrology/ - Hydrology Candidate Review Lane
version: v2
status: draft
policy_label: public
owners:
  - <hydrology-domain-steward>
  - <release-steward>
  - <data-steward>
  - <policy-reviewer-when-required>
created: NEEDS VERIFICATION
updated: 2026-07-20
owning_root: release/
responsibility: pre-publication review packets for Hydrology release candidates
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2b31ccbd9ba5b3fe6772ea1b0165eca45bdfebb0
tags: [kfm, release, candidates, hydrology, evidence, policy, validation, correction, rollback]
notes:
  - "A candidate is not a release, publication approval, or public artifact."
  - "Promotion is a governed state transition, not a file move."
  - "Machine contracts and schemas outrank the illustrative record template in this README."
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-hydrology-1f9eda)
![publication](https://img.shields.io/badge/publication-not_yet-orange)
![posture](https://img.shields.io/badge/posture-fail_closed-critical)

> [!IMPORTANT]
> This lane records **pre-publication review packets**. A file, dossier, artifact pointer, passing schema check, pull request, or `APPROVED_FOR_MANIFEST` status in this directory does not publish Hydrology material. Publication still requires governed evidence, policy, validation, review, manifest, correction, and rollback closure.

## Quick navigation

- [Purpose](#purpose)
- [Status and authority](#status-and-authority)
- [Evidence boundary](#evidence-boundary)
- [Placement and repository fit](#placement-and-repository-fit)
- [Lane boundaries](#lane-boundaries)
- [Hydrology candidate scope](#hydrology-candidate-scope)
- [Candidate states](#candidate-states)
- [Candidate dossier contract](#candidate-dossier-contract)
- [Hydrology review gates](#hydrology-review-gates)
- [Source-role, identity, and time safeguards](#source-role-identity-and-time-safeguards)
- [Manifest handoff](#manifest-handoff)
- [Minimal candidate dossier](#minimal-candidate-dossier)
- [Review checklist](#review-checklist)
- [Naming and change discipline](#naming-and-change-discipline)
- [Related authority surfaces](#related-authority-surfaces)
- [Open verification](#open-verification)
- [Maintenance and rollback](#maintenance-and-rollback)

## Purpose

`release/candidates/hydrology/` is the Hydrology domain lane for assembling and reviewing candidate release packets before a governed promotion decision or `ReleaseManifest` handoff.

A candidate is not a release.

The lane exists to let reviewers answer a bounded question:

> Does this exact Hydrology candidate have enough identified, resolvable, policy-safe, validated, reversible support to advance toward manifest preparation, or must it remain held, be repaired, be superseded, or be withdrawn?

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move. Candidate review must preserve the prior lifecycle state when evidence, identity, rights, sensitivity, time, validation, catalog, review, correction, or rollback support is incomplete.

## Status and authority

| Field | Value |
|---|---|
| Document type | Hydrology release-candidate directory README |
| Owning responsibility root | `release/` |
| Domain segment | `hydrology` |
| Lane status | `draft` |
| Public posture | Pre-publication; no candidate is public merely because it is recorded here |
| Semantic authority | Release contracts, evidence contracts, policy, accepted ADRs, and steward decisions outrank this README |
| Machine authority | Applicable schemas and validators define machine shape and conformance; their maturity must be checked separately |
| GitHub review route | `@bartytime4life` is the CONFIRMED CODEOWNERS route for `release/`; semantic steward assignments remain NEEDS VERIFICATION |
| Default failure posture | Preserve the prior state; use `BLOCKED`, `REPAIR_REQUIRED`, `DEFERRED`, `WITHDRAWN`, or a schema-defined negative decision as appropriate |

This README is orientation and review guidance. It is not a `PromotionDecision`, `PolicyDecision`, `ReleaseManifest`, `ReviewRecord`, `EvidenceBundle`, validation receipt, correction notice, rollback card, release approval, or publication authority.

## Evidence boundary

This revision is grounded in the default branch at commit `2b31ccbd9ba5b3fe6772ea1b0165eca45bdfebb0` and in the supplied Directory Rules. The table distinguishes what the repository proves from what remains open.

| Evidence | Confirmed in the inspected snapshot | Limit |
|---|---|---|
| [`docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) and supplied Directory Rules | `release/` owns release decisions and `release/candidates/<domain>/` is the domain-lane pattern | The repository also contains a conflicting architecture-path copy of Directory Rules; both copies agree on this lane's placement |
| [`release/README.md`](../../README.md) | `release/` is distinct from `data/published/`; candidate review, promotion decisions, manifests, corrections, and rollback support remain separate | The root README records unresolved singular/plural manifest and correction lane conventions |
| [`release/candidates/README.md`](../README.md) | Parent candidate states and minimum review fields | Parent prose is guidance, not a schema or release decision |
| [`contracts/release/promotion_decision.md`](../../../contracts/release/promotion_decision.md) and its [schema](../../../schemas/contracts/v1/release/promotion_decision.schema.json) | The current machine decision enum is `APPROVE`, `DENY`, or `ABSTAIN`; Hydrology IDs match `promo:hydrology:<suffix>` | Contract and schema remain `PROPOSED`; validator, fixtures, policy wiring, and enforcement need verification |
| [`contracts/release/release_manifest.md`](../../../contracts/release/release_manifest.md) and its [schema](../../../schemas/contracts/v1/release/release_manifest.schema.json) | The common schema is a thin, permissive `PROPOSED` stub with only `id` required | Schema validity alone does not establish release closure |
| [Hydrology release-manifest schema](../../../schemas/contracts/v1/domains/hydrology/release_manifest.schema.json) | A second Hydrology-specific thin `PROPOSED` schema exists | Its authority relationship to the common release schema is NEEDS VERIFICATION; do not maintain divergent instances silently |
| [`docs/domains/hydrology/DATA_LIFECYCLE.md`](../../../docs/domains/hydrology/DATA_LIFECYCLE.md) and [`PUBLICATION_POSTURE.md`](../../../docs/domains/hydrology/PUBLICATION_POSTURE.md) | Hydrology candidates must preserve source role, identity, temporal scope, evidence, policy, correction, and rollback boundaries | Many described implementation leaves remain `PROPOSED` or `NEEDS VERIFICATION` |
| [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) | `release/` routes review to `@bartytime4life` | CODEOWNERS is not semantic stewardship, proof that review occurred, or release approval |

No runtime route, production dataset, populated candidate dossier, successful Hydrology release, or published Hydrology artifact is asserted by this README.

## Placement and repository fit

Directory Rules place a file by responsibility, then lifecycle and domain. This README satisfies that protocol:

1. Its primary responsibility is release-candidate governance, so the owning root is `release/`.
2. It is not lifecycle data, so it does not belong under `data/raw/`, `data/processed/`, or `data/published/`.
3. It is Hydrology-specific, so `hydrology` is a segment inside the release-candidate root.
4. The path already exists and does not create a parallel release authority.

```text
release/
├── candidates/
│   ├── README.md
│   └── hydrology/
│       └── README.md          # this file; candidate review guidance
├── promotion_decisions/
│   └── hydrology/             # governed transition decisions
└── manifests/                 # release manifests and index

data/
├── processed/hydrology/       # validated candidate payloads, when present
├── catalog/domain/hydrology/  # catalog closure, when present
├── proofs/                    # proof objects; separate authority family
├── receipts/                  # process memory; separate authority family
└── published/layers/hydrology/# released public-safe artifacts only
```

The tree is a responsibility map, not proof that every illustrated child contains implementation or released artifacts.

## Lane boundaries

| Concern | Correct responsibility | Candidate-lane behavior |
|---|---|---|
| Candidate dossier and readiness review | `release/candidates/hydrology/` | Record or link the bounded review packet |
| Candidate bytes and normalized records | Appropriate `data/<phase>/hydrology/` lane | Link by stable pointer and digest; do not copy payloads here |
| Object meaning | `contracts/` | Link the governing contract; do not redefine it in candidate prose |
| Machine shape | `schemas/` | Record schema ID/version and validation result |
| Admissibility, rights, sensitivity, and release policy | `policy/` | Link the evaluated policy bundle and decision |
| Evidence and proof | Evidence contracts plus `data/proofs/` | Require resolvable references; do not treat summaries or screenshots as proof |
| Validation and process memory | Validators plus `data/receipts/` | Link immutable reports/receipts and identify skipped checks |
| Promotion decision | `release/promotion_decisions/hydrology/` | Link the decision; do not duplicate or infer it |
| Release manifest | Accepted manifest lane under `release/` | Handoff only after candidate closure; do not create a manifest by prose |
| Published Hydrology layer | `data/published/layers/hydrology/` | Candidate lane never stores or directly serves it |
| Correction and rollback | Accepted `release/` correction/rollback families plus governed data-plane receipts | Link targets and lineage; do not silently overwrite history |

### What belongs here

- Candidate dossiers and lane indexes.
- Readiness matrices and bounded review summaries.
- Stable pointers to candidate artifacts, source descriptors, EvidenceBundles, validation reports, policy decisions, review records, manifests, corrections, rollback cards, receipts, and proofs.
- Explicit blockers, negative decisions, repair plans, supersession notes, and withdrawal records.
- Hydrology-specific source-role, identity, temporal, freshness, and public-safety checks needed for a release decision.

### What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published payloads.
- Bulk datasets, tiles, PMTiles, GeoParquet, COGs, exports, API payloads, or direct model output.
- Contracts, schemas, policy-as-code, source descriptors, validators, fixtures, or test implementations.
- Secrets, restricted source material, private operational data, or exact sensitive cross-lane joins.
- Generated language, maps, charts, screenshots, or dashboards presented as root evidence.
- Flood warnings, emergency instructions, engineering determinations, or statements that substitute for the responsible source authority.
- Final release or publication approval without the separately governed records and review.

## Hydrology candidate scope

A Hydrology candidate may concern one or more of these families, but each family keeps its own source role, evidence, identity, temporal, policy, and limitation posture.

| Candidate family | Minimum review emphasis |
|---|---|
| Watershed or HUC boundary | Source snapshot/vintage, HUC hierarchy, CRS, geometry digest, stable identity, administrative/context limits |
| Hydro feature or reach network | Source family/version, permanent identifiers, crosswalk relation, split/merge/retired/ambiguous handling |
| Gauge site | Provider/site identity, location precision, source role, parameter coverage, status and retirement posture |
| Flow or water-level observation | Parameter, unit, qualifier, provisional/final state, observed time, retrieval time, valid time, freshness and stale behavior |
| Water-quality observation | Parameter/method/unit/qualifier, sampling context, detection limits, evidence and source terms |
| Groundwater or aquifer context | Well/aquifer identity, location generalization, private-land or sensitive-join review, time and measurement context |
| NFHL or other regulatory flood context | Regulatory role only, effective date/version, no observed-inundation or current-warning claim |
| Modeled or derived hydrograph/trace | Model/run identity, inputs, parameters, bounds, uncertainty, derivation receipt, no upgrade to observation |
| Cross-domain Hydrology join | Join purpose, each source role, policy decision, sensitivity transform, reconstruction risk, validation and release scope |

Candidate scope must say what the material supports and what it does **not** support. Labels such as `water`, `flood`, `stream`, or `current` are not sufficient source-role or temporal descriptions.

## Candidate states

Use the parent candidate vocabulary for dossier state. Do not substitute a runtime outcome, policy outcome, or GitHub state.

| Candidate state | Meaning | Release effect |
|---|---|---|
| `PROPOSED` | Candidate is named; packet is incomplete | None |
| `ASSEMBLING` | Evidence and review materials are being gathered | None |
| `READY_FOR_REVIEW` | Required packet sections are present for steward review | None |
| `APPROVED_FOR_MANIFEST` | Review permits manifest preparation | Not published; manifest and remaining gates still required |
| `PROMOTED` | Candidate is linked to an approved governed release path | Do not infer `PUBLISHED`; verify the manifest and release record |
| `DEFERRED` | Candidate remains valid to retain but is not ready now | None; prior public state remains |
| `REPAIR_REQUIRED` | A bounded defect must be corrected before review continues | None; preserve prior state |
| `BLOCKED` | Named evidence, policy, rights, sensitivity, identity, validation, review, or rollback blocker prevents progress | None; fail closed |
| `WITHDRAWN` | Candidate is removed from consideration | None; retain review lineage |
| `SUPERSEDED` | A newer candidate replaces this packet | None; link both directions where possible |

### Vocabulary separation

These vocabularies answer different questions and must not be collapsed:

| Vocabulary | Current values | Question answered |
|---|---|---|
| Candidate state | Table above | Where is the dossier in review? |
| Machine `PromotionDecision.decision` | `APPROVE`, `DENY`, `ABSTAIN` | Did the governed transition gate permit a specific run? |
| Hydrology promotion-lane recommendation | `PROMOTE_TO_MANIFEST`, `HOLD_FOR_EVIDENCE`, `HOLD_FOR_VALIDATION`, `HOLD_FOR_POLICY`, `REPAIR_REQUIRED`, `SUPERSEDE_CANDIDATE`, `NO_ACTION` | What should reviewers do next? |
| Runtime/policy response | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, and `HOLD` where defined | What may a governed consumer return? |

The machine enum and promotion-lane recommendation vocabulary are not identical in the current repository. Record both when both exist; do not translate between them silently.

## Candidate dossier contract

Every dossier should contain enough information for a reviewer to reproduce the candidate boundary without reading unstated context.

### 1. Identity and change control

- Stable candidate ID, version, and human-readable title.
- Candidate state and state date.
- Owning domain/release roles and GitHub review route.
- Exact scope: geography, feature/object families, time interval, source versions, release surface, and excluded claims.
- Predecessor, `supersedes`, `superseded_by`, or withdrawal relationship where applicable.
- Candidate packet digest or an explanation of how the reviewed bytes are pinned.

### 2. Artifact and lifecycle pointers

- Exact pointer to the candidate artifact in its governed lifecycle lane.
- Artifact media/type, byte digest, schema ID/version, and producing run ID.
- Current lifecycle state and proposed published target.
- Explicit confirmation that no payload is duplicated in this candidate directory.

### 3. Source and evidence closure

- Every source descriptor ID/version and source role.
- Rights, license, redistribution, attribution, cadence, and sensitivity posture.
- EvidenceRef-to-EvidenceBundle resolution status for every consequential public claim.
- Source limitations, citation text, and official-source referral where material.
- Explicit source-role anti-collapse result.

### 4. Spatial identity and temporal scope

- CRS, geometry precision/generalization, geometry digest, and identity/crosswalk status.
- Treatment of ambiguous, split, merged, retired, or unresolved HUC/reach/gauge identity.
- Separate observed, valid, source, retrieval, release, correction, provisional/final, and model-run times where material.
- Freshness threshold, current freshness result, stale-state behavior, and update cadence.

### 5. Validation, policy, proof, and review

- Validation report and receipt references with outcomes and the exact checked revision.
- Invalid/negative cases exercised, including the expected finite outcome.
- Policy bundle/version/hash and `PolicyDecision` reference.
- Proof/catalog closure references and unresolved dependencies.
- Review record, required roles, separation-of-duties status, and open objections.

### 6. Release, correction, and rollback readiness

- Proposed release surface and intended manifest family.
- Promotion recommendation and, when emitted, machine `PromotionDecision` reference.
- Correction notice path and downstream invalidation scope.
- Rollback card/target and prior safe release, or a reviewed reason rollback is not available.
- Public-cache, alias, catalog, API, map, Evidence Drawer, export, and AI-answer impact.

## Hydrology review gates

No single check substitutes for the complete gate set.

| Gate | Pass condition | Default candidate disposition when unresolved |
|---|---|---|
| Scope and placement | Candidate responsibility, lifecycle pointer, domain, and intended release surface are explicit and correctly placed | `REPAIR_REQUIRED` |
| Artifact identity | Reviewed bytes, version, digest, run, and schema are pinned | `BLOCKED` |
| Source admission | Source descriptor, role, citation, rights, cadence, and sensitivity resolve | `BLOCKED` or policy `DENY` |
| Source-role separation | Regulatory, observed, modeled, aggregate, administrative, candidate, and synthetic roles remain distinct | `BLOCKED`; NFHL role collapse requires denial/correction |
| Evidence closure | Consequential claims resolve through EvidenceRef to EvidenceBundle | `BLOCKED`; downstream answer posture is `ABSTAIN` or `ERROR` as defined |
| Spatial identity | HUC/reach/gauge/object identity and geometry assumptions are deterministic or visibly unresolved | `REPAIR_REQUIRED` or `BLOCKED`; no silent identity choice |
| Temporal and freshness | Material time kinds, cadence, provisional/final state, stale threshold, and stale behavior are explicit | `DEFERRED` or `BLOCKED` |
| Validation | Applicable schema, contract, policy, identity, temporal, field-allowlist, and negative checks have recorded outcomes | `REPAIR_REQUIRED` or `BLOCKED` |
| Rights and sensitivity | Redistribution and public-safe transformation are permitted and reviewable | `BLOCKED` or policy `DENY` |
| Catalog and proof | Catalog refs, proof objects, receipts, digests, and citations close without using derived surfaces as truth | `BLOCKED` |
| Review | Required reviewers and separation of duties are satisfied | `READY_FOR_REVIEW` or `BLOCKED`; never self-approve material release work |
| Correction and rollback | Correction lineage, invalidation scope, rollback target, and prior-safe-state posture are explicit | `BLOCKED` |
| Manifest handoff | Candidate packet identifies the accepted manifest/schema path and remaining release checks | `APPROVED_FOR_MANIFEST` only after reviewer decision |

A `PASS` means only that the named check passed for the cited scope. It does not upgrade the candidate to a release or make a candidate artifact public.

## Source-role, identity, and time safeguards

### NFHL and flood-related material

- Treat NFHL as **regulatory flood context**, not observed inundation, forecast, current event truth, or emergency warning.
- Preserve effective date, source version, issuing authority, and regulatory limitations.
- If candidate wording, attributes, layer names, queries, or AI summaries collapse the role, block the candidate and correct the claim before review continues.
- KFM candidate review does not replace FEMA, NWS, USGS, state, local, engineering, or emergency-management authority.

### Identity ambiguity

- Record exact, split, merge, retired, heuristic, ambiguous, and unknown relationships rather than choosing a convenient match.
- A heuristic crosswalk must carry method, inputs, threshold, score, and receipt.
- Unresolved identity may support a narrowed context display, but not a confident feature-level claim. Use the policy/runtime outcome defined by the governing contract.

### Temporal integrity

- Never substitute retrieval time for observation time, release time for validity, or a current API response for historical finality.
- A stale candidate is not silently freshened by rerunning prose, a map build, or an AI summary.
- Provisional measurements remain provisional until the source and policy permit a new reviewed state.
- A time-sensitive candidate must define what happens when the freshness window expires before or after manifest handoff.

### Cross-domain joins

Hydrology joined to hazards, roads, infrastructure, private land, archaeology, ecology, agriculture, or living-person context may raise sensitivity and reconstruction risk. The candidate must record each source role, the join purpose, public-safe transform, policy decision, review burden, and whether precision must be generalized, restricted, quarantined, delayed, or denied.

## Manifest handoff

`APPROVED_FOR_MANIFEST` authorizes preparation, not publication.

Before handoff, the dossier must identify:

- the candidate and producing run;
- exact artifact pointers and digests;
- source/evidence, policy, validation, review, rights, sensitivity, catalog, proof, receipt, correction, and rollback references;
- the intended common or Hydrology manifest schema and its current maturity;
- unresolved fields that the permissive manifest schema does not enforce;
- the linked promotion recommendation and schema-conformant `PromotionDecision`, when one exists;
- the proposed public surface and public-safe field/geometry posture;
- the prior release or explicit withdrawal posture.

> [!WARNING]
> The common and Hydrology release-manifest schemas are currently thin `PROPOSED` stubs. A schema-valid manifest with only an `id` is not release-complete. Reviewers must apply the semantic, policy, evidence, validation, correction, and rollback gates even when the schema passes.

## Minimal candidate dossier

The following is a documentation template, not a machine schema. Replace every placeholder or mark it `N/A` with a reason. Do not leave angle-bracket examples in a submitted dossier.

```markdown
# <candidate-title>

## Candidate identity

| Field | Value |
|---|---|
| Candidate ID | <stable-id> |
| Version | <version> |
| State | PROPOSED / ASSEMBLING / READY_FOR_REVIEW / APPROVED_FOR_MANIFEST / PROMOTED / DEFERRED / REPAIR_REQUIRED / BLOCKED / WITHDRAWN / SUPERSEDED |
| State date | <YYYY-MM-DD> |
| Domain | hydrology |
| Owners | <role identifiers> |
| Review route | <verified GitHub owner or N/A> |
| Supersedes | <candidate-ref or N/A> |
| Packet digest | <sha256:... or method> |

## Scope

- Geography: <scope>
- Object or layer families: <scope>
- Source versions: <versions>
- Temporal support: <observed/valid/source/retrieval/release/model times>
- Intended release surface: <API/map/export/Evidence Drawer/other>
- Supported claims: <bounded claim classes>
- Excluded claims: <explicit non-claims>

## Candidate artifact

| Field | Value |
|---|---|
| Lifecycle state | <PROCESSED or CATALOG/TRIPLET state> |
| Artifact pointer | <governed repository/artifact ref> |
| Artifact digest | <sha256:...> |
| Media/object type | <type> |
| Schema | <schema id/version/path> |
| Producing run | <run-id and receipt> |
| Proposed published target | <target or N/A> |

## Source and evidence closure

| Source descriptor | Source role | Rights/sensitivity | EvidenceBundle | Citation/limitations | Status |
|---|---|---|---|---|---|
| <ref> | <role> | <decision/ref> | <resolved ref> | <citation and limits> | PASS / FAIL / PARTIAL / UNKNOWN |

### Source-role anti-collapse

<result; include NFHL regulatory-context check when applicable>

## Spatial identity and temporal posture

- CRS and precision: <value>
- Geometry digest/generalization: <value>
- HUC/reach/gauge identity: <value>
- Ambiguity/crosswalk method: <value or N/A>
- Freshness threshold and result: <value>
- Stale-state behavior: <value>
- Provisional/final posture: <value>

## Validation and policy

| Check | Evidence | Outcome | Notes |
|---|---|---|---|
| Schema/contract | <ref> | PASS / FAIL / PARTIAL / NOT RUN | <notes> |
| Identity/geometry | <ref> | PASS / FAIL / PARTIAL / NOT RUN | <notes> |
| Temporal/freshness | <ref> | PASS / FAIL / PARTIAL / NOT RUN | <notes> |
| Source-role negative cases | <ref> | PASS / FAIL / PARTIAL / NOT RUN | <notes> |
| Rights/sensitivity | <ref> | PASS / FAIL / PARTIAL / NOT RUN | <notes> |
| Catalog/proof closure | <ref> | PASS / FAIL / PARTIAL / NOT RUN | <notes> |

- Policy bundle/version: <ref>
- PolicyDecision: <ref and outcome>
- Open blockers: <list or none>

## Review and promotion

- Required reviewers: <roles>
- ReviewRecord: <ref or pending>
- Separation of duties: <status>
- Candidate recommendation: PROMOTE_TO_MANIFEST / HOLD_FOR_EVIDENCE / HOLD_FOR_VALIDATION / HOLD_FOR_POLICY / REPAIR_REQUIRED / SUPERSEDE_CANDIDATE / NO_ACTION
- PromotionDecision: <ref with APPROVE/DENY/ABSTAIN, or not emitted>
- Decision rationale: <evidence-grounded reason>

## Correction and rollback

- Correction path: <ref or planned governed path>
- Invalidates: <claims/artifacts/surfaces or none>
- RollbackCard/target: <ref>
- Prior safe release: <ref or none>
- Public cache/alias/catalog/API/map/AI impact: <scope>

## Open verification

- [ ] <item, owner, and resolving evidence>
```

## Review checklist

### Packet integrity

- [ ] Candidate ID, version, state, scope, predecessor, and digest are explicit.
- [ ] Candidate artifact pointer resolves and the reviewed bytes are digest-pinned.
- [ ] Lifecycle state and proposed release target are distinct.
- [ ] No payload, schema, policy, proof, receipt, source record, or published artifact is duplicated here.

### Evidence and source integrity

- [ ] Every source descriptor and source role resolves.
- [ ] Rights, attribution, redistribution, cadence, and sensitivity are recorded.
- [ ] Consequential claims resolve from EvidenceRef to EvidenceBundle.
- [ ] Source limitations and official-source referral are visible.
- [ ] Regulatory, observed, modeled, aggregate, administrative, candidate, and synthetic roles do not collapse.
- [ ] NFHL is regulatory context only when present.

### Hydrology correctness

- [ ] CRS, geometry digest, precision/generalization, and identity method are recorded.
- [ ] Ambiguous, split, merged, retired, heuristic, and unknown identities fail closed.
- [ ] Units, parameters, methods, and qualifiers are preserved where applicable.
- [ ] Observed, valid, source, retrieval, release, correction, provisional/final, and model times remain distinct where material.
- [ ] Freshness and stale-state behavior are tested or explicitly unresolved.

### Governance and reversibility

- [ ] Validation, negative cases, policy decision, proofs, receipts, and catalog closure are linked.
- [ ] Required reviewers and separation of duties are recorded.
- [ ] Candidate recommendation and machine promotion decision are kept distinct.
- [ ] Correction scope, invalidation targets, rollback target, and prior safe state are explicit.
- [ ] Public/API/UI/map/export/AI impact is bounded and uses governed interfaces only.
- [ ] No warning, regulatory determination, engineering conclusion, or unsupported AI claim is introduced.

### Handoff decision

- [ ] Every checklist exception has an owner, disposition, and evidence needed to close it.
- [ ] The final candidate state matches the recorded review decision.
- [ ] `APPROVED_FOR_MANIFEST` is used only for manifest preparation.
- [ ] Publication remains denied until the separately governed release closes.

## Naming and change discipline

The release-root README currently recommends dated, lowercase, descriptive Markdown filenames. Until a candidate-specific naming contract is accepted, use this as **PROPOSED guidance**:

```text
<YYYY-MM-DD>_<hydrology-scope>_candidate.md
```

Examples:

```text
2026-07-20_huc12-watershed_candidate.md
2026-07-20_gauge-flow-observation_candidate.md
2026-07-20_nfhl-regulatory-context_candidate.md
```

- Do not encode unverified release approval in a filename.
- Do not use `final`, `official`, `current`, or `published` unless a governed record establishes that state.
- Do not overwrite a reviewed dossier to hide history; emit a correction or successor and link lineage.
- Do not create family subdirectories until responsibility, naming, index updates, review ownership, and any ADR need are resolved.
- Keep one candidate packet narrow enough to review, invalidate, supersede, or withdraw independently.

## Related authority surfaces

| Surface | Role |
|---|---|
| [`release/candidates/README.md`](../README.md) | Parent candidate states and common packet expectations |
| [`release/README.md`](../../README.md) | Release-governance root and current lane inventory |
| [`release/promotion_decisions/hydrology/README.md`](../../promotion_decisions/hydrology/README.md) | Hydrology promotion recommendation and decision lane |
| [`release/manifests/README.md`](../../manifests/README.md) | Current manifest collection lane |
| [`contracts/release/promotion_decision.md`](../../../contracts/release/promotion_decision.md) | PromotionDecision meaning |
| [`schemas/contracts/v1/release/promotion_decision.schema.json`](../../../schemas/contracts/v1/release/promotion_decision.schema.json) | PromotionDecision machine shape |
| [`contracts/release/release_manifest.md`](../../../contracts/release/release_manifest.md) | ReleaseManifest meaning and current maturity boundary |
| [`schemas/contracts/v1/release/release_manifest.schema.json`](../../../schemas/contracts/v1/release/release_manifest.schema.json) | Common ReleaseManifest machine shape |
| [`contracts/evidence/evidence_bundle.md`](../../../contracts/evidence/evidence_bundle.md) | EvidenceBundle meaning |
| [`contracts/policy/policy_decision.md`](../../../contracts/policy/policy_decision.md) | PolicyDecision meaning |
| [`contracts/release/rollback_card.md`](../../../contracts/release/rollback_card.md) | RollbackCard meaning |
| [`contracts/correction/correction_notice.md`](../../../contracts/correction/correction_notice.md) | CorrectionNotice meaning |
| [`docs/domains/hydrology/RELEASE_INDEX.md`](../../../docs/domains/hydrology/RELEASE_INDEX.md) | Human navigation across Hydrology release surfaces |
| [`docs/domains/hydrology/PUBLICATION_POSTURE.md`](../../../docs/domains/hydrology/PUBLICATION_POSTURE.md) | Hydrology publish/hold/deny posture |
| [`docs/domains/hydrology/DATA_LIFECYCLE.md`](../../../docs/domains/hydrology/DATA_LIFECYCLE.md) | Hydrology lifecycle and gate context |
| [`docs/runbooks/hydrology/PROMOTION_RUNBOOK.md`](../../../docs/runbooks/hydrology/PROMOTION_RUNBOOK.md) | Hydrology promotion procedure guidance |
| [`docs/runbooks/hydrology/ROLLBACK_RUNBOOK.md`](../../../docs/runbooks/hydrology/ROLLBACK_RUNBOOK.md) | Hydrology correction and rollback guidance |
| [`policy/domains/hydrology/README.md`](../../../policy/domains/hydrology/README.md) | Hydrology policy lane orientation |
| [`tests/domains/hydrology/README.md`](../../../tests/domains/hydrology/README.md) | Hydrology enforceability-proof lane orientation |
| [`data/published/layers/hydrology/README.md`](../../../data/published/layers/hydrology/README.md) | Released public-safe Hydrology layer boundary |

## Open verification

- [ ] **NEEDS VERIFICATION** - assign semantic Hydrology, release, data, policy, evidence, and rollback stewards; CODEOWNERS supplies GitHub routing only.
- [ ] **NEEDS VERIFICATION** - accept a candidate ID and filename convention; this README's naming pattern is guidance only.
- [ ] **NEEDS VERIFICATION** - determine whether a dedicated release-candidate schema is required and, if so, place it through the contract/schema/ADR process rather than defining it here.
- [ ] **CONFLICTED / NEEDS VERIFICATION** - reconcile review-level promotion recommendations with the machine `APPROVE | DENY | ABSTAIN` enum.
- [ ] **CONFLICTED / NEEDS VERIFICATION** - establish the authority relationship between the common and Hydrology-specific `release_manifest` schema stubs.
- [ ] **NEEDS VERIFICATION** - resolve the release root's singular/plural manifest and correction lane conventions before creating parallel record homes.
- [ ] **NEEDS VERIFICATION** - verify validator implementation, fixtures, policy wiring, CI enforcement, branch protection, and required reviews for promotion and manifest objects.
- [ ] **UNKNOWN** - whether any populated Hydrology candidate dossier currently satisfies the full packet contract; this revision verified the lane README, not a complete candidate inventory.
- [ ] **UNKNOWN** - whether any Hydrology artifact has completed a governed public release; no such claim is made here.
- [ ] **NEEDS VERIFICATION** - decide whether family sublanes are needed after real candidate volume demonstrates a stable responsibility split.

## Maintenance and rollback

Update this README when candidate states, promotion-decision semantics, manifest authority, Hydrology source-role rules, temporal/freshness requirements, review burden, correction/rollback objects, or parent lane conventions change.

For a documentation-only correction:

1. restore or revert the prior README revision;
2. preserve the reason for correction in the commit or pull request;
3. re-run the same Markdown, link, metadata, and sensitivity checks;
4. update any generated receipt or index affected by the correction;
5. confirm no candidate, manifest, policy, or public release record relied on the withdrawn wording.

Reverting this README does not roll back a Hydrology release. Release rollback requires the governed release, correction, invalidation, and rollback records for the affected release.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-20 |
| Evidence snapshot | `main@2b31ccbd9ba5b3fe6772ea1b0165eca45bdfebb0` |
| Review status | Draft v2; expanded from compact lane guidance |
| Next review trigger | First complete Hydrology candidate dossier, candidate schema decision, promotion vocabulary reconciliation, manifest authority decision, or governed Hydrology release handoff |
