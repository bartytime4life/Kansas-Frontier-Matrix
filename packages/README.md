<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/795bfcc7-71af-4d02-a69b-19a97007d799
title: packages/README — Versioned, testable modules
type: standard
version: v3
status: draft
owners: KFM Maintainers (set via CODEOWNERS)
created: 2026-02-25
updated: 2026-03-01
policy_label: public
related:
  - ../README.md
  - ../docs/
  - ../apps/
  - ../contracts/
  - ../configs/
  - ../policy/
tags:
  - kfm
  - monorepo
  - packages
  - layering
  - trust-membrane
  - promotion-contract
  - evidence-first
notes:
  - Directory-level contract for packages/ aligned to KFM invariants (truth path, trust membrane, evidence-first UX, cite-or-abstain).
  - Adds a controlled vocabulary section for governance-bearing fields so policy/tests can fail closed without guessing.
  - Keeps language/toolchain-agnostic patterns; does not claim specific modules exist until verified in-repo.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# packages/
Versioned, testable modules for the Kansas Frontier Matrix (KFM) monorepo.

**Purpose:** Keep core system logic **reusable**, **reviewable**, and **governed** by enforcing clear module boundaries.  
**Status:** draft • **Owners:** set via `CODEOWNERS` • **Policy:** public (docs)  
**Posture:** default-deny • fail-closed • evidence-first • cite-or-abstain • reproducible by digest

