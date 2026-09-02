<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-sensitivity-readme
title: policy/sensitivity/ — Sensitivity Policy Trust Boundary
type: readme
version: v0.1
status: draft; BOUNDARY_COMPACT; repository-grounded; proposed-scaffold-corpus; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes policy/ review to @bartytime4life; no accepted sensitivity steward or independent approver was established
created: 2026-03-16
updated: 2026-08-12
policy_label: public; policy; sensitivity; trust-boundary; default-hold; non-release; non-publication
owning_root: policy/
responsibility: Define the local sensitivity-policy source boundary, its inherited authority, current child inventory, separation rules, evidence limits, correction posture, and release handoffs without claiming runtime enforcement or publication authority.
truth_posture: CONFIRMED accepted placement under policy/, exact baseline child inventory, proposed scaffold corpus, mixed Rego defaults, public repository visibility, internal operating exposure, and bounded validation surfaces / PROPOSED BOUNDARY_COMPACT contract and default-hold authoring posture / NEEDS VERIFICATION local scope ID, steward assignments, accepted inputs and outcomes, evaluator and bundle binding, complete native tests, revocation propagation, release integration, and required-check enforcement
related:
  - ../README.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../control_plane/root_registry.yaml
  - ../../contracts/policy/sensitivity_label.md
  - ../../schemas/contracts/v1/policy/sensitivity_label.schema.json
  - ../../fixtures/contracts/v1/policy/sensitivity_label/README.md
  - ../../contracts/shared/redaction_receipt.md
  - ../../schemas/contracts/v1/receipts/redaction_receipt.schema.json
  - ../../contracts/domains/people-dna-land/consent_revocation_propagation_assessment.md
  - ../../contracts/governance/sensitive_location_parity_assessment.md
  - ../../contracts/governance/sensitive_release_review_closure.md
  - ../../packages/policy-runtime/README.md
  - ../../apps/governed-api/README.md
  - ../../release/README.md
  - ../../.github/workflows/policy-test.yml
  - ../../.github/workflows/policy-boundary-guards.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# policy :: sensitivity

This directory is KFM's <strong>BOUNDARY_COMPACT local policy trust boundary</strong> for sensitivity-related rule source and candidate profiles. It inherits the canonical policy authority and limitations of [policy/](../README.md). It does not create sensitivity facts, execute policy, approve release, or publish data.

> [!IMPORTANT]
> <strong>Safe current conclusion:</strong> the tracked corpus is proposed scaffold material. It contains 16 Rego files, 11 YAML files, six Markdown files including this README, and 18 placeholder <code>.gitkeep</code> files at the required baseline. No reviewed evidence establishes an active sensitivity bundle, a general evaluator binding, complete native tests, authenticated decisions, revocation propagation, or release/publication enforcement.

> [!CAUTION]
> The corpus is not uniformly default-deny. Eleven generated Rego scaffolds use <code>default allow := false</code>. Five greenfield stubs use <code>default deny := false</code> and contain no operative denial rule. File names, comments, placeholder status, or a green structural check must not be interpreted as protection.

