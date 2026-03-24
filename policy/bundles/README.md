# Policy Bundles

Executable bundle lane for KFM deny-by-default policy, finite outcome grammar, and reviewable trust seams.

> **Status:** `experimental`  
> **Owners:** `@bartytime4life`  
> **Path:** `policy/bundles/README.md`  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![owners](https://img.shields.io/badge/owners-%40bartytime4life-1f6feb) ![surface](https://img.shields.io/badge/surface-policy%2Fbundles-blue) ![inventory](https://img.shields.io/badge/current%20public%20inventory-README--only-lightgrey) ![posture](https://img.shields.io/badge/posture-deny--by--default-critical) ![branch](https://img.shields.io/badge/branch-public%20main-0a7d5a)  
> **Repo fit:** parent [`../README.md`](../README.md) · sibling fixtures [`../fixtures/README.md`](../fixtures/README.md) · sibling tests [`../tests/README.md`](../tests/README.md) · current runtime scaffold [`../policy-runtime/README.md`](../policy-runtime/README.md) · contract boundary [`../../contracts/README.md`](../../contracts/README.md) · workflow guardrails [`../../.github/workflows/README.md`](../../.github/workflows/README.md)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> Current public `main` exposes `policy/` as a real lane with `bundles/`, `fixtures/`, `policy-runtime/`, `tests/`, and `README.md`. This leaf directory, however, is still scaffold-level: `policy/bundles/` currently shows `README.md` only. Treat this file as the operating guide for a bundle lane that exists publicly but is not yet evidenced here as a mounted executable policy pack.

## Scope

`policy/bundles/` is where KFM policy should become small, typed, reviewable, and executable.

The bundle lane is not a generic place for “any governance file.” Its job is narrower and more consequential: hold the rule packs that shape admission, rights, sensitivity, review, release, runtime, export, and correction behavior under KFM’s default-deny posture. These bundles should explain why a result happened, what obligations follow, and which downstream trust objects must carry the decision.

### Status markers used here

| Marker | Meaning in this README |
|---|---|
| **CONFIRMED** | Visible in the current public repo tree or directly stated by adjacent current repo docs |
| **INFERRED** | Strongly supported by the current repo docs, but not established here as a mounted implementation fact |
| **PROPOSED** | Repo-native starter structure or maintenance guidance consistent with KFM doctrine |
| **UNKNOWN** | Not verified strongly enough to state as current repo reality |
| **NEEDS VERIFICATION** | A path, engine detail, token, or workflow behavior that should be checked before merge |

### Working rule

One bundle should map to one trust seam—or to one tightly related seam family—so reviewers can answer three questions quickly:

1. What decision does this bundle own?
2. What sibling fixtures and tests prove it?
3. What downstream trust objects must reflect its result?

[Back to top](#policy-bundles)

## Repo fit

This directory sits below the parent `policy/` lane and beside the sibling `fixtures/`, `tests/`, and current `policy-runtime/` scaffold. It should stay close to those surfaces, but it should not absorb their responsibilities.

| Item | What to treat as current |
|---|---|
| Path | `policy/bundles/README.md` |
| Current public snapshot | `policy/bundles/` contains `README.md` only |
| Parent lane | [`../README.md`](../README.md) defines `policy/` as the governed executable policy surface |
| Sibling verification lanes | [`../fixtures/README.md`](../fixtures/README.md) and [`../tests/README.md`](../tests/README.md) should carry paired proof, not hidden bundle-local drift |
| Schema / contract boundary | [`../../contracts/README.md`](../../contracts/README.md) is the stronger current machine-contract lane; do not quietly copy canonical schema law here |
| Workflow guardrails | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) is the current automation lane; it currently documents workflow expectations rather than proving a checked-in YAML gate set |
| Runtime seam | Current public `main` also has [`../policy-runtime/README.md`](../policy-runtime/README.md) as a scaffold; attached doctrine elsewhere also sketches `packages/policy-runtime/`. Treat runtime-home choice as **NEEDS VERIFICATION** before hardening imports or paths |
| Ownership | `/policy/` currently routes to `@bartytime4life` in `CODEOWNERS` |

> [!CAUTION]
> `policy/bundles/` is not the place to resolve `contracts/` versus `schemas/` authority by accident. If a bundle depends on shared reason, obligation, rights, or sensitivity vocabularies, reference the chosen shared home or document the interim ownership explicitly. Do not let a second authoritative registry quietly grow here.

### Why this README exists

The current file started as a one-line scaffold. That is enough to prove the lane exists, but not enough to help a maintainer answer:

- what belongs in a bundle,
- what must stay out,
- how this directory relates to fixtures, tests, and runtime mediation,
- or what “done” looks like for a policy-significant change.

[Back to top](#policy-bundles)

## Accepted inputs

Only content that helps `policy/bundles/` behave like an executable, reviewable rule lane belongs here.

| Input class | What belongs here | Examples |
|---|---|---|
| Bundle rule files | Rule packs that decide a bounded trust seam | `*.rego`, seam-local helper modules, machine-readable rule files |
| Bundle manifests / indexes | Files that identify seam, version, dependencies, and paired verification | `bundle.yaml`, `bundle.json`, manifest notes |
| Bundle-local glossary notes | Minimal human-readable notes that keep review practical | `glossary.md`, outcome notes, steward-facing seam notes |
| Shared imports used by multiple bundle families | Helper modules that stay inside the bundle lane and do not replace runtime code | `shared/imports.rego`, common predicates, result helpers |
| Bundle-local reference maps | Explicit references to sibling fixtures, tests, and shared vocabularies | fixture index, test index, dependency notes |

### Minimum bar for a real bundle

A bundle is not “present” merely because a file exists. The minimum useful bar is:

- the trust seam is named,
- the bundle version is explicit,
- the result grammar is finite,
- paired fixtures exist,
- paired tests exist,
- downstream trust objects affected by the bundle are named,
- and the README or rationale explains what changed if semantics move.

[Back to top](#policy-bundles)

## Exclusions

`policy/bundles/` should stay narrow.

| Does **not** belong here | Put it instead | Why |
|---|---|---|
| Canonical JSON Schema / OpenAPI definitions | [`../../contracts/`](../../contracts/) | Shared object shape should not drift into bundle logic |
| A second authoritative schema home | [`../../schemas/README.md`](../../schemas/README.md) boundary guidance | Parallel contract law is risk, not resilience |
| Generic policy fixtures | [`../fixtures/`](../fixtures/) | Bundle verification should stay inspectable and reusable across seams |
| Generic policy tests | [`../tests/`](../tests/) | Tests should remain a sibling proof surface |
| Runtime bundle loaders, API adapters, decision assemblers | current scaffold [`../policy-runtime/README.md`](../policy-runtime/README.md) or the verified runtime package | Execution glue is adjacent to the bundle lane, not the bundle lane |
| Secrets, signing keys, `.env`, live credentials | secret manager / host config | Sensitive operational material must not live in a public rule lane |
| RAW / WORK / QUARANTINE / PROCESSED / CATALOG / PUBLISHED artifacts | [`../../data/README.md`](../../data/README.md) | Policy governs these artifacts; it is not their canonical store |
| UI-only conditionals treated as the only policy surface | nowhere | KFM rejects policy theater in presentation code |

[Back to top](#policy-bundles)

## Directory tree

### Current public snapshot (**CONFIRMED**)

```text
policy/
├── README.md
├── bundles/
│   └── README.md
├── fixtures/
│   └── README.md
├── policy-runtime/
│   └── README.md
└── tests/
    └── README.md
```

### This directory today (**CONFIRMED**)

```text
policy/bundles/
└── README.md
```

### Starter lane shape after first real bundle wave (**PROPOSED**)

```text
policy/bundles/
├── README.md
├── shared/
│   ├── imports.rego
│   └── glossary.md
├── admission/
│   ├── bundle.yaml
│   └── source_admission.rego
├── rights/
│   ├── bundle.yaml
│   └── access_rights.rego
├── sensitivity/
│   ├── bundle.yaml
│   ├── generalize_or_restrict.rego
│   └── transforms.rego
├── review/
│   ├── bundle.yaml
│   └── steward_review_required.rego
├── release/
│   ├── bundle.yaml
│   └── publication_gate.rego
├── runtime/
│   ├── bundle.yaml
│   └── finite_outcomes.rego
├── export/
│   ├── bundle.yaml
│   └── export_scope.rego
└── correction/
    ├── bundle.yaml
    └── correction_propagation.rego
```

> [!NOTE]
> The tree above is a buildable starter pattern, not a claim about the mounted branch. Keep the current public snapshot and the proposed target shape visibly separate.

[Back to top](#policy-bundles)

## Quickstart

### 1) Inspect the actual bundle lane

```bash
find policy -maxdepth 3 \
  \( -path 'policy/bundles' -o -path 'policy/fixtures' -o -path 'policy/tests' -o -path 'policy/policy-runtime' \) \
  -print 2>/dev/null
```

### 2) Discover real bundle artifacts

```bash
find policy/bundles -type f \
  \( -name '*.rego' -o -name 'bundle.*' -o -name '*.yaml' -o -name '*.yml' -o -name '*.json' -o -name '*.md' \) \
  | sort
```

### 3) Trace trust-bearing joins

```bash
grep -R -nE \
  'DecisionEnvelope|ReviewRecord|ReleaseManifest|ReleaseProofPack|EvidenceBundle|RuntimeResponseEnvelope|CorrectionNotice|reason_codes|obligation_codes|rights_class|sensitivity_class' \
  policy contracts tests docs apps packages 2>/dev/null || true
```

### 4) Check paired verification

```bash
find policy/fixtures policy/tests -maxdepth 4 -type f 2>/dev/null | sort

grep -R -nE \
  'allow|deny|generalize|restrict|review|required|withdraw|supersede|ANSWER|ABSTAIN|DENY|ERROR' \
  policy/fixtures policy/tests 2>/dev/null || true
```

### 5) Inspect workflow references

```bash
find .github/workflows -maxdepth 2 -type f 2>/dev/null | sort

grep -R -nE 'opa|rego|conftest|policy|DecisionEnvelope|RuntimeResponseEnvelope|CorrectionNotice' \
  .github/workflows policy tests docs 2>/dev/null || true
```

### 6) Optional local policy check

```bash
# Illustrative only — verify the real entrypoint before relying on it in CI.
conftest test policy/bundles
```

> [!TIP]
> These commands are discovery tools, not proof by themselves. Update this README to match the checked-out branch after inspection; do not let the README drift ahead of the lane it describes.

[Back to top](#policy-bundles)

## Usage

### Add a new bundle family

1. Start from the trust seam, not the filename.
2. Decide whether the new rule belongs in an existing seam family or needs its own family.
3. Name the bundle so a reviewer can infer its responsibility quickly.
4. Reference the shared vocabulary that explains its reasons and obligations.
5. Add paired fixtures in `../fixtures/`.
6. Add paired tests in `../tests/`.
7. Document which downstream trust objects must reflect the result.

### Change a bundle safely

1. Keep semantic changes explicit.
2. Bump the bundle version when the meaning of a result changes.
3. Do not rename or repurpose reason or obligation semantics casually.
4. Re-check sibling fixtures and tests in the same PR.
5. Update steward notes when a changed rule alters public or reviewer-visible behavior.
6. Record rollback posture if the change touches release, runtime, export, or correction seams.

### Keep the bundle lane singular

- A bundle may **reference** contracts, fixtures, tests, and runtime mediation.
- A bundle may **not** silently replace them.
- If a helper starts behaving like runtime code, move it to the verified runtime seam.
- If a bundle starts collecting canonical schemas or duplicated registries, stop and resolve authority first.

### Change review expectation

A policy-significant PR should remain small, reversible, and additive where possible. For this lane, that normally means:

- one seam-focused change,
- explicit fixtures and tests,
- steward rationale where semantics matter,
- and no hidden widening of trust scope.

[Back to top](#policy-bundles)

## Diagram

```mermaid
flowchart LR
    V[Shared vocab / contracts] --> B[policy/bundles]
    B --> D[DecisionEnvelope]
    D --> R[ReviewRecord]
    D --> RR[RuntimeResponseEnvelope]
    R --> M[ReleaseManifest / ReleaseProofPack]
    M --> E[EvidenceBundle-linked public or steward surface]
    C[CorrectionNotice] --> M
    C --> E

    F[policy/fixtures] -. paired proof .-> B
    T[policy/tests] -. policy regression .-> B
    W[.github/workflows] -. merge / release gates .-> B
    PR[policy-runtime seam] -. load / evaluate / assemble .-> B
```

Above: `policy/bundles/` is the executable rule lane between shared vocab and contracts and the trust-bearing artifacts that make review, release, runtime, and correction reconstructable.

[Back to top](#policy-bundles)

## Tables

### Core bundle seams (**PROPOSED starter grouping**)

| Bundle seam | Primary question | Typical downstream consequence | Must coordinate with |
|---|---|---|---|
| admission | Can candidate material enter the governed path? | allow / hold / deny | source descriptors, validation, review |
| rights | Does this actor or surface have permitted use? | deny / restrict | rights vocab, release scope, exports |
| sensitivity | Must detail be generalized, withheld, or narrowed? | generalize / restrict / hold | transform receipts, release scope, EvidenceBundle |
| review | Does steward approval become mandatory here? | review-required | ReviewRecord, queue semantics |
| release | May candidate material become publishable? | allow / deny / hold | DecisionEnvelope, ReleaseManifest / proof pack |
| runtime | May a claim-bearing surface answer or export now? | finite outcome behavior | RuntimeResponseEnvelope, EvidenceBundle |
| export | May an outward artifact leave the governed surface? | allow / deny / transform | release scope, rights, sensitivity |
| correction | How do withdrawal and supersession propagate? | withdrawn / superseded / correction-pending | CorrectionNotice, visible state cues |

### Result grammar to keep explicit

| Result / state | Meaning | Expected visible consequence |
|---|---|---|
| `allow` | Action is permitted as scoped | Continue with named obligations |
| `deny` | Rights, sensitivity, actor, or scope blocks the action | Stable denial with explicit reason |
| `generalize` | Release is allowed only after narrowing or masking | Visible transform state and receipt linkage |
| `restrict` | Action is allowed only for a narrower actor or mode | No quiet fallback to public |
| `review-required` | Machine policy alone is insufficient | Review queue plus explicit waiting reason |
| `withdrawn` | Prior surface must no longer present as current | Visible withdrawal state plus lineage |
| `superseded` | Prior surface remains inspectable but no longer current | Visible supersession pointer |
| `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | Finite runtime outcomes for claim-bearing response paths | No silent fifth outcome |

### What should trigger a bundle version bump

| Change type | Bump? | Why |
|---|---|---|
| comment-only clarification | usually no | semantics unchanged |
| helper refactor with identical semantics | maybe not | prove with unchanged fixtures and tests |
| new reason or obligation meaning | yes | public and reviewer-visible interpretation changed |
| `allow` → `generalize` / `restrict` / `deny` change | yes | trust behavior changed |
| new review-required path | yes | workflow burden changed |
| correction propagation change | yes | downstream lineage behavior changed |

[Back to top](#policy-bundles)

## Task list — definition of done

- [ ] The trust seam is named clearly.
- [ ] The bundle has an explicit version.
- [ ] Shared vocab dependencies are referenced without quietly duplicating authority.
- [ ] Paired fixtures exist for at least one happy path and one negative path.
- [ ] Paired tests exist for the same seam.
- [ ] The bundle’s downstream trust objects are named (`DecisionEnvelope`, `ReviewRecord`, `RuntimeResponseEnvelope`, `CorrectionNotice`, or release artifacts as relevant).
- [ ] Result grammar stays finite and explicit.
- [ ] Public or steward-visible state changes are documented.
- [ ] Rollback or correction expectations are noted when semantics affect release or runtime trust.
- [ ] This README still distinguishes **CONFIRMED** current repo state from **PROPOSED** starter structure.

[Back to top](#policy-bundles)

## FAQ

### Why not keep policy logic only in the parent `policy/README.md`?

Because the parent README describes the whole lane. `policy/bundles/` needs a narrower contract: what a bundle is, what must stay out, and how rule packs travel with fixtures, tests, and runtime consequences.

### Why should bundles stay separate from `policy-runtime`?

Because rule definition and rule execution are different seams. Keeping them separate makes review clearer and prevents runtime glue from silently becoming authoritative policy law.

### Why not put canonical reason or obligation registries directly here?

Because the repo already keeps contract and schema authority visibly unresolved between `contracts/` and `schemas/`. This leaf should not make that decision accidentally.

### Why is the current snapshot called scaffold-level?

Because the current public directory shows `README.md` only. A real executable bundle lane needs rule files, manifests, paired fixtures, and paired tests.

### Why does this README emphasize negative paths so heavily?

Because KFM treats fail-closed behavior as trust-preserving behavior. Denial, restriction, abstention, generalization, withdrawal, and supersession are not edge cases to hide.

[Back to top](#policy-bundles)

## Appendix

<details>
<summary>Illustrative starter bundle manifest (PROPOSED)</summary>

This example is illustrative only. It is a starter shape for discussion, not a claim about the mounted branch.

```yaml
bundle_id: policy.runtime.v1
bundle_version: 0.1.0
seam: runtime
status: draft
depends_on:
  - ../../contracts/vocab/reason_codes.json
  - ../../contracts/vocab/obligation_codes.json
rules:
  - finite_outcomes.rego
  - citation_required.rego
paired_fixtures:
  - ../fixtures/runtime/allow_answer.json
  - ../fixtures/runtime/deny_missing_rights.json
paired_tests:
  - ../tests/runtime/test_finite_outcomes.rego
emits:
  - DecisionEnvelope
  - RuntimeResponseEnvelope
review_notes:
  - "Use when claim-bearing runtime behavior must remain finite and cite-or-abstain."
```

</details>

[Back to top](#policy-bundles)
