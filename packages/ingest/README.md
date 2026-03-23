# ingest
Governed source intake, normalization, validation, and receipt helpers for KFM’s truth path.

> **Status:** experimental  
> **Owners:** `@bartytime4life`  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![owner](https://img.shields.io/badge/owner-%40bartytime4life-blue) ![scope](https://img.shields.io/badge/scope-governed%20intake-0a7ea4) ![surface](https://img.shields.io/badge/surface-packages%2Fingest-2f81f7) ![tree](https://img.shields.io/badge/current%20tree-README--only-lightgrey)  
> **Path:** `packages/ingest/README.md`  
> **Repo fit:** child package beneath [`../README.md`](../README.md); constrained by [`../../data/registry/README.md`](../../data/registry/README.md), [`../../data/README.md`](../../data/README.md), [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md), and [`../../policy/README.md`](../../policy/README.md)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current package surface](#current-package-surface) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Object placement](#object-placement) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> The current public `main` branch confirms that `packages/ingest/` exists, but the visible package surface is still **README-only**.  
> This file therefore documents the **directory contract first** and keeps package-local implementation claims visibly bounded.

> [!WARNING]
> `packages/ingest/` is a **shared internal boundary**, not a direct runtime entrypoint.  
> It must not serve clients directly, bypass lifecycle gates, replace top-level contract or policy authority, or quietly become a second truth path.

> [!NOTE]
> In KFM, ingest is not “just fetching files.”  
> It is the shared seam where source admission, deterministic acquisition, normalization, validation, and receipt-bearing intake stay inspectable before anything can move downstream.

## Scope

`packages/ingest/` exists to hold **shared, non-deployable ingest law and helpers** that support KFM’s governed movement from source edge into lifecycle zones such as `RAW`, `WORK / QUARANTINE`, and `PROCESSED`.

This package is the right home for code that needs to be reused across more than one ingest lane or worker **without** taking over the stronger authority held elsewhere in the repository.

### Evidence posture used in this README

| Statement type | Posture | Meaning here |
|---|---|---|
| Current package path exists | **CONFIRMED** | Public `main` shows `packages/ingest/README.md` |
| Package role as “source intake, normalization, validation, and receipt helpers” | **CONFIRMED** | Parent `packages/README.md` names that role directly |
| Package-local code, manifests, tests, or fixtures already exist | **UNKNOWN / NEEDS VERIFICATION** | Not visible in the package path inspected during this rewrite |
| Shared helper responsibilities described below | **PROPOSED** | Directory contract aligned to current KFM doctrine and repo boundaries |
| Any direct runtime ownership or publication authority in this package | **EXCLUDED** | Would violate current parent-package and trust-path guidance |

### Working rule

If logic is:

- reusable across ingest lanes,
- internal rather than client-facing,
- clearly subordinate to top-level contracts, policy, and lifecycle surfaces,
- and naturally tied to deterministic intake, normalization, validation, or receipts,

then it probably belongs here.

If it changes public API behavior, owns canonical schemas, publishes directly, or hides policy decisions inside package-local convenience code, it probably belongs somewhere else.

[Back to top](#ingest)

## Repo fit

| Relationship | Path | Why it matters here | Current posture |
|---|---|---|---|
| Parent boundary | [`../README.md`](../README.md) | Defines what `packages/` is for and what each child package must not do | **CONFIRMED** |
| Upstream source registration | [`../../data/registry/README.md`](../../data/registry/README.md) | Governs dataset/source identity, onboarding, cadence, rights, and handoff intent | **CONFIRMED** |
| Upstream lifecycle zones | [`../../data/README.md`](../../data/README.md) | Owns the truth path and storage-zone semantics | **CONFIRMED** |
| Upstream contract surface | [`../../contracts/README.md`](../../contracts/README.md) | Owns machine-readable contract families and shared object grammar | **CONFIRMED** |
| Upstream schema surface | [`../../schemas/README.md`](../../schemas/README.md) | Holds schema authority questions that ingest must not duplicate casually | **CONFIRMED** |
| Upstream policy surface | [`../../policy/README.md`](../../policy/README.md) | Owns deny-by-default policy posture and policy-as-code boundary | **CONFIRMED** |
| Adjacent verification | [`../../tests/README.md`](../../tests/README.md) | Negative paths, fixtures, and proof drills should stay explicit | **CONFIRMED** |
| Adjacent operator tooling | [`../../tools/README.md`](../../tools/README.md) | Validators and support tooling belong here rather than inside hidden ingest logic | **CONFIRMED** |
| Adjacent operator scripts | [`../../scripts/README.md`](../../scripts/README.md) | Entry-point scripts may call ingest helpers, but should not own domain law | **CONFIRMED** |
| Adjacent workflow surface | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | CI/promotion gates are part of ingest truth, even when YAML inventory remains to be verified | **CONFIRMED** |
| Lateral sibling packages | [`../catalog/README.md`](../catalog/README.md) · [`../domain/README.md`](../domain/README.md) · [`../evidence/README.md`](../evidence/README.md) · [`../indexers/README.md`](../indexers/README.md) · [`../policy/README.md`](../policy/README.md) | Ingest should hand off cleanly without collapsing boundaries | **CONFIRMED** |
| Downstream catalog/runtime consumers | [`../../data/catalog/stac/README.md`](../../data/catalog/stac/README.md) · [`../../apps/`](../../apps/) | Ingest prepares material for later catalog and runtime use; it does not replace them | **CONFIRMED / INFERRED** |

### Repo-fit summary

`packages/ingest/` sits **between** source registration and lifecycle movement:

- it should begin from governed source intent,
- obey top-level contracts and policy,
- prepare deterministic intake artifacts,
- and hand off cleanly into lifecycle zones and later catalog/runtime surfaces.

It should **not** become a shadow registry, shadow policy engine, or shadow publication layer.

[Back to top](#ingest)

## Accepted inputs

The following material belongs here when it is **shared, reusable, and internal**.

| Input / content type | Belongs here? | Notes |
|---|---|---|
| Shared acquisition helpers | Yes | **PROPOSED** when reused across lanes and kept subordinate to descriptors and policy |
| Deterministic fetch/snapshot helpers | Yes | **PROPOSED**; should preserve source-native payloads and integrity metadata |
| Normalization and harmonization helpers | Yes | **PROPOSED**; explicit downstream transforms, not hidden inline mutations |
| Validation helpers used before promotion | Yes | **PROPOSED**; should consume top-level contracts/policy rather than redefine them |
| Receipt / manifest / checksum emitters | Yes | **PROPOSED**; high-value fit for this package when shared |
| Incremental-state helpers (cursor / high-water-mark / replay support) | Yes | **PROPOSED**; only when deterministic and reviewable |
| Package-local documentation for real helpers | Yes | **PROPOSED**; update this README as implementation becomes visible |
| Lane-specific one-off scripts | Usually no | Prefer `scripts/` for operator entrypoints and promote reusable logic back here only when justified |
| Client-facing HTTP handlers or UI code | No | Those belong in `apps/` |
| Canonical schema ownership | No | Stronger home is `contracts/` and/or `schemas/` |
| Canonical policy bundle ownership | No | Stronger home is `policy/` |
| Raw, work, processed, or published artifacts | No | Stronger home is `data/` |

### Typical accepted inputs, once implementation exists

- source-mode adapters shared across connectors,
- fetch parameter builders,
- acquisition metadata assemblers,
- integrity verification helpers,
- normalization pipelines that can replay from immutable inputs,
- receipt and validation emitters,
- safe retry / resume helpers,
- package-local utilities that reduce duplication **without** blurring authority.

## Exclusions

The following content does **not** belong in `packages/ingest/`.

| Excluded content | Why it does not belong here | Where it goes instead |
|---|---|---|
| Public API endpoints, route handlers, or direct UI entrypoints | This package is internal and non-deployable | `../../apps/` |
| Canonical JSON Schemas, OpenAPI contracts, shared vocabularies | Contract authority must stay top-level and reviewable | `../../contracts/` and `../../schemas/` |
| Executable policy bundles or policy decision logs | Policy authority must remain explicit and independently versioned | `../../policy/` |
| RAW / WORK / QUARANTINE / PROCESSED / CATALOG / PUBLISHED artifacts | Lifecycle zones are storage and release surfaces, not package internals | `../../data/` |
| Release manifests, proof packs, or promotion records | Promotion and release state must stay externally visible | designated top-level release / proof surfaces |
| Secrets, tokens, or provider credentials | Secrets must never live in package source | runtime secret management / environment wiring |
| “misc/common/utils” drift | KFM explicitly rejects vague authority mixing | keep boundaries sharp and promote only justified shared helpers |

### Red flags

If a proposed change would make this package:

- callable directly by clients,
- responsible for deciding publication visibility on its own,
- the sole place where rights/sensitivity logic lives,
- or the only place where a source can be understood,

stop and redesign the change before merging.

[Back to top](#ingest)

## Current package surface

This section describes **what is visible now**, not what the package may eventually contain.

| Surface | Status | Notes |
|---|---|---|
| `packages/ingest/README.md` exists | **CONFIRMED** | Current public tree shows the file |
| Package-local code under `packages/ingest/` | **UNKNOWN / NEEDS VERIFICATION** | Not visible in the inspected package path during this rewrite |
| Package-local tests / fixtures under this path | **UNKNOWN / NEEDS VERIFICATION** | No package-local inventory was visible here |
| Parent-package role statement | **CONFIRMED** | Parent docs name ingest as source intake, normalization, validation, and receipt helpers |
| Fallback owner for `/packages/` | **CONFIRMED** | `@bartytime4life` |
| Workflow enforcement specific to this package | **UNKNOWN / NEEDS VERIFICATION** | Current public workflow surface is README-first |

## Directory tree

### Current verified snapshot

```text
packages/ingest/
└── README.md
```

### Update rule

Keep this tree **strictly truthful**.

When real files land under this package:

1. update the tree in the same PR,
2. add only paths that are actually present,
3. keep generated artifacts out of this listing unless they are committed and intentionally owned here.

## Quickstart

Start by inspecting the package **in context**, not in isolation.

```bash
# 1) Read the package family contract first
sed -n '1,220p' packages/README.md

# 2) Read the immediate package contract
sed -n '1,260p' packages/ingest/README.md

# 3) Review the stronger authority surfaces this package must obey
sed -n '1,260p' data/registry/README.md
sed -n '1,260p' data/README.md
sed -n '1,260p' contracts/README.md
sed -n '1,260p' schemas/README.md
sed -n '1,260p' policy/README.md
sed -n '1,220p' tests/README.md
sed -n '1,220p' .github/workflows/README.md
```

Then inventory what is actually present under this path:

```bash
find packages/ingest -maxdepth 3 -print | sort
```

Search for the highest-value object families that ingest is expected to consume or emit:

```bash
grep -RInE 'SourceDescriptor|IngestReceipt|ValidationReport|DatasetVersion|CatalogClosure' \
  packages contracts schemas data tests docs . 2>/dev/null
```

Check whether any package-local manifests or module entrypoints already exist:

```bash
find packages/ingest -maxdepth 2 \
  \( -name 'package.json' -o -name 'pyproject.toml' -o -name 'Cargo.toml' -o -name '*.ts' -o -name '*.py' \) \
  -print | sort
```

> [!TIP]
> Do the inventory before promising structure changes.  
> In KFM, a tidy guess is worse than an untidy truth.

[Back to top](#ingest)

## Usage

### When logic belongs here

Add shared ingest logic here when all of the following are true:

- it is reused or is clearly headed toward reuse,
- it is internal rather than directly deployable,
- it improves deterministic intake, normalization, validation, or receipt emission,
- it does **not** weaken the stronger authority of `data/registry`, `contracts`, `schemas`, `policy`, or `data/`,
- and it can be tested without inventing a second governance model.

### When logic does **not** belong here

Keep it out of this package when it is:

- route or controller code,
- public-facing contract ownership,
- policy-bundle ownership,
- a one-off migration script,
- lane-specific operational glue with no reusable value,
- or a convenience shortcut that jumps past lifecycle stages.

### Add the first real ingest helper safely

1. Start from a governed source-registration or intake object, not a hard-coded fetch.
2. Preserve source-native capture and integrity metadata before normalization.
3. Keep normalization as an explicit downstream step that can replay from immutable input.
4. Emit or verify receipt-bearing artifacts rather than relying on logs alone.
5. Put tests and fixtures where reviewers expect them: top-level `tests/`, `contracts/`, and companion surfaces as appropriate.
6. Update this README and [`../README.md`](../README.md) when the visible package role changes.

### Working intake stages

| Stage | What helpers here may do | What helpers here must not do |
|---|---|---|
| Discover | Resolve source mode, parameters, and capability metadata | Redefine registry authority |
| Acquire | Fetch deterministically, snapshot, checksum, and record acquisition context | Mutate source-native payloads inline without trace |
| Normalize | Convert encoding, geometry, and temporal shape explicitly | Quietly replace canonical contract meaning |
| Validate | Run structural, temporal, geometry, and integrity checks | Act as the sole policy authority |
| Handoff | Prepare reviewable outputs for `RAW`, `WORK / QUARANTINE`, or `PROCESSED` flows | Publish directly to outward runtime surfaces |

## Diagram

```mermaid
flowchart LR
    SRC[Source edge] --> REG[data/registry]
    REG -. declares source intent .-> ING[packages/ingest]

    CON[contracts/ + schemas/] -. shape objects .-> ING
    POL[policy/] -. default-deny gates .-> ING

    ING --> RAW[data/ RAW]
    RAW --> WQ[data/ WORK / QUARANTINE]
    WQ --> PROC[data/ PROCESSED]
    PROC --> CAT[data/catalog/ DCAT + STAC + PROV]

    CAT --> APPS[apps/ + downstream surfaces]
    PROC --> EVID[packages/evidence]
    PROC --> IDX[packages/indexers]

    classDef strong fill:#eef7ff,stroke:#2f81f7,color:#0b1f33;
    classDef stage fill:#f6f8fa,stroke:#57606a,color:#24292f;
    classDef package fill:#eefaf1,stroke:#2da44e,color:#123b1d;

    class REG,CON,POL strong;
    class RAW,WQ,PROC,CAT stage;
    class ING,EVID,IDX package;
```

## Object placement

This section exists to prevent authority drift.

| Object family | Stronger home | `packages/ingest/` relationship |
|---|---|---|
| `SourceDescriptor` | `data/registry` + contract/schema surfaces | Consume, honor, and help apply; do not quietly redefine |
| `IngestReceipt` | shared contract / proof surfaces | Likely emitter or emitter helper once implementation exists |
| `ValidationReport` | contract + verification surfaces | Likely emit or enrich; must stay compatible with top-level review expectations |
| `DatasetVersion` | data / contract / release surfaces | Contribute inputs; do not become the sole owner of version law |
| `CatalogClosure` | catalog / contract surfaces | Handoff target, not package-local substitute |
| `DecisionEnvelope` / review objects | policy + review surfaces | Consume or reference; do not replace steward decision paths |
| `EvidenceBundle` / runtime envelopes | evidence + runtime surfaces | Downstream consumers of ingest consequences, not objects this package should own in isolation |

### Placement principle

`packages/ingest/` should make intake **possible and consistent**.  
It should not make every trust-bearing object **belong** here.

[Back to top](#ingest)

## Task list / definition of done

A meaningful change to this package is done when:

- [ ] the actual tree under `packages/ingest/` is reflected truthfully in this README,
- [ ] the change clearly belongs to a shared internal ingest boundary,
- [ ] source registration / source intent remains explicit rather than hard-coded,
- [ ] deterministic acquisition or replay semantics are visible,
- [ ] checksum, manifest, receipt, or validation behavior is explicit where relevant,
- [ ] no-op, quarantine, and failure states are not silently collapsed,
- [ ] top-level contract, schema, policy, and lifecycle authority remains intact,
- [ ] tests and fixtures land in predictable review surfaces,
- [ ] parent-package documentation still reads correctly after the change.

> [!IMPORTANT]
> “The code works” is not enough.  
> In KFM, ingest is done when the path is still inspectable after the code works.

## FAQ

### Is this where connectors live?

Shared connector logic may live here.  
Deployable workers, CLI entrypoints, or service-specific orchestration should stay in `apps/`, `scripts/`, or other explicit runtime surfaces.

### Should `SourceDescriptor` or `IngestReceipt` schemas live here?

No.  
This package may consume or emit those object families, but the stronger authority for their public shape is top-level contract/schema space.

### Can this package write directly to `PUBLISHED` or to client-facing surfaces?

No.  
This package supports intake and handoff. Publication remains a governed downstream state, not a package shortcut.

### Why not keep this logic in `scripts/`?

Because scripts are operator entrypoints, not a durable home for shared ingest law.  
If behavior is reusable and important, it should be promoted into a package with tests and documentation.

[Back to top](#ingest)

## Appendix

<details>
<summary><strong>Review questions before adding code here</strong></summary>

1. Does this helper start from a governed source description or other explicit intake contract?
2. Can the flow replay from immutable source capture without hand editing?
3. Are checksum, manifest, receipt, and validation seams explicit?
4. Does the helper preserve source-native packaging before normalization?
5. Are rights, sensitivity, and generalization burdens still visible from outside this package?
6. Does the code keep no-op, quarantine, and failure outcomes legible?
7. Would moving this logic into a deployable app make the trust story clearer? If yes, this package may not be the right home.
8. Can a new contributor tell, quickly, whether this code is shared ingest law or just incidental glue?

</details>

<details>
<summary><strong>Open unknowns to retire before claiming maturity</strong></summary>

- Whether package-local code, manifests, or tests already exist outside the currently visible public tree.
- Whether workflow YAML already enforces package-specific schema, policy, or receipt checks.
- Whether a first-wave contract set for ingest objects is already mounted elsewhere in the repo.
- Whether sibling packages already consume ingest-facing helpers or only document the intended split.

</details>
