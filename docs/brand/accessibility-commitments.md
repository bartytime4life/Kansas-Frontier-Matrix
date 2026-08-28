<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/brand-accessibility-commitments
title: Accessibility Commitments
type: standard
version: v1.1
prior_version: v1
status: draft; repository-grounded; partial-keyboard-ci; no-conformance-authority; no-release-authority
owners:
  - "@bartytime4life — verified CODEOWNERS review route"
owner_status: "Accessibility, UI, assistive-technology, policy, release, and independent review assignments remain NEEDS VERIFICATION."
created: 2026-05-15
updated: 2026-08-28
policy_label: public
owning_root: docs/
responsibility: "Describe human-facing accessibility commitments and route readers to current bounded implementation evidence without becoming doctrine, policy, a release gate, or a conformance statement."
truth_posture: "CONFIRMED repository evidence / PROPOSED accessibility targets / UNKNOWN whole-application and production conformance; cite-or-abstain"
authority_effect: none
lifecycle_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: bacb77cfbc04014a2c05da541f9cba8025629068
  target_prior_blob: d80d2c3d185db41cd7f3c36bb5c1f6df13f1b7f9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  accessibility_architecture_blob: 62bc5ab6e5ee9070bbaf3053356c35499dde45ed
  accessibility_workflow_blob: 1b3137905c441d5f5fab52afe33599fdda2ced88
  accessibility_workflow_test_blob: f512c0d4cb57133e78c7e4738bc1a3c4ddd32e69
  explorer_manifest_blob: d9ada6539e07a4a5cd9b65ec9792105bd4856807
  playwright_config_blob: 03fddcd1f34e1e07bb499e01dfc3cdc7bd235f16
  a11y_report_readme_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
source_lineage:
  - title: KFM_Comprehensive_Research_and_Verification_Report.docx
    source_class: DRIVE_RESEARCH_LINEAGE
    use: "Candidate accessibility targets and review ideas only; not repository implementation, adoption, or conformance evidence."
  - title: KFM Repository Workbench
    source_class: NOTION_COORDINATION_ONLY
    use: "Current work and overlap discovery only; GitHub bytes remain controlling evidence."
related:
  - ./README.md
  - ../architecture/ui/ACCESSIBILITY.md
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../.github/workflows/accessibility.yml
  - ../../tests/ci/test_accessibility_workflow.py
  - ../../apps/explorer-web/package.json
  - ../../apps/explorer-web/playwright.config.ts
  - ../../artifacts/qa/reports/a11y/README.md
tags: [kfm, brand, accessibility, a11y, keyboard, focus, wcag, trust-visible-states]
notes:
  - "v1.1 removes the unsupported claim that this draft brand reference is canonical doctrine or an implemented release gate."
  - "The accessibility workflow has one executable eight-spec keyboard/focus job; its axe job remains an explicit readiness hold."
  - "A passing workflow is bounded CI evidence, not WCAG conformance, manual assistive-technology review, release approval, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Accessibility commitments

This page records KFM's human-facing accessibility targets and the repository evidence that currently supports them. It is a draft brand reference: it does not create doctrine, policy, a release gate, or a claim that any KFM surface conforms to an external standard.

> [!IMPORTANT]
> Current evidence is partial. The repository executes a bounded keyboard-and-focus browser smoke over eight deterministic Explorer Web specifications. Automated axe coverage, a whole-application audit, manual assistive-technology testing, contrast and zoom/reflow proof, reduced-motion coverage, non-map parity, PDF/UA validation, and production conformance remain held or unknown.

## Status and authority

| Question | Current answer |
|---|---|
| What kind of document is this? | Draft human-facing brand and accessibility guidance. |
| Is it canonical doctrine or policy? | No. Accepted decisions and their owned doctrine or policy paths control those claims. |
| Does it establish a release gate? | No. No accepted accessibility-specific release gate was verified from current repository evidence. |
| Does current CI prove WCAG conformance? | No. The executable job covers only the named fixture journeys below. |
| Who receives repository review requests? | `@bartytime4life` through CODEOWNERS. This is routing, not proof that accessibility or independent review occurred. |
| What is the standards target? | WCAG 2.2 Level AA is a **proposed target**, not a conformance statement. |

The placement is intentionally narrow. Under accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and the adopted [Directory Rules](../doctrine/directory-rules.md), `docs/brand/` may explain human-facing voice and visual language. Runtime behavior belongs in `apps/` or shared packages, executable evidence in `tests/`, workflow orchestration in `.github/`, machine shape in `schemas/`, policy in `policy/`, and release decisions in `release/`.

## Current repository evidence

### Implemented checks

The [`accessibility` workflow](../../.github/workflows/accessibility.yml) preserves two stable job surfaces with different meanings:

| Job | Current behavior | What a success means | What it does not mean |
|---|---|---|---|
| `keyboard-navigation` | Installs the locked workspace and runs eight named Playwright specifications against local Vite fixtures. | The bounded fixture journeys completed at the tested revision. | Whole-app keyboard completion, screen-reader parity, WCAG conformance, release approval, deployment, or publication. |
| `axe` | Emits `WORKFLOW_SKIPPED_EXPLICIT` and `WORKFLOW_HOLD`; it runs no axe ruleset. | The explicit hold-reporting step completed. | An accessibility scan or an axe pass. |

The workflow contract is regression-tested by [`tests/ci/test_accessibility_workflow.py`](../../tests/ci/test_accessibility_workflow.py). Those tests assert the stable job names, exact browser-spec list, read-only permissions, pinned actions, local no-publication posture, and the continuing axe hold.

### Executed browser scope

The keyboard job runs exactly these Explorer Web specifications:

1. `tests/browser/citation-pill.spec.ts`
2. `tests/browser/evidence-drawer.spec.ts`
3. `tests/browser/evidence-tooltip.spec.ts`
4. `tests/browser/focus-composed-claim.spec.ts`
5. `tests/browser/map-evidence-drawer.spec.ts`
6. `tests/browser/map-runtime-trust-status.spec.ts`
7. `tests/browser/time-banner.spec.ts`
8. `tests/browser/workspace-navigation.spec.ts`

The current workflow describes their shared scope as native navigation, keyboard activation, focus entry and restoration, Escape dismissal, a keyboard-operable time slider, text-first runtime trust states, finite negative states, and protected-detail suppression. Each specification remains the authority for its own assertions.

### Report and receipt boundary

`artifacts/qa/reports/a11y/` contains an empty README placeholder and a `.gitkeep`; no tracked accessibility report payload or repository producer is established there. The workflow emits GitHub job state, logs, annotations, and step summaries only. It does not upload an accessibility report, receipt, proof, release record, or publication artifact.

A generated receipt under `data/receipts/generated/` may record generator lineage, but neither that filename nor this document establishes accessibility conformance, human review, release approval, or publication.

## Reproduce the bounded checks

Run commands from the repository root.

### Workflow contract

```bash
python -m pytest -q tests/ci/test_accessibility_workflow.py
```

### Keyboard and focus smoke

Install the locked workspace, then run the same browser selection used by the workflow:

