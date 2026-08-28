<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-people-dna-land-land-ownership-readme
title: release/candidates/people-dna-land/land-ownership/ — Land Ownership Candidate Review Lane
version: v2
status: draft
policy_label: public
owners:
  - <people-dna-land-domain-steward>
  - <land-ownership-lane-steward>
  - <release-steward>
  - <data-steward>
updated: 2026-07-20
tags: [kfm, release, candidates, people-dna-land, land-ownership, pre-publication, evidence, rights, privacy, sensitivity, review, validation, correction, rollback]
[/KFM_META_BLOCK_V2] -->

# `release/candidates/people-dna-land/land-ownership/` — Land Ownership Candidate Review Lane

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-people--dna--land-purple)
![sublane](https://img.shields.io/badge/sublane-land--ownership-brown)
![publication](https://img.shields.io/badge/publication-not_yet-orange)
![review](https://img.shields.io/badge/review-required-red)
![posture](https://img.shields.io/badge/default-fail_closed-red)

> [!CAUTION]
> **KFM land-ownership material is evidence, not title.** A dossier in this lane is not a title opinion, legal abstract, survey, adjudication, ownership certificate, legal advice, release approval, or public artifact. Assessor and tax records remain administrative context; parcel geometry is not title-boundary proof; unresolved private person-to-parcel joins fail closed.

> [!IMPORTANT]
> **A candidate is not a release.** A commit, pull request, review, merge, file move, passing schema check, generated manifest, or AI summary does not publish KFM material. Publication remains a governed state transition supported by separate evidence, policy, review, release, correction, and rollback objects.

## Quick jump

[Purpose](#purpose) · [Status and evidence boundary](#status-and-evidence-boundary) · [Repository fit](#repository-fit) · [Lane boundaries](#lane-boundaries) · [Land-ownership invariants](#land-ownership-invariants) · [Candidate lifecycle](#candidate-lifecycle) · [Candidate dossier contract](#candidate-dossier-contract) · [Review gates](#review-gates) · [Sensitive-data safeguards](#sensitive-data-safeguards) · [Identity and time](#identity-and-time) · [Decision vocabulary](#decision-vocabulary) · [Manifest handoff](#manifest-handoff) · [Illustrative dossier](#illustrative-candidate-dossier) · [Review checklist](#review-checklist) · [Open verification](#open-verification) · [Rollback](#rollback)

## Purpose

This directory is the pre-publication review lane for land-ownership candidates within the People / DNA / Land bounded context.

It gives stewards one inspectable place to evaluate whether a proposed land-ownership artifact is sufficiently identified, evidence-bound, rights-aware, privacy-safe, validated, reviewable, correctable, and reversible to move toward manifest preparation.

The lane preserves the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move. This lane records candidate review; it does not store lifecycle payloads or perform promotion.

## Status and evidence boundary

| Field | Current posture |
|---|---|
| Document lifecycle | `draft` |
| Owning responsibility root | `release/` |
| Domain lane | `people-dna-land` |
| Sublane | `land-ownership` |
| Default release posture | Fail closed; no public release while evidence, rights, sensitivity, privacy, validation, review, correction, or rollback remains unresolved. |
| GitHub review route | `.github/CODEOWNERS` currently routes `release/` to `@bartytime4life`; this routes review but does not prove semantic stewardship, approval, or separation of duties. |
| Current candidate inventory | `UNKNOWN`; the inspected repository evidence did not establish a completed land-ownership candidate dossier or governed public release. |
| Executable validation | `NEEDS VERIFICATION`; the domain workflow is a readiness/hold workflow and says accepted executable validation, proof production, consent enforcement, and release dry-run commands are not established. |
| Manifest enforcement | `NEEDS VERIFICATION`; the common and domain-specific release-manifest schemas are thin `PROPOSED` stubs. |
| Public effect of this README | None. It is guidance and an index boundary, not release evidence or publication authority. |

Repository facts in this document are bounded to the evidence snapshot named in the implementing pull request. Links are maintainable repository-relative references; they do not upgrade draft contracts, schemas, policies, runbooks, or scaffolds into verified runtime behavior.

## Repository fit

```text
release/
├── candidates/
│   └── people-dna-land/
│       ├── README.md
│       └── land-ownership/
│           └── README.md        # this file
├── manifests/
├── promotion_decisions/
├── rollback_cards/
└── correction_notices/
```

The [Directory Rules](../../../../docs/doctrine/directory-rules.md) place release candidate dossiers under `release/candidates/<domain>/` and keep release decisions distinct from released payloads under `data/published/`. The [Domain Placement Law](../../../../docs/architecture/domain-placement-law.md) identifies `people-dna-land` as the canonical compound domain segment for responsibility-root lanes.

This sublane inherits the [People / DNA / Land candidate-lane guidance](../README.md) and the [release-candidate parent contract](../../README.md). It narrows those rules for land instruments, land-ownership assertions, parcel versions, ownership intervals, assessor/tax context, and public-safe land derivatives.

No path in this README authorizes a new schema, policy, source registry, evidence store, receipt family, proof family, release family, or public-data authority.

## Lane boundaries

Keep each responsibility in its owning object family and root.

| Concern | Owning surface | Relationship to this lane |
|---|---|---|
| Candidate dossier and readiness notes | `release/candidates/people-dna-land/land-ownership/` | Stored here as pre-release review material. |
| Final promotion decision | `release/promotion_decisions/` using the governed `PromotionDecision` family | Referenced by the dossier; not replaced by a candidate status. |
| Release binding | `release/manifests/` using the governed `ReleaseManifest` family | Prepared only after approval for manifest; not stored as candidate payload. |
| Correction and rollback | `release/correction_notices/`, `release/rollback_cards/` | Must be reachable before material promotion. |
| Semantic meaning | `contracts/` | Candidate cites contracts; this README does not redefine them. |
| Machine shape | `schemas/` | Candidate records validation results; this README is not a schema. |
| Admissibility | `policy/` | Policy records allow, restrict, abstain, or deny; this README does not decide policy. |
| Evidence closure | `EvidenceRef` and `EvidenceBundle` families; materialized proof under `data/proofs/` | Candidate must resolve evidence rather than cite a bare pointer. |
| Process memory | `data/receipts/` | Candidate links receipts; a receipt is not proof or release approval. |
| Source identity and rights | `data/registry/sources/people-dna-land/` | Candidate cites admitted source descriptors and current rights posture. |
| Lifecycle payloads | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/` | Payloads stay outside `release/candidates/`. |
| Generated release scratch | `artifacts/release/people-dna-land/` | Transitional, non-trust-bearing inspection output only; never release authority. |

### What belongs here

- Land-ownership candidate dossiers and sublane indexes.
- Immutable pointers and digests for proposed artifacts.
- Candidate scope, geography, temporal extent, and intended public surface.
- Evidence-closure, source-role, rights, sensitivity, privacy, consent, and review summaries.
- Validation results and safe references to receipts or reports.
- Explicit blockers, abstentions, repair requirements, withdrawals, and supersession notes.
- Manifest-handoff, correction, invalidation, and rollback readiness notes.

### What does not belong here

- Deeds, title files, plats, surveys, probate packets, assessor tables, tax rolls, parcel downloads, OCR text, or other source payloads.
- Raw, work, quarantine, processed, catalog, triplet, or published data artifacts.
- Real living-person identifiers, private addresses, private holdings, exact person-to-parcel joins, DNA/genomic data, consent records, or restricted source content.
- Schema, contract, policy, validator, pipeline, connector, registry, proof, receipt, or runtime implementation.
- Legal conclusions, title opinions, marketable-title determinations, heirship decisions, mineral/water-right conclusions, survey certifications, or legal advice.
- A floating `latest` pointer without immutable identity, digest, temporal scope, and correction lineage.
- Generated language, screenshots, dashboards, map tiles, search indexes, or graph projections used as sovereign evidence.

## Land-ownership invariants

Every dossier must preserve these domain rules.

### Evidence is not title

- A `LandInstrument` can evidence its existence, recording context, stated parties, legal description, and stated land interest.
- A recorded instrument does not by itself prove a complete or current chain of title.
- A `LandOwnershipAssertion` remains an evidence-bound assertion, not a KFM-issued legal conclusion.
- Gaps, conflicts, ambiguous parties, uncertain legal-description parsing, and superseded parcel versions remain visible.
- If evidence does not support the requested ownership statement, the correct posture is `ABSTAIN`, `DENY`, `HOLD`, or `REPAIR_REQUIRED`—not fluent completion.

### Source roles do not collapse

| Source or derivative | Required posture | Prohibited upgrade |
|---|---|---|
| Recorded deed, patent, mortgage, lien, easement, lease, probate, or court instrument | Preserve source authority, recording jurisdiction, instrument type, dates, parties-as-stated, legal description, citation, and caveats. | Do not upgrade the instrument into a complete current-ownership conclusion. |
| Assessor or tax record | `administrative` context with source date, tax/valuation cycle, and jurisdiction. | Never present taxpayer-of-record, mailing name, or assessed parcel as title truth. |
| Parcel geometry or parcel identifier | Versioned spatial/administrative context with source, vintage, CRS, precision, and caveats. | Never present geometry as legal boundary, survey, title, residence, or ownership proof. |
| OCR or parsed legal description | Derived candidate with parser version, confidence, original-text reference, and error posture. | Never replace the original instrument text or silently normalize uncertainty away. |
| Georeferenced or reconstructed boundary | Modeled/derived context with method, inputs, uncertainty, and transform receipt. | Never label it observed, surveyed, adjudicated, or title-authoritative. |
| Aggregate land statistic | Aggregate context with geography and time scope. | Never join it to one person or parcel as record-level truth. |
| AI-generated chain summary | Interpretive output with evidence citations and an `AIReceipt` where applicable. | Never use generated text as evidence, decision, title opinion, or release approval. |

### Public clients stay behind the trust membrane

Public map, API, export, graph, search, Evidence Drawer, Focus Mode, screenshot, embedding, and AI surfaces may consume only released, policy-filtered, public-safe derivatives through governed interfaces. They must not read candidate, RAW, WORK, QUARANTINE, internal canonical, or direct model-runtime state as the normal path.

## Candidate lifecycle

Candidate status describes dossier progress. It does not replace promotion, policy, review, or release objects.

| Candidate status | Meaning | Allowed next posture |
|---|---|---|
| `PROPOSED` | Candidate is named; identity, scope, or evidence may be incomplete. | Assemble or withdraw. |
| `ASSEMBLING` | Dossier inputs are being gathered and resolved. | Continue assembling, quarantine blockers, or move to review. |
| `READY_FOR_REVIEW` | Required sections are present and the packet is ready for independent review. | Review may approve for manifest, require repair, defer, block, abstain, or withdraw. |
| `APPROVED_FOR_MANIFEST` | Review permits preparation of a separate manifest and promotion decision. | Build and validate governed release objects. This is not publication. |
| `PROMOTED` | Candidate was incorporated into an approved release path. | Verify the referenced release objects; this status alone does not prove `PUBLISHED`. |
| `DEFERRED` | Candidate is retained but not ready within the current review window. | Re-evaluate after a named trigger. |
| `REPAIR_REQUIRED` | A correctable evidence, rights, sensitivity, identity, temporal, validation, or rollback defect blocks progress. | Repair and issue a new reviewable state. |
| `BLOCKED` | A governing condition prevents progress and no in-scope repair is currently accepted. | Preserve prior lifecycle state and escalate the named blocker. |
| `WITHDRAWN` | Candidate is no longer under consideration. | Preserve audit lineage; do not silently reuse identity. |
| `SUPERSEDED` | A newer candidate replaces this one. | Link the successor and preserve the prior dossier. |

`PROMOTED` is historical candidate-lane vocabulary. Reviewers must still resolve the referenced `PromotionDecision`, `ReleaseManifest`, policy decisions, evidence, review, and rollback records before describing an artifact as released or published.

## Candidate dossier contract

A complete dossier should make the following review surfaces explicit. A missing required surface fails closed.

| Section | Required content | Fail-closed condition |
|---|---|---|
| Candidate identity | Stable candidate ID, version, dossier path, owner role, status, creation/update times, predecessor/successor refs. | Identity is mutable, ambiguous, person-named, or reused. |
| Scope | Object classes, geography, jurisdictions, temporal extent, intended use, intended audience, and public-surface proposal. | Scope is open-ended or hides a person/parcel/title use. |
| Artifact binding | Immutable artifact URI/path, digest, media type, schema/contract versions, build/run reference. | Floating pointer, missing digest, or candidate payload stored in this lane. |
| Source inventory | Source IDs, providers, source roles, recording/administrative jurisdictions, retrieval times, freshness, and caveats. | Source role, currency, or provenance is unresolved. |
| Evidence closure | EvidenceRefs, resolved EvidenceBundle IDs/digests, citation status, contradictions, gaps, and confidence limits. | Bare EvidenceRef, broken resolver, unsupported ownership statement, or hidden conflict. |
| Land semantics | Instrument types, parcel versions, legal-description posture, ownership intervals, severed interests, and explicit not-title caveat. | Assessor-as-title, geometry-as-boundary, or incomplete chain presented as complete. |
| Rights and attribution | License/terms, public-record access versus redistribution, attribution, embargo, source restrictions, and rights review. | Rights are unknown, expired, conflicting, or not scoped to the proposed release. |
| Sensitivity and privacy | Living-person screen, private person-parcel posture, consent/revocation where applicable, redaction/generalization, re-identification risk, access tier. | Living-person or private holdings exposure is unresolved. |
| Temporal closure | Effective, execution, recording, source, retrieval, review, release, and correction times as applicable; staleness thresholds. | Undated `current owner` claim, ambiguous parcel version, or stale source treated as current. |
| Validation | Schema, semantic, source-role, identity, temporal, legal-description, chain-gap, geometry, privacy, public-surface, and no-network results. | Required validation is absent, failed, stale, or not reproducible. |
| Policy decisions | Resolved policy-decision refs, outcome, policy family/bundle identity, reasons, obligations, and evaluation time. | Decision is missing, stale, non-resolving, or carries unmet obligations. |
| Independent review | ReviewRecord refs, reviewer roles, separation-of-duties check, decision time, ticket, and unresolved comments. | Author is sole approver or sensitive review is incomplete. |
| Release handoff | Proposed PromotionDecision and ReleaseManifest refs/IDs, manifest schema posture, intended published targets, catalog/index impact. | Candidate status is substituted for release objects or manifest authority is unresolved. |
| Correction and rollback | Correction path, invalidation set, cache/graph/search/tile/AI cascade, rollback target/card, withdrawal path, drill status. | No safe rollback target or downstream invalidation plan. |
| Final recommendation | Candidate status, promotion recommendation, safe reasons, blockers, expiration/review trigger, steward sign-off. | Recommendation overclaims evidence, rights, title, validation, or release state. |

## Review gates

The dossier is reviewable only when each gate records an outcome and evidence location. Gate lettering is local to this README; the machine objects and policy bundles remain authoritative.

| Gate | Review questions | Minimum evidence | Blocking examples |
|---|---|---|---|
| A — Identity and scope | Is the exact candidate, artifact, geography, jurisdiction, object family, time window, intended audience, and public surface bounded? | Candidate ID/version; immutable artifact digest; scope statement. | Floating `latest`; scope drift; real person name embedded in candidate ID. |
| B — Source and evidence | Are source roles preserved and do EvidenceRefs resolve to complete EvidenceBundles? | SourceDescriptor refs; EvidenceBundle digests; citations; contradiction/gap notes. | Assessor-only title claim; unresolved evidence; source-role collapse. |
| C — Land and temporal semantics | Are instruments, legal descriptions, parcel versions, ownership intervals, gaps, conflicts, and dates represented without legal overclaim? | LandInstrument/parcel/version refs; temporal checks; chain-gap report; not-title caveat. | Geometry treated as boundary; undated owner claim; gap smoothed away. |
| D — Rights, sensitivity, and privacy | Are redistribution rights, living-person risk, private person-parcel joins, consent/revocation, and re-identification risk resolved? | Rights review; PolicyDecision refs; Redaction/Aggregation receipts; sensitivity review. | Rights unknown; private holdings exposed; consent stale or revoked. |
| E — Validation and public-safe transform | Do schemas, semantic checks, source-role checks, temporal checks, public field allowlists, and no-network tests pass? | ValidationReport/receipt refs; transform digests; deterministic test evidence. | Failed test; unreviewed fixture; unreproducible transform; sensitive field leak. |
| F — Independent review | Are domain, land, release, evidence, policy/privacy, rights, and data responsibilities represented with required separation? | ReviewRecord refs; reviewer/ticket binding; open-comment disposition. | Author-only approval; missing sensitivity/rights review. |
| G — Release, correction, and rollback | Can governed promotion objects be produced and can every released derivative be corrected, withdrawn, invalidated, or restored safely? | PromotionDecision; ReleaseManifest; CorrectionNotice path; RollbackCard/target; invalidation plan. | Thin schema treated as closure; rollback target missing; caches or AI derivatives omitted. |

Recommended gate outcomes are `PASS`, `FAIL`, `HOLD`, and `NOT APPLICABLE`, with a reason and evidence reference. These review outcomes are not the `PromotionDecision` enum and must not be serialized into that object unless its schema permits them.

## Sensitive-data safeguards

Land records may be publicly inspectable at a source while still creating privacy, rights, aggregation, redistribution, or harm concerns when linked, normalized, mapped, searched, or combined with living-person information.

### Deny-by-default cases

The candidate must not advance toward a public surface when any of the following is unresolved:

- a living or possibly living person is linked to an exact parcel, residence, holding, family relation, probate relation, genealogy assertion, or DNA-derived hypothesis;
- an assessor/tax mailing name is labeled as current owner or title holder;
- a parcel polygon is labeled as a legal or surveyed boundary;
- source terms permit access but redistribution, bulk export, derivative publication, or map display is unclear;
- a public record contains incidental personal data that has not been minimized or reviewed;
- an ownership interval, chain-of-title summary, or legal-description parse hides gaps, conflicts, uncertainty, or staleness;
- generalization or redaction can be reversed through joined public fields, tiles, search, graph, screenshots, embeddings, or model outputs;
- a consent or rights state is stale, revoked, unreachable, or scoped to a different use;
- release, correction, withdrawal, downstream invalidation, or rollback support is missing.

### Safe dossier content

- Use synthetic identifiers and non-sensitive examples.
- Refer to protected artifacts by governed opaque reference and digest; do not paste payloads.
- Keep public PR text free of living-person records, private addresses, exact private holdings, DNA information, restricted legal documents, and reconstruction hints.
- Route security-sensitive defects through the repository's [private-first security process](../../../../SECURITY.md), not public candidate prose.
- Record the review result and safe reason code without reproducing the sensitive fact that caused denial.

## Identity and time

### Candidate identity

A candidate identity should bind the review unit without encoding a real person's name, address, private parcel identifier, or sensitive source value.

At minimum, record:

- `candidate_id` and dossier version;
- domain and sublane;
- immutable artifact digest;
- object-family scope;
- geography/jurisdiction scope at a safe level;
- temporal scope;
- predecessor/successor candidate refs;
- creation and last-review timestamps.

The exact identifier grammar remains `NEEDS VERIFICATION`. Until accepted, prefer a repository-safe opaque slug and record the mapping in governed review state rather than inventing a canonical ID format here.

### Land time kinds

Do not collapse these time meanings:

| Time | Meaning |
|---|---|
| Execution time | When parties executed an instrument, when known. |
| Effective time | When the stated interest or legal effect begins, where the source supports it. |
| Recording time | When the recording authority recorded the instrument. |
| Source time | When the source record or administrative cycle was created or valid. |
| Retrieval time | When KFM retrieved the source. |
| Parcel-version time | Which cadastral version or geometry vintage is referenced. |
| Ownership-interval time | The bounded interval asserted from cited evidence, including gaps/conflicts. |
| Review time | When stewards evaluated the candidate. |
| Release time | When a governed release state became effective. |
| Correction time | When a correction, withdrawal, revocation, or rollback changed downstream posture. |

Avoid unqualified phrases such as `current owner`, `current parcel`, or `latest title`. State the evidence date, asserted interval, retrieval time, and known staleness instead.

## Decision vocabulary

Keep progress, promotion, policy, runtime, and publication vocabulary separate.

| Vocabulary family | Current values or posture | What it does not mean |
|---|---|---|
| Candidate lifecycle | `PROPOSED`, `ASSEMBLING`, `READY_FOR_REVIEW`, `APPROVED_FOR_MANIFEST`, `PROMOTED`, `DEFERRED`, `REPAIR_REQUIRED`, `BLOCKED`, `WITHDRAWN`, `SUPERSEDED` | Does not replace policy, promotion, manifest, or publication state. |
| PromotionDecision | Schema-confirmed `APPROVE`, `DENY`, `ABSTAIN` | `APPROVE` is not a ReleaseManifest or public permission. |
| PolicyDecision | Contract/schema finite outcomes `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | `ANSWER` is not release approval. |
| Review gate | Human review result such as `PASS`, `FAIL`, `HOLD`, `NOT APPLICABLE` | Local review vocabulary is not automatically machine-schema vocabulary. |
| KFM lifecycle | `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED` | A directory location alone does not prove a governed transition. |
| Public-surface posture | Public-safe, generalized, redacted, restricted, held, withdrawn, stale, or not ready, as supported by policy/release state | A label without resolving records does not authorize exposure. |

## Manifest handoff

`APPROVED_FOR_MANIFEST` allows maintainers to prepare separate governed objects. It does not permit copying the artifact to `data/published/` or exposing it through an API, map, export, graph, search, or AI surface.

Before handoff, verify:

1. The candidate identity and artifact digest are immutable and reproducible.
2. EvidenceRefs resolve to complete EvidenceBundles.
3. Source roles, rights, attribution, sensitivity, privacy, and temporal scope are current.
4. Required validation and public-safe transforms passed against the same digest.
5. PolicyDecision obligations are satisfied.
6. Independent ReviewRecords are present for the materiality and sensitivity involved.
7. PromotionDecision, ReleaseManifest, correction, withdrawal, and rollback objects can be produced without inventing fields or authority.
8. Intended published artifacts and catalog/index updates are named without storing their payloads here.
9. Downstream cache, tile, graph, search, export, screenshot, embedding, and AI invalidation is planned.

> [!WARNING]
> The common [`release_manifest` schema](../../../../schemas/contracts/v1/release/release_manifest.schema.json) and the People / DNA / Land-specific [`release_manifest` schema](../../../../schemas/contracts/v1/domains/people-dna-land/release_manifest.schema.json) are both thin `PROPOSED` stubs. The [Domain Placement Law](../../../../docs/architecture/domain-placement-law.md) says cross-cutting release object families belong under `contracts/release/` and `schemas/contracts/v1/release/`, while domains cite rather than shadow them. Their relationship is therefore **CONFLICTED / NEEDS VERIFICATION**. Do not treat either schema's minimal validation as release closure until an accepted authority decision reconciles the homes and hardens the required fields.

The file `artifacts/release/people-dna-land/release_manifest.json` is a `PROPOSED` placeholder in a compatibility scratch lane. Its own parent README says that lane is not release authority. It must not be used as a candidate's manifest, proof of release, or publication evidence.

## Illustrative candidate dossier

The following is a Markdown review template, not a machine schema. Replace bracketed prompts with safe, evidence-backed values. Do not include real sensitive payloads.

```markdown
# <opaque-candidate-id> — Land Ownership Candidate Dossier

## Candidate status

| Field | Value |
|---|---|
| Candidate ID | `<opaque-candidate-id>` |
| Version | `<version>` |
| Status | `PROPOSED / ASSEMBLING / READY_FOR_REVIEW / APPROVED_FOR_MANIFEST / PROMOTED / DEFERRED / REPAIR_REQUIRED / BLOCKED / WITHDRAWN / SUPERSEDED` |
| Owner role | `<verified-role-or-OWNER_TBD>` |
| Prior candidate | `<opaque-ref-or-N/A>` |
| Successor candidate | `<opaque-ref-or-N/A>` |
| Created | `<RFC-3339-date-time>` |
| Last reviewed | `<RFC-3339-date-time-or-NOT-RUN>` |

## Scope

- Object classes: `<LandInstrument / LandOwnershipAssertion / ParcelVersion / OwnershipInterval / public-safe derivative>`
- Geography and jurisdiction: `<safe bounded scope>`
- Temporal extent: `<evidence-bounded interval>`
- Intended audience: `<reviewer / restricted / public-safe>`
- Proposed surface: `<governed API / map / export / Evidence Drawer / none>`
- Explicit non-goals: `<legal/title/survey/private-person-parcel exclusions>`

## Artifact binding

| Field | Value |
|---|---|
| Artifact pointer | `<governed immutable path-or-URI>` |
| SHA-256 | `sha256:<64-hex>` |
| Media type | `<type>` |
| Contract/schema refs | `<repo-relative refs>` |
| Build/run receipt | `<opaque ref>` |

## Sources and roles

| Source ID | Provider/jurisdiction | Source role | Source/retrieval time | Rights posture | Caveats |
|---|---|---|---|---|---|
| `<source-id>` | `<provider>` | `<recorded / administrative / modeled / aggregate / candidate>` | `<times>` | `<resolved / unresolved>` | `<safe summary>` |

## Evidence closure

| EvidenceRef | EvidenceBundle | Digest | Scope supported | Gaps/conflicts | Status |
|---|---|---|---|---|---|
| `<opaque-ref>` | `<opaque-bundle-ref>` | `sha256:<64-hex>` | `<narrow claim scope>` | `<safe summary>` | `<resolved / abstain / blocked>` |

## Land and temporal posture

- Instrument and legal-description posture: `<evidence and caveats>`
- Parcel version/vintage: `<source and time>`
- Ownership interval: `<asserted interval; gaps and conflicts visible>`
- Assessor/tax use: `<administrative context only / N/A>`
- Geometry caveat: `Parcel geometry is not title-boundary proof.`
- Legal posture: `KFM evidence is not a title opinion, survey, adjudication, or legal advice.`

## Rights, sensitivity, and privacy

| Review | Result | Evidence/decision ref | Open obligation |
|---|---|---|---|
| Redistribution/attribution | `<PASS / FAIL / HOLD>` | `<ref>` | `<safe summary>` |
| Living-person screen | `<PASS / FAIL / HOLD>` | `<ref>` | `<safe summary>` |
| Private person-parcel screen | `<PASS / FAIL / HOLD>` | `<ref>` | `<safe summary>` |
| Consent/revocation, if applicable | `<PASS / FAIL / HOLD / N/A>` | `<ref>` | `<safe summary>` |
| Redaction/generalization | `<PASS / FAIL / HOLD / N/A>` | `<receipt-ref>` | `<safe summary>` |
| Re-identification review | `<PASS / FAIL / HOLD>` | `<ref>` | `<safe summary>` |

## Validation

| Check | Command/report/receipt | Bound digest | Outcome | Notes |
|---|---|---|---|---|
| Schema and semantic checks | `<ref>` | `sha256:<64-hex>` | `<PASS / FAIL / NOT RUN>` | `<safe summary>` |
| Source-role and assessor-as-title denial | `<ref>` | `sha256:<64-hex>` | `<PASS / FAIL / NOT RUN>` | `<safe summary>` |
| Legal-description and chain-gap checks | `<ref>` | `sha256:<64-hex>` | `<PASS / FAIL / NOT RUN>` | `<safe summary>` |
| Temporal and parcel-version checks | `<ref>` | `sha256:<64-hex>` | `<PASS / FAIL / NOT RUN>` | `<safe summary>` |
| Privacy/public-field checks | `<ref>` | `sha256:<64-hex>` | `<PASS / FAIL / NOT RUN>` | `<safe summary>` |
| Deterministic no-network suite | `<ref>` | `sha256:<64-hex>` | `<PASS / FAIL / NOT RUN>` | `<safe summary>` |

## Policy and review

| Record | Ref | Outcome/state | Evaluated/reviewed at | Obligations or blockers |
|---|---|---|---|---|
| PolicyDecision | `<ref>` | `<ANSWER / ABSTAIN / DENY / ERROR>` | `<date-time>` | `<safe summary>` |
| ReviewRecord | `<ref>` | `<state>` | `<date-time>` | `<safe summary>` |
| Separation of duties | `<ref>` | `<PASS / FAIL / HOLD>` | `<date-time>` | `<safe summary>` |

## Release handoff

| Field | Value |
|---|---|
| PromotionDecision | `<proposed/ref/N/A>` |
| ReleaseManifest | `<proposed/ref/N/A>` |
| Intended published targets | `<paths/URIs or none>` |
| Catalog/index impact | `<refs or none>` |
| Correction path | `<ref or unresolved>` |
| RollbackCard/target | `<ref or unresolved>` |
| Downstream invalidation plan | `<safe summary>` |

## Gate outcomes

| Gate | Outcome | Evidence | Blocking reason |
|---|---|---|---|
| A — Identity and scope | `<PASS / FAIL / HOLD / N/A>` | `<ref>` | `<reason or none>` |
| B — Source and evidence | `<PASS / FAIL / HOLD / N/A>` | `<ref>` | `<reason or none>` |
| C — Land and temporal semantics | `<PASS / FAIL / HOLD / N/A>` | `<ref>` | `<reason or none>` |
| D — Rights, sensitivity, and privacy | `<PASS / FAIL / HOLD / N/A>` | `<ref>` | `<reason or none>` |
| E — Validation and public-safe transform | `<PASS / FAIL / HOLD / N/A>` | `<ref>` | `<reason or none>` |
| F — Independent review | `<PASS / FAIL / HOLD / N/A>` | `<ref>` | `<reason or none>` |
| G — Release, correction, and rollback | `<PASS / FAIL / HOLD / N/A>` | `<ref>` | `<reason or none>` |

## Final recommendation

- Candidate status: `<status>`
- Promotion recommendation: `<prepare manifest / repair / defer / block / withdraw / supersede>`
- Evidence-bounded rationale: `<safe summary>`
- Next review trigger: `<specific evidence, decision, date, or event>`
- Steward sign-off refs: `<refs or pending>`
```

## Review checklist

### Scope and authority

- [ ] Candidate identity, version, digest, scope, owner role, and lineage are explicit.
- [ ] Dossier contains pointers and safe summaries, not lifecycle payloads or protected data.
- [ ] Candidate, PolicyDecision, PromotionDecision, ReviewRecord, ReleaseManifest, receipt, proof, correction, and rollback families remain separate.
- [ ] No file path or schema is treated as authority merely because it exists.

### Land semantics and evidence

- [ ] Every consequential land statement resolves to a complete EvidenceBundle.
- [ ] Source roles are preserved through the proposed derivative.
- [ ] Assessor and tax records remain administrative context, not title truth.
- [ ] Parcel geometry remains versioned context, not legal/title-boundary proof.
- [ ] Instrument, legal-description, parcel-version, ownership-interval, gap, conflict, and confidence posture are visible.
- [ ] The dossier contains no title opinion, legal advice, survey certification, heirship decision, or unsupported present-owner claim.

### Rights, sensitivity, and privacy

- [ ] Source access, redistribution, attribution, embargo, and derivative-use rights are resolved for the exact release use.
- [ ] Living-person, possibly living-person, private person-parcel, consent/revocation, and re-identification reviews fail closed on uncertainty.
- [ ] Redaction/generalization receipts bind the same artifact digest under review.
- [ ] Public PR content contains no real protected payload, private address, exact private holding, DNA data, or reconstruction hint.

### Validation and release

- [ ] Schema, semantic, source-role, identity, temporal, chain-gap, geometry, privacy, and public-field checks are reported honestly.
- [ ] Failed, skipped, pending, and unavailable checks are not relabeled as passing.
- [ ] Independent review and separation-of-duties requirements are satisfied for the materiality involved.
- [ ] Manifest authority conflict is resolved before relying on schema validity as release closure.
- [ ] Correction, withdrawal, derivative invalidation, and rollback targets are specific and testable.
- [ ] No candidate status, commit, PR, merge, workflow result, or generated artifact is described as KFM publication.

## Naming guidance

The exact candidate identifier and filename grammar is `NEEDS VERIFICATION`.

Until a contract or accepted ADR defines it:

- use an opaque repository-safe candidate slug;
- avoid names, addresses, private parcel identifiers, instrument numbers, or other sensitive values in paths;
- include version and immutable digest in the dossier body;
- use ISO dates only for a real review event, not as a substitute for candidate identity;
- preserve withdrawn and superseded dossiers instead of silently reusing names.

## Current repository posture and conflicts

| Item | Status | Review significance |
|---|---|---|
| This sublane README and its parent candidate README exist. | `CONFIRMED` at the implementing PR's pinned base. | The earlier statement that the parent was a greenfield stub is stale and is removed by this revision. |
| `people-dna-land` is the repository's canonical compound domain segment under Domain Placement Law. | `CONFIRMED` for current placement doctrine. | Older Atlas-derived docs still mention short `people` paths; treat them as lineage/conflict, not a reason to rename this lane. |
| CODEOWNERS routes `release/` to `@bartytime4life`. | `CONFIRMED` routing evidence. | Semantic steward assignments, required reviews, and enforced separation remain `NEEDS VERIFICATION`. |
| Domain CI is a readiness/hold workflow. | `CONFIRMED` workflow text. | It intentionally does not prove title, privacy, consent, evidence closure, validation maturity, release readiness, or publication. |
| Common and domain-specific release-manifest schemas are thin stubs. | `CONFIRMED`; authority relationship `CONFLICTED`. | Schema success cannot establish release closure. Resolve through accepted release/schema authority governance. |
| `artifacts/release/people-dna-land/release_manifest.json` is a `PROPOSED` placeholder. | `CONFIRMED` file posture. | Compatibility scratch must not be promoted into release authority. |
| Completed land-ownership candidate dossier and governed public release | `UNKNOWN`. | Do not infer either from README, directory, schema, or placeholder presence. |

## Open verification

- [ ] Assign and verify the People / DNA / Land domain, land-ownership, evidence, rights, privacy/sensitivity, data, release, correction, and rollback steward responsibilities.
- [ ] Confirm which review roles are required for land-only, living-person-adjacent, private person-parcel, probate/genealogy, and consent-sensitive candidates.
- [ ] Define the canonical candidate ID, filename, versioning, supersession, and status-transition contract without sensitive path values.
- [ ] Reconcile the cross-cutting and domain-specific `ReleaseManifest` schema homes through an accepted authority decision; harden required fields, fixtures, validators, and policy gates.
- [ ] Confirm the authoritative PromotionDecision, ReviewRecord, PolicyDecision, CorrectionNotice, RollbackCard, and manifest storage conventions for this lane.
- [ ] Confirm source-descriptor rights fields, freshness windows, citation rules, and deactivation behavior for each land-record source family.
- [ ] Establish deterministic synthetic fixtures and no-network tests for assessor-as-title denial, geometry-as-boundary denial, chain gaps/conflicts, legal-description parsing, living-person/private person-parcel denial, stale rights, correction cascades, and rollback.
- [ ] Establish accepted validator commands, ValidationReport destinations, proof/receipt emission, policy binding, and CI wiring.
- [ ] Verify published-target and catalog/index paths only after a real public-safe artifact and governed release exist.
- [ ] Confirm downstream invalidation coverage for API caches, tiles, catalog entries, graph/triplet projections, search/vector indexes, exports, screenshots, embeddings, Evidence Drawer, Focus Mode, and AI responses.
- [ ] Confirm branch protection, required checks, code-owner review enforcement, and independent reviewer requirements.

## Rollback

For this documentation change, rollback means reverting the reviewed commit or pull-request merge through the normal GitHub review path and re-running the same Markdown, link, receipt, and remote-diff checks. Do not rewrite shared history.

For a land-ownership candidate or release:

1. Preserve the candidate, decision, manifest, evidence, review, correction, and receipt history.
2. Disable or deny an unsafe public surface first when living-person, private-land, rights, consent, or security exposure is involved.
3. Re-verify the proposed prior safe release; an older release may no longer be safe or rights-valid.
4. Issue the governed `CorrectionNotice` and `RollbackCard` or hold/withdraw when no safe prior release exists.
5. Invalidate affected catalog, tile, graph, search, export, cache, screenshot, embedding, Evidence Drawer, Focus Mode, and AI derivatives.
6. Re-run evidence, rights, policy, sensitivity, validation, review, release, and public-surface checks.

Reverting this README does not roll back a land-ownership release.

## Related documentation

### Release and governance

- [Release root](../../../README.md)
- [Release candidate parent](../../README.md)
- [People / DNA / Land candidate parent](../README.md)
- [People / DNA / Land release-review parent](../../../people-dna-land/README.md)
- [PromotionDecision contract](../../../../contracts/release/promotion_decision.md)
- [PromotionDecision schema](../../../../schemas/contracts/v1/release/promotion_decision.schema.json)
- [ReleaseManifest contract](../../../../contracts/release/release_manifest.md)
- [Common ReleaseManifest schema](../../../../schemas/contracts/v1/release/release_manifest.schema.json)
- [RollbackCard contract](../../../../contracts/release/rollback_card.md)
- [Directory Rules](../../../../docs/doctrine/directory-rules.md)
- [Domain Placement Law](../../../../docs/architecture/domain-placement-law.md)
- [Deny-by-default ADR](../../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md)

### People / DNA / Land doctrine and runbooks

- [Domain release index](../../../../docs/domains/people-dna-land/RELEASE_INDEX.md)
- [Land ownership model](../../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md)
- [Chain-of-title notes](../../../../docs/domains/people-dna-land/CHAIN_OF_TITLE_NOTES.md)
- [Scope and boundary](../../../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md)
- [Sensitivity posture](../../../../docs/domains/people-dna-land/SENSITIVITY.md)
- [Data lifecycle](../../../../docs/domains/people-dna-land/DATA_LIFECYCLE.md)
- [Promotion runbook](../../../../docs/runbooks/people-dna-land/PROMOTION_RUNBOOK.md)
- [Rollback runbook](../../../../docs/runbooks/people-dna-land/ROLLBACK_RUNBOOK.md)

### Contracts, lifecycle lanes, and validation posture

- [Land-ownership contract lane](../../../../contracts/domains/people-dna-land/land-ownership/README.md)
- [LandInstrument contract](../../../../contracts/domains/people-dna-land/LandInstrument.md)
- [EvidenceBundle contract](../../../../contracts/evidence/evidence_bundle.md)
- [PolicyDecision contract](../../../../contracts/policy/policy_decision.md)
- [Processed land-ownership lane](../../../../data/processed/people-dna-land/land-ownership/README.md)
- [Catalog land-ownership lane](../../../../data/catalog/domain/people-dna-land/land-ownership/README.md)
- [Published land-ownership layer lane](../../../../data/published/layers/people-dna-land/land-ownership/README.md)
- [Assessor-as-title denial test lane](../../../../tests/domains/people-dna-land/assessor_as_title_denial_test/README.md)
- [Person-parcel join validator lane](../../../../tools/validators/joins/person-parcel/README.md)
- [People / DNA / Land CI readiness workflow](../../../../.github/workflows/domain-people-dna-land.yml)
- [Security policy](../../../../SECURITY.md)

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-20 |
| Review status | Draft v2; repository-grounded expansion; human review pending. |
| Next review trigger | First real land-ownership candidate dossier, accepted manifest-authority decision, executable validation/policy integration, source-rights change, privacy/sensitivity review change, correction, withdrawal, or release decision. |
