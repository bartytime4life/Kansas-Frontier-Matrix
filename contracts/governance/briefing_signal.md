<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/briefing-signal
title: BriefingSignal Contract
type: semantic-contract
version: v0.2.0
status: proposed; deterministic-identity-and-dedup-profile; non-authoritative
owners: OWNER_TBD — Governance steward · Architecture steward · Source/evidence steward · Validation steward
created: 2026-07-29
updated: 2026-08-03
policy_label: internal-control-plane; no-public-authority; no-repository-mutation; no-source-activation; no-release
related:
  - ../../schemas/contracts/v1/governance/briefing_signal.schema.json
  - ../../fixtures/contracts/v1/governance/briefing_signal/README.md
  - ../../tools/validators/governance/validate_briefing_signal.py
  - ../../tools/validators/governance/deduplicate_briefing_signals.py
  - ../../tests/governance/test_briefing_signal.py
  - ../../tests/governance/test_briefing_signal_dedup.py
  - ../../docs/architecture/briefing-integration.md
  - ../../.github/workflows/briefing-integration.yml
tags: [kfm, governance, briefing, discovery, identity, deduplication, idempotency, routing, no-network]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BriefingSignal Contract

> A `BriefingSignal` is a non-authoritative, time-bounded discovery and routing record derived from a human-readable KFM briefing. It identifies one daily signal revision, associates repeated coverage with one durable event cluster, and proposes a finite issue-routing action without creating evidence, repository authority, source admission, policy, review, proof, release, deployment, publication, or public truth.

## Status and authority

| Concern | Posture |
|---|---|
| Object meaning | **PROPOSED** semantic contract |
| Machine profile | `schemas/contracts/v1/governance/briefing_signal.schema.json`, version `1.1.0` |
| Identity algorithm | `kfm-briefing-identity-v1` |
| Execution posture | deterministic; file-backed; no network; dry-run routing only |
| Public use | always `false` |
| Repository mutation | always `false` in the signal and dedup dry run |
| Source/evidence/release authority | none |

The contract is deliberately weaker than `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, `PromotionDecision`, and `ReleaseManifest`.

## Directory Rules basis

The accepted Directory Governance Standard routes each artifact by one owning responsibility:

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/governance/briefing_signal.md` |
| Machine shape | `schemas/contracts/v1/governance/briefing_signal.schema.json` |
| Synthetic examples | `fixtures/contracts/v1/governance/briefing_signal/` |
| Repository-wide validation and dry-run tooling | `tools/validators/governance/` |
| Enforceability proof | `tests/governance/` |
| Human architecture explanation | `docs/architecture/briefing-integration.md` |
| CI orchestration | existing `.github/workflows/briefing-integration.yml` |
| Generated process provenance | `data/receipts/generated/` |

No new root, runtime store, source registry, evidence store, policy family, release family, or public carrier is created.

## Semantic shape

A signal contains:

- `schema_version` and monotonic `signal_version`;
- deterministic `signal_id` for one daily signal revision;
- deterministic `event_cluster_id` for the durable event across briefings;
- `briefing_date`, signal lifecycle `status`, orientation `headline`, `story_type`, and domain labels;
- explicit identity inputs and a reproducible `signal_digest`;
- deduplication status, prior signal/issue matches, and finite reason codes;
- explainable materiality dimensions and priority;
- bounded geography identity or an explicit unresolved state;
- atomic claim candidates with truth labels and evidence references;
- official-source candidates that remain locators, not source admission;
- existing KFM issues, pull requests, paths, and object references;
- proposed object families, which remain modeling hypotheses;
- one finite next action with a deterministic issue idempotency key;
- all consequential permissions fixed to `false`;
- a generation-receipt reference;
- optional non-authoritative candidate payload without inline geometry or secrets; and
- an expiry or re-verification deadline.

## Deterministic identity

### Daily signal identity

`signal_digest` is SHA-256 over canonical JSON containing the briefing date and substantive discovery content:

- normalized headline;
- story type;
- sorted domains;
- bounded geographic scope;
- sorted atomic claims and evidence references;
- source kind, authority name, and locator, excluding retrieval-time state;
- sorted proposed object families; and
- normalized candidate payload.

Operational and authority-like fields are excluded: lifecycle status, materiality, deduplication result, existing links, next action, permissions, public-use flag, generation receipt, expiry, and the derived identity fields themselves.

```text
signal_id = "kfm:briefing-signal:" + briefing_date + ":" + first_24_hex(signal_digest)
```

Equivalent object-key order and unordered-list order reproduce the same digest. A substantive headline or claim change creates a new daily signal revision.

### Durable event cluster identity

The event cluster deliberately excludes the briefing date and headline:

```text
event_cluster_id = sha256(
  story_type
  | primary_authority_id
  | native_id_or_identity_key
  | geography_identity
  | durable_subject_key
)
```

The four identity tokens are Unicode-normalized, case-folded, whitespace-collapsed, and stored in normalized lowercase token form. A revised headline may change `signal_id` while preserving `event_cluster_id`.

