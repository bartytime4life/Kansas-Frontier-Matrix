# IdentityToken fixtures

These fixtures exercise the existing `identity_token` machine schema at
`schemas/contracts/v1/common/identity_token.schema.json`.

## Boundary

The fixtures test machine-shape behavior only. A schema-valid token is not proof of
object existence, actor identity, source authority, evidence closure, policy approval,
review, release, publication, or public safety.

The `valid/` lane covers the required fields and the optional `issuer`. The `invalid/`
lane covers missing required fields, an unsupported `kind`, and additional properties.
The current shared JSON Schema runner does not enable format checking, so these fixtures
do not claim enforcement of RFC 3339 `date-time` semantics beyond the schema declaration.

All fixture values are synthetic and public-safe.
