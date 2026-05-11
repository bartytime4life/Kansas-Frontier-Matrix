<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/github-root-readme
title: .github/ — Repository Governance Hooks
type: standard
version: v1
status: draft
owners: Docs steward + Release / CI owners (TBD — see CODEOWNERS)
created: 2026-05-10
updated: 2026-05-10
policy_label: public
related:
  - ../README.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/doctrine/trust-membrane.md
  - ../docs/governance/
  - ../docs/runbooks/
  - ../control_plane/
  - ../release/
tags: [kfm, governance, ci, github]
notes:
  - Repository not mounted in authoring session; concrete file presence marked PROPOSED / NEEDS VERIFICATION.
  - Replaces any prior ad-hoc landing notes for .github/.
[/KFM_META_BLOCK_V2] -->

# `.github/` — Repository Governance Hooks

> GitHub-side glue for KFM: workflows, templates, CODEOWNERS, and policy hooks that make the governed, evidence-first, lifecycle-aware repo enforceable on every PR.

<p align="left">
  <a href="../README.md"><img alt="Project: Kansas Frontier Matrix" src="https://img.shields.io/badge/project-Kansas%20Frontier%20Matrix-1f6feb"></a>
  <a href="../docs/doctrine/directory-rules.md"><img alt="Doctrine: Directory Rules" src="https://img.shields.io/badge/doctrine-directory--rules-3fb950"></a>
  <a href="#status"><img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow"></a>
  <a href="#review-burden"><img alt="Authority: canonical root" src="https://img.shields.io/badge/authority-canonical-blueviolet"></a>
  <!-- TODO: replace once workflow names + branch are NEEDS VERIFICATION-cleared -->
  <a href="#"><img alt="CI: TODO" src="https://img.shields.io/badge/CI-TODO-lightgrey"></a>
  <a href="#"><img alt="CodeQL: TODO" src="https://img.shields.io/badge/CodeQL-TODO-lightgrey"></a>
  <a href="../LICENSE"><img alt="License" src="https://img.shields.io/badge/license-see%20LICENSE-informational"></a>
</p>

