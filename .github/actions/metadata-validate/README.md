# metadata-validate

Composite action that verifies markdown files contain a required metadata token (defaults to `[KFM_META_BLOCK_V2]`).

## Inputs

- `files` (optional): newline-delimited list of files to validate. If omitted, scans all `*.md` files.
- `required-token` (optional): token to require in each file.

## Outputs

- `checked-count`
- `missing-count`

## Example

```yaml
- name: Validate metadata blocks
  uses: ./.github/actions/metadata-validate
  with:
    required-token: "[KFM_META_BLOCK_V2]"
```
