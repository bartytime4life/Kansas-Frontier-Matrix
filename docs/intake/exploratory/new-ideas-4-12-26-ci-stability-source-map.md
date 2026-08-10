<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/new-ideas-4-12-26-ci-stability-source-map
title: New Ideas 4-12-26 - CI Stability Observation Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; decision-required
owners: OWNER_TBD - CI steward; repository steward; observability steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; intake; exploratory; repository-operations
truth_posture: cite-or-abstain; measurements do not create merge or release authority
owning_root: docs/
responsibility: Reconcile the private New Ideas 4-12-26 CI-health proposal with current KFM CI outcome, repository-control, and dashboard surfaces while preserving the separation among observed stability, required-check settings, merge decisions, and governed release.
source_class: connected private document
source_title: New Ideas 4-12-26
source_section: CI Health Card (Governed Checks)
source_status: non-authoritative exploratory proposal
source_disclosure: privacy-minimized; full source text, connector locator, private link, timestamps, digest, and file size omitted
repository: bartytime4life/Kansas-Frontier-Matrix
repository_snapshot: 70229e41cc434c9cb0b3b29f02742773d4a18b77
repository_verified_on: 2026-08-09
related:
  - ./README.md
  - ./new-ideas-4-12-26-cosign-attestation-verification-source-map.md
  - ../../dashboards/observability/build-ci-health.md
  - ../../../contracts/governance/repository_control_state.md
  - ../../../schemas/contracts/v1/governance/ci_outcome.schema.json
  - ../../../tools/validators/repository_control/validate_repository_control.py
  - ../../../tests/validators/test_repository_control.py
  - ../../../tests/e2e/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, ci, stability, flakes, required-checks, repository-control, observability, merge-boundary]
notes:
  - "The connected document was searched and the CI Health Card section was reviewed in context. Private source text and connector metadata are deliberately excluded."
  - "The source is evidence that CI-health thresholds and a workflow were proposed. It is not evidence of current workflow names, branch protection, required checks, run history, flake rates, hosted enforcement, or release coupling."
  - "Current-repository conclusions are limited to the pinned main snapshot."
  - "This source map does not change GitHub settings, required checks, workflows, retries, mergeability, policy, promotion, release, deployment, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# New Ideas 4-12-26 - CI stability observation source map

> **Outcome:** KFM already has a per-run CI outcome schema, a repository-control settings snapshot, and a draft internal build-health dashboard. The remaining useful idea is narrower: define how stability observations over multiple hosted runs could be measured without turning a retry rate, duration percentile, dashboard color, or workflow result into authority to remove a required check, merge, promote, release, or publish.

> [!CAUTION]
> The source proposes check names, flake thresholds, duration budgets, retry behavior, and temporary removal from the required set. These values conflict with current draft dashboard values or lack current repository/platform evidence. None is adopted here.

