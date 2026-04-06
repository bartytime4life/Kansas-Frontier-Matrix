<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION
title: Dependency Confusion Checks
type: standard
version: v1
status: review
owners: [@bartytime4life]
created: NEEDS VERIFICATION
updated: 2026-04-06
policy_label: public
related: [docs/security/supply-chain/dependency-confusion/README.md, docs/security/supply-chain/dependency-confusion/policy/README.md, docs/security/supply-chain/dependency-confusion/examples/README.md, .github/CODEOWNERS, .github/workflows/README.md]
tags: [kfm, security, supply-chain, dependency-confusion, checks]
notes: [doc_id placeholder pending repo UUID assignment, created date needs verification]
[/KFM_META_BLOCK_V2] -->

# Dependency Confusion Checks

Reviewer-facing check guidance for what to inspect, what evidence to capture, and where dependency-confusion enforcement should live under `docs/security/supply-chain/dependency-confusion/checks/`.

**Repo fit:** `docs/security/supply-chain/dependency-confusion/checks/README.md` → upstream [`../README.md`](../README.md) · adjacent [`../policy/README.md`](../policy/README.md), [`../examples/README.md`](../examples/README.md) · downstream future check pages in this directory.

> **Status:** experimental  
> **Owners:** `@bartytime4life` *(confirmed broad `/docs/` CODEOWNERS coverage; any narrower dependency-confusion-specific split remains `NEEDS VERIFICATION`)*  
> ![Status: experimental](https://img.shields.io/badge/status-experimental-orange)
> ![Owner: @bartytime4life](https://img.shields.io/badge/owner-%40bartytime4life-blue)
> ![Lane: dependency confusion](https://img.shields.io/badge/lane-dependency--confusion-critical)
> ![Tree: README only](https://img.shields.io/badge/tree-README--only-lightgrey)
> ![Visibility: public main](https://img.shields.io/badge/visibility-public__main-2ea44f)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current verified snapshot](#current-verified-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Minimum reviewer questions](#minimum-reviewer-questions) · [Usage](#usage) · [Diagram](#diagram) · [Check families](#check-families) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> This directory is the **checks lane** for dependency confusion. It explains **what to inspect**, **what evidence to capture**, and **where enforcement should live**. It does **not** by itself prove that a workflow, policy bundle, or runnable scanner is already active.

> [!WARNING]
> Current public `main` shows `README.md` as the only checked-in file inside `docs/security/supply-chain/dependency-confusion/checks/`. The sibling `examples/` and `policy/` lanes are visible and should be treated as confirmed anchors. Any deeper filenames listed below **inside `checks/`** remain **INFERRED / NEEDS VERIFICATION** until they are directly visible here.

---

## Scope

This README turns a scaffold into a usable control surface for dependency-confusion review.

In KFM terms, this directory should stay focused on **inspection logic** and **reviewer/operator guidance** for package-source precedence, namespace collision, lockfile drift, provenance gaps, registry anomalies, and related supply-chain trust failures. It should remain downstream of broader security doctrine and upstream of executable enforcement in CI, policy, scripts, tools, or tests.

### Truth posture used here

- **CONFIRMED** — present in the current visible tree or directly anchored by adjacent KFM documentation
- **INFERRED** — repo-aligned interpretation of how the local security-doc structure is meant to work
- **PROPOSED** — recommended documentation shape or future check-page split
- **UNKNOWN / NEEDS VERIFICATION** — not directly reverified from the current public tree

This file is a lane guide, not an enforcement receipt.

## Repo fit

| Field | Value |
| --- | --- |
| Path | `docs/security/supply-chain/dependency-confusion/checks/README.md` |
| Role | Directory README for reviewer-facing dependency-confusion checks |
| Immediate parent | [`../README.md`](../README.md) |
| Upstream context | [`../../README.md`](../../README.md) · [`../../../README.md`](../../../README.md) · [`../../../../../README.md`](../../../../../README.md) |
| Adjacent lanes | [`../policy/README.md`](../policy/README.md) · [`../examples/README.md`](../examples/README.md) |
| Confirmed sibling anchors | [`../examples/lockfile-drift-attack.md`](../examples/lockfile-drift-attack.md) · [`../examples/namespace-collision-basic.md`](../examples/namespace-collision-basic.md) · [`../policy/README.md`](../policy/README.md) |
| Ownership signal | [`../../../../../.github/CODEOWNERS`](../../../../../.github/CODEOWNERS) |
| Public workflow surface | [`../../../../../.github/workflows/README.md`](../../../../../.github/workflows/README.md) |
| Current public state | `checks/` is README-only on public `main`; do not describe checked-in enforcement here without separate proof |
| Downstream intent | Future deep-dive check pages in this directory, plus implementation hooks in `tests/`, `scripts/`, `tools/`, `.github/workflows/`, and policy/runtime surfaces when verified |

## Accepted inputs

This directory accepts material such as:

- check definitions for dependency-confusion failure modes
- reviewer guidance for package-source precedence and namespace ownership
- lockfile, resolver, and registry-host inspection rules
- provenance-hook guidance for digest, attestation, and source-origin checks
- anomaly-detection notes for suspicious registry, mirror, or package-resolution behavior
- local operator or contributor guidance for pre-PR inspection
- mapping from observed signals to **allow / review / deny / correct** outcomes

## Exclusions

This directory should **not** become a dumping ground for adjacent work.

Send the following elsewhere:

- **policy decisions, exception rules, and decision grammar** → [`../policy/README.md`](../policy/README.md)
- **attack narratives, demonstrations, and teaching examples** → [`../examples/README.md`](../examples/README.md)
- **runnable scanners, hooks, scripts, or harnesses** → repo execution surfaces such as `tests/`, `scripts/`, `tools/`, or `.github/workflows/`
- **broad signing / SBOM / release-integrity guidance not specific to dependency confusion** → higher-level supply-chain docs under [`../../README.md`](../../README.md)
- **claims of active enforcement** without visible repo evidence

## Current verified snapshot

| Surface | Current public-main evidence | Reading implication |
| --- | --- | --- |
| `checks/` local inventory | `README.md` only | Use this lane as reviewer guidance; do not claim mounted child check pages or scanners here |
| `examples/` sibling lane | `README.md`, `lockfile-drift-attack.md`, and `namespace-collision-basic.md` are visible | Examples are the confirmed teaching and scenario anchors for this lane |
| `policy/` sibling lane | `README.md` is visible | The policy lane exists as a checked-in docs surface, but local policy implementation still needs separate proof |
| Broad docs ownership | `.github/CODEOWNERS` routes `/docs/` to `@bartytime4life` | The owner line in this README can safely name current broad docs ownership, but not a narrower split |
| Public workflow surface | `.github/workflows/README.md` is visible and describes the directory as README-only on public `main` | Historical workflow names or Actions UI signals are not proof of checked-in merge-blocking YAML for this lane |
| Parent-lane forward references | [`../README.md`](../README.md) points toward future check leaves such as `provenance-hooks.md`, `registry-anomaly-detection.md`, and `local-scan-guidance.md` | Keep those seams visible, but mark them **INFERRED / NEEDS VERIFICATION** until they are directly present here |

## Directory tree

### Confirmed current public-main inventory

```text
docs/security/supply-chain/dependency-confusion/checks/
└── README.md
```

### Confirmed sibling anchors

```text
docs/security/supply-chain/dependency-confusion/
├── policy/
│   └── README.md
└── examples/
    ├── README.md
    ├── lockfile-drift-attack.md
    └── namespace-collision-basic.md
```

### Forward seams worth keeping visible

| Candidate doc | Intended role in this lane | Current status |
| --- | --- | --- |
| `provenance-hooks.md` | Explain where dependency-origin, digest, attestation, and release-proof checks should hook in | INFERRED / NEEDS VERIFICATION |
| `registry-anomaly-detection.md` | Describe suspicious package-source or registry-behavior signals and review flow | INFERRED / NEEDS VERIFICATION |
| `local-scan-guidance.md` | Give contributor/operator guidance for local pre-merge inspection | INFERRED / NEEDS VERIFICATION |

## Quickstart

1. Start from [`../README.md`](../README.md) to confirm the lane-level dependency-confusion purpose.
2. Decide whether your addition is a **check**, a **policy rule**, an **example**, or an **implementation surface**.
3. If it is a check, document:
   - the threat or failure mode
   - the observable signal
   - the evidence to capture
   - the enforcement surface
   - the expected outcome
4. If you claim a check is enforced, point to the implementation surface that proves it.
5. Keep broken assumptions visible. Do not write future enforcement as present-tense fact.

### Minimum change shape

```text
checks/
├── README.md
└── <future-check>.md
```

A new check page should be small, specific, and link outward to policy, examples, and implementation surfaces instead of duplicating them.

### Minimum evidence packet

| Signal type | Keep at least |
| --- | --- |
| Namespace / source-precedence issue | manifest intent, registry or mirror config, resolver output, expected source owner |
| Lockfile / resolver drift | before/after lockfile diff, integrity field changes, resolved registry URLs, package metadata |
| Provenance gap | digest record, attestation or release-proof reference, policy note, subject artifact identifier |
| Registry anomaly | hostname delta, allowlist comparison, anomaly threshold or reviewer rationale, affected package list |
| Correction / rollback case | affected release or artifact refs, correction note, rollback or rebuild pointer, retained evidence link |

## Minimum reviewer questions

Before adding or approving a dependency-confusion check, answer these questions explicitly:

1. What package source, namespace, or registry was **supposed** to answer the dependency request?
2. What source, namespace, or registry **actually** answered it?
3. What evidence proves that result: manifest intent, resolver config, lockfile diff, artifact digest, attestation, or release proof?
4. Where should the decision live after inspection: `checks/`, `policy/`, `examples/`, or executable enforcement?
5. What is the correct outcome for the signal: **allow**, **review**, **deny**, or **correct**?

## Usage

| Need | Start here | Then go to |
| --- | --- | --- |
| Clarify what belongs in the checks lane | this README | [`../README.md`](../README.md) |
| Explain how to interpret a suspicious dependency-resolution signal | this README | future deep-dive check doc in `checks/` |
| Document an attack pattern or teaching example | [`../examples/README.md`](../examples/README.md) | confirmed example doc |
| Explain why a finding should block, warn, or require review | [`../policy/README.md`](../policy/README.md) | policy deep-dive docs when verified |
| Add executable validation | repo execution surfaces | `tests/`, `scripts/`, `tools/`, `.github/workflows/` |

## Diagram

```mermaid
flowchart LR
    A["Dependency / registry / lockfile change"] --> B["Triage the change"]
    B --> C["Checks lane<br/>docs/security/.../checks/"]
    C --> D{"What signal is present?"}

    D --> E["Namespace collision<br/>or source-precedence risk"]
    D --> F["Lockfile / resolver drift"]
    D --> G["Provenance or digest gap"]
    D --> H["Registry anomaly"]

    E --> I["Policy lane<br/>../policy/README.md"]
    F --> I
    G --> I
    H --> I

    E --> J["Examples lane<br/>../examples/README.md"]
    F --> J
    G --> J
    H --> J

    I --> K["Outcome:<br/>allow · review · deny · correct"]
    K --> L["Capture evidence + link implementation surface"]
    L --> M["tests/ · scripts/ · tools/ · workflows<br/>when verified"]
```

## Check families

| Check family | Primary question | Typical evidence | Enforcement surface | Current documentation state |
| --- | --- | --- | --- | --- |
| Namespace / source precedence | Can an internal or expected package be replaced by a public or higher-precedence source? | package manager config, registry hostnames, namespace ownership, resolver output | policy, local review, CI | PARTIAL: confirmed sibling example in [`../examples/namespace-collision-basic.md`](../examples/namespace-collision-basic.md); deeper check doc not yet visible here |
| Lockfile / resolver drift | Did the resolved package source, tarball, or integrity value change without intentional review? | lockfile diff, integrity fields, registry URL changes, package metadata | tests, CI, local inspection | PARTIAL: confirmed sibling example in [`../examples/lockfile-drift-attack.md`](../examples/lockfile-drift-attack.md) |
| Provenance hooks | Are origin, digest, attestation, or release-proof checks wired before merge or publication? | digest records, attestations, proof packs, workflow evidence | CI, policy, release assembly | INFERRED / NEEDS VERIFICATION |
| Registry anomaly detection | Are typosquats, mirror drift, or resolver anomalies made visible before trust is granted? | allowlists, anomaly thresholds, registry logs, source deltas | local review, CI, policy | INFERRED / NEEDS VERIFICATION |
| Local scan guidance | What should a contributor or reviewer run locally before opening a PR or approving a dependency change? | dry-run installs, audit output, lockfile diff review, source-origin summaries | scripts, tools, docs | INFERRED / NEEDS VERIFICATION |
| Correction / rollback linkage | If a bad dependency enters scope, is the correction path visible forward through release state? | correction notice, release manifest, affected surfaces, follow-up evidence | release/correction workflows | INFERRED / NEEDS VERIFICATION |

## Task list / definition of done

A dependency-confusion check doc is ready to keep when all of these are true:

- [ ] The threat model is named plainly.
- [ ] The failing condition is observable.
- [ ] The evidence a reviewer must capture is explicit.
- [ ] The expected outcome is mapped to **allow / review / deny / correct**.
- [ ] The correct neighboring lane is linked (`policy`, `examples`, or implementation surfaces).
- [ ] Any claim of live enforcement is backed by visible repo evidence.
- [ ] The page distinguishes **confirmed current public tree state** from **inferred future structure**.
- [ ] Filenames referenced from this README match the visible local tree or are clearly marked **INFERRED / NEEDS VERIFICATION**.
- [ ] The write-up does not confuse documentation intent with current implementation state.
- [ ] The page stays specific to dependency confusion rather than drifting into generic supply-chain prose.

## FAQ

### Is this directory the enforcement engine?

No. This directory is for **check guidance**. Enforcement belongs in verified policy, CI, test, script, tool, or runtime surfaces.

### Why separate checks from policy?

Because they answer different questions:

- **checks** = what to inspect
- **policy** = how to interpret and decide
- **examples** = how the failure mode looks in practice

Keeping them separate reduces drift and makes review easier.

### Why are some filenames marked `INFERRED / NEEDS VERIFICATION`?

Because current public `main` shows this directory as README-only, while adjacent dependency-confusion documentation points toward a richer future split. This README keeps those likely seams visible without pretending the files already exist here.

### Why not claim CI enforcement here?

Because visible public-tree evidence matters. If the checked-in workflow surface is not present in the current tree, this README should not imply that merge-blocking enforcement is already mounted.

### Why not put package-manager-specific rules here?

Because this lane should stay focused on **inspection logic**. The exact decision grammar, allowed registries, exception handling, and merge/publish outcomes belong in the policy lane or in executable enforcement once those surfaces are verified.

### Where should runnable code or hooks live?

Not in this directory. Put runnable behavior in the repo’s executable surfaces and link to it from here once verified.

## Appendix

<details>
<summary><strong>Starter template for a future check page</strong></summary>

### `<check-name>.md`

**Goal**  
What this check is trying to prevent or reveal.

**Threat / failure mode**  
What goes wrong if the check is skipped or fails.

**Signals to inspect**  
The concrete conditions, fields, files, logs, or diffs a reviewer should inspect.

**Required inputs**  
Configs, lockfiles, registry settings, attestations, manifests, or examples needed to run the check.

**Current evidence state**  
Mark each linked surface as **CONFIRMED**, **INFERRED**, **PROPOSED**, or **NEEDS VERIFICATION**.

**Manual review flow**  
1. Inspect source-precedence inputs.  
2. Inspect resolution output.  
3. Compare against expected namespace / origin / integrity posture.  
4. Capture evidence.  
5. Escalate to policy if needed.

**Automation hook points**  
Where this check should eventually run: CI, pre-merge, local tooling, release assembly, or runtime audit.

**Evidence to retain**  
What should be attached to a PR, review note, proof pack, or correction record.

**Outcome mapping**  
- allow  
- review  
- deny  
- correct / rollback

**Related docs**  
- `../README.md`  
- `../policy/README.md`  
- `../examples/README.md`

</details>

[Back to top](#dependency-confusion-checks)
