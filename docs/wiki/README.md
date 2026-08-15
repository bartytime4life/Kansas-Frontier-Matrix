<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/wiki-source/readme
title: docs/wiki — GitHub Wiki Source Set
type: readme
version: v0.2.0
status: proposed; review-required; not-native-wiki-published
owners: ["@bartytime4life"]
created: 2026-08-07
updated: 2026-08-14
policy_label: public-documentation
current_path: docs/wiki/README.md
owning_root: docs/
responsibility: reviewable source for the public GitHub Wiki orientation pages
truth_posture: cite-or-abstain; canonical repository evidence and adopted authority outrank the wiki
related:
  - ../../README.md
  - ../README.md
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../CONTRIBUTING.md
  - Wiki-Maintenance.md
  - ../../tools/docs/wiki/README.md
  - ../../data/receipts/generated/README.md
notes:
  - "The native GitHub Wiki is a separate Git repository and is not a KFM authority root."
  - "This source set creates no release, deployment, data publication, policy, evidence, or lifecycle state."
  - "Native-wiki synchronization remains a separate reviewed action."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/wiki/` — GitHub Wiki source set

> **One-line purpose.** Maintain KFM's public-facing wiki pages as reviewable Markdown in the main repository, then project an explicitly reviewed page set into the separate native GitHub Wiki only through a bounded synchronization step.

> [!IMPORTANT]
> The native wiki is an **orientation projection**, not a second doctrine, contract, schema, policy, evidence, release, or publication authority. A polished page, diagram, badge, commit, pull request, merge, or wiki push does not establish factual truth or promote KFM data.

## At a glance

| Need | Start here |
|---|---|
| Public reader entry point | [`Home.md`](Home.md) |
| First-time orientation | [`Getting-Started.md`](Getting-Started.md) |
| Evidence-bounded project state | [`Project-Status.md`](Project-Status.md) |
| Source/projection maintenance contract | [`Wiki-Maintenance.md`](Wiki-Maintenance.md) |
| Native-wiki synchronization helper | [`tools/docs/wiki/`](../../tools/docs/wiki/README.md) |
| Native page navigation | [`_Sidebar.md`](_Sidebar.md) and [`_Footer.md`](_Footer.md) |
| Canonical KFM authority | Main-repository evidence, adopted doctrine, accepted ADRs, and the owning responsibility roots |
| Native-wiki publication state | **Not established by this README or by a source-only pull request** |

## Purpose

GitHub stores a repository wiki in a separate `<repository>.wiki.git` repository. That surface does not participate in the main repository's normal pull-request review flow. KFM therefore keeps the source packet in `docs/wiki/` so changes can be inspected, reviewed, corrected, and rolled back before any native-wiki synchronization.

This directory owns the **human-facing wiki source packet**. It does not own the implementation, evidence, policy, data lifecycle, release, or publication records that the pages explain.

Canonical entry points remain in the main repository:

- repository identity and current entry points: [`README.md`](../../README.md);
- documentation map: [`docs/README.md`](../README.md);
- placement authority: [Directory Rules](../doctrine/directory-rules.md), adopted by [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md);
- contribution workflow: [`CONTRIBUTING.md`](../../CONTRIBUTING.md);
- synchronization behavior and operator safeguards: [`tools/docs/wiki/README.md`](../../tools/docs/wiki/README.md).

## Start here by audience

| Audience | Recommended path |
|---|---|
| New reader | [`Home.md`](Home.md) → [`Getting-Started.md`](Getting-Started.md) → [`Project-Status.md`](Project-Status.md) |
| Architecture or evidence reviewer | [`Architecture.md`](Architecture.md) → [`Governance-and-Evidence.md`](Governance-and-Evidence.md) → [`Data-Lifecycle.md`](Data-Lifecycle.md) |
| Domain or experience reviewer | [`Domains.md`](Domains.md) → [`Map-UI-and-AI.md`](Map-UI-and-AI.md) → [`Security-and-Sensitivity.md`](Security-and-Sensitivity.md) |
| Contributor | [`Repository-Map.md`](Repository-Map.md) → [`Development-and-Validation.md`](Development-and-Validation.md) → [`Contributing.md`](Contributing.md) |
| Wiki maintainer | [`Wiki-Maintenance.md`](Wiki-Maintenance.md) → [`tools/docs/wiki/README.md`](../../tools/docs/wiki/README.md) |

## Authority boundary

| Concern | Owning source | Wiki role |
|---|---|---|
| Repository identity and current implementation evidence | Main-repository bytes, tests, workflows, manifests, logs, and artifacts at a known revision | Summarize and link; never replace |
| KFM-wide invariants | `docs/doctrine/` and accepted ADRs | Explain in accessible language |
| Object meaning, shape, admissibility, and enforceability | `contracts/`, `schemas/`, `policy/`, `tests/`, and `fixtures/` | Point readers to the owning surface |
| Lifecycle records, evidence, receipts, proofs, and catalogs | Governed `data/` lanes | Never host or elevate |
| Release, correction, withdrawal, and rollback decisions | `release/` | Link to reviewed records when public-safe |
| This directory | `docs/wiki/` | Reviewable source and maintenance contract |
| Native GitHub Wiki | `<repository>.wiki.git` | Derived public orientation target after separate review and synchronization |

Wiki pages use KFM's core truth labels:

| Label | Reader meaning |
|---|---|
| `CONFIRMED` | Supported by current repository evidence or adopted authority inspected for the claim |
| `PROPOSED` | A recommended design or future state, not verified as current implementation |
| `UNKNOWN` | Available evidence is insufficient |
| `NEEDS VERIFICATION` | A concrete check remains before the claim can be relied upon |

## Page inventory

### Orientation

| Source page | Purpose |
|---|---|
| [`Home.md`](Home.md) | Public landing page and project orientation |
| [`Getting-Started.md`](Getting-Started.md) | Reader and contributor onboarding |
| [`Project-Status.md`](Project-Status.md) | Evidence-bounded implementation snapshot |

### System and governance

| Source page | Purpose |
|---|---|
| [`Architecture.md`](Architecture.md) | Connected operating model and trust membrane |
| [`Repository-Map.md`](Repository-Map.md) | Responsibility-root map and placement guidance |
| [`Governance-and-Evidence.md`](Governance-and-Evidence.md) | Truth labels, evidence closure, promotion, and correction |
| [`Data-Lifecycle.md`](Data-Lifecycle.md) | RAW-to-PUBLISHED lifecycle and accountability lanes |

### Knowledge and experience

| Source page | Purpose |
|---|---|
| [`Domains.md`](Domains.md) | Domain lanes and cross-domain seams |
| [`Map-UI-and-AI.md`](Map-UI-and-AI.md) | MapLibre, Explorer Web, Evidence Drawer, and governed AI |
| [`Security-and-Sensitivity.md`](Security-and-Sensitivity.md) | Fail-closed public-safety and sensitive-data posture |

### Build and maintain

| Source page | Purpose |
|---|---|
| [`Development-and-Validation.md`](Development-and-Validation.md) | Environment, commands, tests, and CI interpretation |
| [`Contributing.md`](Contributing.md) | Branch, pull-request, review, receipt, and rollback workflow |
| [`Glossary.md`](Glossary.md) | Shared KFM vocabulary |
| [`Wiki-Maintenance.md`](Wiki-Maintenance.md) | Review, synchronization, drift, correction, and rollback procedure |

### Projection support

| Source page | Purpose |
|---|---|
| [`_Sidebar.md`](_Sidebar.md) | Native-wiki navigation |
| [`_Footer.md`](_Footer.md) | Authority and correction reminder |

`docs/wiki/README.md` governs the source packet and is intentionally excluded from the native-wiki page allowlist unless a later reviewed decision changes that boundary.

## Editing workflow

1. **Inspect authority.** Read the canonical source for every material claim and pin current implementation claims to a known repository revision.
2. **Edit the source packet.** Start in `docs/wiki/` on a focused feature branch; do not use the native wiki as the normal authoring surface.
3. **Preserve truth posture.** Label unverified implementation or publication claims `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`.
4. **Preserve navigation.** Use relative links inside `docs/wiki/`; use stable links from projected wiki pages back to the main repository.
5. **Check public safety.** Do not expose secrets, private records, restricted evidence, protected locations, or harmful precision.
6. **Validate the complete page set.** Check links, anchors, page identity, sidebar coverage, Markdown structure, and generated receipt integrity.
7. **Review before projection.** Merge the source change through the normal repository process before selecting an immutable source commit for native-wiki synchronization.
8. **Correct source first.** Treat synchronization as one-way; backport any emergency native-wiki correction immediately.

## Validation

A wiki-source change should verify:

- one H1 per ordinary page;
- no duplicate page names;
- all local page links resolve inside `docs/wiki/`;
- all linked repository paths exist at the inspected base;
- `_Sidebar.md` reaches every intended public page;
- Markdown fences, tables, alerts, and HTML are balanced;
- no secret, private, restricted, or harmful-precision content is present;
- generated receipt path/hash parity;
- `git diff --check`;
- applicable repository-native documentation checks.

The synchronization helper can exercise the allowlist and staged-diff controls without committing or pushing:

```powershell
pwsh -File tools/docs/wiki/sync_kfm_github_wiki.ps1 `
  -SourceCommit <reviewed-40-character-commit-sha>
```

