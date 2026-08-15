<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture-governed-api
title: Governed API — Architecture
type: standard
version: v2
status: draft
owners: API steward + Security steward (TODO confirm)
created: 2026-05-14
updated: 2026-08-14
policy_label: public
owning_root: docs/
responsibility: "Explain the governed API architecture boundary and verified current scaffold state without creating contract, policy, release, deployment, or publication authority."
truth_posture: cite-or-abstain
related:
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/authority-ladder.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/README.md
  - contracts/runtime/runtime_response_envelope.md
  - schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - apps/governed-api/README.md
  - apps/governed-api/src/governed_api/stub.py
  - apps/governed-api/src/governed_api/routes/
  - apps/governed-api/tests/test_abstain_routes.py
  - packages/evidence-resolver/README.md
  - .github/workflows/api-test.yml
tags: [kfm, architecture, governed-api, trust-membrane, runtime-response-envelope, finite-outcomes]
notes:
  - "v2 reconciles the architecture guide with current repository evidence through main@3ea2ab5701074168b0dab32e94dccae8dbcc0d4f."
  - "Current executable behavior remains a fail-closed scaffold: three GET routes emit schema-aligned ABSTAIN / NOT_IMPLEMENTED RuntimeResponseEnvelope shapes."
  - "No ANSWER path, evidence lookup, policy evaluation, release binding, production deployment, or public publication authority is claimed."
[/KFM_META_BLOCK_V2] -->

# Governed API — Architecture

> The governed API is KFM's public trust membrane. Current repository evidence proves only a bounded fail-closed scaffold, not a complete public service.

## 1. Authority and current-state posture

The doctrinal boundary is stable: ordinary public clients must use governed interfaces rather than canonical stores, lifecycle internals, model runtimes, graph/vector stores, or unpublished candidates.

Current implementation claims in this document are limited to repository evidence inspected at `main@3ea2ab5701074168b0dab32e94dccae8dbcc0d4f`.

### CONFIRMED current implementation

The repository currently contains:

- `apps/governed-api/` as the deployable application responsibility root;
- a standard-library WSGI entry point in `apps/governed-api/src/governed_api/main.py`;
- three registered GET scaffold routes under `apps/governed-api/src/governed_api/routes/`:
  - `/bootstrap`;
  - `/layers`;
  - `/evidence`;
- `apps/governed-api/src/governed_api/stub.py`, which emits a `RuntimeResponseEnvelope`-shaped negative result;
- `contracts/runtime/runtime_response_envelope.md` and `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json` as the semantic/machine-shape family consumed by that scaffold;
- focused governed-api tests, including `apps/governed-api/tests/test_abstain_routes.py`;
- `.github/workflows/api-test.yml` as the repository-native CI surface for the app; and
- a separate internal `packages/evidence-resolver/` candidate implementation that is not yet a public governed-api answer path.

The scaffold response contains the ten unconditional runtime-envelope fields required by the current schema:

```text
id
spec_hash
version
issued_at
outcome
reason_code
evidence_refs
policy_state
freshness
correction_state
```

For the three existing scaffold routes, the current finite outcome is:

```text
outcome     = ABSTAIN
reason_code = NOT_IMPLEMENTED
evidence_refs = []
```

That is intentionally non-substantive and fail-closed.

### UNKNOWN / not established by current evidence

This document does not claim that the repository currently has:

- a production deployment of the governed API;
- authenticated public or partner traffic;
- an `ANSWER` route;
- live EvidenceRef-to-EvidenceBundle lookup from the API;
- policy, rights, sensitivity, role, or release evaluation in the scaffold routes;
- correction/rollback resolution in runtime requests;
- governed AI/model execution through this app;
- a live layer catalog backed by released artifacts;
- public telemetry ingestion;
- review/correction/export route implementations; or
- operational logs, dashboards, SLOs, or production runbooks proving live service maturity.

Those remain **NEEDS VERIFICATION** or future implementation work.

## 2. Trust-membrane invariants

The following remain the governing architecture rules:

1. **Public clients use governed interfaces.** They do not read `RAW`, `WORK`, `QUARANTINE`, unpublished candidates, canonical stores, or provider runtimes directly.
2. **Finite outcomes only.** Public trust-bearing responses use `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` rather than silent partial success.
3. **Cite-or-abstain.** Claim-bearing `ANSWER` behavior requires resolvable evidence support; missing or insufficient support yields `ABSTAIN`.
4. **Policy before exposure.** Rights, sensitivity, access, review, freshness, and release state must be evaluated before substantive disclosure.
5. **EvidenceBundle outranks generated language.** AI or other generated output is interpretive and never becomes root truth.
6. **Promotion remains separate.** The API may reflect release state but cannot create publication authority by serving a response.
7. **No direct runtime shortcut.** Browser or map clients do not call model/provider adapters directly.
8. **Safe failure.** Errors and denials do not expose internal paths, secrets, raw evidence, restricted coordinates, or adapter internals.
9. **Receipts are not proofs.** Process provenance does not substitute for evidence, review, policy, release, or publication authority.

## 3. Current request path

The implemented scaffold is intentionally narrow:

```text
GET /bootstrap | /layers | /evidence
        |
        v
route registry
        |
        v
make_abstain_envelope(...)
        |
        v
RuntimeResponseEnvelope-shaped
ABSTAIN / NOT_IMPLEMENTED
```

