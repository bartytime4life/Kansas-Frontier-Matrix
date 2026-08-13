<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/genealogy
title: policy/genealogy/ — Genealogy Publication Policy Compatibility Boundary
type: readme
version: v0.2
status: draft; BOUNDARY_COMPACT; repository-grounded; placement-conflicted; scaffold-only; evaluator-unbound; non-release; non-publication
owner: NEEDS VERIFICATION — .github/CODEOWNERS routes /policy/ to @bartytime4life; accepted genealogy, living-person privacy, consent, policy, release, and independent approval roles remain unproved
created: 2026-07-22
updated: 2026-08-13
current_path: policy/genealogy/README.md
owning_root: policy/
responsibility: Document the local compatibility boundary for the existing genealogy publication-rule scaffold, its inherited policy authority, safe inputs and outputs, placement conflict, validation limits, sensitive-data exclusions, and migration or rollback handoffs without creating genealogy truth, activating policy, approving release, or authorizing publication.
policy_label: internal-operating-policy; repository-public; genealogy; people-dna-land; assertion-first; living-person-aware; consent-aware; evidence-bound; source-role-aware; fail-closed; release-gated; correction-aware; rollback-aware
base_commit: 3e6db4917f89d71331d7f46c08dc64c5000558bf
target_baseline_blob: b12f21e204bb753b745d49812798c6894d4f308c
publication_rule_blob: f2811f825b5ac1b56f7d7dc4cbc8f4f65b7c438e
policy_root_blob: 6c5021f9d92778581a4e9331a9dd6ddb7efc5e35
people_dna_land_policy_blob: 571a4a6d5c8ba7cf6c1fa9fcdd63da88bc05eb2a
directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
adr_0029_blob: b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62
root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
genealogy_doctrine_blob: 49fa3ad1af188f072e6404c984ee95664e52ac6b
consented_overlay_contract_blob: d548e5eb93efe0b48accfa497de90dd924f753eb
consented_overlay_schema_blob: dbb3d8cd6310ee4534c4180dafc288f941e82dfd
consented_overlay_validator_blob: b2ff0e5037de0f1c22486743ab5e20926c68474d
consented_overlay_test_blob: 4f529582d961ed2b87df20a7f158e03d52eccbc8
people_dna_land_workflow_blob: bcf64c3e3b6653b9543489fc5a6031805ae3ef48
codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
directory_governance: Accepted ADR-0029 adopts Directory Rules v2; policy/ is the singular policy-source root; the current topic path remains a same-path compatibility candidate because domain-lane placement points to policy/domains/people-dna-land/ and no accepted genealogy placement decision was found.
truth_posture: CONFIRMED exact two-file inventory, default-false publication scaffold, no operative rule body, no local native Rego test or package consumer found, accepted policy-root placement, executable synthetic consent-overlay validation in an adjacent domain lane, and unproved general evaluator, bundle, release, and publication integration / PROPOSED local publication-gate semantics, inputs, normalization, reasons, obligations, tests, migration, correction, and rollback / CONFLICTED policy/genealogy/ compatibility path versus policy/domains/people-dna-land/ domain placement and standalone genealogy versus people-sublane ownership / NEEDS VERIFICATION canonical local scope ID, accepted owners, source citation, package and entrypoint, bundle membership, evaluator binding, decision-family mapping, consumers, receipts, required checks, and production enforcement
related:
  - ../README.md
  - ../domains/people-dna-land/README.md
  - ../consent/people-dna-land/README.md
  - ../sensitivity/README.md
  - ../rights/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/domains/people-dna-land/sublanes/genealogy.md
  - ../../contracts/domains/people-dna-land/genealogy/README.md
  - ../../contracts/domains/people-dna-land/consented_genealogy_overlay.md
  - ../../schemas/contracts/v1/domains/people-dna-land/consented_genealogy_overlay.schema.json
  - ../../fixtures/domains/people-dna-land/consent_overlay/README.md
  - ../../tools/validators/domains/people-dna-land/validate_consent_overlay.py
  - ../../tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py
  - ../../packages/policy-runtime/README.md
  - ../../release/README.md
  - ../../.github/workflows/domain-people-dna-land.yml
notes:
  - "This v0.2 revision reconciles the existing v0.1 README with current main and changes documentation only."
  - "The sibling publication.rego file remains a PROPOSED default-false scaffold and is not modified or activated."
  - "The executable consent-overlay profile is synthetic, restricted, fixture-only, no-network, and non-release; it does not evaluate publication.rego."
  - "No real person, family, DNA/genomic, parcel, private-source, consent, or sensitive-location payload belongs in this public repository-facing README."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# policy :: genealogy

