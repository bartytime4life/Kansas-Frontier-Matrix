<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/briefing-signal
title: BriefingSignal Contract
type: semantic-contract
version: v0.3.0
status: proposed; deterministic-identity-dedup-materiality-routing-profile; non-authoritative
owners: OWNER_TBD — Governance steward · Architecture steward · Source/evidence steward · Validation steward
created: 2026-07-29
updated: 2026-08-04
policy_label: internal-control-plane; no-public-authority; no-repository-mutation; no-source-activation; no-release
related:
  - ../../schemas/contracts/v1/governance/briefing_signal.schema.json
  - ../../fixtures/contracts/v1/governance/briefing_signal/README.md
  - ../../tools/validators/governance/validate_briefing_signal.py
  - ../../tools/validators/governance/deduplicate_briefing_signals.py
  - ../../tools/validators/governance/route_briefing_signals.py
  - ../../tests/governance/test_briefing_signal.py
  - ../../tests/governance/test_briefing_signal_dedup.py
  - ../../tests/governance/test_briefing_signal_materiality.py
  - ../../docs/architecture/briefing-integration.md
  - ../../.github/workflows/briefing-integration.yml
tags: [kfm, governance, briefing, discovery, identity, deduplication, materiality, idempotency, routing, no-network]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BriefingSignal Contract

> A `BriefingSignal` is a non-authoritative, time-bounded discovery and routing record derived from a KFM briefing. It identifies one daily signal revision, groups repeated coverage into one durable event cluster, computes an explainable materiality class, and proposes a finite issue-routing action without creating evidence, repository authority, source admission, policy, review, proof, release, deployment, publication, or public truth.

## Status and authority

| Concern | Posture |
|---|---|
| Object meaning | **PROPOSED** semantic contract |
| Machine profile | `schemas/contracts/v1/governance/briefing_signal.schema.json`, version `1.2.0` |
| Identity algorithm | `kfm-briefing-identity-v1` |
| Materiality algorithm | `kfm-briefing-materiality-v1` |
| Threshold profile | `kfm-briefing-thresholds-v1` — **PROPOSED**, deterministic initial calibration |
| Routing algorithm | `kfm-briefing-routing-v1` |
| Execution posture | deterministic; file-backed; no network; dry-run issue operations only |
| Public use | always `false` |
| Repository mutation | always `false` in the signal and both dry-run tools |
| Source/evidence/policy/release authority | none |

The contract remains deliberately weaker than `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, `PromotionDecision`, and `ReleaseManifest`.

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

- deterministic daily `signal_id`, durable `event_cluster_id`, and full `signal_digest`;
- signal lifecycle state independent from real-world and KFM lifecycle state;
- normalized authority, source-native, geography, and durable-subject identity inputs;
- deduplication state, matches, and finite reason codes;
- ten explicit materiality dimensions, a reproducible raw score, a finite priority, finite reasons, and an optional mandatory override;
- bounded routing context, a finite proposed disposition, and an idempotency key;
- atomic claim candidates with truth labels and evidence references;
- official-source candidates that remain locators rather than admitted sources;
- bounded geography references without guessed inline coordinates;
- existing KFM issue, pull request, path, and object references;
- proposed object families, which remain modeling hypotheses;
- all consequential permissions fixed to `false`;
- a generation-receipt reference; and
- an expiry or re-verification deadline.

## Deterministic identity

### Daily signal identity

`signal_digest` is SHA-256 over canonical JSON containing the briefing date and substantive discovery content: headline, story type, sorted domains, bounded geography, claims and evidence references, source locator identity, proposed object families, and candidate payload.

Operational or decision-like fields are excluded: lifecycle status, materiality, routing, deduplication result, existing links, next action, permissions, public-use flag, generation receipt, expiry, and derived identity fields.

```text
signal_id = "kfm:briefing-signal:" + briefing_date + ":" + first_24_hex(signal_digest)
```

This separation means materiality recalibration or routing refinement does not rewrite the identity of the discovered content.

### Durable event cluster identity

```text
event_cluster_id = sha256(
  story_type
  | primary_authority_id
  | native_id_or_identity_key
  | geography_identity
  | durable_subject_key
)
```

The briefing date and headline are deliberately excluded. Reworded coverage may produce a new daily signal while remaining in the same event cluster.

### Issue-operation idempotency

The `next_action.idempotency_key` binds the event cluster, disposition, normalized scope, existing issue IDs, and matched issue IDs. It is an identity for a proposed operation, not permission to execute it.

## Explainable materiality

Materiality is a transparent prioritization aid. It is not evidence, policy, repository authorization, review approval, or issue-writing authority.

### Dimensions

Every dimension is an integer from `0` through `5`:

| Dimension | Interpretation |
|---|---|
| `public_safety` | Potential immediate harm or safety consequence. |
| `repository_integrity` | Impact on repository control, trust, or protected state. |
| `geospatial_relevance` | Value of explicit spatial representation or comparison. |
| `recurrence` | Likelihood that the same pattern will recur. |
| `reuse_value` | Reuse across sources, domains, or future capabilities. |
| `authority_quality` | Quality of the candidate issuing or observing authority. |
| `time_sensitivity` | Cost of delayed verification or modeling. |
| `rights_sensitivity_risk` | Rights, privacy, sovereignty, or harmful-precision risk. |
| `identity_uncertainty` | Uncertainty in native identity, event identity, or scope. |
| `implementation_readiness` | Readiness for a bounded fixture-first implementation. |

### Raw-score formula

```text
raw_score =
    3 * public_safety
  + 3 * repository_integrity
  + 2 * time_sensitivity
  + 2 * recurrence
  + 2 * reuse_value
  + 2 * geospatial_relevance
  +     authority_quality
  +     implementation_readiness
  - 2 * rights_sensitivity_risk
  - 2 * identity_uncertainty
