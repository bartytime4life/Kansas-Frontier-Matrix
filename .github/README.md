# `.github`

GitHub-facing repository controls for review flow, CI/CD gates, and governed contribution paths.

> [!IMPORTANT]
> **Status:** PROPOSED directory README  
> **Path:** `.github/`  
> **Verification state:** The live `.github/` subtree is **UNKNOWN** in this session. This draft is aligned to KFM’s documented repo shape and governance posture, but exact files, owners, badge targets, and local conventions still need repo-tree verification.

**Status:** PROPOSED  
**Owners:** UNKNOWN  
**Badges:** TODO-build-status · TODO-policy-gates · TODO-docs-version · TODO-review-boundaries  
**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Expected surfaces](#expected-surfaces-proposed) · [Review checks](#review-checks) · [Definition of done](#definition-of-done) · [Verification notes](#verification-notes)

## Scope

This directory is the GitHub-side control surface for repository-wide automation and contribution flow.

In KFM terms, `.github/` should reinforce the project’s documented trust posture at the repository boundary by making review, validation, promotion, and contributor expectations visible and enforceable.

## Repo fit

**Repository path:** `.github/`

**Upstream context**
- [`../docs/`](../docs/) for architecture, governance, runbooks, and operating guidance
- [`../contracts/`](../contracts/) for machine-checked schemas and API contracts
- [`../policy/`](../policy/) for policy-as-code and policy test fixtures
- [`../data/`](../data/) for truth-path artifacts, registry entries, and release-boundary data products

**Downstream impact**
- Pull request quality and review discipline
- CI/CD enforcement for docs, schemas, policy, contracts, and release gates
- Contributor experience for issues, PRs, and release-significant changes
- Protection against undocumented bypasses of governance, evidence, and publication controls

## Accepted inputs

The following kinds of repo-wide GitHub concerns belong here:

- CI workflow definitions and workflow support files
- issue templates, discussion prompts, and pull request templates
- ownership and review-routing controls
- security-reporting entry points and related repository health configuration
- release and promotion automation that remains inside governed review boundaries

## Exclusions

The following do **not** belong here as their primary home:

| Out of scope for `.github/` | Put it here instead |
|---|---|
| Canonical data artifacts, raw captures, processed outputs, or catalog triplets | [`../data/`](../data/) |
| API schemas, JSON Schemas, vocabulary contracts, and interface definitions | [`../contracts/`](../contracts/) |
| Policy logic, fixtures, and authoritative policy rules | [`../policy/`](../policy/) |
| System doctrine, architecture manuals, ADRs, and runbooks | [`../docs/`](../docs/) |
| Runtime application code | [`../apps/`](../apps/) |
| Reusable implementation libraries | [`../packages/`](../packages/) |

## Why this directory matters

KFM’s trust membrane is not only a runtime concern.

If repository automation allows undocumented merge paths, unreviewed promotion behavior, or inconsistent contributor requirements, the runtime trust posture will drift. This directory should therefore support the same core rules documented elsewhere in KFM:

- truth-path discipline over convenience shortcuts
- fail-closed behavior when checks, evidence, or policy expectations are missing
- cite-or-abstain expectations for claim-bearing surfaces
- separation of duty for policy-significant review and release actions
- documentation updates when behavior-significant process changes land

## Expected surfaces (PROPOSED)

Because the live subtree was not directly visible, the list below is intentionally framed as an expected, repo-native baseline rather than a claim about current file presence.

| Surface | Role in KFM | Notes |
|---|---|---|
| `workflows/` | CI/CD and governed release checks | Expected home for docs checks, schema checks, policy checks, integration checks, and release gates |
| `ISSUE_TEMPLATE/` or equivalent | Contributor intake | Useful for dataset requests, bug reports, policy questions, and workflow-safe change proposals |
| `PULL_REQUEST_TEMPLATE.md` or equivalent | Review discipline | Should prompt for scope, evidence impact, policy impact, docs updates, and rollback notes |
| `CODEOWNERS` or equivalent ownership routing | Review boundaries | Helps preserve separation of duty and explicit stewardship paths |
| Security/community health files | Public-facing repo guidance | Useful for security reporting, contribution expectations, and review clarity |

## Operating rules for changes under `.github/`

A change in this directory should make the repository easier to change **safely**, not merely easier to change.

A strong change here usually does one or more of the following:

- makes a required gate clearer
- tightens review routing or ownership boundaries
- improves contributor instructions without weakening controls
- blocks invalid publication paths earlier
- keeps docs, contracts, policy, and automation aligned

A weak change here usually does the opposite:

- adds convenience while hiding evidence or policy requirements
- creates a quiet bypass around review or release discipline
- duplicates governance logic that belongs in authoritative policy or contract layers
- changes contributor expectations without updating the written guidance

## Review checks

Before merging a `.github/` change, review against these questions:

- Does this preserve the truth-path and trust-membrane posture?
- Does it fail closed when required checks or artifacts are missing?
- Does it change contributor behavior, and if so, are the instructions updated too?
- Does it introduce or weaken any review boundary?
- Does it imply release or promotion behavior that is not documented elsewhere?
- Are all referenced paths, commands, and expected checks verified against the live repository?

## Definition of done

A `.github/` change is ready when:

- the workflow or template matches the live repository layout
- required checks are understandable and intentionally scoped
- contributor prompts reflect actual review and release expectations
- no GitHub-side automation creates an undocumented bypass around policy, evidence, or publication controls
- related docs are updated when behavior-significant process changes land

## Verification notes

The following items remain **UNKNOWN** until the live repo is inspected:

- exact files currently present under `.github/`
- whether `CODEOWNERS` exists and how ownership is routed
- the actual workflow inventory and merge-blocking checks
- whether badges are already used in adjacent README-style files at this path
- the correct owners for this directory-level README
- whether additional community health files already exist here

If this draft is adopted, those values should be replaced with confirmed repo-native details before merge.

[Back to top](#github)
