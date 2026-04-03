<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION_UUID
title: Policy
type: standard
version: v1
status: review
owners: @bartytime4life
created: YYYY-MM-DD
updated: 2026-04-03
policy_label: public
related: ["../README.md", "../CONTRIBUTING.md", "../.github/README.md", "../.github/workflows/README.md", "../contracts/README.md", "../schemas/README.md", "../data/README.md", "../packages/policy/README.md", "../tests/policy/README.md", "./bundles/README.md", "./fixtures/README.md", "./policy-runtime/README.md", "./tests/README.md"]
tags: [kfm, policy, governance, trust, review]
notes: ["doc_id and created date require repo-backed verification before merge", "updated reflects this 2026-04-03 revision draft", "current public main confirms policy/, policy/bundles/, policy/fixtures/, policy/policy-runtime/, policy/tests/, packages/policy/, and tests/policy/ documentation surfaces", "inspected child policy lanes and .github/workflows remain README-only on public main", "OPA/Rego is treated here as a documented starter direction, not as confirmed checked-in bundle adoption"]
[/KFM_META_BLOCK_V2] -->

# Policy

_Governed, executable policy surface for KFM publication, runtime trust, rights and sensitivity handling, and visible correction._

> **Status:** `experimental`  
> **Owners:** `@bartytime4life`  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![owners](https://img.shields.io/badge/owners-%40bartytime4life-0969da) ![surface](https://img.shields.io/badge/surface-policy-blue) ![inventory](https://img.shields.io/badge/inventory-lane%20visible%20on%20public%20main-lightgrey) ![posture](https://img.shields.io/badge/posture-deny--by--default-critical) ![engine](https://img.shields.io/badge/engine-OPA%2FRego%20starter-lightgrey)  
> **Repo fit:** `policy/README.md` · parent lane for [`./bundles/README.md`](./bundles/README.md), [`./fixtures/README.md`](./fixtures/README.md), [`./policy-runtime/README.md`](./policy-runtime/README.md), and [`./tests/README.md`](./tests/README.md) · adjacent machine-contract and authority boundaries at [`../contracts/README.md`](../contracts/README.md) and [`../schemas/README.md`](../schemas/README.md) · adjacent shared internal support at [`../packages/policy/README.md`](../packages/policy/README.md) · broader proof lane at [`../tests/policy/README.md`](../tests/policy/README.md) · workflow guardrail at [`../.github/workflows/README.md`](../.github/workflows/README.md)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Policy seams](#policy-seams) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Gates and definition of done](#gates-and-definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> Current public `main` now confirms `policy/` as a real top-level lane with child policy surfaces and adjacent package/test boundaries. The inspected public tree is still documentation-heavy, though: the child policy lanes and `packages/policy/` are README surfaces, and `.github/workflows/` is README-only on public `main`. Keep **current-tree facts** separate from **proposed executable fill**.

## Scope

`policy/` is where KFM turns governance from prose into reviewable, machine-checkable behavior.

In KFM, policy is not a detached compliance appendix. It is the gate layer that shapes source admission, rights handling, sensitivity and redaction, review and release, runtime answers, correction and withdrawal, and the trust cues users see in the shell.

### Evidence posture used here

| Label | Meaning in this README |
|---|---|
| **CONFIRMED** | Directly supported by attached KFM doctrine or the current public `main` tree |
| **INFERRED** | Strongly implied by repeated doctrine or adjacent repo docs, but not re-proven as checked-in implementation behavior |
| **PROPOSED** | Commit-ready structure or practice that fits KFM doctrine but is not asserted as current repo reality |
| **UNKNOWN** | Not supported strongly enough to present as current branch or runtime fact |
| **NEEDS VERIFICATION** | Placeholder, branch-specific, or platform-only detail that should be checked before merge |

### Load-bearing commitments preserved here

| Commitment | Practical consequence |
|---|---|
| Default deny / fail closed | Missing rights, missing evidence linkage, unresolved sensitivity, or missing review posture should end in a governed negative outcome rather than a silent allow |
| Reasons and obligations stay explicit | Policy should emit stable vocabularies instead of drifting into prose-only decisions |
| Publication is a governance event | Publishable output must be explainable through decision, review, release, and correction artifacts |
| Runtime outcomes stay finite | Claim-bearing runtime behavior should converge on explicit outcomes, not graceful-looking ambiguity |
| Correction remains visible | `withdrawn`, `superseded`, `review_pending`, and similar states must survive into downstream surfaces |
| UI reflects enforcement, but does not replace it | Trust cues belong in the shell, but backend, review, release, and runtime gates remain primary |

[Back to top](#policy)

## Repo fit

The earlier “README-only / target-shape only” picture is no longer accurate for public `main`. The current public tree proves a fuller policy lane, but it still does **not** prove populated rule packs, fixture cases, runnable policy suites, or checked-in workflow YAML under `.github/workflows/`.

### Current public snapshot

| Surface | Current public `main` | What that proves |
|---|---|---|
| `policy/README.md` | Present | `policy/` is a real repo-root lane, not a hypothetical target |
| `policy/bundles/README.md` | Present; directory is README-only | The executable bundle lane exists publicly, but populated bundle artifacts are not evidenced here |
| `policy/fixtures/README.md` | Present; directory is README-only | The fixture lane exists publicly, but fixture cases are not evidenced here |
| `policy/policy-runtime/README.md` | Present; directory is README-only | Runtime-policy coordination is documented, but mounted runtime glue is not proven here |
| `policy/tests/README.md` | Present; directory is README-only | Bundle-local verification is documented as a separate surface |
| `packages/policy/README.md` | Present; package directory is README-only in inspected surface | A separate shared internal policy-support boundary is documented under `packages/` |
| `tests/policy/README.md` | Present; directory is README-only in inspected surface | Repo-facing policy behavior proof is documented separately from `policy/tests/` |
| `.github/workflows/README.md` | Present; workflow lane is README-only | Workflow claims must stay conservative on public `main` |

### Upstream, lateral, and downstream links

| Direction | Surface | Why it matters |
|---|---|---|
| Upstream | [`../README.md`](../README.md) | Root system identity, doctrine summary, and public-tree navigation |
| Upstream | [`../CONTRIBUTING.md`](../CONTRIBUTING.md) | Review discipline for policy-significant change |
| Lateral | [`../contracts/README.md`](../contracts/README.md) | Current machine-contract lane for trust-bearing objects such as `DecisionEnvelope`, `EvidenceBundle`, and `RuntimeResponseEnvelope` |
| Lateral | [`../schemas/README.md`](../schemas/README.md) | Authority/boundary guide that keeps schema-home ambiguity visible |
| Lateral | [`../data/README.md`](../data/README.md) | Truth-path zones and release-adjacent data surfaces policy governs but does not own |
| Lateral | [`./bundles/README.md`](./bundles/README.md) | Seam-local rule-pack lane |
| Lateral | [`./fixtures/README.md`](./fixtures/README.md) | Seam-local positive/negative example lane |
| Lateral | [`./tests/README.md`](./tests/README.md) | Bundle-local assertion lane |
| Lateral | [`./policy-runtime/README.md`](./policy-runtime/README.md) | Runtime-policy coordination lane inside top-level `policy/` |
| Downstream | [`../packages/policy/README.md`](../packages/policy/README.md) | Shared internal code boundary that should remain subordinate to repo-authoritative policy |
| Downstream | [`../tests/policy/README.md`](../tests/policy/README.md) | Broader repo-facing proof that policy behavior survives into runtime, release, and correction lanes |
| Guardrail | [`../.github/workflows/README.md`](../.github/workflows/README.md) | Documents current workflow-lane visibility and future merge-gate expectations |

> [!WARNING]
> Do not let `policy/` quietly resolve `contracts/` versus `schemas/` by duplication. Current public docs keep `contracts/` as the machine-contract lane while `schemas/` exists specifically to keep schema-home authority explicit and singular.

[Back to top](#policy)

## Accepted inputs

`policy/` should stay compact, typed, and execution-oriented.

| Input class | What belongs here | Typical examples |
|---|---|---|
| Bundle rule packs | Rule families that decide one trust seam or seam family | seam-local `*.rego`, helper modules, bundle manifests |
| Policy fixtures | Positive and negative cases that prove deny-by-default behavior | `allow`, `deny`, `generalize`, `restrict`, `needs-review`, `withdraw`, `supersede` examples |
| Bundle-local assertions | Checks that prove one bundle family behaves as documented | Conftest/OPA checks, seam-local regression packs, outcome grammar assertions |
| Runtime-policy coordination notes | Small docs that explain how policy semantics should be consumed without relocating policy authority | decision assembly notes, runtime parity notes, mediation guidance |
| Shared internal support code | Package code that helps governed runtimes consume policy consistently | loaders, adapters, mediation helpers under `../packages/policy/` |
| Steward-facing notes | Minimal human-readable notes needed to review policy-significant changes | glossary notes, dependency maps, review notes |

### Working placement rule

If the change mostly defines **policy law**, it belongs under `./bundles/`, `./fixtures/`, or `./tests/`.  
If it mostly defines **shared internal code**, it belongs under [`../packages/policy/README.md`](../packages/policy/README.md).  
If it mostly proves **repo-facing policy behavior under pressure**, it belongs under [`../tests/policy/README.md`](../tests/policy/README.md).

## Exclusions

| Does **not** belong in `policy/` | Put it instead | Why |
|---|---|---|
| Canonical JSON Schema / OpenAPI definitions | [`../contracts/`](../contracts/) | Shared trust-object shape should not drift into rule-pack lanes |
| A second authoritative schema registry | [`../schemas/README.md`](../schemas/README.md) boundary guidance | Parallel schema homes increase ambiguity, not resilience |
| Shared internal package code treated as repo-authoritative policy | [`../packages/policy/README.md`](../packages/policy/README.md) | Support code should stay subordinate to the top-level policy lane |
| Broader repo-facing policy proof | [`../tests/policy/README.md`](../tests/policy/README.md) | `policy/tests/` and `tests/policy/` have different scopes |
| API handlers, workers, or UI conditionals | governed app/package boundaries under `../apps/` and `../packages/` | Enforcement code is not the same artifact as the policy pack |
| RAW / WORK / QUARANTINE / PROCESSED / CATALOG / PUBLISHED artifacts | [`../data/README.md`](../data/README.md) | Policy governs movement and exposure; it is not the canonical store |
| Workflow orchestration or platform settings | [`../.github/workflows/README.md`](../.github/workflows/README.md) and GitHub platform settings | Public docs do not yet prove checked-in YAML gate coverage |
| Secrets, keys, `.env` files, or live credentials | secret manager / host configuration | Sensitive operational material must not live in the policy tree |

[Back to top](#policy)

## Directory tree

### Current public `main` (**CONFIRMED**)

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

### Adjacent verified policy-facing surfaces (**CONFIRMED**)

```text
packages/
└── policy/
    └── README.md

tests/
└── policy/
    └── README.md

.github/
└── workflows/
    └── README.md
```

<details>
<summary><strong>Possible next executable fill (PROPOSED)</strong></summary>

```text
policy/
├── bundles/
│   ├── shared/
│   ├── admission/
│   ├── rights/
│   ├── sensitivity/
│   ├── review/
│   ├── release/
│   ├── runtime/
│   └── correction/
├── fixtures/
│   ├── allow/
│   ├── deny/
│   ├── generalize/
│   ├── restrict/
│   ├── needs-review/
│   └── correction/
├── tests/
│   ├── decision-grammar/
│   ├── seam-local-regression/
│   └── runtime-parity/
└── policy-runtime/
    └── coordination-notes/
```

This is a starter fill pattern, not a claim about the checked-out branch.
</details>

[Back to top](#policy)

## Policy seams

Policy is most useful when it is organized by **responsibility seam** and kept honest about what each lane does.

| Surface / seam | Current public state | Why it exists | What it still does **not** prove |
|---|---|---|---|
| `./bundles/` | README-only | Holds seam-local rule packs and finite decision grammar | Checked-in `.rego` or equivalent rule files |
| `./fixtures/` | README-only | Holds positive and negative examples that make deny-by-default behavior reviewable | Mounted fixture payloads or case inventory |
| `./tests/` | README-only | Holds bundle-local assertions close to the policy lane | Runnable suite depth or actual toolchain |
| `./policy-runtime/` | README-only | Documents runtime-facing policy semantics and coordination inside top-level `policy/` | Mounted runtime glue, loaders, or adapters |
| `../packages/policy/` | README-only in inspected surface | Holds shared internal policy-support code that should stay subordinate to repo-authoritative policy | Populated package code or resolved import shape |
| `../tests/policy/` | README-only in inspected surface | Holds broader repo-facing proof that policy behavior survives into runtime, release, and correction lanes | End-to-end coverage or current runner wiring |
| `../.github/workflows/` | README-only | Holds workflow expectations and release/promotion guardrail documentation | Checked-in merge-blocking workflow YAML on current public `main` |

### Trust seams policy should ultimately govern

| Trust seam | Primary objects policy should touch | Fail-closed expectation |
|---|---|---|
| Source admission | `SourceDescriptor`, `IngestReceipt`, `ValidationReport` | Unresolved rights, malformed shape, or unsupported support/cadence should quarantine or deny |
| Rights and sensitivity | `DecisionEnvelope`, `ReviewRecord`, transform receipts | Exact-location or reuse risk should never fall through to public-safe output silently |
| Review and release | `DecisionEnvelope`, `ReviewRecord`, `ReleaseManifest` / `ReleaseProofPack` | No silent publish path |
| Runtime answer handling | `EvidenceBundle`, `RuntimeResponseEnvelope` | Empty scope, stale support, unresolved policy, or uncited output should produce a governed negative outcome |
| Correction and withdrawal | `CorrectionNotice`, release refs, rebuild refs | Correction must propagate visibly rather than erasing history |

[Back to top](#policy)

## Quickstart

### 1) Inspect the current policy-facing surfaces

```bash
find policy packages/policy tests/policy .github/workflows -maxdepth 3 -type f 2>/dev/null | sort
```

### 2) Inspect the current contract and schema boundaries

```bash
find contracts schemas -maxdepth 3 -type f 2>/dev/null | sort
```

### 3) Trace trust-bearing object names across repo surfaces

```bash
grep -RInE \
  'DecisionEnvelope|ReviewRecord|ReleaseManifest|ReleaseProofPack|EvidenceBundle|RuntimeResponseEnvelope|CorrectionNotice|reason_codes|obligation_codes|rights_class|sensitivity_class' \
  policy packages tests contracts schemas docs apps 2>/dev/null || true
```

### 4) Inspect workflow claims before assuming checked-in gates

```bash
find .github/workflows -maxdepth 2 -type f 2>/dev/null | sort
```

### 5) Surface any checked-in policy rule or registry files

```bash
find . -type f \
  \( -name '*.rego' -o -name '*reason_codes*' -o -name '*obligation_codes*' -o -name '*reviewer_roles*' \) \
  | sort
```

> [!NOTE]
> These are discovery commands, not proof by themselves. Update this README against the checked-out branch before letting its claims harden into review or release assumptions.

[Back to top](#policy)

## Usage

### Add or change a policy family

1. Start with the seam, not the filename: admission, rights, sensitivity, review, release, runtime, export, or correction.
2. Decide whether the change belongs in `./bundles/`, `./fixtures/`, `./tests/`, `./policy-runtime/`, `../packages/policy/`, or `../tests/policy/`.
3. Keep machine-contract and schema authority singular: point to `../contracts/` and `../schemas/` instead of re-inventing their ownership inside `policy/`.
4. Pair every bundle-significant change with fixtures and bundle-local assertions.
5. If runtime, release, or correction behavior changes, extend the broader proof lane in `../tests/policy/` or the relevant end-to-end surface.
6. Document which downstream trust objects must reflect the result.

### Keep reasons and obligations stable

- **Reasons** explain why a result occurred.
- **Obligations** explain what must happen next.
- Semantically changing a reason or obligation code should version the relevant bundle or registry.
- Transform obligations should create explicit receipts or visible downstream consequences, not invisible UI behavior.
- Exception handling must stay review-bearing. No quiet override path belongs in normal flow.

### Illustrative starter decision (**PROPOSED**)

```yaml
input:
  actor_role: public
  surface_class: focus
  action: answer
  release_id: rel.example.public.v1
  rights_class: open
  sensitivity_class: public

decision:
  result: allow
  reason_codes:
    - PUBLIC_SAFE
  obligation_codes:
    - REQUIRE_CITATION
    - RECORD_AUDIT
```

Use this as a starter fixture shape, not as proof that the checked-out branch already emits this exact payload.

### What policy should prove before broader expansion

| Policy seam | Minimum thing to prove |
|---|---|
| Review / release | Publish or block through explicit `DecisionEnvelope` and, where required, `ReviewRecord` |
| Runtime ask | No uncited fifth outcome; only `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` |
| Generalization | A visible transform path with obligation handling and receipt linkage |
| Correction | Withdrawal and supersession remain inspectable after release |
| CI / runtime parity | The same core semantics survive both pull-request gates and live requests |

[Back to top](#policy)

## Diagram

```mermaid
flowchart LR
  Root["../README.md"] --> Policy["policy/README.md"]
  Policy --> Bundles["./bundles/"]
  Policy --> Fixtures["./fixtures/"]
  Policy --> PolicyTests["./tests/"]
  Policy --> PolicyRuntime["./policy-runtime/"]

  Contracts["../contracts/README.md"] --> TrustObjects["DecisionEnvelope<br/>ReviewRecord<br/>ReleaseManifest / ReleaseProofPack<br/>EvidenceBundle<br/>RuntimeResponseEnvelope<br/>CorrectionNotice"]
  Schemas["../schemas/README.md"] -. boundary / authority .-> Contracts

  Bundles --> Fixtures
  Fixtures --> PolicyTests
  PolicyRuntime --> PackageSupport["../packages/policy/"]
  PolicyTests --> RepoProof["../tests/policy/"]
  RepoProof --> Workflows["../.github/workflows/README.md"]
  TrustObjects --> Surfaces["Map / Dossier / Story / Focus / Export"]
```

Above: the boxes are the **currently verified documentation surfaces**; the trust objects and outward surfaces are the doctrine-bearing downstream responsibilities those lanes are expected to serve.

## Tables

### Lane responsibilities

| Surface | Owns what | Should stay out of |
|---|---|---|
| `policy/README.md` | Parent lane contract and current-state guide | Shadow runtime code or shadow schema authority |
| `policy/bundles/` | Rule families and finite decision grammar | Generic fixtures, generic tests, and app glue |
| `policy/fixtures/` | Small positive/negative examples | Canonical contracts or runtime code |
| `policy/tests/` | Bundle-local assertions | Broader repo-facing proof responsibilities |
| `policy/policy-runtime/` | Runtime-policy coordination notes | Claiming mounted runtime glue before branch proof |
| `packages/policy/` | Shared internal support code | Replacing top-level policy as repo-authoritative surface |
| `tests/policy/` | Repo-facing proof that policy behavior survives under pressure | Becoming a second bundle tree |
| `.github/workflows/` | Workflow-lane documentation and future gate burden | Being treated as checked-in YAML proof when only README is visible |

### Policy result grammar

| Result / state | Meaning | Expected consequence |
|---|---|---|
| `allow` | Request or release is policy-safe as scoped | Continue with named obligations |
| `deny` | Rights, sensitivity, actor, or release posture blocks the action | Explicit denial with stable reason |
| `generalize` | Exposure is allowed only after masking, aggregation, or geometry reduction | Visible transform state and receipt linkage |
| `restrict` | Surface is limited to a narrower actor or mode | Role-aware exposure; no quiet public fallback |
| `needs-review` / `STEWARD_REVIEW` | Machine gate cannot safely resolve the case alone | Route to steward review with reason and audit refs |
| `withdrawn` / `superseded` | Trust state changed after release | Preserve lineage and correction visibility |

### Runtime envelope outcomes

| Outcome | Meaning | Surface behavior |
|---|---|---|
| `ANSWER` | Support is sufficient and policy-safe | Return response with evidence and trust cues |
| `ABSTAIN` | Evidence is weak, partial, stale, conflicted, or unresolved | Narrow scope or decline with inspectable reason |
| `DENY` | Policy blocks the request | Calm refusal with accountable reason |
| `ERROR` | Technical failure prevented reliable governed handling | Explicit failure without pretending policy or evidence passed |

[Back to top](#policy)

## Gates and definition of done

- [ ] `doc_id` and `created` were replaced with repo-backed values.
- [ ] `policy/README.md` stays aligned with the **current branch**, not just public `main`.
- [ ] Claims about `policy/bundles/`, `policy/fixtures/`, `policy/tests/`, `policy/policy-runtime/`, `packages/policy/`, and `tests/policy/` match the checked-out tree exactly.
- [ ] New policy law changes pair with fixtures and bundle-local assertions.
- [ ] Broader runtime/release/correction behavior changes extend `tests/policy/` or the relevant end-to-end proof lane.
- [ ] No second authoritative contract or schema home grows inside `policy/`.
- [ ] Any runtime glue claims point to the verified package or app seam that actually owns them.
- [ ] Workflow claims stay bounded to what the branch proves in `.github/workflows/`.
- [ ] Runtime outcomes remain finite: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`.
- [ ] Correction and review remain visible and audit-bearing.
- [ ] Any mention of `OPA/Rego` stays explicitly documented as starter direction unless the branch proves checked-in adoption.

[Back to top](#policy)

## FAQ

### Does current public `main` prove that `policy/` is more than a single README?

Yes. Public `main` now confirms `policy/` plus child lanes for `bundles/`, `fixtures/`, `policy-runtime/`, and `tests/`, along with adjacent `packages/policy/` and `tests/policy/` documentation surfaces.

### Does current public `main` prove executable policy bundles or runnable suites?

No. The inspected child policy lanes are still README-only on public `main`, so checked-in rule packs, fixture payloads, and runnable assertions still need branch-level verification.

### Are `policy/tests/` and `tests/policy/` the same thing?

No. `policy/tests/` is the bundle-local verifier lane. `tests/policy/` is the broader repo-facing proof lane for policy behavior under runtime, release, and correction pressure.

### Is `packages/policy/` confirmed?

Yes, as a documented package boundary. That confirms a shared internal support seam exists publicly. It does **not** by itself prove populated package code.

### Does `.github/workflows/` prove checked-in merge-gate YAML on current public `main`?

No. Current public `main` documents `.github/workflows/` as `README.md` only. Treat workflow references here as proof burden, not as already-checked-in gate coverage.

### Is `OPA/Rego` confirmed as mounted adoption?

Not from the inspected public tree. It remains the strongest documented starter direction for policy-as-code, but this README should not present it as a checked-in fact unless the active branch proves it.

## Appendix

<details>
<summary><strong>Lowest-friction next executable fill (PROPOSED)</strong></summary>

| Current lane | First evidence-bearing addition | Why it is the smallest useful move |
|---|---|---|
| `policy/bundles/` | One seam-local bundle plus a versioned manifest | Converts the lane from descriptive to executable |
| `policy/fixtures/` | One positive and one negative case for the same seam | Makes deny-by-default behavior inspectable |
| `policy/tests/` | One seam-local assertion pack | Proves the bundle does what the README says |
| `tests/policy/` | One runtime-outcome or correction-parity pack | Proves bundle semantics survive broader verification pressure |
| `policy/policy-runtime/` | One coordination note pointing to the actual consuming package/app seam | Prevents “runtime” from staying abstract |
| `packages/policy/` | One shared internal adapter or loader boundary | Gives runtime consumers a real place to stay consistent without relocating policy authority |

### Starter families worth proving first

| Family | Why it is a good first wave |
|---|---|
| Admission | Makes source intake governable early |
| Rights | Prevents casual release drift |
| Sensitivity | Forces visible generalize/restrict behavior |
| Review / release | Makes promotion and hold states explicit |
| Runtime | Enforces finite outward outcomes |
| Correction | Keeps withdrawal and supersession visible instead of implicit |

### Practical reminder

Touch `../contracts/README.md` and `../schemas/README.md` whenever a policy change:
- introduces a new trust-bearing object family,
- changes who owns a shared vocabulary,
- or starts sounding like a second authoritative schema home.

</details>

[Back to top](#policy)
