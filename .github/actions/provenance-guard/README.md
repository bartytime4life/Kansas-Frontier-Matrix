# provenance-guard

Composite action that validates a file's SHA-256 checksum against an expected value.

## Inputs

- `file` (required)
- `expected-sha256` (required)

## Output

- `actual-sha256`

## Example

```yaml
- name: Verify artifact digest
  uses: ./.github/actions/provenance-guard
  with:
    file: dist/build.tar.gz
    expected-sha256: ${{ secrets.BUILD_SHA256 }}
```
