<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS_VERIFICATION_UUID>
title: React2Shell advisory
type: standard
version: v1
status: draft
owners: @bartytime4life
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public
related: [docs/security/README.md, docs/security/react2shell/README.md, docs/security/vulnerability-management.md, SECURITY.md, .github/dependabot.yml]
tags: [kfm, security, advisory, react2shell, react, rsc]
notes: [doc_id placeholder pending authoritative UUID assignment, dates pending commit metadata, public repo evidence does not yet prove current KFM package inventory or deployed exposure]
[/KFM_META_BLOCK_V2] -->

# React2Shell advisory

_Evidence-first KFM advisory leaf for React Server Components / React2Shell exposure, containment, verification, and correction-aware remediation._

> **Status:** experimental  
> **Owners:** `@bartytime4life` *(confirmed docs owner for `/docs/`; finer-grained security-owner split still needs verification)*  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![owner](https://img.shields.io/badge/owner-%40bartytime4life-blue) ![surface](https://img.shields.io/badge/surface-react2shell--advisory-c62828) ![scope](https://img.shields.io/badge/scope-rsc%20security%20advisory-critical) ![repo](https://img.shields.io/badge/repo-public%20main%20visible-brightgreen) ![truth](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20INFERRED%20%7C%20PROPOSED%20%7C%20UNKNOWN-lightgrey)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current verified snapshot](#current-verified-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list--gates--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)  
> **Repo fit:** `docs/security/react2shell-advisory/README.md` · upstream [`../README.md`](../README.md) · upstream [`../../README.md`](../../README.md) · adjacent [`../vulnerability-management.md`](../vulnerability-management.md) · sibling [`../react2shell/README.md`](../react2shell/README.md) · coupled [`../../../SECURITY.md`](../../../SECURITY.md), [`../../../.github/dependabot.yml`](../../../.github/dependabot.yml), [`../../../policy/README.md`](../../../policy/README.md), [`../../../contracts/README.md`](../../../contracts/README.md), [`../../../schemas/README.md`](../../../schemas/README.md), [`../../../tests/README.md`](../../../tests/README.md)

> [!WARNING]
> **CONFIRMED:** this path exists on public `main`, and the current checked-in file is scaffold-only.  
> **UNKNOWN:** whether Kansas Frontier Matrix currently ships a vulnerable React / Next.js / React Server Components runtime.  
> Do not close this advisory as “not affected” until mounted manifests, lockfiles, and deployed release evidence are inspected.

> [!CAUTION]
> Do **not** stop at the first December 2025 React2Shell patch floor. React issued follow-on React Server Components advisories after the initial RCE disclosure. This leaf therefore tracks the advisory family, not just the first emergency patch.

| At a glance | Working rule |
|---|---|
| Advisory purpose | Turn upstream React2Shell signal into a KFM-safe triage, containment, validation, and correction path |
| Truth posture | Keep `CONFIRMED`, `INFERRED`, `PROPOSED`, `UNKNOWN`, and `NEEDS VERIFICATION` explicit |
| Local exposure claim | Stay **UNKNOWN** until mounted package and deployment evidence exist |
| Closure rule | A patch alone is not closure; docs, policy, contracts, tests, and visible correction state must line up |

## Scope

This file owns the **issue-specific advisory lane** for React2Shell as it matters to Kansas Frontier Matrix.

It should answer questions like these:

1. What is the upstream advisory family, in its current usable form?
2. Which repo and release surfaces must be checked before KFM claims “affected” or “not affected”?
3. Which proof-bearing artifacts should move with containment or remediation?
4. When does this issue require visible correction, advisory linkage, or rollback rather than a silent dependency bump?

This file should stay focused on the **React2Shell / React Server Components advisory path**. Broader cross-cutting vulnerability lifecycle guidance belongs in [`../vulnerability-management.md`](../vulnerability-management.md).

## Repo fit

| Item | Value |
|---|---|
| **Path** | `docs/security/react2shell-advisory/README.md` |
| **Role in repo** | Narrow advisory leaf for the React2Shell / React Server Components security family |
| **Upstream** | [`../README.md`](../README.md), [`../../README.md`](../../README.md), [`../vulnerability-management.md`](../vulnerability-management.md) |
| **Adjacent** | [`../react2shell/README.md`](../react2shell/README.md) |
| **Operationally coupled surfaces** | [`../../../SECURITY.md`](../../../SECURITY.md), [`../../../.github/dependabot.yml`](../../../.github/dependabot.yml), [`../../../policy/README.md`](../../../policy/README.md), [`../../../contracts/README.md`](../../../contracts/README.md), [`../../../schemas/README.md`](../../../schemas/README.md), [`../../../tests/README.md`](../../../tests/README.md) |
| **Typical reader** | maintainer, reviewer, incident responder, release steward |
| **What this file should do** | summarize advisory state, define KFM triage posture, point to coupled proof surfaces, and prevent “safe by assumption” closure |
| **What this file must not do** | store secrets, embed exploit payloads, duplicate canonical architecture manuals, or imply mounted runtime/package reality without direct evidence |

Working relationship with the sibling lane:

- Use [`../react2shell/README.md`](../react2shell/README.md) for **family-level** or package-family orientation once that sibling grows beyond scaffold status.
- Keep this file **issue-specific**: current advisory state, KFM verification burden, containment path, and closure conditions.
- If the sibling lane remains scaffold-only, prefer one authoritative issue leaf over two thin, drifting documents.

## Accepted inputs

Content that belongs here:

- official React and framework/bundler advisories relevant to React2Shell
- mounted package inventories, lockfile evidence, and version-diff notes
- deployed release evidence that proves whether a public or steward-facing runtime was exposed
- KFM containment decisions, rollback notes, and correction/advisory linkage
- safe detection guidance, triage commands, and reviewer/operator checklists
- proof-bearing deltas that must move with remediation: docs, policy, contracts, tests, runbooks, release evidence

Framework- or bundler-specific detail only belongs here when package or runtime evidence proves it is relevant to KFM. That includes, for example, `next`, `react-router`, `waku`, `@parcel/rsc`, `@vite/rsc-plugin`, or `rwsdk`.

## Exclusions

| Keep out of this file | Where it goes instead | Why |
|---|---|---|
| Secrets, tokens, keys, live credentials | deployment environment or secret boundary | docs must never become a secret surface |
| Raw incident artifacts or restricted evidence | governed evidence stores and steward-only review lanes | this leaf should guide response without widening exposure |
| Exploit payloads, weaponized proof-of-concepts, or replayable attack strings | restricted security review material | this file is for triage and governance, not exploit distribution |
| General vulnerability lifecycle doctrine | [`../vulnerability-management.md`](../vulnerability-management.md) | keep this leaf issue-specific |
| Broad security architecture copied verbatim | [`../README.md`](../README.md), [`../../../SECURITY.md`](../../../SECURITY.md) | avoid duplicated doctrine surfaces |
| Executable policy expressed only as prose | [`../../../policy/README.md`](../../../policy/README.md) plus verified policy bundles/tests | reviewer guidance belongs here; enforcement does not |
| Contract bodies or schema authorities | [`../../../contracts/README.md`](../../../contracts/README.md), [`../../../schemas/README.md`](../../../schemas/README.md) | do not create a second contract home |
| Repo/runtime claims not directly evidenced | leave as `UNKNOWN` / `NEEDS VERIFICATION` | KFM requires visible uncertainty |

## Current verified snapshot

| Signal | Label | What it means now |
|---|---|---|
| `docs/security/react2shell-advisory/README.md` exists on public `main` | **CONFIRMED** | this is the right path for a repo-native advisory leaf |
| Current file content was scaffold-only | **CONFIRMED** | expansion is needed before this lane becomes useful |
| `docs/security/react2shell/README.md` also exists and is scaffold-only | **CONFIRMED** | sibling/family lane is not yet carrying substantive package-family guidance |
| `docs/security/README.md` routes readers to both `react2shell` and `react2shell-advisory` | **CONFIRMED** | the broader security subtree already expects both lanes |
| `/docs/` owner is `@bartytime4life` | **CONFIRMED** | direct docs ownership is visible; narrower security reviewer split still needs verification |
| `.github/dependabot.yml` documents npm monitoring for `/`, `/apps/*`, and `/packages/*` | **CONFIRMED** | package-update coverage is documented at repo level |
| `apps/explorer-web/`, `apps/governed-api/`, and `apps/review-console/` exist as README-level boundaries | **CONFIRMED** | likely runtime inspection starts there, but that is not proof of package inventory |
| Mounted `package.json` / lockfile inventory for KFM | **UNKNOWN / NEEDS VERIFICATION** | the public docs do not prove exact dependency state |
| Deployed RSC / App Router / Server Function exposure in current KFM releases | **UNKNOWN / NEEDS VERIFICATION** | no mounted runtime or release evidence is established here |
| Automated remediation / merge-blocking closure for this advisory family | **UNKNOWN / NEEDS VERIFICATION** | documentary surfaces exist, but active gate behavior must be rechecked |

## Directory tree

```text
docs/security/react2shell-advisory/
└── README.md
```

Adjacent currently relevant surfaces:

```text
docs/security/
├── README.md
├── vulnerability-management.md
├── react2shell/
│   └── README.md
└── react2shell-advisory/
    └── README.md
```

Potentially coupled proof surfaces outside this lane:

```text
.github/dependabot.yml
SECURITY.md
policy/README.md
contracts/README.md
schemas/README.md
tests/README.md
```

## Quickstart

These commands are intentionally **verification-first** and **read-only** until you decide to patch.

```bash
# 1) Inventory manifests and lockfiles
find . \
  \( -name package.json -o -name package-lock.json -o -name pnpm-lock.yaml -o -name yarn.lock -o -name bun.lockb \) \
  2>/dev/null | sort

# 2) Search for React2Shell-relevant packages and likely downstream frameworks
grep -RInE '"(next|react|react-dom|react-server-dom-webpack|react-server-dom-parcel|react-server-dom-turbopack|react-router|waku|@parcel/rsc|@vite/rsc-plugin|rwsdk)"' \
  . 2>/dev/null

# 3) Search for likely RSC / Server Function indicators
grep -RInE "'use server'|\"use server\"|next-action|rsc-action-id|server actions|server functions" \
  apps packages web src . 2>/dev/null

# 4) Confirm which trust-bearing proof surfaces must move with a fix
find docs/security policy contracts schemas tests .github \
  -maxdepth 5 -type f 2>/dev/null | sort | head -n 250
```

Minimal triage order:

1. **Prove whether any mounted dependency tree includes an affected RSC package or a downstream framework that can expose the vulnerable protocol.**
2. **Classify public/steward/internal blast radius before polishing remediation notes.**
3. **Contain first if exposure is plausible.** Prefer a safe visible state over an optimistic uncertain one.
4. **Upgrade to the current vendor-advised floor for the affected line.**
5. **Move proof surfaces together**: docs, policy, contracts, schemas, tests, and release/correction evidence.

## Usage

| When you need to… | Start here | Then verify or continue with… |
|---|---|---|
| Determine whether KFM is currently affected | this file | mounted manifests, lockfiles, deployment evidence, and release history |
| Record the advisory and containment path | this file | correction/release evidence surfaces once verified |
| Handle the cross-cutting lifecycle of remediation | [`../vulnerability-management.md`](../vulnerability-management.md) | coupled proof and release surfaces |
| Understand subtree-wide security doctrine | [`../README.md`](../README.md), [`../../../SECURITY.md`](../../../SECURITY.md) | canonical KFM manuals if needed |
| Update policy / contract / test consequences of a fix | this file for coupling rules | [`../../../policy/README.md`](../../../policy/README.md), [`../../../contracts/README.md`](../../../contracts/README.md), [`../../../schemas/README.md`](../../../schemas/README.md), [`../../../tests/README.md`](../../../tests/README.md) |
| Track a broader React2Shell family lane later | [`../react2shell/README.md`](../react2shell/README.md) | keep this leaf focused on the advisory itself |

Working rule: **do not let this leaf become a detached incident diary**. It should remain a precise advisory surface that helps reviewers and maintainers decide, prove, and close correctly.

## Diagram

```mermaid
flowchart TD
    A[Upstream advisory signal<br/>React / framework / bundler] --> B[Inventory mounted manifests<br/>lockfiles and deployed releases]
    B --> C{RSC-capable runtime proven?}

    C -->|No proof yet| D[State = UNKNOWN / NEEDS VERIFICATION<br/>keep advisory open]
    C -->|Yes| E{Affected package or downstream line present?}

    E -->|Yes| F[Contain / fail closed<br/>pause promotion, narrow exposure, or rollback]
    F --> G[Patch / upgrade to current vendor floor]
    G --> H[Validate]
    H --> I[Update coupled proof surfaces<br/>docs + policy + contracts + schemas + tests + release evidence]
    I --> J[Correction / disclosure / closure]

    E -->|No| K[Record unaffected claim<br/>with mounted evidence]
    K --> J
```

## Tables

### Upstream advisory snapshot

| Advisory family | CONFIRMED upstream state | KFM working rule |
|---|---|---|
| **React2Shell / RCE** | The original React Server Components issue is an unauthenticated RCE advisory affecting `react-server-dom-webpack`, `react-server-dom-parcel`, and `react-server-dom-turbopack`. | Treat any proven use of these packages as high-priority until the current safe floor is verified. |
| **Current React package floor** | Later follow-on React Server Components advisories mean the safe backport floor for the affected `react-server-dom-*` packages is `19.0.4`, `19.1.5`, and `19.2.4`. | Do **not** close on the initial emergency patch floor alone. |
| **Not-affected precondition** | Apps without a server, or without a framework/bundler/plugin that supports React Server Components, are not affected. | Use this close path only when mounted repo and deployed runtime evidence actually prove it. |
| **Next.js downstream** | Official Next.js advisories track downstream impact for App Router. Pages Router is not affected. | Verify router mode and release line before choosing remediation. Prefer current vendor guidance or vendor tooling over freezing a stale version list in this leaf. |
| **Upgrade helper** | Next.js publishes `npx fix-react2shell-next` for deterministic version bumps by release line. | Use only after mounted inventory proves KFM is actually in the affected Next.js family. |

### KFM exposure decision matrix

| Condition | Label to use here | Immediate next action |
|---|---|---|
| No mounted JS/TS manifests or lockfiles reviewed yet | **UNKNOWN** | keep advisory open; inventory first |
| Framework or bundler is present, but RSC capability and deployed release are unresolved | **NEEDS VERIFICATION** | prove App Router / RSC / Server Function usage before closing |
| Affected `react-server-dom-*` package is present below the current safe floor | **CONFIRMED (affected package state)** | contain, patch, validate, and record correction path |
| Next.js App Router is proven on an affected release line | **CONFIRMED (affected runtime class)** | follow vendor patch guidance for that line and preserve correction lineage |
| React/browser UI exists, but mounted proof shows no server and no RSC-capable framework/bundler/plugin | **CONFIRMED (non-affected upstream precondition)** + **PROPOSED local close path** | record the evidence, keep the advisory linked, and close only with mounted proof |
| Historically public and unpatched exposure is suspected | **NEEDS VERIFICATION** | reconstruct release window, decide on secret rotation and visible correction/advisory handling |
| Public tree alone “looks thin,” so impact is assumed impossible | **INVALID CLOSE PATH** | do not use scaffold depth as a security proof |

### Repo-coupled surfaces that should move with remediation

| Surface | Why it should move with this advisory |
|---|---|
| [`../vulnerability-management.md`](../vulnerability-management.md) | cross-cutting lifecycle and closure expectations |
| [`../README.md`](../README.md) | subtree doctrine and lane routing |
| [`../../../SECURITY.md`](../../../SECURITY.md) | repo-level public security posture if behavior changes materially |
| [`../../../policy/README.md`](../../../policy/README.md) | deny-by-default, reasons/obligations, and runtime trust outcomes |
| [`../../../contracts/README.md`](../../../contracts/README.md) | trust-bearing object vocabulary if remediation changes outward or review-facing behavior |
| [`../../../schemas/README.md`](../../../schemas/README.md) | avoid drifting schema authority if object shapes or examples change |
| [`../../../tests/README.md`](../../../tests/README.md) | negative-path and proof expectations should keep pace with remediation |
| [`../../../.github/dependabot.yml`](../../../.github/dependabot.yml) | package monitoring coverage is part of the advisory operating context |
| release / correction evidence | correction-visible closure depends on release lineage, not only code change |

[Back to top](#react2shell-advisory)

## Task list / gates / definition of done

- [ ] mounted package inventory captured
- [ ] affected package or framework decision recorded with evidence
- [ ] public, steward, and internal blast radius classified
- [ ] containment decision recorded before convenience optimization
- [ ] current vendor floor applied, or unaffected status proven with mounted evidence
- [ ] docs, policy, contracts, schemas, tests, and release evidence reviewed together
- [ ] rollback / correction / disclosure need evaluated explicitly
- [ ] residual unknowns left visible instead of silently collapsed

Definition of done:

1. **Not just patched** — the trust consequence is contained.
2. **Not just tested** — negative-path behavior and coupled proof surfaces are updated.
3. **Not just redeployed** — closure preserves release/correction lineage.
4. **Not just asserted** — unaffected claims have mounted evidence behind them.

## FAQ

### Is every React app affected?

No. The upstream condition is narrower: apps without a server, or without a framework/bundler/plugin that supports React Server Components, are not affected. KFM still needs mounted evidence before using that as a local close path.

### Does the scaffold-only public tree prove KFM is safe?

No. It proves this advisory lane needed expansion. It does **not** prove current package inventory, deployed router mode, or runtime exposure.

### Can this advisory be closed with a doc-only change?

No. If KFM is affected, closure should move behavior, proof, and communication together.

### Should exploit details or replayable payloads live here?

No. Keep this leaf actionable but non-weaponized.

[Back to top](#react2shell-advisory)

## Appendix

<details>
<summary><strong>Source basis and verification boundary</strong></summary>

### CONFIRMED from the current public repo

- `docs/security/react2shell-advisory/README.md` exists.
- `docs/security/react2shell/README.md` exists.
- both files were scaffold-only before this rewrite.
- `docs/security/README.md` already routes readers to both lanes.
- `/docs/` ownership is visible via `/.github/CODEOWNERS`.
- npm dependency monitoring is documented via `/.github/dependabot.yml`.
- likely runtime inspection begins under `apps/explorer-web/`, `apps/governed-api/`, and `apps/review-console/`, but their public-tree evidence remains README-level.

### CONFIRMED upstream facts this leaf is built around

- the original React2Shell disclosure is the React Server Components RCE advisory family.
- follow-on React advisories mean earlier emergency patch floors are not the end state.
- the current safe backport floor for affected `react-server-dom-*` packages is `19.0.4`, `19.1.5`, and `19.2.4`.
- Next.js App Router is downstream-affected; Pages Router is not.

### UNKNOWN / NEEDS VERIFICATION before merge-time closure

- exact mounted `package.json` / lockfile inventory
- exact deployed React / Next.js / RSC surface
- whether KFM uses App Router, other RSC-capable frameworks, or only browser/client rendering
- whether any historical public exposure requires rotation, visible correction, or advisory escalation
- whether current CI gates already enforce the closure path this leaf describes

</details>

<details>
<summary><strong>Suggested close-note template</strong></summary>

Use a close note that leaves a trail:

- advisory family reviewed
- mounted inventory checked
- affected / not affected decision and why
- patched floor or non-affected proof
- containment / rollback / correction decision
- coupled surfaces updated
- remaining unknowns, if any

</details>

[Back to top](#react2shell-advisory)
