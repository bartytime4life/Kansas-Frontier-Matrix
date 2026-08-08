# Fixture-first Focus composed-claim projection

## Goal

Implement the bounded Explorer Web continuation of **ML-Y-109**: resolved,
qualified, abstained, denied, and errored composed-claim states rendered through
a finite Focus Panel before any live model, source connector, or public route is
admitted.

## Evidence and dependency basis

The shared repository packet
`ComposedClaimDependencyClosureCandidate` already defines required, optional,
alternative, and exclusion dependencies plus the finite closure outcomes
`SUPPORTED`, `QUALIFIED`, `ABSTAIN`, `DENY`, and `ERROR`. This app-local slice
does not redefine that semantic contract. It consumes a deliberately narrower
public-safe projection and maps closure state to the existing Focus vocabulary:

| Dependency closure | Focus outcome | Render posture |
|---|---|---|
| `SUPPORTED` | `ANSWER` | cited, released support |
| `QUALIFIED` | `ANSWER` | cited support plus visible optional-role limitations |
| `ABSTAIN` | `ABSTAIN` | fixed no-leak copy; unresolved role remains visible |
| `DENY` | `DENY` | fixed no-leak copy; protected detail is not reflected |
| `ERROR` | `ERROR` | fixed no-leak operational copy |

## Directory Rules basis

The slice remains inside existing responsibility roots:

- app-local request parsing, projection parsing, finite state, accessibility,
  and Evidence Drawer handoff: `apps/explorer-web/src/features/focus_panel/`;
- synthetic UI projections: `fixtures/ui/focus_composed_claim_projection/`;
- unit and browser proof: `apps/explorer-web/tests/`;
- generated AI-authoring accountability: `data/receipts/generated/`.

No schema, contract, policy, source registry, evidence store, proof store,
release home, or publication path is created. The shared evidence contract and
schema remain the semantic and machine-shape authorities for dependency
closure.

## Browser trust boundary

The feature:

- strictly validates a bounded question, request identity, claim identity, and
  allowlisted EvidenceRefs;
- injects the governed resolver instead of performing transport;
- requires response request/claim identity to match the request;
- rejects Focus or Evidence Drawer EvidenceRefs outside request scope;
- requires every answer EvidenceRef to have exactly one citation and matching
  Evidence Drawer support;
- requires `ANSWER` to be reviewed, released, current, policy-allowed, and bound
  to a safe AIReceipt reference;
- sanitizes all negative Evidence Drawer inputs before retaining browser state;
- renders AIReceipt references as process memory, never release proof;
- exposes no hidden reasoning, provider trace, raw prompt bundle, or protected
  denial reason;
- performs no network, model-runtime, vector-store, graph-store, renderer,
  policy, source, or lifecycle-store access; and
- provides keyboard activation, focus entry, Escape closure, focus restoration,
  non-color outcome labels, and Evidence Drawer handoff.

## Proof scope

A green result proves only strict app-local projection parsing, finite rendering,
request/evidence subset binding, fixed negative copy, accessibility mechanics,
and synthetic Evidence Drawer handoff. It does not prove a governed API route,
model adapter, live evidence resolution, policy execution, human review,
release authorization, deployment, publication, or public use.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an
authorized merge, revert the implementation commit and generated receipt, then
rerun Explorer build, unit, browser, receipt, promotion, and release-dry-run
checks. No live data, cache, source, release, deployment, or publication state is
created by this slice.
