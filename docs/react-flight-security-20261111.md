# React Flight security dependency candidate

This candidate starts at public Explorer composition
`784d56a6db16f8f2fb11d7692d35eabdfc40d3ba`, including merged PR #5808.
It updates only React, React DOM and `react-server-dom-webpack` from 19.2.8 to
19.2.9, with the corresponding lockfile metadata and transport regressions.
The existing framework archives, overrides, Next/Vite/plugin versions and
optional platform entries are preserved.

## Finding and static assessment

The production npm audit identified critical
[GHSA-xqc2-xf4c-x3h3 / CVE-2026-126187](https://github.com/advisories/GHSA-xqc2-xf4c-x3h3)
in the direct RSC dependency. The advisory affects `>=19.2.0 <19.2.9` and names
19.2.9 as its patched release on this line. Its RCE claim requires a rare
response containing multiple typed arrays and an attacker-controlled value.

The affected version is present in the manifest, lock and original server
bundle. This composition serves an anonymous Vinext App Router application.
Page Flight is encoded on the server and decoded again during SSR, so a client
homepage does not make the server codec irrelevant. The current build selects
the installed direct codec through the RSC plugin's alias.

The exact application exploit path remains **needs review**: neither the parent
investigation nor the independent read-only investigation found a concrete
server-component producer combining the advisory's required inputs. No
application `use server` function was found. Existing CSRF, body-size and
container-reference checks do not implement the upstream typed-array fix.
No applicable `SECURITY.md` exists in this worktree; the deployment and anonymous
service evidence comes from `AGENTS.md`, `server/start.mjs`, `vite.config.ts` and
`docs/godaddy-node-preview.md`.

The change applies the official dependency mitigation without claiming that an
application RCE was reproduced. React DOM and RSC require matching React
versions; all three pins therefore move together. Their declared peers remain
compatible with the existing Vinext, Next and RSC-plugin versions.

## Transport and compatibility checks

The harmless production-codec regressions derive from the upstream
[transport patch](https://github.com/react/react/commit/0c9913ae87283f96e868a8f1c20a3389827632d0).
They use separate Node processes for the React-server encoder and ordinary
SSR decoder. They cover:

- Distinct full-buffer aliases, including a DataView variant, must fail closed.
  Both raw-codec and actual Vinext-wrapper paths are checked.
- Independent arrays, an independent DataView, promised partial views and
  repeated references to the same view retain their ordinary values/identity.
- The ordinary independent-array control also traverses Vinext's wrapper.
- Built RSC and SSR servers select the direct codec and exclude the plugin
  fallback and Next's separate bundled codec. The RSC server also contains the
  declared React version guard.

On 19.2.8, the four unsafe-view assertions fail because transport succeeds;
the six controls/artifact checks pass. After the patch, all ten pass on Node
22.23.3 and Node 24.19.0. These are transport regressions, **not an RCE payload**.
Whole-buffer transport may consume/detach its buffer; reusing one view by
identity or copying distinct views follows the upstream contract. Partial views
retain their sibling buffer.

A clean `npm ci` passes. The production build and TypeScript check pass on
Node 22.23.3, matching the repository's CI version. Scoped test lint passes.
The complete Node 22 suite passes: 2,887 passed, 25 skipped, zero failures
(2,912 total).
The production audit changes from one critical/seven moderate findings to
zero critical, zero high and seven moderate findings; this GHSA is absent.
The remaining moderate findings are not resolved by this patch.

All five existing hydrated-browser journeys pass against the production Node
22 server: welcome/topic composition at desktop and phone widths, and independent
Reports/Stories draft persistence at desktop, phone and short landscape sizes.
Provider/AI requests use isolated unavailability fixtures. These checks do not
certify live providers, hosted deployment or every client/runtime version.

## Review findings and limits

An independent read-only candidate review found no introduced bypass or material
application regression. It identified a separate, pre-existing Vinext transport
defect: `dist/server/rsc-stream-hints.js` decodes the entire Flight stream as
UTF-8 before re-encoding it. Non-UTF-8 binary rows can therefore change byte
length or have embedded hint-like text rewritten. A harmless wrapped control
containing bytes `ff 80 0a` fails decoding with `Connection closed` on **both**
19.2.8 and 19.2.9. No application producer exercising this condition was found.
This establishes a binary-transport compatibility defect, not an advisory
bypass or RCE. It remains a separate framework follow-up; this dependency patch
does not claim to repair it.

The RSC plugin still contains an unselected 19.2.6 fallback and Next contains
its own unselected codec. The emitted-bundle checks guard the supported direct
codec path; they do not claim those bundled copies were updated.

GitHub reported two critical alerts on the repository's default branch, but its
Dependabot REST endpoint returned Forbidden. Those two records and manifest
paths remain unmapped. The advisory above was independently imported from the
saved npm audit and verified against the public advisory page. The audit result
is scoped to this Explorer lockfile, not proof that GitHub's records are closed.

## Commands and retained evidence

```bash
npm ci --no-audit
npm exec --yes --package=node@22.23.3 -- npm run build
npm exec --yes --package=node@22.23.3 -- tsc --noEmit
npm exec --yes --package=node@22.23.3 -- node --test tests/react-flight-transport.test.mjs
node --test tests/react-flight-transport.test.mjs
npm exec --yes --package=node@22.23.3 -- node --test --test-concurrency=4 tests/*.test.mjs
npm audit --omit=dev --json
KFM_TEST_CHROME=/path/to/chromium-wrapper \
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5215 \
node --test --test-concurrency=1 \
  --test-name-pattern='welcome cards open directly|draft workspaces preserve' \
  tests/explorer-startup.browser.mjs
```

Logs, audit metadata, upstream evidence, the harmless wrapper comparison and
static triage/review notes are retained outside the app tree at
`/workspace/scratch/kfm-react-security/`. No deployment, database operation,
source admission, model setting or original Sites binding change is included.
Any later compatibility adjustment should keep the React family aligned and
use a patched release rather than restoring the affected 19.2.8 version.