```bash
corepack enable
pnpm install --frozen-lockfile

CI=true KFM_NO_NETWORK=1 \
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

The browser tests serve repository fixtures from `127.0.0.1`. Dependency installation may contact the configured package registry. Setting `KFM_NO_NETWORK=1` records the workflow's intended fixture posture; it is not evidence of process- or operating-system-level network isolation for Node or the package manager.

## Interpret outcomes narrowly

| Observation | Safe interpretation | Required follow-up |
|---|---|---|
| Workflow-contract tests fail | Accessibility orchestration drifted from the pinned contract. | Inspect the workflow and test together; do not weaken assertions merely to obtain green CI. |
| A named browser specification fails | At least one assertion in that bounded fixture journey regressed or the harness failed. | Classify fixture, harness, and product behavior separately. |
| `keyboard-navigation` succeeds | The eight selected specifications completed for that revision. | Keep untested surfaces and modalities explicitly held. |
| `axe` succeeds | The hold-reporting step completed. | Do not call it an axe scan; a reviewed ruleset and representative state matrix are still missing. |
| Every hosted check is green | Repository checks found no configured failure at that revision. | Human review, conformance assessment, release, deployment, and publication remain separate. |

## Proposed accessibility targets

The targets below guide design and review but are not implemented promises or release rules unless a governing decision and corresponding enforcement adopt them.

| Target | Desired user outcome | Current repository posture |
|---|---|---|
| Keyboard operation and visible focus | Consequential controls remain operable without a pointing device, and focus entry/restoration is predictable. | **PARTIAL** — bounded fixture evidence only. |
| Non-map alternatives | Consequential map results and evidence remain available through an equivalent text, list, or table path. | **HOLD / NEEDS VERIFICATION**. |
| Non-color trust states | Source, evidence, restriction, freshness, correction, and finite outcomes do not rely on color alone. | **PARTIAL** in named fixture assertions; no whole-app audit. |
| Reduced motion | Informative motion has an equivalent and optional motion respects user preference. | **HOLD / NEEDS VERIFICATION**. |
| Touch, zoom, reflow, and target size | Trust information remains reachable at supported narrow viewports and zoom levels. | **HOLD / NEEDS VERIFICATION**. |
| Accessible names and announcements | Meaningful controls, media, state changes, denials, and abstentions are exposed to assistive technology. | **PARTIAL** in named fixtures; manual parity is unverified. |
| Sensitive and sovereignty notices | Required notices remain perceivable and operable without exposing restricted details. | **PROPOSED / policy and specialist review required**. |
| Publication-grade documents | Public documents have an adopted, repeatable accessibility validation profile. | **HOLD** — no PDF/UA producer, toolchain, or gate is established here. |

## External standards

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) is the proposed web-content target used by current KFM accessibility architecture guidance.
- The [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) offers implementation guidance for common widgets and keyboard behavior; it is not itself a KFM conformance result.

External standards define requirements or guidance. Referencing them, running automated checks, or satisfying a synthetic fixture does not establish whole-surface conformance. A defensible conformance claim requires a declared scope, supported environment matrix, applicable success-criterion evaluation, known exceptions, and accountable human review.

## Review checklist

For a change affecting a public or review-facing surface:

- identify the exact routes, components, states, viewports, and input methods in scope;
- preserve text-first `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` distinctions where the surface uses those outcomes;
- verify keyboard entry, operation, dismissal, and focus restoration for the changed interaction;
- verify that color, position, animation, hover, or the map canvas is not the only carrier of consequential meaning;
- exercise negative, stale, restricted, loading, and error states that the changed surface can emit;
- record automated and manual checks separately, including skipped or unavailable modalities;
- treat fixture evidence, hosted checks, human review, conformance, release, deployment, and publication as distinct states;
- keep sensitive reasons, precise protected locations, personal data, credentials, and internal-only paths out of screenshots, logs, summaries, and reports.

## Known gaps

The following remain unverified or unimplemented from current repository evidence:

- a reviewed automated accessibility ruleset and representative state matrix;
- a supported browser, device, zoom, viewport, contrast, and forced-color matrix;
- accountable manual testing with named assistive technologies;
- whole-application focus-order and non-map-parity assessment;
- reduced-motion and touch/target-size coverage;
- an accessibility-report producer, governed report schema, retention policy, and correction linkage;
- a PDF/UA validation toolchain and document-publication profile;
- an accepted accessibility-specific release gate and named accountable reviewers.

## Maintenance and correction

Update this page when the executable workflow scope, exact browser-spec list, external target, report producer, or authority boundary changes. Verify the implementation and tests first; do not promote planning prose or generated output into current repository fact.

If this page overstates evidence, narrow the claim in place and record the prior wording in Git history. If the executable keyboard job is reverted, restore the earlier maturity label without deleting the proposed targets. Closing or reverting a documentation pull request changes documentation only; it does not undo a workflow run, review, release, deployment, or publication.

## Evidence ledger

| Evidence | Blob | Bounded use |
|---|---|---|
| Accepted Directory Rules decision | `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` | Establishes adopted placement authority without making this page doctrine. |
| Directory Rules | `fd49a0b83e55cef52c1124281f093e263526898d` | Routes human guidance, implementation, tests, workflows, policy, and release records to their responsibility roots. |
| CODEOWNERS | `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` | Establishes the repository review route only. |
| Accessibility architecture | `62bc5ab6e5ee9070bbaf3053356c35499dde45ed` | Records the broader partial-implementation and proposed-target boundary. |
| Accessibility workflow | `1b3137905c441d5f5fab52afe33599fdda2ced88` | Defines the axe hold and exact keyboard job. |
| Workflow regression tests | `f512c0d4cb57133e78c7e4738bc1a3c4ddd32e69` | Verifies workflow shape and the selected browser-spec contract. |
| Explorer manifest | `d9ada6539e07a4a5cd9b65ec9792105bd4856807` | Defines current browser-test scripts and pinned tool versions. |
| Playwright configuration | `03fddcd1f34e1e07bb499e01dfc3cdc7bd235f16` | Defines the local Vite fixture server and Chromium harness. |
| Accessibility-report README | `8b137891791fe96927ad78e64b0aad7bded08bdc` | Confirms the tracked report boundary is still empty. |

These identities describe the evidence snapshot at `main@bacb77cfbc04014a2c05da541f9cba8025629068`. Later revisions require fresh inspection.

## Changelog

### v1.1 — 2026-08-28

- removed unsupported canonical-doctrine and implemented-release-gate claims;
- replaced proposal-era paths and validation inventories with current repository evidence;
- documented the exact keyboard/focus smoke and the explicit axe hold;
- separated proposed targets from executable coverage and conformance;
- added commands, failure interpretation, maintenance guidance, and current evidence pins.

### v1 — 2026-05-15

- introduced draft accessibility commitments from external planning material before repository inspection;
- proposed release-gate, testing, reporting, and PDF/UA behavior that was not yet implemented.

[Back to top](#top)
