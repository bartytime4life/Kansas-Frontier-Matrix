<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-provenance-citations-source-map
title: Pass 32 provenance citations panel - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; implementation-mapped; non-authoritative
owners: OWNER_TBD - UI steward; provenance steward; evidence steward; release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-FEAT-0019 with current repository authorities and the bounded Explorer implementation
truth_posture: CONFIRMED source statement and current-repository overlap / PROPOSED app-local implementation / UNKNOWN production integration and runtime proof
related: [../../../apps/explorer-web/src/features/provenance_citations/README.md, ../../architecture/evidence-drawer.md, ../../../contracts/evidence/evidence_bundle.md]
[/KFM_META_BLOCK_V2] -->

# Pass 32 provenance citations panel - governed implementation source map

## Source statement

`KFM-P32-FEAT-0019` in the supplied *KFM Domains v1.1 + Pass 23/Pass 32 Consolidated Atlas* proposes source citation blocks, DOI labels, KFM republication notes, and PROV linkage for derived or republished material. The connected Drive atlas/seed-card corpus corroborates evidence and provenance traceability but does not establish repository implementation.

## Current repository reconciliation

At inspected `main@149af17075f7f12d716aa14de439ea22ee6a343e`:

- the Evidence Drawer already establishes inspectable evidence references and finite no-leak states;
- evidence and provenance contracts remain the authority for evidence membership and lineage;
- UI doctrine forbids treating display signals as proof; and
- open pull requests `#2438` through `#2443`, plus draft `#2446`, do not implement a grouped citation/DOI/republication panel.

No new evidence, provenance, rights, policy, receipt, review, release, or proof object is justified. The bounded gap is an app-local public-safe projection and link-only reader panel.

## Implemented boundary

Only `ANSWER / CITATIONS_AVAILABLE` carries one to twelve exact citation entries, a PROV activity reference, a fixed republication-note code, and a release-manifest reference. DOI values must close exactly over their `https://doi.org/` URLs. Negative outcomes carry no source-controlled text, links, DOI values, or references. Unknown fields, duplicate IDs, unsafe URLs, IP/localhost targets, fragments, credentials, excessive arrays, and incomplete positive closure fail closed.

The component does not fetch sources, resolve evidence, query a provenance graph, infer license or rights, execute policy, authenticate review, authorize release, deploy, publish, or persist state.

## Directory Rules basis

UI implementation remains under `apps/`; synthetic projections remain under `fixtures/ui/`; tests remain in the Explorer harness; this reconciliation remains under `docs/intake/exploratory/`; authoring accountability remains under `data/receipts/generated/`. Existing evidence/provenance authorities are referenced rather than copied.

## Validation and rollback

Validation is the Explorer unit suite, production typecheck/build, isolated browser-fixture typecheck, hosted Playwright coverage, and generated-receipt byte binding. Rollback is a focused revert of this additive packet; it has no data, evidence, provenance, rights, policy, review, release, deployment, or publication effect.