No evidence resolver, policy runtime, release lookup, provider adapter, or canonical store is called by this scaffold path.

That negative behavior is useful: it demonstrates the client-facing envelope family without fabricating implementation maturity.

## 4. RuntimeResponseEnvelope boundary

The current schema defines exactly four top-level outcomes:

| Outcome | Architecture meaning |
|---|---|
| `ANSWER` | A substantive response may be emitted only after the required evidence, policy, precision, release, review, freshness, and correction obligations close. |
| `ABSTAIN` | The system cannot support a substantive answer at the required trust level. |
| `DENY` | Policy, rights, sensitivity, role, exposure, or release posture forbids disclosure. |
| `ERROR` | Contract, validation, adapter, or infrastructure failure prevents a reliable response. |

The schema currently requires `precision_actually_used` only for `ANSWER`, and requires at least one evidence reference for that outcome. Negative outcomes must not carry `precision_actually_used`.

The present scaffold therefore correctly omits precision and evidence references while returning `ABSTAIN`.

## 5. Evidence resolver relationship

`packages/evidence-resolver/` is a separate reusable internal lane. Its implemented profile is explicitly non-authoritative and non-deployable. It evaluates caller-supplied candidate objects without network/store access and returns candidate statuses that must not be confused with public runtime authority.

Its runtime projection deliberately maps:

```text
RESOLVED   -> CONTINUE_GOVERNED_CHECKS
UNRESOLVED -> ABSTAIN
DENIED     -> DENY
ERROR      -> ERROR
```

A resolver `RESOLVED` candidate is **not** a public `ANSWER`. Remaining governed checks include evidence authority, rights, sensitivity, policy, review, release, citation, and correction.

Accordingly, wiring the resolver directly to `/evidence` as an `ANSWER` shortcut would violate the current package boundary and KFM doctrine.

## 6. Directory Rules basis

Accepted ADR-0029 adopts `docs/doctrine/directory-rules.md` as the directory-governance authority.

The current placement follows those responsibility boundaries:

| Concern | Owning root |
|---|---|
| deployable governed API | `apps/governed-api/` |
| reusable evidence-resolution implementation | `packages/evidence-resolver/` |
| runtime object semantics | `contracts/runtime/` |
| machine-readable runtime shape | `schemas/contracts/v1/runtime/` |
| admissibility rules | `policy/` |
| provider/runtime adapters | `runtime/` |
| evidence/proof and lifecycle artifacts | `data/` |
| release/correction/rollback authority | `release/` |
| repository-native validation | `tests/`, `tools/`, `.github/workflows/` |

No public client should bypass `apps/governed-api/` to consume one of those internal roots directly.

## 7. Next dependency-closed implementation stages

The next implementation work should remain small and separately reviewable. Current evidence supports this ordering:

1. **Negative-outcome expansion.** Add deterministic `DENY` and `ERROR` scaffold cases only when a current contract/fixture/acceptance boundary clearly owns those inputs and outcomes.
2. **Evidence-route candidate integration.** Introduce a request contract and fixture-only governed-api adapter to the evidence-resolver candidate lane, preserving `RESOLVED -> CONTINUE_GOVERNED_CHECKS` rather than promoting it to `ANSWER`.
3. **Policy/runtime gate integration.** Add an explicit caller-supplied or fixture-backed policy decision boundary before substantive output.
4. **Release/correction binding.** Require release/correction state where the payload depends on released artifacts.
5. **First `ANSWER` vertical slice.** Only after evidence, policy, citation, release, review, precision, freshness, correction, and rollback obligations have objective fixtures and tests.
6. **Public UI transport.** Connect Explorer or other clients only after the governed-api route is demonstrably safe and release-backed.

Each stage must preserve deny-by-default behavior and must not activate sources, publish data, or widen access implicitly.

## 8. Explicit non-goals of the current scaffold

The current implementation does not authorize:

- live source activation;
- direct public lifecycle-store reads;
- EvidenceBundle construction from unreviewed inputs;
- AI or model-generated public answers;
- policy bypass;
- release creation or promotion;
- publication;
- repository mutation;
- admin shortcuts as ordinary public paths; or
- exposure of sensitive or rights-unclear material.

## 9. Validation expectations

For current scaffold changes, the minimum focused validation set is:

```bash
python -m pytest apps/governed-api/tests/test_abstain_routes.py -q --strict-config --strict-markers
make governed-api-smoke
```

Relevant repository-wide ratchets should then be compared with untouched current main so inherited failures are not attributed to the branch.

For any future substantive `ANSWER` path, focused validation must also prove evidence resolution, citation closure, policy decisions, release state, precision, correction/rollback handling, negative cases, and public-boundary non-leakage.

## 10. Rollback

A governed-api change should remain independently reversible. Before merge, close the draft PR. After merge, revert the specific change through the normal reviewed repository path. No API-plane code change alone may rewrite or bypass source, lifecycle, policy, evidence, review, or release history.

---

**Truth summary:** the trust-membrane doctrine is CONFIRMED; three schema-aligned `ABSTAIN / NOT_IMPLEMENTED` GET scaffold routes are CONFIRMED; the evidence-resolver candidate package is CONFIRMED internal/non-authoritative; substantive public answer behavior remains **NEEDS VERIFICATION / not implemented by the inspected scaffold**.
