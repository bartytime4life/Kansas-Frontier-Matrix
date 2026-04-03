<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-NEEDS-VERIFICATION>
title: Policy Runtime
type: standard
version: v1
status: draft
owners: @bartytime4life
created: 2026-03-22
updated: 2026-04-03
policy_label: public
related: [../README.md, ../bundles/README.md, ../bundles/runtime/README.md, ../fixtures/README.md, ../tests/README.md, ../../tests/README.md, ../../tests/policy/README.md, ../../contracts/README.md, ../../schemas/README.md, ../../packages/policy/README.md, ../../apps/api/src/api/README.md, ../../.github/workflows/README.md]
tags: [kfm, policy, runtime]
notes: [doc_id placeholder pending repo-backed document registry verification, created date grounded in current public file history on main, updated date reflects this draft revision and should be reconciled to the actual merge date if committed later, owner grounded in .github/CODEOWNERS, current packages/policy neighbor confirmed on public main, dedicated packages/policy-runtime path remains unverified]
[/KFM_META_BLOCK_V2] -->

# Policy Runtime

_Runtime-facing policy semantics, decision coordination, and CI/runtime parity for KFM trust-bearing responses, publication decisions, and visible negative states._

> **Status:** experimental  
> **Owners:** `@bartytime4life`  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![owners](https://img.shields.io/badge/owners-%40bartytime4life-blue) ![surface](https://img.shields.io/badge/surface-policy%2Fruntime-1f6feb) ![posture](https://img.shields.io/badge/posture-deny--by--default-critical) ![outcomes](https://img.shields.io/badge/runtime-finite_outcomes-6f42c1) ![inventory](https://img.shields.io/badge/public_main-README--first-lightgrey)
>
> **Repo fit:** `policy/policy-runtime/README.md`  
> **Upstream:** [`../README.md`](../README.md)  
> **Adjacent policy + proof lanes:** [`../bundles/README.md`](../bundles/README.md), [`../bundles/runtime/README.md`](../bundles/runtime/README.md), [`../fixtures/README.md`](../fixtures/README.md), [`../tests/README.md`](../tests/README.md), [`../../tests/policy/README.md`](../../tests/policy/README.md), [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md)  
> **Current shared/runtime neighbors:** [`../../packages/policy/README.md`](../../packages/policy/README.md), [`../../apps/api/src/api/README.md`](../../apps/api/src/api/README.md), [`../../.github/workflows/README.md`](../../.github/workflows/README.md)
>
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#runtime-policy-shape) · [Tables](#boundary-matrix) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> This directory is a **runtime-policy documentation and coordination seam**.
>
> It does **not** prove:
> 1. a mounted policy decision point,
> 2. a route-handling runtime implementation,
> 3. a shared internal helper package beyond the repo-visible `packages/policy/` boundary, or
> 4. a dedicated `packages/policy-runtime/` split.
>
> Keep a hard boundary between:
> - **top-level policy artifacts** such as rule packs, fixtures, and policy tests,
> - **shared internal policy-support helpers** that may live in [`../../packages/policy/README.md`](../../packages/policy/README.md),
> - **governed API/runtime entrypoints** that belong in verified app surfaces such as [`../../apps/api/src/api/README.md`](../../apps/api/src/api/README.md), and
> - **any future dedicated runtime package split**, which remains **PROPOSED / NEEDS VERIFICATION** until the active branch proves it.

---

## Scope

`policy/policy-runtime/` documents how KFM policy behaves **at request time and at release-significant runtime seams**.

This README exists to keep the policy/runtime boundary inspectable. It is the place to describe:

- finite runtime outcomes
- decision/result grammar
- reason and obligation vocabulary expectations
- CI/runtime semantic parity
- explainability and audit-link expectations
- handoff points between policy bundles, fixtures, tests, contracts, schemas, shared internal policy helpers, and outward API/runtime envelopes

### Status posture used here

| Label | Meaning in this directory |
|---|---|
| **CONFIRMED** | Present in the current public repo snapshot or explicitly established by attached doctrinal material. |
| **INFERRED** | Strongly implied by nearby docs and directory relationships, but not directly proven as mounted implementation. |
| **PROPOSED** | Recommended structure or operating rule that fits KFM doctrine and current repo patterns. |
| **UNKNOWN** | Not verified from the current public repo surfaces or attached corpus. |
| **NEEDS VERIFICATION** | Review item before treating this README as implementation truth. |

[Back to top](#policy-runtime)

---

## Repo fit

### Why this README exists

The public repo exposes `policy/` as a first-class top-level area, and the current `main` branch also exposes a dedicated `policy/policy-runtime/` subtree. At the same time, adjacent policy, package, API, and test docs repeatedly warn against converting documentation seams into unverified implementation claims.

That makes this file responsible for one thing above all:

**keeping the runtime-policy boundary explicit without pretending the mounted runtime is already proven.**

### Current public-main snapshot

| Path | Role here | Confidence |
|---|---|---|
| `policy/policy-runtime/README.md` | This boundary and coordination document | **CONFIRMED** |
| `policy/bundles/README.md` | Bundle-lane directory contract and executable-rule placement guidance | **CONFIRMED** |
| `policy/bundles/runtime/README.md` | Runtime bundle subtree scaffold | **CONFIRMED path / scaffold-only current snapshot** |
| `policy/fixtures/README.md` | Policy fixture lane | **CONFIRMED path / README-only current snapshot** |
| `policy/tests/README.md` | Bundle-local policy assertion lane | **CONFIRMED path / README-only current snapshot** |
| `tests/policy/README.md` | Repo-facing policy behavior proof lane | **CONFIRMED path / README-only current snapshot** |
| `../../contracts/README.md` | Stronger working signal for machine-readable trust-bearing contracts | **CONFIRMED** |
| `../../schemas/README.md` | Secondary schema surface with explicit drift cautions | **CONFIRMED** |
| `../../packages/policy/README.md` | Current shared internal policy-support boundary | **CONFIRMED path / README-only current snapshot** |
| `../../apps/api/src/api/README.md` | Current governed API enforcement boundary for outward runtime surfaces | **CONFIRMED path / draft boundary README** |
| `../../.github/workflows/README.md` | Workflow policy/documentation seam; current public `main` shows README only | **CONFIRMED path / README-only current snapshot** |
| `packages/policy-runtime/` | Sometimes implied as a future dedicated runtime package split | **PROPOSED / NEEDS VERIFICATION** |

### Current verification delta worth carrying forward

This revision preserves the strong boundary-first shape of the checked-in file, but it sharpens two repo-visible neighbors that are easy to under-model:

- **`packages/policy/` is current and real** as the shared internal policy-support boundary.
- **`apps/api/src/api/` is current and real** as the governed API enforcement boundary for outward runtime behavior.

That means this README should no longer force every runtime-adjacent implementation thought into a single future `packages/policy-runtime/` seam. The repo already shows a better current distinction:

- top-level `policy/` explains and governs policy,
- `packages/policy/` may hold shared internal policy-support helpers,
- `apps/api/src/api/` owns outward route and enforcement behavior,
- and any dedicated `packages/policy-runtime/` split remains a future boundary decision until proven.

### Practical interpretation

Use this directory to explain runtime policy behavior and to point maintainers to the correct artifact homes.

Do **not** use it to imply that the repo already contains:

- a mounted policy decision point,
- request-time bundle loaders,
- live OPA/Rego wiring,
- merge-blocking runtime policy workflows on the current public branch,
- or a verified `packages/policy-runtime/` implementation.

Also do **not** use this directory to blur the current difference between:

- `policy/policy-runtime/` as a **documentation and coordination seam**,
- `packages/policy/` as a **shared internal support boundary**,
- and `apps/api/src/api/` as a **governed outward enforcement boundary**.

[Back to top](#policy-runtime)

---

## Accepted inputs

The following content belongs here:

- runtime outcome grammar and response semantics
- mapping notes between policy decisions and outward API/UI behavior
- documentation of required joins such as `policy_bundle_version`, `reason_codes`, `obligation_codes`, `audit_ref`, or equivalent runtime trace handles
- explain-trace expectations for request-time decisions
- CI/runtime parity notes for policy evaluation
- references to runtime-focused bundle packs, fixtures, and tests
- boundary notes that keep `policy/`, `packages/policy/`, and outward API/runtime surfaces distinct
- review checklists for runtime-significant policy changes
- correction and withdrawal behavior where runtime decisions affect public meaning

### Typical examples

- “What does `DENY` mean on a public request surface?”
- “Which obligations must survive into the outward envelope?”
- “Which fixtures prove runtime abstention behavior?”
- “Which package path is current today: `packages/policy/` or `packages/policy-runtime/`?”
- “Which outward runtime fields must stay explicit at the governed API boundary?”
- “How should a corrected or withdrawn release affect runtime answers?”

[Back to top](#policy-runtime)

---

## Exclusions

The following do **not** belong in this directory:

| Does **not** belong here | Put it here instead |
|---|---|
| Executable policy bundles and rule files | [`../bundles/runtime/README.md`](../bundles/runtime/README.md) and that subtree |
| Runtime policy fixtures | [`../fixtures/README.md`](../fixtures/README.md) |
| Bundle-local policy assertions | [`../tests/README.md`](../tests/README.md) |
| Repo-facing policy behavior proofs | [`../../tests/policy/README.md`](../../tests/policy/README.md) |
| Canonical contract authority for shared runtime objects | [`../../contracts/README.md`](../../contracts/README.md) |
| Competing schema families that drift from contract authority | Reconcile at [`../../contracts/README.md`](../../contracts/README.md) first |
| Shared internal policy-support adapters, obligation helpers, or decision normalizers | [`../../packages/policy/README.md`](../../packages/policy/README.md) |
| Governed API route handlers, request mediation, outward error mapping, or public runtime entrypoints | [`../../apps/api/src/api/README.md`](../../apps/api/src/api/README.md) or other verified app surfaces |
| A dedicated runtime package split that is not yet visible on the working branch | Document the split only after `packages/policy-runtime/` is actually present |
| Secrets, tokens, policy credentials, signing material | Secret manager / verified infra path |
| Product-surface copy and interaction design | Product/app/UI docs |
| Ad hoc scratch notes or one-off experiments | issue / ADR / runbook / draft location with explicit scope |

### Core rule

This directory should **explain** runtime policy.  
It should not quietly become the place where runtime policy is **implemented by accident**.

[Back to top](#policy-runtime)

---

## Directory tree

### Current public-main shape

```text
policy/
├── README.md
├── bundles/
│   ├── README.md
│   └── runtime/
│       └── README.md
├── fixtures/
│   └── README.md
├── policy-runtime/
│   └── README.md
└── tests/
    └── README.md

tests/
└── policy/
    └── README.md

contracts/
└── README.md

schemas/
└── README.md

packages/
└── policy/
    └── README.md

apps/
└── api/
    └── src/
        └── api/
            └── README.md

.github/
└── workflows/
    └── README.md
```

### Current directory-local shape

```text
policy/policy-runtime/
└── README.md
```

### Doctrine-aligned responsibility map

```text
policy/
├── bundles/
│   └── runtime/          # runtime-focused rule packs / manifests / bundle notes
├── fixtures/             # valid / invalid / deny / abstain / correction fixtures
├── tests/                # bundle-local parity checks and negative-path policy assertions
└── policy-runtime/
    └── README.md         # this boundary + coordination surface

tests/
└── policy/               # repo-facing policy behavior proofs and trust-bearing regressions

contracts/
└── README.md             # canonical shared runtime object and vocabulary authority

schemas/
└── README.md             # secondary schema surface; drift risk if treated as co-equal authority

packages/
└── policy/
    └── README.md         # current shared internal policy-support boundary

apps/
└── api/src/api/
    └── README.md         # current outward enforcement boundary

packages/
└── policy-runtime/       # PROPOSED dedicated runtime split only if the active branch proves it
```

> [!NOTE]
> The map above is intentionally mixed:
> - the **current public-main tree** is repo-visible,
> - the **responsibility split** is doctrine-aligned,
> - the **current shared internal package** is `packages/policy/`,
> - and the **dedicated runtime package split** remains **PROPOSED / NEEDS VERIFICATION** until the active branch proves it.

[Back to top](#policy-runtime)

---

## Quickstart

### 1) Inspect the runtime-policy seam

```bash
find policy -maxdepth 4 \
  \( -path './policy/policy-runtime' \
  -o -path './policy/bundles/runtime' \
  -o -path './policy/fixtures' \
  -o -path './policy/tests' \) \
  -print
```

### 2) Inspect repo-facing policy proof neighbors

```bash
find tests -maxdepth 4 \
  \( -path './tests/policy' -o -path './tests/policy/*' \) \
  -print
```

### 3) Inspect contract and schema neighbors before editing runtime semantics

```bash
find contracts schemas -maxdepth 4 -type f | sort
```

### 4) Inspect the current shared internal policy-support and outward API seams

```bash
sed -n '1,260p' packages/policy/README.md
sed -n '1,260p' apps/api/src/api/README.md
```

### 5) Search for finite runtime outcomes and policy vocabulary

```bash
grep -RInE 'ANSWER|ABSTAIN|DENY|ERROR|reason_codes|obligation_codes|policy_bundle_version|audit_ref|RuntimeResponseEnvelope|EvidenceBundle' \
  policy tests contracts schemas packages apps .github 2>/dev/null
```

### 6) Check whether workflow-backed policy gates are actually present

```bash
find .github/workflows -maxdepth 2 -type f | sort
grep -RInE 'opa|rego|conftest|policy' .github/workflows 2>/dev/null
```

### 7) Confirm whether a dedicated runtime package split exists before documenting it as fact

```bash
find packages -maxdepth 3 \
  \( -type d -name 'policy' -o -type d -name 'policy-runtime' \) \
  -print | sort
```

> [!WARNING]
> If the mounted checkout does **not** prove a dedicated `packages/policy-runtime/` path, keep that split marked **PROPOSED** or **NEEDS VERIFICATION** and avoid confusing it with the current `packages/policy/` boundary.

[Back to top](#policy-runtime)

---

## Usage

### When you change runtime outcomes or decision semantics

1. Update the adjacent policy docs first so runtime meaning stays aligned with [`policy/README.md`](../README.md).
2. Reconcile outward semantics with `contracts/` before adding local prose.
3. Recheck [`../../packages/policy/README.md`](../../packages/policy/README.md) if the change affects shared internal reason/obligation handling.
4. Recheck [`../../apps/api/src/api/README.md`](../../apps/api/src/api/README.md) if the change affects outward envelopes, route behavior, or error shaping.
5. Add or update fixtures for:
   - allow / answer
   - abstain
   - deny
   - error
   - correction-sensitive cases where applicable
6. Check that docs, fixtures, and tests still describe the same finite grammar.

### When you add a runtime-focused policy family

1. Put executable rule content in `../bundles/runtime/`.
2. Put examples and negative cases in `../fixtures/`.
3. Put bundle-local assertions in `../tests/`.
4. Put repo-facing trust and regression proof in `../../tests/policy/` when the new family affects cross-surface runtime behavior.
5. Update `packages/policy/` only if the new family introduces **shared internal** helpers.
6. Update outward app/runtime docs only if the new family changes governed API behavior.
7. Add a short entry here only if the new rule family changes how runtime decisions are interpreted by Explore, Dossier, Story, Focus, Compare, Export, or review surfaces.

### When CI and runtime semantics drift

Treat that as a trust failure, not a wording issue.

Use this directory to record:

- what drift occurred,
- which path was stronger (`CI`, `runtime`, or contract authority),
- what fixtures were added to prevent recurrence,
- whether shared internal helpers or outward API boundaries were affected,
- and whether the incident requires correction or withdrawal behavior in public surfaces.

### When public meaning can change

If a runtime decision changes what a user can see or rely on, document the expected relationship between:

- decision,
- obligation,
- outward envelope,
- evidence linkage,
- audit linkage,
- and correction or withdrawal behavior.

[Back to top](#policy-runtime)

---

## Runtime policy shape

```mermaid
flowchart TD
    A[Incoming request] --> B[Governed API / request seam]
    B --> C[Policy semantics described here]
    C --> D[Runtime-focused bundle packs]
    C --> E[Shared vocab + contracts]
    D --> F[Decision result]
    E --> F
    F --> G[Finite outward outcome]
    G --> H[ANSWER]
    G --> I[ABSTAIN]
    G --> J[DENY]
    G --> K[ERROR]

    F --> L[Reason codes + obligation codes]
    L --> M[Audit / explain linkage]
    M --> N[Response envelope / release-sensitive behavior]

    O[policy/fixtures] --> C
    P[policy/tests] --> C
    Q[tests/policy] --> C

    R[packages/policy]
    R -. current shared internal helpers .-> C

    S[apps/api/src/api]
    S -. outward enforcement boundary .-> B

    T[packages/policy-runtime]
    T -. PROPOSED dedicated runtime split .-> D
```

### Reading rule for the diagram

- **Solid lines** represent the runtime-policy meaning this README should describe.
- **Dashed lines** represent current adjacent boundaries or future split points that must stay explicitly labeled.
- **Finite outcome set** is intentional: runtime trust depends on explicit negative states, not fallback prose.
- **Current `packages/policy/`** and **future `packages/policy-runtime/`** are not interchangeable.

[Back to top](#policy-runtime)

---

## Boundary matrix

| Surface | Primary job | Must not do | Status |
|---|---|---|---|
| `policy/policy-runtime/` | Explain runtime policy behavior and boundaries | Pretend runtime implementation exists because the directory exists | **CONFIRMED path** |
| `policy/bundles/runtime/` | Hold runtime-focused rule packs / bundle notes | Become the canonical contract home | **CONFIRMED path / scaffold-only current snapshot** |
| `policy/fixtures/` | Hold valid/invalid/deny/abstain/correction examples | Replace real tests | **CONFIRMED path / README-only current snapshot** |
| `policy/tests/` | Hold bundle-local policy assertions and parity checks | Quietly diverge from runtime behavior | **CONFIRMED path / README-only current snapshot** |
| `tests/policy/` | Hold repo-facing policy behavior proofs | Drift from contract/runtime semantics while still passing prose review | **CONFIRMED path / README-only current snapshot** |
| `contracts/` | Own canonical shared object shapes and vocabularies | Be bypassed by local one-off schemas | **CONFIRMED** |
| `schemas/` | Remain a secondary schema surface unless authority is explicitly redefined | Drift into a competing schema universe | **CONFIRMED risk seam** |
| `packages/policy/` | Hold shared internal policy-support helpers | Quietly become a second policy authority or a route-facing runtime surface | **CONFIRMED path / README-only current snapshot** |
| `apps/api/src/api/` | Enforce outward request/response behavior at the governed API edge | Become the sovereign home for policy rules or shared vocabularies | **CONFIRMED path / draft boundary README** |
| `.github/workflows/` | Carry workflow-backed gates when they exist | Be described here as current enforcement if only README scaffolding is present | **CONFIRMED path / README-only current snapshot** |
| `packages/policy-runtime/` | Hold a future dedicated runtime-package split if the branch introduces one | Be documented here as current implementation without proof | **PROPOSED / NEEDS VERIFICATION** |

[Back to top](#policy-runtime)

---

## Runtime result grammar

| Outcome | Meaning | Minimum runtime expectation | Public-surface consequence |
|---|---|---|---|
| `ANSWER` | A supported response may be emitted | policy allow, evidence linkage, outward envelope, audit linkage | show answer with traceable support |
| `ABSTAIN` | Evidence is insufficient or scope must narrow | explicit abstention semantics, not silent omission | preserve trust by refusing unsupported synthesis |
| `DENY` | Policy blocks the action or surface | deny result plus visible reason class / obligation handling as allowed | fail closed rather than leak or improvise |
| `ERROR` | Runtime could not complete safely | error path must remain accountable and non-fabricating | do not convert operational failure into plausible prose |

### Working interpretation

There is **no uncited fifth outcome**.

If a case does not qualify as `ANSWER`, it must remain visibly negative, constrained, or incomplete rather than being smoothed over for convenience.

[Back to top](#policy-runtime)

---

## Runtime-facing fields that must stay explicit

| Field or concept | Why it matters | Where authority should live |
|---|---|---|
| `reason_codes` | Makes denials, abstentions, and holds reconstructable | shared vocab / contract authority |
| `obligation_codes` | Carries required follow-on behavior | shared vocab / contract authority |
| `policy_bundle_version` | Lets runtime behavior be traced to a specific rule set | policy + contract seam |
| `audit_ref` | Connects user-visible behavior to runtime and review history | runtime / audit seam |
| `dataset_version_id` | Keeps outward responses tied to promoted scope instead of ambient data state | governed API response contract |
| artifact digests / checksums | Make outward payloads auditable and correction-ready | response contract + catalog closure |
| `policy_label` | Keeps user-visible restriction state explicit rather than implied | response contract + policy surface |
| evidence refs | Prevent unsupported “citation-like” prose | contracts + evidence resolver seam |
| correction / withdrawal refs | Keep change visible instead of silent | correction / release seam |
| finite outcome enum | Preserves fail-closed behavior | outward response contract |

[Back to top](#policy-runtime)

---

## Task list / definition of done

### Minimum review gate for this README

- [ ] Mounted checkout inspected before claiming implementation facts.
- [ ] All relative links in this README resolve.
- [ ] Current `packages/policy/README.md` and `apps/api/src/api/README.md` neighbors are still present and still the right links.
- [ ] Any mention of a dedicated `packages/policy-runtime/` split remains **PROPOSED** or **NEEDS VERIFICATION** unless the active branch proves it.
- [ ] Any mention of OPA/Rego stays scoped as starter direction unless actual mounted bundles/tests are visible.
- [ ] `contracts/` remains the named authority for shared runtime object shapes.
- [ ] `schemas/` is not silently treated as a second sovereign schema home.
- [ ] Shared internal helper placement and outward API placement stay explicitly distinct.
- [ ] Runtime outcome grammar here matches adjacent policy, contract, and outward API docs.
- [ ] At least one negative-path example exists for deny or abstain behavior before this README is called “stable.”
- [ ] CI/runtime parity expectations are documented without implying checked-in workflow YAML that is not present.
- [ ] Correction-sensitive runtime behavior is described where public meaning can change.

### Stronger completion state

- [ ] `policy/bundles/runtime/` contains real runtime-focused rule packs.
- [ ] `policy/fixtures/` contains request/decision/result fixtures.
- [ ] `policy/tests/` contains bundle-local parity or regression checks.
- [ ] `tests/policy/` contains repo-facing policy behavior proofs.
- [ ] `contracts/` contains the canonical runtime envelope and decision-related artifacts.
- [ ] The mounted workspace confirms what belongs in current `packages/policy/` and whether any separate `packages/policy-runtime/` split exists.
- [ ] `apps/api/src/api/` documents or proves the outward envelope fields this README names.
- [ ] This README no longer has to rely on scaffold-only neighbor directories for context.

[Back to top](#policy-runtime)

---

## FAQ

### Does this directory contain the policy engine?

No. This path is the **documentation and coordination surface** for runtime policy semantics. Engine code, bundle loading, request mediation, or adapter logic must be verified elsewhere before being documented as implementation fact.

### Is `policy/policy-runtime/` the same thing as `packages/policy/` or `packages/policy-runtime/`?

No.

- `policy/policy-runtime/` is a repo-visible documentation seam under top-level `policy/`.
- `packages/policy/` is the current repo-visible shared internal policy-support boundary.
- `packages/policy-runtime/` is a **PROPOSED / NEEDS VERIFICATION** future split sometimes implied by nearby doctrine.

Treat them as related but not interchangeable.

### Why mention `apps/api/src/api/` here?

Because outward runtime behavior is not just a package concern. The current repo also exposes a governed API enforcement boundary for request validation, policy-safe response shaping, evidence resolution orchestration, and outward error handling. If runtime semantics change what the user sees, that API seam matters.

### Does this README prove executable runtime policy files already exist?

No.

A README can define the boundary and expectations without proving the subtree has mounted bundles, fixtures, tests, or runtime code behind it.

### Why keep a README-only directory?

Because KFM benefits from **visible seams**. A thin directory can still be useful if it clarifies where trust-bearing responsibilities belong and prevents accidental authority mixing while implementation catches up.

### Should canonical runtime response shapes live here?

No. Put canonical shared object shapes under `contracts/`, then link to them from here.

### What is the main failure mode to avoid?

The main failure mode is **trust theater**: rich prose that makes runtime governance sound implemented when the mounted repo has not yet proven bundles, fixtures, tests, loaders, helper placement, outward API behavior, or workflow gates.

[Back to top](#policy-runtime)

---

## Appendix

<details>
<summary><strong>Verification backlog and maintainer notes</strong></summary>

### Open verification items

| Item | Current posture |
|---|---|
| Is `policy/policy-runtime/` more than a boundary seam on the public branch? | **NEEDS VERIFICATION** |
| Are runtime-focused bundles mounted under `policy/bundles/runtime/` beyond scaffold text? | **NEEDS VERIFICATION** |
| Are runtime fixtures present under `policy/fixtures/` beyond README guidance? | **NEEDS VERIFICATION** |
| Are bundle-local runtime policy tests present under `policy/tests/`? | **NEEDS VERIFICATION** |
| Are repo-facing runtime behavior proofs present under `tests/policy/`? | **NEEDS VERIFICATION** |
| What shared internal runtime-adjacent behavior, if any, already belongs in `packages/policy/`? | **NEEDS VERIFICATION** |
| Does a real `packages/policy-runtime/` package exist on the working branch? | **NEEDS VERIFICATION** |
| Which outward envelope fields are canonical in `apps/api/src/api/` versus illustrative draft text? | **NEEDS VERIFICATION** |
| Are merge-blocking runtime policy workflows checked in on the mounted branch? | **NEEDS VERIFICATION** |
| Which shared contracts are authoritative for runtime outcomes and decision semantics? | **NEEDS VERIFICATION** |

### Suggested inspection sequence

```bash
# 1) policy subtree
find policy -maxdepth 5 -print | sort

# 2) repo-facing policy proofs
find tests/policy -maxdepth 5 -print | sort

# 3) contract / schema overlap
find contracts schemas -maxdepth 5 -print | sort

# 4) current package and possible runtime split
find packages -maxdepth 5 -print | sort | grep -E 'packages/(policy|policy-runtime)' || true

# 5) outward API boundary
find apps/api/src/api -maxdepth 5 -print | sort

# 6) workflow evidence
find .github/workflows -maxdepth 3 -type f | sort

# 7) vocabulary and outcome semantics
grep -RInE 'ANSWER|ABSTAIN|DENY|ERROR|reason_codes|obligation_codes|policy_bundle_version|audit_ref|dataset_version_id|policy_label' \
  policy tests contracts schemas packages apps .github 2>/dev/null
```

### PROPOSED runtime artifact families to reconcile against contracts

- `DecisionEnvelope`
- `RuntimeResponseEnvelope`
- `EvidenceBundle`
- `ReviewRecord` when separation of duty or public release review applies
- `CorrectionNotice` where runtime-visible meaning is superseded, withdrawn, or narrowed

### Maintenance note

Keep this README short on implementation claims and strong on boundaries.

When the mounted repo proves more, move authority outward to:

- `contracts/` for shared shapes,
- `policy/bundles/runtime/` for executable bundle packs,
- `policy/tests/` for bundle-local parity assertions,
- `tests/policy/` for repo-facing runtime behavior proof,
- `packages/policy/` for shared internal helpers that are actually present,
- `apps/api/src/api/` for outward route and envelope behavior,
- and `packages/policy-runtime/` only if the active branch explicitly introduces that split.

Then reduce the explanatory weight here instead of duplicating it.

</details>

[Back to top](#policy-runtime)
