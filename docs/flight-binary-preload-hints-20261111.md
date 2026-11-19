# Flight preload normalization without binary corruption

This follows the React 19.2.9 dependency update in PR #5809, from public
composition `b98fe7bd1620a2c207f906de1fb34377ea84fc61`. React and the existing
vendored Vinext archive remain unchanged.

## Reproduced defect

Vinext's `dist/server/rsc-stream-hints.js` decodes every Flight chunk with a
`TextDecoder`, replaces stylesheet preload text, then reencodes it. Flight
contains length-framed binary and long-text rows alongside newline-framed JSON
and resource hints. Decoding arbitrary binary replaces invalid UTF-8 bytes;
replacing hint-like text inside a payload also changes its declared length.

A harmless independent typed array containing `ff 80 0a` fails the React client
decoder with `Connection closed`. This was reproduced with the original helper
on both React 19.2.8 and 19.2.9 during the dependency update. The follow-up also
reproduces corruption of long Unicode text containing an apparent `:HL` row.
Eighteen focused byte-preservation/codec assertions fail against the original
helper, including all fourteen length-framed tags.

This is a transport compatibility repair. No application producer triggering
the original symptom or application-level RCE was established. It does not
change the exploitability limits or unresolved GitHub-alert mapping recorded
in [the React dependency notes](react-flight-security-20261111.md).

## Replacement and integration

`server/rsc-stream-hints.mjs` tracks the pinned Flight framing in bytes:

- Copy declared payload lengths for `T A O o U S s L l G g M m V` directly to
  the output. Embedded newlines, invalid UTF-8, and apparent resource hints
  inside those payloads remain byte-exact. Zero-length payloads work too.
- Pass ordinary newline-framed model rows through without decoding or waiting
  for a whole row.
- Buffer only candidate `H` hint rows. Rewrite only valid `HL` JSON arrays
  whose second item is the literal `"stylesheet"`, keeping URL escapes, options
  and other fields intact. Other hint types and malformed hints pass unchanged.
- Limit header buffering to 64 bytes and candidate hints to 64 KiB. Oversized
  hints pass unchanged, and normalization resumes on the next row. Invalid or
  unsafe framing makes the rest of that stream opaque; truncated data is
  forwarded unchanged for the downstream codec to handle.
- Preserve upstream errors and downstream cancellation through `pipeThrough`.

The Vite alias replaces only the resolved internal Vinext helper path used by
its generated App Router RSC entry. It applies to development and production;
no installed package mutation, postinstall hook, fork repack, or dependency
change is required. The production artifact assertion verifies selection of
the repository helper and exclusion of Vinext's original text-only helper.
The original React security rejection checks now exercise the selected helper.

The tag table is tied to the pinned React 19.2.9 protocol. Review it and the
generated Vinext import whenever upgrading either dependency; an unknown future
length-framed tag is outside this implementation's verified contract.

## Verification

- Clean `npm ci --no-audit` succeeds; manifest, lockfile and vendor archives
  are unchanged.
- Production build and TypeScript pass on Node 22.23.3. Scoped ESLint passes
  for the helper, Vite config and both transport test files.
- All 33 focused checks pass on Node 22.23.3 and Node 24.19.0. The framing
  cases cover every two-chunk split and one byte per chunk, non-UTF8 data,
  embedded row text, zero lengths, malformed/truncated frames, oversized hints,
  early streaming, errors and cancellation. Real production React encoder and
  decoder checks preserve the binary array, DataView and long Unicode text.
- The full Node 22 suite passes: 2,910 passed, 25 skipped, zero failures.
- A real React stylesheet element emits `:HL["/fixture.css","style"]`, while
  its model retains `rel="stylesheet"`. Served home HTML retains its CSS links
  with no `as="stylesheet"` attribute. Development config resolves the same
  alias, and the emitted production RSC bundle selects the new helper.
- All five production-browser journeys have passing results: welcome/topic
  composition on desktop and phone, and independent Reports/Stories drafts on
  desktop, phone and short landscape. The initial desktop journey exceeded its
  90-second timeout while the full suite was also running; the other four
  passed. Its isolated retry passed in 40.19 seconds with unchanged code and
  the same 90-second limit. Both attempt logs are retained.

Repeat the substantive checks after building:

```bash
npm ci --no-audit
npm exec --yes --package=node@22.23.3 -- npm run build
npm exec --yes --package=node@22.23.3 -- tsc --noEmit
npx --no-install eslint vite.config.ts server/rsc-stream-hints.mjs \
  tests/rsc-stream-hints.test.mjs tests/react-flight-transport.test.mjs
npm exec --yes --package=node@22.23.3 -- node --test \
  tests/rsc-stream-hints.test.mjs tests/react-flight-transport.test.mjs
node --test tests/rsc-stream-hints.test.mjs tests/react-flight-transport.test.mjs
npm exec --yes --package=node@22.23.3 -- node --test --test-concurrency=4 tests/*.test.mjs
# Against a separately started, built production loopback server:
KFM_TEST_CHROME=/path/to/chromium-wrapper \
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5216 \
node --test --test-concurrency=1 \
  --test-name-pattern='welcome cards open directly|draft workspaces preserve' \
  tests/explorer-startup.browser.mjs
```

Logs and baseline comparisons are outside the application tree at
`/workspace/scratch/kfm-flight-binary/`. Browser fixture APIs return isolated
unavailable responses; they do not establish live provider or AI availability.
Rollback is reverting the helper, alias and accompanying tests together; retain
the patched React dependency family. No deployment, source admission, database
change, model setting or original Sites binding change is included.
