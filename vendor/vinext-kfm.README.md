# Local runtime package

`vinext-0.0.50-kfm.1.tgz` is a source-preserving fork of `vinext@0.0.50`.
It removes an unused social-image generator dependency and replaces that
optional shim with an explicit unsupported response. KFM does not import that
shim. The package retains its upstream license and all runtime paths used by
this Site.

Fork SHA-256:
`853832fbe391cf1c33c8d3d47447ccf441ed5cb83beffdc8cb97b806db4b244c`


## Standalone compressed data-file repair candidate

`vinext-0.0.50-kfm.2.tgz` retains kfm.1 and adds a bounded static-cache distinction:
`.gz`, `.br` and `.zst` files are transport variants only when their uncompressed
sibling exists. Standalone compressed files retain their own URL and bytes; gzip
data uses `application/gzip`, without `Content-Encoding`. Existing compressed
JavaScript/CSS negotiation remains intact. This repairs Node delivery only and
does not authorize publication of any held source asset.

Changed archive members: package metadata, static-file-cache.js and its embedded
source map. Upstream license and all other members remain unchanged.
SHA-256: `276f257130d285d8478403148737ae27f69fd5ee1ea86fdc8ce777cebe768b15`.

The owner clarified on 2026-10-13 that locations may remain precise when the
underlying data is public. Official KGS public-download records and its reuse
terms were checked for this candidate; see
[the scoped verification record](../docs/public-core-repair-20261013.md).
This clarification does not authorize private assets, source admission or
publication. The monorepo's separate PR #5110 containment is not changed here.
Tests use synthetic data, and the real-record journey runs on loopback.
