<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/stac-link-closure-assessment
title: STAC Link-Closure Assessment Contract
type: semantic-contract
version: v0.1.0
status: proposed; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Catalog steward · STAC steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; data; stac; graph-closure; cite-or-abstain
owning_root: contracts/
responsibility: Define deterministic closure checks over a supplied local STAC record graph while keeping record conformance, API behavior, network resolution, availability, policy, release, and publication separate.
truth_posture: PROPOSED contract / CONFIRMED deterministic synthetic implementation / NEEDS VERIFICATION steward approval and operational integration
related:
  - ../../schemas/contracts/v1/data/stac_link_closure_assessment.schema.json
  - ../../fixtures/contracts/v1/data/stac_link_closure_assessment/cases.json
  - ../../tools/validators/catalog/validate_stac_link_closure_assessment.py
  - ../../docs/intake/exploratory/stac-link-closure-assessment-source-map.md
  - ../../docs/standards/STAC.md
tags: [kfm, catalog, stac, local-graph, link-closure]
notes:
  - "PASS proves closure only for the supplied declared graph; it does not prove record shape, remote resolution, API behavior, availability, or publication state."
[/KFM_META_BLOCK_V2] -->

# STAC link-closure assessment

## Status and purpose

`STAC_LINK_CLOSURE_ASSESSMENT_V1` is a **PROPOSED**, fixture-only profile for checking a supplied local graph of STAC Catalog, Collection, and Item projections. It prevents a record-profile result from silently implying graph closure, API conformance, network availability, or release readiness.

Every record carries a reference to a separate record-conformance result. This validator does not replay or upgrade that result. It checks only local identity, target presence, declared target type, reciprocal hierarchy links, and reachability from one declared root.

## Closure rules

- Records and links are unique and lexically ordered.
- The root exists and is declared as a `CATALOG`.
- `root` links target the declared root Catalog.
- `child` links target a Catalog or Collection and reciprocate with `parent`.
- `parent` links target a Catalog or Collection and reciprocate with `child`.
- `item` links originate at a Collection, target an Item, and reciprocate with `collection`.
- `collection` links originate at an Item, target a Collection, and reciprocate with `item`.
- Every target exists with the declared type, and every record is reachable from the root through `child` and `item` links.

## Finite outcomes

| Validator outcome | Assessment outcome | Meaning |
|---|---|---|
| `PASS` | `LINK_GRAPH_CLOSED` | The supplied full graph satisfies the local closure rules. |
| `ABSTAIN` | `PARTIAL_GRAPH` | The supplied graph closes locally but is explicitly only a partial sample. |
| `DENY` | `LINK_GRAPH_OPEN` or validation finding | A target, reciprocal edge, declared type, reachability claim, report, order, shape, or identity is inconsistent. |
| `ERROR` | `ERROR` | The packet declares upstream failure or cannot be safely read. |

## Anti-collapse boundary

A `PASS` does **not** validate STAC record content, extension discipline, asset bytes, query behavior, pagination, remote link resolution, HTTP status, service availability, catalog authority, evidence, policy, review, release, deployment, publication, or public use. Those remain separate governed checks.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the packet excluding `assessment_id` and `spec_hash`.

```text
spec_hash     = SHA-256(JCS(identity subject))
assessment_id = "kfm:stac-link-closure:" + first 24 digest hex characters
```

## Directory Rules basis and rollback

Catalog meaning remains in `contracts/data/`; machine shape in `schemas/contracts/v1/data/`; synthetic cases in `fixtures/contracts/v1/data/`; validation in `tools/validators/catalog/`; tests in `tests/validators/`; CI in `.github/workflows/`; source mapping in `docs/intake/exploratory/`; and process memory in `data/receipts/generated/`. These are existing responsibility roots under accepted ADR-0029.

Rollback is an ordinary revert of this additive packet. No STAC record, remote endpoint, catalog, evidence object, policy decision, release, deployment, or publication state is changed.