### Issue-routing idempotency

The next-action idempotency key binds:

- event cluster;
- finite disposition;
- normalized scope;
- existing issue IDs; and
- deduplication-matched issue IDs.

Retries therefore reproduce the same proposed operation rather than opening parallel work.

## Deduplication states

| State | Meaning | Allowed routing posture |
|---|---|---|
| `UNRESOLVED` | Match evidence is not strong enough. | Hold or bounded issue proposal after review. |
| `UNIQUE` | No prior signal, object, or issue match was found. | A bounded new issue may be proposed; mutation remains false. |
| `DUPLICATE` | An existing event cluster, signal, object, or issue owns the work. | `UPDATE_EXISTING_ISSUE` or `NO_ACTION`; opening a second issue is invalid. |
| `CONFLICTED` | Identity or official-source evidence conflicts. | Preserve a conflict cluster; do not merge by headline alone. |

Exact source-native identifiers and explicit KFM links outrank headline similarity. Fuzzy text is never sufficient without compatible authority, identity, geography, and event type.

## Required invariants

1. A signal never becomes evidence merely because its claims are schema-valid.
2. A `CONFIRMED` claim has at least one evidence reference.
3. All identity inputs are normalized and all declared hashes/IDs reproduce.
4. `DUPLICATE` requires a prior signal or issue match and cannot propose opening a new issue.
5. `UPDATE_EXISTING_ISSUE` requires a matched issue already present in `existing_kfm_links.issues`.
6. A signal cannot match itself.
7. Public use, repository mutation, source activation, proof, release, deployment, and publication remain false.
8. Candidate payloads contain no inline coordinates, secret-like fields, or true trust-bearing states.
9. Expiry cannot precede the briefing date.
10. Validation and clustering perform no network or external write.

## Finite findings

The bounded validators emit sorted `{code, path}` findings without echoing claim text, source content, credentials, or candidate values. Identity and routing findings include:

- `IDENTITY_TOKEN_NOT_NORMALIZED`
- `SIGNAL_DIGEST_MISMATCH`
- `SIGNAL_ID_MISMATCH`
- `EVENT_CLUSTER_ID_MISMATCH`
- `ISSUE_IDEMPOTENCY_KEY_MISMATCH`
- `DUPLICATE_MATCH_REQUIRED`
- `DUPLICATE_CANNOT_OPEN_ISSUE`
- `MATCHED_ISSUE_NOT_LINKED`
- `UPDATE_ISSUE_TARGET_REQUIRED`
- `SELF_DUPLICATE_REFERENCE_FORBIDDEN`
- `SIGNAL_DEDUP_STATUS_MISMATCH`
- `SIGNAL_EXPIRY_PRECEDES_BRIEFING`
- `INLINE_GEOMETRY_FORBIDDEN`
- `SECRET_LIKE_FIELD_FORBIDDEN`

The multi-file dry run additionally reports collision, replay, primary-reference, and duplicate-classification findings. It emits `authority_created=false` and `repository_mutation_allowed=false`.

## Compatibility and migration

Version `1.1.0` replaces the ordinal `kfm-briefing-YYYY-MM-DD-NNN` fixture identity with content-derived IDs and adds required cluster, identity, deduplication, issue-idempotency, pull-request-link, and generation-receipt fields. Current repository fixtures and examples are migrated atomically in this slice.

This is a breaking change to a **PROPOSED, non-public fixture profile**. No released artifact or public route is migrated. Any external consumer is **UNKNOWN / NEEDS VERIFICATION** and must adopt the `1.1.0` profile deliberately.

## Validation

```bash
PYTHONPATH=. KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 \
  python -m unittest discover \
  --start-directory tests/governance \
  --pattern 'test_briefing_signal*.py' \
  --verbose

python tools/validators/governance/validate_briefing_signal.py \
  fixtures/contracts/v1/governance/briefing_signal/valid/*.json \
  examples/briefing_integration/*.json

python tools/validators/governance/deduplicate_briefing_signals.py \
  fixtures/contracts/v1/governance/briefing_signal/valid/*.json
```

Passing proves only the declared profile, identity, deduplication, routing, parser, deterministic-output, and no-network behavior.

## Non-goals

- no live source retrieval or source activation;
- no GitHub issue write, branch write, pull-request mutation, review, settings change, or merge;
- no lifecycle data, EvidenceBundle, policy decision, proof, release, public route, map layer, search index, graph edge, alert, or AI answer;
- no fuzzy cross-source entity resolution beyond the declared exact cluster inputs;
- no claim that a briefing signal represents current real-world status.

## Rollback

Before merge, close the draft pull request and delete the feature branch. After merge, revert the bounded implementation commit through review. The rollback restores the `1.0.0` fixture profile and removes the dry-run cluster implementation; it does not modify any external event, issue, source, evidence, release, deployment, or published state.

[Back to top](#top)
