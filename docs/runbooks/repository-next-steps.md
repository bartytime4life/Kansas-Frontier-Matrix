# Repository Next Steps (2026-04-24)

This runbook captures the most practical next actions after a repository scan on 2026-04-24.

## Current snapshot

- The repository is documentation-heavy: 200 files total, with 130 Markdown files and only a small set of executable artifacts (shell, Rego, JSON schemas).  
- The currently executable CI baseline path is narrow but healthy: `.github/workflows/verification-baseline.yml` runs shell syntax checks, self-tests, and `tools/ci/verify_baseline.sh`.  
- `tools/ci/test_verify_baseline.sh` passes locally and validates both pass/fail behavior for the baseline verifier.

## Key gaps discovered

1. **Documentation-to-repo drift is high.**
   - Several READMEs describe scripts or helpers that are not present in the current tree.
   - Example drift:
     - `scripts/README.md` lists helper files that do not exist.
     - `tools/ci/README.md` lists renderer helpers and tests that do not exist.
2. **Placeholder density is very high.**
   - A scan found ~1,875 `TODO`, `UNKNOWN`, and `NEEDS VERIFICATION` markers across core documentation lanes.
3. **Machine-enforced governance is minimal today.**
   - Current CI checks structural baseline only.
   - Contract, schema, and policy gates are represented in docs but are not yet wired into runnable enforcement from this checkout.

## Recommended next steps (priority order)

### P0 — Stabilize truth of repository documentation

1. Align README claims to currently mounted files (or create the referenced files).
2. Start with top drift surfaces:
   - `scripts/README.md`
   - `tools/ci/README.md`
3. Introduce one explicit status marker in each README section:
   - `Present in repo`
   - `Planned`
   - `Archived`

**Definition of done:** no README claims file paths that do not exist without explicitly marking them as planned.

### P1 — Expand thin-slice CI beyond baseline

1. Add a lightweight docs consistency check script (for example, verify referenced local file paths exist).
2. Add JSON schema validation smoke tests using existing `schemas/contracts/v1/*.schema.json` files and fixture payloads.
3. Add policy smoke checks for `policy/bundles/runtime/*.rego` using existing fixtures.

**Definition of done:** CI fails on broken local doc links/path claims, invalid schema fixtures, and broken runtime policy tests.

### P2 — Build one end-to-end governed proof slice

1. Select one claim type (recommended: runtime finite outcomes).
2. Produce a minimal fixture-to-decision path:
   - fixture input
   - policy decision
   - envelope validation
   - receipt/proof artifact
3. Document this in `docs/runbooks/` as the canonical “first governed release slice.”

**Definition of done:** a single command path can reproduce a governed decision artifact from fixture input with deterministic output.

### P3 — Reduce placeholder debt deliberately

1. Triage top 20 files by unresolved marker count.
2. For each file, choose one action:
   - resolve now,
   - downgrade claim scope,
   - split into `planned` appendix.
3. Track marker burn-down weekly.

**Definition of done:** 30% reduction in unresolved markers in the top 20 files without introducing unverified implementation claims.

## Suggested first sprint backlog (1 week)

- Fix drift in `scripts/README.md` and `tools/ci/README.md`.
- Add `tools/ci/check_readme_paths.sh`.
- Add workflow job to run:
  - baseline verifier
  - README path check
  - schema smoke check
  - runtime policy smoke check
- Add one concise runbook for “baseline + smoke CI failure triage”.

