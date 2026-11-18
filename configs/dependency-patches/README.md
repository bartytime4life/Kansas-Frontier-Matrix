# Dependency patches

This directory holds patches that pnpm applies to locked third-party packages
(`patchedDependencies` in `pnpm-workspace.yaml`). It also holds the reviewed
audit exceptions bound to those patches (`audit-exceptions.json`). Use a patch
only when no fixed upstream release exists. Remove it as soon as one does.

## picomatch 4.0.7: ReDoS through repeated extglobs (GHSA-fc5q-39xc-vjpf)

| Field | Value |
|---|---|
| Advisory | [GHSA-fc5q-39xc-vjpf](https://github.com/advisories/GHSA-fc5q-39xc-vjpf), high, CWE-1333 |
| Affected | every published `picomatch` release `<=4.0.7`; no patched release exists |
| Path in this repository | root pnpm workspace: `vite@8.3.3` and `vitest@5.1.0` (dev tooling for `packages/maplibre`), and `tinyglobby`/`fdir` beneath them. The two npm projects use vendored forks instead; see [npm projects](#npm-projects-vendored-forks). |
| Fix applied | [micromatch/picomatch#264](https://github.com/micromatch/picomatch/pull/264), `lib/parse.js` only, unchanged except for context line offsets against 4.0.7 |
| Patch file | `picomatch-4.0.7.patch` |

### Effect

The advisory's input `isMatch('a'.repeat(48) + '/', '+(*a)')` behaves
differently with and without the patch:

- Unpatched 4.0.7 does not return within 10 s. It was stopped by a timeout.
- Patched, it returns `false` in about 2 ms.

The other shapes listed in the upstream PR, such as `+(*)`, `*(*a)`, `+(a*b)` and
`@(*a)+`, also return promptly, and ordinary globs match as before.
`packages/maplibre/tests/picomatch-redos.test.ts` checks both properties
against the installed patched package.

### Why the audit accepts it

`pnpm audit` matches advisories by version number, so it still reports the
patched 4.0.7. A pnpm `auditConfig.ignoreGhsas` entry cannot be used here: pnpm
removes the advisory from the report but keeps it in the severity counts, and
the repository's fail-closed classifier rejects that mismatch.

Instead, `tools/validators/dependencies/pnpm_audit_readiness.py classify-audit
--exceptions configs/dependency-patches/audit-exceptions.json` excepts this one
advisory. It does so only while all of these hold:

- the exception is unexpired. Each exception lasts at most 184 days, and this one
  expires on 2027-02-18.
- the patch file's SHA-256 equals the recorded `patch_sha256`.
- `pnpm-lock.yaml` applies exactly that patch hash to `picomatch@4.0.7`.
- no other `picomatch` version is locked.
- the audit finding names only that package, advisory and version.

Any other finding at or above the threshold still fails the job.

### Removal

When a fixed `picomatch` is released and the lockfile resolves to it, remove
three things together:

1. the `patchedDependencies` entry;
2. this patch file;
3. the exception.

The classifier rejects the register as soon as the lockfile stops applying the
patch, so an exception cannot be left behind silently. If the exception expires
first, re-review the upstream status and either renew it with a fresh date or
replace the patch.

## npm projects: vendored forks

npm has no equivalent of pnpm `patchedDependencies`. The two standalone npm
projects that locked unpatched picomatch instead install patched forks from
their own `vendor/` directories:

| Project | Fork | Base | Consumers |
|---|---|---|---|
| `apps/site/source` | `vendor/picomatch-4.0.7-kfm.1.tgz` | 4.0.7 + `picomatch-4.0.7.patch` | vite, tinyglobby, fdir |
| `apps/site/source` | `vendor/picomatch-2.3.2-kfm.1.tgz` | 2.3.2 + `picomatch-2.3.2.patch` | micromatch (fast-glob) |
| `apps/review-console/recovery` | `vendor/picomatch-4.0.7-kfm.1.tgz` | 4.0.7 + `picomatch-4.0.7.patch` | vite, tinyglobby, fdir |

`picomatch-2.3.2.patch` carries the same fix to the 2.x line, so micromatch
keeps its declared `^2` range:

- Ten of its eleven hunks are the 4.0.7 hunks at new offsets.
- The eleventh adds the same source-tracking calls around 2.x's text-token
  merge.

In a 60,000-pattern differential check against each unpatched base, the two
forks changed exactly the same 38 match results:

- **Malformed patterns:** most of the changed results come from patterns with
  unbalanced parentheses.
- **Repeated wildcard extglobs:** the rest are well-formed patterns such as
  `*(**)` and `+(**)`. These now compile as literal text, the same fallback
  unpatched picomatch already applies to other risky repeats such as
  `+(+(a))`.

Each project has a `vendor/picomatch-kfm.md` with the fork digests and
how to rebuild them, and a `tests/picomatch-redos.test.mjs` regression test.
Each test resolves the copy each consumer loads and fails if that copy is
unpatched. `npm audit` reports no findings for either project with the forks
installed, because npm does not match `file:` packages against registry
advisories. Remove the forks, devDependencies and overrides together when a
fixed release exists.
