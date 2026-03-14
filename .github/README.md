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

[Back to top](#github)# `.github`

Repo-level automation, review boundaries, and contributor-facing GitHub surfaces for Kansas Frontier Matrix.

> **Status:** `PROPOSED` directory README  
> **Confirmed role:** repo workflows, templates, and ownership controls  
> **Working posture:** keep GitHub-side automation aligned with KFM’s evidence-first, fail-closed, governed delivery model

## Quick navigation

- [Project overview](../README.md)
- [Documentation](../docs/)
- [Contracts](../contracts/)
- [Policy](../policy/)
- [Data](../data/)
- [Apps](../apps/)
- [Packages](../packages/)
- [Infrastructure](../infra/)
- [Workflows](./workflows/)

## Scope

This directory is the GitHub-facing control surface for the repository.

It should hold the repo-level files that shape how work is proposed, reviewed, validated, and promoted, including:

- CI/CD workflow definitions
- issue and pull request templates
- review-boundary and ownership controls
- GitHub-side automation for release hygiene, provenance checks, or repo health
- contributor guidance that is specifically about GitHub workflow behavior

## Repo fit

**Path:** `.github/`

**Depends on**
- project doctrine and architecture in [`../README.md`](../README.md) and [`../docs/`](../docs/)
- machine-readable contracts in [`../contracts/`](../contracts/)
- policy logic and fixtures in [`../policy/`](../policy/)
- dataset, source, and catalog expectations in [`../data/`](../data/)

**Affects**
- pull request quality and merge safety
- release and promotion gates
- contributor onboarding and review ergonomics
- provenance, verification, and attestation workflow behavior
- protection against trust-membrane bypass through repository automation

## Accepted inputs

The following concerns belong here when they are repo-wide and GitHub-mediated:

| Area | Purpose | Typical contents |
|---|---|---|
| Workflow automation | Build, test, validate, publish, and promote safely | CI jobs, release jobs, policy checks, docs checks, catalog checks |
| Contributor intake | Make requests reviewable and triageable | issue forms, issue templates, discussion prompts |
| Pull request structure | Standardize what reviewers must see before merge | evidence summaries, checklist items, rights/sensitivity prompts, release-impact prompts |
| Ownership and review routing | Keep approval boundaries explicit | ownership files, reviewer routing, protected-boundary guidance |
| Repo-health automation | Improve repeatability without weakening doctrine | dependency automation, release drafting, security-reporting entry points |

## Exclusions

The `.github/` directory is not where KFM’s canonical truth or domain logic should live.

| Keep out of `.github/` | Put it here instead |
|---|---|
| Dataset specs, source descriptors, and catalog artifacts | [`../data/`](../data/) |
| API schemas and machine contracts | [`../contracts/`](../contracts/) |
| Policy rules and fixture packs | [`../policy/`](../policy/) |
| Architecture docs, runbooks, ADRs, and doctrine manuals | [`../docs/`](../docs/) |
| Application or package implementation code | [`../apps/`](../apps/) and [`../packages/`](../packages/) |
| Canonical release artifacts and evidence bundles | governed data and release paths, not repository metadata folders |

## Directory contract

A good `.github/` change in KFM should make the repository easier to change **safely**, not merely easier to change.

That usually means it does one or more of these well:

- tightens a review boundary
- makes required proof or receipt expectations visible earlier
- blocks invalid publication paths sooner
- improves contributor clarity without weakening controls
- keeps documentation, policy, and automation in sync

A weak `.github/` change usually does the opposite:

- adds convenience while hiding evidence requirements
- loosens review around policy-significant or release-significant changes
- duplicates logic that belongs in governed backend or policy code
- silently changes merge or release behavior without updating contributor-facing guidance

## Typical surfaces in this directory

### Confirmed core role

The mounted project evidence supports `.github/` as the home for repository workflows, templates, and ownership controls.

### Expected GitHub responsibilities

In KFM, repository automation should help enforce these concerns where they apply:

1. contract and schema validation  
2. policy and fixture tests  
3. catalog and link integrity checks  
4. evidence-resolution and citation-safe publishing checks  
5. public-surface quality gates, including accessibility-sensitive paths  
6. release or promotion checks that require receipts, manifests, or equivalent proof objects  
7. contributor prompts that capture enough context for review, especially around data, policy, and publication changes  

## How `.github/` supports the trust model

KFM’s trust membrane is not only an API concern. It is also a repository concern.

If merge-time automation allows undocumented bypasses, missing evidence, broken policy gates, or casual release behavior, the runtime trust posture will eventually drift. This directory should therefore reinforce the same core rules that appear elsewhere in the system:

- public or release-significant behavior should be gated
- broken evidence paths should fail closed
- policy-significant changes should be reviewable
- contributor prompts should surface rights, sensitivity, and publication implications early
- repo automation should never become a quiet shortcut around governed release discipline

## Change workflow through this directory

1. Open or update work through the correct GitHub intake surface.
2. Let workflow gates evaluate formatting, contracts, policy, and release-relevant checks.
3. Route review through the appropriate ownership boundary.
4. Merge only when both automation and required human approvals pass.
5. Update contributor-facing guidance whenever merge or release behavior changes.

## Review prompts for `.github/` changes

Before merging a change under `.github/`, check these questions:

- Does this strengthen or weaken the trust membrane?
- Does it make fail-closed behavior clearer or more ambiguous?
- Does it introduce any path that could expose unpublished, unevidenced, or policy-unsafe state?
- Are contributor prompts still aligned with the actual checks and review boundaries?
- If merge or release behavior changed, were the user-facing instructions updated too?
- Were all referenced paths, filenames, and invoked checks verified against the live tree?

## Definition of done

A `.github/` change is ready when:

- the automation matches the live repository layout
- required checks are intentional and understandable
- contributor prompts reflect current review and release expectations
- no repo automation creates a shortcut around policy, evidence, or publication discipline
- adjacent documentation has been updated when behavior-significant expectations changed

## Maintainer note

This README is intentionally conservative.

The directory role is stable, but exact filenames, workflow inventory, template coverage, and optional GitHub-side controls should be verified against the live tree before this file is treated as fully ratified.
