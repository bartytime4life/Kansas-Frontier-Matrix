<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/watchers/watcher-gate-packet
title: Watcher Gate Packet
type: semantic-contract
version: v0.1.0
status: draft; PROPOSED_INACTIVE; fixture-first; no-network; no-release-authority
owners: OWNER_TBD — Watcher steward · Source steward · Policy steward · Validation steward · Release steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; watchers; deterministic-routing; synthetic; no-network; review-candidate-only
related:
  - ../../schemas/contracts/v1/watchers/watcher_gate_profile.schema.json
  - ../../schemas/contracts/v1/watchers/watcher_gate_packet.schema.json
  - ../../pipeline_specs/watchers/watcher_gate_profile.v1.json
  - ../../fixtures/contracts/v1/watchers/watcher_gate_packet/
  - ../../tools/validators/watchers/validate_watcher_gate_packet.py
  - ../../tests/validators/watchers/test_validate_watcher_gate_packet.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "Derived from the watcher-to-policy-to-decision lane in New Ideas 5-19-26, pages 14-17."
  - "GREEN, AMBER, and DENY are deterministic routing outcomes, not policy approval, promotion, release, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Watcher Gate Packet

> Normalize a watcher prefilter, score, artifact references, finite routing
> decision, exit code, and stewardship obligations into one deterministic,
> fixture-only packet without making the watcher a publisher.

## Goal

The source packet proposes a small watcher lane that emits separate prefilter,
feature-vector, scorecard, policy-report, and run-receipt artifacts; computes a
canonical SHA-256; and returns `GREEN`, `AMBER`, or `DENY`. This contract adopts
only the reusable **routing packet** and fixture threshold profile. It does not
adopt any live endpoint, source, dataset, network probe, or publication action.

## Directory Rules basis

| Responsibility | Home | Artifact |
|---|---|---|
| Shared watcher meaning | `contracts/watchers/` | This semantic contract |
| Machine shape | `schemas/contracts/v1/watchers/` | Profile and packet schemas |
| Inactive declarative thresholds | `pipeline_specs/watchers/` | Versioned profile instance |
| Synthetic examples | `fixtures/contracts/v1/watchers/` | Exact positive and negative fixtures |
| Reusable validation | `tools/validators/watchers/` | Deterministic validator |
| Enforceability proof | `tests/validators/watchers/` | Focused no-network tests |
| CI orchestration | `.github/workflows/` | Read-only workflow |

The slice creates no new root and no parallel source, policy, receipt, proof,
release, or publication authority.

## Profile and packet boundary

The inactive profile fixes one reviewed fixture vocabulary:

- score `>= 80` is eligible for `GREEN` when no hard deny or amber condition exists;
- score `< 50` is `DENY`;
- a median cloud value above `40%`, zero discovered items, or any missing asset is `DENY`;
- a score from `50` through `79`, or a missing ETag, is `AMBER`;
- `GREEN` and `AMBER` use process exit code `0`; `DENY` uses exit code `2`.

The packet carries references to the five source-derived artifact families. It
does not embed their contents and does not collapse them into one mega-receipt.

## Finite behavior

| Deterministic result | Required process behavior | Meaning |
|---|---:|---|
| `GREEN` | exit `0`; no obligations | Reviewed fixture conditions are satisfied. |
| `AMBER` | exit `0`; `ROUTE_STEWARD_REVIEW` | Continue the pipeline only as a held human-review candidate. |
| `DENY` | exit `2`; block and route review | Fail closed; the candidate is non-promotable. |

Multiple hard-deny facts produce one `DENY` packet with every applicable stable
reason code. Reason codes and obligations are sorted and duplicate-free so the
packet is replayable.

## Trust boundary and non-effects

This slice:

- performs no network requests and activates no source;
- does not implement OPA/Conftest or claim an adopted policy decision;
- does not write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED;
- does not resolve `EvidenceRef` or create `EvidenceBundle` support;
- does not create a `PromotionDecision`, `ReleaseManifest`, issue, notification,
  map layer, or public claim;
- keeps every governance flag false and `release_ref` null.

`AMBER` is a stewardship route, not a soft allow. `GREEN` is a deterministic
fixture outcome, not publication authority.

## Validation

```bash
python -m pytest -q -p no:cacheprovider \
  tests/validators/watchers/test_validate_watcher_gate_packet.py

python tools/validators/watchers/validate_watcher_gate_packet.py --fixtures
```

A green result proves only schema shape, profile integrity, deterministic
classification, fixture polarity, canonical ordering, and no-network replay.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an
authorized merge, revert the additive feature commit. No live source, lifecycle
record, external notification, release, deployment, or published artifact needs
restoration.

<p align="right"><a href="#top">Back to top</a></p>
