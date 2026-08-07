<!--
KFM_WIKI_SOURCE
page_id: Development-and-Validation
title: Development and Validation
status: PROPOSED wiki source; review required
updated: 2026-08-07
authority: orientation-only; canonical repository evidence and adopted KFM authority outrank this page
source_path: docs/wiki/Development-and-Validation.md
publication_effect: none until separately synchronized to the native GitHub Wiki
-->
# Development and Validation

Validation must match the claim. A green command proves only the scope it actually executes; it does not establish factual truth, rights clearance, security, release fitness, deployment, or publication.

## Root Python baseline

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[test]"

make validate
git diff --check
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Inspect the current `Makefile`, `pyproject.toml`, and target README before relying on a command.

## Targeted commands documented by the repository

| Command | Bounded purpose |
|---|---|
| `make validate` | Aggregate schema/contract baseline configured by the repository |
| `make governed-api-smoke` | Governed API test suite |
| `make governed-api-verify` | Governed API tests plus renderer/model import-boundary check |
| `make boundary-guards` | Policy, API, connector, and pipeline boundary tests |
| `make deny-test` | Public route, store, and runtime import guards |
| `make ui-build` | Explorer Web production build |
| `make maplibre-govern` | MapLibre performance-governance validation |
| `git diff --check` | Whitespace and patch formatting |

Command availability and behavior may change. Read current source before use.

## Holds, TODOs, and skips

Some repository surfaces intentionally report readiness holds or print TODO markers. Interpret outcomes precisely:

| Outcome | Meaning |
|---|---|
| `PASS` | The declared check passed for the declared inputs |
| `FAIL` | The declared check found a violation or operational failure |
| `HOLD` | A prerequisite or authority is intentionally unresolved |
| `SKIPPED` | The check did not execute its substantive behavior |
| `PARTIAL` | Only part of the required acceptance boundary was exercised |
| zero exit from a TODO target | Not substantive proof unless the target contract says otherwise |

Do not rename a hold as readiness or a skipped test as success.

## Documentation and wiki validation

For `docs/wiki/`:

1. Require one H1 per ordinary page.
2. Validate every relative page link.
3. Verify canonical repository targets at the pinned base.
4. Check sidebar coverage and duplicate slugs.
5. Check balanced fences, tables, alerts, and HTML.
6. Scan for secrets and sensitive content.
7. Validate the generated receipt and artifact hashes.
8. Review source rendering in the pull request.
9. After native-wiki synchronization, read back every page and link.

## Workflows and hosted checks

GitHub Actions orchestrate repository-owned commands. Workflow files do not become policy, evidence, release, or publication authority. Before changing or relying on CI, inspect:

- event trigger and changed-path filters;
- fork and untrusted-code behavior;
- top-level and job permissions;
- secrets, OIDC, caches, artifacts, and network access;
- immutable third-party action pins;
- stable workflow/job/check names;
- branch-protection coupling;
- kill switch and rollback.

See [`.github/workflows/README.md`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/.github/workflows/README.md).

## Negative tests matter

KFM's trust boundaries need deterministic negative cases:

- missing evidence -> `ABSTAIN`;
- blocked sensitivity -> `DENY`;
- invalid schema -> fail;
- stale or superseded support -> hold or abstain;
- denied/error payload -> no data leakage;
- watcher attempt to publish -> deny;
- missing rollback or release support -> hold;
- invalid path placement -> hold or deny.

## Reporting validation

Record:

| Field | Example |
|---|---|
| Command | exact command |
| Revision | branch and exact head SHA |
| Inputs | fixtures, paths, environment |
| Outcome | PASS / FAIL / PARTIAL / NOT RUN |
| Negative cases | expected failures exercised |
| Limitations | what the check did not prove |
| Evidence | log, workflow run, test report, artifact digest |

## Validation references

- [Root README validation section](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/README.md#build-and-validation)
- [Contributing validation guidance](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/CONTRIBUTING.md#validation)
- [Workflow governance](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/.github/workflows/README.md)
- [Validators](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/tools/validators)
- [Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/tests)
- [Fixtures](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/fixtures)
