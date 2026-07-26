<!--
KFM_DOCUMENT_CONTROL
document_id: kfm://doctrine/directory-governance/v2
title: Kansas Frontier Matrix Directory Governance Standard
short_title: Directory Rules v2
version: 2.0.0-draft.1
status: PROPOSED_FOR_ADOPTION
created: 2026-07-26
authority_class: proposed_successor_doctrine
proposed_canonical_home: docs/doctrine/directory-rules.md
supersession_effect: none_until_adopted
source_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  commit: 00d33c0e3a2b970bfde8a88e36b76cd834319d75
  branch: agent/harden-fauna-fixture-safety-20260725
-->

<a id="top"></a>

# Kansas Frontier Matrix Directory Governance Standard

## Directory Rules v2.0.0-draft.1

> **Operating law:** A path is an authority claim. Place an artifact by the one responsibility that owns it, then refine by lifecycle, execution role, scope, exposure, mutability, and retention. A topic, filename, producer, or convenient import path never creates authority.

> [!IMPORTANT]
> This is a **complete proposed successor**, not an adopted rule set. Until an accepted decision adopts it, the current KFM placement doctrine remains controlling. Adoption should make `docs/doctrine/directory-rules.md` the single canonical human-readable rules file and convert `docs/architecture/directory-rules.md` into a temporary, read-only redirect before retirement.

| Field | Value |
|---|---|
| Document class | Governance doctrine and placement standard |
| Version | `2.0.0-draft.1` |
| Status | `PROPOSED_FOR_ADOPTION` |
| Date | 2026-07-26 |
| Proposed canonical home | `docs/doctrine/directory-rules.md` |
| Proposed machine projection | `control_plane/root_registry.yaml` |
| Proposed validator family | `tools/validators/directory_governance/` |
| Proposed conformance outcomes | `PLACE`, `SPLIT`, `MIGRATE`, `MIRROR`, `HOLD`, `DENY` |
| Supersedes | The attached unversioned `Directory Rules.pdf`, repository `docs/doctrine/directory-rules.md` v1.4, and repository `docs/architecture/directory-rules.md` v1.3.1 **only after adoption** |
| Primary reviewer classes | Documentation governance, architecture, affected responsibility-root owner, and an independent reviewer for authority-changing decisions |
| Core invariant | `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED`; promotion is a governed state transition, not a file move |

## Executive change summary

The existing rules establish the right foundation: responsibility roots, domain-as-lane placement, lifecycle separation, compatibility-root controls, migration discipline, and a prohibition on parallel authority. The next generation keeps those principles and corrects the parts that do not scale.

| Current limitation | v2 resolution |
|---|---|
| The supplied PDF has no explicit edition, effective date, adoption record, or rule identifiers. | Versioned document control, adoption state, stable rule IDs, and explicit supersession behavior. |
| Rules, proposed paths, live implementation, and illustrative trees are interleaved. | Normative core, machine projection, root profiles, and repository-specific convergence appendix are separated. |
| â€œChoose exactly one responsibilityâ€ is useful but too coarse for composite objects. | Every artifact receives one **authority owner** and may reference many related concerns; mixed authority requires `SPLIT`. |
| A new compatibility root both requires an ADR and, elsewhere, does not require one. | One rule: any tracked compatibility or conditional root requires an accepted decision before admission. |
| Product decisions such as renderer selection enter placement doctrine. | Directory law governs **where a renderer implementation belongs**; accepted architecture decisions govern **which renderer exists**. |
| Root status is expressed only in prose. | Canonical, platform, conditional, compatibility, deprecated, and retired root classes have machine-checkable fields. |
| No deterministic tie-breaker exists when two roots appear plausible. | A responsibility signature plus hard exclusion predicates produces a finite placement outcome. |
| Directory READMEs repeat large, stale trees and uniform long section lists. | Full root, lane, and leaf README profiles with inheritance; directory trees show the current directory and direct children only. |
| Path spelling, singular/plural forms, domain aliases, and language identifiers drift independently. | Registered path slugs, collection naming rules, explicit code-identifier aliases, and case-collision controls. |
| Logical KFM homes and physical byte storage are not separated. | Logical authority remains stable even when payloads live in object storage, a database, package registry, or CI cache. |
| Enforcement is mostly documentary. | A root registry, alias register, schema, validator, negative fixtures, and CI gate form an executable projection of adopted law. |

## Contents

