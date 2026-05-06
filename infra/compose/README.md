# infra/compose/

- Status: PROPOSED / NEEDS VERIFICATION
- Owner: NEEDS VERIFICATION
- Runtime profile: NEEDS VERIFICATION
- Public exposure posture: Deny-by-default until explicit review evidence exists.
- Source of truth for related policy/contracts: ../../policy/, ../../contracts/, ../../schemas/
- Secrets posture: No plaintext secrets; use environment-level secret management.
- Rollback path: Revert infra change + update release/correction notes as applicable.
- Verification commands:
  - `find infra/compose -maxdepth 2 -type f | sort`
  - `git status --short infra/compose`
- Remaining UNKNOWN / NEEDS VERIFICATION:
  - Local or narrowly scoped multi-service orchestration descriptors and decision notes.
  - Lane-specific implementation files and runtime evidence are not yet present.