`policy/genealogy/` is KFM's **BOUNDARY_COMPACT compatibility boundary** for an existing genealogy publication-rule scaffold. It inherits policy authority from [`policy/`](../README.md), but its canonical placement, package identity, evaluator binding, and activation remain unresolved. It does not establish person identity, kinship, consent, evidence closure, release approval, or publication safety.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-status)
[![Placement: conflicted](https://img.shields.io/badge/placement-CONFLICTED-d97706?style=flat-square)](#inherited-authority-owner-and-scope)
[![Rule: scaffold only](https://img.shields.io/badge/rule-scaffold%20only-6e7781?style=flat-square)](#current-rule-inventory)
[![Default: false](https://img.shields.io/badge/default-allow%20false-b42318?style=flat-square)](#default-posture)
[![Evaluator: unbound](https://img.shields.io/badge/evaluator-unbound-d97706?style=flat-square)](#current-status)
[![Publisher: no](https://img.shields.io/badge/publisher-no-b42318?style=flat-square)](#inherited-authority-owner-and-scope)

> [!IMPORTANT]
> **Safe current conclusion at `main@3e6db4917f89`:** this directory contains only this README and `publication.rego`. The Rego file declares `default allow := false` but has no operative rule body, local native test, verified package consumer, accepted bundle membership, or evaluator binding. Repository presence is not policy activation.

> [!CAUTION]
> A separate People / DNA / Land fixture profile now executes deterministic, no-network checks for a synthetic consent-safe genealogy overlay. That bounded proof does **not** evaluate `publication.rego`, authenticate consent, establish identity or kinship, approve release, or prove public-surface enforcement.

> [!WARNING]
> Do not place real people, family graphs, GEDCOM exports, DNA/genomic material, kit identifiers, private source records, precise residences or parcels, consent tokens, revocation records, or other protected payloads in this directory, its documentation, tests, logs, reasons, or examples.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Directory](#current-direct-child-map) · [Rules](#current-rule-inventory) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Boundary](#genealogy-trust-boundary) · [Inputs and outputs](#inputs-and-outputs) · [Exposure](#exposure-mutation-and-retention) · [Posture](#default-posture) · [Gates](#proposed-publication-gates) · [Adjacent proof](#bounded-adjacent-fixture-proof) · [Validation](#validation-coverage-and-limits) · [Review](#review-burden) · [Migration](#migration-correction-revocation-and-rollback) · [Open work](#open-verification-register) · [Evidence](#no-loss-and-evidence-ledger)

## Purpose

This lane documents one narrow policy question:

> Given an explicit operation, actor, audience, purpose, genealogy assertion, source and evidence posture, living-person status, rights, consent, sensitivity, lifecycle, review, release, correction, and rollback context, may a specific derivative cross a governed trust boundary—and under which enforceable obligations?

The existing rule does not yet implement that question. This README defines the review boundary and the evidence required before maintainers could safely graduate the scaffold.

Genealogy remains **assertion-first**:

- a name is a source-bound assertion, not canonical identity merely because it appears in a record or tree;
- a relationship is a hypothesis or reviewed assertion, not sovereign kinship truth;
- GEDCOM, family-tree, obituary, census, vital, cemetery, church, school, military, court, probate, and similar records retain their source roles and caveats;
- generated language, graph structure, confidence, repetition, or attractive rendering cannot become evidence;
- historical or deceased-person posture does not by itself close rights, cultural, burial, sensitivity, evidence, review, or release gates;
- living-person, possibly-living, DNA-derived, private-family, and private person-to-parcel material fails closed for public exposure;
- an allow-like policy result is never a release or publication decision.

This README is a directory contract and drift boundary. It is not executable policy, a `PolicyDecision`, a consent grant, an evidence record, a review record, a release manifest, a correction notice, or a publication approval.

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent | [`policy/`](../README.md), the canonical root for normative allow, deny, hold, restrict, and abstain rule source. |
| Directory profile | `BOUNDARY_COMPACT`, because this lane changes policy, exposure, sensitivity, and release assumptions. |
| Governing placement | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Sections 9.3, 12.2, and 16 separate policy from contracts and schemas, show the domain-lane pattern, and define this README contract. |
| Machine projection | [`root_registry.yaml`](../../control_plane/root_registry.yaml) classifies `policy/` as canonical, internal, versioned, and durable policy-rule authority while prohibiting data instances, release decisions, and schemas. The registry is a projection, not new authority. |
| Current local path | `policy/genealogy/` is tracked and referenced by FamilySearch source documents as a `PROPOSED` publication gate. |
| Placement conflict | Directory Rules route domain policy to `policy/domains/<domain>/`; the confirmed domain lane is [`policy/domains/people-dna-land/`](../domains/people-dna-land/README.md). No accepted decision found in this review selects this topic path as canonical, migrates it, or permits duplicate rule growth. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` to `@bartytime4life`. Routing does not prove stewardship, independent review, approval, or required-check enforcement. |
| Local owner | **NEEDS VERIFICATION.** No accepted genealogy policy steward, living-person privacy steward, consent steward, or independent approver was established. |
| Local scope ID | **NEEDS VERIFICATION.** No accepted scope identifier for this boundary was found. The stable document ID is not a policy scope ID. |
| Release authority | None. [`release/`](../../release/README.md) owns release, correction, withdrawal, and rollback decisions. |
| Publication authority | None. Public carriers require a separate governed release path and enforceable trust-membrane consumer. |

Until placement is resolved:

1. treat `publication.rego` as a frozen compatibility scaffold, not an active policy family;
2. make only bounded safety, documentation, or migration-preparation changes here;
3. do not implement the same rule under both this path and `policy/domains/people-dna-land/`;
4. do not infer authority from a generated package name or repository link;
5. preserve history and a forward pointer if the rule moves; and
6. keep consent, sensitivity, rights, access, identity, evidence, release, and correction authority in their owning lanes.

## Current status

| Surface | Confirmed state at baseline | Safe interpretation |
|---|---|---|
| Target README | Existing v0.1 boundary, blob `b12f21e204bb753b745d49812798c6894d4f308c` | Substantial July documentation existed, but it predated accepted Directory Rules and the adjacent executable fixture slice. |
| Direct inventory | Two tracked files; no subdirectories | The child map is complete at the pinned base. |
| `publication.rego` | Four-line module; package `kfm.generated.policy.genealogy.publication`; `default allow := false`; no other rule body | A default-false scaffold exists. It does not establish parsing, evaluation, bundle selection, or enforcement. |
| Rule source comment | Points to `docs/domains/people-dna-land/sublanes/dna.md` | **STALE / MISALIGNED.** A genealogy publication rule should not silently cite the DNA sublane as its sole source. The rule is unchanged here. |
| Package consumers | Exact package-name search found only the defining file | No tracked evaluator or consumer binding was found. Documentation path references are not package consumers. |
| Local native tests | No `*_test.rego`, local test directory, or test payload in this lane | Genealogy publication-rule behavior is not natively tested. |
| Domain policy lane | [`policy/domains/people-dna-land/`](../domains/people-dna-land/README.md) contains proposed default-only stubs | Canonical domain placement exists as a scaffold; it does not implement genealogy publication policy. |
| Shared genealogy validators | Four Python files under [`tools/validators/genealogy/`](../../tools/validators/genealogy/README.md) are docstring-only placeholders | GEDCOM, living-person, consent-receipt, and overlay-pointer validation is not implemented by those files. |
| Genealogy fixture lane | Parent, positive, and negative README files only; no payloads found | Scenario documentation exists; executable genealogy-publication fixture coverage is not established there. |
| Consent-overlay fixture profile | Contract, two closed schemas, two valid fixtures, 13 invalid fixtures with exact sidecars, deterministic validator, and Python tests exist in adjacent People / DNA / Land lanes | **CONFIRMED bounded executable fixture proof.** It is synthetic, restricted, non-release, and not a policy evaluator. |
| People / DNA / Land workflow | Executes the consent-overlay and consent-revocation-propagation fixture profiles while retaining broader holds | It proves those frozen profiles, not identity, kinship, real consent, policy approval, release, or publication. |
| Broad policy workflow | Static readiness guard plus one separately governed release-gate Rego lane | It does not evaluate this rule or emit a genealogy `PolicyDecision`. |
| Policy runtime | `0.0.0` package metadata with empty/comment-only implementation surfaces | No general evaluator, bundle selector, normalized decision flow, or production consumer is established. |
| `PolicyDecision` shape | Proposed schema permits four outcomes and six policy families | `genealogy` is not an admitted `policy_family`; no accepted composition or schema migration exists. |
| Required checks and production enforcement | Not proved by reviewed repository files | Workflow presence and CODEOWNERS do not establish ruleset enforcement, deployment, or public behavior. |

### Truth labels used here

- **CONFIRMED** — verified from the exact repository bytes pinned in this revision.
- **PROPOSED** — a reviewable target, candidate contract, or future behavior not established as current.
- **UNKNOWN** — the reviewed evidence is insufficient.
- **NEEDS VERIFICATION** — a concrete check remains before relying on the claim.
- **CONFLICTED** or **STALE** — a qualifier attached to one of the core labels; never a substitute for evidence.

## Current direct-child map

Verified at `main@3e6db4917f89d71331d7f46c08dc64c5000558bf`:

```text
policy/genealogy/
├── README.md          — local compatibility and safety boundary; no runtime effect
└── publication.rego   — PROPOSED default-false scaffold; placement and evaluator unbound
```

Directory Rules require direct children only. This tree does not copy deeper contract, schema, fixture, test, validator, runtime, or release inventories into the policy lane.

## Current rule inventory

| Property | Current value | Consequence |
|---|---|---|
| File | [`publication.rego`](publication.rego) | Only executable-looking file in this directory. |
| Package | `kfm.generated.policy.genealogy.publication` | Generated-style name; no accepted package or versioning contract found. |
| Entrypoint candidate | `data.kfm.generated.policy.genealogy.publication.allow` | Inferred from Rego naming only; no accepted evaluator binding establishes it. |
| Default | `allow := false` | If parsed and evaluated under compatible Rego semantics, the value remains false because no positive rule exists. Repository execution is not established. |
| Input references | None | The rule evaluates no operation, audience, evidence, rights, consent, sensitivity, review, release, or correction context. |
| Reasons and obligations | None | A Boolean alone cannot explain or safely enforce a governed result. |
| Tests | None in this lane | No positive, negative, error, or normalization proof exists for the rule. |
| Bundle and evaluator | None found | The file is not shown to participate in an active policy bundle. |
| Consumers | None found by exact package search | No governed caller is shown to enforce its result. |

The module is safer than an unconditional allow, but it is not a complete deny-by-default policy. File presence, `default allow := false`, or a green unrelated workflow must not be cited as proof that every deployed surface blocks unsafe genealogy disclosure.

## What belongs here

While placement remains conflicted, this directory may contain only:

- this local boundary README;
- the existing genealogy publication-rule scaffold;
- narrowly scoped safety corrections to that scaffold;
- package, placement, supersession, and migration notes;
- stable links to the owning domain, consent, sensitivity, rights, evidence, runtime, release, correction, and rollback lanes; and
- a bounded inventory of inputs, outputs, tests, bundle membership, and consumers after those facts are verified.

Before adding substantive logic, reviewers must choose one canonical rule home and prevent dual writes.

## What is prohibited

Do not place any of the following here:

- person, family, household, relationship, residence, cemetery, probate, vital-record, or land-record payloads;
- GEDCOM or GEDZip files, family-tree exports, scans, OCR output, source captures, or private notes;
- living-person identifiers, contact details, precise residences, family-graph edges, private tree metadata, or private person-to-parcel joins;
- raw DNA/genomic data, kit or vendor identifiers, sequences, segments, match tables, haplogroups, triangulation hints, or re-identification material;
- consent grants, revocation records, rights records, sensitivity labels, evidence bundles, reviews, receipts, proofs, release manifests, or decision instances;
- contract or schema definitions, source descriptors, validators, runtime code, API routes, UI code, prompts, embeddings, or model weights;
- generated narratives or relationship hypotheses represented as evidence;
- duplicate rules owned by consent, sensitivity, rights, access, identity, promotion, release, or the domain policy lane;
- secrets, credentials, private endpoints, production configuration, or public examples derived from real people or families.

Policy source may consume stable references and public-safe decision summaries. It must not copy protected values into decisions, logs, fixtures, receipts, documentation, or error messages.

## Genealogy trust boundary

### Non-collapse rules

| Keep separate | Why |
|---|---|
| Person assertion vs canonical identity | A source claim or tree node does not authenticate or resolve a person. |
| Relationship assertion vs kinship truth | Confidence, repetition, DNA proximity, or model agreement does not establish a sovereign relationship. |
| Source availability vs source role | Public access does not make a community tree an observed or authority source. |
| Evidence access vs publication rights | A reviewer may inspect material that cannot be redistributed or exposed. |
| Consent vs policy permission | Consent is scoped, time-bound, revocable, and never sufficient by itself. |
| Sensitivity transform vs release | Redaction, aggregation, or generalization still requires validation, review, and release authority. |
| Policy result vs release decision | A policy decision is one gate; it neither promotes nor publishes an artifact. |
| Synthetic fixture pass vs real-world enforcement | Fixture behavior proves only the frozen test profile under its stated constraints. |

### Sensitive classes

Public or semi-public delivery must fail closed when any of the following is unresolved:

- living or possibly living status;
- DNA/genomic derivation or re-identification risk;
- private family relationships, addresses, contact details, or person-to-parcel links;
- burial, cemetery, cultural, community, sovereignty, or harmful-precision concerns;
- evidence, source role, rights, consent, sensitivity, review, release, correction, or rollback state;
- evaluator, bundle, schema, obligation interpreter, consumer, or cache invalidation integrity.

Denial and abstention metadata must not become an oracle for protected facts. Public-safe reasons should remain coarse, stable, and non-enumerating.

## Inputs and outputs

### Current behavior

The current module reads no `input` fields and declares only a default Boolean `allow`. No accepted input contract, reason vocabulary, obligation vocabulary, or normalized decision binding is attached to this package.

### Proposed explicit input profile

A future rule must receive a versioned, schema-valid `PolicyInputBundle` or accepted equivalent and must not fetch missing facts silently.

| Input class | Minimum governed context | Fail-closed condition |
|---|---|---|
| Operation | render, answer, map, graph, export, share, promote, release, correct, withdraw, or rollback; stable request/candidate identity | missing, generic, unsupported, or broader than reviewed scope |
| Actor and audience | authenticated subject/service class, purpose, public/restricted context, project or tenant scope where relevant | unknown actor or audience where admissibility differs |
| Subject posture | stable references; living, deceased, possibly living, or unknown; determination source and time | absent, stale, weakly inferred, or unknown living status |
| Assertion posture | claim type, assertion identity, temporal scope, confidence, contradiction, and review state | relationship or identity presented as fact without provenance |
| Source and evidence | source role, SourceDescriptor and EvidenceBundle refs, citations, freshness, contradiction, and withdrawal state | unresolved, stale, contradicted, withdrawn, or insufficient support |
| Rights and consent | permitted use, redistribution, attribution, embargo, audience, purpose, validity interval, revocation, and downstream duties | unknown, incompatible, expired, revoked, ambiguous, or unverifiable posture |
| Sensitivity | living-person, DNA/genomic, private-family, person-parcel, burial/cultural, mosaic, and precision decisions | missing decision or unsafe detail remains |
| Lifecycle and release | current/requested state, review, release candidate, intended surfaces, correction, withdrawal, and rollback refs | unreviewed or non-release-eligible artifact |
| Execution | exact policy source or bundle digest, evaluator/version, entrypoint, input hash, obligation interpreter, and evaluation time | unknown, incompatible, non-replayable, or failed component |

Input rules:

1. Preserve absent, unknown, conflicted, restricted, revoked, false, and not applicable as distinct states.
2. Treat a person as possibly living when an accepted determination cannot establish otherwise.
3. Never infer consent from public availability, family relationship, tree membership, account access, silence, prior publication, or deceased status.
4. Never let consent override evidence, rights, sensitivity, source role, review, release, or explicit denial.
5. Pass references and minimized decision context across the trust membrane; keep protected payloads in governed stores.
6. Bind evaluation to immutable or content-addressed policy, schema, evidence, and release identities where practical.
7. Hashing or redaction must not create a re-identification channel.

### Outputs and decision-family compatibility

The proposed [`PolicyDecision`](../../contracts/policy/policy_decision.md) schema permits `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`, with policy families `promotion`, `access`, `render`, `capability`, `consent`, and `sensitivity`. `genealogy` is not an admitted family.

Until contracts and schemas are deliberately versioned, a future implementation must compose accepted families or remain unbound; it must not emit an invented production value.

| Outward outcome | Genealogy publication meaning |
|---|---|
| `ANSWER` | The evaluated operation may proceed only after every independent gate passes and every obligation is enforced. It is not release approval. |
| `ABSTAIN` | Policy does not establish a categorical prohibition, but admissible evidence or required context cannot support a trustworthy result. |
| `DENY` | Policy blocks the operation or disclosure for the evaluated audience and purpose. |
| `ERROR` | Shape, integrity, evaluator, bundle, timeout, or obligation-enforcement failure prevents a trustworthy decision. No fallback output is allowed. |

Candidate reason categories include unknown living status, consent absence or revocation, DNA-derived risk, source-role collapse, missing or conflicting evidence, unresolved rights, unsafe precision, private family or parcel linkage, missing review or release state, and evaluator or consumer failure. Exact codes require an accepted registry.

Candidate obligations include redaction or generalization, omission of protected fields, claim-scoped citations, preserved uncertainty and source role, attribution and limitation notices, restricted audience, no caching or export, steward review, decision and transform receipts, expiry, and downstream invalidation after correction or revocation. If a caller cannot prove it enforces every obligation, it must not proceed.

## Exposure, mutation, and retention

| Dimension | Local posture |
|---|---|
| Repository visibility | Public source bytes. Documentation and rule text must therefore contain no protected payload, credential, private endpoint, or reconstruction-enabling example. |
| Operational exposure | Internal policy source. Browsers, maps, exports, search, graphs, Focus Mode, and AI surfaces must consume governed decisions or released derivatives rather than loading repository rule source. |
| Mutation | Versioned Git changes on reviewed feature branches. Substantive rule changes require package, input, outcome, test, bundle, consumer, correction, and rollback evidence. |
| Retention | Durable policy-source history. Superseded rules and migration pointers remain available for replay and audit according to accepted retention controls. |
| Generated state | The package name is generated-style, but no generator or canonical source was proved. Do not regenerate, overwrite, or rename it until provenance is resolved. |
| Decision instances | Prohibited here. Emitted decisions, receipts, reviews, corrections, and release records belong in their accepted process or accountability lanes. |

This v0.2 change updates documentation only. It does not modify `publication.rego`, policy behavior, bundle selection, runtime code, workflow behavior, release state, or public exposure.

## Default posture

The local source is default-false, but a complete genealogy policy must also make missing or failed context explicit:

- unknown living status, rights, consent, sensitivity, source role, evidence, review, or release state produces a non-answer;
- living-person, possibly-living, raw genomic, re-identifying, private-family, and private person-to-parcel public exposure is denied unless an accepted narrower profile explicitly proves otherwise;
- evidence insufficiency produces `ABSTAIN`, not a plausible lineage narrative;
- evaluator, schema, bundle, obligation, or consumer failure produces `ERROR`, never allow;
- a community tree, GEDCOM import, model suggestion, or high score remains candidate/model material until corroborated and reviewed;
- post-transform and post-render artifacts must be rechecked for leakage and mosaic risk;
- stale, corrected, withdrawn, or revoked results must not be served from caches, indexes, graphs, exports, embeddings, tiles, screenshots, or AI context.

## Proposed publication gates

The smallest sound future evaluation composes independent gates:

1. **Request admission** — validate operation, purpose, actor, audience, schema, and bounded scope.
2. **Subject safety** — establish living or possibly-living posture without treating missing evidence as death.
3. **Source-role integrity** — keep community trees, GEDCOM imports, modeled relationships, and AI suggestions in candidate or modeled roles until corroborated.
4. **Evidence sufficiency** — require resolvable, current, claim-scoped evidence; cite or abstain.
5. **Rights and consent** — verify exact use, duration, audience, revocation, redistribution, attribution, and derivative duties.
6. **Sensitivity and re-identification** — assess family-graph, DNA, location, person-parcel, burial/cultural, small-count, and mosaic risks.
7. **Public-safe transformation** — apply only accepted redaction, aggregation, or generalization profiles and validate the derivative again.
8. **Review and release** — require appropriate independent review, an eligible release state, correction path, and rollback target.
9. **Post-generation and render inspection** — inspect the actual API, map, graph, export, search, or AI candidate for leakage and citation closure.
10. **Correction and revocation** — reject stale results and propagate invalidation before delivery or cache reuse.

Failure at any gate produces an explicit non-answer. Never fall back to raw model text, uncited relationship prose, a lower policy version, an internal-store path, or a less restrictive audience.

### Minimum decision matrix

| Synthetic scenario | Expected posture | Critical assertion |
|---|---|---|
| Historical/deceased posture, eligible evidence, compatible rights, safe derivative, review, and release context | Candidate `ANSWER` only after all gates | Historical posture alone is insufficient. |
| Evidence missing, conflicting, stale, or withdrawn | `ABSTAIN` | No plausible lineage narrative is substituted. |
| Subject living, possibly living, or unknown for a public operation | `DENY` or accepted restricted-review route | No identifying or relationship payload leaks. |
| Required consent absent, expired, revoked, or unverifiable | `DENY` | Prior access or publication is not consent. |
| DNA-derived relationship or re-identification hint requested publicly | `DENY` | No raw or inferred genomic linkage is exposed. |
| Community-tree or GEDCOM assertion lacks corroboration | `ABSTAIN` or review hold | Candidate material does not become observed truth. |
| Rights or redistribution posture unresolved | Non-answer | Evidence access does not imply publication rights. |
| Protected identifiers or private family edges appear after transformation | `DENY` | Post-render inspection catches leakage. |
| Bundle, evaluator, schema, or obligation interpreter fails | `ERROR` | Candidate output is not rendered. |
| Correction or revocation affects a prior result | Non-answer plus invalidation | Downstream derivatives become unavailable or visibly stale under accepted policy. |

## Bounded adjacent fixture proof

The adjacent People / DNA / Land implementation now provides one useful but deliberately narrow proof surface:

| Component | Confirmed role | Does not prove |
|---|---|---|
| [`consented_genealogy_overlay.md`](../../contracts/domains/people-dna-land/consented_genealogy_overlay.md) | Defines a synthetic fixture profile and explicit non-effects. | Production identity, kinship, consent, policy, or release semantics. |
| [`consented_genealogy_overlay.schema.json`](../../schemas/contracts/v1/domains/people-dna-land/consented_genealogy_overlay.schema.json) and revocation-manifest schema | Closed fixture shapes for restricted/non-release candidates. | Real consent authenticity or publication safety. |
| [`consent_overlay/`](../../fixtures/domains/people-dna-land/consent_overlay/README.md) | Two valid and 13 exact-invalid synthetic cases. | Coverage of every genealogy, DNA, privacy, or release threat. |
| [`validate_consent_overlay.py`](../../tools/validators/domains/people-dna-land/validate_consent_overlay.py) | Deterministic, fail-closed fixture validator with value-safe findings. | OPA evaluation, `PolicyDecision` emission, source admission, or release. |
| [`test_consent_overlay_safety.py`](../../tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py) | No-network tests for schema closure, hashes, revocation, fixtures, diagnostics, and failure cases. | Runtime consumer enforcement or public operation. |
| [`domain-people-dna-land.yml`](../../.github/workflows/domain-people-dna-land.yml) | Executes the bounded overlay and revocation-propagation profiles on GitHub-hosted runners with read-only contents permission. | Branch-protection significance, production consent, policy activation, promotion, release, or publication. |

The profile intentionally denies public/released state and uses only synthetic sentinels. It does not import or evaluate the package in `publication.rego`. Its findings are validator outcomes, not policy decisions.

## Validation coverage and limits

### Current proof

| Check | Current conclusion |
|---|---|
| README metadata and links | Repository-native validators can check this file's metadata shape and local references. |
| Direct-child inventory | Two-file inventory verified at the pinned base. |
| Rego source inspection | Default and absence of operative rules confirmed from exact bytes; no OPA execution is claimed. |
| Package/consumer search | No exact package consumer found in the tracked tree. |
| Local native policy tests | Not established. |
| Shared genealogy validator scripts | Confirmed placeholder-only. |
| Adjacent consent-overlay profile | Deterministic synthetic tests and workflow wiring exist and are separate from this rule. |
| General policy evaluation | Not established; the broad policy workflow remains a readiness guard. |
| Production enforcement | Unknown. No accepted bundle, evaluator, consumer, decision receipt, release binding, or deployed behavior was proved. |

### Documentation validation commands

From the repository root:

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --profile present \
  --registry control_plane/document_registry.yaml \
  --format text \
  policy/genealogy/README.md

python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  policy/genealogy/README.md

git diff --check
```

These commands validate documentation structure and references only. They do not parse Rego, evaluate policy, inspect branch protection, authenticate review, or approve publication.

### Minimum evidence before rule graduation

1. Resolve canonical placement and package naming through an accepted decision.
2. Correct and review the rule's doctrine/source citation.
3. Accept an explicit, closed input profile and compatible decision-family mapping.
4. Define reviewed reason and obligation vocabularies with public-safe diagnostics.
5. Implement fail-closed rules for every applicable gate.
6. Add deterministic native policy tests using synthetic, public-safe fixtures only.
7. Cover engine-native results and `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` normalization.
8. Bind an immutable rule or bundle identity to a reviewed evaluator and governed consumer.
9. Prove that every consumer enforces all obligations and refuses unknown obligations.
10. Add authenticated, replayable decision evidence without sensitive payloads.
11. Test correction, withdrawal, consent revocation, expiry, supersession, cache invalidation, and rollback.
12. Prove map, graph, search, export, Focus Mode, API, and AI paths cannot bypass the gate.
13. Complete privacy, security, rights, consent, evidence, runtime, and release review.

The repository has no accepted general OPA command for this lane. Do not convert the broad readiness hold into an echo-only success or claim `opa test policy/` coverage until an accepted command, evaluator provenance, entrypoint, and non-vacuous tests are wired.

## Review burden

This lane carries a high review burden because genealogy outputs can expose living people, family relationships, DNA-derived inferences, private residences, land associations, protected sources, and sensitive historical, burial, community, or cultural context.

Every substantive rule or placement change requires:

- policy and People / DNA / Land domain review;
- genealogy assertion and source-role review;
- living-person privacy, consent, rights, and sensitivity review;
- contract and schema review for input or decision changes;
- security and runtime review for evaluator, bundle, logging, caching, or API changes;
- evidence and release review for public-output changes;
- synthetic fixtures and negative-path native tests;
- exact changed-path, package, bundle, evaluator, consumer, and rollback inventory;
- correction, withdrawal, revocation, expiry, and downstream invalidation evidence; and
- human approval distinct from generation and automated validation.

`CODEOWNERS` routes `policy/` review to `@bartytime4life`. That is repository routing only; it is not a StewardshipAssignment, independent approval record, policy acceptance, release approval, or proof of separation of duties.

## Related contracts, schemas, fixtures, tests, and release

| Responsibility | Owning surface |
|---|---|
| Policy root and current maturity | [`policy/`](../README.md) |
| Canonical domain policy candidate | [`policy/domains/people-dna-land/`](../domains/people-dna-land/README.md) |
| Consent and sensitivity composition | [`policy/consent/people-dna-land/`](../consent/people-dna-land/README.md) and [`policy/sensitivity/`](../sensitivity/README.md) |
| Rights admissibility | [`policy/rights/`](../rights/README.md) |
| Genealogy domain doctrine | [`docs/domains/people-dna-land/sublanes/genealogy.md`](../../docs/domains/people-dna-land/sublanes/genealogy.md) |
| Genealogy semantic planning boundary | [`contracts/domains/people-dna-land/genealogy/`](../../contracts/domains/people-dna-land/genealogy/README.md) |
| Synthetic consent-overlay profile | [`contracts/domains/people-dna-land/consented_genealogy_overlay.md`](../../contracts/domains/people-dna-land/consented_genealogy_overlay.md) |
| Fixture schemas | [`schemas/contracts/v1/domains/people-dna-land/`](../../schemas/contracts/v1/domains/people-dna-land/README.md) |
| Genealogy scenario index | [`fixtures/domains/people-dna-land/genealogy/`](../../fixtures/domains/people-dna-land/genealogy/README.md) |
| Executable adjacent fixtures | [`fixtures/domains/people-dna-land/consent_overlay/`](../../fixtures/domains/people-dna-land/consent_overlay/README.md) |
| Shared genealogy validator boundary | [`tools/validators/genealogy/`](../../tools/validators/genealogy/README.md) |
| Executable adjacent validator | [`tools/validators/domains/people-dna-land/validate_consent_overlay.py`](../../tools/validators/domains/people-dna-land/validate_consent_overlay.py) |
| Executable adjacent tests | [`tests/domains/people-dna-land/consent/revocation/`](../../tests/domains/people-dna-land/consent/revocation/README.md) |
| Policy decision contract and schema | [`contracts/policy/policy_decision.md`](../../contracts/policy/policy_decision.md) and [`policy_decision.schema.json`](../../schemas/contracts/v1/policy/policy_decision.schema.json) |
| Policy runtime | [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) |
| Public trust membrane | [`apps/governed-api/`](../../apps/governed-api/README.md) |
| Release, correction, withdrawal, rollback | [`release/`](../../release/README.md) |
| People / DNA / Land bounded checks | [`domain-people-dna-land.yml`](../../.github/workflows/domain-people-dna-land.yml) |
| Broad policy readiness | [`policy-test.yml`](../../.github/workflows/policy-test.yml) |

## ADRs and placement decisions

| Decision | Current status | Relevance |
|---|---:|---|
| [ADR-0029 — adopt Directory Governance Standard v2](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **ACCEPTED** | Makes Directory Rules v2 effective for policy-root placement, domain-lane patterns, and README profiles. |
| [ADR-0003 — singular policy root](<../../docs/adr/ADR-0003-policy-singular-is-canonical-(policies-is-compatibility).md>) | **PROPOSED** | Narrow root-compatibility decision; accepted Directory Rules already establish the singular root. |
| [ADR-0010 — deny by default for sensitive classes](../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | **DRAFT / effective PROPOSED** | Useful candidate posture for DNA and other protected classes; not accepted enforcement proof. |
| [ADR-0020 — abstain is first class](../../docs/adr/ADR-0020-abstain-is-a-first-class-decision.md) | **PROPOSED** | Defines candidate separation of evidence insufficiency from categorical denial and process failure. |
| Genealogy placement, package normalization, and policy-family mapping | **NOT FOUND / NEEDS DECISION** | This README does not create or accept the missing decision. |

## Migration, correction, revocation, and rollback

### Documentation correction

If this README overstates current authority or behavior, correct it through a reviewed forward fix. Before merge, close or abandon the draft PR. After merge, revert the documentation commit or restore baseline blob `b12f21e204bb753b745d49812798c6894d4f308c` through normal Git history. Reverting documentation does not alter policy behavior because this revision changes no rule or runtime surface.

### Placement migration

If an accepted decision selects `policy/domains/people-dna-land/` or another canonical lane:

1. inventory every genealogy rule, package, test, fixture, bundle reference, validator, contract, schema, workflow, consumer, receipt, and release dependency;
2. select one canonical destination and one package namespace;
3. record old and new paths, exact hashes, owners, effective time, consumers, and rollback target;
4. move rule and native tests together without changing semantics unless the behavior change is separately reviewed;
5. leave this README as a frozen forward pointer or retire it only under the accepted migration plan;
6. prohibit independent writes at the old path;
7. repair references and rerun package, bundle, evaluator, consumer, correction, and rollback checks; and
8. preserve historical decisions, reviews, receipts, releases, and replay evidence.

### Future active-policy correction and rollback

A future active-policy response must disable unsafe delivery first, select a previously verified rule/bundle/evaluator combination by immutable identity, replay representative decisions, preserve audit history, issue correction or withdrawal records where required, and invalidate affected caches, indexes, graphs, exports, tiles, screenshots, embeddings, Focus Mode results, and AI context. If no safe prior version exists, fail closed.

A Git revert of this README or a rule file is not, by itself, correction of a previously exposed derivative.

## Open verification register

| ID | Question | Current state |
|---|---|---:|
| GEN-POL-001 | Is `policy/genealogy/` a canonical cross-cutting policy family, a compatibility path, or a migration source for `policy/domains/people-dna-land/`? | **CONFLICTED / NEEDS DECISION** |
| GEN-POL-002 | Is genealogy a standalone People / DNA / Land sublane or part of the people sublane? | **CONFLICTED in domain documentation** |
| GEN-POL-003 | Who owns genealogy policy, living-person privacy review, consent review, and independent approval? | **NEEDS VERIFICATION** |
| GEN-POL-004 | What accepted source replaces the stale DNA-only comment in `publication.rego`? | **NEEDS VERIFICATION** |
| GEN-POL-005 | What are the accepted package, version, entrypoint, input profile, and bundle membership? | **UNKNOWN** |
| GEN-POL-006 | How does genealogy compose into the six current `PolicyDecision.policy_family` values, or what versioned schema change is required? | **NEEDS DECISION** |
| GEN-POL-007 | Which reason codes, obligations, and public-safe diagnostics are accepted? | **PROPOSED / registry unproved** |
| GEN-POL-008 | Which native Rego tests and synthetic fixtures prove the publication gate? | **NOT ESTABLISHED** |
| GEN-POL-009 | Which accepted evaluator and governed consumer enforce the decision and every obligation? | **UNKNOWN** |
| GEN-POL-010 | What decision receipt, replay, expiry, correction, withdrawal, and revocation propagation contract applies? | **PARTIAL adjacent fixture proof / active flow unknown** |
| GEN-POL-011 | Which GitHub checks are required and which independent approvals are enforced? | **UNKNOWN** |
| GEN-POL-012 | What deployment and release evidence proves public-surface enforcement without a bypass? | **UNKNOWN** |

## Last reviewed

**2026-08-13** against `main@3e6db4917f89d71331d7f46c08dc64c5000558bf`.

Reviewed:

- the complete v0.1 target and exact two-file directory inventory;
- `publication.rego`, its package, default, source comment, and bounded consumer search;
- accepted ADR-0029, Directory Rules v2 §§9.3, 12.2, and 16, and the root registry projection;
- the policy root, People / DNA / Land policy stubs, and genealogy domain doctrine;
- genealogy contracts, schema indexes, fixture indexes, and shared validator placeholders;
- the consent-overlay contract, schemas, synthetic fixtures, validator, tests, and People / DNA / Land workflow;
- policy decision contract/schema, broad policy workflow, policy runtime, CODEOWNERS, contribution rules, and pull-request template.

Not established:

- accepted local owners, scope ID, placement, package, entrypoint, bundle, or evaluator;
- native genealogy publication-policy tests or a normalized decision binding;
- production consumer imports, authenticated decisions, receipts, replay, expiry, or audit sink;
- real consent verification, correction propagation, cache invalidation, release integration, deployment, or public operation;
- branch-protection, ruleset-required checks, or independently enforced review.

Re-review when placement, package, rule logic, source citation, inputs, outcomes, schemas, tests, bundle membership, evaluator, consumer, consent/sensitivity posture, release integration, correction, withdrawal, revocation, or rollback evidence changes.

## No-loss and evidence ledger

| v0.1 element | v0.2 disposition |
|---|---|
| Stable path, document ID, and genealogy publication purpose | Preserved; H1 and metadata normalized to the current directory-contract style. |
| Compatibility and placement conflict | Preserved; reconciled to accepted ADR-0029 and current domain-lane law. |
| Default-false rule and stale source citation | Preserved; exact current rule inventory and consumer/test limits added. |
| Assertion-first genealogy doctrine | Preserved and strengthened with explicit non-collapse rules. |
| Living-person, DNA, private-family, and person-parcel safeguards | Preserved without adding sensitive examples. |
| Belongs and exclusions | Preserved; aligned to root-registry responsibility and public repository visibility. |
| Proposed inputs and invariants | Preserved; clearly separated from the current input-free scaffold. |
| Boolean-vs-`PolicyDecision` distinction | Preserved; current six-family schema constraint made explicit. |
| Outcomes, reason categories, and obligations | Preserved as proposed, not accepted runtime vocabulary. |
| Ten publication gates and representative scenarios | Preserved and reconciled to current evidence. |
| Validation and activation checklist | Preserved; stale broad-command implication removed and adjacent executable proof added. |
| Review, migration, correction, and rollback | Preserved; current baseline blob and no-publication correction limit added. |
| Related surfaces and ADRs | Preserved; accepted and proposed decision states updated. |
| Direct-child map, exposure/mutation/retention, open register | Added to satisfy the current `BOUNDARY_COMPACT` contract. |
| July claim that genealogy validation was entirely placeholder-only | Narrowed: shared genealogy scripts remain placeholders, while a separate consent-overlay fixture profile is now executable. |

## Changelog

| Version | Date | Change | Rollback |
|---|---|---|---|
| v0.1 | 2026-07-22 | Replaced an effectively empty README with a repository-grounded genealogy publication boundary and compatibility warning. | Historical Git revision. |
| v0.2 | 2026-08-13 | Reconciles accepted Directory Rules, valid metadata, exact child map, current rule limits, adjacent consent-overlay proof, exposure and retention, decision-family constraints, validation, migration, and no-loss evidence. Documentation only. | Revert this README commit or restore baseline blob `b12f21e204bb753b745d49812798c6894d4f308c`; no policy runtime state changes. |

<p align="right"><a href="#top">Back to top</a></p>
