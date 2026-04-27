# opa-gate

Composite action wrapper for running an OPA (or equivalent policy) decision command and failing closed unless output matches an allow pattern.

## Inputs

- `command` (required): policy decision command.
- `allow-pattern` (optional): regex that indicates success.

## Output

- `decision`: raw command output.

## Example

```yaml
- name: Policy gate
  uses: ./.github/actions/opa-gate
  with:
    command: "opa eval --format raw --data policy --input input.json 'data.kfm.allow'"
```