1. [Status, scope, and non-effects](#1-status-scope-and-non-effects)
2. [Authority model](#2-authority-model)
3. [Truth labels and placement outcomes](#3-truth-labels-and-placement-outcomes)
4. [The responsibility signature](#4-the-responsibility-signature)
5. [Deterministic placement protocol](#5-deterministic-placement-protocol)
6. [Root classes and admission](#6-root-classes-and-admission)
7. [Canonical root registry](#7-canonical-root-registry)
8. [Repository-root files and platform directories](#8-repository-root-files-and-platform-directories)
9. [Governance and authority roots](#9-governance-and-authority-roots)
10. [Implementation and operations roots](#10-implementation-and-operations-roots)
11. [Data, evidence, and release placement](#11-data-evidence-and-release-placement)
12. [Domain, source, geography, and cross-domain scope](#12-domain-source-geography-and-cross-domain-scope)
13. [Names, identity, and collection grammar](#13-names-identity-and-collection-grammar)
14. [Dependency direction](#14-dependency-direction)
15. [Generated output, external storage, and caches](#15-generated-output-external-storage-and-caches)
16. [README contracts and documentation inheritance](#16-readme-contracts-and-documentation-inheritance)
17. [Compatibility, aliases, and deprecation](#17-compatibility-aliases-and-deprecation)
18. [Migration, correction, and rollback](#18-migration-correction-and-rollback)
19. [Machine enforcement](#19-machine-enforcement)
20. [Current repository convergence map](#20-current-repository-convergence-map)
21. [Adoption and implementation sequence](#21-adoption-and-implementation-sequence)
22. [Reviewer checklist](#22-reviewer-checklist)
23. [Glossary](#23-glossary)
24. [Appendix A: placement examples](#appendix-a-placement-examples)
25. [Appendix B: evidence ledger](#appendix-b-evidence-ledger)

---

## 1. Status, scope, and non-effects

### 1.1 What these rules govern

These rules govern:

- tracked repository roots and root files;
- canonical, conditional, platform, compatibility, deprecated, and retired homes;
- ownership of semantic contracts, schemas, policy, data instances, release decisions, implementation, tests, configuration, and generated output;
- domain and cross-domain lane placement;
- path naming, aliases, migrations, README inheritance, and conformance evidence;
- logical KFM homes even when physical bytes are stored elsewhere.

### 1.2 What these rules do not decide

Directory governance does not decide:

- whether an object, source, feature, renderer, model, domain, or release should exist;
- the field-level shape of an object;
- whether data is admissible, rights-cleared, public-safe, or ready for release;
- whether a proposed ADR is accepted;
- whether a passing test proves publication, deployment, or operational maturity.

Those decisions remain with contracts, schemas, policy, accepted ADRs, source admission, evidence, review, release, correction, and rollback controls.

### 1.3 Non-effects

`DIR-SCOPE-001` â€” A path does not grant truth, source authority, rights, sensitivity clearance, review, release, or publication status.

`DIR-SCOPE-002` â€” A filename such as `release_manifest.json`, a signature, a passing workflow, or placement under `data/published/` does not substitute for governed closure.

`DIR-SCOPE-003` â€” Documentation may describe authority but cannot create machine, policy, release, or data authority outside the decision class it legitimately owns.

`DIR-SCOPE-004` â€” This draft does not move, rename, publish, promote, delete, or authorize any repository object.

---

## 2. Authority model

### 2.1 Placement authority order

When sources disagree about placement, apply this order:

1. KFM trust, safety, lifecycle, evidence, public-boundary, correction, and rollback invariants.
2. Accepted, unsuperseded ADRs, only within their stated scope.
3. The adopted Directory Rules edition.
4. Non-conflicting per-root and adjacent `README.md` contracts.
5. Current repository evidence, as implementation fact rather than automatic canon.
6. Architecture manuals, domain dossiers, atlases, prompts, and prior plans as design lineage.
7. Generic convention or personal preference.

`DIR-AUTH-001` â€” A proposed, draft, rejected, or superseded ADR cannot amend placement doctrine.

`DIR-AUTH-002` â€” Current repository convention that conflicts with higher authority is drift, not precedent.

`DIR-AUTH-003` â€” A per-root README may narrow or explain a root contract; it may not expand its authority.

### 2.2 Authority freeze and two-change rule

Structural work must freeze its authority inputs before editing.

`DIR-AUTH-004` â€” A change may not edit Directory Rules or an ADR and then use that unaccepted edit to authorize dependent root, lifecycle, or parallel-home changes in the same authority batch.

For a new canonical, conditional, or compatibility root:

1. **Decision change:** accept the ADR and update the adopted rules or root registry projection.
2. **Implementation change:** add or migrate the root after the decision is effective.

Emergency containment may quarantine or stop writes immediately, but it must not declare a new canonical home.

### 2.3 Amendment classes

| Change | Required authority |
|---|---|
| Typo, link repair, clearer example with no changed meaning | Routine review |
| Per-root refinement inside an existing authority boundary | Root owner review |
| New path alias for a verified consumer | Migration record and root owner review |
| New canonical, conditional, or compatibility root | Accepted ADR, then implementation change |
| Root rename, merge, split, retirement, or promotion | Accepted ADR and migration plan |
| Lifecycle phase or release/data authority change | Accepted ADR and independent trust review |
| Naming convention inside one root | Root README decision unless identity or compatibility changes |
| Rule that changes an object family's authority owner | Accepted ADR, compatibility analysis, correction and rollback plan |

---

## 3. Truth labels and placement outcomes

Truth state and placement result are different axes. They must not be collapsed.

### 3.1 Truth labels

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current-session repository evidence, a supplied source, test, log, or generated artifact. |
| `PROPOSED` | A design or decision not yet adopted or implemented. |
| `UNKNOWN` | Evidence is insufficient to determine the answer. |
| `NEEDS_VERIFICATION` | A concrete check can resolve the question but has not yet been completed. |
| `CONFLICTED` | Two or more admissible sources or writable homes claim incompatible authority. |
| `LINEAGE` | Retained history or prior design; not current authority by itself. |

### 3.2 Finite placement outcomes

| Outcome | Meaning | Required action |
|---|---|---|
| `PLACE` | Exactly one canonical home satisfies every hard rule. | Create or edit at that home. |
| `SPLIT` | The proposed artifact contains more than one authority owner. | Split into linked artifacts, each with one owner. |
| `MIGRATE` | An existing artifact has a known canonical target but currently lives elsewhere. | Freeze writes and follow migration discipline. |
| `MIRROR` | A verified consumer requires a derived, one-way compatibility copy. | Generate from canonical; prohibit direct edits and set exit criteria. |
| `HOLD` | Ownership, authority, identity, sensitivity, or target evidence is unresolved. | Do not create a new home; open verification or drift work. |
| `DENY` | The path would violate an invariant, expose protected state, or create parallel authority. | Reject the placement. |

`DIR-OUTCOME-001` â€” â€œProbably hereâ€ is not a conformance outcome.

`DIR-OUTCOME-002` â€” A `HOLD` is an intentional fail-closed result, not an implementation failure.

---

## 4. The responsibility signature

Before proposing or changing a path, describe the artifact with the following signature:

| Axis | Required values or questions |
|---|---|
| `artifact_kind` | Human document, machine register, semantic contract, schema, policy rule, executable code, data instance, release decision, test, fixture, config, migration, example, generated output |
| `authority_owner` | Which responsibility is allowed to define or mutate this artifact? |
| `lifecycle_stage` | Not applicable, pre-RAW event, RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, PUBLISHED, receipt, proof, registry |
| `execution_role` | None, deployable, reusable library, source connector, transformation pipeline, declarative spec, repository tool, thin script, runtime adapter, infrastructure |
| `scope_kind` | Global, domain, source, geography/focus scope, cross-domain seam, object family |
| `scope_id` | Registered domain/source/scope/object identifier |
| `exposure` | Public, semi-public, internal, steward-only, restricted |
| `mutability` | Immutable, append-only, versioned replacement, generated, ephemeral |
| `retention` | Durable, release-bound, audit-bound, cacheable, disposable |
| `physical_storage` | Git, database, object storage, package registry, CI artifact, external system |

`DIR-SIGNATURE-001` â€” Every artifact has exactly one `authority_owner`.

`DIR-SIGNATURE-002` â€” An artifact may reference many related authorities without owning them. A `ReleaseManifest`, for example, may reference proofs, catalog records, policy decisions, and published carriers while remaining a release-governance object.

`DIR-SIGNATURE-003` â€” If two authority owners would need to edit the same artifact independently, return `SPLIT`.

`DIR-SIGNATURE-004` â€” The producer does not determine the home. A pipeline may produce a receipt, proof, catalog record, or published carrier; each output goes to its owning family.

---

## 5. Deterministic placement protocol

### 5.1 Decision sequence

Apply these gates in order:

1. **Classify authority.** Identify the artifact kind and one authority owner.
2. **Choose the candidate responsibility root.** Use the root registry in Â§7.
3. **Apply hard exclusions.** Reject roots that prohibit the artifact, exposure, mutation, or lifecycle state.
4. **Classify executable role.** For code, distinguish deployable, reusable, connector, pipeline, tool, script, adapter, and infrastructure.
5. **Classify lifecycle.** For data instances, choose the state or accountability lane.
6. **Add scope.** Add a registered domain, source, geography, seam, or object-family segment only after the root is fixed.
7. **Apply identity and naming rules.** Use registered slugs and collection grammar.
8. **Check for parallel authority and aliases.** Search canonical, compatibility, generated, and legacy homes.
9. **Check dependency direction.** A correct-looking path with a forbidden dependency is nonconforming.
10. **Emit one finite outcome.** Record rule IDs and evidence.

### 5.2 Formal uniqueness rule

Let `C(x)` be the set of roots whose responsibility includes artifact `x`. Remove every root that violates a hard exclusion for authority, lifecycle, execution role, exposure, mutability, or retention.

- If `|C(x)| = 1`, return `PLACE`.
- If `|C(x)| > 1` because the artifact carries multiple owners, return `SPLIT`.
- If `|C(x)| > 1` because roots claim the same owner, return `HOLD` or `DENY` for parallel authority.
- If `|C(x)| = 0` and a current artifact exists, return `HOLD`; do not invent a root.
- If a unique target exists but the artifact is elsewhere, return `MIGRATE`.
- If a noncanonical copy is required by a verified consumer, return `MIRROR`.

### 5.3 Hard exclusion predicates

`DIR-PLACE-001` â€” Domain, source, county, feature, renderer, model, or data format names do not justify repository roots.

`DIR-PLACE-002` â€” Public and ordinary UI paths may not read RAW, WORK, QUARANTINE, restricted, canonical/internal, or unreleased candidate stores.

`DIR-PLACE-003` â€” Connectors may emit only to RAW, QUARANTINE, and their corresponding receipts; they do not publish.

`DIR-PLACE-004` â€” Watchers may emit events, candidate work, and receipts; they do not approve promotion, rewrite catalog authority, or publish.

`DIR-PLACE-005` â€” Generated output under `artifacts/`, caches, examples, or fixtures cannot satisfy canonical contract, policy, evidence, catalog, release, or publication authority.

`DIR-PLACE-006` â€” A compatibility root is never a writable alternative to its canonical target.

`DIR-PLACE-007` â€” Exact sensitive geometry, living-person data, DNA/genomic material, archaeology, rare-species locations, or protected infrastructure information cannot be made public-safe by path placement.

`DIR-PLACE-008` â€” A root or lane may be justified by a durable trust boundary even when it initially contains one file; file count alone never overrides authority.

### 5.4 Path decision record

Every structural PR should include:

~~~yaml
path_decision:
  artifact: "<stable artifact or object-family name>"
  proposed_path: "<path>"
  artifact_kind: "<kind>"
  authority_owner: "<one owner>"
  lifecycle_stage: "<stage or not_applicable>"
  execution_role: "<role or none>"
  scope_kind: "<global|domain|source|geography|cross_domain|object_family>"
  scope_id: "<registered id>"
  exposure: "<public|semi_public|internal|steward_only|restricted>"
  mutability: "<immutable|append_only|versioned|generated|ephemeral>"
  evidence: ["<repo path, accepted ADR, or source>"]
  rules: ["DIR-..."]
  outcome: "<PLACE|SPLIT|MIGRATE|MIRROR|HOLD|DENY>"
~~~

---

## 6. Root classes and admission

### 6.1 Root classes

| Class | Purpose | Writable? | Admission |
|---|---|---:|---|
| `canonical` | Stable repo-wide responsibility and authority boundary | Yes, within contract | Accepted Directory Rules or ADR |
| `platform` | Tool- or host-required integration surface such as `.github/` | Yes, narrowly | Root registry entry; ADR if it gains KFM authority |
| `conditional` | Valid only while an explicit project profile exists, such as a root distribution facade | Yes, narrowly | Accepted ADR with activation and exit conditions |
| `compatibility` | Legacy, mirror, external export, or transition path | No independent writes | Accepted ADR, canonical target, owner, and exit criteria |
| `deprecated` | Frozen path awaiting verified retirement | No | Deprecation record and migration status |
| `retired` | Historical identity only; no tracked authority-bearing content | No | Retirement receipt and reference closure |

### 6.2 Root admission test

A proposed tracked root must satisfy every applicable condition:

1. The responsibility is repository-wide and materially distinct.
2. No existing canonical root can own it without violating that root's contract.
3. The root creates a real authority, execution, platform, or lifecycle boundary rather than a topic bucket.
4. Its dependency direction is explicit.
5. Its public exposure, mutation, retention, and secret posture are explicit.
6. It has an owner, review burden, README profile, validation plan, migration plan, and rollback plan.
7. It does not create a parallel home.
8. An accepted ADR authorizes canonical, conditional, or compatibility status.
9. The machine root registry is updated only as a projection of the accepted decision.

`DIR-ROOT-001` â€” Untracked build directories, language caches, virtual environments, and local editor state are not repository roots; they belong in ignore policy.

`DIR-ROOT-002` â€” A new compatibility root is an architectural commitment and always requires an accepted decision. This resolves the contradictory v1 treatment.

`DIR-ROOT-003` â€” A tool-mandated dot directory may be admitted as `platform` without an ADR only when it owns no KFM truth, semantics, schema, policy, lifecycle data, evidence, release, or publication authority.

`DIR-ROOT-004` â€” Do not create a directory merely to reserve a possible future path. A new directory must contain an admitted implementation or data artifact, establish a real authority or trust boundary, or serve as a declared compatibility pointer with owner, target, and exit condition.

`DIR-ROOT-005` â€” A README and `.gitkeep` alone do not establish implementation, maturity, or a reason to retain speculative scaffolding.

### 6.3 Root state transitions

~~~text
PROPOSED
â””â”€â”€ ACCEPTED
    â””â”€â”€ ACTIVE
        â”œâ”€â”€ DEPRECATED
        â”‚   â””â”€â”€ RETIRED
        â””â”€â”€ SUPERSEDED
            â””â”€â”€ RETIRED
~~~

No root moves directly from `PROPOSED` to `ACTIVE` without an effective decision. No retired root may be recreated under the same name without a new ADR that addresses identity reuse.

---

## 7. Canonical root registry

### 7.1 Normalized root tree

The tree below shows repository root and direct children only.

~~~text
Kansas-Frontier-Matrix/
â”œâ”€â”€ .github/               # platform integration and repository automation
â”œâ”€â”€ apps/                  # deployable applications
â”œâ”€â”€ configs/               # non-secret configuration profiles and templates
â”œâ”€â”€ connectors/            # source acquisition and admission edges
â”œâ”€â”€ contracts/             # semantic and interface meaning
â”œâ”€â”€ control_plane/         # machine projections of governance
â”œâ”€â”€ data/                  # governed instances, lifecycle, and delivery carriers
â”œâ”€â”€ docs/                  # human doctrine, decisions, architecture, and guidance
â”œâ”€â”€ examples/              # runnable public-safe demonstrations
â”œâ”€â”€ fixtures/              # reusable synthetic, valid, invalid, and golden inputs
â”œâ”€â”€ infra/                 # deployment and exposure infrastructure
â”œâ”€â”€ migrations/            # migration implementation and rollback definitions
â”œâ”€â”€ packages/              # reusable non-deployable implementation
â”œâ”€â”€ pipeline_specs/        # declarative pipeline definitions
â”œâ”€â”€ pipelines/             # executable lifecycle transformations
â”œâ”€â”€ policy/                # normative allow, deny, hold, restrict, and abstain rules
â”œâ”€â”€ release/               # release, correction, withdrawal, and rollback decisions
â”œâ”€â”€ runtime/               # bounded runtime composition and local adapters
â”œâ”€â”€ schemas/               # machine-checkable shapes
â”œâ”€â”€ scripts/               # thin non-authoritative operator wrappers
â”œâ”€â”€ tests/                 # executable conformance evidence
â””â”€â”€ tools/                 # repository-wide validators, generators, and operators
~~~

### 7.2 Canonical responsibility table

| Root | Owns | Explicitly does not own |
|---|---|---|
| `.github/` | Workflows, templates, CODEOWNERS routing, repository automation | KFM truth, release approval, proof that review ran |
| `docs/` | Human-readable doctrine, accepted decisions, architecture, runbooks, domain guidance, registers presented for people | Machine schema, executable policy, data instances, release status by prose alone |
| `control_plane/` | Machine-readable projections and indexes of what governs what | Source payloads, normative policy code, domain truth, release decisions |
| `contracts/` | Semantic meaning and interface promises | Canonical machine shape, policy outcome, data instance |
| `schemas/` | Machine-checkable shape, contexts, generated type authority where declared | Object meaning, admissibility, release decision |
| `policy/` | Normative decision rules and policy bundles | Decision instances, published data, schema authority |
| `tests/` | Executable conformance, boundary, negative, integration, and end-to-end evidence | Unique production behavior or canonical fixtures |
| `fixtures/` | Reusable public-safe or synthetic test inputs and expected outputs | Real sensitive source payloads, published truth, production state |
| `tools/` | Repository-wide validators, generators, builders, inspectors, and operators | Deployable services, hidden domain authority |
| `scripts/` | Thin wrappers around governed tools and routine maintenance entrypoints | Unique trust-bearing logic or permanent one-off archives |
| `apps/` | Deployable processes and user-facing service boundaries | Reusable libraries, canonical data, machine schema authority |
| `packages/` | Reusable, independently testable, non-deployable code | Deployment, source acquisition identity, release approval |
| `connectors/` | Source-specific fetch, capture, and admission implementation | Normalization authority, cataloging, promotion, publication |
| `pipelines/` | Executable transformations and lifecycle orchestration | Declarative run definitions, source authority, release approval |
| `pipeline_specs/` | Declarative run graphs, schedules, inputs, outputs, and resource envelopes | Executable transformation code |
| `data/` | Governed data and accountability instances, projections, and released carriers | Normative contracts, schema, policy, or release approval |
| `release/` | Promotion, release, correction, withdrawal, rollback, and signature records | Published carrier bytes, policy source, proofs as substitutes for decisions |
| `runtime/` | Bounded process composition, local adapters, provider harnesses, deterministic mocks | Domain business logic, public ingress, canonical data, deployment topology |
| `infra/` | Deployment, network, host, access, secret-reference, and exposure configuration | Application business logic or actual secrets |
| `configs/` | Non-secret defaults, profiles, templates, and examples | Secrets, canonical policy, release decisions |
| `migrations/` | Versioned migration implementation, mapping manifests, forward/rollback definitions | Execution receipts or authority-changing decisions |
| `examples/` | Runnable, public-safe demonstrations of supported use | Tests, fixtures, canonical data, release proof |

### 7.3 Noncanonical roots in the current project

| Root | v2 class | Proposed posture |
|---|---|---|
| `artifacts/` | `compatibility` / generated-output transition | Allow only `build/`, `docs/`, `qa/`, and `temporary/`; no trust-bearing payloads; work toward ignored or external CI output. |
| `catalog/` | `deprecated` containment root | Freeze all writes, preserve redirect documentation during migration, then retire after zero-producer and zero-consumer proof. |
| `src/` | `conditional`, currently unresolved | Permit only an accepted root-distribution facade profile; otherwise migrate reusable code to `packages/`. Current minimal facade remains `HOLD` pending a decision. |
| `jsonschema/`, `policies/`, `ui/`, `web/`, `styles/`, `viewer_templates/` | Potential `compatibility` roots | Do not create. If discovered, inventory, classify, and migrate to canonical homes. |

---

## 8. Repository-root files and platform directories

### 8.1 Root-file law

Only repository-wide identity, governance, build, packaging, security, and ecosystem entrypoints belong directly at root.

Allowed classes include:

- `README.md`, `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `AUTHORS.md`, and `CITATION.cff`;
- root build and package manifests such as `Makefile`, `pyproject.toml`, `package.json`, and lockfiles when they coordinate the repository;
- tool configuration such as `.editorconfig`, `.gitignore`, and reviewed pre-commit configuration;
- one canonical root map or bootstrap manifest when it is machine-validated and does not duplicate the root registry.

`DIR-ROOTFILE-001` â€” Domain documents, datasets, schemas, policy, scripts, and release objects may not live directly at root.

`DIR-ROOTFILE-002` â€” A root build manifest may coordinate child workspaces but may not become a second package, schema, policy, or release authority.

`DIR-ROOTFILE-003` â€” A root `src/` layout is not implied merely because `pyproject.toml` exists; the root distribution profile must be explicit.

### 8.2 Platform directories

Platform-required directories such as `.github/` may contain only the integration surface required by that platform.

- Workflow results are run artifacts, not KFM receipts, proofs, or releases unless a governed process promotes them to the canonical family.
- CODEOWNERS routes review requests; it is not proof of review or separation of duties.
- Repository templates may require evidence and rule IDs but may not amend doctrine.
- Secrets are referenced by name; they are never committed.

---

## 9. Governance and authority roots

### 9.1 `docs/`

`docs/` is the human-readable governance and explanation surface.

~~~text
docs/
â”œâ”€â”€ adr/                    # architecture decisions and decision history
â”œâ”€â”€ architecture/           # system structure subordinate to accepted decisions
â”œâ”€â”€ archive/                # frozen lineage, not current authority
â”œâ”€â”€ atlases/                # curated atlas collections
â”œâ”€â”€ doctrine/               # stable KFM operating and trust law
â”œâ”€â”€ domains/                # human domain guidance
â”œâ”€â”€ registers/              # human-readable drift and verification views
â”œâ”€â”€ runbooks/               # operational procedures
â”œâ”€â”€ security/               # threat, incident, and exposure guidance
â”œâ”€â”€ sources/                # source guidance and human source catalog
â””â”€â”€ standards/              # KFM and external standards guidance
~~~

`DIR-DOCS-001` â€” Directory Rules belong in `docs/doctrine/` because they are stable governance law, not a product architecture decision.

`DIR-DOCS-002` â€” `docs/architecture/directory-rules.md` becomes a time-bounded redirect after v2 adoption and must not evolve independently.

`DIR-DOCS-003` â€” Collections use plural lane names; therefore `docs/atlases/` is the proposed canonical collection and `docs/atlas/` is a migration candidate.

`DIR-DOCS-004` â€” Human source descriptions under `docs/sources/` do not replace machine source registry instances under `data/registry/`.

### 9.2 `control_plane/`

`control_plane/` contains machine-readable projections of adopted governance:

- document, authority, domain, object-family, policy-gate, release-state, root, alias, deprecation, contradiction, and verification registers;
- stable crosswalks between human decisions and machine enforcement;
- no source payloads, domain truth, release approval, or policy source code.

`DIR-CONTROL-001` â€” A control-plane register is a projection of accepted authority; editing a register cannot self-authorize a new rule.

`DIR-CONTROL-002` â€” A registry entry must cite its governing document or accepted ADR and carry status, effective scope, and evidence snapshot.

### 9.3 `contracts/`, `schemas/`, and `policy/`

The three-way split is mandatory:

| Root | Question answered |
|---|---|
| `contracts/` | What does this object or interface mean? |
| `schemas/` | What machine shape is valid? |
| `policy/` | Under what conditions is it allowed, denied, held, restricted, or abstained? |

`DIR-AUTHROOT-001` â€” Machine schemas default to `schemas/contracts/v1/<family>/` unless an accepted ADR establishes another versioned schema profile.

`DIR-AUTHROOT-002` â€” `contracts/` may contain semantic Markdown and interface specifications, but a duplicated schema embedded there must be generated from or reference the canonical schema.

`DIR-AUTHROOT-003` â€” Policy rule source is singular under `policy/`. Policy decision instances belong with the process or release object they record; they do not live beside the rule merely because the type is â€œpolicy.â€

`DIR-AUTHROOT-004` â€” Generated language bindings and types are derived artifacts; their README must name the schema source and regeneration command.

---

## 10. Implementation and operations roots

### 10.1 Executable role routing

| Question | Root |
|---|---|
| Is it an independently deployable process or user surface? | `apps/` |
| Is it reusable by more than one deployable or bounded context? | `packages/` |
| Does it acquire from and admit one external source/provider? | `connectors/` |
| Does it transform or orchestrate lifecycle state? | `pipelines/` |
| Does it declaratively describe a run graph or schedule? | `pipeline_specs/` |
| Is it a repository-wide validator, generator, inspector, or operator? | `tools/` |
| Is it only a thin invocation wrapper with no unique trust logic? | `scripts/` |
| Does it compose local providers/adapters for a running process? | `runtime/` |
| Does it deploy, network, expose, harden, or provision? | `infra/` |
| Is it non-secret configuration shared by several owners? | `configs/` |

`DIR-EXEC-001` â€” A deployment wrapper in `apps/` should delegate reusable logic to `packages/`, source acquisition to `connectors/`, and transformations to `pipelines/`.

`DIR-EXEC-002` â€” A source/provider name may appear inside `connectors/`; it does not create a root. Connectors are source-first because one source may feed several domains.

`DIR-EXEC-003` â€” Domain-specific normalization belongs in `pipelines/<stage>/<domain>/` or a domain package, not in the source connector unless the source and domain are provably identical and declared.

`DIR-EXEC-004` â€” Executable pipeline implementation is stage-first:

~~~text
pipelines/
â”œâ”€â”€ ingest/
â”œâ”€â”€ normalize/
â”œâ”€â”€ validate/
â”œâ”€â”€ catalog/
â”œâ”€â”€ triplets/
â”œâ”€â”€ publish/
â””â”€â”€ rollback/
~~~

A domain is added below the applicable stage. Shared stage code uses an explicitly named shared lane. `pipelines/domains/<domain>/<stage>/` and `pipelines/<stage>/<domain>/` may not both be writable.

`DIR-EXEC-005` â€” `pipeline_specs/` owns declarative whole-run or domain-run definitions. `pipelines/specs/` is a compatibility candidate and must not become a second spec authority.

`DIR-EXEC-006` â€” `tools/validate_all.py` may remain a thin repository entrypoint while validator implementation lives under `tools/validators/`. A placeholder entrypoint is not proof of orchestration.

`DIR-EXEC-007` â€” Trust-bearing or reused logic must graduate from `scripts/` to `tools/`, `pipelines/`, `packages/`, or `connectors/`. Scripts call governed implementations; production implementations do not import scripts.

### 10.2 Conditional root `src/`

A root `src/` is permitted only under an accepted **root distribution facade** profile:

- the root build manifest intentionally produces one aggregate distribution;
- `src/<package>/` contains a bounded public facade, version metadata, or compatibility exports;
- domain and reusable implementation remain under `packages/`;
- dependency direction is facade -> packages, never packages -> facade;
- the facade has explicit API, packaging, test, version, deprecation, and release contracts;
- removal conditions are defined if no verified consumer requires the distribution.

Without this profile, root `src/` returns `HOLD` and accepts no new implementation.

### 10.3 Runtime boundary

`runtime/` is intentionally narrow:

- provider adapters and deterministic mock harnesses used to compose a running process;
- local-only wiring that is neither reusable package logic nor deployment infrastructure;
- no domain directories merely to hold topic-specific code;
- no public ingress, canonical store, release decision, or direct model endpoint exposure.

Domain behavior under `runtime/<domain>/` should be reclassified to an app, package, pipeline, config, or test lane.

### 10.4 Configuration ownership

Configuration follows its consumer unless it is genuinely shared:

| Configuration kind | Home |
|---|---|
| Repository-wide non-secret profile or template | `configs/` |
| One app's configuration | Colocated under the app, referencing shared defaults |
| Declarative pipeline run definition | `pipeline_specs/` |
| Infrastructure deployment configuration | `infra/` |
| Provider adapter configuration | Colocated with the adapter or in `configs/` when shared |
| Secret value | External secret store; never Git |
| Executable admissibility rule | `policy/`, not `configs/` |

---

## 11. Data, evidence, and release placement

### 11.1 Data is three related planes

The `data/` root contains three different kinds of instance state. They must not be described as one flat list of lifecycle phases.

1. **Lifecycle state:** pre-RAW intake, RAW, WORK, QUARANTINE, PROCESSED.
2. **Derived and delivery projections:** CATALOG, TRIPLETS, PUBLISHED.
3. **Accountability and identity stores:** RECEIPTS, PROOFS, REGISTRY.

`release/` is a separate decision plane.

### 11.2 Normalized data tree

The tree shows `data/` and its direct children only.

~~~text
data/
â”œâ”€â”€ pre_raw/                # conditional event/intake envelopes; not admitted source data
â”œâ”€â”€ raw/                    # immutable source-edge captures
â”œâ”€â”€ work/                   # mutable/versioned candidate transformations
â”œâ”€â”€ quarantine/             # held material plus remediation obligations
â”œâ”€â”€ processed/              # validated canonical records; not automatically public
â”œâ”€â”€ catalog/                # STAC, DCAT, PROV, domain and closure projections
â”œâ”€â”€ triplets/               # optional relationship/graph projections
â”œâ”€â”€ receipts/               # durable process memory
â”œâ”€â”€ proofs/                 # evidence, validation, citation, review and integrity support
â”œâ”€â”€ registry/               # source, dataset, layer, rights and sensitivity identities
â””â”€â”€ published/              # immutable release-approved public-safe carriers
~~~

`DIR-DATA-001` â€” `pre_raw/` is a conditional intake lane, not a new source-of-truth phase. It may hold bounded event envelopes and admission candidates; persistent admission actions emit receipts. If KFM does not implement a durable pre-RAW queue, the lane remains absent.

`DIR-DATA-002` â€” Valid material does not have to pass through QUARANTINE. TRIPLETS are optional when no graph projection is required.

`DIR-DATA-003` â€” The lifecycle is a state machine, not a demand that every artifact visit every directory:

~~~text
PRE_RAW â”€â”€admitâ”€â”€> RAW
RAW â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€> WORK
RAW â”€â”€holdâ”€â”€â”€â”€â”€â”€â”€> QUARANTINE
WORK â”€â”€validateâ”€â”€> PROCESSED
WORK â”€â”€holdâ”€â”€â”€â”€â”€â”€> QUARANTINE
QUARANTINE â”€â”€remediateâ”€â”€> WORK
PROCESSED â”€â”€â”€â”€â”€â”€â”€> CATALOG
PROCESSED â”€â”€â”€â”€â”€â”€â”€> TRIPLETS        # when applicable
CATALOG + PROOF + RELEASE DECISION â”€â”€> PUBLISHED
~~~

`DIR-DATA-004` â€” Promotion emits a new governed state or version. It is never inferred from a copy, move, filename, job completion, or mutable alias.

`DIR-DATA-005` â€” Canonical trust-instance lanes such as `data/proofs/`, `data/catalog/`, `data/published/`, and release record collections may not contain objects that self-identify as placeholders, scaffolds, templates, or merely `PROPOSED` instances. Draft examples belong in `fixtures/`, `configs/templates/`, QUARANTINE, or `release/candidates/`.

### 11.3 Lifecycle and accountability contracts

| Lane | Owns | Prohibits |
|---|---|---|
| `pre_raw/` | Bounded intake events and admission candidates | Public consumption, source authority, unbounded queue dumps |
| `raw/` | Immutable captured source bytes or logical pointers with retrieval identity | Normalized claims, public routes, direct AI context |
| `work/` | Candidate normalization, georeferencing, crosswalk, and transform state | Release aliases and public access |
| `quarantine/` | Held material, reason codes, obligations, remediation linkage | Promotion without recorded exit |
| `processed/` | Validated canonical records and deterministic versions | Assumption of public safety or release |
| `catalog/` | Discovery, interoperability, provenance, and closure projections | Canonical replacement truth or hand-authored release approval |
| `triplets/` | Rebuildable relationship projections | Replacement of canonical records |
| `receipts/` | What process ran, on what, with which inputs, tools, policies, and outputs | Proof or approval by itself |
| `proofs/` | EvidenceBundle, validation, citation, review, integrity, and proof-pack support | Release decision by itself |
| `registry/` | Stable source, dataset, layer, rights, sensitivity, and crosswalk identities | Canonical domain facts or public payloads |
| `published/` | Immutable, versioned, release-approved public-safe carriers | RAW, WORK, QUARANTINE, exact restricted geometry |

### 11.4 Logical home versus physical bytes

`DIR-STORAGE-001` â€” The directory names above define logical authority even when bytes live in PostgreSQL/PostGIS, object storage, a package registry, an external archive, or another governed service.

For non-Git payloads, the logical home contains or resolves through a versioned manifest or registry record with:

- stable object ID and version;
- storage class and locator appropriate to access policy;
- digest, media type, size, and creation time;
- source, rights, sensitivity, retention, and legal-hold posture;
- producer receipt and schema/policy versions;
- public exposure and release references;
- correction, withdrawal, and rollback target.

`DIR-STORAGE-002` â€” A locator is not authority. Consumers resolve it through the owning registry, policy, and release state.

`DIR-STORAGE-003` â€” Restricted bytes must not be committed merely because their logical home is under `data/`. Encryption, access control, audit, and retention are separate mandatory controls.

### 11.5 Release decision plane

~~~text
release/
â”œâ”€â”€ candidates/             # candidate dossiers; no release authority
â”œâ”€â”€ manifests/              # immutable ReleaseManifest collections
â”œâ”€â”€ promotion_decisions/    # allow, deny, hold or abstain decisions
â”œâ”€â”€ correction_notices/     # correction lineage
â”œâ”€â”€ withdrawal_notices/     # withdrawal lineage
â”œâ”€â”€ rollback_cards/         # rollback decisions and targets
â”œâ”€â”€ signatures/             # signatures and attestations
â””â”€â”€ changelog/              # release-level history
~~~

`DIR-RELEASE-001` â€” Object-family first, domain second: `release/manifests/<domain>/`, not `release/<domain>/`.

`DIR-RELEASE-002` â€” `release/manifests/` is the proposed canonical collection spelling. A singular `release/manifest/` is compatibility-only after an inventoried migration.

`DIR-RELEASE-003` â€” `RollbackCard` lives only under `release/rollback_cards/`. Executed rollback and cache-invalidation process records live under `data/receipts/rollback/`.

`DIR-RELEASE-004` â€” Generic `data/rollback/` is deprecated as an ambiguous authority lane. Its existing objects must be classified before migration; no bulk move by filename.

`DIR-RELEASE-005` â€” Policy source under `release/` is denied. Release policy belongs under `policy/release/`; release decisions reference the policy version and outcome.

`DIR-RELEASE-006` â€” `data/published/` owns released payloads. `release/` owns the decisions that authorize and correct them. Proofs support the decision but do not replace it.

---

## 12. Domain, source, geography, and cross-domain scope

### 12.1 Scope follows responsibility

Scope segments are added only after the owning root and family are known.

`DIR-SCOPELANE-001` â€” Domains never become repository roots.

`DIR-SCOPELANE-002` â€” A new domain is registered before new lanes are created. The register supplies canonical `domain_id`, path slug, code aliases, owner, sensitivity baseline, status, dependencies, and supersession data.

`DIR-SCOPELANE-003` â€” Create only lanes with an owned artifact, consumer, validation need, or boundary contract. Empty symmetry scaffolding is prohibited.

`DIR-SCOPELANE-004` â€” Shared object families are defined once. Domain contracts and schemas extend or reference shared definitions rather than copy them.

### 12.2 Domain-lane pattern

Illustrative homes for domain `hydrology`:

~~~text
docs/domains/hydrology/
contracts/domains/hydrology/
schemas/contracts/v1/domains/hydrology/
policy/domains/hydrology/
tests/domains/hydrology/
fixtures/domains/hydrology/
packages/domains/hydrology/
pipelines/<stage>/hydrology/
pipeline_specs/hydrology/
data/<lane>/hydrology/
release/<object_family>/hydrology/
~~~

The pattern is sparse and evidence-driven. It does not authorize every lane merely because the domain exists.

### 12.3 Source identity

`DIR-SOURCE-001` â€” Source capture identity is source-first. One capture may support several domains without duplicated RAW bytes.

`DIR-SOURCE-002` â€” A canonical `source_id` is registered once. Connector implementation uses that ID or a declared provider grouping; domain assignments live in descriptors and downstream projections.

`DIR-SOURCE-003` â€” Machine source identities and descriptors live under `data/registry/sources/`. Human source guidance lives under `docs/sources/`. Connector code lives under `connectors/`.

`DIR-SOURCE-004` â€” `data/registry/<domain>/sources/` may be a generated view but not an independent writer when `data/registry/sources/<source_id>/` is canonical.

Subtype-first registry placement is canonical:

~~~text
data/registry/
â”œâ”€â”€ sources/
â”œâ”€â”€ datasets/
â”œâ”€â”€ layers/
â”œâ”€â”€ domains/
â”œâ”€â”€ rights/
â”œâ”€â”€ sensitivity/
â””â”€â”€ crosswalks/
~~~

Catalog projections also use subtype-first placement:

~~~text
data/catalog/
â”œâ”€â”€ stac/
â”œâ”€â”€ dcat/
â”œâ”€â”€ prov/
â”œâ”€â”€ domains/
â””â”€â”€ matrix/
~~~

Direct siblings such as `data/prov/`, `data/catalog/domain/`, or `data/catalog/<domain>/` are migration candidates unless an accepted standard profile gives them distinct authority.

### 12.4 Geography and Focus Mode

A county, corridor, watershed, region, or Focus Mode is a composition scope, not a domain and not a root.

- register a stable `scope_id`;
- compose released or candidate domain lanes through references;
- keep scope-specific UI under the owning app;
- keep scope-specific fixtures under the owning fixture lane;
- do not copy canonical domain records merely to populate a scope directory.

### 12.5 Cross-domain seams

Cross-domain artifacts live under the root that owns their primary authority and use a registered seam ID:

- cross-domain semantic contract -> `contracts/cross_domain/<seam_id>/`;
- cross-domain test -> `tests/cross_domain/<seam_id>/`;
- shared validator -> `tools/validators/cross_domain/<seam_id>/`;
- shared architecture explanation -> `docs/architecture/cross-domain/<seam_id>.md`.

Never select an arbitrary â€œleadâ€ domain merely to obtain a path.

---

## 13. Names, identity, and collection grammar

### 13.1 Registered names

`DIR-NAME-001` â€” Canonical root names are fixed by the root registry.

`DIR-NAME-002` â€” Domain, source, geography, seam, and object-family path slugs are registered once. Aliases are explicit and time-bounded.

`DIR-NAME-003` â€” Language-native identifiers may differ from path slugs:

| Identity | Example |
|---|---|
| Canonical domain ID | `people-dna-land` |
| Python or TypeScript module alias | `people_dna_land` |
| Display label | `People, DNA & Land` |

The mapping belongs in the applicable register; code aliases do not create filesystem authority.

### 13.2 Safe path grammar

New governed path segments must:

- use ASCII letters, digits, hyphen, or underscore only;
- be lowercase except externally fixed standards or repository entrypoint filenames;
- avoid spaces, parentheses, ambiguous Unicode, trailing dots/spaces, and case-only variants;
- avoid Windows reserved device names;
- remain stable after publication; identity-changing renames require migration.

Root-defined conventions choose hyphen or underscore for a segment class:

- domain, source, geography, and seam slugs default to kebab-case;
- language module directories follow the language convention inside code roots;
- governed machine collection lanes may use established snake_case names such as `promotion_decisions`;
- existing canonical root `pipeline_specs/` is a registered exception.

### 13.3 Singular and plural

`DIR-NAME-004` â€” Collection directories are plural; record types and individual filenames are singular unless an external standard fixes the name.

Proposed resolutions:

| Conflict | Canonical | Compatibility or migration source |
|---|---|---|
| `triplet/`, `triplet(s)/`, `triplets/` | `triplets/` | singular and parenthesized forms |
| `manifest/`, `manifests/` | `manifests/` | singular form |
| `atlas/`, `atlases/` | `atlases/` | singular form |
| `correction/`, `corrections/`, `correction_notices/` | `correction_notices/` for public correction objects | other forms require object classification |
| `rollback/`, `rollback_cards/` | `rollback_cards/` for decisions; `data/receipts/rollback/` for execution | generic rollback lanes |

`DIR-NAME-005` â€” A path containing placeholder punctuation such as `triplet(s)` is denied for canonical use.

### 13.4 Stable object identity

Path, object ID, display name, and storage locator are distinct. Moving a file must not silently change object identity. When path is part of an external identifier or schema `$id`, migration must preserve an alias or issue a versioned identity change.

---

## 14. Dependency direction

Path conformance includes dependency conformance.

### 14.1 Core dependency rules

| Consumer | May depend on | Must not depend on |
|---|---|---|
| `apps/` | `packages/`, governed contracts/schemas/policy clients, bounded runtime adapters | Other apps' internals, tests, fixtures as production data, raw stores |
| `packages/` | Other lower-level packages and generated schema bindings | `apps/`, `tools/`, `scripts/`, deployment-specific infra |
| `connectors/` | Shared packages, source contracts, schemas, admission policy | `data/processed/`, catalog writers, publishers, UI |
| `pipelines/` | Packages, contracts, schemas, policy, declared connector outputs | Apps, direct public surfaces, release approval |
| `pipeline_specs/` | Registered identifiers and schemas | Executable business logic |
| `runtime/` | Packages, configs, deterministic adapters | Canonical data authority, public clients, domain implementation |
| `tools/` | Packages and explicit operator interfaces | Becoming a runtime dependency of production apps |
| `scripts/` | Tools and supported CLIs | Being imported by production code |
| `tests/` | Any declared test target and public-safe fixtures | Production code depending back on tests |
| `docs/` | References to every root | Executable authority merely through prose |

`DIR-DEP-001` â€” Normative roots (`contracts/`, `schemas/`, `policy/`) do not depend on application implementation. Generated projections may be built from them.

`DIR-DEP-002` â€” Public clients consume governed APIs or release-approved carriers. Direct filesystem, database, object-store, model-adapter, or internal-registry access is denied.

`DIR-DEP-003` â€” Renderer and AI provider technologies are implementation details behind governed adapters. Technology selection belongs to accepted architecture decisions, not root naming.

### 14.2 Write-capability matrix

| Actor | Permitted durable writes |
|---|---|
| Connector | RAW or QUARANTINE candidate plus ingest receipts |
| Watcher | Pre-RAW event/candidate plus watcher receipt |
| Pipeline stage | Its declared output lane plus run/validation receipts |
| Catalog builder | Catalog projections from validated inputs and proof references |
| Proof builder | Proof objects from resolvable evidence and receipts |
| Release authority | Release decision objects after required review |
| Publisher | Versioned PUBLISHED carriers only after an accepted release decision |
| Public UI/client | No canonical writes; correction requests use governed interfaces |

Capabilities are granted by authenticated runtime policy, not merely by directory convention.

---

## 15. Generated output, external storage, and caches

### 15.1 Generated output classes

| Class | Home | Rule |
|---|---|---|
| Generated source required to build | Colocated with owner or a declared generated subtree | Source pointer and regeneration command required |
| Generated docs preview | `artifacts/docs/` or external CI artifact | Never the documentation source |
| QA, lint, coverage, render output | `artifacts/qa/` or external CI artifact | Not proof of release |
| Compiled/package output | `artifacts/build/` or external package registry | Rebuildable; no canonical data authority |
| Cache, virtual environment, dependency install | Ignored local/tool cache | Never tracked |
| Durable receipt/proof/catalog/release/published object | Its canonical family | Never left in `artifacts/` |

`DIR-GEN-001` â€” Generated content must declare `generated_from`, generator identity/version, content digest, and edit policy.

`DIR-GEN-002` â€” Mirrors are one-way and reproducible. Manual edits to a mirror are denied.

`DIR-GEN-003` â€” Symlinks, submodules, or remote references may not hide a second writable authority. Their source, pin, license, update policy, and failure behavior must be explicit.

### 15.2 `artifacts/` transition

The only permitted direct children are:

~~~text
artifacts/
â”œâ”€â”€ build/
â”œâ”€â”€ docs/
â”œâ”€â”€ qa/
â””â”€â”€ temporary/
~~~

`artifacts/release/`, `artifacts/proofs/`, and trust-shaped equivalents are nonconforming even when they contain placeholders. The long-term target is no tracked generated payload except the boundary README, ignore rules, and intentionally retained small QA fixtures.

---

## 16. README contracts and documentation inheritance

### 16.1 README profiles

The v1 requirement is replaced with risk-based profiles.

| Profile | Applies to | Required depth |
|---|---|---|
| `ROOT_FULL` | Every canonical, platform, conditional, compatibility, and deprecated root | Full authority contract |
| `BOUNDARY_COMPACT` | Domain lane, object-family lane, lifecycle lane, deployable, package, connector, pipeline stage, sensitive boundary | Compact local contract |
| `LEAF_INHERITED` | Ordinary implementation or data leaf with no independent boundary | Inherit parent; README optional |

`DIR-README-001` â€” A README is required where ownership, authority, exposure, mutation, generation, or lifecycle behavior changes. It is not required merely because a directory exists.

`DIR-README-002` â€” A README does not upgrade an empty or placeholder lane to implemented status.

### 16.2 `ROOT_FULL` fields

1. Purpose.
2. Root class and authority owner.
3. Adoption and conformance status.
4. What belongs and what is prohibited.
5. Inputs, outputs, and permitted writers.
6. Public exposure and sensitivity posture.
7. Mutability, retention, generation, and physical storage.
8. Validation and negative checks.
9. Owner, reviewers, and escalation path.
10. Governing ADRs, migrations, aliases, and canonical target if noncanonical.
11. Direct-child directory map.
12. Last evidence review and review trigger.

### 16.3 `BOUNDARY_COMPACT` fields

- purpose and inherited parent;
- local owner and scope ID;
- belongs / prohibited;
- inputs / outputs;
- exposure, mutation, and retention;
- validation;
- related contract, schema, policy, fixtures, tests, and release family;
- status and open verification items.

### 16.4 Directory-map law

`DIR-README-003` â€” A directory README shows the directory it governs and direct children only. A child README owns deeper detail.

`DIR-README-004` â€” Directory maps use lined trees with `â”‚`, `â”œâ”€â”€`, and `â””â”€â”€` in a `text` fence. Comments align and describe authority, not aspiration.

`DIR-README-005` â€” An illustrative future tree must be labeled `PROPOSED`; a current tree must be generated or verified from repository evidence.

### 16.5 Review triggers

Review is event- and risk-based, not a blanket six-month timer. Re-review when:

- authority, root class, writer, consumer, exposure, sensitivity, or storage changes;
- an ADR is accepted or superseded;
- validation or CODEOWNERS coverage changes;
- a compatibility deadline arrives;
- drift, security, correction, withdrawal, or rollback occurs;
- a risk-based maximum interval set by the root profile expires.

---

## 17. Compatibility, aliases, and deprecation

### 17.1 Compatibility classes

| Class | Meaning |
|---|---|
| `legacy` | Former canonical home, frozen to new authority |
| `mirror` | Generated one-way projection of canonical content |
| `external_export` | Shape/path required by a verified downstream consumer |
| `transitional` | Temporary migration path with active cutover |
| `deprecated` | Read-only, scheduled for retirement |

Every compatibility entry must record:

- old path and canonical target;
- object family and identity mapping;
- reason and accepted ADR;
- verified writers and consumers;
- read/write rule;
- generation or synchronization method;
- owner, start date, expiry, and exit criteria;
- parity validation and rollback behavior.

`DIR-COMPAT-001` â€” Compatibility uses dual-read/single-write when necessary: consumers may temporarily read old and new; all new writes go only to canonical.

`DIR-COMPAT-002` â€” An alias cannot be more permissive, public, mutable, or authoritative than its target.

`DIR-COMPAT-003` â€” A tombstone README may preserve navigation and migration facts but may not contain a live copy of the authority object.

### 17.2 Bounded exceptions

A time-limited exception may defer migration but cannot amend authority. It requires:

- exact paths and rule IDs;
- reason and risk;
- owner and approving reviewers;
- compensating controls;
- issue/ADR/migration reference;
- expiry and automatic failure after expiry;
- no public-boundary, sensitivity, or parallel-writer weakening.

---

## 18. Migration, correction, and rollback

### 18.1 Migration phases

1. Freeze governing inputs, tree, producers, consumers, identities, and digests.
2. Classify every object; do not route by filename alone.
3. Accept the authority decision before dependent structural implementation.
4. Add canonical target and negative write guard.
5. Record old-to-new mappings in a schema-backed migration manifest.
6. Cut producers to canonical single-write.
7. Support bounded dual-read if verified consumers require it.
8. Validate content, identity, rights, sensitivity, links, imports, schemas, policy, tests, workflows, release, correction, and rollback.
9. Prove zero writers and zero consumers at the old path.
10. Retire the alias and preserve decision history.

### 18.2 Migration manifest minimum

~~~yaml
migration:
  migration_id: "<stable id>"
  decision_ref: "<accepted ADR>"
  object_family: "<family>"
  old_path: "<old>"
  new_path: "<new>"
  object_id_rule: "<preserved or versioned change>"
  content_digest_before: "<digest>"
  content_digest_after: "<digest>"
  producers: []
  consumers: []
  compatibility_mode: "<none|dual_read_single_write|generated_mirror>"
  effective_at: "<ISO-8601>"
  sunset_at: "<ISO-8601 or explicit condition>"
  validation_refs: []
  rollback_or_forward_fix: "<plan>"
  result: "<PLANNED|ACTIVE|VERIFIED|ROLLED_BACK|SUPERSEDED>"
~~~

`DIR-MIGRATE-001` â€” `git mv` expresses staging intent; history preservation must be verified through content continuity, rename detection, references, and object identity.

`DIR-MIGRATE-002` â€” A move that changes semantic identity requires contract/schema versioning, fixture parity, consumer migration, and correction of released references.

`DIR-MIGRATE-003` â€” Unknown, restricted, or trust-bearing payloads are inventoried before movement. Destructive cleanup is the last step.

`DIR-MIGRATE-004` â€” Rollback must not recreate two writable authorities. When rollback is unsafe, record a forward-fix plan and the reason.

---

## 19. Machine enforcement

### 19.1 Normative source and machine projection

The adopted human rules remain the normative placement law. Machine files project that law:

~~~text
control_plane/
â”œâ”€â”€ root_registry.yaml
â”œâ”€â”€ path_alias_register.yaml
â”œâ”€â”€ domain_lane_register.yaml
â”œâ”€â”€ object_family_register.yaml
â”œâ”€â”€ deprecation_register.yaml
â””â”€â”€ verification_backlog.yaml
~~~

The first two files are proposed additions. Existing registers remain in place.

`DIR-ENFORCE-001` â€” Every machine entry cites an adopted rule or accepted ADR and carries its source digest. A register cannot amend the doctrine it projects.

`DIR-ENFORCE-002` â€” A rules change and its machine projection must pass parity validation before adoption.

### 19.2 Root-registry entry

~~~yaml
root:
  root_id: "<stable id>"
  path: "<root/>"
  class: "<canonical|platform|conditional|compatibility|deprecated|retired>"
  responsibility: "<one primary responsibility>"
  allowed_artifact_kinds: []
  prohibited_artifact_kinds: []
  permitted_writers: []
  dependency_rules: []
  exposure: "<public|semi_public|internal|restricted|mixed>"
  mutation: "<immutable|append_only|versioned|generated|mixed>"
  retention: "<policy ref>"
  owner: "<verified owner>"
  reviewers: []
  governing_decisions: []
  canonical_target: null
  activation_conditions: []
  exit_conditions: []
  validation_profiles: []
  status: "<PROPOSED|ACCEPTED|ACTIVE|DEPRECATED|RETIRED>"
~~~

### 19.3 Validator profile

The proposed validator family `tools/validators/directory_governance/` should check:

- unknown tracked roots and disallowed root files;
- root registry/document parity;
- proposed or expired roots becoming writable;
- canonical/compatibility duplicate writers;
- domain, source, scope, and object-family slug registration;
- path grammar, case collisions, singular/plural conflicts, and parenthesized placeholders;
- data lifecycle and release-family placement;
- policy code outside `policy/`;
- trust objects under `artifacts/`;
- direct public imports or routes to internal data stores;
- duplicate schema `$id`, contract authority, policy ID, source ID, or release identity;
- generated mirrors without sources/digests;
- authority-bearing boundaries missing the correct README profile;
- structural changes lacking accepted ADR and migration manifest;
- expired exceptions and unclosed aliases.

### 19.4 Ratcheted conformance

Brownfield adoption should baseline verified existing drift:

- existing, owned drift may begin as a warning with a closure issue and deadline;
- any newly introduced instance of a baselined violation fails;
- safety, sensitivity, direct-public-path, secret, parallel-writer, and publication-bypass violations fail immediately;
- warnings cannot be used to create new authority;
- the baseline shrinks monotonically.

Finite validator outcomes:

| Outcome | Meaning |
|---|---|
| `PASS` | No applicable violation |
| `FAIL_NEW_DRIFT` | Change introduces or expands drift |
| `FAIL_INVARIANT` | Trust, lifecycle, sensitivity, authority, or public-boundary violation |
| `HOLD_UNRESOLVED` | Evidence or decision missing |
| `ERROR_VALIDATOR` | Validator could not evaluate safely |

### 19.5 Required proof suite

At minimum:

- root and root-file positive/negative fixtures;
- one example for every root class;
- domain/source alias collision cases;
- lifecycle legal and illegal transitions;
- policy/release/proof/receipt separation cases;
- compatibility single-write and expired-alias cases;
- direct-public-store denial tests;
- platform-root non-authority tests;
- migration manifest validation;
- deterministic, no-network execution.

---

## 20. Current repository convergence map

This section is **informative implementation evidence**, not timeless doctrine.

### 20.1 Evidence snapshot

The inspected repository was:

| Field | Verified value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Commit | `00d33c0e3a2b970bfde8a88e36b76cd834319d75` |
| Branch | `agent/harden-fauna-fixture-safety-20260725` |
| Commit time | 2026-07-25T11:17:10-07:00 |
| Worktree | Clean |
| Relationship to local `origin/main` | 20 commits behind and 2 ahead |
| Scope limit | Shallow feature-branch snapshot; selected topology files matched the local `origin/main`, but this is not proof of current remote main |

### 20.2 Confirmed structural facts

| Observation | Current evidence | v2 result |
|---|---|---|
| Two divergent Directory Rules files | `docs/doctrine/directory-rules.md` blob `2affb080â€¦`, v1.4 draft; `docs/architecture/directory-rules.md` blob `18653c00â€¦`, v1.3.1 review | `CONFLICTED`; doctrine path should become canonical on adoption |
| Reference weight favors doctrine path | 2,903 exact references to doctrine path versus 234 to architecture path | Supports doctrine-path migration, not proof of adoption |
| Two divergent skeleton maps | Root `SKELETON_MAP.md` and `docs/architecture/SKELETON_MAP.md` have different blobs and content | Keep one orientation map; archive or redirect the duplicate |
| Root README identity is wrong | Root `README.md` is a 2,598-line Markdown-agent prompt and is used by `pyproject.toml` as package metadata | High-priority correction; prompts belong under `docs/prompts/` |
| Tracked top-level directories | 25, including `artifacts/`, `catalog/`, and `src/` | 22 normalized canonical/platform roots plus three noncanonical/conditional roots |
| Repository scale | 7,329 tracked files; 2,258 READMEs; 1,217 `.gitkeep` files | Requires inheritance and a materialization gate |
| Speculative leaf scaffolding | 1,317 of 1,885 leaf directories contain only README and/or `.gitkeep` | Baseline and retire; prohibit new empty scaffolding |
| ADR status | All 28 numbered ADRs resolve to `proposed`; index coherence passes but acceptance is absent | No structural ADR can presently be treated as accepted authority |
| Machine registers | Domain, source, object-family, and deprecation registers have empty `entries` | Machine governance is scaffolded, not operational |
| Topology validation | No root/path topology validator or CI workflow found; `tools/validate_all.py` is a placeholder | Build the ratchet before broad migration |

### 20.3 Root convergence

1. **`catalog/`** â€” contains 27 READMEs and 16 `.gitkeep` files and no other tracked payloads. It is documented as severe parallel-authority drift. This is the safest first root retirement after reference validation.
2. **`src/`** â€” contains only `README.md`, `src/kfm/README.md`, and a minimal `src/kfm/__init__.py`, but root `pyproject.toml` packages it. Return `HOLD` until an umbrella-facade decision verifies consumers and API intent.
3. **`artifacts/`** â€” has 44 tracked files and a nonconforming `artifacts/release/` lane. Keep only the four generated-output lanes, remove trust-state contamination through reviewed migration, and move toward ignored or external CI output.

### 20.4 Naming and lane convergence

Confirmed collisions include:

- `data/triplet/`, `data/triplet(s)/`, and `data/triplets/`;
- `docs/atlas/` and `docs/atlases/`;
- `release/manifest/` and `release/manifests/`;
- `release/correction/`, `release/corrections/`, and `release/correction_notices/`;
- `release/rollback/` and `release/rollback_cards/`;
- `data/registry/<domain>/sources/` and `data/registry/sources/<domain>/`;
- domain aliases such as `air` / `atmosphere`, `people` / `people-dna-land`, `settlement` / `settlements-infrastructure`, and `transport` / `roads-rail-trade`;
- source connector aliases and hyphen/underscore pairs;
- flat domain contracts and `contracts/domains/<domain>/`;
- `pipelines/specs/` beside root `pipeline_specs/`.

Apply registered IDs, one writer, plural collection rules, subtype-first registries, and bounded aliases. Do not mass-rename before consumer and identity mapping.

### 20.5 Trust-family convergence

Confirmed current issues:

- three `.rego` policy files live directly under `release/`;
- `data/rollback/` overlaps `release/rollback_cards/`;
- proposed or placeholder objects exist under trust-shaped catalog, proof, published, release, and artifacts lanes;
- 468 schema JSON files include 467 proposed or placeholder signals, 223 empty-object schemas, and 47 normalized-basename collision groups covering 309 files;
- five SourceDescriptor schema path variants coexist;
- all 312 non-README semantic contract Markdown files contain proposed, placeholder, or scaffold signals.

The first bounded object-family migration should be `SourceDescriptor` because it exercises semantic meaning, one schema `$id`, registry identity, source connector references, valid and invalid fixtures, tests, alias migration, and rollback without publishing source payloads.

### 20.6 Convergence priority

| Priority | Change | Why first |
|---:|---|---|
| 1 | Bootstrap adoption authority and select one Directory Rules identity | Every later path decision depends on it |
| 2 | Restore a real project root README and one skeleton map | Root identity and package metadata are currently misleading |
| 3 | Populate root/domain/object/source/alias registers and add topology ratchet | Stops new drift before migration |
| 4 | Retire empty `catalog/`, extra triplet spellings, `pipelines/specs/`, and empty alias scaffolds | Low payload risk, high ambiguity reduction |
| 5 | Remove policy and trust objects from wrong roots | Restores authority boundaries |
| 6 | Converge SourceDescriptor and domain/source registries | Establishes a reusable migration pattern |
| 7 | Normalize release object families and `data/rollback/` | Requires stronger decision and rollback review |
| 8 | Decide root `src/` facade and active package/UI aliases | Active consumer risk must be proven |

---

## 21. Adoption and implementation sequence

Because the repository currently has no accepted structural ADR, v2 needs an explicit bootstrap decision rather than pretending a proposed ADR is effective.

### Phase 0 â€” Ratification packet

1. Review this draft against core KFM invariants and current repository evidence.
2. Record the adopting decision, approvers, effective date, content digest, and exact supersession targets.
3. Resolve the compatibility-root ADR contradiction and the Directory Rules canonical home.
4. Assign verified owners; CODEOWNERS routing alone does not prove stewardship or independent review.

### Phase 1 â€” Single authority surface

1. Install the adopted bytes at `docs/doctrine/directory-rules.md`.
2. Replace `docs/architecture/directory-rules.md` with a short read-only redirect carrying its prior blob and supersession link.
3. Update references without changing unrelated doctrine.
4. Retain prior editions in Git history or an explicit doctrine lineage archive.

### Phase 2 â€” Executable projection

1. Add root and alias registers.
2. Populate domain, object-family, source, and deprecation registers with verified entries.
3. Add schemas, positive and negative fixtures, validator, tests, Make target, and CI.
4. Baseline inherited drift with stable IDs, owners, and exit criteria.
5. Fail all new invariant and drift violations.

### Phase 3 â€” Low-risk convergence

Retire empty compatibility scaffolds and duplicate spellings after reference closure. Do not mix this phase with trust-object migration.

### Phase 4 â€” Authority-family convergence

Migrate one bounded object family at a time. Use `SourceDescriptor` first, then release decision families. Preserve stable IDs, digests, producer and consumer mapping, and rollback.

### Phase 5 â€” Enforcement graduation

Move baselined warnings to failures as each drift class reaches zero. No phase claims completion without the declared proof suite.

---

## 22. Reviewer checklist

### Authority and identity

- [ ] The governing rules edition and accepted ADR baseline were frozen before editing.
- [ ] The artifact has one authority owner and a complete responsibility signature.
- [ ] The selected path produces one finite outcome.
- [ ] No proposed ADR or same-change doctrine edit is being used as authority.

### Root and scope

- [ ] The root is registered and active for this artifact kind.
- [ ] A domain, source, geography, technology, or format is a segment, not a root.
- [ ] The domain/source/scope ID and aliases are registered.
- [ ] No speculative empty lane is being created.

### Lifecycle and trust

- [ ] Data state, receipt, proof, catalog, release decision, and published carrier are not collapsed.
- [ ] Public clients use governed APIs or released carriers.
- [ ] Rights, sensitivity, retention, and physical storage are independently controlled.
- [ ] No placeholder or proposed instance enters a canonical trust lane.

### Implementation

- [ ] Executable role and dependency direction are correct.
- [ ] Connector, watcher, pipeline, catalog builder, publisher, and release capabilities are not conflated.
- [ ] Tests and fixtures do not become production dependencies.

### Migration and documentation

- [ ] Existing writers, consumers, links, identities, and digests were inventoried.
- [ ] Compatibility is single-write, time-bounded, and validated.
- [ ] Migration, correction, and rollback records are complete.
- [ ] The applicable README profile is accurate and its tree shows direct children only.
- [ ] Rule IDs, evidence, and validation results appear in the PR.

---

## 23. Glossary

| Term | Meaning |
|---|---|
| Authority owner | The one responsibility allowed to define or mutate an artifact's canonical meaning or state |
| Responsibility root | A top-level directory representing a repo-wide authority or execution boundary |
| Lane | A registered family, lifecycle, domain, source, or scope segment inside a root |
| Platform root | A host or tool integration directory with no independent KFM truth authority |
| Conditional root | A root valid only while an accepted activation profile is satisfied |
| Compatibility root | A noncanonical, non-independent path retained for legacy, mirror, export, or migration |
| Parallel authority | Two writable homes claiming the same object family or decision power |
| Responsibility signature | The multi-axis classification used to select a path |
| Logical home | The KFM authority path for an object regardless of physical byte storage |
| Lifecycle state | PRE_RAW, RAW, WORK, QUARANTINE, or PROCESSED state of admitted data |
| Projection | CATALOG or TRIPLETS output derived from canonical records |
| Accountability store | RECEIPTS, PROOFS, or REGISTRY instances supporting traceability and governance |
| Promotion | Governed state transition supported by validation, policy, evidence, review, release, correction, and rollback |
| Published carrier | Immutable release-approved public-safe payload consumed downstream |
| Tombstone | Read-only migration notice at an old path; not a live copy |
| Ratchet | Enforcement that baselines owned legacy drift but rejects any new or expanded violation |

---

## Appendix A: placement examples

### A.1 Source-specific fetcher

| Signature axis | Value |
|---|---|
| Artifact kind | Executable code |
| Authority owner | Source acquisition |
| Execution role | Connector |
| Scope | Registered source ID |
| Output capability | RAW or QUARANTINE plus ingest receipt |
| Outcome | `PLACE` under `connectors/<source_id>/` |

If the same provider appears under a domain alias, return `MIGRATE` or `MIRROR`, not a second implementation.

### A.2 Domain schema

| Signature axis | Value |
|---|---|
| Artifact kind | Machine schema |
| Authority owner | Machine shape |
| Scope | Domain |
| Outcome | `PLACE` under `schemas/contracts/v1/domains/<domain>/` |

A prose explanation belongs in the semantic contract or domain docs and references the schema. Duplicated schema JSON under `contracts/` returns `DENY`.

### A.3 Release manifest

| Signature axis | Value |
|---|---|
| Artifact kind | Release decision record |
| Authority owner | Release governance |
| Scope | Object family then domain |
| Mutability | Immutable |
| Outcome | `PLACE` under `release/manifests/<domain>/` |

The released PMTiles or GeoParquet carrier belongs under `data/published/`; proof support belongs under `data/proofs/`.

### A.4 Generated QA report

| Signature axis | Value |
|---|---|
| Artifact kind | Generated output |
| Authority owner | None beyond its producing run |
| Retention | Disposable or CI-bound |
| Outcome | `PLACE` under `artifacts/qa/` or an external CI artifact store |

It does not become a KFM proof unless a governed proof builder emits a canonical proof object.

### A.5 Cross-domain validator

| Signature axis | Value |
|---|---|
| Artifact kind | Repository validator |
| Authority owner | Validation tooling |
| Scope | Registered cross-domain seam |
| Outcome | `PLACE` under `tools/validators/cross_domain/<seam_id>/` |

Tests belong under the corresponding `tests/` lane; reusable fixtures under `fixtures/`.

### A.6 Root Python facade

| Signature axis | Value |
|---|---|
| Artifact kind | Aggregate package facade |
| Authority owner | Root distribution API |
| Root class | Conditional |
| Required evidence | Accepted facade ADR, verified consumers, package/API tests, dependency direction |
| Outcome without evidence | `HOLD` |

---

## Appendix B: evidence ledger

### B.1 Supplied sources

| ID | Source | Use in this draft |
|---|---|---|
| S1 | `Directory Rules.pdf`, 22 pages, SHA-256 `759de4fcb51cf0f55896089e397d9c47481d60d9fb80ac9a44d47b2f60a0a335` | Baseline placement doctrine, canonical/compatibility roots, lifecycle, migration, README, and contradiction analysis |
| S2 | `Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf` | Pre-RAW events, source admission, immutable releases, receipts, proof, catalog, and rollback implications |
| S3 | `Kansas_Frontier_Matrix_Pipeline_Living_Implementation_Manual_v0.3.pdf` | Pipeline lifecycle, source acquisition, schema and fixture placement implications |
| S4 | `KFM_MapLibre_Operating_Architecture_Governed_UI_AI_Interaction_Manual_REVISED.pdf` | Public trust membrane, UI, renderer, and AI downstream boundary |
| S5 | `# Kansas Frontier Matrix Implementation Reference.pdf` | Historical root conflicts and compatibility evidence |
| S6 | `Unified Implementation Architecture Build Manual.md` | Responsibility roots, inspectable claims, lifecycle, trust planes, data/release/object-family separation |
| S7 | `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | Existence-versus-authority distinction, migration/versioning, open directory questions |
| S8 | `maplibre3d.md` | Adapter-boundary implications; technology decision remains ADR-scoped |
| S9 | Repository snapshot at commit `00d33c0eâ€¦` | Current implementation facts and drift inventory |

### B.2 Page-grounded findings from the supplied Directory Rules PDF

| Finding | Pages |
|---|---:|
| Self-declared canonical doctrine but no explicit version, issue date, effective date, or ratification record | 1, 20â€“21 |
| Authority order, accepted-ADR rule, and drift procedure | 1â€“3 |
| Responsibility-root and domain-as-lane foundation | 3â€“5, 16 |
| Canonical/compatibility root model | 5â€“6, 11â€“12, 22 |
| Contracts/schema/policy/test separation | 6â€“9 |
| Data and release separation | 12â€“14 |
| Migration discipline and README contract | 18â€“20 |
| Open triplet, rollback, manifest, schema, policy, and API questions | 21 |
| Direct contradiction over whether a new compatibility root requires an ADR | 4 and 20 |
| RollbackCard placed in both data rollback and release rollback-card homes | 13â€“14 and 21 |
| Lifecycle phases conflated with receipts, proofs, registry, and rollback stores | 4 and 13 |

### B.3 Preserved strengths

This successor deliberately preserves:

- responsibility over topic;
- domain as lane, never root;
- contract, schema, policy, test, receipt, proof, catalog, release, and published-carrier separation;
- connectors and watchers as non-publishers;
- governed public interfaces;
- explicit drift rather than convention-as-canon;
- reversible, evidence-backed migration;
- rule citation in path-bearing changes.

---

## Closing law

> **One canonical writer. One registered identity. One explicit lifecycle and exposure posture. Many references are allowed; parallel authority is not. A path helps route trust, but only evidence, policy, review, release, correction, and rollback can earn trust.**

[Back to top](#top)
