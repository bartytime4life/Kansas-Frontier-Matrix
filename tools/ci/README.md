<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION_UUID
title: ci
type: standard
version: v1
status: draft
owners: @bartytime4life
created: NEEDS_VERIFICATION_DATE
updated: 2026-04-13
policy_label: public
related: [../README.md, ../../README.md, ../../.github/README.md, ../../.github/CODEOWNERS, ../../.github/workflows/README.md, ../../.github/actions/README.md, ../../scripts/README.md, ../../contracts/README.md, ../../schemas/README.md, ../../policy/README.md, ../../tests/README.md, ../../tools/validators/promotion_gate/README.md, ../../tools/attest/README.md]
tags: [kfm, tools, ci, summaries, annotations, reviewer-output, promotion]
notes: [Merged from the older tools/ci lane contract and the newer promotion-oriented thin-slice renderer work. README-like lane contract; hidden metadata uses placeholders where current public evidence does not confirm a stable document record.]
[/KFM_META_BLOCK_V2] -->

# ci

Reusable CI-facing helpers for reviewer-readable summaries, annotations, and compact gate output over already-governed artifacts.

> **Status:** experimental  
> **Owners:** `@bartytime4life` *(via current public `/tools/` coverage in [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS); no narrower `/tools/ci/` rule directly verified)*  
> **Path:** [`tools/ci/README.md`](./README.md)  
> **Repo fit:** child lane of [`../README.md`](../README.md); workflow orchestration boundary in [`../../.github/workflows/README.md`](../../.github/workflows/README.md); adjacent step-level reuse seam in [`../../.github/actions/README.md`](../../.github/actions/README.md); thin orchestration in [`../../scripts/README.md`](../../scripts/README.md); canonical law stays upstream in [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md), [`../../policy/README.md`](../../policy/README.md), and [`../../tests/README.md`](../../tests/README.md)  
> **Evidence posture:** doctrine-grounded · public-`main` repo-grounded for visible tree state · exact helper inventory, live callers, rulesets, and platform settings remain bounded  
> **Current public snapshot:** `tools/ci/` was historically **README-only** on the public tree; this README therefore defines the lane contract without pretending every renderer, caller, or workflow is already proven on all branches  
> **Badges:** [![status](https://img.shields.io/badge/status-experimental-orange)](./README.md) [![owner](https://img.shields.io/badge/owner-%40bartytime4life-blue)](../../.github/CODEOWNERS) [![lane](https://img.shields.io/badge/lane-tools%2Fci-6f42c1)](../README.md) [![branch](https://img.shields.io/badge/branch-main-111111)](../../README.md) [![posture](https://img.shields.io/badge/posture-read--only%20by%20default-0a7d5a)](./README.md) [![current%20public%20tree](https://img.shields.io/badge/current%20public%20tree-bounded-lightgrey)](./README.md)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Current verified snapshot](#current-verified-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Helper matrix](#helper-matrix) · [Definition of done](#definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> `tools/ci/` is the reusable helper boundary for **rendering** gate results, not the authority boundary for **deciding** them. Workflow orchestration belongs in [`../../.github/workflows/`](../../.github/workflows/) or [`../../scripts/`](../../scripts/). Canonical schema, policy, release, and truth-bearing logic remain upstream.

> [!TIP]
> **Current executable snapshot (thin slice)**  
> The current documented thin slice for this lane includes reviewer-facing renderers used by the Promotion Gate flow:
>
> **Reviewer / auditor summary helpers**
> - `tools/ci/render_promotion_summary.py`
> - `tools/ci/render_promotion_bundle_summary.py`
>
> **Primary downstream trust surfaces**
> - `decision.json`
> - `promotion-record.json`
> - `promotion-bundle.json`
>
> **Primary adjacent lanes**
> - `tools/validators/promotion_gate/`
> - `tools/attest/`
>
> These helpers are intended to render already-governed outputs into:
>
> - CI step summaries
> - reviewer-readable Markdown
> - compact auditor-facing bundle summaries
>
> They must not silently redefine policy, promotion law, or release truth.

> [!NOTE]
> On some public snapshots this directory may still appear README-led or inventory-light. That is intentional here: the lane contract is stronger than the currently surfaced helper inventory so later additions do not become a miscellaneous CI junk drawer.

> [!WARNING]
> Helpers in `tools/ci/` should be deterministic, read-only by default, and safe to print in logs. Never leak tokens, unpublished evidence, policy-review internals, or trust-bearing state changes through convenience output.

---

## Scope

`tools/ci/` is for small, reusable helpers that turn already-produced machine output into review-friendly CI surfaces.

Use this lane when the job is to:

- summarize validator, policy, docs, geospatial, or test output for a pull request or check run
- normalize noisy tool output into a compact, stable intermediate format
- emit annotations, markdown summaries, or compact gate digests
- attach evidence, proof-pack, receipt, or artifact links to reviewer-facing output
- render trust-object bundles into concise reviewer or auditor summaries

Do **not** use this lane when the job is to:

- define canonical policy or contract law
- mutate release state, promotion state, or authoritative data
- replace workflow orchestration with hidden shell logic
- smuggle business meaning into “just CI glue”

### Truth labels used here

| Label | Meaning in this file |
| --- | --- |
| **CONFIRMED** | Directly supported by the current public repo tree, checked-in public Markdown, or attached KFM doctrine |
| **INFERRED** | Conservative interpretation of adjacent repo evidence or repeated doctrine, but not proven as current checked-in helper reality |
| **PROPOSED** | Recommended landing shape or operating rule consistent with KFM doctrine |
| **UNKNOWN** | Not verified strongly enough to present as current repo fact |
| **NEEDS VERIFICATION** | Explicit placeholder that should be checked against the working branch or platform settings before merge |

[Back to top](#ci)

## Repo fit

| Direction | Surface | Why it matters |
| --- | --- | --- |
| Parent lane | [`../README.md`](../README.md) | Defines the overall `tools/` contract and family boundaries. |
| Root posture | [`../../README.md`](../../README.md) | Sets the repo-wide evidence-first, map-first, trust-visible identity. |
| Ownership | [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) | Current public owner coverage for `/tools/` flows through here. |
| Workflow boundary | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | Workflow YAML should stay thin and call stable helpers instead of embedding large scripts. |
| Step-level reuse seam | [`../../.github/actions/README.md`](../../.github/actions/README.md) | Repo-local actions are the step-wrapper surface; `tools/ci/` should not duplicate action metadata or orchestration. |
| Thin orchestration | [`../../scripts/README.md`](../../scripts/README.md) | Local/operator entrypoints may call `tools/ci` helpers, but reusable review rendering should not be buried in `scripts/`. |
| Upstream truth law | [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md), [`../../policy/README.md`](../../policy/README.md), [`../../tests/README.md`](../../tests/README.md) | Canonical machine-checkable rules, fixtures, and proof burdens live here, not in CI presentation helpers. |
| Neighbor lanes | [`../validators/README.md`](../validators/README.md), [`../diff/README.md`](../diff/README.md), [`../attest/README.md`](../attest/README.md), [`../docs/README.md`](../docs/README.md), [`../probes/README.md`](../probes/README.md), [`../catalog/README.md`](../catalog/README.md) | Adjacent reusable helpers may feed inputs into `tools/ci/` summaries. |
| Promotion consumer | [`../../tools/validators/promotion_gate/README.md`](../../tools/validators/promotion_gate/README.md) | Current thin-slice reviewer summaries are now clearest in the promotion flow. |
| Attestation consumer | [`../../tools/attest/README.md`](../../tools/attest/README.md) | Verification state may need reviewer-facing rendering in CI surfaces. |
| Downstream consumers | pull request reviews, check summaries, compact merge-gate output, release-review breadcrumbs | These are the human-facing or gate-facing surfaces this lane is meant to improve. |

---

## Inputs

### Accepted inputs

| Input class | Examples | Why it belongs here |
| --- | --- | --- |
| Structured check results | contract validation, policy evaluation, docs/accessibility checks, geospatial validation, unit/contract/policy/e2e results | `tools/ci/` is the right place to compact and present these for reviewers. |
| Receipts and manifests | candidate summaries, release manifests, proof-pack indexes, correction or rollback receipts | Reviewer-facing CI often needs links and short context around trust objects. |
| Diff context | changed files, affected packages, affected route families, doc surfaces touched | Helps render “what changed” without re-implementing git or policy logic. |
| Run metadata | branch, SHA, job name, run ID, artifact locations | Needed for traceability and stable review output. |
| Normalized intermediate artifacts | compact JSON or line-oriented status files created upstream | Prefer consuming declared, structured artifacts over scraping raw logs. |
| Promotion trust objects | `decision.json`, `promotion-record.json`, `promotion-bundle.json` | Current thin-slice renderers operate over these governed artifacts. |
| Verification state | sign/verify result refs, attestation verification booleans | Reviewer surfaces increasingly need trust visibility, not just pass/fail text. |

### Input rules

1. Prefer declared file inputs over implicit environment scraping.
2. Prefer structured formats over free-form log parsing.
3. Keep helper-specific contracts small and explicit.
4. Refuse undeclared or malformed inputs clearly and early.
5. Render what upstream lanes already decided; do not silently re-decide it here.

---

## Exclusions

| Does **not** belong here | Put it here instead | Why |
| --- | --- | --- |
| Workflow orchestration YAML | [`../../.github/workflows/`](../../.github/workflows/) | Workflow sequencing, permissions, and trigger logic should stay visible at the workflow boundary. |
| Repo-local composite action metadata or workflow-step wrappers | [`../../.github/actions/`](../../.github/actions/) | Step-wrapper contracts belong in the gatehouse action lane; `tools/ci/` should stay as reusable helper surface callable locally and from CI. |
| Large orchestration scripts, retries, or state transitions | [`../../scripts/`](../../scripts/) | `scripts/` is the better home for orchestration; `tools/ci/` should stay reusable and narrow. |
| Canonical JSON Schema and OpenAPI truth | [`../../contracts/`](../../contracts/) and [`../../schemas/`](../../schemas/) | CI helpers may report on contract law, but must not become its hidden home. |
| Machine-readable policy bundles or decision grammar | [`../../policy/`](../../policy/) | Deny-by-default logic belongs in policy assets and tests, not summary renderers. |
| Trust-bearing domain logic | packages, pipelines, or workers under the repo’s main implementation structure | Business meaning should not hide inside “utility” helpers. |
| Durable proof objects, releases, or authoritative outputs | the repo’s release / data / proof surfaces | CI summaries may link to proof objects; they should not silently become them. |
| Long-form runbooks and doctrine | [`../../docs/`](../../docs/) | Keep this lane focused on executable CI support rather than narrative documentation. |
| Signature generation or verification | [`../attest/README.md`](../attest/README.md) | `tools/ci/` may display verification state, but signing and verifying stay in `tools/attest/`. |
| Promotion decisions | [`../validators/README.md`](../validators/README.md) and `promotion_gate/` | `tools/ci/` renders decisions; it does not author them. |

---

## Current verified snapshot

| Evidence item | Status | CI-lane consequence |
| --- | --- | --- |
| `tools/ci/` currently exposed `README.md` only on older public snapshots | **CONFIRMED historical snapshot** | This lane contract must not imply landed helper binaries or scripts without branch verification. |
| Parent `tools/` exposes `attest/`, `catalog/`, `ci/`, `diff/`, `docs/`, `probes/`, `validators/`, and `README.md` | **CONFIRMED** | `ci/` is one of seven visible helper families, not an ad hoc directory. |
| Current public `/tools/` ownership flows through broad `/tools/` coverage in `CODEOWNERS` | **CONFIRMED** | Owner wording should stay conservative until a narrower `/tools/ci/` rule exists. |
| `.github/workflows/` may be README-only or otherwise bounded on some public snapshots | **CONFIRMED bounded workflow evidence** | Checked-in workflow caller inventory remains bounded unless directly re-verified. |
| Public Actions history exposes workflow names such as `verify-docs.yml`, `release-evidence.yml`, and `promote-and-reconcile.yml` | **CONFIRMED historical signal** / **NEEDS VERIFICATION** current | Useful reconstruction clue, not proof of current checked-in callers. |
| `.github/actions/` is visible and placeholder-heavy on current public surfaces | **CONFIRMED** | Step-level reuse exists as a neighboring lane, but direct `tools/ci` caller maturity is not yet proven. |
| Current public repo root visibly includes `scripts/`, `tests/`, `contracts/`, `schemas/`, `policy/`, `tools/`, and `pipelines/` | **CONFIRMED** | `tools/ci` helpers should expect upstream artifacts from several governed lanes, not just workflow YAML. |
| Promotion Gate documentation now names `render_promotion_summary.py` and `render_promotion_bundle_summary.py` as current thin-slice CI surfaces | **CONFIRMED via adjacent documentation** | This lane now has concrete renderer identities to document. |
| Exact helper inventory, live callers, artifact upload wiring, and platform-only settings are not derivable from the public tree alone | **UNKNOWN** | Keep platform claims out of this README unless re-verified against live settings. |

[Back to top](#ci)

## Directory tree

### Current public snapshot (**CONFIRMED historically bounded**)

```text
tools/
└── ci/
    └── README.md
```

That snapshot should be read literally: this README is a lane contract, not proof of a fully landed helper inventory.

### Current documented thin-slice shape

```text
tools/
└── ci/
    ├── README.md
    ├── render_promotion_summary.py
    └── render_promotion_bundle_summary.py
```

<details>
<summary>Possible stable growth shape (<strong>PROPOSED</strong>, not guaranteed current public tree)</summary>

```text
tools/
└── ci/
    ├── README.md
    ├── emit-pr-summary
    ├── emit-annotations
    ├── compact-gate-output
    ├── normalize-check-output
    ├── render_promotion_summary.py
    ├── render_promotion_bundle_summary.py
    └── templates/
```

Use the smallest useful set. Resist the temptation to turn `tools/ci/` into a second `scripts/` directory.

</details>

---

## Quickstart

Start with inventory, not invention.

```bash
# Inspect the current lane and the adjacent contracts that define it
ls -la tools/ci
sed -n '1,260p' tools/README.md
sed -n '1,260p' .github/workflows/README.md
sed -n '1,260p' .github/actions/README.md
sed -n '1,220p' .github/CODEOWNERS
sed -n '1,220p' scripts/README.md
sed -n '1,260p' tools/validators/promotion_gate/README.md
sed -n '1,260p' tools/attest/README.md

# Find existing references before adding a helper
git grep -n "tools/ci" -- . || true
git grep -n "annotation\|summary\|proof-pack\|contract\|policy\|geospatial\|GITHUB_STEP_SUMMARY\|promotion-bundle" -- .github scripts tests tools docs || true

# Inspect likely producers of CI-facing artifacts
find .github/actions tools scripts tests -maxdepth 3 -type f | sort
```

Before adding a helper, answer four questions:

1. What single review problem does it solve?
2. What declared inputs does it consume?
3. What exact outputs does it emit?
4. Why does this belong in `tools/ci/` instead of `scripts/`, `.github/actions/`, `policy/`, `contracts/`, or a package?

### Exercise the current promotion summary renderers

```bash
python tools/ci/render_promotion_summary.py \
  decision.json \
  --output promotion-summary.md

python tools/ci/render_promotion_bundle_summary.py \
  promotion-bundle.json \
  --output promotion-bundle-summary.md
```

---

## Usage

### Recommended operating model

A good `tools/ci/` helper follows this shape:

1. **Receive** declared artifacts and run metadata.
2. **Normalize** them into a compact internal status model.
3. **Render** human-facing and machine-facing outputs separately.
4. **Exit** with helper-status semantics, not hidden policy semantics.

### Choose the right boundary

| Surface | Primary job | Good fit | Do **not** hide here |
| --- | --- | --- | --- |
| `.github/workflows/` | job ordering, triggers, permissions, required gates | orchestration, sequencing, blocking review flow | reusable helper internals |
| `.github/actions/` | repeated workflow steps with stable inputs/outputs | thin step wrappers | whole reviewer-summary families |
| `../../scripts/` | local/operator entrypoints and staged orchestration | sequencing, convenience wrappers, operator-safe entrypoints | canonical decisions or buried reusable renderers |
| `tools/ci/` | reviewer-readable summaries, annotations, compact digests | rendering already-produced artifacts for humans and CI | policy law, schema law, release authority |

### Practical rules

- One helper, one responsibility.
- Render results; do not invent authority.
- Stay read-only by default.
- Emit concise logs and stable outputs.
- Keep platform-specific behavior shallow and explicit.
- Make local invocation and CI invocation as close as possible.

### Recommended exit-code rule

Use non-zero exit codes when the helper itself is broken or its declared input contract is violated.

Do **not** hide gate meaning inside an opaque crash. If a check found failures, the helper should still be able to render that result cleanly and let the caller decide how to enforce it.

### Illustrative invocation patterns

```bash
# Illustrative future entrypoint — not a claim that this helper exists today
tools/ci/emit-pr-summary \
  --input build/reports/contracts.json \
  --input build/reports/policy.json \
  --input build/reports/geospatial.json \
  --sha "$GITHUB_SHA" \
  --run-id "$GITHUB_RUN_ID" \
  --out build/ci/pr-summary.md
```

```bash
# Current thin-slice promotion-oriented renderer
python tools/ci/render_promotion_summary.py \
  decision.json \
  --output promotion-summary.md
```

```bash
# Current thin-slice bundle-oriented renderer
python tools/ci/render_promotion_bundle_summary.py \
  promotion-bundle.json \
  --output promotion-bundle-summary.md
```

---

## Diagram

```mermaid
flowchart LR
    WF[".github/workflows/*<br/>or equivalent CI caller"]
    AC[".github/actions/*<br/>thin repeated steps"]
    SC["scripts/*<br/>thin orchestration only"]

    VA["tools/validators/*"]
    DF["tools/diff/*"]
    CA["tools/catalog/*"]
    AT["tools/attest/*"]
    TS["tests/*"]
    PO["policy/*"]
    CO["contracts/* / schemas/*"]
    PI["pipelines/*<br/>or build reports"]

    IN1["declared reports / manifests / receipts / trust objects"]
    CI["tools/ci/*<br/>summary + annotation helpers"]
    OUT1["PR summary<br/>check-run text<br/>compact gate digest"]
    OUT2["annotations<br/>review breadcrumbs<br/>bundle summaries"]
    NO["authoritative truth / promotion / policy law"]

    WF --> AC
    WF --> CI
    AC --> CI
    SC --> CI

    VA --> IN1
    DF --> IN1
    CA --> IN1
    AT --> IN1
    TS --> IN1
    PO --> IN1
    CO --> IN1
    PI --> IN1

    IN1 --> CI
    CI --> OUT1
    CI --> OUT2

    CI -. must not own .-> NO
```

[Back to top](#ci)

## Helper matrix

| Helper family | Primary job | Typical inputs | Typical outputs | Status |
| --- | --- | --- | --- | --- |
| Summary helpers | Produce reviewer-readable run summaries | structured validator / test / policy / docs outputs | Markdown or plain-text summaries | **CONFIRMED fit / thin-slice active for promotion** |
| Annotation helpers | Surface file- or line-scoped problems | structured failures with file context | platform-specific annotations | **PROPOSED** |
| Gate-compaction helpers | Collapse many checks into one small digest | multiple report files | compact JSON or terse status blocks | **PROPOSED** |
| Linkage helpers | Attach receipts, proof-pack, or artifact links to CI output | manifests, receipts, artifact indexes | link bundles for review surfaces | **PROPOSED** |
| Normalizers | Convert tool-specific output into a stable CI-facing shape | raw tool output | normalized intermediate artifacts | **PROPOSED** |
| Bundle renderers | Render full governed trust bundles for reviewer/auditor handoff | promotion bundle manifests, verification state | one-page Markdown summaries | **Thin-slice active for promotion** |

> [!TIP]
> The lane itself is real. The helper families above are intentionally distinguished between current thin-slice use and broader proposed growth so the README stays useful without overstating current branch contents.

---

## Definition of done

Use this checklist when adding or revising a `tools/ci/` helper.

- [ ] The helper has one clear job and one obvious caller.
- [ ] Its declared inputs are documented in this README or in a colocated help surface.
- [ ] Its outputs are deterministic and easy for both humans and CI to consume.
- [ ] It does **not** hide canonical policy, schema, release, or domain law.
- [ ] It is read-only by default.
- [ ] It does not leak secrets or unpublished evidence into logs.
- [ ] It can be run locally with the same contract used in CI.
- [ ] If a workflow or repo-local action calls it, that caller remains a thin wrapper rather than the only place helper behavior exists.
- [ ] Its tests and fixtures live in the repo’s shared test surfaces, not in ad hoc scratch files.
- [ ] It links back to real artifacts, receipts, manifests, or reports where useful.
- [ ] Failure semantics are explicit: helper failure is different from gate failure.
- [ ] If it renders trust state, that state comes from upstream artifacts rather than being recomputed opaquely inside the renderer.

---

## FAQ

### Why is this not `.github/workflows/`?

Because workflow YAML is orchestration. `tools/ci/` is for reusable helpers that workflows call. Keeping that boundary visible makes review easier and reduces hidden logic in workflow files.

### Why is this not `.github/actions/`?

Because repo-local actions are the thin step-wrapper seam inside the `.github` gatehouse. `tools/ci/` helpers should remain runnable outside GitHub Actions and should not require `action.yml` metadata just to render a summary or emit annotations.

### Why is this not `scripts/`?

Because `scripts/` is the more natural home for orchestration, sequencing, and operator-facing entrypoints. `tools/ci/` should stay small, reusable, and CI-facing.

### Does this README claim helpers already exist?

It claims the lane contract is real and that the promotion thin slice currently depends on reviewer-facing summary renderers. Exact mounted inventory still requires branch verification where public evidence is bounded.

### Can a `tools/ci/` helper publish, promote, or correct artifacts?

It should not own those trust-bearing actions. It may summarize evidence about them, but the authoritative action belongs in governed policy, review, release, and runtime lanes.

### Where should tests and fixtures live?

Prefer the repo’s shared test surfaces so helper behavior stays reviewable beside broader contract, policy, and regression evidence.

### Can `tools/ci/` render attestation verification state?

Yes — that is a good fit. But the signing and verification themselves belong in `tools/attest/`; `tools/ci/` should only render the already-produced state.

[Back to top](#ci)

## Appendix

<details>
<summary>Illustrative output shapes (<strong>PROPOSED</strong>)</summary>

### Example markdown summary

```md
## Contract and policy gate

- Contracts checked: 12
- Policy bundles evaluated: 4
- Failures: 1
- Review links:
  - proof-pack: `build/proof/proof-pack.json`
  - policy log: `build/policy/decision-log.json`

### Blocking items
- `contracts/runtime/runtime_response_envelope.schema.json` failed validation
```

### Example compact gate JSON

```json
{
  "kind": "ci_gate_summary",
  "schema_version": "0.1.0",
  "sha": "abc123",
  "run_id": "123456789",
  "status": "fail",
  "checks": {
    "contracts": "fail",
    "policy": "pass",
    "docs": "pass",
    "tests": "pass"
  },
  "artifacts": {
    "proof_pack": "build/proof/proof-pack.json",
    "summary_md": "build/ci/pr-summary.md"
  }
}
```

### Example annotation record

```json
{
  "path": "contracts/runtime/runtime_response_envelope.schema.json",
  "level": "error",
  "message": "Required property 'kind' missing in invalid fixture expectation block."
}
```

Keep these shapes small, boring, and stable. Reviewer trust is helped more by consistency than by cleverness.

</details>

<details>
<summary>Illustrative promotion summary role (<strong>thin-slice aligned</strong>)</summary>

A promotion-oriented CI renderer may take a machine-readable decision or bundle and emit:

- candidate identity
- finite decision outcome
- gate or bundle health table
- attestation verification visibility
- compact artifact index
- one short reviewer / auditor conclusion block

That is a rendering concern, not a decision-authority concern.

</details>

[Back to top](#ci)
