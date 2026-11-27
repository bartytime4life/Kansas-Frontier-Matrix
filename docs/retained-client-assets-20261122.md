# Browser files kept from earlier builds: how much room is left (2026-11-22)

## The limit a publish will eventually meet

Every build stages its browser scripts and styles into `public/assets`
(`scripts/stage-public-client-assets.mjs`) and never removes one, so that a page opened before
a publish can still load its scripts after it. The framework then copies `public/assets` back
into the build's own output, and the staging step refuses to finish when that folder holds more
than **4,096 entries** or **256 MB**:

```
Error: CLIENT_ASSET_COUNT_LIMIT
```

A build that stops there does not publish. Because nothing is pruned, each publish moves the
host closer to that point, and nothing outside the host can list the folder to see how close it
is.

This was met on 2026-11-22 in a development checkout that had been built about 200 times since
2026-11-13: 4,097 entries and 168 MB, 201 versions of the main page script among them. Clearing
the two ignored folders (`dist/` and `public/assets/`) let it build again. CI is not affected,
because it builds in a fresh checkout.

## What is known about the public host

The host keeps the folder between publishes. On 2026-11-22, 291 script and style files from
builds made since 2026-11-13 were still served by the public site, 32 versions of the main page
script among them. With their compressed copies that is at least 845 entries and 34 MB. Publishes
made before 2026-11-13 are not in that count, so the true figures are higher by an unknown
amount.

At the rate seen in those builds (about 26 entries a publish) the entry limit is somewhere
between roughly 60 and 125 publishes away. That is an estimate from a lower bound, not a
measurement.

## What changed

The build now records how much of each limit was used when it started, in the identity file it
already writes, so `/api/build` shows it:

```json
"retainedClientAssets": { "entries": 1912, "bytes": 81234567, "entryLimit": 4096, "byteLimit": 268435456 }
```

- Counts only. No file name is published.
- The build log prints the same line: `Browser files kept from earlier builds: 1912 of 4096
  entries, 77 of 256 MB`.
- The figures are from the start of the build, before its own new files are added. One publish
  adds at most a few hundred entries.
- `sourceDigest`, `sourceFileCount`, `--print` and `--verify` are unchanged: the comparable
  identity still covers application inputs only. The field is absent when the folder is absent
  or empty, as in CI.

## What it does not do

It does not prune anything and does not raise a limit. After the next publish the real numbers
will be on `/api/build`. Then the choice is between removing files that no build since some
date has used (which needs a reliable record of what each build used), raising the limits, or
clearing the folder at a quiet hour and accepting that pages left open across that publish must
reload.

## Inspect a checkout before reviewing cleanup

From the hosted application root, run this while the build and staging processes are idle.

```sh
node scripts/stage-public-client-assets.mjs --inventory
```

The command inventories `public/assets` without writing to the checkout. It reports the current
entry and byte counts, compression variants whose same-name uncompressed file is absent, and
temporary files named by the staging process. Unrecognized entries and links are counted.
Candidate names appear only in the command output. A candidate requires review against active
and rollback releases before disposal. Ordinary hashed files, including files from earlier
builds, remain outside the candidate list.

## Tests

`tests/build-identity.test.mjs` checks the counts, that the limits equal the ones the staging
step enforces, that no file name is written, and that `--print` is unchanged.
`tests/build-identity-http.test.mjs` accepts the field on `/api/build` only with these four
positive integers.
`tests/public-client-assets.test.mjs` checks that the inventory distinguishes paired variants
from candidates, refuses a linked inventory directory, and leaves the files intact.
