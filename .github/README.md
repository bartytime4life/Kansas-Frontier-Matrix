# `.github`

GitHub-native control plane for workflows, templates, ownership routing, required-check synchronization, and merge discipline.

> **Status:** active working control-plane README  
> **Owners:** [@bartytime4life](https://github.com/bartytime4life)  
> **Badges:** ![Repo](https://img.shields.io/badge/repo-Kansas--Frontier--Matrix-0b3d91) ![Path](https://img.shields.io/badge/path-.github-1f6feb) ![Scope](https://img.shields.io/badge/scope-GitHub%20control%20plane-8250df) ![Posture](https://img.shields.io/badge/posture-evidence--first-238636)  
> **Quick jump:** [Purpose](#purpose) · [Repo fit](#repo-fit) · [Current snapshot](#current-visible-control-plane-snapshot) · [Control-plane contract](#control-plane-contract) · [Quickstart](#quickstart) · [Definition of done](#definition-of-done) · [FAQ](#faq)

---

## Purpose

This directory is the repository’s GitHub-facing control plane.

It exists to define and coordinate the parts of the project that govern contribution flow, review routing, automation entrypoints, merge discipline, and repository health from the GitHub side. It is where maintainers look to understand how pull requests are shaped, how issue and discussion intake is structured, how ownership is routed, how workflows are organized, and how GitHub-native checks relate to KFM’s broader governed release model.

This directory is **not** the place where canonical data truth, publication evidence, runtime policy enforcement, or user-facing product behavior originate. Those belong elsewhere in the system and must remain downstream of governed APIs, evidence resolution, and promotion discipline.

[Back to top](#github)

## Evidence posture

KFM documentation is strongest when it keeps current evidence, target-state design, and unknowns visibly separate.

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Directly visible in the current repository surface or strongly established by the project’s mounted doctrine |
| **PROPOSED** | Recommended directory behavior or maintenance rule that fits repo doctrine but is not proven here as enforced in all GitHub settings |
| **UNKNOWN** | Not directly verifiable from the visible repository surface or attached evidence in the current session |

### Directory posture

| Area | Posture |
|---|---|
| `.github/` tree, file presence, and current README role | **CONFIRMED** |
| Ownership routing through `CODEOWNERS` for this directory | **CONFIRMED** |
| Out-of-repo GitHub settings such as branch protection, rulesets, merge queue, environment approvals, and required-check enforcement details | **UNKNOWN** |
| Recommended discipline for keeping merge checks aligned to KFM trust posture | **PROPOSED** |

## Repo fit

| Field | Value |
|---|---|
| **Path** | `.github/` |
| **Repo role** | GitHub-native control plane for contribution, review, and merge governance |
| **Upstream dependencies** | Root repo doctrine, contribution rules, ownership rules, workflow definitions, issue/PR/discussion templates |
| **Downstream effects** | PR behavior, issue intake quality, maintainer routing, merge blocking, review consistency, contributor ergonomics |

### Closely related docs

- [`../README.md`](../README.md) — project-wide identity, architecture posture, and current repo snapshot
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — contributor contract and change expectations
- [`./CODEOWNERS`](./CODEOWNERS) — ownership routing for paths in the repository
- [`./PULL_REQUEST_TEMPLATE.md`](./PULL_REQUEST_TEMPLATE.md) — contributor-facing merge checklist surface
- [`./ISSUE_TEMPLATE/`](./ISSUE_TEMPLATE/) — structured issue intake
- [`./DISCUSSION_TEMPLATE/`](./DISCUSSION_TEMPLATE/) — structured discussion intake
- [`./workflows/`](./workflows/) — GitHub Actions workflow entrypoints
- [`./actions/`](./actions/) — reusable local GitHub Actions building blocks
- [`./required-checks.v1.json`](./required-checks.v1.json) — versioned check inventory surface, if used by repository governance tooling

## Scope

This directory should contain GitHub-native repository governance and automation surfaces such as:

- workflow definitions
- reusable GitHub Actions
- issue, discussion, and pull-request templates
- ownership routing files
- support or code-of-conduct documents
- repository-facing merge or check metadata
- other GitHub control-plane assets that shape contribution and review behavior

## Accepted inputs

Material belongs here when it answers one of these questions:

- How does work enter the repository through GitHub?
- How does GitHub route review and ownership?
- How are checks, workflows, and merge expectations expressed?
- How do contributors know what information to provide in issues and PRs?
- How do maintainers keep GitHub automation aligned with KFM governance?

## Exclusions

The following do **not** belong here:

- application runtime business logic
- canonical dataset schemas for domain data
- evidence bundles or publication artifacts
- API implementation code
- frontend product components
- environment-specific deployment manifests unless they are strictly GitHub automation inputs
- policy enforcement that must execute inside governed runtime paths rather than GitHub merge checks

### Boundary rule

GitHub merge discipline is important, but it is **not** the same thing as KFM publication governance.

A passing pull request may still be insufficient for release if runtime evidence, policy review, catalog closure, or promotion proofs are incomplete.

## Current visible control-plane snapshot

The visible repository surface shows `.github/` already functioning as a real control-plane directory rather than a placeholder. Current visible contents include discussion templates, issue templates, pull-request templates, reusable actions, workflows, ownership routing, support files, and this README. That makes this directory part of the repo’s maintained operating surface, not just scaffolding.

### Confirmed visible inventory

```text
.github/
├── DISCUSSION_TEMPLATE/
├── ISSUE_TEMPLATE/
├── PULL_REQUEST_TEMPLATE/
├── actions/
├── workflows/
├── CODEOWNERS
├── CODE_OF_CONDUCT.md
├── PULL_REQUEST_TEMPLATE.md
├── README.md
├── SUPPORT.md
├── dependabot.yml
├── labeler.yml
└── required-checks.v1.json
```

### What this snapshot means

| Item | Why it matters |
|---|---|
| Templates directories are present | Intake and review discipline are already structured at the GitHub boundary |
| `actions/` and `workflows/` are present | Automation is organized as reusable GitHub-native components, not only ad hoc workflow steps |
| `CODEOWNERS` is present | Ownership routing is explicit and review responsibility can be enforced or inspected |
| `required-checks.v1.json` is present | The repo appears to reserve a versioned surface for merge-check inventory, though live enforcement details remain **UNKNOWN** |
| `README.md` is present in `.github/` | This directory is documented as a first-class repo surface |

## Verification boundary

This README should stay honest about what it can and cannot prove from the visible repository surface.

### Confirmed here

- `.github/README.md` exists and already serves as a control-plane guide
- `.github/` contains templates, workflows, reusable actions, and governance-adjacent files
- `CODEOWNERS` currently routes `/.github/*` to `@bartytime4life`
- the repo’s root docs already treat documentation and governance surfaces as operational, not decorative

### Unknown here

- the exact set of merge-blocking checks configured in GitHub settings
- whether `required-checks.v1.json` is actively consumed by automation or only reserved for future/partial use
- exact ruleset, branch protection, merge queue, or environment-approval configuration
- whether every workflow currently listed under `.github/workflows/` is active, required, or advisory
- the live relationship between GitHub-side checks and any off-platform release approval mechanisms

### Safe authoring rule

When this README refers to enforcement, treat GitHub-visible files as the source of truth for file-based control surfaces, and treat anything configured only in GitHub settings as **UNKNOWN** unless directly inspected and documented.

## Control-plane contract

### What `.github/` is authoritative for

| Control surface | Authoritative here? | Notes |
|---|---:|---|
| PR/issue/discussion intake structure | Yes | Templates and docs in this directory define the GitHub-side contributor path |
| Ownership routing for GitHub review | Yes | `CODEOWNERS` is the visible routing surface |
| Workflow entrypoint definitions | Yes | Workflow YAML lives here |
| Reusable local GitHub Actions | Yes | Action definitions in `actions/` live here |
| Merge-check intent documentation | Yes | This directory can describe expected checks and review posture |
| Release approval beyond GitHub merge | No | Must remain governed by broader KFM release evidence and verification |
| Runtime policy enforcement | No | Must remain inside governed backend/control-plane paths |
| Canonical publication truth | No | Never relocate release truth into `.github/` convenience files |

### Merge gate vs publication gate

| Gate type | Primary home | Purpose | Must never be confused with |
|---|---|---|---|
| **Merge gate** | `.github/` + GitHub settings | Blocks unsafe or incomplete changes from merging | Proof that a dataset, story, or runtime answer is publishable |
| **Publication gate** | KFM lifecycle, policy, review, and release artifacts | Governs whether something may become user-visible | A normal CI pass |

### Required-check synchronization rule

If this repository uses a versioned required-check inventory file, it should be kept synchronized with three things:

1. workflow reality  
2. branch/ruleset reality  
3. contributor-facing documentation  

That means the control-plane contract should never drift into one of these failure modes:

| Failure mode | Why it is bad |
|---|---|
| README promises checks that workflows no longer provide | Contributors prepare for the wrong gate |
| Workflows run checks that branch protection does not require | Trust posture looks stronger than it is |
| Branch protection requires checks that docs do not explain | Contributors hit opaque merge friction |
| Check names drift without versioned coordination | Merge discipline becomes brittle and confusing |

### Review-routing rule

Ownership routing should stay explicit, path-based, and boring.

If a path matters enough to block or shape release quality, it should usually have a clear owner in `CODEOWNERS`, and the corresponding documentation should make that responsibility legible to contributors.

### Control-plane flow

```mermaid
flowchart LR
    A[Contributor change] --> B[Issue / Discussion / PR intake]
    B --> C[Template-guided context]
    C --> D[Ownership routing via CODEOWNERS]
    D --> E[Workflow execution]
    E --> F[Required checks / review outcomes]
    F --> G[Merge decision]
    G --> H[Repository state changes]

    H --> I[Downstream governed build / publish systems]
    I -. not owned by .github .-> J[KFM release evidence and publication gates]
```

## CI baseline

A healthy `.github/` control plane usually makes the expected merge checks obvious even when the exact active set evolves.

### Default check classes this directory should help coordinate

1. documentation and link integrity
2. lint, format, and type discipline
3. policy/config validation where relevant
4. schema/contract validation where relevant
5. test execution for changed code paths
6. contributor-facing review signals for high-risk changes

### What good checks look like

| Check quality | Good | Weak |
|---|---|---|
| Naming | Stable and human-readable | Renamed casually, hard to track in rulesets |
| Scope | Matches real risk surface | Too broad or too narrow to be meaningful |
| Failure output | Tells contributor what to fix | Emits generic red X with no next step |
| Ownership | Clear maintainer responsibility | No clear owner for flaky or obsolete checks |
| Docs fit | Reflected in contributor docs and templates | Hidden in workflow YAML only |

### Important distinction

Checks in `.github/` should support KFM’s fail-closed posture, but they should not impersonate domain truth.

A CI pass can verify structure, policy packs, fixtures, and smoke paths. It cannot by itself prove that public claims are evidence-safe unless the broader KFM verification and publication artifacts also exist and pass.

## Automation safety

GitHub automation is useful when it reduces ambiguity. It is harmful when it hides authority, invents state, or silently escalates privileges.

### Safe defaults

- prefer explicit PR-based changes over direct protected-branch mutation
- keep automation outputs reviewable
- pin or version important automation surfaces where practical
- separate advisory automation from merge-blocking automation
- keep evidence-bearing release steps outside undocumented convenience scripts

### Unsafe patterns to avoid

- automation that changes policy-significant files without clear review routing
- templates that imply approval rather than collect evidence for approval
- workflows that publish or expose artifacts without documented release evidence
- bots that make repository state appear more verified than current evidence supports

## Quickstart

### Inspect the control plane

```bash
git rev-parse --show-toplevel
find .github -maxdepth 2 -type f | sort
sed -n '1,220p' .github/README.md
sed -n '1,220p' .github/CODEOWNERS
```

### Inspect workflow entrypoints

```bash
find .github/workflows -maxdepth 1 -type f | sort
grep -R "name:" .github/workflows
```

### Inspect template surfaces

```bash
find .github/ISSUE_TEMPLATE -maxdepth 2 -type f | sort
find .github/DISCUSSION_TEMPLATE -maxdepth 2 -type f | sort
find .github/PULL_REQUEST_TEMPLATE -maxdepth 2 -type f | sort
sed -n '1,220p' .github/PULL_REQUEST_TEMPLATE.md
```

### Inspect ownership routing for this directory

```bash
grep -n "/.github" .github/CODEOWNERS
```

### Inspect required-check inventory surface

```bash
ls -l .github/required-checks.v1.json
sed -n '1,220p' .github/required-checks.v1.json
```

> **CAUTION**  
> A visible file inventory does not prove active GitHub settings. Use it to inspect repo-native control surfaces, not to overclaim live enforcement.

## Change discipline

Changes under `.github/` should be treated as control-plane changes, not as casual housekeeping.

### When changing workflows

Check all of the following:

- does the workflow still match contributor-facing docs?
- do names remain stable enough for required-check wiring?
- did risk coverage change in a way that should update templates or README guidance?
- did any privilege boundary or token usage change?

### When changing templates

Check all of the following:

- does the template still collect the information required for safe review?
- did it remove evidence that a reviewer depends on?
- does it match current repo terminology?
- does it push contributors toward the right adjacent docs?

### When changing `CODEOWNERS`

Check all of the following:

- are path patterns correct and non-overlapping enough to be predictable?
- did a critical path lose an explicit owner?
- should README guidance change because ownership routing changed?

### When changing `.github/README.md`

Check all of the following:

- are current visible files and ownership still described accurately?
- are merge gates still clearly separated from publication gates?
- are out-of-repo GitHub settings still marked as **UNKNOWN** when not directly verified?
- does the doc still feel native to the repo’s current style?

### Recommended change bundle for higher-risk edits

For any non-trivial `.github/` change, bundle these together when applicable:

- the file change itself
- any corresponding template or doc update
- any corresponding ownership-routing change
- any corresponding required-check inventory change
- a short PR explanation of what governance or contributor behavior changed

### Failure patterns to watch

| Pattern | Why it hurts |
|---|---|
| Workflow renamed without doc update | Contributors and branch protection drift apart |
| Template simplified too far | Review quality drops before anyone notices |
| Ownership routing left implicit | High-risk paths lose accountability |
| README overstates GitHub enforcement | Repo appears more governed than current evidence proves |
| GitHub-side checks treated as full release proof | Trust membrane and publication discipline get weakened |

## Definition of done

A revision to `.github/README.md` is ready when all of the following are true:

- the file reflects the current visible `.github/` structure
- ownership statements match current `CODEOWNERS`
- merge-gate language is clearly separated from broader KFM publication governance
- unknown GitHub settings are not presented as facts
- quickstart commands still match the visible directory
- no section is visually dead, stale, or generic
- adjacent docs do not materially contradict this file

## FAQ

### Is `.github/` the source of truth for KFM release governance?

No. It is the GitHub-side control plane for contribution, review, and merge behavior. KFM release governance still depends on evidence, policy, verification, and publication artifacts outside this directory.

### Does a passing PR mean something is publishable?

Not by itself. A passing PR means the repository-side gate passed. Publication still depends on the broader KFM trust path.

### Should runtime policy live in GitHub workflows?

No. Workflows can validate policy files, fixtures, and expected structure, but runtime policy enforcement must remain in governed runtime/control-plane paths.

### Why keep this README at all if GitHub surfaces are visible in the UI?

Because file presence is not enough. Contributors and maintainers still need one repo-native explanation of what this directory governs, what it does not govern, and how it fits into KFM’s broader evidence-first architecture.

## Appendix

<details>
<summary><strong>Minimal maintenance checklist</strong></summary>

Before merging a `.github/` change, verify:

- visible file tree still matches this README
- `CODEOWNERS` entries still reflect intended review routing
- templates still point contributors toward current repo language
- workflow names and expectations are still coherent
- no new language implies runtime or publication guarantees this directory cannot actually prove

</details>

<details>
<summary><strong>Suggested PR notes for `.github/` changes</strong></summary>

Use a short PR note that answers:

1. what control-plane surface changed  
2. why the change was needed  
3. what contributor or maintainer behavior changes as a result  
4. whether ownership routing, workflow names, or required-check expectations changed  
5. whether adjacent docs were updated in the same change set  

</details>

[Back to top](#github)
