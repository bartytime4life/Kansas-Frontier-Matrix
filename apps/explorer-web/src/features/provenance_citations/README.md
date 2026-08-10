<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/apps-explorer-web-provenance-citations
title: Explorer Provenance Citations Panel
type: component-readme
version: v1.0.0
status: proposed; fixture-first; public-safe projection; non-authoritative
owners: OWNER_TBD - Explorer UI steward; provenance steward; evidence steward; release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public
owning_root: apps/
responsibility: render bounded public source links, DOI labels, and governed provenance/release references
related: [../../adapters/ProvenanceCitationsProjection.ts, ../../../../docs/architecture/evidence-drawer.md, ../../../../contracts/evidence/evidence_bundle.md]
[/KFM_META_BLOCK_V2] -->

# Explorer Provenance Citations Panel

This fixture-first component implements the reader surface proposed by Pass 32 card `KFM-P32-FEAT-0019`: source citation blocks, DOI labels, a fixed KFM republication note, and references to the governing PROV activity and release manifest.

## Boundary

The panel displays a bounded upstream projection. It does not fetch a source, query a provenance graph, resolve an `EvidenceBundle`, infer license or rights, establish evidence sufficiency, execute policy, authenticate review, authorize release, or publish.

- Only exact `ANSWER / CITATIONS_AVAILABLE` payloads may carry citations and references.
- `ABSTAIN`, `DENY`, and `ERROR` carry no citations, URLs, identifiers, or free-form diagnostics.
- Links must be canonical public HTTPS URLs without credentials, fragments, IP-literal hosts, or localhost targets.
- A DOI, when present, must match its `https://doi.org/` link exactly.
- Unknown fields, duplicate citation IDs, excessive arrays, unsafe text, and incomplete positive closure fail closed.

## Directory Rules basis

UI code remains under `apps/explorer-web/`; synthetic public-safe inputs remain under `fixtures/ui/`; source reconciliation remains under `docs/intake/exploratory/`; authoring accountability remains under `data/receipts/generated/`. No contract, evidence, provenance, policy, rights, review, release, or publication authority is created.

## Validation

```bash
pnpm --filter explorer-web run test:unit
pnpm --filter explorer-web run build
```

The hosted UI workflow installs a browser and exercises the companion Playwright fixture.

## Rollback

Revert this additive component packet. It mutates no data, evidence, provenance, policy, review, release, deployment, or publication state.
