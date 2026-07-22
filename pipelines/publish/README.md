<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-publish-readme
title: Publish Pipeline README
type: readme
version: v0.2
status: draft
owners:
  - <pipeline-owner>
  - <publish-steward>
  - <release-steward>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-07-22
policy_label: public
path: pipelines/publish/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/release-discipline.md
  - docs/standards/RELEASE_MANIFEST.md
  - docs/adr/README.md
  - pipelines/README.md
  - pipelines/validate/README.md
  - pipelines/catalog/README.md
  - pipelines/triplets/README.md
  - pipelines/rollback/README.md
  - pipelines/publish/fauna/README.md
  - pipeline_specs/README.md
  - tests/pipelines/README.md
  - policy/release/README.md
  - data/catalog/README.md
  - data/triplets/README.md
  - data/receipts/pipeline/README.md
  - data/proofs/evidence_bundle/README.md
  - data/published/README.md
  - release/README.md
  - release/candidates/README.md
  - release/manifests/README.md
tags: [kfm, pipelines, publish, readiness, release, evidence, policy, review, trust-membrane, correction, rollback]
notes:
  - "This lane supports publish-readiness checks and release-authority handoff; it does not approve or perform publication."
  - "Directory Rules confirms pipelines/ as executable logic and pipeline_specs/ as declarative configuration."
  - "The current bounded repository snapshot does not establish shared publish executables, a target-specific test or fixture leaf, a declarative publish profile leaf, or canonical readiness receipt and reason-code schemas."
  - "Named implementation files and absent leaves are PROPOSED until created with accepted contracts, schemas, fixtures, tests, CI ownership, and review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Publish-readiness pipelines

> Shared executable-lane contract for checking whether release candidates have the evidence, validation, policy, review, integrity, correction, and rollback support needed for a release-authority decision. A readiness result is never publication.