```

The raw range is `-20..80`.

### Initial threshold profile

| Priority | Rule | Routing meaning |
|---|---:|---|
| `P0` | raw score `>= 55`, or a mandatory override | Immediate safety or repository-integrity review. No automatic correction, merge, release, or publication. |
| `P1` | `35..54` | High-reuse, recurring, statewide, or high-value capability candidate. |
| `P2` | `20..34` | Planning, governance, source, or modeling value that is not urgent. |
| `P3` | `1..19` | Useful context lacking stronger readiness or materiality. |
| `IGNORE` | `<= 0` | Duplicate, unsupported, out-of-scope, risk-heavy, or low-materiality candidate. |

These thresholds are a versioned **PROPOSED** calibration. Changing them requires a profile version, fixture migration, exact boundary tests, documentation, and a generated receipt. A monthly governance review may recommend a successor profile; it cannot silently change historical records.

### Mandatory overrides

The finite override reasons are:

- `ACTIVE_PUBLIC_SAFETY_CONFLICT`;
- `UNEXPECTED_REPOSITORY_MERGE`;
- `PUBLIC_INTERNAL_STORE_BYPASS`.

An applied override forces `P0` while preserving the raw score. The validator checks only bounded internal consistency—for example, repository-integrity overrides require a nonzero `repository_integrity` dimension. It does **not** prove that the underlying incident occurred.

### Reason codes

Every nonzero dimension produces its corresponding finite reason code. The applied override reason is also included. A record with no nonzero dimensions and no override uses `LOW_MATERIALITY`. The validator requires the exact deterministic order and set; free-form rationale cannot replace machine reasons.

## Deterministic issue routing

Routing consumes declared deduplication, materiality, support, readiness, dependency, safety, and issue-kind context. It emits a proposed operation only.

### Finite dispositions

- `UPDATE_EXISTING_ISSUE`
- `OPEN_SOURCE_DISCOVERY_ISSUE`
- `OPEN_OBJECT_MODEL_ISSUE`
- `OPEN_CORRECTIVE_ISSUE`
- `HOLD_FOR_DEPENDENCY`
- `REJECT_UNSAFE`
- `NO_ACTION`
- `ERROR`

`ERROR` is reserved for an evaluator failure or an explicitly recorded failed routing attempt; a valid normal signal will not select it through `kfm-briefing-routing-v1`.

### Routing precedence

```text
1. DUPLICATE with matched issue -> UPDATE_EXISTING_ISSUE
2. DUPLICATE without matched issue -> NO_ACTION
3. safety_state == UNSAFE -> REJECT_UNSAFE
4. dependency_state == BLOCKED -> HOLD_FOR_DEPENDENCY
5. P0 + corrective + official support resolved -> OPEN_CORRECTIVE_ISSUE
6. P0/P1 + modeling ready + source-discovery kind -> OPEN_SOURCE_DISCOVERY_ISSUE
7. P0/P1 + modeling ready + object-model kind -> OPEN_OBJECT_MODEL_ISSUE
8. otherwise -> NO_ACTION with an exact reason
```

The validator recomputes the disposition and reason codes. Duplicate signals remain schema-limited to `UPDATE_EXISTING_ISSUE` or `NO_ACTION`.

### Routing reasons

Finite reasons distinguish an existing issue match, duplicate cluster without an issue, unsafe posture, blocked dependency, corrective readiness, source-discovery readiness, object-model readiness, unresolved official support, modeling not ready, no routable issue kind, and low-priority no action.

## Anti-collapse rules

| Never collapse | Required distinction |
|---|---|
| Briefing story→ evidence | Narrative creates a verification target; immutable source snapshots and evidence objects support claims. |
| Priority → truth | A high score changes review order, not factual authority. |
| Priority → permission | `P0` does not authorize issue mutation, merge, policy, release, or publication. |
| Routing dry run → GitHub mutation | The dry run reports an idempotent proposal and always emits `repository_mutation_allowed=false`. |
| Announced meeting → held meeting | Schedule facts may be confirmed while occurrence and outcomes remain unresolved. |
| Link presence → approval | An official index link does not prove submission acceptance, review, approval, implementation, or outcome. |
| Missing link → nonexistence | Missing material becomes `UNKNOWN` or `NEEDS_VERIFICATION`. |
| Venue → regional scope | Venue and planning-region geographies remain separate. |
| Schema pass → public use | Shape and deterministic consistency never supply evidence, policy, review, release, or publication authority. |

## Validation boundary

The validator and dry-run tools prove only bounded local behavior:

- closed Draft 2020-12 shape;
- bounded, duplicate-key-safe, non-finite-safe parsing;
- deterministic identity, deduplication, scoring, reasons, routing, and idempotency;
- exact structural and semantic-negative fixture outcomes;
- no inline geometry, secret-like fields, or false trust-bearing permissions;
- value-minimized output; and
- no network access.

They do not authenticate source bytes, establish event truth, classify actual urgency, prove rights or sensitivity, verify repository authority, write issues, evaluate policy, construct proof, release, deploy, or publish.

## Correction and rollback

Before merge, close the draft pull request and delete its feature branch. After merge, use a reviewed revert or corrective pull request. A later threshold profile preserves the prior profile identifier and historical score; it does not silently rewrite old decisions. No external or public state is created by this profile.

[Back to top](#top)
