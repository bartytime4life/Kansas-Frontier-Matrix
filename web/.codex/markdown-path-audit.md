# Markdown Path Audit

Source corpus scanned (within `web/`):
- `README.md`

## Method
- Parsed strong-evidence markdown links and fenced directory trees from `web/README.md`.
- Resolved relative paths against `web/README.md` and normalized to repo-root paths.
- Marked proposed/needs-verification tree entries as `UNKNOWN` to stay conservative.

## Audit entries

| normalized_path | kind | exists_now | confidence | source_file | source_locator | evidence_excerpt |
|---|---|---:|---|---|---|---|
| web/README.md | file | true | CONFIRMED | web/README.md | L14 markdown link `./README.md` | Current public `main` now exposes both [`web/README.md`](./README.md) |
| README.md | file | true | CONFIRMED | web/README.md | L9 markdown link `../README.md` | root [`../README.md`](../README.md) |
| apps/README.md | file | true | CONFIRMED | web/README.md | L9 markdown link `../apps/README.md` | runtime family [`../apps/README.md`](../apps/README.md) |
| apps/explorer-web/README.md | file | true | CONFIRMED | web/README.md | L9 markdown link `../apps/explorer-web/README.md` | parallel shell boundary [`../apps/explorer-web/README.md`](../apps/explorer-web/README.md) |
| apps/governed-api/README.md | file | true | CONFIRMED | web/README.md | L9 markdown link `../apps/governed-api/README.md` | governed API [`../apps/governed-api/README.md`](../apps/governed-api/README.md) |
| contracts/README.md | file | true | CONFIRMED | web/README.md | L9 markdown link `../contracts/README.md` | shared law [`../contracts/README.md`](../contracts/README.md) |
| policy/README.md | file | true | CONFIRMED | web/README.md | L9 markdown link `../policy/README.md` | shared law [`../policy/README.md`](../policy/README.md) |
| tests/README.md | file | true | CONFIRMED | web/README.md | L9 markdown link `../tests/README.md` | shared law [`../tests/README.md`](../tests/README.md) |
| data/README.md | file | true | CONFIRMED | web/README.md | L9 markdown link `../data/README.md` | shared law [`../data/README.md`](../data/README.md) |
| .github/README.md | file | true | CONFIRMED | web/README.md | L9 markdown link `../.github/README.md` | shared law [`../.github/README.md`](../.github/README.md) |
| .github/CODEOWNERS | file | true | CONFIRMED | web/README.md | L6 markdown link `../.github/CODEOWNERS` | confirm against [`../.github/CODEOWNERS`](../.github/CODEOWNERS) |
| web/package.json | file | false | UNKNOWN | web/README.md | L149-L154 proposed directory tree | `package.json # NEEDS VERIFICATION` |
| web/tsconfig.json | file | false | UNKNOWN | web/README.md | L149-L154 proposed directory tree | `tsconfig.json # NEEDS VERIFICATION` |
| web/.env.example | file | false | UNKNOWN | web/README.md | L149-L155 proposed directory tree | `.env.example # PROPOSED / NEEDS VERIFICATION` |
| web/public | directory | false | UNKNOWN | web/README.md | L155-L157 proposed directory tree | `public/ # PROPOSED` |
| web/src | directory | false | UNKNOWN | web/README.md | L157-L186 proposed directory tree | `src/ # PROPOSED` |

## Creation decision
- Missing `CONFIRMED` paths: none.
- Therefore no repository paths were auto-created.
