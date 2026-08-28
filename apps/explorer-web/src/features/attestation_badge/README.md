<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/apps-explorer-web-attestation-badge
title: Explorer Attestation Badge
type: component-readme
version: v1.0.0
status: proposed; fixture-first; public-safe projection; non-authoritative
owners: OWNER_TBD - Explorer UI steward; evidence steward; release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public
owning_root: apps/
responsibility: render one compact, text-first verification-evidence signal from a governed public-safe projection
related: [../../adapters/AttestationBadgeProjection.ts, ../../../../docs/architecture/evidence-drawer.md, ../../../../docs/architecture/ui/TRUST_BADGES.md, ../../../../contracts/evidence/release_bound_run_receipt.md]
[/KFM_META_BLOCK_V2] -->

# Explorer Attestation Badge

This fixture-first component implements the bounded reader surface proposed by Pass 32 card `KFM-P32-FEAT-0011`. It reports whether an upstream governed projection says the required attestation, run-receipt, EvidenceBundle, and release references are available.

## Boundary

The badge is a signal that supporting references exist. It is not evidence, a signature verifier, a `RunReceipt`, an `EvidenceBundle`, a policy decision, review approval, release approval, or publication authority.

- `AttestationBadgeProjection.ts` accepts an exact app-local projection and rejects unknown fields.
- Only `ANSWER / CHECKS_VERIFIED` carries reference handles.
- `ABSTAIN`, `DENY`, and `ERROR` use fixed copy and carry no references or free-form diagnostics.
- The browser performs no network access, cryptography, evidence resolution, lifecycle-store reads, persistence, promotion, release, or publication.
- A positive action delegates the parsed projection to a caller-supplied inspection callback; the badge never claims that its own rendering proves verification.

## Directory Rules basis

The UI adapter and component live under `apps/explorer-web/`; public-safe synthetic payloads live under `fixtures/ui/`; tests live beside the Explorer test harness; exploratory source reconciliation lives under `docs/intake/exploratory/`; authoring accountability lives under `data/receipts/generated/`. No schema, evidence, receipt, policy, review, release, proof, or publication authority is created here.

## Validation

```bash
pnpm --filter explorer-web run test:unit
pnpm --filter explorer-web run build
```

The hosted UI workflow installs a browser and exercises the companion Playwright fixture. Local browser execution may be skipped when Chromium is unavailable.

## Rollback

Revert this additive component packet. No source, lifecycle, policy, release, deployment, or public artifact requires restoration.
