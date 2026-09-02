<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-people-readme
title: release/candidates/people/ — People Candidate Compatibility Lane
version: v2
status: draft
policy_label: public
owners:
  - <people-domain-steward>
  - <release-steward>
  - <data-steward>
  - <policy-privacy-reviewer>
updated: 2026-07-20
tags: [kfm, release, candidates, people, people-dna-land, compatibility, pre-publication, privacy, sensitivity, review, validation, correction, rollback]
[/KFM_META_BLOCK_V2] -->

# `release/candidates/people/` — People Candidate Compatibility Lane

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![class](https://img.shields.io/badge/class-compatibility-orange)
![canonical lane](https://img.shields.io/badge/canonical-people--dna--land-purple)
![publication](https://img.shields.io/badge/publication-not_yet-orange)
![posture](https://img.shields.io/badge/default-fail_closed-red)

> [!CAUTION]
> **This is a compatibility and navigation lane, not the canonical People domain lane.** Current Directory Rules and the Domain Placement Law use `people-dna-land` as the canonical compound domain segment. Place new People, genealogy, DNA, or land candidate dossiers under [`release/candidates/people-dna-land/`](../people-dna-land/README.md). Do not create or advance a second release authority under `people/`.

> [!IMPORTANT]
> **A candidate is not a release.** A file, commit, pull request, merge, passing check, generated manifest, map layer, export, or AI summary does not publish KFM material. Publication remains a governed state transition supported by separate evidence, policy, validation, review, manifest, correction, and rollback objects.

## Quick jump

[Purpose](#purpose) · [Status and evidence boundary](#status-and-evidence-boundary) · [Repository fit](#repository-fit) · [Compatibility contract](#compatibility-contract) · [Candidate boundaries](#candidate-boundaries) · [People review posture](#people-review-posture) · [Candidate lifecycle](#candidate-lifecycle) · [Dossier contract](#candidate-dossier-contract) · [Review gates](#review-gates) · [Decision vocabulary](#decision-vocabulary) · [Manifest handoff](#manifest-handoff) · [Illustrative dossier](#illustrative-candidate-dossier) · [Verification](#verification-checklist) · [Open items](#open-verification-items) · [Rollback](#rollback)

## Purpose

This directory preserves discoverability for older or short-name references to a People release-candidate lane while routing current work into the canonical People / Genealogy / DNA / Land bounded context.

It may contain only:

- this compatibility README;
- migration or supersession pointers approved by repository governance;
- safe indexes that point to canonical candidate dossiers without copying their contents; and
- temporary, non-authoritative notes required to retire a legacy reference.

It must not become a second place to assemble, approve, manifest, or publish People candidates.

The lifecycle boundary remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Candidate review occurs before `PUBLISHED`. Promotion is a governed state transition, not a file move.

## Status and evidence boundary

| Field | Current finding |
|---|---|
| Document lifecycle | `draft` |
| Owning responsibility root | `release/` |
| Path class | Compatibility/index lane; no independent release authority |
| Canonical compound domain segment | `people-dna-land` |
| Canonical candidate lane | [`release/candidates/people-dna-land/`](../people-dna-land/README.md) |
| GitHub review route | [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) routes `release/` to `@bartytime4life`; this is review routing, not proof of semantic ownership, independent approval, or release authority. |
| Semantic owners in the meta block | `NEEDS VERIFICATION`; the role placeholders predate this revision and are not verified GitHub identities. |
| Candidate inventory in this lane | `UNKNOWN`; the scoped inspection established this README, not a complete tree or a governed candidate dossier. |
| Policy implementation | `NEEDS VERIFICATION`; inspected living-person and ambiguous-evidence policy files are `PROPOSED` scaffolds, not demonstrated enforcement. |
| Release-manifest enforcement | `NEEDS VERIFICATION`; the inspected common release-manifest schema describes itself as a thin `PROPOSED` stub. |
| Public effect of this README | None; it is guidance and a compatibility boundary, not a `PromotionDecision`, `ReleaseManifest`, policy decision, proof, or publication record. |

Repository facts above are bounded to the pinned evidence commit recorded in the implementing pull request and generated receipt. Repository-relative links improve maintainability; they do not upgrade draft documents, schemas, policies, runbooks, or workflows into verified runtime behavior.

## Repository fit

```text
release/
├── candidates/
│   ├── people/                  # compatibility/index lane; you are here
│   └── people-dna-land/         # canonical compound-domain candidate lane
├── promotion_decisions/         # PromotionDecision records
├── manifests/                   # ReleaseManifest records
├── rollback_cards/              # rollback records
└── correction_notices/          # correction records
```

The [Directory Rules](../../../docs/doctrine/directory-rules.md) assign candidate dossiers to `release/candidates/<domain>/` and keep release decisions separate from released artifacts in `data/published/`. The [Domain Placement Law](../../../docs/architecture/domain-placement-law.md) identifies `people-dna-land` as the canonical filesystem segment and treats the shorter atlas form `people` as lineage pending reconciliation.

Accordingly, this existing short-name path is retained only as a compatibility boundary. This README does not rename or remove the directory, declare a migration complete, create an alias recognized by tooling, or supersede the canonical lane.

### Authority map

| Concern | Owning surface | Relationship to this README |
|---|---|---|
| Canonical People candidate dossier | [`release/candidates/people-dna-land/`](../people-dna-land/README.md) | Create and review the dossier there. |
| Candidate-parent guidance | [`release/candidates/`](../README.md) | Supplies the shared candidate status and review vocabulary. |
| Release-root guidance | [`release/`](../../README.md) | Defines the release-governance boundary. |
| Final transition decision | [`release/promotion_decisions/`](../../promotion_decisions/README.md) and [`PromotionDecision`](../../../contracts/release/promotion_decision.md) | Referenced by a canonical dossier; never replaced by a README status. |
| Release binding | [`release/manifests/`](../../manifests/README.md) and [`ReleaseManifest`](../../../contracts/release/release_manifest.md) | Prepared after an approved transition; a candidate does not self-manifest. |
| Correction and rollback | [`release/correction_notices/`](../../correction_notices/README.md), [`release/rollback_cards/`](../../rollback_cards/README.md), and [`CorrectionNotice`](../../../contracts/correction/correction_notice.md) | Must be reachable for a material release; not stored here. |
| People-domain meaning | [`docs/domains/people-dna-land/people.md`](../../../docs/domains/people-dna-land/people.md) | Human-facing domain meaning and bounded-context guidance. |
| Sensitivity and release posture | [`SENSITIVITY.md`](../../../docs/domains/people-dna-land/SENSITIVITY.md) and [`RELEASE_INDEX.md`](../../../docs/domains/people-dna-land/RELEASE_INDEX.md) | Governing guidance; implementation maturity remains separately verified. |
| Evidence closure | [`EvidenceBundle`](../../../contracts/evidence/evidence_bundle.md) and proof objects under `data/proofs/` | A dossier resolves evidence; this README is not evidence. |
| Machine shape | `schemas/` | Schema authority stays outside this lane. |
| Admissibility | `policy/` | Policy authority stays outside this lane. |
| Lifecycle payloads | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/` | Payloads never belong in this directory. |
| Generated-work provenance | [`data/receipts/generated/`](../../../data/receipts/generated/README.md) | Records AI authorship; a generated receipt is process memory, not release evidence. |

No path or example in this README authorizes a parallel schema, contract, policy, registry, receipt, proof, release, catalog, or public-data home.

## Compatibility contract

### Required behavior

- Treat `people/` as a short-name compatibility surface only.
- Route every new candidate dossier to `../people-dna-land/` unless an accepted ADR and migration plan change the canonical domain identity.
- Keep legacy references intact long enough to identify and migrate their consumers.
- Use repository-relative links rather than duplicating canonical candidate material.
- Mark any legacy dossier discovered here `HOLD` for placement review before further mutation.
- Preserve history through an explicit migration, supersession, or deprecation record; do not silently rewrite identity.
- Keep this lane non-publishing and free of sensitive payloads.

### Prohibited behavior

- Do not create new dossier subdirectories under `people/`.
- Do not mirror a canonical dossier and allow both copies to evolve.
- Do not infer that `people/` and `people-dna-land/` are interchangeable in schemas, policy packages, object identifiers, source registries, or runtime routes.
- Do not copy, link publicly to, or summarize private living-person, family, address, DNA, consent, or person-to-parcel content here.
- Do not use compatibility language to bypass rights, sensitivity, consent, review, or release gates.
- Do not delete or redirect the path until inbound references, generated consumers, and rollback implications have been checked.

### Reconciliation state

The existence of both `release/candidates/people/` and `release/candidates/people-dna-land/` is a placement conflict, not proof that KFM has two People domains. Current doctrine chooses `people-dna-land`; removal or migration of the short path remains `NEEDS VERIFICATION` because this revision does not establish a complete inbound-reference inventory, accepted migration ADR, deprecation window, or rollback manifest.

## Candidate boundaries

### What belongs in the canonical People dossier

The canonical dossier may record public-safe review metadata for a specific proposed release, including:

- stable candidate identity, version, domain, and immutable build or run reference;
- bounded subject scope, geography, time window, and intended release surface;
- source roles and admitted source-descriptor references;
- resolvable `EvidenceRef` to `EvidenceBundle` closure;
- validation reports and safe receipt references;
- rights, attribution, consent, privacy, sensitivity, and public-surface findings;
- transformations such as redaction, aggregation, generalization, or withholding, with receipts where required;
- reviewer roles, conflicts, holds, and separation-of-duties status;
- proposed release target and manifest-handoff status;
- correction, invalidation, supersession, withdrawal, and rollback readiness; and
- an evidence-grounded `APPROVE`, `DENY`, or `ABSTAIN` promotion decision reference when one exists.

### What belongs nowhere in either candidate lane

- raw, work, quarantine, processed, catalog, triplet, or published payloads;
- secrets, credentials, private endpoints, or access tokens;
- direct identifiers for living people, private addresses, private family records, private holdings, exact person-to-parcel joins, raw DNA segments, kit identifiers, consent tokens, or restricted source content;
- source descriptors, schemas, contracts, policy modules, validators, pipelines, connectors, proofs, receipts, or manifests as embedded copies;
- unsupported identity merges, family relationships, residence claims, title conclusions, or legal advice;
- a floating `latest` pointer without immutable identity and correction lineage;
- generated language, map tiles, dashboards, search indexes, graph projections, or screenshots used as sovereign evidence; or
- final release approval or a public artifact.

## People review posture

People candidates are unusually sensitive because identity, time, kinship, location, consent, DNA, and land context can combine into a more revealing claim than any field carries alone.

### Fail-closed safeguards

| Condition | Required posture |
|---|---|
| Living-person status is true, possible, conflicting, or unknown | `DENY` or `ABSTAIN`; preserve the prior state and route to sensitivity review. |
| Evidence cannot resolve to an applicable `EvidenceBundle` | `ABSTAIN`; generated text must not fill the gap. |
| Rights, license, attribution, sovereignty, consent, or source terms are unresolved | `DENY` or `HOLD`; do not prepare a public handoff. |
| Raw DNA, kit identifiers, genomic segments, or private match data are present | `DENY` for public release; named restricted access still requires explicit policy, consent, and review authority. |
| A person-to-parcel join could reveal a private person, address, holding, or precise location | `DENY` unless a reviewed, receipted public-safe transform is explicitly allowed. |
| Identity resolution or kinship confidence is insufficient | `ABSTAIN`; preserve competing assertions and uncertainty. |
| A source role is missing or collapsed | `REPAIR_REQUIRED`; do not turn context, administrative data, or a model into primary proof. |
| Required validation, review, correction, or rollback support is missing | `DENY`, `ABSTAIN`, or `HOLD`; a green check on unrelated shape validation is insufficient. |
| Policy or consent evaluation cannot run | Fail closed; do not return a partial public answer or promote the candidate. |

The inspected [`living_person.rego`](../../../policy/domains/people-dna-land/living_person.rego) file defaults `allow` to false but identifies itself as a proposed scaffold. The inspected [`abstain_on_ambiguous.rego`](../../../policy/domains/people-dna-land/abstain_on_ambiguous.rego) file also identifies itself as a greenfield stub with no operative rule body. Their presence supports a conservative documentation posture; it does not prove runtime enforcement.

### Evidence and source-role discipline

- A source record proves only what that source is competent to assert.
- Administrative, contextual, modeled, corroborating, and primary roles must not collapse.
- An index entry, search result, OCR transcript, family tree, assessor record, geocoder result, or AI extraction is not automatically identity or relationship truth.
- Conflicting name, date, place, kinship, or residence assertions remain separate until the applicable resolution policy and evidence support a bounded conclusion.
- A bare citation is not evidence closure. Consequential claims must resolve to an applicable `EvidenceBundle` with source identity, scope, provenance, and integrity.
- Evidence about a well-deceased historical person does not authorize the release of living relatives, private addresses, raw DNA, or private land associations.

### Identity and time

Every canonical dossier should state which identity and time assertions it contains and which it explicitly excludes.

At minimum, record:

- stable candidate and dataset identifiers;
- subject-identity strategy and unresolved collisions;
- geography version and spatial precision;
- valid time for the claim;
- observed or source-record time;
- retrieval time;
- candidate-build time;
- proposed release time, if known; and
- correction or supersession time, when applicable.

Do not infer that a person is deceased from record age alone, that an address is a residence, that a relationship is biological, or that a historical location remains current. If the time basis is insufficient, use `ABSTAIN` or narrow the claim.

## Candidate lifecycle

The shared parent lane currently documents these candidate statuses. They are workflow labels, not public-release authority:

| Candidate status | Meaning in a canonical dossier |
|---|---|
| `PROPOSED` | Candidate has been identified but is not ready for assembly or review. |
| `ASSEMBLING` | Evidence, validation, rights, sensitivity, and rollback material are being gathered. |
| `READY_FOR_REVIEW` | The dossier is complete enough for the named reviewers to evaluate. |
| `APPROVED_FOR_MANIFEST` | A governed decision permits manifest preparation; this is still not publication. |
| `PROMOTED` | A separately governed release path records the transition; verify the manifest and public artifact rather than relying on this label. |
| `DEFERRED` | Work is intentionally paused without declaring the candidate invalid. |
| `REPAIR_REQUIRED` | A named defect must be corrected before review continues. |
| `BLOCKED` | A policy, rights, sensitivity, evidence, implementation, or authority blocker prevents progress. |
| `WITHDRAWN` | Candidate has been removed from consideration while preserving audit history. |
| `SUPERSEDED` | A newer candidate replaces this candidate through explicit lineage. |

Discovery of a new or active dossier under this compatibility path should produce a placement `HOLD` and a migration review, not automatic status advancement.

## Candidate dossier contract

A People-only candidate remains part of the canonical `people-dna-land` bounded context. Its dossier should answer every field below or explicitly record `UNKNOWN`, `NEEDS VERIFICATION`, or a blocking reason.

| Field | Required content |
|---|---|
| Candidate identity | Stable candidate ID, version, domain `people-dna-land`, and immutable run/build reference |
| Scope | Included object classes, excluded object classes, geography, time interval, population, and intended public surface |
| Artifact pointer | Immutable pointer to the candidate artifact in its owning lifecycle path; never the payload itself |
| Proposed target | Exact proposed released artifact family; no floating `latest` alias |
| Source closure | Source descriptor references, source roles, retrieval context, rights, and attribution |
| Evidence closure | `EvidenceRef` plus resolvable `EvidenceBundle`, claim scope, integrity digest, and citation-validation state |
| Identity and time | Identity strategy, unresolved conflicts, geography version, valid/source/retrieval/build/release/correction times |
| Sensitivity | Living-person, relationship, location, DNA, land, aggregation, re-identification, and combination-risk findings |
| Consent and rights | Whether consent applies, how its authority and revocation state are checked, and every unresolved obligation |
| Transform receipts | Redaction, aggregation, generalization, withholding, or other public-safe transformation references |
| Validation | Schema, semantic, evidence, temporal, spatial, privacy, sensitivity, policy, and negative-test results |
| Review | Author, reviewer roles, independence requirement, conflicts, ticket or review record, and current disposition |
| Manifest handoff | `PromotionDecision` reference, manifest-readiness state, exact blockers, and intended manifest family |
| Correction and rollback | Correction path, invalidation targets, rollback target, supersession link, and safe prior state |

### Source and evidence closure

Before a dossier can be `READY_FOR_REVIEW`, it should demonstrate that:

1. every source is admitted and identified at an immutable version;
2. source roles remain explicit and appropriate to each claim;
3. every consequential `EvidenceRef` resolves to the intended `EvidenceBundle`;
4. the bundle scope matches the candidate's identity, geography, time, and object class;
5. rights and attribution are current for the proposed use;
6. checksums and deterministic identifiers match the reviewed artifacts; and
7. unresolved or conflicting claims remain visible rather than being silently merged.

### Sensitive-data safeguards

Before any manifest handoff, reviewers should verify:

- living-person detection and uncertain-life-status handling;
- direct and indirect identifier removal;
- combination and re-identification risk;
- DNA/genomic exclusion or explicitly authorized restricted posture;
- consent scope, audience, expiry, revocation, and fail-closed behavior where consent applies;
- address, residence, household, family, and person-to-parcel exposure;
- minimum aggregation, generalization, and suppression thresholds;
- absence of sensitive values in filenames, logs, receipts, examples, diffs, and PR text;
- cache and derivative invalidation requirements; and
- safe-to-disclose reason text for denial or abstention.

This README does not set numeric privacy thresholds or invent consent semantics. Those values require policy, contract, schema, fixture, test, and steward evidence in their owning roots.

## Review gates

The gate names below describe the review burden for this lane. They do not claim that the draft [promotion-gate ADR](../../../docs/adr/ADR-0018-promotion-gate-sequence.md) or repository workflows enforce the entire sequence.

| Gate | Minimum question | Fail-closed result |
|---|---|---|
| Placement | Is the dossier in the canonical `people-dna-land` lane with no evolving short-name copy? | `HOLD` and migrate or reconcile. |
| Identity | Are candidate, subject, dataset, geography, and version identities stable and collision-aware? | `REPAIR_REQUIRED` or `ABSTAIN`. |
| Evidence | Do applicable references resolve to scoped EvidenceBundles with source-role and integrity closure? | `ABSTAIN`. |
| Rights and consent | Are source rights, attribution, sovereignty, consent, audience, expiry, and revocation resolved? | `DENY` or `HOLD`. |
| Sensitivity and privacy | Are living-person, DNA, family, address, location, land, and combination risks evaluated with required transforms? | `DENY` or `HOLD`. |
| Validation | Did applicable schema, semantic, temporal, spatial, policy, privacy, negative, and citation checks run and pass? | `REPAIR_REQUIRED`, `DENY`, or `ABSTAIN`. |
| Review | Are required roles identified, conflicts visible, and author/approver separation satisfied where applicable? | `HOLD`. |
| Release readiness | Are promotion decision, manifest inputs, immutable targets, correction path, and rollback support complete? | `DENY` or `ABSTAIN`. |

The draft [separation-of-duties ADR](../../../docs/adr/ADR-0024-steward-separation-of-duties-for-release.md) proposes stronger role separation for sensitive releases. Its enforcement remains `NEEDS VERIFICATION`; `CODEOWNERS` alone does not demonstrate independent domain, sensitivity, rights-holder, or release approval.

## Decision vocabulary

Keep candidate status, promotion decisions, and public runtime outcomes distinct.

### Promotion decision

The inspected [`PromotionDecision` contract](../../../contracts/release/promotion_decision.md) and paired schema define:

| Decision | Meaning |
|---|---|
| `APPROVE` | The evaluated transition has enough evidence, policy, review, and rollback support to proceed through the remaining release process. It is not publication by itself. |
| `DENY` | A blocking condition prevents the transition; preserve the prior state and record a safe reason. |
| `ABSTAIN` | The gate cannot decide from the available, current, safe evidence; preserve the prior state and route for remediation or review. |

### Governed public response

Public API, UI, map, export, and AI surfaces use their governed response contract, commonly `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. A promotion `APPROVE` does not authorize a public `ANSWER`; the released artifact, manifest, policy, sensitivity, and request context still govern the response.

### Review hold

`HOLD` and `REPAIR_REQUIRED` are review/workflow dispositions used to stop advancement safely. Do not add them to a machine enum unless the owning contract and schema authorize them.

## Manifest handoff

A canonical dossier may move to manifest preparation only after a separately governed `PromotionDecision` records `APPROVE` and all applicable gates are satisfied.

The handoff should identify:

- immutable candidate and run identifiers;
- exact processed, catalog, or triplet inputs;
- evidence-bundle digests and citation-validation state;
- source-rights and attribution state;
- sensitivity, privacy, consent, and transform-receipt references;
- validation reports and policy-bundle identity;
- author and reviewer role bindings;
- proposed released artifacts and their content hashes;
- correction, invalidation, supersession, and rollback targets; and
- every remaining `UNKNOWN` or `NEEDS VERIFICATION` item.

The inspected common [`release_manifest.schema.json`](../../../schemas/contracts/v1/release/release_manifest.schema.json) is a thin `PROPOSED` stub that requires only `id` and permits additional properties. Shape acceptance against that stub is not release closure. The dossier must not describe manifest enforcement as complete until the contract, schema, validator, fixtures, policy, review, and end-to-end release evidence agree.

## Illustrative candidate dossier

The following is a documentation example, not a schema, real candidate, release record, or permission to place it in this compatibility directory.

```markdown
# <candidate-id> — People candidate dossier

## Status

ASSEMBLING

## Placement

- Canonical lane: release/candidates/people-dna-land/<candidate-id>/
- Short-name copy: none

## Scope

- Object classes: <bounded historical-person assertion classes>
- Excluded: <living-person, raw DNA, private address, private person-parcel data>
- Geography version: <immutable reference>
- Valid/source/retrieval/build time: <explicit values>
- Intended release surface: <bounded public-safe surface>

## Candidate artifact

- Immutable artifact ref: <owning lifecycle path + digest>
- Proposed released target: <artifact family + stable ID>

## Sources and evidence

- Source descriptors and roles: <refs>
- EvidenceRef: <ref>
- EvidenceBundle: <resolved ref + digest>
- Citation validation: <report ref + outcome>

## Rights, consent, sensitivity, and privacy

- Rights and attribution: <status + evidence>
- Living-person posture: <result + uncertainty>
- Consent applicability: <status + authority>
- Public-safe transforms: <receipt refs or not applicable>
- Remaining blockers: <named blockers>

## Validation and review

- Validation reports: <refs + outcomes>
- Policy bundle and decision: <refs>
- Author and reviewer roles: <bindings>
- Review state: <pending / changes requested / approved>

## Release handoff

- PromotionDecision: <ref + APPROVE / DENY / ABSTAIN>
- Manifest readiness: <status>
- Correction path: <ref>
- Rollback target: <ref>
- Supersession or withdrawal: <ref or not applicable>
```

## Verification checklist

### Compatibility and placement

- [ ] No new dossier or sublane was created under `release/candidates/people/`.
- [ ] The canonical dossier uses domain segment `people-dna-land`.
- [ ] No mirrored dossier is evolving in both lanes.
- [ ] Inbound short-name references and generated consumers are inventoried before retirement.
- [ ] Any migration has an approved authority basis, mapping, deprecation window, and rollback plan.

### Candidate closure

- [ ] Candidate identity, version, geography, scope, and time are explicit and immutable.
- [ ] Sources are admitted, rights-aware, and assigned non-collapsed roles.
- [ ] Every consequential EvidenceRef resolves to the intended EvidenceBundle.
- [ ] Living-person, DNA, family, address, location, land, and combination risks were evaluated.
- [ ] Required consent, redaction, aggregation, generalization, withholding, or denial evidence is present.
- [ ] Schema, semantic, temporal, spatial, citation, policy, sensitivity, privacy, and negative checks are recorded.
- [ ] Required reviewers and independence constraints are identified without treating CODEOWNERS as approval.
- [ ] PromotionDecision, ReleaseManifest inputs, correction path, and rollback target are separately reachable.
- [ ] Candidate, internal, RAW, WORK, and QUARANTINE material remains unavailable to public clients and ordinary AI/UI surfaces.
- [ ] No generated text, map, tile, graph, index, screenshot, or README is treated as sovereign evidence.

### Documentation and provenance

- [ ] Repository-relative links resolve at the reviewed commit.
- [ ] Truth labels distinguish confirmed repository facts from proposals and unknowns.
- [ ] No secret, private person, precise sensitive location, raw DNA, consent token, or restricted source content appears in the dossier or PR.
- [ ] AI-authored changes carry a schema-valid generated receipt with human review pending or completed as applicable.
- [ ] A future behavior change updates this README or explains why no documentation change is required.

## Open verification items

- **NEEDS VERIFICATION** — whether any candidate dossiers, inbound links, generators, workflows, scripts, or external consumers still depend on `release/candidates/people/`.
- **NEEDS VERIFICATION** — whether the short-name lane already has a drift, deprecation, alias, or migration entry outside the scoped search; no matching entry was established during this revision.
- **NEEDS VERIFICATION** — the semantic owner, sensitivity reviewer, rights-holder role, and release authority for People candidates; placeholder meta-block roles are not verified assignments.
- **NEEDS VERIFICATION** — whether branch protection or rulesets enforce independent review for `release/` and the sensitive `people-dna-land` lane.
- **NEEDS VERIFICATION** — executable living-person, ambiguous-evidence, consent, revocation, redaction, aggregation, and person-to-parcel deny tests; inspected policy files remain scaffolds.
- **NEEDS VERIFICATION** — full common and domain-specific ReleaseManifest field closure, validator behavior, fixtures, and required-check wiring.
- **NEEDS VERIFICATION** — end-to-end correction, derivative invalidation, cache purge, supersession, withdrawal, and rollback drills for a People release.
- **CONFLICTED / NEEDS VERIFICATION** — the short `people` segment remains present here while current Directory Rules and Domain Placement Law name `people-dna-land` as canonical; retirement requires a bounded migration decision, not a README-only deletion.
- **UNKNOWN** — whether this compatibility directory should ultimately be retained as a permanent redirect/index or removed after a time-bounded deprecation window.

## Maintenance

Review this README when any of the following occurs:

- a candidate or subdirectory appears under this compatibility lane;
- an inbound-reference inventory or domain-segment ADR resolves the short-name path;
- a migration, alias, deprecation, or removal plan is accepted;
- the canonical People candidate README changes its dossier contract;
- living-person, consent, DNA, privacy, sensitivity, or person-to-parcel policy becomes executable;
- ReleaseManifest or PromotionDecision contracts, schemas, validators, or workflows materially change;
- a People candidate reaches manifest handoff, correction, withdrawal, supersession, or rollback; or
- six months pass without review.

## Rollback

Before merge, abandon or close the unmerged review branch only with the appropriate repository authority. After merge, create a transparent revert commit or revert pull request for the README and its generated receipt; do not rewrite shared history.

Reverting this documentation does not roll back data, a candidate, a policy decision, a manifest, or a published artifact. If repository or public state changed separately, use the applicable governed `CorrectionNotice`, `RollbackCard`, invalidation, supersession, and release procedures.

## Related documents

- [Canonical People / DNA / Land candidate lane](../people-dna-land/README.md)
- [Release candidate parent index](../README.md)
- [Release governance root](../../README.md)
- [Directory Rules](../../../docs/doctrine/directory-rules.md)
- [Domain Placement Law](../../../docs/architecture/domain-placement-law.md)
- [People domain guidance](../../../docs/domains/people-dna-land/people.md)
- [People / DNA / Land sensitivity posture](../../../docs/domains/people-dna-land/SENSITIVITY.md)
- [People / DNA / Land release index](../../../docs/domains/people-dna-land/RELEASE_INDEX.md)
- [PromotionDecision contract](../../../contracts/release/promotion_decision.md)
- [ReleaseManifest contract](../../../contracts/release/release_manifest.md)
- [EvidenceBundle contract](../../../contracts/evidence/evidence_bundle.md)
- [People / DNA / Land promotion runbook](../../../docs/runbooks/people-dna-land/PROMOTION_RUNBOOK.md)
- [Proposed promotion-gate ADR](../../../docs/adr/ADR-0018-promotion-gate-sequence.md)
- [Proposed release separation-of-duties ADR](../../../docs/adr/ADR-0024-steward-separation-of-duties-for-release.md)

## Last reviewed

| Field | Value |
|---|---|
| Date | 2026-07-20 |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Base ref | `main` |
| Pinned evidence commit | `0b9307b94c67920e3451e1d40b80d287e7364ee7` |
| Review type | Repository-grounded compatibility-boundary revision; no candidate, data, schema, contract, policy, workflow, manifest, release, or publication state changed. |
| Next review trigger | First compatibility-lane consumer inventory, migration decision, canonical People candidate, manifest handoff, policy graduation, correction, rollback, or 2027-01-20, whichever occurs first. |
