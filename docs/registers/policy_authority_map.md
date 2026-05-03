# Policy Authority Map
Current homes: `policy/`, `policies/`.
Likely authority: `policy/` primary pack; `policies/` compatibility residue.
Prohibited duplication: duplicate policy package names across homes.
Migration rule: require ADR-0013 aligned decision.
Validator expectation: detect duplicate package names and split-home drift (PROPOSED).
Owner/status: CONFLICTED / needs policy owner resolution.
Rollback risk: high for runtime regressions if moved blindly.
