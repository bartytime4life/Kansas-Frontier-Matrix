# Scorecard alert 53: `braces` dependency currentness

Status on 2026-10-07: **OPEN / upstream patch unavailable**. The Scorecard
`VulnerabilitiesID` finding on `main@f4838068d2abebdc6962b5cabfe1be0dbf8791a7`
reports [GHSA-vfj7-8cjw-p6xm](https://github.com/advisories/GHSA-vfj7-8cjw-p6xm).
That advisory marks `braces` versions through 3.0.3 affected and lists no
patched version. The npm registry's latest release is 3.0.3; `braces@3.0.4`
returns 404. The 3.0.4 override added at that head was therefore removed in
this candidate. npm 11.4.2 then rejected the existing lockfile because its
optional `next/node_modules/sharp` entry was missing. Regenerating the lockfile
with npm 11 added that placeholder and normalized four development metadata
flags; it did not change the locked `braces` version or any package tarball
version. This is not a vulnerability fix or an alert dismissal.

The Site lockfile places `braces@3.0.3` in the development dependency tree.
Two paths reach it:

- `eslint-config-next` → `@next/eslint-plugin-next` → `fast-glob` →
  `micromatch` → `braces`;
- vendored `vinext` → `vite-plugin-commonjs` → `vite-plugin-dynamic-import`
  → `fast-glob` → `micromatch` → `braces`.

No Site source import of `braces` was found. A package-lock-only production
audit with `--omit=dev` reported zero vulnerabilities; the full audit still
reports this advisory and its dependent development packages. This limits the
observed exposure to developer/build tooling. It does not prove that every
glob pattern reaching those tools is safe. Do not suppress the alert on that
basis alone.

Candidate verification: `npm ci --dry-run --ignore-scripts --no-audit --no-fund`
completed with npm 10.9.2 and npm 11.4.2 after the manifest and lockfile
changes; `git diff --check` passed. These dry runs do not prove a full install,
build, deployment, or Site browser acceptance. Revisit when an upstream patched
release exists or a separately reviewed toolchain replacement removes
`braces`; update the manifest and lockfile together, run the Site install/build
tests and both production/full audits, then
confirm the Scorecard finding at the exact merged head. Keep alert 53 open until
that evidence exists.
