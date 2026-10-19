# Subsurface candidate preparation and publication hold

The WWC5/core snapshot previously committed under `public/data/subsurface`
is treated as disclosed. This containment removes the 257 exact-coordinate
tiles and statewide locator from the current source tree. It replaces the
manifest with an empty `PUBLICATION_HELD` notice. Repository history, downloaded
copies, previously saved client report snapshots, saved Site versions, deployed
artifacts and CDN caches are not erased
by this source change; their inventory and remediation remain separate work.

Exact well/core records are withheld. Underground reports the hold without
fetching records, including when older assets remain cached. Separate survey,
aquifer and soil features retain their existing behavior. `geophysics.json`
is preserved byte-for-byte and pinned by the containment gate; this does not
claim a new rights or release review for that separate carrier.

## Private preparation

`scripts/prepare-subsurface.py` retains deterministic pinned-source parsing,
original intervals, datum/depth caveats and source integrity checks for private
review. Python 3.10+ and `pyproj==3.7.1` are preparation dependencies.
Both directories must be explicit, separate, access-controlled external paths;
output must be new or empty. Its existing parent (or nearest existing ancestor
when creating nested directories) and any existing output must belong to the
effective user and have owner-only permissions, normally `0700`:

```sh
python scripts/prepare-subsurface.py --input-dir /private/cache/kgs --output-dir /private/quarantine/kgs-candidate
```

There is no default public output. CLI and imported `build()` validate paths
before dependency imports, downloads or writes. Resolved paths inside the
repository/application or named `public`, `dist`, `.next` or `published` are
rejected, including traversal and symlink aliases. Every output path component
is opened without following symlinks. Before dependencies or downloads, the
command anchors the output to a retained POSIX directory descriptor, creates
missing directories with `0700`, and checks owner-only directory permissions.
All tiles, the locator and the manifest are created exclusively relative to
that descriptor with `0600` file permissions; existing files and links are never
overwritten. The selected directory's identity is rechecked before writing the
manifest. Unsupported platforms fail closed. A failed run can leave an empty or
partial private directory without a manifest; inspect and retain it separately
before retrying into another new or empty directory.

The candidate manifest is `RESTRICTED_REVIEW_REQUIRED`; its file references are
relative. These checks do not audit filesystem ACLs, defend against a malicious
process running as the same user or root, or authorize promotion. Operators must
still supply genuinely restricted storage.
Preparation continues to exclude ownership/direction fields; that exclusion
alone does not make exact geometry or stable provider joins safe to release.

## Delivery denial and future release

`scripts/validate-subsurface-public.mjs` permits only the exact empty hold notice
and unchanged separate survey asset in the reserved delivery directory. It also
rejects recognizable renamed JSON/gzip well/core records (including GeoJSON
properties/geometry separation) and locators, invalid
JSON carriers and static symlinks. It checks the actual source tree through
Vite configuration and the direct build helper; the helper checks `dist/client`
after building. Both local launcher branches and `npm start` validate their
static assets. Arbitrary unrelated binary encodings are outside this bounded
gate; this is containment, not a universal sensitive-data classifier.

The geology validator's `--site-public` mode runs this real-asset check. Its
existing `--fixtures` mode remains synthetic declaration validation and grants
no release authority. CI watches source public assets and affected tooling. The historical 2026-08-14
authoring receipt remains unchanged and is replayed against the exact pre-fix
ancestor `c52ceb2dcc028dd35da266f2c7702ca6fa108e44`; it does not bind or approve
the containment patch. Current containment is checked independently.

No approval boolean or self-declared release manifest bypasses the hold. A
future public-safe generalized/aggregated carrier needs a separate reviewed
implementation binding artifact digests to SourceDescriptor, rights and
sensitivity decisions, PolicyDecision, transform/redaction/aggregation receipts,
EvidenceBundle closure, ReviewRecord, ReleaseManifest, correction and rollback
records. Exact/source-precision public geometry remains denied by the geology
contract. Public provider availability does not resolve these KFM gates.

## Verification and placement

```sh
node --test tests/subsurface-assets.test.mjs tests/subsurface-worker.test.mjs
node scripts/validate-subsurface-public.mjs
```

Files reuse existing `apps/site/source/scripts`, `tests`, `app`, `public` and
`docs` responsibilities, plus repository `tools/validators` and `.github`.
Accepted ADR-0029 adopts Directory Rules v2 (`docs/doctrine/directory-rules.md`);
its §§2.2, 10, 11 and 15 support containment without creating a parallel data,
policy or release home. The original Directory Rules PDF was unavailable in
this workspace; the accepted canonical doctrine and ADR were checked.

Rollback must preserve the delivery hold: revert unrelated regressions or use
a previously safe build. Restoring the disclosed exact assets into `public`
requires no ordinary rollback shortcut. This patch does not rewrite history,
merge, deploy, publish, purge caches or approve a public derivative.
