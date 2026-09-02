# Authors

> **Purpose.** Record verified human attribution for the Kansas Frontier Matrix while keeping authorship, contribution history, review routing, stewardship, licensing, and publication authority separate.

> [!IMPORTANT]
> This file is a curated attribution register, not a substitute for Git history and not a grant of governance or release authority. A commit, pull request, review assignment, or name in this file does not by itself make a person a policy steward, release approver, or KFM publication authority.

## Status and evidence boundary

| Field | Current state |
|---|---|
| Repository | [`bartytime4life/Kansas-Frontier-Matrix`](https://github.com/bartytime4life/Kansas-Frontier-Matrix) |
| Document role | Root attribution and contributor-recognition guide |
| Evidence snapshot for this revision | [`main@d00ec5a`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/d00ec5a3792324b338a34363022be8ef8ed47be6) |
| Current named identity | [Andy (`@bartytime4life`)](https://github.com/bartytime4life) |
| Verification basis | Repository ownership, verified commit authorship, and the current [CODEOWNERS review route](.github/CODEOWNERS) |
| Complete historical record | Git commits, merged pull requests, and the [GitHub contributor graph](https://github.com/bartytime4life/Kansas-Frontier-Matrix/graphs/contributors) |
| License boundary | The repository [license remains unresolved](LICENSE); this file grants no license or reuse permission |
| Update route | Focused branch and draft pull request, following [`CONTRIBUTING.md`](CONTRIBUTING.md) |

## Current verified attribution

### Repository owner and active contributor

| Contributor | Verified relationship | Authority boundary |
|---|---|---|
| [Andy (`@bartytime4life`)](https://github.com/bartytime4life) | Repository owner, verified commit author, and the only GitHub identity currently asserted in [`.github/CODEOWNERS`](.github/CODEOWNERS) | CODEOWNERS provides review routing only. It does not prove that review occurred or confer independent policy, release, or publication authority. |

> [!NOTE]
> Additional contributors may already be represented in repository history. They are not manually named here until their GitHub identity and the intended attribution scope can be verified. The Git history and merged pull requests remain the source of record.

## Attribution surfaces

KFM keeps several kinds of attribution separate so that credit does not become mistaken authority.

| Surface | What it records | What it does **not** prove |
|---|---|---|
| `AUTHORS.md` | Curated, verified human attribution | Complete commit history, review approval, stewardship, licensing, or publication state |
| Git commits and merged pull requests | Historical contribution activity tied to repository identities | Ownership of external source material or authority over every affected KFM object |
| [`.github/CODEOWNERS`](.github/CODEOWNERS) | GitHub review routing for matching paths | Authorship, completed review, policy approval, or release authorization |
| Source descriptors, citations, and catalog records | Attribution and provenance for external data, documents, standards, and evidence | KFM repository authorship |
| Receipts and generated records | Process provenance, tools, inputs, outputs, and hashes where supported | Human authorship, truth, or approval by themselves |

## Contributor-recognition policy

A person may be added to the curated list when there is evidence of a material contribution, such as:

- merged code, documentation, contract, schema, policy, fixture, test, pipeline, data-governance, or release-support work;
- sustained review, stewardship, research, design, or domain expertise documented in repository history;
- a verified GitHub identity or another public attribution identity the contributor has approved;
- enough evidence to describe the relationship without inventing a title, role, organization, or level of authority.

Attribution entries should:

- use the contributor's public name or GitHub handle;
- avoid private email addresses, legal names, affiliations, or other personal information unless the contributor explicitly requests publication;
- describe verified contribution or repository relationships narrowly;
- preserve prior credit when responsibilities change;
- use a correction note or pull-request explanation when an entry must be amended or removed.

## AI-assisted and automated work

AI assistants, bots, formatters, generators, and other tools may support KFM work, but they are not listed as human authors.

- Material AI or automation assistance should be disclosed in the relevant pull request, receipt, or generated-artifact metadata when repository practice supports it.
- The human contributor who submits or approves a change remains responsible for verifying its evidence, accuracy, policy posture, validation, and scope.
- Generated language, badges, diagrams, receipts, or commits do not become evidence, authorship proof, review approval, or publication authority merely because they were produced successfully.
- `Co-authored-by` trailers should identify actual human co-authors only and should not be fabricated for tools or model personas.

## External sources and acknowledgments

KFM depends on public agencies, archives, research institutions, standards communities, open-source projects, and other source providers. Their attribution belongs in the source-specific governance chain—such as source descriptors, citations, rights records, catalog metadata, dependency notices, and release artifacts—rather than being collapsed into repository authorship.

This separation preserves source authority, licensing obligations, provenance, and the distinction between creating KFM and supplying evidence or software that KFM uses.

## Updating this file

A focused update should:

1. verify the contributor identity and contribution evidence;
2. read the current [`CONTRIBUTING.md`](CONTRIBUTING.md), [`.github/CODEOWNERS`](.github/CODEOWNERS), and [Directory Rules](docs/architecture/directory-rules.md);
3. change only `AUTHORS.md` unless another exact path is necessary and explicitly in scope;
4. preserve the `# Authors` heading and existing verified attribution;
5. validate links, heading structure, privacy, and the final diff;
6. open a draft pull request that states the evidence basis, uncertainty, and rollback method.

## Related governance

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow, evidence, validation, and pull-request expectations.
- [`.github/CODEOWNERS`](.github/CODEOWNERS) — verified GitHub review routing and its authority limits.
- [`docs/architecture/directory-rules.md`](docs/architecture/directory-rules.md) — repository placement doctrine and change discipline.
- [`LICENSE`](LICENSE) — repository licensing status; currently unresolved and not replaced by this file.

---

Authorship credit should be accurate, consent-aware, evidence-backed, and correctable. When attribution cannot be verified, preserve the contribution in Git history and mark the manual entry as pending rather than guessing.
