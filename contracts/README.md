<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/b5e9f8c2-1e25-4f09-8a55-9201a05f9b2d
title: contracts/ — KFM contract surfaces (schemas, APIs, profiles, gates)
type: standard
version: v3
status: draft
owners: TBD (set via CODEOWNERS)
created: 2026-02-22
updated: 2026-02-28
policy_label: public
related:
  - ../README.md
  - ../.github/README.md
  - ../configs/README.md
  - ../docs/
  - ../policy/
tags: [kfm, contracts, governance, schema, api, evidence, promotion-contract]
notes:
  - Aligned to vNext: truth-path zones + Promotion Contract gates A–G + triplet profiles + evidence resolver/API contract requirements.
  - Fail-closed: repo-specific wiring (exact filenames, generators, emitted CI check names) remains UNKNOWN until verified in-repo.
  - Prefer versioned artifacts + fixtures + CI validation over “tribal knowledge.”
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `contracts/` — KFM contract surfaces
**Contract-first • fail-closed • governed-by-default • evidence-first • time-aware**

**Status:** draft • **Owners:** TBD via `CODEOWNERS`  
**Purpose:** Make KFM interfaces **explicit, versioned, and machine-validated** so promotion + runtime behavior can’t drift.

![status](https://img.shields.io/badge/status-draft-yellow)
![principle](https://img.shields.io/badge/principle-contract--first-blue)
![gates](https://img.shields.io/badge/gates-fail--closed-critical)
![promotion](https://img.shields.io/badge/promotion%20contract-A--G-critical)
![triplet](https://img.shields.io/badge/catalog-triplet%20(DCAT%20%7C%20STAC%20%7C%20PROV)-informational)
![evidence](https://img.shields.io/badge/evidence-resolvable-important)
![policy](https://img.shields.io/badge/policy-CI%20%3D%3D%20runtime-critical)
<!-- TODO: replace placeholder checks with real workflow/status badges once repo workflows exist -->
<!-- e.g., https://img.shields.io/github/actions/workflow/status/<org>/<repo>/contracts-gate-summary.yml?branch=main -->

> [!IMPORTANT]
> **A contract is not documentation.**  
> A contract is a **machine-validated interface** with fixtures + tests. If a contract is missing/invalid/ambiguous, KFM must **block promotion** and/or **refuse to serve** affected data (policy-safe).

---

## Navigation

- [Truth status legend](#truth-status-legend)
- [Directory contract](#directory-contract)
- [What is a contract artifact](#what-is-a-contract-artifact)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Promotion Contract gates A–G](#promotion-contract-gates-a–g)
- [Catalog triplet and EvidenceRef](#catalog-triplet-and-evidenceref)
- [Governed API contract](#governed-api-contract)
- [Relationship to configs/ and policy/](#relationship-to-configs-and-policy)
- [Directory layout](#directory-layout)
- [How to add or change a contract](#how-to-add-or-change-a-contract)
- [Validation and gates](#validation-and-gates)
- [Governance and safety](#governance-and-safety)
- [Glossary](#glossary)
- [Appendix](#appendix)

---

## Truth status legend

This README uses explicit labels so we don’t “invent repo state”:

- **CONFIRMED (design):** required KFM posture (must hold regardless of stack)
- **UNKNOWN (repo):** not verified in this repository yet (treat as TODO; fail-closed)
- **PROPOSED:** recommended template/pattern (adopt only after verification)

> [!NOTE]
> Repo facts should graduate from **UNKNOWN → CONFIRMED (repo)** by attaching paths/snippets in PRs.

---

## Directory contract

This section satisfies the **Directory Documentation Standard** (purpose, where it fits, acceptable inputs, exclusions).

### Where this fits in the repo

`contracts/` is the system’s **trust membrane in file form**:
- CI uses `contracts/` to decide what’s promotable.
- Runtime services use `contracts/` to decide what’s servable.
- UIs and tools treat contracts as **authoritative interface definitions**, not suggestions.

Dependency direction (ideal):
- **Upstream inputs:** governance standards in `docs/` and policy posture in `policy/`
- **Downstream consumers:** pipelines, validators, catalog builders, governed API, evidence resolver, Focus Mode, UI SDKs

### Acceptable inputs

| Category | Examples | Why it belongs here |
|---|---|---|
| Interface schemas/specs | JSON Schema, OpenAPI, GraphQL SDL, protobuf | Defines externally visible shapes |
| Profiles + constraints | DCAT/STAC/PROV profiles, required fields, cross-link rules | Makes catalogs enforceable |
| Evidence contracts | EvidenceRef rules + schemes, EvidenceBundle schema | Enables cite-or-abstain guarantees |
| Promotion contracts | promotion manifest schema, run receipt schema, release manifest schema, gate codes | Blocks unsafe promotion/serving |
| Fixtures | known-good / known-bad examples | Prevent “it validates but breaks” |
| Contract tests | schema validation, linkcheck, parity checks | Turns intent into enforcement |
| Controlled vocab | policy labels, artifact zones, citation kinds | Prevents taxonomy drift |
| Version metadata | registries/locks/changelogs | Prevent drift + enable rollback |

### Exclusions (must not go here)

| Excluded | Put it elsewhere | Reason |
|---|---|---|
| Runtime code / business logic | `apps/`, `packages/`, `infra/` | Contracts define interfaces, not implementations |
| Secrets / tokens / credentials | secret manager / CI secrets | Contracts are reviewable and often public-ish |
| Large datasets or derived data | `data/` truth path zones | Keep contracts diff-friendly and small |
| Binary artifacts | release/build outputs | Contracts must be text + reviewable |
| “Docs only” explanations | `docs/` | If it can’t be tested/validated, it isn’t a contract |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## What is a contract artifact

A **contract artifact** is a *machine-validated schema/spec/profile* that defines an interface plus its enforcement scaffolding.

A contract change is incomplete unless it includes:
- updated validation/tests
- fixtures (known-good + known-bad)
- compatibility notes + migration/rollback plan
- downstream updates (pipeline/API/UI/Focus) if impacted

> [!IMPORTANT]
> A contract change without fixtures is **code without tests**. Treat as merge-blocking.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Non-negotiable invariants

These are **CONFIRMED (design)** and apply to all contract surfaces.

### 1) Trust membrane (no bypasses)
- Clients/UI **never** access databases/object storage directly.
- Backend logic **never** bypasses repository interfaces to reach storage.
- All access flows through governed APIs that apply **policy + obligations + audit** consistently.

### 2) Truth path zones are real (not a metaphor)
Contracts must reinforce the storage zones and promotion boundaries:

- **RAW**: immutable, append-only acquisition + checksums.
- **WORK**: intermediate transforms + QA + candidate redactions/generalizations (rewritable).
- **QUARANTINE**: failed validation, unclear licensing, sensitivity concerns; **not promotable**.
- **PROCESSED**: publishable artifacts in KFM-approved formats + checksums.
- **CATALOG/TRIPLET**: cross-linked DCAT + STAC + PROV describing metadata/assets/lineage.
- **PUBLISHED**: governed runtime surfaces (API + UI) served via policy enforcement.

**Invariant:** Published surfaces may only serve promoted dataset versions that have processed artifacts, validated catalogs, run receipts, and policy label assignment.

### 3) Policy semantics parity (CI == runtime)
Contracts that depend on policy (promotion gates, evidence resolution, exports) must produce the **same outcomes** in:
- CI policy tests (merge gates)
- runtime enforcement (governed API + evidence resolver)
- Focus Mode citation verification

If CI and runtime disagree, CI guarantees are meaningless → **release blocker**.

### 4) Deterministic identity and hashing
Anything used in dataset identity (`dataset_version_id`, `spec_hash`, locks) must be:
- deterministically serialized
- stable under benign ordering/whitespace differences
- versioned and regression-tested (golden tests)

### 5) No silent looseness
- Removing a required field/gate or weakening validation is a breaking change.
- Ambiguity defaults to **deny** (fail-closed), then tighten the contract.

### 6) Evidence is a UX hard requirement (≤ 2 calls)
Evidence resolution must be usable in **≤ 2 calls** from UI interactions; otherwise users ignore provenance and trust collapses.

### 7) Policy-safe errors (no “ghost metadata”)
Errors and abstentions must not leak restricted existence through response differences or “helpful” metadata.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Promotion Contract gates A–G

These are the minimum fail-closed gates that must be enforceable by CI and reviewable during steward sign-off.

| Gate | What it protects | Typical contract artifacts |
|---|---|---|
| **A — Identity & versioning** | Immutable DatasetVersion identity | promotion manifest schema, `spec_hash` rules, deterministic serialization tests |
| **B — Licensing & rights** | Legal permission + obligations | license fields in schemas, attribution requirements, rights-holder fields |
| **C — Sensitivity & redaction plan** | Safety + cultural/community constraints | `policy_label` vocab, obligations schema, redaction/generalization transforms recorded in PROV |
| **D — Catalog triplet validation** | Interop + evidence surface | DCAT/STAC/PROV profiles + cross-link rules; EvidenceRef schemes |
| **E — QA & thresholds** | Data quality + fitness | QA report schema, thresholds declared in spec/profile; quarantine on failure |
| **F — Run receipt & audit record** | Repro + traceability | run receipt schema, audit entry schema, policy decision references |
| **G — Release manifest** *(optional but recommended)* | Production posture + rollback | release manifest schema; references to digests; supply chain attestations (if enabled) |

> [!WARNING]
> Weakening a gate is a **breaking governance change**. Treat as high-risk and require explicit review + migration plan.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Catalog triplet and EvidenceRef

KFM treats catalogs not as “nice metadata,” but as the canonical interface between pipeline outputs and runtime.

### Triplet responsibilities (conceptual)
- **DCAT** answers: “What is this dataset? Who published it? What is the license? What are the distributions?”
- **STAC** answers: “What assets exist? What are their spatiotemporal extents? Where are the files?”
- **PROV** answers: “How were these outputs created? Which inputs/tools/parameters?”

### EvidenceRef schemes (minimum)
> [!NOTE]
> Schemes are **interfaces**. Keep them stable and parseable.

- `dcat://...` resolves to dataset/distribution metadata
- `stac://...` resolves to collection/item/asset metadata
- `prov://...` resolves to lineage (activities/entities/agents)
- `doc://...` resolves to governed docs and story citations
- `graph://...` resolves to entity relations (if graph is enabled)

### Cross-link rules (must be testable)
Define explicit cross-links so navigation is deterministic:
- DCAT dataset → distributions → artifact digests
- DCAT dataset → `prov:wasGeneratedBy` → PROV bundle
- STAC collection → `rel="describedby"` → DCAT dataset
- STAC item → link to PROV activity and/or run receipt
- EvidenceRef schemes resolve into these objects **without guessing**

**CI must include link-checkers** verifying cross-links for every promoted dataset version.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Governed API contract

The governed API is the enforcement boundary:
- applies policy decisions + obligations
- enforces versioning + audit
- provides evidence resolution for UI/Focus Mode

### API contract requirements (minimum)
- Responses include `dataset_version_id` (when applicable), artifact digests (when applicable), and policy label (public-safe).
- Errors follow a stable error model (e.g., `error_code`, policy-safe `message`, `audit_ref`, optional remediation hints).
- Avoid leaking sensitive existence via error differences (align 403/404 behavior with policy).
- Versioning policy: freeze `/api/v1` semantics; introduce `/api/v2` only for breaking changes.

### Evidence resolver endpoint posture
- Accepts EvidenceRef (scheme-based) or a structured reference.
- Applies policy and returns allow/deny + obligations.
- Returns an EvidenceBundle with: human view (renderable card), machine metadata, allowed artifact links, digests, dataset_version IDs, and audit references.
- Must be usable from UI in ≤ 2 calls.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Relationship to configs/ and policy/

To avoid duplicate “sources of truth,” use this division of labor:

- `contracts/` = **canonical interface definitions**
  - schemas, profiles, OpenAPI, cross-link rules, controlled vocab
  - fixtures + contract tests that enforce interfaces

- `configs/` = **governed wiring / selection / knobs**
  - which profile sets are active
  - gate thresholds and environment-safe defaults
  - validator selection and lane configuration
  - (No secrets; no raw restricted data)

- `policy/` = **policy engine source** (rules and bundles)
  - policy code (e.g., Rego) + tests + bundles
  - shared semantics across CI and runtime
  - parity fixtures may live in `configs/` or `contracts/` depending on repo convention, but outcomes MUST match

> [!IMPORTANT]
> If a contract is required for promotion or serving, do **not** duplicate it across directories.
> Choose one canonical location and reference it.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Directory layout

> [!NOTE]
> This is a **PROPOSED** layout aligned to KFM vNext. Keep repo-specific filenames **UNKNOWN (repo)** until verified on-branch.

```text
contracts/
├─ README.md
├─ CHANGELOG.md                           # OPTIONAL: contract changes + migration notes
│
├─ registry/                              # PROPOSED: contract index + locks (audit + reproducibility)
│  ├─ contracts.manifest.v1.json          # what exists + versions + owners + validators
│  ├─ contracts.lock.v1.json              # deterministic digests of contract artifacts (spec_hash posture)
│  └─ schemas/
│     ├─ kfm.contract_manifest.v1.schema.json
│     └─ kfm.contract_lock.v1.schema.json
│
├─ openapi/                               # Governed API contracts (versioned)
│  ├─ v1/
│  │  ├─ openapi.yaml
│  │  ├─ error_model.schema.json
│  │  └─ response_envelopes.schema.json
│  └─ v2/                                 # ONLY when breaking changes require it
│     └─ openapi.yaml
│
├─ schemas/                               # JSON Schemas (or equivalent) for contract surfaces
│  ├─ promotion/
│  │  ├─ promotion_manifest.v1.schema.json
│  │  ├─ release_manifest.v1.schema.json          # Gate G
│  │  └─ promotion_gate_codes.v1.schema.json      # stable, enumerable codes
│  ├─ run/
│  │  ├─ run_receipt.v1.schema.json               # Gate F
│  │  └─ run_manifest.v1.schema.json              # OPTIONAL: typed inputs/outputs envelope
│  ├─ audit/
│  │  └─ audit_entry.v1.schema.json               # Gate F
│  ├─ policy/
│  │  ├─ policy_decision.v1.schema.json           # allow/deny + obligations + reason codes
│  │  └─ obligation_types.v1.schema.json
│  ├─ evidence/
│  │  ├─ evidence_ref.v1.schema.json
│  │  └─ evidence_bundle.v1.schema.json
│  ├─ catalogs/
│  │  ├─ dcat.profile.v1.schema.json              # KFM-required DCAT shape constraints
│  │  ├─ stac.profile.v1.schema.json              # KFM-required STAC constraints
│  │  └─ prov.profile.v1.schema.json              # KFM-required PROV constraints
│  └─ ui/
│     ├─ view_state.v1.schema.json                # bbox/time/layers; used by Focus Mode + Story Nodes
│     └─ story_node.v1.schema.json                # governed narrative contract (if stored here)
│
├─ profiles/                              # Governed profiles/constraints (what “valid” means in KFM)
│  ├─ catalogs/
│  │  ├─ dcat.profile.v1.yaml
│  │  ├─ stac.profile.v1.yaml
│  │  ├─ prov.profile.v1.yaml
│  │  └─ crosslinks.profile.v1.yaml               # DCAT↔STAC↔PROV link rules
│  ├─ promotion/
│  │  └─ promotion_contract.v1.yaml               # gates A–G (high-level) + required checks mapping
│  ├─ evidence/
│  │  └─ evidence_resolver.profile.v1.yaml        # resolution rules + fail-closed requirements
│  └─ time/
│     └─ time_axes.profile.v1.yaml                # event/transaction/valid time expectations
│
├─ vocab/                                 # Controlled vocabularies (versioned)
│  ├─ policy_labels.v1.yaml               # e.g., public | restricted | internal (repo-defined)
│  ├─ artifact_zones.v1.yaml              # raw | work | quarantine | processed | published
│  ├─ citation_kinds.v1.yaml              # map_feature | story_claim | focus_answer | doc_quote ...
│  └─ themes.v1.yaml
│
├─ linkcheck/                             # Cross-link and resolvability rules (may also live under profiles/)
│  ├─ evidence_ref_schemes.v1.yaml
│  ├─ catalog_crosslinks.v1.yaml
│  ├─ artifact_digest_rules.v1.yaml
│  └─ url_allowlist.v1.yaml               # if url:// is allowed at all
│
├─ fixtures/                              # Known-good / known-bad artifacts (required for contract changes)
│  ├─ promotion/
│  ├─ run/
│  ├─ evidence/
│  ├─ catalogs/
│  └─ api/
│
└─ tests/                                 # Contract tests (schema validate + linkcheck + parity checks)
   ├─ contract_test_plan.md
   ├─ validate_schemas.testplan.md
   ├─ validate_crosslinks.testplan.md
   ├─ validate_policy_parity.testplan.md
   └─ validate_evidence_resolver.testplan.md
```

> [!TIP]
> If your repo prefers executable tests elsewhere, keep the *plans* here and put implementations under
> `tools/validators/` (or repo-standard tooling), but ensure CI runs them as required checks.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## How to add or change a contract

### Step 1 — Choose the contract surface
Promotion? Catalog? Evidence? API? UI state? Audit?

### Step 2 — Decide whether this is breaking
- **Backwards-compatible:** add optional fields; preserve defaults
- **Breaking:** bump major version (or add `openapi/v2/`) and document a migration plan

### Step 3 — Add fixtures (required)
Every contract change MUST include:
- at least one **known-good** example
- at least one **known-bad** example that fails for the correct reason

### Step 4 — Add/extend contract tests (required)
At minimum:
- schema validation
- cross-link validation (DCAT↔STAC↔PROV; EvidenceRef resolvability)
- policy parity outcomes (CI == runtime) for any allow/deny behavior the contract touches
- policy-safe error model invariants (no restricted inference)
- spec_hash stability + deterministic output tests (goldens)

### Step 5 — Update registry/lock (if used)
- add contract/version entry to `contracts.manifest.v1.json`
- update `contracts.lock.v1.json` digests deterministically

### Step 6 — Document the change
- what changed and why
- what breaks (if anything)
- required downstream updates (pipeline/API/UI/Focus)
- rollback plan (how to revert safely)

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Validation and gates

Contracts are only valuable if they’re **enforced continuously**.

### Minimum CI gates (required posture)

- Validate all schemas in `contracts/schemas/**`
- Validate all profiles in `contracts/profiles/**`
- Validate all fixtures (known-good must pass; known-bad must fail)
- Validate link rules (DCAT↔STAC↔PROV; EvidenceRef resolvability)
- Validate evidence resolver contract behavior:
  - “public” evidence resolves to bundle with allowed artifacts
  - “restricted” evidence returns 403 with **no sensitive metadata leakage**
- Validate spec_hash determinism:
  - stability tests across runs
  - golden tests for canonicalization + deterministic outputs
- Validate policy parity fixtures (CI == runtime decisions)
- Validate API contract invariants (envelopes + error model)
- **Anti-skip:** a single always-runs “gate summary” job fails if any required validator didn’t run

> [!WARNING]
> Required gates MUST NOT be bypassable by `paths:` filters or conditional workflow logic.
> Prefer one required status check (`contracts / gate-summary`) for branch protection/rulesets.

### Promotion Contract mapping (contracts’ responsibility)

| Gate | Contract artifacts typically involved |
|---|---|
| A Identity/versioning | promotion manifest schema; deterministic `spec_hash` rules + golden tests |
| B Rights/licensing | required license/rights fields; vocab where needed |
| C Sensitivity | policy labels + obligations schema; generalization/redaction requirements recorded in PROV |
| D Catalog triplet | DCAT/STAC/PROV profile sets + cross-link rules |
| E QA thresholds | QA report schema + thresholds declaration in spec/profile |
| F Run receipt/audit | run_receipt + audit_entry schemas; policy decision refs |
| G Release manifest | release manifest schema; digest link rules; optional attestations |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Governance and safety

### Rights and licensing are enforceable
- Promotion requires explicit license + rights holder + attribution requirements per distribution.
- “Metadata-only reference” is allowed when assets cannot be mirrored.
- Exports must be rights-aware by default and policy-safe.

### Sensitive locations and restricted data
- Store precise geometries in restricted datasets only.
- Publish generalized public derivatives when allowed.
- Never leak restricted existence via subtle error behavior.

### Audit is required (and itself sensitive)
- Governed operations must emit an audit record capturing who/what/when/why plus inputs/outputs by digest and policy decisions.
- Audit logs require retention + access policy + redaction.

### Focus Mode: cite-or-abstain depends on contracts
- EvidenceRefs must be resolvable without guessing.
- EvidenceBundles must carry policy decision + obligations + provenance references.
- Citation verification is a hard gate; contracts enable that verification.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Glossary

- **Contract artifact:** machine-validated interface definition with versioning + fixtures + tests.
- **Profile:** additional constraints that define “valid” for KFM (beyond base schemas).
- **Promotion Contract:** fail-closed gates A–G controlling what can reach runtime surfaces.
- **Triplet:** DCAT (dataset), STAC (assets), PROV (lineage).
- **EvidenceRef:** stable reference (scheme-based) resolvable to an EvidenceBundle.
- **EvidenceBundle:** resolved evidence record including policy, license, provenance, digests, and audit reference.
- **Policy decision:** allow/deny + obligations + reason codes with an audit trail.
- **Policy-safe errors:** error behavior that prevents inferring restricted existence.

---

## Appendix

### Contract change checklist (copy/paste)

- [ ] Contract version bumped appropriately (or `openapi/v2` introduced if breaking)
- [ ] Schema/spec validates
- [ ] Fixtures updated (known-good + known-bad)
- [ ] Cross-link rules updated (DCAT↔STAC↔PROV↔artifacts; EvidenceRef resolvability)
- [ ] Policy parity outcomes preserved (or explicitly changed with fixtures + review)
- [ ] Error model remains policy-safe (no restricted inference)
- [ ] spec_hash stability + deterministic output tests updated
- [ ] Dependent implementations updated (pipeline/API/UI/Focus)
- [ ] Migration notes + rollback plan included

### Repo verification checklist (to graduate UNKNOWN → CONFIRMED (repo))

- [ ] Confirm actual contract storage locations (`contracts/` vs root `schemas/`, etc.)
- [ ] List CI jobs that validate contracts and identify the required status check name(s)
- [ ] Identify canonical policy bundle location and how CI/runtimes load it
- [ ] Identify the evidence resolver interface (service/tool) and its contract test harness
- [ ] Confirm whether release manifests and/or attestations are used in practice (Gate G)

<p align="right"><a href="#top">Back to top ↑</a></p>
