# IdentityToken fixtures

These fixtures exercise the existing `identity_token` machine schema at
`schemas/contracts/v1/common/identity_token.schema.json`.

## Boundary

The fixtures test machine-shape behavior only. A schema-valid token is not proof of
object existence, actor identity, source authority, evidence closure, policy approval,
review, release, publication, or public safety.

The `valid/` lane covers the required fields and the optional `issuer`. The `invalid/`
lane covers missing required fields, an unsupported `kind`, additional properties, and
an invalid `issued_at` value. The IdentityToken validator opts into JSON Schema format
checking, so the schema's existing `format: date-time` declaration is enforced for this
fixture family. The shared runner remains backward-compatible by leaving format
checking disabled unless a validator explicitly opts in.

All fixture values are synthetic and public-safe.
