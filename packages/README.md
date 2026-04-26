<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION-packages-readme
title: packages/
type: standard
version: v1.1
status: review
owners: @bartytime4life
created: NEEDS-VERIFICATION
updated: 2026-04-22
policy_label: public
related: [../README.md, ../.github/CODEOWNERS, ../.github/README.md, ../contracts/README.md, ../schemas/README.md, ../policy/README.md, ../data/README.md, ../data/registry/README.md, ../docs/README.md, ../tests/README.md, ../tools/README.md, ../pipelines/README.md, ./catalog/README.md, ./domain/README.md, ./evidence/README.md, ./genealogy_ingest/README.md, ./indexers/README.md, ./ingest/README.md, ./policy/README.md]
tags: [kfm, packages, implementation, evidence, governance, trust-membrane, reusable-modules]
notes: [doc_id and created date need repository metadata confirmation, policy_label is provisional for a public repository README, this revision upgrades the packages directory contract and preserves an evidence-bounded truth posture]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `packages/`

Shared internal package boundaries for reusable KFM logic that must stay subordinate to evidence, contracts, schemas, policy, lifecycle state, review state, release state, and governed APIs.

![status](https://img.shields.io/badge/status-review-blue?style=flat-square)
![surface](https://img.shields.io/badge/surface-packages%2F-6f42c1?style=flat-square)
![owner](https://img.shields.io/badge/owner-%40bartytime4life-0b7285?style=flat-square)
![truth](https://img.shields.io/badge/truth-evidence--bounded-orange?style=flat-square)
![membrane](https://img.shields.io/badge/trust%20membrane-preserve-red?style=flat-square)
![public](https://img.shields.io/badge/policy-public-lightgrey?style=flat-square)

> [!IMPORTANT]
> **Status:** `review` README revision for an implementation-bearing directory boundary  
> **Path:** `packages/README.md`  
> **Authority class:** shared internal implementation contract; not doctrine, not policy law, not canonical data, not release evidence  
> **Truth posture:** `CONFIRMED` supplied README intent and KFM boundary vocabulary · `PROPOSED` strengthened parent directory contract · `UNKNOWN / NEEDS VERIFICATION` package-local source code, manifests, tests, imports, CI gates, and runtime wiring until the active checkout is inspected  
> **Default rule:** package code may help KFM operate, but it must not become a side door around governed evidence, policy, lifecycle, review, or release gates.

> [!WARNING]
> `packages/` must never become a normal public path to RAW, WORK, QUARANTINE, canonical stores, unpublished candidates, model runtimes, vector indexes, policy-unchecked answers, or release-unreviewed artifacts. Public clients and normal UI surfaces must remain behind governed APIs and released, policy-safe artifacts.

## Quick jumps

[Scope](#scope) · [At a glance](#at-a-glance) · [Evidence posture](#evidence-posture) · [Repo fit](#repo-fit) · [Placement test](#placement-test) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current package surface](#current-package-surface) · [Directory tree](#directory-tree) · [Maintainer workflow](#maintainer-workflow) · [Quickstart](#quickstart) · [Usage patterns](#usage-patterns) · [Diagram](#diagram) · [Package map](#package-map) · [Boundary rules](#boundary-rules) · [Definition of done](#definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

---

## Scope

`packages/` is the shared internal module lane for reusable KFM implementation logic.

It sits between stronger top-level authority surfaces and deployable or execution-facing surfaces. Its job is to keep shared logic bounded, testable, reviewable, and reusable without relocating authority away from `contracts/`, `schemas/`, `policy/`, governed `data/` artifacts, release evidence, review state, correction lineage, or trust-visible runtime seams.

A healthy package in this directory preserves:

- the governed truth path
- the trust membrane
- authoritative-versus-derived separation
- deterministic identity where practical
- evidence-linked behavior
- fail-closed defaults where rights, sensitivity, policy, review state, or evidence are uncertain
- rebuildable derived layers that do not pretend to be canonical truth
- correction and rollback references when package outputs affect downstream projections

`packages/` is useful only when it makes reusable logic easier to inspect. It is harmful when it hides authority, policy, release state, source identity, or data lifecycle transitions inside generic helper code.

[Back to top](#top)

---

## At a glance

| Question | Answer |
| --- | --- |
| What belongs here? | Reusable, non-deployable internal logic shared across apps, pipelines, tools, validators, or UI-support seams. |
| What does not belong here? | Canonical schemas, policy law, data artifacts, release records, route handlers, workers, live connectors, secrets, public UI entrypoints, or model runtimes. |
| What must packages respect? | Top-level contracts, schemas, policy, source registry, lifecycle zones, catalog/proof/release objects, review state, and correction lineage. |
| What should packages emit? | Bounded helper outputs, validation reports, normalized envelopes, or derived artifacts only through the owning lifecycle or release lane. |
| What should packages never become? | Shadow authority, hidden public surface, unreviewed publication path, or substitute for evidence. |
| What is the safe default? | `ABSTAIN`, `DENY`, `ERROR`, quarantine, redaction, or review-required state when evidence, rights, policy, sensitivity, or release state is unclear. |

[Back to top](#top)

---

## Evidence posture

This README uses truth labels because package documentation can easily overstate implementation maturity.

| Label | Meaning in this README |
| --- | --- |
| `CONFIRMED` | Directly supported by supplied README content, visible adjacent documentation text, or active checkout evidence when later inspected. |
| `INFERRED` | Strongly suggested by child README wording or adjacent KFM doctrine, but not proven as executable implementation. |
| `PROPOSED` | Recommended boundary guidance consistent with KFM doctrine and supplied package documentation. |
| `UNKNOWN` | Not established strongly enough from current-session evidence, active checkout evidence, tests, workflows, or runtime artifacts. |
| `NEEDS VERIFICATION` | A concrete repo, source file, manifest, owner, fixture, CI, runtime, license, policy, or platform check is required before stronger claims are safe. |

> [!NOTE]
> A README can establish intended boundaries. It does not prove source files, test coverage, import graphs, package publishing, runtime behavior, deployment state, or release maturity.

[Back to top](#top)

---

## Repo fit

`packages/` is implementation-bearing. It should stay downstream of stronger governance and upstream of deployable reuse.

| Relationship | Path | Role for `packages/` | Package posture |
| --- | --- | --- | --- |
| Root orientation | [`../README.md`](../README.md) | Project identity, truth posture, and repo-wide guardrails. | Respect and reference. |
| Ownership routing | [`../.github/CODEOWNERS`](../.github/CODEOWNERS) | Owner review routing for package changes. | Verify before claiming coverage. |
| GitHub gatehouse | [`../.github/README.md`](../.github/README.md) | Review, CI/CD, and repository-control posture. | Do not replace. |
| Contracts | [`../contracts/README.md`](../contracts/README.md) | Interface commitments and object meaning. | Consume, validate, adapt. |
| Schemas | [`../schemas/README.md`](../schemas/README.md) | Machine-checkable validation surface. | Consume, validate, adapt. |
| Policy | [`../policy/README.md`](../policy/README.md) | Rights, sensitivity, obligations, denials, and release admissibility. | Consume outcomes; do not redefine. |
| Data lifecycle | [`../data/README.md`](../data/README.md) | Registries, lifecycle zones, catalogs, receipts, proofs, and published artifacts. | Support lifecycle; do not own lifecycle records. |
| Source registry | [`../data/registry/README.md`](../data/registry/README.md) | SourceDescriptor and source-role handoff. | Consume activation posture. |
| Pipelines | [`../pipelines/README.md`](../pipelines/README.md) | Lane-specific fetch, normalize, validate, and emit execution. | Provide helpers; do not become the runner. |
| Apps / runtime | [`../apps/`](../apps/) | Deployable services and governed API consumers. | Provide reusable internals only. |
| Web / presentation | [`../web/`](../web/) | Browser-delivered presentation surface downstream of governed contracts. | Support trust-visible UI; do not bypass governed API. |
| Tests | [`../tests/README.md`](../tests/README.md) | Verification posture, fixtures, and integration evidence. | Add local tests; defer repo-wide proof here. |
| Tools | [`../tools/README.md`](../tools/README.md) | Validators, probes, CLIs, link checks, and utility tooling. | Share helpers only when reusable. |
| Infra | [`../infra/`](../infra/) | Deployment and environment wiring. | Never own secrets or deployment state. |

[Back to top](#top)

---

## Placement test

Add logic under `packages/` only when **all** of these are true:

1. The logic is shared across more than one app, worker, validator, pipeline, package, or presentation-facing surface.
2. The logic is not deployable on its own.
3. The logic is easier to review as a stable internal boundary than as app-local or pipeline-local glue.
4. The logic is subordinate to stronger top-level contract, schema, policy, data, and review authority.
5. The logic can be tested without live source activation or public release.
6. The logic does not require secrets, machine-local config, direct model clients, public routes, or unpublished data access as its normal path.

### Decision matrix

| Situation | Put it in `packages/`? | Better home when not |
| --- | --- | --- |
| Shared `EvidenceRef` resolver used by API and UI trust surfaces | Yes, if it returns bounded states and respects policy. | `apps/` only if it is route-local glue. |
| One pipeline's fetch schedule | No. | `pipelines/` or lane runbook. |
| Canonical JSON Schema | No. | `schemas/` or `contracts/`, per repo convention. |
| Policy adapter that formats a `PolicyDecision` for runtime callers | Yes, if top-level policy remains authoritative. | `policy/` if it defines the rule. |
| Generated receipt or proof object | No. | `data/receipts/`, `data/proofs/`, `release/`, or confirmed lifecycle home. |
| Search index builder for released artifacts | Yes, if rebuildable and release-linked. | `data/` / `release/` for emitted outputs. |
| Public map popup component | No. | `web/` or governed UI shell. |
| A generalized helper named `common/` or `utils/` | Usually no. | Create a named package with a crisp responsibility. |

[Back to top](#top)

---

## Accepted inputs

Content belongs in `packages/` when it is shared internal logic, not a public artifact, deployable entrypoint, or top-level authority source.

| Accepted input | Belongs here when… | Must stay linked to… |
| --- | --- | --- |
| Domain vocabulary and invariant helpers | They preserve stable KFM meaning across packages and runtime surfaces. | `contracts/`, `schemas/`, `docs/`, tests |
| Source intake helpers | They are reusable connector, normalization, validation, checksum, quarantine, or receipt helpers. | `data/registry/`, `pipelines/`, `policy/` |
| Catalog closure helpers | They compile or validate DCAT / STAC / PROV closure without becoming the outward catalog. | `data/catalog/`, `release/`, governed API |
| Evidence helpers | They support `EvidenceRef` → `EvidenceBundle` resolution or evidence-safe presentation. | `contracts/`, `schemas/`, `apps/`, Evidence Drawer |
| Policy-support adapters | They normalize policy outcomes, reason codes, obligations, or fail-closed errors without owning policy truth. | `policy/`, `tests/policy/`, governed API |
| Rebuildable indexers | They build search, tile, graph, vector, embedding, or runtime projections that are derived and release-linked. | `data/`, `release/`, `tests/`, cache invalidation notes |
| Package-local tests and fixtures | They prove package behavior without replacing repo-level tests or policy fixtures. | `tests/`, child README, CI |
| Export maps and package docs | They make package boundaries explicit and reviewable. | parent README, child README, CODEOWNERS |

[Back to top](#top)

---

## Exclusions

`packages/` is not a catch-all. When in doubt, keep authority visible at the top-level lane that owns the meaning.

| Do not put this in `packages/` | Put it here instead | Why |
| --- | --- | --- |
| Deployable HTTP services, route handlers, workers, CLIs, or app entrypoints | [`../apps/`](../apps/), [`../web/`](../web/), or lane-specific runtime homes | Packages are reusable internals, not deployment units. |
| Lane-local fetch recipes, watcher schedules, or one-off pipeline runners | [`../pipelines/README.md`](../pipelines/README.md), [`../scripts/README.md`](../scripts/README.md) | Execution belongs with the lane or automation surface. |
| Canonical OpenAPI definitions, JSON Schemas, shared vocabularies, or object law | [`../contracts/`](../contracts/), [`../schemas/`](../schemas/) | Prevents parallel contract universes. |
| Repo-authoritative policy bundles, Rego, fixtures, or gate definitions | [`../policy/`](../policy/) and policy tests | Package helpers may consume policy; they do not define it. |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED artifacts | [`../data/`](../data/) lifecycle lanes and [`../release/`](../release/) | Preserves KFM lifecycle boundaries. |
| Receipts, proofs, manifests, catalogs, or release bundles as primary records | `data/receipts/`, `data/proofs/`, `data/manifests/`, `data/catalog/`, `release/` as repo conventions confirm | Packages may emit or validate these objects; they do not own release memory. |
| Secrets, credentials, local machine state, tokens, private service URLs, model endpoints | Secret manager, deployment environment, or non-repo operational config | Prevents accidental exposure. |
| Architecture doctrine, ADRs, runbooks, and contributor policy | [`../docs/`](../docs/) | Maintains a visible documentation control plane. |
| Direct model-client traffic or free-form AI behavior | Governed API + evidence resolver + runtime envelope | AI remains downstream of evidence, policy, release state, and citation validation. |
| Public UI trust cues stripped of evidence context | Governed API, Evidence Drawer, layer manifests, Focus envelope | Public surfaces must preserve trust cues and correction state. |

[Back to top](#top)

---

## Current package surface

`PROPOSED / NEEDS VERIFICATION`: the package family is documented as README-first child boundaries. Confirm package-local code depth, manifests, tests, exports, runtime imports, and branch-enforced CI in the active checkout before stronger claims.

| Package | Root-contract reading | Documented state | Must never do |
| --- | --- | --- | --- |
| [`./catalog/`](./catalog/) | Shared internal catalog-closure compiler / validator seam. | README-first child boundary surface. | Become an ad hoc runtime API surface or release authority. |
| [`./domain/`](./domain/) | Stable semantic core for KFM vocabulary, invariants, and cross-package meaning. | README-first child boundary surface. | Own deployable side effects, transport, filesystem, database, or policy authority. |
| [`./evidence/`](./evidence/) | Governed `EvidenceRef` → `EvidenceBundle` resolution and evidence-safe presentation helpers. | README-first child boundary surface. | Emit uncited or policy-unchecked evidence surfaces. |
| [`./genealogy_ingest/`](./genealogy_ingest/) | Genealogy-shaped ingest seam; documented with path-alignment tension against `pipelines/genealogy_ingest/`. | README-first child surface with lane-shaped naming. | Blur package boundary, lane execution, living-person privacy, DNA sensitivity, consent, or review gates. |
| [`./indexers/`](./indexers/) | Rebuildable search, tile, graph, vector, embedding, and runtime projection builders. | README-first child boundary surface. | Become authoritative truth or a source of record. |
| [`./ingest/`](./ingest/) | Source intake, normalization, validation, quarantine, and receipt helpers. | README-first child boundary surface. | Serve clients directly or bypass lifecycle gates. |
| [`./policy/`](./policy/) | Shared internal policy-support logic and adapters. | README-first child boundary surface. | Replace repo-authoritative [`../policy/`](../policy/). |

> [!NOTE]
> This package family is not perfectly uniform. Most child surfaces are package seams; `genealogy_ingest/` is more lane-shaped and currently names a pipeline-oriented starter path. Keep package path, pipeline path, and actual checked-in implementation visibly separate until the active branch proves they align.

[Back to top](#top)

---

## Directory tree

### Current package-family snapshot

Verify this from the active checkout before treating it as implementation inventory.

```text
packages/
├── README.md
├── catalog/
│   └── README.md
├── domain/
│   └── README.md
├── evidence/
│   └── README.md
├── genealogy_ingest/
│   └── README.md
├── indexers/
│   └── README.md
├── ingest/
│   └── README.md
└── policy/
    └── README.md
```

### Doctrine-aligned growth shape

`PROPOSED`, not current implementation evidence:

```text
packages/<package-name>/
├── README.md
├── package manifest             # package.json / pyproject.toml / go.mod / Cargo.toml as repo convention requires
├── src/                         # reusable internal implementation only
├── tests/                       # package-local tests proving the local contract
├── fixtures/                    # package-local valid/invalid examples, when useful
└── examples/                    # non-production examples, clearly labeled
```

> [!TIP]
> Replace the snapshot only with inventory generated from the active checkout. Do not infer package manifests, `src/` trees, import graphs, runnable commands, or test status from README prose.

[Back to top](#top)

---

## Maintainer workflow

Use this sequence for package changes:

1. **Inventory** the active checkout before changing package claims.
2. **Classify** the change as boundary doc, implementation helper, validator, adapter, fixture, or derived-output builder.
3. **Check authority** against `contracts/`, `schemas/`, `policy/`, `data/registry/`, `data/`, `release/`, and `docs/`.
4. **Update both layers**: the affected child README and this parent README.
5. **Add local tests** when implementation code exists.
6. **Run repo-level checks** using the repo's confirmed package manager and CI conventions.
7. **Record migration / rollback** when downstream imports, generated outputs, or release-linked projections are affected.

### Change impact matrix

| Change type | Required documentation | Required validation | Rollback note |
| --- | --- | --- | --- |
| Add package | Parent README, child README, CODEOWNERS check, related ADR if authority is ambiguous. | Manifest check, local tests, import map, link check. | Remove package entry and package path; invalidate generated derivatives if any. |
| Rename package | Parent README, child README, migration note, import impact note. | Import graph, tests, affected tools, generated references. | Alias or revert path; preserve correction history. |
| Split package | Parent README, child READMEs, migration map, downstream consumer list. | Tests for old and new boundaries, export map. | Recombine or alias until consumers migrate. |
| Add validator helper | Child README, test fixture docs, toolchain reference. | Valid and invalid fixtures; fail-closed behavior. | Disable helper; keep fixture and reason for removal. |
| Add derived indexer | Child README, source/release dependency notes, cache invalidation notes. | Rebuild test, release-link validation, correction propagation check. | Drop derivative output; rebuild from prior release source. |
| Add policy adapter | Child README, policy authority link, reason-code mapping. | Policy fixture parity; `DENY` / `ABSTAIN` / `ERROR` handling. | Revert adapter; preserve top-level policy as source of truth. |

[Back to top](#top)

---

## Quickstart

Run these commands from the repository root unless noted otherwise. They are read-only inspection commands, not proof of build success.

```bash
# Confirm repository state.
git status --short
git branch --show-current
git rev-parse --show-toplevel

# Inventory the package family.
find packages -maxdepth 2 -type d | sort
find packages -maxdepth 2 -name README.md | sort
find packages -maxdepth 4 -type f | sort

# Check whether package-local implementation exists.
find packages -maxdepth 4 \
  \( -name package.json -o -name pyproject.toml -o -name Cargo.toml -o -name go.mod -o -name tsconfig.json -o -name Makefile \) \
  | sort

# Read the parent and child package boundary docs.
sed -n '1,260p' packages/README.md
for d in catalog domain evidence genealogy_ingest indexers ingest policy; do
  echo "---- packages/$d ----"
  test -f "packages/$d/README.md" && sed -n '1,180p' "packages/$d/README.md"
done

# Recheck adjacent authority and downstream surfaces.
sed -n '1,220p' README.md
sed -n '1,160p' .github/CODEOWNERS
sed -n '1,220p' contracts/README.md
sed -n '1,220p' schemas/README.md
sed -n '1,220p' policy/README.md
sed -n '1,240p' data/README.md
sed -n '1,220p' data/registry/README.md
sed -n '1,220p' pipelines/README.md
sed -n '1,220p' tests/README.md
sed -n '1,220p' tools/README.md

# Look for KFM trust-surface vocabulary in implementation-bearing paths.
grep -RInE \
  'EvidenceRef|EvidenceBundle|DecisionEnvelope|RuntimeResponseEnvelope|SourceDescriptor|ReleaseManifest|CatalogMatrix|run_receipt|ai_receipt|spec_hash|ABSTAIN|DENY|ERROR|ANSWER|trust membrane|RAW|WORK|QUARANTINE|PUBLISHED' \
  packages contracts schemas policy data tests tools apps pipelines docs 2>/dev/null || true
```

> [!CAUTION]
> These commands prove only the current checkout they inspect. They do not prove package publication, package-manager selection, build success, import graphs, deployed behavior, branch protection, workflow enforcement, or runtime adoption.

[Back to top](#top)

---

## Usage patterns

### Treat this README as the parent package contract

Use `packages/README.md` to decide whether logic belongs in `packages/` at all. Then confirm the child package README and live files before documenting narrower ownership.

### Keep child READMEs as boundary docs first

Child READMEs can carry useful package-local intent, but a README is not executable proof. Do not claim source files, tests, import graphs, build commands, or runtime consumers until the active branch exposes them.

### Prefer named packages over `common/` sprawl

A reusable package should have a crisp responsibility. Catch-all buckets such as `common/`, `shared/`, or `utils/` erase architecture and make review harder.

### Keep imports directional

Packages should depend inward toward stable semantics and top-level contracts. They should not depend outward on volatile runtime shells, app-local glue, environment-specific deployment code, or lane orchestration.

### Keep deployable concerns out

Package code may support apps, pipelines, and web-delivered surfaces, but it should not quietly become an app, lane, or presentation shell by accumulating startup behavior, route handlers, schedulers, auth entrypoints, or environment ownership.

### Keep negative states first-class

Packages that touch evidence, policy, AI-adjacent flows, source intake, or publication-related decisions must carry `ABSTAIN`, `DENY`, `ERROR`, stale, unavailable, restricted, generalized, and review-required outcomes instead of collapsing them into success or silence.

### Update both layers when boundaries change

When a package is added, renamed, split, removed, or materially repurposed, update:

1. the child package README
2. this parent README
3. related CODEOWNERS entries
4. affected tests, fixtures, contracts, schemas, policy docs, or runbooks
5. rollback and migration notes where downstream imports may be affected

[Back to top](#top)

---

## Diagram

```mermaid
flowchart LR
    subgraph Authority["Top-level authority surfaces"]
        ROOT["../README.md<br/>project posture"]
        CONTRACTS["../contracts/"]
        SCHEMAS["../schemas/"]
        POLICY["../policy/"]
        DATA["../data/"]
        DOCS["../docs/"]
    end

    subgraph Packages["packages/ shared internal modules"]
        CATALOG["catalog/"]
        DOMAIN["domain/"]
        EVIDENCE["evidence/"]
        GENEALOGY["genealogy_ingest/"]
        INDEXERS["indexers/"]
        INGEST["ingest/"]
        PPOLICY["policy/"]
    end

    subgraph Execution["Execution, verification, and presentation surfaces"]
        APPS["../apps/"]
        PIPELINES["../pipelines/"]
        WEB["../web/"]
        TESTS["../tests/"]
        TOOLS["../tools/"]
        RELEASE["../release/"]
    end

    ROOT -. constrains .-> Packages
    DOCS -. explains .-> Packages
    CONTRACTS --> DOMAIN
    SCHEMAS --> DOMAIN
    POLICY --> PPOLICY
    DATA --> CATALOG
    DATA --> INGEST

    DOMAIN --> CATALOG
    DOMAIN --> EVIDENCE
    DOMAIN --> INDEXERS
    DOMAIN --> INGEST
    PPOLICY --> EVIDENCE

    INGEST -. supports .-> PIPELINES
    GENEALOGY -. current README references starter lane under .-> PIPELINES
    CATALOG --> APPS
    EVIDENCE --> APPS
    INDEXERS --> APPS
    PPOLICY --> APPS

    TESTS -. verifies .-> Packages
    TOOLS -. validates .-> Packages
    Packages -. must not own .-> RELEASE
```

The boundary is intentional: package code may implement reusable internal mechanics, but KFM truth remains anchored in evidence, policy, contracts, lifecycle artifacts, review state, release manifests, and correction lineage outside the package directory.

[Back to top](#top)

---

## Package map

### Child package roles

| Package | Primary role | Stronger authority it must respect | First maturity check |
| --- | --- | --- | --- |
| [`catalog/`](./catalog/) | Compile / validate linked catalog closure. | `data/catalog/`, release state, contracts, policy. | Does it validate identifier parity across DCAT, STAC, PROV, release refs, and EvidenceBundle routes? |
| [`domain/`](./domain/) | Stable semantic vocabulary and invariant helpers. | Contracts, schemas, docs, policy. | Does it stay side-effect-free and reusable across multiple packages? |
| [`evidence/`](./evidence/) | Resolve evidence handles into policy-safe support packages. | EvidenceBundle contract, policy, governed API. | Can it return bounded negative states instead of unsupported evidence? |
| [`genealogy_ingest/`](./genealogy_ingest/) | Starter genealogy-shaped ingest seam. | People/DNA/land policy, privacy, consent, pipeline ownership. | Is package-vs-pipeline placement explicitly resolved before implementation claims grow? |
| [`indexers/`](./indexers/) | Build derived search, tile, graph, vector, embedding, or runtime projections. | Release state, source lineage, freshness, correction propagation. | Are outputs rebuildable, release-linked, and clearly non-authoritative? |
| [`ingest/`](./ingest/) | Shared source intake, normalization, validation, quarantine, and receipt helpers. | SourceDescriptor, data lifecycle, policy, quarantine rules. | Does it emit or support receipts without bypassing RAW → WORK / QUARANTINE? |
| [`policy/`](./policy/) | Shared internal policy-support adapters. | Top-level `policy/`, policy tests, contracts, schemas. | Does it consume policy outputs without redefining policy truth? |

### Package-adjacent governed objects

| Object family | Stronger home | Typical package relationship |
| --- | --- | --- |
| `SourceDescriptor` | `contracts/`, `schemas/`, `data/registry/` | `ingest/` consumes source identity and activation posture. |
| `IngestReceipt`, `ValidationReport` | `contracts/`, `schemas/`, `data/receipts/`, `data/proofs/` | `ingest/` may emit or validate process memory. |
| `DatasetVersion` | `contracts/`, `schemas/`, `data/processed/` | `catalog/` and `indexers/` consume stable processed state. |
| `EvidenceRef`, `EvidenceBundle` | `contracts/`, `schemas/`, governed API, Evidence Drawer | `evidence/` resolves and packages support for runtime surfaces. |
| `DecisionEnvelope`, `PolicyDecision` | `policy/`, `contracts/`, `schemas/` | `policy/` package helpers may normalize outcomes and obligations. |
| `ReleaseManifest`, `CatalogMatrix`, `LayerManifest` | `release/`, `data/catalog/`, `contracts/`, `schemas/` | `catalog/` and `indexers/` may build or validate release-linked derivatives. |
| `RuntimeResponseEnvelope`, `AIReceipt` | governed API / runtime contract surfaces | Packages may support structured emission; they must not publish model output directly. |
| `CorrectionNotice`, `RollbackReference` | release, correction, and docs/runbook surfaces | Packages should carry references forward, not erase correction memory. |

[Back to top](#top)

---

## Boundary rules

### What makes a good package

A good KFM package usually has:

- one crisp responsibility
- stable dependency direction
- README-local accepted inputs and exclusions
- tests or fixtures near the logic they prove
- explicit dependency on top-level contracts, schemas, and policy where relevant
- bounded negative outcomes for unsupported or policy-blocked behavior
- no silent authority claims beyond its layer
- migration and rollback notes when downstream consumers change

### What should stay at the top level

Even when package code supports these surfaces, the authoritative versions stay outside `packages/`:

- API contracts
- shared schemas
- policy bundles and policy fixtures
- governed data artifacts
- catalog outputs
- release-bearing manifests, receipts, and proof objects
- deployment and environment definitions
- documentation doctrine, ADRs, and runbooks

### Policy overlap rule

`packages/policy/` may help runtime and pipeline code carry policy outcomes consistently. It must not become a shadow `policy/` directory. If the same rule exists both as package code and top-level policy, the package is the adapter and the top-level policy surface is the authority.

### Evidence overlap rule

`packages/evidence/` may resolve, shape, validate, or summarize support packages. It must not become a hidden evidence store or a browser-accessible bypass around the governed API.

### Indexer overlap rule

`packages/indexers/` produces rebuildable projections. Search indexes, tiles, embeddings, graph projections, PMTiles, COG derivatives, cached descriptors, and summaries are not sovereign truth.

### Ingest overlap rule

`packages/ingest/` supports source intake. It must not publish, promote, or serve outputs. Failed, sensitive, rights-unclear, or malformed inputs must remain visible through quarantine, receipts, validation reports, or denial states.

### Runtime overlap rule

Package helpers may be runtime-adjacent, but direct client traffic belongs behind governed APIs. A package must not become a direct model-client path, a browser-accessible evidence bypass, or an unpublished-data gateway.

[Back to top](#top)

---

## Trust membrane checks

Before merging a package change, ask:

| Check | Pass condition |
| --- | --- |
| Raw data access | No normal public/UI path reaches RAW, WORK, QUARANTINE, canonical stores, or unpublished candidates. |
| Evidence resolution | Consequential claims resolve `EvidenceRef` → `EvidenceBundle` or return a bounded negative state. |
| Policy outcome | Policy-denied, restricted, sensitive, stale, unavailable, or uncertain inputs do not silently become public outputs. |
| Derived outputs | Indexes, tiles, embeddings, graph projections, summaries, and caches are rebuildable and release-linked. |
| Release memory | Receipts, proofs, catalogs, manifests, review records, corrections, and rollback references remain in their owning lanes. |
| AI boundary | Package code does not expose direct model calls or treat generated language as proof. |
| UI boundary | Package code does not strip trust cues required by Evidence Drawer, Focus Mode, layer manifests, or governed API envelopes. |

[Back to top](#top)

---

## Definition of done

A `packages/` change is done enough to support stronger claims only when the checked items below are true in the active repository.

- [ ] KFM meta block has a real `doc_id`, verified created date, verified policy label, and valid related links.
- [ ] CODEOWNERS coverage is confirmed for changed package paths.
- [ ] Parent `packages/README.md` and affected child README are updated together.
- [ ] Package purpose, accepted inputs, exclusions, and stronger authority surfaces are explicit.
- [ ] Package manifest and test runner are directly inspected before install/build/test commands are documented.
- [ ] Package-local tests or fixtures exist when implementation code exists.
- [ ] Package does not define canonical schemas, policy law, release records, data lifecycle artifacts, public routes, or app entrypoints by accident.
- [ ] Package does not create a normal public path to RAW, WORK, QUARANTINE, canonical stores, model runtimes, vector indexes, or unpublished candidates.
- [ ] Package handles `ABSTAIN`, `DENY`, `ERROR`, stale, restricted, generalized, unavailable, and review-required states where its boundary can encounter them.
- [ ] Any emitted receipt, proof, manifest, catalog closure, or layer descriptor stays in its owning lifecycle or release lane.
- [ ] Changes that affect downstream imports include migration notes and rollback steps.
- [ ] Documentation avoids upgrading README presence into implementation maturity.

[Back to top](#top)

---

## FAQ

### Is `packages/` where KFM truth lives?

No. `packages/` can implement reusable logic, but KFM truth remains governed through source identity, evidence, policy, lifecycle state, catalog closure, release manifests, review records, and correction lineage.

### Can package code call RAW or canonical stores?

Only through approved internal paths that preserve lifecycle and policy boundaries. Package code must not create a normal public or UI path to RAW, WORK, QUARANTINE, canonical stores, unpublished candidates, or model runtimes.

### Can a package publish a result if its tests pass?

No. Passing package tests is evidence, not publication authority. Publication requires validation, policy checks, review state where required, provenance, proof objects, release manifest, correction/rollback context, and governed promotion.

### Can `packages/policy/` define policy?

No. It may normalize or adapt policy outputs for shared package use. The repo-authoritative policy surface remains `../policy/` and its linked fixtures and tests.

### Can packages contain AI helpers?

Yes, but only as evidence-subordinate, provider-neutral helpers behind governed API boundaries. They must not read unpublished stores directly, receive direct client traffic, or publish uncited model output.

### Why are most implementation claims still `UNKNOWN`?

Because README-visible package directories do not prove manifests, source files, tests, import graphs, CI gates, runtime behavior, package publishing, or deployment. Those require direct checkout, file, test, workflow, or runtime evidence.

[Back to top](#top)

---

## Appendix

<details>
<summary>Verification backlog</summary>

| Item | Why it matters | Suggested evidence |
| --- | --- | --- |
| Parent README replacement | Confirms this file is no longer a placeholder. | Direct `git show HEAD:packages/README.md` or PR diff. |
| Child package inventory | Prevents stale package map. | `find packages -maxdepth 2 -type d \| sort`. |
| Package-local code depth | Prevents README-only surfaces from being described as implemented packages. | `find packages/<name> -maxdepth 4 -type f \| sort`. |
| Package manager | Needed before documenting install/build commands. | Lockfiles, package manifests, CI workflows. |
| Test runner | Needed before claiming validation. | Local test config and passing test output. |
| Import graph | Needed before claiming downstream consumers. | Static imports, package exports, tests, runtime docs. |
| Schema home | Prevents `contracts/` vs `schemas/` drift. | ADR, object map, validation fixtures. |
| Policy toolchain | Needed before claiming OPA/Rego/Conftest or equivalent enforcement. | Policy tests, tool versions, workflow logs. |
| Release artifact storage | Needed before saying packages emit release evidence. | Generated receipts, proofs, manifests, catalogs, release dry-run logs. |
| Local exposure posture | Package helpers may touch runtime-adjacent boundaries. | Deployment docs, reverse proxy/VPN config, CORS/auth/secrets evidence. |

</details>

<details>
<summary>Glossary</summary>

| Term | Meaning in this README |
| --- | --- |
| Package boundary | A reusable internal module seam under `packages/`, not a deployable product surface. |
| Trust membrane | KFM boundary preventing public clients, UI surfaces, and model runtimes from bypassing governed evidence and policy flow. |
| EvidenceRef | Stable reference to support material that must resolve to an EvidenceBundle before consequential claims. |
| EvidenceBundle | Inspectable support package carrying source, scope, lineage, rights, review, freshness, release, and correction context. |
| Finite outcome | A bounded result such as `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |
| Rebuildable projection | Derived search, tile, graph, vector, cache, embedding, or summary output that can be regenerated from governed release inputs. |
| Shadow authority | Duplicate policy, schema, data, release, or evidence meaning hidden inside package code. |
| Promotion | Governed state transition into public-safe release, not a file move or package test success. |

</details>

<details>
<summary>Revision notes for this README version</summary>

- Strengthened the parent directory contract and quick decision path.
- Added at-a-glance, placement, maintainer workflow, change impact, and trust membrane sections.
- Tightened truth posture to avoid treating README text as implementation proof.
- Preserved child package map, object-family handoffs, Mermaid diagram, verification backlog, and glossary.
- Kept all package claims bounded pending active checkout inspection.

</details>

[Back to top](#top)
