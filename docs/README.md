<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/2e7a0e0b-5c0a-4cb0-9fd6-7b3f4bbf67b1
title: docs/ — Governed Documentation Hub
type: standard
version: v2
status: draft
owners: KFM Maintainers (resolve via CODEOWNERS)
created: 2026-02-24
updated: 2026-02-28
policy_label: public
related:
  - ../README.md
  - ../.github/README.md
  - ../CONTRIBUTING.md
  - ../SECURITY.md
  - ../configs/README.md
  - ../contracts/README.md
  - ./adr/README.md
  - ./governance/README.md
  - ./runbooks/README.md
  - ./standards/README.md
tags:
  - kfm
  - docs
  - governance
  - evidence-first
  - cite-or-abstain
notes:
  - Upgraded from scaffold to governed doc index aligned to KFM vNext invariants.
  - Aligned language to truth path + trust membrane + EvidenceRef semantics; clarified “repo-root vs deeper paths” verification posture.
  - Added slots for templates + domain docs + quality docs (target structure; fail-closed if referenced by contract).
  - Treat repo-specific structure as UNKNOWN until verified; fail-closed on missing referenced files.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/` — Governed Documentation Hub
**Map-first • time-aware • governed • evidence-first • cite-or-abstain**

This directory is **documentation-as-production** for Kansas Frontier Matrix (KFM). Anything here is expected to be:
- **reviewable** (small diffs, stable IDs, clear owners),
- **testable where applicable** (linkcheck, schema examples, policy fixtures),
- **safe under policy** (default-deny posture; no sensitive leakage),
- **traceable** (claims link back to resolvable evidence or are marked Unknown).

![Status](https://img.shields.io/badge/status-draft-orange)
![Docs](https://img.shields.io/badge/docs-governed-blue)
![Evidence](https://img.shields.io/badge/evidence-required-brightgreen)
![Policy](https://img.shields.io/badge/policy-default--deny-critical)
![MetaBlock](https://img.shields.io/badge/metadata-KFM__META__BLOCK__V2-informational)

> [!IMPORTANT]
> **Trust membrane rule:** docs must never become a bypass.  
> Do not include secrets, restricted coordinates, or “just trust me” claims.  
> If a claim can’t be supported by evidence, **abstain** or mark it **UNKNOWN** with verification steps.

---

## Quick navigation

- [Truth status legend](#truth-status-legend)
- [Directory contract](#directory-contract)
- [Documentation stance](#documentation-stance)
- [Where docs fit in KFM](#where-docs-fit-in-kfm)
- [Repo context](#repo-context)
- [Directory layout](#directory-layout)
- [System map](#system-map)
- [Doc templates](#doc-templates)
- [CI gates for docs](#ci-gates-for-docs)
- [Definition of Done](#definition-of-done)
- [Contribution workflow](#contribution-workflow)
- [Glossary](#glossary)
- [Reference library](#reference-library)

---

## Truth status legend

Use explicit truth labels to keep docs evidence-first and fail-closed:

- **CONFIRMED (repo):** backed by artifacts in this repository (paths, schemas, tests, receipts)
- **CONFIRMED (repo-root snapshot):** backed by a repository inventory snapshot; deeper module paths still require verification
- **CONFIRMED (design):** a KFM invariant/contract (must hold regardless of implementation)
- **PROPOSED:** a recommended template/pattern (adopt only after review)
- **UNKNOWN (repo):** not verified on this branch; include verification steps

> [!NOTE]
> If you reference a file that doesn’t exist, treat that as **missing and merge-blocking** if the reference is required by contract.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Directory contract

### Purpose
`docs/` is the canonical home for:
- architecture and boundary contracts (human-readable)
- governance standards and review workflows
- operational runbooks
- narrative standards (Story Nodes)
- specs and examples that support enforcement (schemas, fixtures, checklists)

### What belongs in `docs/`
- **Architecture docs:** system overview, layering, trust membrane, canonical vs rebuildable
- **Governance docs:** policy labels, obligations, promotion gates, review triggers, roles
- **Runbooks:** incident response, pipeline operations, promotion procedures, rollback
- **Standards:** doc standards, schema/profile standards, catalog profile references
- **Narrative specs:** Story Node spec(s), citation conventions, evidence drawer expectations
- **Templates:** universal doc, story node, and API extension templates (governed + versioned)
- **Quality docs:** checklists, threat model prompts, and validation explainers (human-facing)
- **Evidence artifacts (bounded):** example receipts/manifests, redacted QA reports, validation examples

### What must not go in `docs/`
- **Secrets** (tokens, keys, credentials), even in examples
- **Raw or sensitive data** (default-deny): use redacted samples + digests + EvidenceRefs
- **Large binaries/build outputs** unless explicitly required and size-controlled
- **Unverifiable assertions**: if it can’t be cited, label it **UNKNOWN** and add verification steps
- **Policy enforcement logic** (belongs in `policy/` and runtime services), except for human-facing documentation of policy behavior

> [!WARNING]
> If it would be unsafe to paste into a public issue, it does not belong in public-labeled docs.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Documentation stance

### Truth discipline
Every statement should be treated as one of:
- **Confirmed:** backed by repo artifacts or resolvable evidence
- **Proposed:** a design option with rationale + tradeoffs
- **Unknown:** not verified; must include **minimum verification steps**

> [!IMPORTANT]
> Do not “fill gaps” by inventing repo state. Prefer TODOs, explicit Unknowns, and small verification checklists.

### Safety posture
- **Default-deny** when sensitivity/permissions are unclear.
- If content could enable harm (e.g., vulnerable sites), publish only generalized detail.
- If a doc is governance-sensitive (e.g., security operations, internal escalation), label it `restricted|internal` and ensure review routing via CODEOWNERS.

### Cite-or-abstain applies to docs too
If a document makes factual claims that would influence decisions (policy, security, promotion eligibility), it should:
- cite in-repo artifacts (contracts, receipts, manifests, validators) **or**
- cite governed evidence references (EvidenceRefs) **or**
- mark the claim as **UNKNOWN**.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Where docs fit in KFM

Docs sit alongside the enforceable artifacts and should point to them:

- **Contracts:** `contracts/` defines enforceable interfaces (OpenAPI, schemas, profiles, gates)
- **Policy:** `policy/` defines default-deny rules + obligations + test fixtures (enforced in CI and at runtime)
- **Configs:** `configs/` defines governed configuration inputs (labels, obligations, gate thresholds)
- **Data truth path:** `data/` holds canonical specs/registries/manifests/catalogs/receipts/digests
- **Governance:** `.github/` + `docs/governance/` define merge-time + human review posture
- **Tooling:** `tools/` + `tests/` make rules enforceable (validators, link checkers, fixtures)

> [!NOTE]
> If docs are served via governed APIs, the `policy_label` in the MetaBlock determines who can see the doc.
> If docs are “git-only,” still keep the label—it is a governance signal and can be enforced later.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Repo context

`docs/` is only one surface of the system. To avoid overreach, treat any repo layout claims as **branch/commit-specific**:

- **Do not** assume deep module paths exist just because they’re shown in a target layout.
- Prefer **repo-root inventory** + **minimum verification steps** before writing “CONFIRMED (repo).”

Minimum verification steps (example):
- `ls -1` at repo root (confirm top-level folders)
- `tree -L 2 docs/` (confirm doc subfolders)
- run `linkcheck` / `MetaBlock lint` (confirm docs gates)

> [!TIP]
> If a doc is referenced by a contract, CI workflow, or release checklist, a missing link should be treated as merge-blocking.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Directory layout

> [!NOTE]
> This is a **target structure** aligned to the KFM vNext operating model.  
> If your branch differs, update this README and any linkcheck/validators together.

```text
docs/                                                              # Governed docs hub (production docs; PR-reviewed; linkcheck-clean)
├─ README.md                                                       # Docs hub index + rules + “what goes where” + doc taxonomy + review gates
│
├─ architecture/                                                   # Architecture docs (invariants, decisions, diagrams, contracts)
│  ├─ README.md                                                    # Index + invariants + quick-nav + “start here” reading order (trust membrane + truth path + promotion pointers)
│  ├─ overview/                                                    # High-level architecture narrative (what/why/how)
│  │  ├─ README.md                                                 # How to read the architecture set + link map + glossary pointer + “normative vs informative”
│  │  ├─ system-context.md                                         # C4-ish context: external actors, upstream sources, infra deps, trust boundaries
│  │  ├─ actors-and-trust-surfaces.md                              # Humans/services + UI trust surfaces; “who can touch what” matrix (high-level)
│  │  ├─ layering.md                                               # Clean architecture layering + dependency rules + anti-patterns (no IO in domain)
│  │  ├─ component-decomposition.md                                # Major components (API, apps, pipelines, tools) + responsibilities + interfaces
│  │  ├─ deployment-topology.md                                    # Conceptual deployment: envs, gateways, networks, secrets posture (no credentials)
│  │  ├─ trust-membrane.md                                         # Boundary rules + enforcement points (PEP/PDP, adapters, UI trust components)
│  │  ├─ policy-boundary.md                                        # Policy decision IO (allow/deny/obligations), redaction semantics, audit outputs
│  │  ├─ evidence-and-claims.md                                    # Claim model + EvidenceRef/EvidenceBundle meaning + resolvability/linking rules
│  │  ├─ focus-mode-constraints.md                                 # Cite-or-abstain contract + failure modes + “no evidence → no claim”
│  │  ├─ truth-path.md                                             # Truth path zones (RAW→WORK→QUARANTINE→PROCESSED→CATALOG→PUBLISHED) + invariants
│  │  ├─ promotion-contract.md                                     # Promotion gates (executable contract) + required artifacts + fail behavior
│  │  ├─ provenance-and-audit.md                                   # Run receipts, audit ledger, correlation IDs, provenance graph expectations
│  │  ├─ canonical-vs-rebuildable.md                               # Canonical truth vs rebuildable projections (search/tiles/graph) + rebuild triggers
│  │  ├─ identity-and-hashing.md                                   # Deterministic IDs, spec_hash rules, canonicalization, collision strategy
│  │  ├─ time-model.md                                             # Event/valid/transaction time definitions + required fields + conventions
│  │  ├─ time-queries-and-snapshots.md                             # As-of queries, snapshot semantics, version pinning, UI implications (view_state)
│  │  ├─ security-and-privacy.md                                   # Cross-cutting posture: secrets, least privilege, logging redaction, safe defaults
│  │  ├─ sensitive-locations.md                                    # Sensitive site handling: no precise coords, generalization, obligations, leakage tests
│  │  ├─ observability.md                                          # Logs/metrics/traces conventions + audit correlation + policy-safe dimensions
│  │  └─ glossary.md                                               # Canonical terms (used across docs/contracts/errors; reduces ambiguity)
│  ├─ decisions/                                                   # ADRs (small, reversible, versioned decisions)
│  │  ├─ README.md                                                 # ADR process + statuses + linking rules (code/tests/contracts)
│  │  ├─ adr-0000-template.md                                      # ADR template (copy/paste; ideally includes MetaBlock v2)
│  │  ├─ adr-0001-example.md                                       # Complete example ADR (illustrative)
│  │  ├─ adr-0002-trust-membrane-enforcement.md                    # Decision: where/how invariants are enforced (CI/runtime/UI)
│  │  ├─ adr-0003-policy-engine-integration.md                     # Decision: PDP integration, obligations model, caching posture
│  │  ├─ adr-0004-evidence-resolution.md                           # Decision: evidence resolver contract, redaction guarantees, errors
│  │  ├─ adr-0005-canonical-vs-rebuildable-stores.md               # Decision: storage vs projections + rebuild receipts + drift checks
│  │  ├─ adr-0006-time-model.md                                    # Decision: time semantics + schema/API/UI impacts
│  │  └─ adr-index.yml                                             # Optional: machine ADR registry (id/title/status/links) for tooling
│  ├─ diagrams/                                                    # Mermaid sources (linted; exported optionally)
│  │  ├─ README.md                                                 # Diagram style rules + naming + export policy + review checklist
│  │  ├─ system-context.mmd                                        # Actors + boundaries + dependencies diagram
│  │  ├─ layering.mmd                                              # Allowed dependency direction + interface seams diagram
│  │  ├─ truth-path.mmd                                            # Zones + promotion gates diagram
│  │  ├─ contracts.mmd                                             # Contract surfaces + validation flow diagram (contracts/ ↔ tools/tests)
│  │  ├─ pep-pdp-obligations.mmd                                   # PEP/PDP decision + obligations emission flow
│  │  ├─ evidence-flow.mmd                                         # EvidenceRef → resolve → EvidenceBundle → UI rendering/verification flow
│  │  ├─ time-model.mmd                                            # Time relationships + as-of query + version pinning flow
│  │  ├─ deployment.mmd                                            # Conceptual deployment + trust boundaries + secret handling posture
│  │  └─ exports/                                                  # OPTIONAL: rendered exports (generated; never hand-edited)
│  │     ├─ .gitkeep                                               # Keep folder if exports are generated in CI
│  │     └─ README.md                                              # How exports are generated/verified and when committed
│  ├─ contracts/                                                   # Stable contracts (human + machine; link to /contracts when canonical)
│  │  ├─ README.md                                                 # Overview + versioning + normative language rules + drift policy
│  │  ├─ api-contract.md                                           # Normative API behavior summary (auth, pagination, receipts, errors)
│  │  ├─ api-versioning-and-compat.md                              # Deprecation/compat rules + breaking-change gates + migration notes
│  │  ├─ api-error-model.md                                        # Error envelope semantics (policy-safe), trace IDs, retryability, UX mapping
│  │  ├─ authn-authz-contract.md                                   # Auth expectations (roles/scopes), audit requirements, denial semantics
│  │  ├─ policy-contract.md                                        # Policy contract (labels, decisions, obligations, fail-closed defaults)
│  │  ├─ policy-labels.vocab.json                                  # Labels vocab mirror/pointer (definitions + stability rules)
│  │  ├─ obligations.vocab.yml                                     # Obligations vocab mirror/pointer (types + required params)
│  │  ├─ evidence-resolver-contract.md                             # Resolver contract (inputs/outputs, verification, obligations, errors)
│  │  ├─ evidence-ref.schema.json                                  # EvidenceRef schema mirror/pointer (schemes + required fields)
│  │  ├─ evidence-bundle.schema.json                               # EvidenceBundle schema mirror/pointer (safe render fields + hashes)
│  │  ├─ run-receipt.schema.json                                   # Run receipt schema mirror/pointer (audit_ref, checks, inputs/outputs)
│  │  ├─ run-receipt.example.json                                  # Golden example referenced by docs + CI
│  │  ├─ promotion-manifest.schema.json                            # Promotion manifest schema mirror/pointer (artifacts, digests, approvals)
│  │  ├─ promotion-manifest.example.json                           # Golden example referenced by docs + CI
│  │  ├─ story-node.schema.json                                    # StoryNode schema mirror/pointer (or doc explaining canonical location)
│  │  ├─ claim.schema.json                                         # Claim schema (statement + evidence links + policy refs + time bounds)
│  │  └─ fixtures/                                                 # Small canonical examples used across docs/tests (policy-safe)
│  │     ├─ example-evidence-ref.json                              # Minimal valid EvidenceRef example
│  │     ├─ example-evidence-bundle.json                           # Minimal valid EvidenceBundle example
│  │     ├─ example-claim.json                                     # Minimal valid Claim example
│  │     └─ example-story-node.json                                # Minimal valid StoryNode example
│  ├─ enforcement/                                                 # How invariants become CI/runtime gates (make it testable)
│  │  ├─ README.md                                                 # How to add/modify enforcement (tests/tools/policy) + fail-closed guidance
│  │  ├─ invariants.md                                             # Normative invariants list (each links to a test/tool gate)
│  │  ├─ policy-enforcement-points.md                              # PEP inventory: location, endpoints, required context, expected outputs
│  │  ├─ contract-testing.md                                       # Contract testing strategy (OpenAPI/schema, fixtures, drift detection)
│  │  ├─ data-promotion-gates.md                                   # Gate mapping → checks → artifacts → failure semantics
│  │  ├─ redaction-and-generalization-tests.md                     # Testing posture for sensitive locations + no-leakage guarantees
│  │  └─ ci-checks.md                                              # CI job mapping (workflow → tools/tests → required artifacts)
│  ├─ registries/                                                  # Machine-readable indexes that keep architecture docs honest
│  │  ├─ README.md                                                 # What registries are + how validated + ownership rules
│  │  ├─ boundary-surface-registry.yml                             # Trust surfaces list (UI/API/batch/Focus/admin) + owners + labels
│  │  ├─ service-catalog.yml                                       # Services/modules catalog (owners, contracts, data touched, PEPs)
│  │  ├─ contract-index.yml                                        # Contract → canonical source → version → tests/tools that validate it
│  │  ├─ pep-registry.yml                                          # PEP locations + endpoints + auth requirements + audit hooks
│  │  └─ policy-label-registry.yml                                 # Human-friendly label index mirroring machine vocab
│  ├─ templates/                                                   # Architecture templates (reviewed; stable entrypoints)
│  │  ├─ README.md                                                 # Template usage rules + what must be customized before merge
│  │  ├─ kfm-meta-block-v2.txt                                     # Authoritative MetaBlock v2 snippet
│  │  ├─ standard-doc.template.md                                  # Standard doc skeleton (Context → Contract → Verification → DoD)
│  │  ├─ adr.template.md                                           # ADR skeleton (mirrors ADR template)
│  │  ├─ contract-doc.template.md                                  # Contract doc skeleton (normative language + examples + tests)
│  │  ├─ diagram.template.mmd                                      # Mermaid boilerplate (styles + lint-friendly patterns)
│  │  └─ review-checklist.md                                       # Architecture review checklist (what reviewers must verify)
│  └─ threat-model/                                                # Threat modeling (assets, actors, risks, mitigations)
│     ├─ README.md                                                 # Overview + cadence + acceptance criteria + “how to update”
│     ├─ scope-and-assets.md                                       # Protected assets + explicit out-of-scope items + trust boundaries
│     ├─ actors-and-entrypoints.md                                 # Threat actors + entry points (UI/API/batch/tools) + assumptions
│     ├─ data-classification-and-handling.md                       # Data classes + handling rules + default-deny + logging/redaction posture
│     ├─ abuse-cases.md                                            # Misuse scenarios + expected system response (deny/abstain/audit)
│     ├─ control-mapping.md                                        # Controls mapped to threats (policy, contracts, tests, infra controls)
│     ├─ risk-register.md                                          # Risk register (likelihood/impact/mitigation/owner/status)
│     └─ residual-risk.md                                          # Accepted risks + monitoring plan + revisit triggers
│
├─ adr/                                                           # Repo-wide ADRs (governed; shared entrypoint)
│  ├─ README.md                                                   # ADR process + rules + status definitions + index (human entrypoint)
│  ├─ TEMPLATE.md                                                 # Single-source ADR template (copy/paste; can embed MetaBlock v2)
│  ├─ ADR-REVIEW-CHECKLIST.md                                     # PR checklist: evidence links, rollback, verification gates, policy label, etc.
│  ├─ ADR-STYLE-GUIDE.md                                          # Optional: short style rules (tense, headings, decision statement format)
│  ├─ INDEX.md                                                    # Optional: canonical index (recommended if auto-generated)
│  ├─ _generated/                                                 # Optional: generated artifacts (never hand-edited)
│  │  ├─ adr-index.json                                           # Machine-readable ADR index for UI/search tooling
│  │  └─ adr-index.md                                             # Generated markdown ADR index (if automated)
│  ├─ tools/                                                      # Optional: glue scripts to enforce invariants
│  │  ├─ adr-next-number.sh                                       # Prints next available NNNN (fails if collision)
│  │  ├─ adr-lint.js                                              # Checks required sections exist + links/status are present
│  │  └─ adr-indexer.js                                           # Regenerates INDEX.md and/or _generated/* from filesystem scan
│  ├─ assets/                                                     # Optional: rare binaries (prefer Mermaid in ADRs)
│  │  ├─ diagrams/                                                # Exported diagrams when Mermaid is insufficient
│  │  └─ screenshots/                                             # Use sparingly; ensure no sensitive info
│  ├─ archive/                                                    # Optional: legacy/imported ADRs (kept for history)
│  │  └─ 20xx-legacy/                                             # Keep original filenames; add notes instead of rewriting
│  └─ 0001-*.md                                                   # ADR files live flat here (0001-..., 0002-..., etc.)
│
├─ governance/                                                    # Governance hub (human docs + checklists + policy fixtures)
│  ├─ README.md                                                   # Entrypoint + directory contract + navigation
│  ├─ ROOT_GOVERNANCE.md                                          # Charter: roles, decision process, definitions, escalation
│  ├─ ETHICS.md                                                   # Ethical commitments + “we will not do”
│  ├─ SOVEREIGNTY.md                                              # CARE-aligned sovereignty rules + restricted knowledge handling
│  ├─ REVIEW_GATES.md                                             # Review triggers + sign-off rules + promotion checklist pointers
│  ├─ GLOSSARY.md                                                 # Canonical governance terms
│  ├─ CHANGELOG.md                                                # Governance policy changes (human-readable; dated)
│  ├─ roles/                                                      # Governance ownership + roles + responsibilities
│  │  ├─ OWNERSHIP.md                                             # Who owns what (datasets, services, policies, catalogs)
│  │  ├─ ROLE_MODEL.md                                            # Role taxonomy (public, staff, researcher, admin, etc.)
│  │  ├─ RBAC_MATRIX.md                                           # Role → permissions matrix (high-level)
│  │  └─ REVIEWERS.md                                             # Required reviewers / quorum rules
│  ├─ labels/                                                     # Policy label taxonomy + how to apply it
│  │  ├─ POLICY_LABEL_TAXONOMY.md                                 # Definitions + required fields + defaults (fail-closed)
│  │  ├─ SENSITIVITY_GUIDE.md                                     # How to classify layers/fields/locations/media
│  │  ├─ REDACTION_GENERALIZATION.md                              # Redaction/generalization rules as first-class transforms
│  │  └─ examples/                                                # Worked examples (policy-safe)
│  │     ├─ public_generalized_example.md
│  │     ├─ restricted_location_example.md
│  │     └─ mixed_sensitivity_story_example.md
│  ├─ gates/                                                      # CI + human gates + release/promotion gates
│  │  ├─ PROMOTION_CONTRACT.md                                    # Minimum promotion requirements (zones, artifacts, receipts)
│  │  ├─ CI_GATES.md                                              # What CI must enforce
│  │  ├─ RUNTIME_GATES.md                                         # What runtime must enforce
│  │  ├─ FOCUS_MODE_EVALUATION.md                                 # Cite-or-abstain eval cases + regression expectations
│  │  └─ waivers/
│  │     ├─ WAIVER_POLICY.md                                      # When waivers are allowed + required approvals
│  │     └─ WAIVER_RECORD_TEMPLATE.md                             # Waiver record format (who/why/expiry/mitigations)
│  ├─ records/                                                    # Durable governance decisions + sign-offs (auditable)
│  │  ├─ decisions/
│  │  │  ├─ README.md
│  │  │  └─ GDR_TEMPLATE.md
│  │  ├─ reviews/
│  │  │  └─ (YYYY)/
│  │  │     └─ (PR-or-change-id).md
│  │  └─ incidents/
│  │     ├─ INCIDENT_TEMPLATE.md
│  │     └─ (YYYY)/...
│  ├─ templates/                                                  # Governance templates used across workflows
│  │  ├─ GOVERNANCE_REVIEW_RECORD.md
│  │  ├─ DATASET_INTAKE_CHECKLIST.md
│  │  ├─ SOVEREIGNTY_ASSESSMENT.md
│  │  ├─ AI_FEATURE_RISK_REVIEW.md
│  │  └─ PUBLICATION_SIGNOFF.md
│  └─ policy/                                                     # Policy-as-code documentation + fixtures (code may live elsewhere)
│     ├─ README.md                                                # Policy boundary: CI == runtime semantics; where code lives
│     ├─ POLICY_MODEL.md                                          # PDP/PEP model + decision IO + failure modes
│     ├─ OBLIGATIONS.md                                           # Obligation types + semantics
│     ├─ INPUT_CONTEXT.md                                         # What context is evaluated
│     ├─ schemas/
│     │  ├─ policy_context.schema.json
│     │  ├─ policy_decision.schema.json
│     │  └─ obligation.schema.json
│     ├─ fixtures/
│     │  ├─ allow_deny/
│     │  ├─ redaction_generalization/
│     │  └─ focus_mode/
│     ├─ testplan/
│     │  ├─ ci_policy_tests.md
│     │  ├─ runtime_policy_parity.md
│     │  └─ coverage_expectations.md
│     └─ mappings/
│        ├─ policy_code_locations.md
│        └─ enforcement_points.md
│
├─ standards/                                                     # Non-negotiable standards (CI-enforced where configured)
│  ├─ README.md                                                   # Index + how standards are reviewed/updated + versioning/deprecation rules
│  ├─ KFM_MARKDOWN_WORK_PROTOCOL.md                               # Docs protocol (formatting, linkcheck, review discipline)
│  ├─ KFM_REPO_STRUCTURE_STANDARD.md                              # Repo structure invariants (paths, naming, registries)
│  ├─ KFM_STAC_PROFILE.md                                         # STAC conformance standard (human-facing summary)
│  ├─ KFM_DCAT_PROFILE.md                                         # DCAT conformance standard (human-facing summary)
│  ├─ KFM_PROV_PROFILE.md                                         # PROV conformance standard (human-facing summary)
│  ├─ registry/                                                   # Machine-readable inventory (CI validation)
│  │  ├─ README.md
│  │  ├─ standards.registry.yaml
│  │  └─ deprecations.yaml
│  ├─ authoring/                                                  # Authoring rules (MetaBlock, citations, diagrams, normative language)
│  │  ├─ README.md
│  │  ├─ KFM_META_BLOCK_V2_STANDARD.md
│  │  ├─ KFM_NORMATIVE_LANGUAGE_STANDARD.md
│  │  ├─ KFM_CITATION_PROTOCOL.md
│  │  ├─ KFM_DIAGRAM_MERMAID_STANDARD.md
│  │  └─ examples/
│  │     ├─ good/
│  │     └─ bad/
│  ├─ repo/                                                       # Repo/process standards (branching, release, versioning)
│  │  ├─ README.md
│  │  ├─ KFM_BRANCHING_RELEASE_STANDARD.md
│  │  ├─ KFM_VERSIONING_DEPRECATION_STANDARD.md
│  │  └─ examples/
│  │     └─ repo_trees/
│  ├─ catalog/                                                    # Catalog standards (triplet linking + profiles)
│  │  ├─ README.md
│  │  ├─ triplet/
│  │  │  ├─ KFM_TRIPLET_LINKING_STANDARD.md
│  │  │  └─ examples/
│  │  │     ├─ minimal_triplet/
│  │  │     └─ complex_triplet/
│  │  ├─ stac/
│  │  │  ├─ README.md
│  │  │  ├─ CONFORMANCE.md
│  │  │  └─ examples/
│  │  ├─ dcat/
│  │  │  ├─ README.md
│  │  │  ├─ CONFORMANCE.md
│  │  │  └─ examples/
│  │  └─ prov/
│  │     ├─ README.md
│  │     ├─ CONFORMANCE.md
│  │     └─ examples/
│  ├─ policy/
│  │  ├─ README.md
│  │  ├─ KFM_POLICY_LABEL_STANDARD.md
│  │  ├─ KFM_REDACTION_OBLIGATIONS_STANDARD.md
│  │  └─ examples/
│  │     ├─ public/
│  │     └─ restricted/
│  ├─ evidence/
│  │  ├─ README.md
│  │  ├─ KFM_EVIDENCE_REF_STANDARD.md
│  │  ├─ KFM_EVIDENCE_BUNDLE_STANDARD.md
│  │  ├─ KFM_RUN_RECEIPT_STANDARD.md
│  │  └─ examples/
│  ├─ api/
│  │  ├─ README.md
│  │  ├─ KFM_API_CONTRACT_EXTENSION.md
│  │  ├─ KFM_ERROR_MODEL_STANDARD.md
│  │  ├─ KFM_PAGINATION_FILTERING_STANDARD.md
│  │  └─ examples/
│  ├─ ui/
│  │  ├─ README.md
│  │  ├─ KFM_STORY_NODE_STANDARD.md
│  │  ├─ KFM_EVIDENCE_FIRST_UX_STANDARD.md
│  │  └─ accessibility/
│  │     └─ KFM_A11Y_MINIMUM_STANDARD.md
│  └─ _archive/
│     ├─ README.md
│     └─ 2026-02-xx/
│
├─ templates/                                                     # Governed templates (docs-as-prod; reviewed; stable entrypoints)
│  ├─ README.md                                                   # Template index + usage rules + “must customize before merge” checklist
│  ├─ TEMPLATE__KFM_UNIVERSAL_DOC.md                              # Universal doc template (Context→Contract→Verification→DoD)
│  ├─ TEMPLATE__STORY_NODE_V3.md                                  # Story Node v3 template (MetaBlock + claims + EvidenceRefs)
│  └─ TEMPLATE__API_CONTRACT_EXTENSION.md                         # API contract extension template (normative language + examples)
│
├─ runbooks/                                                      # Operational runbooks (production-grade, step-by-step)
│  ├─ README.md                                                   # Runbooks index + incident flow + “how to use during outages”
│  ├─ _registry/                                                  # Optional: machine-checkable completeness + ownership
│  │  ├─ runbooks.yml                                             # Runbook registry (id, owners, scope, last_reviewed)
│  │  ├─ runbooks.schema.json                                     # Schema for runbooks.yml
│  │  └─ owners.yml                                               # Owner aliases (routing reviews; CODEOWNERS sync input)
│  ├─ templates/                                                  # Runbook templates (copy/paste; consistent sections)
│  │  ├─ runbook-template.md
│  │  ├─ evidence-bundle-template.md
│  │  ├─ incident-notes-template.md
│  │  ├─ comms-update-template.md
│  │  ├─ postmortem-template.md
│  │  └─ change-record-template.md
│  ├─ incidents/                                                  # Incident playbooks + comms + drills (SEV-aligned)
│  ├─ change/                                                     # Change management runbooks (intake→execute→rollback→closeout)
│  ├─ pipelines/                                                  # Pipeline ops (rerun/backfill/quarantine/promote/receipts verify)
│  ├─ data/                                                       # Data stewardship ops (QA failures/redaction/schema change/restore/tombstone)
│  ├─ catalog/                                                    # Catalog ops (build/validate/publish/rebuild/deprecate)
│  ├─ evidence/                                                   # Evidence ops (bundle create/resolve/redaction/retention/audit append)
│  ├─ indexing/                                                   # Indexing ops (search/tiles/graph rebuild + freshness verification)
│  ├─ api/                                                        # API ops (deploy/rollback/migrations/rate limits/read-only)
│  ├─ ui/                                                         # UI ops (deploy/flags/cache/emergency banners/style updates)
│  ├─ policy/                                                     # Policy ops (bundle build/publish/regression triage/emergency deny-all)
│  ├─ governance/                                                 # Governance ops (access reviews/grants/revokes/release approvals)
│  ├─ platform/                                                   # Platform ops (backup/restore/DR/k8s upgrades/cert rotate/storage expand)
│  ├─ observability/                                              # Observability ops (alerts/dashboards/retention/SLOs/sampling)
│  └─ _assets/                                                    # Supporting assets (prefer Mermaid + text; policy-safe)
│
├─ guides/                                                        # Onboarding + how-to (developer, steward, operator)
│  ├─ README.md                                                   # Guides index + recommended learning path
│  ├─ onboarding.md                                               # New contributor/operator onboarding checklist
│  ├─ add_a_dataset.md                                            # Dataset onboarding walkthrough (specs → pipelines → promotion gates)
│  ├─ publish_a_story.md                                          # Story authoring + review + publish workflow (EvidenceRefs required)
│  └─ focus_mode_eval.md                                          # Focus evals + reports interpretation + regression triage
│
├─ data/                                                          # Data documentation (manifests, schemas, QA, provenance, promotion evidence)
│  ├─ README.md                                                   # How data docs map to registry + promotion gates + where “truth” lives
│  ├─ CONTRIBUTING.md                                             # How to add/update a dataset_id folder (PR checklist, naming rules)
│  ├─ GLOSSARY.md                                                 # Shared terms: dataset_id, dataset_version, run_id, extents, checks, zones, etc.
│  ├─ _templates/                                                 # Copy/paste starters (kept in sync with _schemas)
│  │  ├─ manifest.yaml                                            # Template: identity/license/sensitivity/extents/owners
│  │  ├─ sources.yaml                                             # Template: upstream acquisition metadata + checksums/etags
│  │  ├─ checks.yaml                                              # Template: QA rules + thresholds + failure semantics
│  │  ├─ publish_receipt.json                                     # Template: audit record + checksums + policy decisions + artifact list
│  │  ├─ data_dictionary.md                                       # Template: human-friendly dictionary starter
│  │  └─ lineage.mmd                                              # Template: Mermaid lineage diagram starter
│  ├─ _schemas/                                                   # Machine-validation for docs in this folder (CI uses these)
│  │  ├─ manifest.schema.json                                     # JSON Schema for datasets/*/manifest.yaml
│  │  ├─ sources.schema.json                                      # JSON Schema for datasets/*/provenance/sources.yaml
│  │  ├─ checks.schema.json                                       # JSON Schema for datasets/*/qa/checks.yaml
│  │  ├─ receipt.schema.json                                      # JSON Schema for datasets/*/receipts/*.json
│  │  └─ naming.schema.md                                         # Human rules: dataset_id format, dates, run_id format, file naming
│  ├─ governance/                                                 # Human-readable policy guidance (not dataset-specific)
│  │  ├─ licenses.md
│  │  ├─ sensitivity.md
│  │  ├─ redaction.md
│  │  ├─ retention.md
│  │  └─ access.md
│  ├─ promotion/                                                  # Promotion Contract helpers (what must exist to move zones)
│  │  ├─ gates.md
│  │  ├─ checklists/
│  │  │  ├─ gate-a-identity.md
│  │  │  ├─ gate-b-schema.md
│  │  │  ├─ gate-c-qa.md
│  │  │  ├─ gate-d-provenance.md
│  │  │  └─ gate-e-publish-receipt.md
│  │  └─ examples/
│  │     ├─ example_dataset/
│  │     └─ example_receipts/
│  │        └─ publish_YYYY-MM-DD.json
│  ├─ registries/                                                 # Optional global reference indices (human-readable)
│  │  ├─ datasets.csv
│  │  ├─ sources.csv
│  │  ├─ owners.yaml
│  │  ├─ tags.yaml
│  │  └─ vocabulary/
│  │     ├─ geometry_types.md
│  │     ├─ measurement_units.md
│  │     └─ place_names.md
│  ├─ datasets/                                                   # Recommended: one folder per dataset_id
│  │  └─ <dataset_id>/
│  │     ├─ README.md
│  │     ├─ manifest.yaml
│  │     ├─ CHANGELOG.md
│  │     ├─ access.md
│  │     ├─ extents/
│  │     │  ├─ bbox.json
│  │     │  └─ footprint.geojson
│  │     ├─ schema/
│  │     │  ├─ schema.json
│  │     │  ├─ ddl.sql
│  │     │  ├─ dictionary.md
│  │     │  └─ mappings/
│  │     │     ├─ source_to_canonical.csv
│  │     │     └─ codebooks/
│  │     │        └─ <field>.md
│  │     ├─ pipeline/
│  │     │  ├─ ingest.yaml
│  │     │  ├─ transform.yaml
│  │     │  ├─ publish.yaml
│  │     │  └─ runbook.md
│  │     ├─ qa/
│  │     │  ├─ checks.yaml
│  │     │  ├─ expectations.md
│  │     │  ├─ baselines/
│  │     │  │  └─ 2026-02-01.json
│  │     │  └─ reports/
│  │     │     └─ 2026-02-24/
│  │     │        ├─ report.json
│  │     │        ├─ report.md
│  │     │        └─ artifacts/
│  │     ├─ provenance/
│  │     │  ├─ sources.yaml
│  │     │  ├─ retrieval/
│  │     │  │  └─ 2026-02-24.json
│  │     │  ├─ lineage.mmd
│  │     │  └─ citations.bib
│  │     ├─ receipts/
│  │     │  ├─ ingest_2026-02-24.json
│  │     │  ├─ promote_work_2026-02-24.json
│  │     │  ├─ promote_processed_2026-02-24.json
│  │     │  └─ publish_2026-02-24.json
│  │     ├─ versions/
│  │     │  └─ <dataset_version>/
│  │     │     ├─ manifest.lock.json
│  │     │     ├─ schema.lock.json
│  │     │     ├─ qa/
│  │     │     ├─ provenance/
│  │     │     └─ receipts/
│  │     └─ examples/
│  │        ├─ queries.sql
│  │        ├─ api.http
│  │        ├─ notebook.md
│  │        └─ viz.md
│  └─ samples/
│     ├─ README.md
│     ├─ _generated/
│     └─ <dataset_id>/
│        ├─ sample.csv
│        ├─ sample.geojson
│        └─ sample.md
│
├─ stories/                                                       # Story Nodes: narratives + map state + citations (policy-labeled, review-gated)
│  ├─ README.md                                                   # Authoring + review + publish rules (gates + invariants)
│  ├─ story_node_spec.md                                          # (Compat) Human-facing spec pointer to canonical StoryNode schema/standard
│  ├─ templates/                                                  # (Compat) Simple entrypoint templates (may forward to _templates/story_node_v3)
│  │  ├─ story_node.md                                            # (Compat) Markdown template wrapper (if you keep this for legacy links)
│  │  └─ story_node.sidecar.json                                  # (Compat) Sidecar template wrapper (if you keep this for legacy links)
│  ├─ _schemas/                                                   # JSON Schemas (CI validates story packs + sidecars)
│  │  ├─ story_node.schema.json                                   # story.md structural expectations (optional markdown lint schema)
│  │  ├─ story_sidecar.schema.json                                # story.json: map state + citations + policy labels/obligations
│  │  ├─ media_attribution.schema.json                            # Optional structured media attribution schema
│  │  └─ story_index.schema.json                                  # Schema for aggregated story indexes
│  ├─ _registry/                                                  # Lightweight catalog/index of stories for UI + discovery
│  │  ├─ stories.index.json                                       # Story index (slug → title/status/tags; derived or curated)
│  │  ├─ tags.vocab.json                                          # Controlled tags vocabulary (optional)
│  │  └─ policy_labels.vocab.json                                 # Allowed labels/obligations vocab (optional mirror/pointer)
│  ├─ _lint/                                                      # Repo-local lint config for story QA
│  │  ├─ linkcheck.allowlist.txt                                  # Allowlist for stable external domains (optional)
│  │  ├─ markdownlint.json                                        # Markdown style rules (optional)
│  │  └─ story_rules.yaml                                         # House rules: required sections, prohibited patterns, etc.
│  ├─ _shared/                                                    # Shared, non-story-specific assets (optional)
│  │  ├─ media/                                                   # Shared media used across stories (licensed; policy-safe)
│  │  └─ snippets/                                                # Reusable markdown fragments (disclaimers/boilerplates)
│  ├─ _templates/                                                 # Copy/paste starters (aligned to Story Node v3)
│  │  └─ story_node_v3/
│  │     ├─ story.md                                              # Template markdown (sections + citation pattern)
│  │     ├─ story.json                                            # Template sidecar (map state + refs placeholders)
│  │     ├─ media_attribution.md                                  # Template attribution notes (license + credits)
│  │     └─ review_checklist.md                                   # Reviewer checklist template
│  ├─ draft/                                                      # Proposed stories (NOT authoritative)
│  │  └─ <story_slug>/
│  │     ├─ story.md
│  │     ├─ story.json
│  │     ├─ story.lock.json
│  │     ├─ evidence/
│  │     │  ├─ evidence_refs.json
│  │     │  ├─ claim_map.json
│  │     │  └─ notes.md
│  │     ├─ map/
│  │     │  ├─ map_state.json
│  │     │  ├─ layer_overrides.json
│  │     │  └─ bookmarks.json
│  │     ├─ media/
│  │     │  ├─ src/
│  │     │  ├─ derived/
│  │     │  └─ thumbnails/
│  │     ├─ media_attribution.md
│  │     ├─ review/
│  │     │  ├─ checklist.md
│  │     │  ├─ signoff.yaml
│  │     │  └─ discussion.md
│  │     └─ exports/
│  │        ├─ preview.html
│  │        └─ figures/
│  ├─ review/                                                     # Stories in formal review (pre-publish freeze)
│  │  └─ <story_slug>/
│  │     ├─ story.md
│  │     ├─ story.json
│  │     ├─ story.lock.json
│  │     ├─ review/
│  │     │  ├─ checklist.md
│  │     │  ├─ signoff.yaml
│  │     │  └─ decision_log.md
│  │     └─ receipts/
│  │        ├─ lint_report.json
│  │        ├─ linkcheck_report.json
│  │        ├─ schema_validation.json
│  │        └─ policy_check.json
│  ├─ published/                                                  # Published stories (authoritative)
│  │  └─ <story_slug>/
│  │     ├─ story.md
│  │     ├─ story.json
│  │     ├─ story.manifest.json
│  │     ├─ story.receipt.json
│  │     ├─ media/
│  │     │  └─ …
│  │     ├─ media_attribution.md
│  │     ├─ versions/
│  │     │  ├─ v1/
│  │     │  │  ├─ story.md
│  │     │  │  ├─ story.json
│  │     │  │  ├─ story.manifest.json
│  │     │  │  ├─ story.receipt.json
│  │     │  │  └─ media/…
│  │     │  └─ v2/
│  │     │     └─ …
│  │     └─ CHANGELOG.md
│  ├─ withdrawn/                                                  # Removed from publication (policy/quality/rights reasons)
│  │  └─ <story_slug>/
│  │     ├─ tombstone.md
│  │     ├─ withdrawal_receipt.json
│  │     └─ references/
│  └─ _archive/                                                   # Deprecated structures or retired templates (keep minimal)
│     └─ …
│
├─ investigations/                                               # Discover-mode notes (not user-visible until promoted)
│  ├─ README.md                                                  # Rules: drafts only; promotion path into architecture/guides/standards
│  └─ <investigation-slug>/
│     ├─ README.md
│     └─ notes.md
│
├─ quality/                                                      # Human-facing QA checklists + explainers (maps to CI gates)
│  ├─ README.md                                                  # Quality docs index + how they map to tests/tools
│  ├─ threat_model_checklist.md                                  # Checklist linking to architecture/threat-model/*
│  └─ ...                                                       # Additional quality docs (release readiness, doc QA, etc.)
│
├─ schemas/                                                      # Human-facing schema docs/examples (NOT canonical machine schemas)
│  ├─ README.md                                                  # Where canonical schemas live (/contracts) + how to read examples safely
│  ├─ run_receipt.md                                             # Field-by-field explanation + examples + common failures
│  ├─ promotion_manifest.md                                      # Explanation + examples + compatibility notes
│  ├─ evidence_bundle.md                                         # Explanation + safe rendering guidance + verification expectations
│  └─ examples/                                                  # Policy-safe examples referenced by docs/tests
│
└─ diagrams/                                                     # Shared diagrams referenced across docs (mermaid/mmd/svg)
   ├─ README.md                                                  # Cross-doc diagram conventions + naming + export rules
   └─ <diagram-files>                                            # Shared diagram sources/exports used outside architecture/