<strong>Quick navigation:</strong> [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Child map](#current-direct-child-map) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Inputs and outputs](#inputs-and-outputs) · [Exposure and retention](#exposure-mutation-and-retention) · [Safety posture](#default-deny-hold-and-abstain-posture) · [Evaluation boundary](#rule-source-runtime-evaluation-and-release) · [Related evidence](#related-contracts-schemas-fixtures-tests-and-release) · [Validation](#validation-coverage-and-limits) · [Correction](#correction-revocation-propagation-and-rollback) · [Open verification](#open-verification-register)

## Purpose

<code>policy/sensitivity/</code> is the local source boundary for proposed rules and profiles that constrain exposure, precision, joins, access, transformation, and release when sensitivity is material.

The boundary may express operation-specific allow, deny, hold, restrict, abstain, redaction, generalization, aggregation, or review obligations. It does not decide whether a claim is true, whether evidence is sufficient, whether rights or consent exist, or whether a release is approved. Those facts and decisions must arrive through their owning contracts, schemas, registries, evidence, runtime, and release mechanisms.

The README documents current repository evidence. It does not activate any child, repair an unsafe rule default, accept a policy profile, or authorize use of protected material.

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent | [policy/](../README.md), the canonical root for normative allow, deny, hold, restrict, and abstain rule source. |
| Directory class | <code>BOUNDARY_COMPACT</code>, because this lane changes sensitivity, exposure, mutation, and release trust assumptions. |
| Governing placement | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Sections 9.3 and 16 separate policy from contracts and schemas and define the README contract. |
| Machine projection | [root_registry.yaml](../../control_plane/root_registry.yaml) classifies <code>policy/</code> as canonical, internal, versioned, durable policy-rule authority and prohibits data instances, release decisions, and schemas. The registry is a projection, not new authority. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes <code>/policy/</code> to <code>@bartytime4life</code>. CODEOWNERS is routing only; it does not prove review, stewardship, independence, or approval. |
| Local owner | <strong>NEEDS VERIFICATION.</strong> No accepted sensitivity steward or independently authorized approver was established in the reviewed evidence. |
| Local scope ID | <strong>NEEDS VERIFICATION.</strong> No explicit scope identifier for this local boundary was found in the reviewed root registry or target tree. This README does not invent one. |
| Release authority | None. Sensitivity policy may supply a gate result, but [release/](../../release/README.md) owns release, correction, withdrawal, and rollback decisions. |
| Publication authority | None. Public carriers require a separate governed release path. |

## Current status

| Surface | Confirmed state at baseline | Safe interpretation |
|---|---|---|
| Target README | 49-byte greenfield stub, blob <code>635bbed7f1ca58f7fea5bd0a4956cdc8becb7529</code> | Boundary contract was absent before this documentation-only update. |
| Rego source | 16 proposed scaffolds; no sensitivity-native test module was found beside them | Presence does not establish parsing, evaluation, bundle selection, or enforcement. |
| Generated-style Rego | 11 files use <code>default allow := false</code> | Fail-closed-looking defaults are local source bytes only; accepted inputs, evaluator behavior, and consumer binding remain unverified. |
| Greenfield Rego | Five files use <code>default deny := false</code> and only commented example structure | These files do not deny anything and must not be cited as default-deny protection. |
| YAML profiles | 11 files, each marked <code>PROPOSED</code> or described as a placeholder | They are not accepted sensitivity registries, transforms, thresholds, or release profiles. |
| Child Markdown | Fauna, flora, plant, geoprivacy, and infrastructure documents are proposed scaffolds | Documentation does not upgrade the child lanes to implemented status. |
| Placeholder lanes | 18 tracked <code>.gitkeep</code> files under deeper children | Empty symmetry is not capability, authority, or readiness. |
| Runtime | [policy-runtime](../../packages/policy-runtime/README.md) remains a placeholder according to the parent policy evidence | No general sensitivity evaluator or production consumer is established. |
| Release/publication | Separate, governed roots and mechanisms | Nothing in this directory releases or publishes an object. |

All status claims are pinned to <code>main@a8511d3690a5009fecec508185a9baf8e2f0ecde</code>. Later changes require a fresh review.

## Current direct-child map

This map was verified against the complete tracked tree at the required baseline. It shows <code>policy/sensitivity/</code> and direct children only; child READMEs own deeper detail.

~~~text
policy/sensitivity/
├── README.md
├── agriculture/
├── archaeology/
├── archaeology_precise_coords_redaction.rego
├── atmosphere/
├── consent/
├── cultural-routes/
├── dna_segment_public_deny.rego
├── fauna/
├── flora/
├── habitat/
├── habitat_classes.yaml
├── hazards/
├── hydrology/
├── infrastructure/
├── infrastructure_interior_redaction.rego
├── joins/
├── living_person_redaction.rego
├── people/
├── people-dna-land/
├── profiles/
├── profiles.yaml
├── rare_species_location_redaction.rego
├── release/
├── rights/
├── roads-rail-trade/
├── settlement/
├── settlements-infrastructure/
├── soil/
└── transport/
~~~

Presence in this map says only that the path is tracked. It does not establish adoption, ownership, complete content, a consumer, or operational maturity. In particular, parallel-looking paths such as <code>profiles/</code> and <code>profiles.yaml</code> require classification before either is treated as canonical.

## What belongs here

The local boundary may contain reviewed, versioned sensitivity-policy source whose placement remains under the parent policy authority, including:

- Rego or another accepted declarative policy source with stable package and entrypoint identity;
- bounded sensitivity profiles, tier mappings, aggregation thresholds, and redaction/generalization obligations when their semantics are defined by contracts and their shape is defined by schemas;
- local policy-family documentation that explains rule scope, inputs, native outcomes, failure behavior, dependencies, and supersession;
- explicit references to evidence, rights, consent, source role, sensitivity labels, review state, release state, and correction state;
- public-safe reason codes and obligations that do not reveal the fact being protected; and
- version and supersession metadata needed to bind a reviewed bundle or evaluator without storing decision instances here.

A domain or topic child remains inside the <code>policy/</code> responsibility root. It does not become a new authority root.

## What is prohibited

Do not place the following in this boundary:

| Prohibited material | Owning surface or required action |
|---|---|
| Semantic meaning or object invariants | [contracts/](../../contracts/README.md) |
| JSON Schema or other machine shape | [schemas/](../../schemas/README.md) |
| Canonical, candidate, quarantined, processed, cataloged, or published data instances | Governed [data/](../../data/README.md) lifecycle and accountability lanes |
| PolicyDecision instances, review records, release decisions, correction notices, withdrawal notices, or rollback cards | Their process, evidence, or [release/](../../release/README.md) object families |
| Receipts and proofs | [data/receipts/](../../data/receipts/README.md) and [data/proofs/](../../data/proofs/README.md) |
| Reusable synthetic fixtures and executable conformance tests | [fixtures/](../../fixtures/README.md) and [tests/](../../tests/README.md), except an explicitly accepted engine-native co-location profile |
| Evaluator, API, application, cache, storage, or deployment implementation | Packages, governed applications, runtime adapters, or infrastructure as assigned by Directory Rules |
| Secrets, credentials, real protected payloads, exact sensitive locations, living-person private records, genomic material, exploit-enabling infrastructure detail, or private joins | Keep out of Git, documentation, fixtures, reasons, logs, and generated receipts; use authorized restricted systems and review |
| Release policy source under <code>release/</code> | Keep rule source under <code>policy/</code>; release records reference the exact policy version and outcome |
| Client-side hiding as the only control | Enforce sensitivity before public delivery through governed server-side interfaces and released public-safe carriers |

Existing placeholders or drift do not authorize new writes of prohibited material. Classify and migrate through a separately reviewed change with consumer, reference, correction, and rollback evidence.

## Inputs and outputs

### Candidate inputs

A mature sensitivity evaluation should receive explicit, normalized, versioned context rather than perform hidden fetches. Depending on the accepted policy family, that context may include:

- operation, actor or caller, audience, purpose, and requested precision;
- governed object, dataset, layer, feature, claim, or release-candidate references;
- evidence, source-role, rights, consent, lifecycle, review, and release references;
- a [SensitivityLabel](../../contracts/policy/sensitivity_label.md) or equivalent accepted context;
- join and re-identification risk, requested fields, geometry precision, and applicable transform profile;
- exact policy source or bundle digest, evaluator version, effective time, and correction state.

<strong>Current limitation:</strong> the reviewed sensitivity scaffolds do not define a complete accepted input contract. The items above are inherited authoring requirements and related contract surfaces, not proof that the current files consume them.

### Source outputs

Authoring in this directory produces versioned policy source, profiles, mappings, and documentation. Those source artifacts are not evaluated decisions.

If an accepted evaluator later runs a rule, it may produce engine-native outcomes and obligations. An accepted normalization contract must then map those results into the applicable decision object without collapsing deny, hold, abstain, error, or review-required states.

This directory does not emit release approval, publication state, receipts, proofs, or public payloads.

## Exposure, mutation, and retention

| Dimension | Boundary contract |
|---|---|
| Repository visibility | The repository is public, so tracked source is publicly readable. That visibility is not permission to expose protected data or to use rule files as a public API. |
| Operating exposure | The root registry classifies <code>policy/</code> as <code>internal</code>. Normal clients consume governed decisions and released public-safe outputs, not repository policy source. |
| Mutation | Versioned and review-bound. Material rule changes preserve package identity, effective time, prior version, tests, bundle/evaluator binding, and supersession lineage. |
| Retention | Durable policy source and history. Decision instances, receipts, proofs, release records, and protected payloads retain under their owning roots and policies. |
| Generation | Generated or scaffolded source remains proposed until provenance, review, deterministic regeneration, tests, and consumer binding are established. A generated package name is not activation evidence. |
| Physical storage | Restricted bytes do not belong in this Git tree. External locators do not create authority and require governed identity, access, audit, retention, and correction controls. |

## Default-deny, hold, and abstain posture

For unresolved rights, consent, sensitivity, source role, evidence, review, release state, or harmful precision, the inherited safety posture is to deny, hold, abstain, quarantine, generalize, redact, aggregate, delay, or route to authorized review. Errors must not fall back to allow.

That posture is a governance requirement, not a claim about current enforcement.

Current source evidence is mixed:

- eleven generated scaffolds define <code>default allow := false</code>;
- five greenfield stubs define <code>default deny := false</code> and no active denial conditions;
- no accepted sensitivity bundle manifest, selector, evaluator input assembly, native outcome normalization, or consumer binding was found;
- no complete sensitivity corpus test executes these 16 files; and
- no repository evidence reviewed here proves that a public request is blocked by this directory.

Until those gaps close, callers must treat current sensitivity-policy runtime behavior as <strong>UNKNOWN</strong> and hold any operation that depends on it.

## Rule source, runtime evaluation, and release

| Stage | Owning responsibility | What this directory may do | What it cannot do |
|---|---|---|---|
| Rule source | <code>policy/sensitivity/</code> under [policy/](../README.md) | Hold reviewed declarative rules and profiles. | Create evidence, rights, consent, sensitivity facts, or release state. |
| Semantic contract | [contracts/](../../contracts/README.md) | Reference accepted meanings. | Redefine meanings locally. |
| Machine shape | [schemas/](../../schemas/README.md) | Reference accepted schemas. | Treat a policy rule as schema authority. |
| Runtime evaluation | An accepted evaluator, such as a governed implementation under [policy-runtime](../../packages/policy-runtime/README.md) | Supply exact versioned source or bundle references. | Execute itself, hide fetches, authenticate actors, or invent normalized outcomes. |
| Public enforcement | Governed APIs and released public-safe artifacts, including the [governed API](../../apps/governed-api/README.md) | Provide an input to a server-side decision chain after acceptance. | Rely on browser filters, map styling, or AI explanation as the control. |
| Release/correction | [release/](../../release/README.md) plus evidence, review, receipts, and proofs | Supply a policy result and obligations. | Approve, promote, release, publish, correct, withdraw, or roll back by itself. |

A successful schema validator, static wiring job, Rego parse, unit test, workflow, or pull request is evidence about that bounded check only. None is a release decision.

## Related contracts, schemas, fixtures, tests, and release

| Family | Current linked evidence | Boundary and maturity |
|---|---|---|
| Sensitivity label meaning | [SensitivityLabel contract](../../contracts/policy/sensitivity_label.md) | Proposed semantic contract; label context is not a PolicyDecision or publication approval. |
| Sensitivity label shape | [SensitivityLabel schema](../../schemas/contracts/v1/policy/sensitivity_label.schema.json) and [synthetic fixtures](../../fixtures/contracts/v1/policy/sensitivity_label/README.md) | Proposed shape and fixture coverage. The schema-declared dedicated validator path was not found in the reviewed tree. |
| Redaction semantics | [shared RedactionReceipt contract](../../contracts/shared/redaction_receipt.md), [candidate schema](../../schemas/contracts/v1/receipts/redaction_receipt.schema.json), [fixtures](../../fixtures/contracts/v1/receipts/redaction_receipt/cases.json), and [focused validator test](../../tests/validators/test_validate_redaction_receipt.py) | A receipt records a transform; it does not prove sufficiency or authorize release. |
| Consent revocation | [propagation assessment contract](../../contracts/domains/people-dna-land/consent_revocation_propagation_assessment.md), [schema](../../schemas/contracts/v1/domains/people-dna-land/consent_revocation_propagation_assessment.schema.json), and [test](../../tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py) | Proposed assessment machinery; repository-wide operational propagation remains unverified. |
| Sensitive-location parity | [contract](../../contracts/governance/sensitive_location_parity_assessment.md), [schema](../../schemas/contracts/v1/governance/sensitive_location_parity_assessment.schema.json), and [test](../../tests/validators/test_validate_sensitive_location_parity_assessment.py) | Bounded candidate validation; not live release or runtime proof. |
| Sensitive release closure | [contract](../../contracts/governance/sensitive_release_review_closure.md), [schema](../../schemas/contracts/v1/governance/sensitive_release_review_closure.schema.json), and [test](../../tests/validators/governance/test_sensitive_release_review_closure.py) | Review-closure candidate; it does not self-authenticate or publish. |
| Release plane | [release README](../../release/README.md) | Owns separate release, correction, withdrawal, and rollback decisions; operational maturity is independently bounded. |
| Broad policy readiness | [policy-test workflow](../../.github/workflows/policy-test.yml) | Static readiness and fixture-shape holds; explicitly evaluates no general policy and emits no PolicyDecision. |
| Trust-boundary checks | [policy-boundary-guards workflow](../../.github/workflows/policy-boundary-guards.yml) | 18 structural/static/API tests; explicitly excludes policy bundles, rights/sensitivity matrices, evidence closure, and release decisions. |
| Contributor behavior | [CONTRIBUTING.md](../../CONTRIBUTING.md) and [pull-request template](../../.github/PULL_REQUEST_TEMPLATE.md) | Require private-first handling, explicit validation limits, review separation, and specific rollback. |

Small domain test files that contain only placeholder docstrings are readiness markers, not executable sensitivity evidence.

## Validation coverage and limits

| Check | Actual coverage | Explicit limitation |
|---|---|---|
| Target child-map reconciliation | Compares this README's direct-child entries with the complete tracked baseline tree. | Proves names and depth only, not semantics or maturity. |
| No-network documentation link checker | Checks local file, directory, case, and bounded fragment targets for this README; external URLs are never requested. | Does not validate authority, citations, policy meaning, or external availability. |
| Metadata-block validator, <code>present</code> profile | Validates a bounded metadata structure when present and reports registry delta. | Structural success does not establish truth, ownership, authority, adoption, or release. A missing registry entry remains review-only. |
| <code>make validate</code> | Declared to run aggregate schema validators and schema/contract tests. | It is not a sensitivity-policy evaluator and does not prove this corpus. Environment availability and actual execution must be reported separately. |
| <code>make policy</code> | Current target prints <code>TODO: opa test policy/ -v</code>. | Readiness-only; evaluates no policy. A zero exit is not validation. |
| <code>policy-test</code> | Checks broad static inventory, one separately governed Pass 12 Rego lane, PolicyDecision shape fixtures, and preserves general holds. | It does not evaluate <code>policy/sensitivity/</code> as a corpus or emit a decision. |
| <code>policy-boundary-guards</code> | Runs 18 named structural/static/API tests in four modules. | It explicitly does not evaluate policy bundles, rights/sensitivity matrices, evidence closure, or release decisions. |
| Domain placeholder tests | Several tracked Python files contain only proposed placeholder docstrings. | Collection or file presence is not behavioral proof. |
| Focused candidate validators | Some related contracts and schemas have deterministic synthetic tests. | Each proves only its declared candidate profile, not end-to-end enforcement or release. |

Do not describe <code>make policy</code>, <code>policy-test</code>, <code>policy-boundary-guards</code>, or <code>make validate</code> as complete policy or sensitivity enforcement.

## Correction, revocation propagation, and rollback

### Documentation correction

For a README defect:

1. pin current main and target bytes;
2. reconcile open work and governing evidence;
3. correct only this README unless a broader dependency is explicitly authorized;
4. rerun the same child-map, link, metadata, and diff checks;
5. keep the correction reviewable and preserve the prior blob in Git history.

Before merge, close the draft PR and delete or abandon its branch if the change should not proceed. After an authorized merge, use a transparent revert or forward-fix PR; do not rewrite shared history.

The README-only rollback target for this update is blob <code>635bbed7f1ca58f7fea5bd0a4956cdc8becb7529</code> from <code>main@a8511d3690a5009fecec508185a9baf8e2f0ecde</code>. Reverting the documentation commit restores documentation bytes only. It does not change a policy rule, evaluator, release, cache, data object, or public artifact.

### Policy correction and supersession

A material sensitivity-rule correction should:

1. preserve the prior source, package, bundle, evaluator, fixture, and test identities needed for replay;
2. issue a versioned successor with effective time, scope, reasons, and supersession linkage;
3. re-evaluate affected governed decisions and identify downstream releases or carriers;
4. append correction, withdrawal, or rollback decisions through [release/](../../release/README.md);
5. invalidate affected governed API, catalog, tile, search, cache, and AI projections when an accepted mechanism exists; and
6. emit receipts and proofs in their owning lanes without copying protected values into logs or public reason codes.

No operational policy rollback mechanism is established by this README.

### Revocation propagation

When consent, rights, authorization, or a sensitivity determination is revoked or tightened, the safe posture is immediate hold or denial for affected operations while scope is resolved. Propagation should follow stable references from the revoked authority through decisions, derived products, release records, public carriers, caches, and citations; append accountable correction or withdrawal lineage; and verify completion without exposing the protected subject.

The repository contains a proposed [consent-revocation propagation assessment](../../contracts/domains/people-dna-land/consent_revocation_propagation_assessment.md), but current evidence does not establish repository-wide runtime execution, complete dependency discovery, cache invalidation, public notification, or recovery proof. Those capabilities remain <strong>NEEDS VERIFICATION</strong>.

## Open verification register

| ID | Unresolved item | Current posture |
|---|---|---|
| SEN-001 | Accepted local <code>scope_id</code>, sensitivity steward, domain reviewers, and independent approver | <strong>NEEDS VERIFICATION</strong> |
| SEN-002 | Classification and intended future of every placeholder lane and the parallel <code>profiles/</code> versus <code>profiles.yaml</code> surfaces | <strong>NEEDS DIRECTORY REVIEW</strong> |
| SEN-003 | Whether the five <code>default deny := false</code> stubs should be corrected, replaced, migrated, or retired | <strong>HOLD — separate policy change required</strong> |
| SEN-004 | Accepted input bundle, native outcomes, normalization into decision contracts, public-safe reasons, and enforceable obligations | <strong>UNKNOWN / NEEDS DECISION</strong> |
| SEN-005 | Accepted bundle manifest, selector, evaluator, signing/provenance, runtime consumer, decision receipt, replay, expiry, and cache key contract | <strong>UNKNOWN</strong> |
| SEN-006 | Native positive and negative tests for all 16 Rego files, with synthetic public-safe fixtures and mutation/negative coverage | <strong>NOT ESTABLISHED</strong> |
| SEN-007 | Dedicated SensitivityLabel validator and enforcement of safe reason content without copying protected values | <strong>DECLARED PATH ABSENT / NEEDS IMPLEMENTATION</strong> |
| SEN-008 | End-to-end consent, rights, and sensitivity revocation propagation, including release correction, withdrawal, cache invalidation, and completion proof | <strong>PARTIAL CANDIDATE / OPERATIONAL PATH UNKNOWN</strong> |
| SEN-009 | Required-check and branch-ruleset coupling for policy, sensitivity, and independent review | <strong>UNKNOWN</strong> |
| SEN-010 | Whether current generated package names have reproducible generators, provenance, owner review, and stable regeneration commands | <strong>NEEDS VERIFICATION</strong> |
| SEN-011 | Which exact sensitivity rules, if any, are accepted for runtime or release use | <strong>NONE ESTABLISHED BY REVIEWED EVIDENCE</strong> |
| SEN-012 | Real retention, legal-hold, restricted-storage, and audit requirements for protected bytes outside Git | <strong>NEEDS POLICY AND OPERATIONS DECISION</strong> |

## Last evidence review and triggers

<strong>Reviewed:</strong> 2026-08-12 against exact <code>main@a8511d3690a5009fecec508185a9baf8e2f0ecde</code>.

Evidence included accepted ADR-0029, exact Directory Rules v2 bytes, the root registry, parent policy README, CODEOWNERS, contributor and pull-request guidance, the complete tracked <code>policy/sensitivity/</code> tree and file contents, target history, related contracts and schemas, focused fixtures and tests, release documentation, <code>Makefile</code>, <code>policy-test</code>, and <code>policy-boundary-guards</code>.

Re-review when authority, owner, scope ID, child inventory, rule default, input or outcome contract, evaluator, bundle, consumer, exposure, retention, storage, validation, CODEOWNERS, accepted ADR, release integration, correction, revocation, withdrawal, rollback, or public behavior changes.

<p align="right"><a href="#top">Back to top</a></p>
