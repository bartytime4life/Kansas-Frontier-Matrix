<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS-VERIFICATION-UUID>
title: dashboards
type: standard
version: v1
status: draft
owners: @bartytime4life
created: <NEEDS-VERIFICATION-YYYY-MM-DD>
updated: <NEEDS-VERIFICATION-YYYY-MM-DD>
policy_label: <NEEDS-VERIFICATION>
related: [infra/README.md, infra/monitoring/README.md, .github/workflows/README.md, tests/README.md, policy/README.md, contracts/README.md, schemas/README.md]
tags: [kfm, infra, dashboards, observability]
notes: [Target path inferred from uploaded draft; current public tree confirms a README-only directory; doc_id, dates, and policy label still need verification]
[/KFM_META_BLOCK_V2] -->

# dashboards

Operator-facing dashboards and drill-through observability definitions for Kansas Frontier Matrix.

> **Status:** experimental  
> **Owners:** `@bartytime4life` (current public `CODEOWNERS` coverage for `/infra/`; narrower dashboard-only ownership is **NEEDS VERIFICATION**)  
> **Path:** `infra/dashboards/README.md`  
> **Repo fit:** dashboard-definition lane under [`../README.md`](../README.md); upstream from repo identity in [`../../README.md`](../../README.md); lateral to [`../monitoring/README.md`](../monitoring/README.md), [`../local/`](../local/), [`../compose/`](../compose/), [`../hosted/`](../hosted/), and [`../systemd-or-compose/`](../systemd-or-compose/); downstream into review and governance surfaces such as [`../../.github/workflows/README.md`](../../.github/workflows/README.md), [`../../tests/README.md`](../../tests/README.md), [`../../policy/README.md`](../../policy/README.md), [`../../contracts/README.md`](../../contracts/README.md), and [`../../schemas/README.md`](../../schemas/README.md)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current verified snapshot](#current-verified-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Operating tables](#operating-tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

![status: experimental](https://img.shields.io/badge/status-experimental-f59e0b)
![owners: @bartytime4life](https://img.shields.io/badge/owners-%40bartytime4life-1f6feb)
![branch: main](https://img.shields.io/badge/branch-main-0a7d5a)
![repo tree: public main](https://img.shields.io/badge/repo%20tree-public%20main-6f42c1)
![surface: infra/dashboards](https://img.shields.io/badge/surface-infra%2Fdashboards-0a7ea4)
![role: operator-facing](https://img.shields.io/badge/role-operator--facing-5b6b7a)
![truth: bounded](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20INFERRED%20%7C%20PROPOSED-2ea043)

> [!IMPORTANT]
> Current public `main` shows `infra/dashboards/` as a **README-only** lane. Treat dashboard provisioning details, live datasources, alert-rule ownership, screenshots, and active operator workflows as **UNKNOWN** or **NEEDS VERIFICATION** until the checked-out branch and runtime evidence are inspected.

## Scope

This directory is for **dashboard definitions** and **dashboard-local review guidance** in KFM’s infrastructure and operations layer.

In KFM terms, dashboards are **derived operational surfaces**. They help operators, reviewers, and stewards see runtime health, promotion state, drill-through evidence links, stale signals, and correction pressure quickly. They are useful because they compress signal. They stop being useful when they become a second source of truth.

A good dashboard lane stays thin:

- it shows status
- it preserves joins
- it points to stronger objects
- it never quietly absorbs policy, contracts, or business logic

### Evidence labels used in this README

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Visible in the current public repo tree or directly grounded in stable KFM doctrine |
| **INFERRED** | Careful conclusion drawn from adjacent repo surfaces or repeated doctrine |
| **PROPOSED** | Commit-ready starter shape or practice that fits KFM doctrine but is not asserted as current checked-in behavior |
| **UNKNOWN** | Not verified strongly enough to present as a current repo or runtime fact |
| **NEEDS VERIFICATION** | Explicit placeholder that should be checked against the checked-out branch, platform settings, or live stack before merge |

[Back to top](#dashboards)

## Repo fit

### What this directory does

`infra/dashboards/` should hold **reviewable, diffable dashboard assets** that belong with infrastructure and operations concerns:

- operator-facing panel definitions
- dashboard-local notes on signal meaning
- drill-through link conventions
- small supporting docs that explain what a dashboard is for and how to review changes safely

### How it relates to nearby areas

| Area | Relationship | Why it matters |
|---|---|---|
| [`../README.md`](../README.md) | **Parent authority for infra fit** | Defines infra as the lane for environment wiring, delivery mechanics, observability, rollback, and operational surfaces |
| [`../monitoring/README.md`](../monitoring/README.md) | **Lateral companion lane / NEEDS VERIFICATION on exact split** | Monitoring explains signal capture and joinability; dashboards should explain how operators see and drill through those signals |
| [`../../policy/README.md`](../../policy/README.md) | **Boundary** | Dashboards may visualize policy outcomes, but policy rules themselves do not belong here |
| [`../../contracts/README.md`](../../contracts/README.md) and [`../../schemas/README.md`](../../schemas/README.md) | **Boundary** | Dashboards may consume contract-shaped data, but contract law and schema authority should stay there |
| [`../../tests/README.md`](../../tests/README.md) | **Review / validation neighbor** | Dashboard changes that affect drill-through, thresholds, or operator decisions should still be testable and reviewable |
| [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | **Operational downstream** | Workflow and promotion outputs often feed the operator views this lane is expected to describe |

### Working rule

A good dashboard file in KFM should answer three questions quickly:

1. **What is being shown?**
2. **What signal or decision does it support?**
3. **Where does a reviewer go next when the panel is red, stale, or contradictory?**

[Back to top](#dashboards)

## Accepted inputs

The following content belongs here when the mounted repo uses this lane for dashboard assets.

| Accepted input | Belongs here? | Notes |
|---|---|---|
| Hand-authored dashboard JSON definitions | Yes | Preferred when they stay diffable and environment-neutral |
| Exported dashboard definitions suitable for review in Git | Yes | Keep them stable, formatted, and named by purpose |
| Dashboard-local README notes | Yes | Explain panel intent, key joins, thresholds, and review expectations |
| Query or panel semantics notes | Yes | Especially useful when a panel encodes non-obvious thresholds or drill-through behavior |
| Screenshot or render references used in PR review | Yes, sparingly | Useful as review aids, but not as the authoritative asset |
| Stable drill-through link conventions | Yes | Example: trace → receipt, run → release, alert → runbook |
| Datasource placeholders / variables | Yes | Keep them non-secret and environment-safe |
| Alert panel annotations | Yes | Good when they clarify operator action without duplicating alert-engine logic |

## Exclusions

This directory should stay narrow.

| Does **not** belong here | Put it here instead |
|---|---|
| Service code, workers, or API handlers | `apps/` or `packages/` |
| Policy rules, exception grammar, Rego bundles | `../../policy/` |
| Contract schemas, vocabularies, OpenAPI authority | `../../contracts/` or `../../schemas/` |
| Canonical receipts, evidence bundles, release manifests | Their designated `data/`, catalog, or release/evidence surfaces |
| Scrape configs, alert rules, collector config, or observability plumbing | `../monitoring/` or the verified runtime lane that owns monitoring configuration |
| Long-form incident or ops runbooks | `../../docs/` or the repo’s verified runbook lane |
| Secret datasource credentials, tokens, or URLs with embedded auth | Secret manager / deployment wiring lane |
| Unexplained one-off screenshots with no asset source | Keep only if paired with the underlying dashboard artifact and review notes |
| Business logic masquerading as panel math | Move logic to governed services or packages; keep the dashboard thin |

> [!NOTE]
> Dashboard files should explain and expose signals. They should not become the place where KFM’s domain law quietly lives.

[Back to top](#dashboards)

## Current verified snapshot

The current public tree supports the following narrow claims:

- **CONFIRMED:** `infra/dashboards/` currently exposes `README.md` only.
- **CONFIRMED:** the parent [`infra/README.md`](../README.md) explicitly treats dashboards and operator views as accepted infrastructure content.
- **CONFIRMED:** sibling [`infra/monitoring/README.md`](../monitoring/README.md) exists as a separate lane.
- **CONFIRMED:** public `.github/workflows/` is currently README-only, so this README should not imply checked-in workflow YAMLs as public-`main` fact.
- **CONFIRMED:** current public `CODEOWNERS` assigns `/infra/` to `@bartytime4life`.
- **UNKNOWN / NEEDS VERIFICATION:** active dashboard vendor, provisioning path, datasource conventions, screenshot standards, alert-rule ownership, and live operator workflow depth.

> [!CAUTION]
> Directory presence is not the same thing as runtime maturity. A README-only lane proves scope and intent, not active dashboard coverage.

[Back to top](#dashboards)

## Directory tree

### Current verified snapshot

```text
infra/
└── dashboards/
    └── README.md
```

### Starter growth shape (PROPOSED)

```text
infra/
└── dashboards/
    ├── README.md
    ├── kfm-trace-to-receipt.json   # PROPOSED: drill-through from trace/run to receipt/evidence
    ├── <lane>-overview.json        # PROPOSED: promotion / runtime / correction overview
    └── <service-or-domain>.json    # PROPOSED: focused operator-facing dashboard definition
```

### Naming guidance

Use names that expose **purpose**, not vendor branding:

- `kfm-trace-to-receipt.json`
- `promotion-lane-overview.json`
- `governed-api-runtime.json`

Prefer avoiding vague names like:

- `dashboard-final.json`
- `ops2.json`
- `grafana-export-new.json`

[Back to top](#dashboards)

## Quickstart

Use this sequence before adding or restructuring anything here.

```bash
# 1) confirm repo root
git rev-parse --show-toplevel

# 2) inspect the live dashboards lane and nearby infra README surfaces
find infra/dashboards -maxdepth 2 -print | sort
find infra -maxdepth 2 -type f -name 'README.md' | sort

# 3) inspect parent infra guidance, sibling monitoring, workflow lane, and ownership
sed -n '1,240p' infra/README.md
sed -n '1,240p' infra/monitoring/README.md
sed -n '1,220p' .github/workflows/README.md
sed -n '1,220p' tests/README.md
sed -n '1,220p' policy/README.md
sed -n '1,220p' contracts/README.md
sed -n '1,220p' schemas/README.md
sed -n '1,200p' .github/CODEOWNERS

# 4) list dashboard-like assets if any have appeared since this README was written
git ls-files 'infra/dashboards/*'

# 5) validate JSON shape locally if dashboard files exist
for f in infra/dashboards/*.json; do
  [ -f "$f" ] && jq type "$f"
done
```

### First useful PR for this directory

1. Keep `README.md` authoritative for the lane.
2. Add **one** dashboard definition with a clear name.
3. Include a short note explaining:
   - what question the dashboard answers
   - which join keys or drill-through links it depends on
   - what should happen when the signal goes red
4. Add a rollback note to the PR so reviewers know how to revert safely.

[Back to top](#dashboards)

## Usage

### Treat dashboards as derived surfaces

Dashboards are for **seeing**, **triaging**, and **drilling through**.

They should summarize operational state, but they should still point back to stronger objects:

- governed API outputs
- receipts and release artifacts
- policy decisions
- traces, logs, and metrics
- runbooks and review surfaces

### Prefer drill-through over duplication

The more a panel copies raw operational detail into itself, the faster it drifts.

Prefer this pattern:

- panel shows a compact signal
- click or link opens the next governing object
- reviewer sees the underlying run, receipt, evidence, or runbook

### Keep dashboard assets diffable

Good dashboard changes review well in Git:

- stable filenames
- formatted JSON
- small, comprehensible diffs
- explicit notes on changed thresholds or joins
- no secrets embedded in the artifact

When a vendor export is noisy or opaque, pair it with a short sibling note that explains purpose, joins, thresholds, and drill-through behavior in plain language.

### Use stable identifiers when possible

When the live system supports them, favor stable joins over human guesswork.

Examples of good dashboard-level joins:

- request identifier
- audit or decision reference
- trace identifier
- run identifier
- release identifier
- correction identifier
- receipt or evidence reference

If the mounted implementation uses different field names, follow that reality and update this README.

[Back to top](#dashboards)

## Diagram

```mermaid
flowchart TD
    A[Metrics / logs / traces / run outputs] --> B[Dashboard definition]
    R[Receipts / release refs / correction refs] --> B
    B --> C[Operator or reviewer]
    C --> D[Drill-through link]
    D --> E[Governed API / evidence view / runbook]

    X[Canonical stores and truth-changing internals]
    X -. never treat the dashboard as a bypass path .-> C
```

### Reading the diagram

The dashboard is a **surface**, not a bypass. It can summarize multiple signals, but operator action should still move through governed interfaces and evidence-bearing objects.

[Back to top](#dashboards)

## Operating tables

### Dashboard family matrix

| Family | Primary question | Typical inputs | Trust note | Status |
|---|---|---|---|---|
| Lane overview | Is a release, promotion, or correction lane healthy right now? | workflow outputs, summaries, receipts, runtime indicators | Good for fast triage; poor if it hides provenance | **PROPOSED** |
| Trace ↔ receipt drill-through | Which exact run produced this state? | traces, manifests, receipts, evidence refs | High-value because it connects dashboards to inspectable evidence | **PROPOSED** |
| Runtime health | Is a service or worker degraded, stalled, or noisy? | metrics, logs, health probes, queue/latency views | Keep service logic out of the dashboard asset | **INFERRED** |
| Correction / rollback visibility | What was superseded, corrected, or rolled back? | correction notices, release lineage, incident annotations | Particularly important for trust-visible operations | **PROPOSED** |

### Preferred drill-through targets

| Signal on panel | Prefer linking to | Avoid |
|---|---|---|
| Release or promotion state | release manifest, receipt, or review record | panel-only summaries that cannot reconstruct scope |
| Runtime failure, hold, or denial | trace, audit reference, log bundle, or runbook | screenshot-only proof or unexplained red badges |
| Correction, rollback, or stale state | correction notice, rollback record, or supersession note | silent replacement of the previous state |
| Data freshness or evidence lag | source snapshot, evidence-bearing object, or runbook | a green tile that hides stale inputs |

### Change review matrix

| Change type | Minimum review payload |
|---|---|
| New dashboard asset | Purpose note, screenshot or preview, rollback note, ownership note |
| Query / panel semantic change | Explain changed thresholds, joins, or filters; include expected operator impact |
| Drill-through link addition | Show target object type and confirm the path remains governed |
| Sensitive or high-impact visibility change | Confirm policy or privacy implications and whether redaction or aggregation is needed |
| Removal / deprecation | Explain replacement path and whether any runbook, alert, or review flow must be updated |

### Heuristics for a healthy dashboard lane

| Signal | Good sign | Warning sign |
|---|---|---|
| Reviewability | Small readable diffs | Large opaque exports with no notes |
| Governance | Links resolve to stronger objects | Panel becomes the only explanation |
| Portability | Datasources are variable-driven | Environment-specific secrets are embedded |
| Trust | Negative states are visible | Green dashboards hide stale or missing evidence |

[Back to top](#dashboards)

## Task list / definition of done

A dashboard change in this directory is ready when:

- [ ] the file name is purposeful and stable
- [ ] the asset is diffable in Git
- [ ] the panel or dashboard purpose is explained in plain language
- [ ] drill-through targets are named
- [ ] no secrets are embedded
- [ ] any threshold or alert-facing semantics are described
- [ ] rollback or removal is straightforward
- [ ] repo fit is still correct relative to `infra/` and nearby lanes
- [ ] anything not verified in the live checkout is still labeled **PROPOSED**, **UNKNOWN**, or **NEEDS VERIFICATION**

For this directory itself, “done” means:

- [ ] current live subtree has been inspected
- [ ] relation to `../monitoring/README.md` is explicit
- [ ] at least one real dashboard asset exists, or this README clearly remains a scaffold guide
- [ ] ownership and review expectations are documented
- [ ] the lane does not quietly accumulate policy, contract, or business logic

[Back to top](#dashboards)

## FAQ

### Is this the same thing as `infra/monitoring/`?

**NEEDS VERIFICATION.** The current public tree shows both `dashboards/` and `monitoring/` under `infra/`, but this README does not assume the exact split until the checked-out branch and runtime are inspected.

### Does this lane own dashboard provisioning?

**UNKNOWN / NEEDS VERIFICATION.** This README is written for dashboard definitions and review guidance. Provisioning, collector config, or alert wiring may live elsewhere.

### Are dashboard files authoritative truth?

No. They are **operator-facing derived surfaces**.

### Should every dashboard here be Grafana JSON?

Not necessarily. Use the format the mounted repo actually uses. The important property is reviewability, not the vendor.

### Can dashboard assets contain business or policy logic?

Only in the lightest descriptive sense. If the logic is load-bearing, move it into governed code, policy, or contracts and keep the dashboard thin.

### Can this directory stay small?

Yes. A small, trustworthy dashboard lane is better than a large, stale one.

[Back to top](#dashboards)

## Appendix

<details>
<summary><strong>Verification backlog</strong></summary>

Before promoting this README from scaffold guide to stable operational contract, verify:

1. whether live dashboard assets already exist outside public `main`
2. whether `infra/monitoring/` owns provisioning while `infra/dashboards/` owns definitions
3. whether screenshots, exports, or datasource conventions are already standardized
4. whether any dashboard change should be paired with workflow, test, or runbook updates
5. whether CODEOWNERS should become more specific than the parent `/infra/` rule
6. the real values for `doc_id`, `created`, `updated`, and `policy_label` in the KFM Meta Block v2

</details>

<details>
<summary><strong>Editing rule</strong></summary>

When the checked-out repo or live stack is available, update this file by **mapping current reality first**.

Do not normalize the lane from memory, from doctrine alone, or from aesthetic preference.

</details>
