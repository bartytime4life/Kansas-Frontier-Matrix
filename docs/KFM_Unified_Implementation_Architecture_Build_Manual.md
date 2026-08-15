<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/whole-system-reference
title: Kansas Frontier Matrix — Whole-System Reference
type: whole-system-reference
version: 2026-08-15-convergence-draft
status: PROPOSED_FOR_ADOPTION
authority_class: proposed_human_readable_synthesis
current_path: docs/KFM_Unified_Implementation_Architecture_Build_Manual.md
owning_root: docs/
base_repository: bartytime4life/Kansas-Frontier-Matrix
base_commit: a768ed812df41e3466758b60af087129997fb337
source_corpus_snapshot_date: 2026-08-15
last_verified: 2026-08-15
owner_review_route: "@bartytime4life"
required_independent_review: NEEDS_VERIFICATION
truth_posture: cite-or-abstain
implementation_maturity_posture: evidence-separated-from-doctrine
non_effects:
  - does_not_activate_sources
  - does_not_approve_policy
  - does_not_release_or_publish
  - does_not_deploy
  - does_not_change_repository_settings
  - does_not_supersede_accepted_adrs_contracts_schemas_policy_or_current_code
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas Frontier Matrix — Whole-System Reference

> **PROPOSED FOR ADOPTION — WHOLE-SYSTEM REFERENCE**
>
> This is KFM's proposed canonical **human-readable synthesis**. It does not outrank accepted ADRs, semantic contracts, machine schemas, policy, current code/configuration, tests/workflows, generated receipts/proofs/manifests, or runtime evidence. It becomes authoritative only through a separate accepted adoption decision.

## 0. Document Control and Authority

| Field | Current value | Evidence / boundary |
|---|---|---|
| Document ID | `kfm://doc/whole-system-reference` | Stable identifier introduced for this same-path convergence; adoption remains **PROPOSED**. |
| Source path | `docs/KFM_Unified_Implementation_Architecture_Build_Manual.md` | Existing whole-system document updated **in place**; no sibling master document created. |
| Status | **PROPOSED FOR ADOPTION — WHOLE-SYSTEM REFERENCE** | No accepted ADR currently designates this file as whole-system authority. |
| Authority class | Proposed human-readable synthesis | Subordinate to accepted ADRs, contracts, schemas, policy, repository evidence, tests, workflows, and release records. |
| Repository base | `bartytime4life/Kansas-Frontier-Matrix@a768ed812df41e3466758b60af087129997fb337` | Immutable current-main snapshot used for this convergence. |
| Default branch | `main` | Repository metadata at the snapshot. |
| Directory authority | Directory Rules v2 exact bytes at `docs/doctrine/directory-rules.md`, adopted by ADR-0029 | The rules file retains a historical `PROPOSED_FOR_ADOPTION` header; the accepted ADR establishes actual adoption state. [R-DIR] [R-ADR29] |
| Owners / review route | `@bartytime4life` | Current CODEOWNERS review routing; independent domain/security/release stewardship is **NEEDS VERIFICATION**. [R-CODEOWNERS] |
| Required reviewers | **NEEDS VERIFICATION** beyond current CODEOWNERS routing | Branch-protection and required-code-owner enforcement were inaccessible to the connector in this run. |
| Adoption state | Not adopted | Requires a separate human/governance decision that explicitly designates this path and records its supersession role. |
| Supersedes | Prior contents at this same path only as a documentation revision | No accepted document-authority supersession is asserted. |
| Generated projections | None verified as a generated projection of this Markdown | A future site/PDF projection must identify this Markdown as its source and remain non-authoritative. |
| Source snapshot | 2026-08-15 | Repository, Drive, attached corpus, and primary external references reconciled. |
| Stale-state rule | Reverify before relying on “current” claims after material changes to main, adopted ADRs, root registries, major contracts/schemas/policy, or deployment evidence | Current-state statements are commit-pinned. |
| Review cadence | **NEEDS VERIFICATION** | Proposed trigger-based review is safer than inventing a calendar cadence. |
| Correction method | Same-path correction PR with evidence, change log, and affected-link validation | Do not create a competing “fixed/final/v2” document. |
| Rollback method | Revert this documentation commit and any directly coupled navigation/receipt edit | Does not roll back system behavior, release state, or data. |

**Non-effects.** This document does not activate a source, authorize live network access, approve policy, alter sensitivity classifications, release or publish data, deploy services, change repository settings, synchronize the native GitHub Wiki, authenticate reviewers, or supersede accepted ADRs/contracts/schemas/policy.

### Truth-label key

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified in this build from current repository evidence, a supplied source, generated artifact, or authoritative primary source. |
| `PROPOSED` | Design, recommendation, target, path interpretation, or future state not proven as implemented/adopted. |
| `UNKNOWN` | Insufficient evidence. |
| `NEEDS VERIFICATION` | Checkable, but not verified strongly enough to act as fact. |
| Qualifiers | `CONFLICTED`, `SUPERSEDED`, `STALE`, `INFERRED`, `NARROWED`, and `PARTIAL` refine a core label. |

### Implementation-maturity key

| Maturity | Meaning |
|---|---|
| `IMPLEMENTED` | Current repository evidence plus appropriate executable/consumption evidence supports the capability. |
| `IMPLEMENTED_WITH_LIMITATIONS` | Working bounded surface exists, but important scope/operational constraints remain. |
| `PARTIAL` | Some dependency-closed parts exist; end-to-end capability is not established. |
| `DRAFT` | Repository artifact exists but remains proposal/draft or is not adopted. |
| `FIXTURE_ONLY` | Demonstrated only with deterministic/synthetic fixtures. |
| `PROPOSED` | Design exists without implementation proof. |
| `DEPRECATED` | Retained for compatibility/migration; not for new canonical writes. |
| `ABSENT` | Verified missing at the inspected scope. |
| `NOT_INSPECTED` | No sufficient inspection was performed. |
| `UNKNOWN` | Evidence does not support a maturity classification. |

### Source IDs used throughout

Repository citations use commit-pinned sources. Attached/Drive sources are lineage or design evidence unless explicitly adopted. External references provide current technical language, not KFM authority.

