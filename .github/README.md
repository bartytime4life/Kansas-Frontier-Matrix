<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/repo/.github/readme
title: .github README
type: standard
version: v2
status: draft
owners: @bartytime4life
created: 2026-03-15
updated: 2026-04-02
policy_label: NEEDS_VERIFICATION
related: [../README.md, ../CONTRIBUTING.md, ../SECURITY.md, ../docs/governance/, ../docs/architecture/, ../docs/domains/, ../docs/runbooks/, ../docs/adr/, ../contracts/, ../policy/, ../data/registry/, ../apps/, ../packages/, ../infra/, ../tools/, ../scripts/, ../tests/, ./ISSUE_TEMPLATE/, ./actions/, ./watchers/, ./workflows/, ./CODEOWNERS, ./PULL_REQUEST_TEMPLATE.md, ./SECURITY.md, ./dependabot.yml]
tags: [kfm, github, governance, ci-cd, verification, review, delivery, dependabot, watchers]
notes: [Created date preserved from the supplied baseline record; updated date reflects this draft revision; current public main now includes .github/watchers/; ISSUE_TEMPLATE/config.yml and actions/action.yml remain empty on current public main; workflows/ remains README-only; .github/SECURITY.md and ../SECURITY.md are not yet fully aligned; GitHub rulesets, required checks, environment approvals, and app/OIDC permissions remain NEEDS VERIFICATION.]
[/KFM_META_BLOCK_V2] -->

<div align="center">
  <strong>Kansas Frontier Matrix</strong><br />
  <sub>Repository gatehouse for governance, review, CI/CD, disclosure, and emit-only watcher control</sub>
</div>

# `.github`

Repository-wide governance, contributor intake, review routing, automation scaffolding, disclosure posture, and control-plane-adjacent watcher entrypoint for Kansas Frontier Matrix.