**Quick links:** [Source boundary](#source-boundary-and-review-method) · [Placement](#directory-rules-and-authority-basis) · [Reconciliation](#repository-grounded-reconciliation) · [Retained gap](#retained-non-duplicative-gap) · [Decision candidate](#proposed-ci-stability-observation-decision) · [Unsafe transfers](#unsafe-direct-transfers) · [Next action](#recommended-next-bounded-action) · [Validation](#validation-and-review-boundary) · [Rollback](#rollback-and-correction)

## Source boundary and review method

### Privacy-minimized source identity

| Field | Bounded value |
|---|---|
| Supplied title | *New Ideas 4-12-26* |
| Reviewed section | *CI Health Card (Governed Checks)* |
| Source posture | Non-authoritative exploratory proposal |
| Current repository comparison | `main@70229e41cc434c9cb0b3b29f02742773d4a18b77`, inspected `2026-08-09` |
| Private material | Full source text, Drive locator, private link, connector timestamps, digest, and file size intentionally omitted |

### Review method

This pass:

1. inventoried the connected document and reviewed the CI-health section in context;
2. treated its workflow YAML, branch-protection directions, thresholds, tool versions, check names, and embedded commands as proposal data;
3. searched current main for CI outcome, repository-control, dashboard, retry, flake-rate, required-check, merge, and promotion surfaces;
4. compared the source's thresholds with the current draft dashboard rather than averaging them;
5. separated measurement, interpretation, platform settings, merge review, promotion, and release responsibilities; and
6. retained only a decision candidate that creates no live workflow, platform mutation, or trust upgrade.

The source's security, dependency, and product-version claims are outside this bounded CI-stability pass. The existing [Cosign attestation source map](./new-ideas-4-12-26-cosign-attestation-verification-source-map.md) separately handles one security-sensitive portion.

[Back to top](#top)

## Directory Rules and authority basis

Accepted [Directory Rules v2](../../doctrine/directory-rules.md), adopted through [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), place human-readable exploratory reconciliation under `docs/`. The [exploratory intake README](./README.md) defines this directory as the waiting room for noncanonical ideas that need classification, evidence review, routing, promotion, archive, or rejection.

This source map belongs under `docs/intake/exploratory/` because it records source pressure, current repository evidence, threshold conflict, a residual decision candidate, and explicit non-effects. It does not belong under:

- `.github/workflows/`, because no hosted workflow is admitted or changed;
- `control_plane/`, because no accepted settings or live CI-state projection is created;
- `contracts/` or `schemas/`, because measurement semantics and threshold authority remain undecided;
- `tools/`, because no provider reader, aggregator, validator, or settings writer is implemented;
- `policy/`, because no merge, retry, flake, or release rule is adopted;
- `data/receipts/` or `data/proofs/`, because a dashboard observation is neither a process receipt nor release proof; or
- `release/`, because CI stability does not authorize promotion or release.

[Back to top](#top)

## Repository-grounded reconciliation

Disposition terms:

- `REPRESENTED` - a current repository surface already owns the idea.
- `PARTIAL` - related shape exists, but the source's end-to-end claim is not established.
- `CONFLICTED` - proposed values or responsibilities disagree.
- `RETAIN` - a narrower non-duplicative decision gap remains.
- `REJECT_AS_CURRENT` - the source statement cannot be treated as current repository or platform fact.

| Source contribution | Current-main evidence | Disposition | Boundary |
|---|---|---|---|
| Finite result for one workflow/job at one head SHA | [`ci_outcome.schema.json`](../../../schemas/contracts/v1/governance/ci_outcome.schema.json) already classifies one workflow/job result as `PASS`, `EXPECTED_READINESS_HOLD`, `REGRESSION`, `NOT_APPLICABLE`, `SKIPPED_EXPLICIT`, or `UNKNOWN`. | `REPRESENTED` | Do not replace the repository vocabulary with the source's simpler `PASS/FAIL/ERROR` list. |
| Required-check and pull-request enforcement posture | [`RepositoryControlState`](../../../contracts/governance/repository_control_state.md) and its validator bind a settings snapshot and required-check names without reading or mutating GitHub. | `PARTIAL / REPRESENTED` | A tracked snapshot is not current platform truth or mutation authority. |
| Build pass rate, wallclock, runner conformance, sampling, retry/flake rate, and telemetry emission | The draft [Build & CI Health](../../dashboards/observability/build-ci-health.md) dashboard already names these internal metrics and explicitly marks several thresholds proposed. | `REPRESENTED` | Dashboard metrics do not decide merge or release. |
| Source flake threshold: retry rate over 2% in seven days; restore below 1% | The dashboard instead names a proposed flake-rate posture below 5% and a 24-hour pass-rate window. No accepted decision reconciles the values. | `CONFLICTED` | Do not average thresholds or select the stricter number without measured repository evidence and an owner decision. |
| Source duration targets: required path below ten minutes and first failure below two minutes | The dashboard leaves per-workflow wallclock budgets open. Current workflow inventory, run distributions, runner classes, and branch-protection significance were not established by this pass. | `REJECT_AS_CURRENT / DECISION REQUIRED` | Budgets must be workflow- and runner-class-specific and measurement-backed. |
| Remove a flapping check temporarily from the required set | Current repository-control tooling explicitly does not change settings. No current authorization, replacement check, incident record, or risk acceptance was supplied. | `REJECT_AS_AUTOMATIC` | A stability observation may recommend `HOLD`; only a separate authorized platform transition may change the required set. |
| Weekly and monthly health maintenance | Current test READMEs repeatedly mark pass rate, runtime, coverage, and flake rate unknown pending repeated CI evidence. | `PARTIAL / RETAIN` | A cadence proposal does not prove provider access, retention, ownership, or collected history. |
| One aggregate `HEALTHY/DEGRADED/UNSTABLE` status | Current health-projection patterns avoid threshold-derived authority and report bounded measurements only. | `NARROW / RETAIN` | A future CI observation should emit measurements and data quality, not an unreviewed health judgment. |

This pass did not inspect a current GitHub ruleset, branch-protection configuration, complete workflow inventory, historical run population, rerun linkage, runner fleet, required-check list, or hosted retention window. Those remain `UNKNOWN`.

[Back to top](#top)

## Retained non-duplicative gap

The repository has a one-run outcome and a dashboard target, but this pass did not find a bounded object that explains how a multi-run CI stability measurement was produced.

A useful future observation would keep six questions separate:

1. **Run result:** What did this job conclude at this head SHA?
2. **Population:** Which exact runs, attempts, branches, events, and time window were included?
3. **Stability:** How often did an unchanged head fail then pass, time out, cancel, or vary materially?
4. **Performance:** What are the median and p95 durations for comparable runner and workflow classes?
5. **Enforcement:** Was the check required in the observed settings snapshot?
6. **Authority:** Who, if anyone, may change that setting, accept residual risk, merge, or couple the result to promotion?

Collapsing these into one color or percentage hides whether the data are incomplete, the check is optional, the runner changed, retries mask failures, cancellations were censored, or a required-check transition was separately approved.

[Back to top](#top)

## Proposed CI stability observation decision

**PROPOSED decision candidate, not an implemented object:** decide whether a fixture-only `CIStabilityObservation` responsibility is distinct enough to add after the measurement semantics are reviewed.

### Minimum bounded input

- repository and provider identity;
- workflow and job identity;
- branch/event/runner class;
- observation start and end;
- exact included run and attempt identifiers;
- head SHA for every run;
- original and rerun relationship;
- normalized provider conclusion;
- queued, started, and completed times;
- cancellation, skip, timeout, infrastructure-failure, and missing-data classification;
- settings-snapshot reference recording whether the check was required; and
- collector version, query parameters, result digest, and currentness note.

### Minimum deterministic measurements

- total runs, completed runs, and excluded runs by reason;
- first-attempt failure count;
- unchanged-head fail-then-pass count;
- rerun count and retry rate with an explicit denominator;
- timeout and cancellation counts;
- median and p95 duration over comparable completed runs;
- observation coverage and missingness; and
- a finite data-quality state such as `COMPLETE`, `PARTIAL`, `EMPTY`, or `ERROR`.

### Required non-effects

The observation must not:

- label a check `HEALTHY`, `SAFE`, or `RELEASE_READY` without an accepted interpretation policy;
- mutate GitHub settings, required checks, workflows, retries, or branch protection;
- remove or restore a required check;
- infer that a failure is flaky solely because a rerun passed;
- treat skipped, cancelled, neutral, timed-out, or missing runs as success;
- turn a dashboard threshold into policy;
- authorize merge, override, promotion, release, deployment, or publication; or
- create a receipt, proof, incident, or waiver by implication.

[Back to top](#top)

## Unsafe direct transfers

| Source pattern | Why direct transfer is unsafe | Required correction |
|---|---|---|
| Adopt the named check list as branch protection | The source list is not a verified current workflow or ruleset inventory. | Discover exact current workflows, stable job names, dependency closure, and current settings first. |
| Use 2%, 1%, 5%, ten-minute, or two-minute constants globally | The source and dashboard disagree, and workflow/runner classes differ. | Measure representative histories and accept thresholds per class through the owning policy/settings decision. |
| Mark any fail-then-pass run as flaky | The underlying cause may be code, order dependence, cache, rate limit, runner loss, or hidden mutable input. | Emit an observation and require triage; do not erase the original failure. |
| Automatically retry every failure | Retries can hide deterministic regressions and inflate capacity. | Declare retry policy separately and preserve every attempt in the population. |
| Temporarily remove a required check | This weakens a protected merge boundary and changes external platform state. | Require explicit authorized settings transition, risk assessment, replacement/containment, expiry, audit, and restoration criteria. |
| Treat all required checks passing as promotion eligibility | Merge checks do not close evidence, rights, policy, review, release, correction, or rollback. | Keep repository merge, KFM promotion, and release decisions separate. |
| Write an override directly into `data/receipts/` | Placement and object meaning are unresolved; a receipt cannot approve its own exception. | Use the accepted incident, waiver, transition-authorization, or review family if and when applicable. |
| Publish workflow/job names or runner identifiers without review | Names can encode sensitive lanes or internal topology. | Apply internal access, minimization, and redaction at collection and rendering. |

[Back to top](#top)

## Recommended next bounded action

Prepare a **decision-only CI stability measurement issue** before implementing a contract. It should:

- inventory current hosted workflows, stable job identities, event and runner classes, retention, and required-check settings;
- define run/attempt identity and unchanged-head rerun linkage;
- decide treatment of skipped, neutral, cancelled, timed-out, infrastructure-failed, superseded, and missing runs;
- define metric denominators and percentile method;
- reconcile the source and dashboard threshold conflicts with measured history;
- separate observation from interpretation, incident/waiver, settings transition, merge review, promotion, and release;
- define redaction and retention; and
- authorize no settings mutation, workflow change, check removal, merge, promotion, release, deployment, or publication.

Only after that decision should a fixture-only `CIStabilityObservation` contract/schema/validator packet be considered. This intake source map does not authorize it.

[Back to top](#top)

## Validation and review boundary

This source map is complete only if:

- the reviewed section and its private source identity remain bounded;
- private connector metadata and full source text are absent;
- current-repository claims are pinned to `main@70229e41cc434c9cb0b3b29f02742773d4a18b77`;
- every linked repository path resolves;
- current per-run outcome, repository-control, dashboard, and test-evidence surfaces are distinguished;
- threshold conflicts remain visible;
- observed stability remains separate from settings and decision authority;
- no workflow, settings, check, retry, policy, receipt, proof, merge, promotion, release, deployment, or publication state changes; and
- the pull request remains one bounded documentation-only review surface.

## Rollback and correction

Before merge, rollback is closing the draft pull request and abandoning its branch. After a separately authorized merge, use a focused reviewed revert of this one source-map file.

If CI provider behavior, repository workflows, settings, schema vocabulary, dashboard thresholds, or measurement evidence changes:

1. preserve this file as dated intake lineage;
2. add a correction or supersession note rather than rewriting the prior proposal as current fact;
3. re-run the current workflow/settings inventory and repeated-run measurement;
4. route any settings or enforcement change through its separately authorized transition and rollback path; and
5. never let an updated metric silently become merge, promotion, or release authority.

[Back to top](#top)
