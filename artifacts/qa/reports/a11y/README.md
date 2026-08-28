<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/artifacts-qa-reports-a11y-readme
title: Accessibility QA report lane
type: readme
version: v0.1
status: draft; repository-grounded; report-payload-absent; axe-held; non-authoritative
owner: OWNER_TBD — accessibility steward, Explorer UI steward, QA/report steward, and CI steward
created: 2026-08-28
updated: 2026-08-28
policy_label: public
owning_root: artifacts/
responsibility: Describe the current accessibility QA report staging lane, its executable upstream checks, and its non-authority boundary without claiming a report producer, conformance, review, release, deployment, or publication.
truth_posture: CONFIRMED tracked repository and workflow evidence / PROPOSED future report contract / UNKNOWN external, ignored, historical, and untracked outputs / NEEDS VERIFICATION accountable ownership and retention
authority_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: bacb77cfbc04014a2c05da541f9cba8025629068
target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
lane_gitkeep_blob: 58398fff03a94a8b82fd5632fcb872923fe01d93
parent_reports_readme_blob: 0f07a8ea112f67f0b93eaa364cd23860789803ee
accessibility_workflow_blob: 1b3137905c441d5f5fab52afe33599fdda2ced88
accessibility_workflow_test_blob: f512c0d4cb57133e78c7e4738bc1a3c4ddd32e69
source_lineage:
  - "Drive — KFM_Whole_UI_Governed_AI_Expansion_Report_Extended_Pro.pdf — proposed accessibility targets and future axe/report ideas only; not implementation or conformance evidence."
  - "Notion — KFM Repository Workbench and Alignment Register — overlap and exact-ref coordination only; GitHub bytes control implementation claims."
related:
  - ../README.md
  - ../../README.md
  - ../../../../.github/workflows/accessibility.yml
  - ../../../../tests/ci/test_accessibility_workflow.py
  - ../../../../docs/architecture/ui/ACCESSIBILITY.md
  - ../../../../docs/brand/accessibility-commitments.md
tags: [kfm, accessibility, a11y, qa, reports, axe, keyboard, focus, generated-output, non-authoritative]
notes:
  - "The direct lane contained only an empty README and a .gitkeep before this revision."
  - "The current workflow emits job results, logs, and step summaries; it does not write or upload a report here."
  - "The axe job reports an explicit hold and runs no axe ruleset."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Accessibility QA report lane

`artifacts/qa/reports/a11y/` is the reserved compatibility lane for
regenerable accessibility inspection reports. It does not currently contain a
report payload, run manifest, conformance statement, receipt, proof, release
record, or published artifact.

> [!IMPORTANT]
> The repository's `accessibility` workflow does **not** write to this
> directory. Its keyboard job runs a bounded eight-spec Explorer browser smoke,
> while its axe job records an explicit readiness hold without running axe.

## Current status

| Surface | Status | Evidence-bounded meaning |
|---|---|---|
| `README.md` | `CONFIRMED` | Authored boundary for this otherwise empty report lane. |
| `.gitkeep` | `CONFIRMED` | Retains the proposed directory; it is not a report. |
| Retained report payload | `ABSENT` | No tracked JSON, HTML, Markdown, SARIF, or run manifest is present. |
| Report producer | `NOT ESTABLISHED` | No inspected workflow writes or uploads an accessibility report here. |
| `keyboard-navigation` job | `BOUNDED EXECUTABLE` | Runs eight named Explorer Playwright specifications against local fixtures. |
| `axe` job | `WORKFLOW_HOLD` | Emits hold messaging and executes no axe ruleset. |
| Accessibility conformance | `NOT ESTABLISHED` | Current checks do not prove WCAG or whole-application conformance. |
| Retention and pruning | `NEEDS VERIFICATION` | No lane-specific retention contract was verified. |
| Accountable ownership | `NEEDS VERIFICATION` | CODEOWNERS routing is not specialist review or approval. |

The absence statements above are limited to the tracked tree at the recorded
base commit. They do not prove that ignored local files, historical workflow
artifacts, other branches, external services, or uninspected storage never
contained accessibility output.

## Upstream executable evidence

The
[`accessibility` workflow](../../../../.github/workflows/accessibility.yml)
preserves two stable jobs:

| Job | Current operation | Successful completion means | It does not mean |
|---|---|---|---|
| `keyboard-navigation` | Installs the locked workspace and runs eight named Playwright specifications. | Those bounded fixture journeys completed at the tested revision. | Whole-app coverage, manual assistive-technology review, conformance, release approval, or publication. |
| `axe` | Writes `WORKFLOW_SKIPPED_EXPLICIT` and `WORKFLOW_HOLD` to the step summary. | The hold-reporting step completed. | An axe scan, ruleset evaluation, or accessibility pass. |

The workflow contract test at
[`tests/ci/test_accessibility_workflow.py`](../../../../tests/ci/test_accessibility_workflow.py)
checks the exact browser-spec list, stable job names, read-only permission,
pinned actions, and no-upload posture. It tests workflow shape; it does not run
the browser smoke or validate accessibility.

## Focused reproduction

From the repository root, validate the workflow contract with:

```bash
python -m pytest -q tests/ci/test_accessibility_workflow.py
```

