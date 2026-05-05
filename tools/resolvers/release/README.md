# tools/resolvers/release

Release-level resolver utilities that verify whether a `ReleaseManifest` can be
closed over all required references before publishing.

## Included tool

- `resolve_release_manifest.py` — offline closure resolver with finite outcomes:
  - `PUBLISHABLE`
  - `ABSTAIN`
  - `DENY`
  - `ERROR`

## What it checks

For each artifact entry in a release manifest, the resolver checks:

- `artifact_ref`
- `evidence_ref`
- `provenance_ref`
- `stac_ref`
- `dcat_ref`
- optional `run_receipt_ref`
- optional `attestation_ref`

It also:

- validates `spec_hash` alignment between manifest and artifacts
- runs validators for recognized file kinds:
  - release manifest (`*.release-manifest.json`)
  - PROV sidecar (`*.prov.jsonld`)
  - STAC item (`*.item.json`)
  - DCAT dataset (`*.dataset.jsonld`)

## Usage

```bash
python tools/resolvers/release/resolve_release_manifest.py \
  examples/promotion/release/kfm-demo.release-manifest.json
```

### Strict remote mode

By default, non-placeholder HTTP(S) references are reported as warnings in
offline mode. To fail closed for those references, enable strict mode:

```bash
python tools/resolvers/release/resolve_release_manifest.py \
  examples/promotion/release/kfm-demo.release-manifest.json \
  --strict-remote
```

In strict mode, unresolved remote references are treated as `ABSTAIN`.

## Notes

- `kfm://` references are treated as logical references and require an external
  mapping layer.
- `https://example.invalid/...` placeholders are accepted for fixture-safe test
  data.
