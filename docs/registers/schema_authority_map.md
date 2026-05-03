# Schema Authority Map
- current homes: `schemas/`, `contracts/`, `jsonschema/`.
- likely authority: contracts=semantic meaning; schemas/jsonschema=machine validation.
- allowed interim use: dual-home with ADR-0001/0012 references.
- prohibited duplication: duplicate schema IDs across homes.
- migration rule: no cross-home machine moves without ADR.
- validator expectation: detect duplicate IDs and undocumented homes.
- decision owner/status: CONFLICTED / pending maintainer decision.
- rollback risk: high (runtime/API breakage).
