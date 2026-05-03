# eBird Preservation and Fixity (Layer 40)

Layer 40 adds local-only fixity and long-term preservation governance. It does not mutate archived originals, does not call external storage/signing/notarization APIs, and does not download eBird data.

## CLIs
- `kfm-ebird-fixity`
- `kfm-ebird-preservation`

Both are offline, synthetic-safe, and produce public-safe summaries only.
