<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/domains/people-dna-land
title: People, DNA, and Land Domain Policy Boundary and Activation Contract
type: readme; directory-readme; domain-policy-boundary; policy-index
version: v0.2
status: draft; repository-grounded; mixed-maturity; T4-baseline-projection; direct-proposed-rego-scaffolds; two-synthetic-fixture-profiles; evaluator-unbound; fail-closed-public-edge; non-release; non-publication
owners: "@bartytime4life — verified CODEOWNERS review route; People, genealogy, DNA/genomic, consent, privacy, land/title, source, rights, sensitivity, evidence, policy, contract/schema, validation, runtime, release, security, and documentation stewardship assignments NEEDS VERIFICATION"
created: 2026-05-08
updated: 2026-08-13
supersedes: unversioned greenfield scaffold
policy_label: restricted-review; policy; people-dna-land; living-person; genealogy; dna-genomic; consent-revocation; land-title-sensitive; person-parcel-join; T4-baseline; source-role-aware; rights-aware; sensitivity-aware; evidence-bound; cite-or-abstain; reconstruction-resistant; release-gated; correction-aware; rollback-aware; no-public-authority
current_path: policy/domains/people-dna-land/README.md
owning_root: policy/
responsibility: >-
  Define and index the People, DNA, and Land-specific admissibility-policy boundary: the
  bounded operations that may be evaluated, the governed context they require, the finite
  decisions and obligations an accepted evaluator would emit, and the conditions that must
  remain held or denied. This README does not establish person identity, kinship, DNA or
  genomic truth, consent validity, land title, ownership, parcel boundaries, evidence closure,
  policy activation, release, or publication.
truth_posture: >-
  CONFIRMED direct lane inventory of this README, seven proposed Rego scaffolds, six empty
  compatibility or sublane directories, and one non-empty consent subdirectory; CONFIRMED two
  bounded synthetic consent fixture profiles with 25 deterministic no-network tests, two
  substantive validators, and a domain workflow whose proof and release jobs remain explicit
  holds; CONFIRMED a parent-level policy/domains/people/ legacy sibling whose README is one
  blank byte and whose identity is absent from the machine register; PROPOSED People-DNA-Land
  T4 baseline machine projection, policy composition, decision normalization, package
  convergence, and activation requirements; CONFLICTED five deny-named
  or deny-shaped Rego stubs that default deny to false versus two allow-shaped stubs that
  default allow to false, multiple package namespaces, a sparse unregistered people sibling,
  and duplicated SCOPE_AND_BOUNDARY and SENSITIVITY document bytes; UNKNOWN accepted policy
  bundle, manifest, selector, evaluator, normalized input assembler, native Rego test harness,
  production consumer, obligation handlers, decision receipts, revocation executor, promotion
  binding, runtime enforcement, and rollback drill; NEEDS VERIFICATION functional steward
  assignments, accepted default-result semantics, naming migration, source and identity
  authority, consent and rights currency, sensitivity transforms, independent review,
  public-surface enforcement, correction propagation, cache invalidation, and emergency
  deactivation.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 299c8a81325689c68a38304ce7b14921342dcdd0
  prior_blob: 571a4a6d5c8ba7cf6c1fa9fcdd63da88bc05eb2a
  policy_root_blob: 6c5021f9d92778581a4e9331a9dd6ddb7efc5e35
  policy_domains_parent_blob: ed9be975c9da2c7d77d94fab621db39f23953813
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  domain_lane_register_blob: 1bfc6f91cfa713a5e3d51ece011b63b46310734f
  people_legacy_readme_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  people_dna_land_docs_readme_blob: 19a3ea59bab2d5e04c73f402a35048c1a55ab071
  people_dna_land_contract_readme_blob: d99e7fc318f34fbeb90a1ee31658f5121b8ffd38
  people_dna_land_schema_readme_blob: fbe5557ff4e19d1b70a97d284ab1743dd3d08f29
  consent_policy_readme_blob: fa7ea7c95a473a7fd498053536ca0b72b17461f6
  sensitivity_person_parcel_blob: f641d963394971fe8ba36e601c113fcfb2a380b1
  fixture_readme_blob: 8eb10804c587c62edf1eb9750c2c82b5cf237f2a
  test_readme_blob: ecdaac8e2509d07e39279e23e99273a15716d053
  validator_readme_blob: 7a78d278aa03d843107d4d66a954c7a670d2ac19
  workflow_blob: bcf64c3e3b6653b9543489fc5a6031805ae3ef48
  consent_overlay_validator_blob: b2ff0e5037de0f1c22486743ab5e20926c68474d
  revocation_assessment_validator_blob: 76c7805428f253a7a711c7bc68a27e9cbcce40e7
  abstain_on_ambiguous_blob: 04be32ebc939fa0d0a3ee7a3f4b611bee702b582
  consent_validator_rego_blob: 820daa2199be24f0f651404367d89576f96a825f
  deny_unpublished_blob: 17bb64085c98387baf70837a6ccd62be19dcdb65
  dna_restricted_blob: d174e586b63b282c6e75ea62804072e7abb00399
  living_person_blob: ba3a55dcc14bee79f815358a4945a91a01c23b0c
  living_person_redaction_blob: 32607517aeb919aeb253757beddc22a5508e9706
  dna_consent_revocation_blob: bb4400e4995bb2381bcb88782a3ff97ea272ebd0
related:
  - ../README.md
  - ../../README.md
  - ../../consent/people-dna-land/README.md
  - ../../sensitivity/people-dna-land/person_parcel_join.deny.rego
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md
  - ../../../docs/domains/people-dna-land/DNA_HANDLING.md
  - ../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md
  - ../../../contracts/domains/people-dna-land/README.md
  - ../../../schemas/contracts/v1/domains/people-dna-land/README.md
  - ../../../fixtures/domains/people-dna-land/README.md
  - ../../../tests/domains/people-dna-land/README.md
  - ../../../tools/validators/domains/people-dna-land/README.md
  - ../../../pipeline_specs/people-dna-land/README.md
  - ../../../pipelines/domains/people-dna-land/README.md
  - ../../../packages/domains/people-dna-land/README.md
  - ../../../data/registry/sources/people-dna-land/README.md
  - ../../../data/proofs/people-dna-land/README.md
  - ../../../release/candidates/people-dna-land/README.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "Accepted ADR-0029 adopts the exact Directory Rules v2 bytes despite the adopted document's preserved proposal-era header. The ADR controls decision status."
  - "people-dna-land is the registered domain segment; people_dna_land is its projected code alias. The parent-level people sibling now contains a one-blank-byte README but is not a registered compatibility alias."
  - "The proposed domain-lane projection records a T4 baseline; that projection cannot authorize access, disclosure, downgrade, release, or publication."
  - "No real living-person data, DNA/genomic material, consent credential, person-parcel join, or title assertion belongs in this public README."
  - "No source, policy bundle, evaluator, proof, release, deployment, or publication is activated by this README."
-->

<a id="top"></a>

# policy/domains/people-dna-land

> **One-line purpose.** `policy/domains/people-dna-land/` is the People, DNA, and Land-specific admissibility boundary: it may eventually decide whether a governed operation involving person assertions, genealogy, DNA-derived evidence, consent, or land-linked claims can proceed, but it cannot create identity, kinship, genomic, consent, title, ownership, boundary, release, or publication truth.

