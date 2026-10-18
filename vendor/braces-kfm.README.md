# Bounded Braces dependency repair

`braces-3.0.3-kfm.1.tgz` contains upstream `braces@3.0.3` plus the inspectable
`braces-kfm.patch`. The upstream version, MIT license, and all unrelated source
remain intact. Package metadata adds `kfmPatch: depth-limit-128-v1`; this is not
an upstream release or a claim that the registry advisory is withdrawn.

The source package is `https://registry.npmjs.org/braces/-/braces-3.0.3.tgz`.
Upstream SHA-512 (base64):
`yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==`.
This matches the parent commit's package lock.
Patched archive SHA-256:
`760bbcd249170e0d5f57195bb643d2b2228cd21e562fb32fca527cadcfc53643`.
The current lock pins this archive's SHA-512. The direct file dependency and
`$braces` override make both fast-glob dependency chains use these same bytes.

The [advisory](https://github.com/advisories/GHSA-vfj7-8cjw-p6xm) lists no patched
upstream version as checked on 2026-10-18. Nested input below the 10,000-character
limit exhausted the recursive compile, expand and stringify stacks. The local
repair bounds parser brace/parenthesis nesting, each recursive AST walker, and
both AST-parent walks at a fixed depth of 128. It throws an explicit RangeError;
callers cannot raise the cap. A parsed pattern may contain at most 127 nested
containers, leaving room for its leaf. Direct AST inputs are bounded too.
Escaped, quoted and character-class delimiter text does not consume nesting.
Recursive array append/flatten helpers use the same cap. Malformed AST values
other than strings receive an explicit TypeError before array coercion or
expansion. Parsed ASTs already use strings; build-tool callers retain that form.

This affects build/lint glob processing. No public KFM request path to the
vulnerable parser was established. Excessively nested patterns are deliberately
rejected; ordinary alternatives, ranges, literal delimiters, ordering and
duplicate/empty handling remain unchanged. Existing range/length limits remain.
This is not a claim to solve every possible brace-expansion resource attack.

Reproduce by obtaining the exact upstream package with `npm pack braces@3.0.3`,
verifying its integrity against the parent lock, extracting into an isolated
directory, and applying `patch -p1 < braces-kfm.patch`. The committed archive is
a sorted USTAR archive of those files under `package/`, mode 0644, uid/gid/mtime
zero, compressed with gzip's filename empty and mtime zero. Inspect the patch
and run `node tests/braces-depth.test.mjs` after a fresh `npm ci`.

Raw `npm audit` still reports the original advisory and its eight affected
package entries because the upstream version remains 3.0.3. The mitigation is
separate evidence; no audit suppression, version disguise or acceptance waiver
is added. Reverting this dependency change restores the vulnerable upstream
bytes and requires renewed risk review.

Placement follows the existing `vendor/` runtime-package precedent. Regression
tests belong in `tests/`; application code, database schemas and AI stores are
not part of this dependency patch.
