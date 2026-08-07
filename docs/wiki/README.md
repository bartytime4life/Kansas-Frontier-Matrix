<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/wiki-source/readme
title: docs/wiki — GitHub Wiki Source Set
type: readme
version: v0.1.0
status: proposed; review-required; not-native-wiki-published
owners: ["@bartytime4life"]
created: 2026-08-07
updated: 2026-08-07
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
notes:
  - "The native GitHub Wiki is a separate Git repository and is not a KFM authority root."
  - "This source set creates no release, deployment, publication, policy, evidence, or data-lifecycle state."
  - "Native-wiki synchronization remains a separate reviewed action."
[/KFM_META_BLOCK_V2] -->

# `docs/wiki/` — GitHub Wiki source set

> Reviewable Markdown source for the Kansas Frontier Matrix GitHub Wiki. The native wiki is a **public orientation projection**, not a second doctrine, contract, schema, policy, evidence, release, or publication authority.

## Purpose

GitHub stores a repository wiki in a separate `<repository>.wiki.git` repository. That surface does not participate in the normal pull-request review flow. KFM therefore keeps the proposed wiki pages in `docs/wiki/` first so changes can be inspected, reviewed, corrected, and rolled back before any native-wiki synchronization.

This directory owns only the **human-facing wiki source packet**. Canonical answers remain in the main repository:

- repository identity and current entry points: [`README.md`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/README.md);
- placement authority: [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md) as adopted by [ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md);
- contribution workflow: [`CONTRIBUTING.md`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/CONTRIBUTING.md);
- doctrine, architecture, domain, contract, schema, policy, test, lifecycle, and release owners in their existing responsibility roots.

## Authority boundary

| Concern | Owning source | Wiki role |
|---|---|---|
| Repository identity and current implementation evidence | Main-repository bytes, tests, workflows, manifests, logs, and artifacts at a known revision | Summarize and link; never replace |
| KFM-wide invariants | `docs/doctrine/` and accepted ADRs | Explain in accessible language |
| Object meaning, shape, admissibility, and enforceability | `contracts/`, `schemas/`, `policy/`, `tests/`, and `fixtures/` | Point readers to the owning surface |
| Lifecycle records, evidence, receipts, proofs, and catalogs | governed `data/` lanes | Never host or elevate |
| Release, correction, withdrawal, and rollback decisions | `release/` | Link to reviewed records when public-safe |
| Native GitHub Wiki pages | `<repository>.wiki.git` | Derived publication target after review |
| This directory | `docs/wiki/` | Reviewable source and maintenance contract |

> [!IMPORTANT]
> A wiki page, polished diagram, badge, commit, pull request, merge, or native-wiki push does not establish factual truth, policy approval, KFM release, promotion, or publication of data.

## Page inventory

| Source page | Purpose |
|---|---|
| [`Home.md`](Home.md) | Public landing page and project orientation |
| [`Getting-Started.md`](Getting-Started.md) | Reader and contributor onboarding |
| [`Project-Status.md`](Project-Status.md) | Evidence-bounded implementation snapshot |
| [`Architecture.md`](Architecture.md) | Connected operating model and trust membrane |
| [`Repository-Map.md`](Repository-Map.md) | Responsibility-root map and placement guidance |
| [`Governance-and-Evidence.md`](Governance-and-Evidence.md) | Truth labels, evidence closure, promotion, and correction |
| [`Data-Lifecycle.md`](Data-Lifecycle.md) | RAW-to-PUBLISHED lifecycle and accountability lanes |
| [`Domains.md`](Domains.md) | Thirteen domain lanes and cross-domain seams |
| [`Map-UI-and-AI.md`](Map-UI-and-AI.md) | MapLibre, Explorer Web, Evidence Drawer, and governed AI |
| [`Security-and-Sensitivity.md`](Security-and-Sensitivity.md) | Fail-closed public-safety and sensitive-data posture |
| [`Development-and-Validation.md`](Development-and-Validation.md) | Environment, commands, tests, CI interpretation |
| [`Contributing.md`](Contributing.md) | Branch, pull-request, review, receipt, and rollback workflow |
| [`Glossary.md`](Glossary.md) | Shared KFM vocabulary |
| [`Wiki-Maintenance.md`](Wiki-Maintenance.md) | Review, synchronization, drift, and rollback procedure |
| [`_Sidebar.md`](_Sidebar.md) | Native-wiki navigation |
| [`_Footer.md`](_Footer.md) | Authority and correction reminder |

## Editing contract

1. Start changes in `docs/wiki/` on a focused feature branch.
2. Read the canonical source for every material claim; do not copy stale prose from the native wiki.
3. Keep implementation claims tied to a current repository revision or label them `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`.
4. Use repository-relative links between source pages and stable absolute links from wiki pages back to the main repository.
5. Preserve sensitive-data, rights, sovereignty, security, and public-safety boundaries.
6. Include the required generated-work receipt for AI-authored changes.
7. Synchronize to the native wiki only after the source change is reviewed and the exact target page set is confirmed.
8. Treat the native wiki as a one-way projection. Correct the source packet first, then republish.

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
- repository-native documentation checks when available.

Native GitHub rendering and native-wiki publication are separate checks. Source validation does not prove that synchronization occurred.

## Publication and rollback

Follow [`Wiki-Maintenance.md`](Wiki-Maintenance.md). The safe default is:

```text
docs/wiki/ reviewed source
  -> explicit synchronization review
  -> native GitHub Wiki projection
  -> readback and link check
  -> correction or rollback from Git history when needed
```

Before merge, close the pull request or delete the unneeded feature branch. After merge, use a focused revert or forward-fix. After native-wiki synchronization, revert the wiki commit or republish a corrected source snapshot; do not rewrite shared history.