```

> [!TIP]
> Keep “canonical schemas” and validators under `contracts/` and `tools/`.  
> Keep `docs/schemas/` as **human-readable explanations + examples**, not the enforcement source of truth.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## System map

KFM is governed end-to-end:

**Upstream → RAW → WORK/QUARANTINE → PROCESSED → CATALOG (DCAT/STAC/PROV + receipts) → projections → trust membrane (PEP + policy + evidence) → UI → audit**

```mermaid
flowchart LR
  S["Upstream sources"] --> R["RAW zone"]
  R --> W["WORK zone"]
  W --> Q["QUARANTINE zone"]
  W --> P["PROCESSED zone"]
  Q -.->|blocks promotion| P
  P --> C["CATALOG triplet + receipts"]
  C --> IDX["Rebuildable projections"]
  C --> PUB["PUBLISHED exports<br/>(policy & rights filtered)"]

  subgraph TM["Trust membrane"]
    API["Governed API (PEP)"]
    POL["Policy Engine"]
    ER["Evidence Resolver"]
    API <--> POL
    API <--> ER
  end

  IDX --> API
  API --> UI["Map Explorer • Stories • Catalog • Focus"]
  API --> AUD["Append-only audit ledger"]
  C --> AUD
```

### Architecture invariants (CONFIRMED — design)
- UI/clients never access storage/DB directly; **all access goes through governed APIs + policy boundary**.
- Policy enforcement is evaluated at the **PEP**; no “static bypass” via object storage links.
- Core logic never bypasses repositories to reach storage.
- Catalogs/provenance are canonical; projections are rebuildable.
- Promotion gates fail closed.
- Focus Mode answers cite-or-abstain; citation verification is a hard gate; governed runs emit receipts.

---

## Doc templates

### MetaBlock v2 header (required)
All governed docs should start with MetaBlock v2 (no YAML frontmatter):

```md
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: <Title>
type: guide|standard|story|dataset_spec|adr|runbook|run_receipt
version: v1
status: draft|review|published
owners: <team or names>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|internal|embargoed|...
related:
  - kfm://dataset/<slug>@<version>
  - kfm://story/<id>@<version>
  - <paths or other kfm:// ids>
