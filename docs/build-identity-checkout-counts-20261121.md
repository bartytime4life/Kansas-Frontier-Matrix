# Build identity: what kind of checkout change Git reports (2026-11-21)

`/api/build` has reported `commitState: WORKTREE_MODIFIED` and `sourceCommit: null` on the
public site after several publishes, while its digest and file count matched a clean checkout of
the published commit exactly. Earlier records note the same state on 2026-10-19, 2026-11-01 and
2026-11-19. The cause has stayed unknown because it lives in the host's checkout, which nobody
outside the host can read.

## What changed

When `git status` in the build's checkout is not empty, the identity now carries one more
field:

```json
"worktreeChanges": { "trackedInputs": 0, "trackedOther": 0, "untrackedInputs": 0, "untrackedOther": 1 }
```

| Count | Meaning |
| --- | --- |
| `trackedInputs` | Committed application inputs that Git reports as changed. If the digest still matches the commit, their bytes are unchanged and the difference is something else Git tracks, such as the executable bit. |
| `trackedOther` | Committed files outside the application inputs (documentation, tests, receipts) that Git reports as changed. |
| `untrackedInputs` | New entries under the application inputs. These also change the digest. |
| `untrackedOther` | New entries outside the application inputs: a file or directory the host or a build step left in the checkout. |

Git reports a wholly new directory as one entry and a rename as one entry, so these are entry
counts, not file counts. The build log prints the same counts.

## What it does not do

- It publishes **no path or file name**. `/api/build` is public, and a host's stray file names
  are not application identity.
- It does not change `sourceDigest`, `sourceFileCount`, `sourceCommit`, `commitState` or the
  `--verify` outcome. The digest comparison is still what binds the application inputs.
- The field is absent on a clean checkout, when Git is unavailable, and when the only
  difference is one that `git status` cannot see (the `assume-unchanged` and `skip-worktree`
  cases, which already report `WORKTREE_MODIFIED`).

## Reading it after the next publish

A rebuild over an existing build in a clean checkout of `804132d1` stays `CLEAN_CHECKOUT`, so
the build's own outputs are not the cause. After the next publish the counts will say whether
the host's checkout holds a new entry outside the inputs, an edited committed file outside the
inputs, or a tracked input whose bytes match but whose mode differs. Naming the file still
needs `git status` on the host.

## Tests

`tests/build-identity.test.mjs` covers the host's case (inputs identical, one new file outside
them), a mixed case with a rename and a new directory, and checks that no file name appears in
the published identity. `tests/build-identity-http.test.mjs` accepts the field only with
`WORKTREE_MODIFIED` and only with these four non-negative counts.