**Quick jump:** [Purpose](#purpose) · [Authority level](#authority-level) · [Status](#status) · [What belongs here](#what-belongs-here) · [What does NOT belong here](#what-does-not-belong-here) · [Directory tree](#directory-tree) · [Diagram](#diagram) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review burden](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Open verification](#open-verification) · [Last reviewed](#last-reviewed)

---

## Purpose

`.github/` is the **GitHub-side enforcement surface** for KFM doctrine. It carries the workflows, issue/PR templates, CODEOWNERS routing, and policy hooks that turn governance rules — lifecycle invariant, trust membrane, cite-or-abstain, schema-home, separation of release duties — into checks GitHub actually runs on every push and PR.

It does not store doctrine, decisions, or trust-bearing artifacts. Those live in [`docs/`](../docs/), [`control_plane/`](../control_plane/), [`policy/`](../policy/), and [`release/`](../release/). `.github/` exists to make those layers **operationally visible** at the platform boundary.

[Back to top ↑](#github--repository-governance-hooks)

---

## Authority level

**Canonical root.** Per [Directory Rules §5](../docs/doctrine/directory-rules.md), `.github/` is listed in the canonical root tree alongside `docs/`, `contracts/`, `schemas/`, `policy/`, `tests/`, `release/`, and the rest. Its responsibility — "workflows, issue/PR templates, governance hooks" — is recognized by GitHub and cannot be relocated.

`.github/` is **implementation-bearing**: its files run code (Actions) and route review burden (CODEOWNERS, templates). It is **not** the authority for what *should* be enforced — that comes from `docs/doctrine/`, `policy/`, and `contracts/`. `.github/` is where those rules are *wired up*.

| Aspect | Position |
|---|---|
| Root status | Canonical (Directory Rules §5) |
| Authority kind | Implementation-bearing (executes; does not decide) |
| Lifecycle phase | N/A — operates across phases via validators and gates |
| Trust posture | Public-readable; protected from unreviewed self-modification |
| Mirrors / aliases | None permitted |

[Back to top ↑](#github--repository-governance-hooks)

---

## Status

**Draft.** This README documents the *intended* structure and contract for `.github/`. Concrete file presence (specific workflow names, CODEOWNERS entries, configured branch protections, template inventory) is **NEEDS VERIFICATION** until inspected against the live repository — see [Open verification](#open-verification).

Doctrinal claims (what belongs, what doesn't, who reviews) are CONFIRMED against [Directory Rules](../docs/doctrine/directory-rules.md). Implementation depth claims are bounded accordingly.

[Back to top ↑](#github--repository-governance-hooks)

---

## What belongs here

Files in `.github/` MUST serve one of these roles. The list is **closed** — additions require an entry under `docs/registers/DRIFT_REGISTER.md` or an ADR.

| Family | Examples (PROPOSED layout) | Role |
|---|---|---|
| **CI / validation workflows** | `workflows/ci.yml`, `workflows/schema-validate.yml`, `workflows/policy-check.yml`, `workflows/link-check.yml` | Run validators from [`tools/`](../tools/) and [`policy/`](../policy/) on PR. Block merges that violate doctrine. |
| **Release / signing workflows** | `workflows/release-dry-run.yml`, `workflows/release-publish.yml`, `workflows/sign-artifacts.yml` | Drive the release decision flow from [`release/`](../release/). Sign artifacts (DSSE / Sigstore) per `release/signatures/`. |
| **Security workflows** | `workflows/codeql.yml`, `workflows/dependency-review.yml`, `workflows/secret-scan.yml` | Static analysis, dependency review, secret scanning. |
| **Maintenance workflows** | `workflows/stale.yml`, `workflows/auto-label.yml`, `workflows/lock-threads.yml` | Repo hygiene. Non-trust-bearing. |
| **Reusable workflows** | `workflows/_validate.yml`, `workflows/_evidence-gate.yml` | Composed by other workflows; clearly prefixed and documented. |
| **Issue templates** | `ISSUE_TEMPLATE/bug.yml`, `ISSUE_TEMPLATE/data-correction.yml`, `ISSUE_TEMPLATE/sensitivity-report.yml`, `ISSUE_TEMPLATE/source-proposal.yml`, `ISSUE_TEMPLATE/config.yml` | Route incoming reports into the correction / sensitivity / source-admission paths. |
| **PR template** | `PULL_REQUEST_TEMPLATE.md` | Enforce the §4 placement protocol — every PR cites the Directory Rules section that justifies new/moved paths. |
| **Discussion templates** | `DISCUSSION_TEMPLATE/` | Optional. Same hygiene as issue templates. |
| **Routing & policy hooks** | `CODEOWNERS`, `dependabot.yml`, `labeler.yml`, `release-drafter.yml`, `auto_assign.yml` | Code ownership, dependency cadence, automatic labels. Owners listed here MUST be real and reviewable. |
| **Funding / community** | `FUNDING.yml` (optional) | If KFM accepts funding/sponsorship; otherwise omit. |

> [!IMPORTANT]
> Every workflow that gates a merge MUST call a validator from [`tools/`](../tools/) or a policy bundle from [`policy/`](../policy/). Workflows MUST NOT inline KFM doctrine, define schemas, or re-express policy. They invoke; they do not author.

[Back to top ↑](#github--repository-governance-hooks)

---

## What does NOT belong here

These are common drift attractors. The "do not put X here" list is as load-bearing as the inclusion list — see [Directory Rules §15](../docs/doctrine/directory-rules.md).

| Do NOT place here | Belongs in | Why |
|---|---|---|
| Doctrine, policy doctrine, or ADRs | [`docs/doctrine/`](../docs/), [`docs/adr/`](../docs/) | Workflows enforce; doctrine decides. Collapsing them hides authority. |
| Schemas (JSON Schema, JSON-LD context) | [`schemas/contracts/v1/`](../schemas/) | Schema-home rule (ADR-0001). |
| Contract definitions (object meaning) | [`contracts/`](../contracts/) | Meaning is authored, not CI-side. |
| Policy bundles (Rego/OPA, allow/deny logic) | [`policy/`](../policy/) | Policy is canonical; `.github/` only *invokes* it. |
| Validators, generators, builders | [`tools/`](../tools/) | Long-lived, trust-bearing logic. Workflows call them; do not embed them. |
| Receipts, proofs, evidence bundles | [`data/receipts/`](../data/), [`data/proofs/`](../data/) | Trust artifacts belong on the lifecycle plane, not the CI plane. |
| Release manifests, promotion decisions, rollback cards | [`release/`](../release/) | Release decisions are governed objects, not workflow outputs. |
| Secrets, tokens, real credentials | GitHub Actions secrets / external secret store | Never in repo files. See [Directory Rules §10.3](../docs/doctrine/directory-rules.md). |
| Site / explorer UI assets | [`apps/explorer-web/`](../apps/), [`packages/ui/`](../packages/) | UI is its own canonical lane. |
| Lifecycle data of any kind | [`data/`](../data/) | `.github/` never holds RAW / WORK / PROCESSED / PUBLISHED bytes. |
| Generated reports for human reading | [`docs/reports/`](../docs/) or [`artifacts/qa/`](../artifacts/) | CI may *emit* into those; the report itself does not live under `.github/`. |
| Parallel CODEOWNERS, parallel templates | Root `CODEOWNERS` *or* `.github/CODEOWNERS` — pick one | Two homes = drift. See [Directory Rules §5](../docs/doctrine/directory-rules.md) note on CODEOWNERS placement. |

> [!CAUTION]
> A workflow that writes to `data/processed/`, `data/catalog/`, `data/published/`, or `release/` outside an approved promotion or release flow violates the **watcher-as-non-publisher** invariant. CI can *propose* — it does not *publish*.

[Back to top ↑](#github--repository-governance-hooks)

---

## Directory tree

The tree below is **PROPOSED** — it expresses the doctrinally-correct shape for `.github/` under KFM. The current repository's actual contents are **NEEDS VERIFICATION**; treat divergence as a [`docs/registers/DRIFT_REGISTER.md`](../docs/) entry, not as new authority.

```text
.github/
├── README.md                       # this file
├── CODEOWNERS                      # OR at repo root; never both
├── PULL_REQUEST_TEMPLATE.md
├── FUNDING.yml                     # optional
├── dependabot.yml
├── labeler.yml                     # optional
├── release-drafter.yml             # optional
│
├── ISSUE_TEMPLATE/
│   ├── config.yml                  # disables blank issues; routes to discussions
│   ├── bug.yml
│   ├── data-correction.yml         # public correction path (CorrectionNotice intake)
│   ├── sensitivity-report.yml     # rights / sovereignty / sensitivity intake
│   ├── source-proposal.yml         # new source admission request
│   └── doc-fix.yml
│
├── DISCUSSION_TEMPLATE/            # optional
│
└── workflows/
    ├── ci.yml                      # build + lint + unit tests
    ├── schema-validate.yml         # validates schemas/ and fixtures/
    ├── contract-check.yml          # cross-checks contracts/ ↔ schemas/
    ├── policy-check.yml            # runs policy/ bundles + fixtures
    ├── directory-rules-check.yml   # enforces placement protocol on changed paths
    ├── link-check.yml              # doc link health
    ├── codeql.yml                  # static analysis
    ├── dependency-review.yml
    ├── secret-scan.yml
    ├── release-dry-run.yml         # exercises release/ decision flow
    ├── release-publish.yml         # gated; signs artifacts; updates release/
    ├── sign-artifacts.yml          # DSSE / Sigstore signing
    ├── stale.yml
    └── _validate.yml               # reusable composite
```

> [!NOTE]
> Filenames above are **illustrative** and follow common GitHub Actions conventions. They are not guaranteed to match the live repo. Reconcile via the validator described in [Validation](#validation).

[Back to top ↑](#github--repository-governance-hooks)

---

## Diagram

How `.github/` connects to the rest of the repo. Arrows point in the direction of *invocation* (left side **calls into** right side); `.github/` is a thin wiring layer over canonical authorities.

```mermaid
flowchart LR
    subgraph GH[".github/"]
        WF[workflows/]
        TPL[ISSUE_TEMPLATE/<br/>PULL_REQUEST_TEMPLATE.md]
        OWN[CODEOWNERS]
    end

    subgraph CANON["Canonical authorities"]
        DOC[docs/doctrine/<br/>docs/adr/]
        CP[control_plane/]
        CON[contracts/]
        SCH[schemas/]
        POL[policy/]
        TST[tests/ + fixtures/]
        TOOL[tools/validators/<br/>tools/generators/]
        REL[release/]
    end

    subgraph LIFE["Lifecycle / proofs"]
        DATA[data/raw → work → processed →<br/>catalog → published]
        RECEIPTS[data/receipts/]
        PROOFS[data/proofs/]
    end

    WF -- "invokes" --> TOOL
    WF -- "invokes" --> POL
    WF -- "runs" --> TST
    WF -- "validates shape" --> SCH
    WF -- "cross-checks meaning" --> CON
    WF -- "exercises decision flow" --> REL
    WF -- "writes process memory" --> RECEIPTS
    WF -- "never writes to" -.-> DATA
    WF -- "never authors" -.-> DOC

    TPL -- "routes intake into" --> REL
    TPL -- "routes intake into" --> POL
    TPL -- "routes intake into" --> CP

    OWN -- "routes review burden to" --> DOC
    OWN -- "routes review burden to" --> POL
    OWN -- "routes review burden to" --> REL

    classDef gh fill:#e7f1ff,stroke:#1f6feb,color:#0b1f3a;
    classDef canon fill:#eafbe7,stroke:#3fb950,color:#0b1f3a;
    classDef life fill:#fff4e5,stroke:#d29922,color:#0b1f3a;
    class GH,WF,TPL,OWN gh
    class CANON,DOC,CP,CON,SCH,POL,TST,TOOL,REL canon
    class LIFE,DATA,RECEIPTS,PROOFS life
```

[Back to top ↑](#github--repository-governance-hooks)

---

## Inputs

What feeds `.github/`:

- **Doctrine changes** in [`docs/doctrine/`](../docs/) — when an invariant changes, a workflow or template here usually changes too.
- **New / updated validators** in [`tools/validators/`](../tools/) — workflows wrap them.
- **Policy bundles** in [`policy/bundles/`](../policy/) and fixtures in [`policy/fixtures/`](../policy/) — invoked from `policy-check.yml`.
- **Schema changes** in [`schemas/contracts/v1/`](../schemas/) and fixtures in [`fixtures/`](../fixtures/) — invoked from `schema-validate.yml`.
- **Release flow changes** in [`release/`](../release/) — invoked from `release-dry-run.yml` and `release-publish.yml`.
- **CODEOWNERS routing intent** from [`docs/governance/`](../docs/) — separation-of-duties rules become `CODEOWNERS` lines.

[Back to top ↑](#github--repository-governance-hooks)

---

## Outputs

What `.github/` emits:

- **Check runs and statuses** on PRs (blocking and informational).
- **Generated artifacts uploaded to Actions** (logs, test reports, validator outputs) — kept in CI, *not* persisted into the repo as trust content. Trust-bearing receipts land in `data/receipts/` via the relevant pipeline, not via the Actions UI.
- **Release flow signals** that drive entries in [`release/`](../release/) (manifests, promotion decisions, rollback cards, signatures). The decisions themselves are authored elsewhere; `.github/` runs the gates that let them land.
- **Labels and routing** on issues/PRs.
- **Review assignment** via CODEOWNERS.

> [!IMPORTANT]
> A green CI run is **not** proof of release-readiness. Release readiness is a `release/promotion_decisions/` artifact governed by [Directory Rules §9.2](../docs/doctrine/directory-rules.md). CI proves enforceability of constraints; it does not author release state.

[Back to top ↑](#github--repository-governance-hooks)

---

## Validation

How `.github/` is itself checked:

| Check | Mechanism | Status |
|---|---|---|
| Workflow syntax & schema | `actionlint` (or equivalent) invoked from `ci.yml` | PROPOSED |
| Reusable-workflow contract | Lint that `_*.yml` files declare `workflow_call` and inputs | PROPOSED |
| CODEOWNERS validity | GitHub's built-in validator + a check that every path pattern has a real owner | PROPOSED |
| No duplicate CODEOWNERS homes | Validator: root `CODEOWNERS` XOR `.github/CODEOWNERS` (not both) | PROPOSED |
| Template completeness | Lint that every `ISSUE_TEMPLATE/*.yml` carries a `labels:` block and an owner | PROPOSED |
| Placement protocol | `directory-rules-check.yml` runs the §4 placement protocol on every changed path; PR description MUST cite the rule | PROPOSED |
| Pinned action SHAs | Lint that third-party actions are pinned to a commit SHA, not a floating tag | PROPOSED |
| No secrets in repo | `secret-scan.yml` (and pre-commit, where present) | PROPOSED |
| Drift detection | Missing-README scan opens entries in [`docs/registers/DRIFT_REGISTER.md`](../docs/) | PROPOSED |

> [!WARNING]
> Until the rows above are confirmed against the live repo, do not cite "CI enforces X" as fact. Cite the doctrine that *requires* X, and mark the wiring NEEDS VERIFICATION.

[Back to top ↑](#github--repository-governance-hooks)

---

## Review burden

Changes inside `.github/` are policy-significant. Default routing:

| Change | Required reviewers |
|---|---|
| New or modified merge-gating workflow | Docs steward + CI/Release owner + owner of the invoked validator/policy |
| `CODEOWNERS` change | Docs steward + at least one affected subsystem owner |
| New issue template touching corrections, sensitivity, or source admission | Docs steward + Policy owner + Release owner |
| `PULL_REQUEST_TEMPLATE.md` change | Docs steward (because it encodes the §4 placement protocol) |
| Release workflow change (`release-*.yml`, `sign-artifacts.yml`) | Release owner + Security owner + Docs steward (separation of duties per [Directory Rules §0](../docs/doctrine/directory-rules.md)) |
| Security workflow change (`codeql.yml`, `secret-scan.yml`, `dependency-review.yml`) | Security owner + Docs steward |
| Routine maintenance (`stale.yml`, labels) | Single reviewer acceptable |

Owners are routed via [`CODEOWNERS`](./CODEOWNERS). The current list is **NEEDS VERIFICATION** — see [Open verification](#open-verification).

> [!IMPORTANT]
> **Separation of duties.** A single reviewer MUST NOT approve a change that simultaneously (a) authors a workflow gate and (b) publishes the artifact that workflow would gate. This is the GitHub-side expression of the release-duties separation called out in [Directory Rules §0](../docs/doctrine/directory-rules.md).

[Back to top ↑](#github--repository-governance-hooks)

---

## Related folders

| Folder | Relationship |
|---|---|
| [`../docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) | Authority for what `.github/` exists to enforce. |
| [`../docs/doctrine/`](../docs/) | Source of all invariants the workflows wrap. |
| [`../docs/adr/`](../docs/) | ADRs that change what `.github/` must enforce (e.g., schema-home rule). |
| [`../docs/governance/`](../docs/) | Roles, review burden, separation of duties — sourced into CODEOWNERS. |
| [`../docs/runbooks/`](../docs/) | Incident response procedures for failed releases, leaked secrets, broken gates. |
| [`../control_plane/`](../control_plane/) | Machine-readable registers that workflows may read (e.g., `deprecation_register.yaml`). |
| [`../contracts/`](../contracts/) | Object meaning — checked by `contract-check.yml`. |
| [`../schemas/`](../schemas/) | Object shape — validated by `schema-validate.yml`. |
| [`../policy/`](../policy/) | Allow/deny/restrict/abstain bundles — invoked by `policy-check.yml`. |
| [`../tools/`](../tools/), [`../tools/validators/`](../tools/) | Long-lived validators — wrapped by workflows. |
| [`../tests/`](../tests/), [`../fixtures/`](../fixtures/) | Enforceability proof — run by `ci.yml`. |
| [`../release/`](../release/) | Release decisions — exercised by `release-dry-run.yml`, gated by `release-publish.yml`. |
| [`../data/receipts/`](../data/) | Where pipelines write process memory — `.github/` does not write here directly. |

[Back to top ↑](#github--repository-governance-hooks)

---

## ADRs

ADRs that materially shape what `.github/` enforces:

| ADR | What it requires of `.github/` |
|---|---|
| **ADR-0001 — Schema home** ([Directory Rules §6.4](../docs/doctrine/directory-rules.md)) | `schema-validate.yml` MUST validate `schemas/contracts/v1/...`. If both `contracts/<domain>/<x>.schema.json` and the canonical home are populated, the workflow MUST fail with a drift-register pointer. |
| **ADR for any §2.4 change** ([Directory Rules §2.4](../docs/doctrine/directory-rules.md)) | Adding/renaming a canonical root, splitting a lifecycle phase, or creating a parallel home triggers a corresponding update to `directory-rules-check.yml`. |
| **Future ADRs** | Listed here as they land. Each ADR that changes invariants MUST include a checklist item: "Does this require a `.github/` workflow or template change? If yes, link the PR." |

> [!NOTE]
> A complete ADR inventory lives in [`../docs/adr/`](../docs/). This table is the subset whose enforcement surface intersects `.github/`.

[Back to top ↑](#github--repository-governance-hooks)

---

## Open verification

Items to resolve against the live repository. Track in [`docs/registers/VERIFICATION_BACKLOG.md`](../docs/) and close with PRs that update this README.

- [ ] **NEEDS VERIFICATION** — Inventory of files actually present under `.github/` (workflows, templates, CODEOWNERS, dependabot, FUNDING).
- [ ] **NEEDS VERIFICATION** — Whether `CODEOWNERS` lives at repo root, under `.github/`, or both. If both, open a drift entry.
- [ ] **NEEDS VERIFICATION** — Which workflows are configured as **required** in branch protection on the default branch.
- [ ] **NEEDS VERIFICATION** — Whether `directory-rules-check.yml` (or equivalent) exists; if not, it is **PROPOSED**.
- [ ] **NEEDS VERIFICATION** — Whether third-party actions are pinned to commit SHAs.
- [ ] **NEEDS VERIFICATION** — Real owner names for the badges and review table above (currently placeholders).
- [ ] **NEEDS VERIFICATION** — Whether `release-publish.yml` actually invokes the `release/` decision flow and signs artifacts via Sigstore/DSSE.
- [ ] **NEEDS VERIFICATION** — Whether `ISSUE_TEMPLATE/sensitivity-report.yml` (or equivalent) exists; if not, **PROPOSED** as the intake path for rights / sovereignty / sensitivity reports.
- [ ] **PROPOSED** — Adopt the workflow naming scheme in [Directory tree](#directory-tree); if the repo uses different names, update either the repo or this README and pick one.
- [ ] **PROPOSED** — Adopt a `_validate.yml` reusable-workflow pattern so individual gates compose instead of duplicating setup.

[Back to top ↑](#github--repository-governance-hooks)

---

## Last reviewed

`2026-05-10` — initial draft against [Directory Rules](../docs/doctrine/directory-rules.md). Re-review trigger: any §2.4 change in Directory Rules, any new workflow added, or 6 months elapsed — whichever comes first.

<sub>This README satisfies the canonical-root README contract in <a href="../docs/doctrine/directory-rules.md">Directory Rules §15</a>. Sections marked PROPOSED / NEEDS VERIFICATION must be closed before this document moves from <code>draft</code> to <code>published</code>.</sub>