A dry run may return `NOOP` or `PLANNED`. It does **not** prove that native-wiki publication occurred.

## Native wiki projection

The native wiki repository has a separate identity:

```text
https://github.com/bartytime4life/Kansas-Frontier-Matrix.wiki.git
```

The governed projection path is:

```text
reviewed docs/wiki source at an immutable commit
  -> allowlisted page copy
  -> staged path and whitespace validation
  -> dry-run review
  -> explicit -Publish authorization
  -> native-wiki commit and push without force
  -> remote commit readback
  -> link, rendering, and public-safety review
```

The bounded helper is documented in [`tools/docs/wiki/README.md`](../../tools/docs/wiki/README.md). An actual publish run is a separate public documentation mutation:

```powershell
pwsh -File tools/docs/wiki/sync_kfm_github_wiki.ps1 `
  -SourceCommit <reviewed-40-character-commit-sha> `
  -Publish
```

> [!CAUTION]
> `-Publish` must not be inferred from a source-only documentation request. Confirm the immutable source commit, page allowlist, credentials, projected diff, operator authority, and rollback path before use.

Nothing in this directory automatically initializes, synchronizes, or publishes the native wiki.

## Correction and rollback

Follow [`Wiki-Maintenance.md`](Wiki-Maintenance.md) for the full procedure.

| State | Safe response |
|---|---|
| Source pull request not merged | Close the pull request or update the feature branch; do not touch the native wiki |
| Source merged but not synchronized | Revert or forward-fix the main-repository change |
| Native wiki synchronized incorrectly | Revert the native-wiki commit or publish a corrected reviewed source snapshot |
| Emergency native-wiki correction | Backport the correction into `docs/wiki/` immediately |
| Sensitive or restricted content exposed | Follow [`SECURITY.md`](../../SECURITY.md), contain the exposure through the fastest safe platform path, and preserve private incident evidence |
| Authority drift | Restore links to canonical sources and record the conflict for review |

Do not force-push or rewrite shared history merely to make the wiki appear clean.

## Maintenance

Material changes to this source packet should remain reviewable, receipt-bearing when AI-authored, and reversible. Native-wiki synchronization should record the selected source commit, resulting wiki commit, operator, timestamp, and review reference.

[Back to top](#top)
