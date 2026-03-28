<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS_VERIFICATION>
title: fixtures
type: standard
version: v1
status: draft
owners: @bartytime4life
created: <NEEDS_VERIFICATION: YYYY-MM-DD>
updated: <SET_ON_MERGE: YYYY-MM-DD>
policy_label: public
related: [../README.md, ../bundles/README.md, ../policy-runtime/README.md, ../tests/README.md, ../../contracts/README.md, ../../schemas/README.md, ../../tests/README.md, ../../tests/policy/README.md, ../../.github/workflows/README.md]
tags: [kfm, policy, fixtures, governance, verification]
notes: [Current public `main` confirms `policy/fixtures/README.md` as the only visible file in this directory; `/policy/` ownership is publicly routed to `@bartytime4life` via `/.github/CODEOWNERS`; doc_id and dates still need repo-backed verification.]
[/KFM_META_BLOCK_V2] -->

# fixtures

_Governed fixture surface for KFM policy decisions, fail-closed behavior, and trust-visible negative states._

> **Status:** `experimental`
> **Owners:** `@bartytime4life`
> **Path:** `policy/fixtures/README.md`
> **Current public inventory:** `README.md` only on public `main`
> **Repo fit:** current public repo confirms this directory exists as a real child lane under `policy/`; doctrine expects this lane to hold positive and negative policy examples that prove deny-by-default behavior before policy claims graduate into merge gates or runtime trust surfaces
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

