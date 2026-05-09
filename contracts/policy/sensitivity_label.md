# sensitivity_label

Schema: `https://schemas.kfm.local/contracts/v1/policy/sensitivity_label.schema.json`

## Meaning
Defines the governed semantics for `sensitivity_label` in KFM.

## Fields
- See schema properties; each field carries provenance-safe, policy-evaluable meaning.

## Invariants
- Required fields must exist.
- Enumerated values remain finite where specified.
- No undeclared fields unless explicitly allowed.

## Lifecycle
- Created in RAW/WORK processing.
- Validated before promotion decisions.
- Released through governed interfaces.
- Superseded by newer versioned records.

## Related contracts
- Neighbor contracts in the same family and runtime policy decisions.

## Open questions
- NEEDS VERIFICATION: additional domain-specific constraints may be added in follow-up PRs.
