# Patched picomatch

`picomatch-4.0.7-kfm.1.tgz` is `picomatch@4.0.7` with the upstream fix for
[GHSA-fc5q-39xc-vjpf](https://github.com/advisories/GHSA-fc5q-39xc-vjpf)
applied. That advisory is a high-severity ReDoS through repeated extglobs, and
no fixed picomatch release exists.

- **Change:** only `lib/parse.js` and the `version` field in `package.json`.
  `lib/parse.js` is patched with
  [`configs/dependency-patches/picomatch-4.0.7.patch`](../../../../configs/dependency-patches/picomatch-4.0.7.patch),
  the same patch the root pnpm workspace applies.
- **Use:** `package.json` lists the fork as a devDependency, and `overrides`
  points every `picomatch` in the tree at it through `$picomatch`. vite,
  tinyglobby and fdir, all build-time tooling, load it.
- **Test:** `tests/picomatch-redos.test.mjs` checks that vite resolves the
  fork, that the advisory's inputs return promptly, and that ordinary globs
  keep their results.

Fork SHA-256:
`d50e8063019826c9298e1d3bc1054c6c8867a3e20500b71bd1da90143bbe35df`

To rebuild it, unpack `npm pack picomatch@4.0.7`, apply the patch to
`lib/parse.js`, set `version` to `4.0.7-kfm.1`, and run `npm pack`. The output
is byte-reproducible.

Remove the fork, the devDependency and the override when a fixed picomatch
release exists.
