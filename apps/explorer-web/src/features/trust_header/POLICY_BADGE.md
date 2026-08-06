# Governed Policy Badge and Trust Header Slice

## Status

**PROPOSED, fixture-first implementation.** This slice replaces the one-line Trust Header placeholder with a bounded projection of the existing `GovernedEvidenceDrawerProjection`. It does not create a policy engine, release decision, evidence resolver, source authority, or public route.

## Responsibility and placement

The implementation stays under `apps/explorer-web/src/features/trust_header/` because it is app-local UI composition. It references the existing adapter-owned browser projection and delegates detail to the existing Evidence Drawer boundary. Contracts, schemas, policy, lifecycle records, release authority, and canonical evidence remain in their existing responsibility roots.

## Finite rendering behavior

| Governed projection | Header behavior | Evidence Drawer action |
|---|---|---|
| `ANSWER / SUPPORTED` | Show text badges for outcome, policy, review, release, freshness, and correction | Available through the caller-supplied governed callback |
| `ABSTAIN` | Show a generic insufficient-support state | Not available |
| `DENY` | Show a generic restricted state | Not available |
| `ERROR` | Show a generic unavailable state | Not available |
| Missing or malformed projection | Render no Trust Header | Not available |

Negative states never reflect evidence identifiers, citations, denial explanations, upstream error text, unknown fields, or fixture canaries. The compact option changes only the layout marker; it does not remove any required text or ARIA label.

## Trust boundary

The module:

- makes no network request;
- reads no browser persistence;
- reads no lifecycle or canonical data store;
- invokes no model or provider runtime;
- does not decide policy, review, release, freshness, correction, or publication state;
- does not resolve an `EvidenceRef` or inspect a canonical `EvidenceBundle`;
- uses text and ARIA status semantics rather than color-only meaning;
- is not connected to a released public route by this change.

A successful unit, browser, or hosted check proves only the bounded repository-local projection and interaction behavior described above.

## Validation

The dependency-closed validation surface is:

- strict Explorer TypeScript compilation;
- unit tests for supported, finite-negative, malformed, and absent projections;
- browser tests for text/ARIA badges, compact preservation, generic negative states, and Evidence Drawer delegation;
- static denial checks for transport, browser persistence, lifecycle paths, and model-runtime references;
- generated-receipt integrity verification.

## Rollback

Revert the implementation commit. No data migration, source correction, release withdrawal, cache invalidation, or publication correction is required because this slice emits no release and wires no public route.
