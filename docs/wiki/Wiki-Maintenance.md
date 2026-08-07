<!--
KFM_WIKI_SOURCE
page_id: Wiki-Maintenance
title: Wiki Maintenance
status: PROPOSED wiki source; review required
updated: 2026-08-07
authority: orientation-only; canonical repository evidence and adopted KFM authority outrank this page
source_path: docs/wiki/Wiki-Maintenance.md
publication_effect: none until separately synchronized to the native GitHub Wiki
-->
# Wiki Maintenance

The GitHub Wiki is a separate Git repository. KFM keeps a reviewable source packet under `docs/wiki/` and treats the native wiki as a one-way public projection.

## Current boundary

At the authoring checkpoint:

- repository metadata reported `has_wiki: true`;
- the native wiki had no readable `Home` page;
- the connected GitHub tool could not initialize or write the special `.wiki.git` repository;
- this source packet therefore creates **no native-wiki publication effect**.

Re-check those facts before synchronization.

## Source and projection

```text
main repository
  docs/wiki/*.md
    -> feature branch
    -> draft pull request
    -> review and merge
    -> explicit native-wiki synchronization
    -> readback and correction
```

| Surface | Role |
|---|---|
| `docs/wiki/` | Reviewed source packet and maintenance contract |
| Native `<repo>.wiki.git` | Public projection |
| Main repository authority docs | Canonical sources linked by the wiki |
| Git history | Rollback and provenance for both repositories |

Direct native-wiki edits should be reserved for urgent correction. Backport the correction to `docs/wiki/` immediately so the next synchronization does not reintroduce the defect.

## Page set

Synchronize these files:

```text
Home.md
Getting-Started.md
Project-Status.md
Architecture.md
Repository-Map.md
Governance-and-Evidence.md
Data-Lifecycle.md
Domains.md
Map-UI-and-AI.md
Security-and-Sensitivity.md
Development-and-Validation.md
Contributing.md
Glossary.md
Wiki-Maintenance.md
_Sidebar.md
_Footer.md
```

Do not copy `docs/wiki/README.md` into the native wiki unless a reviewed decision intentionally creates a reader-facing README page.

## First-time initialization

GitHub may require the first page to be created through the repository's **Wiki** tab before the `.wiki.git` repository can be cloned. An authorized maintainer should:

1. open the repository's Wiki tab;
2. create a temporary or reviewed `Home` page if the wiki is still uninitialized;
3. confirm the `.wiki.git` repository is cloneable;
4. replace the temporary page with the reviewed source set in one bounded wiki commit.

This is a platform mutation and public documentation publication. It remains separate from the main-repository pull request.

## Manual synchronization

After the source PR is reviewed and merged:

```bash
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.wiki.git

cd Kansas-Frontier-Matrix
git checkout main
git pull --ff-only

for page in \
  Home.md \
  Getting-Started.md \
  Project-Status.md \
  Architecture.md \
  Repository-Map.md \
  Governance-and-Evidence.md \
  Data-Lifecycle.md \
  Domains.md \
  Map-UI-and-AI.md \
  Security-and-Sensitivity.md \
  Development-and-Validation.md \
  Contributing.md \
  Glossary.md \
  Wiki-Maintenance.md \
  _Sidebar.md \
  _Footer.md
do
  cp "docs/wiki/$page" "../Kansas-Frontier-Matrix.wiki/$page"
done

cd ../Kansas-Frontier-Matrix.wiki
git status --short
git diff --check
git diff --stat
git add -A
git commit -m "docs: synchronize reviewed KFM wiki source"
git push
```

Before pushing, inspect deletions and compare the exact source commit. Do not use force push.

## Readback validation

After synchronization:

- open every page from `_Sidebar`;
- verify the logo, tables, alerts, code fences, and Mermaid blocks;
- test internal page links;
- test links back to canonical repository files;
- confirm no `README` page or unreviewed file was published;
- verify the wiki commit and source commit are recorded in the maintenance note or pull request;
- scan for secrets and sensitive material;
- check mobile and keyboard navigation.

## Drift detection

A drift review compares native-wiki bytes to the reviewed source set. Classify differences:

| Result | Action |
|---|---|
| Exact match | Record the source and wiki commits |
| Native wiki has an urgent correction | Backport to `docs/wiki/`, review, then resynchronize |
| Source has reviewed changes | Synchronize after merge |
| Both changed | Hold; reconcile meaning and preserve unique correction history |
| Native page has unsupported claims | Correct or remove promptly; do not copy unsupported text back |

Automated publishing is not enabled by this source set. A future sync workflow would require an explicit threat model, least-privilege write authority, credential handling, fork safety, failure behavior, review boundary, and rollback. Workflow convenience does not justify bypassing review.

## Rollback

- **Main source PR not merged:** close the PR; delete the branch only with appropriate authority.
- **Source merged but not synchronized:** revert or forward-fix the main-repository commit.
- **Wiki synchronized incorrectly:** revert the wiki commit, or commit a correction from a known reviewed source.
- **Sensitive content exposed:** follow [SECURITY.md](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/SECURITY.md), remove exposure through the fastest safe platform path, preserve private incident evidence, rotate affected credentials, and issue the required correction.
- **Authority drift:** restore links to canonical repository sources and record the conflict.

Do not rewrite shared history merely to make the wiki appear clean.
