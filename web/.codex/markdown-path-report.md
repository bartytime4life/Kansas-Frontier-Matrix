# Markdown Path Reconstruction Report

## Scope and corpus
- Working directory: `web/`
- Markdown-like files scanned in reconstruction pass:
  - `web/README.md`
- Rescan after audit/create pass found:
  - `web/README.md`
  - `web/.codex/markdown-path-audit.md`

## Created paths
- None.

## Already-existing confirmed paths
- `web/README.md`
- `README.md`
- `apps/README.md`
- `apps/explorer-web/README.md`
- `apps/governed-api/README.md`
- `contracts/README.md`
- `policy/README.md`
- `tests/README.md`
- `data/README.md`
- `.github/README.md`
- `.github/CODEOWNERS`

## Unresolved unknown paths (not auto-created)
- `web/package.json`
- `web/tsconfig.json`
- `web/.env.example`
- `web/public/`
- `web/src/`

Reason: all unknown entries came from a section explicitly labeled “Proposed working subtree” and “NEEDS VERIFICATION”, so they were treated as ambiguous and intentionally not created.

## Confirmed paths still missing
- None.

## Verification summary
- No missing `CONFIRMED` paths remained after the create pass.
- No `UNKNOWN` paths were auto-created.
- Final diff was checked for speculative creations; only `.codex` audit/report files were added.