![status: experimental](https://img.shields.io/badge/status-experimental-orange)
![owners: @bartytime4life](https://img.shields.io/badge/owners-%40bartytime4life-blue)
![path: policy/fixtures](https://img.shields.io/badge/path-policy%2Ffixtures-lightgrey)
![repo: public](https://img.shields.io/badge/repo-public-brightgreen)
![truth: bounded](https://img.shields.io/badge/truth-bounded-yellow)
![surface: policy fixtures](https://img.shields.io/badge/surface-policy_fixtures-6f42c1)

> [!IMPORTANT]
> The current public `main` branch confirms `policy/fixtures/` exists and that this README is presently the only visible file in the directory.
> The richer structure below is a doctrine-aligned starter pattern, not proof that a mounted fixture inventory already exists.

## Scope

`policy/fixtures/` is the narrow seam where KFM turns policy doctrine into concrete example cases that can be reviewed, diffed, tested, and eventually gated.

Use this directory for policy-semantic examples that answer questions like these:

- What does an **allow** case look like when rights, sensitivity, and evidence posture are all acceptable?
- What should a **deny**, **generalize**, **restrict**, or **needs-review** case prove before publication or runtime exposure?
- How do stable **reason codes** and **obligation codes** stay visible across bundle changes, test runs, and review?
- Which negative states must remain inspectable rather than being polished away?

Do **not** treat this directory as a generic examples bucket. In KFM, fixtures are part of the trust story: they prove that the same decision grammar survives policy review, CI checks, and runtime mediation.

### Evidence posture used in this README

| Label | Meaning in this file |
| --- | --- |
| **CONFIRMED** | Supported by the current public repo tree or by March 2026 KFM doctrine that directly names policy bundles, fixtures, tests, and finite outcomes. |
| **INFERRED** | Conservative conclusion drawn from the public tree plus adjacent repo docs, useful for boundary interpretation but not yet proof of mounted executable behavior. |
| **PROPOSED** | A doctrine-consistent starter shape, fixture family, naming pattern, or workflow that is useful now but not yet proven as mounted repo reality. |
| **UNKNOWN** | Not supported strongly enough in the current evidence to present as a settled fixture inventory or executable harness fact. |
| **NEEDS VERIFICATION** | A value, path, owner, command, or lifecycle detail that should be checked on the active branch before merge. |

### Working evidence frame

| Source role | What it establishes for this README |
| --- | --- |
| Current public repo tree | `policy/fixtures/` exists and is scaffold-only today; `policy/` currently exposes `bundles/`, `fixtures/`, `policy-runtime/`, and `tests/` as sibling lanes. |
| `/.github/CODEOWNERS` | Public ownership currently routes `/policy/` to `@bartytime4life`, which is strong enough to carry that owner value in this README until narrower path ownership is checked in. |
| `policy/README.md` | The parent directory explicitly assigns `policy/` responsibility for executable bundles, fixtures, tests, reasons, obligations, and finite policy/result grammar. |
| `policy/tests/README.md`, `tests/policy/README.md`, and `.github/workflows/README.md` | Fixture cases have distinct downstream proof lanes: bundle-local policy tests, repo-facing policy verification, and workflow/documented gate scaffolding should stay separate rather than being silently collapsed into this directory. |
| March 2026 KFM doctrine + repo-grounded sprint | Policy fixtures are load-bearing verification artifacts tied to `DecisionEnvelope`, `ReviewRecord`, `ReleaseManifest`, `EvidenceBundle`, `RuntimeResponseEnvelope`, and visible correction lineage; the next enforcement slice still depends on valid/invalid fixtures plus a deterministic validator and merge gate. |

<p align="right"><a href="#fixtures">Back to top</a></p>

## Repo fit

This README sits below the human-facing `policy/README.md` surface and above any future executable harness that consumes fixture cases.

### Current public snapshot

| Surface | Current public evidence | Why it matters |
| --- | --- | --- |
| `policy/fixtures/` | README only, currently the note "Scaffold directory defined from repository README guidance." | The directory is real, but mounted fixture inventory beyond this scaffold is not yet evidenced. |
| `policy/` | `README.md`, `bundles/`, `fixtures/`, `policy-runtime/`, `tests/` | Fixtures are meant to live beside policy bundles and policy-local tests, not as an orphaned examples folder. |
| `policy/policy-runtime/` | Present as a public repo lane | The public tree currently shows a runtime-adjacent seam under `policy/`, even though doctrine also sketches a broader `packages/policy-runtime/` direction. This README should not silently resolve that tension. |

### Upstream and downstream links

| Direction | Path | Why it matters |
| --- | --- | --- |
| Upstream | [`../README.md`](../README.md) | Parent policy boundary, result grammar, and repo-grounded evidence posture. |
| Lateral | [`../bundles/README.md`](../bundles/README.md) | Canonical place for executable policy rules. Fixtures should prove bundle meaning, not replace it. |
| Lateral | [`../policy-runtime/README.md`](../policy-runtime/README.md) | Current public runtime-adjacent seam under `policy/`; verify whether it stays here or moves elsewhere. |
| Lateral | [`../tests/README.md`](../tests/README.md) | Policy-local test lane that should consume or validate fixture packs. |
| Lateral | [`../../contracts/README.md`](../../contracts/README.md) | Contract and vocabulary boundary. Schema authority must not drift into fixture-only examples. |
| Lateral | [`../../schemas/README.md`](../../schemas/README.md) | Keeps schema-home ambiguity visible and prevents parallel registries. |
| Downstream | [`../../tests/README.md`](../../tests/README.md) | Repo-wide verification families, correction drills, and proof expectations. |
| Downstream | [`../../tests/policy/README.md`](../../tests/policy/README.md) | Repo-facing policy verification lane that should prove bundle and fixture semantics survive broader test pressure. |
| Workflow guardrail | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | Current public workflow lane documents automation scaffolding and README-only workflow inventory on public `main`. |

> [!NOTE]
> `policy/README.md` already treats `allow`, `deny`, `generalize`, `restrict`, `needs-review`, `withdraw`, and `supersede` as the core fixture-worthy policy states. This README keeps that grammar stable rather than inventing a competing one.

## Accepted inputs

The safest reading is: keep `policy/fixtures/` compact, machine-reviewable, and outcome-oriented.

| Belongs here | Why it belongs here | Typical examples |
| --- | --- | --- |
| Positive and negative policy cases | They prove fail-closed behavior instead of merely describing it. | `allow`, `deny`, `generalize`, `restrict`, `needs-review`, `withdraw`, `supersede` packs. |
| Fixture pairs tied to stable decision grammar | Each policy seam needs both happy-path and negative-path pressure. | input + expected result + expected reasons + expected obligations. |
| Bundle-facing case manifests | They help reviewers see which bundle or vocabulary version a case is exercising. | manifest files, small index files, suite descriptors. |
| Public-safe domain examples | They make policy behavior realistic without introducing avoidable rights risk. | thin hydrology, hazard, or public infrastructure examples. |
| Minimal steward notes | They keep fixture intent reviewable when filenames alone are not enough. | short README fragments, glossary notes, review hints local to one fixture family. |

### Minimum bar for any fixture added here

- It names a real policy seam: **admission**, **rights**, **sensitivity**, **review-release**, **runtime**, or **correction**.
- It makes the expected result explicit.
- It makes expected **reason codes** explicit.
- It makes expected **obligation codes** explicit when obligations exist.
- It says whether the case is public-safe, restricted, or review-bearing.
- It can be traced to an adjacent contract, bundle, or trust object.
- It avoids silent overwrite of an older semantic case; supersession should stay visible.

## Exclusions

| Does **not** belong here | Put it instead | Why |
| --- | --- | --- |
| Executable policy rule bodies | [`../bundles/`](../bundles/) | Bundles own rule logic; fixtures only prove rule behavior. |
| Runtime loaders, adapters, or decision assembly code | [`../policy-runtime/`](../policy-runtime/) or the verified runtime package | Execution glue is adjacent to fixtures, but it is not the fixture surface itself. |
| Canonical JSON Schema / OpenAPI definitions | [`../../contracts/`](../../contracts/) and [`../../schemas/`](../../schemas/) | Shared object shape and schema authority must not drift into fixture cases. |
| Repo-facing policy proof suites, e2e drills, or broader correction/release verification | [`../../tests/policy/`](../../tests/policy/) and [`../../tests/`](../../tests/) | `policy/fixtures/` should stay focused on semantic cases, not absorb broader verification ownership. |
| RAW / WORK / QUARANTINE / PROCESSED / CATALOG / PUBLISHED data | `../../data/` | Policy governs exposure and movement, but it is not the canonical store. |
| Secrets, live credentials, or operational key material | secret manager / host configuration | Sensitive operational material should never live in fixture packs. |
| UI-only conditionals used as faux policy | nowhere | KFM requires backend and review enforcement, not policy theater in presentation code. |

## Directory tree

### Current public repo evidence (**CONFIRMED**)

```text
policy/
├── README.md
├── bundles/
├── fixtures/
├── policy-runtime/
└── tests/

policy/fixtures/
└── README.md
```

### Doctrine-aligned starter shape (**PROPOSED**)

```text
policy/fixtures/
├── README.md
├── shared/
│   ├── suite-index.yaml
│   └── public-safe-notes.md
├── admission/
├── rights/
├── sensitivity/
├── review-release/
├── runtime/
└── correction/
```

### Result-oriented subshape (**PROPOSED**)

```text
policy/fixtures/runtime/
├── answer/
├── abstain/
├── deny/
└── error/

policy/fixtures/sensitivity/
├── allow/
├── generalize/
├── restrict/
└── needs-review/
```

> [!WARNING]
> The trees under **PROPOSED** are starter scaffolds, not mounted inventory. Keep them labeled that way until the active branch proves a real fixture family layout.

<p align="right"><a href="#fixtures">Back to top</a></p>

## Quickstart

### 1) Inspect the real surface before editing it

```bash
find . -maxdepth 5 \
  \( -path './policy/fixtures' \
   -o -path './policy/bundles' \
   -o -path './policy/policy-runtime' \
   -o -path './policy/tests' \
   -o -path './tests/policy' \
   -o -path './contracts' \
   -o -path './schemas' \
   -o -path './.github/workflows' \) \
  -print 2>/dev/null
```

### 2) Trace trust-bearing objects and finite outcome grammar that fixture cases should exercise

```bash
grep -R -nE \
  'DecisionEnvelope|ReviewRecord|ReleaseManifest|ReleaseProofPack|EvidenceBundle|RuntimeResponseEnvelope|CorrectionNotice|reason_codes|obligation_codes|rights_class|sensitivity_class|policy_bundle_version|ANSWER|ABSTAIN|DENY|ERROR' \
  policy tests contracts docs packages apps .github 2>/dev/null || true
```

### 3) Check whether a runnable policy harness already exists

```bash
find . -type f \
  \( -name '*.rego' -o -name '*fixture*' -o -name '*conftest*' -o -name '*policy*' \) \
  | sort
```

### 4) Add cases only after the harness boundary is clear

```text
<NEEDS_VERIFICATION: replace with the repo's real policy-fixture command>
```

> [!TIP]
> If the repo still lacks a real validator command, keep this README honest about that gap instead of inventing one. The March 2026 repo-grounded sprint treats valid/invalid fixtures plus a deterministic validator as the next highest-value trust slice.

## Usage

### Add a new fixture pack safely

1. Start with the **policy seam**, not the filename.
2. Decide the expected result first: `allow`, `deny`, `generalize`, `restrict`, `needs-review`, `withdraw`, `supersede`, or a runtime-envelope outcome where that is the actual seam under test.
3. Record stable `reason_codes` and `obligation_codes` alongside the expected result.
4. Link the case to the nearest governing object or contract family: `DecisionEnvelope`, `ReviewRecord`, `ReleaseManifest`, `EvidenceBundle`, `RuntimeResponseEnvelope`, or `CorrectionNotice` when applicable.
5. Pair every happy path with a negative path.
6. Prefer public-safe examples first; hydrology-style public fixtures are a good starter burden because they exercise time, evidence, and correction without forcing the most sensitive rights cases first.

### Change an existing fixture safely

1. Prefer additive evolution over silent replacement.
2. If meaning changes, mark the older case superseded or version-bumped rather than quietly editing history.
3. Update sibling docs and tests in the same PR, including `policy/tests/` and, when the change escapes the local seam, `tests/policy/`.
4. Keep old cases interpretable long enough to preserve regression meaning and audit context.
5. Do not let a convenience test case become the unofficial schema or vocabulary authority.

### Review a fixture PR like a trust surface

- Does the case name a real seam?
- Does it prove a meaningful negative path?
- Are reasons and obligations stable and explicit?
- Is the case public-safe enough for its lane?
- Does it avoid duplicating contract or runtime authority?
- Does it hand off cleanly to `policy/tests/` or `tests/policy/` when broader proof is required?
- Does it preserve visible correction / supersession behavior where outward truth changes?

## Diagram

```mermaid
flowchart LR
    A[contracts / vocab] --> B[policy bundles]
    B --> C[policy fixtures]
    C --> D[policy-local tests<br/>(policy/tests)]
    C --> E[repo-facing policy tests<br/>(tests/policy)]
    D --> F[merge gates / workflows]
    E --> F
    B --> G[policy runtime<br/>(current public lane: policy/policy-runtime)]
    G --> H[DecisionEnvelope / ReviewRecord / RuntimeResponseEnvelope]
    H --> I[trust-visible surfaces]
    J[CorrectionNotice] --> H
    J --> I
```

Fixtures matter because they sit between abstract rule text and claim-bearing outward behavior. They are the reviewable proof that bundle semantics, negative outcomes, and correction lineage survive contact with actual cases.

## Tables

### Fixture family matrix

| Family | What it should prove | Typical results / states | Adjacent trust objects |
| --- | --- | --- | --- |
| `admission/` | Source-intake policy behavior | `allow`, `deny`, `needs-review` | `SourceDescriptor`, `DecisionEnvelope` |
| `rights/` | Release eligibility under rights posture | `allow`, `restrict`, `deny` | `DecisionEnvelope`, `ReviewRecord`, `ReleaseManifest` |
| `sensitivity/` | Exact-location, masking, aggregation, or public-safe transforms | `generalize`, `restrict`, `deny`, `needs-review` | `DecisionEnvelope`, transform receipts, correction lineage |
| `review-release/` | Promotion and publication governance | `allow`, `needs-review`, `deny` | `DecisionEnvelope`, `ReviewRecord`, `ReleaseManifest`, `ReleaseProofPack` |
| `runtime/` | Claim-bearing response shaping | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | `EvidenceBundle`, `RuntimeResponseEnvelope` |
| `correction/` | Withdrawal, supersession, and stale-visible behavior | `withdraw`, `supersede`, `stale-visible` | `CorrectionNotice`, `ReleaseManifest`, downstream trust cues |

### Fixture-to-proof handoff

| Surface | What it should own | What it should not quietly absorb |
| --- | --- | --- |
| `policy/fixtures/` | Semantic policy cases and expected outcomes | Executable rule bodies, repo-wide proof suites, or runtime glue |
| `policy/tests/` | Bundle-local assertions close to the seam | Broader repo-facing policy proof ownership |
| `tests/policy/` | Repo-facing proof that policy semantics survive broader verification and gates | Bundle-local fixture authoring or rule ownership |

### Policy result grammar vs runtime outcome grammar

| Layer | Grammar | Why this distinction matters |
| --- | --- | --- |
| Policy decision layer | `allow`, `deny`, `generalize`, `restrict`, `needs-review`, `withdraw`, `supersede` | These states explain what governance decided and what obligations follow. |
| Runtime envelope layer | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | These states explain what the user-facing request path can honestly do at request time. |

## Task list

- [ ] Replace `doc_id` and date placeholders with repo-backed values.
- [ ] Verify whether the public `policy/policy-runtime/` lane is intentional long-term structure or a temporary scaffold.
- [ ] Confirm the real fixture runner / validator command before documenting it as current truth.
- [ ] Ensure at least one positive and one negative case exist for every mounted fixture family.
- [ ] Keep reason / obligation vocabulary ownership explicit and non-duplicative.
- [ ] Verify that fixture semantics match the same visible trust grammar used by `policy/tests/`, `tests/policy/`, and workflow gates.
- [ ] Keep correction, supersession, and stale-visible behavior explicit where outward meaning can change.
- [ ] Prefer public-safe starter cases before higher-sensitivity lanes.

## FAQ

### Does this README prove that runnable policy fixtures already exist here?

No. The current public repo proves the directory and its scaffold README, not a mounted executable fixture inventory.

### Should contract-shape examples live here?

Only when the example is primarily exercising **policy semantics**. Canonical schema and OpenAPI authority still belongs in `contracts/` and `schemas/`.

### Is `OPA/Rego` confirmed for this directory?

It is a strong design fit in doctrine and repo guidance, but this README should keep actual engine adoption marked **NEEDS VERIFICATION** until the active branch proves it.

### How is this different from `policy/tests/` or `tests/policy/`?

`policy/fixtures/` owns semantic cases. `policy/tests/` owns bundle-local assertions close to the rule seam. `tests/policy/` is the repo-facing proof lane that shows those semantics survive broader verification pressure, gates, and downstream trust surfaces.

### Why not put all fixtures under `tests/` and keep `policy/fixtures/` empty?

Because KFM treats policy as a first-class governed surface. A policy-local fixture lane keeps decision grammar, reasons, obligations, and review semantics close to the bundles they explain, while broader repo-facing verification still lives where the current public test docs place it.

### What should block broader publication work?

Missing or invalid fixture coverage for trust-bearing policy seams, unclear vocabulary ownership, missing negative-path cases, and any path that lets runtime or release behavior drift from documented decision grammar.

<p align="right"><a href="#fixtures">Back to top</a></p>

## Appendix

<details>
<summary><strong>Illustrative starter case shape (PROPOSED)</strong></summary>

This is an illustrative example only. It shows the kind of information a policy-semantic fixture should make explicit; it is not proof that the mounted repo already uses this exact schema.

```yaml
case_id: pf.sensitivity.generalize.001
seam: sensitivity
summary: Public map request is allowed only after geometry reduction.
input:
  actor_role: public
  surface_class: map
  action: publish
  rights_class: open
  sensitivity_class: public_location_sensitive
expected:
  result: generalize
  reason_codes:
    - PUBLIC_SAFE_AFTER_GENERALIZATION
  obligation_codes:
    - GENERALIZE_GEOMETRY
    - REQUIRE_CITATION
    - RECORD_AUDIT
notes:
  public_safe: true
  related_objects:
    - DecisionEnvelope
    - ReleaseManifest
    - CorrectionNotice
```

</details>

<details>
<summary><strong>PROPOSED naming guidance</strong></summary>

Use naming that makes seam and expected outcome obvious to reviewers. A safe starter convention is:

```text
<seam>.<subject>.<expected-result>.<nnn>.<json|yaml>
```

Examples:

```text
rights.release.allow.001.yaml
sensitivity.geometry.generalize.002.yaml
runtime.focus.answer.003.yaml
runtime.focus.abstain.004.yaml
correction.release.supersede.005.yaml
```

Keep meaning changes explicit. Do not silently repurpose an old filename for a new decision grammar.

</details>

<details>
<summary><strong>First-wave family order (PROPOSED)</strong></summary>

1. `rights/` and `sensitivity/` — because deny/default-deny and public-safe generalization are core KFM trust seams.
2. `review-release/` — because publication is a governance event, not just a successful deploy.
3. `runtime/` — because outward claims must stay finite, cite-backed, and abstain-capable.
4. `correction/` — because visible supersession and withdrawal prevent silent overwrite.
5. `admission/` — add once source onboarding and intake-side policy checks are mounted enough to exercise concretely.

</details>

<p align="right"><a href="#fixtures">Back to top</a></p>