![status](https://img.shields.io/badge/status-draft-blue)
![maturity](https://img.shields.io/badge/implementation-UNKNOWN-orange)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![authority](https://img.shields.io/badge/release%20authority-separate-d62728)
![posture](https://img.shields.io/badge/posture-fail%20closed-d62728)

**Path:** `pipelines/publish/README.md`  
**Responsibility root:** `pipelines/` - executable pipeline logic, the **how**  
**Lane role:** shared publish-readiness support  
**Document lifecycle:** DRAFT  
**Component maturity:** UNKNOWN  
**Public posture:** no direct public-serving, release-state, manifest, catalog, or artifact mutation

> [!IMPORTANT]
> This lane may check readiness and assemble a handoff. It must not approve release, author a final `ReleaseManifest`, perform the transition to `PUBLISHED`, create evidence or policy decisions, silently alter a candidate, or change a governed API, map, export, search index, cache binding, or other public surface as a side effect.

## Quick navigation

- [Purpose](#purpose)
- [Authority level](#authority-level)
- [Status and evidence boundary](#status-and-evidence-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Validation](#validation)
- [Review burden](#review-burden)
- [Related folders](#related-folders)
- [ADRs and placement decisions](#adrs-and-placement-decisions)
- [Correction and rollback](#correction-and-rollback)
- [Definition of done](#definition-of-done)
- [Last reviewed](#last-reviewed)

---

<a id="purpose"></a>

## Purpose

`pipelines/publish/` is the shared implementation lane for bounded publish-readiness work. It may help an authorized caller determine whether a release candidate is sufficiently closed for handoff to release authority.

The lane's responsibilities are to:

- resolve the exact candidate, artifact, catalog, triplet, source, evidence, validation, policy, review, and receipt references supplied by an authorized caller;
- verify that release-facing claims have admissible, resolvable evidence support;
- verify source-role, identity, rights, sensitivity, temporal, and public-representation closure;
- check content digests, dependency lineage, manifest inputs, correction paths, rollback targets, and trust-membrane constraints;
- return one finite readiness outcome with structured blockers and an auditable receipt or receipt fragment once canonical contracts exist;
- return control to release authority without changing release or public-serving state.

This directory describes the **how** of readiness checking. Declarative configuration belongs under `pipeline_specs/`; semantic meaning belongs under `contracts/`; machine shape belongs under `schemas/`; admissibility belongs under `policy/`; enforceability belongs under `tests/`; release decisions belong under `release/`; released artifacts belong under `data/published/`.

[Back to top](#top)

---

<a id="authority-level"></a>

## Authority level

**Implementation-lane documentation; readiness support only.**

| Question | Answer | Evidence status |
|---|---|---|
| Why is this under `pipelines/`? | Directory Rules assigns executable pipeline logic to `pipelines/` and explicitly lists `publish/` as a pipeline lane. | CONFIRMED |
| Does this directory own declarative publish configuration? | No. `pipeline_specs/` owns what should run. | CONFIRMED root split |
| Does a readiness result approve release? | No. Release authority and release records remain under `release/`. | CONFIRMED boundary |
| Does this lane own published artifacts? | No. Released public-safe artifacts belong under `data/published/`. | CONFIRMED boundary |
| Does this lane own evidence, policy, contracts, or schemas? | No. It consumes governed references from those responsibility roots. | CONFIRMED boundary |
| Does it replace domain pipelines? | No. Domain-owned executable behavior normally belongs under `pipelines/domains/<domain>/`. | CONFIRMED placement rule |
| Are shared publish executables currently proven here? | No executable depth was established by the bounded snapshot. | UNKNOWN |
| Can public clients call this directory or canonical stores directly? | No. Public clients use governed interfaces and released artifacts. | CONFIRMED trust-membrane rule |

### Authority boundaries

| Object or decision | This lane may | This lane must not |
|---|---|---|
| Release candidate | Resolve and inspect the pinned candidate. | Treat candidate status as `PUBLISHED` or silently mutate it. |
| `EvidenceRef` / `EvidenceBundle` | Resolve references and report closure. | Create, repair, or fabricate evidence to make a candidate pass. |
| `ValidationReport` | Verify applicable reports and result state. | Convert validation success into policy or release approval. |
| `PolicyDecision` | Require and consume an applicable decision. | Infer permission or author policy. |
| `ReviewRecord` | Verify required review state and role separation. | Self-approve a material or sensitive release. |
| Manifest inputs | Validate completeness, canonicalization, and digests. | Author or sign the final `ReleaseManifest` unless release authority explicitly owns that separate action. |
| Correction and rollback support | Verify routes, targets, invalidation scope, and lineage. | Execute correction, withdrawal, rollback, cache purge, or route rebinding as an undocumented side effect. |
| Public representation | Verify the referenced representation and transformation receipts. | Expose raw, quarantined, restricted, or over-precise material. |

### Non-authoritative equivalences

```text
readiness READY       != release approval
candidate             != PUBLISHED
EvidenceRef           != EvidenceBundle
ValidationReport      != PolicyDecision
PolicyDecision allow  != completed review
manifest input        != final ReleaseManifest
receipt               != proof of release
catalog/triplet       != canonical public truth
redacted candidate    != proven public-safe derivative
generated summary     != evidence
deployment or copy    != governed publication
```

[Back to top](#top)

---

<a id="status-and-evidence-boundary"></a>

## Status and evidence boundary

### Confirmed at the reviewed snapshot

- `pipelines/publish/README.md` exists under the canonical `pipelines/` implementation root.
- Directory Rules explicitly lists `pipelines/publish/` and distinguishes executable logic from declarative `pipeline_specs/` configuration.
- The lifecycle is `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`, and promotion is a governed state transition rather than a file move.
- `release/` owns release decisions; `data/published/` owns released public-safe artifacts.
- The repository contains the linked lifecycle, release-discipline, `ReleaseManifest`, pipeline-root, release-root, receipt, proof, catalog, triplet, published-data, and ADR guidance listed below.
- `pipelines/publish/fauna/README.md` exists as a documented domain adapter under this lane.

### Not established at the reviewed snapshot

- No shared publish executable named by the prior README's proposed tree was present.
- `pipeline_specs/publish/`, `tests/pipelines/publish/`, and `fixtures/publish/` were not present.
- No canonical shared publish-readiness receipt schema, blocker schema, or finite-outcome enum was confirmed.
- No exact CI job, runtime entrypoint, package import, release integration, or production receipt from this shared lane was confirmed.
- No target-specific accepted ADR was found that turns this directory into release authority or makes it the permanent home for full domain publish workflows.

> [!NOTE]
> The contracts below define the required posture for future implementation. They do not claim that executables, schemas, fixtures, tests, receipts, integrations, or release effects already exist.

### Lifecycle boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The shared publish lane begins only with an explicitly scoped candidate or approved synthetic fixture. It checks the support needed for the final transition and ends with a readiness handoff. Release authority remains responsible for the manifest, decision, proof closure, materialization, route binding, correction surface, rollback readiness, and final state change.

### Truth labels used in this README

| Label | Meaning here |
|---|---|
| CONFIRMED | Verified from the reviewed repository snapshot or supplied governing Directory Rules. |
| PROPOSED | A design or expansion pattern that is not yet verified in implementation. |
| UNKNOWN | Not established by the bounded inspection. |
| NEEDS VERIFICATION | Checkable, but not sufficiently resolved to adopt as repository fact. |

[Back to top](#top)

---

<a id="what-belongs-here"></a>

## What belongs here

Only shared executable publish-readiness logic or a narrowly documented adapter to that logic belongs here.

Appropriate future contents may include:

- fixture-only dry-run entrypoints with no network or public-serving side effects;
- candidate, evidence-closure, review-state, manifest-input, correction-path, rollback-target, and trust-membrane checkers;
- deterministic blocker and readiness-report builders;
- receipt emitters that implement an accepted contract and schema;
- shared adapters used by more than one domain or release workflow;
- documentation that defines the lane's bounded authority, inputs, outputs, failure posture, and handoff.

A placement test:

> If the code answers “how do multiple governed workflows check publish readiness without making the release decision?”, it may belong here. If it defines what runs, what an object means, what is allowed, what was released, or what a public client reads, it belongs in another responsibility root.

### Admission rule for new implementation

A new executable should not be added until its change also identifies:

1. the accepted semantic contract and machine schema it implements;
2. the declarative profile or caller contract that scopes the run;
3. public-safe valid, invalid, held, denied, and integrity-error fixtures;
4. deterministic no-network tests, including negative paths;
5. receipt ownership and canonicalization rules;
6. reviewer and CI ownership;
7. correction, invalidation, and rollback implications;
8. proof that it cannot approve release or mutate public state by itself.

[Back to top](#top)

---

<a id="what-does-not-belong-here"></a>

## What does not belong here

| Do not place here | Owning responsibility home |
|---|---|
| Full domain pipeline behavior | `pipelines/domains/<domain>/` unless an accepted placement decision says otherwise |
| Declarative profiles, schedules, source lists, or run scopes | `pipeline_specs/` |
| Object semantics | `contracts/` |
| Machine-readable shapes | `schemas/` |
| Allow, deny, restrict, redact, or abstain rules | `policy/` |
| Tests and executable proof | `tests/` |
| Golden, valid, invalid, or synthetic test inputs | `fixtures/` |
| Source descriptors, catalog state, triplets, receipts, proofs, or published data | Their governed `data/` lifecycle homes |
| EvidenceBundle creation or repair | Evidence-construction lanes and `data/proofs/evidence_bundle/` |
| Release decisions, manifests, promotion decisions, rollback cards, or correction notices | `release/` |
| Public API, UI, map, tile, export, or search-serving code | Governed application and package roots |
| Credentials, signing keys, real secrets, or unrestricted sensitive payloads | Approved secret/runtime systems; never this directory |

This directory must not become a parallel home for contracts, schemas, policy, receipts, proofs, release records, or published artifacts. Creating a parallel authority home requires an ADR and migration decision under Directory Rules.

[Back to top](#top)

---

<a id="inputs"></a>

## Inputs

All inputs must be pinned, resolvable, authorized for the requested check, and treated as read-only unless a separate owning workflow explicitly authorizes mutation.

| Input class | Minimum required information | Failure posture |
|---|---|---|
| Caller context | Authorized owner, purpose, requested release class, candidate scope, and profile or drill reference. | `HELD` when ownerless, ambiguous, or out of scope. |
| Release candidate | Stable candidate reference, lifecycle state, parent lineage, artifact references, and content digests. | `HELD` on missing, stale, or unresolvable closure. |
| Catalog and triplet closure | Stable catalog/triplet references, object identities, dependency lineage, and release-relevant claims. | `HELD` when closure or identity is ambiguous. |
| Source support | `SourceDescriptor` references, source roles, authority limits, rights, attribution, and freshness. | `HELD` or `DENIED` according to the governing decision. |
| Evidence support | Required `EvidenceRef` values and resolvable `EvidenceBundle` references for release-facing claims. | `HELD`; unsupported claims do not pass. |
| Validation support | Applicable validation reports, transform receipts, integrity results, and blocker state. | `HELD` for missing or failing results; `ERROR` for integrity failure. |
| Policy support | Applicable rights, sensitivity, exposure, redaction, aggregation, temporal, and release decision references. | `DENIED` or `HELD`; never infer permission. |
| Review support | Required `ReviewRecord` references, reviewer roles, signatures or attestations where required, and separation-of-duties state. | `HELD` when review is required but unresolved. |
| Public-safe representation | Digest-linked generalized, redacted, aggregated, delayed, restricted, or withheld representation plus its receipts. | `DENIED` for unsafe public exposure. |
| Manifest inputs | Hashable artifact set, release metadata, dependencies, public representation, proof pointers, and declared canonicalization profile. | `HELD` until complete and internally consistent. |
| Correction and rollback | Correction route, invalidation scope, prior release digest, rollback target, and downstream dependency posture. | `HELD` until resolvable and testable. |

### Source-role and evidence rules

- Discovery, aggregator, contextual, or corroborating sources must not be silently elevated to primary, legal-status, or regulatory authority.
- Conflicting source roles and authority limits remain visible and block unsupported claims.
- Every release-facing factual claim must resolve to admissible evidence or be removed, narrowed, generalized, restricted, or withheld.
- An `EvidenceRef` is a pointer, not the proof itself; the referenced `EvidenceBundle` must resolve and match the candidate scope.
- Generated text, classification, summarization, or confidence scores cannot replace evidence, policy, review, or release records.

### Identity, time, rights, and sensitivity rules

- Candidate, source, dataset, layer, evidence, artifact, and prior-release identities must be deterministic or use an accepted stable identifier.
- The check must distinguish event time, observation time, source publication time, ingestion time, effective time, and release time where relevant; one timestamp must not stand in for all temporal meanings.
- Unknown rights, sovereignty, consent, cultural sensitivity, living-person exposure, genomic data, rare-species locations, archaeology, infrastructure, or other restricted precision fail closed.
- A transformed representation is not public-safe merely because it is generalized or redacted; the transform, policy basis, reviewer state, and digest-linked output must be verifiable.

[Back to top](#top)

---

<a id="outputs"></a>

## Outputs

The lane may emit only non-authoritative readiness support:

- one finite readiness outcome;
- deterministic blocker or reason codes after a canonical vocabulary exists;
- a readiness report pinned to the exact candidate and evidence snapshot;
- a manifest-input package for release-authority review;
- an auditable receipt or receipt fragment with input, check, decision-reference, and output digests;
- a controlled handoff to the owning domain workflow or release steward.

### Proposed finite readiness outcomes

This vocabulary is **PROPOSED** for documentation and testing. It is not a confirmed schema enum.

| Outcome | Meaning | Permitted next step |
|---|---|---|
| `READY` | Every required check for the bounded readiness scope completed with resolvable support. | Hand off to release authority; do not publish. |
| `HELD` | Evidence, identity, time, rights, sensitivity, validation, review, manifest input, correction, rollback, or another required dependency is incomplete or unresolved. | Supply or correct support, then rerun. |
| `DENIED` | Governing policy, rights, sensitivity, sovereignty, consent, or exposure rules prohibit the requested representation or operation. | Stop; use only an authorized alternative scope or representation. |
| `ERROR` | The checker could not determine readiness because of parsing, dependency, integrity, configuration, or system failure. | Preserve non-sensitive diagnostics and rerun after repair. |

`READY` means only “ready for release-authority review within this checker's declared scope.” It must never trigger the final manifest, promotion, publication, route binding, cache invalidation, or public artifact write by itself.

### Proposed blocker families

The repository release-discipline document describes machine-readable failure families, but its specific strings remain proposed pending confirmation from accepted policy and schemas. Future implementation should use a canonical registry rather than inventing local free-text errors.

| Family | Example proposed codes | Expected posture |
|---|---|---|
| Missing support | `MISSING_RECEIPT`, `MISSING_EVIDENCE`, `MISSING_REVIEW` | `HELD` |
| Contract or schema drift | `SCHEMA_MISMATCH`, `CONTRACT_DRIFT` | `HELD` or `ERROR` |
| Rights or sensitivity | `RIGHTS_UNKNOWN`, `SENSITIVITY_UNRESOLVED` | `HELD` or `DENIED` |
| Source-role integrity | `ROLE_COLLAPSE`, `ROLE_DOWNCAST_FORBIDDEN` | `HELD` or `DENIED` |
| Review state | `REVIEW_NEEDED`, `REVIEW_INSUFFICIENT`, `REVIEW_REJECTED` | `HELD` or `DENIED` |
| Release integrity | `RELEASE_MANIFEST_INVALID`, `ROLLBACK_TARGET_MISSING` | `HELD` or `ERROR` |
| Correction lineage | `CORRECTION_DERIVATIVES_UNRESOLVED`, `CORRECTION_PRIOR_RELEASE_MISSING` | `HELD` |

### Prohibited outputs and side effects

This lane must not emit or mutate, as a direct readiness side effect:

- a final or signed `ReleaseManifest`;
- a `PromotionDecision`, `CorrectionNotice`, `RollbackCard`, or withdrawal decision;
- a new or repaired `EvidenceBundle` or `PolicyDecision`;
- a public layer, tile set, API payload, report, story, search document, route binding, or cache purge;
- a silent candidate rewrite, release alias change, catalog release-state change, or deletion of prior history.

### Minimal readiness receipt

The following shape is **PROPOSED** and must not be treated as a canonical contract or schema:

```yaml
schema_version: PROPOSED.kfm.publish_readiness_receipt.v1
run_id: publish_readiness_<stable-id>
checker_id: publish.<profile-id>
outcome: HELD
scope:
  caller_ref: <stable-ref>
  profile_ref: <stable-ref-or-null>
  candidate_ref: <stable-ref>
  candidate_digest: <sha256>
inputs:
  catalog_refs: []
  triplet_refs: []
  source_descriptor_refs: []
  evidence_bundle_refs: []
  validation_report_refs: []
  policy_decision_refs: []
  review_record_refs: []
  artifact_refs: []
checks:
  identity_closed: false
  evidence_closed: false
  source_roles_closed: false
  rights_sensitivity_closed: false
  validation_closed: false
  review_closed: false
  manifest_inputs_closed: false
  correction_path_closed: false
  rollback_target_closed: false
  trust_membrane_preserved: false
reason_codes: []
outputs:
  readiness_report_ref: null
  manifest_input_ref: null
  receipt_ref: null
integrity:
  canonicalization_profile: <accepted-profile-or-null>
  receipt_digest: <sha256-or-null>
side_effects:
  release_state_changed: false
  public_surface_changed: false
```

[Back to top](#top)

---

<a id="validation"></a>

## Validation

### Required readiness gates

Future executable behavior must fail closed across every applicable gate:

1. **Caller and scope** - owner, purpose, profile, domain, release class, and candidate are explicit.
2. **Lifecycle** - the candidate is at the accepted pre-publication state and has not bypassed RAW, WORK/QUARANTINE, PROCESSED, CATALOG/TRIPLET, or required remediation.
3. **Identity and lineage** - stable identities, parentage, dependencies, and digests resolve without collision or ambiguity.
4. **Source role and evidence** - source authority is not collapsed, and every release-facing claim has resolvable `EvidenceBundle` support.
5. **Catalog and triplet closure** - catalog and relationship projections resolve without becoming substitute canonical truth.
6. **Validation and receipts** - applicable validation, transform, redaction, aggregation, model, and pipeline receipts resolve and agree with the candidate digest.
7. **Policy, rights, and sensitivity** - applicable decisions are present, current, scoped, and fail closed on uncertainty.
8. **Review and duty separation** - required reviewers and materiality-sensitive role separation are satisfied.
9. **Artifact integrity** - artifact set, dependency graph, hashes, canonicalization, and public-representation references close.
10. **Manifest input** - required release metadata, proof pointers, correction path, rollback target, and release scope are complete.
11. **Trust membrane** - public consumers would receive only governed, released, public-safe representations through governed interfaces.
12. **Correction and rollback** - correction route, derivative invalidation scope, prior release digest, and rehearsable rollback target resolve.
13. **Receipt** - the check produces deterministic, non-secret audit metadata with structured outcomes and blockers.
14. **No direct release** - the run makes no release decision and changes no public or release state.

### Proposed test burden

No target-specific test leaf was confirmed. When implementation begins, tests should cover at least:

- no-network deterministic dry runs;
- exact candidate and digest pinning;
- all four proposed finite outcomes;
- ownerless and out-of-scope callers;
- missing, stale, contradictory, and wrong-scope evidence;
- source-role collapse and authority upcast attempts;
- identity collision, temporal ambiguity, and dependency drift;
- missing or failing validation, receipt, policy, and review support;
- unknown rights and sensitivity, restricted precision, and unsafe public representations;
- incomplete manifest inputs, missing correction routes, and missing rollback targets;
- deterministic receipt canonicalization and replay;
- proof that no final manifest, release decision, published artifact, route, alias, or cache state changes;
- correction or withdrawal invalidation of stale `READY` results.

### Fixture burden

Future fixtures should be synthetic or demonstrably public-safe and include:

- one minimal valid candidate;
- one case for every `HELD` dependency family;
- one policy or rights `DENIED` case;
- one integrity or dependency `ERROR` case;
- one sensitive or precision-limited candidate whose only safe result is restricted, generalized, delayed, or withheld;
- one correction and rollback lineage case;
- expected outcome, blocker codes, and receipt digest for every fixture.

Fixtures must not contain credentials, signing keys, living-person details, protected locations, unreleased coordinates, raw restricted payloads, or data whose reuse rights are unresolved.

### CI ownership

Exact CI ownership is **UNKNOWN**. A future change must identify the command-bearing workflow and required checks before claiming enforcement. Documentation alone is not proof that a gate runs.

[Back to top](#top)

---

<a id="review-burden"></a>

## Review burden

### Documentation changes

At minimum, changes to this README should receive:

- pipeline-owner or publish-steward review for executable-lane scope;
- release-steward review for release-authority separation and handoff semantics;
- docs-steward review for placement, truth labels, links, and lifecycle terminology;
- evidence, policy, rights, sensitivity, security, or domain-steward review when the change alters those boundaries.

### Future implementation changes

| Change class | Minimum review posture |
|---|---|
| Shared checker or receipt behavior | Pipeline owner plus contract/schema owner and test owner |
| Release-input or manifest-input behavior | Pipeline owner plus release steward |
| Evidence or source-role logic | Evidence steward plus applicable domain/source steward |
| Rights, sensitivity, sovereignty, consent, or public representation | Policy/rights/sensitivity reviewer plus applicable domain steward |
| Signing, attestations, content addressing, or dependency integrity | Release steward plus security/supply-chain reviewer |
| Correction, invalidation, withdrawal, rollback, or public route implications | Correction reviewer plus release authority and affected surface owner |

### Separation of duties

- A checker author may validate deterministic behavior, but must not use that authorship to self-approve a material release.
- When materiality applies, release author and release authority remain separate.
- Sensitive-lane release requires the role combination defined by governing policy and release doctrine; this shared lane only verifies the supplied review state.
- Correction or rollback of a steward-significant release requires a detector or author, correction reviewer, and release authority as applicable.
- A missing reviewer cannot be replaced by a generated summary, green CI status, or checker `READY` result.

[Back to top](#top)

---

<a id="related-folders"></a>

## Related folders

All links below were present at the reviewed snapshot.

### Governing doctrine and architecture

- [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) - placement authority and `pipelines/` / `pipeline_specs/` split.
- [`docs/doctrine/lifecycle-law.md`](../../docs/doctrine/lifecycle-law.md) - lifecycle and governed transition contract.
- [`docs/architecture/release-discipline.md`](../../docs/architecture/release-discipline.md) - release gates, reason-code posture, duty separation, correction, and rollback.
- [`docs/standards/RELEASE_MANIFEST.md`](../../docs/standards/RELEASE_MANIFEST.md) - manifest identity, integrity, lifecycle, correction, and rollback guidance.
- [`docs/adr/README.md`](../../docs/adr/README.md) - accepted-decision and placement review index.

### Executable and declarative lanes

- [`pipelines/README.md`](../README.md) - executable pipeline root contract.
- [`pipelines/validate/README.md`](../validate/README.md) - shared validation boundary.
- [`pipelines/catalog/README.md`](../catalog/README.md) - catalog-closure pipeline guidance.
- [`pipelines/triplets/README.md`](../triplets/README.md) - relationship projection guidance.
- [`pipelines/rollback/README.md`](../rollback/README.md) - rollback-readiness boundary.
- [`pipelines/publish/fauna/README.md`](fauna/README.md) - existing thin Fauna readiness adapter documentation.
- [`pipeline_specs/README.md`](../../pipeline_specs/README.md) - declarative pipeline specification root; no `publish/` leaf was confirmed.

### Tests, policy, lifecycle data, and release authority

- [`tests/pipelines/README.md`](../../tests/pipelines/README.md) - pipeline behavior test boundary; no target-specific `publish/` leaf was confirmed.
- [`policy/release/README.md`](../../policy/release/README.md) - present release-policy leaf; current depth is minimal and should not be overstated.
- [`data/catalog/README.md`](../../data/catalog/README.md) - catalog lifecycle home.
- [`data/triplets/README.md`](../../data/triplets/README.md) - triplet lifecycle home.
- [`data/receipts/pipeline/README.md`](../../data/receipts/pipeline/README.md) - pipeline receipt home.
- [`data/proofs/evidence_bundle/README.md`](../../data/proofs/evidence_bundle/README.md) - EvidenceBundle proof home.
- [`data/published/README.md`](../../data/published/README.md) - released public-safe artifact home.
- [`release/README.md`](../../release/README.md) - release decision authority.
- [`release/candidates/README.md`](../../release/candidates/README.md) - release candidate review index.
- [`release/manifests/README.md`](../../release/manifests/README.md) - final manifest collection lane.

### Confirmed and proposed directory shape

```text
pipelines/publish/
├── README.md          # CONFIRMED: this shared lane contract
├── fauna/
│   └── README.md      # CONFIRMED: thin adapter documentation
└── <implementation>   # PROPOSED only after contract, schema, fixture, test, CI, and review closure
```

The earlier README's named shared contract and executable files were not present at the reviewed snapshot. Do not copy that prospective tree into implementation without re-verifying placement and satisfying the admission rule in this document.

[Back to top](#top)

---

<a id="adrs-and-placement-decisions"></a>

## ADRs and placement decisions

The bounded inspection did not establish a target-specific accepted ADR that grants this directory release authority, creates a parallel receipt/contract/schema/policy home, or makes `pipelines/publish/<domain>/` the default home for full domain workflows.

Current decision posture:

- `pipelines/publish/` is a confirmed shared executable lane under Directory Rules.
- `pipeline_specs/` remains the confirmed declarative configuration root.
- `pipelines/domains/<domain>/` remains the normal home for domain-owned executable behavior.
- `pipelines/publish/fauna/` may remain a thin adapter while its scope stays subordinate to shared readiness and the primary domain lane.
- expansion into release decisions, a parallel authority root, or full domain ownership requires a placement review and may require an ADR or migration record.

### Open decisions

| ID | Question | Status | Resolution evidence needed |
|---|---|---|---|
| `PIPE-PUBLISH-001` | What accepted contract and schema own shared readiness outcomes, blockers, and receipts? | UNKNOWN | Contract, schema, validator, fixtures, compatibility policy, and accepted owner |
| `PIPE-PUBLISH-002` | What exact declarative profile path scopes shared publish-readiness runs? | NEEDS VERIFICATION | `pipeline_specs/` placement decision and accepted profile schema |
| `PIPE-PUBLISH-003` | Where should target-specific tests and fixtures live? | NEEDS VERIFICATION | Current tree review, owning README updates, and test/fixture owners |
| `PIPE-PUBLISH-004` | Which CI job proves shared publish invariants? | UNKNOWN | Command-bearing workflow and required-check decision |
| `PIPE-PUBLISH-005` | Which reason-code and finite-outcome vocabulary is canonical? | UNKNOWN | Accepted policy/contract/schema registry and negative tests |
| `PIPE-PUBLISH-006` | Which shared helpers are reusable enough for this lane rather than a package or domain pipeline? | NEEDS VERIFICATION | First implementation slice, call sites, ownership, and placement review |
| `PIPE-PUBLISH-007` | How are readiness receipts canonicalized, content-addressed, superseded, and invalidated? | UNKNOWN | Hash profile, receipt contract, replay tests, and correction semantics |
| `PIPE-PUBLISH-008` | May domain adapters remain under `pipelines/publish/`, or should executable domain behavior move to `pipelines/domains/<domain>/`? | NEEDS VERIFICATION / ADR review | Accepted placement decision and migration plan if moved |

[Back to top](#top)

---

<a id="correction-and-rollback"></a>

## Correction and rollback

### Documentation correction

If this README overstates implementation, links to a moved authority, or misstates a trust boundary:

1. open a focused correction change;
2. identify the unsupported claim and the pinned evidence that corrects it;
3. update version, review date, related links, truth labels, and open decisions;
4. preserve supersession or migration lineage where applicable;
5. re-run structure, link, sensitivity, and no-loss checks.

Before merge, repository rollback is closure of the unmerged PR or a transparent replacement commit. After merge, use a revert commit or revert PR; do not rewrite shared history.

### Readiness-result invalidation

Future implementations must invalidate or supersede a prior `READY` result when any pinned dependency changes materially, including:

- candidate, artifact, catalog, triplet, evidence, policy, validation, review, or manifest-input digest;
- source role, rights, sensitivity, identity, temporal, or public-representation decision;
- correction, withdrawal, supersession, or downstream invalidation notice;
- canonicalization profile, checker version, contract, schema, or policy bundle;
- rollback target or prior-release integrity.

A stale readiness receipt must remain auditable but must not be reused as current authorization.

### Release correction and rollback boundary

This lane may verify that a correction path and rollback target exist. The owning release workflow must still create and review the required release records, identify affected derivatives, validate inverse changes, update or supersede the manifest, and rebind or invalidate public surfaces. No history is silently edited or deleted merely to make the current state look clean.

Future readiness logic is incomplete until it can prove:

- the exact prior release digest and last known-good public representation;
- the complete downstream derivative and cache-invalidation scope;
- the correction or rollback record references and required reviewer state;
- that restored or corrected artifacts still pass evidence, policy, rights, sensitivity, integrity, and trust-membrane gates;
- that a failed rollback rehearsal returns `HELD` or `ERROR`, never `READY`.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This README revision is complete when it:

- states the confirmed placement of `pipelines/publish/` without granting it release authority;
- distinguishes confirmed repository paths from proposed executables, profiles, tests, fixtures, schemas, and integrations;
- preserves the lifecycle and the separation among candidate, catalog/triplet, evidence, validation, policy, review, manifest, release decision, published artifact, correction, rollback, receipt, and public serving;
- defines inputs, bounded outputs, finite fail-closed outcomes, validation gates, review burden, and prohibited side effects;
- links only to repository paths confirmed at the reviewed snapshot;
- records open contract, schema, profile, test, fixture, CI, reason-code, canonicalization, and placement decisions;
- introduces no sensitive payload, credential, signing key, release mutation, or public behavior change.

Future executable work is done only when accepted contracts and schemas, scoped declarative configuration, public-safe fixtures, deterministic positive and negative tests, canonical receipts, CI ownership, role-separated review, correction invalidation, rollback rehearsal, and remote verification all exist and pass.

[Back to top](#top)

---

<a id="last-reviewed"></a>

## Last reviewed

| Field | Value |
|---|---|
| Date | 2026-07-22 |
| Document version | v0.2 |
| Status | DRAFT |
| Repository evidence base | `main` at `6930e2ed29bc45a55f36c4f17c393a754153aec7` |
| Placement basis | Directory Rules §§4, 7.4, 9, 12, 15, and 16 |
| Implementation depth | UNKNOWN |
| Release/publication impact | None; documentation-only readiness contract |
| Next review trigger | First shared executable, accepted contract/schema, declarative profile, test/fixture leaf, CI owner, adapter placement decision, or material release-policy change |

### Maintenance checklist

- [ ] Confirm owner and steward placeholders.
- [ ] Re-check accepted ADRs and drift entries before adding or moving implementation.
- [ ] Confirm the canonical contract, schema, outcome, blocker, and receipt vocabularies.
- [ ] Confirm the declarative profile, test, fixture, and CI ownership paths.
- [ ] Keep rights and sensitivity uncertainty fail closed and test every negative path.
- [ ] Verify every related link and implementation claim at the next pinned commit.
- [ ] Invalidate stale readiness results after material dependency or policy changes.
- [ ] Update this README when behavior, validation, review, correction, rollback, or public-surface responsibilities change.

[Back to top](#top)
