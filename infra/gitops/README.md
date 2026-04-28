# infra/gitops/

- Status: PROPOSED / NEEDS VERIFICATION
- Owner: NEEDS VERIFICATION
- Runtime profile: NEEDS VERIFICATION
- Public exposure posture: Deny-by-default until explicit review evidence exists.
- Source of truth for related policy/contracts: ../../policy/, ../../contracts/, ../../schemas/
- Secrets posture: No plaintext secrets; use environment-level secret management.
- Rollback path: Revert infra change + update release/correction notes as applicable.
- Verification commands:
  - `find infra/gitops -maxdepth 2 -type f | sort`
  - `git status --short infra/gitops`
- Remaining UNKNOWN / NEEDS VERIFICATION:
  - Declarative reconciliation plans and environment synchronization controls.
  - Lane-specific implementation files and runtime evidence are not yet present.
