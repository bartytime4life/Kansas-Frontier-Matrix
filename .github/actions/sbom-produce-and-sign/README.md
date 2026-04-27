# sbom-produce-and-sign

Composite action that emits a deterministic SHA-256 inventory manifest for an artifact path and can optionally produce a detached signature.

## Inputs

- `artifact-path` (required): file or directory to inventory.
- `output-manifest` (optional): manifest output path.
- `signature-path` (optional): detached signature output path.

## Outputs

- `manifest-path`
- `signature-path` (only when generated)

## Notes

Signature generation requires:

- `openssl` in PATH
- `KFM_SIGNING_KEY_PEM` environment variable containing a PEM private key

## Example

```yaml
- name: Build SBOM manifest
  uses: ./.github/actions/sbom-produce-and-sign
  with:
    artifact-path: dist/
    output-manifest: dist/sbom.sha256
```
