<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: Changed-file Audit — 2026-04-30
type: standard
version: v1
status: draft
owners: OWNER_TBD
created: 2026-04-30
updated: 2026-05-02
policy_label: NEEDS VERIFICATION
related: [docs/architecture/changed-file-audit-2026-04-30.md, apps/governed_api/server.py, tests/governed_api, apps/web/src/api/governedClient.js, apps/web/src/map, schemas/contracts/v1/ecology/layer_manifest.schema.json, data/published/ecology/dry-run/layer_manifest.json, .github/workflows]
tags: [kfm, audit, architecture, changed-files, governance, ecology, governed-api, web-ui]
notes: [Target path inferred from supplied rollback path, owners and policy label require repository verification, implementation findings preserve the supplied audit record and were not replayed during this Markdown revision.]
[/KFM_META_BLOCK_V2] -->

# Changed-file Audit — 2026-04-30

Audit artifact for files changed on 2026-04-30, focused on KFM trust-boundary alignment, validation blockers, and safe follow-up work.

> [!IMPORTANT]
> **Status:** Draft audit record  
> **Target path:** `docs/architecture/changed-file-audit-2026-04-30.md` — **INFERRED** from the supplied rollback path  
> **Truth posture:** **CONFIRMED** within the supplied audit record / **UNKNOWN** for current revalidation outside that checkout / **NEEDS VERIFICATION** for runtime, CI, schema-validation, and web-build outcomes

> [!NOTE]
> This document preserves the supplied audit’s reported checkout evidence. This Markdown revision did **not** replay the repository commands in a mounted KFM checkout. Treat current implementation behavior as **UNKNOWN** until the audit commands and validation steps are re-run in the target repository.

## Quick navigation

