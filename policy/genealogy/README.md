<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/genealogy
title: Genealogy Publication Policy Compatibility Lane
type: policy-readme; directory-contract; compatibility-lane
version: v0.1
status: draft; repository-grounded; placement-CONFLICTED; scaffold-only; not activated
owners: OWNER_TBD — People/DNA/Land domain steward · Genealogy assertion steward · Living-person privacy steward · Consent steward · Sensitivity steward · Policy steward · Policy-runtime steward · Evidence steward · Release steward · Docs steward
created: 2026-07-22
updated: 2026-07-22
policy_label: restricted-review; genealogy; people-dna-land; assertion-first; living-person-aware; consent-aware; evidence-bound; source-role-aware; fail-closed; release-gated; correction-aware; rollback-aware
current_path: policy/genealogy/README.md
truth_posture: CONFIRMED repository path, blank prior README, one proposed publication Rego scaffold, default-false rule body, canonical singular policy root, Domain Placement Law, People/DNA/Land domain policy lane, genealogy contracts/docs/schema/fixture/validator lanes, proposed PolicyInputBundle and PolicyDecision contracts, PolicyDecision outcome and policy-family enums, placeholder policy runtime, README-only bundle lane, and policy-test readiness hold / PROPOSED genealogy publication gate semantics, explicit policy inputs, reason codes, obligations, evaluator binding, bundle membership, test matrix, governed API integration, release integration, correction propagation, and migration destination / CONFLICTED top-level policy/genealogy placement versus policy/domains/people-dna-land ownership, standalone genealogy sublane versus genealogy folded into people, and engine boolean allow versus canonical PolicyDecision envelope / UNKNOWN production consumers, deployed evaluator, active bundle, enforcement, branch-protection significance, and public release behavior / NEEDS VERIFICATION accepted owners, placement ADR, rule source citation, complete inventory, contracts/schemas, fixtures, tests, validator wiring, reason and obligation registries, receipts, replay, correction, withdrawal, rollback, and migration plan
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 640fc2f3c9720cf17d640f0267bf540328e973f0
  prior_target_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  publication_rule_blob: f2811f825b5ac1b56f7d7dc4cbc8f4f65b7c438e
related:
  - ../README.md
  - ../domains/people-dna-land/README.md
  - ../consent/people-dna-land/README.md
  - ../sensitivity/people-dna-land/person_parcel_join.deny.rego
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md
  - ../../docs/domains/people-dna-land/SENSITIVITY.md
  - ../../docs/domains/people-dna-land/CONSENT_MODEL.md
  - ../../docs/domains/people-dna-land/sublanes/genealogy.md
  - ../../contracts/domains/people-dna-land/genealogy/README.md
  - ../../contracts/policy/policy_input_bundle.md
  - ../../contracts/policy/policy_decision.md
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../fixtures/domains/people-dna-land/genealogy/README.md
  - ../../tools/validators/genealogy/README.md
  - ../../packages/policy-runtime/README.md
  - ../../.github/workflows/policy-test.yml
notes:
  - "This revision replaces a one-newline README and changes documentation only."
  - "The sibling publication.rego file remains an untested PROPOSED scaffold and is not modified here."
  - "Repository presence is not policy activation, and default allow := false is not proof that a governed runtime evaluates the rule."
  - "No living-person, DNA/genomic, private-family, private-land, or source payload is included."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Genealogy Publication Policy Compatibility Lane

`policy/genealogy/`

