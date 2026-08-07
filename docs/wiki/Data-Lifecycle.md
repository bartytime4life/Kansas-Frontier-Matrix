<!--
KFM_WIKI_SOURCE
page_id: Data-Lifecycle
title: Data Lifecycle
status: PROPOSED wiki source; review required
updated: 2026-08-07
authority: orientation-only; canonical repository evidence and adopted KFM authority outrank this page
source_path: docs/wiki/Data-Lifecycle.md
publication_effect: none until separately synchronized to the native GitHub Wiki
-->
# Data Lifecycle

The KFM lifecycle is a governance sequence:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

It answers **what state an artifact is in**, **what controls have run**, and **what transition is allowed next**. It is not merely a folder layout.

## Stages

| Stage | Purpose | Typical controls | Public posture |
|---|---|---|---|
| Pre-RAW | Evaluate a source-edge event before admission | Source identity, rights/sensitivity precheck, event receipt | Internal |
| RAW | Preserve retrieved source bytes or immutable references | Source descriptor, retrieval metadata, digest | Never ordinary public path |
| WORK | Normalize, map, analyze, and inspect candidates | Transform receipts, candidate deltas, validation | Internal |
| QUARANTINE | Hold unresolved, unsafe, malformed, conflicting, or restricted material | Reason codes, review tasks, deny/hold decision | Denied |
| PROCESSED | Store validated domain products | Schema/contract checks, identity, geometry, temporal QA | Not public by default |
| CATALOG / TRIPLETS | Make governed records discoverable and relational | STAC/DCAT/PROV, graph projection, catalog integrity | Downstream only |
| PUBLISHED | Serve reviewed, released public-safe artifacts | Promotion decision, proof, release manifest, correction and rollback | Governed delivery |

QUARANTINE is a valid fail-closed state, not a failure to be hidden. CATALOG and TRIPLETS are derived discovery/projection surfaces, not sovereign truth.

## Accountability lanes

The `data/` responsibility root also contains object families that are not lifecycle stages:

| Lane | Role |
|---|---|
| `registry/` | Source, dataset, layer, identity, rights, and other governed registries |
| `receipts/` | Process memory: what ran, with which inputs, tools, and outcomes |
| `proofs/` | Evidence that a release or validation condition can be independently checked |
| `rollback/` | Data-side rollback support and prior-state references |
| published carriers | Released public-safe files and projections, when the governing release exists |

A producer does not own the output's authority. A pipeline may emit a receipt, proof, catalog record, and public artifact; each belongs in its own family.

## Transition rule

A transition should be explicit, finite, reviewable, and replayable:

```text
current state
  + candidate identity
  + pinned inputs
  + validation results
  + policy decision
  + review state
  + provenance/integrity
  + correction and rollback support
  -> transition outcome
```

Possible outcomes include pass, hold, deny, abstain, and error. A move or copy cannot stand in for this decision.

## Public-client rule

Public and semi-public clients use:

- governed API projections;
- released public-safe artifacts;
- catalog records that point to released material;
- tiles and layer manifests bound to release state;
- EvidenceBundle-derived details;
- finite response envelopes.

They do not use RAW, WORK, QUARANTINE, unpublished candidates, canonical-internal databases, or direct model outputs.

## Watchers and connectors

A watcher may detect source drift and emit a candidate or receipt. A connector may fetch and normalize source material. Neither is a publisher. Live network activation requires current source identity, terms, rights, sensitivity, failure behavior, fixtures, and review.

## Example: safe update

```text
Source change detected
  -> watcher receipt
  -> source snapshot in RAW
  -> normalized candidate in WORK
  -> conflict or rights issue? QUARANTINE
  -> validated product in PROCESSED
  -> catalog/proof closure
  -> reviewed release
  -> public-safe artifact
  -> governed API and map
```

A later correction produces a correction record and updated release lineage rather than erasing the prior state.

## Canonical references

- [Lifecycle Law](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/lifecycle-law.md)
- [Data root](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/data)
- [Release root](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/release)
- [Pipeline root](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/pipelines)
- [Connector root](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/connectors)
- [Generated receipt boundary](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/data/receipts/generated/README.md)