- **R-DIR** — [Directory Rules v2](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/docs/doctrine/directory-rules.md)
- **R-ADR29** — [ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- **R-ADRINDEX** — [ADR index](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/docs/adr/INDEX.md)
- **R-ROOTREG** — [root registry](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/control_plane/root_registry.yaml)
- **R-DOMREG** — [domain-lane register](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/control_plane/domain_lane_register.yaml)
- **R-OBJREG** — [object-family register](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/control_plane/object_family_register.yaml)
- **R-CODEOWNERS** — [CODEOWNERS](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/.github/CODEOWNERS)
- **R-README** — [repository README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/README.md)
- **R-CONTRIB** — [CONTRIBUTING](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/CONTRIBUTING.md)
- **R-MAKE** — [Makefile](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/Makefile)
- **R-PYPROJECT** — [pyproject.toml](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/pyproject.toml)
- **R-PACKAGE** — [root package.json](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/package.json)
- **R-DATA** — [data root README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/data/README.md)
- **R-CONTRACTS** — [contracts root README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/contracts/README.md)
- **R-SCHEMAS** — [schemas root README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/schemas/README.md)
- **R-POLICY** — [policy root README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/policy/README.md)
- **R-RELEASE** — [release root README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/release/README.md)
- **R-RUNTIME** — [runtime root README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/runtime/README.md)
- **R-SECURITY** — [security guidance index](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/docs/security/README.md)
- **R-DOMAINS** — [domain documentation index](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/docs/domains/README.md)
- **R-EXPLORER** — [Explorer Web README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/apps/explorer-web/README.md)
- **R-GAPI** — [Governed API README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/apps/governed-api/README.md)
- **R-GAPI-MAIN** — [Governed API WSGI entrypoint](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/apps/governed-api/src/governed_api/main.py)
- **R-GAPI-REG** — [Governed API route registry](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/apps/governed-api/src/governed_api/routes/registry.py)
- **R-CLI** — [CLI README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/apps/cli/README.md)
- **R-GENREC** — [generated-receipt README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/data/receipts/generated/README.md)
- **R-GENREC-SCHEMA** — [GENERATED_RECEIPT schema](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a768ed812df41e3466758b60af087129997fb337/schemas/contracts/v1/receipts/generated_receipt.schema.json)

[Back to top](#top)

---

## Table of Contents

0. [Document Control and Authority](#0-document-control-and-authority)  
1. [Executive Summary](#1-executive-summary)  
2. [Audience and Reading Paths](#2-audience-and-reading-paths)  
3. [Evidence Basis and Authority Model](#3-evidence-basis-and-authority-model)  
4. [Purpose, Scope, Principles, and Non-Goals](#4-purpose-scope-principles-and-non-goals)  
5. [Current-State Repository and Capability Snapshot](#5-current-state-repository-and-capability-snapshot)  
6. [Target Whole-System Architecture](#6-target-whole-system-architecture)  
7. [Repository and Directory Architecture](#7-repository-and-directory-architecture)  
8. [Ubiquitous Language, Bounded Contexts, and Core Object Families](#8-ubiquitous-language-bounded-contexts-and-core-object-families)  
9. [Identity, Time, Geography, Scale, and Uncertainty](#9-identity-time-geography-scale-and-uncertainty)  
10. [Data Lifecycle, Storage, and Processing](#10-data-lifecycle-storage-and-processing)  
11. [Source Admission, Connectors, and Watchers](#11-source-admission-connectors-and-watchers)  
12. [Evidence, Provenance, Catalog, Receipts, and Proof](#12-evidence-provenance-catalog-receipts-and-proof)  
13. [Promotion, Release, Publication, Correction, and Rollback](#13-promotion-release-publication-correction-and-rollback)  
14. [Domain Atlas](#14-domain-atlas)  
15. [Cross-Domain Relations and Anti-Collapse Rules](#15-cross-domain-relations-and-anti-collapse-rules)  
16. [Applications, Packages, Services, and Workers](#16-applications-packages-services-and-workers)  
17. [API and CLI Reference](#17-api-and-cli-reference)  
18. [MapLibre, Maps, Tiles, and Governed UI](#18-maplibre-maps-tiles-and-governed-ui)  
19. [Governed AI](#19-governed-ai)  
20. [Feature and Capability Catalog](#20-feature-and-capability-catalog)  
21. [Security, Privacy, Rights, and Sensitivity](#21-security-privacy-rights-and-sensitivity)  
22. [Governance and Decision Rights](#22-governance-and-decision-rights)  
23. [Developer Build, Installation, and Contribution Guide](#23-developer-build-installation-and-contribution-guide)  
24. [Pipeline and Data Engineering Guide](#24-pipeline-and-data-engineering-guide)  
25. [Testing, Validation, and Quality Assurance](#25-testing-validation-and-quality-assurance)  
26. [CI/CD, Repository Controls, Release, and Deployment](#26-cicd-repository-controls-release-and-deployment)  
27. [Runtime, Infrastructure, and Operations](#27-runtime-infrastructure-and-operations)  
28. [User and Operator Guides](#28-user-and-operator-guides)  
29. [Accessibility, Performance, Reliability, and Compatibility](#29-accessibility-performance-reliability-and-compatibility)  
30. [Current Gaps, Roadmap, and Dependency Order](#30-current-gaps-roadmap-and-dependency-order)  
31. [Risks, Limitations, Assumptions, and Open Questions](#31-risks-limitations-assumptions-and-open-questions)  
32. [Glossary and Acronyms](#32-glossary-and-acronyms)  
33. [Embedded Appendices](#33-embedded-appendices)  

[Back to top](#top)

---

## 1. Executive Summary

KFM is a **Kansas-first, map-first, time-aware, evidence-first spatial knowledge and publication system**. Its durable public value is the **inspectable claim**: a claim whose source role, evidence, place/time scope, policy posture, review state, release state, correction lineage, and rollback support can be inspected. **CONFIRMED doctrine / PARTIAL implementation.** [R-README] [R-DIR]

KFM is **not** merely a map application, data warehouse, chatbot, alert authority, or collection of domain datasets. Maps, tiles, graphs, indexes, summaries, dashboards, scenes, exports, and AI responses are downstream carriers. Public clients should consume governed interfaces and released public-safe carriers rather than RAW, WORK, QUARANTINE, canonical/internal stores, or direct model runtimes. **CONFIRMED doctrine; multiple structural guards exist; operational deployment remains UNKNOWN.** [R-README] [R-RUNTIME] [R-DATA]

### Current overall maturity

| Area | Truth status | Maturity | Current evidence-bounded conclusion |
|---|---|---|---|
| Directory governance | `CONFIRMED` | `IMPLEMENTED_WITH_LIMITATIONS` | ADR-0029 is accepted and adopts exact Directory Rules v2 bytes; machine projections and topology ratchets exist, but migration debt remains. [R-ADR29] [R-ROOTREG] |
| Repository responsibility roots | `CONFIRMED` | `IMPLEMENTED_WITH_LIMITATIONS` | Canonical, compatibility, deprecated, conditional, and platform roots are projected; legacy drift is intentionally visible. [R-ROOTREG] |
| Contracts and schemas | `CONFIRMED` | `PARTIAL` | Canonical semantic/machine-shape roots exist with extensive artifacts and validation; schema subhome ADRs remain proposed and compatibility drift remains. [R-CONTRACTS] [R-SCHEMAS] |
| Policy | `CONFIRMED` | `PARTIAL / FIXTURE_ONLY` | Canonical policy root and bounded Rego profiles exist; no accepted repository-wide evaluator or production PolicyDecision flow is proved. [R-POLICY] |
| Release | `CONFIRMED` | `FIXTURE_ONLY / HOLD` | Release object shapes and promotion-gate fixtures exist; authenticated operational release/promotion/rollback and public parity are not proved. [R-RELEASE] |
| Governed API | `CONFIRMED` | `IMPLEMENTED_WITH_LIMITATIONS` | Three GET routes exist and deliberately return finite scaffold envelopes; unknown routes/methods return finite errors. No production deployment is proved. [R-GAPI-MAIN] [R-GAPI-REG] |
| Explorer Web | `CONFIRMED` | `PARTIAL / FIXTURE_ONLY` | Vite/TypeScript shell and bounded trust-visible slices exist; live map transport, production API binding, public deployment, and full route tree are not established. [R-EXPLORER] |
| MapLibre proof/tooling | `CONFIRMED` | `PARTIAL` | Build/performance/proof commands exist; a production released map is not established. [R-MAKE] |
| AI runtime | `CONFIRMED surfaces` | `PARTIAL / UNKNOWN execution` | Provider-neutral runtime documentation/contracts/mocks exist; direct public runtime is denied; production model execution and evidence/citation closure are not established. [R-RUNTIME] |
| Domain lanes | `CONFIRMED registry` | `MIXED / NEEDS VERIFICATION` | 13 registered domain lanes exist in a proposed machine projection; lane implementation maturity is intentionally not inferred. [R-DOMREG] [R-DOMAINS] |
| Operations/deployment | `UNKNOWN` | `UNKNOWN` | Configuration/infrastructure/runtime artifacts exist, but deployment, production storage, DNS/TLS, backups, dashboards, and public serving were not verified. |

### Most important current surfaces

- Accepted Directory Rules v2 through ADR-0029 and active root/domain governance projections.
- Canonical semantic-contract, machine-schema, policy, lifecycle-data, release, runtime, test, fixture, validator, and app roots.
- Three bounded Governed API GET routes: `/bootstrap`, `/layers`, and `/evidence`, each currently fail-safe scaffolding.
- Explorer Web trust-visible UI work, Evidence Drawer-oriented slices, and MapLibre performance/proof tooling.
- Registry-driven validation, workflow-security and repository-topology ratchets, boundary guards, publication-denial/release fixture checks, and generated AI-work receipts.
- Thirteen registered domain lanes with substantive human-readable lane READMEs.

### Most important incomplete or unresolved surfaces

- No adopted decision designates this whole-system document as canonical authority.
- No accepted general policy evaluation and authenticated PolicyDecision consumption are proved.
- Operational release, deployment, publication, cache invalidation, correction propagation, and rollback execution are not proved end to end.
- Domain/source stewardship and independent review remain mostly unassigned or unverified.
- Current public map, public search, live-source ingestion, and direct EvidenceBundle-backed user flows are not established as deployed.
- Schema subhome authority and several compatibility/migration paths remain unresolved.
- Branch protection and required-check configuration could not be read through the connector.

### Recommended reading paths

Maintainers should read §§0–7, 10–13, 22–27 first. Domain stewards should add §§8–15 and Appendix G. UI/API/AI engineers should focus on §§16–20. Security/release reviewers should focus on §§12–13 and §§21–27. Public/research users should start with §§1, 2, 18, 20, and 28.

[Back to top](#top)

---

## 2. Audience and Reading Paths

| Audience | Start here | Primary questions |
|---|---|---|
| Public user | §§1, 18, 20, 28 | What can I inspect now? What do trust/stale/deny/correction states mean? |
| Researcher / analyst | §§3, 9, 12, 14, 17, 28 | What is authoritative, how do place/time/source roles work, and how should outputs be cited? |
| Developer | §§5–8, 16–17, 23–26 | Where does code belong, what builds, what contracts apply, and which checks must run? |
| Domain maintainer | §§8–15, 24–25, Appendix G | What does my lane own, which source roles are valid, and how does the lane join shared trust objects? |
| Source steward | §§3, 10–12, 21–22, 24 | What can be admitted, under which rights/currentness/sensitivity conditions? |
| Evidence reviewer | §§8, 9, 12, 13, 25 | Does a claim close to admissible evidence and provenance? |
| Policy/sensitivity reviewer | §§10–13, 21–22 | What must fail closed and what transformations are permitted? |
| Security reviewer | §§16–21, 25–27, Appendix J | Where are the trust boundaries and current enforcement gaps? |
| Release steward | §§12–13, 22, 25–27 | What evidence, review, manifest, rollback, and correction objects are required? |
| Operator | §§23–29 | How are validation, runtime, deployment, health, incidents, and rollback handled? |
| AI builder | §§8, 12, 19, 21, 23, 25 | What may a model do, and what evidence/policy path constrains it? |
| Project decision-maker | §§1, 3, 5–6, 20, 30–31 | What is implemented, what is proposed, and which decisions block safe progress? |

[Back to top](#top)

---

## 3. Evidence Basis and Authority Model

### 3.1 Authority by question

| Question | Primary authority | Secondary evidence |
|---|---|---|
| What exists now? | Pinned repository tree and current bytes | Current tests/workflows/manifests tied to the same revision |
| What works now? | Implementation plus representative test/run/runtime evidence | Current docs describing the exact implementation |
| Where does a file belong? | Accepted Directory Rules and accepted ADRs | Root registry and per-root README contracts |
| What does an object mean? | Semantic contract | Machine schema, policy, implementation |
| What machine shape is valid? | Machine schema | Fixtures/validators/tests |
| May an operation or claim be exposed? | Policy + source/evidence/review/release context | Runtime enforcement and tests |
| Is something released/published? | Release decision plus public-safe carrier and current delivery evidence | Manifests, proofs, receipts, runtime/public verification |
| What should exist next? | Current user scope + adopted governance + evidence-backed gap | Proposal corpus and primary technical references |

### 3.2 Source classes

1. **Current repository evidence** — highest authority for current implementation claims.
2. **Accepted ADRs and adopted doctrine** — decision/operating-law authority.
3. **Current contracts, schemas, policy, tests, workflows, manifests, and root READMEs** — responsibility-specific current evidence.
4. **Drive and attached KFM doctrine/lineage** — design, rationale, historical decisions, and proposal pressure; never current implementation proof by repetition.
5. **General technical references** — background language only.
6. **Primary external standards/tool documentation** — current technical facts and vocabulary, not KFM authority.

### 3.3 Current-session limitations

- No local repository clone could be created because the execution container had no DNS access to GitHub; repository reads and writes therefore use the GitHub connector.
- Branch-protection details were not accessible through the integration and remain `UNKNOWN / NEEDS VERIFICATION`.
- No production runtime, database, object store, DNS, TLS endpoint, dashboard, private secret store, or deployment environment was inspected.
- Google Drive search was broad; only selected high-signal documents were opened in depth. Search result dates are not treated as authority.
- Attached documents were read as supplied evidence; older “no mounted repo” statements remain valid for their authoring runs but are superseded for current-state claims by this repository inspection.

### 3.4 Baseline CI evidence

At exact `main@a768ed812df41e3466758b60af087129997fb337`, the `validator-suite` push run failed in its `run-validators` job at the guardrail-attribution test; the fail-closed canary job passed. A separate open **draft** PR (#2937) already owns the focused repair. This documentation work does not duplicate or modify that repair. Later validation failures skipped by the baseline job must not be misclassified as either passing or failing.

[Back to top](#top)

---

## 4. Purpose, Scope, Principles, and Non-Goals

### Mission

KFM exists to make Kansas-centered spatial knowledge **traceable, reviewable, useful, correctable, and reversible across place and time**. It connects sources to claims through explicit evidence, identity, policy, validation, release, and correction controls.

### Core invariants

1. `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`.
2. Publication is a governed transition, not a path, commit, merge, badge, GitHub release, or UI toggle.
3. Public clients use governed interfaces and released public-safe carriers.
4. Canonical/internal stores are not normal public paths.
5. Consequential `EvidenceRef` values should resolve to `EvidenceBundle`.
6. Cite-or-abstain is the default truth posture.
7. Unknown rights, sensitivity, source role, or review state fails closed where risk matters.
8. Deterministic identity and replay are preferred where practical.
9. Watchers/drift detectors propose work; they do not publish.
10. Receipts, proofs, catalogs, registries, manifests, reviews, decisions, corrections, rollback records, and published carriers remain distinct families.
11. Maps, tiles, graphs, indexes, scenes, dashboards, screenshots, summaries, and AI answers are downstream carriers.
12. AI is interpretive and subordinate to evidence, policy, review, and release state.
13. Corrections, withdrawal, supersession, invalidation, and rollback are first-class.
14. File placement encodes responsibility and authority.
15. Domains normally appear as lanes under responsibility roots.
16. Higher-consequence release requires proportionate review; separation of duties remains a maturity target where not yet enforced.

### Non-goals

KFM is not an emergency-alert authority, a source-license bypass, a substitute for tribal/cultural/legal review, a direct browser-to-model architecture, a client-side redaction system, an ungoverned scraper, a single-confidence-score truth engine, or a mechanism for turning generated prose into evidence.

Documentation is part of the control plane because it records meaning, placement, procedures, limits, and verification state. Documentation still cannot replace code, policy, review, or runtime proof.

[Back to top](#top)

---

## 5. Current-State Repository and Capability Snapshot

### 5.1 Repository snapshot

**CONFIRMED at `a768ed812df41e3466758b60af087129997fb337`.** The active responsibility-root model includes canonical roots for applications, configuration, connectors, contracts, control-plane projections, data, docs, examples, fixtures, infrastructure, migrations, packages, pipeline specs/pipelines, policy, release, runtime, schemas, scripts, tests, and tools; `.github/` is platform integration. `artifacts/` is compatibility/temporary output, `catalog/` is deprecated/frozen containment, and `src/` is conditional/unresolved. [R-ROOTREG]

```text
repository root
├── .github/                platform integration
├── apps/                   deployable applications
├── configs/                non-secret configuration
├── connectors/             source-specific intake implementation
├── contracts/              semantic meaning
├── control_plane/          machine projections of governance
├── data/                   lifecycle/accountability instances
├── docs/                   human-readable doctrine/decisions/guidance
├── examples/               runnable public-safe demonstrations
├── fixtures/               reusable synthetic/golden inputs
├── infra/                  deployment/network/exposure implementation
├── migrations/             governed migrations and rollback definitions
├── packages/               reusable non-deployable libraries
├── pipeline_specs/         declarative run graphs/configuration
├── pipelines/              executable lifecycle transforms
├── policy/                 admissibility rules
├── release/                release/correction/rollback decisions
├── runtime/                internal runtime composition/adapters
├── schemas/                machine-checkable shapes
├── scripts/                thin helpers
├── tests/                  executable conformance evidence
└── tools/                  validators/builders/inspectors/operators
```

### 5.2 App inventory

| App | Current state | Maturity | Evidence-bounded use |
|---|---|---|---|
| `apps/explorer-web/` | Vite/TypeScript shell with bounded fixture-first trust/UI slices | `PARTIAL / FIXTURE_ONLY` | Developer/review shell; public deployment not proved. [R-EXPLORER] |
| `apps/governed-api/` | WSGI scaffold with finite envelopes and tests | `IMPLEMENTED_WITH_LIMITATIONS` | GET `/bootstrap`, `/layers`, `/evidence`; scaffold responses; local serving at 127.0.0.1:8000 by default. [R-GAPI-MAIN] |
| `apps/cli/` | Documentation/package skeleton; command implementation not established | `DRAFT / PARTIAL` | Operator CLI target architecture; do not advertise commands not present. [R-CLI] |
| `apps/admin/` | Path present | `NEEDS VERIFICATION` | Restricted admin responsibility; implementation not inspected in this build. |
| `apps/review-console/` | Path present | `NEEDS VERIFICATION` | Steward/review surface; implementation not inspected in depth. |
| `apps/workers/` | Path present | `NEEDS VERIFICATION` | Background/deployable worker boundary; exact worker inventory not documented here. |

### 5.3 Trust-root inventory

| Root | Current posture | Important limitation |
|---|---|---|
| `contracts/` | Canonical semantic-meaning root | Some inherited machine-schema drift remains under contracts; subhome ADRs proposed. |
| `schemas/` | Canonical machine-shape root; JSON Schema 2020-12 | Compatibility lanes remain; schema validity is not truth or permission. |
| `policy/` | Canonical admissibility root | Repository-wide active evaluator and production consumers not proved. |
| `data/` | Canonical lifecycle/accountability root | Internal lanes are not public; compatibility/migration children remain. |
| `release/` | Canonical append-only release-decision plane | Operational release/promotion/rollback execution is held/unproved. |
| `runtime/` | Canonical internal adapter/composition root | Production model/provider behavior and deployment unproved. |
| `tests/`, `fixtures/`, `tools/` | Executable/synthetic/tooling evidence roots | A green bounded check proves only its declared scope. |

### 5.4 Domain inventory

The current machine projection contains **13 registered lanes**: agriculture, archaeology, atmosphere, fauna, flora, geology, habitat, hazards, hydrology, people-dna-land, roads-rail-trade, settlements-infrastructure, and soil. The projection is itself `PROPOSED / machine_projection_only`; it does not assign stewards or prove implementation. [R-DOMREG]

Spatial foundation, frontier-matrix analytics, planetary/3D, remote sensing/field capture, Briefing-to-System integration, and Focus Modes are cross-cutting capability families in the corpus and/or repository—not automatically additional canonical domains.

### 5.5 Current baseline failures and active work

- `validator-suite` fails on exact main at the focused guardrail-attribution test.
- Draft PR #2937 is the current focused repair owner.
- This documentation PR must therefore classify the baseline validator-suite failure as **inherited** unless its own changes introduce a distinct failure.
- Branch protection and required checks remain `NEEDS VERIFICATION` because the integration cannot read protection settings.

[Back to top](#top)

---

## 6. Target Whole-System Architecture

> **Diagram source note: SYNTHESIS.** The responsibilities are derived from accepted KFM doctrine plus current repository boundaries; the end-to-end operational closure is a target where current runtime/release evidence is incomplete.

```text
SOURCE SYSTEMS / ARCHIVES / FIELD CAPTURE
        |
        v
source identity + rights + source role + activation decision
        |
        v
PRE-RAW / ADMISSION  ---- unsafe / unresolved ----> QUARANTINE
        |
        v
RAW capture / immutable locator / retrieval receipt
        |
        v
WORK normalization / identity / time / geometry / crosswalk
        |
        +---- invalid / conflicted / over-precise ----> QUARANTINE
        v
PROCESSED validated domain records
        |
        v
EVIDENCE + CATALOG + optional TRIPLET projections
        |
        v
POLICY + REVIEW + VALIDATION + PROOF + PROMOTION DECISION
        |
        v
RELEASE MANIFEST + PUBLIC-SAFE CARRIERS + ROLLBACK TARGET
        |
        v
PUBLISHED / RELEASED DELIVERY
        |
        +--> governed API
        +--> tiles / PMTiles / COG / GeoParquet / catalog
        +--> Explorer Web / Evidence Drawer / Focus Mode
        +--> exports / stories / analyst surfaces
        |
        v
CORRECTION / WITHDRAWAL / SUPERSESSION / INVALIDATION / ROLLBACK
```

### Trust boundaries

- **External boundary:** source material is untrusted until identity/role/rights/sensitivity checks.
- **Lifecycle boundary:** internal stages do not imply public eligibility.
- **Policy/release membrane:** validation success cannot substitute for policy/review/release.
- **Public delivery boundary:** only released/public-safe carriers and governed API responses are normal public inputs.
- **AI boundary:** model/runtime execution occurs behind governed application controls; model text is never evidence authority.
- **Correction boundary:** public carriers, caches, search/indexes, map state, and AI context must be invalidatable/rebuildable from corrected governed state.

### Current versus target

| Capability | Current | Target |
|---|---|---|
| Governed API | Three finite scaffold GET routes | Evidence/release-aware versioned resource families with authorization, pagination/filtering where needed |
| Explorer | Fixture-first trust slices, no established live map transport | Released-layer map shell, time controls, Evidence Drawer, Focus Mode, export/review states |
| Policy | Bounded inactive profiles, structural guards | Accepted evaluator/bundle selection, authenticated PolicyDecision flow, operation-specific obligations |
| Release | Fixture-first manifest/promotion/rollback shapes | Authenticated promotion, immutable release assembly, signatures/attestations as adopted, correction/invalidation/rollback drills |
| Domain lanes | 13 registered documentation identities, mixed implementation | Consistent source/evidence/policy/lifecycle/release packet per mature lane |
| AI | Runtime/adapters/contracts partially present | Provider-neutral, evidence-resolving, policy-checked, citation-validated finite outcomes with receipts |
| Operations | Repo configuration and runbooks exist | Verified environments, observability, backup/recovery, capacity, incident and rollback evidence |

[Back to top](#top)

---

## 7. Repository and Directory Architecture

### 7.1 Directory law

Accepted Directory Rules v2 make **responsibility** the primary placement key. A root is not a topic bucket. Domain and geographic concerns normally appear as lanes inside the root that owns the artifact type. [R-DIR] [R-ADR29]

### 7.2 Canonical root responsibility matrix

| Root | Owns | Must not own | Public exposure |
|---|---|---|---|
| `docs/` | Human doctrine, ADRs, architecture, runbooks, guidance | Schemas, policy rules, data/release instances | Mostly public documentation |
| `control_plane/` | Machine projections/indexes of adopted governance | New governance authority | Internal |
| `contracts/` | Semantic meaning/invariants/promises | Machine schemas, policy, instances | Public docs |
| `schemas/` | Machine-checkable shapes | Semantic meaning, policy, data | Public artifacts |
| `policy/` | Allow/deny/hold/restrict/abstain rules | Evidence/data/release instances | Internal |
| `tests/` | Executable conformance evidence | Canonical data instances | Public/synthetic |
| `fixtures/` | Reusable synthetic valid/invalid/golden cases | Sensitive real data | Public/synthetic |
| `tools/` | Repo-wide validators/builders/operators | Deployable apps or policy authority | Internal |
| `apps/` | Deployable service/user boundaries | Shared semantic authority | Mixed |
| `packages/` | Reusable libraries | Deployable service ownership | Internal |
| `connectors/` | Source-specific fetch/admission implementation | Publication | Internal |
| `pipelines/` | Executable lifecycle transformations | Release decisions | Internal |
| `pipeline_specs/` | Declarative pipeline graphs/config | Runtime execution itself | Internal |
| `data/` | Lifecycle/accountability instances | Policy/schema/semantic authority | Mixed; internal by default |
| `release/` | Release/correction/withdrawal/rollback decisions | Published payloads, policy source | Internal/audit |
| `runtime/` | Internal provider/runtime composition | Public API, release authority | Internal |
| `infra/` | Deployment/network/exposure/provisioning implementation | Application/domain semantics | Internal |
| `configs/` | Non-secret defaults/templates | Secrets | Internal |
| `migrations/` | Versioned migration and rollback definitions | Ordinary runtime state | Internal |
| `examples/` | Runnable public-safe examples | Unreleased real data | Public |
| `scripts/` | Thin non-authoritative helpers | Long-lived trust authority | Internal |

### 7.3 Compatibility and drift

- `artifacts/` is temporary/generated compatibility output and may not acquire receipts/proofs/release/data authority.
- top-level `catalog/` is deprecated containment; new canonical catalog instances belong under the accepted `data/` model.
- `src/` remains a conditional facade candidate, not an independent authority.
- legacy architecture Directory Rules path is read-only compatibility during ADR-0029 migration.
- current direct-child and nested drift is a migration problem, not permission to create parallel homes.

### 7.4 Dependency direction

Implementation should depend on stable semantics and machine contracts, not the reverse. Public surfaces depend on governed/released interfaces. Derived carriers remain rebuildable. A package may implement shared behavior, but it does not acquire policy/evidence/release authority.

[Back to top](#top)

---

## 8. Ubiquitous Language, Bounded Contexts, and Core Object Families

KFM's domain model is intentionally split: a source is not evidence; evidence is not a policy decision; a receipt is not proof; a proof is not release; a catalog record is not publication; a representation is not reality; an AI answer is not source truth.

### 8.1 Core terms

| Term | KFM meaning |
|---|---|
| Entity | A thing with stable identity in a bounded context. |
| Observation | A source/method/time/place-bounded measurement or report. |
| Assertion / claim | A proposition whose support and scope must be inspectable. |
| Source | External or internal origin with explicit role, rights, identity, cadence, and limitations. |
| Evidence | Admissible support for a claim; not equivalent to raw source bytes. |
| Dataset version | Reproducible version identity for a dataset or logical snapshot. |
| Geometry version | Versioned spatial representation with CRS/datum/scale/validity. |
| Policy decision | Operation-specific admissibility result with reasons/obligations. |
| Validation result | Bounded evidence that an instance/process met declared checks. |
| Receipt | Process memory: what ran, with which inputs/results. |
| Proof | Closure evidence for a declared proposition/gate; distinct from receipt. |
| Catalog record | Discoverability/projection metadata, not sovereign truth. |
| Release | Governed decision state plus immutable/identifiable public-safe carrier set. |
| Correction | Explicit amendment that preserves lineage. |
| Rollback | Controlled restoration to a prior governed state. |
| Representation | Map/tile/scene/export/summary carrier with explicit reality/evidence limits. |
| AI interpretation | Generated explanation/proposal subordinate to evidence and policy. |

### 8.2 Object-family crosswalk

| Object family | Repository evidence | Current maturity | Required relationship |
|---|---|---|---|
| `SourceDescriptor` | Contracts/schemas/source registries appear across repo | `PARTIAL` | Defines source role/rights/cadence before live activation. |
| `SourceActivationDecision` | Corpus + source governance surfaces | `PROPOSED / NEEDS VERIFICATION` | Must not be inferred from connector presence. |
| `DatasetVersion` | Contract/schema work exists in repo lineage | `PARTIAL / NEEDS VERIFICATION current consumer closure` | Binds source version, schema, hashes, scope. |
| `EventEnvelope` | Pre-RAW/event proposals and some schemas | `PARTIAL / PROPOSED` | Admission signal only; not public truth. |
| `BriefingSignal` | Briefing integration design; repo adoption not established | `PROPOSED` | Internal discovery/control-plane object. |
| `TemporalAuthorityEnvelope` | Briefing integration design | `PROPOSED` | Shared metadata envelope; not domain replacement. |
| `EvidenceRef` | Core doctrine and repo evidence family | `PARTIAL` | Stable pointer/locator with scope. |
| `EvidenceBundle` | Core doctrine, validators, canary tests | `PARTIAL` | Resolved support for consequential claims. |
| `PolicyDecision` | Contracts/schemas/policy language | `PARTIAL / no general active evaluator` | Operation-specific admissibility, reasons, obligations. |
| `DecisionEnvelope` | Object-family register | `PARTIAL` | Runtime finite decision transport; subordinate to policy/evidence. |
| `RuntimeResponseEnvelope` | Object-family register + Governed API | `IMPLEMENTED_WITH_LIMITATIONS` | Finite API response envelope. |
| `RunReceipt` | Object-family register | `PARTIAL` | Process provenance, not proof. |
| `TransformReceipt` | Corpus + receipt lanes | `PARTIAL / NEEDS VERIFICATION` | Records transformation inputs/spec/output. |
| `AIReceipt` | Object-family register + runtime contract/schema | `PARTIAL` | Model/runtime provenance; no truth authority. |
| `PromotionDecision` | Release fixtures/tests | `FIXTURE_ONLY / PROPOSED_INACTIVE` | Explicit governed transition decision. |
| `PromotionReceipt` | Proposal corpus; A–G gate vocabulary exists | `PROPOSED / NEEDS VERIFICATION` | Auditable gate aggregation where adopted. |
| `ProofPack` | Data/release/MapLibre proof lanes | `PARTIAL` | Proof closure separate from receipts and release decision. |
| `LayerManifest` | Map/UI corpus and repository artifacts | `PARTIAL` | Released layer identity, inputs, style/delivery/evidence policy. |
| `TileArtifactManifest` | Map delivery proposal/current tooling | `PARTIAL / PROPOSED` | Digest/format/hosting metadata for tile carrier. |
| `ReleaseManifest` | Release schema/fixtures | `FIXTURE_ONLY / PROPOSED_INACTIVE strict profile` | Released carrier set and rollback/correction refs. |
| `RollbackCard` | Release schema/fixtures | `FIXTURE_ONLY` | Bounded rollback target and prerequisites. |
| `CorrectionNotice` / `WithdrawalNotice` | Release/docs corpus | `PARTIAL / NEEDS VERIFICATION` | First-class correction/withdrawal lineage. |
| `RepresentationReceipt` | 3D/map corpus | `PROPOSED / PARTIAL` | Records derived representation/reality boundary. |
| `RealityBoundaryNote` | Planetary/3D corpus | `PROPOSED` | Explicitly separates reconstruction/model from observation. |
| `GENERATED_RECEIPT` | Schema, validator, populated lane, PR template | `IMPLEMENTED_WITH_LIMITATIONS` | AI-authored artifact provenance; human review stays separate. [R-GENREC] |

The current machine object-family register is intentionally partial and covers six runtime families only; do not treat it as an exhaustive registry. [R-OBJREG]

[Back to top](#top)

---

## 9. Identity, Time, Geography, Scale, and Uncertainty

### Identity

KFM prefers stable source-native identifiers where available, deterministic derived IDs where practical, canonical serialization for hashes where contractually defined, and explicit version IDs for mutable datasets/geometry. A digest proves bytes, not semantics or rights.

### Time model

Keep distinct when material:

- source valid time;
- observation time;
- issue/publication time from source;
- retrieval time;
- processing/transform time;
- KFM review/release time;
- correction/withdrawal time;
- transaction/system time for bitemporal uses.

A stale source is not equivalent to false data. A corrected source is not equivalent to deleting history.

### Geography

Every spatially consequential object should carry or resolve:

- geometry/feature identity;
- geometry version/vintage;
- CRS and datum;
- source scale/resolution and fitness-for-use;
- spatial scope/bbox/administrative or natural-unit context;
- public-safe transform/generalization status where applicable.

### Scale and uncertainty

KFM must not hide:

- source scale mismatch;
- interpolation/model uncertainty;
- map generalization;
- confidence vs quality vs source authority;
- observed vs interpreted vs modeled status;
- exact vs generalized geometry;
- historical vs current boundaries.

[Back to top](#top)

---

## 10. Data Lifecycle, Storage, and Processing

### 10.1 Lifecycle transitions

| Stage | Entry criteria | Allowed producers | Required checks | Failure outcome | Public visibility |
|---|---|---|---|---|---|
| Pre-RAW/admission | Identified candidate event/source and governing intake context | Watcher, connector preflight, steward/manual intake | Source identity, role, terms/rights, sensitivity precheck | HOLD/QUARANTINE/DENY | None |
| RAW | Admitted capture or immutable locator with source provenance | Connector/intake system | Retrieval integrity, source descriptor linkage, receipt | QUARANTINE/ERROR | None |
| WORK | Candidate transform/normalization | Pipelines/tools | Schema evolution, identity, time, geometry, source-role rules | QUARANTINE/HOLD | None |
| QUARANTINE | Any unresolved safety/quality/rights/evidence state | Any upstream gate | Review and reason codes; no silent promotion | Retain/deny/correct | None |
| PROCESSED | Domain-shape and bounded validations pass | Pipelines | Contract/schema/domain checks, receipts | HOLD/ERROR | Internal |
| CATALOG/TRIPLET | Validated records can be projected/discovered | Catalog/graph emitters | Provenance/evidence references, projection consistency | HOLD/ERROR | Governed/internal unless released |
| PUBLISHED | Explicit release decision for public/semi-public scope | Release process only | Evidence, policy, review, proof, manifest, correction/rollback | DENY/HOLD/ERROR | Through governed/released delivery |

### 10.2 Logical home versus physical bytes

Directory authority identifies the **logical KFM home**. Large payloads may physically live in object storage, databases, registries, or caches; their identity/manifest/provenance still resolves to the logical lifecycle and governance model. Do not commit sensitive or massive bytes merely because `data/` is the logical owner.

### 10.3 Mutability

- RAW captures and audit receipts should be immutable or append-only where contractually appropriate.
- WORK can be mutable by controlled process.
- QUARANTINE retains reason/lineage.
- PROCESSED artifacts should be versioned/reproducible.
- Catalog/graph projections are rebuildable and should not overwrite canonical evidence.
- PUBLISHED carriers are immutable/versioned; correction creates new lineage rather than silent mutation.

[Back to top](#top)

---

## 11. Source Admission, Connectors, and Watchers

### 11.1 Source-admission model

A source must be classified before live use by:

- issuing organization/system and stable identity;
- source role (`authoritative`, `regulatory`, `observational`, `modeled`, `aggregator`, `contextual`, etc.);
- rights/license/terms/attribution/caching/redistribution constraints;
- access method and credentials boundary;
- update cadence/currentness and change signals;
- spatial/temporal/scale scope;
- sensitivity and public-safe transform requirements;
- expected identifiers/schema;
- failure and correction behavior;
- activation/review state.

Unknown rights or sensitivity does not mean “probably public”: it means hold/quarantine/deny at the applicable risk level.

### 11.2 Connector boundary

`connectors/` owns source-specific retrieval/admission implementation. A connector may fetch and emit intake artifacts/receipts; it must not publish, create release authority, or let source response shape silently become canonical domain semantics.

Default CI should remain no-network and fixture-driven. Live probes belong in explicitly governed/manual/scheduled contexts with credentials, rate limits, terms, and failure handling.

### 11.3 Watchers

Watchers detect candidate material change. Useful signals include:

- ETag / Last-Modified / content length when trustworthy;
- source version IDs or item IDs;
- schema/field drift;
- checksums/digests;
- status/currentness changes;
- bounded domain materiality.

A watcher output is a **candidate**, not a publication. Repeated text or recurring AI summaries never upgrade authority.

### 11.4 Current source/connector maturity

The repository contains many connector/source lanes, but this document does not claim they are all live or admitted. Source activation must be proved per source. The Drive/attached source corpus provides candidate source families (e.g., soil, geology, habitat, atmosphere), but current connector implementation and rights are resolved only from repository/source-specific evidence.

[Back to top](#top)

---

## 12. Evidence, Provenance, Catalog, Receipts, and Proof

### 12.1 Evidence resolution

Preferred consequential-claim path:

```text
claim / feature / answer
  -> EvidenceRef
  -> EvidenceBundle
  -> source identity + role + locator + scope
  -> provenance + integrity
  -> policy/review/release context
  -> citation presented to user/reviewer
```

If the resolver cannot produce admissible support, return a finite negative state (`ABSTAIN`, `DENY`, `HOLD`, or `ERROR`) rather than substitute map properties or generated language.

### 12.2 Anti-collapse matrix

| Object | Records | Does not prove |
|---|---|---|
| Receipt | What process ran, inputs/spec/results | Claim truth, review, release |
| Proof | Closure for a declared proof proposition | Policy permission unless explicitly included |
| Catalog record | Discoverability/projection metadata | Source truth or release |
| Manifest | Enumerated versioned objects/carriers | Human approval by itself |
| Policy decision | Admissibility under an evaluated context | Evidence truth |
| Review record | Human/steward decision state | Machine shape/integrity |
| Release decision | Governed transition | Public reachability by itself |
| Published carrier | Delivery bytes | Currentness/correction unless linked |
| AI receipt | Model execution provenance | Truth or hidden reasoning |

### 12.3 Catalog standards

KFM corpus uses STAC/DCAT/PROV as interoperability patterns. Current external anchors (accessed 2026-08-15) are OGC STAC Community Standard 1.1.0, W3C DCAT 3 Recommendation (2024-08-22), and W3C PROV-O Recommendation. Adoption of a **KFM profile** remains a KFM decision; the standards do not create repository authority.

### 12.4 Derived indexes

Search indexes, vector indexes, graph/triplet projections, map tiles, and caches must be rebuildable from governed source/evidence/release state. They must preserve correction and withdrawal handling and cannot become a hidden truth store.

[Back to top](#top)

---

## 13. Promotion, Release, Publication, Correction, and Rollback

### 13.1 Promotion posture

Current repository evidence supports an **A–G promotion-gate fixture vocabulary** and bounded promotion/review validators, but not authenticated operational promotion. [R-RELEASE] [R-MAKE]

Do not assume older A–F or expanded gate sets are current authority. The safe current statement is: **A–G exists as bounded fixture/test semantics; operational gate authority remains unproved.**

### 13.2 Required release chain

```text
candidate
 -> schema/contract validation
 -> pinned inputs and reproducibility
 -> tests/quality checks
 -> source/evidence closure
 -> policy/rights/sensitivity decision
 -> integrity/signature/attestation checks where adopted
 -> human/steward review where required
 -> PromotionDecision / release decision
 -> ReleaseManifest + public-safe carrier set
 -> rollback/correction/invalidation target
 -> governed delivery
```

### 13.3 Current release maturity

`release/` has fixture-first schemas/validators/tests for ReleaseManifest, PromotionDecision, promotion gates, RollbackCard, and related profiles. This is meaningful implementation evidence, but it is not an operational release system. The general policy evaluator, authenticated reviewers, signing custody, production assembly, live alias mutation, deployment, correction propagation, and rollback application remain held/unknown. [R-RELEASE]

### 13.4 Publication is separate

- Merge ≠ release.
- GitHub release page ≠ KFM publication.
- File under `data/published/` ≠ publication by placement.
- Deployment ≠ publication unless a release decision and public-safe carrier are actually exposed through the governed delivery path.
- A workflow or badge ≠ approval.

### 13.5 Correction and rollback

Every material public release should define:

- prior release identity;
- correction/withdrawal/supersession trigger;
- affected claims and carriers;
- invalidation plan for APIs, tiles, caches, indexes, exports, stories, and AI context;
- rollback target;
- replay/rebuild verification;
- public correction visibility appropriate to significance.

[Back to top](#top)

---

## 14. Domain Atlas

### 14.1 Canonical-domain determination

**CONFIRMED repository projection / PROPOSED authority status.** The current machine projection contains 13 domain lanes and explicitly excludes `matrix`, `scene`, and `spatial` from domain status. The register itself is `PROPOSED / machine_projection_only`; it cannot create or remove domains. [R-DOMREG]

The registered lanes are: agriculture, archaeology, atmosphere, fauna, flora, geology, habitat, hazards, hydrology, people-dna-land, roads-rail-trade, settlements-infrastructure, and soil. The current domain README confirms substantive lane documentation but explicitly refuses to infer implementation maturity. [R-DOMAINS]

### 14.2 Required domain template

Every lane is documented and reviewed against the same 22 questions:

1. purpose/bounded context; 2. owned concepts; 3. exclusions; 4. current repo implementation; 5. target architecture; 6. entities/value objects/observations/claims/relations; 7. source roles; 8. spatial model; 9. temporal model; 10. identity/versioning; 11. lifecycle/pipeline; 12. evidence/provenance; 13. policy/rights/sensitivity/public-safe transforms; 14. contracts/schemas/fixtures/validators/tests; 15. API/map/UI/export/AI behavior; 16. implemented features; 17. proposed features; 18. anti-collapse rules; 19. operations; 20. maturity; 21. verification backlog; 22. smallest governed next step.

### 14.3 Agriculture

| Field | Result |
|---|---|
| Purpose/ownership | Agricultural observations, statistics, field/county representations and derived indicators. |
| Must not absorb | Soil truth, hydrology measurements, land/title, weather observations, or policy authority. |
| Current implementation | Registered lane and substantive docs are **CONFIRMED**; end-to-end public product is **NEEDS VERIFICATION**. |
| Sources | NASS/CDL and related candidates are design pressure only until source-specific admission/rights/currentness are verified. |
| Spatial/time/identity | Source-native geography and IDs; vintage/observation/release time remain distinct. |
| Lifecycle/evidence | Source capture -> normalized observations -> evidence -> catalog/released derivatives. |
| Sensitivity | Register projects T0, but that is not adopted universal sensitivity policy; private-field/source terms may raise risk. |
| Anti-collapse | Remote-sensing classification ≠ observed management; modeled suitability ≠ measured yield. |
| Smallest next step | One no-network, source-specific observation-to-released-carrier proof slice. |

### 14.4 Archaeology

| Field | Result |
|---|---|
| Purpose/ownership | Archaeological/cultural-heritage assertions, records, research context, controlled public representations. |
| Must not absorb | Tribal/cultural authority, private-land authority, exact sensitive locations as public truth, or reconstruction as observation. |
| Current implementation | Registered lane/substantive docs confirmed; live sensitive source activation/public release not inferred. |
| Sources | Government, tribal, archival and scholarly sources require case-specific authority/rights. |
| Spatial/time/identity | Exact internal geometry may be restricted; generalized/denied public geometry; site IDs must not leak protected identity. |
| Lifecycle/evidence | Admission -> quarantine/review -> restricted evidence -> public-safe derivative after explicit approval. |
| Sensitivity | T4 is projected, not universally adopted policy. Treat exact sites/sacred knowledge as fail-closed. |
| Anti-collapse | Observed site ≠ candidate ≠ inference ≠ reconstruction. |
| Smallest next step | Synthetic-only sensitivity/generalization proof with no real protected coordinates. |

### 14.5 Atmosphere

| Field | Result |
|---|---|
| Purpose/ownership | Weather/air observations, classifications, modeled/forecast products with explicit roles. |
| Must not absorb | Emergency alert or health-directive authority; forecast/model as observation. |
| Current implementation | Registered lane with repository validators/history; live ingestion/deployment unproved. |
| Time | Observed, issued, valid, retrieved and stale times are first-class. |
| Identity | Station/product/model-run identity; model cycles versioned. |
| Evidence | Values tie to source/product/run and exact time scope. |
| Sensitivity | Usually low, but operational-alert posture requires non-authority disclaimer and stale handling. |
| Anti-collapse | Observation ≠ forecast ≠ model ≠ warning. |
| Smallest next step | No-network observation profile with stale/missing-source negative cases. |

### 14.6 Fauna

| Field | Result |
|---|---|
| Purpose/ownership | Taxa, occurrence evidence, ranges and public-safe biodiversity derivatives. |
| Must not absorb | Exact sensitive occurrences as public truth; habitat suitability as occurrence. |
| Current implementation | Registered lane/substantive docs; end-to-end release unproved. |
| Spatial | Exact occurrence may be restricted; public geometry generalized before rendering. |
| Identity | Source-native occurrence/taxon IDs with governed reconciliation. |
| Evidence | Occurrence/range/model support types remain explicit. |
| Sensitivity | T4 projected; rare-species geoprivacy requires fail-closed review. |
| Anti-collapse | Occurrence ≠ range ≠ habitat ≠ modeled suitability. |
| Smallest next step | Synthetic occurrence EvidenceBundle -> generalized carrier -> deny exact-location proof. |

### 14.7 Flora

| Field | Result |
|---|---|
| Purpose/ownership | Plant taxonomy, specimen/occurrence evidence, phenology and invasive/rare-plant context. |
| Must not absorb | Rare exact locations as public truth; modeled habitat as specimen evidence. |
| Current implementation | Registered lane/substantive docs; operational public product unproved. |
| Source/spatial | Herbaria/agency/community sources require role/rights; rare coordinates can be generalized/denied. |
| Time/identity | Collection/observation/publication/retrieval/correction; specimen/taxon/source IDs. |
| Sensitivity | T4 projected; rarity may require stricter release. |
| Anti-collapse | Specimen ≠ occurrence ≠ inferred range ≠ suitability. |
| Smallest next step | Synthetic specimen/occurrence packet with generalization and abstention. |

### 14.8 Geology

| Field | Result |
|---|---|
| Purpose/ownership | Bedrock/surficial geology, stratigraphy, structures, subsurface references and resource context. |
| Must not absorb | Hydrology measurement truth, regulatory/lease status as physical geology, estimate as observed deposit. |
| Current implementation | Registered lane/substantive docs; live public geology product not proved. |
| Source role | KGS/USGS/regulatory/legacy sources remain distinct; caveats/scale retained. |
| Spatial/time | Map scale/vintage essential; borehole/resource precision can require controls. |
| Anti-collapse | Observed ≠ interpreted ≠ modeled; occurrence ≠ deposit ≠ estimate ≠ production/regulatory status. |
| Smallest next step | One public geologic-map fixture slice with source scale/evidence visible. |

### 14.9 Habitat

| Field | Result |
|---|---|
| Purpose/ownership | Habitat classes/patches, connectivity, restoration context and modeled suitability when labeled. |
| Must not absorb | Species occurrence, ownership, or remote-sensing classification as unquestioned ground truth. |
| Current implementation | Registered lane and habitat validation/design work; public product unproved. |
| Source/spatial/time | Land-cover/ecology sources retain method/scale; classification/model vintage visible. |
| Sensitivity | T0 projected, but joins to T4 biodiversity can create derived sensitivity. |
| Anti-collapse | Habitat ≠ occurrence ≠ modeled suitability; land cover ≠ habitat without accepted mapping. |
| Smallest next step | Classification EvidenceBundle -> layer manifest -> Explorer fixture proof. |

### 14.10 Hazards

| Field | Result |
|---|---|
| Purpose/ownership | Hazard observations/events/classifications/context and public-safety posture. |
| Must not absorb | Emergency warning authority or guaranteed current status. |
| Current implementation | `make hazards-validate` is a bounded synthetic USDM materiality surface; no operational hazard product is proved. |
| Time | Issue/valid/expiry/observation/retrieval/rescission/correction all matter. |
| Evidence | Official source snapshot and time scope; missing rows cannot imply “clear”. |
| Anti-collapse | Advisory ≠ observation ≠ forecast ≠ impact model; KFM ≠ alert authority. |
| Smallest next step | Official-source fixture profile with update/rescind/false-clear negatives. |

### 14.11 Hydrology

| Field | Result |
|---|---|
| Purpose/ownership | Hydrologic units, waterways, gauges/observations and watershed relations. |
| Must not absorb | Water rights/title, warnings or model outputs as measurements. |
| Current implementation | Rich docs/contracts/fixtures lineage; `make proof-slice` remains a readiness stub, so no current end-to-end proof is claimed. |
| Identity | HUC/native station/reach IDs and governed crosswalks. |
| Evidence | Observations and unit context close through EvidenceBundle. |
| Anti-collapse | Gauge observation ≠ modeled flow ≠ watershed classification ≠ warning. |
| Smallest next step | Implement the currently stubbed no-network HUC/gauge evidence-to-layer proof with release-denial negatives. |

### 14.12 People, DNA & Land

| Field | Result |
|---|---|
| Purpose/ownership | Evidence-backed assertions about people/genealogy/historical records/land relations under privacy/consent controls. |
| Must not absorb | Living-person dossiering, inferred kinship as fact, DNA exposure, title/legal authority. |
| Current implementation | Registered lane/substantive docs/policy/schema surfaces; no real person/genomic public release claimed. |
| Model | Assertion-first; conflicting assertions can coexist until resolved. |
| Spatial/identity | Public IDs/geometry must not enable re-identification or private-location reconstruction. |
| Sensitivity | T4 projected; living-person, genomic and private-land concerns fail closed. |
| Anti-collapse | Assertion ≠ fact; biological ≠ legal relationship; land record ≠ definitive title; DNA inference ≠ identity. |
| Smallest next step | Synthetic assertions only until qualified privacy/legal/domain authority and consent/revocation/correction rules exist. |

### 14.13 Roads, Rail & Trade

| Field | Result |
|---|---|
| Purpose/ownership | Modern/historic routes, depots/crossings, network and trade context. |
| Must not absorb | Sensitive infrastructure operations; historic route as current passability. |
| Current implementation | Registered lane/substantive docs; live routing/public network service unproved. |
| Time/identity | Historic/current validity and route/segment/facility IDs. |
| Evidence | Feature source/vintage visible; network/accessibility inference is derivative. |
| Anti-collapse | Historic ≠ current; designation ≠ physical passability; modeled accessibility ≠ observed travel. |
| Smallest next step | Fixture-first historic/current route parity plus public-safe map carrier. |

### 14.14 Settlements & Infrastructure

| Field | Result |
|---|---|
| Purpose/ownership | Settlements/places, public service areas and public-safe infrastructure context. |
| Must not absorb | Critical operational details, private utility data, guaranteed current service state. |
| Current implementation | Registered lane/substantive docs; end-to-end public infrastructure product unproved. |
| Spatial | Place/service geometry; harmful precision transformed before public release. |
| Sensitivity | T0 projected, but critical-infrastructure detail can require restriction. |
| Anti-collapse | Physical asset ≠ service status ≠ administrative jurisdiction ≠ modeled access. |
| Smallest next step | Public settlement/service-area fixture slice with exact-infrastructure deny tests. |

### 14.15 Soil

| Field | Result |
|---|---|
| Purpose/ownership | Soil survey/map units, horizons/properties, interpretations, station moisture and gridded/satellite support as distinct roles. |
| Must not absorb | Static survey, station reading, grid derivative and satellite estimate into one authority. |
| Current implementation | Registered/substantive soil lane; attached soil report is proposal-era and cannot prove current implementation. |
| Source role | SSURGO/SDA/gSSURGO, stations and satellite products require separate SourceDescriptors/support types. |
| Spatial/time | Map polygons/grids/stations/profiles; survey version vs observation/retrieval/interpretation time. |
| Evidence | Support type/source role/quality/limitations remain explicit. |
| Anti-collapse | Static survey ≠ station measurement ≠ gridded derivative ≠ satellite retrieval. |
| Smallest next step | One SSURGO/SDA public-safe fixture plus station record with anti-collapse tests. |

### 14.16 Cross-cutting lanes that are not currently registered domains

| Capability family | Current status | Treatment |
|---|---|---|
| Spatial foundation / geography / cartography / time | `CONFIRMED cross-cutting need / NOT REGISTERED AS DOMAIN` | Shared kernel/representation discipline; do not create a root/domain without accepted decision. |
| Frontier Matrix / demography / economy / access | `PROPOSED / PARTIAL cross-domain analytical product` | Versioned definitions/observations compose several domains; `matrix` is explicitly excluded from domain registry. |
| Planetary / 3D / digital twin / synthetic | `PROPOSED / CONFLICTED cross-cutting surface` | Current corpus contains 3D architecture; current register excludes `scene`; keep as governed representation. |
| Remote sensing / field capture | `CROSS-CUTTING` | Capture/analysis across domains; source role/evidentiary humility required. |
| Briefing-to-System integration | `PROPOSED cross-cutting control-plane capability` | Generated briefing prose is discovery input, not evidence/release authority. |
| Focus Modes | `CROSS-CUTTING compositional proof slice` | Area/scope composition across responsibility roots, not domain/root. |

[Back to top](#top)

---

## 15. Cross-Domain Relations and Anti-Collapse Rules

Shared trust objects—identity, source, evidence, policy, receipts, release, correction, runtime envelopes—remain shared by responsibility, while domain semantics remain domain-owned.

| Relation | Owning meaning | Cross-domain rule |
|---|---|---|
| source supports claim | Evidence/source | Other domains may cite after evidence resolution. |
| soil parent material relates geology | Soil/geology seam | Link without making soil a geology authority. |
| habitat supports fauna context | Habitat/fauna seam | Never infer occurrence from habitat alone. |
| hydrostratigraphy informs hydrology | Geology/hydrology seam | Context cannot overwrite measured hydrology. |
| infrastructure intersects hazards | Infrastructure/hazards seam | Exposure model is not event observation. |
| land/ownership relates people/place | People-DNA-land seam | Bounded record is not definitive legal title without proper authority. |
| remote sensing classifies land/habitat/agriculture | Capture/analysis seam | Keep method/model/uncertainty visible. |

**Anti-collapse language:** observed ≠ interpreted ≠ modeled ≠ synthetic; current ≠ historical; physical reality ≠ administrative/legal status; exact ≠ generalized; authoritative ≠ aggregator/contextual; canonical evidence ≠ derivative carrier; 2D/2.5D/3D ≠ reality; confidence ≠ authority.

[Back to top](#top)

---

## 16. Applications, Packages, Services, and Workers

| Surface | Purpose/audience | Entry/technology | Trust boundary | Build/test | Maturity |
|---|---|---|---|---|---|
| Governed API | Public/internal finite response membrane | Python WSGI | No renderer/model imports; public application boundary | `make governed-api-smoke`, `make governed-api-verify` | `IMPLEMENTED_WITH_LIMITATIONS` |
| Explorer Web | Map-first/UI proof shell | Vite + TypeScript; Node 22.13.x; pnpm | Must not read internal stores directly | Explorer build, Vitest, Playwright | `PARTIAL / FIXTURE_ONLY` |
| CLI | Operator surface target | Python-package skeleton/readmes | Restricted; never public release shortcut | implementation commands unestablished | `DRAFT / PARTIAL` |
| Review console | Reviewer surface | path present | restricted | not inspected | `NEEDS VERIFICATION` |
| Admin | Admin surface | path present | not normal public path | not inspected | `NEEDS VERIFICATION` |
| Workers | Background work | path present | watcher/worker non-publisher | not inspected | `NEEDS VERIFICATION` |

Root JavaScript workspace includes `apps/*` and `packages/*`. Reusable non-deployable behavior belongs in `packages/`; deployable boundaries remain under `apps/`.

[Back to top](#top)

---

## 17. API and CLI Reference

### 17.1 Verified Governed API routes

At the base SHA, the WSGI app accepts GET for registered routes, returns 405 finite error envelopes for other methods on registered paths, and 404 finite error envelopes for unknown paths. [R-GAPI-MAIN] [R-GAPI-REG]

| Method | Route | Current result | Maturity |
|---|---|---|---|
| GET | `/bootstrap` | finite `ABSTAIN` scaffold | `IMPLEMENTED_WITH_LIMITATIONS` |
| GET | `/layers` | finite `ABSTAIN` scaffold | `IMPLEMENTED_WITH_LIMITATIONS` |
| GET | `/evidence` | finite `ABSTAIN` scaffold | `IMPLEMENTED_WITH_LIMITATIONS` |
| non-GET | registered route | HTTP 405 + finite error envelope | implemented scaffold |
| GET/other | unknown route | HTTP 404 + finite error envelope | implemented scaffold |

**Do not invent:** authentication, authorization, pagination, spatial/temporal query grammar, rate limits, CORS, cache policy, version prefixes, production hostnames, SLAs, or real EvidenceBundle transport. Local source defaults to `127.0.0.1:8000`, which is not deployment evidence.

### 17.2 CLI

CLI documentation describes intended command families, but runnable commands/entrypoints were not established. Use the repository `Makefile` as the current verified operator command definition surface.

[Back to top](#top)

---

## 18. MapLibre, Maps, Tiles, and Governed UI

MapLibre is a **downstream renderer and interaction runtime**, never evidence/policy/release/citation authority. Explorer documentation remains fixture-first and explicitly does not prove a production live map. [R-EXPLORER]

### Current partial surfaces

- Vite/TypeScript Explorer shell.
- Bounded projections and trust-state components.
- Evidence Drawer-oriented parsing/component tests.
- Synthetic MapLibre/PMTiles proof slices.
- Map performance/governance/proof commands in the Makefile.
- Vitest/Playwright build and browser tooling.

### Target governed flow

```text
released layer/manifest
 -> renderer
 -> selected feature candidate
 -> governed API lookup
 -> EvidenceRef / EvidenceBundle
 -> policy/release/correction state
 -> Evidence Drawer
 -> optional bounded Focus Mode AI
 -> export/story with release/citation context
```

### Trust-visible states

UI should represent `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, stale/expired, corrected/superseded/withdrawn, generalized/redacted, source-role/evidence availability and release state. Sensitive geometry must be transformed before delivery, not hidden client-side.

### 2D/3D

The corpus contains historical dual-renderer language and a later proposal for MapLibre-only 3D. No accepted renderer ADR was verified. Current safe rule: 3D is conditional representation; preserve evidence parity, public-safety transforms and Reality Boundary semantics.

[Back to top](#top)

---

## 19. Governed AI

AI may summarize resolved evidence, explain released claims, propose searches/map actions, draft work, classify candidates and emit AI-work receipts. It may **not** substitute for evidence; decide rights/sensitivity/consent/release; expose direct public model access; reconstruct denied sensitive detail; or self-publish.

### Preferred runtime sequence

```text
scope request
 -> resolve release/public context
 -> retrieve EvidenceRefs
 -> resolve EvidenceBundle
 -> policy/sensitivity pre-check
 -> bounded context
 -> model adapter
 -> citation/claim validation + post-check
 -> RuntimeResponseEnvelope
 -> ANSWER | ABSTAIN | DENY | ERROR
 -> AIReceipt / permitted audit record
```

Provider-neutral runtime lanes, finite envelopes, AIReceipt shapes and mocks exist. Production provider execution, accepted prompt authority, complete citation resolver/policy consumption and a deployed AI endpoint are not established. Private chain-of-thought is not an auditable proof object.

Evaluation should cover finite outcome, evidence/citations, source-role fidelity, place/time scope, prompt injection, sensitive-data leakage, correction awareness and safe map-action proposals.

[Back to top](#top)

---

## 20. Feature and Capability Catalog

| Feature | Audience | Status | Current evidence | Input -> output | Limitation / next step |
|---|---|---|---|---|---|
| Directory governance | maintainers | `IMPLEMENTED_WITH_LIMITATIONS` | ADR-0029, Directory Rules, root registry | path metadata -> finite placement | migration debt remains |
| Root registry | tooling | `IMPLEMENTED` as projection | R-ROOTREG | doctrine -> machine projection | not authority itself |
| Domain register | domain/tooling | `PARTIAL / PROPOSED` | R-DOMREG | current lane identities -> projection | stewards/sensitivity unratified |
| Contracts | engineers | `PARTIAL` | R-CONTRACTS | semantics -> implementation promises | mixed maturity |
| Schemas | engineers/validators | `PARTIAL` | R-SCHEMAS | JSON -> validity | compatibility debt |
| Validator orchestrator | maintainers | `IMPLEMENTED_WITH_LIMITATIONS` | R-MAKE | validator profiles -> finite results | base CI currently blocked by inherited test |
| Workflow-security ratchet | security/CI | `IMPLEMENTED_WITH_LIMITATIONS` | R-MAKE | workflow files -> findings | required-check coupling unverified |
| Topology ratchet | governance/CI | `IMPLEMENTED_WITH_LIMITATIONS` | R-MAKE/ADR29 | tree -> findings | inherited baseline remains |
| GENERATED_RECEIPT | AI governance | `IMPLEMENTED_WITH_LIMITATIONS` | R-GENREC/schema | artifact bytes -> provenance receipt | receipt cannot authenticate review |
| Governed API | API users | `IMPLEMENTED_WITH_LIMITATIONS` | R-GAPI-MAIN/REG | request -> finite scaffold envelope | no real resource service |
| Explorer Web | UI | `PARTIAL / FIXTURE_ONLY` | R-EXPLORER | fixtures/projections -> browser UI | no established production live map |
| Evidence Drawer | UI/evidence | `PARTIAL / FIXTURE_ONLY` | Explorer docs/tests | evidence projection -> drawer | live governed transport unproved |
| Focus Mode | UI/AI | `PROPOSED / PARTIAL` | corpus/repo lanes | scope+evidence -> bounded view | route/production integration unproved |
| MapLibre performance/proof | map QA | `PARTIAL` | R-MAKE | browser/map test -> artifacts/proof | no public-release proof |
| Evidence resolver | evidence | `PARTIAL / FIXTURE_ONLY` | R-MAKE | fixtures -> validation | live store/resolution unproved |
| Promotion gates | release | `FIXTURE_ONLY` | R-MAKE/R-RELEASE | synthetic candidate -> gate result | no authenticated transition |
| ReleaseManifest/RollbackCard | release | `FIXTURE_ONLY / PROPOSED_INACTIVE` | R-RELEASE | fixtures -> records | no production application |
| Rego release profile | policy | `FIXTURE_ONLY / PROPOSED_INACTIVE` | R-POLICY | bounded input -> allow/deny/reasons | no general evaluator |
| Hazards materiality | domain | `IMPLEMENTED_WITH_LIMITATIONS` | R-MAKE | synthetic USDM -> validation | no live/public alert authority |
| Watchers/material change | source ops | `PARTIAL / MIXED` | tools/connectors/corpus | source state -> candidate/receipt | per-source admission required |
| Catalog/STAC/DCAT/PROV | data/catalog | `PARTIAL / NEEDS VERIFICATION` | repo + standards | governed data/release -> projection | KFM profile authority unresolved |
| Public publication | public | `UNKNOWN / HOLD` | no deployment evidence | release -> public carrier | do not claim production readiness |
| Full governed AI | public/research | `PARTIAL / UNKNOWN execution` | runtime contracts/docs | evidence/context -> finite answer | no deployed endpoint proved |

[Back to top](#top)

---

## 21. Security, Privacy, Rights, and Sensitivity

KFM's primary security boundary is the **trust membrane** from untrusted/source/internal material to released public-safe outputs. Security includes identity/access, source rights, harmful precision, integrity, workflow safety, supply chain, AI exfiltration, correction and rollback.

| Threat/control | Current evidence | Gap / target |
|---|---|---|
| Authentication | not established for public runtime | define only for real protected route |
| Authorization | policy root/profiles | accepted evaluator + runtime binding |
| Least privilege | workflow-security ratchet/read-only patterns | verify deployed identities and branch/ruleset permissions |
| Secrets | security guidance prohibits repo secrets | secret-store/deployment integration not inspected |
| TLS/network | infra responsibility exists | actual DNS/TLS/proxy/VPN unverified |
| CORS/CSP | not verified | configure/test at deployed boundaries |
| Input validation | schemas/contracts/boundary guards | extend per live route/source |
| XSS/output encoding | browser framework/tests exist | verify all source/user rendered content |
| CSRF | no authenticated mutation route proved | reassess when state-changing endpoints exist |
| SSRF | connector risk surface | source allowlists, URL validation, egress control |
| SQL injection | deployed DB-backed query not established | parameterized query layer when introduced |
| Path traversal | tools/source-processing risk | canonical path validation and negative tests |
| Unsafe deserialization | JSON/YAML ingestion risk | safe parsers, closed schemas, size/depth budgets |
| Supply chain | locks/ratchets/checksum-pinned bounded OPA profile | verify all actions/images/packages; SBOM/attestation where adopted |
| GitHub Actions | workflow-security validation exists | required settings inaccessible in this run |
| Logging/audit | receipts/audit doctrine | production redaction/retention unverified |
| Rate limiting/DoS | parser/validator budgets, perf tooling | endpoint/runtime capacity and abuse control unverified |
| AI prompt injection/exfiltration | untrusted-content/evidence-first doctrine | runtime enforcement/evals incomplete |
| Tile/map leakage | pre-render transform doctrine | prove public-artifact/server-side enforcement |
| Sensitive errors | denial reasons must not leak protected facts | outward reason-code tests needed |

Fail closed for unresolved living-person data, DNA/genomics, rare species/plants, archaeology/sacred sites, critical infrastructure, private wells/private-land joins, title/ownership assertions and source-restricted archives. Use synthetic fixtures in public CI. Client-only filtering is not a security boundary.

Current external references: NIST SSDF SP 800-218 v1.1, NIST AI RMF 1.0 / GenAI Profile, OWASP API Security Top 10 2023. They are references, not KFM adoption decisions.

[Back to top](#top)

---

## 22. Governance and Decision Rights

### Authority hierarchy

1. platform/safety and current explicit project task authority;
2. accepted KFM decisions/ADRs;
3. adopted Directory Rules for placement;
4. contracts for meaning, schemas for shape, policy for admissibility;
5. current implementation/test/runtime evidence for current behavior;
6. root/lane READMEs as guidance;
7. Drive/attached proposals and lineage;
8. primary external references for non-KFM technical facts;
9. memory never counts as evidence.

ADR-0029 is the verified accepted numbered ADR for Directory Rules v2. Other numbered ADRs remain proposed unless their own current evidence establishes acceptance. CODEOWNERS routes to `@bartytime4life`; it does not prove independent review or separation of duties.

| Operation | Required authority |
|---|---|
| normal docs | docs ownership + evidence |
| root/placement change | Directory Rules + ADR process |
| object meaning | contract review + dependency impact |
| machine shape | schema compatibility/migration review |
| admissibility | policy + source/evidence/sensitivity context |
| source activation | source rights/currentness/sensitivity + activation authority |
| promotion/release | evidence + policy + validation + authorized review + release decision |
| correction/withdrawal | correction authority + release/evidence lineage |
| rollback | authorized release/ops decision + rollback target |
| deployment | environment/ops authority; separate from release/publication |
| publication | release/public-delivery authority |
| adopt this document | explicit governance decision naming path and scope |

[Back to top](#top)

---

## 23. Developer Build, Installation, and Contribution Guide

### Prerequisites

| Requirement | Current declaration | Status |
|---|---|---|
| Python | `>=3.11` | source verified |
| Node | `>=22.13 <23` | source verified |
| pnpm | `11.17.0` | source verified |
| Git | contribution workflow | source verified |
| Network | default tests should prefer fixtures/no network | doctrine/current patterns |

The execution container could not clone GitHub because DNS resolution failed, so local commands were not falsely labeled executed.

### Current repository-native commands

| Command | Purpose / classification |
|---|---|
| `make validate` | aggregate schemas + schema/contract tests; source-defined |
| `make schemas` | compatibility aggregate validator runner |
| `make test` | `pytest tests/schemas tests/contracts -q` |
| `make validator-list` / `validator-full` / `validator-focused` | registry profiles |
| `make validator-registry-check` | validate validator registry |
| `make workflow-security` | workflow-security ratchet |
| `make repository-topology` | topology ratchet |
| `make repository-guardrails` | aggregate registry/workflow/topology |
| `make hazards-validate` | bounded synthetic hazards materiality |
| `make governed-api-dev` | start local API; not executed here |
| `make governed-api-smoke` / `governed-api-verify` | API tests/boundary import guard |
| `make boundary-guards` / `deny-test` | trust-boundary negatives |
| `make ui-build` | Explorer build |
| `make maplibre-perf` / `maplibre-govern` / `maplibre-proof` | map performance/governance/proof |
| `make publish-check` | fixture-first review/promotion-gate checks; no release effect |
| `make release-dry-run` | current Makefile invokes dry-run script + unittest; source-defined, not executed here |
| `make evidence-resolver` / `evidence-resolver-deny` | fixture evidence profiles |
| `make policy` | readiness stub; **not** a working policy evaluator |
| `make fixtures` | readiness stub; **not** a fixture generator claim |
| `make proof-slice` | readiness stub; **not** a hydrology proof |
| `make catalog` | readiness stub; **not** catalog implementation |

### Contribution sequence

Record base SHA; inspect Directory Rules/ADR/root README and overlaps; create a feature branch; implement smallest dependency-closed change; use synthetic fixtures; run changed-area checks; emit GENERATED_RECEIPT for AI-authored work; push/open a **draft PR**; classify inherited vs introduced failures; do not merge/release/deploy/publish from the implementation task.

[Back to top](#top)

---

## 24. Pipeline and Data Engineering Guide

Pipeline specs declare graphs/inputs/outputs; pipelines transform lifecycle material; connectors fetch/admit sources; validators prove bounded conformance; release decisions remain separate.

```text
source candidate
 -> admit/hold/deny
 -> capture
 -> normalize
 -> identify/crosswalk
 -> temporalize
 -> validate geometry and semantics
 -> bind evidence
 -> apply policy/sensitivity
 -> processed artifact + receipts
 -> catalog/triplet projection
 -> proof/release candidate
 -> review/promote
 -> released carrier
 -> public-boundary validation
```

A governed query-save-recompile loop may retrieve evidence, save candidate deltas/validation results, compile derivatives, request review, and recompile after authorized promotion. Automation may propose; it cannot self-promote.

Requirements: idempotency, deterministic identity, source-native IDs, explicit versions, no-network default tests, parser budgets, quarantine, geometry/CRS/time checks, source roles, evidence closure, finite reason codes, replay/rebuild and correction/reprocessing.

[Back to top](#top)

---

## 25. Testing, Validation, and Quality Assurance

| Concern | Current evidence | Mature proof needed |
|---|---|---|
| schemas/contracts | schema tree, aggregate runners/tests | complete valid/invalid fixtures and compatibility |
| source admission | mixed source/connector validators | per-source rights/currentness/identity negatives |
| identity/time | object/domain validators | replay/collision/stale/correction/bitemporal cases |
| geometry | geospatial/domain validators | CRS/datum/invalid/scale/generalization cases |
| evidence | resolver + fail-closed canary | live/released resolver and citation negatives |
| policy | bounded Rego/profile tests | accepted evaluator/runtime binding |
| catalog | partial tools/docs | STAC/DCAT/PROV closure + correction parity |
| release | fixture profiles | real candidate assembly + authenticated review |
| promotion | A–G fixture tests | operational transition + rollback negatives |
| security | workflow/topology/boundary/deny tests | deployed threat-control evidence |
| MapLibre | build/perf/proof tools | released-layer parity + accessibility/perf budgets |
| AI | contracts/mocks/envelopes | citations/policy/prompt-injection/sensitive/correction evals |
| rollback | shapes/fixtures | executed drill + cache/index/API parity |
| docs | meta/link/path workflows | same-revision citation/link/anchor checks |

Exact-main `validator-suite` is **red** at guardrail attribution; downstream checks in that run were skipped. Draft PR #2937 owns the focused repair. This documentation change must not hide that baseline.

Changed-area documentation validation should include UTF-8/Markdown structure, heading hierarchy, duplicate headings, anchors/internal links, repo paths, source citations, no unresolved placeholders, no sensitive data, no current-state claims supported only by plans, no public internal/model path, and generated-receipt validation.

[Back to top](#top)

---

## 26. CI/CD, Repository Controls, Release, and Deployment

Workflow presence is not required-check or production evidence. Exact-main validator-suite shows fail-closed canary PASS and validator job FAIL at attribution. Branch-protection details were inaccessible (`403`) and remain `NEEDS VERIFICATION`.

Design rules: least privilege; stable check names; no persisted credentials for untrusted checkout where avoidable; no secret use on untrusted forks; dependency/action/image pinning; no masking governing failures; explicit network use; generated-artifact authority boundaries; workflows orchestrate validators but do not become policy/release authority.

### State separation

1. CI validates candidate code/artifacts.
2. Repository review authorizes a code/doc change.
3. KFM promotion/release authorizes a governed product/data release.
4. Deployment places software/carriers in an environment.
5. Publication exposes a governed release to its intended audience.
6. Correction/rollback reverses public state independently of Git history.

No evidence in this build supports calling KFM fully production-deployed or fully published.

[Back to top](#top)

---

## 27. Runtime, Infrastructure, and Operations

`runtime/` is canonical internal composition; `infra/` owns deployment/network/exposure implementation. Production deployment was not inspected.

| Concern | Current evidence | Required mature state |
|---|---|---|
| containers/orchestration | repo infra/config present but not inspected deeply | versioned images, health, least privilege, reproducible deploy |
| databases/spatial DB | corpus proposes roles; deployed DB unverified | migrations/backups/read-write roles/spatial health |
| object storage | logical-vs-physical doctrine | versioning/retention/integrity/restore |
| graph/search | derived projections discussed | rebuildable/correction-aware |
| tile serving | map tooling exists | range/cache correctness + manifest closure |
| proxy/network | infra responsibility | TLS/headers/ingress-egress/rate limits |
| secrets | guidance exists | approved secret store/rotation/incident handling |
| backups/DR | unverified | RPO/RTO + restore drills |
| logs | receipts/audit doctrine | structured/redacted retention/correlation/access |
| metrics/traces | perf/workflow metrics | service/source/release health dashboards |
| source health | watcher concepts | stale propagation and steward workflow |
| cache invalidation | first-class doctrine | corrections invalidate tiles/API/search/AI caches |
| incident response | security + runbook docs with drift | one approved command surface + synthetic drill |
| rollback | release fixtures | executed drill + public parity |

KFM operational incident response is not a public emergency service. Public docs must not expose sensitive security details.

[Back to top](#top)

---

## 28. User and Operator Guides

**Current-state warning:** repository evidence proves a fixture-first Explorer, not a deployed production public map. Public procedures below are **target experience** unless a deployed endpoint is separately verified.

### Public user

Choose a released layer/Focus Mode; set supported place/time; select a feature; inspect Evidence Drawer source/evidence/scope/release/correction; treat ABSTAIN/DENY/stale/generalized/corrected states as meaningful; use Focus Mode only for bounded evidence-backed interpretation; export only with release/citation context; use a verified correction channel when one exists.

### Researcher/analyst

Resolve source role; record release/version/time/geography; preserve uncertainty/scale; use released APIs/exports instead of internal stores; cite source/evidence and KFM release when available; never reverse-engineer exact sensitive locations from generalized outputs.

### Reviewer/steward

Confirm identity/source role/rights/currentness; resolve EvidenceRefs; inspect validation; apply sensitivity/policy; review public-safe transforms; check proof/manifest/correction/rollback; approve/hold/deny via authorized mechanism; keep protected reasons internal.

### Developer

Follow §23/CONTRIBUTING; use existing roots; pair meaning/shape/fixtures/tests only as needed; no-network fixtures; governed API/released projections for public features; generated receipts for AI work; draft PR default.

### Operator

Verify deployed revision/config; check health/freshness/release/correction; never use merge as deployment/publication truth; fail safely; use approved rollback; verify post-rollback API/map/cache/index parity.

### Security/policy reviewer

Review exposure/harmful precision/source rights; verify transform before render; confirm no direct internal/model path; inspect secrets/logging/errors; validate correction/incident escalation.

[Back to top](#top)

---

## 29. Accessibility, Performance, Reliability, and Compatibility

Accessibility targets: keyboard operation, visible/restored focus, screen-reader landmarks/names, non-color trust states, contrast, reduced motion, text equivalents, accessible tables/diagrams, programmatic error/deny/abstain announcements. Complete conformance is `NEEDS VERIFICATION`.

Map performance tooling exists. Performance claims must bind exact build, browser/device, artifact versions, scenario, budgets, thresholds and proof/receipt. A fast unsafe/uncited map is failure.

Reliability: bounded retries, idempotent intake, visible stale state, no false-clear on outage, rebuildable derivatives, finite partial failures, correction-aware caches, deterministic negatives.

Compatibility roots/aliases must remain mirror/frozen with canonical targets; breaking contract/schema/API changes need migration, compatibility tests and rollback.

[Back to top](#top)

---

## 30. Current Gaps, Roadmap, and Dependency Order

| ID | Priority | Gap | Smallest sound next step | Acceptance / rollback |
|---|---|---|---|---|
| RM-P0-001 | P0 | exact-main validator-suite failure; #2937 owns repair | finish focused repair without workflow semantic change | hosted exact-head progresses past attribution; revert repair |
| RM-P0-002 | P0 | required checks/branch protection inaccessible | evidence-only settings reconciliation | current ruleset/check list; no settings mutation in this PR |
| RM-P0-003 | P0 | general policy evaluator/runtime binding unproved | one bounded accepted operation profile + adapter | deterministic positives/negatives; disable profile |
| RM-P0-004 | P0 | operational release/review/rollback held | one synthetic authenticated release dry run without publication | decisions/manifests/rollback/correction; reset synthetic state |
| RM-P0-005 | P0 | sensitive reviewer/source-rights authority unresolved | ratify roles/admission requirements before T4 live data | deny unknown rights; revoke/hold activation |
| RM-P1-001 | P1 | whole-system docs fragmented | review/adopt this same-path synthesis | accepted decision/source ledger; revert adoption/doc |
| RM-P1-002 | P1 | Governed API remains scaffold | implement one read-only released fixture resource family | finite contract/schema/tests; remove route/adapter |
| RM-P1-003 | P1 | Explorer lacks established governed transport | connect RM-P1-002 to one Evidence Drawer flow | browser tests/no internal paths; restore fixture adapter |
| RM-P1-004 | P1 | hydrology proof-slice target is stub | implement one no-network hydrology proof slice | actual proof artifact + release negatives; revert slice |
| RM-P1-005 | P1 | object-family registry partial | expand only from verified current families | registry validator/tests; revert entries |
| RM-P2-001 | P2 | catalog profile convergence partial | decide/validate KFM STAC/DCAT/PROV mapping | metadata parity/correction; regenerate prior profile |
| RM-P2-002 | P2 | uneven domain maturity | graduate one proof slice per lane | source->evidence->policy->carrier; withdraw slice |
| RM-P2-003 | P2 | observability/deployment unverified | environment inventory + health/log/restore packet | exact revision/endpoints/restore evidence; rollback config |
| RM-P2-004 | P2 | accessibility incomplete | keyboard/screen-reader/negative-state tests | explicit browser assertions; revert fix |
| RM-P3-001 | P3 | 3D breadth | admit only bounded representation use case | evidence parity/Reality Boundary/perf/sensitivity; disable |
| RM-P3-002 | P3 | ML/analytics breadth | method-governed derivative | provenance/uncertainty/reproducibility; remove derivative |
| RM-P3-003 | P3 | broader source ecosystem | add one source at a time | rights/currentness/fixture/non-publisher proof; deactivate |

[Back to top](#top)

---

## 31. Risks, Limitations, Assumptions, and Open Questions

| ID | Status | Risk / question | Next check |
|---|---|---|---|
| RISK-AUTH-001 | `CONFIRMED` | this document is not adopted authority | separate adoption decision |
| RISK-AUTH-002 | `NEEDS VERIFICATION` | only one verified review identity; independent stewardship unproved | assignments/required approvals |
| RISK-DIR-001 | `CONFIRMED` | legacy/compatibility path debt remains | topology ratchet/migrations |
| RISK-SCHEMA-001 | `CONFLICTED / PARTIAL` | schemas root is accepted but subhome ADR remains proposed | decide/document configured subhome |
| RISK-POL-001 | `CONFIRMED gap` | no accepted general evaluator | bounded evaluator proof |
| RISK-REL-001 | `CONFIRMED gap` | fixture release can be mistaken for operational release | synthetic authenticated dry run |
| RISK-SRC-001 | `ONGOING` | candidate source terms/cadence are volatile | per-source official review |
| RISK-SENS-001 | `HIGH` | joins/errors/client filters can leak T4-like detail | server transforms + negative tests + qualified review |
| RISK-OPS-001 | `UNKNOWN` | deployment/backups/observability/DR unverified | environment evidence packet |
| RISK-CI-001 | `CONFIRMED` | exact-main validator-suite red | follow #2937 without bypass |
| RISK-AI-001 | `PARTIAL` | fluent output can outrun evidence/policy | resolver + policy + citations + evals |
| RISK-MAP-001 | `PARTIAL` | renderer data can leak or be mistaken for truth | released public artifact + Drawer parity |
| RISK-DOC-001 | `ONGOING` | large synthesis can become stale | trigger re-verification on material changes |
| RISK-SINGLE-001 | `NEEDS VERIFICATION` | single owner route creates continuity/SoD risk | establish steward roles |
| OPEN-API-001 | `UNKNOWN` | future API auth/version/query grammar | first real resource + threat model |
| OPEN-DEPLOY-001 | `UNKNOWN` | actual deployed environments/services | deployment inspection |
| OPEN-PUBLIC-001 | `UNKNOWN` | has any product completed governed publication? | immutable release + public carrier readback |
| OPEN-PROV-001 | `CONFLICTED` | canonical KFM semantic PROV profile | current ADR/standards convergence |
| OPEN-HASH-001 | `NEEDS VERIFICATION` | object-family hash/canonicalization differs | contract/policy per family |
| OPEN-SENS-001 | `NEEDS VERIFICATION` | T0–T4 projection not universal adopted policy | domain-specific policy ratification |
| OPEN-DOC-001 | `PROPOSED` | who adopts/maintains this synthesis? | owner/review/adoption decision |

[Back to top](#top)

---

## 32. Glossary and Acronyms

| Term | KFM meaning |
|---|---|
| ADR | Architecture Decision Record; only accepted decisions have decision authority. |
| ABSTAIN | Insufficient admissible support to answer/claim. |
| AIReceipt | Model/runtime provenance, not evidence truth. |
| CATALOG | Discoverability/projection stage; not publication by itself. |
| COG | Cloud Optimized GeoTIFF; raster carrier when admitted. |
| CRS | Coordinate Reference System. |
| DCAT | W3C Data Catalog Vocabulary. |
| DENY | Policy/safety outcome prohibiting operation/exposure. |
| EvidenceBundle | Resolved evidence support package. |
| EvidenceRef | Stable evidence pointer requiring resolution. |
| Focus Mode | Cross-cutting area/scope proof/interpretation experience, not domain root. |
| GeoParquet | Columnar geospatial interchange carrier. |
| KFM | Kansas Frontier Matrix. |
| MapLibre | Renderer/runtime downstream of trust. |
| MVT | Vector tile encoding. |
| PMTiles | Single-file tiled archive; delivery carrier. |
| PROV-O | W3C provenance ontology. |
| PromotionDecision | Governed transition decision; shape alone is not authenticated authority. |
| ProofPack | Proof-closure artifact family. |
| QUARANTINE | Held lifecycle state for unresolved quality/rights/sensitivity/policy. |
| RAW | Admitted source capture/locator before normalization. |
| ReleaseManifest | Released-carrier inventory requiring actual release context. |
| RuntimeResponseEnvelope | Finite API/runtime response transport. |
| SSDF | NIST Secure Software Development Framework. |
| STAC | SpatioTemporal Asset Catalog standard family. |
| T0–T4 | Proposed sensitivity-tier vocabulary, not universally adopted by appearance alone. |
| TRIPLET | Graph/relation projection, not sovereign truth. |
| WORK | Candidate normalization/analysis stage, never normal public path. |

[Back to top](#top)

---

## 33. Embedded Appendices

### Appendix A — Source Ledger

#### Repository evidence

This convergence inspected **35 material repository files/trees/runs/PR surfaces**, including: root README/metadata/tree; Directory Rules + accepted ADR-0029 + ADR index; root/domain/object registers; CODEOWNERS/CONTRIBUTING/Makefile/package manifests; contracts/schemas/policy/data/release/runtime/security/domain root docs; Explorer/Governed API/CLI; Governed API route code; generated-receipt lane/schema; exact-main validator-suite run; and draft repair PR #2937.

#### Attached files

The conversation contained **29 attachment entries / 28 unique files**: **25 KFM-specific** and **3 general references** (`AI Concepts Using Python`, `Domain-Driven Design Reference`, `GPT Markdown Prompt 4.0`). Material KFM sources include Soil and Geology architecture reports, MapLibre manual, Pipeline v0.3, Implementation Reference, Encyclopedia, Greenfield Plan, Master MapLibre atlas, Pass 18/20 atlases, consolidated domain atlas, MapLibre 3D proposal, Unified Build Manual, repository structure guides, doctrine syntheses, full-atlas seed cards, Connected-Dots brief, AI Build Contract, Markdown agent, Directory Governance Standard v2, Research/Verification Agenda, Briefing-to-System blueprint, and Living Compass.

**Classification rule:** domain reports/greenfield/pass atlases are LINEAGE/PROPOSED; general books are REFERENCE; the attached Directory Standard supplies exact doctrine bytes but adoption comes from repo ADR-0029; older implementation references cannot prove current main.

#### Google Drive

Multiple broad/focused searches classified **20 high-signal Drive sources; 3 were opened/read in depth**. They include AI Build Contract, Data Intake guide, several Comprehensive System Documentation/master-reference manuals, Improvements/Idea Integration, Documentation Architecture Passes, architecture deepening/consolidation passes, technical blueprints, Implementation Reference variants, Replacement-Grade Master Manual, Connected-Dots brief, Research/Verification Report, Tooling Manual, Foundational Guide, Living Compass, Pass 21–32 atlases and MapLibre master variants. Modified date/title never establishes authority.

#### External primary references (accessed 2026-08-15)

- NIST SP 800-218 SSDF v1.1 — secure development reference.
- NIST AI RMF 1.0 and NIST AI 600-1 GenAI Profile — AI-risk references.
- OWASP API Security Top 10 2023 — API threat reference.
- OGC STAC Community Standard 1.1.0 — spatiotemporal catalog reference.
- W3C DCAT 3 Recommendation (2024-08-22) — catalog vocabulary.
- W3C PROV-O Recommendation — provenance vocabulary.
- MapLibre official docs — renderer technical reference.

### Appendix B — Authority and Supersession Register

| Artifact | Status | Result |
|---|---|---|
| `docs/doctrine/directory-rules.md` | embedded proposed label, exact bytes | **ADOPTED BY ADR-0029**; writable Directory Rules authority |
| `docs/architecture/directory-rules.md` | legacy compatibility | read-only; retirement is separate migration |
| ADR-0029 | accepted | placement/doctrine adoption authority |
| other numbered ADRs | proposed unless individually proved otherwise | do not upgrade through synthesis |
| this whole-system file | **PROPOSED FOR ADOPTION** | candidate human-readable synthesis only |
| Drive “master/final/comprehensive” manuals | lineage/reference | titles do not grant authority |
| domain/pass PDFs | lineage/proposal | design pressure, not implementation |
| technical books | reference | no KFM authority |

### Appendix C — Repository and Responsibility-Root Inventory

Platform: `.github/`. Canonical: `apps/`, `configs/`, `connectors/`, `contracts/`, `control_plane/`, `data/`, `docs/`, `examples/`, `fixtures/`, `infra/`, `migrations/`, `packages/`, `pipeline_specs/`, `pipelines/`, `policy/`, `release/`, `runtime/`, `schemas/`, `scripts/`, `tests/`, `tools/`. Compatibility: `artifacts/`. Deprecated: `catalog/`. Conditional: `src/`. Current presence is not permission for new noncanonical writes.

### Appendix D — Current Capability and Feature Matrix

- Implemented with limitations: Directory governance, root registry, generated receipts, finite Governed API scaffold, selected boundary/validator tooling.
- Partial: Explorer, schemas/contracts, evidence resolver, runtime adapters, domain lanes, MapLibre proof tooling.
- Fixture-only/proposed inactive: release strict profiles, promotion gates, rollback card, selected Rego profile.
- Proposed cross-cutting: BriefingSignal, TemporalAuthorityEnvelope, full Focus Mode, broad 3D/digital twin.
- Unknown/held: production publication, active general policy evaluator, deployed public AI, complete operations/DR.

### Appendix E — Core Object-Family Registry

The §8 crosswalk is a human synthesis, not a replacement machine registry. Before adopting a new family, verify semantic contract, schema, identity, producer/consumer, policy, fixtures/tests, versioning, correction and release impact.

### Appendix F — Contract / Schema / Policy / Fixture / Validator Crosswalk

| Layer | Canonical root | Acceptance evidence |
|---|---|---|
| Meaning | `contracts/` | semantic contract + semantic tests |
| Shape | `schemas/` | Draft 2020-12 schema + valid/invalid fixtures |
| Admissibility | `policy/` | exact input profile + reasons + policy tests |
| Examples | `fixtures/` | synthetic positive/negative/golden |
| Enforcement | `tools/validators/`, `tests/` | deterministic execution + negatives |
| Instances | `data/` | identity/provenance/receipt/policy/release context |
| Release | `release/` | authenticated decision, manifest, correction/rollback refs |

### Appendix G — Domain and Source Matrix

| Domain | Registered | Projected baseline | Key source-role separation |
|---|---:|---:|---|
| Agriculture | yes | T0 | statistics/classification/remote sensing |
| Archaeology | yes | T4 | protected/tribal/archival/research |
| Atmosphere | yes | T0 | observation/model/forecast/advisory |
| Fauna | yes | T4 | occurrence/range/model |
| Flora | yes | T4 | specimen/occurrence/range |
| Geology | yes | T0 | observed/interpreted/modeled/regulatory |
| Habitat | yes | T0 | habitat/classification/suitability |
| Hazards | yes | T0 | event/advisory/model; non-alert authority |
| Hydrology | yes | T0 | unit/observation/model/warning |
| People, DNA & Land | yes | T4 | assertion/evidence/consent/legal-source roles |
| Roads, Rail & Trade | yes | T0 | historic/current/administrative/network |
| Settlements & Infrastructure | yes | T0 | settlement/service/asset/admin |
| Soil | yes | T0 | survey/station/grid/satellite |

These tiers are proposed registry metadata, not adopted universal policy.

### Appendix H — API, CLI, UI, and Application Inventory

Governed API: Python WSGI and three current scaffold GET routes. Explorer: Vite/TypeScript partial fixture-first. CLI: docs/package skeleton, commands unverified. Review/admin/workers: paths present, not inspected in depth. MapLibre: Explorer/tool integration partial. Governed AI: runtime/contracts/mocks partial/execution unverified.

### Appendix I — Workflow, Test, and Required-Check Matrix

| Family | Base status | Required-check status |
|---|---|---|
| validator fail-closed canary | PASS | UNKNOWN |
| validator run-validators | FAIL at attribution | UNKNOWN |
| validator registry/security/topology/aggregate | SKIPPED after earlier failure | UNKNOWN |
| schema/contracts/Explorer/release profiles | not rerun in this doc task | UNKNOWN |

Branch protection could not be read.

### Appendix J — Security Control and Threat Matrix

| Threat | Control posture | Maturity |
|---|---|---|
| public internal-store bypass | governed API + boundary rules | partial |
| direct browser-model | runtime/API separation/import guards | partial |
| sensitive location leak | pre-render transform/generalization | domain-dependent |
| source-role confusion | SourceDescriptor/EvidenceBundle | partial |
| unknown rights | quarantine/deny | per-source verification |
| workflow privilege escalation | least privilege + workflow ratchet | implemented with limitations |
| supply-chain substitution | locks/pins/checksums where adopted | mixed |
| prompt injection | untrusted-content/evidence-policy flow | partial/proposed runtime |
| stale false-clear | finite stale/unknown + source health | partial |
| review spoofing | authenticated review/separation | gap |
| release spoofing | release decision plane/manifests | fixture-only |
| correction/cache drift | invalidation/replay | operational gap |

### Appendix K — Release / Correction / Withdrawal / Rollback Matrix

Candidate->review requires validation/evidence/policy/review. Review->release requires promotion/release decisions, manifest/proof/rollback. Release->publication additionally needs governed public delivery. Correction/withdrawal require new lineage plus invalidation. Rollback requires target, authorization and public parity verification. Current operational maturity is fixture-first/unknown.

### Appendix L — Drift and Contradiction Register

| ID | Conflict | Current bounded resolution |
|---|---|---|
| DRIFT-001 | Directory source label proposed vs accepted ADR | ADR-0029 controls adoption; bytes remain unchanged |
| DRIFT-002 | legacy architecture Directory Rules path | read-only compatibility |
| DRIFT-003 | schema subhome ADR vs configured structure | `schemas/` root accepted; narrower ADR proposed |
| DRIFT-004 | policy canonical vs compatibility paths | singular `policy/` placement accepted; migrate object-by-object |
| DRIFT-005 | top-level `catalog/` vs `data/catalog/` | top-level deprecated/frozen |
| DRIFT-006 | artifacts trust-like historical content | compatibility root cannot become authority |
| DRIFT-007 | triplet naming variants | use accepted data model/migrate with identity parity |
| DRIFT-008 | release README dry-run wording vs current Makefile real invocation | current code wins; doc follow-up required |
| DRIFT-009 | A–F/A–G/expanded promotion vocabularies | current repo proves bounded A–G fixture semantics only |
| DRIFT-010 | dual-renderer vs MapLibre-only 3D proposals | no accepted renderer ADR verified |
| DRIFT-011 | T0–T4 in domain register | projection metadata, not universal adopted policy |
| DRIFT-012 | many Drive master/final manuals | lineage only; this PR converges existing repo path |

### Appendix M — Verification Backlog

VB-001 required checks/rulesets; VB-002 deployments/public endpoints; VB-003 active policy evaluator; VB-004 first actual governed release; VB-005 correction/rollback drill; VB-006 source activation matrix; VB-007 independent stewardship; VB-008 full object-family registry; VB-009 API auth/query/version contract; VB-010 Explorer live transport; VB-011 accessibility; VB-012 production observability/backups/DR; VB-013 provenance profile authority; VB-014 this document's adoption; VB-015 current source rights for first live candidates.

### Appendix N — Verified Command Reference

`make validate`, `schemas`, `test`, validator profiles/registry, workflow-security, repository-topology, governed API, boundary guards, UI build, MapLibre perf/govern/proof, publish-check, release-dry-run, evidence-resolver and hazards validation are **present in current source**. They were not locally executed because clone/DNS failed. The exact-main validator-suite hosted run is separately known to fail at attribution. Readiness stubs (`make policy`, `make fixtures`, `make proof-slice`, `make catalog`) are not implementation evidence.

### Appendix O — Document Changelog and Adoption Checklist

**2026-08-15 convergence draft:** updated the existing same-path Whole-System Build Reference; pinned current main; reconciled ADR-0029; separated truth/maturity; added root/domain/object/app/API/policy/release/runtime/security current evidence; recorded exact-main CI failure and active repair boundary; incorporated Drive/attachments as lineage; added external primary references; preserved non-release/no-wiki boundaries.

Adoption checklist:

- [ ] Human reviewer verifies source ledger/current-state claims.
- [ ] Recheck current main for material drift.
- [ ] Documentation links/anchors/path references pass repository-native checks.
- [ ] No sensitive/internal-only material or harmful precision is exposed.
- [ ] No proposed ADR/design is represented as accepted/implemented.
- [ ] Owner/reviewer roles and stale/review triggers are decided.
- [ ] Supersession relationship to other human master manuals is decided.
- [ ] Generated projections are source-bound and non-authoritative.
- [ ] An accepted ADR or equivalent decision explicitly designates this path as canonical human-readable synthesis.
- [ ] Rollback to pre-adoption revision is recorded.

**Exact adoption step:** accept a governance decision that pins this path and reviewed digest, names its authority as the canonical *human-readable synthesis only*, records owner/review/stale/correction/supersession rules, and explicitly keeps ADRs/contracts/schemas/policy/current implementation/runtime/release evidence higher authority for their respective questions.

[Back to top](#top)