> Fail-closed publication-policy scaffolding for genealogy material. This directory is repository-present, but its placement and activation are unresolved. It does not establish person identity, kinship truth, consent, evidence closure, release approval, or runtime enforcement.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.1-informational)
![placement](https://img.shields.io/badge/placement-CONFLICTED-orange)
![implementation](https://img.shields.io/badge/implementation-scaffold--only-lightgrey)
![default](https://img.shields.io/badge/default-fail__closed-critical)
![release authority](https://img.shields.io/badge/release__authority-none-red)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Gates](#proposed-publication-gates) · [Validation](#validation) · [Review](#review-burden) · [Migration](#migration-correction-and-rollback) · [Related](#related-folders) · [ADRs](#adrs)

## Purpose

This directory documents the repository's existing genealogy publication-policy scaffold and the evidence required before any genealogy result may cross the KFM trust membrane.

The intended concern is narrow: determine whether a proposed genealogy derivative is admissible for a specific operation, audience, surface, and time. The decision must remain subordinate to evidence, source-role, rights, sensitivity, consent, review, release, correction, and rollback authority.

Genealogy material is assertion-first:

- a person name is an assertion, not canonical identity merely because it appears in a tree;
- a relationship is a hypothesis or reviewed assertion, not sovereign kinship truth;
- a GEDCOM, family tree, obituary, census row, vital record, cemetery record, probate record, or model output retains its source role and caveats;
- generated language cannot become evidence by being stored, cited, repeated, or rendered;
- living-person, possibly living-person, DNA-derived, private-family, and private person-to-parcel information fails closed;
- publication requires a governed release transition; an allow-like policy result is never sufficient by itself.

This README is a directory contract and drift boundary. It is not an executable policy bundle, accepted placement decision, `PolicyDecision`, review record, consent grant, evidence record, release manifest, or publication approval.

## Authority level

`policy/` is the canonical singular root for allow, deny, restrict, abstain, sensitivity, rights, promotion, and release decisions. The current `policy/genealogy/` path is **CONFIRMED repository-present** but **CONFLICTED / transitional** as a policy authority lane.

Directory Rules place domain policy under:

```text
policy/domains/<domain>/
```

For genealogy, the confirmed domain segment is `people-dna-land`, and the repository already contains `policy/domains/people-dna-land/`. Current domain documentation also disputes whether genealogy is a standalone sublane or part of the broader people sublane. Therefore this README does not declare `policy/genealogy/` canonical and does not authorize additional parallel rule growth.

Until an accepted ADR or migration decision resolves placement:

1. treat the existing file as a compatibility scaffold;
2. make only bounded safety, documentation, or migration-preparation changes here;
3. do not duplicate a rule under both this path and `policy/domains/people-dna-land/`;
4. do not infer authority from the generated Rego package name;
5. preserve history and a forward pointer if the rule moves;
6. keep consent, sensitivity, rights, access, release, and promotion decisions in their owning policy families.

## Status

### Pinned evidence boundary

This revision was prepared against `main@640fc2f3c9720cf17d640f0267bf540328e973f0`.

| Surface | Observed state | Safe conclusion |
|---|---|---|
| `policy/genealogy/README.md` | One newline; blob `8b137891...` | The prior README defined no directory contract. |
| `publication.rego` | Package `kfm.generated.policy.genealogy.publication`; comment says `PROPOSED scaffold`; only `default allow := false` | A fail-closed placeholder exists. If evaluated directly, `allow` remains false for every input; runtime evaluation is not established. |
| Rule source comment | Points to `docs/domains/people-dna-land/sublanes/dna.md` | The genealogy-publication rule's source citation appears misaligned and requires review. |
| Domain policy parent | `policy/domains/people-dna-land/README.md` is a greenfield scaffold | Canonical domain placement is documented, but genealogy rules are not implemented there. |
| Consent policy | Detailed README exists under `policy/consent/people-dna-land/`; placement is itself conflicted | Consent semantics are documented; executable enforcement is not established. |
| Sensitivity policy | A person-parcel default-false Rego scaffold exists | Presence does not prove an active sensitivity bundle or evaluator. |
| Genealogy validators | Four inspected Python files contain only placeholder module docstrings | GEDCOM, living-person, consent-receipt, and overlay-pointer validation is not implemented by those files. |
| Genealogy fixtures | Parent, positive, and negative README lanes exist | Concrete payload inventory and evaluator-backed use remain unverified. |
| Policy runtime | Package remains a `0.0.0` placeholder | No accepted evaluator binding or deployed runtime is established. |
| Policy bundles | README-only lane | No active bundle manifest, selection, signing, or rollback contract is established. |
| Rego tests | The policy workflow asserts no Rego test modules are present | No executable rule test matrix is established. |
| Policy workflow | Read-only readiness holds and schema-fixture inventory | It does not evaluate this rule or emit a `PolicyDecision`. |
| `PolicyDecision` shape | Proposed schema admits four outcomes and six policy families | `genealogy` is not a schema-approved policy-family value. |

### Current maturity

| Capability | Status |
|---|---|
| Directory boundary | Documented by this README; human review pending |
| Publication rule | `PROPOSED` default-false scaffold |
| Canonical placement | `CONFLICTED / NEEDS VERIFICATION` |
| Explicit input contract | Semantically proposed; schema remains permissive |
| Decision normalization | Not implemented |
| Rule tests | Not established |
| Genealogy payload fixtures | Not verified |
| Bundle and evaluator | Not established |
| Governed API integration | `UNKNOWN` |
| Release/correction/rollback integration | `UNKNOWN` |
| Production enforcement | `UNKNOWN` |

Repository presence is not policy activation. A green readiness workflow is not policy conformance, and a default-false Rego scaffold is not proof that public genealogy disclosure is blocked at every deployed surface.

## What belongs here

While placement remains conflicted, this directory may contain only:

- this boundary README;
- the existing genealogy publication-rule scaffold;
- narrowly scoped safety corrections to that scaffold;
- migration notes, package-rename notes, and forward pointers;
- links to the authoritative People / DNA / Land policy, consent, sensitivity, rights, evidence, release, correction, and rollback lanes;
- a bounded inventory of rule inputs, outputs, tests, bundle membership, and consumers once those are verified.

Before adding substantive rule logic here, reviewers must resolve whether the accepted home is this compatibility path or `policy/domains/people-dna-land/`. New logic must not be implemented twice.

## What does NOT belong here

Do not place any of the following in this directory:

- person, family, household, relationship, residence, cemetery, probate, vital-record, or land-record payloads;
- GEDCOM/GEDZip files, family-tree exports, scans, OCR output, or source captures;
- living-person identifiers, contact details, precise residences, private family graphs, or private person-to-parcel joins;
- raw DNA/genomic data, kit or vendor identifiers, segments, match tables, or re-identification hints;
- consent grants, revocation records, rights records, sensitivity labels, evidence bundles, review records, receipts, proofs, or release manifests;
- schema definitions, semantic contracts, source descriptors, validator implementations, UI code, API routes, model prompts, or model weights;
- generated narratives or relationship hypotheses represented as evidence;
- duplicate rules owned by consent, sensitivity, rights, access, promotion, release, or the canonical domain policy lane;
- secrets, credentials, private endpoints, or production configuration;
- public payload examples derived from real people or families.

Policy rules may consume stable references and safe decision summaries. They must not copy protected payloads into decisions, logs, fixtures, receipts, documentation, or error messages.

## Inputs

### Proposed explicit evaluation context

A future genealogy publication gate should receive a versioned, schema-valid `PolicyInputBundle` or accepted equivalent. It must not fetch missing facts silently.

| Input class | Minimum semantics | Fail-closed condition |
|---|---|---|
| Operation | Render, answer, map, export, share, promote, release, correct, withdraw, or rollback | Missing, generic, or unsupported operation |
| Actor and audience | Authenticated role, public/restricted context, purpose, tenant/project scope if applicable | Unknown actor/audience where access differs |
| Subject posture | Stable subject refs; living, deceased, possibly living, or unknown status; determination source and time | Living status absent, stale, inferred weakly, or unknown |
| Assertion posture | Claim type, assertion ID, temporal scope, confidence, contradiction and review state | Claim is presented as fact without assertion provenance |
| Evidence | EvidenceRefs resolving to eligible EvidenceBundles; citation validation; freshness and correction state | Missing, unresolved, stale, contradicted, withdrawn, or insufficient support |
| Source roles | Candidate, observed, administrative, authority, context, modeled, or synthetic role as accepted by source governance | Candidate/model/tree material collapsed into observation or authority |
| Rights | Access, redistribution, attribution, embargo, derivative-use, and jurisdiction posture | Unknown, expired, incompatible, or denied rights |
| Consent | Scope, purpose, subjects, grantee, issue/expiry time, revocation/status proof, and downstream obligations | Required consent absent, ambiguous, expired, revoked, or unverifiable |
| Sensitivity | Living-person, DNA/genomic, private-family, person-parcel, burial/cultural, and re-identification decisions | Required decision absent or unsafe precision retained |
| Release context | Lifecycle state, review state, candidate/release identifiers, intended surfaces, correction and rollback targets | Artifact is not release-eligible for the requested surface |
| Runtime context | Policy bundle, evaluator, contract/schema, adapter, and obligation-interpreter identities | Unknown or incompatible component/version |

### Input invariants

1. Preserve the difference between absent, unknown, conflicted, restricted, revoked, false, and not applicable.
2. Treat a person as possibly living when death status cannot be established under an accepted rule.
3. Do not infer consent from public availability, family relationship, account access, tree membership, silence, prior publication, or deceased status.
4. Do not let consent override rights, sensitivity, evidence, source-role, review, or release denial.
5. Pass references and decision summaries across the trust membrane; keep protected payloads in governed stores.
6. Bind evaluation to immutable or content-addressed policy, schema, evidence, and release versions where practical.
7. Hash or minimize audit inputs without creating a re-identification channel.

## Outputs

### Engine result versus repository-facing decision

The current scaffold exposes a Boolean `allow`. That value is not a complete KFM decision record.

A future evaluator must normalize engine-native results into the accepted `PolicyDecision` contract:

| Canonical outcome | Genealogy publication meaning |
|---|---|
| `ANSWER` | The specific operation may proceed only after every independent gate passes and all obligations are enforced. |
| `ABSTAIN` | The request is not categorically prohibited, but admissible evidence or required context cannot support a trustworthy public result. |
| `DENY` | Policy prohibits the operation or disclosure for the evaluated audience and purpose. |
| `ERROR` | Integrity, schema, evaluator, bundle, timeout, or obligation-enforcement failure prevents a trustworthy decision. |

The current `PolicyDecision` schema does not admit `genealogy` as `policy_family`. Until reviewed contracts and schemas change, a future implementation must compose accepted families such as `access`, `consent`, `sensitivity`, `render`, or `promotion`; it must not emit an invented production value.

### Proposed reason categories

Exact reason-code vocabulary requires a reviewed registry. Candidate categories include:

- living status unknown or possibly living;
- required consent absent, expired, revoked, or unverifiable;
- DNA-derived or re-identification risk;
- candidate/model source role not corroborated;
- evidence missing, conflicted, stale, or withdrawn;
- rights or redistribution posture unresolved;
- sensitivity decision missing or denied;
- raw GEDCOM/source identifier exposure;
- private family-graph or person-parcel disclosure;
- review, release, correction, or rollback state missing;
- evaluator, bundle, schema, or obligation-interpreter failure.

Reason text must not reveal the protected fact. Public-safe reasons should be coarse, stable, non-enumerating, and resistant to differential probing.

### Proposed obligations

An `ANSWER`-eligible decision may still require obligations, including:

- redact or generalize names, dates, places, geometry, family edges, source identifiers, or timing;
- omit living-person, possibly living-person, DNA-derived, private-family, or private-land fields;
- bind each material claim to validated, audience-eligible evidence;
- preserve source role, uncertainty, contradiction, and temporal scope;
- display attribution, limitations, freshness, correction, and non-title notices;
- prohibit caching, export, resharing, indexing, embedding, or model reuse;
- require steward review or a restricted audience;
- record policy, redaction/generalization, release, and generated-work receipts;
- invalidate downstream API, map, graph, search, cache, export, screenshot, embedding, Focus Mode, and AI derivatives after correction or revocation.

If a caller cannot prove it enforces every returned obligation, the operation must not proceed.

## Proposed publication gates

The smallest sound publication evaluation is a composition of independent gates:

1. **Request admission** — validate operation, purpose, actor, audience, schema, and bounded scope.
2. **Subject safety** — determine living/possibly-living posture without treating missing evidence as death.
3. **Source-role integrity** — keep community trees, GEDCOM imports, modeled relationships, and AI suggestions in candidate/model roles until corroborated and reviewed.
4. **Evidence sufficiency** — require resolvable, current, claim-scoped evidence; cite or abstain.
5. **Rights and consent** — verify exact use, purpose, duration, audience, revocation, redistribution, and derivative rights.
6. **Sensitivity and re-identification** — evaluate family-graph, DNA, location, person-parcel, burial/cultural, small-count, and mosaic risks.
7. **Public-safe transformation** — apply only accepted redaction/generalization transformations and validate the transformed artifact again.
8. **Review and release** — require independent review appropriate to materiality plus a valid release state and rollback target.
9. **Post-generation/render check** — inspect the actual API, map, export, or AI candidate for leakage and citation closure.
10. **Correction and revocation check** — reject stale outputs and propagate invalidation before delivery or cache reuse.

Failure at any gate produces an explicit non-answer outcome. Never fall back to raw model text, an uncited relationship narrative, a lower policy version, an internal-store path, or a less restrictive audience.

### Minimum decision matrix

| Scenario | Expected posture | Critical assertion |
|---|---|---|
| Synthetic historical claim, deceased subjects, eligible evidence, compatible rights, safe transform, reviewed release | Candidate `ANSWER` only after all gates | Historical status alone is insufficient. |
| Evidence missing or conflicting | `ABSTAIN` | No plausible lineage narrative is substituted. |
| Subject is living, possibly living, or status unknown | `DENY` or restricted review under an accepted policy | No identifying or relationship payload leaks. |
| Required consent is missing, expired, revoked, or unverifiable | `DENY` | Prior access or publication is not consent. |
| DNA-derived relationship or re-identification hint requested publicly | `DENY` | No raw or inferred genomic linkage is exposed. |
| Community tree or GEDCOM assertion lacks corroboration | `ABSTAIN` or review hold | Candidate material does not become observed truth. |
| Rights or redistribution terms are unresolved | non-answer | Evidence access does not imply publication rights. |
| Raw source IDs or private family edges appear in candidate output | `DENY` | Post-render inspection catches leakage. |
| Policy bundle, evaluator, schema, or obligation interpreter fails | `ERROR` | Candidate output is not rendered. |
| Correction or revocation affects a prior result | non-answer plus invalidation | Downstream copies are disabled or marked stale according to policy. |

## Keystone invariants

- EvidenceBundle outranks generated language, family trees, memory, confidence, and visual presentation.
- Cite-or-abstain applies to every material genealogy claim.
- RAW, WORK, and QUARANTINE records never become public because a policy file exists.
- Policy evaluates admissibility; it does not establish person, relationship, source, evidence, consent, review, or release truth.
- Public clients use governed interfaces and released public-safe derivatives, never canonical/private stores.
- Sensitivity, rights, consent, evidence, review, and release are independent gates; the most restrictive applicable decision wins.
- Living-person, possibly living-person, DNA-derived, private-family, and private person-parcel disclosures fail closed.
- Denial and abstention metadata must not become an oracle for protected facts.
- Watchers, validators, policy evaluators, AI adapters, and renderers are non-publishers.
- Promotion is a governed state transition, not a copy, render, merge, or file move.
- Corrections, withdrawals, consent revocations, and rights changes propagate to downstream derivatives.
- Historical audit evidence is preserved; rollback does not erase the decision trail.

## Validation

### Current validation posture

The inspected repository evidence establishes only readiness checks:

- `publication.rego` has no positive rule body and no directly associated `_test.rego` module;
- the policy workflow deliberately holds because no accepted OPA command, bundle artifact, manifest, evaluator binding, or executable policy runtime exists;
- the common schema harness validates `PolicyDecision` JSON shape, not genealogy rule behavior;
- the four inspected genealogy validator modules are docstring-only placeholders;
- genealogy fixture READMEs describe positive and negative cases, but concrete evaluator-backed fixture use is unverified.

Do not report policy behavior as tested or enforced from those facts.

### Minimum executable proof before activation

1. Resolve canonical rule placement and package naming through an accepted decision.
2. Correct and review the rule's doctrine/source citation.
3. Accept an explicit input contract and harden the paired schema.
4. Define reviewed reason-code and obligation registries.
5. Implement rules for every gate and default-deny branch.
6. Add deterministic Rego tests using synthetic, public-safe fixtures only.
7. Cover `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` normalization.
8. Prove that unknown living status, missing consent, revoked consent, DNA inference, source-role collapse, missing evidence, unknown rights, unsafe precision, missing release, and evaluator failure all fail closed.
9. Bind a versioned bundle to an accepted evaluator and governed API consumer.
10. Prove every consumer enforces obligations and refuses unknown obligations.
11. Add replayable decision and generated-work receipts without sensitive payloads.
12. Test correction, withdrawal, revocation, cache invalidation, supersession, and rollback.
13. Demonstrate that UI, map, export, graph, search, Focus Mode, and AI paths cannot bypass the gate.
14. Run an independent privacy, security, rights, policy, and release review.

### Suggested commands after implementation

The repository has not accepted these commands yet; they are targets for the implementation contract:

```bash
opa test policy/ -v
pytest -q tests/policy tests/domains/people-dna-land
```

Do not replace the current readiness hold with an echo-only success. Wire the actual accepted commands and fail when zero tests are collected.

## Review burden

This lane has a high review burden because genealogy outputs can expose living people, family relationships, DNA-derived inferences, private residences, land associations, and sensitive historical or cultural context.

Every substantive change requires:

- policy and People / DNA / Land domain review;
- genealogy assertion and source-role review;
- living-person privacy, consent, rights, and sensitivity review;
- contract/schema review for input or decision changes;
- security/runtime review for evaluator, bundle, logging, caching, or API changes;
- evidence and release review for public-output changes;
- synthetic fixtures and negative-path proof;
- exact changed-path and bundle inventory;
- deterministic version/hash binding and remote read-back;
- correction, withdrawal, revocation, and rollback evidence;
- a generated-work receipt for AI-authored changes;
- human approval separate from generation and validation.

`CODEOWNERS` routes `policy/` review to `@bartytime4life`. That is repository routing only; it is not a StewardshipAssignment, independent review record, policy approval, release approval, or proof that separation of duties occurred.

## Migration, correction, and rollback

### Documentation rollback

Before merge, close the review PR. After merge, revert the documentation commit through normal Git history. Do not force-push shared history.

### Placement migration

If an accepted decision moves this lane into `policy/domains/people-dna-land/`:

1. inventory every genealogy rule, test, fixture, bundle reference, package, workflow, validator, contract/schema reference, and consumer;
2. choose one canonical destination and package namespace;
3. add a migration note with old/new paths, hashes, owners, effective date, and rollback target;
4. move rule and tests together without changing semantics in the same step unless separately reviewed;
5. leave this README as a frozen forward pointer or remove it only under the accepted migration plan;
6. prohibit independent writes at the old path;
7. re-run bundle, evaluator, consumer, correction, and rollback tests;
8. preserve historical receipts, decisions, reviews, and release records.

### Active-policy rollback

A future active policy rollback must:

- disable unsafe public delivery first;
- select a previously verified bundle, not merely an older bundle;
- verify evaluator/schema compatibility;
- compare replayed decisions on the synthetic matrix;
- issue correction or withdrawal records when public behavior changed;
- invalidate affected caches, indexes, exports, graphs, tiles, screenshots, embeddings, Focus Mode results, and AI answers;
- retain immutable audit history;
- use `DENY` or `ERROR` when no safe prior version exists.

Reverting this README does not roll back a policy bundle, release, or published derivative.

## Related folders

### Policy and runtime

- [Policy root](../README.md)
- [People / DNA / Land domain policy](../domains/people-dna-land/README.md)
- [People / DNA / Land consent policy](../consent/people-dna-land/README.md)
- [Person-parcel sensitivity scaffold](../sensitivity/people-dna-land/person_parcel_join.deny.rego)
- [Policy runtime package](../../packages/policy-runtime/README.md)
- [Policy readiness workflow](../../.github/workflows/policy-test.yml)

### Doctrine and domain boundary

- [Directory Rules](../../docs/doctrine/directory-rules.md)
- [People / DNA / Land scope and boundary](../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md)
- [Genealogy sublane doctrine](../../docs/domains/people-dna-land/sublanes/genealogy.md)
- [Sensitivity posture](../../docs/domains/people-dna-land/SENSITIVITY.md)
- [Sensitivity profile](../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md)
- [Consent model](../../docs/domains/people-dna-land/CONSENT_MODEL.md)
- [Consent register](../../docs/domains/people-dna-land/CONSENT_REGISTER.md)
- [Data lifecycle](../../docs/domains/people-dna-land/DATA_LIFECYCLE.md)
- [Governed AI architecture](../../docs/architecture/governed-ai.md)

### Contracts, schemas, fixtures, and validation

- [Genealogy semantic contracts](../../contracts/domains/people-dna-land/genealogy/README.md)
- [Genealogy schema compatibility index](../../schemas/contracts/v1/domains/people-dna-land/genealogy/README.md)
- [PolicyInputBundle contract](../../contracts/policy/policy_input_bundle.md)
- [PolicyDecision contract](../../contracts/policy/policy_decision.md)
- [PolicyInputBundle schema](../../schemas/contracts/v1/policy/policy_input_bundle.schema.json)
- [PolicyDecision schema](../../schemas/contracts/v1/policy/policy_decision.schema.json)
- [Genealogy fixture index](../../fixtures/domains/people-dna-land/genealogy/README.md)
- [Positive fixture lane](../../fixtures/domains/people-dna-land/genealogy/positive/README.md)
- [Negative fixture lane](../../fixtures/domains/people-dna-land/genealogy/negative/README.md)
- [Genealogy validator lane](../../tools/validators/genealogy/README.md)
- [Security policy](../../SECURITY.md)

## ADRs

- [ADR-0003 — singular policy root](<../../docs/adr/ADR-0003-policy-singular-is-canonical-(policies-is-compatibility).md>) is `proposed`; it supports the root name but is not an accepted genealogy placement decision.
- [ADR-0010 — deny by default for DNA and other sensitive classes](../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) is `draft / proposed / numbering-conflicted`; this README follows the stronger fail-closed doctrine without claiming ADR acceptance.
- A genealogy policy placement and package-normalization ADR is **NEEDS VERIFICATION**. This README does not create or accept one.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-22 |
| Evidence base | `main@640fc2f3c9720cf17d640f0267bf540328e973f0` |
| Review state | Draft v0.1; AI-authored; human review pending |
| Next review trigger | Placement decision, substantive Rego change, corrected source citation, accepted input/decision schema, first Rego test, first active bundle/evaluator, governed API integration, consent/sensitivity change, release decision, correction, withdrawal, or rollback drill |

<p align="right"><a href="#top">Back to top</a></p>
