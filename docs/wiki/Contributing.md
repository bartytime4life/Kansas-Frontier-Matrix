<!--
KFM_WIKI_SOURCE
page_id: Contributing
title: Contributing
status: PROPOSED wiki source; review required
updated: 2026-08-07
authority: orientation-only; canonical repository evidence and adopted KFM authority outrank this page
source_path: docs/wiki/Contributing.md
publication_effect: none until separately synchronized to the native GitHub Wiki
-->
# Contributing

KFM treats a consequential repository change as a governed, evidence-backed, reviewable, and reversible event. This page is an orientation summary; the current [CONTRIBUTING.md](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/CONTRIBUTING.md) controls repository contribution details.

## Standard flow

```text
inspect current evidence
  -> define bounded task contract
  -> choose owning responsibility root
  -> create focused feature branch
  -> implement dependency-closed change
  -> run proportionate validation
  -> emit generated-work receipt when required
  -> open draft pull request
  -> human review and hosted checks
  -> separate merge/release/publication decisions
```

## Task contract

Before editing, record:

- observable goal;
- base branch and immutable SHA;
- exact target paths;
- in-scope behavior and non-goals;
- acceptance criteria;
- validation plan and negative cases;
- stop conditions;
- change budget;
- rollback path.

Search current open pull requests, active branches, issues, campaign records, and recent merges for overlap before authoring and before the final push.

## Branch and pull-request discipline

- Use one bounded purpose per feature branch.
- Agent-created branches use `agent/<short-description>` unless continuing an existing authorized branch.
- Do not force-push or rewrite shared history.
- Do not push directly to `main` merely because permissions exist.
- Use the full pull-request template.
- Default AI-authored or governance-significant work to a draft pull request.
- A green check or merge is not a KFM data-publication event.

## Placement

Choose a path by responsibility, not topic. Read:

- [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md)
- [Accepted ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- the nearest parent README
- relevant ADRs and drift records.

Do not create parallel homes for schemas, contracts, policy, sources, registries, receipts, proofs, catalogs, releases, or published truth.

## Dependency closure

A complete change may require more than one file. Include the directly necessary:

- documentation;
- contract and schema;
- policy;
- valid and invalid fixtures;
- validator and tests;
- generator or migration;
- workflow wiring;
- generated receipt;
- correction and rollback notes.

Do not create every layer mechanically. Change the layers whose behavior or promise actually changes, and explain why adjacent layers are unaffected.

## AI-assisted work

AI may draft and implement bounded changes, but it cannot self-approve. AI-authored artifacts require a generated-work receipt under `data/receipts/generated/` according to the current repository contract. The receipt:

- lists artifact paths and hashes;
- identifies model and governing contract;
- records evidence and validation;
- keeps human review `pending`;
- excludes prompts, hidden reasoning, secrets, and sensitive payloads;
- does not become proof, approval, release, or publication authority.

## Review

Reviewers should verify:

- the actual diff matches the task contract;
- claims match current repository evidence;
- placement follows Directory Rules;
- tests cover positive and negative behavior;
- rights and sensitivity are safe;
- generated outputs are attributable;
- no trust membrane or public-store boundary is bypassed;
- rollback is realistic.

CODEOWNERS routes review; it does not prove that review occurred or that separation of duties is sufficient.

## Security

Follow [SECURITY.md](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/SECURITY.md) for vulnerabilities and sensitive exposures. Do not put exploit details or protected data into a public issue, pull request, wiki, log, or receipt.

## Rollback

- Before merge: close the PR and remove the unneeded branch with appropriate authority.
- After merge: use a focused revert or forward-fix PR; do not rewrite shared history.
- After native-wiki synchronization: revert the wiki commit or republish corrected reviewed source.
- For public data or releases: use the owning correction, withdrawal, and rollback process rather than a documentation edit.

## Full guide

Read [CONTRIBUTING.md](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/CONTRIBUTING.md) and the [pull-request template](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/.github/PULL_REQUEST_TEMPLATE.md) before opening a change.