tags:
  - kfm
notes:
  - <short notes>
[/KFM_META_BLOCK_V2] -->
```

**Rules:**
- `doc_id` must be stable (do not regenerate on edits).
- `updated` must change on meaningful edits.
- `policy_label` must reflect the most restrictive content in the doc (default-deny if unsure).

### Template registry (PROPOSED)
If `docs/templates/` exists, treat templates as governed artifacts (reviewed, versioned, link-checked):

- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

### ADR template
```md
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: ADR-XXXX: <decision title>
type: adr
version: v1
status: draft|accepted|rejected|superseded
owners: <team>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: internal
related:
  - <link to impacted contracts/docs>
tags: [kfm, adr]
notes:
  - <optional>
[/KFM_META_BLOCK_V2] -->

# ADR-XXXX: <decision title>

## Context

## Decision

## Consequences

## Alternatives considered

## Verification
- [ ] Tests updated/added
- [ ] Migration/rollback documented
- [ ] Security/policy review completed (if applicable)
```

### Story Node template note
Story Nodes are governed narratives:
- markdown body (human)
- sidecar metadata JSON (map state, citations, policy label, review state)

Publishing gate: all citations must resolve through the evidence resolver.

---

## CI gates for docs

Docs are only safe at scale if they’re continuously validated.

Recommended doc CI gates (PROPOSED):
- **MetaBlock lint:** required fields present; `doc_id` stable; dates parse
- **Internal linkcheck:** relative links resolve; no broken anchors
- **Policy label lint:** policy_label must exist; forbidden content patterns flagged for public docs
- **Secret scan:** prevent tokens/keys from landing in docs
- **Diagram render checks:** mermaid blocks parse (at least basic lint)
- **Story citation checks (when applicable):** citations resolve (or are marked UNKNOWN with verification)

> [!IMPORTANT]
> Fail-closed posture: if a doc is required by contract (e.g., runbook referenced in release workflow) and linkcheck fails, merging should be blocked.

---

## Definition of Done

A doc change is ready to merge when:

- [ ] MetaBlock v2 is present and correct (including `policy_label` and `owners`)
- [ ] Any user-facing or decision-driving claim is traceable (links to contracts/configs/receipts/manifests)
- [ ] Unknowns are explicitly labeled and include **minimum verification steps**
- [ ] No secrets, credentials, or sensitive coordinates are present
- [ ] Links are valid (or intentionally marked TODO with an owner and plan)
- [ ] Diagrams render (Mermaid) and are readable
- [ ] If governance/policy behavior changed, related gates/tests/docs are updated together

---

## Contribution workflow

1. Create or update a doc in the appropriate subfolder.
2. Add/refresh the MetaBlock v2 header.
3. Keep changes small and reversible (prefer additive glue over sweeping rewrites).
4. If you introduce a new requirement, point to (or add) the validator/test/gate that makes it enforceable.
5. Route review via CODEOWNERS (especially for governance, security, and promotion-related docs).

> [!TIP]
> For long docs, use `<details>` appendices so the main narrative stays scannable.

---

## Glossary

- **Trust membrane:** enforced boundary where governed policy + evidence controls what can be claimed or served.
- **PEP (Policy Enforcement Point):** the API boundary that evaluates policy on every request; clients never bypass it.
- **Policy Engine:** the policy decision mechanism (e.g., OPA/Rego), invoked by the PEP.
- **Promotion gate:** required checklist + evidence bundle before a DatasetVersion can be surfaced.
- **Policy label:** sensitivity classification that drives allow/deny + obligations.
- **EvidenceRef:** stable scheme reference (dcat://, stac://, prov://, doc://, …) resolvable without guessing.
- **EvidenceBundle:** resolved evidence package (policy decision + license + provenance + digests + audit ref).
- **Canonical vs rebuildable:** catalogs/provenance/artifacts are canonical; DB/search/tiles/graph are rebuildable.
- **Cite-or-abstain:** if citations can’t be verified and policy-allowed, abstain or reduce scope.

---

## Reference library

Some KFM workstreams maintain a reference library (GIS/cartography, pipelines, security, standards).

**Policy-safe posture:**
- Prefer a **bibliography/index** (titles + notes + pointers) over committing copyrighted PDFs.
- If a PDF must be included, ensure rights allow redistribution, and label it appropriately.

> [!NOTE]
> If a “project library index” exists, treat it as a helper, not a contract.
> Do not accidentally publish copyrighted materials by bundling them into a public repo.

---

<p align="right"><a href="#top">Back to top ↑</a></p>
