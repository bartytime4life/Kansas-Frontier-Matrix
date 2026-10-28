# Kansas people and history catalogue availability

`/history/people-events` displays an availability notice. Research records and
JSON/CSV downloads are withheld pending rights, sensitivity, evidence and release
review. The candidate catalogue, its public reader and the public CSV generator
are absent from this application. No replacement record export or release profile
is implied by the notice.

The history source directory, Prentis book reader, selected original downloads and
independently governed `/knowledge` search remain available. See
[kansas-history-library.md](kansas-history-library.md).

## Containment checks

The existing `scripts/validate-subsurface-public.mjs` command now composes the
subsurface and history denial checks. Existing development, pre/post-build and
startup entry points invoke that shared command. The direct local Worker also
checks built assets before opening the runtime or private configuration.

`scripts/validate-history-public.mjs` denies the reserved people-events asset
paths and research JSON/CSV profiles under other names, including gzip and Brotli
carriers. Changing lifecycle labels is not a release decision. The guard grants
no public release authority; any future derivative needs an independently
reviewed release contract and integration.

Regression tests use synthetic records. Local build and runtime checks do not
establish the state of an existing hosted version, historical artifacts or caches.
Restoring candidate assets or the retired exporter is not a valid mirror repair.