![status](https://img.shields.io/badge/status-active-0a7d5a)
![doc](https://img.shields.io/badge/doc-draft-8250df)
![owners](https://img.shields.io/badge/owners-%40bartytime4life-0969da)
![repo](https://img.shields.io/badge/repo-public-1f6feb)
![branch](https://img.shields.io/badge/default%20branch-main-0a7d5a)
![truth](https://img.shields.io/badge/truth-public%20tree%20inspected%20%7C%20KFM%20doctrine-6f42c1)
![delivery](https://img.shields.io/badge/delivery-gatehouse-0a7d5a)

| Field | Value |
|---|---|
| Status | **active** directory · **draft** README revision |
| Owners | **`@bartytime4life`** *(current public `CODEOWNERS` coverage for `/.github/`)* |
| Path | `.github/README.md` |
| Default branch | `main` |
| Visibility | public |
| Audience | maintainers, reviewers, contributors, release stewards |
| Repo role | gatehouse for intake, review boundaries, local GitHub automation, workflow documentation, dependency-update policy, disclosure/release-control surfaces, and emit-only watcher scaffolding |
| Trust posture | **CONFIRMED** current public repo tree and public Markdown surfaces · **CONFIRMED** KFM doctrine language already used in-repo · **UNKNOWN** GitHub rulesets, required checks, environment approvals, app permissions, OIDC wiring, and other platform-only settings |
| Current public tree state | `.github/` contains `ISSUE_TEMPLATE/`, `actions/`, `watchers/`, `workflows/`, `CODEOWNERS`, `PULL_REQUEST_TEMPLATE.md`, `README.md`, `SECURITY.md`, and `dependabot.yml`; `ISSUE_TEMPLATE/config.yml` and `actions/action.yml` are empty; `watchers/` and `workflows/` are README-only on public `main` |

**Quick jump:** [Scope](#scope) · [Current public deltas](#current-public-deltas) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Current public inventory](#current-public-inventory--control-surfaces) · [Task list / definition of done](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> This revision remains **public-tree-grounded** rather than merely documentary.
>
> It keeps the strong structure of the current checked-in README, but updates it for the now-visible `.github/watchers/` lane, keeps workflow-YAML claims conservative, and makes the current security-path drift impossible to miss.
>
> Use these labels throughout this file:
> - **CONFIRMED** — directly supported by the current public repo tree or checked-in Markdown surfaces
> - **INFERRED** — conservative interpretation that follows from confirmed repo evidence
> - **PROPOSED** — doctrine-consistent realization guidance not yet proven as checked-in behavior
> - **UNKNOWN** — not established strongly enough to present as current repo or platform reality
> - **NEEDS VERIFICATION** — placeholder or platform detail that should be checked before merge

## Scope

`.github/` is KFM’s repository-level **gatehouse**.

This is where contributor intake, review routing, ownership boundaries, disclosure posture, update automation, and workflow-bearing delivery controls become explicit repo surfaces instead of ambient intention. In KFM terms, `.github/` is one of the clearest repository expressions of the **trust membrane**: the place where changes are supposed to cross review, verification, and release-bearing gates before they widen into outward-facing consequence.

A strong `.github/` tree does more than “host CI.” It keeps responsibility visible. It shapes intake before drift spreads. It helps documentation, templates, policy checks, and release evidence move through one governed stream rather than fragment into side channels.

Current public `main` also shows a second, more unusual role: `.github/` now hosts a small **watcher** lane. That lane is still docs-only in the checked-in tree, but it makes the gatehouse responsible not just for review and automation scaffolding, but also for describing how derived monitoring surfaces must remain **emit-only**, **rebuildable**, and **review-bearing** rather than silently publishing themselves.

### Evidence boundary used here

| Evidence layer | What this README treats as settled |
|---|---|
| **CONFIRMED doctrine language already present in-repo** | truth path, trust membrane, authoritative-versus-derived split, cite-or-abstain posture, fail-closed defaults, promotion as governed state transition, and documentation as a trust surface |
| **CONFIRMED current public repo tree** | exact checked-in `.github/` inventory on public `main`, including `ISSUE_TEMPLATE/`, `actions/`, `watchers/`, `workflows/`, `CODEOWNERS`, `PULL_REQUEST_TEMPLATE.md`, `README.md`, `SECURITY.md`, and `dependabot.yml` |
| **CONFIRMED current public adjacent docs** | root `README.md`, `CONTRIBUTING.md`, root `SECURITY.md`, and visible repo-root directories under `docs/`, `data/`, `policy/`, `contracts/`, `tests/`, and `tools/` |
| **UNKNOWN / NEEDS VERIFICATION** | protected branches, required checks, rulesets, environment approvals, private reporting switches, GitHub App permissions, OIDC trust relationships, unpublished workflow history, and any non-public deployment or release controls |

### Current public signals worth carrying forward

| Public signal | What it supports | Status |
|---|---|---|
| Public repo with default branch `main` | GitHub is the active repo-facing control plane | CONFIRMED |
| `.github/` includes intake, ownership, security, actions, watchers, workflow, and dependency-update surfaces | the gatehouse is real and non-trivial in the checked-in tree | CONFIRMED |
| `.github/workflows/` contains `README.md` only | current public `main` does **not** expose checked-in workflow YAMLs in that directory | CONFIRMED |
| `.github/workflows/README.md` documents prior workflow activity and deleted YAML names | historical workflow signal exists, but it is not proof of current checked-in YAML inventory | CONFIRMED |
| `.github/actions/` contains multiple local action directories plus docs | reusable repo-local automation scaffolding exists even without checked-in workflow YAMLs on public `main` | CONFIRMED |
| `.github/watchers/` exists with `README.md` only | the gatehouse now includes a docs-only derived monitoring lane | CONFIRMED |
| `CODEOWNERS` assigns global fallback and `/.github/` coverage to `@bartytime4life` | review routing exists, but is currently broad and single-owner | CONFIRMED |
| `PULL_REQUEST_TEMPLATE.md` requires truth labels, evidence links, doctrine impact, and validation structure | PR review is explicitly shaped around KFM governance language | CONFIRMED |
| `dependabot.yml` is checked in | dependency-update policy is part of the repo-side control surface | CONFIRMED |
| both `.github/SECURITY.md` and `../SECURITY.md` exist | disclosure guidance still needs one clearly aligned public path | CONFIRMED existence / NEEDS VERIFICATION alignment |

> [!NOTE]
> Platform state is not the same thing as repo state. A checked-in file can describe required checks or disclosure posture, but it cannot by itself prove that GitHub settings, rulesets, reviewer gates, or private-reporting switches currently match the prose.

## Current public deltas

These are the concrete public-tree changes and tensions that make this revision necessary.

| Delta | Why it matters now | Status |
|---|---|---|
| `.github/watchers/` now exists on public `main` | the gatehouse now includes a watcher lane that the earlier README inventory did not name | CONFIRMED |
| `watchers/` is README-only | current public tree proves documentation/scaffold presence, not mounted watcher jobs here | CONFIRMED |
| `.github/SECURITY.md` claims the canonical public disclosure path is `.github/SECURITY.md` | the gatehouse security doc is trying to become authoritative | CONFIRMED doc claim |
| root `../SECURITY.md` still says the canonical public security-policy path is `REVIEW-REQUIRED` | the two public security-policy files are not yet fully aligned | CONFIRMED conflict |
| `.github/workflows/` remains README-only while `workflows/README.md` records historical deleted workflow filenames | historical automation signal exists, but current checked-in workflow inventory is still docs-only | CONFIRMED |
| `ISSUE_TEMPLATE/config.yml` and `actions/action.yml` are still empty | two entrypoint/config paths exist only as placeholders on current public `main` | CONFIRMED |

[Back to top](#github)

## Repo fit

**Path:** `.github/README.md`

**Role in repo:** directory README for repository-wide governance, contributor intake, review boundaries, reusable GitHub automation, workflow documentation, watcher-boundary guidance, disclosure posture, and dependency-update policy.

**Why it exists:** explain how repository-side control surfaces preserve KFM’s truth path without pretending that `.github/` is the canonical home of contracts, policy bundles, runtime code, data artifacts, or long-form doctrine.

### Upstream and downstream anchors

| Direction | Path | Why it matters | Status in this README |
|---|---|---|---|
| Upstream | [`../README.md`](../README.md) | root repo identity and orientation | CONFIRMED |
| Upstream | [`../CONTRIBUTING.md`](../CONTRIBUTING.md) | contributor expectations and evidence-bounded change discipline | CONFIRMED |
| Upstream | [`../SECURITY.md`](../SECURITY.md) | second checked-in public security-policy path that must align or delegate clearly | CONFIRMED |
| Upstream | [`../docs/governance/`](../docs/governance/) | governance doctrine and repo-facing review rules | CONFIRMED path |
| Upstream | [`../docs/architecture/`](../docs/architecture/) | architecture doctrine adjacent to delivery and review surfaces | CONFIRMED path |
| Upstream | [`../docs/domains/`](../docs/domains/) | Kansas-first operating lanes that change burden and review posture | CONFIRMED path |
| Upstream | [`../docs/runbooks/`](../docs/runbooks/) | operator and rollback/correction procedure home | CONFIRMED path |
| Upstream | [`../docs/adr/`](../docs/adr/) | decision records that should travel with behavior-significant governance change | CONFIRMED path |
| Upstream | [`../contracts/`](../contracts/) | canonical machine-readable contracts and schemas | CONFIRMED path |
| Upstream | [`../policy/`](../policy/) | executable policy bundles, fixtures, and tests | CONFIRMED path |
| Upstream | [`../data/registry/`](../data/registry/) | source descriptors and intake registry material | CONFIRMED path |
| Downstream | [`./CODEOWNERS`](./CODEOWNERS) | executable review boundary map | CONFIRMED |
| Downstream | [`./ISSUE_TEMPLATE/`](./ISSUE_TEMPLATE/) | contributor issue-intake surface | CONFIRMED |
| Downstream | [`./PULL_REQUEST_TEMPLATE.md`](./PULL_REQUEST_TEMPLATE.md) | PR review contract and doctrine checklist | CONFIRMED |
| Downstream | [`./actions/`](./actions/) | repo-local reusable GitHub Actions logic and scaffolding | CONFIRMED |
| Downstream | [`./watchers/`](./watchers/) | docs-only watcher lane describing emit-only derived monitoring rules | CONFIRMED |
| Downstream | [`./workflows/`](./workflows/) | workflow documentation lane; currently README-only on public `main` | CONFIRMED |
| Downstream | [`./SECURITY.md`](./SECURITY.md) | repo-local disclosure-policy surface | CONFIRMED |
| Downstream | [`./dependabot.yml`](./dependabot.yml) | dependency-update automation policy | CONFIRMED |

<details>
<summary><strong>Broader repo context</strong> — current public <code>main</code> root snapshot</summary>

```text
repo/
├── .github/
├── apps/
├── brand/
├── configs/
├── contracts/
├── data/
├── docs/
├── examples/
├── infra/
├── migrations/
├── packages/
├── policy/
├── schemas/
├── scripts/
├── tests/
├── tools/
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

</details>

[Back to top](#github)

## Accepted inputs

The following content belongs in `.github/` when it applies across the repository rather than to one package or application.

| Input class | What belongs here | Why it belongs here |
|---|---|---|
| Review-boundary files | `CODEOWNERS`, repo-wide review-routing notes, path ownership, self-protection rules | review is part of KFM’s trust system |
| Structured contributor intake | issue-template chooser files, issue-template docs, PR templates, merge-readiness checklists | intake should be shaped before change widens |
| Reusable repo-local automation | composite actions, setup helpers, policy/install helpers, provenance or metadata guards | keeps repeated steps reviewable and local to the repo |
| Workflow definitions and workflow docs | CI, validation, promotion, correction, rollback, reconciliation, and release-control lanes | repo-wide control and trust-state transitions live here when checked in |
| Watcher control docs | emit-only rules, materiality thresholds, receipt/open-PR conventions, and review-bearing watcher guidance | keeps monitoring surfaces derived, rebuildable, and steward-reviewed |
| Security and disclosure entrypoints | `SECURITY.md`, disclosure flow docs, safe-harbor guidance, automation-identity notes | trust-bearing reporting needs a clear repo-level home |
| Dependency update policy | `dependabot.yml` and adjacent governance notes | automated dependency change is part of delivery posture, not an afterthought |

## Exclusions

`.github/` can gate, reference, or validate these surfaces, but it should not quietly replace them as their canonical home.

| Does **not** belong here as canonical truth | Keep it here instead |
|---|---|
| machine-readable schemas, envelopes, OpenAPI specs, vocabularies | [`../contracts/`](../contracts/) and [`../schemas/`](../schemas/) |
| policy bodies, reason-code registries, fixtures, decision tests | [`../policy/`](../policy/) |
| canonical data artifacts, source descriptors, lifecycle-zone payloads, receipts, published datasets | [`../data/`](../data/) and [`../data/registry/`](../data/registry/) |
| runtime services, UI logic, ingestion code, evidence resolvers | [`../apps/`](../apps/) and [`../packages/`](../packages/) |
| publishable watcher outputs, canonical source captures, or long-running domain ETL | [`../data/`](../data/), [`../apps/`](../apps/), [`../packages/`](../packages/), or [`../scripts/`](../scripts/) |
| long-form doctrine, ADRs, standards, runbooks, architecture manuals | [`../docs/`](../docs/) |
| secrets, private vulnerability details, unpublished review material, exact restricted coordinates | never in public `.github/`; route through stewarded or private paths |
| release artifacts, immutable manifests, proof packs | owning artifact home or designated release/evidence path, not ad hoc `.github/` storage |

[Back to top](#github)

## Directory tree

Current public `main` shows the following checked-in `.github/` layout.

```text
.github/
├── ISSUE_TEMPLATE/
│   ├── README.md
│   └── config.yml                     # empty on current public main
├── actions/
│   ├── metadata-validate-v2/
│   ├── metadata-validate/
│   ├── opa-gate/
│   ├── provenance-guard/
│   ├── sbom-produce-and-sign/
│   ├── src/
│   ├── README.md
│   └── action.yml                     # empty on current public main
├── watchers/
│   └── README.md                      # docs-only watcher scaffold on current public main
├── workflows/
│   └── README.md                      # no checked-in workflow YAML visible on current public main
├── CODEOWNERS
├── PULL_REQUEST_TEMPLATE.md
├── README.md
├── SECURITY.md
└── dependabot.yml
```

> [!TIP]
> The most important tree correction in this revision is simple: `watchers/` is now visibly part of `.github/` on public `main`, so the directory README must account for it explicitly.

## Quickstart

Before changing repo-wide governance surfaces, inspect the current checkout and compare it against the public-main snapshot above.

```bash
# 0) Start from the repo root
git rev-parse --show-toplevel 2>/dev/null || pwd

# 1) Inventory the gatehouse
find .github -maxdepth 2 -type f | sort
find .github -maxdepth 2 -type d | sort

# 2) Inspect the highest-signal repo-side control surfaces
sed -n '1,220p' .github/README.md
sed -n '1,220p' .github/CODEOWNERS
sed -n '1,260p' .github/PULL_REQUEST_TEMPLATE.md
sed -n '1,260p' .github/SECURITY.md
sed -n '1,260p' .github/dependabot.yml

# 3) Inspect current intake, local-action, and watcher state
find .github/ISSUE_TEMPLATE -maxdepth 1 -type f | sort
find .github/actions -maxdepth 2 -type f | sort
find .github/watchers -maxdepth 2 -type f | sort
test -s .github/ISSUE_TEMPLATE/config.yml || echo ".github/ISSUE_TEMPLATE/config.yml is empty"
test -s .github/actions/action.yml || echo ".github/actions/action.yml is empty"

# 4) Inspect current workflow lane state
find .github/workflows -maxdepth 1 -type f | sort
find .github/workflows -maxdepth 1 \( -name '*.yml' -o -name '*.yaml' \) | sort

# 5) Check adjacent authority surfaces that .github should gate, not replace
find docs -maxdepth 2 -type d | sort | sed -n '1,160p'
find data -maxdepth 2 -type d | sort | sed -n '1,160p'
find policy -maxdepth 2 -type d | sort | sed -n '1,160p'
find contracts -maxdepth 2 -type f | sort | sed -n '1,120p'
find tests -maxdepth 2 -type d | sort | sed -n '1,160p'

# 6) Platform-state checks happen outside the repo tree:
#    - protected branches / rulesets
#    - required status checks
#    - environment reviewers / deployment approvals
#    - private vulnerability reporting
#    - GitHub App and OIDC permissions
```

## Usage

Use this README as the responsibility map for repo-side governance work.

1. **Inspect before editing.** Confirm the live tree, not just remembered structure or historical discussion.
2. **Map the change to trust impact.** Ask whether the edit changes intake, ownership, merge-blocking logic, disclosure flow, dependency automation, watcher behavior, release evidence, or correction posture.
3. **Keep trust-bearing automation review-bearing.** KFM doctrine prefers visible deltas, attached evidence, and reversible changes whenever automation could change trust state.
4. **Update adjacent docs in the same change stream.** If review routing, disclosure posture, automation lanes, watcher rules, or dependency policy change, the corresponding README, template, or runbook should travel with the same PR.

### Build, watch, deploy, and promote are different moves

| Move | What changes | Why `.github/` cares |
|---|---|---|
| **Build** | a versioned artifact or proof object exists | repo automation, metadata guards, and attest/review surfaces often begin here |
| **Watch** | a derived monitoring surface detects change and emits a candidate | `.github/watchers/` must remain emit-only, evidence-backed, and PR/review-bearing |
| **Deploy** | runtime placement or hosted execution changes | environment approvals, rollback readiness, and post-deploy checks may be triggered here |
| **Promote** | trust state changes from candidate to releasable/publishable | policy, docs, review, and proof obligations become mandatory here |

### Current public-main reading of the gatehouse

| Surface family | Current public `main` state | Consequence |
|---|---|---|
| Contributor issue intake | `ISSUE_TEMPLATE/` exists, but current visible files are `README.md` plus an empty `config.yml` | intake directory is present, but no checked-in issue forms are visible on public `main` |
| PR review intake | `PULL_REQUEST_TEMPLATE.md` is present and substantial | PRs already carry structured KFM review prompts |
| Review ownership | `CODEOWNERS` uses broad single-owner coverage with explicit `/.github/` self-protection | routing exists, but granularity is intentionally conservative |
| Local action scaffolding | multiple repo-local action directories are checked in | repeated workflow steps are intended to stay local and reviewable |
| Watcher lane | `watchers/README.md` is present, but no additional watcher files are visible beneath it | watcher behavior is described, but current public `main` proves only a docs/scaffold lane here |
| Workflow lane | `workflows/README.md` is present, but no `.yml` or `.yaml` files are visible in that directory on public `main` | current public branch shows documented intent rather than checked-in workflow definitions |
| Dependency automation | `dependabot.yml` is present and multi-ecosystem | dependency update policy is active as repo config |
| Security disclosure | both `.github/SECURITY.md` and root `SECURITY.md` exist, but they are not yet fully aligned | canonical disclosure wording still needs one decisive public answer |

> [!NOTE]
> `./workflows/README.md` currently records historical GitHub Actions activity and deleted workflow filenames such as `verify-docs.yml`, `verify-contracts-and-policy.yml`, and `release-evidence.yml`. Treat that as **history**, not as proof that those YAMLs are currently checked in.

### When this file should change

- when `.github/` inventory changes
- when workflow YAML files are added, removed, or renamed
- when watcher scaffolding changes, expands, or moves
- when issue or PR intake surfaces change
- when security-path canonicalization changes
- when local action scaffolding changes materially
- when dependency-update policy changes
- when GitHub-settings verification steps need sharper guidance

[Back to top](#github)

## Diagram

```mermaid
flowchart LR
    A[Contributor / maintainer / automation / watcher] --> B[.github gatehouse]

    subgraph G["Current public .github surfaces"]
      G1["README.md<br/>responsibility map"]
      G2["CODEOWNERS<br/>review boundary"]
      G3["PULL_REQUEST_TEMPLATE.md<br/>truth + validation checklist"]
      G4["ISSUE_TEMPLATE/<br/>README + empty config"]
      G5["actions/<br/>local action scaffolding"]
      G6["watchers/<br/>README-only emit-only lane"]
      G7["workflows/<br/>README only on public main"]
      G8["dependabot.yml<br/>dependency update policy"]
      G9["SECURITY.md<br/>disclosure path"]
    end

    B --> G1
    B --> G2
    B --> G3
    B --> G4
    B --> G5
    B --> G6
    B --> G7
    B --> G8
    B --> G9

    G2 --> H[Required review routing]
    G3 --> I[Merge-readiness structure]
    G5 -. intended callers .-> G7
    G6 --> J[Derived change candidate<br/>with evidence]
    G8 --> K[Automated dependency PRs]
    G9 --> L[Disclosure handling]

    H --> M{Trust state can widen?}
    I --> M
    J --> M
    K --> M

    M -->|yes| N[Policy / validation / proof / human review]
    M -->|no| O[Clarify / revise / redirect]

    N --> P[Merge / correction / follow-up]
    P -. platform settings still need direct GitHub verification .-> Q[Rulesets / required checks / environments]
```

## Current public inventory & control surfaces

| Surface | Current evidence status | Primary role | Why it is sensitive |
|---|---|---|---|
| [`./README.md`](./README.md) | CONFIRMED | repo-side responsibility map | drift here blurs the control plane |
| [`./CODEOWNERS`](./CODEOWNERS) | CONFIRMED | executable review routing; current broad ownership coverage | changes approval scope and separation of duty |
| [`./PULL_REQUEST_TEMPLATE.md`](./PULL_REQUEST_TEMPLATE.md) | CONFIRMED | structured PR intake with truth labels, evidence links, doctrine impact, and validation structure | weak PR prompts degrade review quality |
| [`./ISSUE_TEMPLATE/README.md`](./ISSUE_TEMPLATE/README.md) | CONFIRMED | issue-intake guidance | contributor intake should stay governed rather than improvised |
| [`./ISSUE_TEMPLATE/config.yml`](./ISSUE_TEMPLATE/config.yml) | CONFIRMED current file presence | issue chooser config path | currently an empty placeholder on public `main` |
| [`./actions/`](./actions/) | CONFIRMED | repo-local reusable GitHub Actions scaffolding | local actions can hide trust-bearing behavior if undocumented |
| [`./actions/action.yml`](./actions/action.yml) | CONFIRMED current file presence | root action manifest path | currently an empty placeholder on public `main` |
| [`./watchers/README.md`](./watchers/README.md) | CONFIRMED | docs-only watcher lane with emit-only, derived-surface rules | watcher surfaces must not bypass governed publication |
| [`./workflows/README.md`](./workflows/README.md) | CONFIRMED | workflow documentation lane | current public branch shows docs without checked-in workflow YAMLs |
| `./workflows/*.yml|*.yaml` | CONFIRMED current public absence | checked-in workflow definitions | none visible on public `main` at the time of this revision |
| [`./SECURITY.md`](./SECURITY.md) | CONFIRMED | repo-local disclosure-policy surface | public disclosure posture needs one stable path |
| [`../SECURITY.md`](../SECURITY.md) | CONFIRMED | second checked-in security-policy path | canonicalization is still unresolved across the two public files |
| [`./dependabot.yml`](./dependabot.yml) | CONFIRMED | dependency update automation policy | bot-driven dependency PRs still affect trust and delivery posture |
| GitHub rulesets / required checks / env approvals | UNKNOWN in this README | platform enforcement | cannot be proven from checked-in files alone |

### Current public scaffolding-only surfaces

| Path | Observed state | Practical reading |
|---|---|---|
| `./ISSUE_TEMPLATE/config.yml` | empty file | chooser path exists, but public `main` does not yet prove template options here |
| `./actions/action.yml` | empty file | root action manifest path exists, but public `main` does not prove implementation at that level |
| `./watchers/README.md` | docs-only | watcher rules are documented, but no checked-in watcher jobs are visible beneath this path |
| `./workflows/README.md` | docs-only | workflow lane is documented, but no checked-in workflow YAMLs are visible here |

### Current public action inventory

| Path | Observed state | Posture |
|---|---|---|
| `./actions/metadata-validate-v2/` | present | CONFIRMED path |
| `./actions/metadata-validate/` | present | CONFIRMED path |
| `./actions/opa-gate/` | present | CONFIRMED path |
| `./actions/provenance-guard/` | present | CONFIRMED path |
| `./actions/sbom-produce-and-sign/` | present | CONFIRMED path |
| `./actions/src/` | present | CONFIRMED path |
| `./actions/README.md` | present | CONFIRMED path |
| `./actions/action.yml` | present, empty on current public `main` | CONFIRMED current snapshot |

### Current public dependency-update coverage

| Ecosystem | Paths | Schedule (UTC) |
|---|---|---|
| `github-actions` | `/` | weekly · Monday · 06:00 |
| `docker` | `/`, `/apps/*`, `/packages/*`, `/infra/*` | weekly · Monday · 06:30 |
| `npm` | `/`, `/apps/*`, `/packages/*` | weekly · Tuesday · 06:00 |
| `pip` | `/`, `/apps/*`, `/packages/*` | weekly · Wednesday · 06:00 |
| `cargo` | `/`, `/apps/*`, `/packages/*` | weekly · Thursday · 06:00 |

[Back to top](#github)

## Task list / definition of done

- [ ] The live checkout matches the tree documented above, including `watchers/`.
- [ ] `.github/README.md`, `.github/CODEOWNERS`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/SECURITY.md`, `.github/dependabot.yml`, `.github/watchers/README.md`, and `.github/workflows/README.md` were re-read in the same branch being merged.
- [ ] `ISSUE_TEMPLATE/` still contains exactly the files documented here, or this README was updated in the same PR.
- [ ] `actions/` still contains the documented subdirectories, or this README was updated in the same PR.
- [ ] `watchers/` was checked for any new files or jobs beyond `README.md`, or this README was updated in the same PR.
- [ ] `workflows/` was checked for actual `.yml` / `.yaml` files before any workflow claim was merged.
- [ ] Any empty placeholders (`ISSUE_TEMPLATE/config.yml`, `actions/action.yml`) remain intentional and documented, or they were replaced with real content.
- [ ] `CODEOWNERS` coverage still matches the review expectations described here.
- [ ] `.github/SECURITY.md` and `../SECURITY.md` are either text-aligned or one clearly delegates to the other.
- [ ] Branch protection, rulesets, required checks, environment approvals, and private-reporting settings were verified in GitHub settings when relevant.
- [ ] UNKNOWN items remain explicit instead of being rewritten as certainty.
- [ ] Docs, templates, automation, and watcher-boundary changes that affect trust state move through the same review stream.

## FAQ

### Does current public `main` expose checked-in workflow YAML files?

Not in the public directory listing inspected for this revision. `./workflows/README.md` is present, but no `.yml` or `.yaml` files were visible in `./workflows/` on public `main`.

### What is `.github/watchers/` right now?

Current public `main` shows `./watchers/README.md` only. Its own checked-in guidance describes watchers as **derived**, **fail-closed**, and **emit-only** monitoring surfaces that must open a governed review path instead of publishing directly.

### Does current public `main` expose issue-form templates?

The issue-template directory exists, but the visible checked-in files are `README.md` plus an empty `config.yml`. No issue-form or Markdown template files were visible in that directory on public `main`.

### Who currently owns `.github/`?

Current public `CODEOWNERS` assigns the global fallback to `@bartytime4life` and explicitly assigns `/.github/` plus `/.github/CODEOWNERS` to `@bartytime4life`.

### Is the public security-policy path resolved?

Not yet. `.github/SECURITY.md` currently presents itself as the canonical public disclosure path, but root `SECURITY.md` still says the canonical public path is `REVIEW-REQUIRED`. Those two files should be aligned or delegated cleanly.

### What remains unverified after this revision?

GitHub private-reporting settings beyond what the checked-in docs say, protected-branch rules, required checks, rulesets, environment approvals, GitHub App permissions, OIDC trust relationships, and any non-public release or deployment controls.

## Appendix

<details>
<summary><strong>Confirmed public-main snapshot notes</strong></summary>

### `.github/` currently visible on public `main`

- `ISSUE_TEMPLATE/` exists with `README.md` and empty `config.yml`
- `actions/` exists with five named action directories, `src/`, `README.md`, and empty `action.yml`
- `watchers/` exists with `README.md` only
- `workflows/` exists with `README.md` only
- `CODEOWNERS`, `PULL_REQUEST_TEMPLATE.md`, `README.md`, `SECURITY.md`, and `dependabot.yml` are checked in

### Adjacent repo paths confirmed during this revision

- root directories: `apps/`, `brand/`, `configs/`, `contracts/`, `data/`, `docs/`, `examples/`, `infra/`, `migrations/`, `packages/`, `policy/`, `schemas/`, `scripts/`, `tests/`, `tools/`
- repo-root docs: `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `LICENSE`, `README.md`, `SECURITY.md`
- `docs/`, `data/`, `policy/`, `contracts/`, `tests/`, and `tools/` are all visibly present at repo root and remain the more natural homes for canonical doctrine, data, policy, contracts, validation, and tooling

### Practical reading rule

This directory is currently strongest as a **repo-side control map**, **local automation scaffold**, and **review-bearing watcher boundary**. The biggest public-tree gaps are still the absence of checked-in workflow YAMLs under `.github/workflows/` and the unresolved duplication of the public security-policy path.

</details>

<details>
<summary><strong>Historical signal, not present-tree proof</strong></summary>

`./workflows/README.md` documents prior GitHub Actions activity and names deleted workflow files such as:

- `verify-docs.yml`
- `verify-contracts-and-policy.yml`
- `verify-runtime.yml`
- `verify-tests-and-reproducibility.yml`
- `release-evidence.yml`
- `promote-and-reconcile.yml`

That is useful context for recovery, archaeology, or reconstitution work, but it is **not** the same as current checked-in inventory on public `main`.

</details>

<details>
<summary><strong>Open verification backlog</strong></summary>

1. Verify whether watcher logic exists elsewhere in the repo outside the docs-only `.github/watchers/` scaffold.
2. Confirm whether `ISSUE_TEMPLATE/config.yml` and `actions/action.yml` are intentional empty placeholders or incomplete scaffolding.
3. Choose and enforce one canonical public security-policy path, or explicitly delegate from one file to the other.
4. Recheck `CODEOWNERS` granularity if ownership expands beyond the current broad single-owner baseline.
5. Export or inspect GitHub rulesets, required checks, environment approvals, app permissions, OIDC trust bindings, and private vulnerability-reporting settings.
6. Reconcile `.github/README.md`, `.github/workflows/README.md`, `.github/actions/README.md`, `.github/watchers/README.md`, root `README.md`, `CONTRIBUTING.md`, and both security-policy files so they describe the same current control-plane reality.
7. Retire UNKNOWN items only when direct repo or platform evidence is attached to the same PR.

</details>

[Back to top](#github)
