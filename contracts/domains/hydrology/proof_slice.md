<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hydrology-proof-slice
title: Proof Slice Contract — Hydrology (synthetic, no-network)
type: semantic-contract
version: v0.1
status: draft; PROPOSED; synthetic-fixture-only; bounded-executable
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
created: 2026-09-29
updated: 2026-10-08
policy_label: public; semantic-contract; hydrology; proof-slice; synthetic-only; no-release-authority; not-for-life-safety
related:
  - ../../../docs/domains/hydrology/THIN_SLICE.md
  - ../../../docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md
  - ../../../pipelines/domains/hydrology/proof_slice.py
  - ../../../control_plane/readiness/hydrology-proof-slice-profile.json
  - ../../../fixtures/domains/hydrology/proof_slice/
  - ./decision_envelope.md
  - ./evidence_bundle.md
[/KFM_META_BLOCK_V2] -->

# Proof Slice Contract — Hydrology

> [!IMPORTANT]
> **Posture:** `SYNTHETIC_FIXTURE_ONLY`. The slice replays committed synthetic
> fixtures. It reads no real source, admits no source, binds no Rego evaluator,
> emits no `PolicyDecision`, writes no lifecycle state, and approves no release
> or publication. A `PASS` is not a real-source proof under
> [ADR-0009](../../../docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md);
> gates 2–12 of that ADR remain open.

## Meaning

The Hydrology proof slice is the executable form of the
[thin slice](../../../docs/domains/hydrology/THIN_SLICE.md) assertion set. It shows
that one bounded request path reaches a **finite** outcome — `ANSWER`, `ABSTAIN`,
`DENY`, or `ERROR` — for each declared case, that every outcome is a valid
`DecisionEnvelope`, and that the whole run is deterministic without network access.

## Objects

| Object | Schema | Role |
|---|---|---|
| Execution profile | [`proof_slice_profile.schema.json`](../../../schemas/contracts/v1/domains/hydrology/proof_slice_profile.schema.json) | Closed input set: every input path with its SHA-256, the expected outcome and reason code per case, the license allowlist, and a fixed `evaluated_at`. |
| Base request | [`proof_slice_request.schema.json`](../../../schemas/contracts/v1/domains/hydrology/proof_slice_request.schema.json) | The complete synthetic request each case starts from. |
| Case | [`proof_slice_case.schema.json`](../../../schemas/contracts/v1/domains/hydrology/proof_slice_case.schema.json) | Overrides applied to the base request, with the thin-slice assertion number it exercises. |
| Record | [`proof_slice_record.schema.json`](../../../schemas/contracts/v1/domains/hydrology/proof_slice_record.schema.json) | Deterministic output: input manifest, packet validation, one envelope per case, dry-run rollback rehearsal, all-false effects, and a JCS `spec_hash`. |

## Gates

The harness applies these gates in order; the first failing gate decides.

| # | Gate | Failure outcome | Reason code |
|---:|---|---|---|
| 1 | Request arrives through the governed API | `DENY` | `UI_DIRECT_MODEL_CALL_DENIED` |
| 2 | Requested artifact is under `data/published/` and names no RAW/WORK/QUARANTINE/PROCESSED segment | `DENY` | `PUBLIC_RAW_PATH_DENIED` |
| 3 | Policy evaluator is available | `ERROR` | `POLICY_EVALUATOR_UNAVAILABLE` |
| 4 | An EvidenceBundle is supplied | `ABSTAIN` | `MISSING_EVIDENCE_BUNDLE` |
| 5 | The bundle is pinned, schema-valid, its `spec_hash` matches its content, and it binds the packet digest | `ABSTAIN` | `EVIDENCE_CLOSURE_FAILED` |
| 6 | The bundle license is on the profile allowlist | `DENY` | `RIGHTS_UNKNOWN` |
| 7 | Geometry is generalized to HUC12 | `DENY` | `SENSITIVE_EXACT_GEOMETRY` |
| 8 | The feature's source role matches how it is presented (NFHL context is never an observed flood event) | `DENY` | `SOURCE_ROLE_COLLAPSE` |
| 9 | The packet scenario resolves: no results, unavailable, and ambiguous joins are finite non-answers | `ABSTAIN` / `ERROR` | packet reason code |
| 10 | The release candidate names a rollback target | `DENY` | `RELEASE_ROLLBACK_MISSING` |
| — | All gates pass | `ANSWER` | `FIXTURE_EVIDENCE_RESOLVED` (or the stale reason, with a `DISPLAY_STALE_BADGE` obligation) |

Gate 3 models evaluator availability as a declared input; the gates themselves
are bounded in-harness rules, not a repository-wide policy evaluator.

## Failure behavior

Every pinned input is loaded and digest-checked before any case runs, whether or
not a case uses it. An unpinned input, a digest mismatch, a schema-invalid profile/request/case, an
invalid emitted envelope, or a non-identical replay stops the run: exit `2` for
an untrusted input and exit `1` for a mismatch or non-deterministic replay. A case
whose outcome differs from the profile makes the record `FAIL`.

## Run

```bash
python pipelines/domains/hydrology/proof_slice.py
python tools/readiness/run_lane.py proof-slice   # also: make proof-slice
```

The record goes to stdout, or to `--output PATH` outside the repository's
`data/` lifecycle root.

## Changing the slice

### Current Explorer fixture carrier (M08 / #3372)

The repository Site consumes a deterministic, bundled application fixture
projection at `apps/site/source/app/living-waters-proof.json`, generated by
`proof_slice.py --site-carrier`. `--check-site-carrier` checks it without writing;
the hydrology tests also compare every committed byte against a fresh projection.
The projection copies the canonical packet, valid EvidenceBundle, five proved
scenario envelopes, proof identity and dry-run rollback references. It does not
copy negative EvidenceBundles, fetch a provider, or create a released artifact.

The opt-in Living Waters catalog control supplies explicitly schematic display
positions because the packet has no geometry. These positions are neither the
named HUC12 boundary nor the gauge location. Empty, unavailable and ambiguous
outcomes have no drawable features or values. Available and stale answers keep
their exact fixture sample times and provisional qualifier; stale remains
visible. A local correction-hold rehearsal withholds presentation and restores
the same pinned baseline on demand. No source correction history is inferred.
See [Site behavior and rollback](../../../apps/site/source/docs/living-waters-proof.md).

This repository binding replaces the retired `apps/explorer-web` carrier for
bounded implementation evidence only. Browser/WebGL acceptance, independent
review, broader M08 acceptance, real-source admission and Site delivery remain
separate.

Editing any pinned fixture changes its digest, so the profile must be updated in
the same change and reviewed. Adding a case means adding its fixture, its pinned
entry with the expected outcome, and a test in
[`tests/domains/hydrology/test_proof_slice.py`](../../../tests/domains/hydrology/test_proof_slice.py).
