<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/repo/.github/readme
title: .github README
type: standard
version: v2
status: draft
owners: @bartytime4life
created: 2026-03-15
updated: 2026-04-09
policy_label: NEEDS_VERIFICATION
related: [../README.md, ../CONTRIBUTING.md, ../CHANGELOG.md, ../SECURITY.md, ../docs/governance/, ../docs/architecture/, ../docs/domains/, ../docs/runbooks/, ../docs/adr/, ../contracts/, ../schemas/, ../policy/, ../data/registry/, ../apps/, ../packages/, ../pipelines/, ../infra/, ../scripts/, ../tests/, ../tools/, ./ISSUE_TEMPLATE/, ./actions/, ./watchers/, ./workflows/, ./CODEOWNERS, ./PULL_REQUEST_TEMPLATE.md, ./SECURITY.md, ./dependabot.yml]
tags: [kfm, github, governance, ci-cd, review, disclosure, dependabot, watchers]
notes: [Created date preserved from the previously checked-in baseline; updated date reflects this draft revision; snapshot sections below record the last verified .github tree state and must be rechecked in the live branch before merge; ISSUE_TEMPLATE/config.yml and actions/action.yml were documented as empty placeholders in the last verified snapshot; workflows/ and watchers/ were documented as README-only in the last verified snapshot; .github/SECURITY.md and ../SECURITY.md were documented as not yet fully aligned; GitHub rulesets, required checks, environment approvals, private-reporting fallback channels, monitored secrets, app permissions, and OIDC bindings remain NEEDS VERIFICATION.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">
  <strong>Kansas Frontier Matrix</strong><br />
  <sub>Repository gatehouse for review routing, workflow-facing governance, disclosure posture, dependency policy, and emit-only watcher guidance</sub>
</div>

# `.github` README

Repo-side responsibility map for repository-wide governance, contributor intake, review routing, dependency policy, and control-plane-facing documentation in Kansas Frontier Matrix.

> [!NOTE]
> **Status:** active directory · draft README revision  
> **Owners:** `@bartytime4life` *(reconfirm in `CODEOWNERS` before merge if ownership changed)*  
> ![status](https://img.shields.io/badge/status-active-0a7d5a) ![doc](https://img.shields.io/badge/doc-draft-8250df) ![owners](https://img.shields.io/badge/owners-%40bartytime4life-0969da) ![scope](https://img.shields.io/badge/scope-.github-1f6feb) ![role](https://img.shields.io/badge/role-gatehouse-0a7d5a) ![posture](https://img.shields.io/badge/posture-evidence--bounded-6f42c1)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Control surfaces](#control-surfaces--reference-tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)  
> **Repo fit:** `.github/README.md` should route contributors toward `CODEOWNERS`, `PULL_REQUEST_TEMPLATE.md`, `SECURITY.md`, `dependabot.yml`, `watchers/`, and `workflows/`, while staying aligned with `../README.md`, `../CONTRIBUTING.md`, `../CHANGELOG.md`, and `../SECURITY.md`.

> [!IMPORTANT]
> This README is intentionally **evidence-bounded**. It preserves the strongest checked-in `.github` baseline and KFM doctrine, but it does not silently convert historical snapshot detail or GitHub platform settings into fresh proof. Recheck the live branch before merging behavior-bearing claims.

> [!TIP]
> Use these labels consistently:
> - **CONFIRMED** — directly supported by the last verified snapshot or adjacent project doctrine
> - **INFERRED** — conservative interpretation of confirmed evidence
> - **PROPOSED** — doctrine-consistent guidance not yet proven as checked-in behavior
> - **UNKNOWN** — not verified strongly enough to present as settled
> - **NEEDS VERIFICATION** — explicit reviewer action required before the detail should be treated as current repo truth

## Scope

`.github/` is KFM’s repository-level **gatehouse**.

This is where contributor intake, ownership boundaries, disclosure posture, dependency automation, and workflow-bearing delivery controls become explicit repo surfaces instead of ambient convention. In KFM terms, `.github/` is one of the clearest repository expressions of the **trust membrane**: the point where changes are expected to cross review, verification, and release-bearing gates before they widen into outward consequence.

This directory also carries a second burden in the documented snapshot: a small **watcher** lane. Even as a docs-only scaffold, that lane matters architecturally because it makes the gatehouse responsible not only for review and automation scaffolding, but also for stating how derived monitoring surfaces remain **emit-only**, **rebuildable**, and **review-bearing**.

### Evidence boundary used here

| Evidence layer | What this README treats as settled |
| --- | --- |
| **CONFIRMED KFM doctrine already used by the repo** | truth path, trust membrane, authoritative-versus-derived separation, cite-or-abstain posture, fail-closed defaults, promotion as a governed state transition |
| **CONFIRMED last verified `.github` snapshot recorded in this README family** | the `.github/` inventory, visible root directory families, and the presence of `../pipelines/` |
| **CONFIRMED adjacent repo surfaces referenced by that snapshot** | root docs and neighboring directories such as `docs/`, `data/`, `policy/`, `contracts/`, `schemas/`, `tests/`, `tools/`, and `pipelines/` |
| **UNKNOWN / NEEDS VERIFICATION** | live-branch drift since the last verified snapshot, unpublished workflow YAMLs, protected branches, required checks, rulesets, environment approvals, private-reporting switches, GitHub App permissions, OIDC trust relationships, and non-public release controls |

### Last verified snapshot deltas

These are the concrete deltas and tensions the latest verified snapshot already exposed.

| Delta | Why it matters | Status |
| --- | --- | --- |
| `.github/watchers/` is present | the gatehouse now includes a watcher lane that earlier inventories could miss | **CONFIRMED** |
| `watchers/` is README-only | the snapshot proves documentation/scaffold presence, not mounted watcher jobs there | **CONFIRMED** |
| `.github/workflows/` is README-only | workflow documentation exists, but checked-in workflow YAMLs were not documented in that snapshot | **CONFIRMED** |
| `./workflows/README.md` names deleted workflow files | historical automation signal exists, but it is not proof of current checked-in YAML inventory | **CONFIRMED** |
| `ISSUE_TEMPLATE/config.yml` and `actions/action.yml` were empty | two entrypoint/config paths were placeholders in the verified snapshot | **CONFIRMED** |
| `.github/SECURITY.md` and `../SECURITY.md` were not text-aligned | public disclosure routing still needed canonicalization or delegation | **CONFIRMED** |
| repo root included `pipelines/` with visible `soils/gssurgo-ks/` and `wbd-huc12-watcher/` lanes | `.github` should gate pipeline-facing trust changes without pretending to own pipeline runtime code | **CONFIRMED** |
| `dependabot.yml` did not explicitly name `/pipelines/*` | dependency automation exists, but pipeline lanes were not explicitly named in the documented globs | **CONFIRMED** |

[Back to top](#top)

## Repo fit

**Path:** `.github/README.md`

**Role in repo:** directory README for repository-wide governance, contributor intake, review boundaries, reusable GitHub automation, workflow documentation, watcher-boundary guidance, disclosure posture, and dependency-update policy.

**Why it exists:** explain how repo-side control surfaces preserve KFM’s truth path without pretending that `.github/` is the canonical home of contracts, policy bundles, runtime code, pipeline code, data artifacts, or long-form doctrine.

### Upstream and downstream anchors

| Direction | Path | Why it matters | Status in this README |
| --- | --- | --- | --- |
| Upstream | [`../README.md`](../README.md) | root repo identity and orientation | **CONFIRMED** |
| Upstream | [`../CONTRIBUTING.md`](../CONTRIBUTING.md) | contributor expectations and evidence-bounded change discipline | **CONFIRMED** |
| Upstream | [`../CHANGELOG.md`](../CHANGELOG.md) | repo-wide memory for behavior-significant process or trust-state change | **CONFIRMED path** |
| Upstream | [`../SECURITY.md`](../SECURITY.md) | second checked-in public security-policy path that should align or delegate clearly | **CONFIRMED** |
| Upstream | [`../docs/governance/`](../docs/governance/) | governance doctrine and repo-facing review rules | **CONFIRMED path** |
| Upstream | [`../docs/architecture/`](../docs/architecture/) | architecture doctrine adjacent to delivery and review surfaces | **CONFIRMED path** |
| Upstream | [`../docs/domains/`](../docs/domains/) | Kansas-first operating lanes that change burden and review posture | **CONFIRMED path** |
| Upstream | [`../docs/runbooks/`](../docs/runbooks/) | operator, rollback, and correction procedure home | **CONFIRMED path** |
| Upstream | [`../docs/adr/`](../docs/adr/) | decision records that should travel with behavior-significant governance change | **CONFIRMED path** |
| Upstream | [`../contracts/`](../contracts/) | canonical machine-readable contracts and schemas | **CONFIRMED path** |
| Upstream | [`../schemas/`](../schemas/) | schema surface adjacent to contract and policy enforcement | **CONFIRMED path** |
| Upstream | [`../policy/`](../policy/) | executable policy bundles, fixtures, and tests | **CONFIRMED path** |
| Upstream | [`../data/registry/`](../data/registry/) | source descriptors and intake registry material | **CONFIRMED path** |
| Upstream | [`../pipelines/`](../pipelines/) | execution lanes that `.github` may gate but does not canonically own | **CONFIRMED path** |
| Downstream | [`./CODEOWNERS`](./CODEOWNERS) | executable review boundary map | **CONFIRMED** |
| Downstream | [`./ISSUE_TEMPLATE/`](./ISSUE_TEMPLATE/) | contributor issue-intake surface | **CONFIRMED** |
| Downstream | [`./PULL_REQUEST_TEMPLATE.md`](./PULL_REQUEST_TEMPLATE.md) | PR review contract and doctrine checklist | **CONFIRMED** |
| Downstream | [`./actions/`](./actions/) | repo-local reusable GitHub Actions logic and scaffolding | **CONFIRMED** |
| Downstream | [`./watchers/`](./watchers/) | watcher lane describing emit-only derived monitoring rules | **CONFIRMED** |
| Downstream | [`./workflows/`](./workflows/) | workflow documentation lane | **CONFIRMED** |
| Downstream | [`./SECURITY.md`](./SECURITY.md) | repo-local disclosure-policy surface | **CONFIRMED** |
| Downstream | [`./dependabot.yml`](./dependabot.yml) | dependency-update automation policy | **CONFIRMED** |

<details>
<summary><strong>Broader repo context</strong> — last verified root snapshot</summary>

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
├── pipelines/
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

[Back to top](#top)

## Accepted inputs

The following content belongs in `.github/` when it applies across the repository rather than to one package or lane.

| Input class | What belongs here | Why it belongs here |
| --- | --- | --- |
| Review-boundary files | `CODEOWNERS`, repo-wide review-routing notes, self-protection rules | review is part of KFM’s trust system |
| Structured contributor intake | issue-template chooser files, issue-template docs, PR templates, merge-readiness checklists | intake should be shaped before change widens |
| Reusable repo-local automation | composite actions, setup helpers, policy/install helpers, metadata or provenance guards | keeps repeated steps reviewable and local to the repo |
| Workflow definitions and workflow docs | CI, validation, promotion, correction, rollback, reconciliation, and release-control lanes | repo-wide control and trust-state transitions live here when checked in |
| Watcher control docs | emit-only rules, materiality thresholds, receipt/open-PR conventions, and review-bearing watcher guidance | keeps monitoring surfaces derived, rebuildable, and steward-reviewed |
| Security and disclosure entrypoints | `SECURITY.md`, disclosure flow docs, safe-harbor guidance, automation-identity notes | trust-bearing reporting needs a clear repo-level home |
| Dependency update policy | `dependabot.yml` and adjacent governance notes | automated dependency change is part of delivery posture, not an afterthought |

## Exclusions

`.github/` can gate, reference, or validate these surfaces, but it should not quietly replace them as their canonical home.

| Does **not** belong here as canonical truth | Keep it here instead |
| --- | --- |
| machine-readable schemas, envelopes, OpenAPI specs, vocabularies | [`../contracts/`](../contracts/) and [`../schemas/`](../schemas/) |
| policy bodies, reason-code registries, fixtures, decision tests | [`../policy/`](../policy/) |
| canonical data artifacts, source descriptors, lifecycle-zone payloads, receipts, published datasets | [`../data/`](../data/) and [`../data/registry/`](../data/registry/) |
| runtime services, UI logic, ingestion code, pipeline execution code, evidence resolvers | [`../apps/`](../apps/), [`../packages/`](../packages/), [`../pipelines/`](../pipelines/), or [`../scripts/`](../scripts/) |
| publishable watcher outputs, canonical source captures, or long-running domain ETL | [`../data/`](../data/), [`../apps/`](../apps/), [`../packages/`](../packages/), [`../pipelines/`](../pipelines/), or [`../scripts/`](../scripts/) |
| long-form doctrine, ADRs, standards, runbooks, architecture manuals | [`../docs/`](../docs/) |
| secrets, private vulnerability details, unpublished review material, exact restricted coordinates | never in public `.github/`; route through stewarded or private paths |
| release artifacts, immutable manifests, proof packs | owning artifact home or designated release/evidence path, not ad hoc `.github/` storage |

[Back to top](#top)

## Directory tree

The last verified snapshot recorded the following `.github/` layout. Recheck it in the live branch before merging any inventory-sensitive claim.

```text
.github/
├── ISSUE_TEMPLATE/
│   ├── README.md
│   └── config.yml                     # empty in the last verified snapshot
├── actions/
│   ├── metadata-validate-v2/
│   ├── metadata-validate/
│   ├── opa-gate/
│   ├── provenance-guard/
│   ├── sbom-produce-and-sign/
│   ├── src/
│   ├── README.md
│   └── action.yml                     # empty in the last verified snapshot
├── watchers/
│   └── README.md                      # README-only watcher scaffold in the last verified snapshot
├── workflows/
│   └── README.md                      # no checked-in workflow YAMLs documented in the last verified snapshot
├── CODEOWNERS
├── PULL_REQUEST_TEMPLATE.md
├── README.md
├── SECURITY.md
└── dependabot.yml
```

> [!TIP]
> The most important tree correction in this README is simple: `watchers/` is visibly part of `.github/`, and the broader root context also includes `pipelines/`, so this directory README should account for both without collapsing their ownership boundaries.

[Back to top](#top)

## Quickstart

Before changing repo-wide governance surfaces, inspect the live checkout and compare it against the last verified snapshot documented here.

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
find schemas -maxdepth 2 -type f | sort | sed -n '1,120p'
find pipelines -maxdepth 3 | sort | sed -n '1,160p'
find tests -maxdepth 2 -type d | sort | sed -n '1,160p'

# 6) Platform-state checks happen outside the repo tree:
#    - protected branches / rulesets
#    - required status checks
#    - environment reviewers / deployment approvals
#    - private vulnerability reporting
#    - GitHub App and OIDC permissions
```

[Back to top](#top)

## Usage

Use this README as the responsibility map for repo-side governance work.

1. **Inspect before editing.** Confirm the live tree, not just remembered structure or historical discussion.
2. **Map the change to trust impact.** Ask whether the edit changes intake, ownership, merge-blocking logic, disclosure flow, dependency automation, watcher behavior, release evidence, or correction posture.
3. **Keep trust-bearing automation review-bearing.** KFM doctrine prefers visible deltas, attached evidence, and reversible changes whenever automation could change trust state.
4. **Update adjacent docs in the same change stream.** If review routing, disclosure posture, automation lanes, watcher rules, dependency policy, or pipeline-facing gate behavior change, the corresponding README, template, or runbook should travel with the same PR.

### Gatehouse vs. neighboring execution lanes

| Surface | Canonical home | `.github` role |
| --- | --- | --- |
| Review routing and contributor intake | `.github/` | own it directly |
| Workflow orchestration and dependency policy | `.github/` | own it directly when checked in |
| Runtime code and package logic | `../apps/`, `../packages/` | gate via review, CI, and policy |
| Pipeline code and long-running watchers | `../pipelines/` or other owning runtime paths | gate via review, docs, and future workflow/promotion surfaces |
| Canonical data, contracts, policy bundles, receipts | `../data/`, `../contracts/`, `../schemas/`, `../policy/` | validate and route, but do not replace |

### Build, watch, deploy, and promote are different moves

| Move | What changes | Why `.github/` cares |
| --- | --- | --- |
| **Build** | a versioned artifact or proof object exists | repo automation, metadata guards, and attest/review surfaces often begin here |
| **Watch** | a derived monitoring surface detects change and emits a candidate | watcher guidance must remain emit-only, evidence-backed, and PR/review-bearing |
| **Deploy** | runtime placement or hosted execution changes | environment approvals, rollback readiness, and post-deploy checks may be triggered here |
| **Promote** | trust state changes from candidate to releasable or publishable | policy, docs, review, and proof obligations become mandatory here |

[Back to top](#top)

## Diagram

```mermaid
flowchart LR
    A[Contributor / maintainer / automation / watcher] --> B[.github gatehouse]

    subgraph G["Last verified .github surfaces"]
      G1["README.md<br/>responsibility map"]
      G2["CODEOWNERS<br/>review boundary"]
      G3["PULL_REQUEST_TEMPLATE.md<br/>merge-readiness structure"]
      G4["ISSUE_TEMPLATE/<br/>README + config path"]
      G5["actions/<br/>local action scaffolding"]
      G6["watchers/<br/>README-only emit-only lane"]
      G7["workflows/<br/>README-only docs lane"]
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
    G6 --> J[Derived change candidate<br/>with evidence]
    G8 --> K[Automated dependency PRs]

    H --> M{Trust state can widen?}
    I --> M
    J --> M
    K --> M

    M -->|yes| N[Policy / validation / proof / human review]
    M -->|no| O[Clarify / revise / redirect]

    N --> P[Merge / correction / follow-up]

    subgraph R["Adjacent root execution neighbors"]
      R1["pipelines/<br/>soils/gssurgo-ks"]
      R2["pipelines/<br/>wbd-huc12-watcher"]
    end

    P -->|"gates changes without absorbing runtime ownership"| R1
    P -->|"gates changes without absorbing runtime ownership"| R2
    P -->|"platform settings still need direct verification"| Q[Rulesets / required checks / environments]
```

[Back to top](#top)

## Control surfaces & reference tables

### Last verified control surfaces

| Surface | Last verified status | Primary role | Why it is sensitive |
| --- | --- | --- | --- |
| [`./README.md`](./README.md) | **CONFIRMED** | repo-side responsibility map | drift here blurs the control plane |
| [`./CODEOWNERS`](./CODEOWNERS) | **CONFIRMED** | executable review routing | changes approval scope and separation of duty |
| [`./PULL_REQUEST_TEMPLATE.md`](./PULL_REQUEST_TEMPLATE.md) | **CONFIRMED** | structured PR intake with truth labels, evidence links, doctrine impact, and validation structure | weak PR prompts degrade review quality |
| [`./ISSUE_TEMPLATE/README.md`](./ISSUE_TEMPLATE/README.md) | **CONFIRMED** | issue-intake guidance | contributor intake should stay governed rather than improvised |
| [`./ISSUE_TEMPLATE/config.yml`](./ISSUE_TEMPLATE/config.yml) | **CONFIRMED documented file presence** | issue chooser config path | was an empty placeholder in the last verified snapshot |
| [`./actions/`](./actions/) | **CONFIRMED** | repo-local reusable GitHub Actions scaffolding | local actions can hide trust-bearing behavior if undocumented |
| [`./actions/action.yml`](./actions/action.yml) | **CONFIRMED documented file presence** | root action manifest path | was an empty placeholder in the last verified snapshot |
| [`./watchers/README.md`](./watchers/README.md) | **CONFIRMED** | watcher lane with emit-only, derived-surface rules | watcher surfaces must not bypass governed publication |
| [`./workflows/README.md`](./workflows/README.md) | **CONFIRMED** | workflow documentation lane | docs can drift away from real workflow inventory |
| `./workflows/*.yml|*.yaml` | **CONFIRMED last verified absence** | checked-in workflow definitions | none were documented in the last verified snapshot |
| [`./SECURITY.md`](./SECURITY.md) | **CONFIRMED** | repo-local disclosure-policy surface | public disclosure posture needs one stable path |
| [`../SECURITY.md`](../SECURITY.md) | **CONFIRMED** | second checked-in security-policy path | canonicalization remains unresolved until aligned or delegated |
| [`./dependabot.yml`](./dependabot.yml) | **CONFIRMED** | dependency-update automation policy | bot-driven dependency PRs still affect trust and delivery posture |
| GitHub rulesets / required checks / environment approvals | **UNKNOWN** in this README | platform enforcement | cannot be proven from checked-in files alone |

### Last verified root execution neighbors

| Path | Observed state | Why `.github` still cares |
| --- | --- | --- |
| [`../pipelines/`](../pipelines/) | root execution lane family with visible `soils/gssurgo-ks/` and `wbd-huc12-watcher` subdirectories in the last verified snapshot | pipeline-facing changes still traverse `CODEOWNERS`, PR templates, disclosure posture, and any future workflow or promotion gates |

### Last verified dependency-update coverage

| Ecosystem | Paths | Schedule (UTC) |
| --- | --- | --- |
| `docker` | `/`, `/apps/*`, `/packages/*`, `/infra/*` | weekly · Monday · 06:30 |
| `npm` | `/`, `/apps/*`, `/packages/*` | weekly · Tuesday · 06:00 |
| `pip` | `/`, `/apps/*`, `/packages/*` | weekly · Wednesday · 06:00 |
| `cargo` | `/`, `/apps/*`, `/packages/*` | weekly · Thursday · 06:00 |

> [!NOTE]
> The last verified `dependabot.yml` snapshot did **not** name `/pipelines/*`. That is a real config fact from the documented snapshot, not proof that pipeline lanes definitely require Dependabot coverage today. Review and extend the config only when supported manifests in `../pipelines/` actually need that coverage.

[Back to top](#top)

## Task list / definition of done

- [ ] The live checkout matches the snapshot documented here, including `watchers/`, or this README was updated in the same PR.
- [ ] `.github/README.md`, `.github/CODEOWNERS`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/SECURITY.md`, `.github/dependabot.yml`, `.github/watchers/README.md`, and `.github/workflows/README.md` were re-read in the same branch being merged.
- [ ] `ISSUE_TEMPLATE/` still contains exactly the files documented here, or this README was updated in the same PR.
- [ ] `actions/` still contains the documented subdirectories, or this README was updated in the same PR.
- [ ] `watchers/` was checked for any new files or jobs beyond `README.md`, or this README was updated in the same PR.
- [ ] `workflows/` was checked for actual `.yml` / `.yaml` files before any workflow claim was merged.
- [ ] Any empty placeholders (`ISSUE_TEMPLATE/config.yml`, `actions/action.yml`) remain intentional and documented, or they were replaced with real content.
- [ ] Root repo context still includes `pipelines/`, or the broader snapshot above was updated in the same PR.
- [ ] If dependency-bearing files were added or changed under `../pipelines/`, checked-in `dependabot.yml` coverage was reviewed and either extended or intentionally left unchanged with explanation.
- [ ] `CODEOWNERS` coverage still matches the review expectations described here.
- [ ] `.github/SECURITY.md` and `../SECURITY.md` are either text-aligned or one clearly delegates to the other.
- [ ] Branch protection, rulesets, required checks, environment approvals, and private-reporting settings were verified in GitHub settings when relevant.
- [ ] **UNKNOWN** items remain explicit instead of being rewritten as certainty.
- [ ] Docs, templates, automation, and watcher-boundary changes that affect trust state move through the same review stream.

[Back to top](#top)

## FAQ

### Does this README prove that checked-in workflow YAML files currently exist under `.github/workflows/`?

No. The last verified snapshot documented `./workflows/README.md`, but did **not** document checked-in `.yml` or `.yaml` files there. Recheck the live branch before making workflow inventory claims.

### What is `.github/watchers/` in the documented snapshot?

`./watchers/README.md` only. Its documented guidance describes watchers as **derived**, **fail-closed**, and **emit-only** monitoring surfaces that must open a governed review path instead of publishing directly.

### Does the documented snapshot expose issue-form templates?

Not beyond the issue-template directory itself. The last verified snapshot documented `README.md` plus an empty `config.yml`, but no issue-form or Markdown template files there.

### Who owns `.github/` in this README?

The documented baseline assigns the global fallback to `@bartytime4life` and explicitly assigns `/.github/` plus `/.github/CODEOWNERS` to `@bartytime4life`. Treat that as snapshot evidence until the live branch is rechecked.

### Does the documented snapshot expose pipeline lanes outside `.github/`?

Yes. The last verified root snapshot included `pipelines/`, with visible `soils/gssurgo-ks/` and `wbd-huc12-watcher` subdirectories. `.github` should gate those lanes, not absorb them.

### Does the documented `dependabot.yml` explicitly name `pipelines/*`?

No. The last verified globs named `/`, `/apps/*`, `/packages/*`, and `/infra/*` for Docker, and `/`, `/apps/*`, `/packages/*` for npm, pip, and cargo. `pipelines/*` was not explicitly named.

### Is the public security-policy path resolved?

Not yet. The documented baseline treated `.github/SECURITY.md` as the repo-local disclosure surface, but also preserved the unresolved relationship with `../SECURITY.md`. Those two files should be aligned or delegated cleanly.

### What remains unverified after this revision?

GitHub private-reporting fallback channels beyond what checked-in docs say, protected-branch rules, required checks, rulesets, environment approvals, GitHub App permissions, OIDC trust relationships, unpublished workflow YAMLs, and any non-public release or deployment controls.

[Back to top](#top)

## Appendix

<details>
<summary><strong>Last verified snapshot notes</strong></summary>

### `.github/` documented in the last verified snapshot

- `ISSUE_TEMPLATE/` existed with `README.md` and empty `config.yml`
- `actions/` existed with five named action directories, `src/`, `README.md`, and empty `action.yml`
- `watchers/` existed with `README.md` only
- `workflows/` existed with `README.md` only
- `CODEOWNERS`, `PULL_REQUEST_TEMPLATE.md`, `README.md`, `SECURITY.md`, and `dependabot.yml` were checked in

### Adjacent root paths documented in the same snapshot

- root directories: `apps/`, `brand/`, `configs/`, `contracts/`, `data/`, `docs/`, `examples/`, `infra/`, `migrations/`, `packages/`, `pipelines/`, `policy/`, `schemas/`, `scripts/`, `tests/`, `tools/`
- visible pipeline lanes: `pipelines/soils/gssurgo-ks/` and `pipelines/wbd-huc12-watcher/`
- repo-root docs: `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `LICENSE`, `README.md`, `SECURITY.md`

### Practical reading rule

This directory is strongest as a **repo-side control map**, **local automation scaffold**, and **review-bearing watcher boundary**. The biggest gaps the documented snapshot leaves open are the absence of checked-in workflow YAMLs under `.github/workflows/`, the unresolved duplication of the public security-policy path, and the fact that `dependabot.yml` still followed an older root-directory taxonomy that did not explicitly name `/pipelines/*`.

</details>

<details>
<summary><strong>Historical signal, not present-tree proof</strong></summary>

`./workflows/README.md` documented prior GitHub Actions activity and named deleted workflow files such as:

- `verify-docs.yml`
- `verify-contracts-and-policy.yml`
- `verify-runtime.yml`
- `verify-tests-and-reproducibility.yml`
- `release-evidence.yml`
- `promote-and-reconcile.yml`

That is useful context for recovery, archaeology, or reconstitution work, but it is **not** the same as current checked-in workflow inventory.

</details>

<details>
<summary><strong>Open verification backlog</strong></summary>

1. Verify whether watcher logic exists elsewhere in the repo outside the docs-only `.github/watchers/` scaffold.
2. Confirm whether `ISSUE_TEMPLATE/config.yml` and `actions/action.yml` are intentional empty placeholders or incomplete scaffolding.
3. Choose and enforce one canonical public security-policy path, or explicitly delegate from one file to the other.
4. Recheck `CODEOWNERS` granularity if ownership expands beyond the current broad single-owner baseline.
5. Export or inspect GitHub rulesets, required checks, environment approvals, app permissions, OIDC trust bindings, and private vulnerability-reporting settings.
6. Reconcile `.github/README.md`, `.github/ISSUE_TEMPLATE/README.md`, `.github/actions/README.md`, `.github/workflows/README.md`, `.github/watchers/README.md`, root `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, and both security-policy files so they describe the same current control-plane reality.
7. Retire **UNKNOWN** items only when direct repo or platform evidence is attached to the same PR.
8. Review whether `../pipelines/` needs explicit Dependabot directory coverage once supported manifests there are confirmed.

</details>

[Back to top](#top)
