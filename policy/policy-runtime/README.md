# Policy Runtime

_Runtime-facing policy semantics, decision coordination, and CI/runtime parity for KFM trust-bearing responses, publication decisions, and visible negative states._

**Status:** experimental  
**Owners:** NEEDS VERIFICATION  
**Badges:** ![status](https://img.shields.io/badge/status-experimental-blue) ![surface](https://img.shields.io/badge/surface-policy--runtime-1f6feb) ![posture](https://img.shields.io/badge/posture-deny--by--default-bd561d) ![outcomes](https://img.shields.io/badge/runtime-finite_outcomes-6f42c1) ![verification](https://img.shields.io/badge/implementation-needs_verification-orange)

**Repo fit:** `policy/policy-runtime/README.md` · Up: [`../README.md`](../README.md) · Related: [`../bundles/runtime/README.md`](../bundles/runtime/README.md), [`../fixtures/README.md`](../fixtures/README.md), [`../tests/README.md`](../tests/README.md), [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md), [`../../tests/README.md`](../../tests/README.md), [`../../.github/workflows/README.md`](../../.github/workflows/README.md)

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#runtime-policy-shape) · [Tables](#boundary-matrix) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> This directory is a **runtime-policy documentation and coordination seam**, not proof of a mounted runtime implementation. Keep a hard boundary between:
> 1. **policy artifacts** such as rule packs, fixtures, and policy tests, and  
> 2. **runtime glue** such as bundle loaders, decision mediators, or request adapters, which belong in a verified runtime package path only after the mounted repo proves it.

---

## Scope

`policy/policy-runtime/` documents how KFM policy behaves **at request time and release-significant runtime seams**.

This README exists to keep the policy/runtime boundary inspectable. It is the place to describe:

- finite runtime outcomes
- decision/result grammar
- reason and obligation vocab expectations
- CI/runtime semantic parity
- explainability and audit linkage expectations
- handoff points between policy bundles, fixtures, tests, contracts, and any future runtime package

### Status posture used here

| Label | Meaning in this directory |
|---|---|
| **CONFIRMED** | Present in currently visible repo structure or already stated by adjacent repo docs. |
| **INFERRED** | Strongly implied by nearby docs and directory relationships, but not directly proven as mounted implementation. |
| **PROPOSED** | Recommended structure or operating rule that fits KFM doctrine and current repo patterns. |
| **UNKNOWN** | Not verified from the currently visible repo surfaces. |
| **NEEDS VERIFICATION** | Review item before treating this README as implementation truth. |

[Back to top](#policy-runtime)

---

## Repo fit

### Why this README exists

The public repo tree shows `policy/` as a first-class top-level area, and also shows a dedicated `policy-runtime/` subdirectory. At the same time, the adjacent policy docs keep warning against silently turning documentation seams into unverified implementation claims.

That makes this file responsible for one thing above all:

**keeping the runtime-policy boundary explicit without pretending the mounted runtime is already proven.**

### Current role of this path

| Path | Role here | Confidence |
|---|---|---|
| `policy/policy-runtime/README.md` | This boundary and coordination document | **CONFIRMED** |
| `policy/bundles/runtime/` | Runtime-focused policy bundle home | **CONFIRMED path / UNKNOWN content depth** |
| `policy/fixtures/` | Runtime policy fixtures and negative cases | **CONFIRMED path / UNKNOWN content depth** |
| `policy/tests/` | Policy assertions, parity checks, and regression guardrails | **CONFIRMED path / UNKNOWN content depth** |
| `../../contracts/` | Canonical contract home for shared JSON/OpenAPI/vocab artifacts | **CONFIRMED** |
| `../../schemas/` | Secondary schema surface that must not drift away from contract authority | **CONFIRMED** |
| `packages/policy-runtime/` | Possible future runtime implementation seam for loaders/mediators/adapters | **PROPOSED** |

### Practical interpretation

Use this directory to explain runtime-policy behavior and to point maintainers to the correct artifact homes.

Do **not** use it to imply that the repo already contains:

- a mounted policy decision point
- request-time bundle loaders
- live OPA/Rego wiring
- merge-blocking runtime policy workflows
- a verified `packages/policy-runtime/` implementation

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
- review checklists for runtime-significant policy changes
- correction/withdrawal behavior where runtime decisions affect public meaning

### Typical examples

- “What does `DENY` mean on a public request surface?”
- “Which obligations must survive into the outward envelope?”
- “Which fixtures prove runtime abstention behavior?”
- “Where do runtime policy bundles live versus contract files?”
- “How should a corrected or withdrawn release affect runtime answers?”

[Back to top](#policy-runtime)

---

## Exclusions

The following do **not** belong in this directory:

| Does **not** belong here | Put it here instead |
|---|---|
| Executable policy bundles and rule files | [`../bundles/runtime/README.md`](../bundles/runtime/README.md) and that subtree |
| Runtime policy fixtures | [`../fixtures/README.md`](../fixtures/README.md) |
| Runtime policy tests and parity checks | [`../tests/README.md`](../tests/README.md) |
| Canonical contract/schema authority for shared objects | [`../../contracts/README.md`](../../contracts/README.md) |
| Duplicate schema families that drift from contracts | Reconcile at `../../contracts/` first |
| Secrets, tokens, policy credentials, signing material | secret manager / verified infra path |
| HTTP handlers, bundle loaders, decision mediators, adapter code | verified runtime package such as `packages/policy-runtime/` |
| Product-surface copy and interaction design | product/app/UI README surfaces |
| Ad hoc scratch notes or one-off experiments | issue/ADR/runbook/draft location with explicit scope |

### Core rule

This directory should **explain** runtime policy.  
It should not quietly become the place where runtime policy is **implemented by accident**.

[Back to top](#policy-runtime)

---

## Directory tree

### Current repo-visible shape

```text
policy/
├── README.md
├── bundles/
│   └── runtime/
├── fixtures/
├── policy-runtime/
│   └── README.md
└── tests/
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
├── tests/                # parity checks, regression checks, negative-path policy tests
└── policy-runtime/
    └── README.md         # this boundary + coordination surface

contracts/
├── jsonschema/           # canonical object shapes
├── openapi/              # outward contract surfaces
├── vocab/                # shared finite vocabularies
└── fixtures/             # contract-level fixtures

packages/
└── policy-runtime/       # PROPOSED runtime loader / mediator / adapter package
```

> [!NOTE]
> The responsibility map above is intentionally mixed:
> - the **path existence** under `policy/` is current repo-visible structure
> - the **cross-package runtime seam** remains **PROPOSED** until the mounted workspace proves it

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

### 2) Inspect contract and schema neighbors before editing runtime semantics

```bash
find contracts schemas -maxdepth 4 -type f | sort
```

### 3) Search for finite runtime outcomes and policy vocabulary

```bash
grep -RInE 'ANSWER|ABSTAIN|DENY|ERROR|reason_codes|obligation_codes|policy_bundle_version|audit_ref' \
  policy contracts schemas tests .github 2>/dev/null
```

### 4) Check whether workflow-backed policy gates are actually present

```bash
find .github/workflows -maxdepth 2 -type f | sort
grep -RInE 'opa|rego|conftest|policy' .github/workflows 2>/dev/null
```

### 5) Confirm whether a runtime implementation seam exists before documenting it as fact

```bash
find packages -maxdepth 3 -type d -name 'policy-runtime' 2>/dev/null
```

> [!WARNING]
> If the mounted checkout does **not** prove a runtime package, keep all package-level references in this README marked **PROPOSED** or **NEEDS VERIFICATION**.

[Back to top](#policy-runtime)

---

## Usage

### When you change runtime outcomes or decision semantics

1. Update the adjacent policy docs first so the runtime meaning stays aligned with `policy/README.md`.
2. Reconcile outward semantics with `contracts/` before adding local prose.
3. Add or update fixtures for:
   - allow / answer
   - abstain
   - deny
   - error
   - correction-sensitive cases where applicable
4. Check that docs, fixtures, and tests still describe the same finite grammar.

### When you add a runtime-focused policy family

1. Put executable rule content in `../bundles/runtime/`.
2. Put examples and negative cases in `../fixtures/`.
3. Put parity and regression checks in `../tests/`.
4. Add a short entry here only if the new rule family changes how runtime decisions are interpreted by APIs, Focus, Story, Explore, Export, or review surfaces.

### When CI and runtime semantics drift

Treat that as a trust failure, not a wording issue.

Use this directory to record:

- what drift occurred
- which path was stronger (`CI`, `runtime`, or contract authority)
- what fixtures were added to prevent recurrence
- whether the incident requires correction or withdrawal behavior in public surfaces

### When public meaning can change

If a runtime decision changes what a user can see or rely on, document the expected relationship between:

- decision
- obligation
- outward envelope
- evidence linkage
- audit linkage
- correction or withdrawal behavior

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
    Q[packages/policy-runtime]
    Q -. PROPOSED runtime loader / mediator seam .-> D
```

### Reading rule for the diagram

- **Solid lines** represent the runtime-policy meaning this README should describe.
- **Dashed line** represents a likely implementation seam that must stay **PROPOSED** until verified.
- **Finite outcome set** is intentional: runtime trust depends on explicit negative states, not fallback prose.

[Back to top](#policy-runtime)

---

## Boundary matrix

| Surface | Primary job | Must not do | Status |
|---|---|---|---|
| `policy/policy-runtime/` | Explain runtime policy behavior and boundaries | Pretend runtime implementation exists because the directory exists | **CONFIRMED path** |
| `policy/bundles/runtime/` | Hold runtime-focused rule packs / bundle notes | Become the canonical contract home | **CONFIRMED path / UNKNOWN content** |
| `policy/fixtures/` | Hold valid/invalid/deny/abstain/correction examples | Replace real tests | **CONFIRMED path / UNKNOWN content** |
| `policy/tests/` | Assert runtime semantics and CI/runtime parity | Quietly diverge from runtime behavior | **CONFIRMED path / UNKNOWN content** |
| `contracts/` | Own canonical shared object shapes and vocabularies | Be bypassed by local one-off schemas | **CONFIRMED** |
| `schemas/` | Secondary or legacy schema surface | Drift into a competing schema universe | **CONFIRMED risk seam** |
| `packages/policy-runtime/` | Load bundles, mediate decisions, adapt to runtime request flow | Be documented here as implemented without proof | **PROPOSED** |

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
| `audit_ref` | Connects user-visible behavior to runtime and review history | runtime/audit seam |
| evidence refs | Prevents unsupported “citation-like” prose | contracts + evidence resolver seam |
| correction / withdrawal refs | Keeps change visible instead of silent | correction/release seam |
| finite outcome enum | Preserves fail-closed behavior | outward response contract |

[Back to top](#policy-runtime)

---

## Task list / definition of done

### Minimum review gate for this README

- [ ] Mounted checkout inspected before claiming implementation facts.
- [ ] All relative links in this README resolve.
- [ ] Any mention of runtime glue remains **PROPOSED** unless the package path is confirmed.
- [ ] Any mention of OPA/Rego stays scoped as starter direction unless actual mounted bundles/tests are visible.
- [ ] `contracts/` remains the named authority for shared runtime object shapes.
- [ ] `schemas/` is not silently treated as a second sovereign schema home.
- [ ] Runtime outcome grammar here matches adjacent policy and contract docs.
- [ ] At least one negative-path example exists for deny or abstain behavior before this README is called “stable.”
- [ ] CI/runtime parity expectations are documented without implying checked-in workflow YAML that is not present.
- [ ] Correction-sensitive runtime behavior is described where public meaning can change.

### Stronger completion state

- [ ] `policy/bundles/runtime/` contains real runtime-focused rule packs.
- [ ] `policy/fixtures/` contains request/decision/result fixtures.
- [ ] `policy/tests/` contains parity or regression checks.
- [ ] `contracts/` contains the canonical runtime envelope and decision-related artifacts.
- [ ] The mounted workspace confirms whether `packages/policy-runtime/` exists and what it owns.
- [ ] This README no longer has to rely on placeholder-adjacent directories for context.

[Back to top](#policy-runtime)

---

## FAQ

### Does this directory contain the policy engine?

No. This path is the **documentation and coordination surface** for runtime policy semantics. Engine code, bundle loading, request mediation, or adapter logic must be verified elsewhere before being documented as implementation fact.

### Is `policy/policy-runtime/` the same thing as `packages/policy-runtime/`?

No.

`policy/policy-runtime/` is a repo-visible documentation seam under `policy/`.  
`packages/policy-runtime/` is a **PROPOSED** implementation seam commonly referenced by nearby doctrine. Treat them as related but not interchangeable.

### Does this README prove executable runtime policy files already exist?

No.

A README can define the boundary and expectations without proving the subtree has mounted bundles, fixtures, tests, or runtime code behind it.

### Why keep a README-only directory?

Because KFM benefits from **visible seams**. A thin directory can still be useful if it clarifies where trust-bearing responsibilities belong and prevents accidental authority mixing while implementation catches up.

### Should canonical runtime response shapes live here?

No. Put canonical shared object shapes under `contracts/`, then link to them from here.

### What is the main failure mode to avoid?

The main failure mode is **trust theater**: rich prose that makes runtime governance sound implemented when the mounted repo has not yet proven bundles, fixtures, tests, loaders, or workflow gates.

[Back to top](#policy-runtime)

---

## Appendix

<details>
<summary><strong>Verification backlog and maintainer notes</strong></summary>

### Open verification items

| Item | Current posture |
|---|---|
| Is `policy/policy-runtime/` more than a placeholder seam? | **NEEDS VERIFICATION** |
| Are runtime-focused bundles mounted under `policy/bundles/runtime/`? | **NEEDS VERIFICATION** |
| Are runtime fixtures present under `policy/fixtures/`? | **NEEDS VERIFICATION** |
| Are runtime policy tests present under `policy/tests/`? | **NEEDS VERIFICATION** |
| Does a real `packages/policy-runtime/` package exist? | **NEEDS VERIFICATION** |
| Are merge-blocking runtime policy workflows checked in? | **NEEDS VERIFICATION** |
| Which shared contracts are authoritative for runtime outcomes and decision semantics? | **NEEDS VERIFICATION** |

### Suggested inspection sequence

```bash
# 1) policy subtree
find policy -maxdepth 5 -print | sort

# 2) contract / schema overlap
find contracts schemas -maxdepth 5 -print | sort

# 3) runtime package seam
find packages -maxdepth 5 -print | sort | grep 'policy-runtime' || true

# 4) workflow evidence
find .github/workflows -maxdepth 3 -type f | sort

# 5) vocabulary and outcome semantics
grep -RInE 'ANSWER|ABSTAIN|DENY|ERROR|reason_codes|obligation_codes|policy_bundle_version' \
  policy contracts schemas tests .github 2>/dev/null
```

### PROPOSED runtime artifact families to reconcile against contracts

- `DecisionEnvelope`
- `RuntimeResponseEnvelope`
- `ExplainTrace`
- `ReviewRecord` when separation of duty or public release review applies
- `CorrectionNotice` where runtime-visible meaning is superseded, withdrawn, or narrowed

### Maintenance note

Keep this README short on implementation claims and strong on boundaries.  
When the mounted repo proves more, move authority outward to:

- `contracts/` for shared shapes
- `policy/bundles/runtime/` for executable bundle packs
- `policy/tests/` for parity assertions
- `packages/policy-runtime/` for runtime glue

Then reduce the explanatory weight here instead of duplicating it.

</details>

[Back to top](#policy-runtime)
