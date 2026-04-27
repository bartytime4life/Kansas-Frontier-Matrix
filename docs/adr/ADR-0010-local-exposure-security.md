# ADR-0010: Local Exposure Security Posture

- **Status:** proposed
- **Date:** 2026-04-27
- **Decision area:** security / operations / network boundaries

## Context

Local deployments exposed via proxy, VPN, or public tunnels can bypass expected perimeter assumptions.

## Decision

Local exposure paths must follow minimum controls: authenticated access, transport security, audit logging, and restricted route surface for governed services.

## Alternatives considered

- **Open local tunnels for convenience:** rejected due to unacceptable risk.
- **Security by obscurity (unguessable URLs):** rejected as insufficient control.

## Consequences

### Positive

- Safer dev and review exposure patterns.
- Clear baseline for operational hardening.

### Negative / tradeoffs

- Additional setup burden for local sharing.
- May reduce speed of ad-hoc demos.

## Verification

- Security checklist validation for local exposure scripts/config.
- Automated checks for disallowed insecure defaults.

## Migration / rollback

Introduce secure defaults first, then block insecure exposure methods after grace period.
