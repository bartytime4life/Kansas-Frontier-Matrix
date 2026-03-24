<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<TODO: assign-uuid>
title: validators
type: standard
version: v1
status: draft
owners: @bartytime4life
created: <TODO: verify existing file creation date>
updated: <TODO: set on merge>
policy_label: <TODO: verify public|restricted|...>
related: [../../README.md, ../README.md, ../../.github/README.md, ../../.github/CODEOWNERS, ../../.github/workflows/README.md, ../../contracts/README.md, ../../schemas/README.md, ../../policy/README.md, ../../tests/README.md, ../../scripts/README.md]
tags: [kfm, tools, validators, verification, contracts]
notes: [owners are grounded from the current /tools/ CODEOWNERS mapping; current public main shows tools/validators/ as README-only; doc_id and dates still need verification before merge]
[/KFM_META_BLOCK_V2] -->

# validators

Lane contract and landing surface for deterministic, fail-closed validation helpers in Kansas Frontier Matrix.

> **Status:** experimental  
> **Owners:** `@bartytime4life`  
> **Path:** `tools/validators/README.md`  
> **Repo fit:** validator-family lane under [`../README.md`](../README.md) · root orientation in [`../../README.md`](../../README.md) · authority neighbors [`../../contracts/README.md`](../../contracts/README.md) and [`../../schemas/README.md`](../../schemas/README.md) · policy [`../../policy/README.md`](../../policy/README.md) · tests [`../../tests/README.md`](../../tests/README.md) · scripts [`../../scripts/README.md`](../../scripts/README.md) · workflow callers [`../../.github/workflows/README.md`](../../.github/workflows/README.md)  
> **Current public snapshot:** `tools/validators/` exists and currently exposes `README.md` only on public `main`  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![owners](https://img.shields.io/badge/owners-%40bartytime4life-blue) ![path](https://img.shields.io/badge/path-tools%2Fvalidators%2FREADME.md-4051b5) ![branch](https://img.shields.io/badge/branch-main-111111) ![tree](https://img.shields.io/badge/public%20snapshot-README--only-lightgrey) ![posture](https://img.shields.io/badge/posture-fail--closed-red)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current verified snapshot](#current-verified-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Validator behavior contract](#validator-behavior-contract) · [Diagram](#diagram) · [Operating tables](#operating-tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> `validators/` is the narrow `tools/` family for helpers whose main job is **check / report / fail** against trust-bearing artifacts. It is **not** the canonical home of schemas, policy bundles, runtime code, or workflow orchestration.

> [!NOTE]
> This README intentionally separates **current public-tree fact** from **PROPOSED landing shape**. The `validators/` family is visible in the repo tree, but this subtree itself is still README-only on public `main`.

## Scope

`tools/validators/` is where KFM should keep long-lived validation entrypoints that make contract-first doctrine executable without hiding trust logic in shell glue or workflow YAML.

In practical terms, this lane is for validators that:

- compile and check machine-readable contracts
- exercise valid and invalid fixtures
- verify release, catalog, provenance, or correction linkage
- enforce finite runtime outcome grammar
- emit stable, reviewable output for humans and CI

The strongest immediate fit for this family is **contract-first validation**. KFM doctrine repeatedly pushes toward explicit contract families, invalid-example coverage, finite runtime outcomes, and visible correction lineage before broader shell polish or domain expansion.

### What this README does

This file exists to do four jobs at once:

1. describe what `tools/validators/` means in the repo today
2. keep present-state claims honest
3. define the narrow boundary of the validator family
4. provide a clean landing contract for the first executable validator(s)

### Evidence labels used here

| Label | Meaning in this file |
| --- | --- |
| **CONFIRMED** | Directly supported by current public repo evidence or attached KFM doctrine |
| **INFERRED** | Strongly suggested by adjacent repo/docs, but not proven as current subtree implementation |
| **PROPOSED** | Recommended landing shape or operating rule consistent with doctrine |
| **UNKNOWN** | Not verified strongly enough to present as current repo fact |
| **NEEDS VERIFICATION** | Placeholder or unresolved detail that should be checked before merge |

[Back to top](#validators)

## Repo fit

**Path:** `tools/validators/README.md`  
**Role in repo:** directory README for executable validation helpers, not for canonical rule ownership.

| Direction | Surface | Why it matters |
| --- | --- | --- |
| Upstream | [`../README.md`](../README.md) | Parent `tools/` lane defines the broader helper boundary and family map |
| Upstream | [`../../README.md`](../../README.md) | Root repo README sets system identity and verification-first posture |
| Governance | [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) | Current owner coverage for `/tools/` lives here |
| Governance | [`../../.github/README.md`](../../.github/README.md) | Repo-wide review and gatehouse posture |
| Adjacent | [`../../contracts/README.md`](../../contracts/README.md) | Validators consume declared contract surfaces; they do not replace them |
| Adjacent | [`../../schemas/README.md`](../../schemas/README.md) | Current repo still exposes a schema lane; validators must not silently choose authority |
| Adjacent | [`../../policy/README.md`](../../policy/README.md) | Policy bundles, fixtures, and vocabularies remain policy-owned |
| Adjacent | [`../../tests/README.md`](../../tests/README.md) | Authoritative fixture and proof families belong here |
| Adjacent | [`../../scripts/README.md`](../../scripts/README.md) | Scripts orchestrate staged work and may call validators |
| Downstream | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | CI may invoke validators, but workflow YAML must not become the only implementation surface |

### Working interpretation

`validators/` is the first place a maintainer should look for reusable, fail-closed checks.

It is **not** where KFM should bury:

- schema law
- policy law
- fixture authority
- release promotion logic
- long-running service behavior

That separation matters because KFM’s trust posture depends on being able to tell the difference between:

- the thing that **defines** truth-bearing structure
- the thing that **checks** it
- the thing that **proves** it with fixtures
- the thing that **orchestrates** it through operator or CI flow

## Accepted inputs

The following belong in or under `tools/validators/`:

| Belongs here | Why it belongs here |
| --- | --- |
| Narrow validator entrypoints such as `validate_contracts.py` | Their main job is deterministic inspection and failure signaling |
| Pinned validator dependency files such as `requirements.txt` | Local and CI runs should resolve the same validator stack |
| Small validator-local config files | Useful when they shape checker behavior without becoming source-of-truth law |
| Validator-local smoke inputs or report examples | Helpful when they document output shape without replacing `tests/` as the authoritative fixture surface |
| Shared helper modules used only by validator entrypoints | Acceptable while the logic remains family-local and not broadly reusable |
| Machine-readable report schemas or documented output contracts | Reviewers and CI should not parse ad hoc prose logs |

### Family boundary map

| Surface | Belongs there when… | Does **not** belong there when… |
| --- | --- | --- |
| `tools/validators/` | the artifact’s primary job is validate / summarize / emit exit status | it defines authoritative schema or policy law |
| `../../tests/` | the artifact proves behavior with positive/negative fixtures or end-to-end drills | it is the primary operational CLI |
| `../../scripts/` | the artifact coordinates staged work and calls validators | it is a reusable validation helper |
| `../../contracts/` | the artifact defines object shape, required fields, or versioned schema law | it is executable validation logic |
| `../../schemas/` | the artifact documents or resolves schema-lane authority | it is a helper that quietly chooses the winner |
| `../../policy/` | the artifact is executable rule logic, fixture ownership, or vocabulary law | it is only a wrapper around policy evaluation |
| `../../.github/workflows/` | the artifact declares CI orchestration | it is the only place validator behavior exists |

## Exclusions

| Does **not** belong here | Better home | Why |
| --- | --- | --- |
| Canonical JSON Schemas, OpenAPI docs, standards profiles, or vocab registries | [`../../contracts/README.md`](../../contracts/README.md) and the repo’s declared authority surface | Validators consume law; they do not own it |
| Executable policy bundles, policy fixtures, reason/obligation registries, or decision grammar | [`../../policy/README.md`](../../policy/README.md) | KFM keeps governance visible and reviewable outside tool code |
| Full authoritative fixture libraries | [`../../tests/README.md`](../../tests/README.md) | Validators should read fixture truth, not quietly redefine it |
| Workflow-only shell blobs that become the validator implementation | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) **plus** stable tool entrypoints here | Reviewers must be able to inspect logic outside workflow YAML |
| Long-lived runtime service code | app or package surfaces | `validators/` is support tooling, not product runtime |
| One-off operator experiments | local scratch or a clearly disposable script | This lane should stay repeatable and reviewable |
| Secret-bearing config, restricted fixtures, or unrestricted precise-location dumps | secured data/config surfaces | Public validation tooling should remain safe to clone, review, and run |

## Current verified snapshot

| Item | Status | Validator consequence |
| --- | --- | --- |
| `tools/` is a real top-level repo lane | **CONFIRMED** | validator family has a stable repo home |
| Current public `tools/` directory lists `attest/`, `catalog/`, `ci/`, `diff/`, `docs/`, `probes/`, `validators/`, and `README.md` | **CONFIRMED** | validator family is already named in the live tree |
| `tools/validators/` currently lists `README.md` only | **CONFIRMED** | this subtree is still documentary, not executable |
| The current file content is a one-line scaffold | **CONFIRMED** | replacing it with a real family README is appropriate |
| Current CODEOWNERS coverage maps `/tools/` to `@bartytime4life`; no narrower validator-specific owner is directly confirmed here | **CONFIRMED** | owner line should stay conservative |
| `contracts/` and `schemas/` both exist, and schema-home authority is still explicitly unresolved | **CONFIRMED unresolved** | validators must not silently decide schema authority |
| `contracts/README.md` requires machine-validatable surfaces with at least one valid and one invalid example | **CONFIRMED** | first validator should support positive and negative fixture flow |
| `tests/README.md` already exposes `contracts/`, `policy/`, `e2e/correction/`, `e2e/release_assembly/`, and `e2e/runtime_proof/` families | **CONFIRMED** | validators should plug into existing proof surfaces instead of inventing private ones |
| `.github/workflows/` public `main` still exposes `README.md` only | **CONFIRMED** | do not imply a checked-in merge-blocking validator workflow already exists |

> [!WARNING]
> The current live tree and adjacent docs are slightly out of sync. The parent `tools/README.md` still contains earlier prose that treated the parent lane as README-only, but the current public directory listing now shows named family directories under `tools/`. For tree claims, treat the live directory listing as stronger current evidence and reconcile the parent README separately instead of copying stale wording into this subtree.

[Back to top](#validators)

## Directory tree

### Current confirmed snapshot

```text
tools/
├── README.md
├── attest/
├── catalog/
├── ci/
├── diff/
├── docs/
├── probes/
└── validators/
    └── README.md
```

### Near-term landing shape to prefer (PROPOSED)

Keep the first landed validator slice intentionally small.

```text
tools/validators/
├── README.md
├── validate_contracts.py
└── requirements.txt
```

### Why the near-term shape stays this small

The first landed validator should prove one high-value seam well:

- explicit schema compilation
- valid and invalid fixture handling
- stable machine-readable report output
- non-zero exit on blocking failure

Anything broader should wait until that first seam is real.

## Quickstart

Run the inventory-first loop before adding or moving anything here.

### 1) Confirm the subtree you actually have

```bash
tree -a -L 2 tools/validators 2>/dev/null \
  || find tools/validators -maxdepth 2 \( -type f -o -type d \) 2>/dev/null | sort

tree -a -L 2 tools 2>/dev/null \
  || find tools -maxdepth 2 \( -type f -o -type d \) 2>/dev/null | sort
```

### 2) Re-read adjacent authority surfaces before naming a validator

```bash
sed -n '1,240p' tools/README.md 2>/dev/null
sed -n '1,240p' contracts/README.md 2>/dev/null
sed -n '1,240p' schemas/README.md 2>/dev/null
sed -n '1,240p' policy/README.md 2>/dev/null
sed -n '1,260p' tests/README.md 2>/dev/null
sed -n '1,220p' .github/workflows/README.md 2>/dev/null
sed -n '1,200p' .github/CODEOWNERS 2>/dev/null
```

### 3) Search for caller surfaces and trust-bearing object names

```bash
rg -n \
  "validate_contracts|RuntimeResponseEnvelope|CorrectionNotice|DecisionEnvelope|reason_codes|obligation_codes|tools/validators" \
  . -S 2>/dev/null
```

### 4) If the first validator has landed, inspect the interface instead of guessing

```bash
if [ -f tools/validators/validate_contracts.py ]; then
  python3 tools/validators/validate_contracts.py --help
fi
```

## Usage

### Add the first validator

The strongest first move is a **contract-first** validator.

Use this family for the smallest reversible slice that can:

1. compile the first-wave contract set
2. run at least one valid and one invalid example per target surface
3. emit a stable report
4. fail non-zero on blocking conditions
5. stay runnable both locally and from CI

### Keep authority explicit

A validator in this lane should do **one** of the following when schema-home ambiguity still exists:

- accept an explicit `--contract-home` or equivalent input
- read a declared repo authority file
- fail loudly and tell the operator that schema authority must be resolved first

It should **not** silently infer authority from whichever directory happened to be present first.

### Keep fixtures authoritative elsewhere

`validators/` may ship tiny smoke examples or output examples, but the authoritative positive/negative proof packs should stay in `../../tests/`.

That keeps these roles clear:

- `validators/` = executable checker
- `tests/` = proof surface
- `contracts/` / `schemas/` = structure law
- `policy/` = governance law

### Keep orchestration outside the family

When a validator becomes useful in local workflows or CI:

- let [`../../scripts/README.md`](../../scripts/README.md) own operator choreography
- let [`../../.github/workflows/README.md`](../../.github/workflows/README.md) own workflow orchestration
- keep the reusable validation logic here

That split matters because reviewers should be able to inspect the validator directly without reverse-engineering a workflow file.

## Validator behavior contract

| Concern | Required posture |
| --- | --- |
| Determinism | Same inputs should yield the same exit class and report shape |
| Failure semantics | Blocking conditions return non-zero and stay visible |
| Output shape | Prefer JSON or JSONL when CI or review tooling consumes output |
| Side effects | Default to read-only inspection; writing should be limited to explicit report paths |
| Schema-home handling | Follow explicit authority or fail loud when authority is unresolved |
| Fixture handling | Support positive and negative proof paths; do not require only happy-path examples |
| Policy joinability | When policy-relevant objects are validated, carry enough IDs or codes to link back to policy and review surfaces |
| Provenance joinability | Reports should name checked paths, artifact refs, or digests clearly enough for review |
| Safety | Do not dump sensitive raw payloads into logs when summarized output is sufficient |
| Local/CI parity | The same entrypoint should be runnable by a maintainer and by CI |

### Blocking conditions that fit this lane

Blocking conditions will vary by validator, but the following are in-family and doctrine-aligned:

- a schema fails to compile
- a supposedly valid example fails validation
- a supposedly invalid example passes validation
- a runtime envelope admits an outcome outside `ANSWER | ABSTAIN | DENY | ERROR`
- an answer-shaped runtime envelope lacks required citation structure
- a correction drill fails visible supersession or withdrawal linkage
- a release/proof linkage check cannot reconstruct the expected chain

## Diagram

```mermaid
flowchart LR
    subgraph Current["Current public state"]
        T["tools/validators/README.md"]
    end

    subgraph Inputs["Governed inputs"]
        C["contracts/"]
        S["schemas/"]
        P["policy/"]
        TF["tests/fixtures + e2e"]
        SC["scripts/"]
        WF[".github/workflows/"]
    end

    subgraph Target["validators/ family job"]
        V["check / report / fail"]
    end

    C --> V
    S --> V
    P -->|"only as input, not source-of-truth"| V
    TF -->|"positive + negative proof"| V
    SC -->|"calls stable entrypoints"| V
    WF -->|"invokes, does not replace"| V

    V --> R["machine-readable report + exit code"]
    R --> RV["reviewers / maintainers"]
    R --> G["local block or merge gate"]

    T -. "lane contract today" .-> V
    G -. "never publish directly" .-> API["governed interfaces"]
```

## Operating tables

### Current repo signals that shape this README

| Signal | Why it matters for `validators/` |
| --- | --- |
| Parent `tools/` docs already frame validators as the strongest doctrinal fit among tool families | this subtree should lead with validation, not a generic utility bucket |
| `contracts/README.md` sets a minimum bar of machine-validatable surfaces plus valid and invalid examples | first validator should support both positive and negative examples from day one |
| `schemas/README.md` explicitly warns against growing a second authoritative schema registry | validators must not drift into schema-law ownership |
| `scripts/README.md` says reusable validator libraries should graduate out of shell glue | validator logic belongs here, not buried in scripts |
| `policy/README.md` keeps bundles, fixtures, tests, and vocabularies in policy surfaces | validators may evaluate policy-shaped objects, but policy remains policy-owned |
| `tests/README.md` exposes contract-, policy-, runtime-, release-, and correction-proof families | validator design should anticipate caller/proof surfaces that already exist conceptually |

### First-wave priority set for a contract-first validator

| Object family | Minimum expectation from the validator family |
| --- | --- |
| `SourceDescriptor` | compile and validate at least one valid and one invalid example |
| `DatasetVersion` | validate identity, version, and time/support-bearing structure |
| `DecisionEnvelope` | validate finite decision grammar, audit linkage, and policy-bearing fields |
| `ReleaseManifest` / `ReleaseProofPack` | validate release linkage and proof-bearing references |
| `EvidenceBundle` | validate minimum evidence-package structure |
| `RuntimeResponseEnvelope` | enforce finite runtime outcomes and cite-or-abstain structure |
| `CorrectionNotice` | enforce visible correction lineage rather than silent overwrite |

### Near-term landed artifacts to prefer

| Artifact | Job | Status |
| --- | --- | --- |
| `tools/validators/README.md` | family contract and landing guide | **CONFIRMED current file** |
| `tools/validators/validate_contracts.py` | first-wave contract + fixture gate | **PROPOSED next landed helper** |
| `tools/validators/requirements.txt` | deterministic validator dependency pinning | **PROPOSED next landed helper** |

[Back to top](#validators)

## Task list / Definition of done

Before merging work into this lane, confirm all applicable items below.

- [ ] The validator has one narrow, named purpose.
- [ ] Directory placement matches the validator’s real job.
- [ ] Inputs, outputs, and exit semantics are documented here.
- [ ] Schema-home authority is explicit, or ambiguity fails loudly.
- [ ] At least one representative passing case and one failing case exist.
- [ ] The validator is read-only by default.
- [ ] Machine-readable output exists when CI or review tooling needs stable parsing.
- [ ] No policy, schema, or vocabulary source-of-truth was smuggled into helper code.
- [ ] No sensitive raw fixture or secret-bearing config was committed here.
- [ ] Local execution and CI invocation can use the same stable entrypoint.
- [ ] Caller surfaces are documented in the nearest relevant README.
- [ ] If the validator changes merge posture, the workflow and the validator are reviewed together.
- [ ] If the validator touches correction or runtime-envelope logic, the negative-path proof surface is named explicitly.

## FAQ

### Why does `validators/` need its own README if the family is still README-only?

Because the subtree already exists in the live repo tree, and the family needs a boundary contract before executable helpers land. KFM loses trust when code arrives before placement and responsibility are explained.

### Why not just keep validator logic inside `scripts/`?

Because `scripts/` coordinates staged work. Reusable validation logic should remain directly inspectable as a stable helper surface, not buried in operator choreography.

### Should `validators/` own the fixture library?

No. Tiny smoke examples are fine here, but authoritative positive/negative proof packs should stay in `../../tests/`.

### Should validators decide whether `contracts/` or `schemas/` is authoritative?

No. They should follow an explicit repo authority decision or fail loud when that decision is missing.

### Can a validator promote, publish, or correct data on its own?

Normally no. This family is for inspection and failure signaling. Lifecycle state changes belong in governed workflows and operator-reviewed surfaces.

[Back to top](#validators)

## Appendix

<details>
<summary>Illustrative machine-readable report shape (PROPOSED)</summary>

```json
{
  "tool": "validate_contracts",
  "status": "fail",
  "blocking": true,
  "checked_at": "2026-03-24T00:00:00Z",
  "contract_home": "contracts/",
  "checks": [
    {
      "id": "schema-compile",
      "result": "pass"
    },
    {
      "id": "valid-fixture-pass",
      "result": "pass"
    },
    {
      "id": "invalid-fixture-fail",
      "result": "pass"
    },
    {
      "id": "runtime-envelope-outcome-enum",
      "result": "fail",
      "message": "unexpected outcome value outside finite allowed set"
    }
  ]
}
```

</details>

<details>
<summary>Minimal exit-code contract to prefer (PROPOSED)</summary>

| Exit code | Meaning |
| --- | --- |
| `0` | all blocking checks passed |
| `1` | one or more blocking checks failed |
| `2` | invocation or configuration error |
| `3` | authority ambiguity or missing required input prevented evaluation |

</details>

<details>
<summary>Illustrative first follow-on checks after <code>validate_contracts.py</code> lands (PROPOSED)</summary>

- correction drill linkage checks for `CorrectionNotice` and supersession flow
- release/proof linkage checks for `ReleaseManifest` / `ReleaseProofPack`
- runtime-envelope structural checks for `RuntimeResponseEnvelope`
- catalog-closure linkage checks once the contract home is explicit

These are **not** current public-tree claims. They are the next natural proof burdens once the first contract validator is real.

</details>
