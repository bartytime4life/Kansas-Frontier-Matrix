# `.github`

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