![status](https://img.shields.io/badge/status-draft-yellow)
![scope](https://img.shields.io/badge/scope-monorepo_packages-blue)
![governance](https://img.shields.io/badge/governance-fail--closed-critical)
![trust-membrane](https://img.shields.io/badge/trust_membrane-enforced-important)
![promotion-contract](https://img.shields.io/badge/promotion_contract-gates_A--G-critical)
![evidence-first](https://img.shields.io/badge/evidence_first-required-6f42c1)

---

## Navigation
- [Stance and labeling](#stance-and-labeling)
- [Directory contract](#directory-contract)
- [Repo reality check](#repo-reality-check)
- [How packages map to KFM architecture](#how-packages-map-to-kfm-architecture)
- [Canonical package taxonomy](#canonical-package-taxonomy)
- [Directory layout](#directory-layout)
- [Packages registry](#packages-registry)
- [Package manifest contract](#package-manifest-contract)
- [Controlled vocabularies](#controlled-vocabularies)
- [Dependency rules](#dependency-rules)
- [Testing, builds, and CI expectations](#testing-builds-and-ci-expectations)
- [Security and compliance](#security-and-compliance)
- [Adding a new package](#adding-a-new-package)
- [Definition of Done](#definition-of-done)
- [Glossary](#glossary)

---

## Stance and labeling

To preserve the trust membrane and avoid “doc hallucinations,” this README uses three labels:

- **CONFIRMED**: invariants/contracts KFM must enforce (safe to treat as requirements).
- **PROPOSED**: recommended defaults/patterns (adopt, adapt, or replace—document your mapping).
- **UNKNOWN**: anything about current repo state, deployments, or existing modules until verified.

> [!IMPORTANT]
> **This README must not be used to claim repo reality.** Any directory names below are **patterns** unless you verify them under [Repo reality check](#repo-reality-check).
>
> This aligns with KFM’s documented guidance: do not assert specific sub-packages exist until verified in the live repo.

[Back to top](#top)

---

## Directory contract

### Where this fits in the repo
`packages/` is the **module layer** between:
- **apps/** (runnable user/operator surfaces), and
- **infra/** / runtime substrates, and
- **data/** / truth-path artifacts and catalogs, and
- **policy/** / policy-as-code bundles.

Packages are where we keep the reusable building blocks so apps and services do not copy/paste logic.

### Acceptable inputs (what belongs here)
✅ Independently testable modules with:
- a clear **public API** (what other code imports)
- an owner and lifecycle status
- tests (unit minimum; integration if it does I/O)
- explicit dependency boundaries (domain/usecase/adapters/etc.)
- policy-safe behavior where relevant (deny/abstain on uncertainty)

Examples of acceptable package categories:
- **Domain**: types, invariants, ID rules, canonical hashing helpers (no I/O)
- **Use cases**: orchestration workflows (policy-aware; no direct storage)
- **Adapters**: repository implementations for storage/indexing behind interfaces
- **Contracts**: schema/profile validators and DTO types
- **Policy**: policy decision client types + obligation handling (display + enforcement boundaries)
- **Evidence**: EvidenceRef/EvidenceBundle types + resolver client contract
- **Geo**: geospatial utilities (projection, bounds, tiling math)
- **Observability**: logging/tracing helpers (policy-safe by default)
- **UI components**: shared evidence drawer/receipt viewer components (if your repo shares UI as packages)

### Exclusions (what must NOT go in `packages/`)
❌ Raw datasets, processed artifacts, catalogs, or audit ledgers (those belong under `data/` truth-path zones)  
❌ Secrets, tokens, `.env` files, kubeconfigs, private keys  
❌ Build artifacts (`dist/`, `build/`, `target/`, coverage outputs)  
❌ “Misc” scripts without tests and ownership (put in `tools/` or `scripts/`)  
❌ Direct-to-storage patterns from UI clients (trust membrane violation)

> [!WARNING]
> If a package enables bypassing the governed API/policy boundary (e.g., ships DB/object-store clients for browser code), treat it as a **security and governance defect**.

[Back to top](#top)

---

## Repo reality check

This README describes a **target posture** (**CONFIRMED**) plus **recommended patterns** (**PROPOSED**). Before treating any statement as “repo-present,” verify in-repo.

Minimum checks (recommended):

- [ ] Capture repo commit hash + root directory tree (`git rev-parse HEAD` and `tree -L 3`).
- [ ] Confirm the actual list of packages under `packages/`.
- [ ] Confirm the workspace/toolchain boundary (pnpm/yarn/npm/bazel/poetry/uv/go workspaces/etc.).
- [ ] Extract CI gate list from `.github/workflows` and document which checks are merge-blocking.
- [ ] Confirm the policy pack location and that **policy fixtures outcomes match CI and runtime semantics**.
- [ ] Confirm evidence resolution surfaces (route/service) exist and are merge-blocking for Story/Focus citations.

Suggested commands:

```bash
# Capture repo identity + tree snapshot (recommended baseline)
git rev-parse HEAD
tree -L 3

# Inspect package top-level directories
find packages -maxdepth 2 -type d -print

# Optional: identify workspace boundaries/tooling
ls -la pnpm-workspace.yaml yarn.lock package-lock.json turbo.json nx.json Cargo.toml go.work pyproject.toml 2>/dev/null || true

# Optional: list package manifests (language-dependent)
find packages -maxdepth 3 -name 'package.json' -o -name 'pyproject.toml' -o -name 'go.mod' -o -name 'Cargo.toml'
```

> [!NOTE]
> If your repo is multi-language, keep package ownership and dependency rules explicit—otherwise the trust membrane becomes “best effort.”

[Back to top](#top)

---

## How packages map to KFM architecture

Packages should reflect KFM’s layered model so governance is enforceable.

```mermaid
flowchart LR
  subgraph Domain["Domain (no I/O)"]
    domain[packages/domain]
  end

  subgraph UseCases["Use cases (policy-aware workflows)"]
    usecases[packages/usecases]
  end

  subgraph Interfaces["Interfaces (contracts + policy + ports)"]
    contracts[contracts/ + packages/* contract helpers]
    policyPkg[packages/policy]
    evidencePkg[packages/evidence]
  end

  subgraph Infrastructure["Infrastructure (I/O behind interfaces)"]
    adapters[packages/adapters]
    ingest[packages/ingest]
    indexers[packages/indexers]
    exports[packages/exports]
  end

  domain --> usecases
  usecases --> policyPkg
  usecases --> evidencePkg
  usecases --> adapters
  adapters --> contracts
  ingest --> adapters
  indexers --> adapters
  exports --> adapters
```

**Rule of thumb (CONFIRMED posture):**
- Dependency direction flows **inward** (toward domain).
- I/O and vendor SDKs live **only** behind adapters.
- Apps and external clients consume **governed APIs**, not storage clients.
- Domain logic does not talk directly to infrastructure—only through interfaces.

### Policy-as-code: PDP vs PEP (alignment note)
- **PDP (Policy Decision Point)**: policy engine (OPA/Rego or equivalent) that makes allow/deny + obligations decisions.
- **PEPs (Policy Enforcement Points)** exist at:
  - CI (merge-blocking policy + schema/contract tests),
  - Runtime API (before serving data),
  - Evidence resolver (before resolving evidence bundles),
  - **NOT** in UI (UI shows badges/notices but must not decide policy).

[Back to top](#top)

---

## Canonical package taxonomy

> [!NOTE]
> The taxonomy below is **PROPOSED** as a boundary strategy. If your repo uses different names, map them explicitly and enforce the same dependency rules.

KFM’s repo layout (design intent) typically includes these package groups:

- `packages/domain/` — canonical IDs, spec hashing, core types
- `packages/usecases/` — orchestration workflows (promotion, evidence resolution, story flows)
- `packages/adapters/` — repository implementations (storage/indexing), behind interfaces
- `packages/ingest/` — connectors and acquisition helpers (never “ship” without rights/sensitivity metadata)
- `packages/indexers/` — rebuildable projections (search/graph/tiles)
- `packages/exports/` — governed export packaging (policy + rights enforcement)
- `packages/stories/` — Story Node schema/helpers/renderers
- `packages/focus/` — Focus Mode planner/eval harness hooks (cite-or-abstain)
- `packages/evidence/` — EvidenceRef/EvidenceBundle types + resolver client
- `packages/catalog/` — DCAT/STAC/PROV builders + validators + linkcheck helpers
- `packages/policy/` — policy client types + obligation models + enforcement helpers
- `packages/geo/` — geo math + bounds + safe generalization utilities
- `packages/observability/` — logs/metrics/tracing helpers, policy-safe
- `packages/ui-components/` — shared UI components (EvidenceDrawer, ReceiptViewer), if used
- `packages/shared/` — small shared utilities (keep it small; avoid “god package”)

> [!IMPORTANT]
> Taxonomy is about enforceable boundaries. If boundaries are “social only” (not machine-enforced), they will be violated under deadline pressure.

[Back to top](#top)

---

## Directory layout

> [!NOTE]
> This structure is **PROPOSED**. Use it as a template; confirm/adjust based on repo reality.

### Minimal skeleton (recommended)
```text
packages/
├─ README.md
├─ registry/
│  ├─ README.md
│  ├─ packages.v1.json
│  ├─ schemas/
│  └─ fixtures/
├─ domain/
├─ usecases/
├─ adapters/
├─ ingest/
├─ indexers/
├─ exports/
├─ stories/
├─ focus/
├─ evidence/
├─ catalog/
├─ policy/
├─ geo/
├─ observability/
├─ ui-components/
└─ shared/
```

<details>
  <summary><strong>Expanded reference layout (illustrative; not repo-asserted)</strong></summary>

```text
packages/                                                      # Versioned, testable modules (clean layering) + package registry
├─ README.md                                                   # Packages directory contract + navigation
│
├─ registry/                                                   # Machine-readable registry + schemas + fixtures (small, CI-friendly)
│  ├─ README.md                                                # How the registry works + validation rules (fail-closed)
│  ├─ packages.v1.json                                         # Canonical packages registry (paths, layers, owners, constraints)
│  ├─ schemas/                                                 # Schemas that validate registry + per-package manifests
│  │  ├─ packages_registry.v1.schema.json                      # Schema for packages.v1.json
│  │  ├─ kfm_package_manifest.v1.schema.json                   # Schema for per-package kfm.package.json (recommended)
│  │  └─ dependency_rules.v1.schema.json                       # Schema for boundary/dependency rules (optional)
│  └─ fixtures/                                                # Registry fixtures for CI (valid/invalid; synthetic)
│     ├─ valid/                                                # Valid examples that should pass schema + rules
│     │  ├─ packages.v1.min.json                               # Small valid registry fixture
│     │  ├─ packages.v1.full.json                              # Full valid registry fixture (covers all fields)
│     │  └─ kfm.package.valid.json                             # Valid per-package manifest fixture
│     └─ invalid/                                              # Invalid examples that MUST fail (prove gates)
│        ├─ packages.v1.missing_owner.json                     # Invalid: no owners
│        ├─ packages.v1.bad_layer.json                         # Invalid: unknown layer
│        ├─ packages.v1.cycle.json                             # Invalid: dependency cycle
│        └─ kfm.package.invalid.json                           # Invalid: bad policy_label / missing required fields
│
├─ domain/                                                     # Core concepts + invariants (NO I/O)
│  ├─ README.md                                                # Package overview + invariants + usage
│  ├─ kfm.package.json                                         # Package manifest (policy_label, owners, deps, contracts)
│  ├─ CHANGELOG.md                                             # Optional but recommended (governed changes log)
│  ├─ src/                                                     # Implementation (pure domain)
│  ├─ test/                                                    # Tests for domain invariants
│  └─ fixtures/                                                # Small fixtures used by tests (safe + deterministic)
│
├─ usecases/                                                   # Orchestration (policy-aware; uses ports/repositories)
├─ adapters/                                                   # I/O implementations behind ports (storage/index/policy clients)
├─ ingest/                                                     # Acquisition + normalization helpers (rights/sensitivity-aware)
├─ indexers/                                                   # Rebuildable projections (search/graph/tiles); never canonical truth
├─ exports/                                                    # Governed exports packaging (rights + policy enforced)
├─ stories/                                                    # Story Node schema/helpers/renderers (evidence-first)
├─ focus/                                                      # Focus Mode planner/retrieval/cite-verify + eval hooks
├─ evidence/                                                   # EvidenceRef/EvidenceBundle contracts + resolver helpers (client-side)
├─ catalog/                                                    # DCAT/STAC/PROV builders + validators + linkcheck
├─ policy/                                                     # Policy models + fixtures harness + obligation semantics
├─ geo/                                                        # Geo math + validation + safe generalization utilities
├─ observability/                                              # Logging/metrics/tracing helpers (policy-safe defaults)
├─ ui-components/                                              # Optional: shared UI building blocks
└─ shared/                                                     # Small shared utilities (keep small; avoid "god package")
```

</details>

> [!TIP]
> If a package has no tests and no owner, it’s not a package—it’s a liability. Keep the tree disciplined.

[Back to top](#top)

---

## Packages registry

A package is not “real” until it is registered (so CI can enforce boundaries without guessing).

### `packages/registry/packages.v1.json` (recommended shape)

This file enables:
- owner routing and enforcement
- dependency boundary checks
- policy label and data-access audits
- build/test graph generation

Example (illustrative):

```json
{
  "registry_version": "v1",
  "packages": [
    {
      "path": "domain",
      "package_id": "kfm.domain",
      "layer": "domain",
      "owners": ["kfm-engineering"],
      "policy_label": "public",
      "data_access": "none",
      "depends_on": [],
      "ci": {
        "required": ["lint", "test", "typecheck"],
        "optional": []
      }
    },
    {
      "path": "adapters",
      "package_id": "kfm.adapters",
      "layer": "adapters",
      "owners": ["kfm-platform"],
      "policy_label": "restricted",
      "data_access": "io-behind-interfaces",
      "depends_on": ["kfm.domain", "kfm.usecases", "kfm.contracts"],
      "ci": {
        "required": ["lint", "test", "integration"],
        "optional": ["contract-tests"]
      }
    }
  ]
}
```

> [!IMPORTANT]
> The registry should be treated as **governance-bearing**. Changes that alter `data_access`, `policy_label`, or dependency rules require stricter review.

> [!TIP]
> Optional hardening (PROPOSED): add a `registry_digest` (canonical JSON → sha256) and/or a `signature_ref` so CI can detect unauthorized drift in governance-bearing registries.

[Back to top](#top)

---

## Package manifest contract

To avoid language/tooling lock-in, KFM can use a **repo-standard** manifest file that sits alongside the language-native manifest (`package.json`, `pyproject.toml`, `go.mod`, etc.).

### Proposed `kfm.package.json` (optional but recommended)

```json
{
  "package_id": "kfm.catalog",
  "name": "KFM Catalog Helpers",
  "layer": "catalog",
  "policy_label": "public",
  "owners": ["kfm-engineering", "kfm-governance"],
  "public_api": {
    "entry_points": ["src/index.*"],
    "contracts_used": [
      "contracts/catalogs/dcat.profile.md",
      "contracts/catalogs/stac.profile.md",
      "contracts/catalogs/prov.profile.md"
    ]
  },
  "data_access": "none",
  "constraints": {
    "forbid_direct_storage_clients": true,
    "require_fixtures_for_contract_changes": true
  }
}
```

Minimum rules (recommended):
- `package_id`, `layer`, `owners`, and `policy_label` are required.
- packages that touch contract surfaces must declare `contracts_used`.
- packages that do I/O must declare `data_access` as `io-behind-interfaces` and must be owned by platform/engineering (as appropriate).

[Back to top](#top)

---

## Controlled vocabularies

> [!NOTE]
> KFM standardizes a small set of governance-bearing fields so policy, CI, and UI can interoperate **without guessing**.
> This section is **PROPOSED** as a starter set aligned to KFM vNext docs—treat changes as governed decisions.

### `policy_label` (access + sensitivity)
Starter set (recommended):
- `public`
- `public_generalized` (derived public version of sensitive data)
- `restricted`
- `restricted_sensitive_location` (default deny; precise locations protected)
- `internal`
- `embargoed`
- `quarantine` (not promotable: validation/rights unresolved)

### `artifact.zone` (truth path)
Starter set:
- `raw`
- `work`
- `processed`
- `catalog`
- `published`

### `citation.kind` (evidence types)
Starter set:
- `dcat`
- `stac`
- `prov`
- `doc`
- `graph`
- `oci` (optional future)
- `url` (discouraged; prefer resolvable schemes)

### `geometry.generalization_method` (when policy requires generalization)
Starter set:
- `centroid_only`
- `bounding_box_only`
- `dissolve_to_admin_unit`
- `grid_aggregation_<resolution>`
- `random_offset_<meters>`
- `none`

[Back to top](#top)

---

## Dependency rules

These rules are part of KFM’s **trust membrane** and must be enforceable in CI.

### Allowed directions (summary)
- `domain` → (no downward deps)
- `usecases` → `domain`
- `policy`, `evidence`, `catalog`, `stories`, `focus`, `geo`, `observability` → `domain` (+ sometimes `usecases` depending on repo design)
- `adapters`, `ingest`, `indexers`, `exports` → `domain` + `usecases` + contracts (implements I/O behind interfaces)
- `ui-components` → contracts/types only (never DB/storage clients)

### Forbidden dependencies (examples)
- ❌ `domain` importing adapters/infra clients
- ❌ `usecases` importing DB/object-store/index clients directly (must use repositories/adapters)
- ❌ `ui-components` importing server-only or privileged adapters
- ❌ “shared” becoming a dumping ground (if it grows, split it)

### Enforcement approaches (choose what fits your toolchain)
- dependency boundary checks (workspace graph rules)
- lint rules + allow/deny lists for imports
- CI grep checks for known bypass libraries (use sparingly; tune to reduce false positives)
- build tags / compilation boundaries (for multi-language repos)

> [!WARNING]
> If a package boundary is “social only” (not enforced), it will be violated under deadline pressure. Make it machine-enforced.

[Back to top](#top)

---

## Testing, builds, and CI expectations

Packages are only safe if they are continuously validated.

### Minimum expectations (recommended baseline)
- **Fast checks (required):**
  - formatting
  - lint
  - unit tests
  - typecheck (if applicable)
- **Contract checks (required when relevant):**
  - schema/profile validation (DCAT/STAC/PROV, EvidenceBundle, receipts)
  - linkcheck (EvidenceRefs resolvable under allowed policy)
- **Policy checks (required when relevant):**
  - policy fixtures parity (CI semantics match runtime semantics)
- **Security checks (required):**
  - secret scanning
  - dependency scanning (where supported)
  - license allow/deny checks (especially for export/ingest tooling)

> [!IMPORTANT]
> **Policy semantics must match between CI and runtime** (or at minimum the same fixtures and outcomes), otherwise CI guarantees are meaningless.

### Evidence resolution & citation gates (CONFIRMED posture)
- In KFM, a “citation” is not a pasted URL; it is an **EvidenceRef** that must resolve into an **EvidenceBundle** via the evidence resolver.
- **Hard gate:** Story publishing and Focus Mode must **fail closed**: if citations cannot be verified and are not policy-allowed, the system must abstain or reduce scope.
- CI should include:
  - citation linting/linkcheck for any package that publishes Story Nodes or answers Focus queries
  - fixtures + golden tests for resolver behaviors and policy outcomes

### Promotion Contract mapping (A–G)
Packages often implement gate logic even if gates run elsewhere.

#### Baseline (Promotion Contract v1)
| Gate | Typical package responsibilities |
|---|---|
| A: Identity & versioning | dataset ID rules, deterministic `spec_hash` helpers (`domain`, `catalog`) |
| B: Licensing & rights metadata | SPDX handling, attribution wiring (`catalog`, `exports`, `policy`) |
| C: Sensitivity classification & redaction plan | generalization helpers, obligation models (`policy`, `geo`, `exports`) |
| D: Catalog triplet validation | profile validators/builders + linkchecks (`catalog`, `contracts` helpers) |
| E: Run receipt & checksums | receipt writers/readers, digest utilities (`evidence`, `observability`, `adapters`) |
| F: Policy tests & contract tests | OPA tests + schema/contract tests + resolvable EvidenceRefs in CI (`policy`, `contracts`, `evidence`, `stories`, `focus`) |
| G: Optional but recommended (production posture) | SBOM/build provenance, perf + a11y smoke tests, supply-chain hardening (`observability`, `ui-components`, CI tooling) |

#### Common “explicit CI gates” (implementation choice)
Some KFM delivery plans also treat these as explicit merge-blocking checks (either as sub-gates or additional gates):
- **QA & thresholds** (dataset-specific QA reports and fail-closed thresholds; quarantine on failure)
- **Release manifest/tag** (promotion recorded as a release/promotion manifest referencing artifacts + digests)

> [!NOTE]
> Apps “display” trust. Packages often “compute” trust. Both must be consistent and fail closed.

[Back to top](#top)

---

## Security and compliance

- **No secrets in source control.** Treat violations as merge-blocking.
- **No policy bypass utilities.** Anything that enables bypassing governed APIs is a security issue.
- **Policy Enforcement Points (PEPs):** CI + runtime API + evidence resolver. UI does not decide policy; it only renders badges/notices.
- **Rights-aware exports.** Any export tooling must enforce:
  - rights metadata presence
  - attribution generation
  - policy label restrictions
- **Policy-safe errors.** Avoid “existence inference” leaks (e.g., distinguishable 403 vs 404) unless policy explicitly allows.

[Back to top](#top)

---

## Adding a new package

### Step-by-step
1. Choose the layer (`domain`, `usecases`, `adapters`, etc.).
2. Create the directory with:
   - `README.md`
   - language-native manifest (repo standard)
   - tests (`test/`)
   - optional `kfm.package.json`
3. Add the package to:
   - `packages/registry/packages.v1.json`
4. Add/verify boundary enforcement:
   - ensure dependencies follow [Dependency rules](#dependency-rules)
5. Add CI coverage:
   - at minimum: lint + unit tests
   - add contract/policy tests if the package touches contract surfaces

### Package README minimum
Each package README should state:
- purpose (one sentence)
- layer and boundaries (what it must not depend on)
- public API surface
- how to test locally
- ownership and escalation path
- policy and sensitivity posture (if relevant)

[Back to top](#top)

---

## Definition of Done

A package is “done” when:

- [ ] It appears in `packages/registry/packages.v1.json` with owner + layer + policy_label.
- [ ] It has a `README.md` with purpose, boundaries, and test instructions.
- [ ] It has tests (unit minimum; integration if it does I/O).
- [ ] It follows dependency rules and passes boundary checks in CI.
- [ ] If it affects promotion/serving behavior, it includes fixtures and contract/policy tests.
- [ ] It contains no secrets and does not enable trust membrane bypass.

[Back to top](#top)

---

## Glossary
- **Trust membrane:** enforced boundary where policy + provenance controls access; clients never access storage directly.
- **Truth path:** lifecycle of governed data: **RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED**.
- **Promotion Contract:** fail-closed gate set (A–G) that controls what becomes runtime-visible.
- **Contract surface:** schema/spec/profile that is versioned and machine-validated (OpenAPI, JSON Schema, DCAT/STAC/PROV).
- **Evidence-first:** every claim/layer/answer can open into rights, provenance, and validation evidence.
- **Cite-or-abstain:** if citations cannot be verified and policy-allowed, abstain or reduce scope.
- **PDP (Policy Decision Point):** policy engine that computes allow/deny + obligations.
- **PEP (Policy Enforcement Point):** component that blocks or shapes behavior based on policy (CI, API, evidence resolver).

---

<p align="right"><a href="#top">Back to top ↑</a></p>
