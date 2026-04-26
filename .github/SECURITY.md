# Security Policy

This repository follows a fail-closed posture for rights, sensitivity, and release safety.

## Reporting a vulnerability

Please do **not** open public issues for suspected vulnerabilities.

1. Open a private security advisory through GitHub Security Advisories for this repo.
2. Include reproduction steps, impacted paths, and suggested severity.
3. If sensitive data exposure is involved, include exact objects/paths and time window.

## Response expectations

- Initial triage target: within 5 business days.
- If accepted, a fix and disclosure plan will be coordinated with maintainers.
- High-risk issues may require temporary feature disablement or release hold.

## Scope highlights

Security-sensitive areas include:
- `.github/workflows/` (automation and artifact handling)
- `policy/` (decision logic)
- `contracts/` and `schemas/` (validation boundaries)
- `apps/` and `tools/` (runtime/utility execution paths)
- `data/` and `release/` (receipts, proofs, publishable artifacts)