[![Status: draft](https://img.shields.io/badge/status-draft-d4a72c?style=flat-square)](#current-status)
[![Sensitivity: T4 baseline projection](https://img.shields.io/badge/sensitivity-T4%20baseline%20projection-b42318?style=flat-square)](#people-dna-land-safety-invariants)
[![Runtime: evaluator unbound](https://img.shields.io/badge/runtime-evaluator%20unbound-6b7280?style=flat-square)](#activation-and-definition-of-done)
[![Public edge: deny by default](https://img.shields.io/badge/public%20edge-deny%20by%20default-9f1239?style=flat-square)](#public-surface-contract)

> [!IMPORTANT]
> **Policy is not person, DNA, consent, or title truth.** A People–DNA–Land policy decision can evaluate only an explicit governed input assembled from independently owned contracts, schemas, sources, evidence, rights, consent, sensitivity, lifecycle, review, correction, and release state. A filename, directory, validator, workflow, map, search result, or generated answer cannot supply those authorities.

<!-- callout boundary -->

> [!CAUTION]
> **The direct Rego lane is not an active policy system.** Five direct modules currently declare `default deny := false`; two declare `default allow := false`; none contains an operative rule. Their result names, truth polarity, and package namespaces do not form one accepted decision interface, and no accepted bundle, selector, evaluator, native Rego suite, production consumer, or release binding was observed. Do not infer fail-closed enforcement from sensitive filenames.

<!-- callout boundary -->

> [!WARNING]
> **No public path exists by default for protected material.** Real living-person details, raw or segment-level DNA/genomic data, consent or revocation credentials, private genealogy links, private person-parcel joins, and source-bound title material must remain outside public artifacts. Public use requires a separately governed, evidence-bound, rights-cleared, consent-aware, sensitivity-reviewed, non-reconstructable derivative and an accepted release decision.

<!-- callout boundary -->

> [!NOTE]
> Two bounded synthetic profiles are executable: a consent-safe genealogy-overlay fixture profile and an inactive consent-revocation propagation assessment. Their 25 no-network tests establish only the declared synthetic shapes and failure polarities. They do not validate real people, real consent, legal sufficiency, kinship, DNA findings, land title, cleanup execution, policy activation, release, or publication.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-and-current-status) · [Ownership](#ownership-and-non-ownership) · [Safety](#people-dna-land-safety-invariants) · [Inventory](#direct-lane-inventory) · [Scope](#what-belongs-here) · [Inputs](#required-policy-input) · [Decisions](#decision-and-obligation-contract) · [Surfaces](#public-surface-contract) · [Lifecycle](#lifecycle-and-temporal-behavior) · [Naming](#identity-naming-and-versioning) · [Validation](#validation-and-failure-semantics) · [Review](#review-burden) · [Activation](#activation-and-definition-of-done) · [Correction](#correction-revocation-and-invalidation) · [Rollback](#rollback-and-recovery) · [Map](#related-responsibility-roots) · [ADRs](#governing-decisions-and-doctrine) · [Backlog](#open-verification-register) · [Evidence](#last-reviewed-evidence) · [History](#revision-history)

---

## Purpose

This directory is the canonical `policy/` segment for **People, DNA, and Land-specific admissibility questions**. It is where accepted machine policy may eventually decide whether a bounded operation can proceed and which restrictions, holds, denials, or obligations must follow.

Typical questions include:

- whether a person assertion or genealogy relation has enough governed evidence to be evaluated;
- whether an operation concerns a living person, a historical person, an unresolved identity candidate, or multiple subjects with different permissions;
- whether DNA-derived evidence may be used for the requested purpose without exposing raw genomic material, segment data, kit identifiers, or re-identifying combinations;
- whether consent is current, in scope, audience-specific, purpose-specific, time-bounded, and unrevoked for every affected subject;
- whether a land record is an instrument, assessor or tax record, parcel geometry, occupancy assertion, ownership interval, or title claim—and whether the requested language preserves that distinction;
- whether a person-to-parcel or genealogy-to-land join raises sensitivity beyond every input;
- whether a public API, map, tile, graph, index, cache, export, Evidence Drawer, Focus Mode, or AI answer can expose a non-reconstructable released derivative;
- whether a revocation, correction, dispute, supersession, or withdrawal requires immediate denial and downstream invalidation;
- which receipts, review records, proof references, correction targets, and rollback obligations remain outstanding.

This README is both a **directory boundary** and a **maturity index**. It states what an accepted People–DNA–Land policy system must guarantee while distinguishing that target from the implementation evidence currently present.

It does not itself:

- resolve a person, assign identity, or establish personhood;
- establish biological or social kinship;
- interpret raw DNA, genotype, haplotype, segment, match, or medical information;
- grant, authenticate, revoke, or legally interpret consent;
- determine deed validity, chain of title, ownership, occupancy, legal description, parcel boundary, lien, heirship, or legal interest;
- admit, retrieve, rank, or activate a source;
- create an `EvidenceBundle`, receipt, proof, review record, policy decision, or release record;
- perform redaction, aggregation, generalization, tokenization, pseudonymization, withdrawal, or cache invalidation;
- move an artifact through lifecycle states;
- approve a candidate, release, deployment, publication, alert, notification, or public claim;
- replace specialist, rights-holder, privacy, consent, historical, land-record, or legal review.

<p align="right"><a href="#top">Back to top</a></p>

---

## Authority and current status

### Authority chain

The governing chain is:

1. accepted [`ADR-0029`](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact bytes of the [Directory Rules](../../../docs/doctrine/directory-rules.md);
2. Directory Rules place admissibility rules under singular `policy/` and use `people-dna-land` only as a domain segment;
3. the [`policy/` root contract](../../README.md) defines the repository-wide policy boundary;
4. the [`policy/domains/` parent](../README.md) defines domain-policy composition and identifies `people-dna-land/` as the canonical child;
5. the proposed [`domain_lane_register.yaml`](../../../control_plane/domain_lane_register.yaml) projects lane ID `people-dna-land`, code alias `people_dna_land`, and a T4 sensitivity baseline;
6. this README narrows that responsibility without superseding shared consent, sensitivity, evidence, rights, review, release, correction, or rollback authority.

The Directory Rules document retains proposal-era control text because ADR-0029 adopted those exact bytes. The accepted ADR—not the preserved header—controls adoption status.

### Current status

| Question | Repository-grounded answer |
| --- | --- |
| Does the directory exist? | **CONFIRMED.** It contains this README, six root Rego files, one non-empty `consent/` subdirectory, and six empty subdirectories. |
| Is this the canonical domain-policy segment? | **CONFIRMED placement.** `policy/` owns admissibility; `people-dna-land` is the registered domain segment. |
| Is the lane registered? | **CONFIRMED presence / PROPOSED projection.** The machine register records `lane_id: people-dna-land`, `code_alias: people_dna_land`, and a T4 baseline but declares itself `machine_projection_only`. |
| Is `policy/domains/people/` an accepted alias? | **NO evidence.** It now contains a one-blank-byte README, remains absent from the machine register, and has no accepted mapping. The unchanged parent inventory predates that blank file and still describes the directory as having no README. |
| Are operative direct rules present? | **NO.** Seven Rego files are proposed scaffolds containing defaults only; five default `deny` to false and two default `allow` to false. |
| Are any People–DNA–Land profiles executable? | **YES, bounded.** Two synthetic consent fixture profiles have substantive validators and 25 deterministic tests. They do not execute the direct Rego files. |
| Is the direct Rego set normalized? | **NO.** Result names, truth polarity, package namespaces, entrypoints, and responsibility split conflict. |
| Is an accepted bundle or evaluator bound? | **UNKNOWN / not observed.** No accepted bundle manifest, selector, native Rego harness, runtime consumer, or decision-receipt binding was established by the reviewed evidence. |
| Is proof production active? | **NO.** The domain workflow intentionally holds because no accepted proof producer or deterministic proof command exists. |
| Is release dry-run active? | **NO.** The workflow intentionally holds because no accepted domain release command or candidate-manifest contract exists. |
| May public clients consume protected material? | **NO.** Public clients remain governed-interface-only and may receive only released, public-safe, non-reconstructable derivatives. |
| Does this README activate anything? | **NO.** It changes documentation only. |

### Authority ceiling

This directory may own **People–DNA–Land-specific policy source and its local explanatory index** after each artifact satisfies its own placement, package, input, output, review, activation, and rollback gates. It may reference—but never absorb—the following authorities:

- domain doctrine in [`docs/domains/people-dna-land/`](../../../docs/domains/people-dna-land/README.md);
- semantic meaning in [`contracts/domains/people-dna-land/`](../../../contracts/domains/people-dna-land/README.md);
- machine shape in [`schemas/contracts/v1/domains/people-dna-land/`](../../../schemas/contracts/v1/domains/people-dna-land/README.md);
- source identity, role, and terms in governed registries;
- evidence support and conflict state in evidence objects and resolvers;
- consent, rights, privacy, sensitivity, cultural, sovereignty, and geoprivacy decisions in their owning lanes;
- lifecycle state in `data/`;
- executable evaluation in runtime or service code;
- receipts and proofs in their canonical stores;
- candidate, release, correction, withdrawal, and rollback state in `release/` and governed lifecycle records;
- human review and GitHub transition control.

If an answer depends on authority absent from the current governed input, the policy path must **hold, abstain, deny, or error**. It must not reconstruct missing authority from a name, file path, family tree, DNA match score, parcel, map, model, prompt, prior decision, or public-record appearance.

<p align="right"><a href="#top">Back to top</a></p>

---

## Ownership and non-ownership

### Local responsibility

Subject to accepted package, input, output, and activation contracts, this lane may own:

- People–DNA–Land-specific admissibility predicates;
- domain-specific reason and obligation codes;
- explicit deny, restrict, hold, and abstain conditions;
- living-person, genealogy, DNA-derived, consent, land-claim, and person-parcel operation constraints unique to this domain;
- rules that require source-role, evidence, consent, rights, sensitivity, lifecycle, review, and release decisions to compose without weakening one another;
- public-safe field, relation, precision, audience, and purpose profiles after review;
- local package and entrypoint declarations after acceptance;
- documentation references for paired fixtures, tests, validators, bundle membership, evaluator bindings, consumers, correction, and rollback.

### Non-ownership matrix

| This lane does not own | Owning responsibility | Required relationship |
| --- | --- | --- |
| Human domain doctrine and scope | [`docs/domains/people-dna-land/`](../../../docs/domains/people-dna-land/README.md) | Cite as draft guidance; do not execute prose as policy. |
| Person, relationship, DNA-evidence, consent, land-instrument, or ownership semantics | [`contracts/domains/people-dna-land/`](../../../contracts/domains/people-dna-land/README.md) | Consume contract-defined concepts without redefining them. |
| JSON shape and serialization | [`schemas/contracts/v1/domains/people-dna-land/`](../../../schemas/contracts/v1/domains/people-dna-land/README.md) | Validate shape before semantic policy evaluation. |
| Person identity resolution | Governed identity contracts, evidence, review, and services | Evaluate a supplied resolution state; never mint identity. |
| Biological or social kinship truth | Evidence, domain contracts, and specialist review | Preserve assertion, hypothesis, confidence, conflict, and review state. |
| Raw DNA/genomic storage or interpretation | Restricted source/runtime lanes outside public repository artifacts | Accept references and governed posture only; never raw payloads. |
| Consent grant, authentication, or revocation execution | [`policy/consent/people-dna-land/`](../../consent/people-dna-land/README.md) plus accepted consent services and records | Compose a current purpose- and audience-bound result; do not self-grant. |
| Rights, privacy, or sensitivity classification | Shared policy families and reviewed source terms | Apply the most restrictive current decision. |
| Land title, legal interest, or boundary adjudication | Authoritative instruments, source roles, evidence, specialist review, and applicable law | Preserve claim type and limitations; never convert administrative geometry to title truth. |
| Source identity, role, authority, terms, or activation | [`data/registry/sources/people-dna-land/`](../../../data/registry/sources/people-dna-land/README.md) and source governance | Resolve immutable governed references; never promote source role. |
| Evidence sufficiency or provenance truth | Evidence contracts, resolvers, and policy/evidence | Consume current evidence state; cite or abstain. |
| Redaction or withdrawal execution | Governed pipelines and shared redaction/correction lanes | Require transform identity and receipt; policy emits obligations only. |
| Pipeline execution | [`pipelines/domains/people-dna-land/`](../../../pipelines/domains/people-dna-land/README.md) | Pipeline obeys policy; execution success cannot mint approval. |
| Declarative run intent | [`pipeline_specs/people-dna-land/`](../../../pipeline_specs/people-dna-land/README.md) | A spec requests evaluation; it cannot activate policy or release. |
| Fixtures and executable proof | [`fixtures/domains/people-dna-land/`](../../../fixtures/domains/people-dna-land/README.md) and [`tests/domains/people-dna-land/`](../../../tests/domains/people-dna-land/README.md) | Fixtures are synthetic examples; tests prove only declared scope. |
| Validator implementation | [`tools/validators/domains/people-dna-land/`](../../../tools/validators/domains/people-dna-land/README.md) | Validators check bounded inputs; they do not approve policy or release. |
| Shared helper implementation | [`packages/domains/people-dna-land/`](../../../packages/domains/people-dna-land/README.md) | Helpers preserve decisions and references; they cannot create authority. |
| Lifecycle storage | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, catalogs, receipts, proofs, and published carriers | Policy emits a decision; an authorized producer performs any transition. |
| Proof production | [`data/proofs/people-dna-land/`](../../../data/proofs/people-dna-land/README.md) and accepted producers | A policy result is not a proof or proof pack. |
| Release approval or rollback authority | [`release/candidates/people-dna-land/`](../../../release/candidates/people-dna-land/README.md), manifests, corrections, and rollback lanes | Require reviewed current release state; never self-approve. |
| Public API, UI, map, graph, index, export, or AI behavior | Governed application/runtime lanes | Consumers enforce authenticated decisions and obligations; they do not reinterpret them. |

### Review routing is not stewardship

The current [CODEOWNERS](../../../.github/CODEOWNERS) routes `/policy/` review to `@bartytime4life`. That is a verified GitHub review route, not proof of People–DNA–Land stewardship, privacy or consent authority, land-record expertise, independent approval, policy activation, release approval, or publication permission. Functional assignments remain **NEEDS VERIFICATION**.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="people-dna-land-safety-invariants"></a>

## People–DNA–Land safety invariants

These invariants apply even when a narrower file, fixture, workflow, or consumer is incomplete.

### 1. Living-person material fails closed

Protected living-person attributes, relationships, locations, contacts, household links, status, inferred traits, and sensitive combinations must not reach public surfaces unless a current governed path explicitly authorizes a minimized, public-safe derivative for the exact purpose and audience.

Unknown living/deceased status does not become deceased by default. Ambiguity takes the stricter posture.

### 2. DNA and genomic material has no raw public path

Raw genotype, sequence, segment coordinates, haplotypes, kit/vendor identifiers, match lists, credentials, salts, private tokens, health-adjacent interpretations, and reconstructable derivatives do not belong in public artifacts, logs, URLs, screenshots, fixtures, maps, exports, or generated answers.

DNA-derived evidence must remain an explicitly restricted evidence class. A match score or shared segment is not, by itself, identity or kinship proof.

### 3. Consent is necessary where required and never sufficient

Consent is scoped to subjects, purpose, operation, audience, fields or relations, precision, derivation, export, and time. Missing, stale, unverifiable, expired, suspended, disputed, or revoked consent fails closed.

A consent result cannot waive evidence, source-role, rights, privacy, sensitivity, review, release, correction, or rollback requirements. Consent by one person cannot silently authorize disclosure about another.

### 4. Person identity remains assertion-first

Names, identifiers, dates, residences, family links, documents, DNA hints, and graph proximity are evidence-bearing assertions, not automatic canonical identity. Conflicts, alternatives, confidence, source role, temporal scope, and review state remain visible.

Policy may evaluate whether a supplied identity state is admissible for a bounded operation. It cannot resolve the identity itself.

### 5. Relationship hypotheses never silently become fact

Biological, adoptive, legal, household, social, and inferred relationships are distinct. A genealogy hypothesis must preserve its relationship type, evidence basis, confidence, contradictions, temporal scope, and review state.

Generated language must not upgrade a candidate relationship to confirmed kinship.

### 6. Administrative land records are not title truth

Assessor, tax, address, occupancy, mailing, or parcel records may support administrative context. They do not automatically establish legal ownership, chain of title, boundary, deed validity, heirship, lien priority, or present legal interest.

Every land-linked claim must preserve source role, instrument type, effective time, supersession, jurisdiction, geometry version, and legal limitations.

### 7. Parcel geometry is not a legal boundary

A parcel polygon or cadastral representation is a versioned spatial aid. It must not be described as a surveyed or adjudicated boundary unless the governing evidence and review explicitly support that exact claim.

Geometry changes, splits, merges, identifier reuse, and temporal mismatch must remain visible.

### 8. Joins inherit the strictest posture

Joining person, genealogy, DNA-derived, land, address, parcel, infrastructure, historical, or other domain records can create new sensitivity even when each input appears public separately. The output must inherit the most restrictive applicable rights, consent, sensitivity, evidence, lifecycle, and release obligations.

A private person-parcel join has no public path by default.

### 9. Source role never upgrades through processing

An index, aggregator, tree, model, assessor extract, map, normalized record, graph projection, crosswalk, or generated summary cannot become identity, kinship, DNA, title, or boundary authority merely because it was validated, joined, rendered, cited, or released.

### 10. Evidence outranks generated language

Generated text, rankings, embeddings, graph paths, similarity, or AI confidence cannot replace current governed evidence. Consequential answers cite their support or abstain.

### 11. Public safety is cross-surface and reconstruction-aware

A field can be harmless alone and harmful when combined across API responses, tiles, maps, graphs, search indexes, exports, caches, screenshots, stories, or AI context. Review the composition, not only each carrier.

Policy must prevent differencing, linkage, inference, and reconstruction attacks across surfaces and time.

### 12. Release is a separate state

Schema validity, validator success, policy evaluation, consent satisfaction, review, or proof does not create a release. Public use requires an accepted release record that binds the exact artifact, decision set, obligations, transforms, evidence, and rollback target.

### 13. Revocation and correction restrict immediately

When consent, evidence, identity, relationship, rights, sensitivity, land state, or release support becomes less permissive, new use must stop immediately. Downstream graph, search, vector, cache, map, export, story, and AI surfaces remain held until invalidation or withdrawal is proved.

### 14. Non-publishers remain non-publishers

Watchers, validators, policy evaluators, indexers, models, reviewers, and documentation workflows cannot publish. They may report, deny, abstain, hold, or request review only within their accepted contracts.

<p align="right"><a href="#top">Back to top</a></p>

---

## What belongs here

- this README as the local boundary and maturity index;
- reviewed People–DNA–Land-specific Rego, OPA-compatible, or equivalent declarative policy source;
- rules for living-person, genealogy, DNA-derived, consent, land-claim, and private join admissibility;
- domain-specific source-role, evidence, rights, consent, sensitivity, precision, public-exposure, stale-state, review, correction, and release prerequisites;
- stable package names, entrypoints, versions, reason codes, obligations, effective times, and supersession notes for accepted rules;
- explicit composition requirements with shared consent, rights, privacy, sensitivity, evidence, review, release, correction, and rollback policy;
- local bundle-membership declarations only after the bundle convention is accepted;
- links to paired contracts, schemas, fixtures, tests, validators, evaluator profiles, consumers, receipts, release gates, correction paths, and rollback targets;
- synthetic or public-safe native policy tests only after the repository accepts a colocation convention.

### What does not belong here

| Prohibited content or responsibility | Correct home or behavior |
| --- | --- |
| Domain doctrine, architecture, source guides, or legal explanation | `docs/domains/people-dna-land/` |
| Semantic definitions | `contracts/domains/people-dna-land/` |
| JSON Schema, DTO, enum, or field shape | `schemas/contracts/v1/domains/people-dna-land/` |
| Real names, contact details, households, dates of birth, or living-person payloads | Restricted source and lifecycle systems; never this public policy source |
| Raw or segment-level DNA/genomic data, kit IDs, match lists, or credentials | Restricted external/source/runtime systems; references only where governed |
| Consent tokens, signatures, secrets, revocation credentials, or private keys | Accepted consent service or secret store; never Git |
| GEDCOM, family trees, private relationship graphs, or source excerpts | Governed source/lifecycle lanes with rights and consent controls |
| Deeds, title instruments, tax records, assessor payloads, or private person-parcel joins | Governed source/lifecycle lanes; never policy source |
| EvidenceBundles, proofs, decisions, reviews, or receipts emitted at runtime | Their accepted evidence, review, proof, receipt, or lifecycle roots |
| RAW through PUBLISHED material | `data/<phase>/<lane>/` |
| Evaluator, adapter, CLI, service, or reusable runtime code | `packages/`, `apps/`, `runtime/`, or `tools/` by responsibility |
| Generic fixtures and tests | `fixtures/` and `tests/` |
| Release manifests, approvals, corrections, withdrawals, or rollback cards | `release/` |
| Public API routes, MapLibre logic, UI components, graph/index code, exports, or AI responses | Governed application and runtime roots |
| Independently evolving `people`, `dna`, `land_rights`, or other alias policy | No alias authority until a reviewed naming/migration decision exists |
| Generated language presented as identity, kinship, consent, title, policy, or release authority | Governed evidence, policy, human review, and release processes |

<p align="right"><a href="#top">Back to top</a></p>

---

## Direct lane inventory

The physical inventory below is confirmed at the pinned base. Status follows file bytes, not filenames.

| Path | Observed shape | Safe interpretation |
| --- | --- | --- |
| [`README.md`](./README.md) | This boundary document | Documentation only; no activation. |
| [`abstain_on_ambiguous.rego`](./abstain_on_ambiguous.rego) | Proposed stub; `package kfm.people_dna_land_abstain_on_ambiguous`; `default deny := false`; example commented out | Does not abstain or deny anything as written. |
| [`consent_validator.rego`](./consent_validator.rego) | Proposed stub; `package kfm.consent_validator`; `default deny := false`; example commented out | Does not validate consent as written. |
| [`deny_unpublished.rego`](./deny_unpublished.rego) | Proposed stub; `package kfm.people_dna_land_deny_unpublished`; `default deny := false`; example commented out | Does not deny unpublished material as written. |
| [`dna_restricted.rego`](./dna_restricted.rego) | Proposed stub; `package kfm.dna_restricted`; `default deny := false`; example commented out | Does not restrict DNA as written. |
| [`living_person.rego`](./living_person.rego) | Proposed generated-package scaffold; `default allow := false`; no rule | Fail-closed-shaped allow default, but no accepted entrypoint or evaluator. |
| [`living_person_redaction.rego`](./living_person_redaction.rego) | Proposed stub; `package kfm.living_person_redaction`; `default deny := false`; example commented out | Does not redact or deny as written. |
| [`consent/dna_consent_revocation.rego`](./consent/dna_consent_revocation.rego) | Proposed generated-package scaffold; `default allow := false`; no rule | No consent or revocation execution; no accepted evaluator. |
| `consent/` | One Rego scaffold | Non-empty proposed sublane; not an active consent system. |
| `dna/` | Empty tracked directory tree | Placement placeholder only. |
| `genealogy/` | Empty tracked directory tree | Placement placeholder only. |
| `land-ownership/` | Empty tracked directory tree | Placement placeholder only. |
| `land_rights/` | Empty tracked directory tree | Naming/placement placeholder; no authority. |
| `living_persons/` | Empty tracked directory tree | Naming/placement placeholder; no authority. |
| `people/` | Empty tracked directory tree | Local placeholder; not the unregistered parent-level `policy/domains/people/` lane. |

### Direct-lane conflicts that must remain visible

1. **Default-result conflict.** Five modules expose `deny` with a false default, while two expose `allow` with a false default. Those cannot be treated as one decision surface without an accepted composition rule.
2. **Filename-versus-behavior conflict.** Names such as `deny_unpublished`, `dna_restricted`, `living_person_redaction`, and `dna_consent_revocation` describe intended topics, not current enforcement.
3. **Package conflict.** Five root stubs use short `kfm.*` packages; two scaffolds use `kfm.generated.policy.domains.people_dna_land.*`.
4. **Responsibility overlap.** Domain-local consent and living-person files overlap shared consent and sensitivity lanes without an accepted precedence or bundle contract.
5. **Sublane naming conflict.** Hyphenated, underscored, singular, and plural variants coexist (`land-ownership`, `land_rights`, `living_persons`, `people`) with no accepted migration record.
6. **Alias and inventory conflict.** The registered lane is `people-dna-land` with code alias `people_dna_land`; the parent-level `people/` sibling is unregistered and cannot be silently mapped here. Its one-blank-byte README was added after the unchanged parent inventory was written, so physical presence and documented inventory now drift.
7. **Documentation-byte conflict.** [`SCOPE_AND_BOUNDARY.md`](../../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md) and `SENSITIVITY.md` share the same Git blob at the pinned base. This README does not treat duplicated bytes as two independently verified authorities.
8. **Consent documentation drift.** The shared consent README predates the two current synthetic validator profiles and still says no domain fixtures or tests surfaced. Its activation warning remains valid; its inventory needs separate reconciliation.

Until these conflicts are resolved, consumers must not guess entrypoints, invert truth polarity, combine packages, or infer precedence from a directory name.

<p align="right"><a href="#top">Back to top</a></p>

---

## Policy composition boundary

People–DNA–Land admissibility is the intersection of independent decisions. No one family can grant what another family denies or leaves unresolved.

### Composition law

For a bounded operation `o`, an accepted evaluator must obtain current decisions for every applicable family:

```text
domain
AND identity / relationship posture
AND source role
AND evidence
AND rights
AND consent / revocation
AND privacy / sensitivity / cultural or sovereignty controls
AND lifecycle
AND review
AND release
AND correction / withdrawal / rollback
```

The effective result is the **most restrictive applicable result plus the union of enforceable obligations**.

Examples:

- active consent cannot override missing evidence;
- public source availability cannot override living-person sensitivity;
- a validated DNA-derived summary cannot override raw-genomic denial;
- assessor availability cannot convert an administrative record to title authority;
- a released historical layer cannot authorize a new private person-parcel join;
- a prior allow cannot survive a newer revocation or correction;
- a map-safe field list cannot authorize an AI answer that reconstructs protected context.

If composition is incomplete, ambiguous, stale, or contradictory, the safe normalized result is `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` according to an accepted outward contract—never implicit permission.

<p align="right"><a href="#top">Back to top</a></p>

---

## Required policy input

An accepted evaluation must receive one explicit, versioned, minimized, immutable input. It must not silently fetch missing facts from canonical, internal, restricted, or public stores.

| Input family | Minimum governed context | Fail-closed trigger |
| --- | --- | --- |
| Domain identity | `people-dna-land` lane ID, code alias if needed, object family, sublane, policy version | Unknown, legacy-only, or conflicted identity |
| Operation | render, answer, search, export, transform, join, graph, index, cache, review, release-candidate check, correction, withdrawal, or rollback; stable request/candidate ID | Missing or overly broad capability |
| Actor and audience | authenticated service or reviewer class, purpose, public/restricted/steward audience | Missing identity where access differs |
| Subject posture | synthetic/historical/living/unknown, subject references, affected-party count, dispute state | Unknown treated as public-safe; affected subject omitted |
| Person assertion | assertion type, stable reference, source role, evidence refs, confidence, conflict and review state | Assertion collapsed into canonical identity |
| Relationship | biological/legal/adoptive/social/household/inferred type, direction, time, hypothesis status, evidence | Hypothesis or ambiguous relation treated as fact |
| DNA-derived evidence | material class, restricted evidence reference, permitted derivative, consent applicability, no raw payload | Raw data, segment detail, kit/vendor ID, or ungoverned inference |
| Land claim | claim type, instrument or administrative-record role, jurisdiction, effective time, parcel/geometry version, title limitation | Assessor/tax/geometry treated as title or legal boundary |
| Consent | grant reference, subject/holder, purpose, audience, scope, issued/effective/expiry time, status, revocation/dispute reference | Missing, out of scope, expired, disputed, revoked, or unverifiable |
| Spatial and temporal scope | requested precision, place/time bounds, valid time, transaction time, freshness | Harmful precision, stale support, or interval mismatch |
| Evidence | evidence references, bundle resolution, citations, validation, contradiction and supersession state | Unresolved support for a consequential claim |
| Source | descriptor reference, source role, authority posture, provenance, terms, cadence | Unclear role, rights, terms, or freshness |
| Rights and sensitivity | license/terms, privacy class, T-tier, sovereignty/cultural flags, transformations, residual reconstruction risk | Unknown, expired, unsupported, or weaker-than-input posture |
| Lifecycle, review, release | current/requested phase, review state, proof refs, release/correction/withdrawal/rollback refs | Skipped phase, missing review, or exposure without release support |
| Policy execution | bundle ID/version/digest, evaluator profile/version, entrypoint, normalized input hash | Unaccepted, ambiguous, or non-replayable evaluator context |
| Cross-domain composition | participating lanes, join purpose, inherited obligations, output audience and precision | Output less restrictive than any input or join-induced risk omitted |

### Domain and source alias handling

- `people-dna-land` is the registered lane ID.
- `people_dna_land` is the proposed code alias in the machine register.
- `people`, `dna`, `genealogy`, `land`, `land-ownership`, `land_rights`, and plural variants are not interchangeable identities merely because paths exist.
- A source alias never becomes a domain alias, and a domain alias never changes source role.
- If normalized identity and the original declared identity disagree, preserve both and return `HOLD_UNRESOLVED` until a reviewed mapping resolves the collision.
- Never collapse two people, relationships, parcels, instruments, consent grants, or sources because their labels normalize to the same text.

### Input minimization

Policy needs decision context, not protected payloads. Prefer:

- stable governed references over names, addresses, sequences, segments, or document excerpts;
- enumerated posture over free text;
- hashes only when the hash contract is accepted and cannot become a correlation token;
- coarse, authorized spatial/temporal buckets over exact values;
- purpose- and audience-specific consent results over raw credentials;
- source-role and evidence status over copied records;
- immutable refs plus current resolution status over hidden live lookups.

The two executable fixture validators accept synthetic values by design. Their fixture shapes are not permission to place equivalent real-world values in Git.

<p align="right"><a href="#top">Back to top</a></p>

---

## Decision and obligation contract

### Internal policy outcomes

The following vocabulary is a **proposed normalization target**, not a claim about current Rego output:

| Internal outcome | Meaning | Public-edge posture |
| --- | --- | --- |
| `ALLOW` | Every applicable gate explicitly permits the exact operation and all obligations are enforceable. | Return only the approved released derivative. |
| `RESTRICT` | The operation may proceed only with narrower fields, relations, precision, audience, purpose, or time. | Apply all restrictions before exposure. |
| `HOLD` | Review, evidence, consent, rights, sensitivity, correction, or release state is incomplete or changing. | No protected payload; expose safe pending state only if approved. |
| `ABSTAIN` | The system cannot responsibly answer or decide from current governed support. | Cite the limitation without reconstructing protected facts. |
| `DENY` | The operation is prohibited for the evaluated context. | Safe denial; no protected details or policy internals. |
| `ERROR` | Input, evaluator, dependency, or obligation enforcement failed. | Fail closed with a safe stable error. |

The canonical outward policy contract may use a different finite vocabulary. Any mapping—such as `ALLOW` or `RESTRICT` to a constrained `ANSWER`, and `HOLD` to `ABSTAIN` or `DENY`—must be explicit, versioned, tested, and non-permissive.

Fixture-validator outcomes such as `PASS`, `DENY`, and `ERROR` are validation results. They are not runtime policy decisions, consent grants, cleanup execution, proof, release, or publication authority.

### Required decision fields

An accepted decision should bind at least:

- decision ID and schema version;
- policy family, lane, package, entrypoint, bundle ID/version/digest, and evaluator version;
- normalized outcome and stable reason codes;
- safe public reason and separately governed reviewer detail;
- operation, actor/audience class, purpose, and requested surface;
- subject, relationship, DNA-derived, land-claim, source, evidence, consent, rights, sensitivity, lifecycle, review, and release references actually evaluated;
- obligations with responsible handler and enforcement status;
- input digest and replay context;
- evaluation, effective, expiry, and source-valid times;
- superseded decision, correction, revocation, withdrawal, or rollback references;
- receipt-ready metadata without embedded protected payloads.

### Obligation families

An accepted decision may require:

- deny-field or deny-relation controls;
- redaction, aggregation, generalization, bucketing, tokenization, or non-display;
- purpose, audience, authentication, or role restrictions;
- citation and evidence display;
- identity/relationship hypothesis labeling;
- title, parcel, assessor, source-role, and legal-limitation notices;
- no-download, no-export, no-index, no-cache, no-graph, no-AI-context, or retention limits;
- delay, embargo, quarantine, specialist review, or rights-holder review;
- consent recheck at access time;
- revocation, correction, withdrawal, cache invalidation, graph/index deletion, and derivative cleanup;
- receipt, review record, proof reference, release binding, or rollback-target recording.

An obligation is not advisory. If a consumer cannot enforce every required obligation atomically, it must fail closed.

### Public response normalization

Public surfaces must not expose:

- raw policy input;
- names or stable correlation identifiers not present in the released derivative;
- DNA/genomic, consent, title, or private join details;
- hidden source, evidence, or reviewer material;
- internal package names, sensitive reason codes, thresholds, salts, transform parameters, or bypass hints;
- existence or absence of protected records where that fact is sensitive.

Safe public responses use stable coarse status, released citations, approved limitations, and non-reconstructable content only.

<p align="right"><a href="#top">Back to top</a></p>

---

## Public-surface contract

### Governed API

- public callers use governed APIs, never direct canonical or restricted stores;
- every consequential request supplies or resolves an authenticated current decision;
- the response is limited to the released derivative and enforced obligations;
- error differences, counts, timing, and pagination must not reveal protected existence or linkage;
- cache keys include decision, audience, release, correction, and expiry state where relevant;
- a stale, missing, or unverifiable decision fails closed.

### Map and tiles

- no private person-parcel join, exact living-person location, raw DNA-derived relation, consent detail, or unreleased land claim enters public tile source data;
- field allowlists are explicit and versioned;
- geometry precision matches the released claim and never implies surveyed/title boundary authority;
- styles, labels, filters, feature IDs, metadata, URLs, and hover behavior cannot reintroduce denied fields;
- sparse cohorts, time slices, zoom levels, differencing, and cross-layer joins receive reconstruction review;
- policy is enforced before tile production and rechecked when policy, consent, evidence, or release state changes.

### Graph, search, index, and cache

- private relationship edges, person-parcel edges, DNA-derived edges, consent state, and protected identifiers remain outside public indexes;
- graph paths do not upgrade hypotheses to fact;
- search snippets and facets cannot reveal protected existence, households, relationships, or locations;
- embeddings and vector stores inherit source restrictions and withdrawal obligations;
- revocation or correction invalidates every dependent materialized surface, not only the primary record;
- completion requires verified deletion, tombstone, embargo, replacement, or other accepted terminal action for each dependency.

### Evidence Drawer and Focus Mode

- display only released citations and approved claim limitations;
- keep source role, assertion/hypothesis status, confidence, contradiction, valid time, and review status visible;
- do not expose restricted excerpts, raw records, consent credentials, DNA detail, private graph edges, or internal reviewer notes;
- assessor/tax/parcel context must not be labeled title proof;
- if required evidence is not public-safe, show an approved limitation or abstain.

### Exports

- export is a separate operation and requires its own current evaluation;
- exported fields, relations, rows, geometry, temporal precision, metadata, identifiers, and file properties are reviewed as one disclosure surface;
- watermarks or terms do not cure an otherwise unauthorized export;
- an authenticated UI view does not automatically authorize download;
- bulk, repeated, and differenced exports receive reconstruction and re-identification review.

### AI and generated language

- retrieval filters restricted material before prompt assembly;
- the model never receives raw DNA/genomic data, consent credentials, private person-parcel joins, protected identity graphs, or unreleased title material;
- generated answers preserve assertion, hypothesis, source-role, title, parcel, time, and confidence limitations;
- no inference fills a missing identity, relationship, consent, ownership, or boundary claim;
- every consequential claim cites a released evidence path or abstains;
- prompts and logs are governed disclosure surfaces and inherit deletion, revocation, and correction obligations.

<p align="right"><a href="#top">Back to top</a></p>

---

## Lifecycle and temporal behavior

### Lifecycle boundary

Policy may evaluate a requested transition. It does not perform the transition.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

For each transition, the evaluator needs current artifact identity, source/evidence state, rights, consent, sensitivity, review, candidate/release state, correction state, and rollback target. A later lifecycle label cannot retroactively legalize an earlier unauthorized use.

`PUBLISHED` is not synonymous with unrestricted. A released carrier may remain audience-limited, time-limited, purpose-limited, non-exportable, or subject to withdrawal.

### Time semantics

People–DNA–Land decisions are time-sensitive. Keep distinct:

- source observation or record time;
- event or relationship-valid time;
- instrument execution, recording, and effective time;
- ownership/occupancy interval;
- parcel or geometry version time;
- consent issue, effective, expiry, suspension, dispute, and revocation time;
- evidence validation and source-refresh time;
- policy evaluation and decision-effective time;
- review, release, correction, withdrawal, and rollback time;
- current request time.

Do not compare or substitute these without an explicit contract.

### Race and stale-result handling

- bind evaluation to immutable input, bundle, evaluator, source, evidence, consent, and release digests;
- recheck current consent, correction, withdrawal, and expiry state immediately before consequential use;
- reject a result if any bound dependency changed before obligation enforcement completed;
- avoid check-then-use gaps between policy and materialization;
- expire caches no later than the earliest relevant consent, policy, source, evidence, review, or release expiry;
- on revocation or correction, deny new use first, then reconcile downstream surfaces;
- never treat cleanup still in progress as permission to continue serving stale material.

<p align="right"><a href="#top">Back to top</a></p>

---

## Identity, naming, and versioning

### Canonical identity

| Concept | Current repository posture |
| --- | --- |
| Domain lane ID | `people-dna-land` — proposed machine projection and canonical directory segment |
| Code alias | `people_dna_land` — proposed machine projection |
| Documentation path | `docs/domains/people-dna-land/` |
| Direct policy path | `policy/domains/people-dna-land/` |
| Sensitivity baseline | T4 — proposed machine projection; not disclosure authority |
| Parent-level `policy/domains/people/` | Unregistered sparse legacy scaffold with a one-blank-byte README; no inferred alias |

### Naming rules

- use `people-dna-land` for repository domain segments unless an accepted decision says otherwise;
- use `people_dna_land` only where language/package grammar requires the registered code alias;
- do not introduce new `people`, `dna`, `genealogy`, `land`, `land_ownership`, `land-rights`, singular/plural, or generated-package variants without an accepted migration decision;
- package names, bundle IDs, entrypoints, reason codes, obligations, and schema IDs are explicit—not derived silently from paths;
- preserve original source identifiers and declared aliases as data; normalization never overwrites them;
- name relationship, land-claim, consent, and DNA-derived classes by role, not by convenient source label.

### Versioning rules

Any accepted policy artifact needs:

- semantic version or another reviewed immutable version scheme;
- bundle and evaluator compatibility range;
- input and output contract versions;
- effective and expiry time where applicable;
- supersession and rollback target;
- migration notes for package, entrypoint, outcome, reason, obligation, field, or alias changes;
- deterministic digest and replay binding;
- negative compatibility tests.

### No implicit latest

Consumers must not select a policy, consent result, schema, source card, evidence object, release, or correction because it is lexically newest or stored at an unversioned path. Selection is explicit and reviewable.

<p align="right"><a href="#top">Back to top</a></p>

---

## Validation and failure semantics

### Current executable evidence

The [`domain-people-dna-land` workflow](../../../.github/workflows/domain-people-dna-land.yml) currently defines three bounded jobs:

| Job/profile | Confirmed behavior | Authority boundary |
| --- | --- | --- |
| `validate-people-dna-land` — consent-safe genealogy overlay | Runs a substantive validator plus 16 no-network tests against 2 valid synthetic candidates, 13 known-invalid candidate/sidecar pairs, and a synthetic revocation manifest | Proves only the fixture profile, deterministic hash/loader behavior, declared denial families, and expected polarity. |
| `validate-people-dna-land` — consent-revocation propagation assessment | Runs a substantive validator plus 9 no-network tests against a 17-case manifest: 6 `PASS`, 8 `DENY`, and 3 `ERROR` expectations | Assesses declared consent state and seven-surface dependency posture; performs no revocation or cleanup. |
| `build-proof-people-dna-land` | Verifies the documented proof lane remains a hold and that no unexpected proof artifact or command surfaced | Emits no proof and grants no authority. |
| `publish-dry-run-people-dna-land` | Verifies the candidate/release boundary remains a hold and that no unexpected candidate artifact or command surfaced | Performs no release, promotion, deployment, or publication. |

The overlay profile checks, among other things:

- active, expired, revoked, and missing consent behavior;
- revocation-manifest shape, root, membership, and deterministic hashing;
- declared evidence references and high-confidence evidence sufficiency;
- raw-genomic, identifying-kit-field, identifying-field, and precise-location denial;
- synthetic county and coarse time/place constraints;
- explicit `not_released` governance;
- duplicate-key, non-finite-number, non-object, symlink, and file-size safety;
- stable, value-free serialized diagnostics;
- deterministic no-network execution.

The revocation assessment checks the exact closed dependency set `READ`, `ANSWER`, `EXPORT`, `TILE`, `GRAPH`, `INDEX`, and `CACHE`, including required actions and receipts for materialized surfaces. A passing assessment still means **consent dimension only**; it does not prove cleanup, evidence, policy, release, or publication.

### Current non-evidence

The following do not prove active domain policy:

- the seven direct Rego files;
- an empty subdirectory;
- a Python validator passing synthetic fixtures;
- a workflow guardrail job passing;
- a schema accepting a candidate;
- a consent-fixture `PASS` result;
- a proof or release hold remaining green;
- a documentation badge;
- GitHub mergeability or owner self-review.

### Required validation layers before activation

1. **Repository shape:** canonical path, no unresolved alias, accepted ownership, bundle membership, no duplicate authority.
2. **Syntax and static analysis:** Rego parse/format/lint, unsafe-variable checks, capabilities, forbidden built-ins, deterministic evaluation, and no network or hidden I/O.
3. **Package and entrypoint:** one accepted namespace, finite results, no truth-polarity ambiguity, explicit shared-policy composition.
4. **Input contract:** closed versioned shape, minimization, immutable references, alias collision handling, protected-payload rejection.
5. **Semantic invariants:** person assertion, relationship hypothesis, DNA evidence, consent, land claim, title/parcel, source-role, and temporal distinctions.
6. **Policy polarity:** allow, restrict, hold, abstain, deny, and error cases; unknowns and dependency errors fail closed.
7. **Composition:** domain, identity, source, evidence, rights, consent, sensitivity, lifecycle, review, release, correction, and rollback intersections.
8. **Obligation enforcement:** every consumer proves atomic enforcement or denial.
9. **Public-surface safety:** API, map, tiles, graph, index, cache, export, drawer, Focus Mode, story, and AI reconstruction tests.
10. **Lifecycle and time:** stale support, consent expiry, revocation, correction, supersession, candidate/release drift, race and retry tests.
11. **Receipts and replay:** deterministic input/bundle/evaluator/output binding, safe diagnostics, non-secret audit trail.
12. **Rollback and deactivation:** last-known-safe binding, emergency deny path, cache/derivative invalidation, and reviewed restoration drill.

### Minimum negative cases

Before activation, tests must reject at least:

- missing or unknown subject posture;
- living person without current in-scope consent;
- consent for the wrong subject, purpose, audience, operation, field, relation, precision, export, or time;
- expired, suspended, disputed, revoked, unverifiable, or lookup-error consent;
- raw DNA/genomic material, segment coordinates, kit/vendor IDs, or identifying hashes;
- DNA-derived hypothesis presented as confirmed identity or kinship;
- genealogy relationship with missing evidence, type, confidence, contradiction, or review state;
- person merge caused by normalized-name or alias collision;
- assessor/tax/parcel record presented as title proof;
- parcel geometry presented as legal boundary;
- stale instrument, parcel version, ownership interval, or source descriptor;
- private person-parcel join or cross-surface reconstruction;
- missing rights, sensitivity, evidence, review, release, correction, or rollback state;
- public release claim inside a fixture, input, or generated answer;
- unknown package, entrypoint, bundle, evaluator, schema, or outcome;
- unhandled obligation, stale cache, incomplete graph/index cleanup, or check-then-use race;
- direct-public-store access;
- fail-open dependency error.

### Failure behavior

Use separate result families for separate responsibilities:

| Result | Meaning |
| --- | --- |
| `FAIL_INVARIANT` | A declared semantic, policy, lifecycle, public-surface, or authority invariant was violated. |
| `HOLD_UNRESOLVED` | Required authority, mapping, consent, evidence, review, or dependency state is missing, conflicted, or changing. |
| `ERROR_VALIDATOR` | The validator, loader, schema resolver, dependency, or harness could not produce a trustworthy result. |

These are validation/control outcomes, not automatic public response bodies. All must prevent permission from being inferred.

Diagnostics must be deterministic, bounded, non-echoing, and free of protected values, credentials, internal locators, or reconstruction aids.

<p align="right"><a href="#top">Back to top</a></p>

---

## Review burden

### Change classification

| Change | Minimum review burden |
| --- | --- |
| Typo or link with no meaning change | Documentation review plus affected specialist if trust wording changes |
| README boundary or maturity claim | Policy, domain, privacy/sensitivity, consent, evidence, and documentation review |
| Package, entrypoint, default, reason, obligation, or composition change | Independent policy/runtime/security review plus full negative suite |
| Living-person, DNA/genomic, consent/revocation, person-parcel, or public-surface rule | Highest restricted-domain review; privacy, consent, rights, sensitivity, security, and affected-domain specialists |
| Land title, ownership, parcel, assessor/tax, or legal-limitation rule | Land-record/source/evidence review and appropriate legal-domain expertise; no legal conclusion inferred from code review |
| Bundle activation, evaluator binding, release gate, or rollback target | Dependency-closed activation packet, independent approval, replay, public-surface, correction, and rollback evidence |

### Separation of duties

One person or automation must not silently serve as author, evidence resolver, consent authority, privacy reviewer, land/title reviewer, policy approver, release authority, and publication actor for the same consequential change.

Where repository ownership is currently single-owner, the limitation remains explicit. CODEOWNERS routing and automated review are advisory, not independent approval.

### Reviewer questions

- Does the change narrow or widen any audience, purpose, field, relation, precision, export, or time window?
- Could it expose or help reconstruct living-person, DNA/genomic, consent, relationship, location, person-parcel, or title-sensitive information?
- Does it preserve assertion versus identity, hypothesis versus relationship fact, administrative record versus title, and parcel geometry versus legal boundary?
- Is the package, entrypoint, default, outcome, reason, and obligation contract unambiguous?
- Are source role, evidence, rights, consent, sensitivity, lifecycle, review, release, correction, and rollback all explicit?
- Are current and stale states tested, including revocation and check-then-use races?
- Can every consumer enforce every obligation atomically?
- Are public diagnostics and failure modes non-revealing?
- Is the change reversible without restoring withdrawn or revoked material?
- Does the evidence prove the claim, or only the presence of a file or passing fixture?

<p align="right"><a href="#top">Back to top</a></p>

---

## Activation and definition of done

### Current activation state

**INACTIVE / EVALUATOR UNBOUND / RELEASE HELD.** Repository evidence establishes scaffolds and two synthetic validator profiles, not an accepted domain policy runtime.

### Dependency-closed activation packet

Activation requires one reviewed packet containing at least:

- accepted lane, sublane, package, entrypoint, and alias decisions;
- resolved responsibility split across domain, consent, sensitivity, rights, evidence, and release policy;
- versioned minimized input and finite output contracts plus schemas;
- source-role, evidence, consent, rights, sensitivity, lifecycle, review, release, correction, and rollback bindings;
- accepted Rego/equivalent modules with fail-closed defaults and no ambiguous truth polarity;
- bundle manifest, immutable digest, evaluator profile, capabilities, and dependency lock;
- synthetic positive and negative fixtures with no protected material;
- native policy tests and cross-surface integration tests;
- obligation handlers and proof that every consumer fails closed when enforcement is incomplete;
- decision-receipt and safe replay contract;
- public API/map/tile/graph/index/cache/export/AI safety evidence;
- revocation, correction, withdrawal, invalidation, and rollback drills;
- independent specialist review and accepted release binding;
- emergency deactivation procedure and last-known-safe target.

### Definition of done

This lane is not done until:

1. every direct file and subdirectory has an accepted responsibility or is removed through reviewed history;
2. package, entrypoint, default, outcome, reason, obligation, and alias conflicts are resolved;
3. duplicated or stale authority documentation is reconciled without silently overwriting newer implementation evidence;
4. no real protected payload is present in policy, fixtures, tests, logs, or receipts;
5. all required contracts, schemas, validators, tests, bundles, evaluators, consumers, and receipts are version-bound;
6. living-person, DNA/genomic, consent, relationship, land/title, and person-parcel invariants have deterministic negative coverage;
7. every public surface proves non-reconstruction and current-policy enforcement;
8. revocation and correction propagate through all dependent materialized surfaces;
9. rollback and emergency deny paths are exercised;
10. independent reviewers accept the dependency-closed packet;
11. release authority approves the exact artifact and no broader scope;
12. activation, release, deployment, and publication remain separate recorded transitions.

No README, passing workflow, draft PR, merge, or repository presence satisfies these conditions alone.

<p align="right"><a href="#top">Back to top</a></p>

---

## Contributor workflow

### Before authoring

1. Pin current `main` and record the target blob.
2. Check open PRs, branches, and recent commits for target collisions.
3. Read accepted ADR-0029, Directory Rules, `policy/README.md`, and `policy/domains/README.md`.
4. Read the direct files—not only their names.
5. Reconcile domain, consent, sensitivity, evidence, source, rights, release, correction, and rollback evidence.
6. Classify every claim as confirmed, proposed, conflicted, unknown, or needs verification.
7. Define one responsibility root and the smallest dependency-closed scope.
8. Confirm that no real protected material, credential, or source payload is needed.

### While authoring

- keep real data and secrets out of Git;
- preserve evidence, source-role, identity, relationship, consent, title, parcel, lifecycle, and release distinctions;
- make defaults and truth polarity explicit;
- use stable reason and obligation identifiers;
- reject hidden network access and hidden state;
- design diagnostics that do not echo values;
- bind time, version, digest, supersession, and rollback;
- add negative cases before claiming a gate is enforced;
- avoid unrelated formatting churn or cross-root edits;
- do not create a receipt, proof, release, or activation artifact merely to make documentation appear complete.

### Before requesting review

- verify one-file or explicitly authorized dependency-closed scope;
- lint Markdown/Rego/configuration as applicable;
- parse the metadata block;
- check headings, anchors, links, tables, alerts, HTML, and final newline;
- run sensitive-content, secret, identifier, and coordinate scans;
- verify deterministic fixture and test behavior;
- compare exact target bytes with the prepared artifact;
- inspect the remote diff for unrelated files;
- document unresolved conflicts and inherited failures;
- keep the PR draft until authorized human review completes;
- never mark ready, merge, activate, release, deploy, or publish from a documentation task.

<p align="right"><a href="#top">Back to top</a></p>

---

## Correction, revocation, and invalidation

### Triggers

Reconsider an earlier decision when any bound dependency changes, including:

- subject living/deceased/unknown posture;
- identity merge, split, dispute, or correction;
- relationship type, confidence, evidence, or review;
- DNA-derived evidence validity, permitted derivative, or source terms;
- consent scope, expiry, suspension, dispute, revocation, or lookup status;
- source role, rights, privacy, sensitivity, or cultural/sovereignty restrictions;
- land instrument, parcel version, assessor/tax status, ownership interval, or title limitation;
- evidence conflict, supersession, or withdrawal;
- policy bundle, evaluator, reason, obligation, or consumer behavior;
- review, release, correction, withdrawal, or rollback state;
- discovery of cross-surface reconstruction or unauthorized derivative retention.

### Reconsideration law

1. deny or hold new consequential use immediately when support becomes less permissive;
2. preserve the prior decision as an immutable event;
3. issue a superseding decision bound to current evidence and time;
4. enumerate dependent API, tile, map, graph, index, cache, export, story, AI, proof, and release artifacts;
5. require the appropriate invalidate, withdraw, purge, tombstone, embargo, replace, or review action;
6. require action receipts without embedding protected values;
7. verify completion across the exact dependency set;
8. restore access only through a new accepted evaluation and, where required, a new release.

The current synthetic revocation assessment validates declared dependency posture. It does not execute or prove any step above.

### Safe notices

Public correction or withdrawal notices must not reveal:

- that a protected person, relationship, DNA record, consent record, or land link exists;
- the reason a subject revoked consent;
- raw identifiers, private locators, internal evidence, reviewer detail, or exact affected geometry;
- enough timing, count, or error detail to reconstruct protected state.

Use approved coarse status and released correction references only.

<p align="right"><a href="#top">Back to top</a></p>

---

## Rollback and recovery

### This README change

The rollback unit for this documentation modernization is the single changed file. Before merge, close the draft PR and delete only its review branch if the proposal is withdrawn. After merge, revert the documentation commit through reviewed Git history to restore prior blob `571a4a6d5c8ba7cf6c1fa9fcdd63da88bc05eb2a`.

No policy, runtime, data, proof, release, deployment, or publication rollback is required because this README activates none of them.

### Future policy rollback

An accepted policy rollback must identify:

- failing or unsafe bundle/evaluator version;
- last-known-safe bundle, evaluator, contract, schema, and consumer compatibility set;
- affected decisions, receipts, candidates, releases, caches, graphs, indexes, exports, and published carriers;
- consent, evidence, rights, sensitivity, correction, and withdrawal state that must remain current;
- migration or replay behavior for in-flight requests;
- deactivation and restoration actors;
- verification that rollback does not resurrect revoked, withdrawn, corrected, expired, or now-sensitive material.

### Emergency deactivation

When safe evaluation or obligation enforcement cannot be trusted:

1. disable the affected entrypoint or bundle binding;
2. return safe deny/abstain/error behavior;
3. stop new materialization and export;
4. invalidate affected caches and derived surfaces;
5. preserve non-sensitive evidence and audit references;
6. open a bounded incident/review record;
7. restore only after dependency-closed verification.

Emergency access widening is never a recovery mechanism.

<p align="right"><a href="#top">Back to top</a></p>

---

## Related responsibility roots

| Responsibility | Current path | Relationship to this lane |
| --- | --- | --- |
| Domain doctrine | [`docs/domains/people-dna-land/`](../../../docs/domains/people-dna-land/README.md) | Human scope, models, and limitations; draft evidence, not executable policy. |
| Scope boundary | [`SCOPE_AND_BOUNDARY.md`](../../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md) | Draft scope; byte-identical to `SENSITIVITY.md` at the pinned base and therefore conflicted. |
| DNA handling | [`DNA_HANDLING.md`](../../../docs/domains/people-dna-land/DNA_HANDLING.md) | Draft restricted-handling doctrine; not runtime proof. |
| Land ownership | [`LAND_OWNERSHIP.md`](../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md) | Draft distinction among instruments, administrative records, ownership intervals, title, and geometry. |
| Data lifecycle | [`DATA_LIFECYCLE.md`](../../../docs/domains/people-dna-land/DATA_LIFECYCLE.md) | Draft lifecycle and preservation guidance. |
| Semantic contracts | [`contracts/domains/people-dna-land/`](../../../contracts/domains/people-dna-land/README.md) | Meaning and invariants consumed by policy. |
| Machine schemas | [`schemas/contracts/v1/domains/people-dna-land/`](../../../schemas/contracts/v1/domains/people-dna-land/README.md) | Shape only; schema validity grants no policy or release authority. |
| Shared consent | [`policy/consent/people-dna-land/`](../../consent/people-dna-land/README.md) | Consent gate boundary; current inventory text predates new synthetic profiles. |
| Shared sensitivity | [`policy/sensitivity/people-dna-land/`](../../sensitivity/people-dna-land/person_parcel_join.deny.rego) | Proposed person-parcel scaffold; no active rule established. |
| Synthetic fixtures | [`fixtures/domains/people-dna-land/`](../../../fixtures/domains/people-dna-land/README.md) | Test examples only; no real protected material. |
| Tests | [`tests/domains/people-dna-land/`](../../../tests/domains/people-dna-land/README.md) | Two bounded executable consent profiles plus broader placeholder lanes. |
| Validators | [`tools/validators/domains/people-dna-land/`](../../../tools/validators/domains/people-dna-land/README.md) | Two substantive validators plus several tiny placeholder executables; README inventory is stale. |
| Pipeline intent | [`pipeline_specs/people-dna-land/`](../../../pipeline_specs/people-dna-land/README.md) | Mixed scaffold; no active specification established. |
| Pipeline execution | [`pipelines/domains/people-dna-land/`](../../../pipelines/domains/people-dna-land/README.md) | Placeholder-heavy execution lane; not policy authority. |
| Shared package | [`packages/domains/people-dna-land/`](../../../packages/domains/people-dna-land/README.md) | Restricted-review package boundary; no domain policy evaluator established. |
| Source registry | [`data/registry/sources/people-dna-land/`](../../../data/registry/sources/people-dna-land/README.md) | Source-card boundary; source presence does not admit or release data. |
| Proof lane | [`data/proofs/people-dna-land/`](../../../data/proofs/people-dna-land/README.md) | Documented hold; emitted proof files need verification and accepted producers. |
| Release candidates | [`release/candidates/people-dna-land/`](../../../release/candidates/people-dna-land/README.md) | Candidate review only; a candidate is not a release. |
| CI readiness | [`domain-people-dna-land.yml`](../../../.github/workflows/domain-people-dna-land.yml) | Two synthetic validator profiles plus explicit proof and release holds. |

### Cross-domain seams

People–DNA–Land joins may intersect archaeology, settlements, infrastructure, agriculture, roads/rail/trade, habitat, hazards, hydrology, administrative geography, and historical narratives. A cross-domain join:

- preserves each input's source role and evidence scope;
- inherits the most restrictive policy and obligations;
- records purpose, participating lanes, join keys, precision, time, and output audience;
- does not let one lane assert another lane's truth;
- receives reconstruction, cultural/sovereignty, privacy, and public-surface review where applicable;
- is corrected and rolled back as one dependency graph.

<p align="right"><a href="#top">Back to top</a></p>

---

## Governing decisions and doctrine

- [`ADR-0029 — Adopt Directory Governance Standard v2`](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) — accepted placement decision.
- [`Directory Rules`](../../../docs/doctrine/directory-rules.md) — adopted exact bytes; a path is an authority claim.
- [`policy/README.md`](../../README.md) — root admissibility boundary and activation posture.
- [`policy/domains/README.md`](../README.md) — domain composition, direct-child inventory, input/output, validation, and alias posture.
- [`domain_lane_register.yaml`](../../../control_plane/domain_lane_register.yaml) — proposed machine projection of lane ID, code alias, documentation path, and T4 baseline.
- [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) — review routing only; not stewardship or approval proof.

When these sources disagree:

1. accepted ADR decisions control adoption status;
2. accepted singular-root responsibility controls placement;
3. current repository bytes control implementation claims;
4. machine projections cannot self-authorize;
5. uncertainty is recorded and fails closed;
6. no README silently resolves a governance conflict that requires an ADR, assignment, or accepted migration.

<p align="right"><a href="#top">Back to top</a></p>

---

## Open verification register

| ID | Open question | Required evidence | Safe interim posture |
| --- | --- | --- | --- |
| PDL-POL-001 | What is the accepted package and entrypoint surface? | ADR or reviewed bundle/evaluator contract | Evaluator unbound; no runtime claim. |
| PDL-POL-002 | Should defaults expose `allow`, `deny`, or a structured decision? | Accepted composition contract and negative tests | Do not combine or invert current stubs. |
| PDL-POL-003 | Which direct subdirectories are canonical, aliases, migrations, or obsolete? | Naming/placement decision and migration plan | Treat all as non-authoritative placeholders. |
| PDL-POL-004 | Is parent-level `policy/domains/people/` a compatibility lane, and how should its blank README be classified? | Register/ADR update, parent-inventory reconciliation, and path migration evidence | Blank physical presence grants no authority; no inferred alias. |
| PDL-POL-005 | How do domain, consent, sensitivity, rights, and evidence policies compose? | Accepted precedence/composition contract | Most restrictive result; unresolved means hold/deny. |
| PDL-POL-006 | What is the accepted normalized input and outward decision contract? | Versioned contracts, schemas, fixtures, tests | Current vocabulary is proposed only. |
| PDL-POL-007 | Is any direct Rego file in a bundle or production evaluator? | Bundle manifest, digest, selector, runtime binding, receipts | Inactive. |
| PDL-POL-008 | What is the accepted person-identity and relationship-resolution service boundary? | Contracts, source/evidence roles, review and correction evidence | Policy consumes supplied state only. |
| PDL-POL-009 | What DNA-derived representations may enter policy? | Restricted data-minimization contract, consent/rights/sensitivity review | References and coarse posture only; no raw/segment public path. |
| PDL-POL-010 | What consent record, status, and revocation source is authoritative? | Accepted consent contracts/services, freshness and failure tests | Missing or unverifiable state fails closed. |
| PDL-POL-011 | What land sources may support which claim types? | Reviewed source-role matrix and instrument/parcel/title contracts | Administrative records and geometry are not title proof. |
| PDL-POL-012 | How is person-parcel reconstruction risk measured across surfaces? | Threat model, privacy review, negative tests, release criteria | No public path by default. |
| PDL-POL-013 | Why are `SCOPE_AND_BOUNDARY.md` and `SENSITIVITY.md` byte-identical? | Documentation history and reviewed correction | Do not infer independent sensitivity authority. |
| PDL-POL-014 | Which statements in the shared consent and validator READMEs are stale? | Separate current-state reconciliation | Trust current code/fixtures/workflow for implementation inventory; preserve activation warning. |
| PDL-POL-015 | How are obligations enforced across API, tiles, graph, index, cache, export, and AI? | Consumer integration tests and receipts | Any unhandled obligation denies use. |
| PDL-POL-016 | What is the accepted revocation/correction dependency graph? | Contract, producer, action receipts, deterministic cleanup test | Synthetic assessment only; no cleanup claim. |
| PDL-POL-017 | Who holds functional and independent review roles? | Verified assignments and GitHub identity mapping | CODEOWNERS route only; stewardship unproved. |
| PDL-POL-018 | What are the release, rollback, and emergency deactivation commands? | Accepted runbooks, candidate contract, drills, receipts | Proof and release remain held. |

Closing an item requires repository-backed evidence and appropriate review. Editing this table alone does not close it.

<p align="right"><a href="#top">Back to top</a></p>

---

## Last-reviewed evidence

### Review record

| Field | Value |
| --- | --- |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Pinned base | `main@299c8a81325689c68a38304ce7b14921342dcdd0` |
| Review date | 2026-08-13 |
| Target prior blob | `571a4a6d5c8ba7cf6c1fa9fcdd63da88bc05eb2a` |
| Direct inventory | 1 README, 7 proposed Rego scaffolds, 6 empty subdirectories, 1 non-empty consent subdirectory |
| Executable bounded evidence | 2 substantive synthetic validators; 25 deterministic no-network tests; 2 fixture profiles |
| Workflow posture | Validation profiles executable; proof and release dry-run held |
| Runtime posture | No accepted direct Rego bundle/evaluator/consumer established |
| Public posture | Deny by default; governed released derivative only |
| Generated receipt for this edit | Omitted because the authorized change budget is exactly this README |

### Evidence ledger

| Evidence | Blob at pinned base | What it proves |
| --- | --- | --- |
| Accepted ADR-0029 | `b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62` | Adoption decision and governance boundary |
| Directory Rules | `fd49a0b83e55cef52c1124281f093e263526898d` | Adopted placement doctrine bytes |
| Policy root | `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35` | Root admissibility boundary |
| Domain-policy parent | `ed9be975c9da2c7d77d94fab621db39f23953813` | Direct-child map, alias posture, composition and activation rules |
| Domain lane register | `1bfc6f91cfa713a5e3d51ece011b63b46310734f` | Proposed lane ID, code alias, docs path, and T4 baseline projection |
| Legacy `policy/domains/people/README.md` | `8b137891791fe96927ad78e64b0aad7bded08bdc` | One blank byte only; physical presence without registered alias or policy authority |
| CODEOWNERS | `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` | GitHub review route only |
| Domain docs README | `19a3ea59bab2d5e04c73f402a35048c1a55ab071` | Draft human domain landing surface |
| Contracts README | `d99e7fc318f34fbeb90a1ee31658f5121b8ffd38` | Draft semantic-contract boundary and sensitivity warnings |
| Schemas README | `fbe5557ff4e19d1b70a97d284ab1743dd3d08f29` | Draft schema index and naming drift |
| Shared consent README | `fa7ea7c95a473a7fd498053536ca0b72b17461f6` | Consent boundary and valid activation warning; stale implementation inventory |
| Direct Rego set | `04be32e…`, `820daa2…`, `17bb640…`, `d174e58…`, `ba3a55d…`, `3260751…`, `bb4400e…` | Proposed defaults, package conflicts, and absence of operative rules |
| Fixtures README | `8eb10804c587c62edf1eb9750c2c82b5cf237f2a` | Synthetic-only fixture boundary |
| Tests README | `ecdaac8e2509d07e39279e23e99273a15716d053` | Bounded executable profile claim |
| Consent-overlay validator | `b2ff0e5037de0f1c22486743ab5e20926c68474d` | Substantive deterministic fixture validator |
| Revocation-assessment validator | `76c7805428f253a7a711c7bc68a27e9cbcce40e7` | Substantive seven-surface assessment validator |
| Domain workflow | `bcf64c3e3b6653b9543489fc5a6031805ae3ef48` | Two executable profiles plus explicit proof/release holds |
| Proof README | `05359bb623e69dccbda1ee22f8ba0d8345d9d412` | Documented proof boundary, not emitted proof |
| Release candidate README | `cbbef9394fbdbe94ed742957e1b764c84c9907f3` | Candidate-only and no-release posture |

Evidence is scoped to the pinned commit. Later repository state must be re-read before using this inventory as current.

<p align="right"><a href="#top">Back to top</a></p>

---

## Revision history

| Version | Date | Change | Rollback |
| --- | --- | --- | --- |
| Unversioned scaffold | 2026-05-08 | Added a 31-line greenfield placeholder that overclaimed all policy-bearing materials as local and provided no sensitive-domain boundary. | Restore through prior Git history if needed. |
| v0.2 | 2026-08-13 | Reconciles accepted directory governance, canonical lane identity, T4 baseline projection, seven direct Rego scaffolds and their default/package conflicts, empty sublanes, two deterministic consent fixture profiles, policy composition, minimized inputs, decisions/obligations, public surfaces, lifecycle/time, review burden, activation gates, correction/revocation, rollback, evidence, and open verification without changing executable behavior. | Revert this README-only commit to blob `571a4a6d5c8ba7cf6c1fa9fcdd63da88bc05eb2a`. |

---

KFM rule: People–DNA–Land policy may decide only from explicit current governed context, must deny or hold when that context or its enforcement path is incomplete, and must never let a name, graph, DNA hint, consent artifact, assessor record, parcel, validator, workflow, receipt, proof, map, export, or generated answer substitute for person evidence, relationship review, genomic safeguards, consent, title support, rights, sensitivity, release, correction, or rollback.

<p align="right"><a href="#top">Back to top</a></p>