- [Scope](#scope)
- [Document fit](#document-fit)
- [Evidence boundary](#evidence-boundary)
- [Findings summary](#findings-summary)
- [Cross-file alignment matrix](#cross-file-alignment-matrix)
- [Validation backlog](#validation-backlog)
- [Minimal patch decision](#minimal-patch-decision)
- [Rollback](#rollback)
- [Appendix: reported evidence commands](#appendix-reported-evidence-commands)

---

## Scope

This audit records changed-file review for the 2026-04-30 workset and checks alignment against KFM invariants.

The review is intended to answer four narrow questions:

1. Which changed file families were reported by the audit?
2. Did the changed files appear to preserve governed API, public UI, evidence, schema, policy, and documentation boundaries?
3. Which checks were confirmed by the audit record?
4. Which checks remain blocked, unrun, or dependent on CI/runtime evidence?

## Document fit

| Field | Value |
| --- | --- |
| **Document role** | Architecture/control-plane audit artifact |
| **Inferred path** | `docs/architecture/changed-file-audit-2026-04-30.md` |
| **Upstream evidence** | Git history and command output from the 2026-04-30 audit record |
| **Downstream use** | Follow-up validation, CI artifact attachment, schema-validation confirmation, and rollback reference |
| **Primary audience** | KFM maintainers, reviewers, governance stewards, and implementation agents |

### Accepted inputs

This file may include:

- read-only git and repository inspection commands
- changed-file family summaries
- validation blockers
- cross-file alignment notes
- follow-up commands and expected evidence
- rollback instructions for this audit artifact
- links or references to CI job artifacts after verification

### Exclusions

This file must not include:

- secrets, tokens, private environment details, or source credentials
- unsupported claims that runtime behavior passed
- public-release approval language
- direct publication or promotion instructions
- claims that AI output, map tiles, summaries, or graph projections are root truth

## Evidence boundary

The supplied audit record reports the following as its evidence basis:

- git working-tree and branch commands
- changed-file and diff hygiene commands
- repository file discovery under expected KFM homes
- changed-file extraction from git history for 2026-04-30
- path-level inspection of governed API, web UI, schema/contract, docs, and workflow surfaces

The Markdown revision preserves those findings but does not upgrade them beyond the original evidence.

| Evidence item | Status | What it supports | What it does not prove |
| --- | --- | --- | --- |
| Supplied audit command list | **CONFIRMED** as supplied source content | The audit’s stated inspection method | That commands were replayed during this Markdown revision |
| Supplied findings summary | **CONFIRMED** as supplied source content | The audit’s reported repo alignment findings | Current repo state after later commits |
| Current Markdown revision | **PROPOSED** documentation improvement | Clearer structure, labels, rollback, and validation backlog | Runtime behavior, CI outcomes, dependency availability, or schema validation |
| CI artifacts for 2026-04-30 | **UNKNOWN** | Would confirm workflow outcomes if attached | Not available in the supplied Markdown |
| Web build/runtime evidence | **NEEDS VERIFICATION** | Would confirm UI behavior and app build health | Not executed in the supplied audit record |

## Audit flow

```mermaid
flowchart LR
    A[Git history for 2026-04-30] --> B[Changed-file set]
    B --> C[Cross-file boundary review]
    C --> D{Validation evidence}
    D -->|Available in audit record| E[CONFIRMED findings]
    D -->|Blocked or not executed| F[NEEDS VERIFICATION backlog]
    E --> G[Audit artifact]
    F --> G
    G --> H[Follow-up CI/runtime evidence]
```

## Truth labels

The supplied audit used `NEEDS_VERIFICATION`. This revision normalizes that label to **NEEDS VERIFICATION**.

| Label | Meaning in this audit |
| --- | --- |
| **CONFIRMED** | Reported as verified from repository files or command output in the supplied audit record. |
| **NEEDS VERIFICATION** | Requires dependency setup, CI evidence, runtime execution, schema validation, or artifact links before it can be treated as verified. |
| **UNKNOWN** | Not verifiable from the supplied audit record alone. |
| **PROPOSED** | Recommended follow-up, command, or documentation structure not yet verified as completed. |

## Findings summary

### CONFIRMED within the supplied audit record

- Changed files on 2026-04-30 were concentrated in governed API, web UI ecology surfaces, contracts/schema, tests, CI workflows, and doctrine docs.
- No uncommitted working-tree drift was reported after the audit commands.
- `git diff --check` reported no whitespace or patch hygiene failures.
- Governance-critical boundaries remained represented in the audited file paths:
  - governed API routes under `apps/governed_api`
  - ecology EvidenceBundle resolver boundary tests under `tests/governed_api`
  - public-safe map/evidence client boundaries under `apps/web/src/api` and `apps/web/src/map`

### NEEDS VERIFICATION

- Python governed API tests could not execute in the audited local environment because `fastapi` was not installed; collection failed before behavior assertions ran.
- End-to-end web app build/runtime validation was not executed in the supplied audit pass.
- Schema validation for the published ecology dry-run layer manifest should be executed and recorded.
- Workflow results for `.github/workflows/*.yml` changed on 2026-04-30 require CI artifact links or job IDs.

### UNKNOWN

- CI runtime outcomes for the 2026-04-30 changes are unknown from the supplied local checkout record alone.
- Current repository state after 2026-04-30 is unknown in this Markdown revision.
- Current dependency availability, package manager state, branch protections, deployment posture, dashboards, runtime logs, and emitted proof objects are unknown.

## Cross-file alignment matrix

| Changed file family | Related files inspected in supplied audit | Finding | Required patch | Status |
| --- | --- | --- | --- | --- |
| API/runtime + tests | `apps/governed_api/server.py`, `tests/governed_api/*.py` | Local environment lacked the FastAPI dependency, so governed API tests did not reach behavior assertions. | No repository code patch indicated by the supplied audit. Re-run tests in a provisioned environment. | **NEEDS VERIFICATION** |
| UI ecology + map adapters | `apps/web/src/ecology/*`, `apps/web/src/map/*`, `apps/web/src/api/governedClient.js` | No broken-file references were reported in the audited paths. | None indicated by supplied audit. | **CONFIRMED** within audit record |
| Schema/contract + published manifest | `schemas/contracts/v1/ecology/layer_manifest.schema.json`, `data/published/ecology/dry-run/layer_manifest.json` | No immediate path-level mismatch was reported. | Execute schema validation in CI or an equivalent provisioned environment. | **NEEDS VERIFICATION** |
| Docs/architecture + control-plane docs | `docs/architecture/*`, `docs/control-plane/*` | No direct contradiction was reported against the current governed API/layout in the audited pass. | None indicated by supplied audit. | **CONFIRMED** within audit record |
| CI/workflows | `.github/workflows/*.yml` changed on audit date | Workflow command execution was not replayed locally. | Verify workflow jobs from CI run artifacts and attach job IDs. | **NEEDS VERIFICATION** |

## KFM boundary check

| Boundary | Audit result | Follow-up |
| --- | --- | --- |
| `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED` | No lifecycle bypass was reported. | Reconfirm if changed files touch data promotion, published manifests, or release objects. |
| Public clients use governed interfaces | Public-safe API and map/evidence client boundaries were reported under `apps/web/src/api` and `apps/web/src/map`. | Confirm no direct canonical/internal-store access appears in web runtime paths. |
| EvidenceBundle before consequential claims | Ecology EvidenceBundle resolver boundary tests were reported under `tests/governed_api`. | Re-run governed API tests after dependencies are available. |
| Policy-aware fail-closed posture | No policy contradiction was reported in the audited pass. | Attach CI/policy validation evidence when available. |
| Derived surfaces are not root truth | No map/UI boundary violation was reported. | Keep map adapters downstream of governed API and released artifacts. |

## Validation backlog

> [!WARNING]
> The commands below are follow-up validation targets. They should be run only in the intended repository checkout or CI environment, with dependency setup and package-manager conventions verified first.

### 1. Governed API tests

```bash
pytest tests/governed_api -q
```

Expected evidence to attach after success:

- test command
- environment or CI job ID
- dependency installation source
- pass/fail output
- failure trace if any
- follow-up issue or patch reference if blocked

### 2. Ecology layer manifest schema validation

```bash
# PROPOSED: replace <repo-schema-validator> with the repository's established validation command.
<repo-schema-validator> \
  schemas/contracts/v1/ecology/layer_manifest.schema.json \
  data/published/ecology/dry-run/layer_manifest.json
```

Expected evidence to attach after success:

- validator command or workflow name
- schema path
- instance path
- pass/fail result
- validation artifact, if emitted

### 3. Web app tests and build

```bash
npm --prefix apps/web test
npm --prefix apps/web run build
```

Expected evidence to attach after success:

- package manager confirmation
- command output
- CI job ID or local environment note
- build artifact path, if produced
- runtime smoke-test notes, if executed

### 4. Workflow outcome capture

Attach CI evidence for workflow files changed on 2026-04-30.

| Evidence to capture | Status |
| --- | --- |
| Workflow names | **NEEDS VERIFICATION** |
| CI run URLs or job IDs | **NEEDS VERIFICATION** |
| Commit SHA tested | **NEEDS VERIFICATION** |
| Failed jobs, if any | **NEEDS VERIFICATION** |
| Retest after dependency fix | **NEEDS VERIFICATION** |

## Minimal patch decision

**Applied patch:** add this audit artifact only.

**Why minimal and safe:** the audit records observed evidence, unresolved validation blockers, and follow-up checks without changing runtime behavior, policy gates, source registries, schema authority, public UI paths, or publication state.

**Governance impact:** documentation-only. No data promotion, release, publication, connector activation, or AI behavior change is implied.

## Rollback

Rollback is appropriate if this artifact is superseded, contains inaccurate findings, weakens trust-boundary clarity, or causes maintainers to treat unverified runtime behavior as confirmed.

> [!CAUTION]
> Run rollback commands only in the intended repository checkout.

If committed:

```bash
git revert <commit>
```

If not yet committed:

```bash
git rm docs/architecture/changed-file-audit-2026-04-30.md
```

Rollback target: `docs/architecture/changed-file-audit-2026-04-30.md`

## Suggested follow-up actions

1. Install governed API test dependencies in CI or a provisioned local environment and run `pytest tests/governed_api -q`.
2. Validate `data/published/ecology/dry-run/layer_manifest.json` against `schemas/contracts/v1/ecology/layer_manifest.schema.json`.
3. Execute the web test/build checks after confirming the repository’s package-manager convention.
4. Confirm `.github/workflows/*.yml` outcomes from 2026-04-30 CI artifacts and attach job IDs to this audit.
5. Update this audit with validation receipts or supersede it with a follow-up audit if later commits materially change the evidence boundary.

## Appendix: reported evidence commands

<details>
<summary>Expand the supplied Phase 0 command list</summary>

```bash
pwd
git status --short
git branch --show-current
git rev-parse HEAD
git diff --name-only --diff-filter=ACMRTUXB
git diff --stat
git diff --check
find .github docs contracts schemas policy data tools tests apps packages pipelines migrations configs release -maxdepth 4 -type f
git log --since="today 00:00" --name-only --pretty=format: | sed '/^$/d' | sort -u
```

</details>

## Appendix: review checklist

- [ ] Confirm target path and owners.
- [ ] Confirm this audit still matches the commit SHA it describes.
- [ ] Attach governed API test result after dependency setup.
- [ ] Attach schema-validation result for the ecology dry-run layer manifest.
- [ ] Attach web test/build result or explain why not applicable.
- [ ] Attach CI workflow job IDs for changed workflow files.
- [ ] Confirm no public client bypasses governed interfaces.
- [ ] Confirm no documentation wording upgrades **NEEDS VERIFICATION** items to **CONFIRMED**.
- [ ] Confirm rollback target remains valid.
