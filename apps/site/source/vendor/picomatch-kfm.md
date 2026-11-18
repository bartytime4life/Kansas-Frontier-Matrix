# Patched picomatch

These tarballs are `picomatch` releases with the upstream fix for
[GHSA-fc5q-39xc-vjpf](https://github.com/advisories/GHSA-fc5q-39xc-vjpf)
applied. That advisory is a high-severity ReDoS through repeated extglobs, and
no fixed picomatch release exists. Only build-time tooling loads picomatch
here. The Worker bundle does not include it.

| Fork | Base | Used by | SHA-256 |
|---|---|---|---|
| `picomatch-4.0.7-kfm.1.tgz` | `picomatch@4.0.7` | vite, tinyglobby, fdir | `d50e8063019826c9298e1d3bc1054c6c8867a3e20500b71bd1da90143bbe35df` |
| `picomatch-2.3.2-kfm.1.tgz` | `picomatch@2.3.2` | micromatch, which fast-glob uses | `835fd04419711d6e09cc5b1c162c766f0fb9400ce7176a8755f8a117ff0d3bd8` |

## Changes

Each fork changes only `lib/parse.js` and the `version` field in
`package.json`.

- **4.0.7:** `lib/parse.js` takes
  [`configs/dependency-patches/picomatch-4.0.7.patch`](../../../../configs/dependency-patches/picomatch-4.0.7.patch),
  the patch the root pnpm workspace already applies.
- **2.3.2:** it takes
  [`configs/dependency-patches/picomatch-2.3.2.patch`](../../../../configs/dependency-patches/picomatch-2.3.2.patch),
  the same fix carried to the 2.x line. Ten of its eleven hunks are the 4.0.7
  hunks at new offsets. The eleventh adds the same source-tracking calls
  around 2.x's text-token merge, which builds its output differently from 4.x.

## How the forks are wired

- `package.json` lists the 4.x fork as the `picomatch` devDependency.
- `overrides.picomatch` is `$picomatch`, so every consumer gets that fork.
- `overrides.micromatch.picomatch` keeps micromatch on its declared `^2`
  line. npm resolves that nested `file:` path from micromatch's own
  directory, so it begins with `../../`. The lockfile records it as
  `file:vendor/picomatch-2.3.2-kfm.1.tgz`.

## Verification

`tests/picomatch-redos.test.mjs` checks that vite, tinyglobby and micromatch
each resolve their fork, that the advisory's inputs return promptly, and that
ordinary globs keep their results.

A differential check compared each fork with its unpatched base over 60,000
generated patterns and 360,000 matches. The two forks changed exactly the
same 38 results.

- **Malformed patterns:** most of the changed results come from patterns with
  unbalanced parentheses.
- **Repeated wildcard extglobs:** the rest are well-formed patterns such as
  `*(**)` and `+(**)`. The fix now compiles these as literal text, as
  unpatched picomatch already does for other risky repeats such as `+(+(a))`.

## Rebuilding and removal

To rebuild a fork:

1. Unpack `npm pack picomatch@<base>`.
2. Apply the matching patch to `lib/parse.js`.
3. Set `version` to `<base>-kfm.1`.
4. Run `npm pack`.

The output is byte-reproducible.

When a fixed picomatch release exists, remove the forks, the devDependency
and both overrides.