After installing the locked workspace dependencies, reproduce the bounded
browser job with:

```bash
pnpm --filter explorer-web exec playwright test \
  --config=playwright.config.ts \
  tests/browser/citation-pill.spec.ts \
  tests/browser/evidence-drawer.spec.ts \
  tests/browser/evidence-tooltip.spec.ts \
  tests/browser/focus-composed-claim.spec.ts \
  tests/browser/map-evidence-drawer.spec.ts \
  tests/browser/map-runtime-trust-status.spec.ts \
  tests/browser/time-banner.spec.ts \
  tests/browser/workspace-navigation.spec.ts
```

Dependency installation may contact the configured package registry. The
browser specifications use the local Vite fixture server, but
`KFM_NO_NETWORK=1` is an intended test posture rather than proof of operating
system or process-level egress isolation.

## Result interpretation

| Observed result | Safe interpretation | Required follow-up |
|---|---|---|
| Keyboard job passes | The named fixture journeys passed at that revision. | Review scope and remaining holds before making broader claims. |
| Keyboard job fails | At least one named journey or its setup failed. | Inspect the failing spec and logs; do not classify accessibility broadly from the job name alone. |
| Axe job succeeds | The explicit hold-reporting step ran. | Keep automated axe coverage held. |
| Axe job fails | The hold-reporting workflow step failed. | Repair orchestration without calling it an accessibility scan. |
| Job is skipped or cancelled | No normal result exists for that job. | Record the finite state and rerun only when justified. |
| A future report appears here | A generated inspection copy exists. | Verify producer, revision, scope, ruleset, exclusions, digest, and retention before use. |

Logs and step summaries are revision-scoped CI observations. They are not
sovereign truth, accessibility approval, a policy decision, a receipt, a proof,
or a release/publication transition.

## Future report admission

The following requirements describe a **proposed** graduation contract. They
do not assert that a producer or schema exists.

A retained accessibility report should identify:

- repository and exact tested revision;
- producer command and tool/ruleset version;
- inspected application surface and fixture profile;
- finite outcome, start/end time, and runner context;
- included and excluded rules, states, routes, and viewports;
- finding counts without turning a zero count into a conformance claim;
- sanitized finding locations and stable reason codes;
- report digest and regeneration instructions;
- retention class, expiration or pruning behavior, and correction path.

A future workflow must fail visibly when its producer, input scope, ruleset,
fixture set, or output write fails. An empty, missing, stale, or unparsable
report must not be normalized to a pass.

## Security, privacy, and harmful precision

Do not retain credentials, cookies, tokens, private URLs, environment dumps,
absolute user paths, unpublished cultural or archaeological locations,
rare-species coordinates, living-person or DNA details, private-land details,
critical-infrastructure detail, or unnecessary page content in reports.

Prefer bounded diagnostics: repository-relative paths, stable fixture IDs,
rule identifiers, safe selectors, redacted messages, and revision hashes.
Screenshots and HTML snapshots require an explicit sensitivity and rights
review before retention.

## Authority and storage boundary

This lane follows the parent
[`artifacts/qa/reports/` contract](../README.md): generated QA inspection copies
may live here, but trust-bearing objects remain separate.

| Object | Correct posture |
|---|---|
| Generated accessibility report | Regenerable inspection copy in this lane. |
| Workflow definition and producer code | `.github/`, `tools/`, or the owning application/package. |
| Canonical receipt or validation memory | Governed receipt/validation home, not this lane. |
| Proof or EvidenceBundle | Governed proof/evidence home. |
| Policy decision | Policy authority, not a QA report. |
| Release or publication decision | `release/` and its governed transition. |

The current
[`UI accessibility architecture`](../../../../docs/architecture/ui/ACCESSIBILITY.md)
and
[`brand accessibility commitments`](../../../../docs/brand/accessibility-commitments.md)
provide broader context. Neither a report nor a passing job may silently
strengthen their evidence posture.

## Maintenance and correction

Update this README when any of these repository facts change:

- the workflow begins running axe or another automated ruleset;
- the browser-spec inventory changes;
- a report producer, schema, upload, retention policy, or consumer is added;
- the report lane moves or gains an accepted canonical relationship;
- sensitive-output handling or accountable ownership is established;
- a correction invalidates a retained report or its interpretation.

For an incorrect unmerged documentation change, close or revise its draft
branch. For a merged documentation error, revert or correct the Markdown.
Deleting or correcting a report description does not undo a workflow run,
human review, release, deployment, promotion, or publication.

## Evidence ledger

| Evidence | What it establishes |
|---|---|
| Tracked lane inventory at the recorded base | Only an empty `README.md` and `.gitkeep` existed directly in this folder. |
| `.github/workflows/accessibility.yml` | Two jobs, exact browser command, explicit axe hold, read-only permissions, and no artifact upload. |
| `tests/ci/test_accessibility_workflow.py` | Workflow-shape assertions and exact spec inventory. |
| Parent QA/report READMEs | Transitional, regenerable, non-authoritative artifact boundary. |
| Drive UI report | Proposed accessibility and axe ideas only; its own repository inspection was unavailable. |
| Notion workbench and alignment register | Coordination and active-draft overlap only. |

[Back to top](#top)
